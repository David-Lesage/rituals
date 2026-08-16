# -*- coding: utf-8 -*-
"""La couche « chaleureuse » du site, en UN seul exemplaire.

POURQUOI CE FICHIER EXISTE
--------------------------
Le 14/08/2026, `/guso-facile` a ete rechauffee : un degrade signature, des
formes douces, des halos. David a valide la direction et demande la meme chose
partout :

    « Ramener de la couleur prune, ca fait du bien. Resonances a besoin d'avoir
      une image classe mais aussi chaleureuse. Applique ce style a tout le site,
      pas seulement a la page Guso Facile. »

Les 9 autres pages ont chacune leur feuille de style, ecrite dans leur propre
generateur. Recopier la meme trentaine de declarations neuf fois, c'est se
garantir une divergence : une retouche du degrade en corrigerait huit sur neuf,
et la neuvieme resterait froide sans que personne le voie. D'ou ce module :
UNE definition, neuf generateurs qui l'appellent.

⚠️ CE N'EST PAS UN GENERATEUR. Il n'ecrit aucune page, il ne s'execute pas
   seul, et il n'a donc pas de ligne dans `sources/build.py` (dont le controle
   « generateur non inscrit » ne regarde que les fichiers `generate_*.py`).

COMMENT ON S'EN SERT
--------------------
Dans le generateur d'une page :

    import theme_chaleur
    CSS = CSS + theme_chaleur.CSS + CSS_CHALEUR_DE_LA_PAGE

La couche arrive donc EN DERNIER dans la feuille de style de la page : elle
surcharge sans qu'on ait a toucher une seule ligne existante. C'est voulu — une
refonte visuelle qui reecrit le CSS d'origine, c'est une refonte qui casse des
choses qu'on n'avait pas prevu de casser.
⚠️ Sauf `nav_menu.py` et `mobile_nav.py`, qui inserent leur CSS juste avant
   `</style>` et passent donc APRES. Verifie : ni l'un ni l'autre ne declare
   `.btn`, `.kick`, `.divider` ni `.legal`. Le menu garde sa pastille « Adherer »
   en or plein, comme sur `/guso-facile`.

LES REGLES QUI ONT TENU LA MAIN
-------------------------------
1. LA PRUNE REVIENT, mais en ACCENT SECONDAIRE (sur-titres, filets, puces,
   encadres), jamais en aplat. Des qu'il s'agit de TEXTE, c'est `--plum2`
   (#b3a2e4, 7,3:1 sur `--card`) et jamais `--plum` (#8f7ad1, 4,64:1 sur
   `--card` — tout juste au seuil). `--plum` reste aux aplats decoratifs.
2. « CLASSE » N'EST PAS NEGOCIABLE. Le site presente des spectacles et un lieu.
   Le degrade s'emploie PAR TOUCHES — un filet de 3 px, un sur-titre, une puce,
   un bouton — jamais en fond de section ni sur une grande surface. Une page
   bariolee serait un echec, pas une reussite a moitie.
3. AUCUN EMOJI. Regle du site et demande explicite de David : des icones
   « signature » dessinees en trait fin, jamais un pictogramme systeme.
4. PLANCHER TYPOGRAPHIQUE 13 px, contraste 4,5:1 pour le texte courant.

CE QUE LA COUCHE COMMUNE FAIT, ET RIEN D'AUTRE
----------------------------------------------
  * declare `--coral`, `--plum2`, `--grad` et `--grad-warm` (memes valeurs que
    `generate_guso.py`, au caractere pres — les deux fichiers doivent rester
    lisibles cote a cote) ;
  * pose les TROIS HALOS fixes en fond de page. C'est ce qui enleve le fond
    « noir de notice ». Par `body::before` en `position:fixed`, JAMAIS par un
    pseudo-element deborde qui creerait un debordement horizontal ;
  * repeint le `.divider` (1 px or -> 2 px or/corail/prune) ;
  * peint les sur-titres `.kick` au degrade ;
  * donne au bouton principal le degrade chaud et un rayon plein ;
  * ⚠️ CORRIGE LE CONTRASTE DU PIED DE PAGE : `.legal` etait a `#6b6b80` sur
    `#08091a`, soit 3,8:1 — sous le seuil de 4,5:1, sur les 10 pages. Passe a
    `#8b8ba6` (5,96:1), qui reste discret.

Le reste — filets de carte, puces en losange, encadres prune — depend des
classes de CHAQUE page et vit dans son generateur, juste apres cet import.
"""

# =========================================================================
# LA PALETTE — refonte du 16/08/2026
# =========================================================================
# David : « graphiquement, sa page reste vraiment mieux presentee », « la page
# du site est encore un peu trop sombre ». Les deux pages ont ete MESUREES
# avant de toucher a quoi que ce soit, et le diagnostic spontane etait faux :
# les deux FONDS sont quasi identiques (#0f1419 chez eux, #0e0f24 chez nous,
# luminances relatives 0,0067 et 0,0056). Ce n'est donc pas le fond.
#
# Ce qui differe, mesure :
#
#   1. LES COUCHES NE SE DETACHENT PAS. On appelle « ecart » le rapport des
#      luminances relatives WCAG entre le fond de page et la surface d'une
#      carte. Chez eux #0f1419 -> #1e2a38 = x3,30 : l'oeil voit une surface
#      posee sur un fond. Chez nous #0e0f24 -> #191b3d = x2,36 : tout
#      s'aplatit, et une carte a besoin de son filet pour exister.
#   2. LES ACCENTS SONT TIMIDES. Saturation HSV moyenne des accents : 44 %
#      chez nous, ~58 % chez eux. Notre prune claire etait a 28,9 % quand leur
#      rose est a 52,5 %.
#
# CE QU'ON LEUR PREND, ET CE QU'ON NE LEUR PREND PAS
# --------------------------------------------------
# On prend la METHODE — etager les surfaces, oser la vivacite. On ne prend
# NI leur cyan (#4cc9f0) NI leur rose (#f072c0) : le site presente des
# spectacles et un lieu, il reste bleu nuit / or / prune, et il reste premium.
#
# LES SURFACES, ETAGEES
# ---------------------
#   --night   #0e0f24  inchange — c'est le fond de page, il n'a jamais ete
#                      le probleme.
#   --night2  #141633 -> #161839   ecart x1,71 -> x1,99
#   --card    #191b3d -> #1e214a   ecart x2,36 -> x3,30
# Meme teinte (H=236-237), meme saturation : on ne fait que monter la clarte
# jusqu'a la cible. La cible x3,30 est exactement celle de leur page.
#
# LES ACCENTS, PLUS VIFS  (saturation HSV)
# ----------------------------------------
#   --gold    #d8b25a  INCHANGE — c'est l'accent PRIMAIRE, deja a 58,3 %, et
#                      c'est la signature du site. Le laisser tranquille garde
#                      aussi en phase les 133 litteraux `rgba(216,178,90,…)`
#                      (filets, halos, ombres) et `--line`, qui sont sa forme
#                      translucide. David a demande les accents SECONDAIRES.
#   --gold2   #f0d18a -> #f8d274   42,5 % -> 53,2 %
#   --plum    #8f7ad1 -> #9374e2   41,6 % -> 48,7 %  (decoratif seulement)
#   --plum2   #b3a2e4 -> #b38ff5   28,9 % -> 41,6 %
#   --coral   #e08a72 -> #ee8062   49,1 % -> 58,8 %
# Moyenne des cinq : 44,1 % -> 52,1 %.
#
# ⚠️ POURQUOI PAS 55 % PILE. Au-dela de ~42 % de saturation, la prune claire
#    quitte la prune et devient un violet fluo (#aa8cff, teste) : criard, et
#    en contradiction avec « premium ». La contrainte esthetique a prime sur
#    l'arrondi du chiffre. Le chemin le plus court vers 55 % aurait ete de
#    saturer `--gold`, mais c'est l'accent primaire et il desynchroniserait
#    les 133 litteraux ci-dessus.
#
# ⚠️ ECLAIRCIR UN FOND BAISSE LE CONTRASTE D'UN TEXTE CLAIR. Chaque paire a
#    ete RECALCULEE sur le NOUVEAU `--card`, jamais supposee :
#      --ink   12,56:1   --gold2 10,35:1   --plum2 6,71:1 (avant refonte)
#      --muted  6,52:1   --gold   7,61:1   --coral 5,87:1
#      .legal (#8b8ba6) 4,62:1 sur --card, 5,96:1 sur le pied de page #08091a
#    Aucun texte ne descend sous 4,5:1. `--plum` tombe a 4,28:1 : c'est la
#    raison pour laquelle il reste INTERDIT EN TEXTE (regle 1 ci-dessus),
#    verifie — `color:var(--plum)` n'existe nulle part dans le depot, ses six
#    emplois sont des bordures, un `conic-gradient` et un `box-shadow`.
#
# ⚠️ L'AGENDA DE /le-nid NE SUIT PAS. Ses six teintes d'evenement sont des
#    litteraux calibres sur l'ANCIEN `--card`, et `--c` sert de couleur de
#    TEXTE aux 20 boutons de billetterie. Les monter ferait passer « Workshop
#    rythme » sous 4,5:1. La liste d'agenda garde donc sa surface d'origine :
#    voir `generate_agenda_nid.py`, qui la reepingle explicitement.

#: Couche commune. Doit etre concatenee EN FIN de la feuille de style de la
#: page (voir le mode d'emploi ci-dessus).
#: ⚠️ Elle REDEFINIT `--night2`, `--card`, `--gold2` et `--plum` : ces quatre
#:    variables sont declarees dans le `:root` de chaque generateur, et cette
#:    couche arrive apres. Une seule ecriture commande donc les 30 pages.
CSS = """
/* ===== couche chaleureuse commune (sources/theme_chaleur.py) =============
   Le degrade signature de /guso-facile, propage a tout le site. Par touches :
   filets, sur-titres, puces, bouton. Jamais en aplat de fond. */
/* surfaces etagees : fond -> carte = x3,30 de luminance (x2,36 avant) */
:root{--night2:#161839;--card:#1e214a;
/* accents plus vifs — l'or primaire ne bouge pas */
--gold2:#f8d274;--plum:#9374e2;--coral:#ee8062;--plum2:#b38ff5;
--grad:linear-gradient(95deg,var(--gold2),var(--gold) 32%,var(--coral) 66%,var(--plum2));
--grad-warm:linear-gradient(100deg,var(--gold2),var(--gold) 46%,var(--coral));
/* meme degrade, axe VERTICAL : pour les filets de 3 px places sur le cote
   d'une carte. Avec `--grad` (95deg) un filet haut de 200 px et large de 3
   affiche le degrade de biais — mesure a l'ecran, c'est du hasard, pas un
   choix. `--grad-v` le fait courir franchement de haut en bas. */
--grad-v:linear-gradient(180deg,var(--gold2),var(--gold) 30%,var(--coral) 66%,var(--plum2))}
/* trois lueurs fixes : c'est ce qui enleve le fond « noir de notice ».
   position:fixed + inset:0 -> aucun risque de debordement horizontal. */
body::before{content:'';position:fixed;inset:0;z-index:-1;pointer-events:none;background:radial-gradient(58vw 40vw at 10% -6%,rgba(216,178,90,.11),transparent 62%),radial-gradient(52vw 38vw at 100% 14%,rgba(238,128,98,.10),transparent 62%),radial-gradient(62vw 46vw at 46% 106%,rgba(147,116,226,.12),transparent 62%)}
/* texte peint au degrade (titres, sur-titres) */
.grad-t{width:fit-content;max-width:100%;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
/* soulignement degrade de 2 px sous un mot-cle */
.mark{background-image:var(--grad);background-repeat:no-repeat;background-size:100% 2px;background-position:0 100%;padding-bottom:3px}
.divider{height:2px;background:linear-gradient(90deg,transparent,rgba(216,178,90,.42) 16%,rgba(238,128,98,.5) 50%,rgba(179,143,245,.42) 84%,transparent)}
.kick{display:inline-block;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
/* boutons : le principal porte le degrade chaud, le fantome un filet dore */
.btn{border-radius:999px}
.btn:not(.ghost){background:var(--grad-warm);color:#1b1206;box-shadow:0 12px 30px -18px rgba(238,128,98,.55)}
.btn:not(.ghost):hover{box-shadow:0 18px 40px -16px rgba(238,128,98,.65)}
.btn.ghost{background:linear-gradient(180deg,rgba(255,255,255,.055),rgba(255,255,255,.02));border:1px solid rgba(248,210,116,.3);color:var(--gold2)}
.btn.ghost:hover{border-color:rgba(248,210,116,.55)}
/* contraste du pied de page : 3,8:1 -> 5,96:1 sur #08091a (seuil 4,5:1) */
.legal{color:#8b8ba6}
/* a l'impression, un texte peint au degrade sort blanc : on le rend a l'or */
@media print{.kick,.grad-t{-webkit-text-fill-color:var(--gold);color:var(--gold)}}
/* les pictogrammes en ligne (voir ICONES plus bas) */
.ic{width:23px;height:23px;display:block;flex:0 0 auto}
.tc-defs{position:absolute;width:0;height:0;overflow:hidden}
"""


# =========================================================================
# LA DECLINAISON DES DEUX PAGES RITUALS — une seule ecriture
# =========================================================================
# `/rituals` et `/rituals-trio` sont deux pages jumelles : leurs feuilles de
# style (`sources/rituals_source.html` et `sources/trio_source.html`) ne
# different que de DEUX regles — `.jgal` et `.trio-badge`, propres au trio.
# Mesure faite : `diff` des deux blocs `<style>` = 2 lignes.
#
# Ecrire la declinaison chaleureuse deux fois, c'est exactement le scenario
# que ce module existe pour eviter : une retouche du filet du parcours en
# corrigerait une, et l'autre resterait froide sans que personne le voie. Les
# deux generateurs concatenent donc CETTE constante ; ce qui est propre au trio
# reste dans `generate_trio.py`, juste derriere.
#
# ⚠️ POURQUOI ON PEINT LES BORDURES au lieu d'ajouter des pseudo-elements :
#    `.card` s'anime au survol (`translateY(-4px)`) et un `::before` positionne
#    demanderait un `overflow:hidden` qui rognerait les coins arrondis. Peindre
#    la bordure (`background-image` cadre sur `border-box`) ne deplace rien.
# ⚠️ `--grad-v` (vertical) pour les filets de COTE, `--grad` (95deg) pour ceux
#    du HAUT : dans un filet haut de 200 px et large de 3, un degrade a 95deg
#    tombe de biais.
# ⚠️ LE CARROUSEL N'EST PAS TOUCHE : ni la largeur des diapos, ni `--ar`, ni le
#    `eager` des trois premieres. Seul le rayon de leurs coins change. Le
#    remede contre l'effondrement a 2 px doit rester intact.
CSS_RITUALS = """/* ===== RITUALS : declinaisons chaleureuses (15/08/2026) =====
   Communes a /rituals et /rituals-trio — ecrites UNE fois, dans
   sources/theme_chaleur.py, pour que les deux pages jumelles ne divergent pas. */
.hero h1{background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent;width:fit-content;max-width:100%;margin:0 auto}
.step .t,.spec .k{display:inline-block;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
/* les cartes numerotees : filet de tete au degrade + chiffre peint */
.card{border-top:3px solid transparent;border-radius:18px;background-image:var(--grad),linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,0)),linear-gradient(var(--card),var(--card));background-size:100% 3px,100% 100%,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box,padding-box}
.card:hover{border-color:transparent}
.card .n{display:inline-block;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
/* le fil du parcours : le trait vertical dore devient le degrade, et la pastille
   de chaque etape passe au degrade chaud */
.steps{border-left-color:transparent;background-image:var(--grad-v);background-repeat:no-repeat;background-size:2px 100%;background-position:0 0;background-origin:border-box}
.step:before{background:var(--grad-warm);box-shadow:0 0 0 5px rgba(238,128,98,.14)}
/* citations : le trait or plein de 3 px devient le degrade vertical */
.q{border-left-color:transparent;border-radius:14px;background-image:var(--grad-v),linear-gradient(var(--card),var(--card));background-size:3px 100%,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box}
/* les deux cartes « se programme en / s'inscrit dans » : filet de tete */
.scene-card{border-top:3px solid transparent;border-radius:18px;background-image:var(--grad),linear-gradient(var(--card),var(--card));background-size:100% 3px,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box}
/* la prune revient en accent de TEXTE (--plum2 : 8,6:1 sur --night) */
.artist .role{color:var(--plum2)}
/* le filet qui separe les artistes, et ceux de la fiche technique */
.artist,.spec div{border-top-color:transparent;background-image:linear-gradient(90deg,rgba(216,178,90,.42),rgba(238,128,98,.42) 55%,rgba(179,143,245,.38));background-repeat:no-repeat;background-size:100% 2px;background-position:0 0}
/* les deux boutons dores PLEINS qui ne portent pas la classe .btn : la couche
   commune ne les atteint pas, il faut les nommer */
.dlbtn,.car-play{background:var(--grad-warm);color:#1b1206;box-shadow:0 12px 30px -18px rgba(238,128,98,.55)}
.dlbtn:hover{box-shadow:0 18px 40px -16px rgba(238,128,98,.65)}
/* arrondis genereux — la LARGEUR des diapos n'est pas touchee */
.figure,.aphoto,picture.aphoto,.ask .item,.third,.tbl-wrap,.lb-frame{border-radius:18px}
.slide{border-radius:16px}
"""


# =========================================================================
# LES PICTOGRAMMES — des icones dessinees, JAMAIS un emoji
# =========================================================================
# Regle du site, et demande explicite de David : des icones « signature » en
# trait fin. Grille de 24, trait de 1,5, bouts et raccords arrondis — memes
# reglages que les dix pictogrammes de `/guso-facile`, pour que deux icones
# venues de deux pages se ressemblent.
#
# ⚠️ `gradientUnits="userSpaceOnUse"` et non le defaut `objectBoundingBox` :
#    sans cela chaque trace recevrait le degrade entier sur SA boite
#    englobante, et deux icones cote a cote ne seraient plus dans la meme
#    lumiere. Les couleurs sont ecrites en clair (un `stop-color` ne lit pas
#    les variables CSS de facon fiable) : ce sont exactement --gold2, --gold,
#    --coral et --plum2.
# ⚠️ La couleur ecrite APRES l'`url()` est le repli du paint server SVG 1.1 :
#    si le degrade n'etait pas resolu, l'icone reste doree au lieu de
#    disparaitre.
# ⚠️ L'identifiant `gf-ink` est CELUI DE `/guso-facile`, volontairement : une
#    page n'embarque jamais les deux definitions (chaque generateur pose la
#    sienne), et garder le meme nom evite qu'un copier-coller d'un fragment
#    d'une page a l'autre se retrouve sans degrade.

SVG_DEFS = ('<svg class="tc-defs" aria-hidden="true" focusable="false">'
            '<defs><linearGradient id="gf-ink" gradientUnits="userSpaceOnUse" '
            'x1="3" y1="4" x2="21" y2="20">'
            '<stop offset="0" stop-color="#f8d274"/>'
            '<stop offset=".42" stop-color="#d8b25a"/>'
            '<stop offset=".74" stop-color="#ee8062"/>'
            '<stop offset="1" stop-color="#b38ff5"/>'
            '</linearGradient></defs></svg>\n')

ICONES = {
    # remplace l'emoji ❤️ de /rythme-calebasse : le coeur, en trait, pas en
    # aplat rouge — c'est une page sombre et sobre.
    'coeur': '<path d="M12 20.3 4.9 13.2a4.6 4.6 0 0 1 6.5-6.5l.6.6.6-.6a4.6 4.6 0'
             ' 0 1 6.5 6.5Z"/>',
    # remplace l'emoji 🥁 de /rythme-calebasse. Ce n'est pas une batterie : la
    # calebasse se pose au sol et se joue a mains nues -> un dome, le sol, et
    # la main qui frappe au centre.
    'calebasse': '<path d="M4.7 16.3a7.3 7.3 0 0 1 14.6 0"/><path d="M2.9 16.3h18.2"/>'
                 '<path d="M9.5 16.3a2.5 2.5 0 0 1 5 0"/>'
                 '<path d="M6.1 6.6c-.9.8-1.5 1.9-1.7 3.1"/>'
                 '<path d="M17.9 6.6c.9.8 1.5 1.9 1.7 3.1"/>',
    # Ajoutees le 15/08/2026 pour /association (identification, adresses). Meme
    # grille de 24 et meme trait de 1,5 que les precedentes : deux icones venues
    # de deux pages doivent se ressembler.
    # Un feuillet corne : les identifiants officiels (RNA, SIRET, code APE).
    'document': '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8Z"/>'
                '<path d="M14 3v5h5"/><path d="M9 13h6"/><path d="M9 17h4"/>',
    # Un reperage de carte : le siege social et l'adresse de correspondance.
    'lieu': '<path d="M12 21s7-5.7 7-11a7 7 0 1 0-14 0c0 5.3 7 11 7 11Z"/>'
            '<circle cx="12" cy="10" r="2.6"/>',
}


def ic(nom, classe='ic'):
    """Une icone en ligne, DECORATIVE : le texte qu'elle accompagne suffit.

    `aria-hidden` + `focusable="false"` : elle double un texte deja present,
    l'enoncer une seconde fois serait du bruit, et sans `focusable` d'anciens
    moteurs l'inserent dans l'ordre de tabulation.
    """
    return ('<svg class="%s" viewBox="0 0 24 24" fill="none" '
            'stroke="url(#gf-ink) #e3bd7c" stroke-width="1.5" '
            'stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true" focusable="false">%s</svg>' % (classe, ICONES[nom]))
