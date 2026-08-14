# -*- coding: utf-8 -*-
"""Genere la page /rituals/index.html a partir de sources/rituals_source.html.

Les photos ne sont PLUS encodees en base64 dans la page (la page pesait 4,6 Mo).
Elles sont ecrites en fichiers dans /img/rituals/ en trois largeurs
(480 / 900 / 1400 px), en WebP + repli JPEG, et referencees par <picture>
avec srcset / sizes / width / height / loading / decoding.

Dossiers d'entree attendus a cote de ce script (photos d'origine, hors depot) :
  promo_raw/   web_img/
Sortie : ../img/rituals/*.webp|jpg  et  ../rituals/index.html
"""
import glob, io, os, re, sys, unicodedata, html as _html
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
IMG_DIR = os.path.join(REPO, 'img', 'rituals')
IMG_URL = '/img/rituals'
SOURCE = os.path.join(HERE, 'rituals_source.html')
TARGET = os.path.join(REPO, 'rituals', 'index.html')

WIDTHS = (480, 900, 1400)
Q_WEBP = 80
Q_JPEG = 82

# largeur d'affichage reelle, pour que le navigateur choisisse la bonne variante
SIZES_FIG = '(max-width:1040px) calc(100vw - 52px), 988px'
SIZES_SLIDE = '(max-width:900px) 86vw, 700px'
SIZES_APHOTO = '(max-width:600px) 62vw, 210px'

SLUGS = {
    'Au Grand Rex devant 2700 personnes': 'au-grand-rex',
    'L’induction — la voix qui guide, vers un état de conscience élargie': 'l-induction',
}


def slug(txt):
    """Nom de fichier lisible : minuscules, sans accent, sans espace."""
    t = _html.unescape(txt).replace('’', "'").replace('&', ' et ')
    for a, b in (('œ', 'oe'), ('Œ', 'oe'), ('æ', 'ae'), ('Æ', 'ae')):
        t = t.replace(a, b)
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c)).lower()
    t = re.sub(r'[^a-z0-9]+', '-', t).strip('-')
    if len(t) > 52:
        t = t[:52].rsplit('-', 1)[0]
    return SLUGS.get(txt, t)


def variants(im, name):
    """Ecrit name-<w>.webp et name-<w>.jpg. Retourne [(largeur, hauteur), ...]."""
    os.makedirs(IMG_DIR, exist_ok=True)
    im = im.convert('RGB')
    ow, oh = im.size
    out = []
    for w in WIDTHS:
        if w > ow and out:
            break                                  # jamais de suragrandissement
        ww = min(w, ow)
        hh = max(1, round(oh * ww / ow))
        r = im if (ww, hh) == (ow, oh) else im.resize((ww, hh), Image.LANCZOS)
        r.save(os.path.join(IMG_DIR, '%s-%d.webp' % (name, ww)), 'WEBP',
               quality=Q_WEBP, method=6)
        r.save(os.path.join(IMG_DIR, '%s-%d.jpg' % (name, ww)), 'JPEG',
               quality=Q_JPEG, optimize=True, progressive=True)
        out.append((ww, hh))
    return out


def picture(name, vs, sizes, alt, cls='', extra='', img_extra='', lazy=True):
    """Bloc <picture> : WebP d'abord, JPEG en repli pour les vieux navigateurs."""
    base = IMG_URL + '/' + name
    webp = ', '.join('%s-%d.webp %dw' % (base, w, w) for w, h in vs)
    jpeg = ', '.join('%s-%d.jpg %dw' % (base, w, w) for w, h in vs)
    dw, dh = min(vs, key=lambda v: abs(v[0] - 900))   # repli sans srcset
    c = ' class="%s"' % cls if cls else ''
    return ('<picture%s%s><source type="image/webp" srcset="%s" sizes="%s">'
            '<img%s src="%s-%d.jpg" srcset="%s" sizes="%s" width="%d" height="%d"'
            ' alt="%s" loading="%s" decoding="async"></picture>'
            % (c, extra, webp, sizes, img_extra, base, dw, jpeg, sizes,
               vs[-1][0], vs[-1][1], alt, 'lazy' if lazy else 'eager'))


# ---------------------------------------------------------------- photos source
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
    return variants(_open(find(tok), mw, crop), name)


def web(fn, mw, name, crop=None):
    p = os.path.join(HERE, 'web_img', fn)
    if not os.path.exists(p):
        sys.exit('photo introuvable dans web_img/ : ' + fn)
    return variants(_open(p, mw, crop), name)


CAP_INTENTION = 'Le public au cœur du rituel'
CAP_REX = 'Au Grand Rex devant 2700 personnes'
CAP_INDUCTION = 'L’induction — la voix qui guide, vers un état de conscience élargie'

print('images :')
v_hero = web('RITUALS_00_header.jpg', 1600, 'hero-grand-rex')
v_intention = promo('20248.', 1300, slug(CAP_INTENTION))
v_rex = web('RITUALS_00_header.jpg', 1500, slug(CAP_REX))
v_induction = promo('iris_priere', 1300, slug(CAP_INDUCTION))
v_keystone = promo('20245.', 1400, 'cle-de-voute-duo-theatre')
v_david = promo('David_Lesage_2025_Carre_HD', 900, 'portrait-david-lesage')
v_iris = web('RITUALS_06_Iris-Chasles.jpg', 700, 'portrait-iris-chasles',
             crop=(0.20, 0.0, 0.82, 0.78))

GAL = [
 ('202417.', 'Le corps en mouvement'),
 ('202418.', 'Une connexion forte avec le public'),
 ('202419.', 'Danser la vie'),
 ('202420.', 'Everness Festival, Hongrie'),
 ('202422.', 'S’ouvrir, s’offrir'),
 ('202423.', 'L’élan'),
 ('202424.', 'Deux êtres, une intention'),
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

with open(SOURCE, 'r', encoding='utf-8') as f:
    html = f.read()

# ------------------------------------------------------------------------- CSS
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


def bg_rules(sel, name, vs, grad, pos):
    """Fond photo en CSS : url() simple pour tous, image-set (WebP) si supporte."""
    def rule(w):
        b = '%s/%s' % (IMG_URL, name)
        return ('.%s{background:%s,url(%s-%d.jpg) %s}\n'
                '.%s{background:%s,image-set(url(%s-%d.webp) type("image/webp"),'
                'url(%s-%d.jpg) type("image/jpeg")) %s}\n'
                % (sel, grad, b, w, pos, sel, grad, b, w, b, w, pos))
    wide = vs[-1][0]
    small = min((v[0] for v in vs if v[0] >= 900), default=wide)
    css = rule(wide)
    if small != wide:
        css += '@media(max-width:900px){\n' + rule(small) + '}\n'
    return css


GRAD_HERO = 'linear-gradient(rgba(10,11,28,.52),rgba(10,11,28,.78))'
GRAD_KEY = 'linear-gradient(rgba(11,12,30,.74),rgba(11,12,30,.88))'
CSS_ADD = CSS_ADD.replace('__BG__',
                          bg_rules('hero', 'hero-grand-rex', v_hero,
                                   GRAD_HERO, 'center/cover')
                          + bg_rules('keystone', 'cle-de-voute-duo-theatre',
                                     v_keystone, GRAD_KEY, 'center 35%/cover'))
html = html.replace('</style>', CSS_ADD, 1)


def figblock(name, vs, cap, lazy=True):
    return ('<section class="figsec"><div class="wrap"><div class="figure">'
            + picture(name, vs, SIZES_FIG, cap, lazy=lazy)
            + '</div><div class="cap">' + cap + '</div></div></section>\n')


# le fond du hero est desormais pose par la feuille de style (pas de style inline)

# figure de l'intention (premiere image de la page : chargement immediat)
sig = '  <div class="sig">On en repart plus léger. Comme au sortir d’une longue inspiration.</div>'
assert sig in html, 'ancre sig introuvable'
html = html.replace(sig, sig + '\n  <div class="figure">'
                    + picture(slug(CAP_INTENTION), v_intention, SIZES_FIG,
                              CAP_INTENTION, lazy=False)
                    + '</div>\n  <div class="cap">' + CAP_INTENTION + '</div>', 1)

# figure du Grand Rex, avant « Le voyage »
anchor_voyage = '<section class="journey"><div class="wrap">\n  <div class="kick">Le voyage</div>'
assert anchor_voyage in html, 'ancre voyage introuvable'
html = html.replace(anchor_voyage,
                    figblock(slug(CAP_REX), v_rex, CAP_REX) + anchor_voyage, 1)

# figure de l'induction, avant la cle de voute
assert '<section class="keystone"><div class="wrap">' in html
html = html.replace('<section class="keystone"><div class="wrap">',
                    figblock(slug(CAP_INDUCTION), v_induction, CAP_INDUCTION)
                    + '<section class="keystone"><div class="wrap">', 1)

# ------------------------------------------------------------------------- #
# GRAND REX, SECONDE PHOTO (ajout du 14/08/2026, fournie par David).
#
# ⚠️ CE BLOC N'EST PAS PRODUIT PAR CE SCRIPT : il a ete ajoute A LA MAIN dans
# `rituals/index.html`, juste APRES la section `.keystone` inseree ci-dessus
# (`<section class="figsec">` avec `grand-rex-bras-leves-*`). Ce generateur ne
# tourne plus ici (les dossiers `promo_raw/` et `web_img/` sont hors depot), il
# ne peut donc pas le recreer : une regeneration ferait DISPARAITRE cette photo.
# La note est conservee ici, a l'endroit du code ou le bloc s'insere, parce que
# c'est le seul code qui produit cette page.
#
# Placee ICI, juste apres la cle de voute, parce qu'elle montre exactement ce
# que la citation decrit : la salle entiere prise dans le meme geste.
# ⚠️ Elle ne remplace PAS `au-grand-rex` (plus haut) : les deux angles sont
# opposes — celui-la est pris DEPUIS LA SALLE et montre le plateau, l'ecran
# geant et les bras leves, la ou `au-grand-rex` et le fond du hero sont pris
# DEPUIS LA SCENE. Trois sections les separent : aucune repetition.
# ⚠️ CREDIT PHOTO : signee « Nadine Court PHOTOGRAPHE » en bas a droite, pas
# MAGYE D'ART comme les deux autres. Site fourni par David et verifie
# (kairos-photo-artisan.com, « Kairos Photographie »). A CONFIRMER : le titre
# du site affiche « Nadine Tremblay » ; on credite « Nadine Court », le nom
# signe sur la photo.
# ⚠️ David a decrit « David a droite avec un tambour » : c'est INEXACT. Le
# joueur de tambour sur cadre, a droite, est ARNAUD RIOU — identifie par David
# lui-meme le 13/08/2026, avec son accord explicite pour etre cite (« il est
# tres connu dans un certain milieu »). Auteur et conferencier, deja present
# dans les sources du projet : conference-film-concert avec David le
# 30/09/2023 au Theatre de l'Etang. David, lui, est le musicien ASSIS A
# GAUCHE, derriere ses calebasses.
# ------------------------------------------------------------------------- #

# photos des artistes
html = html.replace('<div class="artist">\n    <h3>David Lesage</h3>',
                    '<div class="artist">\n    '
                    + picture('portrait-david-lesage', v_david, SIZES_APHOTO,
                              'David Lesage', cls='aphoto')
                    + '\n    <h3>David Lesage</h3>', 1)
html = html.replace('<div class="artist">\n    <h3>Iris Chasles</h3>',
                    '<div class="artist">\n    '
                    + picture('portrait-iris-chasles', v_iris, SIZES_APHOTO,
                              'Iris Chasles', cls='aphoto')
                    + '\n    <h3>Iris Chasles</h3>', 1)

# ------------------------------------------------------------------ carrousel
slides = ''
for i, (tok, cap) in enumerate(GAL):
    name = slug(cap)
    vs = promo(tok, 1500, name)
    big = '%s/%s-%d' % (IMG_URL, name, vs[-1][0])
    ar = round(vs[-1][0] / vs[-1][1], 4)
    slides += ('      <div class="slide" style="--ar:%s">' % ar
               + picture(name, vs, SIZES_SLIDE, cap, lazy=i >= 3,
                         img_extra=' onclick="openIMG(this)" data-full="%s.webp"'
                                   ' data-full-jpg="%s.jpg"' % (big, big))
               + '<span class="cap2">' + cap + '</span></div>\n')

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
                    ' href="%s/hero-grand-rex-%d.webp" fetchpriority="high">\n<style>'
                    % (IMG_URL, v_hero[-1][0]), 1)

# menu mobile (hamburger) : absent de la source, injecte ici
sys.path.insert(0, HERE)
import mobile_nav
html = mobile_nav.inject(html)

# menu de navigation partage (Accueil / Sur scene / Le Nid / L'association / Contact)
import nav_menu
html = nav_menu.inject(html, 'rituals')

assert 'data:image' not in html.replace("data:image/webp'", ''), 'il reste du base64'

# Garde-fou AVANT l'ecriture : aucune note de redaction en commentaire HTML
# dans la page livree (elle serait publique et indexable).
import verif_commentaires
verif_commentaires.verifier(html, TARGET)

os.makedirs(os.path.dirname(TARGET), exist_ok=True)
with open(TARGET, 'w', encoding='utf-8') as f:
    f.write(html)
print('ECRIT', TARGET, round(len(html.encode()) / 1024), 'ko  +',
      len(os.listdir(IMG_DIR)), 'fichiers dans', IMG_DIR)
