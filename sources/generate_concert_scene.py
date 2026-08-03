# -*- coding: utf-8 -*-
"""Genere la page /david-lesage-en-concert (david-lesage-en-concert/index.html).

DEUXIEME version de la page concert, DESTINEE AUX PROFESSIONNELS :
programmateurs, festivals, lieux, salles. Elle est le pendant « grandes
scenes » de /concerts-david-lesage, qui reste la version INTIMISTE (Le Nid,
Paris 20e, ecrite pour un particulier qui hesite a venir un soir).

  /concerts-david-lesage  -> particulier parisien   -> « Reserver ma place »
  /david-lesage-en-concert -> programmateur          -> « Programmer ce concert »

SOURCE DES FAITS : le dossier de presentation scenique de David Lesage.
REGLES DE REDACTION :
  - Ici l'information professionnelle est BIENVENUE (duree 1 h 30, format,
    composantes du dispositif, options) — contrairement a la page du Nid ou
    David l'a explicitement bannie.
  - AUCUNE donnee absente du dossier : pas de fiche technique, pas de plan de
    scene, pas de rider, pas de tarif, pas de jauge, pas d'effectif. Si une
    fiche technique est necessaire, elle sera fournie par David — elle n'est
    PAS inventee ici.
  - La danse aerienne a l'elastique d'Iris Chasles EST mentionnable (impossible
    au Nid, possible sur grande scene) : presentee comme une OPTION, comme dans
    le dossier.
  - Les formules elogieuses du dossier sont donnees COMME DES CITATIONS
    attribuees au dossier de presentation, jamais comme des affirmations de
    l'association.
  - Le site VOUVOIE. Sobre et premium.
  - Appel a l'action = « Programmer ce concert » / « Demander le dossier »,
    vers contact@resonancesproductions.org avec objet pre-rempli.
  - Renvoi croise discret vers /concerts-david-lesage pour le public parisien.

IMAGES : aucun telechargement externe. On reutilise des declinaisons deja
presentes dans le depot (voir DLC_PHOTOS). La photo du Grand Rex porte le
filigrane « MAGYE D'ART Production » -> le credit photo est repris sous la
figure, comme sur /e-motion. Les 4 photos filigranees de /img/e-motion/
(suspendue-bras-ouverts, l-elastique-en-noir-et-blanc, sur-grande-scene,
le-ciel-en-toile-de-fond) et rituals/le-tournoiement-de-la-beaute-* ne sont
PAS utilisees ici.

Usage :
    python3 sources/generate_concert_scene.py
    -> ecrit directement david-lesage-en-concert/index.html
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mobile_nav  # noqa: E402

HELLO_ASSO = 'https://www.helloasso.com/associations/resonances-productions'
MAIL = 'contact@resonancesproductions.org'
MAILTO_PROG = ('mailto:' + MAIL + '?subject=Programmation%20%E2%80%94%20David%20Lesage'
               '%20en%20concert')
MAILTO_DOSSIER = ('mailto:' + MAIL + '?subject=Dossier%20de%20pr%C3%A9sentation%20'
                  '%E2%80%94%20David%20Lesage%20en%20concert')

# --- Images reutilisees du depot -------------------------------------------
# cle : (dossier, base, [largeurs disponibles], largeur_intrinseque, hauteur)
DLC_PHOTOS = {
    'everness':   ('rituals',  'everness-festival-hongrie',                [480, 900, 1400], 1400, 667),
    'salle':      ('rituals',  'le-public-au-coeur-du-rituel',             [480, 900],        900, 501),
    'echo':       ('rituals',  'chanter-ensemble',                         [480, 900, 1400], 1400, 780),
    'proche':     ('rituals',  'une-connexion-forte-avec-le-public',       [480, 900, 1400], 1400, 786),
    'setup':      ('rituals',  'un-univers-musical-electro-organique',     [480, 900, 1400], 1400, 778),
    'portrait':   ('rituals',  'david-lesage',                             [480, 900, 1400], 1400, 1400),
    'rex':        ('rituals',  'au-grand-rex',                             [480, 900, 1400], 1400, 912),
    'aerien':     ('e-motion', 'danse-aerienne-et-musique-live-sur-scene', [480, 900, 1400], 1400, 783),
    'aerien-fest': ('e-motion', 'everness-festival',                       [480, 900],        900, 600),
}

CREDIT_MAGYE = ('<span class="dlc-cred">Crédit photo <a href="https://magyedart.fr/" '
                'target="_blank" rel="noopener">MAGYE D’ART</a></span>')


def pic(key, alt, sizes, caption=None, cls='dlc-fig', loading='lazy', credit=''):
    """<picture> WebP + repli JPEG, srcset complet, width/height, alt factuel."""
    folder, base, widths, w, h = DLC_PHOTOS[key]
    root = f'/img/{folder}/{base}'
    webp = ', '.join(f'{root}-{x}.webp {x}w' for x in widths)
    jpg = ', '.join(f'{root}-{x}.jpg {x}w' for x in widths)
    big = f'{root}-{widths[-1]}.jpg'
    prio = ' fetchpriority="high"' if loading == 'eager' else ''
    img = (f'<picture><source type="image/webp" srcset="{webp}" sizes="{sizes}">'
           f'<img src="{big}" srcset="{jpg}" sizes="{sizes}" width="{w}" height="{h}" '
           f'loading="{loading}"{prio} decoding="async" alt="{alt}"></picture>')
    cap = f'<figcaption>{caption}{credit}</figcaption>' if caption else ''
    return f'<figure class="{cls}">{img}{cap}</figure>'


# --- Contenu ---------------------------------------------------------------
FICHE = [
    ('Format', 'Concert · Cérémonie · Participatif'),
    ('Durée', '1 h 30'),
    ('Instruments', 'Voix, handpan, calebasse, Ngoni (harpe africaine), wave drum, '
                    'déclencheurs électroniques'),
    ('Langues', 'Français, swahili, sanskrit'),
    ('Esthétique', 'Soul française · African spirit · Électro vibes'),
    ('Dispositif', 'Vidéoprojections · cymatique en temps réel · ambiances sonores · '
                   'échanges vocaux avec la salle'),
    ('En option', 'Danse aérienne à l’élastique — Iris Chasles · extraits du spectacle '
                  '<a href="/e-motion">E-Motion</a>'),
]

# Les 8 composantes de la soiree, telles que decrites dans le dossier.
COMPOSANTES = [
    ('Partages',
     'Des prises de parole entre les morceaux, autour de valeurs au cœur de l’humain : '
     'la vulnérabilité masculine, la spiritualité, l’amour.'),
    ('Chansons en français et en langues du monde',
     'Le répertoire circule du français au swahili et au sanskrit.'),
    ('Instruments traditionnels et électroniques',
     'Handpan, calebasse, Ngoni, wave drum ; déclencheurs électroniques et machines, '
     'joués en direct.'),
    ('Cymatique',
     'Un temps pédagogique sur l’impact de la vibration sonore sur l’eau et sur l’humain. '
     'Le public chante des voyelles et voit l’empreinte de sa propre voix apparaître à '
     'l’écran, en temps réel.'),
    ('Ambiances sonores',
     'Nature, animaux : des paysages sonores ouvrent et referment les séquences.'),
    ('Vidéoprojections',
     'Les morceaux sont accompagnés d’images projetées.'),
    ('Affirmations positives',
     'Des phrases simples, reprises comme des refrains.'),
    ('Échanges vocaux',
     'La salle chante en écho avec l’artiste.'),
]

REPERES = [
    ('Dès 4 ans', 'Batterie.'),
    ('Conservatoire National de Toulouse',
     'Prix de batterie, mention très bien.'),
    ('Collège de Jazz in Marciac',
     'Formation à la batterie, au chant et à l’improvisation vocale.'),
    ('Cinq octaves',
     'Ambitus vocal : pop, soul, lyrique, gospel, chanson française, rap.'),
    ('2012',
     'Rencontre de la calebasse et du Ngoni ; exploration des sonorités et des rythmes '
     'africains.'),
    ('2021', 'The Voice.'),
    ('À la suite de l’émission',
     'Invité pour un concert solo en Côte d’Ivoire.'),
    ('Aujourd’hui',
     'Ambassadeur Neotone — le handpan électronique — et collaboration avec Yishama, '
     'fabricant de handpans d’exception.'),
]

SCENES = [
    ('Everness Festival', 'Hongrie'),
    ('Abbaye à ciel ouvert d’Alet-les-Bains', 'France'),
    ('Église San Subra, Toulouse', 'France'),
    ('Salle du Castillo, Vevey', 'Suisse'),
    ('Mont Korhogo', 'Côte d’Ivoire'),
]

COMPOSITIONS = ['Intro', 'Humano', 'Transe lunaire', 'L’alchimiste', 'L’appel du vent',
                'Au cœur de l’homme', 'Yishama', 'Le tisseur de liens', 'Je te vois']

REPRISES = [
    ('Sting', 'Shape of My Heart'),
    ('M', 'Une Âme'),
    ('Alicia Keys', 'Fallin’'),
    ('Bigflo &amp; Oli', 'Copier Coller'),
    ('Charles Gounod', 'Ave Maria'),
    ('Roberto Orenalla', 'L’Esprit Divin'),
    ('Algonquin Water Song — chant traditionnel', 'Nibiwabo'),
]

CITATIONS = ['Une musique qui tisse des liens', 'Des rythmes envoûtants',
             'Des paroles profondes', 'Des refrains incantatoires',
             'Des envolées jazz d’une voix céleste']

TOC = [
    ('#fiche', 'En un regard'),
    ('#dispositif', 'Le dispositif'),
    ('#salle', 'Ce que fait une salle qui chante'),
    ('#parcours', 'Le parcours'),
    ('#scenes', 'Scènes &amp; festivals'),
    ('#repertoire', 'Le répertoire'),
    ('#option', 'En option : la danse aérienne'),
    ('#programmer', 'Programmer ce concert'),
]

CSS = """
:root{--night:#0e0f24;--night2:#141633;--ink:#eae7f3;--muted:#a9a6c4;--gold:#d8b25a;--gold2:#f0d18a;--plum:#8f7ad1;--card:#191b3d;--line:rgba(216,178,90,.26)}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--night);color:var(--ink);font-family:'Jost',-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.75;font-size:17px;-webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2,h3,h4,.serif{font-family:'Cormorant Garamond',Georgia,serif}
a{color:inherit;text-decoration:none}
img,picture{max-width:100%}
.wrap{max-width:1080px;margin:0 auto;padding:0 26px}
.kick{letter-spacing:.32em;text-transform:uppercase;font-size:13px;font-weight:600;color:var(--gold);margin-bottom:14px}
section{padding:78px 0;position:relative}
.sec-title{font-size:clamp(30px,5vw,50px);font-weight:600;line-height:1.08;color:#fff}
.lead{font-size:19px;color:var(--muted);max-width:760px;margin-top:16px}
p.body{max-width:820px;color:#d7d4ea;margin-top:16px}
b{color:#fff;font-weight:500}
.divider{height:1px;background:linear-gradient(90deg,transparent,var(--line),transparent);max-width:1080px;margin:0 auto}
/* nav — barre identique aux autres pages (8px + 44px + 8px = 60px de haut) */
.nav{position:fixed;top:0;left:0;right:0;z-index:40;display:flex;align-items:center;justify-content:space-between;padding:8px 26px;background:rgba(14,15,36,.6);backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.05)}
.nav .brand{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:19px;letter-spacing:.12em;color:#fff;text-transform:uppercase;display:inline-flex;align-items:center;min-height:44px}
.nav .links{display:flex;align-items:center;gap:19px;font-size:13.5px;letter-spacing:.04em}
.nav .links a{color:var(--muted);transition:color .2s;display:inline-flex;align-items:center;min-height:44px;white-space:nowrap;flex:0 0 auto}
.nav .links a:hover{color:var(--gold2)}
.nav .adh{color:#1a1608!important;background:var(--gold);padding:0 17px;border-radius:30px;font-weight:600}
@media(max-width:760px){.nav .links a:not(.adh){display:none}}
/* Cette page porte 11 entrees (une de plus que les autres : « Programmation »).
   On resserre entre 861 et 1340 px et on masque par ordre de moindre importance :
   Statuts, puis Contact, puis Prestations, puis L'association — toutes restent
   joignables depuis le pied de page et l'accueil. Jamais sous 13 px (plancher typo).
   `white-space:nowrap` sur les liens : sans lui, sous 1340 px les libelles se
   coupaient en deux lignes et la barre passait de 61 a 96 px de haut. */
@media(min-width:861px) and (max-width:1340px){.nav{padding:8px 16px}.nav .brand{font-size:17px;white-space:nowrap}.nav .links{gap:9px;font-size:13px}.nav .adh{padding:0 14px}}
@media(min-width:861px) and (max-width:1340px){.nav .links a[href="/#statuts"]{display:none}}
@media(min-width:861px) and (max-width:1060px){.nav .links a[href="/#association"]{display:none}}
@media(min-width:861px) and (max-width:960px){.nav .links a[href="/#prestations"]{display:none}}
@media(min-width:861px) and (max-width:920px){.nav .links a[href="#contact"]{display:none}}
.nav .links a[aria-current="page"]{color:var(--gold2)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;background:var(--gold);color:#1a1608;font-weight:600;padding:14px 28px;border-radius:40px;font-size:16px;min-height:48px;transition:transform .2s,box-shadow .2s}
.btn:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(216,178,90,.28)}
.btn.ghost{background:transparent;color:var(--gold2);border:1px solid var(--line)}
.cta{display:flex;gap:14px;flex-wrap:wrap}
/* ===== David Lesage en concert (page professionnelle) ===== */
.dlc-top{padding:128px 0 70px;background:radial-gradient(900px 560px at 12% -8%,rgba(143,122,209,.20),transparent 62%),radial-gradient(700px 460px at 90% 102%,rgba(216,178,90,.12),transparent 62%),linear-gradient(180deg,#0b0c1e,var(--night))}
.dlc-top h1{font-size:clamp(36px,6.6vw,68px);font-weight:600;line-height:1.03;color:#fff;letter-spacing:.02em}
.band{background:linear-gradient(180deg,#0b0c1e,var(--night))}
.tagline{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(19px,2.8vw,28px);margin-top:12px}
.dlc-h{color:var(--gold);font-size:13px;letter-spacing:.22em;text-transform:uppercase;font-weight:600;margin-bottom:10px}
.dlc-block p{max-width:820px;color:#d7d4ea;margin-top:16px}
.dlc-fig{margin:0;border-radius:16px;overflow:hidden;border:1px solid var(--line);background:var(--card)}
.dlc-fig img{display:block;width:100%;height:auto}
.dlc-fig figcaption{color:var(--muted);font-size:13.5px;line-height:1.55;padding:12px 16px 14px;border-top:1px solid rgba(255,255,255,.06)}
.dlc-cred{display:block;margin-top:2px;font-style:italic;font-size:15px;color:#8e8ba9}
.dlc-hero-fig{margin-top:34px}
.dlc-wide{max-width:860px;margin-top:26px}
.dlc-portrait{max-width:420px}
.dlc-quote{margin:30px 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(20px,2.7vw,26px);line-height:1.38;border-left:2px solid var(--gold);padding-left:22px;max-width:780px}
.dlc-quote cite{display:block;margin-top:12px;font-style:normal;font-family:'Jost',sans-serif;font-size:13.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.dlc-note{background:var(--card);border:1px solid rgba(255,255,255,.07);border-left:2px solid var(--gold);border-radius:14px;padding:19px 22px;margin-top:26px;max-width:860px}
.dlc-note p{color:#d7d4ea;font-size:15.5px;margin:0;line-height:1.7;max-width:none}
.dlc-note p+p{margin-top:10px}
.dlc-note .dlc-h{margin-bottom:8px}
/* deux colonnes : texte + figure */
.dlc-split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,340px);gap:36px;align-items:start;margin-top:30px}
.dlc-split>div>p:first-child{margin-top:0}
@media(max-width:860px){.dlc-split{grid-template-columns:1fr;gap:26px}}
/* fiche « en un regard » : liste de definitions */
.dlc-id{margin-top:28px;max-width:900px;display:grid;grid-template-columns:minmax(0,220px) minmax(0,1fr);gap:0}
/* gap 0 + padding-right sur le dt : sinon la gouttiere coupait le filet horizontal
   de chaque ligne en deux morceaux desalignes. */
.dlc-id dt{color:var(--gold);font-size:13px;letter-spacing:.18em;text-transform:uppercase;font-weight:600;padding:15px 30px 15px 0;border-top:1px solid rgba(255,255,255,.07);line-height:1.5}
.dlc-id dd{color:#d7d4ea;font-size:16.5px;padding:14px 0 16px;border-top:1px solid rgba(255,255,255,.07);line-height:1.6}
.dlc-id dt:first-of-type,.dlc-id dd:first-of-type{border-top:0}
@media(max-width:640px){.dlc-id{grid-template-columns:1fr;gap:0}
  .dlc-id dt{padding:16px 0 2px}
  .dlc-id dd{border-top:0;padding:0 0 16px;font-size:16px}}
/* composantes du dispositif */
.dlc-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px;margin-top:32px;list-style:none}
.dlc-grid li{background:var(--card);border:1px solid rgba(255,255,255,.06);border-top:2px solid var(--gold);border-radius:14px;padding:22px 24px}
.dlc-grid h3{font-size:23px;color:#fff;font-weight:600;line-height:1.2}
.dlc-grid p{color:#d7d4ea;font-size:15.5px;margin-top:9px;line-height:1.65}
/* reperes de parcours */
.dlc-rep{margin-top:28px;max-width:820px;display:grid;grid-template-columns:minmax(0,265px) minmax(0,1fr);gap:0}
.dlc-rep dt{font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;color:var(--gold2);font-weight:600;padding:14px 28px 14px 0;border-top:1px solid rgba(255,255,255,.07);line-height:1.35}
.dlc-rep dd{color:#d7d4ea;font-size:16px;padding:16px 0;border-top:1px solid rgba(255,255,255,.07);line-height:1.6}
.dlc-rep dt:first-of-type,.dlc-rep dd:first-of-type{border-top:0}
@media(max-width:640px){.dlc-rep{grid-template-columns:1fr}
  .dlc-rep dt{padding:16px 0 0}
  .dlc-rep dd{border-top:0;padding:2px 0 16px}}
/* cartes du repertoire */
.dlc-cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:20px;margin-top:30px;align-items:start}
.dlc-card{background:var(--card);border:1px solid rgba(255,255,255,.06);border-left:2px solid var(--gold);border-radius:14px;padding:24px 26px}
.dlc-card h3{font-family:'Cormorant Garamond',Georgia,serif;font-size:24px;color:#fff;font-weight:600;line-height:1.15}
.dlc-card .sub{color:var(--muted);font-size:14px;font-style:italic;margin-top:3px}
.dlc-card ul{list-style:none;margin-top:16px}
.dlc-card li{color:#d7d4ea;font-size:15.5px;padding:7px 0;border-bottom:1px solid rgba(255,255,255,.05);line-height:1.5}
.dlc-card li:last-child{border-bottom:0}
.dlc-card li span{color:var(--gold2);display:block;font-size:13.5px;letter-spacing:.04em}
/* citations du dossier */
.dlc-cites{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px;max-width:880px;list-style:none}
.dlc-cites li{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:17.5px;line-height:1.4;background:rgba(216,178,90,.08);border:1px solid var(--line);border-radius:30px;padding:8px 20px}
/* scenes */
.dlc-scenes{list-style:none;margin-top:24px;max-width:820px;display:grid;gap:2px}
.dlc-scenes li{display:flex;gap:16px;align-items:baseline;flex-wrap:wrap;color:#d7d4ea;font-size:16px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.06)}
.dlc-scenes li:last-child{border-bottom:0}
.dlc-scenes li b{flex:1 1 260px;min-width:0}
.dlc-scenes li span{color:var(--gold);font-size:13.5px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;flex:0 0 auto}
/* deux figures cote a cote */
.dlc-duo{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin-top:30px;align-items:start}
/* bloc de contact / programmation */
.dlc-prog{background:linear-gradient(160deg,rgba(216,178,90,.12),var(--card));border:1px solid var(--line);border-radius:18px;padding:30px 32px;margin-top:30px;max-width:860px}
.dlc-prog h3{font-size:27px;color:#fff;font-weight:600;line-height:1.2}
.dlc-prog p{color:#d7d4ea;font-size:16px;margin-top:12px;max-width:none}
@media(max-width:560px){.dlc-prog{padding:24px 22px}.dlc-prog .btn{width:100%}}
/* renvoi croise vers la page intimiste */
.dlc-cross{border:1px dashed var(--line);border-radius:14px;padding:20px 24px;margin-top:34px;max-width:860px;background:rgba(25,27,61,.5)}
.dlc-cross p{margin:0;color:var(--muted);font-size:16px;max-width:none;line-height:1.7}
.dlc-cross a{display:inline-block;padding:11px 0}
/* sommaire */
.toc{margin-top:44px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:22px 0}
.toc .dlc-h{margin-bottom:14px}
.toc ol{list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:2px 26px;counter-reset:toc}
.toc li{counter-increment:toc}
.toc a{display:block;color:var(--muted);font-size:15px;padding:9px 0;min-height:44px;transition:color .2s}
.toc a::before{content:counter(toc,decimal-leading-zero);color:var(--gold);font-size:12px;letter-spacing:.1em;margin-right:10px}
.toc a:hover{color:var(--gold2)}
/* retour en haut */
.totop{position:fixed;right:18px;bottom:18px;z-index:35;width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:rgba(25,27,61,.92);border:1px solid var(--line);color:var(--gold2);font-size:19px;opacity:0;visibility:hidden;transition:opacity .3s,visibility .3s,transform .2s}
.totop.on{opacity:1;visibility:visible}
.totop:hover{transform:translateY(-2px)}
/* focus clavier visible (accessibilite) */
:focus-visible{outline:2px solid var(--gold2);outline-offset:2px;border-radius:4px}
footer{background:#08091a;padding:70px 0 56px;border-top:1px solid var(--line)}
.fgrid{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:34px}
footer h4{font-family:'Cormorant Garamond',serif;color:#fff;font-size:22px;font-weight:600;margin-bottom:10px}
footer p,footer a{color:var(--muted);font-size:14.5px}
footer a{display:inline-block;padding:13px 0;line-height:1.3}
footer a.btn,footer a.adh{padding:14px 30px}
footer a:hover{color:var(--gold2)}
.fbrand{letter-spacing:.12em;text-transform:uppercase;color:var(--gold2);font-family:'Cormorant Garamond',serif;font-size:20px;font-weight:600}
.legal{margin-top:40px;text-align:center;color:#6b6b80;font-size:13px}
@media(max-width:760px){.fgrid{grid-template-columns:1fr;gap:24px}section{padding:60px 0}}
/* --- lisibilite des liens (regle du site : liens >= 15 px et soulignes) ---
   Ce bloc doit rester EN DERNIER : il surcharge les tailles ci-dessus. */
footer p,footer a{font-size:16px}
footer a{padding:13px 0}
footer a:not(.btn):not(.adh){text-decoration:underline;text-decoration-color:rgba(216,178,90,.35);
  text-underline-offset:3px}
.nav .links a{font-size:15px}
.nav .links a.adh{font-size:15px}
/* ce bloc final est plus specifique que le resserrement 861-1180 px plus haut :
   on y redonne donc explicitement le 13px de la bande etroite (plancher typo). */
@media(min-width:861px) and (max-width:1340px){.nav .links a{font-size:13px}}
p a:not(.btn):not(.adh),li a:not(.btn):not(.adh),dd a:not(.btn):not(.adh){font-size:inherit;
  text-decoration:underline;text-decoration-color:rgba(216,178,90,.4);text-underline-offset:3px}
/* liens hors bouton : rendus inline-block pour garantir une cible tactile de 44 px
   de haut (regle du site), y compris dans le corps de texte et les credits photo. */
.dlc-note a,.dlc-id dd a,.dlc-prog p a:not(.btn),.dlc-cross a,.dlc-block p a:not(.btn)
  {display:inline-block;padding:11px 0}
.dlc-fig figcaption a{font-size:15px;display:inline-block;padding:12px 0;
  text-decoration:underline;text-decoration-color:rgba(216,178,90,.4);text-underline-offset:3px}
"""

TITLE = ('David Lesage en concert — concert-cérémonie participatif pour grandes scènes '
         'et festivals · Résonances Productions')
DESC = ('Voix, handpan, calebasse, Ngoni et électronique : une expérience immersive de '
        'musique live d’1 h 30, à programmer sur grande scène, en festival ou dans un '
        'lieu d’exception. Everness Festival (Hongrie), abbaye d’Alet-les-Bains, église '
        'San Subra, Vevey, Côte d’Ivoire. Option danse aérienne à l’élastique.')

HTML = f"""<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="David Lesage en concert — grandes scènes &amp; festivals">
<meta property="og:description" content="Concert — Cérémonie — Participatif : 1 h 30 de musique live immersive. Voix, handpan, calebasse, Ngoni, électronique ; cymatique et vidéoprojections ; option danse aérienne à l’élastique. À programmer.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.resonancesproductions.org/david-lesage-en-concert">
<meta property="og:image" content="https://www.resonancesproductions.org/img/rituals/everness-festival-hongrie-1400.jpg">
<meta property="og:image:width" content="1400">
<meta property="og:image:height" content="667">
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
    <a href="/#association">L’association</a>
    <a href="/#prestations">Prestations</a>
    <a href="/rituals">RITUALS</a>
    <a href="/e-motion">E-Motion</a>
    <a href="/david-lesage-en-concert" aria-current="page">Programmation</a>
    <a href="/concerts-david-lesage">Concerts</a>
    <a href="/le-nid">Le Nid</a>
    <a href="/le-soin-soa">Le Soin Soa</a>
    <a href="/#statuts">Statuts</a>
    <a href="#contact">Contact</a>
    <a class="adh" href="{HELLO_ASSO}" target="_blank" rel="noopener">Adhérer</a>
  </div>
</nav>

<header class="dlc-top"><div class="wrap">
  <div class="kick">Concert — Cérémonie — Participatif · Grandes scènes &amp; festivals</div>
  <h1>David Lesage en concert</h1>
  <div class="tagline">« Un profond voyage au cœur de soi »</div>
  <p class="lead">Une expérience immersive de musique live d’<b>1 h 30</b> : voix, handpan, calebasse, Ngoni et électronique. À programmer sur grande scène, en festival, ou dans un lieu d’exception.</p>
  <p class="body">Le format réunit instruments traditionnels et modernité, et alterne deux régimes : des séquences d’<b>écoute active</b>, et des séquences <b>participatives</b> où la salle devient une partie de l’œuvre — elle chante en écho, et voit à l’écran l’empreinte de sa propre voix. Un musicien, chanteur et compositeur formé au conservatoire et au collège de Jazz in Marciac, à l’ambitus vocal de cinq octaves, passé par <i>The Voice</i> et par la scène de l’<b>Everness Festival</b>, en Hongrie.</p>
  <div class="cta" style="margin-top:26px"><a class="btn" href="{MAILTO_PROG}">Programmer ce concert</a><a class="btn ghost" href="{MAILTO_DOSSIER}">Demander le dossier</a></div>
  {pic('everness',
       'David Lesage et Iris Chasles debout main dans la main sur la scène en plein air de l’Everness Festival, un handpan posé devant eux, sous une structure de projecteurs et une toile tendue orange ; à droite, une banderole « everness ».',
       '(max-width:1080px) calc(100vw - 52px), 1028px',
       'Everness Festival, Hongrie.',
       cls='dlc-fig dlc-hero-fig', loading='eager')}
  <nav class="toc" aria-label="Sommaire de la page"><div class="dlc-h">Sommaire</div><ol>{''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in TOC)}</ol></nav>
</div></header>

<section class="dlc-block" id="fiche"><div class="wrap">
  <div class="dlc-h">En un regard</div>
  <h2 class="sec-title">Ce que vous programmez</h2>
  <dl class="dlc-id">{''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in FICHE)}</dl>
  <div class="dlc-note">
    <p>Les éléments ci-dessus sont ceux du <b>dossier de présentation du spectacle</b>. Nous vous l’adressons volontiers, avec les précisions dont vous avez besoin pour votre lieu.</p>
    <p><a href="{MAILTO_DOSSIER}">Demander le dossier de présentation</a></p>
  </div>
</div></section>

<div class="divider"></div>

<section class="dlc-block band" id="dispositif"><div class="wrap">
  <div class="dlc-h">Le dispositif</div>
  <h2 class="sec-title">Une heure trente qui alterne écoute et participation</h2>
  <p>L’architecture de la soirée est simple et tenue : des temps où la salle se laisse traverser, des temps où elle prend part. Entre les deux, l’artiste parle — de vulnérabilité masculine, de spiritualité, d’amour — puis relance la musique.</p>
  <p>Huit composantes se relaient d’un bout à l’autre du concert :</p>
  <ul class="dlc-grid">{''.join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in COMPOSANTES)}</ul>
  {pic('setup',
       'David Lesage de profil, penché sur son handpan, éclairé en bleu dans la nuit ; devant lui un pad électronique lumineux carré, un micro sur pied et une tablette, et derrière lui des guirlandes de grosses ampoules.',
       '(max-width:900px) calc(100vw - 52px), 860px',
       'Instruments acoustiques, machines et voix : la matière électro-organique du concert.',
       cls='dlc-fig dlc-wide')}
</div></section>

<section class="dlc-block" id="salle"><div class="wrap">
  <div class="dlc-h">Le public</div>
  <h2 class="sec-title">Ce que fait une salle qui chante</h2>
  <p>La partie participative n’est pas un supplément : c’est le cœur du format. Le public chante des voyelles et découvre, projetée en direct, la figure que sa voix dessine sur l’eau — c’est la <b>cymatique</b>, expliquée pas à pas avant d’être vécue. Puis viennent les <b>échanges vocaux</b> : une ligne de chant lancée depuis la scène, que la salle renvoie.</p>
  <p>Les <b>vidéoprojections</b> et les ambiances sonores — nature, animaux — tiennent le fil visuel et donnent au plateau une profondeur qui fonctionne aussi bien dans une grande salle qu’en plein air.</p>
  <div class="dlc-duo">
    {pic('salle',
         'Vue depuis le public d’une grande salle : sur scène, une immense vidéoprojection de soleil orange, deux artistes minuscules devant leurs instruments, et au premier plan une forêt de bras levés.',
         '(max-width:860px) calc(100vw - 52px), 500px',
         'Vidéoprojection et salle debout : le moment participatif, à l’échelle d’un plateau.')}
    {pic('echo',
         'David Lesage seul sur une grande scène de festival en plein air, de dos, les bras ouverts vers un public nombreux assis et debout sous les arbres.',
         '(max-width:860px) calc(100vw - 52px), 500px',
         'L’échange vocal avec le public, en festival.')}
  </div>
</div></section>

<div class="divider"></div>

<section class="dlc-block band" id="parcours"><div class="wrap">
  <div class="dlc-h">Le parcours</div>
  <h2 class="sec-title">Conservatoire, Marciac, cinq octaves</h2>
  <div class="dlc-split">
    <div>
      <p>Musicien, chanteur et compositeur français. Ses instruments : la <b>voix</b>, le <b>handpan</b>, la <b>calebasse</b>, le <b>Ngoni</b> — la harpe africaine —, la wave drum et des déclencheurs électroniques.</p>
      <p>Son intention : des musiques <b>électro-organiques</b>, qui mêlent instruments acoustiques, musique électronique et voix humaine. Trois mots pour le situer : <b>soul française</b>, <b>African spirit</b>, <b>électro vibes</b>.</p>
    </div>
    {pic('portrait',
         'Portrait de David Lesage, cheveux longs et barbe courte, éclairé latéralement sur fond sombre.',
         '(max-width:860px) min(calc(100vw - 52px), 420px), 340px')}
  </div>
  <dl class="dlc-rep">{''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in REPERES)}</dl>
  <blockquote class="dlc-quote">Sous une humilité déconcertante, David Lesage présente avec excellence la grande technicité de son répertoire abouti ; rythmes envoûtants et envolées jazz d’une voix céleste. À découvrir en live absolument.<cite>Dossier de présentation du spectacle</cite></blockquote>
  {pic('proche',
       'David Lesage en gros plan sur scène, micro-casque au visage, main tendue vers le public, devant un décor de fils tendus colorés.',
       '(max-width:900px) calc(100vw - 52px), 860px',
       'Une adresse directe au public, du début à la fin du concert.',
       cls='dlc-fig dlc-wide')}
</div></section>

<section class="dlc-block" id="scenes"><div class="wrap">
  <div class="dlc-h">Scènes &amp; festivals</div>
  <h2 class="sec-title">Là où ce répertoire a résonné</h2>
  <p>D’un festival hongrois à une abbaye à ciel ouvert, d’une église toulousaine à une salle suisse et à un mont ivoirien : le même répertoire, à des échelles et sous des acoustiques très différentes.</p>
  <ul class="dlc-scenes">{''.join(f'<li><b>{n}</b><span>{p}</span></li>' for n, p in SCENES)}</ul>
  <p>David Lesage est passé par l’émission <i>The Voice</i> en 2021 ; c’est à sa suite qu’il a été invité pour un concert solo en Côte d’Ivoire.</p>
  {pic('rex',
       'Vue de scène du Grand Rex : deux artistes assis au sol au centre du plateau, face à une salle comble sur deux niveaux, dans les faisceaux de deux projecteurs en contre-jour.',
       '(max-width:900px) calc(100vw - 52px), 860px',
       'Au Grand Rex, devant 2 700 personnes.',
       cls='dlc-fig dlc-wide', credit=CREDIT_MAGYE)}
</div></section>

<div class="divider"></div>

<section class="dlc-block band" id="repertoire"><div class="wrap">
  <div class="dlc-h">Le répertoire</div>
  <h2 class="sec-title">Un album en deux opus, et quelques reprises</h2>
  <p>Le concert puise dans les compositions de l’artiste — un album en deux opus — et dans quelques reprises, ramenées au handpan et à la voix.</p>
  <div class="dlc-cols">
    <div class="dlc-card">
      <h3>Compositions</h3>
      <div class="sub">L’album, en deux opus</div>
      <ul>{''.join(f'<li>{t}</li>' for t in COMPOSITIONS)}</ul>
    </div>
    <div class="dlc-card">
      <h3>Reprises</h3>
      <div class="sub">Au handpan et à la voix</div>
      <ul>{''.join(f'<li>{t}<span>{a}</span></li>' for a, t in REPRISES)}</ul>
    </div>
  </div>
  <p>Cinq formules, empruntées au dossier de présentation, pour dire ce que cette musique cherche :</p>
  <ul class="dlc-cites">{''.join(f'<li>« {c} »</li>' for c in CITATIONS)}</ul>
</div></section>

<section class="dlc-block" id="option"><div class="wrap">
  <div class="dlc-h">En option</div>
  <h2 class="sec-title">La danse aérienne à l’élastique</h2>
  <p>Sur les plateaux qui le permettent, le concert peut accueillir <b>Iris Chasles</b> en <b>danse aérienne à l’élastique</b>, ainsi que des extraits du spectacle <a href="/e-motion">E-Motion</a>. Une silhouette suspendue au-dessus du plateau, portée par la musique jouée en direct.</p>
  <p>C’est une <b>option</b>, à décider avec vous en fonction du lieu.</p>
  <div class="dlc-duo">
    {pic('aerien',
         'Grande scène : à gauche David Lesage à son handpan sur un tapis, à droite Iris Chasles en tenue rouge suspendue à un élastique, en équilibre au sol, devant une vidéoprojection de nuages et de ciel bleu.',
         '(max-width:860px) calc(100vw - 52px), 500px',
         'Musique live et danse aérienne sur un même plateau — extrait d’E-Motion.')}
    {pic('aerien-fest',
         'Iris Chasles en tenue rouge, bras ouverts et regard vers le haut, suspendue à un élastique sur la scène en plein air de l’Everness Festival ; derrière elle, David Lesage joue debout à ses machines.',
         '(max-width:860px) calc(100vw - 52px), 500px',
         'Danse aérienne à l’élastique, Everness Festival.')}
  </div>
</div></section>

<div class="divider"></div>

<section class="dlc-block band" id="programmer"><div class="wrap">
  <div class="dlc-h">Programmation</div>
  <h2 class="sec-title">Programmer ce concert</h2>
  <p>La production est portée par <b>Résonances Productions</b>, association loi 1901 dédiée à l’art du spectacle vivant. Écrivez-nous : nous vous répondons avec le dossier de présentation et les précisions adaptées à votre lieu, à votre jauge et à vos dates.</p>
  <div class="dlc-prog">
    <h3>Un mot suffit pour commencer</h3>
    <p>Dites-nous simplement qui vous êtes, le lieu, et la période envisagée.</p>
    <div class="cta" style="margin-top:22px"><a class="btn" href="{MAILTO_PROG}">Programmer ce concert</a><a class="btn ghost" href="{MAILTO_DOSSIER}">Demander le dossier</a></div>
    <p style="margin-top:20px"><a href="mailto:{MAIL}">{MAIL}</a></p>
  </div>
  <div class="dlc-cross">
    <p>Vous cherchez plutôt une soirée à Paris ? Le même répertoire se joue aussi en version intimiste, au Nid, dans le 20<sup>e</sup> arrondissement : <a href="/concerts-david-lesage">les concerts de David Lesage au Nid</a>.</p>
  </div>
</div></section>

<a class="totop" href="#top" aria-label="Revenir en haut de la page">↑</a>

<footer id="contact"><div class="wrap">
  <div class="fgrid">
    <div>
      <div class="fbrand">Résonances Productions</div>
      <p style="margin-top:8px">Association loi 1901 — Art du spectacle vivant.<br>« l’humain, la vibration »</p>
    </div>
    <div>
      <h4>Contact</h4>
      <p><a href="mailto:{MAIL}">{MAIL}</a></p>
      <p><b>Siège social</b><br>2 impasse des Bleuets<br>09600 Aigues-Vives</p>
      <p><b>Adresse de correspondance</b><br>29 rue des Orteaux<br>75020 Paris</p>
      <p style="margin-top:8px"><a href="https://www.facebook.com/" target="_blank" rel="noopener">Facebook</a></p>
    </div>
    <div>
      <h4>Informations</h4>
      <p>SIRET : 919 514 075 00010</p>
      <p>Code APE : 9001Z<br>Arts du spectacle vivant</p>
      <p style="margin-top:8px"><a href="{HELLO_ASSO}" target="_blank" rel="noopener">Adhérer / soutenir</a></p>
      <p style="margin-top:8px"><a href="https://docs.google.com/document/d/1NxsbvaqHsA9VOXlN7cvsav7cxFwhsK4XCpowHb75o1w/edit?usp=sharing" target="_blank" rel="noopener">Statuts de l’association</a></p>
    </div>
  </div>
  <div class="legal">© 2026 Résonances Productions · resonancesproductions.org</div>
</div></footer>

<script>
(function(){{
  var b=document.querySelector('.totop'); if(!b) return;
  function upd(){{ b.classList.toggle('on', window.scrollY>700); }}
  upd(); window.addEventListener('scroll',upd,{{passive:true}});
}})();
</script>

</body></html>"""

HTML = mobile_nav.inject(HTML)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, 'david-lesage-en-concert')
os.makedirs(OUT_DIR, exist_ok=True)
OUT = os.path.join(OUT_DIR, 'index.html')
open(OUT, 'w', encoding='utf-8').write(HTML)
print('WROTE', OUT, round(len(HTML) / 1024), 'KB')
