# -*- coding: utf-8 -*-
"""Genere la page /rendez-vous-mensuels (fichier rendez-vous-mensuels/index.html).

    python3 sources/generate_rdv_mensuels.py
    -> ecrit directement rendez-vous-mensuels/index.html (menu compris)

POURQUOI CETTE PAGE EXISTE
--------------------------
Demande de David (20/08/2026) : une page qui annonce TOUS les rendez-vous
mensuels du Nid, avec « une proposition d'activite differente a chaque fois ».
Le programme est en cours d'elaboration ; les DATES, elles, existent deja.

    « il faut que la premiere chose qu'on voit ce soit les dates, le titre de
      l'atelier, horaire, prix et un bouton cliquable "en savoir plus" qui en
      fait est une ancre qui fait descendre la personne au bon endroit de la
      page ou il y a la description detaillee »

⚠️ L'ORDRE A CHANGE LE 20/08/2026, APRES UNE PREMIERE MISE EN LIGNE.
   David a revu la page une fois publiee et a dicte une AUTRE structure, en deux
   temps. C'est la SECONDE dictee qui fait foi ; la premiere version est gardee
   ci-dessus comme historique, pour qu'on ne la reintroduise pas par megarde.

    « apres le premier paragraphe qui se termine sur "toujours sur reservation,
      toujours avec des intervenants differents", juste faire UN BOUTON qui
      permet de cliquer sur "voir les prochaines dates" — comme ca ca nous amene
      en bas sur le programme avec les prochaines dates. JUSTE UN BOUTON. Et
      ensuite mettre L'INTENTION : c'est quoi le projet, creer du lien, explorer
      ensemble — comme ca les gens peuvent vraiment lire et decouvrir ce qui est
      notre intention. Et en bas de l'intention, il y a LE PROGRAMME DETAILLE de
      chaque chose. »

Le raisonnement de David, qui explique tout le reste et qu'il faut respecter :
quelqu'un qui DECOUVRE doit pouvoir lire l'intention sans etre coupe par un
tableau de dates ; quelqu'un qui CONNAIT DEJA et vient chercher une date a un
bouton immediat pour sauter. Un seul chemin par intention, pas de compromis.

L'ordre des blocs est donc IMPOSE, et il ne doit pas etre « ameliore » :
  1. LE CHAPEAU d'ouverture, qui se termine par « Toujours sur reservation,
     toujours avec des intervenants differents. » ;
  2. UN BOUTON, ET RIEN D'AUTRE : « Voir les prochaines dates », ancre interne
     vers `#programme`, tout en bas de la page.
     ⚠️ « JUSTE UN BOUTON » — David insiste. Pas deux boutons, pas un bouton
        plus une liste, pas un apercu des dates a cote. UN bouton ;
  3. L'INTENTION developpee (`#intention`) : creer du lien, explorer ensemble,
     les axes, les trois formats, la selection des intervenants. C'est la partie
     qu'on vient lire ;
  4. LE PROGRAMME (`#programme`), tout en bas : les 4 dates, chacune cliquable
     vers son propre encart, puis UN ENCART PAR DATE dans l'ordre chronologique
     — celui d'INSTATIC est complet, les trois autres portent « Programme en
     cours d'elaboration ».

⚠️ LES IDENTIFIANTS `intention`, `programme` et `instatic`
   SONT ATTENDUS PAR `verif_site.py` (`MARQUEURS_UNIQUES`). Ce sont aussi des
   adresses deja partagees. Les blocs se DEPLACENT, ils ne se renomment pas.

LE SLUG : POURQUOI `/rendez-vous-mensuels`
------------------------------------------
`RDV` est l'abreviation que David emploie a l'oral et dans le titre affiche ;
l'adresse, elle, doit rester lisible par quelqu'un qui ne connait pas le site
et par un moteur de recherche. Or le site ecrit DEJA « Rendez-vous mensuel » en
toutes lettres partout ou il en parle : le badge de l'agenda de `/le-nid`
(`TYPES['mensuel']`), la tuile de la grille des activites, les 4 evenements du
Google Agenda public. Prendre `/rdv-mensuels` aurait introduit un troisieme
vocabulaire pour une meme chose. Longueur comparable aux slugs deja publies
(`/concerts-david-lesage`, `/david-lesage-en-concert`).
⚠️ UNE ADRESSE NE SE CHANGE PAS : elle part dans les partages, les messages et
   l'index de Google. Celle-ci est choisie pour ne plus bouger.

LES QUATRE DATES — RELEVEES, PAS SUPPOSEES
------------------------------------------
Source unique : `EVENTS` dans `sources/generate_agenda_nid.py`, lignes de type
`mensuel`. Les jours de la semaine ont ete CALCULES (datetime), pas devines :

    2026-09-04  vendredi     2026-11-07  samedi
    2026-10-02  vendredi     2026-12-04  vendredi

⚠️ Ce sont les seuls rendez-vous mensuels declares jusqu'a decembre 2026.
⚠️ CETTE PAGE NE LIT PAS `generate_agenda_nid.py` (pas d'import) : ce module
   travaille au moment de l'import et reecrit `/le-nid`. Les dates sont donc
   recopiees ci-dessous, et `_controle_dates()` en bas de fichier RELIT le
   fichier source en texte pour verifier qu'elles n'ont pas divergE. Le jour ou
   David ajoutera une date a l'agenda sans la reporter ici, la generation
   s'arrete au lieu de publier une page en retard.

TROIS CONTRADICTIONS CONNUES — REMONTEES A DAVID, PAS TRANCHEES ICI
-------------------------------------------------------------------
1. HORAIRES. L'agenda annonce 18:30-23:30 pour les quatre dates ; le texte
   d'annonce d'INSTATIC ecrit par David dit 19h00-21h30, accueil a 18h45,
   portes fermees a 19h00. La page affiche l'horaire DU TEXTE DE DAVID pour
   INSTATIC (plus precis et plus recent), et AUCUN HORAIRE pour les trois
   autres dates — annoncer un horaire qui bougera est pire que ne rien dire.
2. ADHESION vs BILLETTERIE. L'agenda de `/le-nid` dit les rendez-vous mensuels
   « Reserves aux adherents de l'association » et son seul bouton est
   « Adherer ». INSTATIC, lui, est a 20 EUR avec une billetterie HelloAsso
   publique. Les deux ne peuvent pas etre vrais en meme temps. Cette page
   n'invente pas la regle : elle publie ce que David a ecrit pour INSTATIC
   (20 EUR, jauge 20, reservation HelloAsso) et ne dit RIEN sur l'adhesion.
   (C'est deja la question 11 de « EN ATTENTE DE DAVID » dans le handoff.)
3. LIEN HELLOASSO. Il repond 403 aux tests automatises — c'est le comportement
   habituel de HelloAsso face aux robots, pas une preuve qu'il est casse. Il
   est publie tel que David l'a donne.

CE QUI A ETE RETIRE DE LA PAGE LE 20/08/2026, SUR DEMANDE DE DAVID
-----------------------------------------------------------------
1. LA SECTION « CE QUI SE PREPARE » (`#a-venir`) et ses quatre formats sans
   date — Workshop Sexto, Concert intimiste, La roue du consentement, Scene
   ouverte du vendredi soir. Ils n'avaient ni date, ni prix, ni horaire, ni
   intervenant : la page annoncait donc quatre choses dont on ne pouvait rien
   dire, juste avant trois soirees dont on ne pouvait rien dire non plus.
   ⚠️ SI CE BLOC REVIENT UN JOUR, la precision exacte de David sur « la roue du
      consentement » revient avec lui : « mieux se connaitre dans nos desirs et
      nos limites, pas de sexualite ». Elle cadre l'atelier et evite un
      malentendu — elle ne se resume pas et elle ne se coupe pas.
2. LES DEUX PHOTOS de soirees au Nid et leurs legendes, ainsi que la visionneuse
   plein ecran qui n'existait que pour elles.
   ⚠️ AUCUN FICHIER N'A ETE EFFACE DANS `img/` : ces photos servent toujours sur
      `/le-nid`. Seul leur affichage ici a disparu. `og:image` n'est PAS
      concernee : c'est la vignette de partage, elle n'est pas dans la page.

LE TEXTE D'INSTATIC
-------------------
David a fourni DEUX versions : une annonce longue (un e-mail) et un post pour
les reseaux sociaux. La page reprend L'ANNONCE. Le post — hashtags, @mentions
Instagram, rafales d'emoji — n'a pas sa place sur le site (regle du site :
aucun emoji). Ce qui a ete retire de l'annonce : les salutations
(« Bonjour a toutes et a tous »), la formule de fin (« Hate de danser
ensemble ! ») et la signature — ce sont des marques d'e-mail, pas de page web.
Le corps du texte n'a pas ete reformule.
⚠️ SEUL AJUSTEMENT D'ORTHOGRAPHE : « neotone » -> « Neotone », le nom propre de
   l'instrument tel qu'il est ecrit sur les 30 autres pages du site. Signale a
   David dans le rapport de session.
⚠️ « Fermeture stricte des portes a 19h00 » et « 25 places seulement » sont des
   informations CRITIQUES : quelqu'un qui arrive a 19h05 n'entre pas. Elles
   apparaissent DEUX fois — dans la ligne du programme et en tete de l'encart —
   et jamais noyees dans un paragraphe.
⚠️ LA JAUGE EST PASSEE DE 20 A 25 le 20/08/2026 (David). Elle vit desormais
   dans la constante `JAUGE`, une seule fois. Le TARIF, lui, reste 20 EUR.

CE QUE LA PAGE PARTAGE AVEC LE RESTE DU SITE
--------------------------------------------
Menu (`nav_menu.py`) · hamburger (`mobile_nav.py`) · couche chaleureuse
(`theme_chaleur.py`) · bouton retour en haut (`retour_haut.py`) · garde-fou
commentaires HTML (`verif_commentaires.py`).
⚠️ PLUS DE `visionneuse.py` DEPUIS LE 20/08/2026 : elle n'agrandissait que les
   deux photos, qui ont ete retirees. La reimporter sans photo ajouterait une
   feuille de style et un script que rien n'ouvre.

CETTE PAGE N'AFFICHE AUCUNE IMAGE. Elle en declare une seule, `og:image`, qui
est la vignette des partages (Facebook, Messenger, WhatsApp) et n'apparait
jamais dans la page elle-meme.
"""
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mobile_nav  # noqa: E402
import nav_menu  # noqa: E402
import retour_haut  # bouton « retour en haut »  # noqa: E402
import theme_chaleur  # couche chaleureuse commune  # noqa: E402
import verif_commentaires  # garde-fou commentaires HTML  # noqa: E402

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = 'rendez-vous-mensuels'
SITE = 'https://www.resonancesproductions.org'

# --------------------------------------------------------------------------- #
# LA FEUILLE DE STYLE
# --------------------------------------------------------------------------- #
# Le squelette (`.nav`, `.wrap`, `.kick`, `.sec-title`, `.btn`, `.divider`,
# `footer`) est celui de `generate_soin_soa.py`, a l'identique : c'est la base
# commune des pages « une seule colonne » du site, et c'est ce qui rend la
# nouvelle page indiscernable des autres.
# ⚠️ LE BLOC `.totop` DE CETTE BASE A ETE RETIRE. Il y etait recopie a la main ;
#    ici il vient de `retour_haut.css()`, pose plus bas. Deux copies de la meme
#    regle, c'est la divergence garantie (voir l'en-tete de retour_haut.py).
CSS = ("""
:root{--night:#0e0f24;--night2:#141633;--ink:#eae7f3;--muted:#a9a6c4;--gold:#d8b25a;--gold2:#f0d18a;--plum:#8f7ad1;--card:#191b3d;--line:rgba(216,178,90,.26)}
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
.nav .links a{font-size:14.5px}
.nav .links a.adh{font-size:15px}
p a:not(.btn):not(.adh){text-decoration:underline;text-decoration-color:rgba(216,178,90,.4);text-underline-offset:3px}
""")

# --------------------------------------------------------------------------- #
# LES DECLINAISONS PROPRES A CETTE PAGE
# --------------------------------------------------------------------------- #
# ⚠️ CE BLOC DOIT RESTER APRES `theme_chaleur.CSS` : memes specificites, c'est
#    la derniere regle qui gagne (meme piege que `css_tuiles()` sur /le-nid).
CSS_PAGE = ("""/* ===== Les RDV Mensuels : declinaisons ===== */
section{padding:92px 0}
.rdv-top{padding:128px 0 62px;background:radial-gradient(900px 560px at 10% -8%,rgba(147,116,226,.20),transparent 62%),radial-gradient(700px 460px at 92% 102%,rgba(216,178,90,.12),transparent 62%),linear-gradient(180deg,#0b0c1e,var(--night))}
.rdv-top h1{font-size:clamp(38px,7vw,72px);font-weight:600;line-height:1.02;letter-spacing:.02em;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent;width:fit-content;max-width:100%}
.tagline{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(19px,2.8vw,28px);margin-top:12px}
.band{background:linear-gradient(180deg,#0b0c1e,var(--night))}
"""
            # ⚠️⚠️ `scroll-margin-top` — SANS CETTE LIGNE LES BOUTONS « EN SAVOIR
            # PLUS » ATTERRISSENT SOUS LE MENU. Le menu du site est en
            # `position:fixed` : un lien d'ancre pose le HAUT de la section a
            # y=0, donc derriere la barre. Les valeurs sont celles MESUREES sur
            # /guso-facile (hauteur reellement peinte par `.nav` : 110 px a
            # 390, 77 px a 820, 75 px a 1440) et le point de bascule est celui
            # du menu (760/761 px), pas celui de la mise en page.
            # ⚠️ Aucun effet visuel au chargement : `scroll-margin` ne joue QUE
            #    sur les deplacements vers une ancre.
            """section[id]{scroll-margin-top:56px}
@media(max-width:760px){section[id]{scroll-margin-top:100px}}
"""
            # --- le programme en un coup d'oeil ---------------------------------
            # Une LISTE ORDONNEE : ces quatre dates ont un ordre (chronologique),
            # et c'est une information, pas une decoration. Les puces sont
            # retirees, le compteur ne sert a rien a l'ecran.
            """.rdv-list{list-style:none;margin-top:34px;display:grid;gap:16px}
.rdv-row{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:18px;transition:transform .2s,border-color .2s}
"""
            # ⚠️ TOUTE LA LIGNE EST UN LIEN, et c'est le coeur de la demande de
            # David (« chaque date cliquable »). La grille est donc portee par
            # le `<a>` (`.rdv-go`), pas par le `<li>` : le lien couvre la carte
            # entiere — cible tactile de 100 a 130 px de haut, tres au-dessus du
            # plancher de 44 px — et il n'y a QU'UN SEUL arret de tabulation par
            # date au lieu de deux.
            # ⚠️ Les trois colonnes sont des `<div>` et non des `<span>` : elles
            #    contiennent un `<h3>` et des `<p>`. Un `<a>` a le droit de
            #    contenir du contenu de flux (il est « transparent »), un
            #    `<span>` non — la page serait invalide.
            """.rdv-go{display:grid;grid-template-columns:minmax(0,200px) minmax(0,1fr) minmax(0,190px);gap:20px 26px;align-items:center;padding:22px 24px;border-radius:18px;color:inherit}
.rdv-row:hover{transform:translateY(-2px);border-color:rgba(240,209,138,.5)}
.rdv-row:hover .btn.ghost{color:#fff;border-color:var(--gold2)}
"""
            # Filet degrade de 3 px sur le cote gauche, en `--grad-v` (vertical) :
            # dans un filet haut de 120 px et large de 3, le degrade a 95deg de
            # `--grad` tomberait de biais. Meme technique que `.q` sur /rituals —
            # on PEINT la bordure au lieu d'ajouter un pseudo-element, pour ne
            # pas avoir besoin d'un `overflow:hidden` qui rognerait les coins.
            """.rdv-row{border-left:3px solid transparent;background-image:var(--grad-v),linear-gradient(var(--card),var(--card));background-size:3px 100%,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box}
"""
            # La date : c'est elle que David veut voir en premier.
            """.rdv-when{display:flex;flex-direction:column;gap:3px}
.rdv-day{font-family:'Cormorant Garamond',Georgia,serif;font-size:23px;line-height:1.2;color:#fff;font-weight:600}
.rdv-hours{color:var(--gold2);font-size:15px;letter-spacing:.04em}
.rdv-what h3{font-family:'Cormorant Garamond',Georgia,serif;font-size:25px;line-height:1.2;color:var(--gold2);font-weight:600}
.rdv-type{display:inline-block;font-size:13px;letter-spacing:.18em;text-transform:uppercase;font-weight:600;color:var(--plum2);margin-bottom:4px}
.rdv-sub{color:#d7d4ea;font-size:15.5px;margin-top:7px}
.rdv-soon{color:var(--muted);font-size:16px;font-style:italic;line-height:1.55}
.rdv-act{display:flex;flex-direction:column;align-items:flex-start;gap:11px}
.rdv-price{font-family:'Cormorant Garamond',Georgia,serif;font-size:27px;color:#fff;font-weight:600;line-height:1}
.rdv-act .btn{padding:12px 22px;font-size:14.5px}
"""
            # Le lien « etre prevenu » : il vit maintenant DANS l'encart des
            # trois soirees sans programme (avant le 20/08 il etait dans la
            # ligne du programme, qui est devenue un lien entier et ne peut donc
            # plus contenir un second lien). Lien texte et pas bouton dore : il
            # ne doit pas peser autant que le bouton de reservation d'une soiree
            # reellement ouverte. Cible tactile : 44 px de haut, plancher du site.
            """.rdv-tell{display:inline-flex;align-items:center;min-height:44px;color:var(--gold2);font-size:15px;text-decoration:underline;text-decoration-color:rgba(248,210,116,.42);text-underline-offset:4px}
.rdv-tell:hover{text-decoration-color:var(--gold2)}
"""
            # Sous 860 px la ligne passe en deux colonnes (date + titre), puis en
            # une seule sous 620. Aucune valeur fixe : `minmax(0,…)` partout,
            # sinon une longue date force la grille a deborder.
            """@media(max-width:860px){.rdv-go{grid-template-columns:minmax(0,1fr);gap:14px;padding:20px}
  .rdv-act{flex-direction:row;align-items:center;gap:18px;flex-wrap:wrap}}
"""
            # --- l'intention ---------------------------------------------------
            """.rdv-quote{margin:34px 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(21px,3vw,28px);line-height:1.35;padding-left:22px;max-width:760px;border-left:3px solid transparent;background-image:var(--grad-v);background-size:3px 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box}
.rdv-cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px;margin-top:30px}
.rdv-card{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:18px;padding:22px 24px;border-top:3px solid transparent;background-image:var(--grad),linear-gradient(var(--card),var(--card));background-size:100% 3px,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box}
.rdv-card h3{font-family:'Cormorant Garamond',Georgia,serif;font-size:23px;color:#fff;font-weight:600;line-height:1.15}
.rdv-card p{color:var(--muted);font-size:15.5px;margin-top:8px}
.rdv-note{background:var(--card);border:1px solid rgba(255,255,255,.07);border-radius:18px;padding:20px 24px;margin-top:26px;max-width:820px;border-left:3px solid transparent;background-image:var(--grad-v),linear-gradient(var(--card),var(--card));background-size:3px 100%,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box}
.rdv-note h3{font-family:'Cormorant Garamond',Georgia,serif;font-size:23px;color:#fff;font-weight:600;line-height:1.2}
.rdv-note p{color:#d7d4ea;font-size:15.5px;margin-top:10px;line-height:1.7}
"""
            # les puces : des losanges au degrade chaud, comme sur /le-soin-soa
            """.rdv-ul{list-style:none;margin-top:20px;max-width:820px}
.rdv-ul li{color:#d7d4ea;font-size:16px;padding:9px 0 9px 26px;position:relative;border-bottom:1px solid rgba(255,255,255,.05)}
.rdv-ul li:last-child{border-bottom:0}
.rdv-ul li::before{content:"";position:absolute;left:4px;top:17px;width:7px;height:7px;background:var(--grad-warm);transform:rotate(45deg)}
"""
            # --- l'encart detaille d'un evenement -------------------------------
            # La fiche pratique (date, accueil, lieu, tarif, jauge) est en tete de
            # l'encart, AVANT le texte : c'est ce qu'on vient chercher quand on
            # arrive par le bouton « En savoir plus ».
            """.rdv-facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:2px 26px;margin-top:26px;background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:18px;padding:20px 24px;border-top:3px solid transparent;background-image:var(--grad),linear-gradient(var(--card),var(--card));background-size:100% 3px,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box}
.rdv-facts div{padding:10px 0}
.rdv-facts dt{color:var(--gold);font-size:13px;letter-spacing:.18em;text-transform:uppercase;font-weight:600}
.rdv-facts dd{color:#fff;font-size:16.5px;margin-top:3px;line-height:1.45}
.rdv-facts dd small{display:block;color:var(--muted);font-size:14px;font-style:italic;margin-top:2px}
"""
            # ⚠️ 13 px et pas 12 sur `.rdv-type` et `.rdv-facts dt` : c'est le
            # PLANCHER TYPOGRAPHIQUE du site (hors `<sup>`), pose une fois pour
            # toutes. Mesure faite dans le DOM : les deux etaient a 12 px a la
            # premiere ecriture, corriges avant publication.
            # L'avertissement horaire : il doit se voir, pas se deviner. Fond
            # corail translucide (le corail de la palette, pas un rouge d'alerte
            # importe d'ailleurs) et texte en --gold2 pour rester au-dessus du
            # seuil de contraste sur ce fond.
            """.rdv-warn{margin-top:20px;max-width:820px;background:rgba(238,128,98,.11);border:1px solid rgba(238,128,98,.34);border-radius:16px;padding:16px 20px;color:#f3ded6;font-size:16px;line-height:1.6}
.rdv-warn b{color:var(--gold2)}
.rdv-block h2{margin-top:4px}
.rdv-block p{max-width:820px;color:#d7d4ea;margin-top:16px}
"""
            # `.rdv-cta` remplace le `style="margin-top:28px"` qui etait recopie
            # a la main sur chaque bloc de boutons. Meme valeur, une seule
            # source.
            # `.rdv-attente` : les trois encarts « programme en cours
            # d'elaboration » tiennent en cinq lignes. Leur donner les 92 px de
            # `section` en haut ET en bas ferait trois ecrans presque vides a la
            # suite sur telephone.
            """.rdv-cta{margin-top:28px}
.rdv-attente{padding:62px 0}
"""
            # L'encart d'abonnement des soirees non programmees. Il reprend le
            # cadre dore de `.ag-sub` sur /le-nid — meme geste, meme allure —
            # sans importer sa feuille de style : /le-nid met l'encart sur deux
            # colonnes parce qu'il y a quatre arguments a lire, ici il y en a
            # un seul et la pleine largeur serait du vide.
            """.rdv-abo{margin-top:26px;max-width:820px;background:linear-gradient(135deg,rgba(216,178,90,.10),rgba(255,255,255,.03));border:1px solid rgba(216,178,90,.34);border-radius:16px;padding:22px 24px}
.rdv-abo h3{font-family:'Cormorant Garamond',Georgia,serif;font-size:23px;color:#fff;font-weight:600;line-height:1.2}
.rdv-abo p{color:#d7d4ea;font-size:15.5px;margin-top:8px;line-height:1.65}
.rdv-abo-act{display:flex;flex-wrap:wrap;align-items:center;gap:10px 20px;margin-top:16px}
"""
            # Le bouton unique du chapeau (« Voir les prochaines dates ») : il
            # est SEUL, donc il porte tout le poids du raccourci. Marge un peu
            # plus large que `.rdv-cta` pour le detacher du paragraphe.
            """.rdv-saut{margin-top:34px}
""")

CSS = CSS + theme_chaleur.CSS + CSS_PAGE + retour_haut.css()

# --------------------------------------------------------------------------- #
# LIENS ET ADRESSES
# --------------------------------------------------------------------------- #
HELLO = 'https://www.helloasso.com/associations/resonances-productions'
# ⚠️ Adresse fournie par David. Elle repond 403 aux tests automatises : c'est le
#    comportement habituel de HelloAsso face aux robots, pas une preuve qu'elle
#    est cassee. Elle est publiee telle quelle.
INSTATIC_RESA = ('https://www.helloasso.com/associations/resonances-productions'
                 '/evenements/instatic-dance')
STATUTS = ('https://docs.google.com/document/d/'
           '1NxsbvaqHsA9VOXlN7cvsav7cxFwhsK4XCpowHb75o1w/edit?usp=sharing')


def _source_agenda():
    """Le TEXTE de `generate_agenda_nid.py`. Jamais son import.

    ⚠️ CE MODULE TRAVAILLE AU MOMENT DE L'IMPORT : l'importer reecrirait
    `/le-nid`. On le lit donc comme un fichier, comme le fait `_controle_dates`.
    """
    chemin = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          'generate_agenda_nid.py')
    with open(chemin, encoding='utf-8') as f:
        return f.read()


def _calendrier():
    """Les deux adresses d'abonnement a l'agenda public du Nid.

    ⚠️ ELLES SONT LUES CHEZ LEUR AUTEUR, PAS RECOPIEES. L'identifiant du
    calendrier fait 79 caracteres ; une lettre de travers ne se verrait pas a
    l'oeil, et le bouton menerait a un calendrier vide. Si `generate_agenda_nid`
    change de calendrier, cette page suit toute seule — et si les constantes
    disparaissent, la generation s'arrete au lieu de publier un lien mort.
    """
    src = _source_agenda()
    ident = re.search(r"^CAL_ID = '([^']+)'", src, re.M)
    sub = re.search(r"^CAL_SUB = \((.*?)\)\n", src, re.M | re.S)
    ics = re.search(r"^CAL_WEBCAL = \((.*?)\)\n", src, re.M | re.S)
    if not (ident and sub and ics):
        raise SystemExit('!! ABANDON : CAL_ID / CAL_SUB / CAL_WEBCAL sont '
                         'introuvables dans generate_agenda_nid.py — le bouton '
                         'd’abonnement n’a plus d’adresse. Page NON ecrite.')
    lien_google = ''.join(re.findall(r"'([^']*)'", sub.group(1)))
    # `CAL_WEBCAL` est une expression : prefixe + l'identifiant encode + suffixe.
    # On reprend le prefixe et le suffixe tels qu'ils sont ecrits la-bas.
    morceaux = [m for m in re.findall(r"'([^']*)'", ics.group(1)) if m]
    lien_ics = morceaux[0] + urllib.parse.quote(ident.group(1), safe='') + morceaux[-1]
    if 'calendar.google.com' not in lien_google or not lien_ics.startswith('webcal://'):
        raise SystemExit('!! ABANDON : les adresses d’abonnement relues ne '
                         'ressemblent pas a un calendrier (%s / %s). Page NON '
                         'ecrite.' % (lien_google[:40], lien_ics[:40]))
    return lien_google, lien_ics


CAL_SUB, CAL_WEBCAL = _calendrier()


# --------------------------------------------------------------------------- #
# LES QUATRE SOIREES — LA SEULE SOURCE DE LA PAGE
# --------------------------------------------------------------------------- #
#
#   ┌──────────────────────────────────────────────────────────────────────┐
#   │ COMPLETER UNE SOIREE, PLUS TARD — LA MARCHE A SUIVRE EN TROIS LIGNES │
#   └──────────────────────────────────────────────────────────────────────┘
#   1. Dans `SOIREES` ci-dessous, trouve la soiree a sa date et remplis ses
#      champs : `titre`, `type`, `horaire`, `prix`, `sous`, puis `faits`,
#      `alerte`, `recit`, `au_programme`, `fin`, `resa` et `resa_texte`.
#   2. Ne touche a RIEN d'autre : des qu'une soiree a un `titre`, sa ligne du
#      programme et son encart passent tout seuls en version complete.
#   3. Lance `python3 sources/build.py` puis `python3 sources/verif_site.py`.
#
#   ⚠️ Un champ qu'on ne connait pas, ON LE LAISSE ABSENT. La page ecrit alors
#      « Horaire a preciser », « Programme en cours d'elaboration » — jamais un
#      titre approchant, jamais un horaire repris de l'agenda (voir la
#      contradiction 1 en tete de fichier), jamais un tarif « vraisemblable ».
#
# LES CHAMPS, UN PAR UN
#   iso ........... la date en 2026-09-04. Sert au controle contre l'agenda.
#   jour .......... la date en clair. Le jour de la semaine a ete CALCULE.
#   ancre ......... l'identifiant de l'encart. UNE ANCRE NE SE CHANGE PLUS une
#                   fois la page en ligne : elle part dans les partages.
#   --- a partir d'ici, tout est optionnel : c'est ce qui reste a remplir ---
#   type .......... le sur-titre en petites capitales (« Danse »).
#   titre ......... LE CHAMP PIVOT : sa presence bascule la soiree en « complete ».
#   sous .......... la ligne de resume, sous le titre, dans le programme.
#   horaire ....... affiche a cote de la date dans le programme.
#   prix .......... affiche dans le programme. Le tarif detaille va dans `faits`.
#   chapeau ....... le chapeau de l'encart, juste sous le grand titre.
#   faits ......... la fiche pratique : (intitule, valeur, precision en petit).
#   alerte ........ l'encadre corail. Reserve a ce qui fait qu'on entre ou non.
#   recit ......... les paragraphes de description, dans l'ordre.
#   au_programme .. la liste a puces « Au programme ».
#   fin ........... le dernier paragraphe, celui qui invite.
#   resa .......... l'adresse de la billetterie. `resa_texte` = le libelle.
#: 🚨 LA JAUGE D'INSTATIC. Elle est passee de 20 a 25 personnes le 20/08/2026
#: (David, apres la premiere mise en ligne). Elle est ecrite ICI et NULLE PART
#: ailleurs : elle paraissait a trois endroits du texte, et un chiffre recopie
#: trois fois est un chiffre corrige deux fois sur trois.
#: ⚠️ NE PAS CONFONDRE avec le TARIF, qui vaut 20 EUR et n'a PAS change. Les
#:    deux valaient 20 avant le 20/08 — c'est exactement le piege.
JAUGE = 25

SOIREES = [
    dict(
        iso='2026-09-04',
        jour='Vendredi 4 septembre 2026',
        ancre='instatic',
        type='Danse',
        titre='INSTATIC Dance',
        horaire='19h00 – 21h30',
        prix='20 €',
        sous=('Co-créée et facilitée par Iris &amp; David. '
              'Portes fermées à 19h00 · %d places seulement.' % JAUGE),
        chapeau='Co-créée et facilitée par Iris &amp; David.',
        # Reprise mot pour mot de l'annonce de David. L'accueil et la jauge sont
        # dans cette fiche ET rappeles dans l'encadre juste en dessous : ce sont
        # les deux informations qui font qu'on entre ou qu'on n'entre pas.
        faits=[
            ('Quand', 'Vendredi 4 septembre 2026, de 19h00 à 21h30', ''),
            ('Accueil', 'Portes ouvertes dès 18h45',
             'Fermeture stricte des portes à 19h00'),
            ('Où', 'Le Nid — Paris 20<sup>e</sup>', '29 rue des Orteaux'),
            ('Tarif', '20 €', 'Réservation en ligne'),
            ('Jauge', '%d personnes seulement' % JAUGE, 'Très limitée'),
        ],
        alerte=('<b>Les portes ferment à 19h00, sans exception</b>, et la '
                'jauge est de <b>%d personnes</b>. Arriver à 18h45 fait partie '
                'de la soirée : une fois la traversée commencée, on n’ouvre '
                'plus.' % JAUGE),
        recit=[
            'En cette rentrée, nous avons la joie de vous ouvrir les portes du '
            'Nid, notre cocon dans le 20<sup>e</sup> arrondissement, pour une '
            'toute nouvelle expérience : une <b>INSTATIC Dance</b>, co-créée et '
            'facilitée par Iris &amp; David.',
            'Cette soirée est une invitation à réhabiter pleinement son corps à '
            'travers un véritable <b>voyage musical en vagues</b>.',
            'L’INSTATIC Dance, ce n’est pas une simple méditation passive : '
            'c’est une traversée complète. Attendez-vous à une exploration '
            'dynamique, où des phases d’envolées très rythmées, puissantes et '
            'vibrantes alternent avec des temps d’ancrage, de douceur et '
            'd’intériorité. Loin de la sur-stimulation du clubbing ou de la '
            'recherche de catharsis à tout prix, <b>nous dansons pour restaurer '
            'notre énergie et nourrir notre présence</b>.',
            'Une immersion conçue à quatre mains : Iris aux platines pour '
            'tisser les vagues musicales et la guidance corporelle, rejointe '
            'par David pour faire vibrer l’espace en direct avec sa voix '
            'chantée, son handpan électronique et sa harpe.',
        ],
        au_programme=[
            'DJ set en vagues (du rythme soutenu à la douceur) &amp; guidance '
            'corporelle par Iris.',
            'Créations sonores &amp; instruments live (voix, Neotone, n’goni) '
            'par David.',
            'Danse libre, expressive et consciente, dans le respect des '
            'guidelines traditionnelles.',
            'Un cadre intimiste et sécurisant pour danser pleinement.',
        ],
        fin='Venez comme vous êtes, pour faire circuler l’énergie, traverser le '
            'mouvement et recharger votre flamme intérieure.',
        resa=INSTATIC_RESA,
        resa_texte='Réserver ma place — 20 € ↗',
    ),
    dict(iso='2026-10-02', jour='Vendredi 2 octobre 2026',
         ancre='soiree-2026-10-02'),
    dict(iso='2026-11-07', jour='Samedi 7 novembre 2026',
         ancre='soiree-2026-11-07'),
    dict(iso='2026-12-04', jour='Vendredi 4 décembre 2026',
         ancre='soiree-2026-12-04'),
]

#: les mots de David pour une soiree dont le programme n'est pas arrete. Ils
#: apparaissent dans la ligne du programme ET dans l'encart : c'est la meme
#: information, et elle doit se lire aux deux endroits sans avoir a chercher.
#: ⚠️ 20/08/2026 — ILS REMPLACENT une phrase plus longue (« La proposition de
#:    cette soiree sera annoncee ici. Le programme, l'horaire et le tarif ne
#:    sont pas encore arretes. »). David l'a raccourcie a ces quatre mots :
#:    « court, net ». NE PAS LA RALLONGER, ne pas la faire suivre d'une
#:    explication — c'est precisement ce qu'il a retire.
EN_COURS = 'Programme en cours d’élaboration'

#: 🚨 L'HORAIRE DES TROIS SOIREES NON PROGRAMMEES N'EST PAS TRANCHE.
#: L'agenda du Nid annonce 18:30-23:30 pour les rendez-vous mensuels ; INSTATIC,
#: qui EST un rendez-vous mensuel, est de 19h00 a 21h30. Les deux ne peuvent pas
#: etre vrais. On n'en recopie donc AUCUN et on l'ecrit : « A préciser ».
#: Le jour ou David tranche, cette valeur est remplacee par l'horaire reel dans
#: le champ `horaire` de la soiree concernee, et cette constante disparait.
HORAIRE_INCONNU = 'À préciser'


def ligne(d):
    """Une ligne du programme en un coup d'oeil — la ligne ENTIERE est un lien.

    ⚠️ Aucun `<a>` ne peut apparaitre a l'interieur : un lien dans un lien est
    invalide et le second devient inatteignable au clavier. Ce qui ressemble a
    un bouton (« En savoir plus ») est donc un `<span class="btn ghost">` : il
    n'a pas besoin d'etre focalisable puisque toute la carte l'est deja.
    """
    if d.get('titre'):
        quoi = ('<span class="rdv-type">%s</span><h3>%s</h3>'
                '<p class="rdv-sub">%s</p>'
                % (d['type'], d['titre'], d.get('sous', '')))
        acte = ('<span class="rdv-price">%s</span>'
                '<span class="btn ghost">En savoir plus</span>' % d['prix'])
        heures = '<span class="rdv-hours">%s</span>' % d['horaire']
    else:
        quoi = '<p class="rdv-soon">%s</p>' % EN_COURS
        acte = '<span class="btn ghost">Voir cette date</span>'
        heures = '<span class="rdv-hours">%s</span>' % HORAIRE_INCONNU
    return ('<li class="rdv-row"><a class="rdv-go" href="#%s">'
            '<div class="rdv-when"><span class="rdv-day">%s</span>%s</div>'
            '<div class="rdv-what">%s</div>'
            '<div class="rdv-act">%s</div>'
            '</a></li>' % (d['ancre'], d['jour'], heures, quoi, acte))


def programme():
    return '<ol class="rdv-list">' + ''.join(ligne(d) for d in SOIREES) + '</ol>'


# --------------------------------------------------------------------------- #
# L'INTENTION — les mots de David, mis en forme, jamais remplaces
# --------------------------------------------------------------------------- #
# Les trois cartes reprennent les trois FORMATS qu'il a cites (workshop,
# concert, scene ouverte). Aucun quatrieme format n'a ete ajoute.
FORMATS = [
    ('Un workshop',
     'Une pratique, guidée de bout en bout, dans laquelle on entre à plusieurs.'),
    ('Un concert',
     'De la musique jouée là, dans la pièce, à quelques mètres.'),
    ('Une scène ouverte',
     'Le micro passe : on vient écouter, et on peut venir jouer.'),
]

EXPLORER = [
    'La créativité, le corps, la conscience.',
    'La relation, la musique, le développement personnel.',
    'La spiritualité, le jeu, la danse, le mouvement.',
]


def cartes_formats():
    return '<div class="rdv-cols">' + ''.join(
        '<div class="rdv-card"><h3>%s</h3><p>%s</p></div>' % (t, p)
        for t, p in FORMATS) + '</div>'


def liste(items):
    return '<ul class="rdv-ul">' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'


# --------------------------------------------------------------------------- #
# LES ENCARTS — UN PAR SOIREE, DANS L'ORDRE CHRONOLOGIQUE
# --------------------------------------------------------------------------- #
# Chaque date du programme est un lien vers SON encart. Avant le 20/08/2026,
# seule INSTATIC en avait un : les trois autres dates ne menaient nulle part,
# donc rien n'etait cliquable. C'est ce que David a demande de reparer.
#
# Deux formes, et une seule bascule : la presence du champ `titre`.
#   - soiree complete  -> `_encart_complet` : fiche pratique, encadre d'alerte,
#     recit, « Au programme », phrase de fin, bouton de reservation ;
#   - soiree en attente -> `_encart_attente` : la date, l'horaire, « Programme
#     en cours d'elaboration ». Rien de plus, ce sont les mots de David.


def faits(soiree):
    """La fiche pratique en tete d'encart : ce qu'on vient chercher en arrivant."""
    return '<dl class="rdv-facts">' + ''.join(
        '<div><dt>%s</dt><dd>%s%s</dd></div>'
        % (t, v, ('<small>%s</small>' % s) if s else '')
        for t, v, s in soiree['faits']) + '</dl>'


def _retour():
    """Le chemin du retour : depuis un encart, on remonte au programme."""
    return '<a class="btn ghost" href="#programme">Revoir les dates &#8594;</a>'


def _abonnement():
    """« Etre prevenu » d'une soiree pas encore programmee.

    ⚠️ CE N'ETAIT PAS CA AVANT LE 20/08/2026 : le lien ouvrait un e-mail
    (`mailto:`) et David l'a redirige vers L'ABONNEMENT A L'AGENDA DU NID. Le
    raisonnement se tient tout seul : un e-mail demande a quelqu'un de penser a
    repondre, l'abonnement pose la date dans l'agenda du visiteur des qu'elle
    existe, sans personne au milieu.

    ⚠️ MEME GESTE QUE SUR `/le-nid`, VOLONTAIREMENT : meme bouton Google Agenda,
    meme second lien pour Apple Calendrier / Outlook, memes adresses (relues
    dans `generate_agenda_nid.py`, jamais recopiees). Quelqu'un qui a deja vu
    l'encart de l'agenda reconnait le meme geste ici.
    """
    return ('<div class="rdv-abo">'
            '<h3>Le programme n’est pas encore écrit</h3>'
            '<p>Abonnez-vous à l’agenda du Nid : la soirée s’ajoutera toute '
            'seule dans votre agenda personnel dès qu’elle sera calée, avec son '
            'horaire et son programme. Gratuit, sans inscription.</p>'
            '<div class="rdv-abo-act">'
            '<a class="btn" href="%s" target="_blank" rel="noopener">'
            'S’abonner avec Google Agenda</a>'
            '<a class="rdv-tell" href="%s">Apple Calendrier, Outlook ou autre</a>'
            '</div></div>' % (CAL_SUB, CAL_WEBCAL))


def _encart_complet(d):
    bloc = ['<section class="rdv-block" id="%s"><div class="wrap">' % d['ancre'],
            '<div class="kick">%s</div>' % d['jour'],
            '<h2 class="sec-title">%s</h2>' % d['titre']]
    if d.get('chapeau'):
        bloc.append('<p class="lead">%s</p>' % d['chapeau'])
    if d.get('faits'):
        bloc.append(faits(d))
    if d.get('alerte'):
        bloc.append('<div class="rdv-warn">%s</div>' % d['alerte'])
    bloc += ['<p>%s</p>' % t for t in d.get('recit', [])]
    if d.get('au_programme'):
        bloc.append('<p class="body"><b>Au programme</b></p>')
        bloc.append(liste(d['au_programme']))
    if d.get('fin'):
        bloc.append('<p>%s</p>' % d['fin'])
    boutons = ''
    if d.get('resa'):
        boutons = ('<a class="btn" href="%s" target="_blank" rel="noopener">%s</a>'
                   % (d['resa'], d['resa_texte']))
    bloc.append('<div class="cta rdv-cta">%s%s</div>' % (boutons, _retour()))
    bloc.append('</div></section>')
    return ''.join(bloc)


def _encart_attente(d):
    """La date, l'horaire, « programme en cours d'elaboration ». Rien d'autre.

    Ce sont les mots de David, et « juste » est de lui : on ne complete pas.

    ⚠️ Le titre de l'encart est LA DATE, et pas « Programme en cours
    d'elaboration » : ce dernier serait identique sur les trois encarts, et
    quelqu'un qui navigue au clavier ou au lecteur d'ecran entendrait trois fois
    le meme titre sans savoir de quelle soiree il s'agit. La formule de David
    est juste en dessous, dans la fiche.
    """
    return ('<section class="rdv-block rdv-attente" id="%s"><div class="wrap">'
            '<div class="kick">Rendez-vous mensuel</div>'
            '<h2 class="sec-title">%s</h2>'
            '<dl class="rdv-facts">'
            '<div><dt>Horaire</dt><dd>%s</dd></div>'
            '<div><dt>Programme</dt><dd>En cours d’élaboration</dd></div>'
            '</dl>'
            '%s'
            '<div class="cta rdv-cta">%s</div>'
            '</div></section>'
            % (d['ancre'], d['jour'], HORAIRE_INCONNU, _abonnement(), _retour()))


def encarts():
    """Les quatre encarts, separes par le meme filet que le reste de la page."""
    faits_html = [_encart_complet(d) if d.get('titre') else _encart_attente(d)
                  for d in SOIREES]
    return '<div class="divider"></div>'.join(faits_html)


HTML = f"""<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Les RDV Mensuels au Nid — une proposition différente chaque mois · Résonances Productions</title>
<meta name="description" content="Une fois par mois, Le Nid (Paris 20ᵉ) ouvre ses portes pour une proposition différente : workshop, concert ou scène ouverte, avec des intervenants choisis par Iris et David. Les prochaines dates et le programme.">
<meta property="og:title" content="Les RDV Mensuels au Nid — Paris 20ᵉ">
<meta property="og:description" content="Une soirée par mois au Nid, jamais la même : workshop, concert, scène ouverte. Créer du lien, explorer — la créativité, le corps, la conscience, la relation, la musique, le mouvement.">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}/{SLUG}">
<meta property="og:image" content="{SITE}/img/le-nid/soiree-au-nid-1400.jpg">
<meta property="og:image:width" content="1400">
<meta property="og:image:height" content="646">
<meta property="og:image:alt" content="Une soirée au Nid : le public assis au sol devant un rideau de guirlandes lumineuses, deux musiciennes et des bougies.">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0e0f24">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body id="top">

<nav class="nav">
  <a href="/" class="brand">Résonances Productions</a>
  <div class="links">
    <a href="/">Accueil</a>
    <a href="/le-nid">Le Nid</a>
    <a href="#contact">Contact</a>
    <a class="adh" href="{HELLO}" target="_blank" rel="noopener">Adhérer</a>
  </div>
</nav>

<header class="rdv-top"><div class="wrap">
  <div class="kick">Une fois par mois · Le Nid, Paris 20<sup>e</sup></div>
  <h1>Les RDV Mensuels au Nid</h1>
  <div class="tagline">« Une proposition différente à chaque fois »</div>
  <p class="lead">Un soir par mois, Le Nid ouvre ses portes pour une soirée qui n’est jamais tout à fait la même : un workshop, un concert, une scène ouverte. Toujours sur réservation, toujours avec des intervenants différents.</p>
  <div class="cta rdv-saut"><a class="btn" href="#programme">Voir les prochaines dates &#8595;</a></div>
</div></header>

<section id="intention"><div class="wrap">
  <div class="kick">L’intention</div>
  <h2 class="sec-title">Créer du lien, et explorer ensemble</h2>
  <p class="body">Ce qui relie ces soirées entre elles, ce n’est pas une discipline : c’est une intention. <b>Créer du lien</b>, et <b>explorer</b> — sous plusieurs formes, d’un mois à l’autre.</p>
  {liste(EXPLORER)}
  <p class="body">Trois formats reviennent, et se relaient :</p>
  {cartes_formats()}
  <p class="body">Toujours sur réservation, toujours avec <b>différents intervenants</b> : on va voyager à travers plein d’univers différents.</p>
  <p class="rdv-quote">Créer une communauté qui vient se nourrir, explorer, s’enrichir dans ce lieu porté par notre intention, notre énergie.</p>
  <div class="rdv-note">
    <h3>Qui choisit ce qui se passe ici</h3>
    <p>La sélection des intervenants se fait par <b>Iris et David</b>. Ce sera toujours des personnes que nous connaissons, que nous avons rencontrées, dont on trouve la proposition de qualité, <b>avec du cadre, de la sécurité, du fun</b>.</p>
    <p>C’est le seul filtre, et c’est aussi tout ce qu’on peut promettre d’une soirée dont on ne connaît pas encore le contenu : nous savons qui la porte.</p>
  </div>
</div></section>

<div class="divider"></div>

<section class="band" id="programme"><div class="wrap">
  <div class="kick">Le programme</div>
  <h2 class="sec-title">Les prochaines dates, en un coup d’œil</h2>
  <p class="lead">Quatre rendez-vous sont posés jusqu’en décembre. Le programme du 4 septembre est écrit et la réservation est ouverte ; les trois soirées suivantes attendent le leur, et il sera annoncé ici. Chaque date ouvre son encart, juste en dessous.</p>
  {programme()}
</div></section>

<div class="divider"></div>

{encarts()}

{retour_haut.html()}
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
      <p style="margin-top:8px"><a href="{HELLO}" target="_blank" rel="noopener">Adhérer / soutenir</a></p>
      <p style="margin-top:8px"><a href="{STATUTS}" target="_blank" rel="noopener">Statuts de l’association</a></p>
    </div>
  </div>
  <div class="legal">© 2026 Résonances Productions · resonancesproductions.org</div>
</div></footer>
{retour_haut.js()}</body></html>"""

HTML = mobile_nav.inject(HTML)
HTML = nav_menu.inject(HTML, SLUG)


# --------------------------------------------------------------------------- #
# GARDE-FOUS — la page n'est PAS ecrite si l'un d'eux tombe
# --------------------------------------------------------------------------- #
def _controle_dates():
    """Les 4 dates doivent etre celles de l'agenda de /le-nid.

    On RELIT `generate_agenda_nid.py` en texte plutot que de l'importer : ce
    module travaille au moment de l'import et reecrirait /le-nid (piege
    documente dans build.py). Une date ajoutee ou retiree la-bas arrete donc la
    generation ici, au lieu de laisser une page en retard partir en ligne.
    """
    src = _source_agenda()
    vues = re.findall(r"\('(\d{4}-\d{2}-\d{2})',\s*'[^']*',\s*'[^']*',\s*'mensuel'", src)
    attendu = [d['iso'] for d in SOIREES]
    if vues != attendu:
        raise SystemExit(
            '!! ABANDON : les rendez-vous mensuels de generate_agenda_nid.py '
            'sont %s, cette page annonce %s. Page NON ecrite.' % (vues, attendu))


def _controle_ordre():
    """L'ordre des blocs est celui que David a dicte. Il se verifie.

    Le projet a deja « ameliore » un ordre impose et il a fallu le refaire. Le
    controle est bete et suffisant : on compare les positions dans le texte de
    la page livree.
      chapeau (le bouton) -> l'intention -> le programme -> le premier encart.
    """
    reperes = [('le bouton « Voir les prochaines dates »',
                'class="cta rdv-saut"'),
               ('la section intention (le projet)', 'id="intention"'),
               ('le programme et ses dates', 'id="programme"'),
               ('le premier encart', 'id="%s"' % SOIREES[0]['ancre'])]
    places = []
    for quoi, marqueur in reperes:
        ou = HTML.find(marqueur)
        if ou < 0:
            raise SystemExit('!! ABANDON : %s est introuvable dans la page. '
                             'Page NON ecrite.' % quoi)
        places.append((ou, quoi))
    for (a, quoi_a), (b, quoi_b) in zip(places, places[1:]):
        if a > b:
            raise SystemExit('!! ABANDON : %s arrive APRES %s. L\'ordre voulu '
                             'par David est : chapeau + bouton, puis '
                             'l\'intention, puis le programme, puis les '
                             'encarts. Page NON ecrite.' % (quoi_a, quoi_b))


def _controle_ancres():
    """Chaque date doit mener a un encart qui existe VRAIMENT.

    Le projet a deja publie des liens vers des ancres inexistantes, et jusqu'au
    20/08/2026 trois des quatre dates de cette page ne menaient nulle part. Le
    controle est fait ici, avant l'ecriture, et refait ensuite par
    `verif_site.py` sur la page livree — les deux ne coutent rien et ne se
    remplacent pas.
    """
    ids = set(re.findall(r'\bid="([^"]+)"', HTML))
    for ancre in sorted(set(re.findall(r'href="#([^"]+)"', HTML))):
        if ancre not in ids:
            raise SystemExit('!! ABANDON : lien vers #%s, mais aucun bloc ne '
                             'porte cet identifiant. Page NON ecrite.' % ancre)
    for d in SOIREES:
        if not d.get('ancre'):
            raise SystemExit('!! ABANDON : la soiree du %s n’a pas d’ancre, '
                             'donc pas d’encart. Page NON ecrite.' % d['jour'])
        if d['ancre'] not in ids:
            raise SystemExit('!! ABANDON : la date du %s renvoie a #%s, absente '
                             'de la page. Page NON ecrite.' % (d['jour'], d['ancre']))
        if HTML.count('href="#%s"' % d['ancre']) != 1:
            raise SystemExit('!! ABANDON : %d lien(s) vers #%s, attendu 1 (la '
                             'ligne du programme). Page NON ecrite.'
                             % (HTML.count('href="#%s"' % d['ancre']), d['ancre']))
    # Autant de lignes cliquables que de soirees : une date sans lien, c'est
    # exactement le defaut qu'on vient de corriger.
    lignes = HTML.count('class="rdv-go"')
    if lignes != len(SOIREES):
        raise SystemExit('!! ABANDON : %d ligne(s) cliquable(s) pour %d '
                         'soiree(s). Page NON ecrite.' % (lignes, len(SOIREES)))


def _controle_jauge():
    """La jauge d'INSTATIC est ecrite a trois endroits : elle doit dire pareil.

    Elle est passee de 20 a 25 le 20/08/2026. C'est le genre de chiffre qu'on
    corrige a un endroit sur deux — le second contredit alors le premier sur la
    page publiee, et personne ne s'en apercoit avant la soiree.
    ⚠️ Le TARIF vaut 20 EUR et n'a pas change : ne pas le confondre.
    """
    dits = re.findall(r'(\d+)\s*(?:places|personnes)', HTML)
    faux = [n for n in dits if n != str(JAUGE)]
    if faux:
        raise SystemExit('!! ABANDON : la page annonce une jauge de %s alors '
                         'que JAUGE vaut %d. Page NON ecrite.'
                         % (' et '.join(faux), JAUGE))
    if len(dits) != 3:
        raise SystemExit('!! ABANDON : la jauge est annoncee %d fois, attendu 3 '
                         '(la ligne du programme, la fiche pratique et '
                         'l’encadre des portes). Page NON ecrite.' % len(dits))


def _controle_structure():
    """Ce qui doit exister une fois et une seule sur la page livree."""
    attendus = [
        ('<h1', 'titre principal'),
        ('id="intention"', 'la section intention (le projet)'),
        ('id="programme"', 'le programme et ses dates'),
        (INSTATIC_RESA, 'le lien de reservation HelloAsso'),
        ('class="totop"', 'bouton retour en haut'),
        ('id="top"', 'cible du bouton retour en haut'),
    ]
    attendus += [('id="%s"' % d['ancre'], 'l’encart du %s' % d['jour'])
                 for d in SOIREES]
    for marqueur, role in attendus:
        if HTML.count(marqueur) != 1:
            raise SystemExit('!! ABANDON : %d occurrence(s) de « %s » (%s), '
                             'attendu 1. Page NON ecrite.'
                             % (HTML.count(marqueur), marqueur, role))
    # L'abonnement a l'agenda : une fois par soiree non programmee, et jamais
    # une adresse recopiee a la main.
    attente = sum(1 for d in SOIREES if not d.get('titre'))
    if HTML.count('class="rdv-abo"') != attente:
        raise SystemExit('!! ABANDON : %d encart(s) d’abonnement pour %d '
                         'soiree(s) sans programme. Page NON ecrite.'
                         % (HTML.count('class="rdv-abo"'), attente))
    # Les mots de David pour une soiree pas encore programmee. Ils doivent se
    # lire dans la ligne du programme ET dans l'encart.
    if HTML.count(EN_COURS) != attente:
        raise SystemExit('!! ABANDON : « %s » apparait %d fois, attendu %d (une '
                         'par ligne de soiree sans programme). Page NON ecrite.'
                         % (EN_COURS, HTML.count(EN_COURS), attente))
    # ⚠️ AUCUNE IMAGE DANS CETTE PAGE depuis le 20/08/2026 (David). `og:image`
    #    n'est pas concernee : c'est la vignette de partage, hors de la page.
    corps = HTML.split('</head>', 1)[-1]
    if '<img' in corps or '<picture' in corps:
        raise SystemExit('!! ABANDON : une image est reapparue dans le corps de '
                         'la page. David les a fait retirer le 20/08/2026. '
                         'Page NON ecrite.')


_controle_dates()
_controle_ordre()
_controle_ancres()
_controle_jauge()
_controle_structure()

DOSSIER = os.path.join(RACINE, SLUG)
os.makedirs(DOSSIER, exist_ok=True)
OUT = os.path.join(DOSSIER, 'index.html')
# Garde-fou AVANT l'ecriture : aucune note de redaction en commentaire HTML.
verif_commentaires.verifier(HTML, OUT)
open(OUT, 'w', encoding='utf-8').write(HTML)
print('WROTE', OUT, round(len(HTML) / 1024), 'KB')
