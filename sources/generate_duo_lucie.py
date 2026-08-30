# -*- coding: utf-8 -*-
"""Fabrique /David-Lesage-Lucie-Electric-Violoniste — la page de promo du duo.

CE QUE CETTE PAGE EST, ET CE QU'ELLE N'EST PAS
----------------------------------------------
C'est une page de communication professionnelle destinee aux agences
parisiennes et internationales, pour le duo en emergence entre David Lesage
(handpan electronique, ngoni, calebasse, voix) et Lucie (violon electrique).
Elle a ete demandee par David le 30/08/2026.

⚠️ ELLE EST VOLONTAIREMENT INVISIBLE. Seules les personnes a qui David donne
   l'adresse doivent la trouver. Concretement, quatre choses, et il faut les
   quatre :

     1. AUCUNE ENTREE DE MENU. Ce generateur n'appelle NI `nav_menu.py` NI
        `mobile_nav.py`. La page porte son propre lien de retour discret vers
        l'accueil, et rien du site ne pointe vers elle.
     2. ABSENTE DU PLAN DU SITE. Elle n'est pas dans `sitemap.xml`, et elle
        n'est pas dans `verif_site.PAGES` — c'est voulu : `verif_site.py` ne
        controle que les 31 pages publiees, et son controle « page annoncee
        mais inexistante » ne regarde que cette liste. Une page absente des
        deux listes lui est simplement invisible : le « 31/31 pages
        conformes » reste vrai et intact.
     3. INTERDITE AUX MOTEURS, DEUX FOIS. Un `Disallow:` dans `robots.txt`
        (autorise par le controle de `verif_site.py` : il ne refuse un
        Disallow que sur une page PUBLIEE, c'est-a-dire presente dans
        `PAGES`) ET une balise `<meta name="robots" content="noindex,
        nofollow, noarchive">` dans la page elle-meme. Les deux, parce que
        robots.txt empeche l'exploration mais pas l'indexation d'une adresse
        recuperee ailleurs ; la balise, elle, l'empeche vraiment.
     4. HORS DU TABLEAU DE `build.py`. Ce fichier s'appelle `generate_*.py`,
        il serait donc signale « generateur non inscrit ». Il est declare dans
        `HORS_SITE` de `sources/build.py` : `build.py` ne le lance pas, ne
        touche jamais la page, et ne la sauvegarde pas non plus. Pour la
        reconstruire, on lance CE fichier a la main.

⚠️ CE QUI EST FACTUEL, ET D'OU CA VIENT. Tous les elements de parcours cites
   dans la page (Marciac, The Voice, le Grand Rex, Sziget, les 112 dates cote
   David ; Yamaha YEV-205, Les Muses, Lara Fabian / Florent Pagny / Johnny
   Hallyday / Christophe, la premiere partie d'ERA cote Lucie) viennent des
   sites publies par les interesses eux-memes. RIEN n'a ete invente, aucun
   chiffre n'a ete arrondi a la hausse. Deux points ont ete volontairement
   ECARTES :
     * le NOM DE FAMILLE de Lucie n'apparait nulle part dans le corps visible
       de ses sites (seulement dans des metadonnees) : elle se presente
       commercialement sous son seul prenom, la page fait pareil ;
     * l'annee de fondation du Quatuor Les Muses est donnee differemment
       selon les sources (2007 sur son site, 2010 sur la page Yamaha) : la
       page ne date donc pas la fondation.

COMMENT ON LA RECONSTRUIT
-------------------------
    python3 sources/generate_duo_lucie.py

Les medias (photos et audio) vivent dans le dossier de la page et ne sont pas
fabriques ici : ils ont ete prepares une fois a partir du Drive partage
« 1 - Lucie & David / CAPTATION 28 AOUT 2026 - PARIS ».
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(HERE)

DOSSIER = 'David-Lesage-Lucie-Electric-Violoniste'
SORTIE = os.path.join(RACINE, DOSSIER, 'index.html')
URL = 'https://www.resonancesproductions.org/' + DOSSIER


# --------------------------------------------------------------------------- #
#  LES CINQ MORCEAUX
# --------------------------------------------------------------------------- #
# Enregistres le 28 aout 2026 a Paris. Les durees sont MESUREES sur les
# fichiers (ffprobe), jamais estimees. Le mix retenu est « sortie de table +
# micro d'ambiance Hisong » partout ou il existe — choix de David du 30/08 ;
# « Ave Maria » n'existe qu'en sortie de table.
MORCEAUX = (
    dict(
        fichier='01-lappel-du-vent.mp3', duree='11:09', secondes=669,
        titre_fr="L'appel du vent", titre_en="L'appel du vent",
        sous_fr='Handpan électronique, voix et violon électrique',
        sous_en='Electronic handpan, voice and electric violin',
        note_fr="Du répertoire de David Lesage, album <i>L'Alliance du Phoenix</i>, repris à deux.",
        note_en="From David Lesage's own repertoire, album <i>L'Alliance du Phoenix</i>, rewritten for two.",
    ),
    dict(
        fichier='02-transe-lunaire.mp3', duree='5:52', secondes=352,
        titre_fr='Transe lunaire', titre_en='Transe lunaire',
        sous_fr='Handpan électronique et violon électrique',
        sous_en='Electronic handpan and electric violin',
        note_fr="Du répertoire de David Lesage, album <i>L'Alliance du Phoenix</i>.",
        note_en="From David Lesage's own repertoire, album <i>L'Alliance du Phoenix</i>.",
    ),
    dict(
        fichier='03-ave-maria.mp3', duree='10:07', secondes=607,
        titre_fr='Ave Maria', titre_en='Ave Maria',
        sous_fr='Violon électrique et handpan électronique',
        sous_en='Electric violin and electronic handpan',
        note_fr='Une pièce du grand répertoire, portée par le violon et posée sur le handpan.',
        note_en='A piece from the classical repertoire, carried by the violin over the handpan.',
    ),
    dict(
        fichier='04-voyage-meditatif-d-kurd.mp3', duree='10:03', secondes=603,
        titre_fr='Voyage méditatif en Ré Kurd',
        titre_en='Meditative journey in D Kurd',
        sous_fr='Improvisation — handpan électronique et violon électrique',
        sous_en='Improvisation — electronic handpan and electric violin',
        note_fr='Ré Kurd : la gamme de handpan la plus jouée au monde. Écrit sur le moment, à deux.',
        note_en='D Kurd: the most widely played handpan scale. Written on the spot, by both.',
    ),
    dict(
        fichier='05-ngoni-violon.mp3', duree='8:56', secondes=536,
        titre_fr='Voyage méditatif — ngoni et violon',
        titre_en='Meditative journey — ngoni and violin',
        sous_fr='Harpe africaine 14 cordes et violon électrique',
        sous_en='14-string African harp and electric violin',
        note_fr="L'instrument le plus ancien du duo face au plus récent. Improvisation.",
        note_en="The duo's oldest instrument against its newest. Improvisation.",
    ),
)

DUREE_TOTALE_MIN = sum(m['secondes'] for m in MORCEAUX) // 60   # 46


# --------------------------------------------------------------------------- #
#  LES PHOTOS  (shooting du 28 aout 2026, Paris)
# --------------------------------------------------------------------------- #
#: ⚠️ CE QUI A ETE RETIRE, ET POURQUOI ON NE LE REMET PAS. David a ecarte le
#: 30/08/2026 `duo-02.jpg`, `duo-03.jpg`, `duo-04.jpg` et le portrait de Lucie
#: (qui reste, lui, la photo de sa fiche). Les fichiers `duo-0*.jpg` ont ete
#: supprimes du depot : plus rien ne les reclame.
GALERIE = (
    ('duo-portrait.jpg', 'Lucie et David Lesage, violon électrique et handpan électronique Neotone',
     'Lucie and David Lesage, electric violin and Neotone electronic handpan'),
    ('regard.jpg', 'Lucie et David Lesage, regard vers le lointain',
     'Lucie and David Lesage, looking into the distance'),
    ('jeu-01.jpg', 'Lucie au violon électrique, David au handpan électronique',
     'Lucie on electric violin, David on electronic handpan'),
    ('sourire.jpg', 'Le duo, Paris, août 2026',
     'The duo, Paris, August 2026'),
    ('jeu-03.jpg', 'Le duo en répétition, Paris, août 2026',
     'The duo rehearsing, Paris, August 2026'),
    ('jeu-02.jpg', 'Handpan électronique et violon électrique, en jeu',
     'Electronic handpan and electric violin, playing'),
    ('jeu-04.jpg', 'Le duo en jeu, handpan électronique et violon électrique',
     'The duo playing, electronic handpan and electric violin'),
    ('instrumentarium-01.jpg', 'Le dispositif au sol, avant la captation',
     'The floor setup, before the recording session'),
)


# --------------------------------------------------------------------------- #
#  LA FEUILLE DE STYLE
# --------------------------------------------------------------------------- #
# Memes variables, memes polices et memes regles que le reste du site (voir
# `sources/theme_chaleur.py`) : bleu nuit, or en accent primaire, prune et
# corail en accents secondaires PAR TOUCHES, aucun emoji, plancher
# typographique 13 px. La page ne partage pas le CSS des autres : elle est
# hors du site et ne doit dependre d'aucun de leurs generateurs.
CSS = """
:root{
  --night:#0e0f24; --night2:#161839; --card:#1e214a;
  --ink:#eae7f3; --muted:#a9a6c4;
  --gold:#d8b25a; --gold2:#f8d274; --plum:#9374e2; --plum2:#b38ff5; --coral:#ee8062;
  --line:rgba(216,178,90,.26);
  --grad:linear-gradient(95deg,var(--gold2),var(--gold) 32%,var(--coral) 66%,var(--plum2));
  --grad-warm:linear-gradient(100deg,var(--gold2),var(--gold) 46%,var(--coral));
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--night);color:var(--ink);
  font-family:'Jost',-apple-system,Segoe UI,Roboto,sans-serif;
  line-height:1.75;font-size:17px;-webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2,h3,h4,.serif{font-family:'Cormorant Garamond',Georgia,serif;font-weight:600}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}

/* les trois halos de fond — comme sur le reste du site */
body::before{content:'';position:fixed;inset:0;z-index:-1;pointer-events:none;
  background:
    radial-gradient(680px 460px at 12% 8%,rgba(216,178,90,.10),transparent 70%),
    radial-gradient(620px 520px at 88% 22%,rgba(147,116,226,.09),transparent 72%),
    radial-gradient(760px 560px at 50% 104%,rgba(238,128,98,.08),transparent 70%)}

.wrap{max-width:1120px;margin:0 auto;padding:0 26px}
section{padding:86px 0;position:relative}
.kick{display:inline-block;letter-spacing:.32em;text-transform:uppercase;
  font-size:13px;font-weight:600;margin-bottom:16px;
  background:var(--grad);-webkit-background-clip:text;background-clip:text;
  -webkit-text-fill-color:transparent;color:transparent}
.sec-title{font-size:clamp(30px,5vw,52px);line-height:1.08;color:#fff}
.lead{font-size:19px;color:var(--muted);max-width:780px;margin-top:18px}
p.body{max-width:820px;color:#d7d4ea;margin-top:16px}
b{color:#fff;font-weight:500}
.divider{height:2px;background:var(--grad);opacity:.5;max-width:1120px;margin:0 auto;
  border-radius:2px}

/* ---------------------------------------------------------------- bandeau */
.topbar{position:fixed;top:0;left:0;right:0;z-index:60;display:flex;
  align-items:center;justify-content:space-between;gap:16px;
  padding:14px 26px;background:rgba(14,15,36,.72);
  backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);
  border-bottom:1px solid rgba(216,178,90,.14)}
.topbar .home{font-size:13px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--muted)}
.topbar .home:hover{color:var(--gold2)}
.langsw{display:flex;border:1px solid rgba(248,210,116,.3);border-radius:40px;
  overflow:hidden;flex:none}
.langsw button{background:transparent;border:0;cursor:pointer;
  font-family:inherit;font-size:12px;font-weight:600;letter-spacing:.16em;
  padding:7px 15px;color:var(--muted)}
.langsw button.on{background:var(--grad-warm);color:#1b1206}

/* ------------------------------------------------------------------ hero */
.hero{position:relative;min-height:100svh;display:flex;align-items:flex-end;
  padding-bottom:76px;overflow:hidden}
.hero-img{position:absolute;inset:0;z-index:-1}
.hero-img img{width:100%;height:100%;object-fit:cover;object-position:50% 32%}
.hero-img::after{content:'';position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(14,15,36,.72) 0%,rgba(14,15,36,.34) 30%,
    rgba(14,15,36,.88) 78%,var(--night) 100%)}
.hero h1{font-size:clamp(44px,8.4vw,104px);line-height:.98;color:#fff;
  letter-spacing:-.01em;margin-top:10px}
.hero h1 .amp{font-style:italic;font-weight:400;
  background:var(--grad);-webkit-background-clip:text;background-clip:text;
  -webkit-text-fill-color:transparent;color:transparent;padding:0 .08em}
.hero .sub{font-size:clamp(18px,2.4vw,23px);color:#e6e2f5;max-width:640px;
  margin-top:22px;line-height:1.55}
/* ⚠️ `>` OBLIGATOIRE. Chaque element bilingue est lui-meme un <span> imbrique
   (voir `_bi()`) : sans le selecteur d'enfant direct, la puce en losange se
   dessinait DEUX fois par entree. */
.hero .meta{margin-top:26px;display:flex;flex-wrap:wrap;gap:10px 26px;
  font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:#c8c4dd}
.hero .meta > span{display:inline-flex;align-items:center;gap:10px}
.hero .meta > span::before{content:'';width:5px;height:5px;flex:none;
  transform:rotate(45deg);background:var(--gold)}
/* Sur une photo claire, un texte au degrade decoupe devient illisible et ne
   peut pas porter d'ombre (le fond du texte EST le degrade). Dans le hero
   seulement, le sur-titre repasse donc en or plein, avec une ombre. */
.hero .kick{-webkit-text-fill-color:initial;color:var(--gold2);
  background:none;text-shadow:0 2px 14px rgba(8,7,20,.85)}
.hero h1,.hero .sub{text-shadow:0 6px 34px rgba(8,7,20,.6)}
.hero .meta{text-shadow:0 2px 12px rgba(8,7,20,.8)}
.cta{display:flex;flex-wrap:wrap;gap:14px;margin-top:34px}
.btn{display:inline-flex;align-items:center;gap:10px;min-height:48px;
  padding:14px 28px;border-radius:40px;font-size:16px;font-weight:600;
  font-family:inherit;cursor:pointer;border:0;
  background:var(--grad-warm);color:#1b1206;
  box-shadow:0 12px 30px -18px rgba(238,128,98,.55)}
.btn.ghost{background:linear-gradient(180deg,rgba(255,255,255,.055),rgba(255,255,255,.02));
  border:1px solid rgba(248,210,116,.3);color:var(--gold2);box-shadow:none}
.btn:hover{filter:brightness(1.07)}

/* ------------------------------------------------------------- 3 piliers */
.piliers{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:44px}
.pilier{background:var(--card);border-radius:18px;padding:30px 26px 28px;
  position:relative;overflow:hidden;border:1px solid rgba(255,255,255,.05)}
.pilier::before{content:'';position:absolute;left:0;top:0;bottom:0;width:3px;
  background:var(--grad)}
.pilier h3{font-size:25px;color:#fff;margin-bottom:10px}
.pilier p{font-size:15.5px;color:var(--muted)}
.pilier .num{font-size:12px;letter-spacing:.3em;color:var(--gold);
  display:block;margin-bottom:14px}

/* -------------------------------------------------------------- ecouteur */
.player{margin-top:40px;background:var(--card);border-radius:20px;
  border:1px solid rgba(255,255,255,.05);overflow:hidden}
.tr{display:grid;grid-template-columns:54px 1fr auto;gap:18px;align-items:center;
  padding:20px 24px;cursor:pointer;border-top:1px solid rgba(255,255,255,.055);
  transition:background .18s}
.tr:first-child{border-top:0}
.tr:hover{background:rgba(255,255,255,.032)}
.tr.on{background:rgba(216,178,90,.08)}
.tr-btn{width:44px;height:44px;border-radius:50%;flex:none;display:grid;
  place-items:center;border:1px solid rgba(248,210,116,.34);color:var(--gold2);
  background:rgba(255,255,255,.03)}
.tr.on .tr-btn{background:var(--grad-warm);color:#1b1206;border-color:transparent}
.tr-btn svg{width:15px;height:15px;fill:currentColor}
.tr h4{font-size:22px;color:#fff;line-height:1.25}
.tr .sous{font-size:14px;color:var(--gold);letter-spacing:.04em;margin-top:2px}
.tr .note{font-size:14.5px;color:var(--muted);margin-top:6px;max-width:62ch}
.tr .dur{font-size:14px;color:var(--muted);font-variant-numeric:tabular-nums;
  letter-spacing:.06em;align-self:start;padding-top:6px}
.player-note{font-size:14.5px;color:var(--muted);margin-top:18px;
  display:flex;gap:12px;align-items:flex-start}
.player-note::before{content:'';width:6px;height:6px;flex:none;margin-top:9px;
  transform:rotate(45deg);background:var(--plum2)}

/* barre de lecture, en bas, une fois qu'on a lance quelque chose */
.bar{position:fixed;left:0;right:0;bottom:0;z-index:70;
  transform:translateY(105%);transition:transform .32s cubic-bezier(.2,.7,.3,1);
  background:rgba(20,22,52,.93);
  backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);
  border-top:1px solid rgba(216,178,90,.22)}
.bar.up{transform:translateY(0)}
.bar-in{max-width:1120px;margin:0 auto;padding:12px 26px 14px;
  display:grid;grid-template-columns:auto 1fr auto;gap:18px;align-items:center}
.bar-play{width:46px;height:46px;border-radius:50%;border:0;flex:none;cursor:pointer;
  display:grid;place-items:center;background:var(--grad-warm);color:#1b1206}
.bar-play svg{width:16px;height:16px;fill:currentColor}
.bar-t{font-size:15px;color:#fff;font-weight:500;white-space:nowrap;
  overflow:hidden;text-overflow:ellipsis}
.bar-time{font-size:13px;color:var(--muted);font-variant-numeric:tabular-nums;
  letter-spacing:.06em;white-space:nowrap}
.seek{-webkit-appearance:none;appearance:none;width:100%;height:20px;
  background:transparent;cursor:pointer;display:block;margin-top:4px}
.seek::-webkit-slider-runnable-track{height:4px;border-radius:4px;
  background:linear-gradient(90deg,var(--gold2) 0%,var(--gold) var(--p,0%),
    rgba(255,255,255,.13) var(--p,0%))}
.seek::-moz-range-track{height:4px;border-radius:4px;background:rgba(255,255,255,.13)}
.seek::-moz-range-progress{height:4px;border-radius:4px;background:var(--gold)}
.seek::-webkit-slider-thumb{-webkit-appearance:none;width:13px;height:13px;
  border-radius:50%;background:var(--gold2);margin-top:-4.5px;
  box-shadow:0 0 0 4px rgba(216,178,90,.22)}
.seek::-moz-range-thumb{width:13px;height:13px;border:0;border-radius:50%;
  background:var(--gold2)}
.bar-skip{display:flex;gap:6px}
.bar-skip button{width:38px;height:38px;border-radius:50%;cursor:pointer;
  background:transparent;border:1px solid rgba(255,255,255,.14);color:var(--muted);
  display:grid;place-items:center}
.bar-skip button:hover{color:var(--gold2);border-color:rgba(248,210,116,.4)}
.bar-skip svg{width:13px;height:13px;fill:currentColor}

/* ------------------------------------------------------------ musiciens */
.deux{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:44px}
.qui{background:var(--card);border-radius:20px;overflow:hidden;
  border:1px solid rgba(255,255,255,.05);display:flex;flex-direction:column}
/* Carré : le portrait officiel de David est carré, celui de Lucie est un
   recadrage vertical. Le décalage vers le haut garde les deux visages dans le
   cadre au lieu de les couper au menton. */
.qui-img{aspect-ratio:1/1;overflow:hidden;background:var(--night2)}
.qui-img img{width:100%;height:100%;object-fit:cover;object-position:50% 26%}
.qui-in{padding:30px 28px 30px;flex:1;display:flex;flex-direction:column}
.qui h3{font-size:32px;color:#fff;line-height:1.1}
.qui .role{font-size:13px;letter-spacing:.24em;text-transform:uppercase;
  color:var(--gold);margin-top:8px}
.qui p{font-size:15.5px;color:#d7d4ea;margin-top:16px}
.faits{list-style:none;margin-top:20px;display:flex;flex-direction:column;gap:9px}
.faits li{font-size:14.5px;color:var(--muted);display:flex;gap:12px;
  align-items:flex-start;line-height:1.6}
.faits li::before{content:'';width:5px;height:5px;flex:none;margin-top:10px;
  transform:rotate(45deg);background:var(--gold)}
.liens{margin-top:auto;padding-top:24px;display:flex;flex-wrap:wrap;gap:8px}
.liens a{font-size:13px;letter-spacing:.08em;padding:7px 15px;border-radius:40px;
  border:1px solid rgba(248,210,116,.26);color:var(--gold2)}
.liens a:hover{background:rgba(216,178,90,.1)}

/* ------------------------------------------------------ photos de section */
/* Une grande image portrait au milieu d'une page en colonnes deborderait en
   hauteur : `max-height` la borne, et `object-fit:cover` recadre plutot que
   de deformer. */
.grande{margin-top:44px;border-radius:20px;overflow:hidden;background:var(--night2);
  border:1px solid rgba(255,255,255,.06)}
.grande img{width:100%;max-height:640px;object-fit:cover;object-position:50% 28%}
.grande figcaption{font-size:13.5px;color:#8b8ba6;padding:14px 22px 16px;
  background:var(--card)}
.deux-photos{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:18px}
.deux-photos figure{border-radius:16px;overflow:hidden;background:var(--night2);
  border:1px solid rgba(255,255,255,.06);display:flex;flex-direction:column}
/* `object-position` bas : sur ces deux photos verticales, ce qu'il faut voir
   (la calebasse au sol, la caisse du ngoni) est dans la MOITIE BASSE. Un
   recadrage centre par defaut coupait justement les instruments. */
/* 2/3 et pas 4/5 : les sources sont des verticales de telephone (9/16). Un
   cadre plus haut montre 84 % de l'image au lieu de 70 %, ce qui suffit a
   garder A LA FOIS les visages en haut et les instruments au sol en bas —
   sans quoi la legende promet une calebasse qu'on ne voit pas. */
.deux-photos img{width:100%;aspect-ratio:2/3;object-fit:cover;object-position:50% 96%}
.deux-photos figcaption{font-size:13.5px;color:var(--muted);padding:13px 18px 15px;
  background:var(--card);flex:1}

/* ------------------------------------------------------------- references */
.refs{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:44px}
.ref-col{background:var(--card);border-radius:20px;padding:30px 28px;
  border:1px solid rgba(255,255,255,.05)}
.ref-col h3{font-size:24px;color:#fff}
.ref-col .who{font-size:12.5px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--plum2);margin-top:6px;margin-bottom:20px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
/* Des noms de tiers : jamais de logo (marques deposees), jamais cliquable —
   ce sont des references, pas des partenariats a suggerer. */
.chip{font-size:14px;line-height:1.2;padding:8px 14px;border-radius:40px;
  color:#ded9f0;background:linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,.02));
  border:1px solid rgba(255,255,255,.1)}
.ref-note{font-size:13px;color:#8b8ba6;margin-top:18px}
/* Le panneau clair qui porte la planche de logos. Les logos sont polychromes
   et concus pour du blanc : les poser sur le bleu nuit les salirait. Un
   panneau blanc franc, c'est le geste d'un dossier de presse. */
.logos{background:#fff;border-radius:14px;padding:18px 16px;
  box-shadow:0 18px 40px -26px rgba(0,0,0,.8)}
.logos img{width:100%;height:auto;display:block}

/* -------------------------------------------------------- instrumentarium */
.instr{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:44px}
.instr-col{background:var(--card);border-radius:20px;padding:30px 28px;
  border:1px solid rgba(255,255,255,.05)}
.instr-col h3{font-size:24px;color:#fff}
.instr-col .who{font-size:12.5px;letter-spacing:.24em;text-transform:uppercase;
  color:var(--plum2);margin-top:6px;margin-bottom:18px}
.instr-col ul{list-style:none;display:flex;flex-direction:column;gap:10px}
.instr-col li{font-size:15px;color:var(--muted);display:flex;gap:12px;
  align-items:flex-start;line-height:1.55}
.instr-col li::before{content:'';width:5px;height:5px;flex:none;margin-top:9px;
  transform:rotate(45deg);background:var(--coral)}
.instr-col li b{color:#fff;font-weight:500}

/* ------------------------------------------------------------- carrousel */
.carrousel{position:relative;margin-top:44px}
.piste{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;
  scroll-behavior:smooth;gap:0;border-radius:20px;
  scrollbar-width:none;-ms-overflow-style:none}
.piste::-webkit-scrollbar{display:none}
.piste:focus-visible{outline:2px solid var(--gold2);outline-offset:3px}
.slide{position:relative;flex:0 0 100%;scroll-snap-align:center;
  background:var(--night2);overflow:hidden;isolation:isolate}
/* Le fond : la meme image, floutee et assombrie, pour habiller les bandes
   laterales des photos verticales sans jamais les recadrer. */
.slide-fond{position:absolute;inset:0;z-index:-1;background-size:cover;
  background-position:center;filter:blur(34px) brightness(.42) saturate(.9);
  transform:scale(1.15)}
.slide img{width:100%;height:min(62vh,620px);object-fit:contain;display:block}
.slide figcaption{font-size:13.5px;color:#cfcbe4;padding:14px 22px 16px;
  background:rgba(10,11,30,.72);backdrop-filter:blur(8px);text-align:center}
.fleche{position:absolute;top:calc(50% - 30px);transform:translateY(-50%);
  width:46px;height:46px;border-radius:50%;cursor:pointer;z-index:3;
  display:grid;place-items:center;border:1px solid rgba(248,210,116,.32);
  background:rgba(10,11,30,.66);color:var(--gold2);
  backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
.fleche:hover{background:rgba(216,178,90,.18)}
.fleche svg{width:15px;height:15px;fill:currentColor}
.fleche.prec{left:14px}
.fleche.suiv{right:14px}
.puces{display:flex;justify-content:center;gap:9px;margin-top:20px;flex-wrap:wrap}
.puce{width:9px;height:9px;padding:0;border-radius:50%;cursor:pointer;
  border:0;background:rgba(255,255,255,.22)}
.puce.on{background:var(--grad-warm);transform:scale(1.25)}

/* ---------------------------------------------------------------- contact */
.contact{background:var(--card);border-radius:22px;padding:46px 40px;
  border:1px solid rgba(255,255,255,.05);position:relative;overflow:hidden;
  margin-top:40px}
.contact::before{content:'';position:absolute;left:0;right:0;top:0;height:3px;
  background:var(--grad)}
.ct-grid{display:grid;grid-template-columns:1fr auto;gap:36px;align-items:center}
.ct-l{font-size:13px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);
  display:block;margin-bottom:6px}
/* ⚠️ `overflow-wrap`: l'adresse de courriel fait 33 caracteres sans espace et
   depassait du cadre sur telephone (masquee par `overflow-x:hidden`, donc
   invisible a la mesure : elle ne se voyait qu'a l'oeil). */
.ct-v{font-size:21px;color:#fff;overflow-wrap:anywhere}
.ct-v a:hover{color:var(--gold2)}
.ct-rows{display:flex;flex-direction:column;gap:22px}
.legal{font-size:13.5px;color:#8b8ba6;margin-top:26px;line-height:1.7}

footer{padding:52px 0 40px;text-align:center;background:#08091a;
  border-top:1px solid rgba(216,178,90,.14)}
footer p{font-size:13.5px;color:#8b8ba6}
footer a{color:var(--gold2)}
.pad-bar{height:0;transition:height .32s}
.pad-bar.up{height:86px}

/* ---------------------------------------------------------------- langues */
body.fr [data-lang="en"]{display:none}
body.en [data-lang="fr"]{display:none}

@media (max-width:900px){
  .piliers{grid-template-columns:1fr}
  .deux,.instr,.refs,.deux-photos{grid-template-columns:1fr}
  .grande img{max-height:420px}
  .gal{columns:2}
  .ct-grid{grid-template-columns:1fr;gap:26px}
  section{padding:64px 0}
  .contact{padding:34px 24px}
}
@media (max-width:620px){
  .gal{columns:1}
  /* Cadre CARRE sur telephone. Le cadre haut du bureau (62 vh) laissait, sur
     une photo horizontale en 375 px de large, deux bandes vides de plus d'un
     tiers de la hauteur. Un carre est le seul format qui traite correctement
     les deux orientations du lot : une horizontale y fait 375x211, une
     verticale 211x375 — aucune des deux n'est minuscule, aucune n'est rognee. */
  .slide img{height:auto;aspect-ratio:1/1}
  .fleche{width:40px;height:40px}
  .fleche.prec{left:8px}
  .fleche.suiv{right:8px}
  .topbar{padding:11px 16px}
  .topbar .home{font-size:11px;letter-spacing:.12em}
  .ct-v{font-size:17.5px}
  .tr{grid-template-columns:44px 1fr;gap:14px;padding:18px 18px}
  .tr .dur{grid-column:2;padding-top:0}
  .bar-in{grid-template-columns:auto 1fr;gap:14px;padding:10px 18px 12px}
  .bar-skip{display:none}
  .hero{padding-bottom:56px}
}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  *{transition:none!important}
}
"""


# --------------------------------------------------------------------------- #
#  PETITES ICONES — dessinees, jamais un emoji (regle du site)
# --------------------------------------------------------------------------- #
I_PLAY = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 1.6v12.8L14 8z"/></svg>'
I_PAUSE = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2.6 1.5h3.7v13H2.6zM9.7 1.5h3.7v13H9.7z"/></svg>'
I_PREV = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M13.4 2v12L4.6 8zM2.2 2h1.9v12H2.2z"/></svg>'
I_NEXT = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2.6 2v12L11.4 8zM11.9 2h1.9v12h-1.9z"/></svg>'


def _bi(fr, en):
    """Un bloc en deux langues. L'une des deux est masquee par le CSS."""
    return '<span data-lang="fr">%s</span><span data-lang="en">%s</span>' % (fr, en)


# --------------------------------------------------------------------------- #
#  LES MORCEAUX, EN HTML
# --------------------------------------------------------------------------- #
def _morceaux_html():
    out = []
    for i, m in enumerate(MORCEAUX):
        out.append(
            '<div class="tr" data-i="%d" data-src="media/audio/%s" '
            'data-titre-fr="%s" data-titre-en="%s" role="button" tabindex="0" '
            'aria-label="%s">'
            '<span class="tr-btn">%s</span>'
            '<div>'
            '<h4>%s</h4>'
            '<div class="sous">%s</div>'
            '<div class="note">%s</div>'
            '</div>'
            '<div class="dur">%s</div>'
            '</div>' % (
                i, m['fichier'],
                m['titre_fr'].replace('"', '&quot;'), m['titre_en'].replace('"', '&quot;'),
                m['titre_fr'].replace('"', '&quot;'),
                I_PLAY,
                _bi(m['titre_fr'], m['titre_en']),
                _bi(m['sous_fr'], m['sous_en']),
                _bi(m['note_fr'], m['note_en']),
                m['duree'],
            ))
    return '\n'.join(out)


def _galerie_html():
    """Le carrousel de la galerie.

    ⚠️ POURQUOI `object-fit:contain` ET UN FOND FLOU. Les photos viennent de
       deux appareils : les Canon sont horizontales, les iPhone verticales. Un
       `cover` dans un cadre unique amputerait les verticales de moitie. On
       affiche donc l'image ENTIERE, et on remplit le vide avec la meme image
       floutee et assombrie — le cadre reste stable d'une photo a l'autre sans
       rien couper.
    ⚠️ Il defile aussi SANS JAVASCRIPT : la piste est un conteneur a
       defilement horizontal avec accroche. Les fleches et les puces ne font
       qu'ajouter du confort.
    """
    out = []
    for i, (fichier, alt_fr, alt_en) in enumerate(GALERIE):
        out.append(
            '      <figure class="slide" aria-roledescription="slide" '
            'aria-label="%d / %d">'
            '<span class="slide-fond" style="background-image:url(media/photos/%s)"></span>'
            '<img src="media/photos/%s" loading="%s" alt="%s">'
            '<figcaption>%s</figcaption>'
            '</figure>'
            % (i + 1, len(GALERIE), fichier, fichier,
               'eager' if i == 0 else 'lazy',
               alt_fr.replace('"', '&quot;'),
               _bi(alt_fr, alt_en)))
    return '\n'.join(out)


def _puces_html():
    return '\n'.join(
        '      <button type="button" class="puce" data-i="%d" '
        'aria-label="Photo %d"></button>' % (i, i + 1)
        for i in range(len(GALERIE)))


# --------------------------------------------------------------------------- #
#  LE JAVASCRIPT — bascule de langue + lecteur
# --------------------------------------------------------------------------- #
JS = """
(function(){
  'use strict';
  var PLAY  = '__ICO_PLAY__';
  var PAUSE = '__ICO_PAUSE__';

  /* ---------------------------------------------------------- la langue */
  /* La page s'ouvre en francais. Si le navigateur du visiteur n'est pas
     francophone, elle s'ouvre en anglais : une agence etrangere ne doit pas
     avoir a chercher le bouton. Le choix explicite, lui, est retenu. */
  var body = document.body, boutons = document.querySelectorAll('.langsw button');
  function langue(l, memoriser){
    body.classList.remove('fr','en'); body.classList.add(l);
    document.documentElement.lang = l;
    boutons.forEach(function(b){ b.classList.toggle('on', b.dataset.l === l); });
    document.querySelectorAll('[data-titre-fr]').forEach(function(t){
      t.setAttribute('aria-label', t.dataset['titre' + (l === 'fr' ? 'Fr' : 'En')]);
    });
    if (memoriser) { try { localStorage.setItem('duo-lang', l); } catch(e){} }
    if (courant >= 0) nomBarre();
  }
  var choisi = null;
  try { choisi = localStorage.getItem('duo-lang'); } catch(e){}
  var auto = (navigator.language || 'fr').toLowerCase().indexOf('fr') === 0 ? 'fr' : 'en';
  boutons.forEach(function(b){
    b.addEventListener('click', function(){ langue(b.dataset.l, true); });
  });

  /* ---------------------------------------------------------- le lecteur */
  var audio = new Audio();
  audio.preload = 'none';
  var pistes  = [].slice.call(document.querySelectorAll('.tr'));
  var barre   = document.querySelector('.bar');
  var pad     = document.querySelector('.pad-bar');
  var bPlay   = document.querySelector('.bar-play');
  var bTitre  = document.querySelector('.bar-t');
  var bTemps  = document.querySelector('.bar-time');
  var seek    = document.querySelector('.seek');
  var courant = -1, glisse = false;

  function mmss(s){
    if (!isFinite(s) || s < 0) s = 0;
    var m = Math.floor(s / 60), r = Math.floor(s % 60);
    return m + ':' + (r < 10 ? '0' : '') + r;
  }
  function nomBarre(){
    var l = body.classList.contains('en') ? 'En' : 'Fr';
    bTitre.textContent = pistes[courant].dataset['titre' + l];
  }
  function icones(){
    pistes.forEach(function(t, i){
      var joue = (i === courant && !audio.paused);
      t.classList.toggle('on', i === courant);
      t.querySelector('.tr-btn').innerHTML = joue ? PAUSE : PLAY;
    });
    bPlay.innerHTML = audio.paused ? PLAY : PAUSE;
    bPlay.setAttribute('aria-label', audio.paused ? 'Lecture' : 'Pause');
  }
  /* `play()` rend une promesse qui ECHOUE si le navigateur refuse la lecture
     (onglet muet, economie de donnees, geste non reconnu). Sans ce `catch`,
     l'echec remonte en erreur non capturee dans la console du visiteur. */
  function lire(){
    var p = audio.play();
    if (p && p.catch) p.catch(function(){});
  }
  function bascule(){ audio.paused ? lire() : audio.pause(); }

  function jouer(i){
    if (i === courant) { bascule(); return; }
    courant = i;
    audio.src = pistes[i].dataset.src;
    lire();
    nomBarre();
    barre.classList.add('up'); pad.classList.add('up');
    seek.value = 0; seek.style.setProperty('--p', '0%');
  }

  pistes.forEach(function(t, i){
    t.addEventListener('click', function(){ jouer(i); });
    t.addEventListener('keydown', function(e){
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); jouer(i); }
    });
  });
  bPlay.addEventListener('click', function(){
    if (courant < 0) { jouer(0); return; }
    bascule();
  });
  document.querySelector('.b-prev').addEventListener('click', function(){
    jouer((courant - 1 + pistes.length) % pistes.length);
  });
  document.querySelector('.b-next').addEventListener('click', function(){
    jouer((courant + 1) % pistes.length);
  });

  audio.addEventListener('play', icones);
  audio.addEventListener('pause', icones);
  audio.addEventListener('ended', function(){
    if (courant < pistes.length - 1) jouer(courant + 1); else icones();
  });
  audio.addEventListener('timeupdate', function(){
    if (glisse || !isFinite(audio.duration)) return;
    var p = audio.currentTime / audio.duration * 100;
    seek.value = p; seek.style.setProperty('--p', p + '%');
    bTemps.textContent = mmss(audio.currentTime) + ' / ' + mmss(audio.duration);
  });
  seek.addEventListener('input', function(){
    glisse = true; seek.style.setProperty('--p', seek.value + '%');
    if (isFinite(audio.duration))
      bTemps.textContent = mmss(audio.duration * seek.value / 100) + ' / ' + mmss(audio.duration);
  });
  seek.addEventListener('change', function(){
    if (isFinite(audio.duration)) audio.currentTime = audio.duration * seek.value / 100;
    glisse = false;
  });

  langue(choisi || auto, false);
  icones();

  /* --------------------------------------------------------- le carrousel */
  /* La piste defile deja toute seule (scroll-snap) : ce bloc n'ajoute que les
     fleches, les puces et le clavier. Si le script tombe, on peut encore
     faire defiler a la main — c'est voulu. */
  var piste = document.querySelector('.piste');
  if (piste) {
    var slides = [].slice.call(piste.querySelectorAll('.slide'));
    var puces  = [].slice.call(document.querySelectorAll('.puce'));

    /* ⚠️ UN INDEX EXPLICITE, ET PAS `scrollLeft`. Deduire la position courante
       du defilement paraissait plus simple, mais le defilement est ANIME :
       deux clics rapprochés lisaient tous les deux une position intermediaire
       et demandaient la meme diapositive — le second clic ne servait a rien.
       L'index est donc tenu a part ; `scrollLeft` ne sert plus qu'a se
       resynchroniser quand c'est le doigt qui a fait defiler. */
    var idx = 0, minuteur;

    function majPuces(){
      puces.forEach(function(p, i){ p.classList.toggle('on', i === idx); });
    }
    function versSlide(i){
      idx = Math.max(0, Math.min(slides.length - 1, i));
      piste.scrollTo({left: idx * piste.clientWidth, behavior: 'smooth'});
      majPuces();
    }
    document.querySelector('.prec').addEventListener('click', function(){
      versSlide(idx - 1);
    });
    document.querySelector('.suiv').addEventListener('click', function(){
      versSlide(idx + 1);
    });
    puces.forEach(function(p){
      p.addEventListener('click', function(){ versSlide(+p.dataset.i); });
    });
    piste.addEventListener('keydown', function(e){
      if (e.key === 'ArrowRight') { e.preventDefault(); versSlide(idx + 1); }
      if (e.key === 'ArrowLeft')  { e.preventDefault(); versSlide(idx - 1); }
    });
    piste.addEventListener('scroll', function(){
      clearTimeout(minuteur);
      minuteur = setTimeout(function(){
        idx = Math.round(piste.scrollLeft / piste.clientWidth);
        majPuces();
      }, 140);
    });
    window.addEventListener('resize', function(){
      piste.scrollTo({left: idx * piste.clientWidth, behavior: 'auto'});
    });
    majPuces();
  }

  /* Le lien « Ecouter » du hero lance la premiere piste apres le defilement. */
  var ecouter = document.querySelector('.js-ecouter');
  if (ecouter) ecouter.addEventListener('click', function(){
    if (courant < 0) setTimeout(function(){ jouer(0); }, 620);
  });
})();
"""


# --------------------------------------------------------------------------- #
#  LA PAGE
# --------------------------------------------------------------------------- #
def page():
    h = []
    a = h.append

    a('<!DOCTYPE html>')
    a('<html lang="fr">')
    a('<head>')
    a('<meta charset="utf-8">')
    a('<meta name="viewport" content="width=device-width,initial-scale=1">')
    # ⚠️ LES DEUX VERROUS. robots.txt empeche l'exploration ; cette balise
    #    empeche l'indexation d'une adresse qu'un moteur aurait apprise
    #    autrement (un lien dans un mail, une barre d'adresse partagee).
    a('<meta name="robots" content="noindex, nofollow, noarchive, noimageindex">')
    a('<title>Lucie &amp; David Lesage — violon électrique &amp; handpan électronique</title>')
    a('<meta name="description" content="Duo en émergence : handpan électronique, '
      'ngoni, voix et violon électrique. Cinq pièces enregistrées à Paris le 28 août 2026.">')
    a('<meta property="og:type" content="website">')
    a('<meta property="og:title" content="Lucie &amp; David Lesage">')
    a('<meta property="og:description" content="Violon électrique et handpan électronique. '
      'Duo en émergence, Paris.">')
    a('<meta property="og:image" content="%s/media/photos/og-duo.jpg">' % URL)
    a('<meta property="og:url" content="%s">' % URL)
    a('<meta name="twitter:card" content="summary_large_image">')
    a('<link rel="icon" href="/favicon.svg" type="image/svg+xml">')
    a('<link rel="apple-touch-icon" href="/apple-touch-icon.png">')
    a('<link rel="preconnect" href="https://fonts.googleapis.com">')
    a('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    a('<link href="https://fonts.googleapis.com/css2?'
      'family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&'
      'family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">')
    a('<style>%s</style>' % CSS)
    a('</head>')
    a('<body class="fr">')

    # ------------------------------------------------------------- bandeau
    a('<div class="topbar">')
    a('  <a class="home" href="/">Résonances Productions</a>')
    a('  <div class="langsw" role="group" aria-label="Langue / Language">')
    a('    <button type="button" data-l="fr">FR</button>')
    a('    <button type="button" data-l="en">EN</button>')
    a('  </div>')
    a('</div>')

    # ---------------------------------------------------------------- hero
    a('<header class="hero">')
    a('  <div class="hero-img"><img src="media/photos/hero.jpg" '
      'alt="David Lesage au handpan électronique et Lucie au violon électrique"></div>')
    a('  <div class="wrap">')
    a('    <span class="kick">%s</span>' % _bi(
        'Duo en émergence &middot; Paris &middot; 2026',
        'Emerging duo &middot; Paris &middot; 2026'))
    # Ordre des deux noms : LUCIE D'ABORD, demande de David le 30/08/2026.
    # Les fiches et les colonnes de references suivent le meme ordre — un titre
    # qui annonce un ordre et une page qui en applique un autre se lit comme un
    # oubli.
    a('    <h1>Lucie<span class="amp">&amp;</span>David Lesage</h1>')
    a('    <p class="sub">%s</p>' % _bi(
        'Un handpan électronique et un violon électrique. Deux instruments qui '
        'n&rsquo;existaient pas il y a quinze ans, au service de gestes qui, eux, '
        'sont très anciens.',
        'An electronic handpan and an electric violin. Two instruments that did not '
        'exist fifteen years ago, in the service of gestures that are very old indeed.'))
    a('    <div class="meta">')
    a('      <span>%s</span>' % _bi('Handpan électronique &middot; ngoni &middot; voix',
                                    'Electronic handpan &middot; ngoni &middot; voice'))
    a('      <span>%s</span>' % _bi('Violon électrique &middot; violon acoustique',
                                    'Electric violin &middot; acoustic violin'))
    a('      <span>%s</span>' % _bi('Cinq pièces &middot; %d minutes' % DUREE_TOTALE_MIN,
                                    'Five pieces &middot; %d minutes' % DUREE_TOTALE_MIN))
    a('    </div>')
    a('    <div class="cta">')
    a('      <a class="btn js-ecouter" href="#ecouter">%s</a>'
      % _bi('Écouter les cinq pièces', 'Listen to the five pieces'))
    a('      <a class="btn ghost" href="#contact">%s</a>'
      % _bi('Contact &amp; booking', 'Contact &amp; booking'))
    a('    </div>')
    a('  </div>')
    a('</header>')

    # -------------------------------------------------------------- le duo
    a('<section id="duo"><div class="wrap">')
    a('  <span class="kick">%s</span>' % _bi('Ce que c&rsquo;est', 'What this is'))
    a('  <h2 class="sec-title">%s</h2>' % _bi(
        'Deux musiciens qui ont électrifié<br>un instrument ancestral',
        'Two musicians who electrified<br>an ancestral instrument'))
    a('  <p class="lead">%s</p>' % _bi(
        'Lui joue du handpan &mdash; un instrument né en 2000, en tôle martelée &mdash; '
        'dans sa version numérique. Elle joue du violon &mdash; un instrument né au '
        'XVI<sup>e</sup> siècle &mdash; dans sa version électrique. Chacun est arrivé de '
        'son côté au même endroit : un instrument acoustique, et son double branché. '
        'Le duo est né de cette symétrie.',
        'He plays the handpan &mdash; an instrument born in 2000, from hammered steel &mdash; '
        'in its digital form. She plays the violin &mdash; born in the 16th century &mdash; '
        'in its electric form. Each arrived from a different direction at the same place: '
        'an acoustic instrument, and its plugged-in twin. The duo grew out of that symmetry.'))
    a('  <div class="piliers">')

    piliers = (
        ('01',
         'Moderne et ancestral, sans choisir',
         'Modern and ancestral, without choosing',
         'Une harpe africaine à quatorze cordes et une calebasse à côté d&rsquo;un handpan '
         'numérique et d&rsquo;une station de bouclage. Rien n&rsquo;est cité : tout est joué, '
         'en direct, sans bande.',
         'A fourteen-string African harp and a calabash next to a digital handpan and a '
         'loop station. Nothing is sampled in advance: everything is played live, no backing track.'),
        ('02',
         'Deux mondes professionnels qui se rencontrent',
         'Two professional worlds meeting',
         'La scène de festival et de cérémonie d&rsquo;un côté, l&rsquo;événementiel haut de '
         'gamme et les marques de luxe de l&rsquo;autre. Le duo peut tenir les deux plateaux.',
         'Festival and ceremony stages on one side; high-end corporate events and luxury '
         'brands on the other. The duo can hold either room.'),
        ('03',
         'Un dispositif léger, un rendu large',
         'A light setup, a wide sound',
         'Deux musiciens, deux instruments principaux, aucune batterie à installer. '
         'La densité vient du bouclage en direct et du jeu, pas du nombre de personnes '
         'sur le plateau.',
         'Two musicians, two main instruments, no drum kit to install. The density comes '
         'from live looping and from playing, not from the number of people on stage.'),
    )
    for num, tfr, ten, pfr, pen in piliers:
        a('    <div class="pilier">')
        a('      <span class="num">%s</span>' % num)
        a('      <h3>%s</h3>' % _bi(tfr, ten))
        a('      <p>%s</p>' % _bi(pfr, pen))
        a('    </div>')
    a('  </div>')
    # La photo qui dit ce que le texte ne peut pas dire : ils se regardent.
    a('  <figure class="grande">')
    a('    <img src="media/photos/complicite.jpg" loading="lazy" '
      'alt="David Lesage et Lucie se regardent pendant la captation">')
    a('    <figcaption>%s</figcaption>' % _bi(
        'Première journée d&rsquo;enregistrement, Paris, 28 août 2026.',
        'First recording day, Paris, 28 August 2026.'))
    a('  </figure>')
    a('</div></section>')

    a('<div class="divider"></div>')

    # ------------------------------------------------------------- ecouter
    a('<section id="ecouter"><div class="wrap">')
    a('  <span class="kick">%s</span>' % _bi('Écouter', 'Listen'))
    a('  <h2 class="sec-title">%s</h2>' % _bi(
        'Cinq pièces, enregistrées le 28 août 2026',
        'Five pieces, recorded on 28 August 2026'))
    a('  <figure class="grande">')
    a('    <img src="media/photos/duo-large.jpg" loading="lazy" '
      'alt="Lucie au violon électrique et David Lesage au handpan électronique Neotone">')
    a('    <figcaption>%s</figcaption>' % _bi(
        'Lucie et David Lesage &mdash; violon électrique Yamaha et handpan électronique '
        'Neotone.',
        'Lucie and David Lesage &mdash; Yamaha electric violin and Neotone electronic '
        'handpan.'))
    a('  </figure>')
    a('  <p class="lead" style="margin-top:26px">%s</p>' % _bi(
        'Une seule journée, à Paris. Prise de son en direct : sortie de console et '
        'micro d&rsquo;ambiance, sans retouche ni réenregistrement. C&rsquo;est '
        'littéralement ce que le duo joue dans une pièce.',
        'A single day, in Paris. Live recording: desk output plus a room microphone, '
        'with no overdubs and no fixing. This is literally what the duo sounds like in a room.'))
    a('  <div class="player">')
    a(_morceaux_html())
    a('  </div>')
    a('  <p class="player-note">%s</p>' % _bi(
        'La captation vidéo multicaméra de cette même journée existe : le montage '
        'est en cours. Les rushes sont disponibles sur demande.',
        'The multi-camera video of that same day exists; the edit is in progress. '
        'Raw footage is available on request.'))
    a('</div></section>')

    a('<div class="divider"></div>')

    # ----------------------------------------------------------- musiciens
    a('<section id="musiciens"><div class="wrap">')
    a('  <span class="kick">%s</span>' % _bi('Les deux musiciens', 'The two musicians'))
    a('  <h2 class="sec-title">%s</h2>' % _bi('Qui joue', 'Who plays'))
    a('  <div class="deux">')

    # -- Lucie
    # ⚠️ Son nom de famille n'est PAS ecrit ici : voir l'en-tete du fichier.
    a('    <article class="qui">')
    a('      <div class="qui-img"><img src="media/photos/lucie.jpg" loading="lazy" '
      'alt="Lucie, violoniste électrique"></div>')
    a('      <div class="qui-in">')
    a('        <h3>Lucie</h3>')
    a('        <div class="role">%s</div>' % _bi(
        'Violon électrique &middot; violon acoustique &middot; violon LED',
        'Electric violin &middot; acoustic violin &middot; LED violin'))
    a('        <p>%s</p>' % _bi(
        'Vingt ans de scène, et une spécialité rare : elle est la violoniste que les '
        'grandes maisons appellent quand une soirée doit être mémorable. Airbus, Google, '
        'Chanel, Dior, Louis Vuitton, Moët &amp; Chandon, Patek Philippe l&rsquo;ont fait '
        'jouer. <b>Ses trois terrains</b> : l&rsquo;événementiel haut de gamme et les '
        'marques de luxe, où elle sait tenir une salle sans la couvrir ; le classique, '
        'qu&rsquo;elle a appris au Conservatoire à Paris puis à Londres, diplôme de '
        'performance de l&rsquo;Associated Board of the Royal Schools of Music en violon '
        '<i>et</i> en chant lyrique ; et la scène pop et rock, aux côtés de Lara Fabian, '
        'Florent Pagny ou Johnny Hallyday. Elle a aussi fondé et dirige Les Muses, premier '
        'quatuor de violons électriques féminin en France.',
        'Twenty years on stage, and a rare specialism: she is the violinist the great '
        'houses call when an evening has to be remembered. Airbus, Google, Chanel, Dior, '
        'Louis Vuitton, Moët &amp; Chandon and Patek Philippe have all hired her. '
        '<b>Her three grounds</b>: high-end corporate events and luxury brands, where she '
        'knows how to hold a room without drowning it; classical music, learned at the '
        'Paris Conservatoire and then in London, with an Associated Board of the Royal '
        'Schools of Music performance diploma in violin <i>and</i> in classical singing; '
        'and the pop and rock stage, alongside Lara Fabian, Florent Pagny and Johnny '
        'Hallyday. She also founded and runs Les Muses, France&rsquo;s first all-female '
        'electric string quartet.'))
    a('        <ul class="faits">')
    faits_l = (
        ('A accompagné sur scène Lara Fabian, Florent Pagny, Johnny Hallyday, Christophe',
         'Has performed on stage with Lara Fabian, Florent Pagny, Johnny Hallyday, Christophe'),
        ('Première partie, en duo, de la tournée <i>The Live Experience</i> d&rsquo;ERA '
         'dans les Zéniths de France, de Belgique et de Suisse',
         'Opened, as a duo, for ERA&rsquo;s <i>The Live Experience</i> tour in arenas across '
         'France, Belgium and Switzerland'),
        ('Membre du London Philharmonic Choir et du London Philharmonic Youth Orchestra ; '
         'Royal Albert Hall, Barbican, Royal Festival Hall',
         'Member of the London Philharmonic Choir and London Philharmonic Youth Orchestra; '
         'Royal Albert Hall, Barbican, Royal Festival Hall'),
        ('A joué sous la direction de Kurt Masur et de Pierre Boulez',
         'Has played under Kurt Masur and Pierre Boulez'),
        ('Artiste Yamaha : elle joue un violon électrique Yamaha YEV-205',
         'Yamaha artist: she plays a Yamaha YEV-205 electric violin'),
        ('Expérience internationale : Paris, Séoul, Londres, Genève, Las Vegas',
         'International experience: Paris, Seoul, London, Geneva, Las Vegas'),
        ('Également coach holistique pour artistes et musiciens',
         'Also a holistic coach for artists and musicians'),
    )
    for fr, en in faits_l:
        a('          <li>%s</li>' % _bi(fr, en))
    a('        </ul>')
    a('        <div class="liens">')
    a('          <a href="https://www.violonisteelectrique.com/" target="_blank" '
      'rel="noopener">violonisteelectrique.com</a>')
    a('          <a href="https://www.quatuorlesmuses.com/" target="_blank" '
      'rel="noopener">Quatuor Les Muses</a>')
    a('          <a href="https://www.instagram.com/lucie_electric_violinist_paris/" '
      'target="_blank" rel="noopener">Instagram</a>')
    a('          <a href="https://www.youtube.com/@QuatuorLesMuses" '
      'target="_blank" rel="noopener">YouTube</a>')
    a('        </div>')
    a('      </div>')
    a('    </article>')

    # -- David
    a('    <article class="qui">')
    # Portrait officiel (celui de /rituals), et non une photo du shooting : la
    # carte doit montrer le musicien seul, pas le duo.
    a('      <div class="qui-img"><img src="media/photos/david.webp" loading="lazy" '
      'alt="Portrait de David Lesage"></div>')
    a('      <div class="qui-in">')
    a('        <h3>David Lesage</h3>')
    a('        <div class="role">%s</div>' % _bi(
        'Handpan électronique &middot; ngoni &middot; calebasse &middot; voix',
        'Electronic handpan &middot; ngoni &middot; calabash &middot; voice'))
    a('        <p>%s</p>' % _bi(
        'Percussionniste de formation classique devenu l&rsquo;un des rares musiciens à '
        'jouer le handpan électronique sur scène. Il vient du jazz &mdash; quatre ans au '
        'collège de jazz de Marciac, quatre ans au Conservatoire de Toulouse, prix de '
        'batterie &mdash; et en a gardé un sens du rythme millimétré, qu&rsquo;il applique '
        'aujourd&rsquo;hui à des instruments qui n&rsquo;ont pas de partition. '
        '<b>Ses trois terrains</b> : le handpan, acoustique et numérique, dont il est '
        'ambassadeur officiel de la marque Neotone ; la voix, cinq octaves, en cinq '
        'langues ; et les instruments à peau et à cordes d&rsquo;Afrique de l&rsquo;Ouest. '
        'Ses instruments sont accordés en <b>La 432 Hz</b> &mdash; une couleur, pas un '
        'dogme : le duo se joue aussi en 440.',
        'A classically trained percussionist who became one of the very few musicians '
        'playing the electronic handpan on stage. He comes from jazz &mdash; four years at '
        'the Marciac jazz college, four years at the Toulouse Conservatoire, with a '
        'drumming prize &mdash; and kept from it a millimetric sense of rhythm, which he now '
        'applies to instruments that have no written score. <b>His three grounds</b>: the '
        'handpan, acoustic and digital, for which he is an official Neotone ambassador; '
        'the voice, five octaves across five languages; and the skin and string '
        'instruments of West Africa. His instruments are tuned to <b>A 432 Hz</b> '
        '&mdash; a colour, not a doctrine: the duo plays at 440 just as happily.'))
    a('        <ul class="faits">')
    faits_d = (
        ('Sept pays de scène : France, Hongrie, Suisse, Belgique, Grèce, Espagne, '
         'Côte d&rsquo;Ivoire',
         'Seven countries on stage: France, Hungary, Switzerland, Belgium, Greece, Spain, '
         'Ivory Coast'),
        ('Le Grand Rex, Paris, devant 2 700 personnes',
         'Le Grand Rex, Paris, in front of 2,700 people'),
        ('Sziget Festival, Budapest, en 2022 et 2023 ; Everness Festival, Hongrie',
         'Sziget Festival, Budapest, in 2022 and 2023; Everness Festival, Hungary'),
        ('Vingt et une dates à Jazz in Marciac, sur sept éditions',
         'Twenty-one dates at Jazz in Marciac, over seven editions'),
        ('Première partie d&rsquo;Amadou &amp; Mariam, septembre 2022',
         'Opening for Amadou &amp; Mariam, September 2022'),
        ('The Voice saison 11 (TF1), diffusé le 12 février 2022',
         'The Voice season 11 (TF1, France), broadcast 12 February 2022'),
        ('Ambassadeur officiel et bêta-testeur du handpan électronique Neotone depuis 2023',
         'Official ambassador and beta-tester of the Neotone electronic handpan since 2023'),
    )
    for fr, en in faits_d:
        a('          <li>%s</li>' % _bi(fr, en))
    a('        </ul>')
    a('        <div class="liens">')
    a('          <a href="https://www.resonancesproductions.org/david-lesage-en-concert" '
      'target="_blank" rel="noopener">Biographie complète</a>')
    a('          <a href="https://lesagedavid.fr" target="_blank" rel="noopener">lesagedavid.fr</a>')
    a('          <a href="https://www.youtube.com/@DavidLesageArtiste" '
      'target="_blank" rel="noopener">YouTube</a>')
    a('          <a href="https://www.instagram.com/david.lesage.artiste/" '
      'target="_blank" rel="noopener">Instagram</a>')
    a('        </div>')
    a('      </div>')
    a('    </article>')

    a('  </div>')
    a('</div></section>')

    a('<div class="divider"></div>')

    # ------------------------------------------------------------ references
    # ⚠️ DEUX COLONNES SEPAREES, ET C'EST LE POINT. Les scenes sont celles de
    #    David, les marques sont celles de Lucie : melanger les deux listes
    #    ferait croire que chacun a fait ce que l'autre a fait. Les marques sont
    #    reprises telles qu'elles figurent sur le site de Lucie
    #    (violonisteelectrique.com), les scenes telles qu'elles figurent sur
    #    /david-lesage-en-concert. Rien n'a ete ajoute a l'une ni a l'autre.
    a('<section id="references"><div class="wrap">')
    a('  <span class="kick">%s</span>' % _bi('Références', 'Track record'))
    a('  <h2 class="sec-title">%s</h2>' % _bi(
        'Ce que chacun apporte dans la corbeille',
        'What each of them brings to the table'))
    a('  <p class="lead">%s</p>' % _bi(
        'Le duo est neuf ; les deux parcours ne le sont pas. À gauche les marques et les '
        'institutions qui ont fait jouer Lucie, à droite les scènes de David.',
        'The duo is new; the two careers behind it are not. On the left, the brands and '
        'institutions that have hired Lucie; on the right, David&rsquo;s stages.'))
    a('  <div class="refs">')

    a('    <div class="ref-col">')
    a('      <h3>%s</h3>' % _bi('Les marques de Lucie', 'Lucie&rsquo;s clients'))
    a('      <div class="who">%s</div>' % _bi(
        'Maisons de luxe, groupes internationaux, institutions',
        'Luxury houses, international groups, institutions'))
    # ⚠️ LA PLANCHE DE LOGOS EST CELLE DE LUCIE, reprise telle quelle depuis son
    #    propre site. On ne redessine pas, on ne recolore pas et on ne recompose
    #    pas des marques deposees : on reprend l'image qu'elle publie elle-meme.
    #    Elle a un fond blanc — c'est VOULU qu'elle soit posee sur un panneau
    #    clair : un mur de logos se lit comme une planche de presse, pas comme
    #    un element du decor de la page. Les noms restent dans l'attribut `alt`,
    #    pour que la liste existe aussi pour qui ne voit pas l'image.
    a('      <div class="logos">')
    a('        <img src="media/photos/references-lucie.jpg" loading="lazy" alt="%s">'
      % ('Airbus, Google, Louis Vuitton, Moët &amp; Chandon, Allianz, Audi, Chanel, '
         'Disney+, Dior, Galénic, Huawei, Schlumberger, Société Générale, '
         'Patek Philippe, Generali, HEC Paris, Total, L&rsquo;Oréal, The Ritz-Carlton, '
         'E.Leclerc, M6, Square Enix, Sephora, Sheraton, Pernod Ricard, '
         'Mandarin Oriental, Thales, Renault Nissan Mitsubishi'))
    a('      </div>')
    a('      <p class="ref-note">%s</p>' % _bi(
        'Planche publiée par Lucie sur violonisteelectrique.com. Les marques citées '
        'restent la propriété de leurs titulaires.',
        'Sheet published by Lucie on violonisteelectrique.com. All trademarks remain '
        'the property of their respective owners.'))
    a('    </div>')
    a('    <div class="ref-col">')
    a('      <h3>%s</h3>' % _bi('Les scènes de David', 'David&rsquo;s stages'))
    a('      <div class="who">%s</div>' % _bi(
        'Festivals, salles, lieux de patrimoine, télévision',
        'Festivals, venues, heritage sites, television'))
    a('      <div class="chips">')
    for nom in ('Jazz in Marciac', 'Le Grand Rex', 'Sziget Festival',
                'Everness Festival', 'The Voice &mdash; TF1', 'Amadou &amp; Mariam',
                'Hona Festival &mdash; Naxos', 'HUG Fesztivál',
                'Abbaye Notre-Dame d&rsquo;Alet', 'Basilique Saint-Nazaire',
                'Cloître de Saint-Geniez-d&rsquo;Olt',
                'Église Saint-Jean-l&rsquo;Évangéliste &mdash; Tourcoing',
                'Chapelle du Mas Galifa &mdash; Espagne',
                'Mont Korhogo &mdash; Côte d&rsquo;Ivoire', 'FLORIPAN'):
        a('        <span class="chip">%s</span>' % nom)
    a('      </div>')
    a('    </div>')


    a('  </div>')
    a('</div></section>')

    a('<div class="divider"></div>')

    # ----------------------------------------------------- instrumentarium
    a('<section id="scene"><div class="wrap">')
    a('  <span class="kick">%s</span>' % _bi('Sur scène', 'On stage'))
    a('  <h2 class="sec-title">%s</h2>' % _bi(
        'Ce qui monte sur le plateau', 'What goes on stage'))
    a('  <p class="lead">%s</p>' % _bi(
        'Tout est joué en direct. Le bouclage se construit devant le public, à vue : '
        'il n&rsquo;y a aucune bande préenregistrée. Côté handpan, le Neotone tient la '
        'place principale &mdash; il porte toutes les gammes dans un seul instrument, ce qui '
        'évite d&rsquo;en transporter quatre, tient dans une soute et se branche directement '
        'en console : c&rsquo;est ce qui rend le duo simple à faire voyager et rapide à caler '
        'en balance. Les handpans acoustiques Yishama restent de la partie quand la salle '
        'et le format s&rsquo;y prêtent.',
        'Everything is played live. The looping is built in front of the audience, in '
        'plain sight: there is no pre-recorded backing track. On the handpan side the '
        'Neotone takes the lead &mdash; it holds every scale in one instrument, which saves '
        'carrying four of them, fits in a hold and plugs straight into the desk: that is '
        'what makes this duo easy to fly out and quick to soundcheck. The Yishama acoustic '
        'handpans stay in the picture whenever the room and the format call for them.'))
    a('  <div class="instr">')

    a('    <div class="instr-col">')
    a('      <h3>David Lesage</h3>')
    a('      <div class="who">%s</div>' % _bi('Percussions, cordes, voix', 'Percussion, strings, voice'))
    a('      <ul>')
    instr_d = (
        ('<b>Deux handpans électroniques Neotone</b> &mdash; toutes les gammes dans un seul '
         'instrument, changement de gamme en cours de morceau, sortie directe en console',
         '<b>Two Neotone electronic handpans</b> &mdash; every scale in a single instrument, '
         'scale changes mid-piece, direct output to the desk'),
        ('<b>Deux handpans acoustiques Yishama</b> &mdash; le grain de la tôle martelée, '
         'quand la salle et le format s&rsquo;y prêtent',
         '<b>Two Yishama acoustic handpans</b> &mdash; the grain of hammered steel, when the '
         'room and the format call for it'),
        ('<b>Ngoni quatorze cordes</b> &mdash; harpe africaine',
         '<b>Fourteen-string ngoni</b> &mdash; African harp'),
        ('<b>Calebasse</b>',
         '<b>Calabash</b>'),
        ('<b>Erae 2</b> &mdash; le multipad lumineux d&rsquo;Embodme, une surface de jeu '
         'qui s&rsquo;éclaire sous les doigts',
         '<b>Erae 2</b> &mdash; Embodme&rsquo;s illuminated multipad, a playing surface that '
         'lights up under the fingers'),
        ('<b>Voix</b> &mdash; cinq octaves, en français, anglais, swahili, sanskrit et luo',
         '<b>Voice</b> &mdash; five octaves, in French, English, Swahili, Sanskrit and Luo'),
        ('<b>Loop station Roland RC-505 MK2</b>, sampler TM-2, déclencheurs BT-1',
         '<b>Roland RC-505 MK2 loop station</b>, TM-2 sampler, BT-1 triggers'),
    )
    for fr, en in instr_d:
        a('        <li>%s</li>' % _bi(fr, en))
    a('      </ul>')
    a('    </div>')

    a('    <div class="instr-col">')
    a('      <h3>Lucie</h3>')
    a('      <div class="who">%s</div>' % _bi('Cordes', 'Strings'))
    a('      <ul>')
    instr_l = (
        ('<b>Violon électrique Yamaha YEV-205</b>',
         '<b>Yamaha YEV-205 electric violin</b>'),
        ('<b>Violon acoustique</b>',
         '<b>Acoustic violin</b>'),
        ('<b>Violon lumineux 3Dvarius</b> &mdash; à LED, pour les formats scénographiés',
         '<b>3Dvarius LED violin</b> &mdash; for staged formats'),
        ('Archet <b>Cor Leonis</b> de Jean-Luc Tauziède, ou archet CORUSS HAIR',
         '<b>Cor Leonis</b> bow by Jean-Luc Tauziède, or a CORUSS HAIR bow'),
        ('Tenues de gala, tenues rock, robes lumineuses à LED selon le format demandé',
         'Gala outfits, rock outfits or LED light dresses, depending on the format'),
    )
    for fr, en in instr_l:
        a('        <li>%s</li>' % _bi(fr, en))
    a('      </ul>')
    a('    </div>')

    a('  </div>')

    # Les trois images qui PROUVENT la liste ci-dessus : l'ensemble du parc,
    # le handpan acoustique (qu'aucune photo ne montrait jusqu'au 30/08), et
    # la harpe africaine.
    # ⚠️ LE HANDPAN ACOUSTIQUE PREND LA PLEINE LARGEUR, et ce n'est pas
    #    decoratif : jusqu'au 30/08 aucune photo de la page ne le montrait, alors
    #    que le texte l'annonce. La photo est en 16/9 — la mettre dans une
    #    colonne etroite en 3/4 aurait recadre Lucie hors du cadre.
    a('  <figure class="grande">')
    a('    <img src="media/photos/handpan-acoustique.jpg" loading="lazy" '
      'alt="Le handpan acoustique Yishama en tôle martelée, tenu par David Lesage">')
    a('    <figcaption>%s</figcaption>' % _bi(
        'Le handpan acoustique Yishama, en tôle martelée &mdash; l&rsquo;autre versant '
        'du même geste.',
        'The Yishama acoustic handpan, in hammered steel &mdash; the other side of the '
        'same gesture.'))
    a('  </figure>')
    a('  <div class="deux-photos">')
    photos_scene = (
        ('instruments.jpg',
         'Tout le parc du duo : calebasse au premier plan, handpan électronique, '
         'ngoni et violon électrique.',
         'The duo&rsquo;s full set: calabash in the foreground, electronic handpan, '
         'ngoni and electric violin.'),
        ('ngoni.jpg',
         'Le ngoni quatorze cordes, harpe africaine, et la calebasse.',
         'The fourteen-string ngoni, an African harp, and the calabash.'),
    )
    for fichier, cfr, cen in photos_scene:
        a('    <figure><img src="media/photos/%s" loading="lazy" alt="%s">'
          '<figcaption>%s</figcaption></figure>'
          % (fichier, cfr.replace('"', '&quot;'), _bi(cfr, cen)))
    a('  </div>')
    a('</div></section>')

    a('<div class="divider"></div>')

    # ------------------------------------------------------------- galerie
    a('<section id="galerie"><div class="wrap">')
    a('  <span class="kick">%s</span>' % _bi('En images', 'In pictures'))
    a('  <h2 class="sec-title">%s</h2>' % _bi(
        'Paris, 28 août 2026', 'Paris, 28 August 2026'))
    a('  <div class="carrousel">')
    a('    <div class="piste" tabindex="0" role="group" '
      'aria-roledescription="carrousel" aria-label="Photographies du 28 août 2026">')
    a(_galerie_html())
    a('    </div>')
    a('    <button type="button" class="fleche prec" aria-label="Photo précédente">'
      '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M10.8 1.4 4.2 8l6.6 6.6 1.4-1.4L7 8l5.2-5.2z"/></svg></button>')
    a('    <button type="button" class="fleche suiv" aria-label="Photo suivante">'
      '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M5.2 1.4 3.8 2.8 9 8l-5.2 5.2 1.4 1.4L11.8 8z"/></svg></button>')
    a('    <div class="puces">')
    a(_puces_html())
    a('    </div>')
    a('  </div>')
    a('</div></section>')

    # ------------------------------------------------------------- contact
    a('<section id="contact"><div class="wrap">')
    a('  <span class="kick">%s</span>' % _bi('Contact', 'Contact'))
    a('  <h2 class="sec-title">%s</h2>' % _bi(
        'Parlons du format qui vous va', 'Let us talk about the format you need'))
    a('  <p class="lead">%s</p>' % _bi(
        'Le duo se construit. Le répertoire enregistré compte cinq pièces, soit '
        '%d minutes de musique, et la durée comme la scénographie se calent sur '
        'votre événement. Écrivez-nous : nous répondons vite.'
        % DUREE_TOTALE_MIN,
        'The duo is taking shape. The recorded repertoire holds five pieces &mdash; '
        '%d minutes of music &mdash; and both length and staging are set to fit your '
        'event. Write to us: we answer quickly.' % DUREE_TOTALE_MIN))
    a('  <div class="contact">')
    a('    <div class="ct-grid">')
    a('      <div class="ct-rows">')
    a('        <div><span class="ct-l">%s</span><div class="ct-v">'
      '<a href="mailto:contact@resonancesproductions.org">'
      'contact@resonancesproductions.org</a></div></div>'
      % _bi('Courriel', 'Email'))
    # ⚠️ NI TELEPHONE NI ADRESSE POSTALE — demande de David du 30/08/2026. Cette
    #    page circule chez des tiers : un numero personnel et une adresse de
    #    domicile n'ont rien a y faire, le courriel suffit a une agence. Ne pas
    #    les remettre « pour faire complet ».
    a('        <div><span class="ct-l">%s</span><div class="ct-v">%s</div></div>'
      % (_bi('Base', 'Based in'),
         _bi('Paris &mdash; disponibles à l&rsquo;international',
             'Paris &mdash; available internationally')))
    a('      </div>')
    a('      <div>')
    a('        <a class="btn" href="mailto:contact@resonancesproductions.org'
      '?subject=Duo%%20David%%20Lesage%%20%%26%%20Lucie">%s</a>'
      % _bi('Nous écrire', 'Get in touch'))
    a('      </div>')
    a('    </div>')
    a('    <p class="legal">%s</p>' % _bi(
        'Résonances Productions &mdash; association loi 1901, arts du spectacle vivant. '
        'SIRET 919 514 075 00010, code APE 9001Z. Structure porteuse des projets de '
        'David Lesage, habilitée à contractualiser et à employer.',
        'Résonances Productions &mdash; French non-profit association (loi 1901), '
        'performing arts. SIRET 919 514 075 00010, APE code 9001Z. The structure behind '
        'David Lesage&rsquo;s projects, able to contract and to employ.'))
    a('  </div>')
    a('</div></section>')

    a('<footer><div class="wrap">')
    a('  <p>%s</p>' % _bi(
        'Photographies et enregistrements : Paris, 28 août 2026. '
        'Page privée &mdash; merci de ne pas la diffuser publiquement. '
        '<a href="/">resonancesproductions.org</a>',
        'Photographs and recordings: Paris, 28 August 2026. '
        'Private page &mdash; please do not share it publicly. '
        '<a href="/">resonancesproductions.org</a>'))
    a('</div></footer>')

    # -------------------------------------------- barre de lecture, en bas
    a('<div class="pad-bar"></div>')
    a('<div class="bar" role="region" aria-label="Lecteur audio">')
    a('  <div class="bar-in">')
    a('    <button class="bar-play" type="button" aria-label="Lecture">%s</button>' % I_PLAY)
    a('    <div>')
    a('      <div class="bar-t"></div>')
    a('      <input class="seek" type="range" min="0" max="100" step="0.1" value="0" '
      'aria-label="Position dans le morceau">')
    a('    </div>')
    a('    <div style="display:flex;align-items:center;gap:16px">')
    a('      <span class="bar-time">0:00 / 0:00</span>')
    a('      <span class="bar-skip">')
    a('        <button class="b-prev" type="button" aria-label="Précédent">%s</button>' % I_PREV)
    a('        <button class="b-next" type="button" aria-label="Suivant">%s</button>' % I_NEXT)
    a('      </span>')
    a('    </div>')
    a('  </div>')
    a('</div>')
    # Les deux icones du lecteur sont posees DANS le script (et pas relues
    # depuis le DOM) : un `<template>` ne rend pas son contenu de la meme
    # facon selon les navigateurs, et la barre serait restee sans icone.
    a('<script>%s</script>' % (
        JS.replace('__ICO_PLAY__', I_PLAY).replace('__ICO_PAUSE__', I_PAUSE)))
    a('</body></html>')
    return '\n'.join(h) + '\n'


def main():
    os.makedirs(os.path.dirname(SORTIE), exist_ok=True)
    html = page()
    with open(SORTIE, 'w', encoding='utf-8') as f:
        f.write(html)
    print('  ecrit  %s  (%d Ko)' % (
        os.path.relpath(SORTIE, RACINE), len(html.encode('utf-8')) // 1024))
    print('  ⚠️  page volontairement invisible : ni menu, ni sitemap, ni moteurs.')


if __name__ == '__main__':
    main()
