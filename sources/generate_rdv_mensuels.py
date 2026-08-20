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

L'ordre des trois blocs est donc IMPOSE, et il ne doit pas etre « ameliore » :
  1. le programme en un coup d'oeil (les 4 dates) ;
  2. l'intention des rendez-vous mensuels ;
  3. un encart detaille par evenement, cible par les ancres du bloc 1.

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

CE QUI N'EST PAS ECRIT ICI, ET POURQUOI
---------------------------------------
Quatre autres formats ont ete cites par David — Workshop Sexto, Concert
intimiste, La roue du consentement, Scene ouverte du vendredi soir — SANS
aucune date, aucun prix, aucun horaire, aucun intervenant, aucune description.
Ils sont donc presentes en une ligne chacun, au futur, dans « Ce qui se
prepare ». Rien n'est invente : pas de titre de remplacement, pas de duree
« vraisemblable », pas de fourchette de tarif.
⚠️ « La roue du consentement » porte la precision exacte de David — « mieux se
   connaitre dans nos desirs et nos limites, pas de sexualite ». Elle cadre
   l'atelier et evite un malentendu : elle ne doit pas etre coupee.

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
⚠️ « Fermeture stricte des portes a 19h00 » et « 20 places seulement » sont des
   informations CRITIQUES : quelqu'un qui arrive a 19h05 n'entre pas. Elles
   apparaissent DEUX fois — dans la ligne du programme en haut de page, et en
   tete de l'encart — et jamais noyees dans un paragraphe.

CE QUE LA PAGE PARTAGE AVEC LE RESTE DU SITE
--------------------------------------------
Menu (`nav_menu.py`) · hamburger (`mobile_nav.py`) · couche chaleureuse
(`theme_chaleur.py`) · visionneuse photo (`visionneuse.py`) · bouton retour en
haut (`retour_haut.py`, la page depasse 4 000 px sur telephone) · garde-fou
commentaires HTML (`verif_commentaires.py`).

AUCUN FICHIER N'A ETE AJOUTE DANS `img/`. Les deux photos sont celles des
rendez-vous mensuels deja publiees sur `/le-nid` (`soiree-au-nid-*` et
`soiree-mensuel-2-*`) : ce sont de vraies photos de ces soirees-la. Leurs
legendes ne disent pas qu'elles montrent INSTATIC — la soiree n'a pas encore eu
lieu.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mobile_nav  # noqa: E402
import nav_menu  # noqa: E402
import retour_haut  # bouton « retour en haut »  # noqa: E402
import theme_chaleur  # couche chaleureuse commune  # noqa: E402
import verif_commentaires  # garde-fou commentaires HTML  # noqa: E402
import visionneuse  # visionneuse photo commune  # noqa: E402

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
.rdv-row{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:18px;padding:22px 24px;display:grid;grid-template-columns:minmax(0,200px) minmax(0,1fr) minmax(0,190px);gap:20px 26px;align-items:center}
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
            # Le lien « etre prevenu » des trois dates sans programme : un lien
            # texte, pas un bouton dore. Il ne doit pas peser autant que le seul
            # bouton qui mene vraiment quelque part (« En savoir plus »).
            # Cible tactile : 44 px de haut, plancher du site.
            """.rdv-tell{display:inline-flex;align-items:center;min-height:44px;color:var(--gold2);font-size:15px;text-decoration:underline;text-decoration-color:rgba(248,210,116,.42);text-underline-offset:4px}
.rdv-tell:hover{text-decoration-color:var(--gold2)}
"""
            # Sous 860 px la ligne passe en deux colonnes (date + titre), puis en
            # une seule sous 620. Aucune valeur fixe : `minmax(0,…)` partout,
            # sinon une longue date force la grille a deborder.
            """@media(max-width:860px){.rdv-row{grid-template-columns:minmax(0,1fr);gap:14px;padding:20px}
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
            # --- les photos ----------------------------------------------------
            """.rdv-figs{display:grid;grid-template-columns:minmax(0,1.55fr) minmax(0,1fr);gap:20px;margin-top:34px;align-items:start}
.rdv-fig{margin:0;border-radius:18px;overflow:hidden;border:1px solid var(--line);background:var(--card)}
.rdv-fig img{display:block;width:100%;height:auto}
.rdv-fig figcaption{color:var(--muted);font-size:13.5px;line-height:1.5;padding:12px 16px 14px;border-top:1px solid rgba(255,255,255,.06)}
@media(max-width:760px){.rdv-figs{grid-template-columns:minmax(0,1fr)}}
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
.rdv-prep{display:grid;gap:14px;margin-top:30px;max-width:900px}
.rdv-prep div{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:16px;padding:18px 22px;border-left:3px solid transparent;background-image:var(--grad-v),linear-gradient(var(--card),var(--card));background-size:3px 100%,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box}
.rdv-prep h3{font-family:'Cormorant Garamond',Georgia,serif;font-size:22px;color:var(--gold2);font-weight:600;line-height:1.2}
.rdv-prep p{color:#d7d4ea;font-size:15.5px;margin-top:6px}
""")

CSS = CSS + theme_chaleur.CSS + CSS_PAGE + retour_haut.css() + visionneuse.css('')

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


def _prevenir(quand):
    """Lien « etre prevenu » d'une soiree dont le programme n'est pas arrete.

    ⚠️ CE N'EST PAS UN BOUTON « EN SAVOIR PLUS » DEGUISE. Les trois soirees
    d'octobre, novembre et decembre n'ont AUCUN encart : un bouton qui
    descendrait vers du vide serait une promesse non tenue, et le projet a deja
    eu des liens vers des ancres inexistantes. On propose donc le seul geste
    reellement utile aujourd'hui : demander a etre prevenu. La date part dans
    l'objet du message pour que David sache de laquelle on parle.
    """
    sujet = ('Les RDV Mensuels — être prévenu du %s' % quand)
    return ('mailto:contact@resonancesproductions.org?subject='
            + _url(sujet))


def _url(texte):
    """Encodage pour un `mailto:` — sans dependance, comme partout sur le site."""
    import urllib.parse
    return urllib.parse.quote(texte, safe='')


# --------------------------------------------------------------------------- #
# LES QUATRE DATES
# --------------------------------------------------------------------------- #
# (date ISO, jour + date en clair, horaire affiche, titre, sur-titre, sous-titre,
#  prix affiche, ancre de l'encart detaille)
#
# ⚠️ `horaire`, `titre`, `prix` et `ancre` valent None tant que le programme
#    n'est pas arrete. La page ecrit alors une phrase au FUTUR et propose
#    « etre prevenu » — jamais un titre approchant, jamais un horaire repris de
#    l'agenda (voir la contradiction 1 en tete de fichier), jamais un tarif.
DATES = [
    dict(iso='2026-09-04', jour='Vendredi 4 septembre 2026',
         horaire='19h00 – 21h30', type='Danse',
         titre='INSTATIC Dance',
         sous='Co-créée et facilitée par Iris &amp; David. '
              'Portes fermées à 19h00 · 20 places seulement.',
         prix='20 €', ancre='instatic'),
    dict(iso='2026-10-02', jour='Vendredi 2 octobre 2026',
         horaire=None, type=None, titre=None, sous=None, prix=None, ancre=None),
    dict(iso='2026-11-07', jour='Samedi 7 novembre 2026',
         horaire=None, type=None, titre=None, sous=None, prix=None, ancre=None),
    dict(iso='2026-12-04', jour='Vendredi 4 décembre 2026',
         horaire=None, type=None, titre=None, sous=None, prix=None, ancre=None),
]

#: la phrase des soirees dont le programme n'est pas encore ecrit. Au FUTUR :
#: regle du projet — ce qui n'est pas livre ne s'annonce jamais au present.
A_VENIR = ('La proposition de cette soirée sera annoncée ici. '
           'Le programme, l’horaire et le tarif ne sont pas encore arrêtés.')


def ligne(d):
    """Une ligne du programme en un coup d'oeil."""
    if d['titre']:
        quoi = ('<span class="rdv-type">%s</span><h3>%s</h3>'
                '<p class="rdv-sub">%s</p>' % (d['type'], d['titre'], d['sous']))
        acte = ('<span class="rdv-price">%s</span>'
                '<a class="btn ghost" href="#%s">En savoir plus</a>'
                % (d['prix'], d['ancre']))
        heures = '<span class="rdv-hours">%s</span>' % d['horaire']
    else:
        quoi = '<p class="rdv-soon">%s</p>' % A_VENIR
        acte = ('<a class="rdv-tell" href="%s">Être prévenu du programme</a>'
                % _prevenir(d['jour'].split(' ', 1)[1]))
        heures = ''
    return ('<li class="rdv-row">'
            '<div class="rdv-when"><span class="rdv-day">%s</span>%s</div>'
            '<div class="rdv-what">%s</div>'
            '<div class="rdv-act">%s</div>'
            '</li>' % (d['jour'], heures, quoi, acte))


def programme():
    return '<ol class="rdv-list">' + ''.join(ligne(d) for d in DATES) + '</ol>'


# --------------------------------------------------------------------------- #
# LES PHOTOS — deja publiees sur /le-nid, aucun fichier ajoute dans img/
# --------------------------------------------------------------------------- #
# `width` / `height` portent les dimensions de la photo D'ORIGINE et non la
# largeur d'affichage : c'est la convention de /le-nid, et `verif_site.py` en
# tient compte (il ne controle `width` que sur les images sans `sizes`, et
# verifie surtout que chaque largeur annoncee dans un `srcset` correspond au
# vrai fichier).
PHOTOS = [
    dict(base='/img/le-nid/soiree-au-nid', widths=(480, 900, 1400, 2000),
         src=1400, w=2796, h=1290,
         sizes='(max-width:760px) 100vw, 620px',
         alt='Une soiree au Nid : le public assis au sol devant un rideau de '
             'guirlandes lumineuses, deux musiciennes et des bougies',
         cap='Une soirée au Nid — musique live, bougies et petit comité.'),
    dict(base='/img/le-nid/soiree-mensuel-2', widths=(480, 900, 1400),
         src=900, w=1500, h=2000,
         sizes='(max-width:760px) 100vw, 380px',
         alt='Deux musiciens assis au sol jouent de la calebasse devant un mur '
             'de guirlandes lumineuses et un mandala lumineux, une lampe à '
             'flamme posée entre eux',
         cap='Un autre soir, la calebasse — d’une soirée à l’autre, la '
             'proposition change.'),
]


def figure(p):
    webp = ', '.join('%s-%d.webp %dw' % (p['base'], w, w) for w in p['widths'])
    jpg = ', '.join('%s-%d.jpg %dw' % (p['base'], w, w) for w in p['widths'])
    return ('<figure class="rdv-fig"><picture>'
            '<source type="image/webp" srcset="%s" sizes="%s">'
            '<img src="%s-%d.jpg" srcset="%s" sizes="%s" width="%d" height="%d" '
            'loading="lazy" decoding="async" alt="%s">'
            '</picture><figcaption>%s</figcaption></figure>'
            % (webp, p['sizes'], p['base'], p['src'], jpg, p['sizes'],
               p['w'], p['h'], p['alt'], p['cap']))


def figures():
    return '<div class="rdv-figs">' + ''.join(figure(p) for p in PHOTOS) + '</div>'


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
# INSTATIC — la fiche pratique
# --------------------------------------------------------------------------- #
# Reprise mot pour mot de l'annonce de David. L'accueil et la jauge sont dans
# cette fiche ET rappeles dans l'encart d'avertissement juste en dessous : ce
# sont les deux informations qui font qu'on entre ou qu'on n'entre pas.
FAITS = [
    ('Quand', 'Vendredi 4 septembre 2026, de 19h00 à 21h30', ''),
    ('Accueil', 'Portes ouvertes dès 18h45',
     'Fermeture stricte des portes à 19h00'),
    ('Où', 'Le Nid — Paris 20<sup>e</sup>', '29 rue des Orteaux'),
    ('Tarif', '20 €', 'Réservation en ligne'),
    ('Jauge', '20 personnes seulement', 'Très limitée'),
]

AU_PROGRAMME = [
    'DJ set en vagues (du rythme soutenu à la douceur) &amp; guidance '
    'corporelle par Iris.',
    'Créations sonores &amp; instruments live (voix, Neotone, n’goni) par David.',
    'Danse libre, expressive et consciente, dans le respect des guidelines '
    'traditionnelles.',
    'Un cadre intimiste et sécurisant pour danser pleinement.',
]


def faits():
    return '<dl class="rdv-facts">' + ''.join(
        '<div><dt>%s</dt><dd>%s%s</dd></div>'
        % (t, v, ('<small>%s</small>' % s) if s else '')
        for t, v, s in FAITS) + '</dl>'


# --------------------------------------------------------------------------- #
# CE QUI SE PREPARE — quatre formats cites par David, SANS aucun detail
# --------------------------------------------------------------------------- #
# ⚠️ Ni date, ni prix, ni horaire, ni intervenant, ni description n'existent
#    pour ces quatre-la. Une ligne chacun, au futur. Ne RIEN completer.
PREPARE = [
    ('Un workshop Sexto', 'Le format se prépare.'),
    ('Un concert intimiste', 'Le format se prépare.'),
    ('La roue du consentement',
     'Mieux se connaître dans nos désirs et nos limites — pas de sexualité.'),
    ('Une scène ouverte, un vendredi soir', 'Le format se prépare.'),
]


def prepare():
    return '<div class="rdv-prep">' + ''.join(
        '<div><h3>%s</h3><p>%s</p></div>' % (t, p) for t, p in PREPARE) + '</div>'


VIS_JS = visionneuse.js('.rdv-fig img')

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
</div></header>

<section id="programme"><div class="wrap">
  <div class="kick">Le programme</div>
  <h2 class="sec-title">Les prochaines dates, en un coup d’œil</h2>
  <p class="lead">Quatre rendez-vous sont posés jusqu’en décembre. Le programme du 4 septembre est écrit et la réservation est ouverte ; les trois soirées suivantes attendent le leur, et il sera annoncé ici.</p>
  {programme()}
</div></section>

<div class="divider"></div>

<section class="band" id="intention"><div class="wrap">
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
  {figures()}
</div></section>

<div class="divider"></div>

<section class="rdv-block" id="instatic"><div class="wrap">
  <div class="kick">Vendredi 4 septembre 2026</div>
  <h2 class="sec-title">INSTATIC Dance</h2>
  <p class="lead">Co-créée et facilitée par Iris &amp; David.</p>
  {faits()}
  <div class="rdv-warn"><b>Les portes ferment à 19h00, sans exception</b>, et la jauge est de <b>20 personnes</b>. Arriver à 18h45 fait partie de la soirée : une fois la traversée commencée, on n’ouvre plus.</div>
  <p>En cette rentrée, nous avons la joie de vous ouvrir les portes du Nid, notre cocon dans le 20<sup>e</sup> arrondissement, pour une toute nouvelle expérience : une <b>INSTATIC Dance</b>, co-créée et facilitée par Iris &amp; David.</p>
  <p>Cette soirée est une invitation à réhabiter pleinement son corps à travers un véritable <b>voyage musical en vagues</b>.</p>
  <p>L’INSTATIC Dance, ce n’est pas une simple méditation passive : c’est une traversée complète. Attendez-vous à une exploration dynamique, où des phases d’envolées très rythmées, puissantes et vibrantes alternent avec des temps d’ancrage, de douceur et d’intériorité. Loin de la sur-stimulation du clubbing ou de la recherche de catharsis à tout prix, <b>nous dansons pour restaurer notre énergie et nourrir notre présence</b>.</p>
  <p>Une immersion conçue à quatre mains : Iris aux platines pour tisser les vagues musicales et la guidance corporelle, rejointe par David pour faire vibrer l’espace en direct avec sa voix chantée, son handpan électronique et sa harpe.</p>
  <p class="body"><b>Au programme</b></p>
  {liste(AU_PROGRAMME)}
  <p>Venez comme vous êtes, pour faire circuler l’énergie, traverser le mouvement et recharger votre flamme intérieure.</p>
  <div class="cta" style="margin-top:28px"><a class="btn" href="{INSTATIC_RESA}" target="_blank" rel="noopener">Réserver ma place — 20 € ↗</a><a class="btn ghost" href="#programme">Revoir les dates →</a></div>
</div></section>

<div class="divider"></div>

<section class="band" id="a-venir"><div class="wrap">
  <div class="kick">Ce qui se prépare</div>
  <h2 class="sec-title">Les prochaines propositions</h2>
  <p class="body">Voici les formats sur lesquels nous travaillons pour les mois qui viennent. <b>Rien n’est encore daté</b> : ni le programme, ni l’horaire, ni le tarif ne sont arrêtés. Dès qu’une soirée est calée, elle apparaît en haut de cette page.</p>
  {prepare()}
  <p class="body">Vous voulez être prévenu dès qu’une date est posée, ou vous avez une proposition à nous faire ? <a href="mailto:contact@resonancesproductions.org">Écrivez-nous</a>.</p>
  <div class="cta" style="margin-top:26px"><a class="btn ghost" href="/le-nid#agenda">Voir tout l’agenda du Nid →</a><a class="btn ghost" href="/le-nid">Découvrir Le Nid →</a></div>
</div></section>

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
{retour_haut.js()}
{VIS_JS}</body></html>"""

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
    chemin = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          'generate_agenda_nid.py')
    with open(chemin, encoding='utf-8') as f:
        src = f.read()
    vues = re.findall(r"\('(\d{4}-\d{2}-\d{2})',\s*'[^']*',\s*'[^']*',\s*'mensuel'", src)
    attendu = [d['iso'] for d in DATES]
    if vues != attendu:
        raise SystemExit(
            '!! ABANDON : les rendez-vous mensuels de generate_agenda_nid.py '
            'sont %s, cette page annonce %s. Page NON ecrite.' % (vues, attendu))


def _controle_ancres():
    """Chaque « En savoir plus » doit viser une ancre qui existe VRAIMENT.

    Le projet a deja publie des liens vers des ancres inexistantes. Le controle
    est fait ici, avant l'ecriture, et refait ensuite par `verif_site.py` sur la
    page livree — les deux ne coutent rien et ne se remplacent pas.
    """
    ids = set(re.findall(r'\bid="([^"]+)"', HTML))
    for ancre in sorted(set(re.findall(r'href="#([^"]+)"', HTML))):
        if ancre not in ids:
            raise SystemExit('!! ABANDON : lien vers #%s, mais aucun bloc ne '
                             'porte cet identifiant. Page NON ecrite.' % ancre)
    for d in DATES:
        if d['ancre'] and d['ancre'] not in ids:
            raise SystemExit('!! ABANDON : la date du %s renvoie a #%s, absente '
                             'de la page. Page NON ecrite.' % (d['jour'], d['ancre']))
    # Une date SANS programme ne doit surtout pas porter de bouton « En savoir
    # plus » : il descendrait vers du vide.
    attendus = sum(1 for d in DATES if d['ancre'])
    trouves = HTML.count('>En savoir plus</a>')
    if trouves != attendus:
        raise SystemExit('!! ABANDON : %d bouton(s) « En savoir plus » pour %d '
                         'soiree(s) au programme connu. Page NON ecrite.'
                         % (trouves, attendus))


def _controle_structure():
    """Ce qui doit exister une fois et une seule sur la page livree."""
    for marqueur, role in (
            ('<h1', 'titre principal'),
            ('id="programme"', 'le programme en un coup d’oeil'),
            ('id="intention"', 'la section intention'),
            ('id="instatic"', 'l’encart INSTATIC'),
            ('id="a-venir"', 'la section « ce qui se prepare »'),
            (INSTATIC_RESA, 'le lien de reservation HelloAsso'),
            ('.ph{position:fixed', 'feuille de style de la visionneuse'),
            ("var SEL='.rdv-fig img", 'script de la visionneuse'),
            ('class="totop"', 'bouton retour en haut'),
            ('id="top"', 'cible du bouton retour en haut'),
    ):
        if HTML.count(marqueur) != 1:
            raise SystemExit('!! ABANDON : %d occurrence(s) de « %s » (%s), '
                             'attendu 1. Page NON ecrite.'
                             % (HTML.count(marqueur), marqueur, role))
    # La precision de David sur « la roue du consentement » cadre l'atelier et
    # evite un malentendu : elle ne doit pas disparaitre a la faveur d'une
    # reecriture.
    if 'pas de sexualité' not in HTML:
        raise SystemExit('!! ABANDON : la precision « pas de sexualite » de la '
                         'roue du consentement a disparu. Page NON ecrite.')


_controle_dates()
_controle_ancres()
_controle_structure()

DOSSIER = os.path.join(RACINE, SLUG)
os.makedirs(DOSSIER, exist_ok=True)
OUT = os.path.join(DOSSIER, 'index.html')
# Garde-fou AVANT l'ecriture : aucune note de redaction en commentaire HTML.
verif_commentaires.verifier(HTML, OUT)
open(OUT, 'w', encoding='utf-8').write(HTML)
print('WROTE', OUT, round(len(HTML) / 1024), 'KB')
