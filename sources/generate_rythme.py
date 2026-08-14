# -*- coding: utf-8 -*-
"""Generateur de la page /rythme-calebasse (Resonances Productions).

Deux etapes independantes :

1. LES IMAGES — a partir des photos originales dans `sources/rythme_img/`,
   produit dans `img/rythme-calebasse/` trois largeurs (480 / 900 / 1400,
   plafonnees a la largeur natale) en WebP + repli JPEG. Si le dossier des
   originaux est absent, l'etape est simplement sautee (les images deja
   generees restent en place) — meme comportement que les autres generateurs
   du depot.

2. LA PAGE — ecrit `rythme-calebasse/index.html`.

Sources du contenu :
  - https://sites.google.com/lesagedavid.fr/now-groove/la-calebasse (methode
    « Now Groove » de David Lesage) : la calebasse, les infra-basses, les oeufs,
    la calebasse signature, le deroule de l'atelier, les bienfaits, la bio.
  - https://sites.google.com/lesagedavid.fr/now-groove/faq : le sol dur.
  - Dossier de presentation de David : format des interventions (2 h, jusqu'a
    50 participants, instrument fourni, grand espace ferme a sol dur).
  - Agenda du Nid (`/le-nid#agenda`) : les 3 dates de workshops.

⚠️ Aucun tarif n'est affiche : le site source Now Groove n'en publie aucun
   (les 40 € figurent seulement dans le dossier de presentation interne).
   On renvoie donc systematiquement vers contact@resonancesproductions.org.

Usage : python3 sources/generate_rythme.py   (depuis la racine du depot)
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nav_menu  # menu de navigation partage  # noqa: E402
import verif_commentaires  # garde-fou commentaires HTML  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_IMG = os.path.join(ROOT, 'sources', 'rythme_img')
OUT_IMG = os.path.join(ROOT, 'img', 'rythme-calebasse')
OUT_DIR = os.path.join(ROOT, 'rythme-calebasse')
OUT_HTML = os.path.join(OUT_DIR, 'index.html')

WIDTHS = (480, 900, 1400)

# --- photos : nom de base -> texte alternatif (factuel) -------------------
PHOTOS = {
    'cercle-calebasses': "Une vingtaine de calebasses posees sur des tapis, "
                         "disposees en cercle sur un sol carrele avant un atelier",
    'atelier-cercle': "Une quinzaine de participants assis en cercle, chacun "
                      "derriere sa calebasse posee sur un tapis",
    'david-calebasse': "David Lesage assis en tailleur derriere sa calebasse "
                       "posee sur son tapis, un oeuf bleu dans chaque main",
    'calebasse-tapis-oeufs': "Une calebasse pyrogravee posee sur son tapis "
                             "rond, avec les deux oeufs bleus",
    'calebasses-brutes': "David Lesage accroupi au milieu d'une pile de "
                         "calebasses brutes de differentes tailles",
}


# =========================================================================
# 1. IMAGES
# =========================================================================

def build_images():
    """Genere les derives WebP + JPEG. Retourne {nom: [(largeur, hauteur), ...]}."""
    sizes = {}
    if not os.path.isdir(SRC_IMG):
        print('[images] %s absent -> etape sautee' % SRC_IMG)
        return read_existing_sizes()
    try:
        from PIL import Image
    except ImportError:
        print('[images] Pillow absent -> etape sautee')
        return read_existing_sizes()

    os.makedirs(OUT_IMG, exist_ok=True)
    for name in sorted(PHOTOS):
        src = os.path.join(SRC_IMG, name + '.jpg')
        if not os.path.isfile(src):
            print('[images] %s manquant -> ignore' % src)
            continue
        im = Image.open(src).convert('RGB')
        nw, nh = im.size
        targets = sorted({min(w, nw) for w in WIDTHS})
        made = []
        for w in targets:
            h = max(1, round(nh * w / nw))
            r = im.resize((w, h), Image.LANCZOS)
            r.save(os.path.join(OUT_IMG, '%s-%d.jpg' % (name, w)),
                   quality=82, optimize=True, progressive=True)
            r.save(os.path.join(OUT_IMG, '%s-%d.webp' % (name, w)),
                   quality=80, method=6)
            made.append((w, h))
        sizes[name] = made
        print('[images] %-24s %s' % (name, ' '.join('%dx%d' % s for s in made)))
    return sizes


def read_existing_sizes():
    """Relit les largeurs deja presentes dans img/rythme-calebasse/."""
    sizes = {}
    if not os.path.isdir(OUT_IMG):
        return sizes
    for f in os.listdir(OUT_IMG):
        m = re.match(r'^(.*)-(\d+)\.jpg$', f)
        if not m:
            continue
        name, w = m.group(1), int(m.group(2))
        sizes.setdefault(name, set()).add(w)
    out = {}
    for name, ws in sizes.items():
        try:
            from PIL import Image
            res = []
            for w in sorted(ws):
                with Image.open(os.path.join(OUT_IMG, '%s-%d.jpg' % (name, w))) as im:
                    res.append(im.size)
            out[name] = res
        except Exception:
            out[name] = [(w, 0) for w in sorted(ws)]
    return out


def picture(name, sizes, css_class='', sizes_attr='100vw', eager=False):
    """<picture> complet : WebP + repli JPEG, srcset, width/height, alt."""
    made = sizes.get(name)
    if not made:
        raise SystemExit('image absente : %s (lancer la generation d images)' % name)
    biggest_w, biggest_h = made[-1]
    default_w = made[len(made) // 2][0] if len(made) > 1 else biggest_w
    webp = ', '.join('/img/rythme-calebasse/%s-%d.webp %dw' % (name, w, w) for w, _ in made)
    jpg = ', '.join('/img/rythme-calebasse/%s-%d.jpg %dw' % (name, w, w) for w, _ in made)
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    cls = ' class="%s"' % css_class if css_class else ''
    return (
        '<picture%s>\n'
        '  <source type="image/webp" sizes="%s" srcset="%s">\n'
        '  <img src="/img/rythme-calebasse/%s-%d.jpg" sizes="%s" srcset="%s"\n'
        '    width="%d" height="%d" %s alt="%s">\n'
        '</picture>' % (cls, sizes_attr, webp, name, default_w, sizes_attr, jpg,
                        biggest_w, biggest_h, load, PHOTOS[name])
    )


# =========================================================================
# 2. LA PAGE
# =========================================================================

MAILTO_CONTACT = 'mailto:contact@resonancesproductions.org'

CSS = """
:root{--night:#0e0f24;--night2:#141633;--ink:#eae7f3;--muted:#a9a6c4;--gold:#d8b25a;--gold2:#f0d18a;--plum:#8f7ad1;--card:#191b3d;--line:rgba(216,178,90,.26)}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--night);color:var(--ink);font-family:'Jost',-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.75;font-size:17px;-webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2,h3,h4,.serif{font-family:'Cormorant Garamond',Georgia,serif}
a{color:inherit;text-decoration:none}
img,picture{max-width:100%}
picture>img{height:auto}
.wrap{max-width:1080px;margin:0 auto;padding:0 26px}
.kick{letter-spacing:.32em;text-transform:uppercase;font-size:13px;font-weight:600;color:var(--gold);margin-bottom:14px}
section{padding:78px 0;position:relative}
.sec-title{font-size:clamp(30px,5vw,50px);font-weight:600;line-height:1.08;color:#fff}
.lead{font-size:19px;color:var(--muted);max-width:760px;margin-top:16px}
p.body{max-width:820px;color:#d7d4ea;margin-top:16px}
b{color:#fff;font-weight:500}
.divider{height:1px;background:linear-gradient(90deg,transparent,var(--line),transparent);max-width:1080px;margin:0 auto}
.band{background:linear-gradient(180deg,#0b0c1e,var(--night))}
/* nav */
.nav{position:fixed;top:0;left:0;right:0;z-index:40;display:flex;align-items:center;justify-content:space-between;padding:16px 26px;background:rgba(14,15,36,.6);backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.05)}
.nav .brand{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:19px;letter-spacing:.12em;color:#fff;text-transform:uppercase}
.nav .links{display:flex;align-items:center;gap:19px;font-size:13.5px;letter-spacing:.04em}
.nav .links a{color:var(--muted);transition:color .2s}
.nav .links a:hover{color:var(--gold2)}
.nav .links a[aria-current="page"]{color:var(--gold2)}
.nav .adh{color:#1a1608!important;background:var(--gold);padding:8px 16px;border-radius:30px;font-weight:600}
@media(max-width:760px){.nav .links a:not(.adh){display:none}}
/* 9 entrees de menu : on resserre entre 861 et 1080 px (sous 861 px = hamburger).
   Jamais sous 13 px (plancher typographique du site) : dans la bande la plus
   etroite on masque « Prestations », qui reste accessible depuis l'accueil. */
@media(min-width:861px) and (max-width:1080px){.nav{padding:16px 18px}.nav .brand{font-size:17px;white-space:nowrap}.nav .links{gap:9px;font-size:13px}.nav .adh{padding:8px 13px}}
@media(min-width:861px) and (max-width:1000px){.nav .links a[href="/#prestations"]{display:none}}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;background:var(--gold);color:#1a1608;font-weight:600;padding:15px 26px;border-radius:40px;font-size:16px;min-height:48px;transition:transform .2s,box-shadow .2s}
.btn:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(216,178,90,.28)}
.btn.ghost{background:transparent;color:var(--gold2);border:1px solid var(--line)}
.cta{display:flex;gap:14px;flex-wrap:wrap;margin-top:28px}
/* hero */
.top{padding:128px 0 62px;background:radial-gradient(900px 560px at 8% -10%,rgba(143,122,209,.20),transparent 62%),radial-gradient(760px 480px at 94% 104%,rgba(216,178,90,.13),transparent 62%),linear-gradient(180deg,#0b0c1e,var(--night))}
.top h1{font-size:clamp(38px,7vw,70px);font-weight:600;line-height:1.03;color:#fff;letter-spacing:.02em}
.tagline{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(19px,2.8vw,28px);margin-top:12px}
.hero-fig{margin:34px 0 0;border-radius:16px;overflow:hidden;border:1px solid var(--line);background:var(--card)}
.hero-fig img{display:block;width:100%}
.hero-fig figcaption{color:var(--muted);font-size:13.5px;line-height:1.55;padding:12px 18px 14px;border-top:1px solid rgba(255,255,255,.06)}
/* blocs de texte */
.h-min{color:var(--gold);font-size:13px;letter-spacing:.22em;text-transform:uppercase;font-weight:600;margin-bottom:10px}
.blk h2{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(26px,4vw,42px);color:#fff;font-weight:600;line-height:1.1}
.blk h3{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(22px,3vw,30px);color:#fff;font-weight:600;line-height:1.15;margin-top:34px}
.quote{margin:34px 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(20px,2.9vw,27px);line-height:1.38;border-left:2px solid var(--gold);padding-left:22px;max-width:780px}
.quote .who{display:block;font-style:normal;font-family:'Jost',sans-serif;font-size:14px;color:var(--muted);letter-spacing:.1em;text-transform:uppercase;margin-top:12px}
.lst{list-style:none;margin-top:20px;max-width:820px}
.lst li{color:#d7d4ea;font-size:16.5px;padding:10px 0 10px 26px;position:relative;border-bottom:1px solid rgba(255,255,255,.05)}
.lst li:last-child{border-bottom:0}
.lst li::before{content:"";position:absolute;left:4px;top:20px;width:6px;height:6px;border-radius:50%;background:var(--gold)}
.note{background:var(--card);border:1px solid rgba(255,255,255,.07);border-left:2px solid var(--gold);border-radius:14px;padding:19px 22px;margin-top:24px;max-width:820px}
.note p{color:#d7d4ea;font-size:15.5px;margin:0;line-height:1.7}
.note p+p{margin-top:10px}
.two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,360px);gap:34px;align-items:start;margin-top:30px}
.two .lead,.two p.body{margin-top:0}
.fig{margin:0;border-radius:16px;overflow:hidden;border:1px solid var(--line);background:var(--card)}
.fig img{display:block;width:100%}
.fig figcaption{color:var(--muted);font-size:13.5px;line-height:1.55;padding:12px 16px 14px;border-top:1px solid rgba(255,255,255,.06)}
.fig.on-white{background:#f4f2ee}
@media(max-width:820px){.two{grid-template-columns:1fr;gap:26px}}
/* fiche pratique */
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px;margin-top:30px}
.fact{background:var(--card);border:1px solid rgba(255,255,255,.06);border-top:2px solid var(--gold);border-radius:14px;padding:18px 20px}
.fact .k{color:var(--gold);font-size:13px;letter-spacing:.14em;text-transform:uppercase;font-weight:600}
.fact .v{color:#fff;font-size:17px;margin-top:6px;line-height:1.5}
.fact .v small{display:block;color:var(--muted);font-size:14px;margin-top:4px}
/* dates */
.dates{display:grid;gap:14px;margin-top:28px;max-width:820px}
.date{display:flex;gap:20px;align-items:center;flex-wrap:wrap;background:var(--card);border:1px solid rgba(255,255,255,.06);border-left:2px solid var(--plum);border-radius:14px;padding:16px 20px}
.date .d{font-family:'Cormorant Garamond',Georgia,serif;color:var(--gold2);font-size:25px;font-weight:600;min-width:190px}
.date .h{color:var(--muted);font-size:15.5px;flex:1 1 auto}
.date .a{display:inline-flex;align-items:center;min-height:44px;padding:11px 20px;border-radius:30px;border:1px solid var(--line);color:var(--gold2);font-size:15px}
.date .a:hover{background:rgba(216,178,90,.10)}
/* ===== APPEL A CANDIDATURE ===== */
.appel{background:radial-gradient(880px 540px at 12% -6%,rgba(216,178,90,.16),transparent 62%),radial-gradient(700px 460px at 92% 100%,rgba(143,122,209,.18),transparent 62%),linear-gradient(180deg,#0b0c1e,#101229)}
.appel .letter{max-width:780px;margin-top:26px;border-left:2px solid var(--gold);padding-left:24px}
.appel .letter p{color:#e4e1f2;font-size:17.5px;margin-top:18px}
.appel .letter p:first-child{margin-top:0}
.appel .letter .big{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(23px,3.4vw,31px);color:#fff;line-height:1.2}
.appel .letter .emo{margin-right:9px}
.appel .letter .sign{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:21px;margin-top:22px}
.badge{display:inline-flex;align-items:center;gap:9px;background:rgba(216,178,90,.14);border:1px solid var(--line);color:var(--gold2);border-radius:30px;padding:9px 18px;font-size:15px;font-weight:500;margin-bottom:16px}
@media(max-width:620px){.appel .letter{padding-left:18px}}
/* bloc « ce qui est deja eprouve » : l'experience d'animation, au service de
   l'appel a candidature. Aucune classe nouvelle hors du conteneur : le bloc
   reutilise .h-min, .blk h3, p.body et .lst deja definis plus haut. */
.appel .xp{max-width:820px;margin-top:46px;padding-top:38px;border-top:1px solid var(--line)}
.appel .xp h3{margin-top:0}
/* ===== FORMULAIRE ===== */
.form{margin-top:36px;max-width:820px;background:var(--card);border:1px solid rgba(255,255,255,.08);border-radius:18px;padding:28px}
.form h3{font-family:'Cormorant Garamond',Georgia,serif;color:#fff;font-size:26px;font-weight:600;line-height:1.15;margin:0}
.form .intro{color:var(--muted);font-size:15.5px;margin-top:8px}
.row{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:22px}
@media(max-width:620px){.row{grid-template-columns:1fr}.form{padding:22px 18px}}
.f{display:block;margin-top:22px}
.row .f{margin-top:0}
.f>label,fieldset>legend{display:block;color:#fff;font-size:15.5px;font-weight:500;margin-bottom:8px;line-height:1.45}
.f .hint,fieldset .hint{display:block;color:var(--muted);font-size:14px;font-weight:400;margin-top:3px}
/* variante en ligne : evite qu'un champ de la meme rangee soit decale d'une
   ligne par rapport a son voisin (Email / Telephone) */
.f .hint.inl{display:inline;margin-top:0}
.req{color:var(--gold2)}
.f input,.f select,.f textarea{width:100%;min-height:48px;background:#101229;color:var(--ink);border:1px solid rgba(216,178,90,.30);border-radius:11px;padding:12px 14px;font-family:inherit;font-size:16px;line-height:1.5}
.f textarea{min-height:120px;resize:vertical}
.f select{appearance:none;background-image:linear-gradient(45deg,transparent 50%,var(--gold2) 50%),linear-gradient(135deg,var(--gold2) 50%,transparent 50%);background-position:calc(100% - 21px) 50%,calc(100% - 15px) 50%;background-size:6px 6px,6px 6px;background-repeat:no-repeat;padding-right:44px}
.f input:focus,.f select:focus,.f textarea:focus{border-color:var(--gold2);outline:none;box-shadow:0 0 0 3px rgba(216,178,90,.20)}
fieldset{border:0;margin-top:22px;padding:0}
.opts{display:flex;flex-wrap:wrap;gap:10px;margin-top:4px}
.opt{display:inline-flex;align-items:center;gap:10px;min-height:48px;padding:10px 18px;border:1px solid rgba(216,178,90,.30);border-radius:30px;background:#101229;color:var(--ink);font-size:16px;cursor:pointer}
.opt:hover{border-color:var(--gold2)}
.opt input{width:19px;height:19px;min-height:0;accent-color:var(--gold);margin:0;flex:0 0 auto}
.opt:has(input:checked){border-color:var(--gold2);background:rgba(216,178,90,.13)}
.err{display:none;color:#ffbdbd;font-size:14.5px;margin-top:7px;line-height:1.5}
.f.bad .err,fieldset.bad .err{display:block}
.f.bad input,.f.bad select,.f.bad textarea{border-color:#e0748a;box-shadow:0 0 0 3px rgba(224,116,138,.16)}
fieldset.bad .opt{border-color:#e0748a}
.summary{display:none;margin-top:22px;border:1px solid #e0748a;background:rgba(224,116,138,.10);border-radius:12px;padding:14px 18px;color:#ffd8de;font-size:15.5px}
.summary.on{display:block}
.form-actions{display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin-top:28px}
button.btn{border:0;cursor:pointer;font-family:inherit}
.rgpd{color:var(--muted);font-size:14px;margin-top:18px;line-height:1.6}
.sent{display:none;margin-top:24px;border:1px solid var(--line);background:#101229;border-radius:14px;padding:20px}
.sent.on{display:block}
.sent h4{font-family:'Cormorant Garamond',Georgia,serif;color:var(--gold2);font-size:22px;font-weight:600}
.sent p{color:#d7d4ea;font-size:15.5px;margin-top:10px}
.sent textarea{width:100%;min-height:190px;margin-top:14px;background:#0b0c1e;color:var(--ink);border:1px solid rgba(216,178,90,.26);border-radius:11px;padding:13px 15px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:14px;line-height:1.6;resize:vertical}
.sent .acts{display:flex;gap:12px;flex-wrap:wrap;margin-top:16px}
.copied{color:var(--gold2);font-size:15px;align-self:center}
/* pour aller plus loin */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(272px,1fr));gap:18px;margin-top:30px}
.card{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:16px;padding:24px;display:flex;flex-direction:column}
.card h3{font-family:'Cormorant Garamond',Georgia,serif;color:#fff;font-size:23px;font-weight:600;line-height:1.2;margin:0}
.card .t{color:var(--gold);font-size:13px;letter-spacing:.16em;text-transform:uppercase;font-weight:600;margin-bottom:8px}
.card p{color:var(--muted);font-size:15.5px;margin-top:10px;flex:1 1 auto}
.card .go{margin-top:16px;color:var(--gold2);font-size:15px;text-decoration:underline;text-decoration-color:rgba(216,178,90,.45);text-underline-offset:3px;display:inline-block;min-height:44px;padding:11px 0}
/* retour en haut */
.totop{position:fixed;right:18px;bottom:18px;z-index:35;width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:rgba(25,27,61,.92);border:1px solid var(--line);color:var(--gold2);font-size:19px;opacity:0;visibility:hidden;transition:opacity .3s,visibility .3s,transform .2s}
.totop.on{opacity:1;visibility:visible}
.totop:hover{transform:translateY(-2px)}
:focus-visible{outline:2px solid var(--gold2);outline-offset:2px;border-radius:4px}
/* pied de page */
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
/* ===== MENU MOBILE (hamburger) — repris de sources/mobile_nav.py ===== */
.burger{display:none;background:none;border:1px solid rgba(216,178,90,.34);border-radius:10px;width:44px;height:44px;padding:0;cursor:pointer;position:relative;z-index:1002;flex:0 0 auto}
.burger span{display:block;width:20px;height:2px;background:var(--gold2);margin:4px auto;border-radius:2px;transition:transform .28s,opacity .2s}
.burger[aria-expanded="true"] span:nth-child(1){transform:translateY(6px) rotate(45deg)}
.burger[aria-expanded="true"] span:nth-child(2){opacity:0}
.burger[aria-expanded="true"] span:nth-child(3){transform:translateY(-6px) rotate(-45deg)}
@media(max-width:860px){
  .burger{display:block}
  .nav{flex-wrap:wrap}
  .nav .links{position:fixed;top:0;left:0;right:0;bottom:0;z-index:1001;
    background:rgba(10,11,28,.98);backdrop-filter:blur(14px);
    flex-direction:column;justify-content:center;align-items:center;gap:6px !important;
    padding:80px 26px 40px;
    opacity:0;visibility:hidden;transform:translateY(-12px);
    transition:opacity .3s,transform .3s,visibility .3s;
    overflow-y:auto}
  .nav .links.open{opacity:1;visibility:visible;transform:none}
  .nav .links a,.nav .links a:not(.adh){display:block !important;
    font-size:21px !important;letter-spacing:.06em;padding:14px 18px;text-align:center;
    font-family:'Cormorant Garamond',Georgia,serif;color:#eae7f3 !important;width:100%;max-width:340px}
  .nav .links a:active{color:var(--gold2) !important}
  .nav .links a.adh{margin-top:18px;background:var(--gold);color:#1a1608 !important;
    border-radius:30px;font-family:'Jost',sans-serif;font-size:16px !important;padding:14px 30px;width:auto}
  /* .nav porte un backdrop-filter : il devient le bloc conteneur des descendants
     position:fixed ET un contexte d'empilement -> le panneau restait enferme dans
     la barre et passait sous le contenu. On neutralise le filtre et on remonte le
     nav uniquement quand le menu est ouvert. NE PAS RETIRER. */
  body.nav-open .nav{backdrop-filter:none !important;-webkit-backdrop-filter:none !important;z-index:1001 !important}
  body.nav-open{overflow:hidden}
}
@media print{.burger,.totop{display:none}}
"""

NAV = """<nav class="nav">
  <a href="/" class="brand">Résonances Productions</a>
  <div class="links">
    <a href="/">Accueil</a>
    <a href="/#association">L’association</a>
    <a href="/#prestations">Prestations</a>
    <a href="/le-nid">Le Nid</a>
    <a href="/rituals">RITUALS</a>
    <a href="/e-motion">E-Motion</a>
    <a href="/rythme-calebasse" aria-current="page">Rythme &amp; calebasse</a>
    <a href="#contact">Contact</a>
    <a class="adh" href="https://www.helloasso.com/beta/associations/resonances-productions/adhesions/adhesion-resonances-productions" target="_blank" rel="noopener">Adhérer</a>
  </div>
</nav>"""

FOOTER = """<footer id="contact"><div class="wrap">
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
      <p style="margin-top:8px"><a href="https://www.helloasso.com/associations/resonances-productions" target="_blank" rel="noopener">Adhérer / soutenir</a></p>
      <p style="margin-top:8px"><a href="https://docs.google.com/document/d/1NxsbvaqHsA9VOXlN7cvsav7cxFwhsK4XCpowHb75o1w/edit?usp=sharing" target="_blank" rel="noopener">Statuts de l’association</a></p>
    </div>
  </div>
  <div class="legal">© 2026 Résonances Productions · resonancesproductions.org</div>
</div></footer>"""

JS = r"""<script>
/* Retour en haut ------------------------------------------------------- */
(function(){
  var b=document.querySelector('.totop'); if(!b) return;
  function upd(){ b.classList.toggle('on', window.scrollY>700); }
  upd(); window.addEventListener('scroll',upd,{passive:true});
})();

/* Menu mobile (hamburger) --------------------------------------------- */
(function(){
  var nav=document.querySelector('.nav'); if(!nav) return;
  var links=nav.querySelector('.links'); if(!links) return;
  var b=document.createElement('button');
  b.className='burger'; b.type='button';
  b.setAttribute('aria-label','Ouvrir le menu');
  b.setAttribute('aria-expanded','false');
  b.innerHTML='<span></span><span></span><span></span>';
  nav.appendChild(b);
  function set(open){
    b.setAttribute('aria-expanded',open?'true':'false');
    b.setAttribute('aria-label',open?'Fermer le menu':'Ouvrir le menu');
    links.classList.toggle('open',open);
    document.body.classList.toggle('nav-open',open);
  }
  b.addEventListener('click',function(){ set(b.getAttribute('aria-expanded')!=='true'); });
  links.addEventListener('click',function(e){ if(e.target.tagName==='A') set(false); });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape') set(false); });
  window.addEventListener('resize',function(){ if(window.innerWidth>860) set(false); });
})();

/* Formulaire de candidature -------------------------------------------
   Le site est STATIQUE (HTML sur Vercel) : aucun serveur ne peut recevoir
   les reponses. Le bouton compose donc un email pre-rempli (mailto) que la
   personne envoie depuis sa propre messagerie. Le texte compose reste
   affiche a l'ecran avec un bouton « Copier » : si aucun logiciel de mail
   ne s'ouvre, la candidature n'est pas perdue.
   Sans JavaScript : le formulaire garde son action mailto native et le
   <noscript> indique quoi ecrire. -------------------------------------- */
(function(){
  var f=document.getElementById('candidature'); if(!f) return;
  /* on desactive la validation native SEULEMENT si JS tourne : sans JS elle
     reste le garde-fou du repli */
  f.setAttribute('novalidate','novalidate');

  var DEST='contact@resonancesproductions.org';
  var summary=document.getElementById('form-summary');
  var sent=document.getElementById('form-sent');
  var out=document.getElementById('form-text');
  var mailLink=document.getElementById('form-mail');
  var copied=document.getElementById('form-copied');

  function group(el){ return el.closest('.f') || el.closest('fieldset'); }
  function clear(){
    [].forEach.call(f.querySelectorAll('.bad'),function(g){ g.classList.remove('bad'); });
    summary.classList.remove('on'); summary.textContent='';
  }
  function fail(el,msg){
    var g=group(el); if(!g) return;
    g.classList.add('bad');
    var e=g.querySelector('.err'); if(e) e.textContent=msg;
  }
  function val(name){
    var el=f.elements[name];
    if(!el) return '';
    if(el.length!==undefined && !el.tagName){ /* RadioNodeList */
      for(var i=0;i<el.length;i++) if(el[i].checked) return el[i].value;
      return '';
    }
    return (el.value||'').trim();
  }

  var CHAMPS=[
    ['prenom','Merci d’indiquer ton prénom.'],
    ['nom','Merci d’indiquer ton nom.'],
    ['email','Merci d’indiquer une adresse email — c’est par là que David te répondra.'],
    ['niveau','Merci de choisir ton niveau : il n’y a pas de mauvaise réponse.'],
    ['rythme','Merci de choisir le rythme qui te conviendrait le mieux.'],
    ['motivation','Merci d’écrire quelques lignes : c’est le cœur de ta candidature.']
  ];

  f.addEventListener('submit',function(ev){
    ev.preventDefault();
    clear();
    var first=null, errs=0;
    for(var i=0;i<CHAMPS.length;i++){
      var name=CHAMPS[i][0], msg=CHAMPS[i][1];
      var el=f.elements[name];
      var v=val(name);
      var target=(el.length!==undefined && !el.tagName) ? el[0] : el;
      if(!v){ fail(target,msg); errs++; if(!first) first=target; continue; }
      if(name==='email' && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)){
        fail(target,'Cette adresse email semble incomplète (exemple : prenom@domaine.fr).');
        errs++; if(!first) first=target;
      }
    }
    if(errs){
      summary.textContent = errs===1
        ? 'Il reste 1 champ à compléter avant d’envoyer ta candidature.'
        : 'Il reste '+errs+' champs à compléter avant d’envoyer ta candidature.';
      summary.classList.add('on');
      if(first) first.focus();
      return;
    }

    var L=[];
    L.push('Candidature — groupe de pratique calebasse (Paris)');
    L.push('');
    L.push('Prénom : '+val('prenom'));
    L.push('Nom : '+val('nom'));
    L.push('Email : '+val('email'));
    L.push('Téléphone : '+(val('telephone')||'(non renseigné)'));
    L.push('Niveau : '+val('niveau'));
    L.push('Rythme souhaité : '+val('rythme'));
    L.push('Disponibilités : '+(val('dispos')||'(non renseignées)'));
    L.push('');
    L.push('Pourquoi je veux en faire partie :');
    L.push(val('motivation'));
    L.push('');
    L.push('— Envoyé depuis resonancesproductions.org/rythme-calebasse');
    var body=L.join('\n');
    var subject='Candidature — groupe de pratique calebasse — '+val('prenom')+' '+val('nom');
    var url='mailto:'+DEST+'?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(body);

    out.value='À : '+DEST+'\nObjet : '+subject+'\n\n'+body;
    mailLink.setAttribute('href',url);
    sent.classList.add('on');
    copied.textContent='';
    sent.scrollIntoView({behavior:'smooth',block:'center'});
    /* on tente d'ouvrir la messagerie ; si rien ne se passe, le bloc
       ci-dessus permet de copier le message a la main */
    try{ window.location.href=url; }catch(e){}
  });

  var btn=document.getElementById('form-copy');
  if(btn) btn.addEventListener('click',function(){
    out.focus(); out.select();
    var ok=false;
    if(navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(out.value).then(function(){
        copied.textContent='Message copié — colle-le dans un email à '+DEST;
      },function(){ copied.textContent='Copie impossible : sélectionne le texte puis Cmd/Ctrl + C.'; });
      return;
    }
    try{ ok=document.execCommand('copy'); }catch(e){}
    copied.textContent = ok
      ? 'Message copié — colle-le dans un email à '+DEST
      : 'Copie impossible : sélectionne le texte puis Cmd/Ctrl + C.';
  });
})();
</script>"""


def build_html(sizes):
    p = lambda *a, **k: picture(*a, **k)

    head = """<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Le rythme à la calebasse — workshops et groupe de pratique à Paris · Résonances Productions</title>
<meta name="description" content="Apprendre le rythme à la calebasse avec David Lesage, au Nid (Paris 20ᵉ) : des workshops de 2 h en petit comité, instrument fourni, sans prérequis musical. Et un appel à candidature pour un groupe de pratique engagé sur un an, à raison d’un workshop par mois — il reste environ 4 places.">
<meta property="og:title" content="Le rythme à la calebasse — workshops et groupe de pratique à Paris">
<meta property="og:description" content="Une approche du rythme par le corps et la calebasse, au Nid (Paris 20ᵉ). Workshops de 2 h, instrument fourni. Appel à candidature : un groupe de pratique sur un an, un workshop par mois, environ 4 places à pourvoir.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.resonancesproductions.org/rythme-calebasse">
<meta property="og:image" content="https://www.resonancesproductions.org/img/rythme-calebasse/cercle-calebasses-{ogw}.jpg">
<meta property="og:image:width" content="{ogw}">
<meta property="og:image:height" content="{ogh}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0e0f24">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
"""
    ogw, ogh = sizes['cercle-calebasses'][-1]
    head = head.replace('{css}', CSS).replace('{ogw}', str(ogw)).replace('{ogh}', str(ogh))

    body = []
    A = body.append

    A(NAV)

    # ---------------------------------------------------------------- HERO
    A("""
<header class="top" id="top"><div class="wrap">
  <div class="kick">Transmission · Le Nid, Paris 20<sup>e</sup> · avec David Lesage</div>
  <h1>Le rythme à la calebasse</h1>
  <p class="tagline">« Apprendre les bases du rythme avec la calebasse, en s’amusant. »</p>
  <p class="lead">Une calebasse posée au sol, deux œufs dans les mains, un cercle — et la pulsation
  qui se met à circuler. Une approche du rythme intégrative et joyeuse, qui passe par le corps
  autant que par l’esprit. Aucun prérequis musical : l’instrument est fourni, et on entre dans le
  rythme par la sensation avant d’y entrer par la théorie.</p>
  <div class="cta">
    <a class="btn" href="#appel">L’appel à candidature</a>
    <a class="btn ghost" href="#workshops">Les prochains workshops</a>
  </div>
  <figure class="hero-fig">
""" + p('cercle-calebasses', sizes, sizes_attr='(max-width:1080px) 100vw, 1028px', eager=True) + """
    <figcaption>Avant l’atelier : une calebasse et son tapis par personne, en cercle.</figcaption>
  </figure>
</div></header>

<div class="divider"></div>
""")

    # ------------------------------------------------------ LA CALEBASSE
    A("""
<section class="blk band" id="calebasse"><div class="wrap">
  <div class="h-min">L’instrument</div>
  <h2>Une gourde, deux œufs, et des infra-basses</h2>
  <div class="two">
    <div>
      <p class="body">Utilisée dans le monde entier, la « gourde » est une plante grimpante dont le
      fruit creux, évidé et séché, donne la <b>calebasse</b>. Sa coque est si dure qu’elle autorise
      des usages tout à fait exceptionnels : en musique, on la retrouve dans la kora ou le ngoni,
      la harpe africaine.</p>
      <p class="body">En 2012, David Lesage la rencontre en la posant simplement par terre, sur une
      couverture. Il y découvre un son, une sensation — les <b>infra-basses</b>. Puis lui vient
      l’idée d’utiliser des <b>œufs en plastique</b> pour reproduire le charleston et la caisse
      claire. Une sorte de « batterie portative organique », au son électronique naturel, qu’il
      emmène partout dans son quotidien de musicien : dans la rue, en soirée, en concert, et jusque
      sur le plateau de <i>The Voice</i> en 2021.</p>
    </div>
    <figure class="fig on-white">
""" + p('calebasse-tapis-oeufs', sizes, sizes_attr='(max-width:820px) 100vw, 360px') + """
      <figcaption>Une calebasse, son tapis et ses deux œufs : tout ce qu’il faut pour jouer.</figcaption>
    </figure>
  </div>

  <h3>Les calebasses « signature »</h3>
  <div class="two">
    <div>
      <p class="body">Les calebasses de 46 cm de diamètre et plus, avec un bord épais de 1,5 à 2 cm,
      sont très rares à trouver — en Europe tout particulièrement. Celles que David utilise
      viennent d’<b>Afrique de l’Ouest</b> (Niger, Burkina Faso, Mali) et sont sélectionnées selon
      ses critères propres à la pratique du rythme. Chacune est retravaillée à la main par
      « Kamou », de Djoliba Percussions, qui affine le bord pour que la calebasse épouse
      exactement son tapis — c’est de là que vient ce son unique et puissant. Chacune est enfin
      pyrogravée au laser du logo Now Groove : les quatre éléments en mouvement, formant le
      cinquième, l’éther.</p>
      <div class="note">
        <p><b>Un détail qui compte.</b> La calebasse ne donne sa pleine puissance que sur un
        <b>sol dur</b> — béton, carrelage, pierre, bois plein — parce que le son naît de la
        pression de l’air entre la coque, le tapis et le sol. Sur l’herbe, la terre ou un plancher
        creux, les infra-basses ne sortent pas.</p>
      </div>
    </div>
    <figure class="fig">
""" + p('calebasses-brutes', sizes, sizes_attr='(max-width:820px) 100vw, 360px') + """
      <figcaption>La sélection des calebasses, avant le travail du bord et la pyrogravure.</figcaption>
    </figure>
  </div>
</div></section>

<div class="divider"></div>
""")

    # --------------------------------------------------- CE QU'ON PRATIQUE
    A("""
<section class="blk" id="pratique"><div class="wrap">
  <div class="h-min">Le déroulé</div>
  <h2>Ce que l’on pratique ensemble</h2>
  <p class="lead">Comprendre le rythme, c’est pouvoir se situer dans l’espace et le temps. C’est
  pouvoir se donner des rendez-vous avec les autres, entrer en relation. Quand on comprend le
  rythme, on peut faire des propositions claires.</p>
  <ul class="lst">
    <li>Une approche pédagogique <b>intégrative</b> du rythme par le corps et la calebasse, et
    <b>philosophique</b> à travers l’esprit.</li>
    <li>Une <b>introduction au rythme</b> guidée par la cohérence cardiaque, à travers la
    respiration, et une visualisation guidée.</li>
    <li>Des jeux de <b>questions / réponses</b> avec David.</li>
    <li>La <b>synchronisation des membres</b> : pieds, mains, voix.</li>
    <li><b>Chanter</b> ensemble.</li>
    <li><b>Taper</b> ensemble, et en rythme.</li>
    <li><b>Jouer sur la musique</b>, avec intensité.</li>
    <li>Être <b>accompagné par David en musique</b>.</li>
  </ul>
  <blockquote class="quote">« Je t’invite à nous retrouver en cercle, te laisser guider par ma voix
  et goûter à une expérience joyeuse, en mettant soigneusement ton cerveau de côté pour rentrer
  simplement dans l’expérience de la sensation. »<span class="who">David Lesage</span></blockquote>

  <h3>Ce que la pratique développe</h3>
  <ul class="lst">
    <li>Ressentir une <b>joie sans raison</b>.</li>
    <li>Développer une <b>qualité de présence et d’écoute</b>.</li>
    <li>Développer l’<b>indépendance des membres</b>.</li>
    <li>Soutenir le <b>dépassement de soi</b>.</li>
    <li>Oser <b>chanter en groupe</b> sans même s’en rendre compte.</li>
    <li><b>Gagner en clarté</b> : mieux comprendre la musique et le placement.</li>
    <li>Mieux <b>se situer dans l’espace et le temps</b>.</li>
    <li>Arrêter de penser, et être <b>profondément présent</b>.</li>
  </ul>
  <p class="body" style="font-style:italic;color:var(--gold2)">Bref… on va kiffer et groover ensemble.</p>
  <figure class="fig" style="margin-top:34px;max-width:820px">
""" + p('atelier-cercle', sizes, sizes_attr='(max-width:880px) 100vw, 820px') + """
    <figcaption>Le cercle : chacun derrière sa calebasse, David au milieu.</figcaption>
  </figure>
</div></section>

<div class="divider"></div>
""")

    # ------------------------------------------------------- LES WORKSHOPS
    A("""
<section class="blk band" id="workshops"><div class="wrap">
  <div class="h-min">Au Nid, Paris 20<sup>e</sup></div>
  <h2>Les workshops « rythme à la calebasse »</h2>
  <p class="lead">Deux heures pour faire l’expérience du rythme à travers la calebasse, ton corps et
  ta voix. Au Nid, ces workshops se déroulent en <b>petit comité</b> : chacun a sa calebasse, et
  David peut passer auprès de chacun.</p>

  <div class="facts">
    <div class="fact"><div class="k">Durée</div><div class="v">2 heures</div></div>
    <div class="fact"><div class="k">Lieu</div><div class="v">Le Nid<small>29 rue des Orteaux, 75020 Paris</small></div></div>
    <div class="fact"><div class="k">Niveau</div><div class="v">Tous<small>aucun prérequis musical</small></div></div>
    <div class="fact"><div class="k">Instrument</div><div class="v">Fourni<small>une calebasse, un tapis, deux œufs</small></div></div>
    <div class="fact"><div class="k">Jauge</div><div class="v">Petit comité<small>sur inscription préalable</small></div></div>
    <div class="fact"><div class="k">Participation</div><div class="v">Sur demande<small>précisée à la réservation</small></div></div>
  </div>

  <h3>Les prochaines dates</h3>
  <div class="dates">
    <div class="date">
      <div class="d">Dimanche 20 septembre 2026</div>
      <div class="h">10 h – 12 h</div>
      <a class="a" href="{M}?subject=Workshop%20rythme%20%C3%A0%20la%20calebasse%20%E2%80%94%2020%20septembre%202026">Réserver</a>
    </div>
    <div class="date">
      <div class="d">Samedi 17 octobre 2026</div>
      <div class="h">15 h – 17 h</div>
      <a class="a" href="{M}?subject=Workshop%20rythme%20%C3%A0%20la%20calebasse%20%E2%80%94%2017%20octobre%202026">Réserver</a>
    </div>
    <div class="date">
      <div class="d">Dimanche 15 novembre 2026</div>
      <div class="h">15 h – 17 h</div>
      <a class="a" href="{M}?subject=Workshop%20rythme%20%C3%A0%20la%20calebasse%20%E2%80%94%2015%20novembre%202026">Réserver</a>
    </div>
  </div>
  <div class="note">
    <p>Les dates suivantes sont publiées dans l’agenda du Nid, avec l’ajout au calendrier et les
    autres rendez-vous du lieu : <a href="/le-nid#agenda" style="color:var(--gold2);text-decoration:underline;text-decoration-color:rgba(216,178,90,.45);text-underline-offset:3px">voir l’agenda du Nid</a>.</p>
    <p>Réservation et participation : <a href="{M}" style="color:var(--gold2);text-decoration:underline;text-decoration-color:rgba(216,178,90,.45);text-underline-offset:3px">contact@resonancesproductions.org</a>.
    Le code du portail vous est communiqué avec votre confirmation d’inscription.</p>
  </div>
</div></section>

<div class="divider"></div>
""".replace('{M}', MAILTO_CONTACT))

    # ================================================= APPEL A CANDIDATURE
    #
    # ============ EXPERIENCE D'ANIMATION (ajout 13/08/2026) ============
    # (bloc `<div class="xp" id="experience">`, plus bas dans ce gabarit)
    # Chiffres verifies dans parcours_consolide.json : 26 ateliers musicaux
    # tous en role=confirme et confiance=haute (23 « atelier-calebasse » +
    # 3 « atelier-harpe-voix »), du 15/03/2023 au 15/03/2026, en France,
    # en Suisse et en Hongrie. Aucun evenement « a-confirmer » n'est affiche.
    # Aucun nom de personne ni de participant : uniquement des lieux.
    #
    # ==================== FORMULAIRE DE CANDIDATURE ====================
    # (bloc `<form class="form" id="candidature">`, plus bas dans ce gabarit)
    # Site statique, aucun backend : l'envoi compose un email pre-rempli.
    # Repli sans JavaScript = action mailto native + <noscript>.
    A("""
<section class="blk appel" id="appel"><div class="wrap">
  <div class="badge"><span aria-hidden="true">🥁</span><span>Appel à candidature · il reste environ 4 places</span></div>
  <h2>Créons un groupe de pratique à Paris</h2>

  <div class="letter">
    <p class="big">Et si on créait un groupe de pratique calebasse ?</p>
    <p>Plusieurs personnes passées par mes ateliers m’ont dit la même chose : elles voulaient
    continuer. Pas seulement garder le souvenir d’un bel après-midi — une pratique qui s’installe,
    qui creuse, qui progresse. J’ai envie de leur répondre oui.</p>
    <p>Alors je monte un <b>groupe de pratique régulier à Paris</b> : une progression dans la durée,
    à la fois collective et personnelle. On se retrouve au Nid, <b>un workshop par mois, pendant un
    an</b>. Le groupe se connaît, on ne repart pas de zéro à chaque fois — et c’est précisément là
    que le rythme devient autre chose qu’un exercice.</p>
    <p>C’est ouvert à toute personne motivée et engagée sur la durée, <b>quel que soit ton
    niveau</b>. Débutant complet ou déjà à l’aise : ce qui compte, c’est l’envie d’avancer
    ensemble. Tu n’as pas besoin de posséder une calebasse, elle est fournie. Tu n’as pas besoin de
    savoir lire la musique. Tu n’as même pas besoin d’« avoir le rythme » — c’est exactement ce
    qu’on vient travailler.</p>
    <p>Ce que je demande, en revanche, c’est l’<b>engagement</b> : un groupe de pratique ne tient
    que si les gens sont là. Le noyau existe déjà, <b>il me manque environ quatre personnes</b>
    pour lancer.</p>
    <p><span class="emo">❤️</span>Et ce n’est qu’un début. Mon rêve, c’est de faire de cet espace un lieu vivant : une
    communauté autour du rythme et de cette approche de la musique, mais aussi de petits concerts
    et des soirées partage, où chacun peut venir être qui il est, dans la bienveillance et le
    soutien. J’aimerais que tu en sois.</p>
    <p class="sign">Au plaisir de te rencontrer,<br>David</p>
  </div>

  <div class="facts">
    <div class="fact"><div class="k">Où</div><div class="v">Le Nid, Paris 20<sup>e</sup><small>29 rue des Orteaux</small></div></div>
    <div class="fact"><div class="k">Rythme</div><div class="v">1 workshop par mois</div></div>
    <div class="fact"><div class="k">Engagement</div><div class="v">1 an</div></div>
    <div class="fact"><div class="k">Places</div><div class="v">Environ 4 restantes</div></div>
    <div class="fact"><div class="k">Niveau</div><div class="v">Tous<small>débutant compris</small></div></div>
    <div class="fact"><div class="k">Instrument</div><div class="v">Fourni</div></div>
  </div>

  <div class="note">
    <p><b>Et si le mensuel ne te convient pas ?</b> Dis-le quand même. Le rythme d’un workshop par
    mois est celui qui se dessine aujourd’hui, mais certains préféreraient tous les quinze jours ou
    une fois par semaine. Indique ta préférence dans le formulaire : David en tient compte pour
    fixer le rythme définitif du groupe.</p>
  </div>

  <div class="xp" id="experience">
    <div class="h-min">Ce qui est déjà éprouvé</div>
    <h3>26 ateliers de rythme déjà animés depuis 2023</h3>
    <p class="body">S’engager un an, ça se décide sur du concret plutôt que sur une promesse.
    Depuis 2023, David a animé <b>26 ateliers</b> de rythme — <b>23 à la calebasse</b> et
    <b>3 de harpe africaine et de voix</b> — <b>en France, en Suisse et en Hongrie</b>. En petit
    comité comme en grand cercle de festival, le dernier au Nid en mars 2026.</p>
    <p class="body">Ces ateliers se sont tenus dans des cadres qui ont chacun leurs exigences :</p>
    <ul class="lst">
      <li><b>Deux maisons de percussions et de musiques du monde</b> — Percussion Du Monde, à
      Paris (quatre ateliers), et Djoliba Instruments du Monde, à Toulouse.</li>
      <li><b>Des festivals, en France</b> — le Festival Été Nomade, à Port Dienville (quatre
      ateliers), le Castle Handpan Festival, au château de Frasne-le-Château, et le Festival
      Arts Extatics.</li>
      <li><b>En Hongrie</b> — l’Everness Festival (trois ateliers), le HUG Fesztivál, la rencontre
      hongroise du handpan et des musiques du monde, et deux ateliers au Sziget, à Budapest.</li>
      <li><b>En Suisse et ailleurs en France</b> — le théâtre OZ de Martigny, l’église
      Saint-Jean-l’Évangéliste de Tourcoing, et Le Nid.</li>
    </ul>
    <p class="body">Ce n’est pas un palmarès. C’est ce qui permet de te proposer une année sans
    la promettre à la légère : la manière de faire entrer un groupe dans le rythme a été éprouvée
    assez souvent, et dans des contextes assez différents, pour ne pas s’improviser en chemin. Un
    atelier de deux heures et un groupe suivi sur douze mois ne demandent pas la même chose — mais
    tu ne seras pas le premier cercle que David fait démarrer.</p>
  </div>

  <form class="form" id="candidature"
        action="mailto:contact@resonancesproductions.org?subject=Candidature%20%E2%80%94%20groupe%20de%20pratique%20calebasse"
        method="post" enctype="text/plain">
    <h3>Poser ma candidature</h3>
    <p class="intro">Quelques minutes, et David te répond personnellement. Les champs marqués
    d’une <span class="req">*</span> sont nécessaires.</p>

    <noscript>
      <div class="note" style="margin-top:18px">
        <p><b>JavaScript est désactivé.</b> Le bouton ci-dessous ouvrira quand même votre logiciel
        de messagerie, mais la mise en forme sera brute. Le plus simple est d’écrire directement à
        <a href="mailto:contact@resonancesproductions.org" style="color:var(--gold2)">contact@resonancesproductions.org</a>
        en indiquant : prénom, nom, email, téléphone (facultatif), votre niveau (débutant / a déjà
        pratiqué / plus avancé), le rythme souhaité (1×/mois, tous les 15 jours, 1×/semaine), vos
        disponibilités, et quelques lignes sur ce qui vous donne envie d’en faire partie.</p>
      </div>
    </noscript>

    <div class="row">
      <div class="f">
        <label for="c-prenom">Prénom <span class="req">*</span></label>
        <input id="c-prenom" name="prenom" type="text" autocomplete="given-name" required>
        <span class="err" role="alert"></span>
      </div>
      <div class="f">
        <label for="c-nom">Nom <span class="req">*</span></label>
        <input id="c-nom" name="nom" type="text" autocomplete="family-name" required>
        <span class="err" role="alert"></span>
      </div>
    </div>

    <div class="row">
      <div class="f">
        <label for="c-email">Email <span class="req">*</span></label>
        <input id="c-email" name="email" type="email" autocomplete="email" required>
        <span class="err" role="alert"></span>
      </div>
      <div class="f">
        <label for="c-tel">Téléphone <span class="hint inl">(facultatif)</span></label>
        <input id="c-tel" name="telephone" type="tel" autocomplete="tel">
        <span class="err" role="alert"></span>
      </div>
    </div>

    <div class="f">
      <label for="c-niveau">Ton niveau <span class="req">*</span>
        <span class="hint">Il n’y a pas de mauvaise réponse : le groupe accueille les débutants.</span>
      </label>
      <select id="c-niveau" name="niveau" required>
        <option value="">— choisir —</option>
        <option value="Débutant">Débutant — je n’ai jamais pratiqué</option>
        <option value="A déjà pratiqué">J’ai déjà pratiqué (atelier, cours, un peu de percussions)</option>
        <option value="Plus avancé">Plus avancé — je joue régulièrement</option>
      </select>
      <span class="err" role="alert"></span>
    </div>

    <fieldset>
      <legend>Le rythme qui te conviendrait le mieux <span class="req">*</span>
        <span class="hint">Le groupe démarre sur un workshop par mois ; ta préférence compte pour la suite.</span>
      </legend>
      <div class="opts">
        <label class="opt"><input type="radio" name="rythme" value="1 fois par mois" required> Une fois par mois</label>
        <label class="opt"><input type="radio" name="rythme" value="Tous les 15 jours"> Tous les 15 jours</label>
        <label class="opt"><input type="radio" name="rythme" value="1 fois par semaine"> Une fois par semaine</label>
      </div>
      <span class="err" role="alert"></span>
    </fieldset>

    <div class="f">
      <label for="c-dispos">Tes disponibilités <span class="hint">facultatif — quels jours, quels créneaux te vont le mieux ?</span></label>
      <input id="c-dispos" name="dispos" type="text" placeholder="Ex. : samedi après-midi, ou dimanche matin">
      <span class="err" role="alert"></span>
    </div>

    <div class="f">
      <label for="c-motiv">Pourquoi tu veux en faire partie <span class="req">*</span>
        <span class="hint">Quelques lignes suffisent — dis-le avec tes mots.</span>
      </label>
      <textarea id="c-motiv" name="motivation" rows="6" required></textarea>
      <span class="err" role="alert"></span>
    </div>

    <div class="summary" id="form-summary" role="alert" aria-live="assertive"></div>

    <div class="form-actions">
      <button class="btn" type="submit">Composer ma candidature ✉</button>
      <span class="hint" style="color:var(--muted);font-size:14.5px">Ouvre ta messagerie avec le message déjà écrit.</span>
    </div>

    <p class="rgpd">Ce site est statique : <b>rien n’est enregistré ici</b>. Le bouton prépare
    simplement un email que tu envoies depuis ta propre messagerie, à
    contact@resonancesproductions.org. Tes réponses ne servent qu’à constituer le groupe et ne sont
    transmises à personne d’autre.</p>

    <div class="sent" id="form-sent" aria-live="polite">
      <h4>Ta candidature est prête ✦</h4>
      <p>Ta messagerie devrait s’être ouverte avec ce message — <b>il reste à l’envoyer</b>.
      Si rien ne s’est ouvert, copie le texte ci-dessous et envoie-le à
      contact@resonancesproductions.org.</p>
      <label for="form-text" class="hint" style="display:block;margin-top:12px;color:var(--muted)">Le message composé</label>
      <textarea id="form-text" readonly></textarea>
      <div class="acts">
        <button class="btn ghost" type="button" id="form-copy">Copier le message</button>
        <a class="btn ghost" id="form-mail" href="mailto:contact@resonancesproductions.org">Ouvrir ma messagerie</a>
        <span class="copied" id="form-copied" role="status" aria-live="polite"></span>
      </div>
    </div>
  </form>
</div></section>

<div class="divider"></div>
""")

    # ------------------------------------------------------ INTERVENTIONS
    A("""
<section class="blk" id="interventions"><div class="wrap">
  <div class="h-min">Ailleurs qu’au Nid</div>
  <h2>Faire venir l’atelier chez vous</h2>
  <p class="lead">Festival, séminaire, école, temps d’équipe, événement associatif : l’atelier de
  rythme se déplace, et il change alors complètement d’échelle. C’est un format différent de celui
  du Nid — beaucoup plus large.</p>
  <div class="facts">
    <div class="fact"><div class="k">Durée</div><div class="v">2 heures</div></div>
    <div class="fact"><div class="k">Participants</div><div class="v">Jusqu’à 50</div></div>
    <div class="fact"><div class="k">Instruments</div><div class="v">Fournis<small>une calebasse, un tapis et deux œufs par personne</small></div></div>
    <div class="fact"><div class="k">Lieu requis</div><div class="v">Grand espace fermé<small>impérativement un sol dur</small></div></div>
  </div>
  <div class="note">
    <p><b>Le sol conditionne tout.</b> Béton, carrelage, pierre ou bois plein : sans cela, les
    infra-basses ne sortent pas et l’atelier perd sa puissance. Une salle entourée de murs amplifie
    encore le son.</p>
    <p>Tarif, jauge exacte et conditions sont établis au cas par cas selon le contexte :
    <a href="{M}?subject=Atelier%20de%20rythme%20%C3%A0%20la%20calebasse%20%E2%80%94%20demande%20d%E2%80%99intervention" style="color:var(--gold2);text-decoration:underline;text-decoration-color:rgba(216,178,90,.45);text-underline-offset:3px">écrivez-nous</a>.</p>
  </div>
</div></section>

<div class="divider"></div>
""".replace('{M}', MAILTO_CONTACT))

    # --------------------------------------------------------- QUI EST DAVID
    A("""
<section class="blk band" id="david"><div class="wrap">
  <div class="h-min">Qui transmet</div>
  <h2>David Lesage</h2>
  <div class="two">
    <div>
      <p class="body">Chanteur et musicien multi-instrumentiste, <b>batteur percussionniste depuis
      l’âge de 4 ans</b>. Il aime et explore le rythme sous de nombreuses approches, essentiellement
      en autodidacte et en expérimentateur dans son jeune âge.</p>
      <p class="body">Il suit le parcours du collège de <b>Jazz in Marciac</b>, puis obtient un
      <b>prix de conservatoire de batterie à Toulouse en 2012</b>. Il poursuit ensuite son parcours
      de musicien autour du monde. Il est aujourd’hui chanteur et multi-instrumentiste, notamment
      joueur de <b>handpan</b> — l’instrument qui relie la mélodie et le rythme.</p>
      <p class="body">C’est de cette double appartenance, la percussion et la voix, qu’est née sa
      manière de transmettre le rythme : par le corps, par le chant, et par la calebasse.</p>
      <div class="cta">
        <a class="btn ghost" href="/le-nid">Découvrir Le Nid</a>
      </div>
    </div>
    <figure class="fig">
""" + p('david-calebasse', sizes, sizes_attr='(max-width:820px) 100vw, 360px') + """
      <figcaption>David Lesage et sa calebasse, pyrogravée du logo Now Groove.</figcaption>
    </figure>
  </div>
</div></section>

<div class="divider"></div>
""")

    # ------------------------------------------------------- POUR ALLER PLUS LOIN
    A("""
<section class="blk" id="plus-loin"><div class="wrap">
  <div class="h-min">Pour aller plus loin</div>
  <h2>Entre deux workshops</h2>
  <div class="cards">
    <div class="card">
      <div class="t">Méthode vidéo</div>
      <h3>Now Groove</h3>
      <p>La méthode d’apprentissage du rythme à la calebasse créée par David : 7 h 30 de cours
      vidéo, 107 pages de supports et d’exercices, et un groupe d’élèves privé.</p>
      <a class="go" href="https://www.helloasso.com/associations/resonances-productions/boutiques/formation-de-rythme-now-groove-david-lesage" target="_blank" rel="noopener">Voir la formation ↗</a>
    </div>
    <div class="card">
      <div class="t">Instrument</div>
      <h3>Une calebasse à soi</h3>
      <p>Les calebasses sélectionnées, travaillées à la main et pyrogravées à l’atelier de
      l’association — avec leur tapis et leurs œufs.</p>
      <a class="go" href="mailto:contact@resonancesproductions.org?subject=Une%20calebasse%20%E2%80%94%20renseignements">Nous écrire</a>
    </div>
    <div class="card">
      <div class="t">Au Nid</div>
      <h3>Cours individuels</h3>
      <p>Un accompagnement sur mesure, seul·e à seul·e, sur le rythme et la calebasse. Les autres
      rendez-vous du lieu sont dans l’agenda.</p>
      <a class="go" href="/le-nid#agenda">L’agenda du Nid</a>
    </div>
  </div>
</div></section>
""")

    A(FOOTER)
    A('\n<a class="totop" href="#top" aria-label="Revenir en haut de la page">↑</a>\n')
    A(JS)
    A('\n</body></html>\n')

    return head + '\n'.join(body)


def main():
    sizes = build_images()
    html = build_html(sizes)
    # menu de navigation partage : remplace le <div class="links"> du gabarit
    html = nav_menu.inject(html, 'rythme-calebasse')

    # ---- garde-fous STRUCTURELS, avant l'ecriture -------------------------
    # Le bloc « experience » (26 ateliers) vit dans le gabarit de la section
    # #appel : il est donc produit une fois et une seule par construction. Ce
    # garde-fou est la pour le cas ou quelqu'un le deplacerait vers une
    # injection post-traitement : il attrape AUSSI BIEN sa disparition que sa
    # duplication (le piege des 4 cartes identiques). On refuse d'ecrire une
    # page cassee plutot que d'imprimer un avertissement qui defile.
    for marker, label in (('id="experience"', 'bloc experience (26 ateliers)'),
                          ('data-nav="%s"' % nav_menu.NAV_VERSION,
                           'menu partage nav_menu.py')):
        n = html.count(marker)
        if n != 1:
            raise SystemExit(
                '!! ABANDON : %d occurrence(s) de « %s » (%s), attendu 1. '
                'Page NON ecrite.' % (n, marker, label))

    # Aucune note de redaction en commentaire HTML dans la page livree : elles
    # seraient publiques et indexables. Leur place est ici, en commentaire `#`.
    verif_commentaires.verifier(html, OUT_HTML)

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)
    print('[page]   %s  (%.1f Ko)' % (OUT_HTML, len(html.encode('utf-8')) / 1024))
    # garde-fous : un seul <h1>, pas d'image distante
    n_h1 = html.count('<h1')
    if n_h1 != 1:
        print('!! ATTENTION : %d <h1> dans la page' % n_h1)
    for bad in ('http://img', 'googleusercontent', 'squarespace', 'cloudfront'):
        if bad in html:
            print('!! ATTENTION : reference distante « %s »' % bad)


if __name__ == '__main__':
    main()
