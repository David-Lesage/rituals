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

`/solune` et `/au-nid` etaient les deux seuls dossiers sans generateur — des pages
ORPHELINES, hors du site : absentes du plan du site, sans entree de menu.
**David a tranche leur suppression le 17/08/2026.** Les dossiers n'existent plus.

Ce sont desormais des REDIRECTIONS 301 posees dans `vercel.json` :
`/solune` -> `/e-motion` et `/au-nid` -> `/le-nid` — les pages qui les
remplacaient deja dans les faits. On ne supprime pas une adresse sechement : un
lien externe ou un signet qui pointait dessus aurait rendu 404, alors qu'il
arrive maintenant sur la bonne page.

⚠️ Et leurs `Disallow:` ont ete RETIRES de `robots.txt`, volontairement. C'est
l'inverse de ce qu'on croit d'instinct : un `Disallow` empeche Google d'aller
VOIR l'adresse, donc de constater la redirection — le referencement gagne par
l'ancienne adresse serait perdu au lieu d'etre transfere a la nouvelle. Le
controle `plan` de `verif_site.py` refuse maintenant l'ecriture si l'un des trois
elements manque : dossier encore present, redirection absente, ou `Disallow`
remis (voir `SUPPRIMEES` dans ce fichier).

Il ne reste donc AUCUNE page sans generateur. Ce fichier n'heberge plus aucune
note — il garde son mode d'emploi ci-dessous pour le jour ou le cas se represente.

QUAND FAUT-IL REVENIR ECRIRE DANS CE FICHIER ?
----------------------------------------------
Le jour ou une page sera modifiee A LA MAIN sans avoir de generateur — ce que
`python3 sources/build.py` signale explicitement, page par page, sous le titre
« PAGES SANS GENERATEUR ». Sa note se pose alors ici, sous un en-tete au nom de
la page, et surtout PAS en commentaire HTML dans la page livree.
"""

# (aucune note en attente — voir la docstring ci-dessus)
