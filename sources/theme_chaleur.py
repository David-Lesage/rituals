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

#: Couche commune. Doit etre concatenee EN FIN de la feuille de style de la
#: page (voir le mode d'emploi ci-dessus).
CSS = """
/* ===== couche chaleureuse commune (sources/theme_chaleur.py) =============
   Le degrade signature de /guso-facile, propage a tout le site. Par touches :
   filets, sur-titres, puces, bouton. Jamais en aplat de fond. */
:root{--coral:#e08a72;--plum2:#b3a2e4;
--grad:linear-gradient(95deg,var(--gold2),var(--gold) 32%,var(--coral) 66%,var(--plum2));
--grad-warm:linear-gradient(100deg,var(--gold2),var(--gold) 46%,var(--coral));
/* meme degrade, axe VERTICAL : pour les filets de 3 px places sur le cote
   d'une carte. Avec `--grad` (95deg) un filet haut de 200 px et large de 3
   affiche le degrade de biais — mesure a l'ecran, c'est du hasard, pas un
   choix. `--grad-v` le fait courir franchement de haut en bas. */
--grad-v:linear-gradient(180deg,var(--gold2),var(--gold) 30%,var(--coral) 66%,var(--plum2))}
/* trois lueurs fixes : c'est ce qui enleve le fond « noir de notice ».
   position:fixed + inset:0 -> aucun risque de debordement horizontal. */
body::before{content:'';position:fixed;inset:0;z-index:-1;pointer-events:none;background:radial-gradient(58vw 40vw at 10% -6%,rgba(216,178,90,.11),transparent 62%),radial-gradient(52vw 38vw at 100% 14%,rgba(224,138,114,.10),transparent 62%),radial-gradient(62vw 46vw at 46% 106%,rgba(143,122,209,.12),transparent 62%)}
/* texte peint au degrade (titres, sur-titres) */
.grad-t{width:fit-content;max-width:100%;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
/* soulignement degrade de 2 px sous un mot-cle */
.mark{background-image:var(--grad);background-repeat:no-repeat;background-size:100% 2px;background-position:0 100%;padding-bottom:3px}
.divider{height:2px;background:linear-gradient(90deg,transparent,rgba(216,178,90,.42) 16%,rgba(224,138,114,.5) 50%,rgba(179,162,228,.42) 84%,transparent)}
.kick{display:inline-block;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
/* boutons : le principal porte le degrade chaud, le fantome un filet dore */
.btn{border-radius:999px}
.btn:not(.ghost){background:var(--grad-warm);color:#1b1206;box-shadow:0 12px 30px -18px rgba(224,138,114,.55)}
.btn:not(.ghost):hover{box-shadow:0 18px 40px -16px rgba(224,138,114,.65)}
.btn.ghost{background:linear-gradient(180deg,rgba(255,255,255,.055),rgba(255,255,255,.02));border:1px solid rgba(240,209,138,.3);color:var(--gold2)}
.btn.ghost:hover{border-color:rgba(240,209,138,.55)}
/* contraste du pied de page : 3,8:1 -> 5,96:1 sur #08091a (seuil 4,5:1) */
.legal{color:#8b8ba6}
/* a l'impression, un texte peint au degrade sort blanc : on le rend a l'or */
@media print{.kick,.grad-t{-webkit-text-fill-color:var(--gold);color:var(--gold)}}
/* les pictogrammes en ligne (voir ICONES plus bas) */
.ic{width:23px;height:23px;display:block;flex:0 0 auto}
.tc-defs{position:absolute;width:0;height:0;overflow:hidden}
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
            '<stop offset="0" stop-color="#f0d18a"/>'
            '<stop offset=".42" stop-color="#d8b25a"/>'
            '<stop offset=".74" stop-color="#e08a72"/>'
            '<stop offset="1" stop-color="#b3a2e4"/>'
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
