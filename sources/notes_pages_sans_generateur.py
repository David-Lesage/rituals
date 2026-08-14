# -*- coding: utf-8 -*-
"""Notes de redaction des pages QUI N'ONT PAS DE GENERATEUR.

Ce module n'execute rien et n'est importe par personne : c'est un porte-notes.

Pourquoi il existe : les notes de redaction (« pourquoi cette photo est ici »,
« ne pas reintroduire ceci ») vivaient en commentaires HTML dans les pages
livrees — donc lisibles par n'importe quel visiteur affichant le code source, et
indexables. Elles ont ete sorties du HTML (voir `sources/verif_commentaires.py`,
qui refuse maintenant qu'elles y reviennent). Pour les pages produites par un
generateur, elles sont retournees dans le generateur, juste au-dessus du code
qui emet le bloc. Restait le cas des pages editees A LA MAIN, qui n'ont aucun
code a elles : leurs notes sont ici.

OU SONT LES AUTRES NOTES
------------------------
  /rituals                  sources/generate_site.py
  /rituals-trio             sources/generate_trio.py
  /e-motion                 ICI (aucun generateur)
  /david-lesage-en-concert  sources/generate_concert_scene.py
  /concerts-david-lesage    sources/generate_concert_dl.py
  /le-nid                   sources/generate_agenda_nid.py
  /le-soin-soa              sources/generate_soin_soa.py
  /rythme-calebasse         sources/generate_rythme.py
  /                         sources/generate_assoc.py

⚠️ Le bloc « seconde photo du Grand Rex » de /rituals est lui aussi un ajout a
la main (le generateur ne peut plus tourner, ses dossiers photos sont hors
depot) : sa note est restee dans `sources/generate_site.py`, a l'endroit ou le
bloc s'insere, parce que c'est le seul code qui produit cette page.
"""

# --------------------------------------------------------------------------- #
# /e-motion  (e-motion/index.html)
#
# ⚠️ AUCUN GENERATEUR n'ecrit cette page. `sources/emotion_final.html` en est une
# copie de travail PERIMEE (elle porte encore le menu `resonances-1`) : ne pas
# s'en servir pour regenerer quoi que ce soit. La page se modifie directement
# dans `e-motion/index.html`, et le menu partage se (re)pose avec
#     python3 sources/nav_menu.py e-motion/index.html
# --------------------------------------------------------------------------- #

# --- en-tete de la page, bloc `.inner` du <header> (h1 + sous-titre) ---------
#
# Le titre et le sous-titre sont deja incrustes dans la banniere ci-dessus :
# on les conserve dans le code (h1 unique, SEO + lecteurs d'ecran) mais
# masques visuellement pour ne pas les afficher deux fois.
#
# (d'ou les classes `sr-only` sur `<h1>E-MOTION</h1>` et sur le `.sub`)

# --- section de presentation des artistes, premiere `.figure` ---------------
#
# ancienne image de hero, redescendue ici (presentation des artistes)
#
# (il s'agit de `hero-iris-et-david-*`, qui n'est donc plus le fond du hero)
