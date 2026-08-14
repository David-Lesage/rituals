# -*- coding: utf-8 -*-
"""Notes de redaction des pages QUI N'ONT PAS DE GENERATEUR.

Ce module n'execute rien et n'est importe par personne : c'est un porte-notes.

POURQUOI IL EXISTE
------------------
Les notes de redaction (« pourquoi cette photo est ici », « ne pas reintroduire
ceci », « David a dit que… ») vivaient en commentaires HTML dans les pages
livrees — donc lisibles par n'importe quel visiteur affichant le code source, et
indexables. Elles ont ete sorties du HTML (voir `sources/verif_commentaires.py`,
qui refuse maintenant qu'elles y reviennent).

Pour une page produite par un generateur, la note retourne DANS le generateur,
en commentaire Python `#`, juste au-dessus du code qui emet le bloc concerne.
Restait le cas des pages editees A LA MAIN, qui n'ont aucun code a elles : leurs
notes viennent ici.

ETAT AU 14/08/2026 — CE FICHIER EST VIDE, ET C'EST UNE BONNE NOUVELLE
---------------------------------------------------------------------
Les 9 pages publiees ont desormais TOUTES un generateur. Les notes de `/e-motion`,
qui etaient ici, sont parties dans `sources/generate_emotion.py` le jour ou cette
page a recu le sien.

  /                         sources/generate_assoc.py
  /rituals                  sources/generate_site.py
  /rituals-trio             sources/generate_trio.py
  /e-motion                 sources/generate_emotion.py
  /david-lesage-en-concert  sources/generate_concert_scene.py
  /concerts-david-lesage    sources/generate_concert_dl.py
  /le-nid                   sources/generate_agenda_nid.py
  /le-soin-soa              sources/generate_soin_soa.py
  /rythme-calebasse         sources/generate_rythme.py

Le tableau qui fait foi est celui de `sources/build.py` (`--liste` pour l'afficher) :
il dit aussi ou chaque script ecrit reellement, et derriere lesquels il faut
reposer le menu.

Les deux seuls dossiers sans generateur sont `/solune` et `/au-nid` — des pages
ORPHELINES, hors du site : absentes du plan du site, interdites dans robots.txt,
sans entree de menu. Leur suppression n'a jamais ete tranchee par David. Elles ne
contiennent aujourd'hui aucun commentaire HTML, donc aucune note a heberger ici.

QUAND FAUT-IL REVENIR ECRIRE DANS CE FICHIER ?
----------------------------------------------
Le jour ou une page sera modifiee A LA MAIN sans avoir de generateur — ce que
`python3 sources/build.py` signale explicitement, page par page, sous le titre
« PAGES SANS GENERATEUR ». Sa note se pose alors ici, sous un en-tete au nom de
la page, et surtout PAS en commentaire HTML dans la page livree.
"""

# (aucune note en attente — voir la docstring ci-dessus)
