# -*- coding: utf-8 -*-
"""Filet de securite du site : une commande qui relit les 30 pages publiees.

    python3 sources/verif_site.py        # tout verifier
    echo $?                              # 0 = rien a signaler, 1 = probleme

POURQUOI CE FICHIER EXISTE
--------------------------
Pousser sur `main` PUBLIE le site (Vercel deploie tout seul en ~40 s). Il n'y a
donc pas de filet apres coup : ce qui part est en ligne. Chaque controle
ci-dessous correspond a un incident REELLEMENT survenu sur ce projet, decouvert
a la main et trop tard. Ils sont ici pour qu'aucun ne puisse recommencer.

  1. commentaires     44 notes de redaction parties dans les pages publiques
  2. menu             4 entrees « Agenda » et 4 cartes identiques apres une
                      regeneration (le menu n'etait pas idempotent)
  3. titre            plusieurs <h1> sur une meme page
  4. images           images affichees plus grandes que leur fichier reel
  5. liens            ancres mortes, target="_blank" sans rel="noopener"
  6. doublons         blocs structurels dupliques par une seconde passe
  7. donnees          UN CODE DE PORTAIL A DEJA FUITE DEUX FOIS. Le depot est
                      PUBLIC. C'est le controle le plus important du lot.
  8. chiffres         « 112 dates » affiche alors que la liste en contenait un
                      autre nombre
  9. plan du site     sitemap / robots.txt / vercel.json en desaccord avec les
                      pages qui existent vraiment
 10. google           la balise de verification Search Console recopiee sur
                      toutes les pages au lieu de la seule page d'accueil
 11. partage          sept pages partageaient la meme vignette d'apercu, et
                      rien ne verifiait que le fichier annonce existait ni que
                      ses dimensions etaient les bonnes

CE QU'IL NE FAIT PAS
--------------------
Il ne modifie aucun fichier. Il lit, il compte, il compare. On peut le lancer
autant de fois qu'on veut sans rien risquer.

AJOUTER UN CONTROLE
-------------------
Ecrire une fonction `controle_xxx(pages)` qui renvoie une liste de messages
(vide = tout va bien), puis l'inscrire dans `CONTROLES` en bas du fichier.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(HERE)
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import verif_commentaires  # noqa: E402  (garde-fou deja ecrit, on le reutilise)
# Le numero de version du menu est LU dans nav_menu.py, jamais recopie ici : il
# a deja diverge une fois. Importer ce module est sans effet de bord (il ne
# travaille que sous `if __name__ == '__main__'`), contrairement aux
# `generate_*.py` qu'il ne faut JAMAIS importer.
import nav_menu  # noqa: E402

# --------------------------------------------------------------------------- #
# LES 30 PAGES PUBLIEES  —  url visible <-> fichier sur disque
# --------------------------------------------------------------------------- #
PAGES = (
    ('/',                        'index.html'),
    ('/rituals',                 'rituals/index.html'),
    ('/rituals-trio',            'rituals-trio/index.html'),
    ('/e-motion',                'e-motion/index.html'),
    ('/david-lesage-en-concert', 'david-lesage-en-concert/index.html'),
    ('/concerts-david-lesage',   'concerts-david-lesage/index.html'),
    ('/le-nid',                  'le-nid/index.html'),
    ('/le-soin-soa',             'le-soin-soa/index.html'),
    ('/rythme-calebasse',        'rythme-calebasse/index.html'),
    ('/association',             'association/index.html'),
    ('/guso-facile',             'guso-facile/index.html'),
    ('/guso-facile/blog',        'guso-facile/blog/index.html'),
    ('/guso-facile/blog/atteindre-507-heures-sans-angoisse', 'guso-facile/blog/atteindre-507-heures-sans-angoisse/index.html'),
    ('/guso-facile/blog/c-est-quoi-le-guso-concretement', 'guso-facile/blog/c-est-quoi-le-guso-concretement/index.html'),
    ('/guso-facile/blog/ca-va-te-faire-connaitre-comment-repondre', 'guso-facile/blog/ca-va-te-faire-connaitre-comment-repondre/index.html'),
    ('/guso-facile/blog/combien-de-cachets-pour-507-heures', 'guso-facile/blog/combien-de-cachets-pour-507-heures/index.html'),
    ('/guso-facile/blog/comment-declarer-une-repetition', 'guso-facile/blog/comment-declarer-une-repetition/index.html'),
    ('/guso-facile/blog/employeur-ne-m-a-pas-paye-mon-cachet', 'guso-facile/blog/employeur-ne-m-a-pas-paye-mon-cachet/index.html'),
    ('/guso-facile/blog/evaluer-si-une-date-est-un-bon-plan', 'guso-facile/blog/evaluer-si-une-date-est-un-bon-plan/index.html'),
    ('/guso-facile/blog/faut-il-un-contrat-pour-un-concert', 'guso-facile/blog/faut-il-un-contrat-pour-un-concert/index.html'),
    ('/guso-facile/blog/heures-ne-correspondent-pas-france-travail', 'guso-facile/blog/heures-ne-correspondent-pas-france-travail/index.html'),
    ('/guso-facile/blog/m-organiser-quand-je-joue-dans-plusieurs-groupes', 'guso-facile/blog/m-organiser-quand-je-joue-dans-plusieurs-groupes/index.html'),
    ('/guso-facile/blog/ne-plus-jamais-oublier-une-dpae', 'guso-facile/blog/ne-plus-jamais-oublier-une-dpae/index.html'),
    ('/guso-facile/blog/organiser-une-tournee-qui-tient-la-route', 'guso-facile/blog/organiser-une-tournee-qui-tient-la-route/index.html'),
    ('/guso-facile/blog/pointage-france-travail-sans-stress', 'guso-facile/blog/pointage-france-travail-sans-stress/index.html'),
    ('/guso-facile/blog/quand-tombe-ma-date-anniversaire', 'guso-facile/blog/quand-tombe-ma-date-anniversaire/index.html'),
    ('/guso-facile/blog/structure-accompagner-ses-artistes', 'guso-facile/blog/structure-accompagner-ses-artistes/index.html'),
    ('/guso-facile/blog/structure-comment-gerer-les-guso-de-mes-artistes', 'guso-facile/blog/structure-comment-gerer-les-guso-de-mes-artistes/index.html'),
    ('/guso-facile/blog/studio-et-cheque-intermittents',  'guso-facile/blog/studio-et-cheque-intermittents/index.html'),
    ('/guso-facile/blog/travailler-a-deux-artistes-dates-partagees', 'guso-facile/blog/travailler-a-deux-artistes-dates-partagees/index.html'),
)

#: dossiers encore presents dans le depot mais volontairement HORS du site :
#: absents du sitemap, interdits dans robots.txt. Leur suppression n'a jamais
#: ete tranchee par David — on ne les efface pas, on verifie juste qu'ils
#: restent bien invisibles.
ORPHELINES = ('/solune', '/au-nid')

# --------------------------------------------------------------------------- #
# LISTES BLANCHES  —  ce qui est deja publie et assume
# --------------------------------------------------------------------------- #
# Chaque entree porte la raison de sa presence. Tout ce qui n'est pas ici fait
# echouer le controle : c'est le principe, une nouveaute doit etre decidee.

#: numeros de telephone publies volontairement, sous forme normalisee (chiffres
#: seuls, indicatif national). Rappel : le numero de mobile du contact technique
#: de /david-lesage-en-concert est une question ENCORE OUVERTE cote David
#: (garder le mobile ou n'afficher que l'email ?).
TELEPHONES_AUTORISES = {
    '0170043012': "ligne fixe de l'association (accueil)",
    '0610733152': 'mobile David Lesage — contact technique et booking',
    '0689054758': 'mobile booking (RITUALS, RITUALS trio, E-Motion)',
}

#: adresses email publiees volontairement.
EMAILS_AUTORISES = {
    'contact@resonancesproductions.org': "adresse publique de l'association",
    'contact@lesagedavid.fr': 'adresse publique de David Lesage',
    'booking@solune.show': 'booking E-Motion (marque SOLUNE)',
    'prenom@domaine.fr': "exemple affiche dans le formulaire de /rythme-calebasse",
}

#: mots qui, suivis de chiffres, trahiraient un code d'acces. Le code du portail
#: du Nid a fuite DEUX FOIS sur ce projet (une fois dans une page, une fois dans
#: ce handoff public). La formule autorisee est : « le code du portail vous est
#: communique avec votre confirmation d'inscription » — sans jamais le chiffre.
MOTS_CODE = ('code', 'digicode', 'portail', 'interphone', 'badge',
             'acces', 'accès', 'entree', 'entrée')

#: contextes ou un mot de la liste ci-dessus cotoie legitimement des chiffres.
#: On n'elargit JAMAIS un mot de MOTS_CODE : on inscrit ici la formule exacte,
#: avec sa raison. Chaque entree est un faux positif MESURE, pas une supposition.
CODES_HORS_SOUPCON = (
    'code ape',        # « Code APE : 9001Z » — pied de page des 30 pages
    'siret',           # « SIRET : 919 514 075 00010 » — idem
    'code postal',
    # /guso-facile : « un badge « droits sécurisés » dès 507 heures ». Le mot
    # « badge » suivi d'un nombre est bien la signature d'un code d'entree,
    # mais 507 est ici le seuil d'heures de l'intermittence, present une
    # dizaine de fois sur la page. Faux positif mesure le 14/08/2026.
    'droits sécurisés',
)

#: images dont la definition reste sous le double de leur largeur d'affichage.
#: Une image nette sur ecran Retina demande 2x sa largeur CSS. Ces trois-la sont
#: connues, mesurees et acceptees en l'etat ; toute NOUVELLE image sous le seuil
#: fera echouer le controle.
EXCEPTIONS_HD = {
    ('le-soin-soa/index.html', '/img/soin-soa/portrait-gaia-pegourie-260.jpg'):
        'portrait 260 px affiche a 150 px (1,73x au lieu de 2x) — accepte',
    ('le-soin-soa/index.html', '/img/soin-soa/portrait-iris-chasles-260.jpg'):
        'portrait 260 px affiche a 150 px (1,73x au lieu de 2x) — accepte',
    ('le-soin-soa/index.html', '/img/soin-soa/portrait-david-lesage-260.jpg'):
        'portrait 260 px affiche a 150 px (1,73x au lieu de 2x) — accepte',
}

#: marqueurs de structure qui doivent apparaitre UNE SEULE FOIS par page. C'est
#: la trace de l'incident des 4 cartes identiques : une seconde passe d'un
#: script qui n'etait pas idempotent avait recopie le bloc.
MARQUEURS_UNIQUES = {
    '*': (
        ('data-nav="%s"' % nav_menu.NAV_VERSION, 'menu partage (nav_menu.py)'),
        (nav_menu.JS_MARK, 'ouverture du JS du menu'),
        (nav_menu.JS_END, 'fermeture du JS du menu'),
        ('<footer', 'pied de page'),
        ('<body', 'corps du document'),
        ('</html>', 'fin du document'),
    ),
    'le-nid/index.html': (
        ('id="agenda"', "section agenda"),
        ('id="instruments"', "section presentation d'instruments"),
        ('id="yoga"', 'section atelier de yoga'),
        ('id="psychotherapie"', 'section psychotherapie'),
        ('id="cours-individuels"', 'section cours individuels'),
    ),
    'rythme-calebasse/index.html': (
        ('id="experience"', 'bloc experience (26 ateliers)'),
        ('id="appel"', 'appel a candidature'),
    ),
    # ⚠️ `id="statuts"` A QUITTE L'ACCUEIL le 15/08/2026 : la section « Cadre
    #    legal · Les statuts » est passee sur /association. L'accueil garde une
    #    presentation COURTE de l'association (`#association`) et un bouton
    #    « En savoir plus ». Les trois autres ancres de l'accueil ne bougent
    #    pas : `#adherer`, `#prestations` et `#contact` y sont toujours.
    'index.html': (
        ('id="association"', "section association"),
        ('id="adherer"', 'section adhesion'),
        ('id="prestations"', 'section prestations'),
        ('id="contact"', 'section contact'),
        # (pas de marqueur `href="/association"` ici : il apparait DEUX fois sur
        #  l'accueil — l'entree de menu et le bouton « En savoir plus ». Le
        #  bouton est garde par `generate_assoc.py`, avec sa balise entiere.)
    ),
    'association/index.html': (
        ('id="objet"', "section objet de l'association"),
        ('id="valeurs"', 'section valeurs / engagements'),
        ('id="statuts"', 'section statuts'),
        ('id="mentions"', 'section mentions legales'),
        ('id="adherer"', 'section adhesion & contact'),
    ),
}

#: nombre d'entrees attendu dans le menu partage (hors boutons de sous-menu) :
#: Accueil + 4 « Sur scene » + 9 « Le Nid » + 2 « L’association » (la PAGE
#: /association depuis le 15/08/2026, + Guso Facile) + Contact + Adherer.
MENU_ENTREES_ATTENDUES = 18


# --------------------------------------------------------------------------- #
# Outillage commun
# --------------------------------------------------------------------------- #

class Page(object):
    """Une page publiee, lue une seule fois et partagee entre les controles."""

    def __init__(self, url, rel):
        self.url = url
        self.rel = rel
        self.chemin = os.path.join(RACINE, rel)
        self.existe = os.path.exists(self.chemin)
        self.html = ''
        if self.existe:
            with open(self.chemin, encoding='utf-8') as f:
                self.html = f.read()
        self._ids = None
        self._sans_js = None

    @property
    def ids(self):
        if self._ids is None:
            self._ids = set(re.findall(r'\bid="([^"]+)"', self.html))
        return self._ids

    @property
    def sans_js(self):
        """La page sans le contenu des <script>.

        Le JavaScript parle du document : il contient des « <body> », des
        « id="..." » et des noms de balises en clair, dans du code ou des
        commentaires. Les compter comme des blocs de page produisait de fausses
        alertes. Pour tout ce qui est comptage de structure, on regarde la page
        sans son JavaScript.
        """
        if self._sans_js is None:
            self._sans_js = re.sub(r'<script\b.*?</script>', '<script></script>',
                                   self.html, flags=re.S | re.I)
        return self._sans_js

    def bloc_menu(self):
        """Le `<div class="links" data-nav=...>` complet, ou '' s'il manque.

        On compte les `<div>` ouverts/fermes plutot que d'ecrire une expression
        reguliere : le menu contient des div imbriques (les sous-menus).
        """
        depart = self.html.find('<div class="links" data-nav=')
        if depart < 0:
            return ''
        profondeur = 0
        for m in re.finditer(r'<div\b|</div>', self.html[depart:]):
            profondeur += 1 if m.group(0) != '</div>' else -1
            if profondeur == 0:
                return self.html[depart:depart + m.end()]
        return ''


def _charger():
    return [Page(url, rel) for url, rel in PAGES]


def _taille_jpeg(chemin):
    """(largeur, hauteur) d'un JPEG, en lisant son en-tete. Sans dependance.

    Repli pour les machines ou Pillow n'est pas installe : sans lui,
    `_lire_image` renvoyait None et DEUX controles se taisaient au lieu
    d'echouer. Un controle muet ne protege personne.
    """
    import struct
    try:
        with open(chemin, 'rb') as f:
            donnees = f.read()
    except OSError:
        return None
    if not donnees.startswith(b'\xff\xd8'):
        return None
    i = 2
    while i + 9 < len(donnees):
        if donnees[i] != 0xFF:
            i += 1
            continue
        marqueur = donnees[i + 1]
        if marqueur in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                        0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            haut, larg = struct.unpack('>HH', donnees[i + 5:i + 9])
            return larg, haut
        if marqueur in (0xD8, 0xD9) or 0xD0 <= marqueur <= 0xD7:
            i += 2
            continue
        i += 2 + struct.unpack('>H', donnees[i + 2:i + 4])[0]
    return None


def _lire_image(rel_url):
    """(largeur, hauteur) d'un fichier image du depot, ou None."""
    chemin = os.path.join(RACINE, rel_url.lstrip('/'))
    if not os.path.exists(chemin):
        return None
    try:
        from PIL import Image
        Image.MAX_IMAGE_PIXELS = None
        with Image.open(chemin) as im:
            return im.size
    except Exception:
        pass
    if chemin.lower().endswith(('.jpg', '.jpeg')):
        return _taille_jpeg(chemin)
    return None


def _balises_img(html):
    return re.findall(r'<img\b[^>]*>', html)


def _attr(balise, nom):
    m = re.search(r'\b%s="([^"]*)"' % nom, balise)
    return m.group(1) if m else None


def _candidats_srcset(valeur):
    """[(url, largeur declaree), ...] a partir d'un attribut srcset."""
    out = []
    for morceau in valeur.split(','):
        bouts = morceau.split()
        if len(bouts) == 2 and bouts[1].endswith('w'):
            try:
                out.append((bouts[0], int(bouts[1][:-1])))
            except ValueError:
                pass
    return out


# --------------------------------------------------------------------------- #
# 1. COMMENTAIRES HTML DE TRAVAIL
# --------------------------------------------------------------------------- #

def controle_commentaires(pages):
    """Delegue a `verif_commentaires.py` : notes de redaction dans le HTML livre."""
    pbs = []
    for p in pages:
        for pos, pourquoi, texte in verif_commentaires.anomalies(p.html):
            pbs.append('%s : %s (car. %d) — %s'
                       % (p.rel, pourquoi, pos, verif_commentaires._apercu(texte, 90)))
    return pbs


# --------------------------------------------------------------------------- #
# 2. MENU DE NAVIGATION
# --------------------------------------------------------------------------- #

def controle_menu(pages):
    """Le menu partage : present une fois, complet, sans entree en double."""
    pbs = []
    version = nav_menu.NAV_VERSION
    for p in pages:
        n = p.html.count('data-nav="%s"' % version)
        if n != 1:
            pbs.append('%s : %d marqueur(s) data-nav="%s", attendu 1'
                       % (p.rel, n, version))
            continue
        # reste d'une version anterieure du menu (le passage resonances-1 ->
        # resonances-2 en avait laisse sur une page)
        for ancienne in set(re.findall(r'data-nav="([^"]+)"', p.html)):
            if ancienne != version:
                pbs.append('%s : reste du menu de la version %s' % (p.rel, ancienne))
        bloc = p.bloc_menu()
        if not bloc:
            pbs.append('%s : bloc de menu introuvable ou mal ferme' % p.rel)
            continue
        entrees = re.findall(r'<a\b[^>]*href="([^"]*)"[^>]*>(.*?)</a>', bloc, re.S)
        vues = {}
        for href, libelle in entrees:
            libelle = ' '.join(re.sub(r'<[^>]+>', '', libelle).split())
            cle = (href, libelle)
            vues[cle] = vues.get(cle, 0) + 1
        for (href, libelle), combien in sorted(vues.items()):
            if combien > 1:
                pbs.append('%s : entree de menu en %d exemplaires — « %s » (%s)'
                           % (p.rel, combien, libelle, href))
        if len(entrees) != MENU_ENTREES_ATTENDUES:
            pbs.append('%s : %d entrees dans le menu, attendu %d'
                       % (p.rel, len(entrees), MENU_ENTREES_ATTENDUES))
    return pbs


# --------------------------------------------------------------------------- #
# 3. UN SEUL TITRE PRINCIPAL
# --------------------------------------------------------------------------- #

def controle_titre(pages):
    """Un <h1> et un seul : c'est le titre de la page pour Google et pour un
    lecteur d'ecran. Deux <h1>, c'est deux pages melangees."""
    pbs = []
    for p in pages:
        n = len(re.findall(r'<h1\b', p.html))
        if n != 1:
            pbs.append('%s : %d <h1>, attendu exactement 1' % (p.rel, n))
    return pbs


# --------------------------------------------------------------------------- #
# 4. IMAGES
# --------------------------------------------------------------------------- #

def controle_images(pages):
    """Fichiers presents, dimensions declarees, et jamais d'image etiree."""
    pbs = []
    for p in pages:
        for balise in _balises_img(p.html):
            src = _attr(balise, 'src')
            if not src:
                # <img> vide rempli par le JavaScript (visionneuse plein ecran) :
                # il n'a ni fichier ni dimensions, c'est normal.
                continue
            if src.startswith('/'):
                if not os.path.exists(os.path.join(RACINE, src.lstrip('/'))):
                    pbs.append('%s : image introuvable %s' % (p.rel, src))
                    continue
                # Image SANS `sizes` : le navigateur prend `width` pour la
                # largeur d'affichage. Elle doit donc exister dans un fichier.
                #
                # Avec un `sizes`, c'est le couple srcset+sizes qui decide, et
                # `width`/`height` ne servent plus qu'a reserver la place (ils
                # portent alors les dimensions de la PHOTO D'ORIGINE, ce qui est
                # la convention de /le-nid : 4032 px pour une photo d'iPhone).
                # Ce cas-la est couvert par le controle des largeurs srcset
                # juste en dessous, qui est le vrai garde-fou : si le navigateur
                # croit avoir 1400 px et que le fichier n'en fait que 900,
                # l'image est bel et bien affichee au-dela de sa definition.
                if not _attr(balise, 'sizes'):
                    dispo = [_lire_image(src)]
                    for url, _w in _candidats_srcset(_attr(balise, 'srcset') or ''):
                        if url.startswith('/'):
                            dispo.append(_lire_image(url))
                    plus_grande = max([t[0] for t in dispo if t] or [0])
                    largeur_demandee = _attr(balise, 'width')
                    if plus_grande and largeur_demandee and largeur_demandee.isdigit():
                        if int(largeur_demandee) > plus_grande:
                            pbs.append('%s : %s affichee en %s px de large alors que '
                                       'le plus grand fichier disponible n\'en fait '
                                       'que %d — elle sera floue'
                                       % (p.rel, src, largeur_demandee, plus_grande))
            if not (_attr(balise, 'width') and _attr(balise, 'height')):
                pbs.append('%s : width/height absents sur %s — la page sautera '
                           'au chargement' % (p.rel, src))

        # largeurs annoncees dans srcset : elles doivent correspondre au fichier
        for m in re.finditer(r'\bsrcset="([^"]+)"', p.html):
            for url, declaree in _candidats_srcset(m.group(1)):
                if not url.startswith('/'):
                    continue
                if not os.path.exists(os.path.join(RACINE, url.lstrip('/'))):
                    pbs.append('%s : image introuvable dans srcset %s' % (p.rel, url))
                    continue
                reelle = _lire_image(url)
                if reelle and reelle[0] < declaree:
                    pbs.append('%s : %s annoncee %dw mais ne fait que %d px'
                               % (p.rel, url, declaree, reelle[0]))

        # ecrans haute densite : la plus grande variante doit valoir 2x la
        # largeur d'affichage, sinon l'image est visiblement molle sur un Mac
        # ou un telephone recent.
        for balise in _balises_img(p.html):
            tailles = _attr(balise, 'sizes')
            srcset = _attr(balise, 'srcset')
            src = _attr(balise, 'src') or '(sans src)'
            if not (tailles and srcset):
                continue
            fixe = re.fullmatch(r'\s*(\d+)px\s*', tailles)
            if not fixe:
                continue
            css = int(fixe.group(1))
            dispo = max([w for _u, w in _candidats_srcset(srcset)] or [0])
            if dispo and dispo < 2 * css:
                if (p.rel, src) in EXCEPTIONS_HD:
                    continue
                pbs.append('%s : %s affichee a %d px CSS ; il faudrait %d px de '
                           'definition pour un ecran haute densite, la plus grande '
                           'variante n\'en fait que %d'
                           % (p.rel, src, css, 2 * css, dispo))
    return pbs


# --------------------------------------------------------------------------- #
# 5. LIENS
# --------------------------------------------------------------------------- #

def controle_liens(pages):
    """Ancres qui ne menent nulle part, et onglets ouverts sans protection."""
    pbs = []
    par_fichier = {p.rel: p for p in pages}
    par_url = {}
    for p in pages:
        par_url[p.url] = p.rel

    for p in pages:
        # ancre dans la page elle-meme
        for ancre in sorted(set(re.findall(r'href="#([^"]+)"', p.html))):
            if ancre and ancre not in p.ids:
                pbs.append('%s : lien vers #%s, mais aucun bloc ne porte cet '
                           'identifiant' % (p.rel, ancre))
        # ancre dans une autre page du site
        for url, ancre in sorted(set(re.findall(r'href="(/[^"#]*)#([^"]+)"', p.html))):
            cible = par_url.get(url.rstrip('/') or '/')
            if cible is None:
                pbs.append('%s : lien vers %s#%s — cette page n\'existe pas'
                           % (p.rel, url, ancre))
            elif ancre not in par_fichier[cible].ids:
                pbs.append('%s : lien vers %s#%s — l\'ancre est absente de %s'
                           % (p.rel, url, ancre, cible))
        # page interne inexistante
        for url in sorted(set(re.findall(r'href="(/[^"#]*)"', p.html))):
            propre = url.rstrip('/') or '/'
            if propre in par_url:
                continue
            if os.path.exists(os.path.join(RACINE, url.lstrip('/'))):
                continue
            pbs.append('%s : lien interne mort vers %s' % (p.rel, url))
        # nouvel onglet sans rel="noopener"
        for a in re.findall(r'<a\b[^>]*>', p.html):
            if 'target="_blank"' in a and 'noopener' not in a:
                pbs.append('%s : target="_blank" sans rel="noopener" — %s'
                           % (p.rel, ' '.join(a.split())[:110]))
    return pbs


# --------------------------------------------------------------------------- #
# 6. BLOCS DUPLIQUES
# --------------------------------------------------------------------------- #

def controle_doublons(pages):
    """Chaque bloc de structure une seule fois, et aucun identifiant repete."""
    pbs = []
    for p in pages:
        attendus = list(MARQUEURS_UNIQUES['*']) + list(MARQUEURS_UNIQUES.get(p.rel, ()))
        for marqueur, quoi in attendus:
            n = p.sans_js.count(marqueur)
            if n != 1:
                pbs.append('%s : %d fois « %s » (%s), attendu 1'
                           % (p.rel, n, marqueur, quoi))
        vus = {}
        for ident in re.findall(r'\bid="([^"]+)"', p.sans_js):
            vus[ident] = vus.get(ident, 0) + 1
        for ident, combien in sorted(vus.items()):
            if combien > 1:
                pbs.append('%s : identifiant id="%s" present %d fois — c\'est la '
                           'signature d\'un bloc recopie' % (p.rel, ident, combien))
    return pbs


# --------------------------------------------------------------------------- #
# 7. FUITE DE DONNEES  —  LE CONTROLE LE PLUS IMPORTANT
# --------------------------------------------------------------------------- #

def controle_donnees(pages):
    """Aucun code d'acces, aucun numero ni email qui n'ait ete decide.

    Le depot est PUBLIC et le site aussi. Le code du portail du Nid a deja fuite
    deux fois. Tout ce qui ressemble a un code d'entree fait echouer la passe.
    """
    pbs = []
    re_tel = re.compile(r'(?:\+33[\s.\-]?|0)[1-9](?:[\s.\-]?\d{2}){4}')
    re_mail = re.compile(r'[\w.+-]+@[\w.-]+\.[a-z]{2,}', re.I)
    mots = '|'.join(re.escape(m) for m in MOTS_CODE)
    # ⚠️ La forme du code compte autant que le mot qui le precede. Le code qui a
    # REELLEMENT fuite deux fois sur ce projet s'ecrit « AB0569 » : DEUX lettres
    # puis quatre chiffres. L'ancienne forme n'acceptait qu'UNE lettre avant les
    # chiffres (`[A-Za-z][0-9]{3,6}`) et laissait donc passer le seul code qu'on
    # ait jamais eu a chasser ici — verifie le 15/08/2026. On accepte desormais
    # jusqu'a trois lettres avant et deux apres.
    re_code = re.compile(r'(?i)\b(%s)\b([^<>]{0,45}?)'
                         r'\b([A-Za-z]{0,3}[0-9]{3,6}[A-Za-z]{0,2})\b' % mots)

    for p in pages:
        texte = p.html
        for m in set(re_tel.findall(texte)):
            normal = re.sub(r'\D', '', m)
            if normal.startswith('33'):
                normal = '0' + normal[2:]
            if normal not in TELEPHONES_AUTORISES:
                pbs.append('%s : numero de telephone NON PREVU « %s ». Le site est '
                           'public : verifier avec David avant de le publier.'
                           % (p.rel, m))
        for m in set(re_mail.findall(texte)):
            if m.lower() not in EMAILS_AUTORISES:
                pbs.append('%s : adresse email NON PREVUE « %s ». A confirmer avant '
                           'publication (elle sera aspiree par les robots).' % (p.rel, m))
        # Le controle des codes d'acces ne regarde QUE le texte de la page :
        # les feuilles de style et les scripts sont retires d'abord. Un code de
        # portail ne se cache pas dans du CSS, alors que le CSS, lui, aligne des
        # nombres a longueur de ligne — « .badge{background:linear-gradient(
        # 90deg,rgba(216… » a bloque une publication le 15/08/2026, « badge »
        # suivi de « 216 » ayant tous les traits d'un code d'entree. Un
        # garde-fou qui crie au loup finit contourne : on retire donc le bruit
        # a la source plutot que d'allonger la liste des exceptions.
        texte_sans_style = re.sub(r'(?is)<(style|script)\b[^>]*>.*?</\1>', ' ', texte)
        for m in re_code.finditer(texte_sans_style):
            contexte = ' '.join(m.group(0).split())
            if any(x in contexte.lower() for x in CODES_HORS_SOUPCON):
                continue
            pbs.append('%s : CODE D\'ACCES POSSIBLE — « %s ». Un code de portail a '
                       'deja fuite deux fois sur ce projet. NE PAS PUBLIER sans '
                       'verifier.' % (p.rel, contexte[:100]))
    return pbs


# --------------------------------------------------------------------------- #
# 8. COHERENCE DES CHIFFRES
# --------------------------------------------------------------------------- #

def controle_chiffres(pages):
    """Le nombre de dates annonce doit egaler le nombre de dates affichees.

    `generate_concert_scene.py` protege deja ce chiffre par un `assert NB_DATES`
    au moment de fabriquer la page. On refait le compte sur la page LIVREE :
    c'est elle que lit un programmateur, et elle peut avoir ete retouchee a la
    main apres coup.
    """
    pbs = []
    for p in pages:
        if p.rel != 'david-lesage-en-concert/index.html':
            continue
        chrono = re.search(r'<dl class="dlc-chrono">(.*?)</dl>', p.html, re.S)
        if not chrono:
            pbs.append('%s : chronologie des dates introuvable' % p.rel)
            continue
        rendues = len(re.findall(r'<li>', chrono.group(1)))
        annonces = set()
        for m in re.finditer(r'(\d[\d\s ]*)\s*dates de sc', p.html):
            annonces.add(int(re.sub(r'\D', '', m.group(1))))
        for m in re.finditer(r'<li><b>([\d\s ]+)</b><span>dates de sc', p.html):
            annonces.add(int(re.sub(r'\D', '', m.group(1))))
        if not annonces:
            pbs.append('%s : aucun decompte de dates affiche' % p.rel)
        for n in sorted(annonces):
            if n != rendues:
                pbs.append('%s : la page annonce %d dates de scene mais la liste '
                           'en contient %d' % (p.rel, n, rendues))
    return pbs


# --------------------------------------------------------------------------- #
# 9. PLAN DU SITE, ROBOTS, REDIRECTIONS
# --------------------------------------------------------------------------- #

def controle_plan(pages):
    """sitemap.xml, robots.txt et vercel.json doivent decrire le site reel."""
    pbs = []
    attendues = {url for url, _ in PAGES}

    chemin = os.path.join(RACINE, 'sitemap.xml')
    if not os.path.exists(chemin):
        pbs.append('sitemap.xml : fichier absent')
    else:
        with open(chemin, encoding='utf-8') as f:
            plan = f.read()
        listees = set()
        for loc in re.findall(r'<loc>\s*([^<]+?)\s*</loc>', plan):
            chemin_url = re.sub(r'^https?://[^/]+', '', loc)
            listees.add(chemin_url.rstrip('/') or '/')
        for manquante in sorted(attendues - listees):
            pbs.append('sitemap.xml : la page %s est publiee mais absente du plan '
                       'du site — Google ne la trouvera pas' % manquante)
        for en_trop in sorted(listees - attendues):
            pbs.append('sitemap.xml : %s est annoncee mais ne correspond a aucune '
                       'page publiee' % en_trop)
        for orpheline in ORPHELINES:
            if orpheline in listees:
                pbs.append('sitemap.xml : %s est une page orpheline, elle ne doit '
                           'pas figurer dans le plan du site' % orpheline)

    chemin = os.path.join(RACINE, 'robots.txt')
    if not os.path.exists(chemin):
        pbs.append('robots.txt : fichier absent')
    else:
        with open(chemin, encoding='utf-8') as f:
            robots = f.read()
        interdites = set(re.findall(r'(?im)^\s*Disallow:\s*(\S+)\s*$', robots))
        for orpheline in ORPHELINES:
            if orpheline not in interdites:
                pbs.append('robots.txt : %s reste accessible aux moteurs de '
                           'recherche alors que la page est abandonnee' % orpheline)
        for interdite in sorted(interdites):
            if interdite.rstrip('/') in attendues:
                pbs.append('robots.txt : %s est une page publiee, elle ne doit pas '
                           'etre interdite aux moteurs' % interdite)
        if 'Sitemap:' not in robots:
            pbs.append('robots.txt : le lien vers sitemap.xml a disparu')

    chemin = os.path.join(RACINE, 'vercel.json')
    if not os.path.exists(chemin):
        pbs.append('vercel.json : fichier absent')
    else:
        import json
        try:
            with open(chemin, encoding='utf-8') as f:
                conf = json.load(f)
        except ValueError as e:
            pbs.append('vercel.json : fichier illisible (%s) — Vercel refusera le '
                       'deploiement' % e)
            conf = {}
        ids = {p.url: p.ids for p in pages}
        for red in conf.get('redirects', []):
            cible = red.get('destination', '')
            page, _, ancre = cible.partition('#')
            page = page.rstrip('/') or '/'
            if page not in attendues:
                pbs.append('vercel.json : la redirection %s renvoie vers %s, qui '
                           'n\'existe pas' % (red.get('source'), cible))
            elif ancre and ancre not in ids[page]:
                pbs.append('vercel.json : la redirection %s renvoie vers %s, mais '
                           'l\'ancre #%s n\'existe pas sur cette page'
                           % (red.get('source'), cible, ancre))
    return pbs


# --------------------------------------------------------------------------- #
# 10. VERIFICATION GOOGLE SEARCH CONSOLE  —  une seule pose, sur l'accueil
# --------------------------------------------------------------------------- #

#: la page qui porte la balise `google-site-verification`, et elle seule.
PAGE_VERIFICATION_GOOGLE = 'index.html'


def controle_verification(pages):
    """La balise Google Search Console : exactement une, et sur l'accueil.

    Posee le 15/08/2026 (code fourni par David). Elle verifie la propriete
    « prefixe d'URL » : Google ne lit la balise que sur la page demandee, donc
    une seule pose suffit. La recopier sur les 30 pages ne verifie rien de plus
    et rend son retrait hasardeux — on ne saurait plus, un an apres, combien
    d'exemplaires trainent ni pourquoi.

    ⚠️ Une propriete « domaine » est verifiee EN PARALLELE par un enregistrement
       TXT dans la zone DNS OVH. Les deux methodes coexistent sans conflit :
       trouver la balise absente d'une page ne veut pas dire que la verification
       est cassee, cela veut dire que c'est la ligne DNS qui travaille.
    """
    pbs = []
    total = 0
    for p in pages:
        n = len(re.findall(r'<meta[^>]*name="google-site-verification"[^>]*>', p.html))
        total += n
        if p.rel == PAGE_VERIFICATION_GOOGLE:
            if n != 1:
                pbs.append('%s : %d balise(s) google-site-verification, attendu 1 — '
                           'c\'est la seule page qui doit la porter' % (p.rel, n))
        elif n:
            pbs.append('%s : balise google-site-verification en trop. Elle n\'a le '
                       'droit d\'exister que sur %s.' % (p.rel, PAGE_VERIFICATION_GOOGLE))
    if total > 1:
        pbs.append('la balise google-site-verification apparait %d fois sur le site, '
                   'attendu 1' % total)
    return pbs


# --------------------------------------------------------------------------- #
# Enchainement
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# 11. IMAGE DE PARTAGE  (og:image)
# --------------------------------------------------------------------------- #
# Ce que voit quelqu'un a qui on envoie un lien du site dans WhatsApp, sur
# Facebook ou par SMS : une vignette, un titre, une ligne de texte. La vignette
# est `og:image`, et c'est une balise PAR PAGE — c'est ce qui permet a chaque
# page d'avoir la sienne (demande de David, 16/08/2026).
#
# Ce qui se casse en silence, et que ce controle attrape :
#   - un chemin RELATIF : ignore par toutes les messageries, aucune image ne
#     s'affiche. L'adresse doit etre absolue, sur le domaine du site ;
#   - un fichier renomme ou deplace : le partage montre un cadre vide, et la
#     page, elle, continue de s'afficher normalement — personne ne le voit ;
#   - des dimensions declarees FAUSSES : l'apercu se dessine de travers, ou
#     n'apparait qu'au deuxieme envoi. Elles sont donc relues sur le fichier ;
#   - du WebP : plusieurs messageries ne le rendent pas encore en apercu. Le
#     depot contient les deux formats pour chaque photo, on prend le `.jpg` ;
#   - un `twitter:image` qui aurait diverge de `og:image` (deux balises a tenir
#     d'accord). Aucune page n'en porte aujourd'hui : `twitter:card` +
#     `og:image` suffisent, X reprend `og:image` a defaut. La regle est ecrite
#     pour le jour ou quelqu'un en ajoutera une.
MARQUES_PARTAGE = 'https://www.resonancesproductions.org'


def controle_partage(pages):
    """Une image de partage par page, qui existe et aux bonnes dimensions."""
    pbs = []
    for p in pages:
        images = re.findall(r'<meta\s+property="og:image"\s+content="([^"]*)"', p.html)
        if len(images) != 1:
            pbs.append('%s : %d balise(s) og:image, attendu exactement 1 — c\'est '
                       'l\'image affichee quand on partage le lien' % (p.rel, len(images)))
            continue
        url = images[0]
        if not url.startswith(MARQUES_PARTAGE + '/'):
            pbs.append('%s : og:image = %s — l\'adresse doit etre absolue et sur '
                       '%s, sinon aucune messagerie ne l\'affiche'
                       % (p.rel, url, MARQUES_PARTAGE))
            continue
        rel = url[len(MARQUES_PARTAGE):].split('?')[0]
        if rel.lower().endswith('.webp'):
            pbs.append('%s : og:image en WebP (%s) — plusieurs messageries ne le '
                       'rendent pas en apercu ; prendre le .jpg' % (p.rel, rel))
        chemin = os.path.join(RACINE, rel.lstrip('/'))
        if not os.path.exists(chemin):
            pbs.append('%s : og:image %s — ce fichier n\'existe pas dans le depot'
                       % (p.rel, rel))
            continue
        for balise in ('og:image:width', 'og:image:height', 'og:image:alt'):
            if 'property="%s"' % balise not in p.html:
                pbs.append('%s : og:image sans %s' % (p.rel, balise))
        taille = _lire_image(rel)
        declare = {}
        for nom in ('width', 'height'):
            m = re.search(r'<meta\s+property="og:image:%s"\s+content="(\d+)"' % nom, p.html)
            if m:
                declare[nom] = int(m.group(1))
        if taille and len(declare) == 2:
            if (declare['width'], declare['height']) != taille:
                pbs.append('%s : og:image annonce %dx%d, le fichier %s fait %dx%d'
                           % (p.rel, declare['width'], declare['height'], rel,
                              taille[0], taille[1]))
        m = re.search(r'<meta\s+(?:name|property)="twitter:image"\s+content="([^"]*)"', p.html)
        if m and m.group(1) != url:
            pbs.append('%s : twitter:image (%s) differe de og:image (%s)'
                       % (p.rel, m.group(1), url))
    return pbs


CONTROLES = (
    ('commentaires', 'Aucune note de travail dans le code des pages', controle_commentaires),
    ('menu',         'Menu present une fois, complet, sans doublon',   controle_menu),
    ('titre',        'Un seul titre principal (<h1>) par page',        controle_titre),
    ('images',       'Images presentes, dimensionnees, jamais etirees', controle_images),
    ('liens',        'Aucun lien ni ancre qui ne mene nulle part',     controle_liens),
    ('doublons',     'Aucun bloc de structure en double',              controle_doublons),
    ('donnees',      'Aucun code d\'acces ni contact non prevu',       controle_donnees),
    ('chiffres',     'Les nombres affiches correspondent au contenu',  controle_chiffres),
    ('plan',         'Plan du site, robots.txt et redirections a jour', controle_plan),
    ('google',       'Verification Search Console posee une seule fois', controle_verification),
    ('partage',      'Image de partage propre a chaque page, verifiee',  controle_partage),
)


def verifier(silencieux=False):
    """Renvoie (tout_va_bien, {nom_controle: [problemes]})."""
    pages = _charger()
    absentes = [p for p in pages if not p.existe]
    resultats = {}
    for nom, _titre, fonction in CONTROLES:
        resultats[nom] = fonction([p for p in pages if p.existe])
    if absentes:
        resultats['commentaires'] = (['%s : PAGE ABSENTE du depot' % p.rel
                                      for p in absentes]
                                     + resultats['commentaires'])
    ok = not any(resultats.values())
    if not silencieux:
        _afficher(pages, resultats, ok)
    return ok, resultats


def _afficher(pages, resultats, ok):
    print('')
    print('  VERIFICATION DU SITE — %d pages publiees' % len(pages))
    print('  ' + '-' * 66)
    for nom, titre, _f in CONTROLES:
        pbs = resultats[nom]
        etat = 'OK  ' if not pbs else 'STOP'
        print('  [%s] %-13s %s' % (etat, nom, titre))
        for message in pbs:
            print('         > %s' % message)
    # decompte par page
    fautives = set()
    for pbs in resultats.values():
        for message in pbs:
            for p in pages:
                if message.startswith(p.rel):
                    fautives.add(p.rel)
    conformes = len(pages) - len(fautives)
    print('  ' + '-' * 66)
    if ok:
        print('  %d/%d pages conformes. Rien a signaler, le site peut partir en ligne.'
              % (len(pages), len(pages)))
    else:
        total = sum(len(v) for v in resultats.values())
        print('  %d/%d pages conformes — %d probleme(s) a corriger.'
              % (conformes, len(pages), total))
        print('')
        print('  >> NE PAS PUBLIER EN L\'ETAT. Pousser sur GitHub met le site en')
        print('     ligne automatiquement : ce qui est ci-dessus serait visible.')
        print('     Corrige la SOURCE dans sources/, relance :')
        print('       python3 sources/build.py && python3 sources/verif_site.py')
    print('')


def main(argv):
    return 0 if verifier()[0] else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
