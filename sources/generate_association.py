# -*- coding: utf-8 -*-
"""Generateur de la page /association (Resonances Productions).

Ecrit `association/index.html`. Aucune image, aucune iframe, aucun script de
page, aucune ressource externe en dehors de la feuille de polices deja chargee
par les 29 autres pages.

    python3 sources/generate_association.py     (depuis la racine du depot)

------------------------------------------------------------------------------
POURQUOI CETTE PAGE EXISTE  (decision de David, 15/08/2026)
------------------------------------------------------------------------------
Il a remarque que « Accueil » et « L’association » menaient tous les deux a la
page d'accueil — le second vers l'ancre `/#association`. Doublon confirme dans
le menu.

Le vrai probleme etait derriere : LA PAGE D'ACCUEIL FAISAIT CINQ METIERS. Elle
portait `#association`, `#statuts`, `#adherer`, `#contact` et `#prestations`, en
plus de presenter les six cartes de spectacles. Le raccourci de menu n'etait que
le symptome. David a choisi la solution de fond : une vraie page.

Ce qui a DEMENAGE de l'accueil vers ici :
  * le deuxieme paragraphe de l'objet (supports et moyens de l'association) ;
  * TOUTE la section « Cadre legal · Les statuts » : les deux articles, le
    renvoi au Journal officiel avec le n° RNA, le lien vers le document des
    statuts et la fiche de l'annuaire des entreprises (data.gouv.fr).

Ce qui RESTE sur l'accueil :
  * une presentation courte (le premier paragraphe de l'objet, inchange) suivie
    d'un bouton « En savoir plus sur l’association » ;
  * les quatre engagements, la section « Adhesion » (`#adherer`), les
    prestations (`#prestations`) et le pied de page (`#contact`).

⚠️ AUCUNE PHRASE N'A ETE REECRITE AU PASSAGE. Les textes partages vivent
   desormais dans `sources/textes_association.py`, importe PAR LES DEUX
   generateurs : une correction de David n'a donc qu'un endroit ou se faire.

------------------------------------------------------------------------------
LES ANCRES — pourquoi celle des statuts est la seule a bouger
------------------------------------------------------------------------------
Une redirection `vercel.json` ne peut RIEN pour un lien interne : `/#statuts`
ecrit dans une page n'est jamais une requete vers `/statuts`, c'est une requete
vers `/` suivie d'un saut cote navigateur. Rediriger n'aurait donc repare que
les URL tapees a la main. Le choix retenu, ancre par ancre :

  `/#association`  RESTE sur l'accueil — le bloc court y est toujours, et c'est
                   la cible historique de dizaines de liens (le menu de chaque
                   page la portait jusqu'a `resonances-3`).
  `/#adherer`      RESTE sur l'accueil : la section « Adhesion » n'a pas bouge.
                   `/association#adherer` existe EN PLUS, sur cette page-ci.
  `/#contact`      RESTE : c'est le pied de page, present sur les 30 pages.
  `/#prestations`  RESTE : les six cartes n'ont pas bouge.
  `/#statuts`      DISPARAIT de l'accueil, puisque la section demenage. Mesure
                   faite avant de trancher : AUCUNE page du site ne pointait
                   vers `/#statuts` dans son corps de texte (seuls subsistaient
                   trois selecteurs CSS `.nav .links a[href="/#statuts"]`,
                   vestiges d'un menu remplace depuis). Le seul renvoi reel
                   etait la redirection `/statuts` de `vercel.json` : elle vise
                   maintenant `/association#statuts`.

------------------------------------------------------------------------------
CE QUE LE GENERATEUR REFUSE D'ECRIRE  (garde-fous, voir `_controles`)
------------------------------------------------------------------------------
Meme parti-pris que `generate_rythme.py` et `generate_guso.py` : on ABANDONNE
l'ecriture plutot que d'imprimer un avertissement qui defile. Sont refuses : une
ancre manquante ou dupliquee, un `target="_blank"` sans `rel="noopener"`, un
hote externe hors liste, une iframe ou un script distant, un texte sous 13 px,
une balise de verification Google (elle n'a le droit d'exister QUE sur
l'accueil), un commentaire HTML de travail, un emoji.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mobile_nav            # hamburger mobile              # noqa: E402
import nav_menu              # menu de navigation partage    # noqa: E402
import textes_association as T   # les textes, partages avec l'accueil  # noqa: E402
import theme_chaleur         # couche chaleureuse commune    # noqa: E402
import verif_commentaires    # garde-fou commentaires HTML   # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, 'association')
OUT_HTML = os.path.join(OUT_DIR, 'index.html')

# Le bouton « Adherer » du menu partage et celui de cette page doivent mener au
# meme endroit. Les deux constantes vivent dans deux fichiers pour de bonnes
# raisons (nav_menu ne doit dependre d'aucun texte de page) ; on verifie donc
# qu'elles n'ont pas diverge, plutot que de l'esperer.
assert T.HELLOASSO == nav_menu.ADHESION, (
    'l’URL d’adhesion de textes_association.py a diverge de nav_menu.ADHESION')


# =========================================================================
# LE GABARIT
# =========================================================================
# Le squelette (head, variables de couleur, barre de navigation, boutons, pied
# de page) est celui des 29 autres pages, repris de `generate_guso.py`. Une
# seule difference, assumee : le bouton « retour en haut » (`.totop`) n'est pas
# la, parce qu'il demande du JavaScript de page et que cette page n'en embarque
# aucun. Son CSS n'a donc pas ete recopie non plus — une regle qui ne s'applique
# a rien est un piege pour la prochaine session.
#
# ⚠️ Les deux <link> vers fonts.googleapis.com sont ceux des 29 autres pages :
#    c'est exactement la meme feuille, deja chargee partout. Sans elle,
#    Cormorant Garamond et Jost tombent sur Georgia / system-ui et la page ne
#    ressemble plus au site.
#
# ⚠️ AUCUNE BALISE `google-site-verification` ICI. Le code fourni par David
#    verifie la propriete « prefixe d'URL » et n'a besoin d'etre pose QU'UNE
#    fois, sur `/`. Le repeter sur 30 pages n'apporte rien et brouille la piste
#    le jour ou il faudra le retirer. `_controles` refuse d'ecrire s'il apparait.

HEAD = """<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>L’association — Résonances Productions (loi 1901)</title>
<meta name="description" content="Résonances Productions, association loi 1901 : son objet, ses valeurs, ses statuts, ses mentions légales, ses adresses, l’adhésion et le contact.">
<meta property="og:title" content="L’association — Résonances Productions">
<meta property="og:description" content="Objet, valeurs, statuts, mentions légales, adresses, adhésion et contact de l’association Résonances Productions (loi 1901).">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.resonancesproductions.org/association">
<meta property="og:image" content="https://www.resonancesproductions.org/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://www.resonancesproductions.org/association">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0e0f24">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
"""

# --- le squelette commun du site (identique aux 29 autres pages) -----------
CSS_BASE = """:root{--night:#0e0f24;--night2:#141633;--ink:#eae7f3;--muted:#a9a6c4;--gold:#d8b25a;--gold2:#f0d18a;--plum:#8f7ad1;--card:#191b3d;--line:rgba(216,178,90,.26)}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--night);color:var(--ink);font-family:'Jost',-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.75;font-size:17px;-webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2,h3,h4,.serif{font-family:'Cormorant Garamond',Georgia,serif}
a{color:inherit;text-decoration:none}
.wrap{max-width:1080px;margin:0 auto;padding:0 26px}
.kick{letter-spacing:.32em;text-transform:uppercase;font-size:13px;font-weight:600;color:var(--gold);margin-bottom:14px}
section{padding:78px 0;position:relative}
.sec-title{font-size:clamp(30px,5vw,50px);font-weight:600;line-height:1.08;color:#fff}
.lead{font-size:19px;color:var(--muted);max-width:760px;margin-top:16px}
p.body{max-width:820px;color:#d7d4ea;margin-top:16px}
b{color:#fff;font-weight:500}
.divider{height:1px;background:linear-gradient(90deg,transparent,var(--line),transparent);max-width:1080px;margin:0 auto}
/* nav */
.nav{position:fixed;top:0;left:0;right:0;z-index:40;display:flex;align-items:center;justify-content:space-between;padding:16px 26px;background:rgba(14,15,36,.6);backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.05)}
.nav .brand{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:19px;letter-spacing:.12em;color:#fff;text-transform:uppercase}
.nav .links{display:flex;align-items:center;gap:19px;font-size:13.5px;letter-spacing:.04em}
.nav .links a{color:var(--muted);transition:color .2s}
.nav .links a:hover{color:var(--gold2)}
.nav .adh{color:#1a1608!important;background:var(--gold);padding:8px 16px;border-radius:30px;font-weight:600}
@media(max-width:760px){.nav .links a:not(.adh){display:none}}
@media(min-width:861px) and (max-width:1080px){.nav{padding:16px 18px}.nav .brand{font-size:17px;white-space:nowrap}.nav .links{gap:9px;font-size:13px}.nav .adh{padding:8px 13px}}
.nav .links a[aria-current="page"]{color:var(--gold2)}
.btn{display:inline-flex;align-items:center;gap:8px;background:var(--gold);color:#1a1608;font-weight:600;padding:14px 26px;border-radius:40px;font-size:15px;transition:transform .2s,box-shadow .2s}
.btn:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(216,178,90,.28)}
.btn.ghost{background:transparent;color:var(--gold2);border:1px solid var(--line)}
.cta{display:flex;gap:14px;flex-wrap:wrap}
/* focus clavier visible (accessibilite) */
:focus-visible{outline:2px solid var(--gold2);outline-offset:2px;border-radius:4px}
footer{background:#08091a;padding:70px 0 56px;border-top:1px solid var(--line)}
.fgrid{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:34px}
footer h4{font-family:'Cormorant Garamond',serif;color:#fff;font-size:22px;font-weight:600;margin-bottom:10px}
footer p,footer a{color:var(--muted);font-size:16px}
footer a{display:inline-block;padding:13px 0;line-height:1.3}
footer a.btn,footer a.adh{padding:14px 30px}
footer a:hover{color:var(--gold2)}
footer a:not(.btn):not(.adh){text-decoration:underline;text-decoration-color:rgba(216,178,90,.35);text-underline-offset:3px}
.fbrand{letter-spacing:.12em;text-transform:uppercase;color:var(--gold2);font-family:'Cormorant Garamond',serif;font-size:20px;font-weight:600}
.legal{margin-top:40px;text-align:center;color:#6b6b80;font-size:13px}
@media(max-width:760px){.fgrid{grid-template-columns:1fr;gap:24px}section{padding:60px 0}}
p a:not(.btn):not(.adh){text-decoration:underline;text-decoration-color:rgba(216,178,90,.4);text-underline-offset:3px}
"""

# --- CSS propre a la page --------------------------------------------------
# La chaleur vient de `theme_chaleur.CSS`, concatene juste avant : degrade
# signature, halos de fond, `.divider` de 2 px, `.kick` peint, boutons. On ne
# redeclare RIEN de tout cela ici — seulement les classes que cette page
# invente.
#
# ⚠️ TOUTES LES GRILLES SONT EN `minmax(min(Xpx,100%),1fr)`. Un `minmax(280px,
#    1fr)` sec impose une piste de 280 px meme dans un conteneur de 260 px : la
#    page deborde alors horizontalement a 390 px, et `body{overflow-x:hidden}`
#    masque le symptome sans regler la cause. Le `min(...,100%)` laisse la piste
#    se retracter.
# ⚠️ Rien sous 13 px (plancher typographique du site, verifie par `_controles`).
# ⚠️ Contrastes : `--muted` (#a9a6c4) = 8,0:1 sur `--night`, 7,1:1 sur `--card` ;
#    `--gold2` (#f0d18a) = 11,5:1 sur `--night`. Le corps des encadres est a
#    #d3d0e8. Aucun texte courant ne descend sous 4,5:1.
CSS_PAGE = """/* ===== L’association ===== */
/* --- l'entete : sobre, pas un hero plein ecran. C'est une page de reference,
   on doit arriver au premier paragraphe sans faire defiler. --- */
.ass-top{padding:142px 0 26px;position:relative}
.ass-top h1{font-size:clamp(38px,7.4vw,74px);font-weight:600;line-height:1.04;letter-spacing:.02em}
.ass-top .tag{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(19px,3.2vw,28px);margin-top:6px}
/* --- le sommaire : cinq pastilles, cible tactile de 44 px --- */
.somm{display:flex;flex-wrap:wrap;gap:10px;margin:30px 0 0;padding:0;list-style:none}
.somm li{display:flex}
.somm a{display:inline-flex;align-items:center;min-height:44px;padding:9px 17px;border-radius:999px;border:1px solid rgba(240,209,138,.3);background:linear-gradient(180deg,rgba(255,255,255,.055),rgba(255,255,255,.02));color:var(--gold2);font-size:14.5px;line-height:1.3;transition:border-color .2s}
.somm a:hover{border-color:rgba(240,209,138,.6)}
/* --- les quatre valeurs : filet de tete au degrade (meme geste que l'accueil) --- */
.vals{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(230px,100%),1fr));gap:20px;margin-top:40px}
.val{border-top:2px solid transparent;padding-top:16px;background-image:linear-gradient(90deg,rgba(216,178,90,.5),rgba(224,138,114,.5) 55%,rgba(179,162,228,.45));background-repeat:no-repeat;background-size:100% 2px;background-position:0 0}
.val h3{font-size:21px;font-weight:600;color:var(--plum2)}
.val p{color:var(--muted);font-size:15px;margin-top:6px}
/* --- l'encadre des statuts : repris de l'accueil, coins genereux --- */
.box{margin-top:34px;background:var(--card);border:1px solid rgba(255,255,255,.07);border-radius:18px;padding:28px;max-width:900px}
.box p{color:#d3d0e8;margin-bottom:14px}
.art{display:inline-block;font-size:13px;letter-spacing:.12em;text-transform:uppercase;font-weight:600;margin-bottom:4px;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
/* le trait dore plein des renvois devient le degrade vertical */
.jo{color:var(--muted);font-size:15px;border-left:3px solid transparent;padding-left:16px;margin-top:18px;background-image:var(--grad-v);background-repeat:no-repeat;background-size:3px 100%;background-position:0 0;background-origin:border-box}
.jo:last-child{margin-bottom:0}
.jo a{font-size:15px;display:inline-block;padding:6px 0;text-decoration:underline;text-decoration-color:rgba(216,178,90,.45);text-underline-offset:3px}
.jo a:hover{text-decoration-color:var(--gold2)}
/* --- les mentions legales : deux cartes a filet de tete --- */
.mgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr));gap:20px;margin-top:38px}
.mcard{border-top:3px solid transparent;border-radius:18px;padding:26px 26px 22px;background-image:var(--grad),linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,0)),linear-gradient(var(--card),var(--card));background-size:100% 3px,100% 100%,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box,padding-box}
.mcard h3{display:flex;align-items:center;gap:11px;font-size:23px;font-weight:600;color:#fff;margin-bottom:14px}
.mcard dl{margin:0}
.mcard dt{font-size:13px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--gold);margin-top:16px}
.mcard dt:first-of-type{margin-top:0}
.mcard dd{margin:3px 0 0;color:#d3d0e8;font-size:16px;line-height:1.6}
.mcard dd a{text-decoration:underline;text-decoration-color:rgba(216,178,90,.4);text-underline-offset:3px}
.mcard dd a:hover{color:var(--gold2)}
/* --- adhesion & contact --- */
.adh-sec{text-align:center;background:radial-gradient(800px 460px at 50% 40%,rgba(216,178,90,.12),transparent 65%),#0b0c1e}
.adh-sec .big{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(24px,3.6vw,38px);color:#fff;font-weight:500;max-width:760px;margin:18px auto 0;line-height:1.25}
.adh-sec .cta{justify-content:center;margin-top:30px}
.adh-sec .kick{margin-bottom:0}
@media(max-width:760px){.ass-top{padding:118px 0 18px}.mcard{padding:22px 20px 18px}.box{padding:22px}}
"""


# =========================================================================
# LES MORCEAUX DE PAGE
# =========================================================================

#: le sommaire. (ancre, libelle). Chaque ancre DOIT exister plus bas — c'est
#: verifie avant l'ecriture, ancre par ancre.
SOMMAIRE = (
    ('objet', 'L’objet'),
    ('valeurs', 'Les valeurs'),
    ('statuts', 'Les statuts'),
    ('mentions', 'Mentions légales'),
    ('adherer', 'Adhérer'),
)


def _sommaire():
    return ''.join('    <li><a href="#%s">%s</a></li>\n' % (a, l)
                   for a, l in SOMMAIRE)


def _valeurs():
    return ''.join('    <div class="val"><h3>%s</h3><p>%s</p></div>\n' % (h, p)
                   for h, p in T.VALS)


def _mentions():
    return ''.join('      <dt>%s</dt><dd>%s</dd>\n' % (k, v) for k, v in T.MENTIONS)


def build_html():
    """Construit la page complete (sans le menu : il est injecte apres)."""
    B = []
    A = B.append

    A(HEAD)
    A(CSS_BASE)
    A(theme_chaleur.CSS)
    A(CSS_PAGE)
    # `mobile_nav.inject()` et `nav_menu.inject()` collent leur CSS en
    # remplacant la PREMIERE occurrence de `</style>` : rien ne doit
    # s'intercaler entre le CSS de la page et cette balise.
    A('</style>\n')
    A('</head>\n')
    A('<body id="top">\n')

    # --- barre de navigation ---------------------------------------------
    # GABARIT MINIMAL : `nav_menu.inject()` remplace ce <div class="links"> par
    # le menu partage des 30 pages. Ne pas y ecrire les entrees a la main.
    A("""
<nav class="nav">
  <a href="/" class="brand">Résonances Productions</a>
  <div class="links">
    <a href="/">Accueil</a>
  </div>
</nav>
""")

    # les definitions du degrade des pictogrammes, une seule fois par page
    A(theme_chaleur.SVG_DEFS)

    # `<main>` enveloppe tout le contenu editorial ; le menu et le pied de page
    # restent dehors — c'est tout son interet pour un lecteur d'ecran.
    A('<main>\n')

    # =====================================================================
    # ENTETE
    # =====================================================================
    # Le <h1> dit ce qu'est la page, pas le nom du site : celui-ci est deja
    # dans la barre, dans le <title> et dans le pied de page. « L’association »
    # est aussi le libelle de l'entree de menu qui mene ici — un visiteur doit
    # retrouver le mot sur lequel il a clique.
    A("""
<header class="ass-top"><div class="wrap">
  <p class="kick">Association loi 1901 · Art du spectacle vivant</p>
  <h1 class="grad-t">L’association</h1>
  <p class="tag">l’humain · la vibration</p>
  <p class="lead">Qui nous sommes, ce que disent nos statuts, où nous écrire — et
    comment nous rejoindre.</p>
  <ul class="somm">
""")
    A(_sommaire())
    A("""  </ul>
</div></header>

<div class="divider"></div>
""")

    # =====================================================================
    # L'OBJET  —  le premier paragraphe est aussi celui de l'accueil, le
    #             second a quitte l'accueil pour venir ici.
    # =====================================================================
    A("""
<section id="objet"><div class="wrap">
  <p class="kick">L’objet</p>
  <h2 class="sec-title">%s</h2>
  <p class="body">%s</p>
  <p class="body">%s</p>
</div></section>

<div class="divider"></div>
""" % (T.OBJET_TITRE, T.OBJET_P1, T.OBJET_P2))

    # =====================================================================
    # LES VALEURS  —  les quatre « engagements » de l'accueil, mot pour mot.
    # =====================================================================
    A("""
<section id="valeurs"><div class="wrap">
  <p class="kick">Nos engagements</p>
  <h2 class="sec-title">Ce qui nous anime</h2>
  <div class="vals">
""")
    A(_valeurs())
    A("""  </div>
</div></section>

<div class="divider"></div>
""")

    # =====================================================================
    # LES STATUTS  —  bloc DEMENAGE de l'accueil, a l'identique.
    # =====================================================================
    # ⚠️ L'article 2 est une CITATION du document depose : guillemets compris,
    #    orthographe du document comprise. Ne pas la « corriger ».
    A("""
<section id="statuts"><div class="wrap">
  <p class="kick">Cadre légal</p>
  <h2 class="sec-title">Les statuts</h2>
  <div class="box">
    <p class="art">%s</p>
    <p>%s</p>
    <p class="art">%s</p>
    <p>%s</p>
    <p class="jo">%s</p>
    <p class="jo">%s</p>
    <p class="jo">%s</p>
  </div>
</div></section>

<div class="divider"></div>
""" % (T.STATUTS_ART1_TITRE, T.STATUTS_ART1,
       T.STATUTS_ART2_TITRE, T.STATUTS_ART2,
       T.STATUTS_JO, T.STATUTS_LIEN_DOC, T.STATUTS_LIEN_DATAGOUV))

    # =====================================================================
    # LES MENTIONS LEGALES
    # =====================================================================
    # Deux cartes plutot qu'une liste a rallonge : les IDENTIFIANTS d'un cote,
    # les ADRESSES de l'autre. C'est la question que se pose vraiment un
    # visiteur — « a qui j'ai affaire » / « ou j'ecris ».
    # ⚠️ Le siege social (Ariege) et l'adresse de correspondance (Paris 20e)
    #    sont bien DEUX adresses differentes : voir textes_association.py.
    A("""
<section id="mentions"><div class="wrap">
  <p class="kick">Mentions légales</p>
  <h2 class="sec-title">L’association, officiellement</h2>
  <p class="lead">Les informations d’identification de Résonances Productions,
    telles qu’elles figurent au registre national des associations et à
    l’annuaire des entreprises.</p>
  <div class="mgrid">
    <div class="mcard">
      <h3>%s<span>Identification</span></h3>
      <dl>
""" % theme_chaleur.ic('document'))
    A(_mentions())
    A("""      </dl>
    </div>
    <div class="mcard">
      <h3>%s<span>Adresses</span></h3>
      <dl>
        <dt>Siège social</dt><dd>%s</dd>
        <dt>Adresse de correspondance</dt><dd>%s</dd>
        <dt>Courriel</dt><dd><a href="mailto:%s">%s</a></dd>
      </dl>
    </div>
  </div>
</div></section>

<div class="divider"></div>
""" % (theme_chaleur.ic('lieu'),
       '<br>'.join(T.SIEGE_LIGNES),
       '<br>'.join(T.CORRESPONDANCE_LIGNES),
       T.EMAIL, T.EMAIL))

    # =====================================================================
    # ADHESION & CONTACT
    # =====================================================================
    # L'ancre `#adherer` existe AUSSI sur l'accueil, qui a garde sa section
    # « Adhesion » : ce sont deux pages differentes, il n'y a pas de conflit
    # d'identifiant. `/#adherer` et `/association#adherer` menent tous les deux
    # a un endroit ou l'on peut adherer — c'est le resultat voulu.
    A("""
<section class="adh-sec" id="adherer"><div class="wrap">
  <p class="kick">Adhésion &amp; contact</p>
  <p class="big">%s</p>
  <div class="cta">
    <a class="btn" href="%s" target="_blank" rel="noopener">Adhérer sur HelloAsso</a>
    <a class="btn ghost" href="mailto:%s">Écrire à l’association</a>
  </div>
</div></section>
""" % (T.ADHESION_ACCROCHE, T.HELLOASSO, T.EMAIL))

    A('</main>\n')

    # =====================================================================
    # PIED DE PAGE  —  celui des 29 autres pages, porteur de `#contact`.
    # =====================================================================
    A("""
<footer id="contact"><div class="wrap">
  <div class="fgrid">
    <div>
      <div class="fbrand">Résonances Productions</div>
      <p style="margin-top:8px">Association loi 1901 — Art du spectacle vivant.<br>« l’humain, la vibration »</p>
    </div>
    <div>
      <h4>Contact</h4>
      <p><a href="mailto:%s">%s</a></p>
      <p><b>Siège social</b><br>%s</p>
      <p><b>Adresse de correspondance</b><br>%s</p>
      <p style="margin-top:8px"><a href="https://www.facebook.com/resonancesproductions" target="_blank" rel="noopener">Facebook</a></p>
    </div>
    <div>
      <h4>Informations</h4>
      <p>SIRET : 919 514 075 00010</p>
      <p>Code APE : 9001Z<br>Arts du spectacle vivant</p>
      <p style="margin-top:8px"><a href="%s" target="_blank" rel="noopener">Adhérer / soutenir</a></p>
      <p style="margin-top:8px"><a href="%s" target="_blank" rel="noopener">Statuts de l’association</a></p>
    </div>
  </div>
  <div class="legal">© 2026 Résonances Productions · resonancesproductions.org</div>
</div></footer>

</body></html>""" % (T.EMAIL, T.EMAIL,
                     '<br>'.join(T.SIEGE_LIGNES),
                     '<br>'.join(T.CORRESPONDANCE_LIGNES),
                     T.HELLOASSO, T.URL_STATUTS_DOC))

    return ''.join(B)


# =========================================================================
# LES GARDE-FOUS  —  on REFUSE d'ecrire, on n'avertit pas
# =========================================================================

#: (marqueur, nombre attendu, ce que c'est). Un ecart attrape aussi bien une
#: disparition qu'une duplication — le piege historique de ce projet (quatre
#: entrees « Agenda », quatre cartes identiques).
ANCRES = (
    ('<h1', 1, 'titre principal de la page'),
    # version LUE dans nav_menu : ce garde-fou ne doit pas devenir faux le jour
    # ou NAV_VERSION est incrementee.
    ('data-nav="%s"' % nav_menu.NAV_VERSION, 1, 'menu partage nav_menu.py'),
    ('href="/association"', 1, 'entree « L’association » du menu partage'),
    ('id="objet"', 1, 'section « L’objet »'),
    ('id="valeurs"', 1, 'section « Nos engagements »'),
    ('id="statuts"', 1, 'section « Les statuts »'),
    ('id="mentions"', 1, 'section « Mentions légales »'),
    ('id="adherer"', 1, 'section « Adhésion & contact »'),
    ('id="contact"', 1, 'pied de page / ancre Contact'),
    ('class="val"', len(T.VALS), 'les valeurs de l’association'),
    ('class="mcard"', 2, 'les deux cartes de mentions légales'),
    ('class="jo"', 3, 'les trois renvois officiels (JOAFE, statuts, data.gouv)'),
    # le hamburger est cree en JS par mobile_nav.py : c'est son CSS qui atteste
    # sa presence. `.burger span{` n'existe qu'une fois (`.burger{` apparait
    # trois fois : regle de base + media 860 + media print).
    ('.burger span{', 1, 'CSS du hamburger (mobile_nav.py)'),
    # ⚠️ CES TROIS COMPTES SONT A 2, ET C'EST NORMAL — ils ont ete MESURES, pas
    #    devines. Le n° RNA figure dans le renvoi au Journal officiel (ou il est
    #    cite) ET dans la carte d'identification. Le SIRET et le code APE
    #    figurent dans la carte d'identification ET dans le pied de page, qui
    #    est celui des 29 autres pages du site et les affiche partout depuis le
    #    04/08/2026. Si l'un de ces comptes tombe a 1, c'est qu'une mention a
    #    disparu ; s'il monte a 3, qu'un bloc a ete recopie.
    ('W092002501', 2, 'n° RNA (renvoi au JO + carte d’identification)'),
    ('919 514 075 00010', 2, 'SIRET (carte d’identification + pied de page)'),
    ('9001Z', 2, 'code APE (carte d’identification + pied de page)'),
    ('<svg', 3, 'le bloc de definitions du degrade + les 2 pictogrammes'),
)

#: les seuls hotes externes que la page a le droit de nommer. Tout autre nom de
#: domaine abandonne l'ecriture : c'est ce qui empeche un traceur, une police
#: supplementaire ou une image distante d'entrer par megarde.
HOTES_AUTORISES = (
    'fonts.googleapis.com',
    'fonts.gstatic.com',
    'www.helloasso.com',
    'www.facebook.com',
    'docs.google.com',
    'www.journal-officiel.gouv.fr',
    'annuaire-entreprises.data.gouv.fr',
    'www.resonancesproductions.org',
)


def _controles(html):
    """Leve SystemExit au moindre ecart. Appele AVANT l'ecriture."""
    for marqueur, attendu, quoi in ANCRES:
        n = html.count(marqueur)
        if n != attendu:
            raise SystemExit(
                '!! ABANDON : %d occurrence(s) de « %s » (%s), attendu %d. '
                'Page NON ecrite.' % (n, marqueur, quoi, attendu))

    # chaque ancre du sommaire doit exister dans la page
    for ancre, libelle in SOMMAIRE:
        if 'id="%s"' % ancre not in html:
            raise SystemExit('!! ABANDON : le sommaire renvoie a #%s (« %s ») mais '
                             'aucun bloc ne porte cet identifiant. Page NON ecrite.'
                             % (ancre, libelle))

    # tout `target="_blank"` doit porter `rel="noopener"` (regle du site)
    for m in re.finditer(r'<a\b[^>]*>', html):
        balise = m.group(0)
        if 'target="_blank"' in balise and 'rel="noopener"' not in balise:
            raise SystemExit('!! ABANDON : target="_blank" sans rel="noopener" :\n   %s\n'
                             '   Page NON ecrite.' % balise)

    # aucun hote externe hors liste blanche
    for hote in set(re.findall(r'https?://([^/"\'\s>]+)', html)):
        if hote not in HOTES_AUTORISES:
            raise SystemExit('!! ABANDON : hote externe non autorise « %s ». '
                             'Page NON ecrite.' % hote)

    # aucune iframe, aucun script distant, aucune image
    for interdit in ('<iframe', '<script src', '<img', 'googletagmanager',
                     'analytics'):
        if interdit in html:
            raise SystemExit('!! ABANDON : « %s » dans la page (zero tiers, zero '
                             'image). Page NON ecrite.' % interdit)

    # ⚠️ LA BALISE DE VERIFICATION GOOGLE N'A LE DROIT D'EXISTER QUE SUR `/`.
    #    Elle verifie la propriete « prefixe d'URL » et une seule pose suffit ;
    #    la repeter sur 30 pages ne verifie rien de plus et rend son retrait
    #    hasardeux. C'est `generate_assoc.py` qui la porte, et lui seul.
    if 'google-site-verification' in html:
        raise SystemExit('!! ABANDON : balise « google-site-verification » sur cette '
                         'page. Elle ne doit exister QUE sur la page d’accueil '
                         '(sources/generate_assoc.py). Page NON ecrite.')

    # plancher typographique du site : jamais sous 13 px
    petits = [t for t in re.findall(r'font-size:\s*(\d+(?:\.\d+)?)px', html)
              if float(t) < 13]
    if petits:
        raise SystemExit('!! ABANDON : taille(s) de texte sous le plancher de 13 px : '
                         '%s. Page NON ecrite.' % ', '.join(petits))

    # ⚠️ AUCUN EMOJI (regle du site, demande explicite de David) : les icones
    #    sont dessinees en trait fin, jamais un pictogramme systeme. On refuse
    #    tout caractere des plans emoji.
    emojis = [c for c in html
              if 0x1F300 <= ord(c) <= 0x1FAFF or 0x2600 <= ord(c) <= 0x27BF
              or ord(c) in (0xFE0F, 0x20E3)]
    if emojis:
        raise SystemExit('!! ABANDON : emoji dans la page (%s). Les pictogrammes de '
                         'ce site sont dessines, jamais systeme. Page NON ecrite.'
                         % ' '.join(sorted(set(emojis))))

    # les textes DEMENAGES depuis l'accueil doivent etre integralement ici : si
    # l'un d'eux manquait, la refonte aurait fait PERDRE du contenu au site.
    for quoi, texte in (('2e paragraphe de l’objet', T.OBJET_P2),
                        ('article 1 des statuts', T.STATUTS_ART1),
                        ('article 2 des statuts', T.STATUTS_ART2),
                        ('renvoi au Journal officiel', T.STATUTS_JO),
                        ('lien vers le document des statuts', T.STATUTS_LIEN_DOC),
                        ('fiche data.gouv.fr', T.STATUTS_LIEN_DATAGOUV)):
        if texte not in html:
            raise SystemExit('!! ABANDON : le texte demenage de l’accueil (%s) est '
                             'absent de cette page. Page NON ecrite.' % quoi)


def main():
    html = build_html()
    html = mobile_nav.inject(html)              # 1. le hamburger d'abord
    html = nav_menu.inject(html, 'association')  # 2. puis le menu partage

    _controles(html)
    # Aucune note de redaction en commentaire HTML dans la page livree : elle
    # serait publique et indexable. Sa place est ici, en commentaire `#`.
    verif_commentaires.verifier(html, OUT_HTML)

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)
    print('[page]   %s  (%.1f Ko)' % (OUT_HTML, len(html.encode('utf-8')) / 1024))


if __name__ == '__main__':
    main()
