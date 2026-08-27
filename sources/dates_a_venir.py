# -*- coding: utf-8 -*-
"""Les dates passees disparaissent toutes seules — EN UN SEUL EXEMPLAIRE.

╔══════════════════════════════════════════════════════════════════════════╗
║  RUSTINE ASSUMEE — NIVEAU 1. CE N'EST PAS LA SOLUTION DEFINITIVE.        ║
╚══════════════════════════════════════════════════════════════════════════╝

POURQUOI CE FICHIER EXISTE
--------------------------
Le 27/08/2026, `/le-nid` affichait encore l'evenement du 23 aout, passe depuis
quatre jours. David :

    « quand les dates sont depassees, la date reste visible. Je voudrais
      qu'elle disparaisse pour que seules les dates a venir restent, SANS
      AVOIR A TE LE DEMANDER. Que ce soit automatique. »

La cause est structurelle : le site est STATIQUE. Une page fabriquee le 20 aout
ne sait pas qu'on est le 27. Aucun filtrage n'existait, ni a la generation, ni
dans le navigateur (verifie : le seul `new Date()` de `/le-nid` servait a
fabriquer le fichier `.ics`).

CE QUE FAIT CE MODULE, ET CE QU'IL NE FAIT PAS
----------------------------------------------
Il fait UNE chose : a l'ouverture de la page, le NAVIGATEUR compare chaque date
publiee a l'instant present et masque celles qui sont finies. Le HTML livre,
lui, contient TOUJOURS toutes les dates.

    ⚠️ CE N'EST DONC PAS LA VRAIE REPONSE, ET CE MODULE NE L'A JAMAIS ETE. La
       vraie reponse — le niveau 2 — est la reconstruction automatique du site
       depuis l'agenda Google. ELLE EXISTE DEPUIS LE 27/08/2026 :
       `sources/synchro_agenda.py`, lance chaque nuit par
       `.github/workflows/agenda-du-nid.yml`. C'est elle qui fait GAGNER des
       dates a la page ; ce module-ci ne fait qu'en cacher.

       LES DEUX NE FONT PAS DOUBLE EMPLOI, et il ne faut retirer ni l'un ni
       l'autre : la synchronisation passe une fois par nuit, donc entre 21h31 et
       le lendemain matin, une soiree finie serait encore ecrite dans le HTML.
       C'est exactement le trou que ce module bouche, dans le navigateur, a la
       seconde pres. Il reste aussi le seul filet si la tache planifiee est
       arretee ou saute une nuit.

Il ne touche a rien d'autre : aucune date n'est retiree du HTML, aucun texte
n'est reecrit, et sans JavaScript la page est EXACTEMENT celle d'avant (les
dates passees s'affichent alors, c'est la limite assumee de la rustine).

⚠️ CE N'EST PAS UN GENERATEUR. Il n'ecrit aucune page, il ne s'execute pas seul,
   et il n'a donc pas de ligne dans `sources/build.py` (dont le controle
   « generateur non inscrit » ne regarde que les fichiers `generate_*.py`).
   Meme parti-pris que `sources/visionneuse.py` et `sources/retour_haut.py`.

LES QUATRE REGLES QUI ONT DICTE LA CONCEPTION
---------------------------------------------
1. UNE DATE EST PASSEE A LA FIN DE L'EVENEMENT, PAS A SON DEBUT.
   Un concert qui commence a 20 h le 4 septembre reste visible jusqu'a sa fin ce
   soir-la. On enregistre donc toujours l'HEURE DE FIN. Quand elle n'est pas
   connue (les trois soirees mensuelles dont le programme n'est pas arrete, les
   deux concerts de `/concerts-david-lesage`), on prend la FIN DE LA JOURNEE
   (23 h 59, heure de Paris) : on prefere garder une date quelques heures de
   trop que la faire disparaitre pendant qu'elle a lieu.

2. LE FUSEAU EST TRAITE EN PYTHON, PAS DANS LE NAVIGATEUR — et c'est le point
   qui evitait le piege. Les heures publiees sont des heures de PARIS ; le
   visiteur, lui, peut etre n'importe ou. Si le navigateur comparait un jour
   calendaire a « aujourd'hui », un lecteur a Tokyo verrait la date disparaitre
   a 16 h heure de Paris, et un lecteur a New York la verrait rester jusqu'a
   6 h du matin le lendemain.
   On convertit donc ICI, a la generation, chaque fin d'evenement en INSTANT
   ABSOLU (UTC) — `_offset_paris()` connait le vrai changement d'heure (dernier
   dimanche de mars, dernier dimanche d'octobre). Le navigateur ne compare plus
   que deux instants : `Date.parse(fin) <= Date.now()`. Cette comparaison est
   juste depuis n'importe quel fuseau, sans rien avoir a emuler.
   ⚠️ `generate_agenda_nid.py` porte, pour ses `data-s`/`data-e`, un raccourci
      historique (`offset = 2 if (d.month, d.day) < (10, 25) else 1`) qui donne
      le meme resultat pour 2026 mais serait faux une autre annee. Il n'est PAS
      touche ici : il alimente les fichiers `.ics` deja telecharges par des
      gens. Ce module fait son propre calcul, correct pour toute annee.

3. AUCUN CLIGNOTEMENT. Un script pose en fin de page s'execute APRES que le
   navigateur a pu peindre : la date passee apparaitrait puis disparaitrait.
   Le masquage est donc fait par une FEUILLE DE STYLE ecrite en fin de `<head>`
   (`tete()`), avant que la moindre ligne du corps ne soit lue. Le second
   script (`js()`), lui, ne fait que du menage dans le DOM et ne change rien a
   l'image.

4. ON NE LAISSE JAMAIS UN BLOC VIDE AVEC SON TITRE. C'est le cas qu'on oublie.
   Chaque liste de dates est declaree comme un BLOC ; quand toutes ses dates
   sont passees, on affiche a la place un message de repli (`repli=`), on efface
   le bloc entier (`cacher=`) et on efface ce qui n'a plus d'objet (`lie()` :
   une legende, une barre de filtres, un bouton « tout ajouter a mon agenda »).

COMMENT ON S'EN SERT — DANS UN GENERATEUR
------------------------------------------
    import dates_a_venir
    REG = dates_a_venir.Registre()          # UN par page, remis a neuf a chaque
                                            # generation

    REG.declare('cdl-dates', repli='block')             # configurer le bloc
    ...  '<div class="cdl-date"%s>' % REG.date('cdl-dates', jour, '21:00')
    ...  '<p%s>Prochaines dates en preparation.</p>' % REG.repli('cdl-dates')

    html = html.replace('</style>', dates_a_venir.css() + '</style>', 1)
    html = html.replace('</head>',  REG.tete() + '</head>', 1)
    html = html.replace('</body>',  REG.js()   + '</body>', 1)

⚠️ `tete()` DOIT ETRE APPELE EN DERNIER — apres que toutes les dates ont ete
   enregistrees. C'est lui qui embarque la table.

⚠️ SUR `/le-nid`, `js()` DOIT ETRE POSE AVANT `FILTER_JS`. Le filtre par type et
   par mois construit sa liste d'elements au moment ou il s'execute : s'il la
   construit AVANT le menage, il compte des dates passees, son message « Aucune
   date ne correspond a ces filtres » se declenche a tort, et le bouton
   « Ajouter toutes les dates a mon agenda » telecharge un `.ics` qui contient
   des evenements finis. Poser `js()` en premier resout les trois d'un coup,
   sans toucher une ligne de `FILTER_JS`.

CE QUE CHAQUE PAGE DOIT PORTER
------------------------------
Rien de particulier : deux classes (`.dt-vide`, `.dt-plus`) posees par `css()`,
et la variable CSS `--muted`, deja definie par la feuille de base des 31 pages.

POURQUOI TOUTES LES REGLES GENEREES SONT EN `!important`
--------------------------------------------------------
Elles doivent gagner contre des regles de la page qui sont parfois PLUS
SPECIFIQUES qu'un simple attribut : `.agenda.ag-js .ag-filters{display:flex}`
vaut (0,2,0) quand `html [data-dt-lie]` ne vaut que (0,1,1). Plutot que
d'inventer un empilement de selecteurs different par page — donc fragile —, on
assume un `!important` sur un jeu de regles qui n'existe que pour cacher.

LE SEPARATEUR ORPHELIN
----------------------
Les encarts « Prochaines dates » de `/le-nid` s'ecrivent « 4 sept. · 19 sept. ».
Si la premiere date disparait, un « · » resterait en tete. Chaque date porte
donc SON PROPRE separateur, en tete et a l'interieur d'elle-meme
(`separateur()`), et la feuille generee efface celui de la premiere date encore
a venir. Rien a recalculer dans le navigateur.

LA FENETRE (`fenetre=`)
-----------------------
Les encarts de `/le-nid` montrent « les 3 prochaines ». Si le HTML n'en portait
que trois, elles seraient toutes passees en novembre alors que l'agenda, lui,
en connait d'autres. Le HTML porte donc TOUTES les dates du type ; les
suivantes sont masquees par la classe `.dt-plus`, et la feuille generee revele
les trois premieres ENCORE A VENIR. Sans JavaScript, ce sont les trois
premieres ecrites — exactement la page d'avant.
"""
import datetime as dt
import json


# --------------------------------------------------------------------------- #
# HEURE DE PARIS -> INSTANT ABSOLU
# --------------------------------------------------------------------------- #
def _dernier_dimanche(annee, mois):
    """Le dernier dimanche du mois (mars et octobre ont 31 jours)."""
    d = dt.date(annee, mois, 31)
    return d - dt.timedelta(days=(d.weekday() - 6) % 7)


def _offset_paris(jour):
    """+2 h en heure d'ete, +1 h en heure d'hiver.

    La bascule a lieu a 01:00 UTC le dernier dimanche de mars et le dernier
    dimanche d'octobre. On raisonne a la journee : aucun evenement du site ne
    commence entre 01:00 et 03:00 du matin, donc l'ambiguite d'une heure ne
    peut pas se produire.
    """
    return 2 if (_dernier_dimanche(jour.year, 3) <= jour
                 < _dernier_dimanche(jour.year, 10)) else 1


def fin_utc(jour, heure=None):
    """(date de Paris, 'HH:MM' de fin) -> instant ISO 8601 en UTC.

    `heure` absente = fin de la journee (23:59). Voir la regle 1 en tete.
    """
    if heure:
        h, m = (int(x) for x in heure.strip().split(':')[:2])
    else:
        h, m = 23, 59
    quand = (dt.datetime(jour.year, jour.month, jour.day, h, m)
             - dt.timedelta(hours=_offset_paris(jour)))
    return quand.strftime('%Y-%m-%dT%H:%M:%SZ')


# --------------------------------------------------------------------------- #
# LA FEUILLE DE STYLE LIVREE (deux regles, une ligne chacune)
#
# ⚠️ AUCUN COMMENTAIRE ICI : un garde-fou du projet refuse tout commentaire de
#    plus d'une ligne dans le CSS livre, et le depot est public. Les notes sont
#    en commentaires `#`, comme partout ailleurs.
#      `.dt-vide` : le message de repli. Invisible par defaut — sans JavaScript
#                   les dates sont la, le repli n'a rien a dire.
#      `.dt-plus` : une date au-dela de la fenetre d'affichage (voir `fenetre=`).
# --------------------------------------------------------------------------- #
def css():
    return ('.dt-vide{display:none;color:var(--muted);font-style:italic}\n'
            '.dt-plus{display:none}\n')


def separateur(texte=' · '):
    """Le separateur d'une date, ecrit A L'INTERIEUR d'elle pour disparaitre avec elle."""
    return '<i class="dt-sep">%s</i>' % texte


# --------------------------------------------------------------------------- #
# LE SCRIPT DE TETE — il ecrit la feuille de masquage AVANT la premiere peinture
# --------------------------------------------------------------------------- #
_JS_TETE = """(function(){
var F=__F__,B=__B__,n=Date.now(),r=[],i,k,j;
function passe(x){return Date.parse(F[x])<=n;}
for(i=0;i<F.length;i++){if(passe(i))r.push('html [data-dt="'+i+'"]{display:none!important}');}
for(k=0;k<B.length;k++){
var b=B[k],v=[];
for(j=0;j<b[1].length;j++){if(!passe(b[1][j]))v.push(b[1][j]);}
if(!v.length){
if(b[2])r.push('html [data-dt-bloc="'+b[0]+'"]{display:none!important}');
if(b[3])r.push('html [data-dt-vide="'+b[0]+'"]{display:'+b[3]+'!important}');
r.push('html [data-dt-lie="'+b[0]+'"]{display:none!important}');
}else{
if(b[5]){for(j=0;j<v.length;j++)r.push('html [data-dt="'+v[j]+'"]{display:'+(j<b[5]?'inline':'none')+'!important}');}
if(b[4])r.push('html [data-dt="'+v[0]+'"] .dt-sep{display:none!important}');
}
}
if(r.length&&document.head){var s=document.createElement('style');
s.appendChild(document.createTextNode(r.join('')));document.head.appendChild(s);}
})();"""


# --------------------------------------------------------------------------- #
# LE SCRIPT DE MENAGE — il retire du DOM ce que la feuille de tete a deja cache
#
# Il ne change rien a l'image (tout est deja invisible). Il sert a ce que le
# RESTE du JavaScript de la page ne voie plus les dates passees : les filtres de
# l'agenda, leur compteur, et l'export « toutes les dates » en .ics.
# --------------------------------------------------------------------------- #
_JS_MENAGE = """(function(){
var n=Date.now(),L=document.querySelectorAll('[data-dt-fin]'),i,e;
for(i=L.length-1;i>=0;i--){e=L[i];
if(Date.parse(e.getAttribute('data-dt-fin'))<=n&&e.parentNode)e.parentNode.removeChild(e);}
})();"""


class Registre:
    """Les dates d'UNE page. Un exemplaire par generation, jamais partage."""

    def __init__(self):
        self._fins = []      # index -> instant ISO de fin
        self._blocs = {}     # cle -> configuration + indices

    # -- declaration -------------------------------------------------------- #
    def _bloc(self, cle):
        return self._blocs.setdefault(
            cle, {'i': [], 'cacher': False, 'repli': '', 'sep': False,
                  'fenetre': 0})

    def declare(self, cle, cacher=False, repli='', sep=False, fenetre=0):
        """Configure un bloc de dates.

        cacher  : effacer le bloc entier quand toutes ses dates sont passees
                  (un groupe de mois de l'agenda : son titre part avec lui).
        repli   : valeur CSS `display` du message de repli ('block', 'inline'…).
                  Vide = pas de message.
        sep     : les dates portent un separateur en tete (voir `separateur()`).
        fenetre : n'afficher que les N premieres dates encore a venir.
        """
        b = self._bloc(cle)
        b.update(cacher=cacher, repli=repli, sep=sep, fenetre=fenetre)
        return ' data-dt-bloc="%s"' % cle

    # -- pose des attributs -------------------------------------------------- #
    def date(self, blocs, jour, heure_fin=None):
        """Attributs a poser sur l'element qui PORTE une date.

        `blocs` : une cle, ou plusieurs (une date d'agenda appartient a la fois
        a son groupe de mois et a l'agenda entier).
        Renvoie la chaine d'attributs — la MEME peut etre reposee sur un second
        element (le filet `.divider` qui suit une section, par exemple) pour
        qu'il disparaisse avec elle.
        """
        i = len(self._fins)
        self._fins.append(fin_utc(jour, heure_fin))
        for cle in ((blocs,) if isinstance(blocs, str) else blocs):
            self._bloc(cle)['i'].append(i)
        return ' data-dt="%d" data-dt-fin="%s"' % (i, self._fins[i])

    def bloc_attr(self, cle):
        """Attribut a poser sur le CONTENEUR d'un bloc (utile si `cacher=True`)."""
        return ' data-dt-bloc="%s"' % cle

    def repli(self, cle, classe=''):
        """Attributs du message de repli d'un bloc (invisible par defaut)."""
        return ' class="dt-vide%s" data-dt-vide="%s"' % (
            (' ' + classe) if classe else '', cle)

    def lie(self, cle):
        """Attribut d'un element qui n'a plus d'objet si le bloc est vide."""
        return ' data-dt-lie="%s"' % cle

    # -- sortie -------------------------------------------------------------- #
    def tete(self):
        """Le `<script>` a poser en FIN de `<head>`. A appeler en dernier."""
        if not self._fins:
            return ''
        table = [[cle, b['i'], 1 if b['cacher'] else 0, b['repli'],
                  1 if b['sep'] else 0, b['fenetre']]
                 for cle, b in self._blocs.items()]
        corps = (_JS_TETE
                 .replace('__F__', json.dumps(self._fins, separators=(',', ':')))
                 .replace('__B__', json.dumps(table, separators=(',', ':'))))
        return '<script>\n' + corps + '\n</script>\n'

    def js(self):
        """Le `<script>` de menage, a poser avant `</body>`."""
        return '' if not self._fins else '<script>\n' + _JS_MENAGE + '\n</script>\n'
