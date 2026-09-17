# -*- coding: utf-8 -*-
"""Pose la balise `<link rel="canonical">` sur CHAQUE page publiee.

POURQUOI CE MODULE EXISTE — DEFAUT TROUVE LE 18/09/2026
------------------------------------------------------
David signalait des pages « non indexees » dans Google Search Console. La
cause tenait a deux faits qui, pris ensemble, fabriquent des doublons :

  1. Vercel sert la MEME page a DEUX adresses, les deux en HTTP 200 :
         https://www.resonancesproductions.org/le-nid
         https://www.resonancesproductions.org/le-nid/
     (verifie le 18/09/2026 sur le site en ligne, pas suppose.)

  2. DIX des trente et une pages n'avaient AUCUNE balise canonique — toutes
     les pages principales, justement : l'accueil, /le-nid, /rituals,
     /e-motion, /rendez-vous-mensuels, /concerts-david-lesage… Seules celles
     de Guso Facile, /association et la page du duo en portaient une.

Sans canonique, c'est Google qui choisit l'adresse de reference entre les deux
— et il annonce alors « page en double » ou « Google n'a pas selectionne la
meme page canonique que l'utilisateur ». Le referencement se disperse sur deux
adresses au lieu de s'additionner sur une seule.

⚠️ CE MODULE NE DECIDE RIEN. L'adresse canonique d'une page est celle que
   `verif_site.PAGES` lui donne deja — la meme table qui sert au plan du site
   et aux onze controles. Elle n'est donc jamais recopiee ici : deux listes
   concurrentes finissent toujours par diverger.

⚠️ IL EST IDEMPOTENT, et c'est structurel : `build.py` construit chaque page
   DEUX FOIS et exige le meme fichier a l'octet pres. Une pose qui s'ajouterait
   a chaque passage ferait echouer cette verification — c'est exactement ce
   qui avait produit quatre entrees « Agenda » dans le menu. Une page qui a
   deja sa canonique est donc laissee telle quelle, sans y toucher.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verif_site  # noqa: E402  (la table PAGES, jamais recopiee)

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.resonancesproductions.org'

#: fichier livre -> adresse canonique. Construit depuis `verif_site.PAGES`.
#: ⚠️ L'ACCUEIL GARDE SA BARRE FINALE (« …org/ »), les autres pages n'en ont
#:    pas. Ce n'est pas une inconsistance : c'est exactement ce qu'ecrit le
#:    plan du site (`sitemap.xml`), et une canonique qui ne dirait pas la meme
#:    chose que le plan du site ferait douter Google au lieu de le renseigner.
URL_PAR_FICHIER = {
    fichier: SITE + url
    for url, fichier in verif_site.PAGES
}

#: ⚠️ SANS BARRE OBLIQUE FINALE, et c'est un choix, pas un oubli. Les quatre
#: pages qui portaient deja une canonique avant ce module l'ecrivent ainsi
#: (« …/association », « …/guso-facile »), les liens internes du site aussi, et
#: le plan du site egalement. Changer de forme ici ferait dire au site deux
#: choses differentes de la meme page — precisement le probleme qu'on corrige.

#: la balise est posee JUSTE AVANT le favicon, comme sur les pages qui en
#: avaient deja une : meme place partout, donc lisible d'un coup d'oeil.
ANCRE = '<link rel="icon"'


def manquantes():
    """Les pages publiees qui n'ont pas encore de balise canonique."""
    out = []
    for fichier in URL_PAR_FICHIER:
        chemin = os.path.join(RACINE, fichier)
        if not os.path.exists(chemin):
            continue
        with open(chemin, encoding='utf-8') as f:
            if '<link rel="canonical"' not in f.read():
                out.append(fichier)
    return out


def poser(fichier):
    """Pose la canonique sur UNE page livree. Renvoie True si elle a change.

    Ne touche a rien si la page en a deja une : voir la note d'idempotence en
    tete de fichier.
    """
    url = URL_PAR_FICHIER.get(fichier)
    if url is None:
        return False                      # page hors du site publie
    chemin = os.path.join(RACINE, fichier)
    if not os.path.exists(chemin):
        return False
    with open(chemin, encoding='utf-8') as f:
        html = f.read()
    if '<link rel="canonical"' in html:
        return False
    balise = '<link rel="canonical" href="%s">\n' % url
    if ANCRE in html:
        html = html.replace(ANCRE, balise + ANCRE, 1)
    elif '</head>' in html:
        html = html.replace('</head>', balise + '</head>', 1)
    else:
        raise SystemExit('!! ABANDON : %s n’a ni favicon ni </head> : impossible '
                         'de savoir ou poser la balise canonique.' % fichier)
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write(html)
    return True


if __name__ == '__main__':
    cibles = sys.argv[1:] or list(URL_PAR_FICHIER)
    faits = [f for f in cibles if poser(f)]
    if faits:
        print('Balise canonique posee sur %d page(s) :' % len(faits))
        for f in faits:
            print('  · %-46s %s' % (f, URL_PAR_FICHIER[f]))
    else:
        print('Toutes les pages avaient deja leur balise canonique.')
