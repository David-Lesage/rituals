# -*- coding: utf-8 -*-
"""Generateur de la page /guso-facile (Resonances Productions).

Ecrit `guso-facile/index.html`. Aucune image, aucune ressource tierce
supplementaire, aucun script externe.

------------------------------------------------------------------------------
D'OU VIENT LE TEXTE
------------------------------------------------------------------------------
Le contenu redactionnel a ete redige et valide ailleurs :

    /Users/davidlesage/CLAUDE/GUSO-FACILE-BACKUPS/contenu-page-resonances.md
    (8 sections, fourni par la session qui developpe Guso Facile — LECTURE SEULE,
     ne jamais l'editer depuis ici)

Ce generateur MET EN FORME ce texte, il ne le reecrit pas. Les seules
modifications apportees sont listees ci-dessous, chacune avec sa raison.

------------------------------------------------------------------------------
⚠️⚠️ LE POINT LE PLUS SENSIBLE DE CETTE PAGE : LE LIEN OUTIL <-> ASSOCIATION
------------------------------------------------------------------------------
La formulation qui relie Guso Facile a Resonances Productions est
VOLONTAIREMENT PRUDENTE. Ne pas la « corriger » en « porte par l'association »
ou « projet de l'association » sans savoir ce que cela engage.

Les faits, au 14/08/2026 :
  - l'infrastructure de Guso Facile est ENTIEREMENT PERSONNELLE : projet
    Supabase et projet Vercel sur les comptes propres de David Lesage, depot git
    prive a son nom, envoi d'e-mails via son Workspace contact@lesagedavid.fr ;
  - les donnees traitees sont SENSIBLES : numeros de securite sociale, IBAN,
    salaires, feuillets GUSO de personnes reelles ;
  - le modele payant + affiliation envisage est, en l'etat, hors du champ
    associatif.

Conclusion : aujourd'hui Guso Facile est un PROJET PERSONNEL de David Lesage,
que l'association RELAIE. Un portage associatif demanderait une decision
explicite, probablement actee en proces-verbal.

Ecrire « porte par Resonances Productions » sur le site public d'une
association, a propos d'un outil qui traite des numeros de securite sociale et
des IBAN, serait une approximation au pire endroit possible. Les mots retenus
sont donc : « cree par », « relaie », « n'est pas un service de l'association ».

------------------------------------------------------------------------------
LES ECARTS AU CONTENU FOURNI (liste exhaustive, pour arbitrage par David)
------------------------------------------------------------------------------
1. Kicker. Fourni : « Un outil de Resonances Productions ».
   Ecrit    : « Cree par David Lesage · relaye par l'association ».
   Raison   : voir ci-dessus. « Un outil de » = revendication de propriete.

2. Meta description. Fourni : « Guso Facile : l'outil de Resonances Productions
   qui allege… ». Ecrit : « …un outil cree par David Lesage, relaye par
   Resonances Productions, qui allege… ». Meme raison.

3. Titre de la section 3. Fourni : « Pourquoi Resonances Productions ».
   Ecrit : « Pourquoi Resonances Productions le relaie ». Meme raison.

4. Section 3, phrase d'ouverture AJOUTEE (mot pour mot celle validee) :
   « Guso Facile est un outil cree par David Lesage, musicien intermittent et
   co-fondateur de l'association. Resonances Productions le relaie parce qu'il
   sert directement son objet : le soutien aux artistes. »

5. Section 3, fin du paragraphe. Fourni : « Guso Facile est ne de ce constat, et
   en est le prolongement direct. L'outil est mis gratuitement a disposition des
   artistes accompagnes par l'association, et son developpement continue de se
   nourrir de leurs retours. »
   Ecrit : « Guso Facile est ne de ce constat, et son developpement continue de
   se nourrir des retours des artistes qui l'utilisent. »
   Raison : « prolongement direct » (de l'association) et « mis a disposition
   par l'association » sont deux affirmations de portage associatif.

6. Section 3, encadre AJOUTE : « Precision : Guso Facile n'est pas un service de
   l'association. L'outil, son hebergement et les donnees qu'il traite relevent
   de son createur. » — a supprimer d'un mot si David le juge inutile ; il rend
   la page coherente avec la mention sous le bouton.

7. Badge « Beta privee · places limitees » : le contenu le placait dans la
   section 6. Il est REMONTE DANS LE HERO (et n'apparait qu'une fois) parce que
   l'acces limite doit se voir sans avoir a faire defiler : un visiteur ne doit
   jamais croire qu'il peut s'inscrire immediatement. La section 6 garde son
   encadre a filet or et sa phrase explicite.

8. Le bouton d'action n'existe qu'UNE fois, dans la section « Manifester son
   interet ». Le hero renvoie vers cette section par une ancre interne (#acces).
   Aucun mot du contenu n'est change ; c'est une decision de mise en page,
   coherente avec « on commence par se dire bonjour ».

Rien d'autre n'a bouge : ni un chiffre, ni un fait, ni le niveau d'engagement
des formulations sur la beta, le futur payant et l'affiliation — c'est
delibere, ces trois sujets sont prudents par construction.

------------------------------------------------------------------------------
MISE A JOUR DU 14/08/2026 (soir) — 4 titres corriges, 3 blocs ajoutes
------------------------------------------------------------------------------
Apport de la session qui developpe Guso Facile. Regle qui a guide chaque
formulation : CE QUI EST LIVRE S'ECRIT AU PRESENT, CE QUI NE L'EST PAS S'ECRIT
AU FUTUR ET PORTE « (a venir) ». Un beta-testeur verifie en trois clics.

a) Les 4 univers portaient des intitules APPROCHANTS. Les vrais, releves dans
   le code de l'application, sont desormais ecrits mot pour mot, VIRGULE
   COMPRISE (c'est elle qui donne le rythme) :
       « Suivi des droits »          -> « Tes droits, maitrises »
       « Organisation de tournee »   -> « Ta tournee, organisee »
       « Espace structure »          -> « Ta structure, connectee »
       « Entraide entre artistes »   -> « Ton cercle, solidaire »
   SEULS les titres ont bouge ; le contenu des cartes est inchange.

b) « Faire decouvrir l'outil » (cooptation) — fonctionnalite LIVREE, ajoutee
   dans l'univers 4, AU PRESENT, sans mention « a venir ».

c) « L'entraide entre artistes » (la Guilde) — fonctionnalite NON LIVREE (la
   base existe, l'ecran non), ajoutee dans l'univers 4, AU FUTUR et marquee
   « (a venir) ». ⚠️ Bloc le plus sensible de la page apres celui du lien avec
   l'association : voir la CONTRAINTE REDACTIONNELLE STRICTE ecrite juste
   au-dessus de lui dans le gabarit, et le garde-fou `_controle_guilde()`.

d) « Je cree mon contrat » — fonctionnalite NON LIVREE (le modele en 12
   rubriques existe en base, l'ecran non), ajoutee dans l'univers 2, AU FUTUR
   et marquee « (a venir) ».

e) « Points de vigilance cote structure » et « Confidentialite graduee »
   etaient DEJA presents et DEJA marques « (a venir) » : rien a faire.

Le reste de la page n'a pas ete touche — en particulier « cree par David
Lesage · relaye par l'association », « Pourquoi Resonances Productions le
relaie », l'encadre « n'est pas un service de l'association », le titre
« Trois situations typiques » et sa note sur les prenoms fictifs, le badge
« Beta privee · places limitees » du hero, le bouton unique et les deux
mentions sur les donnees personnelles.

------------------------------------------------------------------------------
LE RACCORDEMENT AU SITE (fait le 14/08/2026)
------------------------------------------------------------------------------
La page n'est plus isolee. Ce qui a ete pose, et ou :
  - `sources/nav_menu.py` : entree « Guso Facile » dans un sous-menu
    « L’association » devenu deroulant (le pourquoi de ce placement est
    documente dans ce fichier-la), cle `guso-facile`, NAV_VERSION passee a
    `resonances-3` pour que les 9 autres pages recoivent le nouveau menu ;
  - `sources/build.py` : la ligne /guso-facile (ecrit=None, passe_menu=False,
    ce script posant lui-meme le menu) ;
  - `sitemap.xml`, `vercel.json` (redirection /Guso-Facile -> /guso-facile,
    l'URL ayant ete communiquee avec des majuscules), et les listes de pages
    de `verif_site.py` / `verif_commentaires.py`, passees a 10.

------------------------------------------------------------------------------
LES 6 MAQUETTES D'INTERFACE (posees le 14/08/2026 — la page ne montrait rien)
------------------------------------------------------------------------------
Verdict de David : « tres plate, elle ne montre rien de l'app ». Le texte
n'etait pas en cause : il manquait le visuel. Six blocs HTML/CSS PURS (aucune
image, aucun script, aucune capture d'ecran) reproduisent des ecrans reels de
l'application avec des donnees INVENTEES.

  Matiere d'origine (LECTURE SEULE, ne jamais editer ni deplacer) :
      /Users/davidlesage/CLAUDE/GUSO-FACILE-BACKUPS/maquettes-pour-resonances.html
  Elle est fournie par la session qui developpe Guso Facile.

CE QUI EST INTEGRE, ET OU
  1. Jauge des 507 h ............ HERO, colonne de droite (grille 1fr / 400px
                                  au-dela de 1000 px, empilee en dessous)
  2. « A faire maintenant » ..... fin de #promesse
  3. Fiche de date .............. #fonctionnalites, dans la grille des univers,
                                  juste apres les univers 1 et 2
  5. Ma tournee ................. idem, a cote de la fiche de date
  6. Tableau de bord structure .. idem, pleine largeur, apres l'univers 4
  4. Recap mensuel France Travail #situations, sous les trois cas d'usage
     (il illustre litteralement le cas de Marco, « Pointer France Travail en
      cinq minutes »)

LES TROIS EXIGENCES QUI NE SE NEGOCIENT PAS
  a) CHAQUE bloc porte, en <figcaption class="gf-cap">, la mention VISIBLE
     « Aperçu de l’interface — données fictives ». Une reproduction credible
     sans mention est indistinguable d'une vraie capture : cette page a deja
     du corriger « situations reelles » pour exactement ce motif.
  b) CE SONT DES ILLUSTRATIONS, PAS DES INTERFACES. Zero <button>, zero
     <input>, zero <a>, zero [tabindex] a l'interieur d'un bloc : un visiteur
     ne doit pas croire qu'il peut cliquer. Chaque bloc porte role="img" +
     aria-label. Garde-fou : `_controle_maquettes()`.
  c) RIEN QUI N'EXISTE PAS. La Guilde et « Je cree mon contrat » ne sont PAS
     illustrees : la page les ecrit au futur, les illustrer les ferait passer
     pour livrees.

CE QUI A ETE CORRIGE DANS LA MATIERE FOURNIE (l'auteur n'a pu tester que son
propre fichier, jamais dans cette page) :
  - Maquette 1, l'anneau etait MAL CALE : l'arc « dates possibles » allait de
    293deg a 336deg, soit 43 degres pour 43 HEURES — l'auteur a pris des heures
    pour des degres. 43 h sur 507 valent 30,5deg : l'arc s'arrete desormais a
    323deg ((412+43)/507 = 89,7 %).
  - Maquette 3, la liste des etapes affichait DEUX FOIS « Salaire reçu » et
    omettait « Actualisation France Travail », alors que son propre aria-label
    et sa note de livraison annoncent les cinq etapes de l'app. Corrige.
  - Maquette 4, le CSS DE LA VERSION EN CARTES N'EXISTAIT PAS dans le fichier
    source : seul restait celui de l'ancienne version en tableau (.gf-tw,
    .gf-tbl, .gf-th), qui ne stylait plus rien. Le bloc en cartes est donc
    habille ici (.gf-recmonth / .gf-reccard / .gf-rectot…), et le CSS de
    tableau, devenu inutile, n'a pas ete repris.
  - Maquette 5, LE KILOMETRAGE A ETE RETIRE. La note de livraison de l'auteur
    dit noir sur blanc : « L'espace Ma tournee de l'app liste les dates et les
    contacts, mais NE CALCULE PAS de kilometrage ». Illustrer « 1 240 km
    parcourus » aurait donc mis en image une fonction qui n'existe pas — la
    regle (c) l'interdit. Le bloc montre ce qui EST livre : l'enchainement
    chronologique des dates et le signalement des lieux a confirmer.
    ⚠️ A ARBITRER PAR DAVID : la puce de l'univers 2, elle, ecrit AU PRESENT
    « avec le calcul des kilometres parcourus depuis le domicile ». Le texte
    est valide et protege, je n'y ai pas touche — mais il dit le contraire de
    ce que dit l'auteur de l'app. L'un des deux doit bouger.
  - Maquette 6, l'aria-label annoncait un indicateur « vert, orange ou rouge »
    alors que la charte n'a ni vert ni rouge et que le rendu emploie la FORME
    de la pastille + un libelle. Un lecteur d'ecran entendait donc des couleurs
    absentes. Reecrit avec les trois libelles reellement affiches.
  - Les deux emoji (🔔 et 🎤) ont ete retires : la charte de la page l'interdit
    (« Aucun emoji », voir le commentaire de la section 4). La classe .gf-ico
    qui les portait a disparu avec eux.
  - Donnees harmonisees entre les six blocs pour qu'un lecteur attentif ne
    trouve pas de contradiction : Association Chant Libre est a Limoges
    partout (la maquette 4 la mettait a Pau), et la tournee ne liste que des
    dates qui existent dans les autres blocs.

MISE EN PAGE — la grille des univers passe a DEUX COLONNES
  Elle etait en `auto-fit minmax(320px,1fr)` : a 1440 px cela donnait TROIS
  cartes sur la premiere ligne et la QUATRIEME toute seule sur la deuxieme, en
  colonne de 328 px pour 1224 px de haut. L'ajout des maquettes n'aurait fait
  qu'aggraver ce desequilibre. Elle est desormais a une colonne sous 761 px et
  a DEUX colonnes au-dela : les univers se lisent 2 + 2, et les illustrations
  s'inserent naturellement entre les deux rangees (la vue structure prenant la
  pleine largeur, `.gf-wide`). Deux colonnes plutot qu'un `grid-column:1/-1`
  sur la seule carte 4 : la carte 4 est justement celle dont la plupart des
  puces sont « (a venir) », l'etaler sur toute la largeur l'aurait mise en
  avant plus que les trois autres.

Usage : python3 sources/generate_guso.py   (depuis la racine du depot)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mobile_nav            # hamburger mobile              # noqa: E402
import nav_menu              # menu de navigation partage    # noqa: E402
import verif_commentaires    # garde-fou commentaires HTML   # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, 'guso-facile')
OUT_HTML = os.path.join(OUT_DIR, 'index.html')

#: URL exacte du formulaire, validee. `target="_blank"` OBLIGATOIREMENT
#: accompagne de `rel="noopener"` (regle du site, verifiee par un garde-fou
#: plus bas).
URL_ACCES = 'https://guso-facile.vercel.app/presentation.html'


# =========================================================================
# LE GABARIT
# =========================================================================
# Le squelette (head, variables de couleur, nav, boutons, footer, retour en
# haut) est celui des 9 pages du site, repris a l'identique de
# `le-soin-soa/index.html` : meme charte, meme comportement, aucune divergence
# a maintenir. Seul le bloc « ===== Guso Facile ===== » est propre a la page.
#
# ⚠️ Les deux <link> vers fonts.googleapis.com sont ceux des 9 autres pages.
#    Ce ne sont PAS des polices supplementaires : c'est exactement la meme
#    feuille, deja chargee partout sur le site. Sans elle, Cormorant Garamond
#    et Jost tombent sur Georgia / system-ui et la page ne ressemble plus aux
#    autres. Ne rien ajouter d'autre : aucun script tiers, aucune iframe,
#    aucun traceur.

HEAD = """<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Guso Facile — l’administratif de l’intermittence, simplifié · Résonances Productions</title>
<meta name="description" content="Guso Facile : un outil web créé par David Lesage, relayé par Résonances Productions, qui allège la charge administrative des artistes intermittents. Suivi des 507 heures, DPAE, feuillets GUSO, factures, pointage France Travail. Accès en bêta privée, sur cooptation.">
<meta property="og:title" content="Guso Facile — l’administratif de l’intermittence, simplifié">
<meta property="og:description" content="Suivi des 507 heures, DPAE, feuillets GUSO, factures, pointage France Travail : un outil web pour les artistes intermittents et les structures qui les accompagnent. Bêta privée, sur invitation ou cooptation.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.resonancesproductions.org/guso-facile">
<meta property="og:image" content="https://www.resonancesproductions.org/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://www.resonancesproductions.org/guso-facile">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0e0f24">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
"""

# --- socle commun aux 9 pages (couleurs, typo, nav, boutons, footer) ------
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

# --- CSS propre a la page -------------------------------------------------
# Sobre et sombre : l'or sert de filet, de puce et de badge, jamais d'aplat
# (hors bouton principal). Les fonds de cartes restent sur --card. Rien ne
# descend sous 13 px, plancher typographique du site.
CSS_PAGE = """/* ===== Guso Facile ===== */
.gf-top{padding:128px 0 66px;background:radial-gradient(900px 560px at 8% -10%,rgba(143,122,209,.20),transparent 62%),radial-gradient(720px 470px at 94% 104%,rgba(216,178,90,.12),transparent 62%),linear-gradient(180deg,#0b0c1e,var(--night))}
.gf-top h1{font-size:clamp(38px,7vw,72px);font-weight:600;line-height:1.02;color:#fff;letter-spacing:.02em}
.gf-claim{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(19px,2.8vw,28px);line-height:1.3;margin-top:14px;max-width:720px}
.badge{display:inline-flex;align-items:center;gap:9px;margin-top:26px;padding:8px 17px;border:1px solid var(--line);border-radius:30px;color:var(--gold2);font-size:13.5px;letter-spacing:.12em;text-transform:uppercase;font-weight:500;background:rgba(216,178,90,.06)}
.badge::before{content:'';width:6px;height:6px;border-radius:50%;background:var(--gold);flex:0 0 auto}
.gf-top .cta{margin-top:30px}
.band{background:linear-gradient(180deg,#0b0c1e,var(--night))}
/* hero : texte a gauche, jauge des 507 h a droite (empile sous 1000 px) */
.gf-topgrid{display:grid;gap:34px;align-items:center}
@media(min-width:1000px){.gf-topgrid{grid-template-columns:minmax(0,1fr) 400px}}
/* quatre univers — DEUX colonnes, jamais trois : voir l'entete du fichier */
.univers{display:grid;grid-template-columns:minmax(0,1fr);gap:22px;margin-top:38px}
@media(min-width:761px){.univers{grid-template-columns:repeat(2,minmax(0,1fr))}}
.u-card{background:var(--card);border:1px solid rgba(255,255,255,.06);border-top:2px solid var(--line);border-radius:16px;padding:28px 26px 24px}
.u-num{letter-spacing:.28em;text-transform:uppercase;font-size:13px;font-weight:600;color:var(--gold)}
.u-card h3{font-size:27px;font-weight:600;color:#fff;line-height:1.15;margin-top:7px}
.u-sub{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--plum);font-size:18px;line-height:1.4;margin-top:8px}
.u-card ul{list-style:none;margin-top:18px}
.u-card li{position:relative;padding-left:19px;margin-top:13px;color:#d7d4ea;font-size:15.5px;line-height:1.6}
.u-card li::before{content:'';position:absolute;left:0;top:11px;width:5px;height:5px;border-radius:50%;background:var(--gold)}
.u-card li b{color:#fff;font-weight:500}
.u-card li i{font-style:normal;color:var(--muted)}
.aussi{margin-top:34px;padding-top:22px;border-top:1px solid rgba(255,255,255,.07);max-width:900px}
.aussi .u-num{display:block;margin-bottom:8px}
.aussi p{color:#d7d4ea;font-size:15.5px}
/* trois situations */
.cas-note{color:var(--muted);font-size:15px;margin-top:14px;max-width:62ch}
.cas{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px;margin-top:38px}
.cas article{border-left:1px solid var(--line);padding-left:22px}
.cas h3{font-size:25px;font-weight:600;color:#fff;line-height:1.18}
.cas p{color:#d7d4ea;font-size:15.5px;margin-top:11px}
/* l'etat du projet */
.etat{margin-top:34px;border:1px solid var(--line);border-radius:18px;background:linear-gradient(180deg,rgba(25,27,61,.85),rgba(20,22,51,.55));padding:34px 32px;max-width:900px}
.etat p{color:#d7d4ea;font-size:16px}
.etat p + p{margin-top:16px}
.etat .first{color:#fff;font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(21px,3vw,27px);line-height:1.3;font-style:italic}
/* appel a l'action */
.acces{max-width:820px}
.acces .cta{margin-top:28px}
.mention{margin-top:20px;max-width:660px;color:var(--muted);font-size:14px;line-height:1.65}
.mention + .mention{margin-top:12px}
@media(max-width:760px){
  .gf-top{padding:108px 0 54px}
  .u-card{padding:24px 21px 21px}
  .etat{padding:26px 22px}
  .cas article{border-left:0;border-top:1px solid var(--line);padding-left:0;padding-top:20px}
}
@media print{.totop{display:none}}
"""

# --- CSS des 6 maquettes d'interface --------------------------------------
# Repris de `GUSO-FACILE-BACKUPS/maquettes-pour-resonances.html` (LECTURE
# SEULE), avec les corrections listees dans l'entete du fichier. Regles :
#   - aucune couleur litterale : uniquement les var(--…) de la charte, pour
#     qu'une retouche du theme entraine les maquettes avec elle ;
#   - rien sous 13 px (plancher typographique du site, verifie par _controles) ;
#   - `.gf-shot{overflow:hidden}` : une maquette ne peut pas pousser la page,
#     quoi qu'il arrive a l'interieur ;
#   - toutes les rangees sont en `flex-wrap:wrap` avec un `flex-basis` modeste :
#     c'est ce qui les fait tenir dans une colonne de 306 px a 390 px de large.
# Le `:root` du fichier d'origine n'est PAS repris (les variables existent deja
# sur le site), ni son cadre de page `.gf-page-*` (decor de son fichier de
# test), ni le CSS de l'ancienne version en tableau de la maquette 4.
CSS_MAQUETTES = """/* ===== maquettes d'interface (illustrations, pas d'interface reelle) ===== */
.gf-block{margin:30px 0 0;max-width:820px}
.gf-topgrid .gf-block,.univers .gf-block{margin:0;max-width:none}
.univers .gf-wide{grid-column:1/-1}
.gf-shot{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 16px 16px;margin:0 0 10px;color:var(--ink);font-size:15px;line-height:1.5;max-width:100%;overflow:hidden}
.gf-shot *{box-sizing:border-box}
.gf-cap{display:block;font-size:13px;line-height:1.4;color:var(--muted);letter-spacing:.02em;margin:0 0 0 2px}
.gf-bar{display:flex;align-items:baseline;justify-content:space-between;gap:10px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:10px;margin-bottom:16px}
.gf-bar-t{font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-weight:600;color:var(--ink)}
.gf-bar-s{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
.gf-hint{font-size:13px;color:var(--muted);margin:0 0 14px}
/* 1 — jauge des 507 h : anneau en conic-gradient, aucune image */
.gf-hero{display:flex;gap:20px;align-items:center;flex-wrap:wrap}
.gf-ring{position:relative;flex:0 0 auto;width:146px;height:146px;border-radius:50%;background:conic-gradient(var(--gold) 0 293deg,var(--plum) 293deg 323deg,var(--night2) 323deg 360deg);display:flex;align-items:center;justify-content:center;margin:0 auto}
.gf-ring-in{width:112px;height:112px;border-radius:50%;background:var(--card);display:flex;flex-direction:column;align-items:center;justify-content:center;border:1px solid var(--line)}
.gf-ring-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:38px;line-height:1;font-weight:600;color:var(--gold2)}
.gf-ring-l{font-size:13px;color:var(--muted);margin-top:3px}
.gf-hero-txt{flex:1 1 200px;min-width:0}
.gf-hero-l{font-size:15px;margin:0 0 6px}
.gf-hero-l b{color:var(--gold2);font-weight:600}
.gf-tag{display:inline-block;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--gold);border:1px solid var(--line);border-radius:999px;padding:1px 8px;margin-left:5px}
.gf-anniv{font-size:13px;color:var(--muted);border-left:2px solid var(--gold);padding-left:10px;margin-top:12px}
.gf-split{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px}
.gf-split-c{flex:1 1 140px;min-width:0;background:var(--night2);border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.gf-split-v{font-size:19px;font-weight:600;color:var(--gold2)}
.gf-split-v.gf-poss{color:var(--plum)}
.gf-split-k{font-size:13px;color:var(--muted)}
.gf-legend{display:flex;gap:16px;flex-wrap:wrap;margin-top:12px;font-size:13px;color:var(--muted)}
.gf-dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:6px;vertical-align:baseline}
.gf-dot-gold{background:var(--gold)}
.gf-dot-plum{background:var(--plum)}
.gf-dot-empty{background:var(--night2);border:1px solid var(--line)}
/* 2 — « A faire maintenant » : pastilles urgent / en retard / a venir */
.gf-tn-head{display:flex;align-items:baseline;gap:9px;margin-bottom:12px}
.gf-tn-t{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
.gf-tn-n{margin-left:auto;font-size:13px;font-weight:600;color:var(--night);background:var(--gold);border-radius:999px;padding:1px 9px}
.gf-tn-row{display:flex;align-items:center;gap:11px;flex-wrap:wrap;border:1px solid var(--line);border-radius:10px;background:var(--night2);padding:11px 12px;margin-bottom:8px}
.gf-tn-pill{flex:0 0 auto;width:10px;height:10px;border-radius:50%}
.gf-tn-pill.gf-urgent{background:var(--gold)}
.gf-tn-pill.gf-late{background:var(--plum)}
.gf-tn-pill.gf-soon{background:transparent;border:2px solid var(--gold)}
.gf-tn-main{flex:1 1 150px;min-width:0}
.gf-tn-lbl{display:block;font-size:15px;font-weight:600;color:var(--ink)}
.gf-tn-meta{display:block;font-size:13px;color:var(--muted)}
.gf-tn-when{flex:0 0 auto;font-size:13px;letter-spacing:.06em;text-transform:uppercase;border:1px solid var(--line);border-radius:999px;padding:2px 9px;color:var(--muted)}
.gf-tn-when.gf-urgent{color:var(--night);background:var(--gold);border-color:var(--gold);font-weight:600}
.gf-tn-when.gf-late{color:var(--gold2)}
/* 3 — fiche d'une date et ses cinq etapes administratives */
.gf-kv{display:grid;grid-template-columns:auto minmax(0,1fr);gap:7px 14px;margin:0 0 16px;font-size:15px}
.gf-kv .gf-k{color:var(--muted);font-size:13px;letter-spacing:.04em}
.gf-kv .gf-v{color:var(--ink);font-weight:500;min-width:0;overflow-wrap:anywhere}
.gf-mini{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);margin:0 0 9px}
.gf-steps{display:flex;flex-wrap:wrap;gap:8px}
.gf-step{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--line);border-radius:999px;background:var(--night2);padding:6px 12px;font-size:13px;color:var(--muted)}
.gf-step .gf-box{width:16px;height:16px;border-radius:5px;border:1px solid var(--line);display:inline-flex;align-items:center;justify-content:center;font-size:13px;line-height:1;color:var(--night);flex:0 0 auto}
.gf-step.gf-done{color:var(--ink);border-color:var(--gold)}
.gf-step.gf-done .gf-box{background:var(--gold);border-color:var(--gold)}
/* 4 — recap mensuel France Travail, en cartes groupees par mois */
.gf-recmonth{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin:0 0 10px}
.gf-reccard{border:1px solid var(--line);border-radius:10px;background:var(--night2);padding:10px 12px;margin-bottom:9px}
.gf-recwhen{font-size:13px;color:var(--muted)}
.gf-recnums{font-size:15px;font-weight:600;color:var(--ink);font-variant-numeric:tabular-nums}
.gf-recnums em{font-style:normal;color:var(--gold2)}
.gf-recmeta{font-size:13px;color:var(--muted);overflow-wrap:anywhere}
.gf-rectot{display:flex;gap:8px 14px;align-items:baseline;flex-wrap:wrap;justify-content:space-between;border-top:1px solid var(--gold);margin-top:12px;padding-top:11px}
.gf-rl{font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.gf-rv{font-size:15px;font-weight:600;color:var(--gold2);font-variant-numeric:tabular-nums}
/* 5 — ma tournee : enchainement chronologique, filet + pastilles, zero image */
.gf-route{position:relative;margin:0;padding:0 0 0 24px;list-style:none}
.gf-route::before{content:'';position:absolute;left:5px;top:9px;bottom:9px;width:1px;background:var(--line)}
.gf-stop{position:relative;padding:0 0 15px}
.gf-stop:last-child{padding-bottom:0}
.gf-stop::before{content:'';position:absolute;left:-23px;top:6px;width:11px;height:11px;border-radius:50%;background:var(--night2);border:1px solid var(--gold)}
.gf-stop.gf-cur::before{background:var(--gold)}
.gf-stop.gf-tbc::before{border-style:dashed}
.gf-stop-top{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
.gf-stop-city{font-size:15px;font-weight:600;color:var(--ink)}
.gf-stop-st{margin-left:auto;font-size:13px;letter-spacing:.06em;text-transform:uppercase;white-space:nowrap;color:var(--gold);border:1px solid var(--line);border-radius:999px;padding:1px 9px}
.gf-stop.gf-tbc .gf-stop-st{color:var(--plum)}
.gf-stop-meta{display:block;font-size:13px;color:var(--muted)}
.gf-route-tot{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;margin-top:16px;border-top:1px solid var(--line);padding-top:12px}
.gf-route-tot-v{font-family:'Cormorant Garamond',Georgia,serif;font-size:26px;color:var(--gold2)}
.gf-route-tot-k{font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
/* 6 — tableau de bord d'une structure. La vigilance se lit a la FORME de la
   pastille et a son libelle, pas seulement a la couleur (la charte n'a ni
   vert ni rouge, et un daltonien doit pouvoir la lire). */
.gf-art{display:flex;flex-direction:column;gap:9px}
.gf-art-row{display:flex;align-items:center;gap:12px;flex-wrap:wrap;border:1px solid var(--line);border-radius:10px;background:var(--night2);padding:11px 12px}
.gf-av{flex:0 0 auto;width:34px;height:34px;border-radius:50%;border:1px solid var(--line);display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:600;color:var(--gold2);background:var(--card)}
.gf-art-txt{flex:1 1 130px;min-width:0}
.gf-art-n{display:block;font-size:15px;font-weight:600}
.gf-art-m{display:block;font-size:13px;color:var(--muted)}
.gf-art-h{flex:0 0 auto;text-align:right;font-variant-numeric:tabular-nums}
.gf-art-hv{font-size:15px;font-weight:600;color:var(--gold2)}
.gf-art-hk{display:block;font-size:13px;color:var(--muted)}
.gf-mbar{flex:1 1 100%;height:5px;margin-top:3px;border-radius:3px;background:var(--night);border:1px solid var(--line);overflow:hidden}
.gf-mbar i{display:block;height:100%;background:var(--gold)}
.gf-vig{flex:0 0 auto;display:inline-flex;align-items:center;gap:6px;font-size:13px;letter-spacing:.05em;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:2px 9px}
.gf-vig-s{width:10px;height:10px;border-radius:50%;flex:0 0 auto}
.gf-vig.gf-ok .gf-vig-s{background:var(--gold)}
.gf-vig.gf-warn .gf-vig-s{background:transparent;border:2px solid var(--gold)}
.gf-vig.gf-bad .gf-vig-s{background:transparent;border:2px solid var(--plum);box-shadow:inset 0 0 0 2px var(--plum)}
.gf-vig.gf-bad{color:var(--ink);border-color:var(--plum)}
@media(max-width:760px){.gf-shot{padding:15px 13px 13px}}
"""


# =========================================================================
# LES 6 MAQUETTES — le HTML de chaque bloc
# =========================================================================
# ⚠️ REGLE ABSOLUE POUR CES SIX BLOCS : ce sont des ILLUSTRATIONS.
#    Aucun <a>, <button>, <input>, <select>, <textarea>, aucun [tabindex] :
#    rien de focusable, rien de cliquable, rien qui laisse croire au visiteur
#    qu'il manipule le logiciel depuis le site de l'association. Le garde-fou
#    `_controle_maquettes()` refuse d'ecrire la page au premier ecart.
#    Le gabarit est toujours le meme :
#        <figure class="gf-block">
#          <div class="gf-shot" role="img" aria-label="…"> … </div>
#          <figcaption class="gf-cap">Aperçu de l’interface — données fictives</figcaption>
#        </figure>
#    <figure>/<figcaption> plutot que <section> : c'est exactement une
#    illustration accompagnee de sa legende, et cela evite au passage
#    d'heriter du `section{padding:78px 0}` du site.

#: la mention VISIBLE, identique sur les six blocs. Elle n'est pas decorative :
#: une reproduction credible sans mention est indistinguable d'une vraie
#: capture d'ecran. Comptee par `_controle_maquettes()`.
MENTION_FICTIVE = 'Aperçu de l’interface — données fictives'


def _figure(aria, corps, classe=''):
    """Enveloppe un bloc de maquette : role=img + aria-label + mention visible."""
    return ('<figure class="gf-block%s">\n'
            '  <div class="gf-shot" role="img" aria-label="%s">%s</div>\n'
            '  <figcaption class="gf-cap">%s</figcaption>\n'
            '</figure>\n' % (classe, aria, corps, MENTION_FICTIVE))


# --- 1. LA JAUGE DES 507 H (hero) ----------------------------------------
# Ecran reproduit : tableau de bord, bloc « Ou j'en suis — periode en cours ».
# C'est l'image signature de l'outil, d'ou sa place dans le hero.
# ⚠️ L'ANNEAU : 412/507 = 81,26 % -> 293deg pour l'arc « heures validees ».
#    Les 43 h de dates possibles valent 43/507 x 360 = 30,5deg, DONC l'arc
#    prune s'arrete a 323deg. Le fichier d'origine ecrivait 336deg (= 293+43),
#    en prenant des heures pour des degres : la jauge annoncait visuellement
#    ~12 % de dates possibles au lieu de 8,5 %. Corrige ici.
# Coherence des donnees fictives (Camille Ferrand) : 28 cachets x 12 h = 336 h,
# + 76 h de repetitions = 412 h. Reste 95 h = 8 cachets, ou 4 cachets + 47 h.
MAQ_JAUGE = _figure(
    'Tableau de bord de Guso Facile : la jauge des 507 heures, 412 heures '
    'validées sur 507, il reste 95 heures à trouver avant la date anniversaire '
    'du 16 août.',
    """
    <div class="gf-bar">
      <span class="gf-bar-t">Où j’en suis — période en cours</span>
      <span class="gf-bar-s">Camille Ferrand</span>
    </div>
    <p class="gf-hint">Période du 17 août 2025 au 16 août 2026 — les 12 mois qui comptent pour les 507 h.</p>
    <div class="gf-hero">
      <div class="gf-ring">
        <div class="gf-ring-in">
          <span class="gf-ring-n">412</span>
          <span class="gf-ring-l">/ 507 h</span>
        </div>
      </div>
      <div class="gf-hero-txt">
        <p class="gf-hero-l">J’ai effectué <b>412 h</b> sur <b>507 h</b><span class="gf-tag">confirmé</span></p>
        <p class="gf-hero-l">Il me reste <b>95 h</b> à trouver</p>
        <p class="gf-hero-l">dans <b>47 jours</b></p>
        <p class="gf-anniv">Date anniversaire le <b>16 août</b> — soit environ 8 cachets, ou 4 cachets et 47 h de répétitions.</p>
      </div>
    </div>
    <div class="gf-split">
      <div class="gf-split-c">
        <div class="gf-split-v">412 h</div>
        <div class="gf-split-k">heures validées — 24 dates confirmées</div>
      </div>
      <div class="gf-split-c">
        <div class="gf-split-v gf-poss">+ 43 h</div>
        <div class="gf-split-k">dates possibles — 3 options à confirmer</div>
      </div>
      <div class="gf-split-c">
        <div class="gf-split-v">28 · 76 h</div>
        <div class="gf-split-k">cachets · heures de répétition</div>
      </div>
    </div>
    <p class="gf-legend">
      <span><span class="gf-dot gf-dot-gold"></span>heures validées</span>
      <span><span class="gf-dot gf-dot-plum"></span>dates possibles</span>
      <span><span class="gf-dot gf-dot-empty"></span>reste à trouver</span>
    </p>
  """)


# --- 2. « A FAIRE MAINTENANT » (fin de #promesse) -------------------------
# Ecran reproduit : bloc #todoNow du tableau de bord, echeances triees par
# urgence. Il repond litteralement a la derniere phrase du paragraphe qui le
# precede : « qu'est-ce que j'ai a faire maintenant ? ».
# L'emoji 🔔 du fichier d'origine a ete retire (charte : aucun emoji).
MAQ_TODO = _figure(
    'Bloc « À faire maintenant » de Guso Facile : trois échéances '
    'administratives triées par urgence — une DPAE à faire dans 2 jours, un '
    'feuillet GUSO en retard et une facture encore à envoyer.',
    """
    <div class="gf-tn-head">
      <span class="gf-tn-t">À faire maintenant</span>
      <span class="gf-tn-n">3</span>
    </div>
    <div class="gf-tn-row">
      <span class="gf-tn-pill gf-urgent"></span>
      <span class="gf-tn-main">
        <span class="gf-tn-lbl">DPAE à faire</span>
        <span class="gf-tn-meta">Théâtre du Pont Tournant, Bordeaux · 12 juin 2026</span>
      </span>
      <span class="gf-tn-when gf-urgent">dans 2 j</span>
    </div>
    <div class="gf-tn-row">
      <span class="gf-tn-pill gf-late"></span>
      <span class="gf-tn-main">
        <span class="gf-tn-lbl">Feuillet GUSO à éditer</span>
        <span class="gf-tn-meta">Le Rocher de Palmer, Cenon · 14 mars 2026</span>
      </span>
      <span class="gf-tn-when gf-late">en retard</span>
    </div>
    <div class="gf-tn-row">
      <span class="gf-tn-pill gf-soon"></span>
      <span class="gf-tn-main">
        <span class="gf-tn-lbl">Facture à envoyer</span>
        <span class="gf-tn-meta">Festival Ouvre-Boîte, Pau · 2 mai 2026</span>
      </span>
      <span class="gf-tn-when gf-late">en attente</span>
    </div>
  """)


# --- 3. LA FICHE D'UNE DATE (grille des univers) --------------------------
# Ecran reproduit : la fenetre de detail d'une date, avec ses CINQ etapes
# administratives — celles de l'app, exactement : DPAE, feuillet GUSO, facture
# reglee, salaire recu, actualisation France Travail.
# ⚠️ Le fichier d'origine listait DEUX FOIS « Salaire recu » (une cochee, une
#    non) et omettait « Actualisation France Travail », alors que son propre
#    aria-label annonce cinq etapes dont trois cochees. Corrige ici.
# L'emoji 🎤 du titre a ete retire (charte : aucun emoji).
MAQ_FICHE = _figure(
    'Fiche d’une date dans Guso Facile : concert au Rocher de Palmer à Cenon '
    'le 14 mars 2026, 2 cachets soit 24 heures, avec les cinq étapes '
    'administratives dont trois sont cochées.',
    """
    <div class="gf-bar">
      <span class="gf-bar-t">Concert — Le Rocher de Palmer, Cenon</span>
      <span class="gf-bar-s">14 mars 2026</span>
    </div>
    <p class="gf-hint">Camille Ferrand · artiste (annexe 10) · date confirmée</p>
    <div class="gf-kv">
      <div class="gf-k">Période</div><div class="gf-v">14 mars 2026</div>
      <div class="gf-k">Lieu</div><div class="gf-v">Le Rocher de Palmer — Cenon (33)</div>
      <div class="gf-k">Cachets</div><div class="gf-v">2 cachets = 24 h</div>
      <div class="gf-k">Répétition</div><div class="gf-v">0 h</div>
      <div class="gf-k">Total comptabilisé</div><div class="gf-v">24 h</div>
      <div class="gf-k">Salaire brut</div><div class="gf-v">1 084,00 €</div>
    </div>
    <p class="gf-mini">Étapes administratives</p>
    <div class="gf-steps">
      <span class="gf-step gf-done"><span class="gf-box">✓</span>DPAE</span>
      <span class="gf-step gf-done"><span class="gf-box">✓</span>Feuillet GUSO</span>
      <span class="gf-step gf-done"><span class="gf-box">✓</span>Salaire reçu</span>
      <span class="gf-step"><span class="gf-box"></span>Facture réglée</span>
      <span class="gf-step"><span class="gf-box"></span>Actualisation France Travail</span>
    </div>
  """)


# --- 4. LE RECAP MENSUEL FRANCE TRAVAIL (#situations) ---------------------
# Ecran reproduit : la fenetre « Recap mensuel », qui groupe les declarations
# par mois — UNE CARTE par declaration, comme dans l'app (buildRecap).
# ⚠️ Le fichier d'origine avait ete refait en cartes, MAIS SANS SON CSS : seul
#    subsistait celui de l'ancienne version en tableau. Les classes .gf-rec*
#    sont donc habillees ici (voir CSS_MAQUETTES).
# ⚠️ « Association Chant Libre » est a LIMOGES (le fichier d'origine la mettait
#    a Pau dans ce bloc et a Limoges dans la tournee).
# Comptes verifies : 2+1+2 = 5 cachets ; 24+12+33 = 69 h ;
#                    1084,00 + 528,00 + 1246,50 = 2 858,50 €.
# Place sous les trois cas d'usage parce qu'il illustre LITTERALEMENT celui de
# Marco (« Le recapitulatif mensuel lui donne une ligne par GUSO »).
MAQ_RECAP = _figure(
    'Récapitulatif mensuel de Guso Facile pour mars 2026 : les déclarations du '
    'mois, chacune avec sa date, ses cachets, ses heures et son salaire brut, '
    'puis le total du mois à reporter sur l’actualisation France Travail.',
    """
    <div class="gf-bar">
      <span class="gf-bar-t">Mes activités à déclarer</span>
      <span class="gf-bar-s">Récap mensuel</span>
    </div>
    <p class="gf-recmonth">Mars 2026</p>
    <div class="gf-reccard">
      <div class="gf-recwhen">14 mars 2026</div>
      <div class="gf-recnums">2 cachets · 24 h · <em>1 084,00 €</em></div>
      <div class="gf-recmeta">Le Rocher de Palmer, Cenon · GUSO n° 6 508 798 010</div>
    </div>
    <div class="gf-reccard">
      <div class="gf-recwhen">21 mars 2026</div>
      <div class="gf-recnums">1 cachet · 12 h · <em>528,00 €</em></div>
      <div class="gf-recmeta">Association Chant Libre, Limoges · GUSO n° 6 494 883 156</div>
    </div>
    <div class="gf-reccard">
      <div class="gf-recwhen">27 au 29 mars 2026</div>
      <div class="gf-recnums">2 cachets · 33 h · <em>1 246,50 €</em></div>
      <div class="gf-recmeta">Scène Nationale, Bayonne · GUSO n° 6 454 979 578 · 9 h de répétition</div>
    </div>
    <div class="gf-rectot">
      <span class="gf-rl">Total du mois</span>
      <span class="gf-rv">5 cachets · 69 h · 2 858,50 € bruts</span>
    </div>
  """)


# --- 5. MA TOURNEE (grille des univers) -----------------------------------
# Ecran reproduit : l'espace « Ma tournee » — les dates enchainees
# chronologiquement, les lieux encore a confirmer signales.
# ⚠️⚠️ LE KILOMETRAGE A ETE RETIRE. La note de livraison du fichier d'origine
#    dit : « L'espace Ma tournee de l'app liste les dates et les contacts, mais
#    ne calcule pas de kilometrage […] elle ne correspond pas (encore) a une
#    fonction existante de l'application. » Illustrer « 1 240 km parcourus »
#    aurait donc mis en image une fonction inexistante — exactement ce que la
#    page s'interdit ailleurs (la Guilde, « Je cree mon contrat »).
#    ⚠️ A ARBITRER PAR DAVID : la puce « Carte des dates » de l'univers 2 ecrit
#    pourtant AU PRESENT « avec le calcul des kilometres parcourus depuis le
#    domicile ». Texte valide, non modifie ici — mais il contredit l'auteur de
#    l'application. L'un des deux doit bouger.
# Les six etapes ne citent que des dates et des lieux qui existent DEJA dans
# les autres maquettes (Cenon, Limoges, Bayonne, Pau, Bordeaux), plus une
# option a confirmer, seule facon d'illustrer « les lieux a confirmer sont
# signales » sans contredire les autres blocs.
MAQ_TOURNEE = _figure(
    'Espace « Ma tournée » de Guso Facile : six étapes reliées '
    'chronologiquement, de Cenon à La Rochelle, dont cinq dates confirmées et '
    'une option encore à confirmer.',
    """
    <div class="gf-bar">
      <span class="gf-bar-t">Ma tournée — saison 2026</span>
      <span class="gf-bar-s">6 étapes</span>
    </div>
    <ul class="gf-route">
      <li class="gf-stop">
        <span class="gf-stop-top">
          <span class="gf-stop-city">Cenon</span>
          <span class="gf-stop-st">confirmée</span>
        </span>
        <span class="gf-stop-meta">14 mars · Le Rocher de Palmer · 2 cachets</span>
      </li>
      <li class="gf-stop">
        <span class="gf-stop-top">
          <span class="gf-stop-city">Limoges</span>
          <span class="gf-stop-st">confirmée</span>
        </span>
        <span class="gf-stop-meta">21 mars · Association Chant Libre · 1 cachet</span>
      </li>
      <li class="gf-stop">
        <span class="gf-stop-top">
          <span class="gf-stop-city">Bayonne</span>
          <span class="gf-stop-st">confirmée</span>
        </span>
        <span class="gf-stop-meta">27 au 29 mars · Scène Nationale · 2 cachets</span>
      </li>
      <li class="gf-stop">
        <span class="gf-stop-top">
          <span class="gf-stop-city">Pau</span>
          <span class="gf-stop-st">confirmée</span>
        </span>
        <span class="gf-stop-meta">2 mai · Festival Ouvre-Boîte · 2 cachets</span>
      </li>
      <li class="gf-stop gf-cur">
        <span class="gf-stop-top">
          <span class="gf-stop-city">Bordeaux</span>
          <span class="gf-stop-st">confirmée</span>
        </span>
        <span class="gf-stop-meta">12 juin · Théâtre du Pont Tournant · 1 cachet</span>
      </li>
      <li class="gf-stop gf-tbc">
        <span class="gf-stop-top">
          <span class="gf-stop-city">La Rochelle</span>
          <span class="gf-stop-st">à confirmer</span>
        </span>
        <span class="gf-stop-meta">3 juillet · lieu non encore arrêté · option</span>
      </li>
    </ul>
    <p class="gf-route-tot">
      <span class="gf-route-tot-v">8 cachets</span>
      <span class="gf-route-tot-k">sur 5 dates confirmées · 1 option à confirmer</span>
    </p>
  """)


# --- 6. LE TABLEAU DE BORD D'UNE STRUCTURE (grille des univers) -----------
# Ecran reproduit : la vue « Mes artistes » du back-office structure.
# Il illustre l'univers 3 ET le cas de Sophie ; place en PLEINE LARGEUR de la
# grille (.gf-wide) parce que ses rangees sont larges par nature.
# ⚠️ L'aria-label d'origine annoncait un indicateur « vert, orange ou rouge » :
#    la charte n'a ni vert ni rouge, le rendu emploie la FORME de la pastille
#    (pleine / contour / contour epais) et un libelle. Un lecteur d'ecran
#    entendait donc des couleurs absentes de l'ecran. Reecrit avec les trois
#    libelles reellement affiches.
# Barres : 412/507 = 81 % · 348 = 69 % · 261 = 51 % · 154 = 30 %.
MAQ_STRUCTURE = _figure(
    'Tableau de bord d’une structure dans Guso Facile : quatre artistes, leur '
    'compteur d’heures sur 507 et leur niveau de vigilance — bon rythme, à '
    'surveiller ou seuil menacé.',
    """
    <div class="gf-bar">
      <span class="gf-bar-t">Mes artistes</span>
      <span class="gf-bar-s">Espace structure</span>
    </div>
    <p class="gf-hint">Chaque artiste, ses heures sur la période, et le niveau de vigilance avant sa date anniversaire.</p>
    <div class="gf-art">
      <div class="gf-art-row">
        <span class="gf-av">CF</span>
        <span class="gf-art-txt">
          <span class="gf-art-n">Camille Ferrand</span>
          <span class="gf-art-m">Chanteuse · anniversaire le 16 août</span>
        </span>
        <span class="gf-art-h"><span class="gf-art-hv">412 h</span><span class="gf-art-hk">/ 507 h</span></span>
        <span class="gf-vig gf-ok"><span class="gf-vig-s"></span>bon rythme</span>
        <span class="gf-mbar"><i style="width:81%"></i></span>
      </div>
      <div class="gf-art-row">
        <span class="gf-av">NB</span>
        <span class="gf-art-txt">
          <span class="gf-art-n">Nadia Belkacem</span>
          <span class="gf-art-m">Violoncelliste · anniversaire le 3 octobre</span>
        </span>
        <span class="gf-art-h"><span class="gf-art-hv">348 h</span><span class="gf-art-hk">/ 507 h</span></span>
        <span class="gf-vig gf-ok"><span class="gf-vig-s"></span>bon rythme</span>
        <span class="gf-mbar"><i style="width:69%"></i></span>
      </div>
      <div class="gf-art-row">
        <span class="gf-av">TR</span>
        <span class="gf-art-txt">
          <span class="gf-art-n">Tomas Riveiro</span>
          <span class="gf-art-m">Percussionniste · anniversaire le 21 juillet</span>
        </span>
        <span class="gf-art-h"><span class="gf-art-hv">261 h</span><span class="gf-art-hk">/ 507 h</span></span>
        <span class="gf-vig gf-warn"><span class="gf-vig-s"></span>à surveiller</span>
        <span class="gf-mbar"><i style="width:51%"></i></span>
      </div>
      <div class="gf-art-row">
        <span class="gf-av">EV</span>
        <span class="gf-art-txt">
          <span class="gf-art-n">Émile Vasseur</span>
          <span class="gf-art-m">Ingénieur du son · anniversaire le 9 juin</span>
        </span>
        <span class="gf-art-h"><span class="gf-art-hv">154 h</span><span class="gf-art-hk">/ 507 h</span></span>
        <span class="gf-vig gf-bad"><span class="gf-vig-s"></span>seuil menacé</span>
        <span class="gf-mbar"><i style="width:30%"></i></span>
      </div>
    </div>
  """, classe=' gf-wide')


def build_html():
    """Construit la page complete (sans le menu : il est injecte apres)."""
    B = []
    A = B.append

    A(HEAD)
    A(CSS_BASE)
    A(CSS_PAGE)
    A(CSS_MAQUETTES)
    A('</style>\n</head>\n')
    A('<body id="top">\n')

    # --- barre de navigation ---------------------------------------------
    # Ce <div class="links"> est un GABARIT MINIMAL : `nav_menu.inject()` le
    # remplace integralement par le menu partage des 9 pages. Ne pas essayer
    # d'y ecrire les entrees a la main.
    A("""
<nav class="nav">
  <a href="/" class="brand">Résonances Productions</a>
  <div class="links">
    <a href="/">Accueil</a>
  </div>
</nav>
""")

    # =====================================================================
    # 1. TITRE ET ACCROCHE  (section 1 du contenu fourni)
    # =====================================================================
    # Kicker MODIFIE : « Un outil de Resonances Productions » -> « Cree par
    # David Lesage · relaye par l'association ». Voir l'entete du fichier :
    # l'outil n'est pas porte par l'association a ce jour.
    #
    # Le badge « Beta privee · places limitees » est ICI et non dans la
    # section 6 : l'acces limite doit se voir sans faire defiler la page.
    #
    # MAQUETTE 1 (`MAQ_JAUGE`) — « le tableau de bord avec la jauge des
    #   507 heures », l'image signature de l'outil. Elle est en colonne de
    #   DROITE de ce hero (grille `minmax(0,1fr) 400px` au-dela de 1000 px,
    #   empilee sous le bouton en dessous : l'outil est beaucoup utilise sur
    #   telephone, et la jauge doit y rester la premiere chose qu'on voit
    #   apres le titre).
    #   Ce n'est PAS une capture d'ecran : aucune image n'entre sur cette page
    #   (l'anneau est un `conic-gradient`). Voir l'entete du fichier.
    A("""
<header class="gf-top"><div class="wrap"><div class="gf-topgrid">
  <div>
  <p class="kick">Créé par David Lesage · relayé par l’association</p>
  <h1>Guso Facile</h1>
  <p class="gf-claim">L’intermittence est un métier. La paperasse ne devrait pas en être un deuxième.</p>
  <p class="lead">Guso Facile est un outil web qui prend en charge le suivi administratif du spectacle
    vivant — heures, déclarations, feuillets, factures — pour que les artistes gardent leur énergie là
    où elle compte.</p>
  <p class="badge">Bêta privée · places limitées</p>
  <div class="cta">
    <a class="btn ghost" href="#acces">Comment demander un accès</a>
  </div>
  </div>
""")
    A(MAQ_JAUGE)
    A("""</div></div></header>
""")

    # =====================================================================
    # 2. LA PROMESSE  (section 2 du contenu fourni — verbatim)
    # =====================================================================
    # MAQUETTE 2 (`MAQ_TODO`) — « A faire maintenant » : DPAE, feuillets et
    #   factures classes par urgence. Elle est posee EN FIN de cette section,
    #   juste sous la phrase qui la nomme (« qu'est-ce que j'ai a faire
    #   maintenant ? ») : c'est la reponse en image a la question du texte.
    A("""
<div class="divider"></div>
<section id="promesse"><div class="wrap">
  <p class="kick">La promesse</p>
  <h2 class="sec-title">Ce que l’outil résout</h2>
  <p class="body">La charge mentale de l’intermittence ne vient pas des heures jouées, mais de tout ce
    qui les entoure : savoir où l’on en est de ses 507 heures, ne pas rater une DPAE, retrouver le
    feuillet GUSO du mois dernier, relancer une facture impayée, et pointer juste chaque fin de mois à
    France Travail. Guso Facile rassemble tout cela en un seul endroit et transforme cette liste diffuse
    en une seule question, posée chaque jour : qu’est-ce que j’ai à faire maintenant ?</p>
  <p class="body">Concrètement, l’artiste saisit ses dates ; l’outil en déduit les heures acquises, les
    échéances, les documents à produire et les sommes à encaisser. Rien à installer : cela fonctionne
    dans un navigateur, sur ordinateur comme sur téléphone.</p>
""")
    A(MAQ_TODO)
    A("""</div></section>
""")

    # =====================================================================
    # 3. LE LIEN AVEC L'ASSOCIATION  (section 3 du contenu fourni, CORRIGEE)
    # =====================================================================
    # ⚠️ SECTION LA PLUS SENSIBLE DE LA PAGE. Lire l'entete du fichier avant
    # d'y toucher : « porte par », « projet de l'association », « mis a
    # disposition par l'association » sont FAUX a ce jour et seraient
    # ecrits sur le site public d'une association a propos d'un outil qui
    # traite des numeros de securite sociale et des IBAN.
    #
    # L'argumentaire du contenu fourni est conserve tel quel — il est bon :
    # un outil qui simplifie l'administratif des intermittents entre
    # pleinement dans l'objet d'une structure de soutien aux artistes. Seul
    # le lien juridique est corrige.
    A("""
<div class="divider"></div>
<section id="association-lien" class="band"><div class="wrap">
  <p class="kick">Le lien avec l’association</p>
  <h2 class="sec-title">Pourquoi Résonances Productions le relaie</h2>
  <p class="body">Guso Facile est un outil <b>créé par David Lesage</b>, musicien intermittent et
    co-fondateur de l’association. Résonances Productions le <b>relaie</b> parce qu’il sert directement
    son objet : le soutien aux artistes.</p>
  <p class="body">L’objet de Résonances Productions est le soutien et la promotion des artistes. Ce
    soutien est d’abord artistique, mais il est aussi, très concrètement, administratif : une grande
    part du temps que l’association passe auprès des artistes qu’elle accompagne est consacrée à des
    déclarations, des feuillets et des échéances. Guso Facile est né de ce constat, et son développement
    continue de se nourrir des retours des artistes qui l’utilisent.</p>
  <p class="mention">Précision : Guso Facile n’est pas un service de l’association. L’outil, son
    hébergement et les données qu’il traite relèvent de son créateur.</p>
</div></section>
""")

    # =====================================================================
    # 4. LES FONCTIONNALITES  (section 4 du contenu fourni — verbatim)
    # =====================================================================
    # Quatre blocs, intitules en Cormorant Garamond, puces en point d'or.
    # Aucun emoji, conformement a la charte.
    #
    # LES TROIS MAQUETTES DE CETTE SECTION sont des elements de la grille
    # `.univers`, pas des blocs poses a cote d'elle : la grille est a DEUX
    # colonnes au-dela de 761 px, la lecture donne donc
    #     univers 1 | univers 2
    #     fiche de date | ma tournee
    #     univers 3 | univers 4
    #     tableau de bord structure (pleine largeur)
    # et, en une colonne sur telephone, le meme ordre a la verticale.
    # ⚠️ NI la Guilde NI « Je cree mon contrat » ne sont illustrees : ces deux
    #    fonctionnalites sont « (a venir) » (la base existe, l'ecran non). Les
    #    mettre en image les ferait passer pour livrees, ce que trois clics
    #    d'un beta-testeur suffiraient a dementir.
    A("""
<div class="divider"></div>
<section id="fonctionnalites"><div class="wrap">
  <p class="kick">Les fonctionnalités</p>
  <h2 class="sec-title">Ce que fait l’outil</h2>

  <div class="univers">

    <article class="u-card">
      <p class="u-num">Univers 1</p>
      <h3>Tes droits, maîtrisés</h3>
      <p class="u-sub">Ne plus jamais perdre une heure ni rater une échéance.</p>
      <ul>
        <li><b>Jauge des 507 heures</b> — la progression vers l’ouverture de droits, toujours visible.</li>
        <li><b>« À faire maintenant »</b> — DPAE, feuillets GUSO et factures à venir, classés par urgence (J-3, J-7).</li>
        <li><b>Alertes de cohérence</b> — un badge « droits sécurisés » dès 507 heures, et un signalement cliquable dès qu’une incohérence se glisse dans les dates saisies.</li>
        <li><b>Récapitulatif mensuel</b> — GUSO, cachets, heures et brut mois par mois, prêt à reporter dans l’actualisation France Travail.</li>
        <li><b>Bilan imprimable</b> — un contrôle de cohérence complet de la période, exporté en un document propre.</li>
        <li><b>Graphique annuel</b> — les heures acquises, et ce que les dates encore « possibles » ajouteraient à la projection.</li>
      </ul>
    </article>

    <article class="u-card">
      <p class="u-num">Univers 2</p>
      <h3>Ta tournée, organisée</h3>
      <p class="u-sub">Développer, relancer, négocier — et savoir avant de dire oui.</p>
      <ul>
        <li><b>Carte des dates</b> — les concerts géolocalisés, avec le calcul des kilomètres parcourus depuis le domicile, utile pour les frais.</li>
        <li><b>Tournée reliée</b> — les dates s’enchaînent chronologiquement sur la carte, les lieux à confirmer sont signalés, les adresses en autocomplétion.</li>
        <li><b>Carnet de contacts</b> — les organisateurs rassemblés automatiquement, avec l’historique des dates jouées ensemble.</li>
        <li><b>Modèles de mails</b> — relance, présentation, remerciement, pré-remplis avec la dernière date jouée avec l’interlocuteur.</li>
        <li><b>Évaluation d’une proposition</b> — l’offre reçue comparée aux conditions idéales de l’artiste, avec un verdict vert, jaune ou rouge avant de s’engager.</li>
        <li><b>Suivi de négociation</b> — statut du contrat, échéance de signature, informations manquantes, et une demande d’informations prête à envoyer.</li>
"""
      # -------------------------------------------------------------------
      # « Je cree mon contrat » — FONCTIONNALITE NON LIVREE : ECRITE AU FUTUR
      # -------------------------------------------------------------------
      # Etat au 14/08/2026, donne par la session qui developpe Guso Facile :
      # le modele d'engagement en 12 rubriques existe EN BASE DE DONNEES,
      # mais l'ECRAN qui le remplit N'EXISTE PAS ENCORE. L'ecrire au present
      # reviendrait a vendre une fonctionnalite qu'un beta-testeur constate
      # absente en trois clics — sur le site public d'une association.
      # D'ou : meme traitement visuel « a venir » que les deux mentions deja
      # presentes dans l'univers 4 (`<i>(a venir)</i>`, rendu en gris par
      # `.u-card li i`), et formulation SOBRE — aucune description du contenu
      # des rubriques, aucune date de livraison annoncee.
      # Cette ligne est placee dans l'univers 2 (« Ta tournee, organisee »)
      # parce que c'est la que se traite la relation a l'organisateur :
      # evaluation de la proposition, puis suivi de negociation, puis contrat.
      """        <li><b>Je crée mon contrat</b> <i>(à venir)</i> — un modèle d’engagement en 12 rubriques, personnalisable, pour poser un cadre clair avec l’organisateur.</li>
      </ul>
    </article>
""")

    # MAQUETTE 3 (`MAQ_FICHE`) — la fiche d'une date et ses cinq etapes
    #   administratives, et MAQUETTE 5 (`MAQ_TOURNEE`) — l'enchainement
    #   chronologique des dates. Elles closent la rangee des univers 1 et 2 :
    #   la premiere montre ce que devient UNE date une fois saisie, la seconde
    #   ce que devient la SUITE des dates. (Le kilometrage annonce dans le
    #   fichier d'origine a ete retire : voir l'entete, il ne correspond a
    #   aucune fonction livree.)
    A(MAQ_FICHE)
    A(MAQ_TOURNEE)

    A("""
    <article class="u-card">
      <p class="u-num">Univers 3</p>
      <h3>Ta structure, connectée</h3>
      <p class="u-sub">Pour celles et ceux qui emploient et accompagnent les artistes.</p>
      <ul>
        <li><b>Back-office transversal</b> — toutes les DPAE, feuillets GUSO et factures à faire, tous artistes confondus, au même endroit.</li>
        <li><b>Fiches artistes</b> — état civil, numéro de sécurité sociale, numéro GUSO, accessibles en un clic pour remplir une DPAE sans rien redemander.</li>
        <li><b>DPAE regroupées</b> — les dates proches (à sept jours près) rassemblées pour tout déclarer d’un coup.</li>
        <li><b>Factures et salaires</b> — dépôt des factures, marquage « facture réglée » et « salaire reçu » : qui est payé, ce qui reste dû.</li>
        <li><b>Multi-artistes</b> — conditions idéales, coordonnées bancaires, contrats, plusieurs artistes gérés côte à côte.</li>
        <li><b>Synchronisation</b> — ce que l’artiste renseigne apparaît côté structure en temps réel, et inversement.</li>
      </ul>
    </article>

    <article class="u-card">
      <p class="u-num">Univers 4</p>
      <h3>Ton cercle, solidaire</h3>
      <p class="u-sub">Parce qu’on avance mieux à plusieurs. Cet univers est en cours de déploiement.</p>
      <ul>
        <li><b>Vue groupe</b> — où en est chaque membre du groupe, pour se soutenir avant que la situation ne coince.</li>
        <li><b>« J’ai besoin d’aide »</b> — trois questions simples, un premier conseil concret, et la possibilité de prévenir qui l’on veut.</li>
"""
      # -------------------------------------------------------------------
      # « Faire decouvrir l'outil » (cooptation) — FONCTIONNALITE LIVREE
      # -------------------------------------------------------------------
      # Celle-ci EST en production (etat au 14/08/2026) : elle s'ecrit donc au
      # PRESENT, sans mention « a venir ». Texte repris quasi verbatim de la
      # session qui developpe Guso Facile ; seule la ponctuation a ete alignee
      # sur le gabarit des puces (titre en <b>, tiret cadratin, puis la
      # phrase). Ne pas la reformuler en promesse commerciale : la derniere
      # phrase (« Chaque acces reste une decision, jamais une inscription
      # automatique ») dit la meme chose que les deux mentions sous le bouton
      # de la section « Manifester son interet » — c'est voulu, la page doit
      # etre coherente d'un bout a l'autre sur ce point.
      """        <li><b>Faire découvrir l’outil</b> — un membre peut recommander Guso Facile à un autre artiste : il renseigne ses coordonnées, l’application prépare un message qu’il peut modifier, et la demande arrive chez David, qui l’étudie personnellement. Chaque accès reste une décision, jamais une inscription automatique.</li>
"""
      # ===================================================================
      # ⚠️⚠️ « L'ENTRAIDE ENTRE ARTISTES » (la Guilde) — CONTRAINTE
      #        REDACTIONNELLE STRICTE. LIRE AVANT DE TOUCHER A CE BLOC.
      # ===================================================================
      # 1. C'est une fonctionnalite NON LIVREE : la base de donnees existe,
      #    L'ECRAN N'EXISTE PAS ENCORE (etat au 14/08/2026). Elle s'ecrit donc
      #    AU FUTUR et porte OBLIGATOIREMENT la mention `<i>(a venir)</i>`,
      #    comme les autres a-venir de la page. Ne jamais la passer au present
      #    « parce que la phrase coule mieux ».
      #
      # 2. LE POINT DELICAT : cette fonctionnalite fait porter a des artistes
      #    des AFFIRMATIONS FACTUELLES SUR DES EMPLOYEURS IDENTIFIABLES. Elle
      #    est reservee aux membres connectes, mais LA PAGE QUI LA DECRIT EST
      #    PUBLIQUE ET INDEXEE. Si ce paragraphe se lit comme « une plateforme
      #    qui note les employeurs du spectacle », un programmateur mecontent
      #    ecrira a l'association — qui n'heberge meme pas l'outil.
      #
      # 3. VOCABULAIRE INTERDIT DANS CE BLOC, sans exception ni synonyme
      #    deguise :
      #        noter · notation · signaler · denoncer · avis · evaluation ·
      #        blacklist · reputation
      #    (Ces mots existent ailleurs sur la page — « signaler un bug »,
      #     « Evaluation d'une proposition » — c'est normal : l'interdit porte
      #     sur CE bloc, et le garde-fou `_controle_guilde()` plus bas ne
      #     controle que lui.)
      #
      # 4. POINTS D'APPUI a utiliser si le texte doit un jour etre retravaille :
      #        - reserve aux MEMBRES CONNECTES : jamais public, jamais indexe ;
      #        - uniquement des FAITS BINAIRES (contrat fourni / pas fourni,
      #          paye dans les delais / non) ;
      #        - AUCUN commentaire libre, AUCUN espace de debat ;
      #        - la sortie proposee est constructive (un modele de contrat a
      #          poser la prochaine fois), pas punitive.
      #
      # 5. Le texte ci-dessous est celui VALIDE par la session qui developpe
      #    Guso Facile, repris quasi verbatim. Seule la ponctuation a ete
      #    adaptee au gabarit des puces. Ne pas le « fluidifier ».
      """        <li><b>L’entraide entre artistes</b> <i>(à venir)</i> — entre membres, on partagera ce qui s’est
          concrètement passé sur une date : le contrat a-t-il été fourni, le paiement est-il arrivé dans les
          délais, les conditions annoncées ont-elles été tenues. Rien que des faits, jamais d’appréciation.
          L’idée n’est pas de juger qui que ce soit, mais de s’informer entre pairs — comme on le fait déjà
          de bouche à oreille, en tournée ou en loge. Et quand le cadre a manqué, l’outil proposera plutôt
          d’aider à le poser la prochaine fois, avec un modèle de contrat prêt à personnaliser.</li>
        <li><b>Points de vigilance côté structure</b> <i>(à venir)</i> — qui approche du seuil, qui aurait besoin d’un coup de main.</li>
        <li><b>Confidentialité graduée</b> <i>(à venir)</i> — chaque artiste choisit exactement ce que chaque structure voit de ses données.</li>
      </ul>
    </article>
""")

    # MAQUETTE 6 (`MAQ_STRUCTURE`) — la vue « Mes artistes » du back-office.
    #   Pleine largeur de la grille (`.gf-wide`) : ses rangees sont larges par
    #   nature, et c'est l'ecran qui parle aux STRUCTURES — donc aussi a
    #   l'association elle-meme, qui accompagne des artistes.
    A(MAQ_STRUCTURE)

    A("""
  </div>

  <div class="aussi">
    <p class="u-num">Et aussi</p>
    <p>Export et import des données · fonctionne sur mobile sans installation · liens directs vers une
      date · comptes sécurisés · un bouton pour signaler un bug depuis n’importe quel écran.</p>
  </div>
</div></section>
""")

    # =====================================================================
    # 5. CAS D'USAGE  (section 5 du contenu fourni — verbatim)
    # =====================================================================
    # Lea, Marco et Sophie sont des personnages ENTIEREMENT FICTIFS, confirme
    # le 14/08/2026 par la session qui developpe Guso Facile : les seules
    # personnes reelles de l'app sont David, Iris, Yannick et Christophe.
    # Aucun nom de beta-testeur, aucune coordonnee, aucune donnee reelle ne
    # doit apparaitre ici (depot PUBLIC).
    #
    # ⚠️ LE TITRE DISAIT « Trois situations REELLES » — c'etait FAUX, corrige
    #   le 14/08/2026. Des personnages inventes presentes comme des cas reels,
    #   sous le nom d'une association, c'est un faux temoignage. Le titre dit
    #   desormais « typiques », et la mention « Les prenoms sont fictifs »
    #   figure sous le titre. NE PAS REMETTRE « reelles » : ce serait
    #   retablir l'approximation, sur le point le plus sensible de la page.
    #
    # MAQUETTE 4 (`MAQ_RECAP`) — le recapitulatif mensuel utilise pour le
    #   pointage France Travail. Il illustre LITTERALEMENT le cas de Marco
    #   (« Le recapitulatif mensuel lui donne une ligne par GUSO »), d'ou sa
    #   place a la suite des trois cas, et non dans la section precedente.
    #   Dans l'app le recap s'affiche en CARTES groupees par mois : c'est
    #   cette version-la qui est reproduite, pas un tableau.
    A("""
<div class="divider"></div>
<section id="situations" class="band"><div class="wrap">
  <p class="kick">Cas d’usage</p>
  <h2 class="sec-title">Trois situations typiques</h2>
  <p class="cas-note">Les prénoms sont fictifs ; les situations, elles, sont celles que l’outil rencontre au quotidien.</p>

  <div class="cas">
    <article>
      <h3>Atteindre ses 507 heures sans angoisse</h3>
      <p>En mars, Léa était à 380 heures et se réveillait la nuit. La jauge lui a montré, non pas le
        chiffre manquant, mais ce qu’il représentait en dates concrètes ; et la projection lui a dit ce
        que ses dates encore incertaines changeraient si elles se confirmaient. Le compte à rebours est
        devenu un plan, mois par mois.</p>
    </article>
    <article>
      <h3>Pointer France Travail en cinq minutes</h3>
      <p>Chaque 28 du mois, Marco redoutait son actualisation : retrouver les feuillets, recompter les
        cachets, espérer ne pas se tromper. Le récapitulatif mensuel lui donne une ligne par GUSO, avec
        les heures et le brut déjà calculés. Il recopie, il valide, c’est terminé.</p>
    </article>
    <article>
      <h3>Accompagner quatre artistes sans tableur</h3>
      <p>Sophie gère quatre artistes au sein d’une structure. Elle voyait passer les DPAE dans ses mails
        et tenait un tableur qui n’était jamais à jour. Le back-office lui affiche désormais, sur un seul
        écran, toutes les déclarations, tous les feuillets et toutes les factures à faire, classés par
        échéance et tous artistes confondus.</p>
    </article>
  </div>
""")
    A(MAQ_RECAP)
    A("""</div></section>
""")

    # =====================================================================
    # 6. L'ETAT DU PROJET  (section 6 du contenu fourni — verbatim)
    # =====================================================================
    # ⚠️ NE PAS DURCIR CES FORMULATIONS. Le futur payant (« probablement
    # payant », « rien n'est chiffre a ce jour ») et l'affiliation (« un
    # systeme est prevu », « par exemple sous la forme de ») sont ecrits au
    # conditionnel EXPRES : rien n'est arrete, et une promesse commerciale
    # ferme sur le site d'une association serait un probleme.
    A("""
<div class="divider"></div>
<section id="etat"><div class="wrap">
  <p class="kick">L’état du projet</p>
  <h2 class="sec-title">Où en est le projet</h2>

  <div class="etat">
    <p class="first">Guso Facile est aujourd’hui en bêta privée, avec un nombre de places limité.</p>
    <p>Ce n’est pas un prototype. L’outil a été construit par un musicien intermittent pour son propre
      usage, et il a été éprouvé en interne pendant des mois sur des données réelles : celles de deux
      artistes professionnels, soit 65 dates de concerts, de répétitions et de sessions studio sur deux
      saisons complètes, avec les feuillets GUSO, les factures et le pointage France Travail
      correspondants. Il a donc déjà tourné en conditions réelles avant d’être ouvert à d’autres.</p>
    <p>L’accès se fait sur invitation ou sur cooptation, et chaque demande est étudiée personnellement.
      En contrepartie de cet accès, il est demandé aux bêta-testeurs de jouer le jeu des retours :
      signaler les bugs, proposer des améliorations, dire ce qui manque. C’est le seul engagement
      demandé.</p>
    <p>À terme, l’outil sera probablement payant — le développer et le maintenir demande du temps. Un
      système d’affiliation est prévu pour récompenser celles et ceux qui le font découvrir, par exemple
      sous la forme d’un tarif préférentiel sur leur propre abonnement. Rien n’est chiffré à ce jour, et
      les bêta-testeurs seront prévenus bien en amont.</p>
  </div>
</div></section>
""")

    # =====================================================================
    # 7. APPEL A L'ACTION  (section 7 du contenu fourni)
    # =====================================================================
    # UN SEUL bouton sur toute la page, ici. `target="_blank"` + `rel="noopener"`
    # (le lien sort du site : c'est un service distinct, pas une page du site).
    #
    # Les DEUX mentions sous le bouton sont indispensables :
    #  - la premiere dit comment se passe la demande (aucune inscription
    #    automatique) ;
    #  - la seconde nomme le RESPONSABLE DE TRAITEMENT des donnees. La page
    #    oriente en effet vers une collecte de nom, prenom, e-mail, telephone
    #    et nature du demandeur, hebergee ailleurs que sur le site de
    #    l'association. Elle renvoie a la mention portee par le formulaire
    #    lui-meme (usage limite a la creation du compte et au recontact, pas
    #    de demarchage, pas de revente, pas de partage a des tiers,
    #    suppression sur demande) sans la recopier.
    #
    # PAS DE MAQUETTE ICI, C'EST DELIBERE. Le sixieme emplacement prevu etait
    # « la modale Demander un acces », a poser a cote du bouton. Ecarte : c'est
    # le seul endroit de la page ou l'on CLIQUE vraiment, et y coller la
    # reproduction d'une fenetre avec ses champs — non focusables, donc morts
    # au clic — juste a cote du vrai bouton, c'est fabriquer une hesitation
    # a l'endroit exact ou il ne doit pas y en avoir. Cinq maquettes qui
    # montrent l'outil valent mieux qu'une sixieme qui brouille l'action.
    A("""
<div class="divider"></div>
<section id="acces" class="band"><div class="wrap">
  <div class="acces">
    <p class="kick">Appel à l’action</p>
    <h2 class="sec-title">Manifester son intérêt</h2>
    <p class="body">Puisque l’accès est limité, il n’y a pas d’inscription immédiate : on commence par
      se dire bonjour. Le formulaire « Demander un accès » recueille le nom, le prénom, l’adresse
      e-mail, le numéro de téléphone et la nature du demandeur — artiste ou structure. Chaque demande
      est ensuite lue et traitée personnellement, et une réponse est apportée par e-mail.</p>
    <div class="cta">
      <a class="btn" href="URL_ACCES" target="_blank" rel="noopener">Demander un accès</a>
    </div>
    <p class="mention">Le bouton « Demander un accès » se trouve en haut et en bas de la page de
      présentation. Aucune inscription automatique : chaque demande est étudiée personnellement.</p>
    <p class="mention">Le formulaire d’accès est hébergé par Guso Facile ; les informations transmises
      sont traitées par David Lesage, créateur de l’outil, uniquement pour l’étude de votre demande.
      Le formulaire porte sa propre mention d’information.</p>
  </div>
</div></section>
""".replace('URL_ACCES', URL_ACCES))

    # --- retour en haut + pied de page ------------------------------------
    # Pied de page identique aux 9 pages, a une correction pres : le lien
    # Facebook pointe sur /resonancesproductions (comme sur l'accueil) et non
    # sur https://www.facebook.com/ , qui traine encore sur plusieurs pages.
    A("""
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
""")
    A('</body></html>\n')

    return ''.join(B)


# =========================================================================
# GARDE-FOUS + ECRITURE
# =========================================================================
# Parti-pris maison (celui de `generate_rythme.py`) : on REFUSE D'ECRIRE
# plutot que d'imprimer un avertissement qui defile et que personne ne lit.
# Chaque ancre ci-dessous est unique PAR CONSTRUCTION : si le compte change,
# c'est qu'un bloc a ete duplique (le piege des 4 cartes identiques) ou qu'il
# a disparu. Les deux cas sont attrapes.

#: nombre de maquettes d'interface posees dans la page. Il sert TROIS fois :
#: autant de blocs, autant de mentions « données fictives », autant de
#: role="img". Si l'un des trois comptes s'ecarte, la page n'est pas ecrite.
NB_MAQUETTES = 6

#: (marqueur, nombre attendu, ce que c'est)
ANCRES = (
    ('<h1', 1, 'titre principal de la page'),
    # version lue dans nav_menu : ce garde-fou ne doit pas devenir faux le jour
    # ou NAV_VERSION est incrementee.
    ('data-nav="%s"' % nav_menu.NAV_VERSION, 1, 'menu partage nav_menu.py'),
    ('href="/guso-facile"', 1, 'entree « Guso Facile » du menu partage'),
    ('id="acces"', 1, 'section « Manifester son intérêt »'),
    (URL_ACCES, 1, 'bouton « Demander un accès » (un seul sur la page)'),
    ('id="etat"', 1, 'section « Où en est le projet »'),
    ('class="badge"', 1, 'badge « Bêta privée · places limitées »'),
    ('class="u-card"', 4, 'les 4 univers de fonctionnalités'),
    # Les intitules EXACTS des 4 univers, virgule comprise. Ils ont ete releves
    # dans le code de l'application le 14/08/2026 : la page portait jusque-la
    # des titres approchants (« Suivi des droits », « Organisation de tournee »,
    # « Espace structure », « Entraide entre artistes »). La virgule donne son
    # rythme a chaque intitule — ce n'est pas une coquille, ne pas la retirer.
    ('<h3>Tes droits, maîtrisés</h3>', 1, 'titre exact de l’univers 1'),
    ('<h3>Ta tournée, organisée</h3>', 1, 'titre exact de l’univers 2'),
    ('<h3>Ta structure, connectée</h3>', 1, 'titre exact de l’univers 3'),
    ('<h3>Ton cercle, solidaire</h3>', 1, 'titre exact de l’univers 4'),
    # Les trois blocs ajoutes le 14/08/2026 (voir les commentaires au-dessus de
    # chacun d'eux dans le gabarit).
    ('<b>Faire découvrir l’outil</b>', 1, 'cooptation — fonctionnalité LIVRÉE, au présent'),
    ('<b>L’entraide entre artistes</b>', 1, 'la Guilde — fonctionnalité À VENIR'),
    ('<b>Je crée mon contrat</b>', 1, 'modèle de contrat — fonctionnalité À VENIR'),
    # 4 mentions « a venir » : Guilde + « Je cree mon contrat » + les deux deja
    # presentes (points de vigilance, confidentialite graduee). Si ce compte
    # tombe a 3, c'est qu'une fonctionnalite non livree vient d'etre presentee
    # comme disponible : l'ecriture est refusee.
    ('<i>(à venir)</i>', 4, 'les mentions « à venir » des fonctionnalités non livrées'),
    # le hamburger est cree en JS par mobile_nav.py : c'est son CSS qui
    # atteste sa presence. `.burger span{` n'existe qu'une fois (`.burger{`
    # apparait 3 fois : regle de base + media 860 + media print).
    ('.burger span{', 1, 'CSS du hamburger (mobile_nav.py)'),
    ('id="contact"', 1, 'pied de page / ancre Contact'),
    # --- les 6 maquettes d'interface (14/08/2026) ------------------------
    # Trois comptes qui doivent rester egaux : un bloc = une mention visible
    # « données fictives » = un role="img". Si l'un decroche, soit un bloc a
    # ete duplique, soit une mention a saute — et une reproduction credible
    # sans mention est indistinguable d'une vraie capture d'ecran.
    ('<figure class="gf-block', NB_MAQUETTES, 'les maquettes d’interface'),
    ('<div class="gf-shot" role="img"', NB_MAQUETTES,
     'chaque maquette est une IMAGE pour les technologies d’assistance'),
    ('<figcaption class="gf-cap">' + MENTION_FICTIVE + '</figcaption>',
     NB_MAQUETTES, 'la mention visible « Aperçu de l’interface — données fictives »'),
    # Ce sont des illustrations, pas des interfaces : rien de focusable, rien
    # de saisissable NULLE PART sur la page hors du menu.
    # ⚠️ MESURE, pas supposition : la page contient bien 3 <button>, et
    #    seulement 3 — les trois ouvertures de sous-menu (« Sur scene »,
    #    « Le Nid », « L’association ») posees par nav_menu.py, plus le
    #    hamburger qui, lui, est cree en JavaScript et n'apparait donc pas
    #    sous forme de balise dans le fichier livre. Le compte est verifie
    #    HORS DU MENU par `_controle_maquettes()`, pour qu'un sous-menu de
    #    plus ou de moins ne fasse pas echouer l'ecriture pour rien.
    ('<input', 0, 'aucun champ de saisie dans la page'),
    ('tabindex', 0, 'aucun ordre de tabulation force'),
)

#: ce qu'aucune maquette ne doit contenir : elles ILLUSTRENT l'outil, elles ne
#: le rejouent pas. Un visiteur qui peut poser le focus dans une reproduction
#: croit manipuler le logiciel depuis le site de l'association.
_FOCUSABLES = (
    r'<a\b', r'<button\b', r'<input\b', r'<select\b', r'<textarea\b',
    r'<iframe\b', r'<details\b', r'<summary\b', r'<audio\b', r'<video\b',
    r'\btabindex\s*=', r'\bcontenteditable\b', r'\bonclick\b',
)


def _controle_maquettes(html):
    """Refuse d'ecrire si une maquette n'est pas une simple illustration.

    Trois exigences, bloc par bloc (le compte global, lui, est dans ANCRES) :
      - un `role="img"` ET un `aria-label` non vide : sans quoi un lecteur
        d'ecran enonce une bouillie de chiffres hors contexte ;
      - la mention visible « données fictives », exactement une fois ;
      - AUCUN element focusable a l'interieur.
    """
    import re

    # Aucun bouton hors du menu partage. Le corps de la page ne doit contenir
    # que du texte, des liens, et des illustrations inertes.
    corps = re.sub(r'<nav\b.*?</nav>', '', html, flags=re.S)
    if '<button' in corps:
        raise SystemExit('!! ABANDON : un <button> hors du menu de navigation. '
                         'Le corps de la page n\'a aucune commande a offrir : le '
                         'seul geste possible est le lien « Demander un accès ». '
                         'Page NON ecrite.')

    blocs = re.findall(r'<figure class="gf-block[^"]*">(.*?)</figure>', html, re.S)
    if len(blocs) != NB_MAQUETTES:
        raise SystemExit('!! ABANDON : %d bloc(s) <figure class="gf-block"> refermé(s) '
                         'correctement, attendu %d. Page NON ecrite.'
                         % (len(blocs), NB_MAQUETTES))

    for i, bloc in enumerate(blocs, 1):
        m = re.search(r'role="img" aria-label="([^"]{20,})"', bloc)
        if not m:
            raise SystemExit('!! ABANDON : maquette %d — role="img" ou aria-label '
                             'manquant (ou trop court pour decrire l\'ecran). '
                             'Page NON ecrite.' % i)
        if bloc.count(MENTION_FICTIVE) != 1:
            raise SystemExit(
                '!! ABANDON : maquette %d — la mention « %s » doit y figurer une '
                'fois et une seule. Sans elle, une reproduction credible de '
                'l\'interface est indistinguable d\'une vraie capture d\'ecran ; '
                'cette page a deja du corriger « situations reelles » pour ce '
                'motif exact. Page NON ecrite.' % (i, MENTION_FICTIVE))
        for motif in _FOCUSABLES:
            trouve = re.search(motif, bloc, re.I)
            if trouve:
                raise SystemExit(
                    '!! ABANDON : maquette %d — element focusable ou interactif '
                    '« %s ».\n   Les maquettes sont des ILLUSTRATIONS : un visiteur '
                    'ne doit pas pouvoir croire qu\'il pilote l\'outil depuis le '
                    'site de l\'association.\n   Page NON ecrite.'
                    % (i, trouve.group(0)))

#: seuls domaines externes autorises. Tout autre `https://` dans la page fait
#: echouer l'ecriture : zero traceur, zero script tiers, zero iframe.
#: fonts.googleapis.com / fonts.gstatic.com sont ceux des 9 pages existantes —
#: ce n'est pas une police SUPPLEMENTAIRE, c'est la meme feuille, deja chargee
#: partout sur le site.
HOTES_AUTORISES = (
    'fonts.googleapis.com',
    'fonts.gstatic.com',
    'www.helloasso.com',
    'guso-facile.vercel.app',
    'www.facebook.com',
    'docs.google.com',
    'www.resonancesproductions.org',
)


#: Le vocabulaire proscrit dans le bloc « L'entraide entre artistes ».
#: (motif, mot tel qu'il est interdit). Voir le long commentaire au-dessus du
#: bloc dans le gabarit : la fonctionnalite fait porter a des artistes des
#: affirmations factuelles sur des employeurs identifiables, sur une page
#: PUBLIQUE. Le bloc ne doit jamais se lire comme « une plateforme qui note les
#: employeurs du spectacle ».
#: ⚠️ L'interdit porte sur CE BLOC SEULEMENT : « signaler un bug » et
#: « Evaluation d'une proposition » sont legitimes ailleurs sur la page.
MOTS_INTERDITS_GUILDE = (
    (r'\bnot(?:e|es|er|ée?s?|ation|ations)\b', 'noter / notation'),
    (r'\bsignal\w*', 'signaler'),
    (r'\bdénonc\w*|\bdenonc\w*', 'dénoncer'),
    (r'\bavis\b', 'avis'),
    (r'\bévalu\w*|\bevalu\w*', 'évaluation'),
    (r'\bblacklist\w*', 'blacklist'),
    (r'\bréputation\w*|\breputation\w*', 'réputation'),
)

#: ce qui identifie le bloc Guilde dans la page livree.
_MARQUEUR_GUILDE = '<b>L’entraide entre artistes</b>'


def _controle_guilde(html):
    """Refuse d'ecrire si le bloc « Guilde » derape.

    Deux exigences, toutes deux liees au fait que la page est PUBLIQUE alors
    que la fonctionnalite, elle, sera reservee aux membres connectes :
      - la mention « (a venir) » y figure (la fonctionnalite n'est pas livree) ;
      - aucun mot du vocabulaire proscrit n'y apparait.
    """
    import re

    debut = html.find(_MARQUEUR_GUILDE)
    if debut < 0:
        raise SystemExit('!! ABANDON : bloc « Guilde » introuvable. Page NON ecrite.')
    ouvre = html.rfind('<li>', 0, debut)
    ferme = html.find('</li>', debut)
    if ouvre < 0 or ferme < 0:
        raise SystemExit('!! ABANDON : bloc « Guilde » mal delimite (pas de <li>…</li> '
                         'autour). Page NON ecrite.')
    bloc = html[ouvre:ferme + len('</li>')]

    if '(à venir)' not in bloc:
        raise SystemExit(
            '!! ABANDON : le bloc « Guilde » ne porte plus la mention « (à venir) ». '
            'La base existe mais l\'ecran n\'est PAS livre : l\'annoncer comme '
            'disponible serait verifiable en trois clics par un beta-testeur. '
            'Page NON ecrite.')

    for motif, mot in MOTS_INTERDITS_GUILDE:
        m = re.search(motif, bloc, re.I)
        if m:
            raise SystemExit(
                '!! ABANDON : mot interdit « %s » (ici : « %s ») dans le bloc '
                '« L\'entraide entre artistes ».\n'
                '   Ce bloc decrit des artistes qui affirment des faits sur des '
                'employeurs identifiables, sur une page PUBLIQUE. Il ne doit jamais '
                'se lire comme une plateforme de notation des employeurs.\n'
                '   Points d\'appui : membres connectes uniquement, faits binaires, '
                'aucun commentaire libre.\n'
                '   Page NON ecrite.' % (mot, m.group(0)))


def _controles(html):
    """Leve SystemExit au moindre ecart. Appele AVANT l'ecriture."""
    import re

    for marqueur, attendu, quoi in ANCRES:
        n = html.count(marqueur)
        if n != attendu:
            raise SystemExit(
                '!! ABANDON : %d occurrence(s) de « %s » (%s), attendu %d. '
                'Page NON ecrite.' % (n, marqueur, quoi, attendu))

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

    # aucune iframe, aucun script distant
    for interdit in ('<iframe', '<script src', 'googletagmanager', 'analytics'):
        if interdit in html:
            raise SystemExit('!! ABANDON : « %s » dans la page (zero tiers). '
                             'Page NON ecrite.' % interdit)

    # plancher typographique du site : jamais sous 13 px
    petits = [t for t in re.findall(r'font-size:\s*(\d+(?:\.\d+)?)px', html)
              if float(t) < 13]
    if petits:
        raise SystemExit('!! ABANDON : taille(s) de texte sous le plancher de 13 px : %s. '
                         'Page NON ecrite.' % ', '.join(petits))

    # aucune donnee personnelle glissee dans la page (depot PUBLIC)
    for motif, quoi in ((r'\b\d{13}\b', 'numero de securite sociale'),
                        (r'\bFR\d{2}[ ]?\d', 'IBAN')):
        if re.search(motif, html):
            raise SystemExit('!! ABANDON : ce qui ressemble a un %s dans la page. '
                             'Page NON ecrite.' % quoi)

    # le bloc le plus sensible de la page depuis le 14/08/2026
    _controle_guilde(html)
    # les 6 maquettes : illustrations, jamais interfaces
    _controle_maquettes(html)


def main():
    html = build_html()
    html = mobile_nav.inject(html)          # 1. le hamburger d'abord
    # 2. puis le menu partage. Depuis le 14/08/2026 « guso-facile » est une cle
    #    de nav_menu.PAGE_KEYS : l'entree du sous-menu « L’association » porte
    #    donc `aria-current="page"` sur cette page, et le parent est marque.
    html = nav_menu.inject(html, 'guso-facile')

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
