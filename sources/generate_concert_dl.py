# -*- coding: utf-8 -*-
"""Genere la page dediee /concerts-david-lesage (concerts-david-lesage/index.html).

SOURCE DES FAITS : le dossier de presentation scenique de David Lesage
(Google Slides), pense pour de GRANDES SALLES. Cette page en garde l'essentiel
et le TRANSPOSE au cadre du Nid (atelier d'artiste, Paris 20e, public assis au
sol sur coussins et sieges bas, tout pres de l'artiste).

REGLES DE REDACTION (posees par David, 03/08/2026) :
  - « Ne mets rien en ce qui concerne les informations techniques de mon
    dossier, SEULEMENT DE L'ARTISTIQUE, DE LA MAGIE pour donner envie aux gens
    de venir. » => AUCUNE fiche technique, AUCUNE contrainte de salle, AUCUN
    materiel, AUCUNE jauge, AUCUNE duree affichee comme donnee logistique.
    La page doit faire DESIRER la soiree, pas informer un programmateur : on
    ecrit pour quelqu'un qui hesite a venir un soir de semaine.
  - AUCUN chiffre invente. Les seules donnees chiffrees affichees sont les deux
    dates fournies (10/10/2026 19 h, 28/11/2026 18 h) et les faits de parcours
    du dossier (4 ans, 5 octaves, 2012, The Voice 2021).
  - Le site VOUVOIE. Sobre et premium, pas d'empilement de superlatifs.
  - Les formules elogieuses du dossier (« Des envolees jazz d'une voix
    celeste »...) sont presentees COMME DES CITATIONS attribuees au dossier de
    presentation, jamais comme des affirmations de l'association.
  - PAS de danse aerienne a l'elastique / pas d'extraits d'E-Motion :
    impossible au Nid (tranche par David). En revanche la DANSE DE
    TOURNOIEMENT d'Iris Chasles (co-fondatrice) est mentionnee comme une
    invitation POSSIBLE sur certaines dates, jamais comme une garantie.
  - Boutons « Reserver ma place » vers la billetterie HelloAsso : hero, chaque
    date, bas de page. >= 16 px, hauteur cliquable >= 44 px.

  - « BOIRE L'EAU DU CONCERT » (ajout du 04/08/2026) : le son du concert est
    envoye EN DIRECT dans l'eau d'une fontaine Melusine specialement modifiee
    (partenariat AquaDyn Auroville + Rebirth Water Group), et le public boit
    cette eau en fin de soiree. PRUDENCE DE REGISTRE ABSOLUE : on n'affirme
    AUCUN bienfait pour la sante, aucune vertu therapeutique, aucune
    « structuration » ni « information » de l'eau. Le brevet son/lumiere est
    ATTRIBUE a ses concepteurs, jamais affirme par l'association. Le mot de la
    pancarte de David, « experimente », porte tout le registre : une invitation
    a l'experience, pas une promesse. Voir le commentaire HTML de la section
    #eau avant toute retouche.

IMAGES : aucune image telechargee de l'exterieur, aucune image distante servie
par la page. La page REUTILISE des declinaisons deja presentes dans le depot
(voir CDL_PHOTOS) et utilise 3 images qui lui sont propres dans
/img/concert-dl/. Ni la photo du tournoiement ni les autres reutilisees ne font
partie des 4 photos filigranees qui exigent le credit MAGYE D'ART (verifie sur
/e-motion).
VIDEO : la video de cymatique est un LIEN SORTANT sur une vignette locale, pas
un iframe YouTube — aucun script ni cookie tiers charge par le site. La vignette
n'existe qu'en 480x360 : ne jamais l'afficher plus large (cf. .cdl-video).
La seconde video de David (chant des voyelles avec CymaScope, note par note)
fait partie du programme PAYANT « Les Trois Piliers » : NE PAS l'integrer ni la
lier.
MANQUENT : des photos dediees d'un concert SOLO AU NID (David seul, public au
sol). A verifier avec David : la 2e photo de la fontaine
(fontaine-melusine-*) montre une salle VOUTEE EN PIERRE, qui ne ressemble pas
au Nid — la legende ne nomme donc aucun lieu.

Usage :
    python3 sources/generate_concert_dl.py
    -> ecrit directement concerts-david-lesage/index.html
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mobile_nav  # noqa: E402

ADHESION = ('https://www.helloasso.com/beta/associations/resonances-productions/adhesions/'
            'adhesion-resonances-productions')
BILLET = ('https://www.helloasso.com/associations/resonances-productions/evenements/'
          'concert-intimiste-david-lesage-au-coeur-de-paris-1')
# Vidéo publique de la chaîne de David Lesage (titre verifie par oEmbed le 04/08/2026 :
# « Chant des voyelles live concert David Lesage »). On NE l'integre PAS en iframe :
# vignette locale + lien sortant, pour ne charger aucun script ni cookie tiers.
VIDEO_CYMA = 'https://www.youtube.com/watch?v=mPUrsusmYyQ'
MELUSINE = 'https://aquadynauroville.com/site/accueil-25/fontaine-melusine/'

# --- Images reutilisees du depot -------------------------------------------
# cle : (dossier, base, [largeurs disponibles], largeur_intrinseque, hauteur_intrinseque)
CDL_PHOTOS = {
    'hero': ('rituals', 'un-univers-musical-electro-organique', [480, 900, 1400], 1400, 778),
    'salon': ('le-nid', 'hero-nid', [800, 1200, 1800, 2400], 2400, 1350),
    'cercle': ('soin-soa', 'cercle-au-nid', [480, 768], 768, 1344),
    'tournoiement': ('e-motion', 'la-danse-de-tournoiement', [480, 900], 900, 900),
    'portrait': ('rituals', 'david-lesage', [480, 900, 1400], 1400, 1400),
    'scene': ('rituals', 'chanter-ensemble', [480, 900, 1400], 1400, 780),
    # Photos propres a cette page (fournies par David, dossier /img/concert-dl/).
    # Ratio natif 4:3 (1280x960) pour les deux photos de la fontaine.
    'eau': ('concert-dl', 'eau-du-concert', [480, 900, 1280], 1280, 960),
    'fontaine': ('concert-dl', 'fontaine-melusine', [480, 900, 1280], 1280, 960),
    # Vignette de la video YouTube : 480x360 = la MEILLEURE resolution disponible.
    # Ne jamais l'afficher plus large que 480 px (sinon flou) -> .cdl-video est borne.
    'video': ('concert-dl', 'cymatique-video', [480], 480, 360),
}


def pic(key, alt, sizes, caption=None, cls='cdl-fig', loading='lazy'):
    """<picture> WebP + repli JPEG, srcset complet, width/height, alt factuel."""
    folder, base, widths, w, h = CDL_PHOTOS[key]
    root = f'/img/{folder}/{base}'
    webp = ', '.join(f'{root}-{x}.webp {x}w' for x in widths)
    jpg = ', '.join(f'{root}-{x}.jpg {x}w' for x in widths)
    big = f'{root}-{widths[-1]}.jpg'
    prio = ' fetchpriority="high"' if loading == 'eager' else ''
    img = (f'<picture><source type="image/webp" srcset="{webp}" sizes="{sizes}">'
           f'<img src="{big}" srcset="{jpg}" sizes="{sizes}" width="{w}" height="{h}" '
           f'loading="{loading}"{prio} decoding="async" alt="{alt}"></picture>')
    cap = f'<figcaption>{caption}</figcaption>' if caption else ''
    return f'<figure class="{cls}">{img}{cap}</figure>'


def video_link(key, href, alt, label, sub, sizes):
    """Vignette LOCALE cliquable vers YouTube : aucun iframe, aucun script tiers,
    aucun cookie depose par le site. Le triangle de lecture est purement CSS et
    aria-hidden : le libelle du lien reste explicite pour les lecteurs d'ecran."""
    folder, base, widths, w, h = CDL_PHOTOS[key]
    root = f'/img/{folder}/{base}'
    webp = ', '.join(f'{root}-{x}.webp {x}w' for x in widths)
    jpg = ', '.join(f'{root}-{x}.jpg {x}w' for x in widths)
    img = (f'<picture><source type="image/webp" srcset="{webp}" sizes="{sizes}">'
           f'<img src="{root}-{widths[-1]}.jpg" srcset="{jpg}" sizes="{sizes}" '
           f'width="{w}" height="{h}" loading="lazy" decoding="async" alt="{alt}"></picture>')
    return (f'<a class="cdl-video" href="{href}" target="_blank" rel="noopener">'
            f'<figure class="cdl-fig"><span class="shot">{img}'
            f'<span class="play" aria-hidden="true"></span></span>'
            f'<figcaption><span class="vlabel">{label}</span>'
            f'<span class="vsub">{sub}</span></figcaption></figure></a>')


# --- Contenu ---------------------------------------------------------------
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

SCENES = [
    ('Abbaye à ciel ouvert d’Alet-les-Bains', 'France'),
    ('Église San Subra, Toulouse', 'France'),
    ('Salle du Castillo, Vevey', 'Suisse'),
    ('Mont Korhogo', 'Côte d’Ivoire'),
]

DATES = [
    ('Samedi 10 octobre 2026', '19 h', '2026-10-10T19:00'),
    ('Samedi 28 novembre 2026', '18 h', '2026-11-28T18:00'),
]

TOC = [
    ('#soiree', 'La soirée'),
    ('#au-nid', 'À quelques pas, assis au sol'),
    ('#voir-sa-voix', 'Voir sa voix'),
    ('#eau', 'Boire l’eau du concert'),
    ('#invitee', 'Une invitée, certains soirs'),
    ('#artiste', 'L’artiste'),
    ('#repertoire', 'Le répertoire'),
    ('#scenes', 'Là où ce répertoire a résonné'),
    ('#dates', 'Dates & réservation'),
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
/* nav */
/* Cibles tactiles : les liens de la barre sont en inline-flex + min-height 44px,
   et le padding vertical du .nav est ramene a 8px pour que la barre garde la
   meme hauteur qu'ailleurs sur le site (8 + 44 + 8 = 60px). */
.nav{position:fixed;top:0;left:0;right:0;z-index:40;display:flex;align-items:center;justify-content:space-between;padding:8px 26px;background:rgba(14,15,36,.6);backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.05)}
.nav .brand{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:19px;letter-spacing:.12em;color:#fff;text-transform:uppercase;display:inline-flex;align-items:center;min-height:44px}
.nav .links{display:flex;align-items:center;gap:19px;font-size:13.5px;letter-spacing:.04em}
.nav .links a{color:var(--muted);transition:color .2s;display:inline-flex;align-items:center;min-height:44px}
.nav .links a:hover{color:var(--gold2)}
.nav .adh{color:#1a1608!important;background:var(--gold);padding:0 17px;border-radius:30px;font-weight:600}
@media(max-width:760px){.nav .links a:not(.adh){display:none}}
/* La barre porte 10 entrees : on resserre entre 861 et 1080 px (sous 861 px =
   hamburger). On ne descend jamais sous 13 px (plancher typographique du site) :
   dans la bande la plus etroite on masque « Statuts » puis « L'association »,
   qui restent joignables depuis le pied de page et l'accueil. */
@media(min-width:861px) and (max-width:1080px){.nav{padding:8px 18px}.nav .brand{font-size:17px;white-space:nowrap}.nav .links{gap:9px;font-size:13px}.nav .adh{padding:0 14px}}
@media(min-width:861px) and (max-width:1080px){.nav .links a[href="/#statuts"]{display:none}}
@media(min-width:861px) and (max-width:980px){.nav .links a[href="/#association"]{display:none}}
.nav .links a[aria-current="page"]{color:var(--gold2)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;background:var(--gold);color:#1a1608;font-weight:600;padding:14px 28px;border-radius:40px;font-size:16px;min-height:48px;transition:transform .2s,box-shadow .2s}
.btn:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(216,178,90,.28)}
.btn.ghost{background:transparent;color:var(--gold2);border:1px solid var(--line)}
.cta{display:flex;gap:14px;flex-wrap:wrap}
/* ===== Concerts de David Lesage ===== */
.cdl-top{padding:128px 0 70px;background:radial-gradient(900px 560px at 12% -8%,rgba(143,122,209,.20),transparent 62%),radial-gradient(700px 460px at 90% 102%,rgba(216,178,90,.12),transparent 62%),linear-gradient(180deg,#0b0c1e,var(--night))}
.cdl-top h1{font-size:clamp(38px,7vw,72px);font-weight:600;line-height:1.02;color:#fff;letter-spacing:.02em}
.band{background:linear-gradient(180deg,#0b0c1e,var(--night))}
.tagline{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(19px,2.8vw,28px);margin-top:12px}
.cdl-h{color:var(--gold);font-size:13px;letter-spacing:.22em;text-transform:uppercase;font-weight:600;margin-bottom:10px}
.cdl-block p{max-width:820px;color:#d7d4ea;margin-top:16px}
.cdl-fig{margin:0;border-radius:16px;overflow:hidden;border:1px solid var(--line);background:var(--card)}
.cdl-fig img{display:block;width:100%;height:auto}
.cdl-fig figcaption{color:var(--muted);font-size:13.5px;line-height:1.55;padding:12px 16px 14px;border-top:1px solid rgba(255,255,255,.06)}
.cdl-hero-fig{margin-top:34px}
.cdl-wide{max-width:820px;margin-top:26px}
/* photo verticale (768x1344) : bornee, sinon elle mangerait tout l'ecran en pile */
.cdl-portrait{max-width:420px}
.cdl-quote{margin:34px 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(21px,3vw,28px);line-height:1.35;border-left:2px solid var(--gold);padding-left:22px;max-width:760px}
.cdl-note{background:var(--card);border:1px solid rgba(255,255,255,.07);border-left:2px solid var(--gold);border-radius:14px;padding:19px 22px;margin-top:24px;max-width:820px}
.cdl-note p{color:#d7d4ea;font-size:15.5px;margin:0;line-height:1.7;max-width:none}
.cdl-note p+p{margin-top:10px}
/* deux colonnes : texte + figure */
.cdl-split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,340px);gap:36px;align-items:start;margin-top:30px}
.cdl-split>div>p:first-child{margin-top:0}
@media(max-width:860px){.cdl-split{grid-template-columns:1fr;gap:26px}}
/* cartes du repertoire */
.cdl-cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:20px;margin-top:30px;align-items:start}
.cdl-card{background:var(--card);border:1px solid rgba(255,255,255,.06);border-left:2px solid var(--gold);border-radius:14px;padding:24px 26px}
.cdl-card h3{font-family:'Cormorant Garamond',Georgia,serif;font-size:24px;color:#fff;font-weight:600;line-height:1.15}
.cdl-card .sub{color:var(--muted);font-size:14px;font-style:italic;margin-top:3px}
.cdl-card ul{list-style:none;margin-top:16px}
.cdl-card li{color:#d7d4ea;font-size:15.5px;padding:7px 0;border-bottom:1px solid rgba(255,255,255,.05);line-height:1.5}
.cdl-card li:last-child{border-bottom:0}
.cdl-card li span{color:var(--gold2);display:block;font-size:13.5px;letter-spacing:.04em}
/* citations du dossier */
.cdl-cites{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px;max-width:880px;list-style:none}
.cdl-cites li{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:17.5px;line-height:1.4;background:rgba(216,178,90,.08);border:1px solid var(--line);border-radius:30px;padding:8px 20px}
/* ===== Boire l'eau du concert =====
   Section volontairement PLAIN (pas .band) pour ne pas casser l'alternance
   band / non-band des sections suivantes : elle prend a la place un halo bleu
   qui lui est propre. Encadree de deux .divider comme les autres. */
.cdl-water{background:radial-gradient(760px 500px at 86% 4%,rgba(70,132,214,.17),transparent 64%),radial-gradient(620px 420px at 4% 98%,rgba(143,122,209,.11),transparent 62%)}
.cdl-duo{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px;margin-top:30px;max-width:820px;align-items:start}
/* ===== Vignette video (aucun lecteur tiers : image locale + lien sortant) =====
   La source ne fait que 480 px de large : on ne l'agrandit JAMAIS au-dela. */
.cdl-video{display:block;max-width:480px;margin-top:26px}
.cdl-video figure{margin:0}
.cdl-video .shot{display:block;position:relative;line-height:0}
.cdl-video .play{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:62px;height:62px;border-radius:50%;background:rgba(11,12,30,.72);border:1px solid rgba(240,209,138,.62);display:flex;align-items:center;justify-content:center;transition:transform .2s,background .2s}
.cdl-video .play::before{content:"";width:0;height:0;border-left:17px solid var(--gold2);border-top:11px solid transparent;border-bottom:11px solid transparent;margin-left:5px}
.cdl-video:hover .play{background:rgba(11,12,30,.9);transform:translate(-50%,-50%) scale(1.06)}
.cdl-video figcaption{display:flex;flex-direction:column;gap:2px;justify-content:center;min-height:44px}
.cdl-video .vlabel{color:var(--gold2);font-size:16px;text-decoration:underline;text-decoration-color:rgba(216,178,90,.42);text-underline-offset:3px}
.cdl-video:hover .vlabel{color:#fff}
.cdl-video .vsub{color:var(--muted);font-size:13.5px}
/* scenes */
.cdl-scenes{list-style:none;margin-top:24px;max-width:820px;display:grid;gap:2px}
.cdl-scenes li{display:flex;gap:16px;align-items:baseline;flex-wrap:wrap;color:#d7d4ea;font-size:16px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.06)}
.cdl-scenes li:last-child{border-bottom:0}
.cdl-scenes li b{flex:1 1 260px;min-width:0}
.cdl-scenes li span{color:var(--gold);font-size:13.5px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;flex:0 0 auto}
/* dates */
.cdl-dates{display:grid;gap:16px;margin-top:30px;max-width:820px}
.cdl-date{background:linear-gradient(160deg,rgba(216,178,90,.12),var(--card));border:1px solid var(--line);border-radius:16px;padding:24px 26px;display:flex;gap:20px;align-items:center;justify-content:space-between;flex-wrap:wrap}
.cdl-date .when{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(22px,3.4vw,29px);color:#fff;font-weight:600;line-height:1.15}
.cdl-date .where{color:var(--gold2);font-size:15px;margin-top:4px}
@media(max-width:560px){.cdl-date{padding:22px}.cdl-date .btn{width:100%}}
/* sommaire */
.toc{margin-top:44px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:22px 0}
.toc .cdl-h{margin-bottom:14px}
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
/* ce bloc final est plus specifique que le resserrement 861-1080 px plus haut :
   on y redonne donc explicitement le 13px de la bande etroite (plancher typo). */
@media(min-width:861px) and (max-width:1080px){.nav .links a{font-size:13px}}
p a:not(.btn):not(.adh),li a:not(.btn):not(.adh){font-size:inherit;text-decoration:underline;
  text-decoration-color:rgba(216,178,90,.4);text-underline-offset:3px}
.cdl-note a{display:inline-block;padding:11px 0}
/* meme traitement pour le lien partenaire de la section « eau » : cible >= 44 px
   (17px * 1.75 = 29.75 + 2 x 11 = 51.75). */
.cdl-water p a{display:inline-block;padding:11px 0}
"""

TITLE = ('Concerts de David Lesage — concert-cérémonie participatif au Nid, '
         'Paris 20ᵉ · Résonances Productions')
DESC = ('Voix, handpan, calebasse et Ngoni : le concert-cérémonie participatif de '
        'David Lesage, au Nid (Paris 20ᵉ). Assis au sol, à quelques pas de l’artiste — '
        'on entre en spectateur, on ressort en ayant chanté. Prochaines dates : '
        '10 octobre et 28 novembre 2026.')

HTML = f"""<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="Concerts de David Lesage — au Nid, Paris 20ᵉ">
<meta property="og:description" content="Un concert-cérémonie participatif : voix, handpan, calebasse et Ngoni. Au Nid, assis au sol à quelques pas de l’artiste — on entre en spectateur, on ressort en ayant chanté.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.resonancesproductions.org/concerts-david-lesage">
<meta property="og:image" content="https://www.resonancesproductions.org/img/rituals/un-univers-musical-electro-organique-1400.jpg">
<meta property="og:image:width" content="1400">
<meta property="og:image:height" content="778">
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
    <a href="/concerts-david-lesage" aria-current="page">Concerts</a>
    <a href="/le-nid">Le Nid</a>
    <a href="/le-soin-soa">Le Soin Soa</a>
    <a href="/#statuts">Statuts</a>
    <a href="#contact">Contact</a>
    <a class="adh" href="{ADHESION}" target="_blank" rel="noopener">Adhérer</a>
  </div>
</nav>

<header class="cdl-top"><div class="wrap">
  <div class="kick">Concert · Le Nid, Paris 20<sup>e</sup></div>
  <h1>Concerts de David Lesage</h1>
  <div class="tagline">« Un profond voyage au cœur de soi »</div>
  <p class="lead">La voix, le handpan, la calebasse et le Ngoni — la harpe africaine. Une soirée de musique live où l’on ne reste pas longtemps spectateur.</p>
  <p class="body">Un <b>concert-cérémonie participatif</b>, dans un atelier d’artiste du 20<sup>e</sup> arrondissement de Paris. Vous êtes assis au sol, à quelques pas des instruments. La musique commence doucement — et à un moment de la soirée, c’est votre voix qui répond.</p>
  <div class="cta" style="margin-top:26px"><a class="btn" href="{BILLET}" target="_blank" rel="noopener">Réserver ma place</a><a class="btn ghost" href="#dates">Voir les prochaines dates →</a></div>
  {pic('hero',
       'David Lesage seul en concert, penché sur son handpan, éclairé en bleu ; à côté de lui un contrôleur électronique et un micro sur pied, et derrière lui des guirlandes lumineuses dans la nuit.',
       '(max-width:1080px) calc(100vw - 52px), 1028px',
       'Voix, handpan et machines : l’univers électro-organique de David Lesage.',
       cls='cdl-fig cdl-hero-fig', loading='eager')}
  <nav class="toc" aria-label="Sommaire de la page"><div class="cdl-h">Sommaire</div><ol>{''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in TOC)}</ol></nav>
</div></header>

<section class="cdl-block" id="soiree"><div class="wrap">
  <div class="cdl-h">La soirée</div>
  <h2 class="sec-title">On entre en spectateur, on ressort en ayant chanté</h2>
  <p>Ce n’est pas tout à fait un concert, pas tout à fait une cérémonie. La soirée respire en deux temps qui alternent : des moments où l’on se laisse simplement traverser, et des moments où le public devient une partie de la musique.</p>
  <p>Les chansons se disent en français et en langues du monde — swahili, sanskrit. Les instruments acoustiques y croisent les machines : le handpan, la calebasse, le Ngoni, et une voix qui passe de la soul au chant lyrique dans la même phrase. David parle d’une musique <b>électro-organique</b> : les machines sont là, mais la musique a gardé un corps.</p>
  <p>Entre les morceaux, il parle. De vulnérabilité masculine, de spiritualité, d’amour — de ces choses qui sont au cœur de l’humain et qu’on n’entend pas souvent dire à voix haute, dans une pièce, par quelqu’un qui les assume.</p>
  <p class="cdl-quote">Un profond voyage au cœur de soi.</p>
  <p>Rien ne vous est demandé. Chanter est une invitation — on peut aussi passer la soirée à écouter, les yeux fermés.</p>
</div></section>

<div class="divider"></div>

<section class="cdl-block band" id="au-nid"><div class="wrap">
  <div class="cdl-h">Au Nid</div>
  <h2 class="sec-title">À quelques pas, assis au sol</h2>
  <div class="cdl-split">
    <div>
      <p>Ce format est né sur de grandes scènes : des abbayes, des églises, des festivals. Au <b>Nid</b>, il se resserre. Le Nid est un atelier d’artiste du 20<sup>e</sup> arrondissement : du parquet ancien, de grandes verrières, des coussins et des sièges bas disposés en cercle, et les instruments posés là, au milieu, à portée de regard.</p>
      <p>Ce resserrement change moins le contenu de la soirée que sa température. Dans une grande salle, chanter avec l’artiste demande un peu de courage. Ici, tout le monde s’entend, personne ne se cache, et la voix de la personne assise à côté de vous vous porte autant que la musique.</p>
      <p>On se déchausse en entrant. On s’assoit par terre. Et très vite, il n’y a plus de scène.</p>
    </div>
    {pic('salon',
         'Le salon du Nid : des sièges bas et des coussins disposés en cercle sur le parquet autour d’un tapis rond, deux handpans posés au sol au premier plan, de grandes verrières et des plantes.',
         '(max-width:860px) calc(100vw - 52px), 340px',
         'Le Nid avant une soirée : le cercle de sièges bas, les handpans au sol.')}
  </div>
</div></section>

<section class="cdl-block" id="voir-sa-voix"><div class="wrap">
  <div class="cdl-h">Voir sa voix</div>
  <h2 class="sec-title">Ce que votre voix fait à l’eau</h2>
  <div class="cdl-split">
    <div>
      <p>Un moment de la soirée est consacré à la <b>cymatique</b> : ce qui arrive à l’eau quand on chante devant elle. David raconte comment la vibration sonore agit sur l’eau — et donc sur nous, qui en sommes faits pour l’essentiel. Puis il invite chacun à chanter quelques voyelles. À l’écran, en temps réel, une figure apparaît : l’empreinte de cette voix-là.</p>
      <p>Ce moment a été filmé lors d’un concert : on y entend le public chanter, et on y voit la figure se dessiner à l’écran.</p>
      {video_link('video', VIDEO_CYMA,
                  'Vignette de la vidéo : vue grand-angle d’un concert, une figure de cymatique '
                  'projetée sur l’écran derrière les instruments ; titre incrusté sur l’image, '
                  '« Le chant des voyelles, live concert David Lesage — Cymatique en temps réel ».',
                  'Voir la vidéo sur YouTube ↗',
                  '« Chant des voyelles live concert David Lesage » — chaîne de l’artiste, '
                  's’ouvre dans un nouvel onglet.',
                  '(max-width:600px) calc(100vw - 52px), 480px')}
      <p>Le reste de la soirée avance de la même façon, par images et par échos. Des sons de nature et d’animaux ouvrent des paysages. Des vidéoprojections accompagnent les morceaux. Des phrases simples reviennent comme des refrains. Et régulièrement, l’artiste lance une ligne de chant que la salle lui renvoie.</p>
    </div>
    {pic('cercle',
         'Un petit groupe assis sur des coussins de jonc, en cercle sur le parquet, autour d’un handpan et de bols chantants, dans la grande pièce mansardée du Nid éclairée par des verrières.',
         '(max-width:860px) min(calc(100vw - 52px), 420px), 340px',
         'Au Nid, tout se joue en cercle, à même le sol.',
         cls='cdl-fig cdl-portrait')}
  </div>
</div></section>

<div class="divider"></div>

<!-- PRUDENCE DE REGISTRE (impose par David, 04/08/2026) : cette section
     n'affirme AUCUN bienfait pour la sante, aucune vertu therapeutique, aucune
     « structuration » ou « information » de l'eau. On s'en tient a ce qui est
     verifiable et vecu : un partenariat, une fontaine modifiee, le son du
     concert envoye dans l'eau, et le fait de la boire. Le brevet son/lumiere
     est ATTRIBUE a ses concepteurs, jamais affirme par l'association. Le mot
     de la pancarte de David (« experimente ») porte tout le registre : une
     invitation a l'experience, pas une promesse. NE RIEN AJOUTER ICI qui
     ressemble a un effet promis. -->
<section class="cdl-block cdl-water" id="eau"><div class="wrap">
  <div class="cdl-h">Le son dans l’eau</div>
  <h2 class="sec-title">Boire l’eau du concert</h2>
  <p>Dans un coin de la pièce, une fontaine attend, son réservoir éclairé de bleu. Elle n’est pas là pour décorer : pendant le concert, le son qui remplit la salle est aussi envoyé, <b>en direct</b>, dans l’eau qu’elle contient. À la fin de la soirée, on remplit un gobelet — et on boit cette eau.</p>
  <p>Un concert, d’ordinaire, on l’écoute. Celui-là, on peut aussi le boire.</p>
  <div class="cdl-duo">
    {pic('eau',
         'Une fontaine à eau au réservoir éclairé en bleu, posée sur une table à côté d’une '
         'carafe et de rangées de gobelets en carton ; derrière, une pancarte manuscrite : '
         '« Eau bio compatible — expérimente — Bois l’eau du concert ».',
         '(max-width:600px) calc(100vw - 52px), (max-width:900px) calc(50vw - 36px), 400px',
         'La fontaine et les gobelets, en fin de concert. Sur la pancarte, un seul mot : « expérimente ».')}
    {pic('fontaine',
         'Gros plan sur la fontaine : son étiquette porte le logo Rebirth Water Group ; '
         'à l’arrière-plan, une salle de concert voûtée en pierre, les instruments installés '
         'et des coussins bleus posés au sol.',
         '(max-width:600px) calc(100vw - 52px), (max-width:900px) calc(50vw - 36px), 400px',
         'La fontaine installée en bord de scène, avant l’arrivée du public.')}
  </div>
  <p>Ce dispositif existe grâce à un partenariat avec <b>AquaDyn Auroville</b> et <b>Rebirth Water Group</b>, concepteurs de la <a href="{MELUSINE}" target="_blank" rel="noopener">fontaine Mélusine ↗</a> — un appareil bâti autour du son et de la lumière, dont ses concepteurs revendiquent le brevet. L’exemplaire qui voyage avec les instruments a été spécialement modifié pour recevoir le signal audio du concert.</p>
  <p>Sur la pancarte posée à côté, un seul mot fait office de mode d’emploi : <b>« expérimente »</b>. Rien ne vous est promis, rien ne vous est démontré : on vous tend un gobelet, et vous en faites ce que vous voulez — le boire, ou passer votre tour.</p>
</div></section>

<div class="divider"></div>

<section class="cdl-block band" id="invitee"><div class="wrap">
  <div class="cdl-h">Une invitée</div>
  <h2 class="sec-title">Certains soirs, une danse au centre du cercle</h2>
  <div class="cdl-split">
    <div>
      <p>Il arrive que la soirée accueille <b>Iris Chasles</b>, co-fondatrice de l’association, pour une <b>danse de tournoiement</b> : une silhouette qui tourne, longtemps, portée par la musique, jusqu’à ce que la pièce entière semble tourner avec elle.</p>
      <p>Ce n’est pas au programme de chaque date. Quand c’est le cas, c’est annoncé.</p>
    </div>
    {pic('tournoiement',
         'Iris Chasles en danse de tournoiement, un bras levé vers le haut, le visage tourné vers sa main, dans une lumière rose et rouge devant un mur de pierre.',
         '(max-width:860px) min(calc(100vw - 52px), 420px), 340px',
         'La danse de tournoiement, invitée sur certaines soirées.',
         cls='cdl-fig cdl-portrait')}
  </div>
</div></section>

<section class="cdl-block" id="artiste"><div class="wrap">
  <div class="cdl-h">L’artiste</div>
  <h2 class="sec-title">David Lesage</h2>
  <div class="cdl-split">
    <div>
      <p>Musicien, chanteur et compositeur français. Ses instruments de prédilection : la <b>voix</b>, le <b>handpan</b>, la <b>calebasse</b> et le <b>Ngoni</b> — la harpe africaine.</p>
      <p>Batteur depuis l’âge de quatre ans, il obtient un prix de batterie avec mention très bien au Conservatoire National de Toulouse, puis se forme à la batterie, au chant et à l’improvisation vocale au collège de Jazz in Marciac. Son <b>ambitus vocal de cinq octaves</b> lui permet de voyager de la pop à la soul, du lyrique au gospel, de la chanson française au rap.</p>
      <p>En 2012, il rencontre la calebasse et le Ngoni, et se met à explorer les sonorités et les rythmes africains. Après son passage dans l’émission <i>The Voice</i> en 2021, il est invité pour un concert solo en <b>Côte d’Ivoire</b>.</p>
      <p>Il collabore avec <b>Neotone</b>, dont il est ambassadeur du handpan électronique, et avec <b>Yishama</b>, fabricant de handpans d’exception.</p>
      <p>Son intention : produire des musiques <b>électro-organiques</b>, qui mêlent instruments acoustiques, musique électronique et voix humaine. Un univers qu’il décrit comme « sensible, subtil, structuré, contenu par un sens du rythme millimétrique ». Trois mots pour le situer : <b>soul française</b>, <b>African spirit</b>, <b>électro vibes</b>.</p>
    </div>
    {pic('portrait',
         'Portrait de David Lesage, cheveux longs et barbe courte, éclairé latéralement sur fond sombre.',
         '(max-width:860px) min(calc(100vw - 52px), 420px), 340px')}
  </div>
</div></section>

<div class="divider"></div>

<section class="cdl-block band" id="repertoire"><div class="wrap">
  <div class="cdl-h">Le répertoire</div>
  <h2 class="sec-title">Ses compositions, et quelques reprises</h2>
  <p>La soirée puise dans ses compositions — un album en deux opus — et dans quelques reprises, ramenées au handpan et à la voix.</p>
  <div class="cdl-cols">
    <div class="cdl-card">
      <h3>Compositions</h3>
      <div class="sub">L’album, en deux opus</div>
      <ul>{''.join(f'<li>{t}</li>' for t in COMPOSITIONS)}</ul>
    </div>
    <div class="cdl-card">
      <h3>Reprises</h3>
      <div class="sub">Au handpan et à la voix</div>
      <ul>{''.join(f'<li>{t}<span>{a}</span></li>' for a, t in REPRISES)}</ul>
    </div>
  </div>
  <p>Cinq formules, empruntées au dossier de présentation du spectacle, pour dire ce que cette musique cherche :</p>
  <ul class="cdl-cites">{''.join(f'<li>« {c} »</li>' for c in CITATIONS)}</ul>
</div></section>

<section class="cdl-block" id="scenes"><div class="wrap">
  <div class="cdl-h">Sur scène</div>
  <h2 class="sec-title">Là où ce répertoire a résonné</h2>
  <p>D’une abbaye à ciel ouvert à une église toulousaine, d’une salle suisse à un mont ivoirien : le même répertoire, à des échelles très différentes.</p>
  <ul class="cdl-scenes">{''.join(f'<li><b>{n}</b><span>{p}</span></li>' for n, p in SCENES)}</ul>
  <p>David Lesage est également passé par l’émission <i>The Voice</i> en 2021.</p>
  {pic('scene',
       'David Lesage seul sur une grande scène de festival en plein air, de dos, les bras ouverts vers un public nombreux assis et debout sous les arbres.',
       '(max-width:1080px) calc(100vw - 52px), 1028px',
       'Le même geste, à une autre échelle : l’échange vocal avec le public, en festival.',
       cls='cdl-fig cdl-wide')}
</div></section>

<div class="divider"></div>

<section class="cdl-block band" id="dates"><div class="wrap">
  <div class="cdl-h">Dates &amp; réservation</div>
  <h2 class="sec-title">Prochaines dates au Nid</h2>
  <p>Le cercle est petit : on réserve à l’avance, en ligne.</p>
  <div class="cdl-dates">
    {''.join(f'''<div class="cdl-date">
      <div><div class="when"><time datetime="{iso}">{d}</time> — {h}</div><div class="where">Le Nid, Paris 20<sup>e</sup></div></div>
      <a class="btn" href="{BILLET}" target="_blank" rel="noopener">Réserver ma place</a>
    </div>''' for d, h, iso in DATES)}
  </div>
  <div class="cdl-note">
    <p>L’adresse et les précisions vous parviennent avec votre confirmation de réservation.</p>
    <p>D’autres dates, et tous les autres rendez-vous du lieu, sur l’agenda : <a href="/le-nid#concerts">les concerts au Nid</a> · <a href="/le-nid#agenda">l’agenda complet</a>.</p>
  </div>
  <div class="cta" style="margin-top:28px"><a class="btn" href="{BILLET}" target="_blank" rel="noopener">Réserver ma place</a><a class="btn ghost" href="mailto:contact@resonancesproductions.org?subject=Concert%20de%20David%20Lesage%20au%20Nid">Poser une question</a></div>
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
      <p><a href="mailto:contact@resonancesproductions.org">contact@resonancesproductions.org</a></p>
      <p><b>Siège social</b><br>2 impasse des Bleuets<br>09600 Aigues-Vives</p>
      <p><b>Adresse de correspondance</b><br>29 rue des Orteaux<br>75020 Paris</p>
      <p style="margin-top:8px"><a href="https://www.facebook.com/" target="_blank" rel="noopener">Facebook</a></p>
    </div>
    <div>
      <h4>Informations</h4>
      <p>SIRET : 919 514 075 00010</p>
      <p>Code APE : 9001Z<br>Arts du spectacle vivant</p>
      <p style="margin-top:8px"><a href="{ADHESION}" target="_blank" rel="noopener">Adhérer / soutenir</a></p>
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
OUT_DIR = os.path.join(ROOT, 'concerts-david-lesage')
os.makedirs(OUT_DIR, exist_ok=True)
OUT = os.path.join(OUT_DIR, 'index.html')
open(OUT, 'w', encoding='utf-8').write(HTML)
print('WROTE', OUT, round(len(HTML) / 1024), 'KB')
