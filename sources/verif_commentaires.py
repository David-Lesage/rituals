# -*- coding: utf-8 -*-
"""Garde-fou : aucune note de travail dans les pages livrees, HTML **ni CSS**.

POURQUOI CE MODULE EXISTE
-------------------------
Les notes de redaction ecrites en commentaires HTML (« pourquoi cette photo est
ici », « ne pas reecrire cette legende », « David a dit que... ») ne s'affichent
pas a l'ecran, mais N'IMPORTE QUI les lit en affichant le code source de la
page, et elles sont indexables. Le depot est PUBLIC et le site est celui d'une
association : ces notes citent des personnes et exposent des raisonnements
editoriaux. Elles n'ont rien a faire dans le HTML livre.

Leur place est dans les generateurs Python, en commentaires `#`, juste au-dessus
du code qui produit le bloc concerne. Elles y restent lisibles pour la prochaine
session, et elles ne partent pas chez le visiteur.

⚠️ LE DEFAUT EST REVENU PAR LA PORTE DU CSS (constate le 16/08/2026)
-------------------------------------------------------------------
Ce fichier ne regardait QUE les commentaires HTML. Les memes notes sont donc
reparties dans les pages, ecrites cette fois en commentaires CSS `/* ... */` a
l'interieur des blocs `<style>` : **1 408 commentaires, 153 366 caracteres** sur
les 30 pages, dont 10 932 sur la seule `/guso-facile`. Raisonnements de
conception, decisions datees, avertissements a de futurs agents — et meme un
emoji (🤗), que la charte du site interdit, entre par cette porte-la.

Les notes n'ont pas ete detruites : elles sont parties en commentaires `#` dans
les generateurs, au-dessus du code qui emet la regle concernee (les gabarits CSS
sont pour cela ecrits en plusieurs litteraux adjacents, concatenes par Python).
Ce module refuse desormais d'ecrire une page qui en contiendrait de nouvelles.

CE QUI RESTE AUTORISE
---------------------
* En HTML : uniquement les marqueurs FONCTIONNELS relus par un script — voir
  `MOTIFS_AUTORISES`, chaque entree porte la raison pour laquelle elle est
  indispensable.
* En CSS : les marqueurs fonctionnels de `MARQUEURS_CSS_FONCTIONNELS` (relus,
  eux aussi, par un script : les retirer casse un generateur EN SILENCE), plus
  les **etiquettes courtes** — une seule ligne, `LONGUEUR_MAX` caracteres au
  plus, sans emoji : `/* carrousel */`, `/* retour en haut */`. Elles servent a
  se reperer dans une feuille de style de 1 500 lignes. Tout ce qui deborde est
  une note de raisonnement : elle va en Python.

COMMENT S'EN SERVIR
-------------------
1. Dans un generateur, JUSTE AVANT d'ecrire le fichier :

       import verif_commentaires
       verif_commentaires.verifier(html, OUT)   # leve SystemExit si probleme

   L'ecriture est alors ABANDONNEE et la page sur disque reste inchangee.
   C'est le meme parti-pris que le garde-fou structurel de `generate_rythme.py`
   (compte d'occurrences d'un marqueur) : mieux vaut refuser d'ecrire que
   d'imprimer un avertissement qui defile et que personne ne lit.

2. Avant n'importe quel deploiement, en une passe sur tout le depot :

       python3 sources/verif_commentaires.py
       echo $?      # 0 = tout est propre, 1 = au moins une page fautive

   Avec des arguments, ne verifie que les fichiers donnes.
"""

import os
import re
import sys

# --------------------------------------------------------------------------- #
# LISTE BLANCHE HTML — les seuls commentaires HTML autorises dans une page
# --------------------------------------------------------------------------- #
#: (motif, raison d'etre). Le motif doit decrire le commentaire ENTIER.
#
# ⚠️ Le motif du marqueur d'ouverture est VOLONTAIREMENT ecrit sans le numero de
#    version (`\([^)>]*\)`) : il accepte donc « resonances-2 », « resonances-3 »
#    et les suivantes. Incrementer `NAV_VERSION` dans `nav_menu.py` ne demande
#    AUCUNE modification ici — verifie le 14/08/2026 lors du passage a
#    resonances-3. Ne pas y figer un numero : le jour ou la version bougerait
#    sans que ce fichier suive, TOUTES les pages seraient refusees a l'ecriture.
MOTIFS_AUTORISES = (
    (r'<!-- nav_menu\.py \([^)>]*\) -->',
     "ouverture du bloc JS du menu partage. C'est la GARDE D'IDEMPOTENCE de "
     "nav_menu.py (JS_MARK) : sans elle le menu se reinjecte a chaque passe et "
     "on retrouve les entrees en double. Elle porte aussi le numero de version "
     "(NAV_VERSION), que `inject()` relit pour nettoyer l'ancien menu avant "
     "d'en poser un neuf."),
    (r'<!-- fin nav_menu\.py -->',
     "fermeture du meme bloc (JS_END). `_strip()` s'en sert comme borne de fin "
     "pour retirer le JS d'une ancienne version du menu ; sans elle le nettoyage "
     "ne trouve plus ou s'arreter."),
)

# --------------------------------------------------------------------------- #
# LISTE BLANCHE CSS — les commentaires CSS qu'un script RELIT
# --------------------------------------------------------------------------- #
#: (motif, raison d'etre). Ceux-la sont exemptes de la limite de longueur : leur
#: texte EST l'ancre, le raccourcir demanderait de toucher plusieurs generateurs
#: du meme coup. Etablie le 16/08/2026 en cherchant, dans `sources/*.py`, tout
#: `replace()`, `find()`, `count()` ou test de presence visant un `/* ... */`.
#: ⚠️ En retirer un ne se verrait PAS a l'ecran : le generateur concerne
#:    reinjecterait son bloc a chaque passe, ou refuserait d'ecrire.
MARQUEURS_CSS_FONCTIONNELS = (
    (r'/\* == nav_menu\.py \([^)*]*\) == \*/',
     "CSS_MARK de nav_menu.py : borne de DEBUT relue par `_strip()` (regex "
     "`/\\* == nav_menu\\.py \\(([^)]*)\\) == \\*/`) pour retirer le CSS d'une "
     "ancienne version du menu. Ecrit SANS numero de version ici, meme raison "
     "que pour le marqueur HTML : incrementer NAV_VERSION ne doit rien casser."),
    (r'/\* == fin nav_menu\.py == \*/',
     "CSS_END de nav_menu.py : borne de FIN du meme nettoyage. Sans elle "
     "`_strip()` ne sait plus ou s'arreter. `generate_soin_soa.py` compte aussi "
     "la ligne vide qui precede CSS_MARK."),
    (r'/\* --- lisibilite des liens --- \*/',
     "debut du bloc « lisibilite des liens », qui doit rester le DERNIER a "
     "parler taille de texte. `generate_site.py` et `generate_trio.py` le "
     "cherchent par `find()` (DEB_LISI) pour DEPLACER le bloc en fin de feuille "
     "de style ; `generate_assoc.py` s'en sert de garde d'idempotence et le "
     "compte dans `_ATTENDU`. Raccourci le 16/08/2026 : sa raison d'etre "
     "(« demande de David : liens et dates trop petits ») est passee en Python."),
    (r'/\* ===== AGENDA DU NID ===== \*/',
     "atteste la feuille de style de l'agenda : comptee par `_exiger()` dans "
     "generate_agenda_nid.py, qui refuse d'ecrire si elle n'est pas la."),
    (r'/\* ===== MENU MOBILE \(hamburger\) ===== \*/',
     "premiere ligne de `mobile_nav.CSS`. `generate_trio.py` compte "
     "« ===== MENU MOBILE » dans `_ATTENDU_1` ; `generate_site.py` et "
     "`generate_trio.py` verifient en plus `html.count(mobile_nav.CSS) == 1`."),
)

#: un marqueur technique ou une etiquette de section tiennent largement dans 60
#: caracteres ; au-dela, c'est une note de travail deguisee en marqueur.
LONGUEUR_MAX = 60

#: les 31 pages publiees (voir REPRENDRE-RESONANCES-SITE.md).
PAGES = (
    'index.html',
    'rituals/index.html',
    'rituals-trio/index.html',
    'e-motion/index.html',
    'david-lesage-en-concert/index.html',
    'concerts-david-lesage/index.html',
    'le-nid/index.html',
    'rendez-vous-mensuels/index.html',
    'le-soin-soa/index.html',
    'rythme-calebasse/index.html',
    'association/index.html',
    'guso-facile/index.html',
    'guso-facile/blog/index.html',
    'guso-facile/blog/atteindre-507-heures-sans-angoisse/index.html',
    'guso-facile/blog/c-est-quoi-le-guso-concretement/index.html',
    'guso-facile/blog/ca-va-te-faire-connaitre-comment-repondre/index.html',
    'guso-facile/blog/combien-de-cachets-pour-507-heures/index.html',
    'guso-facile/blog/comment-declarer-une-repetition/index.html',
    'guso-facile/blog/employeur-ne-m-a-pas-paye-mon-cachet/index.html',
    'guso-facile/blog/evaluer-si-une-date-est-un-bon-plan/index.html',
    'guso-facile/blog/faut-il-un-contrat-pour-un-concert/index.html',
    'guso-facile/blog/heures-ne-correspondent-pas-france-travail/index.html',
    'guso-facile/blog/m-organiser-quand-je-joue-dans-plusieurs-groupes/index.html',
    'guso-facile/blog/ne-plus-jamais-oublier-une-dpae/index.html',
    'guso-facile/blog/organiser-une-tournee-qui-tient-la-route/index.html',
    'guso-facile/blog/pointage-france-travail-sans-stress/index.html',
    'guso-facile/blog/quand-tombe-ma-date-anniversaire/index.html',
    'guso-facile/blog/structure-accompagner-ses-artistes/index.html',
    'guso-facile/blog/structure-comment-gerer-les-guso-de-mes-artistes/index.html',
    'guso-facile/blog/studio-et-cheque-intermittents/index.html',
    'guso-facile/blog/travailler-a-deux-artistes-dates-partagees/index.html',
)

_RE_COMMENTAIRE = re.compile(r'<!--.*?-->', re.S)
_RE_STYLE = re.compile(r'<style\b[^>]*>(.*?)</style>', re.S | re.I)
_AUTORISES = tuple((re.compile(r'\A' + motif + r'\Z', re.S), raison)
                   for motif, raison in MOTIFS_AUTORISES)
_CSS_AUTORISES = tuple((re.compile(r'\A' + motif + r'\Z', re.S), raison)
                       for motif, raison in MARQUEURS_CSS_FONCTIONNELS)


def _est_emoji(ch):
    """Pictogrammes couleur — la charte du site les interdit dans les pages."""
    o = ord(ch)
    return (0x1F000 <= o <= 0x1FAFF        # emoticones, pictogrammes, symboles
            or 0x2600 <= o <= 0x27BF       # symboles divers et dingbats
            or 0x1F1E6 <= o <= 0x1F1FF     # drapeaux
            or o in (0x2B50, 0x2B55, 0xFE0F, 0x20E3, 0x203C, 0x2049))


# --------------------------------------------------------------------------- #
# Lecture des commentaires CSS
# --------------------------------------------------------------------------- #
# ⚠️ On NE PEUT PAS se contenter de `re.findall(r'/\*.*?\*/')` : `/*` peut vivre
#    a l'interieur d'une chaine CSS parfaitement legitime — une `url("data:...")`
#    ou un `content:"…/*…"`. On avance donc caractere par caractere en sautant
#    par-dessus ce qui est entre guillemets. Teste : sur les 30 pages du site les
#    deux lectures donnent aujourd'hui le meme resultat, mais la premiere
#    `data:` un peu tordue ferait refuser toutes les pages a l'ecriture.

def _commentaires_dans_css(css):
    """[(position, texte), ...] pour UNE feuille de style."""
    out = []
    i, n = 0, len(css)
    while i < n:
        c = css[i]
        if c in '"\'':
            fin = c
            i += 1
            while i < n and css[i] != fin:
                if css[i] == '\\':
                    i += 1
                i += 1
            i += 1
        elif css.startswith('/*', i):
            j = css.find('*/', i)
            j = n if j < 0 else j + 2
            out.append((i, css[i:j]))
            i = j
        else:
            i += 1
    return out


def commentaires_css(html):
    """[(position dans la page, texte), ...] pour tous les blocs <style>."""
    out = []
    for m in _RE_STYLE.finditer(html):
        depart = m.start(1)
        for pos, texte in _commentaires_dans_css(m.group(1)):
            out.append((depart + pos, texte))
    return out


def _apercu(txt, n=140):
    """Une ligne lisible pour le message d'erreur."""
    plat = ' '.join(txt.split())
    return plat if len(plat) <= n else plat[:n - 1] + '…'


def anomalies(html):
    """Renvoie [(position, motif du refus, commentaire), ...] — vide si tout va bien."""
    trouve = []
    for m in _RE_COMMENTAIRE.finditer(html):
        c = m.group(0)
        if not any(rx.match(c) for rx, _ in _AUTORISES):
            trouve.append((m.start(), 'commentaire HTML non autorise', c))
        elif len(c) > LONGUEUR_MAX:
            trouve.append((m.start(),
                           'marqueur HTML autorise mais trop long (%d > %d caracteres)'
                           % (len(c), LONGUEUR_MAX), c))

    for pos, c in commentaires_css(html):
        if any(rx.match(c) for rx, _ in _CSS_AUTORISES):
            continue          # marqueur fonctionnel : jamais refuse
        emojis = sorted({x for x in c if _est_emoji(x)})
        if emojis:
            trouve.append((pos, 'commentaire CSS contenant un emoji (%s) — '
                                'la charte du site les interdit'
                                % ' '.join(emojis), c))
        elif '\n' in c:
            trouve.append((pos, 'commentaire CSS sur %d lignes — une etiquette '
                                'tient sur une seule' % (c.count('\n') + 1), c))
        elif len(c) > LONGUEUR_MAX:
            trouve.append((pos, 'commentaire CSS trop long (%d > %d caracteres) : '
                                'ce n\'est plus une etiquette, c\'est une note'
                                % (len(c), LONGUEUR_MAX), c))
    trouve.sort()
    return trouve


def rapport(html):
    """(nombre de commentaires HTML, poids) — les commentaires CSS a part."""
    tous = _RE_COMMENTAIRE.findall(html)
    return len(tous), sum(len(c) for c in tous)


def rapport_css(html):
    """(nombre de commentaires CSS, poids total en caracteres)."""
    tous = [c for _, c in commentaires_css(html)]
    return len(tous), sum(len(c) for c in tous)


def verifier(html, page='(page)'):
    """Leve SystemExit si un commentaire interdit est present. Renvoie `html`.

    A appeler AVANT l'ecriture : la page sur disque reste alors inchangee.
    """
    mauvais = anomalies(html)
    if not mauvais:
        return html
    lignes = ['!! ABANDON : %d commentaire(s) interdit(s) dans %s.'
              % (len(mauvais), page),
              '   Page NON ecrite (le fichier sur disque est inchange).']
    for pos, pourquoi, c in mauvais:
        lignes.append('   - car. %d : %s' % (pos, pourquoi))
        lignes.append('     %s' % _apercu(c))
    lignes.append('')
    lignes.append('   Les notes de redaction vont en commentaire Python `#` dans')
    lignes.append('   le generateur, au-dessus du code qui produit le bloc — pas')
    lignes.append('   dans la page livree, HTML ni CSS. Restent autorises :')
    lignes.append('')
    lignes.append('   * en HTML, ces marqueurs et eux seuls :')
    for motif, raison in MOTIFS_AUTORISES:
        lignes.append('       %s' % motif)
        lignes.append('           %s' % _apercu(raison, 200))
    lignes.append('   * en CSS, ces marqueurs fonctionnels (relus par un script,')
    lignes.append('     les retirer casse un generateur en silence) :')
    for motif, raison in MARQUEURS_CSS_FONCTIONNELS:
        lignes.append('       %s' % motif)
        lignes.append('           %s' % _apercu(raison, 200))
    lignes.append('   * en CSS, les etiquettes courtes : UNE ligne, %d caracteres'
                  % LONGUEUR_MAX)
    lignes.append('     au plus, sans emoji — « /* retour en haut */ ».')
    raise SystemExit('\n'.join(lignes))


# --------------------------------------------------------------------------- #
# CLI : verifie les 31 pages d'un coup, sort en code d'erreur
# --------------------------------------------------------------------------- #

def _controle_fichier(chemin):
    """Affiche une ligne de tableau. Renvoie True si la page est propre."""
    with open(chemin, encoding='utf-8') as f:
        html = f.read()
    n, poids = rapport(html)
    ncss, poids_css = rapport_css(html)
    mauvais = anomalies(html)
    etat = 'OK  ' if not mauvais else 'FAUT'
    print('%s  %-38s HTML %2d (%5d car.)   CSS %2d (%5d car.)'
          % (etat, chemin, n, poids, ncss, poids_css))
    for pos, pourquoi, c in mauvais:
        print('        car. %-7d %s' % (pos, pourquoi))
        print('        %s' % _apercu(c))
    return not mauvais


def main(argv):
    racine = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cibles = argv[1:] or [os.path.join(racine, p) for p in PAGES]
    manquants = [c for c in cibles if not os.path.exists(c)]
    for c in manquants:
        print('ABSENT  %s' % c)
    presents = [c for c in cibles if os.path.exists(c)]
    propres = [_controle_fichier(c) for c in presents]
    ok = all(propres) and not manquants
    print('')
    print('%d/%d page(s) propre(s).%s'
          % (sum(propres), len(presents),
             '' if ok else '  >> NE PAS DEPLOYER EN L\'ETAT.'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
