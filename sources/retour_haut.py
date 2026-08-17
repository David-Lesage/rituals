# -*- coding: utf-8 -*-
"""Le bouton « retour en haut » du site, en UN seul exemplaire.

POURQUOI CE FICHIER EXISTE
--------------------------
Le 17/08/2026, en mesurant `/guso-facile` (25 455 px de haut a 390 px, une
trentaine d'ecrans de telephone), le carnet de bord a rappele un constat
ancien : PLUSIEURS PAGES DU SITE DEPASSENT 12 000 px SANS AUCUN MOYEN DE
REMONTER. C'est le correctif le moins cher du site.

Or le bouton EXISTE DEJA — et il est recopie a l'identique dans CINQ
generateurs, chacun avec sa propre copie de la meme feuille de style, du meme
`<a>` et du meme script :

    generate_guso.py · generate_concert_scene.py · generate_concert_dl.py
    generate_rythme.py · generate_soin_soa.py

Cinq copies, c'est se garantir une divergence : une correction en repare une
sur cinq, et les quatre autres restent en l'etat sans que personne le voie.
C'est exactement ce qui est arrive a `.legal` (#6b6b80 -> #8b8ba6 corrige pour
29 pages, `/guso-facile` oubliee parce qu'elle porte sa propre copie de la
couche). D'ou ce module : UNE definition, N generateurs qui l'appellent. Meme
parti-pris que `sources/visionneuse.py` et `sources/theme_chaleur.py`.

⚠️ CE N'EST PAS UN GENERATEUR. Il n'ecrit aucune page, il ne s'execute pas
   seul, et il n'a donc pas de ligne dans `sources/build.py` (dont le controle
   « generateur non inscrit » ne regarde que les fichiers `generate_*.py`).

ETAT AU 17/08/2026 — QUI L'A, QUI NE L'A PAS
--------------------------------------------
L'ONT (5 pages)   : /guso-facile · /david-lesage-en-concert ·
                    /concerts-david-lesage · /rythme-calebasse · /le-soin-soa
NE L'ONT PAS      : / · /association · /rituals · /rituals-trio · /e-motion ·
                    /le-nid · les 18 articles + l'index de /guso-facile/blog
⚠️ Seul `/guso-facile` passe par ce module a ce jour : c'est le perimetre du
   chantier du 17/08/2026, decide comme tel. Poser le bouton sur les autres
   pages est une DECISION DE DAVID, pas un effet de bord d'un refactor.
   Ce qu'il faudra faire le jour ou il dit oui, page par page :
     1. `import retour_haut` dans le generateur concerne ;
     2. `+ retour_haut.css()` avant `</style>` — attention a l'ordre des
        feuilles quand la page importe `theme_chaleur` ;
     3. `+ retour_haut.html()` juste avant `<footer` ;
     4. `+ retour_haut.js()` avant `</body>` ;
     5. rebatir, verifier que la page ne bouge pas ailleurs, et mesurer.
   Pour les quatre generateurs qui ont deja leur copie, le remplacement doit
   etre prouve NEUTRE A L'OCTET (md5 de la page avant / apres), comme il l'a
   ete ici — sinon ce n'est plus un refactor, c'est une modification.

CE QU'IL DEMANDE A LA PAGE
--------------------------
Trois choses, toutes deja presentes sur les 30 pages :
  * `<body id="top">` — la cible du lien. Sans elle, le bouton ne mene nulle
    part et `verif_site.controle_liens()` le signale.
  * les variables CSS `--line` et `--gold2` (posees par la feuille de base de
    chaque page, ou par `theme_chaleur.py`) ;
  * un `z-index` libre a 35 : au-dessus du contenu, SOUS le menu (40) et sous
    le panneau du menu mobile (1001) et la visionneuse (1100). Ne pas le
    monter : le bouton passerait par-dessus le menu ouvert.

CE QU'IL NE FAIT PAS
--------------------
Il n'ajoute AUCUN comportement sans JavaScript : sans script, la classe `on`
n'est jamais posee, le bouton reste `opacity:0` + `visibility:hidden`, donc
invisible ET hors de l'ordre de tabulation. La page est exactement celle
d'avant. C'est la regle du site.

Il ne remplace pas le sommaire : le sommaire fait DESCENDRE vers un endroit
precis, ce bouton fait REMONTER d'ou qu'on soit. Les deux repondent a deux
gestes differents, et la page longue a besoin des deux.

LES MESURES QUI FIXENT LES VALEURS (17/08/2026, `/guso-facile`)
---------------------------------------------------------------
  * SEUIL 700 px : le bouton n'apparait qu'une fois le hero passe. Plus bas il
    s'afficherait alors que « remonter » ne veut encore rien dire ; plus haut
    il se ferait attendre sur une page qui compte 22 000 px.
  * CIBLE 46 px et non 44 : meme raison que les boutons de la visionneuse — a
    44 px pile, l'arrondi sous-pixel du navigateur rend 43,99 px, sous le
    seuil. Deux pixels de marge mettent la regle hors de doute.
  * IL NE MASQUE RIEN : pose en bas a droite a 18 px des bords, il ne recouvre
    aucun texte ni aucun bouton de `/guso-facile` — verifie en interrogeant le
    document (`elementFromPoint`) sous le bouton, a six hauteurs de defilement
    dont celle du formulaire et celle de son bouton « Envoyer ma demande ».
  * ATTEIGNABLE AU CLAVIER : c'est un vrai `<a href="#top">`. `visibility:
    hidden` le sort de l'ordre de tabulation tant qu'il est cache — donc il
    n'est jamais un arret de tabulation invisible, et il en devient un des
    qu'il se voit.
  * `aria-label` EXPLICITE ET EN FRANCAIS : « Revenir en haut de la page ». La
    fleche « ↑ » seule ne dit rien a un lecteur d'ecran.
"""

# --------------------------------------------------------------------------
# LA FEUILLE DE STYLE
# --------------------------------------------------------------------------
# ⚠️ CES TROIS REGLES SONT REPRISES A L'OCTET des cinq copies existantes. Le
#    module a ete introduit SANS RIEN CHANGER a ce qui etait publie : le md5 de
#    `guso-facile/index.html` est identique avant et apres l'extraction. Toute
#    amelioration (et il y en aura : la transition n'est pas encore gardee par
#    `prefers-reduced-motion`) se fera ENSUITE, ici, et profitera d'un coup a
#    toutes les pages qui appellent ce module — c'est tout l'interet.
_CSS = """/* retour en haut */
.totop{position:fixed;right:18px;bottom:18px;z-index:35;width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:rgba(25,27,61,.92);border:1px solid var(--line);color:var(--gold2);font-size:19px;opacity:0;visibility:hidden;transition:opacity .3s,visibility .3s,transform .2s}
.totop.on{opacity:1;visibility:visible}
.totop:hover{transform:translateY(-2px)}
"""

# --------------------------------------------------------------------------
# LE LIEN
# --------------------------------------------------------------------------
# ⚠️ UN `<a>`, JAMAIS UN `<button>`. Deux raisons, et la seconde est un
#    garde-fou reel :
#      - c'est une navigation vers une ancre, pas une commande : `<a href=
#        "#top">` marche meme si le script ne se charge pas, et il herite du
#        `scroll-behavior:smooth` de la page ;
#      - `/guso-facile` refuse a l'ecriture tout `<button>` hors du menu et du
#        formulaire (`_controle_maquettes()`), pour qu'un visiteur ne croie
#        jamais piloter l'outil depuis le site de l'association. Un bouton ici
#        ferait echouer la generation.
_HTML = '<a class="totop" href="#top" aria-label="Revenir en haut de la page">↑</a>\n'

# --------------------------------------------------------------------------
# LE SCRIPT
# --------------------------------------------------------------------------
# Quatre lignes, et rien de plus :
#   * `if(!b) return` — le script ne suppose pas que le lien est la ;
#   * `upd()` est appele UNE FOIS au chargement, avant meme le premier
#     defilement : une page rechargee au milieu (ancre, retour arriere,
#     restauration de position) doit montrer le bouton tout de suite ;
#   * `{passive:true}` sur `scroll` : l'ecouteur ne peut pas bloquer le
#     defilement, c'est ce qui garde le geste fluide sur telephone ;
#   * `classList.toggle(nom, condition)` fait les deux sens en une ligne — le
#     bouton disparait aussi quand on remonte.
_JS = """
<script>
(function(){
  var b=document.querySelector('.totop'); if(!b) return;
  function upd(){ b.classList.toggle('on', window.scrollY>700); }
  upd(); window.addEventListener('scroll',upd,{passive:true});
})();
</script>
"""


def css():
    """La feuille de style du bouton, a poser avant `</style>`."""
    return _CSS


def html():
    """Le lien lui-meme, a poser juste avant `<footer`."""
    return _HTML


def js():
    """Le script qui le fait apparaitre, a poser avant `</body>`."""
    return _JS
