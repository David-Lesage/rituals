# -*- coding: utf-8 -*-
"""Fabrique le BLOG de Guso Facile : `/guso-facile/blog` + ses 18 articles.

    python3 sources/generate_guso_blog.py     (depuis la racine du depot)

Il ecrit 19 fichiers, tous sous `guso-facile/blog/` :

    guso-facile/blog/index.html                 ->  /guso-facile/blog
    guso-facile/blog/<slug>/index.html          ->  /guso-facile/blog/<slug>

Il ne touche a RIEN d'autre. En particulier il ne touche pas a
`guso-facile/index.html` (page produit, generee par `generate_guso.py`).


D'OU VIENT LA MATIERE
---------------------
Les 18 articles sont RECOPIES, pas reecrits. Deux origines :

  * 8 articles deja publies sur le projet Vercel `guso-facile`
    (`~/CLAUDE/GUSO FACILE/blog/*.html`). Leur contenu redactionnel a ete
    extrait de leur mise en page d'origine (charte bleu/rose, incompatible
    avec celle du site) et retranscrit dans le mini-Markdown decrit plus bas.
  * 10 articles neufs livres en Markdown
    (`~/CLAUDE/GUSO-FACILE-BACKUPS/blog-nouveaux-articles/*.md`), avec un
    bloc de metadonnees YAML en tete.

⚠️ CES DEUX SOURCES SONT HORS DU DEPOT. Elles ne sont donc PAS relues a
   l'execution : le texte des 18 articles est EMBARQUE dans ce fichier, dans
   la table `ARTICLES`. C'est la meme lecon que `generate_trio.py` et
   `generate_site.py`, qui allaient chercher leurs images dans des dossiers
   absents d'un clone neuf et ne tournaient plus. Ici, un clone neuf suffit.

   Corollaire : pour corriger une faute dans un article, on corrige la chaine
   `md` de la table `ARTICLES`, puis on relance ce script. Modifier le HTML
   livre ne sert a rien, il est reecrit par-dessus.


LES URL — ON N'Y TOUCHE PAS
---------------------------
Les slugs sont ceux du dossier SEO (`GUSO-FACILE-BACKUPS/dossier-seo-guso-facile.md`,
section 1), volontairement IDENTIQUES a ceux du projet Vercel. C'est ce qui rend
le plan de redirections 1:1 et auditable. Le dossier le dit sans ambiguite :
les « ameliorer » serait le seul moyen de casser la migration. `_controles()`
verifie que les 18 slugs attendus sont exactement ceux qui sortent.


LE MINI-MARKDOWN
----------------
Aucune bibliotheque externe (regle du depot). Le convertisseur tient dans
`_bloc_a_html()` / `_inline()` et ne connait que ce qui est reellement utilise
par les 18 articles — rien de plus, pour qu'aucune construction ne passe entre
les mailles :

    ## Titre              -> <h2>
    ### Titre             -> <h3>
    - element             -> <ul><li>
    1. element            -> <ol><li>
    > citation            -> <blockquote> (lignes consecutives = un seul bloc)
    **gras**              -> <b>
    *italique*            -> <i>
    [texte](cible)        -> <a> (cible = un slug d'article, ou la page produit)
    @lead phrase          -> paragraphe d'attaque (police plus grande)
    @scene phrase         -> la petite scene en italique qui ouvre les 8 anciens
    ::: encadre Titre     -> encadre (« En bref », « Dans l'app »)
    ...
    :::
    ::: final Titre       -> le panneau de conclusion
    ...
    :::

`@lead`, `@scene`, `::: encadre` et `::: final` ne viennent pas de Markdown :
ce sont les quatre blocs de mise en page que les 8 anciens articles portaient
en HTML (`p.lead`, `p.scene`, `div.callout`, `div.concl`). Les transcrire
plutot que de les perdre evite de reecrire quoi que ce soit.

`_controles()` refuse d'ecrire si un reliquat de Markdown (`**`, `](`, une
ligne commencant par `## ` ou `- `) survit dans le HTML produit.


CE QUI A ETE RETIRE DU TEXTE D'ORIGINE, ET RIEN D'AUTRE
-------------------------------------------------------
Les 8 anciens articles etaient truffes d'emoji (🎯 dans les rubriques, ⚡ « En
bref », 💡 « Dans l'app », ✨ sur les boutons, et 🛡️ 🔮 🔔 🎉 a l'interieur de
citations de l'interface). Le site n'en porte AUCUN — c'est une regle de la
maison et une preference explicite de David. Ils ont donc ete supprimes a
l'extraction, et remplaces la ou ils portaient un sens par une icone SVG en
ligne, au trait fin (voir `ICONES`). AUCUN MOT n'a ete change par ailleurs :
la comparaison mot a mot entre le texte des 8 pages Vercel et le texte
embarque ici ne laisse apparaitre que ces emoji.

Les blocs « A lire ensuite » des 8 anciens ne sont pas recopies : ils sont
REPOSES par ce generateur d'apres la table `SUITE`, qui applique la section 6
du dossier SEO a la lettre pour ces 8, et les paires proposees par le README
des 10 articles neufs pour les autres. Recopier les anciens aurait laisse des
liens vers des `.html` de Vercel.


CE QUI N'A PAS ETE ECRIT ICI, ET POURQUOI
------------------------------------------
Les 10 articles neufs n'ont pas d'encadre « En bref ». Leur bloc de
metadonnees porte un `resume` qui remplit exactement ce role (une reponse
autonome, citable hors contexte) : il devient le chapo de la page ET la
`meta description`. En fabriquer un en plus aurait voulu dire ECRIRE du
texte a la place de leur auteur — ce que ce generateur ne fait nulle part.

Le bouton de fin d'article pointe vers `/guso-facile` tout court, et non vers
`/guso-facile#demander-un-acces` comme le suggere la section 6 du dossier SEO.
Raison mesuree : l'ancre du formulaire sur la page produit s'appelle `#acces`,
pas `#demander-un-acces` — et cette page est refondue en parallele. Un lien
vers une ancre qui n'existe pas est un lien mort silencieux ; le lien vers la
page, lui, ne peut pas se perimer.


LES REGLES DE LA MAISON, ET OU ELLES SONT VERIFIEES
---------------------------------------------------
  * aucune image, aucune iframe, aucune ressource externe (hors la feuille de
    polices deja chargee par les 10 autres pages du site) ;
  * aucun JavaScript propre a ce generateur. Les deux seuls `<script>` de
    comportement sont ceux du site : le hamburger (`mobile_nav.py`) et le menu
    partage (`nav_menu.py`), plus le bouton « retour en haut » du pied de page,
    identique aux 10 autres pages. Les `<script type="application/ld+json">`
    sont des DONNEES, pas du code execute ;
  * plancher typographique 13 px ;
  * aucun commentaire HTML : `verif_commentaires.verifier()` est appele AVANT
    chaque ecriture, et une page fautive n'est pas ecrite ;
  * idempotence : deux executions de suite ne changent pas un octet ;
  * depot PUBLIC — aucune donnee personnelle. Les prenoms qui apparaissent dans
    les articles (Lea, Marco, Sophie, Camille cote anciens ; Nino, Awa, Salome,
    Theo, Elsa, Bastien cote neufs) sont des PERSONNAGES FICTIFS, sans nom de
    famille, sans employeur reel et sans montant reel rattache a quelqu'un.
    `_controles()` interdit d'ajouter un nom de famille a cote de l'un d'eux.

Toutes les notes de travail sont ici, en commentaires Python. Aucune ne part
dans le HTML livre.
"""

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mobile_nav            # hamburger mobile              # noqa: E402
import nav_menu              # menu de navigation partage    # noqa: E402
import theme_chaleur         # couche chaleureuse commune    # noqa: E402
import verif_commentaires    # garde-fou commentaires HTML   # noqa: E402

# ⚠️ `theme_chaleur` N'EST PAS un generateur : il n'ecrit aucune page et ne
#    s'execute pas a l'import (son propre en-tete le dit). L'importer est donc
#    sans danger — contrairement a `generate_*.py`, qu'on ne doit JAMAIS
#    importer puisqu'ils reecrivent leur page au moment de l'import.
#    Il porte, en UN exemplaire pour tout le site : `--coral`, `--plum2`,
#    `--grad`, `--grad-warm`, les trois halos de fond, le `.divider` a deux
#    pixels, les sur-titres `.kick` peints au degrade, le bouton principal, et
#    la correction de contraste du `.legal` (3,8:1 -> 5,96:1). Ces declarations
#    ne sont donc PLUS recopiees ici : une retouche du degrade se fait a un
#    seul endroit et arrive sur les 19 pages du blog en meme temps que sur les
#    10 autres pages du site.

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, 'guso-facile', 'blog')

SITE = 'https://www.resonancesproductions.org'
URL_PRODUIT = '/guso-facile'
URL_BLOG = '/guso-facile/blog'

#: dates du dossier SEO, section 2. `datePublished` des 8 anciens = 18/07/2026
#: (date des fichiers Vercel), des 10 neufs = 15/08/2026 (date de livraison).
#: `dateModified` = 15/08/2026 pour tous. ⚠️ Section 9.4 du dossier : si la
#: vraie date de publication differe, c'est ICI qu'on la corrige — une date
#: fausse dans un `BlogPosting` est un mauvais signal.
DATE_MAJ = '2026-08-15'
DATE_MAJ_FR = '15 août 2026'


# =========================================================================
# LE GABARIT — head, socle CSS, pied de page
# =========================================================================
# Le socle (variables de couleur, typo, nav, boutons, footer, retour en haut)
# est celui des 10 pages du site, repris a l'octet pres de `generate_guso.py`.
# Il n'est PAS importe : importer un generateur l'execute, et il reecrirait sa
# propre page. Regle du depot.
#
# ⚠️ Les deux <link> vers fonts.googleapis.com sont ceux des 10 autres pages.
#    Ce ne sont PAS des polices supplementaires : c'est exactement la meme
#    feuille, deja chargee partout sur le site.

HEAD = """<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(titre)s</title>
<meta name="description" content="%(description)s">
<meta name="author" content="David Lesage">
<meta property="og:title" content="%(og_titre)s">
<meta property="og:description" content="%(description)s">
<meta property="og:type" content="%(og_type)s">
<meta property="og:url" content="%(canonique)s">
<meta property="og:site_name" content="Résonances Productions">
<meta property="og:locale" content="fr_FR">
<meta property="og:image" content="https://www.resonancesproductions.org/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="%(canonique)s">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0e0f24">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
"""

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
/* retour en haut */
.totop{position:fixed;right:18px;bottom:18px;z-index:35;width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:rgba(25,27,61,.92);border:1px solid var(--line);color:var(--gold2);font-size:19px;opacity:0;visibility:hidden;transition:opacity .3s,visibility .3s,transform .2s}
.totop.on{opacity:1;visibility:visible}
.totop:hover{transform:translateY(-2px)}
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

# --- CSS propre au blog ---------------------------------------------------
# Meme parti-pris que la refonte de `/guso-facile` du 14/08/2026 : le socle
# ci-dessus reste celui des 10 autres pages, et TOUTE la chaleur passe par
# cette feuille-ci. Les quatre leviers sont repris a l'identique :
#   1. le degrade signature `--grad` (or clair -> or -> corail -> prune), en
#      filet de 3 px en tete de chaque carte, en texte sur les sur-titres, en
#      marqueur de puce et en bouton ;
#   2. des formes douces : rayons de 16 a 26 px, fonds LEGEREMENT degrades
#      (jamais un aplat sec), ombres portees basses et larges ;
#   3. de l'air : sections a 92 px (66 px sur telephone) ;
#   4. trois halos fixes tres bas en opacite derriere la page.
#
# ⚠️ `--plum2` (#b3a2e4) est la couleur de TOUS les petits textes prune : le
#    `--plum` d'origine tombait a 4,6:1 sur `--card`, tout juste. `--plum`
#    reste aux aplats decoratifs.
# ⚠️ Rien ne descend sous 13 px (verifie par `_controles`).
# ⚠️ `.ic-in` (le pictogramme pose DANS une phrase) ne porte aucune marge
#    laterale : l'espace-mot qui le precede suffit, et une marge a droite le
#    decolle visiblement de la virgule qui le suit dans « detaille, [coche] ou
#    [croix], pour que tu voies ». Mesure a l'ecran, a 390 px.
# ⚠️ Et les notes de ce genre restent ICI, en commentaire Python. Une note
#    ecrite dans la chaine CSS partirait dans le <style> de la page publique :
#    `verif_commentaires.py` ne regarde que les commentaires HTML et ne l'y
#    verrait pas. C'est le controle « aucun emoji » qui l'a attrapee au premier
#    essai — la ceinture a tenu, mais la place de la note n'est pas la.
# ⚠️ La colonne de lecture d'un article est plafonnee a 760 px : au-dela, la
#    ligne devient trop longue pour un texte suivi (le site tient ses autres
#    pages a 820 px, mais elles alternent titres et blocs courts).
CSS_BLOG = """/* ===== Blog Guso Facile ===== */
/* Les variables (--coral, --plum2, --grad, --grad-warm), les halos de fond, le
   .divider, le .kick peint au degrade, le bouton principal et la correction de
   contraste du .legal viennent de la couche commune `theme_chaleur.CSS`,
   inseree JUSTE AVANT cette feuille. On ne redeclare ici que ce qui est propre
   au blog, ou les quelques valeurs ou il s'en ecarte volontairement. */
.ic{width:22px;height:22px;display:block;flex:0 0 auto}
/* les pictogrammes POSES DANS UNE PHRASE (ceux qui remplacent un emoji du
   texte d'origine) : ils doivent s'aligner sur la ligne de base, pas former un
   bloc comme ceux des etiquettes. */
.ic-in{display:inline-block;width:17px;height:17px;vertical-align:-3px;margin:0}
section{padding:92px 0}
.kick{margin-bottom:12px}
.btn{padding:15px 28px}
.btn svg{width:18px;height:18px;flex:0 0 auto;stroke:currentColor}
/* --- tete de page (index et article) ------------------------------------ */
.bl-top{padding:126px 0 62px;background:radial-gradient(900px 560px at 6% -12%,rgba(143,122,209,.22),transparent 62%),radial-gradient(760px 480px at 96% 8%,rgba(224,138,114,.14),transparent 62%),radial-gradient(720px 470px at 60% 108%,rgba(216,178,90,.13),transparent 62%),linear-gradient(180deg,#0b0c1e,var(--night))}
.bl-top h1{font-size:clamp(33px,5.6vw,60px);font-weight:600;line-height:1.06;letter-spacing:.01em;color:#fff;max-width:20ch}
.bl-top .col{max-width:760px}
.bl-dek{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(19px,2.6vw,26px);line-height:1.36;margin-top:16px;max-width:60ch}
.bl-intro{color:#d7d4ea;font-size:17px;margin-top:20px;max-width:66ch}
/* fil d'Ariane : il double le BreadcrumbList du JSON-LD (section 6 du dossier) */
.fil{margin-bottom:20px}
.fil ol{list-style:none;display:flex;flex-wrap:wrap;align-items:center;gap:5px 9px;font-size:13px;letter-spacing:.05em;color:var(--muted)}
.fil li{display:inline-flex;align-items:center;gap:9px}
.fil li+li::before{content:'';width:5px;height:5px;border-radius:1px;background:var(--grad-warm);transform:rotate(45deg);flex:0 0 auto}
.fil a{color:var(--plum2)}
.fil a:hover{color:var(--gold2)}
.fil [aria-current="page"]{color:var(--muted)}
/* la ligne de service : rubrique, duree, public, date de mise a jour */
.bl-meta{display:flex;flex-wrap:wrap;align-items:center;gap:8px 16px;margin-top:26px;font-size:13.5px;color:var(--muted)}
.bl-meta span{display:inline-flex;align-items:center;gap:7px}
.bl-meta .ic{width:17px;height:17px}
.rub{display:inline-flex;align-items:center;gap:8px;padding:6px 15px;border:1px solid rgba(240,209,138,.34);border-radius:999px;color:var(--gold2);font-size:13px;letter-spacing:.14em;text-transform:uppercase;font-weight:500;background:linear-gradient(90deg,rgba(216,178,90,.14),rgba(224,138,114,.10))}
.rub::before{content:'';width:6px;height:6px;border-radius:50%;background:var(--grad-warm);flex:0 0 auto}
/* --- corps d'article ---------------------------------------------------- */
.art{padding:58px 0 0}
.art .wrap{max-width:812px}
.art .col{max-width:760px}
.art h2{font-size:clamp(25px,3.6vw,33px);font-weight:600;color:#fff;line-height:1.16;margin:46px 0 4px}
.art h3{font-size:clamp(20px,2.6vw,24px);font-weight:600;color:var(--gold2);line-height:1.24;margin:34px 0 2px}
.art p{color:#d7d4ea;margin-top:16px;font-size:17px}
.art p.attaque{font-size:19px;color:var(--ink)}
.art b{color:#fff;font-weight:500}
.art a:not(.btn){color:var(--plum2);text-decoration:underline;text-decoration-color:rgba(179,162,228,.5);text-underline-offset:3px}
.art a:not(.btn):hover{color:var(--gold2)}
.art ul,.art ol{margin-top:16px;padding-left:0;list-style:none;counter-reset:pas}
.art li{position:relative;padding-left:27px;margin-top:12px;color:#d7d4ea;font-size:16.5px;line-height:1.68}
.art ul li::before{content:'';position:absolute;left:2px;top:10px;width:8px;height:8px;border-radius:2px;background:var(--grad-warm);transform:rotate(45deg)}
.art ol li{padding-left:36px}
.art ol li::before{counter-increment:pas;content:counter(pas);position:absolute;left:0;top:2px;width:25px;height:25px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',Georgia,serif;font-size:15px;font-weight:600;color:var(--gold2);border:1px solid rgba(240,209,138,.28);background:linear-gradient(140deg,rgba(216,178,90,.16),rgba(224,138,114,.12) 55%,rgba(143,122,209,.14))}
/* la petite scene d'ouverture des 8 anciens articles */
.scene{position:relative;margin-top:26px;padding:4px 0 4px 20px;font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:clamp(19px,2.4vw,23px);line-height:1.44;color:var(--plum2)}
.scene::before{content:'';position:absolute;left:0;top:2px;bottom:2px;width:2px;border-radius:2px;background:var(--grad)}
/* citations et modeles de messages */
.art blockquote{position:relative;overflow:hidden;margin-top:26px;padding:22px 24px;border:1px solid rgba(179,162,228,.26);border-radius:18px;background:linear-gradient(135deg,rgba(143,122,209,.12),rgba(224,138,114,.06))}
.art blockquote p{margin-top:9px;font-size:16.5px;color:var(--ink)}
.art blockquote p:first-child{margin-top:0}
/* encadres « En bref » et « Dans l'app » */
.enc{position:relative;overflow:hidden;margin-top:30px;padding:26px 26px 24px;border:1px solid rgba(255,255,255,.08);border-radius:20px;background:linear-gradient(180deg,#1c1e46,#171935);box-shadow:0 20px 44px -30px rgba(0,0,0,.95)}
.enc::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad)}
.enc-t{display:flex;align-items:center;gap:10px;font-size:13px;letter-spacing:.22em;text-transform:uppercase;font-weight:600;color:var(--gold);margin-bottom:6px}
.enc p{font-size:16.5px}
.enc p:first-of-type{margin-top:8px}
/* le panneau de conclusion */
.final{position:relative;overflow:hidden;margin-top:52px;padding:38px 34px 34px;border:1px solid rgba(255,255,255,.09);border-radius:26px;background:linear-gradient(135deg,rgba(216,178,90,.12),rgba(224,138,114,.10) 48%,rgba(143,122,209,.12));box-shadow:0 30px 70px -46px rgba(0,0,0,.95)}
.final::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad)}
.final h2{margin:0;font-size:clamp(24px,3.4vw,31px)}
.final .cta{margin-top:24px}
.mention{margin-top:18px;color:var(--muted);font-size:14px;line-height:1.65;max-width:64ch}
/* --- « A lire ensuite » -------------------------------------------------- */
.suite{margin-top:58px}
.suite h2{font-size:13px;letter-spacing:.24em;text-transform:uppercase;font-weight:600;margin:0 0 20px;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent;width:fit-content;font-family:'Jost',sans-serif}
.cartes{display:grid;grid-template-columns:repeat(auto-fit,minmax(258px,1fr));gap:20px}
.carte{position:relative;overflow:hidden;display:flex;flex-direction:column;border:1px solid rgba(255,255,255,.07);border-radius:20px;background:linear-gradient(180deg,#1c1e46,#171935);padding:24px 22px 22px;box-shadow:0 20px 44px -30px rgba(0,0,0,.95);transition:transform .2s,border-color .2s}
.carte::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad)}
.carte:hover{transform:translateY(-3px);border-color:rgba(240,209,138,.34)}
.carte-r{font-size:13px;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--gold);margin-bottom:9px}
.carte-t{font-family:'Cormorant Garamond',Georgia,serif;font-size:23px;font-weight:600;color:#fff;line-height:1.2}
.carte-d{color:#cfcbe4;font-size:15px;line-height:1.6;margin-top:11px}
.carte-l{margin-top:16px;padding-top:13px;border-top:1px solid rgba(255,255,255,.08);display:flex;align-items:center;justify-content:space-between;gap:10px;font-size:13px;letter-spacing:.06em;color:var(--plum2)}
.carte-l .ic{width:17px;height:17px}
/* pied d'article : les deux remontees obligatoires */
.remonte{display:flex;flex-wrap:wrap;gap:12px 26px;margin:52px 0 0;padding:24px 0 0;border-top:1px solid rgba(255,255,255,.08);font-size:15px}
.remonte a{display:inline-flex;align-items:center;gap:9px;color:var(--plum2)}
.remonte a:hover{color:var(--gold2)}
.remonte .ic{width:18px;height:18px}
.art .fin{padding-bottom:86px}
/* --- index du blog ------------------------------------------------------- */
.theme{padding:0;margin-top:64px}
.theme:first-of-type{margin-top:8px}
.theme-h{display:flex;align-items:center;gap:14px;padding-bottom:14px;border-bottom:1px solid rgba(255,255,255,.08)}
.theme-h h2{font-size:clamp(24px,3.2vw,31px);font-weight:600;color:#fff;line-height:1.15}
.theme-ico{flex:0 0 auto;width:42px;height:42px;display:flex;align-items:center;justify-content:center;border-radius:14px;border:1px solid rgba(240,209,138,.22);background:linear-gradient(140deg,rgba(216,178,90,.16),rgba(224,138,114,.12) 55%,rgba(143,122,209,.14))}
.theme-n{margin-left:auto;font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);white-space:nowrap}
.theme .cartes{margin-top:24px}
.somm{margin-top:34px;padding:24px 26px;border:1px solid rgba(255,255,255,.07);border-radius:20px;background:linear-gradient(180deg,rgba(28,30,70,.72),rgba(23,25,53,.5))}
.somm-t{font-size:13px;letter-spacing:.22em;text-transform:uppercase;font-weight:600;color:var(--gold);margin-bottom:12px}
.somm ul{list-style:none;display:flex;flex-wrap:wrap;gap:9px 10px}
.somm a{display:inline-flex;align-items:center;gap:8px;padding:8px 15px;border:1px solid rgba(240,209,138,.24);border-radius:999px;font-size:13.5px;color:var(--gold2);background:linear-gradient(180deg,rgba(255,255,255,.05),rgba(255,255,255,.02))}
.somm a:hover{border-color:rgba(240,209,138,.55)}
@media(max-width:760px){
  section{padding:66px 0}
  .bl-top{padding:106px 0 48px}
  .art{padding:44px 0 0}
  .enc{padding:22px 20px 20px}
  .final{padding:28px 22px 24px}
  .carte{padding:22px 19px 19px}
  .somm{padding:20px 18px}
  .theme{margin-top:52px}
}
@media print{.totop{display:none}.kick,.suite h2{-webkit-text-fill-color:var(--gold);color:var(--gold)}}
"""

# --- LA feuille de style des 19 pages, en UN seul assemblage ---------------
# L'ordre est celui que prescrit `theme_chaleur` : le socle des 10 pages du
# site, PUIS la couche chaleureuse commune, PUIS ce qui est propre au blog.
# La couche commune doit arriver APRES le socle (elle le surcharge) et AVANT la
# feuille du blog (que le blog puisse, lui, la surcharger : `.ic` a 22 px, la
# section a 92 px).
#
# ⚠️ Un seul assemblage, nomme, utilise par l'index ET par les articles. Il y
#    avait deux `A(CSS_BASE) / A(CSS_BLOG)` cote a cote ; en retirant de
#    `CSS_BLOG` les declarations desormais portees par `theme_chaleur`, j'ai
#    d'abord oublie d'inserer la couche commune — les 19 pages sont sorties
#    SANS degrade, sans halos, avec le filet d'un pixel : parfaitement valides,
#    et froides. Rien ne l'avait signale. D'ou la constante unique, et le
#    controle `« couche chaleureuse absente »` de `_controle_page()`.
FEUILLE = CSS_BASE + theme_chaleur.CSS + CSS_BLOG

# --- les icones -----------------------------------------------------------
# Grille de 24, trait de 1,5 px, bouts et raccords arrondis, encre = le degrade
# signature (`url(#gf-ink)`). Meme facture que les dix pictogrammes de
# `/guso-facile`. Elles sont DECORATIVES : `aria-hidden`, `focusable="false"`,
# et le texte qu'elles accompagnent se suffit toujours a lui-meme.
# ⚠️ AUCUN EMOJI nulle part : c'est la regle du site. Ces traces sont
#    exactement ce qui remplace les 🎯 ⚡ 💡 ✨ des pages Vercel.
# Le degrade `gf-ink` qui sert d'encre est celui de la couche commune : une
# seule definition pour tout le site (voir `theme_chaleur.SVG_DEFS`).
SVG_DEFS = theme_chaleur.SVG_DEFS

ICONES = {
    # « En bref » : l'eclair, comme le ⚡ des pages Vercel, mais dessine.
    'eclair': '<path d="M13.4 3.2L5.6 13.4h5.2l-.9 7.4 8-10.2h-5.2z"/>',
    # « Dans l'app » : l'ampoule, comme le 💡 des pages Vercel.
    'ampoule': '<path d="M9.6 17.6a5.8 5.8 0 1 1 4.8 0"/><path d="M9.7 17.6h4.6"/>'
               '<path d="M10.4 20.4h3.2"/>',
    # duree de lecture
    'horloge': '<circle cx="12" cy="12" r="8.4"/><path d="M12 7.3V12l3.2 2"/>',
    # a qui l'article s'adresse
    'public': '<circle cx="9.2" cy="8.4" r="3.1"/>'
              '<path d="M3.8 19.6c0-3 2.4-5.1 5.4-5.1s5.4 2.1 5.4 5.1"/>'
              '<path d="M16.2 6.2a3.1 3.1 0 0 1 0 6.1"/>'
              '<path d="M17.3 14.8c1.9.7 3 2.4 3 4.8"/>',
    # date de mise a jour
    'calendrier': '<rect x="3.5" y="5.2" width="17" height="15.2" rx="3"/>'
                  '<path d="M3.5 9.9h17"/><path d="M8.2 3.6v3.1"/><path d="M15.8 3.6v3.1"/>'
                  '<path d="M9 14.8l2.2 2.2 4-4.3"/>',
    # « lire l'article », « retour au blog »
    'fleche': '<path d="M4.6 12h13.6"/><path d="M13.1 6.4L18.8 12l-5.7 5.6"/>',
    'retour': '<path d="M19.4 12H5.8"/><path d="M10.9 17.6L5.2 12l5.7-5.6"/>',
    # theme « Suivi des heures » : le cadran et son aiguille
    'jauge': '<path d="M3.6 18a8.4 8.4 0 1 1 16.8 0"/><path d="M12 18l4.4-5.4"/>'
             '<circle cx="12" cy="18" r="1.15"/>',
    # theme « France Travail » : la feuille de pointage et sa coche
    'pointage': '<path d="M6.4 3.6h8.4l4.4 4.4v12.4H6.4z"/><path d="M14.6 3.6V8h4.4"/>'
                '<path d="M9.4 14.4l2 2 3.8-4.2"/>',
    # theme « GUSO & declarations » : le guichet unique, une porte d'entree
    'guichet': '<path d="M4.2 9.6L12 4.2l7.8 5.4"/><path d="M5.8 10.9v9.1h12.4v-9.1"/>'
               '<path d="M9.8 20v-5.2h4.4V20"/>',
    # theme « Contrat, paiement, negociation » : la signature au bas d'une page
    'contrat': '<path d="M6.2 3.7h8.2l4.2 4.2v9"/><path d="M14.2 3.7V8h4.4"/>'
               '<path d="M4.6 20.2c1.6-3.4 3-5.1 4.2-5.1 1.9 0 .8 4.4 2.6 4.4 1.4 0 2.6-2.2 4.6-2.2 1.2 0 2.3.5 3.4 1.4"/>',
    # theme « Groupe & tournee » : deux reperes relies par la route
    'route': '<path d="M7.4 4.6a2.7 2.7 0 0 1 2.7 2.7c0 2-2.7 4.6-2.7 4.6S4.7 9.3 4.7 7.3a2.7 2.7 0 0 1 2.7-2.7Z"/>'
             '<circle cx="7.4" cy="7.3" r=".9"/>'
             '<path d="M16.6 12.3a2.7 2.7 0 0 1 2.7 2.7c0 2-2.7 4.6-2.7 4.6s-2.7-2.6-2.7-4.6a2.7 2.7 0 0 1 2.7-2.7Z"/>'
             '<path d="M9.9 11.6c1.7 1.3 2.3 2.7 4.5 3.5" stroke-dasharray="2 2.6"/>',
    # theme « Structures » : le classeur d'une equipe
    'structure': '<rect x="3.6" y="9.4" width="16.8" height="10.9" rx="3"/>'
                 '<path d="M8.8 9.4V6.6a2 2 0 0 1 2-2h2.4a2 2 0 0 1 2 2v2.8"/>'
                 '<path d="M3.6 14.2h16.8"/>',
    # le blog lui-meme : un carnet ouvert
    'carnet': '<path d="M12 6.6C10.3 5.2 8.4 4.6 5.4 4.6v12.6c3 0 4.9.6 6.6 2 1.7-1.4 3.6-2 6.6-2V4.6c-3 0-4.9.6-6.6 2Z"/>'
              '<path d="M12 6.6v14"/>',

    # --- les six pictogrammes POSES DANS UNE PHRASE -----------------------
    # Ceux-la ne decorent pas : ils REMPLACENT, a la lettre pres, un caractere
    # que le texte d'origine portait et sans lequel la phrase ne veut plus
    # rien dire (voir `_JETONS_ICONE` et la note devant les deux articles
    # concernes). Ils suivent la meme facture que les autres — grille de 24,
    # trait de 1,5, encre = le degrade signature — donc le sens passe par la
    # FORME, jamais par la couleur : les trois verdicts se distinguent a la
    # coche, au point d'exclamation et a la barre, pas au vert/jaune/rouge des
    # pastilles d'origine. C'est ce qui les rend lisibles en noir et blanc et
    # pour qui ne distingue pas ces trois couleurs.
    'verdict-bon': '<circle cx="12" cy="12" r="8.4"/><path d="M8.2 12.2l2.6 2.6 5-5.4"/>',
    'verdict-negocier': '<circle cx="12" cy="12" r="8.4"/><path d="M12 7.6v5"/>'
                        '<path d="M12 16.2h.01"/>',
    'verdict-eviter': '<circle cx="12" cy="12" r="8.4"/><path d="M6.6 6.6l10.8 10.8"/>',
    'coche': '<path d="M4.8 12.6l4.6 4.6 9.8-10.4"/>',
    'croix': '<path d="M6.4 6.4l11.2 11.2"/><path d="M17.6 6.4L6.4 17.6"/>',
    'maillon': '<path d="M10.2 13.8a3.6 3.6 0 0 0 5.1 0l2.9-2.9a3.6 3.6 0 1 0-5.1-5.1l-1.2 1.2"/>'
               '<path d="M13.8 10.2a3.6 3.6 0 0 0-5.1 0l-2.9 2.9a3.6 3.6 0 1 0 5.1 5.1l1.2-1.2"/>',
}


def _ic(nom, classe='ic', etiquette=None):
    """Une icone en ligne. Meme facture que `theme_chaleur.ic()`.

    Sans `etiquette` elle est DECORATIVE (`aria-hidden`) : le texte qu'elle
    accompagne se suffit a lui-meme. C'est le cas des douze pictogrammes de
    rubrique et de service.

    Avec `etiquette` elle devient une IMAGE annoncee (`role="img"` + `<title>`).
    On ne s'en sert que la ou l'icone remplace un caractere qui portait, seul,
    l'information : sans cela un lecteur d'ecran entendrait « Chaque critere
    est detaille, ou , pour que tu voies ». L'etiquette NOMME LE DESSIN
    (« coche », « croix », « lien ») et n'ajoute aucun propos : ce n'est pas du
    texte redactionnel, c'est l'equivalent d'un `alt`.
    """
    if etiquette is None:
        acc = 'aria-hidden="true" focusable="false"'
        titre = ''
    else:
        acc = 'role="img" aria-label="%s" focusable="false"' % _echap(etiquette)
        titre = '<title>%s</title>' % _echap(etiquette)
    return ('<svg class="%s" viewBox="0 0 24 24" fill="none" '
            'stroke="url(#gf-ink) #e3bd7c" stroke-width="1.5" '
            'stroke-linecap="round" stroke-linejoin="round" '
            '%s>%s%s</svg>' % (classe, acc, titre, ICONES[nom]))


#: Les jetons `{ico:…}` utilisables DANS le texte d'un article, et l'etiquette
#: accessible de chacun (`None` = purement decoratif).
#:
#: ⚠️ Pourquoi ces jetons existent. Les 8 articles repris de Vercel portaient
#:    des emoji A L'INTERIEUR de leurs phrases, pas seulement en decor de
#:    rubrique. Les retirer — regle du site — laissait cinq endroits ou la
#:    phrase de l'auteur devenait fausse ou vide :
#:      « Chaque critere est detaille, ✅ ou ❌, »   -> « detaille, ou , »
#:      « le score : verdict 🟡, a negocier. »       -> « verdict , a negocier. »
#:      « un marqueur « 🔗 » »                       -> « un marqueur «  » »
#:      « verdict 🟢 bon plan / 🟡 … / 🔴 … »        -> la gradation disparait
#:      « le badge devient « Droits securises ✓ » »  -> la marque de fin
#:    Le jeton repose un DESSIN exactement la ou etait le caractere. Aucun mot
#:    n'a ete ajoute, retire ni deplace : on remplace un pictogramme systeme
#:    par un pictogramme maison, ce que la regle « aucun emoji » demande.
_JETONS_ICONE = {
    'bon': ('verdict-bon', None),            # suivi de « bon plan » : redondant
    'negocier': ('verdict-negocier', None),  # suivi de « a negocier » : redondant
    'eviter': ('verdict-eviter', None),      # suivi de « a eviter » : redondant
    'coche': ('coche', 'coche'),             # seul porteur du sens -> annonce
    'croix': ('croix', 'croix'),             # seul porteur du sens -> annonce
    'maillon': ('maillon', 'lien'),          # seul porteur du sens -> annonce
}


# =========================================================================
# LE MINI-MARKDOWN
# =========================================================================
# Volontairement minuscule et strict : il ne connait que ce que les 18
# articles utilisent reellement. Tout le reste passe en texte brut — et
# `_controles()` attrape le reliquat avant l'ecriture.

def _echap(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _cible(href):
    """Resout un lien de la source vers son URL definitive sur le site.

    Les 8 anciens articles se citaient entre eux en `<slug>.html`, et
    pointaient la page produit par `../presentation.html`. Toute cible
    inconnue leve : mieux vaut refuser d'ecrire qu'un lien mort en ligne.
    """
    if href in ('../presentation.html', 'presentation.html'):
        return URL_PRODUIT
    if href in ('../blog.html', 'blog.html'):
        return URL_BLOG
    if href.endswith('.html'):
        slug = href[:-len('.html')].rsplit('/', 1)[-1]
        if slug in SLUGS:
            return '%s/%s' % (URL_BLOG, slug)
    if href.startswith('/') and not href.startswith('//'):
        return href
    raise ValueError('lien interne non resolu : %r' % href)


def _jeton_icone(m):
    nom = m.group(1)
    if nom not in _JETONS_ICONE:
        raise ValueError('jeton d’icone inconnu : {ico:%s}' % nom)
    icone, etiquette = _JETONS_ICONE[nom]
    return _ic(icone, 'ic ic-in', etiquette)


def _inline(t):
    """Gras, italique, liens, jetons d'icone. Applique APRES echappement."""
    t = _echap(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'\*(.+?)\*', r'<i>\1</i>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)',
               lambda m: '<a href="%s">%s</a>' % (_cible(m.group(2)), m.group(1)), t)
    # en dernier : le SVG produit contient des chevrons qu'il ne faut surtout
    # pas repasser dans `_echap`, et un jeton doit pouvoir vivre a l'interieur
    # d'un `**gras**` (c'etait le cas des pastilles de verdict).
    t = re.sub(r'\{ico:([a-z-]+)\}', _jeton_icone, t)
    return t


_RE_OL = re.compile(r'^\d+\.\s+')


def _md_blocs(md):
    """Decoupe le mini-Markdown en blocs (type, charge utile)."""
    lignes = md.split('\n')
    blocs = []
    i = 0
    n = len(lignes)
    while i < n:
        l = lignes[i]
        if not l.strip():
            i += 1
            continue
        if l.startswith('::: '):
            genre, _, titre = l[4:].partition(' ')
            corps = []
            i += 1
            while i < n and lignes[i].strip() != ':::':
                if lignes[i].strip():
                    corps.append(lignes[i].strip())
                i += 1
            if i >= n:
                raise ValueError('bloc « ::: %s » non ferme' % genre)
            i += 1
            blocs.append((genre, (titre.strip(), corps)))
        elif l.startswith('### '):
            blocs.append(('h3', l[4:].strip()))
            i += 1
        elif l.startswith('## '):
            blocs.append(('h2', l[3:].strip()))
            i += 1
        elif l.startswith('@lead '):
            blocs.append(('lead', l[6:].strip()))
            i += 1
        elif l.startswith('@scene '):
            blocs.append(('scene', l[7:].strip()))
            i += 1
        elif l.startswith('> '):
            items = []
            while i < n and lignes[i].startswith('> '):
                items.append(lignes[i][2:].strip())
                i += 1
            blocs.append(('quote', items))
        elif l.startswith('- '):
            items = []
            while i < n and lignes[i].startswith('- '):
                items.append(lignes[i][2:].strip())
                i += 1
            blocs.append(('ul', items))
        elif _RE_OL.match(l):
            items = []
            while i < n and _RE_OL.match(lignes[i]):
                items.append(_RE_OL.sub('', lignes[i]).strip())
                i += 1
            blocs.append(('ol', items))
        else:
            para = [l.strip()]
            i += 1
            while (i < n and lignes[i].strip()
                   and not re.match(r'^(::: |### |## |@lead |@scene |> |- |\d+\.\s)', lignes[i])):
                para.append(lignes[i].strip())
                i += 1
            blocs.append(('p', ' '.join(para)))
    return blocs


#: quelle icone pour quel encadre. Titre inconnu -> l'ampoule (« Dans l'app »).
ICONE_ENCADRE = {'En bref': 'eclair', "Dans l'app": 'ampoule'}


def _bloc_a_html(genre, charge):
    if genre == 'p':
        return '  <p>%s</p>\n' % _inline(charge)
    if genre == 'lead':
        return '  <p class="attaque">%s</p>\n' % _inline(charge)
    if genre == 'scene':
        return '  <p class="scene">%s</p>\n' % _inline(charge)
    if genre == 'h2':
        return '  <h2>%s</h2>\n' % _inline(charge)
    if genre == 'h3':
        return '  <h3>%s</h3>\n' % _inline(charge)
    if genre in ('ul', 'ol'):
        li = ''.join('    <li>%s</li>\n' % _inline(x) for x in charge)
        return '  <%s>\n%s  </%s>\n' % (genre, li, genre)
    if genre == 'quote':
        ps = ''.join('    <p>%s</p>\n' % _inline(x) for x in charge)
        return '  <blockquote>\n%s  </blockquote>\n' % ps
    if genre == 'encadre':
        titre, corps = charge
        ico = _ic(ICONE_ENCADRE.get(titre, 'ampoule'))
        ps = ''.join('    <p>%s</p>\n' % _inline(x) for x in corps)
        return ('  <aside class="enc">\n    <p class="enc-t">%s%s</p>\n%s  </aside>\n'
                % (ico, _echap(titre), ps))
    if genre == 'final':
        titre, corps = charge
        ps = ''.join('    <p>%s</p>\n' % _inline(x) for x in corps)
        return ('  <div class="final">\n    <h2>%s</h2>\n%s'
                '    <div class="cta"><a class="btn" href="%s">Découvrir Guso Facile%s</a></div>\n'
                '  </div>\n' % (_inline(titre), ps, URL_PRODUIT, _ic('fleche')))
    raise ValueError('bloc inconnu : %r' % genre)


def md_en_html(md):
    return ''.join(_bloc_a_html(g, c) for g, c in _md_blocs(md))


# =========================================================================
# LES 18 ARTICLES
# =========================================================================
# ⚠️ LE TEXTE CI-DESSOUS EST CELUI DE SES AUTEURS. On le met en forme, on ne
#    le reecrit pas. En particulier, ces articles portent des AFFIRMATIONS
#    JURIDIQUES (seuils, delais, obligations d'employeur). Aucune n'a ete
#    reformulee, precisee ni ajoutee. Les points signales comme fragiles par
#    le README des articles neufs (articulation DPAE/GUSO, annexes 8 et 10
#    cumulees, convention 2121 du studio) sont a faire relire par un
#    professionnel — ils ne se corrigent pas ici.
#
# Champs :
#   slug        l'URL, telle que la fixe la section 1 du dossier SEO
#   h1          le titre affiche (section 2 du dossier pour les 8 anciens)
#   titre       le <title> de la page
#   description la meta description
#   rubrique    `articleSection` du JSON-LD, et l'etiquette visible
#   motscles    `keywords` du JSON-LD
#   dek         le chapo sous le titre
#   lecture     duree affichee ; `duree` en est la forme ISO 8601
#   public      a qui l'article s'adresse
#   publie      `datePublished`
#   suite       les 3 articles de « A lire ensuite » (voir SUITE, plus haut)
#   md          le corps, en mini-Markdown

ARTICLES = (
  {
    'slug': 'atteindre-507-heures-sans-angoisse',
    'h1': 'Atteindre ses 507 heures sans angoisse',
    'titre': "507 heures d'intermittent : les suivre sans angoisse",
    'description': 'Pour ouvrir ses droits il faut 507 heures sur les 12 mois précédant sa date anniversaire. Comment suivre ce compteur glissant au jour le jour, sans tableur.',
    'rubrique': 'Suivi des heures',
    'motscles': '507 heures, intermittent du spectacle, annexes 8 et 10, date anniversaire, cachet',
    'dek': "Le seuil des 507 heures, ce n'est pas qu'un chiffre : c'est la nuit blanche de trop et le tableur qu'on n'ouvre plus. Voici comment le transformer en un plan clair, mois par mois.",
    'lecture': '4 min',
    'duree': 'PT4M',
    'public': 'Pour les artistes',
    'publie': '2026-07-18',
    'suite': ('studio-et-cheque-intermittents', 'pointage-france-travail-sans-stress', 'ne-plus-jamais-oublier-une-dpae'),
    'md': '''::: encadre En bref

Pour ouvrir ou renouveler ses droits d'intermittent du spectacle (annexes 8 et 10 de l'assurance chômage), il faut réunir **507 heures de travail sur les 12 mois qui précèdent sa date anniversaire**. À raison de **12 heures par cachet** — [y compris pour une session de studio](studio-et-cheque-intermittents.html) — cela représente environ **43 cachets**. Le calcul est glissant : chaque jour, les heures les plus anciennes sortent du compte. Guso Facile affiche en permanence les heures acquises, le reste à trouver et le nombre de jours restants.

:::

@scene Léa est chanteuse. En mars, elle est à 380 heures pour l'année en cours. Elle sait qu'il lui « manque des trucs », mais son ancien tableur Excel n'est plus à jour depuis janvier. Résultat : un chiffre flou, une boule au ventre, et l'impression de courir sans savoir vers quoi.

@lead Le problème de Léa n'est pas le manque de dates. C'est le manque de **visibilité**. Quand on ne sait pas exactement où on en est, chaque concert refusé devient une source d'angoisse et chaque mois qui passe, un reproche. Guso Facile part de là : rendre le chiffre **vivant et lisible**, en permanence.

## Un seul chiffre, toujours à jour

En haut du tableau de bord, une phrase remplace le tableur : **« J'ai effectué 380 h sur 507 h · reste 127 h · dans 158 jours »**. La jauge se remplit sous tes yeux. Plus besoin de calculer quoi que ce soit — le seuil des 507 heures se mesure toujours sur les 12 mois qui précèdent ta **date anniversaire**, et l'app fait le calcul glissant pour toi, chaque jour.

Ce « reste 127 h · dans 158 jours » change tout dans la tête de Léa. Ce n'est plus une menace abstraite, c'est une distance concrète qu'elle peut couvrir.

::: encadre Dans l'app

Le grand bandeau du tableau de bord affiche tes heures **confirmées** sur 507, le reste à trouver, et le nombre de jours jusqu'à ta date anniversaire. Un badge « Droits à sécuriser · reste X h » te rappelle l'objectif tant qu'il n'est pas atteint.

:::

## Un plan mois par mois, pas un mur

127 heures d'un coup, c'est décourageant. Réparties sur les mois qui restent, c'est autre chose. L'app calcule un **rythme conseillé** — « ≈ 32 h/mois » — au prorata des jours réellement restants, et propose un **plan mois par mois**. Léa voit d'un coup ce qu'il lui faut viser en avril, en mai, en juin. Le mur devient un escalier.

## Anticiper avec les dates « possibles »

Léa a deux concerts en discussion, pas encore signés. Elle les entre comme **dates possibles**. Elles ne comptent pas dans ses heures confirmées — pas question de se mentir — mais elles apparaissent dans une **projection** : « Si tes dates possibles se confirment ». Elle voit alors que son reste à trouver passerait de 127 h à 79 h. De quoi décider, en connaissance de cause, s'il faut chercher encore deux dates de plus.

::: encadre Dans l'app

Une date se marque « possible » d'un clic. Le graphique de l'année et le bloc de projection intègrent ces dates à part, pour distinguer clairement **ce qui est acquis** de **ce qui est probable**.

:::

## Et quand le seuil est franchi ?

Le jour où Léa atteint 507 heures, le tableau de bord ne se contente pas d'afficher un chiffre : il **célèbre**. La jauge passe au vert, un « Objectif 507 h atteint ! » s'affiche, le badge devient « Droits sécurisés {ico:coche} ». Parce que franchir ce seuil, après des mois de dates et de démarches, ça se fête — pas juste ça se coche.

::: final Le chiffre travaille pour toi, pas contre toi

Suivre ses 507 heures ne devrait jamais coûter une nuit de sommeil. Un chiffre clair, un plan, une projection honnête : c'est moins d'énergie dans l'admin, et plus dans la musique.

:::''',
  },
  {
    'slug': 'ne-plus-jamais-oublier-une-dpae',
    'h1': 'Ne plus jamais oublier une DPAE',
    'titre': "DPAE : ne plus oublier une déclaration d'embauche",
    'description': "La DPAE est la déclaration préalable à l'embauche, faite par la structure employeuse avant la date. Comment ne plus en rater une, même en semaine chargée.",
    'rubrique': 'Échéances',
    'motscles': "DPAE, déclaration préalable à l'embauche, GUSO, échéance, intermittent",
    'dek': "Une DPAE oubliée, c'est une déclaration en retard, un employeur qui panique et des droits fragilisés. Avec une semaine chargée, l'oubli guette. Voici comment le rendre presque impossible.",
    'lecture': '4 min',
    'duree': 'PT4M',
    'public': 'Pour les artistes',
    'publie': '2026-07-18',
    'suite': ('travailler-a-deux-artistes-dates-partagees', 'atteindre-507-heures-sans-angoisse', 'pointage-france-travail-sans-stress'),
    'md': '''::: encadre En bref

La **DPAE** (déclaration préalable à l'embauche) est réalisée par la **structure employeuse**, avant le début du contrat, à partir des nom, prénom et date de naissance de l'artiste. Une même DPAE peut couvrir plusieurs dates rapprochées (fenêtre de ± 7 jours) ; en revanche, sur une [date jouée à deux](travailler-a-deux-artistes-dates-partagees.html), **il faut une DPAE par artiste**. Guso Facile trie les démarches par urgence dans un bloc « À faire maintenant », avec un badge « J-X » qui passe au rouge à 3 jours ou moins.

:::

@scene Semaine du 15 : Léa a trois concerts. Un le mercredi, un le vendredi, un le samedi. Trois lieux, trois employeurs, trois **DPAE** — la déclaration préalable à l'embauche — à ne pas rater. Entre les répétitions et les trajets, elle sait qu'une va lui passer sous le nez.

@lead La DPAE, c'est la promesse d'embauche que la structure employeuse doit déclarer **avant** la date (nom, prénom, date de naissance de l'artiste). En pratique, on a jusqu'à quelques jours pour la faire, mais dès qu'elles s'accumulent, la charge mentale explose. Guso Facile ne compte pas sur ta mémoire : il te met le prochain pas sous les yeux.

## Le bloc « À faire maintenant »

Juste sous ton tableau de bord, un bloc **« À faire maintenant »** liste les pièces manquantes, **triées par urgence**. Les incohérences à vérifier en premier, puis les dates passées dont il manque encore quelque chose, puis les DPAE des dates à venir avec un badge **« J-X »** — qui passe au rouge quand il ne reste que trois jours ou moins.

Pour la semaine de Léa, le bloc affiche noir sur blanc : « DPAE à faire pour mercredi · J-2 » en rouge. Impossible de passer à côté.

::: encadre Dans l'app

Un bouton **« À faire »** dans l'en-tête porte un compteur : d'un coup d'œil, tu sais combien de choses attendent. Un clic t'amène directement au bloc, et chaque ligne ouvre la date concernée.

:::

## Une seule DPAE pour plusieurs dates

Bonne nouvelle : les trois concerts de Léa sont dans la même semaine. Or une seule DPAE peut couvrir **plusieurs dates rapprochées** (dans une fenêtre de ± 7 jours). Quand Léa saisit sa deuxième date, l'app détecte les autres dates proches et propose un **pop-up** : « Veux-tu relier cette DPAE à ces dates ? », avec des cases à cocher. Elle choisit lesquelles regrouper — et cocher « DPAE faite » sur l'une coche tout le groupe d'un coup.

::: encadre Dans l'app

Le regroupement est proposé automatiquement à la création d'une date confirmée. Les dates liées portent ensuite un marqueur « {ico:maillon} » pour que tu voies, en un instant, ce qui tient ensemble.

:::

## À deux sur une date : chacun sa DPAE

Quand une date est **partagée** entre deux artistes, la DPAE n'est pas commune : il en faut une par personne. L'app le sait et dissocie la démarche en **deux cases** distinctes — « DPAE Léa » et « DPAE Marco ». Le suivi liste alors la DPAE manquante **par personne**, pour que personne ne soit oublié.

::: final La bonne démarche, au bon moment

Ne plus rien oublier, ce n'est pas être plus rigoureux : c'est avoir un outil qui te souffle le prochain pas. Une DPAE réglée à temps, c'est une source de stress en moins et de l'énergie qui repart vers la scène.

:::''',
  },
  {
    'slug': 'pointage-france-travail-sans-stress',
    'h1': 'Pointer France Travail en 5 minutes',
    'titre': 'Actualisation France Travail : pointer en 5 minutes',
    'description': "L'actualisation France Travail réclame chaque mois employeurs, heures et brut. Comment préparer ses lignes d'avance : 1 GUSO = 1 ligne, et un bilan imprimable.",
    'rubrique': 'France Travail',
    'motscles': 'actualisation France Travail, pointage, GUSO, intermittent, Mes activités',
    'dek': "Chaque mois, la même corvée : reporter ses cachets dans l'actualisation, retrouver les montants, recompter. Et si un simple récap faisait le tri à ta place ?",
    'lecture': '4 min',
    'duree': 'PT4M',
    'public': 'Pour les artistes',
    'publie': '2026-07-18',
    'suite': ('atteindre-507-heures-sans-angoisse', 'studio-et-cheque-intermittents', 'evaluer-si-une-date-est-un-bon-plan'),
    'md': '''::: encadre En bref

Pour son actualisation mensuelle, un intermittent reporte dans « Mes activités » **un employeur, des heures et un brut par contrat**, et uniquement les dates **réellement effectuées**. Guso Facile prépare un récap mensuel où **1 GUSO = 1 ligne**, sépare les dates confirmées des dates seulement possibles, et génère un bilan imprimable : total des heures [sur les 507 heures](atteindre-507-heures-sans-angoisse.html), cachets, brut, et statut de chaque date.

:::

@scene Marco est guitariste. On est le 28, jour de son actualisation France Travail. Il ouvre son espace, la page « Mes activités » lui demande d'ajouter ses employeurs et ses heures du mois. Et là, comme chaque fois, il fouille : quels concerts déjà ? combien d'heures ? quel brut ? Trente minutes de doute plus tard, il valide, pas totalement sûr de lui.

@lead Le pointage mensuel n'est pas compliqué en soi. Ce qui l'est, c'est de **rassembler les bonnes lignes** au bon moment. Guso Facile te prépare exactement ce qu'il faut recopier — dans le même esprit que la page « Mes activités » de France Travail.

## Un récap mensuel, calé sur ton actualisation

L'app propose un **récap mensuel** qui reprend, mois par mois, tes GUSO, tes cachets, tes heures et ton brut. Le principe est simple : **1 GUSO = 1 ligne**, comme un employeur = une ligne dans « Mes activités ». Marco n'a plus qu'à lire son mois et reporter. Les cinq minutes remplacent la demi-heure de fouille.

::: encadre Dans l'app

Le **Récap mensuel** se trouve dans l'en-tête. Il découpe l'année en mois et affiche, pour chacun, le total des heures, le nombre de cachets et le brut correspondant — de quoi remplir ton actualisation ligne à ligne.

:::

## Ne pas mélanger le confirmé et le probable

Pour son actualisation, Marco ne doit déclarer que ce qui a **réellement eu lieu**. L'app distingue nettement les dates confirmées des **dates encore « possibles »**, qui restent rangées dans une projection à part — jamais fondues dans les heures qu'il va déclarer. Pas de risque de reporter par erreur un concert qui n'est pas encore signé.

## Le bilan imprimable, pour tout garder au propre

Avant de valider, Marco veut une trace nette de sa période. Le module **« Vérifier & bilan »** passe ses dates en revue, signale ce qui cloche, et génère un **document imprimable** en un clic : total des heures sur 507, cachets, brut, liste des dates avec leur statut. Idéal à garder sous le coude, ou à sortir en cas de contrôle.

::: encadre Dans l'app

Le bouton **« Vérifier & bilan »** ouvre le contrôle de cohérence de ta période, puis un bouton d'impression produit une page propre, prête à imprimer ou à enregistrer en PDF.

:::

::: final Cinq minutes, et c'est réglé

Le pointage n'a pas à être une épreuve mensuelle. Quand les bonnes lignes sont déjà prêtes, tu recopies, tu valides, tu passes à autre chose — moins d'énergie dans l'admin, plus dans la musique.

:::''',
  },
  {
    'slug': 'organiser-une-tournee-qui-tient-la-route',
    'h1': 'Organiser une tournée qui tient la route',
    'titre': 'Organiser une tournée : contacts, trajets et relances',
    'description': "Reprogrammer les salles de l'an dernier sans fouiller ses mails : carnet de contacts auto-alimenté, carte des kilomètres et modèles de mails de relance.",
    'rubrique': 'Développement',
    'motscles': 'tournée, booking, carnet de contacts, relance, salles de concert',
    'dek': "Reprogrammer les bonnes salles, trouver les nouvelles, ne pas rouler pour rien : préparer une tournée, c'est autant de logistique que d'artistique. Voici comment s'appuyer sur ce qu'on a déjà joué.",
    'lecture': '4 min',
    'duree': 'PT4M',
    'public': 'Pour les artistes',
    'publie': '2026-07-18',
    'suite': ('evaluer-si-une-date-est-un-bon-plan', 'structure-accompagner-ses-artistes', 'travailler-a-deux-artistes-dates-partagees'),
    'md': '''::: encadre En bref

Une tournée se construit sur l'historique des dates déjà jouées. Guso Facile en tire trois outils : une **carte** qui calcule les kilomètres aller-retour et relie les dates dans l'ordre chronologique, un **carnet de contacts** alimenté automatiquement par les organisateurs saisis (avec la date de la dernière collaboration), et **quatre modèles de mails** pré-remplis — relance, présentation, candidature à un festival, remerciement. Reste ensuite à [évaluer chaque proposition reçue](evaluer-si-une-date-est-un-bon-plan.html).

:::

@scene Léa veut remonter une tournée cet automne. Son idée : recontacter les salles qui l'ont accueillie l'an dernier, celles où ça s'était bien passé. Sauf que les coordonnées sont éparpillées dans un an de mails, de SMS et de bouts de papier. Rien que retrouver « qui contacter » lui prend une soirée.

@lead Une tournée se construit sur la mémoire de ce qu'on a déjà fait : où on a joué, avec qui, comment c'était. Guso Facile transforme ton historique de dates en **outil de développement**, sans que tu aies à re-saisir quoi que ce soit.

## La carte : voir ses trajets d'un coup d'œil

Le module **Carte** place toutes tes dates sur une carte, avec ton domicile au centre. Il calcule les **kilomètres parcourus** (aller-retour) et peut **relier les dates dans l'ordre chronologique** : la boucle de ta tournée apparaît, du départ au retour à la maison. Léa voit tout de suite si son projet d'automne dessine un itinéraire cohérent ou un zigzag épuisant.

::: encadre Dans l'app

Le bouton **« Carte »** ouvre la vue cartographique. Un lieu mal reconnu ? Tu le renseignes à la main avec l'autocomplétion, et le trajet se recalcule.

:::

## Un carnet de contacts qui se remplit tout seul

Chaque fois que tu renseignes l'organisateur d'une date, il vient nourrir ton **carnet de contacts**. Structure, référent, email, téléphone : tout est regroupé, dédoublonné, prêt à l'emploi. Tu peux aussi ajouter des contacts à la main pour les pistes que tu prospectes.

Mieux : chaque contact garde son **historique**. Léa voit, pour chaque salle, la **dernière fois** qu'elle y a joué, mise en avant. Idéal pour relancer avec un « on s'était vus en octobre dernier… » qui fait toute la différence.

::: encadre Dans l'app

Le module **« Tournée »** réunit trois onglets : **Carnet de contacts** (auto-alimenté par tes dates), **Concerts passés** (filtrables par année et par recherche) et **Mails types**.

:::

## Des mails types, pré-remplis pour toi

Vient le moment d'écrire. Plutôt que de partir d'une page blanche, l'app propose quatre **modèles** : relance, présentation, candidature à un festival, remerciement. Tu choisis un modèle et un contact : l'objet et le corps se pré-remplissent avec ton nom, celui de la structure, et — pour une relance — **la dernière date jouée ensemble**. Tu ajustes, puis tu copies le tout d'un bouton pour le coller dans ton mail.

::: final Ta tournée s'appuie sur ta mémoire, pas sur ta soirée

Retrouver un contact, mesurer un trajet, écrire une relance : ce qui prenait des heures devient l'affaire de quelques clics. C'est de l'énergie récupérée pour ce qui compte — construire des dates et jouer.

:::''',
  },
  {
    'slug': 'evaluer-si-une-date-est-un-bon-plan',
    'h1': 'Évaluer si une date est un bon plan',
    'titre': 'Accepter ou refuser un cachet : évaluer une date',
    'description': "90 € et logé chez l'habitant : bon plan ou pas ? Comparer l'offre à ses conditions idéales, réclamer les infos manquantes et négocier sans culpabiliser.",
    'rubrique': 'Négociation',
    'motscles': 'cachet, négociation, conditions, tournée, intermittent',
    'dek': "« 90 € et logé chez l'habitant. » Bon plan ou piège ? Quand on a besoin d'heures, difficile de dire non. Voici comment décider avec la tête, pas avec la culpabilité.",
    'lecture': '4 min',
    'duree': 'PT4M',
    'public': 'Pour les artistes',
    'publie': '2026-07-18',
    'suite': ('organiser-une-tournee-qui-tient-la-route', 'travailler-a-deux-artistes-dates-partagees', 'atteindre-507-heures-sans-angoisse'),
    'md': '''::: encadre En bref

Décider d'accepter une date revient à comparer l'offre réelle à ses **conditions idéales définies à l'avance** : cachet minimum, distance acceptable, prise en charge du trajet, logement, loge, taille de scène, ingé son, sono, visibilité. Guso Facile rend un verdict {ico:bon} bon plan / {ico:negocier} à négocier / {ico:eviter} à éviter, critère par critère, rassemble les **informations manquantes** à réclamer à l'organisateur et suit l'échéance de signature. Une date acceptée nourrit ensuite [le compteur des 507 heures](atteindre-507-heures-sans-angoisse.html).

:::

@scene Marco reçoit un message : une date dans deux mois, à 250 km, 90 € net, « logé chez l'habitant, on ne peut pas faire les trajets ». Il hésite. Il a besoin d'heures, alors une petite voix lui dit oui. Une autre lui rappelle les fois où il a roulé quatre heures pour rentrer déficitaire. Comment trancher sans culpabiliser ?

@lead Dire oui à tout, c'est s'épuiser ; dire non au hasard, c'est risquer de refuser une belle rencontre. La bonne décision demande de **comparer l'offre à ses propres critères**, froidement. C'est exactement ce que fait l'évaluateur de Guso Facile.

## D'abord, tes conditions idéales

Dans ton profil, tu définis une fois pour toutes tes **conditions idéales** : cachet minimum, distance acceptable, prise en charge du trajet, logement, loge, taille de scène, présence d'un ingé son, sono fournie ou à amener, visibilité attendue. C'est ta boussole personnelle — celle que l'émotion du moment a tendance à faire oublier.

## Ensuite, l'évaluateur « Bon plan ? »

Sur une date, tu saisis les **conditions réelles** proposées par l'organisateur. L'app les compare à ton profil et rend un **verdict** immédiat : **{ico:bon} bon plan**, **{ico:negocier} à négocier**, ou **{ico:eviter} à éviter**. Chaque critère est détaillé, {ico:coche} ou {ico:croix}, pour que tu voies *où* ça coince. Pour l'offre de Marco, le cachet et le trajet non pris en charge font plonger le score : verdict {ico:negocier}, à négocier.

::: encadre Dans l'app

Le bouton **« Bon plan ? »**, dans le détail d'un concert, ouvre l'évaluateur. Si trop peu d'infos sont comparables, il reste prudemment neutre plutôt que de trancher à l'aveugle.

:::

## Les infos manquantes : demander avant de décider

Souvent, on hésite parce qu'il **manque des informations** : montant net exact, prise en charge des repas, matériel sur place. L'app rassemble ces zones d'ombre dans un bloc **« Infos manquantes »** et génère, d'un bouton, un **message poli prêt à envoyer** qui liste précisément ce qu'il reste à préciser, signé de ton prénom. Marco l'envoie tel quel : il négocie sans avoir à trouver les mots.

::: encadre Dans l'app

Le bouton **« Copier la demande d'infos »** met le message dans ton presse-papier, prêt à coller dans un mail ou un WhatsApp.

:::

## Ne pas laisser filer une signature

Une négociation a une **échéance**. Dans le suivi de la date, tu notes le statut (contact, négociation, contrat envoyé, signé) et une **date limite de signature**. L'app affiche alors « à signer avant le… », en jaune quand ça approche, en rouge si c'est dépassé. Plus de « bon plan » qui s'évapore faute d'avoir répondu à temps.

::: final Dire non devient un choix, pas un déchirement

Quand une méthode remplace la culpabilité, refuser une mauvaise date ou en négocier une bonne devient simple et serein. Tu protèges ton énergie — et tu la gardes pour la scène.

:::''',
  },
  {
    'slug': 'travailler-a-deux-artistes-dates-partagees',
    'h1': 'Travailler à deux : les dates partagées',
    'titre': 'Jouer en duo : gérer des dates partagées à deux',
    'description': 'Deux artistes, deux dates anniversaire, mais des concerts communs : comment saisir une date une seule fois et garder deux compteurs de 507 heures justes.',
    'rubrique': 'Duo & groupe',
    'motscles': 'duo, date partagée, date anniversaire, 507 heures, DPAE nominative',
    'dek': "Jouer en duo, c'est une belle aventure — jusqu'à la paperasse, où chacun a son compteur, sa date anniversaire et ses démarches. Voici comment gérer un projet à deux sans tout saisir en double.",
    'lecture': '4 min',
    'duree': 'PT4M',
    'public': 'Pour les artistes',
    'publie': '2026-07-18',
    'suite': ('ne-plus-jamais-oublier-une-dpae', 'atteindre-507-heures-sans-angoisse', 'organiser-une-tournee-qui-tient-la-route'),
    'md': '''::: encadre En bref

Sur un projet à deux, chaque artiste conserve **sa propre date anniversaire et son propre compteur de 507 heures** : une même date ne pèse pas au même endroit dans les deux calculs glissants. Une **date partagée** se saisit une seule fois et apparaît chez les deux, avec des heures de répétition renseignées personne par personne et [une DPAE nominative par artiste](ne-plus-jamais-oublier-une-dpae.html).

:::

@scene Léa et Marco tournent en duo. Sur le papier, c'est simple : ils jouent les mêmes concerts. Dans les faits, ils n'ont pas la même date anniversaire — celle de Léa tombe en février, celle de Marco en août, six mois d'écart. Résultat, la « même » date ne pèse pas pareil dans leurs deux compteurs de 507 heures. Jusqu'ici, ils tenaient deux tableurs séparés.

@lead Un duo, ce n'est pas deux fois le même dossier : c'est deux personnes, deux calendriers de droits, mais des dates communes. Guso Facile gère précisément ce cas avec les **dates partagées** — une saisie, deux suivis justes.

## Une date, saisie une seule fois

Quand Léa entre un concert du duo, elle le marque comme **date partagée**. La date apparaît alors dans l'espace de Léa **et** dans celui de Marco, et compte pour chacun. Fini la double saisie, fini le risque que l'un des deux oublie de la reporter.

::: encadre Dans l'app

À la création d'une date, le sélecteur de propriétaire propose l'option « date partagée ». La date rejoint automatiquement les deux onglets concernés.

:::

## Les heures de répét, personne par personne

Le concert est commun, mais les répétitions ne le sont pas toujours à parts égales : Marco a peut-être bossé deux heures de plus que Léa cette semaine-là. L'app permet de renseigner les **heures de répétition par personne**. Chacun accumule ses propres heures, au plus juste.

## Chacun sa DPAE

Sur une date partagée, il faut **une DPAE par artiste** — pas une seule commune. L'app dissocie donc la démarche en deux cases distinctes, « DPAE Léa » et « DPAE Marco », et le suivi « À faire maintenant » réclame la déclaration manquante **par personne**. Personne ne passe entre les mailles.

::: encadre Dans l'app

Dans le détail d'une date partagée, tu vois deux cases DPAE nominatives. Cocher l'une n'affecte pas l'autre : le suivi de chacun reste exact.

:::

## Deux compteurs, deux dates anniversaire

C'est le cœur du sujet : Léa et Marco ont **chacun leur tableau de bord**, leur jauge de 507 heures et leur date anniversaire. La même date partagée nourrit deux comptes glissants différents. Léa peut avoir déjà sécurisé ses droits pendant que Marco, dont l'anniversaire arrive plus tôt, doit encore trouver des heures. Chacun voit son propre « reste X h · dans X jours », sans confusion.

::: final À deux, mais chacun bien suivi

Gérer un duo sans double saisie ni compteur faussé, c'est une charge mentale en moins pour deux. Et comme une **Vue Groupe** arrive bientôt pour voir où en est chaque membre d'un projet et se soutenir avant que ça coince, l'énergie ira là où elle doit aller : dans la musique qu'on fait ensemble.

:::''',
  },
  {
    'slug': 'structure-accompagner-ses-artistes',
    'h1': 'Accompagner ses artistes sans tableur',
    'titre': 'Gérer les GUSO de plusieurs artistes sans tableur',
    'description': 'Pour une structure : voir sur un seul écran toutes les DPAE, feuillets GUSO et factures à traiter, tous artistes confondus, et suivre les paiements.',
    'rubrique': 'Structures',
    'motscles': 'structure, back-office, GUSO, DPAE, factures, chargé de production',
    'dek': "Gérer les démarches de plusieurs intermittents, c'est jongler avec autant de dossiers que d'artistes. Voici comment tout voir au même endroit, et ne plus rien déclarer en retard.",
    'lecture': '4 min',
    'duree': 'PT4M',
    'public': 'Pour les structures',
    'publie': '2026-07-18',
    'suite': ('ne-plus-jamais-oublier-une-dpae', 'organiser-une-tournee-qui-tient-la-route', 'pointage-france-travail-sans-stress'),
    'md': '''::: encadre En bref

Une structure qui accompagne plusieurs intermittents a besoin d'une **vue transversale** : toutes [les DPAE](ne-plus-jamais-oublier-une-dpae.html), tous les feuillets GUSO et toutes les factures à traiter, tous artistes confondus, sur un seul écran. Guso Facile y ajoute une fiche administrative par artiste (état civil, numéro de sécurité sociale masqué par défaut, numéro GUSO, RIB), le dépôt de la facture directement sur la date, et deux repères de paiement : « Facture réglée » et « Salaire reçu ».

:::

@scene Sophie est chargée de production. Elle accompagne quatre artistes sur leurs GUSO. Chaque semaine, c'est le même casse-tête : quelle DPAE pour qui ? quel GUSO reste à éditer ? quelle facture n'est pas partie ? Elle croise un tableur, ses mails et sa mémoire — et vit dans la crainte de l'oubli qui coûtera des droits à un artiste.

@lead Le travail d'une structure, ce n'est pas de saisir plus, c'est de **ne rien laisser tomber** sur plusieurs personnes à la fois. Guso Facile lui donne une vue transversale : tous les artistes, toutes les tâches, un seul écran.

## Un back-office qui liste tout ce qui reste à faire

Le tableau de bord structure rassemble, **tous artistes confondus**, les **DPAE à faire**, les **feuillets GUSO à éditer** et les **factures à traiter**. Sophie n'ouvre plus quatre dossiers : elle lit une seule to-do. Chaque ligne est **cliquable** et l'amène directement sur la date concernée pour agir.

::: encadre Dans l'app

L'onglet back-office regroupe les tâches par catégorie (DPAE / GUSO / factures-virements). Les DPAE de dates rapprochées sont même dédoublonnées, pour déclarer plusieurs dates d'un coup.

:::

## Les infos d'un artiste, en un clic

Pour remplir une DPAE, il faut l'état civil, le numéro de sécurité sociale, le numéro GUSO… Plutôt que de les redemander à chaque fois, la section **« Mes artistes »** réunit une fiche administrative par personne. Le numéro de sécu est **masqué par défaut** et se dévoile d'un clic. Un bouton **« Copier les infos »** met tout le bloc dans le presse-papier, prêt à coller dans le formulaire de DPAE.

Les **coordonnées bancaires** et le RIB officiel de chaque artiste y figurent aussi, pour préparer les virements sans rien réclamer.

## Déposer les factures, suivre les paiements

Quand le GUSO et la facture sont édités, Sophie peut **déposer la facture directement sur la date** (glisser-déposer, ou lien). Et pour ne pas perdre le fil de l'argent, deux cases claires jalonnent chaque date : **« Facture réglée »** et **« Salaire reçu »**. D'un coup d'œil, elle sait qui a été payé et ce qui reste en attente.

::: encadre Dans l'app

Une fiche **« Ma structure »** centralise le SIRET, l'IBAN et la licence de spectacle, réutilisés partout où c'est nécessaire.

:::

::: final Voir tout, oublier rien

Quand les démarches de tous les artistes tiennent sur un seul écran, l'accompagnement redevient serein. Et une **vue des points de vigilance** — qui approche du seuil, qui a besoin d'un coup de main — arrive bientôt pour aller encore plus loin. Moins d'énergie dans la paperasse, plus dans le soutien aux artistes.

:::''',
  },
  {
    'slug': 'studio-et-cheque-intermittents',
    'h1': 'Déclarer une session studio',
    'titre': 'Session studio : chèque-intermittents et 507 heures',
    'description': "Une session d'enregistrement relève de l'édition phonographique (convention 2121), hors GUSO, réglée au chèque-intermittents — et compte dans les 507 heures.",
    'rubrique': 'Studio',
    'motscles': 'session studio, convention collective 2121, chèque-intermittents, édition phonographique, 507 heures',
    'dek': "Enregistrer sur un album, ce n'est pas un concert : pas de GUSO, une convention différente, un mode de paiement à part. Mais ça compte quand même pour tes droits. Voici comment ne pas s'y perdre.",
    'lecture': '4 min',
    'duree': 'PT4M',
    'public': 'Pour les artistes',
    'publie': '2026-07-18',
    'suite': ('pointage-france-travail-sans-stress', 'atteindre-507-heures-sans-angoisse', 'travailler-a-deux-artistes-dates-partagees'),
    'md': '''::: encadre En bref

Une session d'enregistrement relève de l'**édition phonographique (convention collective 2121)** et non du spectacle vivant : elle n'est donc **pas déclarée via un GUSO**, mais généralement réglée au **chèque-intermittents**. Côté droits, elle compte comme un cachet — **1 cachet = 12 heures** — qui s'ajoutent [au compteur des 507 heures](atteindre-507-heures-sans-angoisse.html).

:::

@scene Marco vient de passer deux jours en studio pour enregistrer l'album d'une copine. Pas de scène, pas de public : des prises, des reprises, un casque sur les oreilles. Au moment de « déclarer ça », il bloque. Ce n'est pas un GUSO comme ses concerts. Est-ce que ça compte seulement pour ses heures ?

@lead Le travail de musicien de studio suit un circuit administratif **différent** de celui des concerts. Le comprendre évite bien des erreurs — et rassure sur un point essentiel : oui, ces heures comptent.

## Un circuit à part : ni GUSO, ni scène

Une session d'enregistrement relève de l'**édition phonographique** (convention collective 2121), pas du spectacle vivant. Elle n'est donc **pas déclarée via un GUSO** mais généralement réglée au **chèque-intermittents**. Bref, ce n'est pas le même formulaire, pas le même employeur, pas le même document.

::: encadre Dans l'app

À la création d'une date, choisis le type **« studio »**. L'app sait alors que cette date sort du circuit GUSO : elle n'apparaît pas dans les feuillets GUSO ni dans la to-do de la structure, qui ne la gère pas.

:::

## Mais ça compte dans tes heures

Voici le point qui rassure Marco : côté droits, une session studio **compte comme un cachet**. La règle est la même que pour un cachet de concert — **1 cachet = 12 heures**. Ses deux jours d'enregistrement nourrissent donc sa progression vers les 507 heures, exactement comme une date de concert.

C'est pour ça que l'app la **compte quand même** dans ton total, tout en la traitant à part sur le plan administratif. Tu ne perds rien de tes heures, et tu ne mélanges pas les circuits.

::: encadre Dans l'app

Le graphique annuel distingue quatre catégories — **Concert**, **Répétition**, **Technicien** et **Studio** — pour que tu voies d'où viennent tes heures, sans jamais confondre une session avec un concert.

:::

## Le bon réflexe à la saisie

Concrètement, Marco entre sa date, choisit le type « studio », indique le nombre de cachets. L'app fait le reste : les heures s'ajoutent à sa jauge, la date reste hors du to-do GUSO, et son bilan de fin de période la signale clairement comme relevant d'un autre circuit. Rien à recalculer, rien à craindre d'oublier.

::: final Chaque type de date à sa juste place

Distinguer une session studio d'un concert, tout en créditant les bonnes heures : c'est le genre de détail qui, mal géré, coûte du temps et de l'angoisse. Bien géré, c'est transparent — et c'est autant d'énergie qui repart vers la musique.

:::''',
  },
  {
    'slug': 'combien-de-cachets-pour-507-heures',
    'h1': 'Combien de cachets faut-il pour atteindre 507 heures ?',
    'titre': 'Combien de cachets faut-il pour atteindre 507 heures ?',
    'description': 'Un cachet vaut 12 heures, donc environ 43 cachets par an. Voici le calcul complet, avec les répétitions et les plafonds à connaître.',
    'rubrique': 'Suivi des heures',
    'motscles': 'cachet, 507 heures, intermittent du spectacle, France Travail, répétition rémunérée',
    'dek': 'Un cachet vaut 12 heures, donc environ 43 cachets par an. Voici le calcul complet, avec les répétitions et les plafonds à connaître.',
    'lecture': '6 min',
    'duree': 'PT6M',
    'public': 'Pour les artistes',
    'publie': '2026-08-15',
    'suite': ('quand-tombe-ma-date-anniversaire', 'm-organiser-quand-je-joue-dans-plusieurs-groupes', 'atteindre-507-heures-sans-angoisse'),
    'md': '''C'est probablement la question la plus tapée par les intermittents. Et la bonne nouvelle, c'est qu'elle a une réponse simple. La mauvaise, c'est qu'elle a aussi trois ou quatre nuances qui font toute la différence quand on est à 40 heures du seuil au mois d'août.

## La réponse courte : environ 43 cachets

Pour France Travail, **un cachet d'artiste vaut 12 heures**. Toujours 12, quelle que soit la durée réelle du contrat : que tu joues 45 minutes en première partie ou trois heures en tête d'affiche, le cachet compte pareil.

Le calcul tient donc en une ligne :

> 507 ÷ 12 = 42,25 → **43 cachets** pour franchir le seuil.

Quarante-trois dates sur douze mois. Environ trois et demie par mois. Dit comme ça, ça devient une distance, plus une menace.

## Fini les « cachets isolés » et les « cachets groupés » (pour France Travail)

Si quelqu'un t'a dit un jour qu'au-delà de cinq cachets d'affilée chez le même employeur, tes cachets ne valaient plus que 8 heures : c'était vrai, mais c'est de l'histoire ancienne côté indemnisation.

Depuis le 1er août 2016, **France Travail retient 12 heures par cachet dans tous les cas**, isolé ou groupé. Ça a été une vraie simplification pour les artistes qui font des séries : une semaine de six représentations dans le même théâtre te rapporte 72 heures, pas 48.

Attention quand même : la distinction isolé / groupé **existe toujours côté URSSAF**, parce qu'elle influence le calcul de certaines cotisations. Tu peux donc la voir apparaître sur un bulletin ou une déclaration sans que ça change quoi que ce soit à tes heures. Si un doute subsiste sur une déclaration précise, c'est à ton employeur ou au GUSO qu'il faut poser la question.

## Ce qui compte en plus des cachets

Les cachets ne sont pas ta seule source d'heures. Comptent aussi :

- **Les heures de répétition rémunérées**, quand elles sont déclarées comme telles. Elles s'ajoutent en heures réelles : trois répétitions de 4 heures payées, ce sont 12 heures de plus. Le point important, c'est *déclarées* — une répétition non rémunérée et non déclarée n'existe pas pour France Travail, même si tu y as passé ton dimanche.
- **Les heures de technicien**, si tu en fais. Elles relèvent de l'annexe 8 quand tu es artiste sous annexe 10, mais elles se cumulent pour atteindre les 507 heures. (Sur l'annexe finalement retenue pour t'indemniser, voir plus bas.)
- **Les heures d'enseignement**, dans une limite précise : elles sont retenues **jusqu'à 70 heures**, portées à **120 heures** si tu as 50 ans ou plus à la fin du contrat retenu pour l'ouverture des droits. Au-delà, elles ne comptent plus. Et si tu cumules cours donnés et formation suivie non indemnisée sur la même période, l'ensemble est plafonné à 338 heures.

## Ce qui ne compte pas

- Les répétitions **non payées**. Le temps de travail réel d'un musicien est massivement supérieur à ses heures déclarées : c'est injuste, c'est comme ça, et ça ne se plaide pas auprès de France Travail.
- Les concerts payés **au noir** ou « en défraiement » sans déclaration. Aucune heure, aucun droit, aucun recours.
- Les auditions, les repérages, les allers-retours, la compo, la promo. Rien de tout ça n'entre dans le compteur.
- Les activités **non salariées** : si tu factures une prestation en auto-entrepreneur, elle ne produit pas d'heures d'intermittence.

## Deux plafonds à garder en tête

**Vingt-huit cachets par mois maximum.** France Travail ne retient pas plus de 28 cachets sur un même mois. En pratique, très peu de gens s'en approchent — mais si tu fais une grosse série d'été, ça peut te concerner.

**Les 507 heures se comptent sur 12 mois glissants**, pas sur l'année civile. Ta période de référence court sur les 365 jours qui précèdent ta date anniversaire. C'est un tapis roulant : chaque mois, tu gagnes les heures du mois en cours et tu perds celles du même mois de l'an dernier. C'est un sujet à part entière — on lui a consacré un article.

## Un exemple pour poser les idées

Nino (personnage fictif) est batteur. Sur ses douze derniers mois, il a :

- 31 cachets de concert → 31 × 12 = **372 h**
- 4 cachets en studio, déclarés comme cachets d'artiste → **48 h**
- 18 heures de répétitions rémunérées et déclarées → **18 h**
- 40 heures de cours en école de musique → **40 h** (sous le plafond de 70 h, tout est retenu)

Total : **478 heures**. Il lui manque 29 heures, soit **3 cachets**. Formulé comme ça, ce n'est plus une angoisse, c'est un objectif de deux mois.

## Les règles bougent — vérifie avant de t'engager

Le régime des annexes 8 et 10 est renégocié régulièrement, et les paramètres d'indemnisation (durée, montant, franchises) évoluent plus souvent que le seuil lui-même. Le seuil de 507 heures est stable depuis longtemps, mais rien n'est gravé dans le marbre.

Les seules sources qui font foi pour ton dossier : **France Travail Spectacle** (ton espace personnel et ton conseiller), le **GUSO** pour les déclarations, et ton **syndicat** (SNAM-CGT, SFA-CGT, entre autres) pour l'interprétation d'un cas particulier. Cet article t'explique un fonctionnement ; il ne remplace aucun de ces trois-là.

## Compter sans y penser

Le vrai piège des 507 heures, ce n'est pas le calcul : c'est de ne pas savoir où on en est. Un tableur ouvert une fois par trimestre donne un chiffre faux, et un chiffre faux coûte des nuits.

**Guso Facile** tient ce compteur à ta place, en glissant : cachets, répétitions, heures de technicien, chacun à sa juste valeur, avec un « reste X h · dans X jours » toujours à jour et un plan mois par mois. L'app est en bêta, accessible sur cooptation.

Moins d'énergie dans le calcul, plus dans la musique.''',
  },
  {
    'slug': 'quand-tombe-ma-date-anniversaire',
    'h1': 'Comment savoir quand tombe ma date anniversaire ?',
    'titre': 'Comment savoir quand tombe ma date anniversaire ?',
    'description': "Ta date anniversaire n'est ni ton anniversaire ni le 31 décembre : c'est douze mois après la fin de contrat qui a ouvert tes droits.",
    'rubrique': 'Suivi des heures',
    'motscles': 'date anniversaire, période de référence, 507 heures, ouverture des droits, France Travail',
    'dek': "Ta date anniversaire n'est ni ton anniversaire ni le 31 décembre : c'est douze mois après la fin de contrat qui a ouvert tes droits.",
    'lecture': '5 min',
    'duree': 'PT5M',
    'public': 'Pour les artistes',
    'publie': '2026-08-15',
    'suite': ('combien-de-cachets-pour-507-heures', 'heures-ne-correspondent-pas-france-travail', 'atteindre-507-heures-sans-angoisse'),
    'md': '''« Il te reste combien de temps ? » En tournée, c'est une question qu'on se pose entre deux balances. Et il y a toujours quelqu'un pour répondre : « moi c'est en novembre », sans être tout à fait sûr de pourquoi.

La date anniversaire est le point le plus mal compris du régime, alors qu'elle commande tout : c'est elle qui décide du jour où on regarde ton compteur.

## Ce que ce n'est pas

- **Ce n'est pas le 31 décembre.** Le régime des intermittents ne fonctionne pas en année civile. Tes 507 heures ne se remettent pas à zéro au réveillon.
- **Ce n'est pas ta date de naissance.** Le mot « anniversaire » est trompeur : il ne s'agit pas de toi, mais de tes droits.
- **Ce n'est pas une date que tu choisis.** Elle découle mécaniquement de ton dossier.

## Ce que c'est

Ta date anniversaire, c'est **douze mois après la fin de contrat de travail qui a été retenue pour ouvrir (ou renouveler) tes droits**.

Autrement dit : le jour où France Travail a ouvert ton droit, il s'est appuyé sur une fin de contrat précise — la dernière avant l'examen de ton dossier. Ajoute 365 jours à cette fin de contrat : tu obtiens la date à laquelle ta situation sera réexaminée.

Un exemple avec Awa (personnage fictif), violoncelliste. Son dernier contrat avant l'ouverture de ses droits s'est terminé le **12 mars**. Sa date anniversaire tombe donc le **12 mars** de l'année suivante. À ce moment-là, France Travail regardera les 365 jours écoulés et cherchera au moins 507 heures.

C'est aussi pour ça que deux musiciens qui jouent exactement les mêmes concerts peuvent avoir des dates anniversaire à six mois d'écart : leurs droits ne se sont pas ouverts au même moment. La même date de concert ne pèse pas de la même façon dans leurs deux compteurs.

## La période de référence : douze mois glissants

Une fois la date anniversaire connue, la période à surveiller se déduit toute seule : ce sont les **365 jours qui la précèdent**.

C'est un tapis roulant. Chaque jour, la fenêtre avance : tu gagnes ce que tu viens de faire, et tu perds ce que tu avais fait le même jour l'an dernier. Deux conséquences très concrètes :

- Un mois d'été chargé te porte pendant un an — puis disparaît d'un coup l'été suivant. Si tu avais fait 80 heures en juillet dernier, ces 80 heures sortent de ton compteur en juillet prochain, même si tu ne joues pas moins.
- Une date ajoutée en fin de période « rentre » entièrement. Une date ajoutée juste après ta date anniversaire compte pour la période *suivante*, pas pour celle qui vient de se clore. Le calendrier compte autant que le nombre de dates.

## Comment retrouver la tienne, concrètement

Trois pistes, de la plus fiable à la plus approximative :

1. **Ton espace France Travail Spectacle.** C'est la source qui fait foi. Les notifications d'ouverture ou de renouvellement de droits indiquent la période retenue. Si tu ne trouves pas, ta ou ton conseiller peut te la confirmer — c'est une question banale, personne ne va te regarder de travers.
2. **Ta dernière notification de droits.** Repère la fin de contrat retenue pour l'examen, ajoute douze mois.
3. **Ton dernier réexamen.** Si tes droits ont été renouvelés, la date anniversaire s'est décalée en conséquence. Ne te fie pas à celle que tu avais en tête il y a trois ans.

Un conseil : **écris-la quelque part**. Beaucoup d'intermittents fonctionnent avec une date approximative dans la tête, et découvrent trois semaines avant qu'ils s'étaient trompés d'un mois. Trois semaines, c'est court pour trouver deux cachets.

## Et si je réunis mes 507 heures en avance ?

C'est possible, et c'est même une bonne chose à connaître. Si tu réunis de nouveau 507 heures **avant** ta date anniversaire, tu peux, sous conditions, demander un **réexamen anticipé** de tes droits. Cela peut décaler ta date anniversaire et, selon ta situation, améliorer ton allocation.

Selon conditions, donc : c'est exactement le genre de décision qui dépend de ton dossier, de ton allocation journalière actuelle et de ce qui t'attend dans les mois qui suivent. Ne tranche pas ça seul depuis un forum. **Pose la question à France Travail, ou à ton syndicat** (SNAM-CGT, SFA-CGT et d'autres accompagnent leurs adhérents sur ces arbitrages).

## Et si je n'y arrive pas ?

Il existe des mécanismes de sécurité — notamment une **clause de rattrapage** et des allocations spécifiques de fin de droits. Leurs conditions et leurs montants évoluent au fil des accords sur l'assurance chômage, et ils ne se déclenchent pas tous automatiquement.

Deux réflexes valent mieux que dix pages lues en ligne : **anticiper** dès qu'on voit que le compte ne rentre pas, et **appeler France Travail avant** la date anniversaire, pas après. Un dossier examiné à froid se répare beaucoup mieux qu'un dossier examiné dans la panique.

## Une date qui travaille pour toi

Connaître sa date anniversaire, ce n'est pas de l'administratif : c'est savoir sur quelle ligne d'arrivée on court. Tant qu'elle reste floue, chaque concert refusé pèse une tonne. Une fois qu'elle est posée, tu peux décider.

**Guso Facile** te demande ta date anniversaire une fois, puis calcule tout en glissant : les heures acquises sur la bonne fenêtre, ce qu'il reste, et le nombre de jours qui te séparent de l'échéance. Chaque personne a la sienne, même sur des dates jouées ensemble. L'app est en bêta, accessible sur cooptation.

Moins d'énergie à compter les mois, plus dans la musique.''',
  },
  {
    'slug': 'employeur-ne-m-a-pas-paye-mon-cachet',
    'h1': "Mon employeur ne m'a pas payé mon cachet : que faire ?",
    'titre': "Mon employeur ne m'a pas payé mon cachet : que faire ?",
    'description': "Relance écrite, mise en demeure, puis prud'hommes : les étapes d'un impayé, les délais à connaître et les interlocuteurs à qui s'adresser.",
    'rubrique': 'Paiement',
    'motscles': "cachet impayé, mise en demeure, conseil de prud'hommes, salaire, intermittent",
    'dek': "Relance écrite, mise en demeure, puis prud'hommes : les étapes d'un impayé, les délais à connaître et les interlocuteurs à qui s'adresser.",
    'lecture': '6 min',
    'duree': 'PT6M',
    'public': 'Pour les artistes',
    'publie': '2026-08-15',
    'suite': ('faut-il-un-contrat-pour-un-concert', 'ca-va-te-faire-connaitre-comment-repondre', 'structure-comment-gerer-les-guso-de-mes-artistes'),
    'md': '''Le concert s'est bien passé. Trois semaines plus tard, rien. Puis un mois. Tu relances par SMS, on te répond « oui oui, c'est en cours ». Deux mois. Et tu commences à te dire que tu vas peut-être laisser tomber, parce que c'est déjà assez pénible comme ça.

Ne laisse pas tomber. Un salaire impayé se réclame, et la loi est nettement de ton côté.

> **Précision utile :** cet article explique un fonctionnement général, il ne constitue pas un conseil juridique. Chaque situation a ses particularités. Pour ton cas précis, adresse-toi à ton syndicat, à l'inspection du travail ou à un professionnel du droit — les coordonnées sont en bas de l'article.

## D'abord : de quoi parle-t-on exactement ?

Trois situations très différentes se cachent derrière « on ne m'a pas payé ».

**1. Le salaire n'est pas arrivé.** Tu as bien été déclaré (contrat, GUSO, bulletin ou attestation d'emploi), mais le virement n'est jamais venu. C'est un **salaire impayé** au sens du code du travail. C'est le cas le plus simple : tu as des preuves, tu as des recours.

**2. Rien n'a jamais été déclaré.** Pas de contrat, pas de GUSO, un accord oral et une promesse. C'est plus lourd : au-delà de l'argent, il manque aussi tes heures. On y revient plus bas.

**3. Le montant ne correspond pas** à ce qui avait été annoncé, ou des frais promis n'ont pas été remboursés. Le raisonnement est le même que pour le cas 1, sur la différence.

Identifier lequel des trois te concerne change les démarches. Prends cinq minutes pour le faire avant d'écrire quoi que ce soit.

## Étape 1 — Rassembler tes preuves

Avant toute relance formelle, réunis tout ce que tu as, même informel :

- le **contrat** (CDDU), s'il existe ;
- la **déclaration GUSO** ou l'**attestation mensuelle d'emploi** que le GUSO t'envoie — elle vaut bulletin de salaire ;
- les **échanges écrits** : mails, SMS, messages, où figurent la date, le lieu, le montant convenu ;
- l'**affiche**, le programme, la billetterie, une photo datée : tout ce qui prouve que tu as bien joué.

Bonne nouvelle sur ce point : **ce n'est pas à toi de prouver que tu n'as pas été payé**. C'est à l'employeur de prouver qu'il t'a payé. Ton travail consiste surtout à établir que le contrat de travail a bien existé.

## Étape 2 — La relance écrite

Un SMS ne laisse pas de trace exploitable. Un mail, si. Écris quelque chose de court, factuel et daté :

> Bonjour,
> Je fais suite au concert du [date] à [lieu], pour lequel un cachet de [montant] avait été convenu. À ce jour, je n'ai pas reçu le paiement. Peux-tu me confirmer sous quel délai il sera effectué ?
> Merci d'avance,
> [Prénom Nom]

Pas d'agressivité, pas de justification, pas d'excuses. Une date, un montant, une question.

Souvent, ça suffit : beaucoup de retards sont des oublis, des trésoreries tendues ou un dossier bloqué chez le comptable. Laisse une dizaine de jours.

## Étape 3 — La mise en demeure

Sans réponse, ou face à des promesses qui ne se réalisent pas, passe à la **mise en demeure**, par **lettre recommandée avec accusé de réception** (ou remise en main propre contre signature).

Elle reprend les mêmes éléments, avec trois ajouts : le mot « mise en demeure » explicitement, un **délai de paiement** (souvent 8 ou 15 jours), et la mention que tu saisiras le conseil de prud'hommes à défaut.

C'est une étape simple mais qui change la nature du dossier : elle date officiellement ta réclamation, elle fait courir les intérêts, et elle est très souvent celle qui débloque. Ton syndicat peut te fournir un modèle et te relire — c'est l'un des services les plus concrets d'une adhésion.

## Étape 4 — Le conseil de prud'hommes

C'est la juridiction compétente pour un litige entre salarié et employeur, et **un artiste au cachet est un salarié**. La saisine est gratuite, et l'avocat n'est pas obligatoire.

Deux choses à savoir :

- Pour une créance de salaire non contestée dans son principe, une procédure **en référé** existe — elle vise à obtenir plus vite une décision provisoire. Le conseil de prud'hommes du lieu concerné peut t'indiquer la marche à suivre.
- Le délai pour agir sur des salaires est de **trois ans** à compter du jour où le salaire aurait dû être payé (article L. 3245-1 du code du travail). C'est confortable, mais ne t'endors pas dessus : les preuves et les témoignages, eux, s'effacent vite. D'autres délais, plus courts, peuvent s'appliquer à d'autres types de demandes (rupture du contrat, par exemple) — d'où l'intérêt de faire vérifier ta situation.

## Le cas particulier : tu n'as jamais été déclaré

Si aucun contrat n'a existé et qu'aucune déclaration n'a été faite, tu n'as pas seulement perdu de l'argent : tu as perdu des **heures**, et donc une partie de tes droits.

Deux interlocuteurs sont là pour ça :

- **L'inspection du travail** (au sein de la DREETS de ton département). Elle est compétente sur le travail dissimulé et sur le respect des obligations de l'employeur. Tu peux la saisir, y compris pour un simple signalement.
- **Ton syndicat**, qui connaît le secteur et saura te dire ce qui vaut la peine d'être engagé.

Sur les cotisations et les déclarations elles-mêmes, le **GUSO** peut t'indiquer si une déclaration te concernant a bien été enregistrée. Et **France Travail Spectacle** te dira, de son côté, ce qui a été reçu à ton nom.

## À qui s'adresser, en résumé

- **Ton syndicat** : SNAM-CGT (musiciens), SFA-CGT (artistes interprètes), et d'autres organisations selon ton métier. C'est l'accompagnement le plus adapté au secteur, et l'adhésion coûte moins cher qu'un cachet perdu.
- **L'inspection du travail** (DREETS) : non-déclaration, travail dissimulé, manquements de l'employeur.
- **Le conseil de prud'hommes** : le litige lui-même.
- **Le GUSO** et **France Travail Spectacle** : ce qui a été déclaré, ou pas.
- Selon tes revenus, l'**aide juridictionnelle** et les **points-justice** (permanences juridiques gratuites) peuvent prendre le relais.

## Et surtout : la fois d'après

La quasi-totalité des impayés ont un point commun — **rien n'avait été écrit avant**. Pas de contrat, un montant dit à l'oral, un délai de paiement jamais évoqué. Sans écrit, tout devient une affaire de mémoire et de bonne volonté.

Un contrat, même court, qui dit qui, quoi, quand, combien et **payé sous combien de temps**, ne t'empêchera pas de tomber sur une structure en difficulté. Mais il transforme un litige flou en créance nette.

**Guso Facile** garde la trace de ce qui a été payé et de ce qui ne l'a pas été, date par date, pour que tu ne découvres pas un impayé six mois trop tard. Un générateur de contrat d'engagement, à personnaliser avant chaque date, arrivera bientôt dans l'app — c'est le meilleur endroit où mettre son énergie. L'app est en bêta, accessible sur cooptation.

Moins d'énergie à courir après l'argent, plus dans la musique.''',
  },
  {
    'slug': 'faut-il-un-contrat-pour-un-concert',
    'h1': 'Faut-il vraiment un contrat pour un concert ?',
    'titre': 'Faut-il vraiment un contrat pour un concert ?',
    'description': "Oui, et l'écrit est obligatoire. Voici ce que la loi impose, ce qu'un contrat protège vraiment, et les douze points qu'il doit contenir.",
    'rubrique': 'Contrat',
    'motscles': "contrat d'engagement, CDDU, concert, écrit obligatoire, intermittent",
    'dek': "Oui, et l'écrit est obligatoire. Voici ce que la loi impose, ce qu'un contrat protège vraiment, et les douze points qu'il doit contenir.",
    'lecture': '6 min',
    'duree': 'PT6M',
    'public': 'Pour les artistes',
    'publie': '2026-08-15',
    'suite': ('employeur-ne-m-a-pas-paye-mon-cachet', 'ca-va-te-faire-connaitre-comment-repondre', 'evaluer-si-une-date-est-un-bon-plan'),
    'md': '''« On se connaît, on va pas s'embêter avec des papiers. » On l'a tous entendu. Parfois de la part d'un organisateur, parfois de sa propre bouche — parce que réclamer un contrat, ça fait un peu méfiant, un peu procédurier, et qu'on n'a pas envie de commencer comme ça.

Réponse courte : oui, il faut un contrat. Et pas seulement parce que ça rassure : **parce que c'est la loi**.

## Ce que la loi impose

Quand tu es engagé pour un concert, tu es **salarié**. Ton contrat est un **CDD d'usage** (CDDU), la forme de CDD propre au spectacle.

Or, en droit français, **tout CDD doit être écrit**. Ce n'est pas une option de confort, c'est une condition de validité. L'écrit doit être **transmis au salarié dans les deux jours ouvrables suivant l'embauche** au plus tard — et dans les faits, il vaut mieux qu'il soit signé avant.

L'absence d'écrit se retourne contre l'employeur : en cas de litige, elle expose à la **requalification du contrat en CDI à temps plein**. C'est une sanction lourde, et c'est précisément pour ça que la loi la prévoit — c'est ce qui rend l'écrit vraiment obligatoire, et pas seulement recommandé.

Autrement dit : quand tu demandes un contrat, tu ne fais pas une faveur ni un caprice. **Tu demandes à l'organisateur de se mettre en règle.** C'est une nuance qui change beaucoup la façon de le formuler.

## Ce que le contrat protège concrètement

Au-delà du principe, voilà ce qu'un écrit change dans la vraie vie.

**Il fige le montant.** Le « autour de 300 » du mois de mars devient 250 le jour du virement, et personne ne se souvient de la même chose. Un montant écrit ne se renégocie pas après le concert.

**Il fixe un délai de paiement.** C'est le point le plus souvent oublié, et celui qui produit le plus de retards. Sans échéance écrite, il n'y a pas de retard — juste une attente qui s'étire.

**Il dit ce qui est pris en charge.** Trajet, repas, hébergement : ce qui n'est pas écrit se transforme en malentendu à 22 h dans le parking d'une salle des fêtes.

**Il prévoit l'annulation.** Si la date saute à trois jours, tu as bloqué le week-end et refusé autre chose. Une clause d'annulation dit qui supporte quoi, à partir de quand.

**Il encadre la captation.** « On filme pour les réseaux, ça te fera de la visibilité » n'est pas un cadre. Une ligne sur les droits à l'image et l'usage des captations évite de retrouver ton set entier en ligne l'année suivante.

**Il rend le litige simple.** En cas d'impayé, un contrat transforme une affaire de parole contre parole en créance nette, avec un montant et une date. C'est ce qui fait la différence devant un conseil de prud'hommes.

## Les douze points d'un contrat d'engagement

Un contrat de concert n'a pas besoin d'être long. Il a besoin d'être complet. Voici les rubriques qui reviennent dans un modèle standard d'engagement d'artiste :

1. **Les parties** — qui emploie (raison sociale, SIRET, forme juridique, numéro de licence d'entrepreneur de spectacles quand elle est requise) et qui est employé (nom, numéro de sécurité sociale, numéro GUSO).
2. **L'objet et la nature de la prestation** — quel spectacle, quelle formation, combien de personnes sur scène, durée du set.
3. **Les dates et horaires** — arrivée, balance, passage, fin. Précis.
4. **Le lieu** — adresse exacte, pas juste le nom de la salle.
5. **La rémunération** — montant, brut ou net, nombre de cachets, répétitions rémunérées éventuelles.
6. **Le délai de paiement** — le point à ne jamais laisser vide.
7. **Les frais pris en charge** — transport, repas, hébergement, et selon quelles modalités.
8. **Les conditions techniques et la loge** — sono fournie ou à amener, ingénieur du son, taille de scène, loge, accès.
9. **Les droits d'image et la captation** — ce qui peut être filmé, photographié, diffusé, et pour quel usage.
10. **Les conditions d'annulation** — de part et d'autre, avec des délais.
11. **L'assurance et la responsabilité** — matériel, dommages, responsabilité civile.
12. **Le règlement amiable** — comment on essaie de régler un désaccord avant d'aller plus loin.

Toutes ne sont pas indispensables à chaque fois. Les six premières, plus le délai de paiement, forment le socle minimum. Le reste dépend du contexte : un festival avec captation vidéo et un bar de quartier ne demandent pas le même niveau de détail.

Deux points à ne pas oublier non plus : la mention explicite qu'il s'agit d'un **CDD d'usage** avec le motif de recours, et la **convention collective applicable**. Ce sont des mentions attendues dans un CDDU, et leur absence fragilise le contrat.

## « Et si je demande un contrat, je vais paraître compliqué ? »

Salomé (personnage fictif) est chanteuse. Elle a longtemps évité la question, de peur de refroidir. Puis elle a changé sa formulation :

> « Super, je bloque la date. Je t'envoie mes infos pour le contrat et la déclaration GUSO — comme ça tu as tout d'un coup. »

Elle ne demande plus un contrat : elle en propose un, et elle rend service. Un petit organisateur de bonne foi qui ne connaît pas le circuit est souvent **soulagé** qu'on lui mâche le travail. Et celui que ça braque t'apprend quelque chose d'utile, tout de suite.

## Contrat de travail, contrat de cession : ne pas confondre

Deux documents différents circulent dans le spectacle.

- Le **contrat de travail** (CDDU) lie l'employeur et l'artiste. C'est celui dont parle cet article, et celui qui produit tes heures.
- Le **contrat de cession** lie deux structures : un producteur qui « vend » un spectacle à un organisateur. Il porte sur le spectacle, pas sur ton salaire.

Si tu es engagé directement par la salle ou l'association, c'est un contrat de travail qu'il te faut — et, si l'employeur n'a pas le spectacle pour activité principale, une déclaration GUSO qui va avec.

## Un modèle vaut mieux qu'une page blanche

Le vrai obstacle n'est presque jamais la mauvaise foi : c'est que personne n'a de modèle sous la main, et que rédiger un contrat à 23 h après une répétition, personne n'en a envie.

**Guso Facile** proposera bientôt un générateur de contrat d'engagement construit sur ces douze rubriques, avec un texte type à adapter pour chacune, la possibilité d'enregistrer ton propre modèle, de l'imprimer et de le copier dans un mail. C'est un modèle indicatif : il ne remplace ni un professionnel du droit, ni ton syndicat, et il s'adapte avant chaque signature. L'app est en bêta, accessible sur cooptation.

Poser le cadre avant, c'est ce qui évite le plus de problèmes après. Moins d'énergie dans les malentendus, plus dans la musique.''',
  },
  {
    'slug': 'c-est-quoi-le-guso-concretement',
    'h1': "C'est quoi le GUSO, concrètement ?",
    'titre': "C'est quoi le GUSO, concrètement ?",
    'description': 'Le guichet unique qui permet à un employeur occasionnel de déclarer un artiste en une fois. Qui déclare, ce que tu reçois, dans quels délais.',
    'rubrique': 'GUSO',
    'motscles': "GUSO, guichet unique du spectacle occasionnel, déclaration, attestation mensuelle d'emploi, intermittent",
    'dek': 'Le guichet unique qui permet à un employeur occasionnel de déclarer un artiste en une fois. Qui déclare, ce que tu reçois, dans quels délais.',
    'lecture': '6 min',
    'duree': 'PT6M',
    'public': 'Pour les artistes',
    'publie': '2026-08-15',
    'suite': ('comment-declarer-une-repetition', 'structure-comment-gerer-les-guso-de-mes-artistes', 'ne-plus-jamais-oublier-une-dpae'),
    'md': '''Tu as joué, on t'a demandé ton « numéro GUSO », tu as reçu un feuillet quelques semaines plus tard, et honnêtement tu n'as jamais bien su ce qu'était ce truc. C'est très commun. Le GUSO est au cœur de la vie administrative d'un musicien, et pourtant presque personne ne te l'explique en entier.

Voici la version claire.

## GUSO = Guichet Unique du Spectacle Occasionnel

C'est un dispositif public, gratuit, dont la logique tient en un mot : **guichet unique**.

Sans lui, un employeur qui engage un artiste pour une soirée devrait s'inscrire auprès de l'URSSAF, de la retraite complémentaire, de la prévoyance, des congés spectacles, de l'assurance chômage, de la formation professionnelle et de la médecine du travail. Autant dire que personne ne le ferait, et que tout le monde jouerait au noir.

Le GUSO fait tout ça **en une seule déclaration**. L'employeur déclare une fois, paie une fois, et le guichet répartit vers les organismes concernés. C'est le service qui rend l'embauche légale d'un artiste accessible à une association de village.

## Qui doit passer par le GUSO ?

Deux conditions, cumulatives :

1. L'employeur **n'a pas le spectacle pour activité principale** — il n'exploite pas de lieu de spectacle et ne produit ni ne diffuse de spectacles à titre principal ;
2. il engage **occasionnellement**, en CDD, des artistes ou des techniciens du spectacle vivant.

Ça couvre une immense partie de ce qu'un musicien joue vraiment : associations, communes et collectivités, comités d'entreprise, restaurants, hôtels, campings, entreprises, écoles, particuliers, établissements publics.

À l'inverse, une salle de spectacle, un festival professionnel ou une compagnie dont c'est le métier **ne passent pas par le GUSO** : ils sont employeurs à titre principal et déclarent par leurs propres circuits. Recevoir un contrat sans GUSO n'est donc pas un signal d'alarme en soi — encore faut-il que l'employeur soit bien dans ce cas.

Le point important pour toi : **quand le GUSO s'applique, il est obligatoire**. Ce n'est pas au choix de l'organisateur.

## Qui déclare ? Pas toi.

C'est **l'employeur** qui déclare. Toujours. Toi, tu es le salarié.

Ton rôle se limite à deux choses :

- **Adhérer une fois** au GUSO, avec ton numéro de sécurité sociale. Un **numéro GUSO** personnel t'est attribué, et il te suivra pour tous tes employeurs occasionnels.
- **Fournir tes informations** à chaque employeur : identité, date de naissance, numéro de sécurité sociale, numéro GUSO, coordonnées bancaires.

C'est tout. Si un organisateur te demande de « faire le GUSO toi-même », quelque chose ne va pas dans le montage — et ça mérite une conversation avant la date, pas après.

## Ce que tu reçois

Deux documents comptent pour toi.

**L'attestation mensuelle d'emploi (AME).** Le GUSO te l'envoie, et elle **vaut bulletin de salaire**. C'est ta preuve d'emploi : dates, employeur, nombre de cachets ou d'heures, montants. Garde-les toutes, sans exception. C'est ce qu'on te demandera en cas de contrôle, de litige ou de désaccord avec France Travail.

**Ton salaire**, versé par l'employeur.

En parallèle, et sans que tu aies rien à faire, le GUSO transmet à **France Travail Spectacle** l'**attestation d'emploi mensuelle (AEM)** correspondante. C'est par ce canal que tes heures arrivent dans ton compteur des 507 heures. Tu n'as pas à envoyer tes feuillets à France Travail toi-même.

## Les délais à connaître

- **La déclaration** peut être faite **jusqu'à un mois avant** la prestation, et **au plus tard dans les 15 jours suivant la fin du contrat**. En clair : la fenêtre est courte après la date. Un employeur qui « fera ça à la rentrée » est déjà hors délai.
- **La DPAE** (déclaration préalable à l'embauche) doit intervenir **avant** que tu ne commences à travailler — au plus tôt dans les huit jours précédant l'embauche. Elle se fait via le site du GUSO quand l'employeur passe par ce dispositif. Sur son articulation exacte avec la déclaration principale, les pratiques varient selon les situations : le mieux est de s'appuyer sur le site officiel **guso.fr** ou d'appeler leur service, qui répond aux employeurs comme aux salariés.
- **Les cotisations** sont dues dans les jours qui suivent la fin du contrat. Un retard expose l'employeur à des majorations.

Ce que ça implique concrètement : la période autour de la date est plus tendue qu'on ne croit. Une DPAE avant, une déclaration dans les quinze jours après. C'est très exactement là que se perdent les heures des gens.

## Ce que le GUSO n'est pas

- **Ce n'est pas France Travail.** Le GUSO déclare et collecte ; France Travail Spectacle indemnise. Deux organismes, deux interlocuteurs. Une heure déclarée au GUSO qui n'apparaît pas chez France Travail, ça se vérifie des deux côtés.
- **Ce n'est pas un statut.** « Être au GUSO » ne veut rien dire : le GUSO est un canal de déclaration, pas un régime. Ton statut, c'est celui de salarié intermittent, sous annexe 8 ou 10.
- **Ce ne sont pas les sessions de studio.** L'enregistrement phonographique relève d'un autre circuit, souvent réglé par chèque-intermittents, hors GUSO — même si ces cachets comptent bien dans tes heures.
- **Ce n'est pas gratuit pour l'employeur** au sens des charges : le GUSO simplifie la démarche, il ne réduit pas les cotisations. Un cachet coûte nettement plus cher que le net que tu touches. C'est utile à savoir quand on négocie avec une petite structure de bonne foi qui découvre la facture.

## Le réflexe qui évite 90 % des ennuis

Après chaque date, une seule question : **est-ce que la déclaration a été faite ?** Puis, quelques semaines plus tard : **est-ce que j'ai bien reçu mon attestation ?**

Théo (personnage fictif), accordéoniste, s'en est rendu compte trop tard : deux dates d'un même été n'avaient jamais été déclarées par une association débordée. Vingt-quatre heures manquantes, découvertes onze mois plus tard. À ce moment-là, tout est plus difficile — sauf la mauvaise humeur.

**Guso Facile** suit ce cycle date par date : DPAE à faire avec un compte à rebours, feuillet GUSO reçu ou non, facture, salaire encaissé. Tu vois d'un coup d'œil ce qui manque, tant qu'il est encore temps d'agir. L'app est en bêta, accessible sur cooptation.

Moins d'énergie dans le suivi, plus dans la musique.''',
  },
  {
    'slug': 'comment-declarer-une-repetition',
    'h1': 'Comment déclarer une répétition ?',
    'titre': 'Comment déclarer une répétition ?',
    'description': "En heures ou en cachet, c'est l'employeur qui déclare — et seule une répétition rémunérée compte. Le mode d'emploi et les erreurs fréquentes.",
    'rubrique': 'GUSO',
    'motscles': 'répétition, déclaration, heures, cachet, intermittent',
    'dek': "En heures ou en cachet, c'est l'employeur qui déclare — et seule une répétition rémunérée compte. Le mode d'emploi et les erreurs fréquentes.",
    'lecture': '5 min',
    'duree': 'PT5M',
    'public': 'Pour les artistes',
    'publie': '2026-08-15',
    'suite': ('c-est-quoi-le-guso-concretement', 'combien-de-cachets-pour-507-heures', 'ne-plus-jamais-oublier-une-dpae'),
    'md': '''Les répétitions sont le grand angle mort du compteur d'heures. On en fait énormément, on en déclare peu, et quand on essaie de rattraper le coup en fin de période, on découvre que ça ne s'improvise pas.

Voici comment ça marche vraiment.

## Le principe : une répétition se déclare comme du travail

Une répétition rémunérée est du **temps de travail salarié**, au même titre qu'un concert. Elle se déclare, elle produit des cotisations, et elle produit des **heures** qui comptent pour tes 507.

La condition tient en un mot : **rémunérée**. Une répétition que tu fais avec ton groupe, dans un local que vous payez, sans employeur et sans salaire, n'est pas déclarable. Ce n'est pas une injustice administrative à contourner : c'est simplement qu'il n'y a pas d'employeur. Il n'y a rien à déclarer.

Donc, avant toute question de formulaire, la vraie question est en amont : **est-ce que le budget de la date prévoit des répétitions payées ?** C'est une question de négociation, pas de paperasse.

## Heures ou cachet ?

Deux façons de rémunérer une répétition coexistent.

**En heures.** L'employeur déclare le nombre d'heures réellement effectuées, payées au taux horaire applicable. Quatre heures de répétition, ce sont quatre heures dans ton compteur. C'est la forme la plus fréquente pour des répétitions ponctuelles.

**En cachet.** Une journée de répétition peut aussi être rémunérée sous forme de cachet. Dans ce cas, elle est valorisée comme n'importe quel cachet d'artiste : **12 heures** pour France Travail. Une journée de répétition payée au cachet « rapporte » donc plus d'heures qu'une journée déclarée en 7 heures réelles.

Ce n'est pas toi qui choisis dans ton coin : la forme dépend de l'employeur, du budget, et de la convention collective applicable. Mais c'est une chose parfaitement légitime à **évoquer au moment de fixer les conditions**, avant de signer. « Est-ce que les répétitions sont prévues, et sous quelle forme ? » n'est pas une question déplacée.

## Qui déclare, et comment

Comme pour les concerts : **c'est l'employeur**.

Quand il s'agit d'un employeur occasionnel qui passe par le GUSO, le principe est simple et souvent mal appliqué : **les répétitions se déclarent avec le spectacle, sur la même déclaration**, dès lors qu'elles se rattachent au même engagement. Les heures de répétition rémunérées apparaissent alors en plus des cachets, comme telles.

Il faut aussi, comme pour tout, une **DPAE** couvrant la période de travail. Une bonne nouvelle sur ce point : une même déclaration préalable peut couvrir **plusieurs dates rapprochées** — typiquement une semaine avec deux répétitions et un concert. Ça évite d'en multiplier une par jour de présence.

## Les erreurs fréquentes

**1. Croire que ça se rattrape après coup.** La déclaration au GUSO doit intervenir au plus tard dans les **15 jours suivant la fin du contrat**. Une répétition de mars ne se déclare pas en octobre parce qu'on s'aperçoit qu'il manque des heures. Les heures oubliées sont, dans les faits, très difficiles à récupérer.

**2. Ne pas parler des répétitions au moment de négocier.** C'est l'erreur la plus coûteuse, et elle n'est pas administrative. Un budget se discute avant, jamais après. Beaucoup de structures acceptent de prévoir une ou deux répétitions payées si la demande arrive au bon moment — et refusent, à raison, de rouvrir un budget déjà bouclé.

**3. Confondre répétition et balance.** Le temps de balance et d'installation le jour même fait partie de l'engagement du concert. Ce n'est pas une répétition supplémentaire à déclarer en plus.

**4. Ne pas vérifier ce qui a été déclaré.** Les heures de répétition sont, de loin, celles qui se perdent le plus souvent en route. Elles se rajoutent à la main sur la déclaration, donc elles s'oublient à la main aussi. Quand tu reçois ton attestation mensuelle d'emploi, regarde si les heures de répétition y figurent. Si elles manquent, signale-le tout de suite à l'employeur : sur le moment, c'est une correction ; six mois plus tard, c'est un dossier.

**5. Déclarer des répétitions non payées.** Ça n'existe pas, et ça n'a rien d'un détail : ce serait une fausse déclaration.

**6. Oublier que ça vaut aussi pour les résidences et les créations.** Une résidence rémunérée est du travail déclarable. Beaucoup d'artistes n'y pensent pas, parce que ça ne « ressemble » pas à un concert.

## Un exemple concret

Elsa (personnage fictif) est clarinettiste dans un projet créé pour un festival associatif. L'engagement prévoit trois répétitions de 4 heures et deux concerts.

- 2 concerts = 2 cachets = **24 h**
- 3 × 4 h de répétitions rémunérées = **12 h**

Total : **36 heures** pour cet engagement, contre 24 si les répétitions étaient passées à la trappe. Sur une année, ce genre d'écart se compte en semaines de travail.

L'employeur déclare l'ensemble sur la même déclaration GUSO, avec une DPAE couvrant la période. Elsa vérifie, à réception de son attestation, que les 12 heures de répétition y sont bien.

## Quand tu as un doute, demande

La forme exacte de la rémunération d'une répétition dépend de la convention collective applicable, du type d'employeur et de l'engagement. Les règles ne sont pas identiques partout, et elles évoluent.

Les bons interlocuteurs : le **GUSO** (guso.fr) pour la mécanique de déclaration, **France Travail Spectacle** pour la prise en compte dans tes droits, et ton **syndicat** (SNAM-CGT, SFA-CGT et d'autres) pour tout ce qui touche à la convention collective et au taux horaire applicable. Aucune app, celle-ci comprise, ne remplace ces trois-là.

## Ne plus perdre ces heures-là

Les heures de répétition sont les plus faciles à oublier, et souvent celles qui font passer un compteur de 480 à 507.

**Guso Facile** te permet de saisir une date de type « répétition », d'y noter les heures rémunérées personne par personne, et de les voir apparaître distinctement dans ton graphique annuel — pour savoir d'où viennent vraiment tes heures. Les DPAE de dates proches sont regroupées automatiquement, et le suivi te rappelle ce qui reste à déclarer, avec un compte à rebours. L'app est en bêta, accessible sur cooptation.

Moins d'énergie perdue en heures oubliées, plus dans la musique.''',
  },
  {
    'slug': 'ca-va-te-faire-connaitre-comment-repondre',
    'h1': '« Ça va te faire connaître » : comment répondre à un organisateur qui ne veut pas payer ?',
    'titre': '« Ça va te faire connaître » : comment répondre à un organisateur qui ne veut pas payer ?',
    'description': "Comprendre le mécanisme d'inversion de la valeur, et surtout des phrases concrètes pour répondre sans se fâcher ni se dévaloriser.",
    'rubrique': 'Négociation',
    'motscles': 'cachet, visibilité, négociation, musicien, rémunération',
    'dek': "Comprendre le mécanisme d'inversion de la valeur, et surtout des phrases concrètes pour répondre sans se fâcher ni se dévaloriser.",
    'lecture': '7 min',
    'duree': 'PT7M',
    'public': 'Pour les artistes',
    'publie': '2026-08-15',
    'suite': ('faut-il-un-contrat-pour-un-concert', 'evaluer-si-une-date-est-un-bon-plan', 'employeur-ne-m-a-pas-paye-mon-cachet'),
    'md': '''« Tu vas jouer devant du monde, ça va te faire connaître. »
« On n'a pas de budget, mais il y aura des gens qui comptent dans la salle. »
« Tu as de la chance de jouer ici. »

Tu as déjà lu ces phrases. Probablement plusieurs fois cette année. Et tu as probablement, au moins une fois, dit oui en te sentant vaguement mal — sans savoir si c'était toi qui étais trop exigeant.

Cet article ne va pas t'apprendre à claquer des portes. Il va faire deux choses : **nommer ce qui se passe** dans cette phrase, et te donner **des formulations utilisables** dès demain matin.

## Le mécanisme : l'inversion de la valeur

Voilà ce que fait cette phrase, très précisément.

Tu apportes ton travail, tes années de pratique, ton matériel, ton déplacement, ton temps de préparation. En face, on te propose une place dans un programme. Dans une transaction ordinaire, celui qui reçoit une prestation la rémunère.

La phrase renverse ce sens. **Celui qui devrait payer devient celui qui offre une opportunité.** Et toi, qui apportes la valeur, tu te retrouves en position de recevoir une faveur — et donc de devoir remercier.

Ce n'est pas de la manipulation consciente dans la plupart des cas. C'est une croyance sincèrement partagée : l'idée que jouer est déjà une récompense en soi.

Et si ça fonctionne aussi bien, c'est parce que ça appuie sur quelque chose de vrai. **Un artiste a besoin de jouer pour exister.** Pas seulement pour gagner sa vie : pour être entendu, pour progresser, pour ne pas disparaître. Ce besoin est réel et parfaitement légitime. Il est aussi, exactement, le levier sur lequel s'appuie l'inversion. On ne négocie jamais bien quand on a peur de ne plus jouer.

Ce n'est donc pas une faiblesse de caractère. C'est un mécanisme, et il est ordinaire. **Le nommer lui enlève déjà la moitié de son pouvoir.**

## Avant de répondre : distinguer deux situations

Une bonne partie des organisateurs qui prononcent cette phrase sont **de bonne foi et sans budget**. Une association de village, un bar qui survit, un collectif étudiant : ils ne cherchent pas à profiter de toi, ils n'ont réellement pas d'argent, et souvent ils ne savent même pas ce que coûte un cachet déclaré.

À côté, il y a des structures qui ont un budget, qui paient le son, la sécurité, la bière et la communication — mais pas les artistes, parce que ça se fait comme ça.

**Ce ne sont pas les mêmes conversations.** Avec les premiers, tu peux construire quelque chose. Avec les seconds, tu poses un cadre. Dans les deux cas, tu restes digne — et surtout, tu ne fais le procès de personne.

## Des phrases qui marchent

### 1. Demander avant de refuser

Le premier réflexe le plus utile n'est pas de dire non : c'est de faire exister la question du budget.

> « Merci pour la proposition, le projet m'intéresse. Quel budget est prévu pour les artistes ? »

Neutre, courte, professionnelle. Elle présuppose qu'il y a un budget, ce qui déplace la discussion sans agresser personne. Beaucoup de conversations se règlent là.

### 2. Répondre à l'argument de la visibilité, sans ironie

> « La visibilité, j'y suis sensible — mais elle ne remplace pas le cachet, elle s'ajoute. De mon côté, une date, c'est du travail déclaré : contrat, GUSO, heures. C'est ce qui me permet de continuer à jouer l'année prochaine. »

Ce qui fait le travail ici, c'est le **« s'ajoute »**. Tu ne nies pas la valeur de ce qu'on te propose, tu refuses juste qu'elle se substitue au salaire. Et tu expliques pourquoi, factuellement : sans heures déclarées, pas de droits, donc pas de métier.

### 3. Quand il n'y a vraiment pas de budget

Ne fais pas semblant de croire qu'il y en a un. Propose autre chose :

> « Je comprends, et je préfère qu'on soit clairs plutôt qu'on s'arrange mal. Sur ce format-là, je ne peux pas jouer sans être déclaré. Ce que je peux proposer : [une formule plus légère / une date où vous aurez du budget / un partage de recette avec un minimum garanti]. Si ça ne colle pas cette fois, ça me fera plaisir de retravailler avec vous quand ce sera possible. »

Cette réponse fait trois choses : elle dit non sans mépris, elle laisse une porte ouverte, et elle donne à l'organisateur une **solution** au lieu d'un problème. C'est souvent celle qui débouche sur une vraie date six mois plus tard.

### 4. Aider celui qui ne sait pas comment faire

Beaucoup de refus ne sont pas des refus de payer : ce sont des refus de paperasse. « On ne sait pas faire », « c'est trop compliqué », « on n'est pas une salle ».

> « C'est plus simple que ça en a l'air : le GUSO est fait exactement pour les structures comme la vôtre. Une déclaration, un paiement, tout est réparti ensuite. Je vous envoie mes informations et un modèle de contrat, vous n'aurez qu'à compléter. »

Là, tu ne demandes plus : tu enlèves l'obstacle. C'est souvent ce qui transforme un « non » en « ah, d'accord ».

### 5. Le mail de synthèse, après un accord oral

> « Super pour le [date]. Je récapitule ce qu'on s'est dit : [nombre] musiciens, set de [durée], balance à [heure], cachet de [montant] par personne, trajet [pris en charge / non], paiement sous [délai]. Je t'envoie le contrat pour signature — dis-moi si j'ai mal noté quelque chose. »

Ce message ne coûte rien et évite les trois quarts des litiges. Il transforme une conversation en engagement, sans qu'aucun des deux n'ait eu à « demander un contrat ».

### 6. Si on te met la pression

> « Je comprends que tu aies besoin d'une réponse. La mienne est celle-là. Si ça change de votre côté, écris-moi, ça m'intéressera toujours. »

Une seule phrase, aucune justification supplémentaire. **Se justifier trop, c'est rouvrir la négociation.**

## Trois principes qui aident, plus que n'importe quelle phrase

**Décide avant, pas pendant.** Si tu sais à l'avance ton cachet minimum, ta distance acceptable et ce que tu es prêt à accepter en échange, tu ne décides plus sous le coup de l'émotion ni de la culpabilité. Tu compares une offre à des critères. C'est infiniment plus simple.

**Toutes les dates gratuites ne sont pas des abus.** Un bœuf entre amis, une scène ouverte, un projet associatif auquel tu tiens : ce sont des choix, et ce sont de bons choix. La différence, c'est que tu les as *choisis*, en sachant ce que tu donnes. Le problème n'est pas la gratuité : c'est la gratuité subie.

**Tu ne joues pas que pour toi.** Chaque cachet accepté sous le prix fixe le prix pour celui qui passera après. C'est exactement pour ça qu'on s'organise en collectif : celui qui a le plus besoin de la date suivante est celui qui parlera le moins, et c'est pour lui que le reste du métier tient la ligne.

## Poser le cadre avant, se dire les faits après

L'immense majorité des mauvaises expériences ne viennent pas de la mauvaise foi. Elles viennent d'**un cadre jamais posé** : pas de contrat, des conditions dites à l'oral, un montant « on verra », un délai de paiement jamais évoqué.

C'est là que se joue l'essentiel, et c'est la partie sur laquelle tu as vraiment la main.

**Guso Facile** t'aide déjà sur l'amont : tu définis une fois tes conditions idéales (cachet minimum, distance, trajet, logement, technique, visibilité), puis tu compares chaque proposition à tes propres critères — verdict à l'appui — et l'app génère un message poli qui demande précisément les informations manquantes à l'organisateur. Négocier sans avoir à trouver les mots.

Viendront bientôt un **générateur de contrat d'engagement** en douze rubriques, et la **Guilde** : un espace réservé aux membres où les artistes partagent, entre pairs, des faits vérifiables — contrat fourni ou non, paiement dans les délais ou non, conditions tenues ou non. Pas d'avis, pas de récit, pas de tribunal : l'information qui circule déjà en loge, mais fiable et accessible **avant** de signer. L'app est en bêta, accessible sur cooptation.

Une phrase nommée perd la moitié de son pouvoir. Un cadre posé lui enlève l'autre moitié — et laisse toute l'énergie à la musique.''',
  },
  {
    'slug': 'heures-ne-correspondent-pas-france-travail',
    'h1': 'Pourquoi mes heures ne correspondent pas à celles de France Travail ?',
    'titre': 'Pourquoi mes heures ne correspondent pas à celles de France Travail ?',
    'description': "Déclaration manquante, décalage de mois, répétitions oubliées, annexe 8 ou 10 : les causes courantes d'un écart, et comment vérifier soi-même.",
    'rubrique': 'France Travail',
    'motscles': 'France Travail Spectacle, heures manquantes, AEM, annexe 8, annexe 10',
    'dek': "Déclaration manquante, décalage de mois, répétitions oubliées, annexe 8 ou 10 : les causes courantes d'un écart, et comment vérifier soi-même.",
    'lecture': '6 min',
    'duree': 'PT6M',
    'public': 'Pour les artistes',
    'publie': '2026-08-15',
    'suite': ('quand-tombe-ma-date-anniversaire', 'pointage-france-travail-sans-stress', 'combien-de-cachets-pour-507-heures'),
    'md': '''Tu comptes 462 heures. France Travail en affiche 431. Trente et une heures d'écart, et personne à qui poser la question avant lundi.

Ce moment est désagréable, mais il est très fréquent — et dans la grande majorité des cas, l'écart s'explique. Voici les causes, de la plus courante à la plus rare, et la méthode pour le régler toi-même.

## Règle d'or : c'est le chiffre de France Travail qui compte

Avant tout : ton tableau à toi n'a aucune valeur officielle. Seules les **déclarations reçues** par France Travail ouvrent des droits.

Ce n'est pas une raison pour ne pas compter de ton côté — au contraire. Ton compteur personnel ne sert pas à *remplacer* le leur : il sert à **détecter un écart assez tôt pour le corriger**. C'est toute sa valeur.

## Cause n° 1 — Une déclaration n'a jamais été faite

C'est, de loin, la première cause.

La date a eu lieu, tu as peut-être même été payé, mais l'employeur n'a pas déclaré — oubli, association débordée, personne partie, dossier bloqué. Rappel du calendrier : la déclaration au GUSO doit intervenir **au plus tard dans les 15 jours suivant la fin du contrat**. Passé ce délai, ça devient un problème.

**Comment le vérifier :** as-tu reçu l'**attestation mensuelle d'emploi** du GUSO pour cette date ? Si oui, la déclaration existe. Si non, appelle l'employeur avant d'appeler qui que ce soit d'autre.

## Cause n° 2 — Un décalage de mois, pas une perte

Une déclaration faite le 3 du mois suivant peut apparaître sur un mois différent de celui où tu situes la date dans ta tête. Ton attestation d'actualisation, ton relevé et ton tableau ne se calent pas forcément sur le même découpage.

**Comment le vérifier :** compare sur **deux ou trois mois consécutifs**, pas sur un seul. Si le total sur trois mois tombe juste, il n'y a pas d'écart — juste un décalage. Beaucoup de fausses alertes s'arrêtent là.

## Cause n° 3 — Des heures de répétition qui n'ont pas suivi

Les heures de répétition rémunérées se déclarent **en plus** des cachets, et elles s'ajoutent souvent à la main sur la déclaration. Donc elles s'oublient à la main aussi.

C'est le type d'écart le plus discret : les cachets sont là, tout a l'air normal, et il manque douze heures.

**Comment le vérifier :** reprends tes engagements avec répétitions payées et regarde, ligne par ligne, si les heures figurent sur ton attestation.

## Cause n° 4 — Tu comptes des heures qui ne comptent pas

Écart dans l'autre sens, tout aussi fréquent :

- des **répétitions non rémunérées** que tu as notées « parce que tu les as faites » ;
- des **dates encore en projet**, pas confirmées, glissées dans le total par optimisme ;
- des **prestations non salariées** (facturées en indépendant) : elles ne produisent aucune heure d'intermittence ;
- des **heures d'enseignement au-delà du plafond** : elles sont retenues dans la limite de 70 heures, portées à 120 si tu as 50 ans ou plus à la fin du contrat retenu pour l'ouverture des droits. Au-delà, elles ne comptent plus ;
- des **cachets au-delà de 28 sur un même mois** : le nombre de cachets retenus par mois est plafonné.

## Cause n° 5 — Tu ne regardes pas la même période

Ton compteur court sur les **365 jours précédant ta date anniversaire**. Si tu comptes en année civile, ou depuis une date approximative, ton total sera faux — parfois de beaucoup, surtout si tu as un été chargé qui « sort » de la fenêtre.

**Comment le vérifier :** confirme ta date anniversaire dans ton espace France Travail Spectacle, puis recompte sur la bonne fenêtre. Un article de ce blog y est consacré.

## Cause n° 6 — Annexe 8, annexe 10, et ce que ça change

Si tu fais à la fois de l'artistique (annexe 10) et de la technique (annexe 8), les deux types d'heures **se cumulent pour atteindre les 507**. En revanche, l'annexe sous laquelle tu es indemnisé est, en principe, celle où tu as le plus d'heures sur la période — et cela peut changer les paramètres de ton indemnisation.

C'est un point technique où les sources en ligne se contredisent souvent, et où ta situation personnelle compte. **Ne tranche pas ça seul** : c'est exactement le genre de question à poser à ton conseiller France Travail Spectacle ou à ton syndicat.

## Cause n° 7 — Une erreur sur la déclaration elle-même

Un mauvais nombre de cachets, un numéro de sécurité sociale erroné, une date de fin de contrat fausse, ton nom mal orthographié : la déclaration existe, mais elle ne se rattache pas correctement à ton dossier, ou elle porte de mauvais chiffres.

**Comment le vérifier :** relis ton attestation. Compare avec ton contrat. Une erreur de saisie se corrige beaucoup plus facilement que ce qu'on imagine, à condition de la signaler tôt.

## La méthode de vérification, en cinq étapes

1. **Confirme ta date anniversaire** et la période exacte à examiner.
2. **Liste tes dates** sur cette période : lieu, dates, employeur, cachets, heures de répétition.
3. **Rapproche chaque ligne d'une attestation mensuelle d'emploi.** Une ligne sans attestation = une déclaration à réclamer.
4. **Compare mois par mois** avec le relevé de ton espace France Travail Spectacle. Regarde sur plusieurs mois avant de conclure.
5. **Isole les écarts** et traite-les un par un, chacun avec le bon interlocuteur.

## À qui s'adresser, selon le cas

- **L'employeur** : déclaration manquante, erreur de chiffres, heures de répétition oubliées. C'est lui qui déclare, c'est donc lui qui corrige.
- **Le GUSO** (guso.fr) : savoir si une déclaration te concernant a bien été enregistrée, et comment la rectifier.
- **France Travail Spectacle** : ce qui a été reçu, la période retenue, l'annexe appliquée. C'est la seule source qui fait foi sur ton dossier.
- **Ton syndicat** (SNAM-CGT, SFA-CGT et d'autres) : un employeur qui ne répond pas, un dossier qui n'avance pas, une règle que personne n'arrive à te confirmer.
- **L'inspection du travail** (DREETS) : une date jamais déclarée du tout, malgré tes relances.

Et un réflexe qui vaut tout le reste : **agis avant ta date anniversaire.** Un écart repéré en février se répare. Le même écart découvert trois jours avant l'échéance, beaucoup moins.

## Garder ses propres chiffres, pour pouvoir les défendre

Ce qui rend ces vérifications pénibles, ce n'est pas leur difficulté : c'est de devoir reconstituer une année entière depuis des mails, des SMS et des PDF éparpillés.

**Guso Facile** garde ta ligne de compte, date par date : cachets, heures de répétition, type d'activité, feuillet GUSO reçu ou non. Un **récap mensuel** te présente tes dates regroupées par déclaration et par mois — pensé pour se rapprocher de ton actualisation — et un **bilan imprimable** signale les incohérences avant que tu ne les découvres trop tard. De quoi arriver à un échange avec un dossier, pas avec une impression. L'app est en bêta, accessible sur cooptation.

Moins d'énergie dans les recomptages, plus dans la musique.''',
  },
  {
    'slug': 'm-organiser-quand-je-joue-dans-plusieurs-groupes',
    'h1': "Comment m'organiser quand je joue dans plusieurs groupes ?",
    'titre': "Comment m'organiser quand je joue dans plusieurs groupes ?",
    'description': "Un seul compteur, plusieurs sources : comment suivre ses heures, savoir qui déclare quoi, et s'entraider entre membres sans se marcher dessus.",
    'rubrique': 'Duo & groupe',
    'motscles': 'plusieurs groupes, 507 heures, compteur, déclaration, intermittent',
    'dek': "Un seul compteur, plusieurs sources : comment suivre ses heures, savoir qui déclare quoi, et s'entraider entre membres sans se marcher dessus.",
    'lecture': '6 min',
    'duree': 'PT6M',
    'public': 'Pour les artistes',
    'publie': '2026-08-15',
    'suite': ('combien-de-cachets-pour-507-heures', 'travailler-a-deux-artistes-dates-partagees', 'ne-plus-jamais-oublier-une-dpae'),
    'md': '''Un quartet le vendredi, un duo le samedi, des remplacements dans un orchestre, deux sessions studio et une création en résidence. C'est la vie normale d'un musicien qui travaille — et c'est un cauchemar administratif, parce que chaque projet a son fonctionnement, son interlocuteur et son rythme.

La bonne nouvelle : côté droits, c'est plus simple qu'il n'y paraît.

## Un seul compteur, quel que soit le nombre de groupes

Le point le plus important, et celui qui rassure : **tes 507 heures sont à toi, pas à tes projets**.

Peu importe que tes heures viennent d'un groupe, de cinq, d'un remplacement isolé ou d'une session studio : elles s'additionnent toutes dans le même compteur, sur la même période de référence, avec la même date anniversaire.

Tu n'as donc **pas** à suivre un compteur par formation. Tu as un compteur, alimenté par plusieurs sources.

Ce qui change avec le nombre de groupes, ce n'est pas le calcul : c'est le **risque de fuite**. Plus il y a d'interlocuteurs, plus il y a de déclarations susceptibles de se perdre — et moins tu as de visibilité sur ce que chacun a fait.

## Qui déclare quoi : la question à poser à chaque projet

Chaque groupe a son montage, et tu dois savoir lequel. Trois cas typiques :

**1. L'organisateur t'emploie directement.** C'est lui qui déclare, généralement via le GUSO s'il n'a pas le spectacle pour activité principale. Chaque membre du groupe est employé séparément : il y a autant de déclarations que de musiciens.

**2. Une structure porte le projet** — association, compagnie, bureau de production, structure d'accompagnement avec licence. C'est elle qui emploie tout le monde, elle qui facture l'organisateur, elle qui déclare. C'est le montage le plus confortable pour toi, et souvent celui qui coûte une commission — normale, elle paie un vrai travail.

**3. Le montage est flou.** « On verra », « c'est Untel qui gère », « on se répartit après ». C'est là que se perdent les heures. Si personne ne sait dire *qui est l'employeur*, il n'y a probablement pas encore d'employeur.

**La question à poser, projet par projet :** *qui est l'employeur sur cette date, et qui fait la déclaration ?* Une phrase. Pose-la au moment où la date se cale, pas la veille.

## Attention aux dates « du même jour » et aux quiproquos

Deux pièges classiques quand on multiplie les formations.

**Le double engagement.** Une date bloquée oralement dans un projet, une autre acceptée dans un second, et personne n'avait noté. Le seul remède est un calendrier unique où **toutes** tes dates figurent, y compris celles qui ne sont pas confirmées — marquées comme telles.

**La DPAE oubliée sur la petite date.** Les gros projets sont souvent bien tenus ; c'est la date de dépannage, calée en dix jours, qui passe entre les mailles. Rappel utile : une même déclaration préalable peut couvrir **plusieurs dates rapprochées** — pratique quand tu enchaînes une répétition et deux concerts dans la même semaine, même contexte.

## Ce que tu dois garder de ton côté

Tu ne peux pas déclarer à la place de tes employeurs. Mais tu peux tenir la seule chose que personne d'autre ne tiendra : **la vue d'ensemble**.

Pour chaque date, quel que soit le projet, note :

- la **date** et le **lieu** ;
- le **projet ou groupe** concerné ;
- l'**employeur** réel (pas le nom du groupe : la structure qui déclare) ;
- le **nombre de cachets** et les **heures de répétition** rémunérées ;
- où en sont la **DPAE**, la **déclaration**, le **paiement** ;
- l'**attestation mensuelle d'emploi** reçue ou non.

Cinq minutes après chaque date valent mieux qu'une journée de reconstitution en juin.

Et le réflexe qui sauve : à chaque attestation reçue, **coche**. Ce qui n'est jamais coché au bout d'un mois est ce qu'il faut aller réclamer.

## L'entraide entre membres : ce qui marche vraiment

Dans un groupe, l'administratif finit presque toujours sur les épaules d'une seule personne. Ça tient un temps, puis ça craque — et c'est souvent là qu'un groupe se fâche pour des raisons qui n'ont rien de musical.

Quelques pratiques qui fonctionnent :

**Désigner un référent administratif par projet**, et le dire à voix haute. Pas « celui qui s'en occupe naturellement » : quelqu'un qui a accepté le rôle. Et si le projet génère du revenu, se demander honnêtement si ce travail doit être rémunéré.

**Faire circuler les informations une fois pour toutes.** Numéro de sécurité sociale, numéro GUSO, date de naissance, RIB : chacun les transmet une fois, dans un endroit sûr, plutôt que de les redemander par SMS à 23 h la veille d'une DPAE. Ce sont des données sensibles : elles se transmettent à des gens de confiance, pas dans une conversation de groupe ouverte.

**Se dire où on en est.** Un tour de table trimestriel — « t'en es à combien ? » — n'a rien d'indiscret. C'est même le seul moyen de repérer que quelqu'un décroche pendant qu'il est encore temps.

**Aider celui qui est en retard.** Un membre à 380 heures en mars et un autre à 520, ce n'est pas la même année. Passer deux dates, proposer un remplacement, penser à quelqu'un pour un dépannage : c'est plus efficace que n'importe quel conseil. C'est aussi ce qui fait qu'un groupe dure.

Bastien (personnage fictif) joue dans trois formations. En janvier, il s'est aperçu qu'un des trois n'avait déclaré aucune des répétitions payées de l'automne — sur les deux autres, tout était nickel. Sans vue d'ensemble, il l'aurait découvert en novembre. Avec, il a réglé ça en un mail.

## Ne pas mélanger ses données personnelles avec celles du groupe

Deux principes simples :

- Ce qui relève de **ton dossier** (heures, droits, montants, date anniversaire) est à toi. Personne n'a besoin de connaître tes montants pour t'aider.
- Ce qui relève de **la date** (qui joue, qui déclare, quelle DPAE, quel feuillet) se partage, avec les gens concernés.

Une entraide utile n'exige jamais qu'on expose ses revenus.

## Une vue par groupe, sans tout mélanger

**Guso Facile** est construit pour ce cas de figure. Chaque date peut être rattachée à un **groupe** ou un projet, ce qui te permet de voir d'où viennent réellement tes heures — sans jamais éclater ton compteur, qui reste unique. Une **vue groupe** permet de veiller les uns sur les autres, en toute transparence et **avec le consentement de chacun** : on voit où en sont les membres, jamais leurs montants.

Les **dates partagées** entre plusieurs artistes se saisissent une seule fois et comptent pour chacun, avec des heures de répétition et une **DPAE distinctes par personne** — puisque chaque personne a la sienne. Chacun garde son tableau de bord, ses 507 heures et sa propre date anniversaire. L'app est en bêta, accessible sur cooptation.

Jouer dans cinq groupes ne devrait pas coûter cinq fois plus d'administratif. Moins d'énergie dans le suivi, plus dans la musique.''',
  },
  {
    'slug': 'structure-comment-gerer-les-guso-de-mes-artistes',
    'h1': 'Je suis une structure : comment gérer les GUSO de mes artistes ?',
    'titre': 'Je suis une structure : comment gérer les GUSO de mes artistes ?',
    'description': 'Pour les associations et petits organisateurs : vos obligations réelles, les pièges qui coûtent cher, et une méthode simple pour ne rien oublier.',
    'rubrique': 'Structures',
    'motscles': 'association, GUSO, DPAE, employeur occasionnel, contrat',
    'dek': 'Pour les associations et petits organisateurs : vos obligations réelles, les pièges qui coûtent cher, et une méthode simple pour ne rien oublier.',
    'lecture': '7 min',
    'duree': 'PT7M',
    'public': 'Pour les structures',
    'publie': '2026-08-15',
    'suite': ('structure-accompagner-ses-artistes', 'c-est-quoi-le-guso-concretement', 'faut-il-un-contrat-pour-un-concert'),
    'md': '''Une association qui programme quatre concerts par an, un comité des fêtes, un bar qui accueille des groupes le vendredi, un collectif qui monte un festival : vous êtes des milliers à employer des artistes sans être une structure de spectacle, et souvent sans que personne, en interne, n'ait été formé à ça.

Cet article ne vous fera pas la morale. Il liste ce qui est obligatoire, ce qui coince en pratique, et comment s'organiser pour ne rien laisser tomber.

> **À savoir :** cet article décrit un fonctionnement général. Il ne remplace ni le site officiel **guso.fr**, ni un conseil professionnel. Si votre situation est atypique — activité régulière, licence, montage en cession — faites-la vérifier.

## Étape 0 : suis-je concerné par le GUSO ?

Le GUSO s'adresse aux employeurs qui remplissent **deux conditions cumulatives** :

1. le spectacle **n'est pas leur activité principale** — pas d'exploitation de lieu de spectacle, pas de production ou diffusion à titre principal ;
2. ils font appel **occasionnellement**, en CDD, à des artistes ou techniciens du spectacle vivant.

Si c'est votre cas, **le GUSO est obligatoire**, pas optionnel. Si vous employez de façon régulière ou que le spectacle devient votre activité principale, vous sortez du dispositif et d'autres obligations s'appliquent (dont, selon les situations, la licence d'entrepreneur de spectacles). En cas de doute sur ce basculement, posez la question avant, pas après.

## Ce que le GUSO fait pour vous

Une seule déclaration remplace les démarches auprès de l'ensemble des organismes de protection sociale du secteur : URSSAF, retraite complémentaire, prévoyance, congés spectacles, assurance chômage, formation, médecine du travail.

Vous déclarez une fois, vous payez une fois, le guichet répartit. Le service est **gratuit** : il vous fait gagner du temps, pas de l'argent — les cotisations restent dues.

Le GUSO transmet aussi les **attestations d'emploi** à France Travail Spectacle et envoie à chaque salarié son **attestation mensuelle d'emploi**, qui vaut bulletin de salaire. Vous n'avez donc pas de bulletin à produire vous-même.

## Le calendrier d'une date, sans zone grise

C'est là que tout se joue. Quatre moments.

**Avant la date — la DPAE.** La déclaration préalable à l'embauche doit intervenir **avant que l'artiste ne commence à travailler**, au plus tôt dans les huit jours qui précèdent. Elle se fait via le site du GUSO. Elle porte sur l'identité du salarié — pas sur le lieu — ce qui permet, dans une même période resserrée, de couvrir plusieurs journées de travail rapprochées. C'est la formalité la plus souvent oubliée, et l'une des plus sensibles.

**Avant la date — le contrat.** Le contrat de travail (CDD d'usage) doit être **écrit**, et transmis au salarié **au plus tard dans les deux jours ouvrables suivant l'embauche**. L'absence d'écrit expose à une requalification en CDI à temps plein en cas de litige. C'est le risque juridique le plus lourd que court une petite structure, et c'est celui qu'on prend le plus souvent sans le savoir.

**Après la date — la déclaration.** Elle peut être saisie **jusqu'à un mois avant** la prestation et **au plus tard dans les 15 jours suivant la fin du contrat**. Quinze jours, c'est court quand la personne qui gère les concerts est bénévole et part en vacances le lendemain du festival.

**Après la date — le paiement.** Le salaire à l'artiste, et les cotisations dues via le GUSO dans les délais prévus. Un retard expose à des majorations.

## Les pièges qui coûtent cher

**« On le déclarera plus tard. »** Non : la fenêtre de 15 jours après la fin du contrat n'est pas indicative. Au-delà, c'est un retard, avec des conséquences pour vous — et pour l'artiste, dont les heures conditionnent le revenu de l'année suivante.

**Payer « en défraiement » ou en espèces.** Un artiste qui joue est un salarié. Le rémunérer comme un remboursement de frais est du travail dissimulé, avec des sanctions à la clé et un préjudice réel pour lui : aucune heure, aucun droit.

**Demander une facture à l'artiste.** Sauf montage particulier (l'artiste est employé par une autre structure qui vous facture une cession), un artiste engagé par vous ne vous facture pas : il est salarié. Une facture d'auto-entrepreneur ne régularise rien et fragilise tout le monde.

**Sous-estimer le coût réel.** Le net que touche l'artiste et le coût pour vous sont deux nombres très différents : les cotisations sociales du spectacle sont significatives. Faites une simulation **avant** d'annoncer un budget — le site du GUSO propose des outils pour ça. Annoncer un cachet puis découvrir la facture est la meilleure façon de gâcher une relation.

**Oublier les répétitions.** Si des répétitions rémunérées sont prévues, elles se déclarent avec le spectacle, en heures ou sous forme de cachet selon ce qui a été convenu. Non déclarées, elles disparaissent purement et simplement des droits de l'artiste.

**Une seule déclaration pour un groupe.** Chaque artiste est employé individuellement. Cinq musiciens, c'est cinq salariés — et cinq attestations.

**Ne pas collecter les bonnes informations.** Il vous faut, par personne : nom, prénom, date et lieu de naissance, adresse, **numéro de sécurité sociale**, **numéro GUSO**, coordonnées bancaires. Demandez-les à la signature, pas la veille. Et traitez-les comme ce qu'elles sont : des données personnelles sensibles, à ne pas faire circuler dans une boucle de messages.

**Oublier la SACEM et les autres obligations.** Le GUSO couvre l'emploi. Les droits d'auteur, l'assurance, la sécurité du public relèvent d'autres démarches, indépendantes.

## Une méthode simple, en quatre listes

La difficulté d'une petite structure n'est pas la complexité : c'est la **charge mentale répartie sur des bénévoles**. Une méthode qui tient tient parce qu'elle est bête.

Tenez quatre listes, à jour, visibles par plusieurs personnes :

1. **Les DPAE à faire**, avec la date de l'échéance.
2. **Les déclarations à saisir**, avec la date limite (fin de contrat + 15 jours).
3. **Les paiements à effectuer** — artistes et cotisations.
4. **Les fiches artistes** : les informations administratives collectées une fois, réutilisées ensuite.

Et une règle d'or : **deux personnes doivent savoir faire**. La quasi-totalité des dossiers qui explosent dans une association sont des dossiers où une seule personne savait, et où cette personne est partie.

## Vous avez plus de pouvoir que vous ne croyez

Le point que beaucoup de petites structures ne réalisent pas : **votre sérieux administratif est un argument**. Un contrat envoyé sans qu'on le demande, une DPAE faite à temps, une déclaration dans les délais, un paiement à la date annoncée — ça se sait très vite entre musiciens, et ça vous ramène de bons artistes.

L'inverse aussi se sait. Et souvent, ce n'est pas de la mauvaise volonté : c'est un cadre jamais posé, faute de temps et de méthode.

## Un back-office pour ne rien laisser tomber

**Guso Facile** propose un espace structure pensé exactement pour ça : une **vue transversale, tous artistes confondus**, de ce qui reste à faire — DPAE, feuillets GUSO à éditer, factures et virements — chaque ligne cliquable pour ouvrir la date concernée. Les DPAE de dates rapprochées sont regroupées, pour en déclarer plusieurs d'un coup.

Une section **« Mes artistes »** réunit une fiche administrative par personne (numéro de sécurité sociale masqué par défaut, coordonnées bancaires, RIB) avec un bouton pour copier le bloc d'informations et le coller dans un formulaire. Une fiche **« Ma structure »** centralise SIRET, IBAN et licence, réutilisés partout. Les factures se déposent date par date, et deux cases suivent l'argent : facture réglée, salaire reçu.

Un **générateur de contrat d'engagement** en douze rubriques arrivera bientôt, pour envoyer un écrit propre sans partir d'une page blanche. L'app est en bêta, accessible sur cooptation.

Bien employer un artiste, ce n'est pas compliqué : c'est juste plein de petites choses à ne pas oublier. Moins d'énergie dans l'administratif, plus dans les concerts que vous organisez.''',
  },
)


SLUGS = tuple(a['slug'] for a in ARTICLES)
PAR_SLUG = {a['slug']: a for a in ARTICLES}

#: l'ordre exact de la section 1 du dossier SEO, pour les 8 premiers. Il sert
#: de garde-fou : si un slug bouge, la migration depuis Vercel n'est plus 1:1.
SLUGS_DOSSIER_SEO = (
    'atteindre-507-heures-sans-angoisse',
    'ne-plus-jamais-oublier-une-dpae',
    'pointage-france-travail-sans-stress',
    'organiser-une-tournee-qui-tient-la-route',
    'evaluer-si-une-date-est-un-bon-plan',
    'travailler-a-deux-artistes-dates-partagees',
    'structure-accompagner-ses-artistes',
    'studio-et-cheque-intermittents',
)

# --- les six themes de l'index -------------------------------------------
# Le dossier SEO ne propose pas de regroupement (il ne connaissait que 8
# articles). Avec 18, une liste plate se lit mal : les themes reprennent
# exactement les `articleSection` deja attribuees, sans en inventer de
# nouvelles pour les articles. Chaque article apparait dans UN seul theme, et
# `_controles()` verifie que les six themes couvrent les 18, sans doublon.
THEMES = (
    ('heures', 'jauge', 'Suivre ses 507 heures',
     'Le compteur glissant, la date anniversaire, et combien de cachets il faut vraiment.',
     ('atteindre-507-heures-sans-angoisse',
      'combien-de-cachets-pour-507-heures',
      'quand-tombe-ma-date-anniversaire')),
    ('france-travail', 'pointage', 'France Travail',
     'L’actualisation mensuelle, et l’écart entre tes chiffres et les leurs.',
     ('pointage-france-travail-sans-stress',
      'heures-ne-correspondent-pas-france-travail')),
    ('guso', 'guichet', 'GUSO, DPAE et déclarations',
     'Qui déclare quoi, dans quels délais, et ce que tu dois recevoir en retour.',
     ('c-est-quoi-le-guso-concretement',
      'ne-plus-jamais-oublier-une-dpae',
      'comment-declarer-une-repetition',
      'studio-et-cheque-intermittents')),
    ('contrat', 'contrat', 'Contrat, paiement et négociation',
     'Avant de jouer : l’écrit. Après avoir joué : être payé. Entre les deux : dire non.',
     ('faut-il-un-contrat-pour-un-concert',
      'evaluer-si-une-date-est-un-bon-plan',
      'ca-va-te-faire-connaitre-comment-repondre',
      'employeur-ne-m-a-pas-paye-mon-cachet')),
    ('groupe', 'route', 'À plusieurs, et sur la route',
     'Les dates partagées, les groupes multiples, et la tournée qui se prépare.',
     ('travailler-a-deux-artistes-dates-partagees',
      'm-organiser-quand-je-joue-dans-plusieurs-groupes',
      'organiser-une-tournee-qui-tient-la-route')),
    ('structures', 'structure', 'Pour les structures',
     'Associations, compagnies, petits organisateurs : vos obligations et vos outils.',
     ('structure-accompagner-ses-artistes',
      'structure-comment-gerer-les-guso-de-mes-artistes')),
)


def url_article(slug):
    return '%s/%s' % (URL_BLOG, slug)


def url_abs(chemin):
    return SITE + chemin


# =========================================================================
# LE JSON-LD
# =========================================================================
# Les blocs de la section 2 du dossier SEO sont repris a l'identique, mais
# CONSTRUITS EN PYTHON plutot que colles en texte : `json.dumps` garantit
# alors qu'aucun bloc ne peut partir avec une virgule finale, une apostrophe
# typographique mal echappee ou un guillemet courbe — le defaut qui rend un
# JSON-LD silencieusement inutile. Ils sont de toute facon repasses par
# `json.loads` dans `_controles()` avant ecriture.
#
# ⚠️ DEUX ECARTS ASSUMES par rapport au texte du dossier, tous deux dus au
#    fait qu'il a ete ecrit quand le blog comptait 8 articles :
#    (1) `blogPost` et `itemListElement` de l'index enumerent les 18, et
#        `numberOfItems` vaut 18. Laisser 8 aurait decrit un blog qui n'existe
#        pas, sur la page meme qui en liste 18.
#    (2) les 10 articles neufs n'ont pas de bloc fourni : le leur est bati sur
#        le MEME gabarit que les 8 (memes cles, meme ordre).

ORGANISATION = {
    '@type': 'Organization',
    '@id': url_abs('/') + '#organization',
    'name': 'Résonances Productions',
    'url': url_abs('/') + '',
}

AUTEUR = {
    '@type': 'Person',
    'name': 'David Lesage',
    'url': url_abs('/david-lesage-en-concert'),
}


def _fil(items):
    """BreadcrumbList — meme forme que dans le dossier SEO."""
    return {
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'name': nom, 'item': url}
            for i, (nom, url) in enumerate(items)
        ],
    }


def jsonld_index():
    posts = [
        {
            '@type': 'BlogPosting',
            '@id': url_abs(url_article(a['slug'])) + '#article',
            'headline': a['h1'],
            'url': url_abs(url_article(a['slug'])),
        }
        for a in ARTICLES
    ]
    liste = [
        {
            '@type': 'ListItem',
            'position': i + 1,
            'name': a['h1'],
            'url': url_abs(url_article(a['slug'])),
        }
        for i, a in enumerate(ARTICLES)
    ]
    return {
        '@context': 'https://schema.org',
        '@graph': [
            ORGANISATION,
            {
                '@type': 'Blog',
                '@id': url_abs(URL_BLOG) + '#blog',
                'name': 'Le blog de Guso Facile',
                'url': url_abs(URL_BLOG),
                'description': ('Cas concrets pour artistes intermittents : 507 heures, DPAE, '
                                'GUSO, actualisation France Travail et organisation de tournée.'),
                'inLanguage': 'fr-FR',
                'publisher': {'@id': ORGANISATION['@id']},
                'author': AUTEUR,
                'blogPost': posts,
            },
            {
                '@type': 'ItemList',
                '@id': url_abs(URL_BLOG) + '#liste',
                'numberOfItems': len(ARTICLES),
                'itemListElement': liste,
            },
            _fil([
                ('Résonances Productions', url_abs('/')),
                ('Guso Facile', url_abs(URL_PRODUIT)),
                ('Blog', url_abs(URL_BLOG)),
            ]),
        ],
    }


def jsonld_article(a):
    u = url_abs(url_article(a['slug']))
    return {
        '@context': 'https://schema.org',
        '@graph': [
            ORGANISATION,
            {
                '@type': 'BlogPosting',
                '@id': u + '#article',
                'headline': a['h1'],
                'name': a['h1'],
                'description': a['description'],
                'url': u,
                'mainEntityOfPage': {'@type': 'WebPage', '@id': u},
                'inLanguage': 'fr-FR',
                'datePublished': a['publie'],
                'dateModified': DATE_MAJ,
                'author': AUTEUR,
                'publisher': {'@id': ORGANISATION['@id']},
                'image': {
                    '@type': 'ImageObject',
                    'url': url_abs('/og-image.jpg'),
                    'width': 1200,
                    'height': 630,
                },
                'articleSection': a['rubrique'],
                'keywords': a['motscles'],
                'timeRequired': a['duree'],
                'isPartOf': {
                    '@type': 'Blog',
                    '@id': url_abs(URL_BLOG) + '#blog',
                    'name': 'Le blog de Guso Facile',
                    'url': url_abs(URL_BLOG),
                },
                'isAccessibleForFree': True,
            },
            _fil([
                ('Résonances Productions', url_abs('/')),
                ('Guso Facile', url_abs(URL_PRODUIT)),
                ('Blog', url_abs(URL_BLOG)),
                (a['h1'], u),
            ]),
        ],
    }


def bloc_jsonld(donnees):
    txt = json.dumps(donnees, ensure_ascii=False, indent=2)
    # Un `</script>` ou un `<!--` a l'interieur d'un bloc JSON-LD casserait le
    # parseur HTML avant meme le parseur JSON. Aucun de nos textes n'en
    # contient, mais on le verifie plutot que de l'esperer.
    if '</' in txt or '<!--' in txt:
        raise ValueError('sequence interdite dans un bloc JSON-LD')
    json.loads(txt)
    return '<script type="application/ld+json">\n%s\n</script>\n' % txt


# =========================================================================
# LES MORCEAUX DE PAGE COMMUNS
# =========================================================================
# La barre de navigation est un GABARIT MINIMAL : `nav_menu.inject()` remplace
# integralement le <div class="links">. Ne pas y ecrire les entrees a la main.
NAV = """
<nav class="nav">
  <a href="/" class="brand">Résonances Productions</a>
  <div class="links">
    <a href="/">Accueil</a>
  </div>
</nav>
"""

# Pied de page identique aux 10 pages du site, repris de `generate_guso.py`.
PIED = """
<a class="totop" href="#top" aria-label="Revenir en haut de la page">↑</a>

<footer id="contact"><div class="wrap">
  <div class="fgrid">
    <div>
      <div class="fbrand">Résonances Productions</div>
      <p style="margin-top:8px">Association loi 1901 — Art du spectacle vivant.<br>« l’humain, la vibration »</p>
    </div>
    <div>
      <h4>Contact</h4>
      <p><a href="mailto:contact@resonancesproductions.org">contact@resonancesproductions.org</a></p>
      <p><b>Siège social</b><br>2 impasse des Bleuets<br>09600 Aigues-Vives</p>
      <p><b>Adresse de correspondance</b><br>29 rue des Orteaux<br>75020 Paris</p>
      <p style="margin-top:8px"><a href="https://www.facebook.com/resonancesproductions" target="_blank" rel="noopener">Facebook</a></p>
    </div>
    <div>
      <h4>Informations</h4>
      <p>SIRET : 919 514 075 00010</p>
      <p>Code APE : 9001Z<br>Arts du spectacle vivant</p>
      <p style="margin-top:8px"><a href="https://www.helloasso.com/associations/resonances-productions" target="_blank" rel="noopener">Adhérer / soutenir</a></p>
      <p style="margin-top:8px"><a href="https://docs.google.com/document/d/1NxsbvaqHsA9VOXlN7cvsav7cxFwhsK4XCpowHb75o1w/edit?usp=sharing" target="_blank" rel="noopener">Statuts de l’association</a></p>
    </div>
  </div>
  <div class="legal">© 2026 Résonances Productions · resonancesproductions.org</div>
</div></footer>

<script>
(function(){
  var b=document.querySelector('.totop'); if(!b) return;
  function upd(){ b.classList.toggle('on', window.scrollY>700); }
  upd(); window.addEventListener('scroll',upd,{passive:true});
})();
</script>
"""


def entete(titre, description, canonique, og_type, jsonld, og_titre=None):
    return (HEAD % {
        'titre': _echap(titre),
        'description': _echap(description),
        'og_titre': _echap(og_titre or titre),
        'canonique': canonique,
        'og_type': og_type,
    }, jsonld)


def fil_ariane(feuille=None):
    """Le fil d'Ariane visible. Il double le BreadcrumbList (section 6)."""
    items = [('Résonances Productions', '/'), ('Guso Facile', URL_PRODUIT)]
    if feuille is None:
        items.append(('Blog', None))
    else:
        items.append(('Blog', URL_BLOG))
        items.append((feuille, None))
    li = []
    for nom, href in items:
        if href is None:
            li.append('      <li><span aria-current="page">%s</span></li>\n' % _echap(nom))
        else:
            li.append('      <li><a href="%s">%s</a></li>\n' % (href, _echap(nom)))
    return ('    <nav class="fil" aria-label="Fil d’Ariane">\n      <ol>\n%s      </ol>\n    </nav>\n'
            % ''.join(li))


def carte(slug, avec_resume=True):
    a = PAR_SLUG[slug]
    resume = ('      <p class="carte-d">%s</p>\n' % _inline(a['dek'])) if avec_resume else ''
    return ('    <a class="carte" href="%s">\n'
            '      <p class="carte-r">%s</p>\n'
            '      <p class="carte-t">%s</p>\n'
            '%s'
            '      <span class="carte-l">%s de lecture%s</span>\n'
            '    </a>\n'
            % (url_article(slug), _echap(a['rubrique']), _echap(a['h1']), resume,
               _echap(a['lecture']), _ic('fleche')))


# =========================================================================
# LES PAGES
# =========================================================================

def build_index():
    B = []
    A = B.append

    tete, ld = entete(
        'Blog Guso Facile — l’intermittence sans paperasse',
        'Cas concrets pour artistes intermittents : suivre ses 507 heures, ne pas rater une '
        'DPAE, éditer ses GUSO, pointer à France Travail et organiser une tournée.',
        url_abs(URL_BLOG), 'website', bloc_jsonld(jsonld_index()))
    A(tete)
    A(FEUILLE)
    A('</style>\n')
    A(ld)
    A('</head>\n<body id="top">\n')
    A(NAV)
    A(SVG_DEFS)

    # Le h1 et le sous-titre sont ceux du dossier SEO (section 2.2) : « Le blog
    # de Guso Facile », et « Des situations réelles, des solutions concrètes »
    # en chapo — ce sont les mots de David, conserves tels quels.
    A('<header class="bl-top"><div class="wrap">\n')
    A(fil_ariane())
    A('    <div class="col">\n')
    A('      <p class="kick">Guso Facile</p>\n')
    A('      <h1>Le blog de Guso Facile</h1>\n')
    A('      <p class="bl-dek">Des situations réelles, des solutions concrètes.</p>\n')
    A('      <p class="bl-intro">Dix-huit articles écrits pour les artistes intermittents et '
      'les structures qui les emploient : le compteur des 507 heures, les DPAE, les feuillets '
      'GUSO, l’actualisation France Travail, le contrat, l’impayé, la tournée. Chacun part '
      'd’une situation concrète et s’arrête à ce qui est utile.</p>\n')
    A('      <p class="bl-meta"><span>%s18 articles</span>'
      '<span>%sMis à jour le <time datetime="%s">%s</time></span></p>\n'
      % (_ic('carnet'), _ic('calendrier'), DATE_MAJ, DATE_MAJ_FR))
    A('    </div>\n')
    # Le sommaire par themes evite de faire defiler 18 cartes pour trouver le
    # bon sujet. Ce sont des ancres internes : aucune page supplementaire.
    A('    <div class="somm">\n      <p class="somm-t">Par thème</p>\n      <ul>\n')
    for cle, _ico, nom, _sous, slugs in THEMES:
        A('        <li><a href="#%s">%s <span>(%d)</span></a></li>\n'
          % (cle, _echap(nom), len(slugs)))
    A('      </ul>\n    </div>\n')
    A('</div></header>\n')
    A('<div class="divider"></div>\n')

    A('<main>\n<section><div class="wrap">\n')
    for cle, ico, nom, sous, slugs in THEMES:
        A('  <div class="theme" id="%s">\n' % cle)
        A('    <div class="theme-h">\n')
        A('      <span class="theme-ico">%s</span>\n' % _ic(ico))
        A('      <h2>%s</h2>\n' % _echap(nom))
        A('      <span class="theme-n">%d article%s</span>\n'
          % (len(slugs), 's' if len(slugs) > 1 else ''))
        A('    </div>\n')
        A('    <p class="carte-d" style="max-width:66ch">%s</p>\n' % _echap(sous))
        A('    <div class="cartes">\n')
        for s in slugs:
            A(carte(s))
        A('    </div>\n  </div>\n')
    A('</div></section>\n')

    # La remontee vers la page produit, exigee par la section 6 du dossier.
    A('<div class="wrap">\n')
    A('  <div class="final" style="margin-bottom:86px">\n')
    A('    <h2>L’outil derrière le blog</h2>\n')
    A('    <p>Guso Facile réunit le suivi des 507 heures, les DPAE, les feuillets GUSO, les '
      'factures et le récap d’actualisation France Travail dans une seule application. '
      'L’app est en bêta, accessible sur cooptation.</p>\n')
    A('    <div class="cta"><a class="btn" href="%s">Découvrir Guso Facile%s</a></div>\n'
      % (URL_PRODUIT, _ic('fleche')))
    A('  </div>\n</div>\n')
    A('</main>\n')

    A(PIED)
    A('</body></html>\n')
    return ''.join(B)


def build_article(a):
    B = []
    A = B.append

    u = url_abs(url_article(a['slug']))
    tete, ld = entete(a['titre'], a['description'], u, 'article',
                      bloc_jsonld(jsonld_article(a)), og_titre=a['h1'])
    A(tete)
    A(FEUILLE)
    A('</style>\n')
    A(ld)
    A('</head>\n<body id="top">\n')
    A(NAV)
    A(SVG_DEFS)

    A('<header class="bl-top"><div class="wrap">\n')
    A(fil_ariane(a['h1']))
    A('    <div class="col">\n')
    A('      <p class="rub">%s</p>\n' % _echap(a['rubrique']))
    A('      <h1>%s</h1>\n' % _echap(a['h1']))
    A('      <p class="bl-dek">%s</p>\n' % _inline(a['dek']))
    # La date de mise a jour est VISIBLE : les moteurs generatifs privilegient
    # fortement le contenu date (section 7 du dossier SEO). Elle se reactualise
    # dans `DATE_MAJ` a chaque revision de fond — une date figee qui vieillit
    # est pire que pas de date.
    A('      <p class="bl-meta">'
      '<span>%s%s de lecture</span>'
      '<span>%s%s</span>'
      '<span>%sMis à jour le <time datetime="%s">%s</time></span></p>\n'
      % (_ic('horloge'), _echap(a['lecture']), _ic('public'), _echap(a['public']),
         _ic('calendrier'), DATE_MAJ, DATE_MAJ_FR))
    A('    </div>\n')
    A('</div></header>\n')
    A('<div class="divider"></div>\n')

    A('<main>\n<article class="art"><div class="wrap"><div class="col fin">\n')
    A(md_en_html(a['md']))

    A('  <nav class="suite" aria-label="À lire ensuite">\n')
    A('    <h2>À lire ensuite</h2>\n')
    A('    <div class="cartes">\n')
    for s in a['suite']:
        A(carte(s, avec_resume=False))
    A('    </div>\n  </nav>\n')

    A('  <p class="remonte">'
      '<a href="%s">%sTous les articles du blog</a>'
      '<a href="%s">%sDécouvrir Guso Facile</a></p>\n'
      % (URL_BLOG, _ic('retour'), URL_PRODUIT, _ic('fleche')))
    A('</div></div></article>\n</main>\n')

    A(PIED)
    A('</body></html>\n')
    return ''.join(B)


# =========================================================================
# GARDE-FOUS
# =========================================================================
# Parti-pris maison (celui de `generate_rythme.py` et de `generate_guso.py`) :
# on REFUSE D'ECRIRE plutot que d'imprimer un avertissement qui defile et que
# personne ne lit. Tant qu'un controle n'est pas passe, les 19 fichiers sur
# disque restent intacts — les pages ne sont ecrites qu'a la toute fin.

#: les prenoms des personnages fictifs des articles. Le depot est PUBLIC : si
#: un nom de famille apparaissait derriere l'un d'eux, ce ne serait plus un
#: personnage mais quelqu'un.
PRENOMS_FICTIFS = ('Léa', 'Marco', 'Sophie', 'Camille', 'Nino', 'Awa',
                   'Salomé', 'Théo', 'Elsa', 'Bastien')

#: les motifs qui trahissent un reliquat de mini-Markdown non converti.
RELIQUATS = (
    ('**', 'gras Markdown non converti'),
    ('](', 'lien Markdown non converti'),
    ('\n## ', 'titre Markdown non converti'),
    ('\n- ', 'puce Markdown non convertie'),
    ('\n> ', 'citation Markdown non convertie'),
    ('::: ', 'bloc « ::: » non converti'),
    ('@lead ', 'marqueur @lead non converti'),
    ('@scene ', 'marqueur @scene non converti'),
    ('{ico:', 'jeton d’icone non converti'),
)

#: Les CICATRICES DE SUPPRESSION D'EMOJI. Elles ont reellement existe : en
#: retirant les emoji du texte des 8 articles Vercel, cinq phrases sont parties
#: amputees — « detaille, ou , », « verdict , a negocier », « un marqueur «  » »
#: — sans qu'aucun controle ne s'en apercoive, puisque du point de vue du HTML
#: la page etait parfaitement valide. Ces motifs ferment la porte : le jour ou
#: un caractere sera de nouveau retire d'une phrase sans etre remplace, le
#: generateur refusera d'ecrire au lieu de publier une phrase trouee.
CICATRICES = (
    (r'«\s*»', 'guillemets vides (un caractere a ete retire sans etre remplace)'),
    (r'<(b|i)>\s', 'espace en tete d’un gras ou d’un italique'),
    (r'\s</(b|i)>', 'espace en fin d’un gras ou d’un italique'),
    (r',\s*(?:ou|et)\s*,', 'enumeration trouee (« , ou , »)'),
    (r':\s*,', 'deux-points suivi d’une virgule'),
    (r'\s{2,}[a-zà-öø-ÿA-ZÀ-Þ]', 'double espace dans une phrase'),
)


def _corps(html):
    """Le HTML sans son <head> : c'est la que se cherchent les reliquats."""
    return html.split('</head>', 1)[1]


def _texte_lu(html):
    """Le texte tel qu'un lecteur le voit, ligne a ligne.

    ⚠️ Une icone en ligne y devient UN CARACTERE (`◆`), elle n'est pas retiree :
    c'est tout l'interet du controle. Sans cela, « un marqueur « <svg…> » »
    redeviendrait « un marqueur «  » » sous l'oeil du garde-fou, qui laisserait
    donc passer exactement la faute qu'on lui demande d'attraper.
    """
    t = _corps(html)
    t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S)
    t = re.sub(r'<style.*?</style>', ' ', t, flags=re.S)
    t = re.sub(r'<svg\b.*?</svg>', '◆', t, flags=re.S)
    t = re.sub(r'<[^>]+>', '', t)          # les balises restantes sont en ligne
    return (t.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&'))


def _controle_page(html, nom):
    """Les controles communs aux 19 pages."""
    ennuis = []

    if html.count('<h1') != 1:
        ennuis.append('%d <h1> (attendu : 1)' % html.count('<h1'))
    marque = 'data-nav="%s"' % nav_menu.NAV_VERSION
    if html.count(marque) != 1:
        ennuis.append('%d menu partage %s (attendu : 1)' % (html.count(marque), marque))
    if html.count('href="/guso-facile"') < 1:
        ennuis.append('aucun lien vers la page produit /guso-facile')

    # la couche chaleureuse commune est bien dans la feuille de style. Sans
    # elle la page reste valide mais sort SANS le degrade signature, sans les
    # halos et avec le filet d'un pixel : froide, donc fausse. Une page froide
    # ne se voit dans aucun controle de structure — celui-ci est la pour ca.
    for reperage, quoi in (('--grad:linear-gradient', 'le degrade signature --grad'),
                           ('--coral:#e08a72', 'la couleur --coral'),
                           ('--plum2:#b3a2e4', 'la couleur --plum2'),
                           ('body::before', 'les trois halos de fond')):
        if reperage not in html:
            ennuis.append('couche chaleureuse absente : %s (theme_chaleur.CSS)' % quoi)
    if html.count('<html lang="fr">') != 1:
        ennuis.append('attribut lang manquant')
    if html.count('<link rel="canonical"') != 1:
        ennuis.append('canonical absent ou en double')
    if html.count('<main>') != 1 or html.count('</main>') != 1:
        ennuis.append('<main> absent ou en double')

    # JSON-LD : un seul bloc, et il doit se relire.
    blocs = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
    if len(blocs) != 1:
        ennuis.append('%d bloc(s) JSON-LD (attendu : 1)' % len(blocs))
    for b in blocs:
        try:
            json.loads(b)
        except ValueError as e:
            ennuis.append('JSON-LD invalide : %s' % e)

    # aucune image, aucune iframe, aucune ressource externe hors la feuille de
    # polices deja chargee par les 10 autres pages du site.
    for balise in ('<img', '<iframe', '<video', '<audio', '<object', '<embed', ' srcset='):
        if balise in html:
            ennuis.append('ressource interdite : %s' % balise.strip())
    externes = set(re.findall(r'(?:href|src)="(https?://[^"]+)"', html))
    for u in externes:
        hote = u.split('/')[2]
        if hote not in ('www.resonancesproductions.org', 'fonts.googleapis.com',
                        'www.facebook.com', 'www.helloasso.com', 'docs.google.com'):
            ennuis.append('ressource externe inattendue : %s' % u)

    # tout target="_blank" porte rel="noopener" (regle du site)
    for lien in re.findall(r'<a\b[^>]*>', html):
        if 'target="_blank"' in lien and 'rel="noopener"' not in lien:
            ennuis.append('target="_blank" sans rel="noopener" : %s' % lien[:90])

    # plancher typographique 13 px
    for taille in re.findall(r'font-size:\s*([0-9.]+)px', html):
        if float(taille) < 13:
            ennuis.append('texte a %spx (plancher du site : 13px)' % taille)

    # aucun emoji nulle part (regle du site)
    for ch in html:
        if 0x1F000 <= ord(ch) <= 0x1FAFF or 0x2600 <= ord(ch) <= 0x27BF:
            ennuis.append('emoji U+%04X dans la page' % ord(ch))
            break

    # aucun reliquat de mini-Markdown dans le corps
    corps = _corps(html)
    for motif, quoi in RELIQUATS:
        if motif in corps:
            i = corps.index(motif)
            ennuis.append('%s (« %s »)' % (quoi, ' '.join(corps[i - 40:i + 40].split())))

    # aucune phrase amputee par le retrait d'un emoji
    for motif, quoi in CICATRICES[:3]:          # les trois motifs a chercher DANS le HTML
        m = re.search(motif, corps)
        if m:
            i = m.start()
            ennuis.append('%s (« %s »)' % (quoi, ' '.join(corps[max(0, i - 50):i + 50].split())))
    lu = _texte_lu(html)
    for ligne in lu.split('\n'):
        ligne = ligne.strip()   # l'indentation du gabarit n'est pas du texte
        for motif, quoi in CICATRICES[3:]:      # ceux a chercher dans le TEXTE LU
            m = re.search(motif, ligne)
            if m:
                i = m.start()
                ennuis.append('%s (« %s »)' % (quoi, ligne[max(0, i - 50):i + 50].strip()))

    # depot public : pas de nom de famille derriere un prenom de personnage
    for p in PRENOMS_FICTIFS:
        m = re.search(re.escape(p) + r' [A-ZÀ-Þ][a-zà-ÿ]+', corps)
        if m:
            ennuis.append('nom de famille possible derriere un personnage : %r' % m.group(0))

    # tous les liens internes du blog pointent une page qui va exister
    for href in re.findall(r'href="(/guso-facile[^"#]*)"', html):
        if href in (URL_PRODUIT, URL_BLOG):
            continue
        if not href.startswith(URL_BLOG + '/') or href[len(URL_BLOG) + 1:] not in SLUGS:
            ennuis.append('lien interne mort : %s' % href)

    if ennuis:
        raise SystemExit(
            '!! ABANDON : %s\n%s\n   Aucune page ecrite (le disque est inchange).'
            % (nom, '\n'.join('   - ' + e for e in ennuis)))


def _controles_structure():
    """Ce qui se verifie AVANT de construire quoi que ce soit."""
    ennuis = []
    if len(ARTICLES) != 18:
        ennuis.append('%d articles (attendu : 18)' % len(ARTICLES))
    if len(set(SLUGS)) != len(SLUGS):
        ennuis.append('slug en double')
    for s in SLUGS_DOSSIER_SEO:
        if s not in SLUGS:
            ennuis.append('slug du dossier SEO absent : %s' % s)
    # les 6 themes couvrent les 18, une seule fois chacun
    vus = [s for _c, _i, _n, _d, slugs in THEMES for s in slugs]
    if sorted(vus) != sorted(SLUGS):
        manquants = sorted(set(SLUGS) - set(vus))
        doublons = sorted(x for x in set(vus) if vus.count(x) > 1)
        ennuis.append('themes incomplets (absents : %s ; en double : %s)'
                      % (manquants or '-', doublons or '-'))
    # titres et descriptions tous differents (checklist du dossier, section 8)
    for cle in ('titre', 'description', 'h1'):
        vals = [a[cle] for a in ARTICLES]
        if len(set(vals)) != len(vals):
            ennuis.append('deux articles partagent le meme %s' % cle)
    # le maillage ne pointe que sur des articles existants, jamais sur soi
    for a in ARTICLES:
        if len(a['suite']) != 3:
            ennuis.append('%s : %d liens « A lire ensuite » (attendu : 3)'
                          % (a['slug'], len(a['suite'])))
        for s in a['suite']:
            if s not in SLUGS:
                ennuis.append('%s renvoie vers un article inconnu : %s' % (a['slug'], s))
            if s == a['slug']:
                ennuis.append('%s se renvoie a lui-meme' % a['slug'])
    if ennuis:
        raise SystemExit('!! ABANDON (structure) :\n%s'
                         % '\n'.join('   - ' + e for e in ennuis))


# =========================================================================
# ECRITURE
# =========================================================================

def main():
    _controles_structure()

    pages = []   # (chemin, html)

    html = build_index()
    html = mobile_nav.inject(html)          # 1. le hamburger d'abord
    html = nav_menu.inject(html, 'guso-facile')   # 2. puis le menu partage
    _controle_page(html, 'guso-facile/blog/index.html')
    if html.count('href="%s/' % URL_BLOG) != len(ARTICLES):
        raise SystemExit('!! ABANDON : l’index ne renvoie pas vers exactement %d articles.'
                         % len(ARTICLES))
    pages.append((os.path.join(OUT_DIR, 'index.html'), html))

    for a in ARTICLES:
        h = build_article(a)
        h = mobile_nav.inject(h)
        h = nav_menu.inject(h, 'guso-facile')
        _controle_page(h, 'guso-facile/blog/%s/index.html' % a['slug'])
        pages.append((os.path.join(OUT_DIR, a['slug'], 'index.html'), h))

    if len(pages) != 19:
        raise SystemExit('!! ABANDON : %d pages a ecrire (attendu : 19).' % len(pages))

    # Aucune note de redaction en commentaire HTML dans les pages livrees :
    # elles seraient publiques et indexables. Leur place est ici, en `#`.
    for chemin, h in pages:
        verif_commentaires.verifier(h, chemin)

    total = 0
    for chemin, h in pages:
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        with open(chemin, 'w', encoding='utf-8') as f:
            f.write(h)
        total += len(h.encode('utf-8'))
    print('[blog]   %d pages ecrites dans %s  (%.1f Ko au total)'
          % (len(pages), OUT_DIR, total / 1024))


if __name__ == '__main__':
    main()
