# -*- coding: utf-8 -*-
"""Genere /rituals-trio/index.html a partir de sources/trio_source.html.

Comme pour /rituals, plus aucune photo en base64 (la page pesait 4,4 Mo) et
plus aucune image servie depuis Google Drive : tout est ecrit en fichiers,
en trois largeurs (480 / 900 / 1400 px), WebP + repli JPEG, via <picture>.

Les photos communes avec /rituals sont ecrites dans /img/rituals/ et
partagees : un visiteur qui voit les deux pages ne les telecharge qu'une fois.
Seules les photos propres au trio (festival Perspectives, portrait de Julien)
vont dans /img/rituals-trio/.

Dossiers d'entree attendus a cote de ce script (photos d'origine, hors depot) :
  promo_raw/   web_img/   trio_img/
  perspectives_raw/  (photos du festival ; telechargees depuis Drive au besoin,
                      puis mises en cache dans ce dossier)
Sortie : ../img/rituals/, ../img/rituals-trio/ et ../rituals-trio/index.html
"""
import glob, os, re, sys, unicodedata, html as _html
from urllib.request import urlopen
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DIR_SHARED = os.path.join(REPO, 'img', 'rituals')        # photos communes
DIR_TRIO = os.path.join(REPO, 'img', 'rituals-trio')     # photos propres au trio
URL_SHARED = '/img/rituals'
URL_TRIO = '/img/rituals-trio'
SOURCE = os.path.join(HERE, 'trio_source.html')
TARGET = os.path.join(REPO, 'rituals-trio', 'index.html')
CACHE = os.path.join(HERE, 'perspectives_raw')

WIDTHS = (480, 900, 1400)
Q_WEBP = 80
Q_JPEG = 82

SIZES_FIG = '(max-width:1040px) calc(100vw - 52px), 988px'
SIZES_SLIDE = '(max-width:900px) 86vw, 700px'
SIZES_APHOTO = '(max-width:600px) 62vw, 210px'

SLUGS = {
    'Au Grand Rex devant 2700 personnes': 'au-grand-rex',
    'L’induction — la voix qui guide, vers un état de conscience élargie': 'l-induction',
}


def slug(txt):
    t = _html.unescape(txt).replace('’', "'").replace('&', ' et ')
    for a, b in (('œ', 'oe'), ('Œ', 'oe'), ('æ', 'ae'), ('Æ', 'ae')):
        t = t.replace(a, b)
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c)).lower()
    t = re.sub(r'[^a-z0-9]+', '-', t).strip('-')
    if len(t) > 52:
        t = t[:52].rsplit('-', 1)[0]
    return SLUGS.get(txt, t)


def variants(im, outdir, name):
    os.makedirs(outdir, exist_ok=True)
    im = im.convert('RGB')
    ow, oh = im.size
    out = []
    for w in WIDTHS:
        if w > ow and out:
            break
        ww = min(w, ow)
        hh = max(1, round(oh * ww / ow))
        r = im if (ww, hh) == (ow, oh) else im.resize((ww, hh), Image.LANCZOS)
        r.save(os.path.join(outdir, '%s-%d.webp' % (name, ww)), 'WEBP',
               quality=Q_WEBP, method=6)
        r.save(os.path.join(outdir, '%s-%d.jpg' % (name, ww)), 'JPEG',
               quality=Q_JPEG, optimize=True, progressive=True)
        out.append((ww, hh))
    return out


def picture(urlbase, vs, sizes, alt, cls='', extra='', img_extra='', lazy=True):
    webp = ', '.join('%s-%d.webp %dw' % (urlbase, w, w) for w, h in vs)
    jpeg = ', '.join('%s-%d.jpg %dw' % (urlbase, w, w) for w, h in vs)
    dw, dh = min(vs, key=lambda v: abs(v[0] - 900))
    c = ' class="%s"' % cls if cls else ''
    return ('<picture%s%s><source type="image/webp" srcset="%s" sizes="%s">'
            '<img%s src="%s-%d.jpg" srcset="%s" sizes="%s" width="%d" height="%d"'
            ' alt="%s" loading="%s" decoding="async"></picture>'
            % (c, extra, webp, sizes, img_extra, urlbase, dw, jpeg, sizes,
               vs[-1][0], vs[-1][1], alt, 'lazy' if lazy else 'eager'))


# ------------------------------------------------------------- photos d'origine
def _open(path, mw, crop=None):
    im = Image.open(path).convert('RGB')
    if crop:
        w, h = im.size
        im = im.crop((int(crop[0] * w), int(crop[1] * h),
                      int(crop[2] * w), int(crop[3] * h)))
    im.thumbnail((mw, mw))
    return im


def find(tok):
    hits = sorted(glob.glob(os.path.join(HERE, 'promo_raw', '*' + tok + '*')))
    if not hits:
        sys.exit('photo introuvable dans promo_raw/ : ' + tok)
    return hits[0]


def promo(tok, mw, name, crop=None):
    """Photo commune avec /rituals -> ecrite dans /img/rituals/."""
    return URL_SHARED + '/' + name, variants(_open(find(tok), mw, crop),
                                             DIR_SHARED, name)


def web(fn, mw, name, crop=None):
    p = os.path.join(HERE, 'web_img', fn)
    if not os.path.exists(p):
        sys.exit('photo introuvable dans web_img/ : ' + fn)
    return URL_SHARED + '/' + name, variants(_open(p, mw, crop), DIR_SHARED, name)


def drive(fid, name):
    """Photo du festival Perspectives -> /img/rituals-trio/ (cache local)."""
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, fid + '.jpg')
    if not os.path.exists(p):
        url = 'https://lh3.googleusercontent.com/d/%s=w2000' % fid
        print('    telechargement', fid)
        with urlopen(url, timeout=90) as r, open(p, 'wb') as f:
            f.write(r.read())
    return URL_TRIO + '/' + name, variants(Image.open(p), DIR_TRIO, name)


def trio_img(fn, mw, name):
    p = os.path.join(HERE, 'trio_img', fn)
    if not os.path.exists(p):
        sys.exit('photo introuvable dans trio_img/ : ' + fn)
    return URL_TRIO + '/' + name, variants(_open(p, mw), DIR_TRIO, name)


CAP_INTENTION = 'Le public au cœur du rituel'
CAP_REX = 'Au Grand Rex devant 2700 personnes'
CAP_INDUCTION = 'L’induction — la voix qui guide, vers un état de conscience élargie'
CAP_PERSP = 'Le trio en scène — festival Perspectives'

print('images :')
u_hero, v_hero = web('RITUALS_00_header.jpg', 1600, 'hero-grand-rex')
u_intent, v_intent = promo('20248.', 1300, slug(CAP_INTENTION))
u_rex, v_rex = web('RITUALS_00_header.jpg', 1500, slug(CAP_REX))
u_induc, v_induc = promo('iris_priere', 1300, slug(CAP_INDUCTION))
u_key, v_key = promo('20245.', 1400, 'cle-de-voute-duo-theatre')
u_david, v_david = promo('David_Lesage_2025_Carre_HD', 900, 'portrait-david-lesage')
u_iris, v_iris = web('RITUALS_06_Iris-Chasles.jpg', 700, 'portrait-iris-chasles',
                     crop=(0.20, 0.0, 0.82, 0.78))
u_julien, v_julien = trio_img('julien_sax.jpg', 1200,
                              'portrait-julien-dub-au-saxophone')

GAL = [
 ('202417.', 'Le corps en mouvement'),
 ('202418.', 'Une connexion forte avec le public'),
 ('202419.', 'Danser la vie'),
 ('202420.', 'Everness Festival, Hongrie'),
 ('202423.', 'L’élan'),
 ('Solune_31', 'Le tournoiement de la beauté'),
 ('202428.', 'Un univers musical électro-organique'),
 ('202443.', 'Respirer en mouvement'),
 ('202444.', 'Retrouver son enfant intérieur'),
 ('202450.', 'Être touché dans son cœur'),
 ('202451.', 'Chanter la joie'),
 ('202452.', 'Chanter ensemble'),
 ('19-42-24', 'Touchée par la grâce'),
 ('David_Lesage_2025_Carre', 'David Lesage'),
 ('RITUALS_07_duo', 'David & Iris'),
 ('everness_faceaface', 'Iris & David, face à face'),
 ('david_iris_la_beaute', 'L’amour au service du collectif'),
 ('iris_soa', 'Iris Chasles'),
]

# photos du festival Perspectives (partage par lien Drive, rapatriees en local)
PERSP = [
 ('15_WWObM1AP2FFVWwKGpd_eAkFJzcFQP1', CAP_PERSP),
 ('1VcrMZyQ22RiJls2UOZjLHKjT7mZ9fsGL', 'Julien Dub au saxophone'),
 ('1MSChhHk6HMghZFIr1U0KMhV1ptp4U2Zw', 'Le public en prière'),
 ('1u5LIqjQWaaEU4d4ejVEz_gnNEBCm0PmU', 'Portés ensemble'),
 ('1aJJWBsCRWG7sHeO-Kh-Hg_uNHnmIz_jn', 'Julien &amp; David — le souffle et le rythme'),
 ('11IHtfighVSWGfCaMoWtcC3PD2f9lODkp', 'La danse collective'),
 ('1gpnX7USd9A9mY4YKN00KZYdYH5_BFRlM', "Iris &amp; David — l'instant de la prière"),
 ('13MPc99NcHg0kAGWhwK5Vlwvjufejhd3j', 'Iris Chasles — le chant qui relie'),
 ('1dm_aLuZRE8KJTZbvL9gs18vy3TlNVbpc', 'Recueilli'),
 ('1zD5Z0GoUVJsJPlfGgVmmNhxs8lOXQYah', 'Communier en cercle'),
 ('1vz2C4Bbbl84BlLwPTHST-og0IHQZ_OO0', 'Autour du feu'),
 ('1E2EYQ1c9kdzDJ5o3f2vyTkZu0NwL-Guv', 'Le final, tous ensemble'),
 ('1JZ1VReu_akPLqEgefqjf7v7zJpk8xrGj', 'Julien Dub'),
]
PERSP_NAME = {
 '15_WWObM1AP2FFVWwKGpd_eAkFJzcFQP1': 'le-trio-en-scene-festival-perspectives',
 '1VcrMZyQ22RiJls2UOZjLHKjT7mZ9fsGL': 'julien-dub-au-saxophone',
 '1MSChhHk6HMghZFIr1U0KMhV1ptp4U2Zw': 'le-public-en-priere',
 '1u5LIqjQWaaEU4d4ejVEz_gnNEBCm0PmU': 'portes-ensemble',
 '1aJJWBsCRWG7sHeO-Kh-Hg_uNHnmIz_jn': 'julien-et-david-le-souffle-et-le-rythme',
 '11IHtfighVSWGfCaMoWtcC3PD2f9lODkp': 'la-danse-collective',
 '1gpnX7USd9A9mY4YKN00KZYdYH5_BFRlM': 'iris-et-david-l-instant-de-la-priere',
 '13MPc99NcHg0kAGWhwK5Vlwvjufejhd3j': 'iris-chasles-le-chant-qui-relie',
 '1dm_aLuZRE8KJTZbvL9gs18vy3TlNVbpc': 'recueilli',
 '1zD5Z0GoUVJsJPlfGgVmmNhxs8lOXQYah': 'communier-en-cercle',
 '1vz2C4Bbbl84BlLwPTHST-og0IHQZ_OO0': 'autour-du-feu',
 '1E2EYQ1c9kdzDJ5o3f2vyTkZu0NwL-Guv': 'le-final-tous-ensemble',
 '1JZ1VReu_akPLqEgefqjf7v7zJpk8xrGj': 'portrait-julien-dub',
}

with open(SOURCE, 'r', encoding='utf-8') as f:
    html = f.read()

CSS_ADD = """
.nav{position:fixed;top:0;left:0;right:0;z-index:60;display:flex;align-items:center;justify-content:space-between;padding:16px 26px;background:rgba(14,15,36,.82);backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.06)}
.nav .brand{font-family:'Cormorant Garamond',serif;letter-spacing:.14em;text-transform:uppercase;font-size:13.5px;color:#fff;text-decoration:none}
.nav .brand:hover{color:var(--gold2)}
.nav .links{display:flex;align-items:center;gap:20px}
.nav .links a{color:var(--muted);text-decoration:none;font-size:14px}
.nav .links a:hover{color:var(--gold2)}
@media(max-width:700px){.nav .links a.hide-s{display:none}.nav .brand{font-size:12px}}
@media print{.nav{display:none}}
.figure{margin-top:38px;border-radius:16px;overflow:hidden;border:1px solid var(--line)}
.figure img{width:100%;display:block}
.cap{color:var(--muted);font-size:13.5px;margin-top:10px;text-align:center;font-style:italic}
.figsec{padding:14px 0}
.artist{position:relative}
.aphoto{width:210px;border-radius:16px;border:1px solid var(--line);float:right;margin:2px 0 16px 28px}
.gallery-sec{background:linear-gradient(180deg,#0b0c1e,var(--night))}
.carousel{position:relative;margin-top:34px}
.car-track{display:flex;gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;padding:4px 2px 14px}
.car-track::-webkit-scrollbar{height:8px}
.car-track::-webkit-scrollbar-thumb{background:var(--line);border-radius:8px}
.slide{flex:0 0 auto;scroll-snap-align:center;position:relative;border-radius:12px;overflow:hidden;border:1px solid rgba(255,255,255,.08)}
.slide img{height:460px;width:auto;max-width:90vw;display:block;cursor:zoom-in}
.cap2{position:absolute;left:0;right:0;bottom:0;background:linear-gradient(transparent,rgba(0,0,0,.78));color:#fff;font-size:12.5px;padding:24px 14px 10px;text-align:center;font-style:italic}
.car-btn{position:absolute;top:50%;transform:translateY(-50%);z-index:3;background:rgba(18,19,43,.72);color:#fff;border:1px solid var(--line);width:46px;height:46px;border-radius:50%;font-size:22px;cursor:pointer}
.car-btn.prev{left:-4px}.car-btn.next{right:-4px}
.car-play{display:none;position:absolute;top:-52px;right:0;z-index:4;align-items:center;gap:6px;background:var(--gold);color:#1a1608;border:none;padding:8px 16px;border-radius:20px;font-size:13px;font-weight:600;cursor:pointer}
@media(max-width:900px){.slide img{height:auto;width:auto;max-width:86vw;max-height:62vh}}
@media(max-width:600px){.aphoto{float:none;width:62%;display:block;margin:0 auto 16px}.car-btn{display:none}}

/* ===== IMAGES LOCALES RESPONSIVES (WebP + repli JPEG) =====
   <picture> ne doit rien changer a la mise en page : il se comporte comme un bloc
   transparent et l'<img> garde exactement les regles CSS d'origine. */
picture{display:block}
/* Les attributs width/height valent aussi comme indication de style : sans
   height:auto explicite, la hauteur en attribut s'appliquerait comme une
   longueur CSS et deformerait l'image (cas des .figure, du teaser, etc.). */
picture>img{height:auto}
picture.aphoto{overflow:hidden}
picture.aphoto>img{width:100%;height:auto;display:block;border-radius:inherit}

/* Le carrousel : chaque diapo RESERVE sa largeur a partir de son rapport
   largeur/hauteur (--ar). Sans cela, loading="lazy" ferait s'effondrer les
   diapos non encore chargees a ~1 px et le defilement serait casse.
   La geometrie reste celle d'avant : hauteur 460 px en grand ecran, et sur
   petit ecran l'image tient dans 86vw x 62vh. */
.slide{width:min(calc(460px * var(--ar,1.5)),90vw)}
.slide picture{width:100%}
.slide img{height:auto;width:100%;max-width:100%;aspect-ratio:var(--ar,1.5)}
@media(max-width:900px){
  .slide{width:min(86vw,calc(62vh * var(--ar,1.5)))}
  .slide img{height:auto;width:100%;max-width:100%;max-height:none}
}
@media print{.slide{width:100%!important}.slide picture{width:100%!important}}
__BG__</style>"""


def bg_rules(sel, urlbase, vs, grad, pos):
    def rule(w):
        return ('.%s{background:%s,url(%s-%d.jpg) %s}\n'
                '.%s{background:%s,image-set(url(%s-%d.webp) type("image/webp"),'
                'url(%s-%d.jpg) type("image/jpeg")) %s}\n'
                % (sel, grad, urlbase, w, pos,
                   sel, grad, urlbase, w, urlbase, w, pos))
    wide = vs[-1][0]
    small = min((v[0] for v in vs if v[0] >= 900), default=wide)
    css = rule(wide)
    if small != wide:
        css += '@media(max-width:900px){\n' + rule(small) + '}\n'
    return css


GRAD_HERO = 'linear-gradient(rgba(10,11,28,.52),rgba(10,11,28,.78))'
GRAD_KEY = 'linear-gradient(rgba(11,12,30,.74),rgba(11,12,30,.88))'
CSS_ADD = CSS_ADD.replace('__BG__',
                          bg_rules('hero', u_hero, v_hero, GRAD_HERO, 'center/cover')
                          + bg_rules('keystone', u_key, v_key, GRAD_KEY,
                                     'center 35%/cover'))
html = html.replace('</style>', CSS_ADD, 1)


def figblock(urlbase, vs, cap, lazy=True):
    return ('<section class="figsec"><div class="wrap"><div class="figure">'
            + picture(urlbase, vs, SIZES_FIG, cap, lazy=lazy)
            + '</div><div class="cap">' + cap + '</div></div></section>\n')


# figure de l'intention (premiere image de la page : chargement immediat)
sig = '  <div class="sig">On en repart plus léger. Comme au sortir d’une longue inspiration.</div>'
assert sig in html, 'ancre sig introuvable'
html = html.replace(sig, sig + '\n  <div class="figure">'
                    + picture(u_intent, v_intent, SIZES_FIG, CAP_INTENTION, lazy=False)
                    + '</div>\n  <div class="cap">' + CAP_INTENTION + '</div>', 1)

# le trio en scene, avant « Le voyage »
u_persp1, v_persp1 = drive('15_WWObM1AP2FFVWwKGpd_eAkFJzcFQP1',
                           PERSP_NAME['15_WWObM1AP2FFVWwKGpd_eAkFJzcFQP1'])
anchor_voyage = '<section class="journey"><div class="wrap">\n  <div class="kick">Le voyage</div>'
assert anchor_voyage in html, 'ancre voyage introuvable'
html = html.replace(anchor_voyage,
                    figblock(u_persp1, v_persp1, CAP_PERSP) + anchor_voyage, 1)

# le Grand Rex, au-dessus de « Pour les organisateurs »
anchor_orga = '<section class="orga"><div class="wrap">\n  <div class="kick">Pour les organisateurs</div>'
assert anchor_orga in html, 'ancre orga introuvable'
html = html.replace(anchor_orga, figblock(u_rex, v_rex, CAP_REX) + anchor_orga, 1)

# la photo d'induction est placee APRES la cle de voute
assert '<!--INDUCTION_FIG-->' in html
html = html.replace('<!--INDUCTION_FIG-->',
                    figblock(u_induc, v_induc, CAP_INDUCTION), 1)

# photos des artistes
html = html.replace('<div class="artist">\n    <h3>David Lesage</h3>',
                    '<div class="artist">\n    '
                    + picture(u_david, v_david, SIZES_APHOTO, 'David Lesage',
                              cls='aphoto')
                    + '\n    <h3>David Lesage</h3>', 1)
html = html.replace('<div class="artist">\n    <h3>Iris Chasles</h3>',
                    '<div class="artist">\n    '
                    + picture(u_iris, v_iris, SIZES_APHOTO, 'Iris Chasles',
                              cls='aphoto')
                    + '\n    <h3>Iris Chasles</h3>', 1)
assert '<!--JULIEN_PHOTO-->' in html
html = html.replace('<!--JULIEN_PHOTO-->',
                    picture(u_julien, v_julien, SIZES_APHOTO,
                            'Julien Dub au saxophone', cls='aphoto'), 1)

# ------------------------------------------------------------------ carrousel
# entrelacement proportionnel : tantot David & Iris, tantot le trio avec Julien
_PORTRAITS = ('David_Lesage_2025_Carre', 'iris_soa')
_JULIEN_PORTRAIT = '1JZ1VReu_akPLqEgefqjf7v7zJpk8xrGj'
_OUVERTURE = '15_WWObM1AP2FFVWwKGpd_eAkFJzcFQP1'

_duo = [('L', t, c) for t, c in GAL if t not in _PORTRAITS]
_trio = [('U', f, c) for f, c in PERSP
         if f != _JULIEN_PORTRAIT and f != _OUVERTURE]
_merged, _i, _j = [], 0, 0
while _i < len(_duo) or _j < len(_trio):
    if _j >= len(_trio) or (_i < len(_duo)
                            and (_i + 1) / max(len(_duo), 1) <= (_j + 1) / max(len(_trio), 1)):
        _merged.append(_duo[_i]); _i += 1
    else:
        _merged.append(_trio[_j]); _j += 1

_final = ([('U', _OUVERTURE, CAP_PERSP)] + _merged
          + [('L', 'David_Lesage_2025_Carre', 'David Lesage'),
             ('L', 'iris_soa', 'Iris Chasles'),
             ('U', _JULIEN_PORTRAIT, 'Julien Dub')])

slides = ''
for i, (kind, ref, cap) in enumerate(_final):
    if kind == 'L':
        urlbase, vs = promo(ref, 1500, slug(cap))
    else:
        urlbase, vs = drive(ref, PERSP_NAME[ref])
    big = '%s-%d' % (urlbase, vs[-1][0])
    ar = round(vs[-1][0] / vs[-1][1], 4)
    slides += ('      <div class="slide" style="--ar:%s">' % ar
               + picture(urlbase, vs, SIZES_SLIDE, cap, lazy=i >= 3,
                         img_extra=' onclick="openIMG(this)" data-full="%s.webp"'
                                   ' data-full-jpg="%s.jpg"' % (big, big))
               + '<span class="cap2">' + cap + '</span></div>\n')
print('carrousel :', len(_final), 'photos =', 1, 'ouverture +', len(_merged),
      'entrelacees + 3 portraits')

gal = ('<section class="gallery-sec"><div class="wrap">\n  <div class="kick">Galerie</div>\n'
       '  <h2 class="sec-title">En scène</h2>\n'
       '  <div class="carousel">\n'
       '    <button class="car-play" id="carplay" onclick="carStart()" aria-label="Reprendre le défilement">▶ Reprendre</button>\n'
       '    <button class="car-btn prev" onclick="carNav(-1)" aria-label="Précédent">‹</button>\n'
       '    <div class="car-track" id="cartrack">\n' + slides + '    </div>\n'
       '    <button class="car-btn next" onclick="carNav(1)" aria-label="Suivant">›</button>\n'
       '  </div>\n</div></section>\n<footer><div class="wrap">')
html = html.replace('<footer><div class="wrap">', gal, 1)

# ------------------------------------------- visionneuse : la plus grande variante
OLD_JS = ("function openIMG(img){document.getElementById('imgbig').src=img.src;"
          "document.getElementById('imglb').classList.add('open');}")
NEW_JS = ("var WEBP_OK=(function(){try{return document.createElement('canvas')"
          ".toDataURL('image/webp').indexOf('data:image/webp')===0}catch(e){return false}})();"
          "function openIMG(img){var b=document.getElementById('imgbig');"
          "b.src=(WEBP_OK?img.getAttribute('data-full'):img.getAttribute('data-full-jpg'))"
          "||img.currentSrc||img.src;b.alt=img.alt||'';"
          "document.getElementById('imglb').classList.add('open');}")
assert OLD_JS in html, 'openIMG introuvable'
html = html.replace(OLD_JS, NEW_JS, 1)
html = html.replace('<img id="imgbig" src="" alt="">', '<img id="imgbig" alt="">', 1)
html = html.replace("document.getElementById('imglb').classList.remove('open');"
                    "document.getElementById('imgbig').src='';",
                    "document.getElementById('imglb').classList.remove('open');"
                    "document.getElementById('imgbig').removeAttribute('src');")

# ------------------------------------------- prechargement du fond du hero (LCP)
html = html.replace('<style>',
                    '<link rel="preload" as="image" type="image/webp"'
                    ' href="%s-%d.webp" fetchpriority="high">\n<style>'
                    % (u_hero, v_hero[-1][0]), 1)

# menu mobile (hamburger)
sys.path.insert(0, HERE)
import mobile_nav
html = mobile_nav.inject(html)

# menu de navigation partage
import nav_menu
import verif_commentaires  # garde-fou commentaires HTML
html = nav_menu.inject(html, 'rituals-trio')

assert 'data:image' not in html.replace("data:image/webp'", ''), 'il reste du base64'
assert 'googleusercontent' not in html, 'il reste une URL Drive'

# Garde-fou AVANT l'ecriture : aucune note de redaction en commentaire HTML
# dans la page livree (elle serait publique et indexable).
verif_commentaires.verifier(html, TARGET)

os.makedirs(os.path.dirname(TARGET), exist_ok=True)
with open(TARGET, 'w', encoding='utf-8') as f:
    f.write(html)
print('ECRIT', TARGET, round(len(html.encode()) / 1024), 'ko  | burger:',
      'class="burger"' in html or '.burger{' in html)
