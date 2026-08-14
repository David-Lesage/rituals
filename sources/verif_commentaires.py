# -*- coding: utf-8 -*-
"""Garde-fou : aucun commentaire HTML de travail dans les pages livrees.

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

CE QUI RESTE AUTORISE
---------------------
Uniquement les marqueurs FONCTIONNELS, ceux qu'un script relit. Les supprimer
casserait le site : voir `MOTIFS_AUTORISES` ci-dessous, chaque entree porte la
raison pour laquelle elle est indispensable.

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
# LISTE BLANCHE — les seuls commentaires autorises dans une page livree
# --------------------------------------------------------------------------- #
#: (motif, raison d'etre). Le motif doit decrire le commentaire ENTIER.
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

#: un marqueur technique tient largement dans 60 caracteres ; au-dela, c'est une
#: note de travail deguisee en marqueur.
LONGUEUR_MAX = 60

#: les 9 pages publiees (voir REPRENDRE-RESONANCES-SITE.md).
PAGES = (
    'index.html',
    'rituals/index.html',
    'rituals-trio/index.html',
    'e-motion/index.html',
    'david-lesage-en-concert/index.html',
    'concerts-david-lesage/index.html',
    'le-nid/index.html',
    'le-soin-soa/index.html',
    'rythme-calebasse/index.html',
)

_RE_COMMENTAIRE = re.compile(r'<!--.*?-->', re.S)
_AUTORISES = tuple((re.compile(r'\A' + motif + r'\Z', re.S), raison)
                   for motif, raison in MOTIFS_AUTORISES)


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
            trouve.append((m.start(), 'commentaire non autorise', c))
        elif len(c) > LONGUEUR_MAX:
            trouve.append((m.start(),
                           'marqueur autorise mais trop long (%d > %d caracteres)'
                           % (len(c), LONGUEUR_MAX), c))
    return trouve


def rapport(html):
    """(nombre de commentaires, poids total en caracteres)."""
    tous = _RE_COMMENTAIRE.findall(html)
    return len(tous), sum(len(c) for c in tous)


def verifier(html, page='(page)'):
    """Leve SystemExit si un commentaire interdit est present. Renvoie `html`.

    A appeler AVANT l'ecriture : la page sur disque reste alors inchangee.
    """
    mauvais = anomalies(html)
    if not mauvais:
        return html
    lignes = ['!! ABANDON : %d commentaire(s) HTML interdit(s) dans %s.'
              % (len(mauvais), page),
              '   Page NON ecrite (le fichier sur disque est inchange).']
    for pos, pourquoi, c in mauvais:
        lignes.append('   - car. %d : %s' % (pos, pourquoi))
        lignes.append('     %s' % _apercu(c))
    lignes.append('')
    lignes.append('   Les notes de redaction vont en commentaire Python `#` dans')
    lignes.append('   le generateur, au-dessus du code qui produit le bloc — pas')
    lignes.append('   dans le HTML livre. Seuls restent autorises :')
    for motif, raison in MOTIFS_AUTORISES:
        lignes.append('     %s' % motif)
        lignes.append('         %s' % _apercu(raison, 200))
    raise SystemExit('\n'.join(lignes))


# --------------------------------------------------------------------------- #
# CLI : verifie les 9 pages d'un coup, sort en code d'erreur
# --------------------------------------------------------------------------- #

def _controle_fichier(chemin):
    """Affiche une ligne de tableau. Renvoie True si la page est propre."""
    with open(chemin, encoding='utf-8') as f:
        html = f.read()
    n, poids = rapport(html)
    mauvais = anomalies(html)
    etat = 'OK  ' if not mauvais else 'FAUT'
    print('%s  %-38s %2d commentaire(s), %6d car.'
          % (etat, chemin, n, poids))
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
