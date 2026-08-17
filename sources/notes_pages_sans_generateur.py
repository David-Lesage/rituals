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

ETAT AU 17/08/2026 — LES 30 PAGES DU SITE ONT TOUTES UN GENERATEUR
------------------------------------------------------------------
Une seule page est ecrite A LA MAIN, et ce n'est pas une page du site : c'est
`/guso-facile/invitation`, une PAGE TECHNIQUE de passage. Sa note est en bas de
ce fichier. Les notes de `/e-motion`, qui etaient ici, sont parties dans
`sources/generate_emotion.py` le jour ou cette page a recu le sien.

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


===========================================================================
/guso-facile/invitation  —  guso-facile/invitation/index.html  (17/08/2026)
===========================================================================
PAGE ECRITE A LA MAIN, VOLONTAIREMENT. NE PAS LUI FABRIQUER DE GENERATEUR.

A QUOI ELLE SERT
----------------
Les liens d'invitation de Guso Facile ont la forme
`https://guso-facile.vercel.app/index.html#invite=<jeton>`. David veut qu'ils
portent l'adresse de l'association. Une redirection ne peut pas le faire :
MESURE EN PRODUCTION LE 17/08/2026, une redirection Vercel AVALE tout ce qui
suit le `#`.

    resonancesproductions.org/guso-facile/app#invite=XXXX  -> fragment PERDU
    guso-facile.vercel.app/index.html#invite=XXXX          -> fragment garde

Les invites seraient donc arrives SANS CODE, et l'invitation aurait echoue en
silence. D'ou cette page : elle lit `location.hash` en JavaScript et rebondit
vers l'application en RECOLLANT le fragment tel quel.

L'adresse a diffuser est : https://www.resonancesproductions.org/guso-facile/invitation#invite=<jeton>

CE QU'IL NE FAUT PAS « SIMPLIFIER »
-----------------------------------
* LE JETON RESTE DANS LE FRAGMENT, jamais en `?invite=`. Un fragment n'est pas
  envoye au serveur : il n'est donc ecrit dans aucun journal, ni dans aucun
  en-tete `Referer`. Le passer en parametre de requete marcherait avec une
  simple redirection — et exposerait le jeton partout. C'est un choix de
  confidentialite, pas un detail d'ecriture.
* `location.replace()`, PAS `location.href` : `replace` n'ecrit pas d'entree
  dans l'historique. Avec `href`, l'invite qui appuie sur « precedent » revient
  ici, et repart aussitot vers l'app : il est prisonnier d'un aller-retour.
* L'ADRESSE DE DEPART EST ECRITE EN DUR dans le script, et le fragment est
  seulement CONCATENE derriere. On ne construit donc jamais une destination a
  partir de ce que porte l'URL : impossible de detourner la page vers un autre
  site en fabriquant un faux lien.
* AUCUN JETON A L'ECRAN, et pas non plus dans le `href` du bouton de secours :
  il reste l'adresse nue de l'application. Consequence assumee, dite dans le
  `<noscript>` : sans JavaScript, le bouton ouvre bien l'application mais
  l'invitation n'est pas reconnue. C'est une limite du HTML, aucun lien ne peut
  recopier le fragment de la page courante sans JavaScript.

POURQUOI PAS DE GENERATEUR, ALORS QUE TOUT LE SITE EN A UN
-----------------------------------------------------------
Un generateur sert a deux choses sur ce projet : reposer le decor partage
(menu, pied de page, feuille de style commune) et empecher qu'une retouche a la
main soit effacee a la reconstruction suivante. Ni l'un ni l'autre ne s'applique
ici : cette page n'a ni menu ni pied de page — c'est voulu, on ne propose rien
d'autre a quelqu'un qui vient de recevoir une invitation —, et `build.py` ne la
touche jamais puisqu'elle n'est pas dans son tableau. Lui ecrire un generateur
ajouterait un script de plus a tenir pour trente lignes de HTML dont le seul
enjeu est le comportement du JavaScript.

CE QUI LA SURVEILLE QUAND MEME
-------------------------------
`sources/verif_site.py` la connait : voir `PAGES_TECHNIQUES` et le controle
`technique`. Il exige qu'elle existe, qu'elle porte `noindex,nofollow`, qu'elle
soit interdite dans `robots.txt`, absente de `sitemap.xml`, qu'elle rebondisse
bien par `location.replace` en recollant `location.hash`, et qu'aucune note de
redaction ne revienne dans son code. Elle n'est PAS comptee dans les 30 pages
publiees : ce n'est pas une page du site, c'est un aiguillage.

CE QUI NE SE TESTE PAS EN LOCAL
--------------------------------
Rien, en fait : contrairement a `/guso-facile/app` (une redirection de
`vercel.json`, que seule la plateforme lit), cette page est un vrai fichier.
`python3 -m http.server` la sert, et le rebond se verifie avec un faux jeton.
"""

# (aucune autre note en attente — voir la docstring ci-dessus)
