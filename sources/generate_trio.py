# -*- coding: utf-8 -*-
import base64, io, glob
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

def enc(im, q):
    b=io.BytesIO(); im.convert('RGB').save(b,'JPEG',quality=q,optimize=True)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()

def find(tok):
    return sorted(glob.glob('promo_raw/*'+tok+'*'))[0]

def promo(tok, mw, q=80, crop=None):
    im=Image.open(find(tok)).convert('RGB')
    if crop:
        w,h=im.size
        im=im.crop((int(crop[0]*w),int(crop[1]*h),int(crop[2]*w),int(crop[3]*h)))
    im.thumbnail((mw,mw)); return enc(im,q)

def web(fn, mw, q=80, crop=None):
    im=Image.open('web_img/'+fn).convert('RGB')
    if crop:
        w,h=im.size
        im=im.crop((int(crop[0]*w),int(crop[1]*h),int(crop[2]*w),int(crop[3]*h)))
    im.thumbnail((mw,mw)); return enc(im,q)

# HERO — Grand Rex
header = web('RITUALS_00_header.jpg', 1600, 82)
# figures between blocks
fig_intention = promo('20248.',            1300, 82)   # public / participation
fig_exp       = web('RITUALS_00_header.jpg', 1500, 84)  # Grand Rex (image nette, sans surimpression)
fig_journey   = promo('iris_priere',       1300, 82)   # Iris en prière / induction
key_bg        = promo('20245.',            1400, 80)   # duo théâtre (keystone)
# artists
david = promo('David_Lesage_2025_Carre_HD', 900, 86)                          # nouveau portrait
iris  = web('RITUALS_06_Iris-Chasles.jpg', 700, 84, crop=(0.20,0.0,0.82,0.78))  # zoom atténué

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
 ('19-42-24','Touchée par la grâce'),
 ('David_Lesage_2025_Carre','David Lesage'),
 ('RITUALS_07_duo','David & Iris'),
 ('everness_faceaface','Iris & David, face à face'),
 ('david_iris_la_beaute','L’amour au service du collectif'),
 ('iris_soa','Iris Chasles'),
]


# ===== PHOTOS PERSPECTIVE (Drive, partage par lien) =====
def gd(fid, w=1600):
    return 'https://lh3.googleusercontent.com/d/'+fid+'=w'+str(w)

PERSP = [
 ('15_WWObM1AP2FFVWwKGpd_eAkFJzcFQP1', 'Le trio en scène — festival Perspectives'),
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
HERO_TRIO = gd('15_WWObM1AP2FFVWwKGpd_eAkFJzcFQP1', 2000)

with open('site_public/trio.html','r',encoding='utf-8') as f:
    html=f.read()

CSS_ADD="""
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
</style>"""
html=html.replace('</style>',CSS_ADD,1)

def figblock(src,cap):
    return '<section class="figsec"><div class="wrap"><div class="figure"><img src="'+src+'" alt=""></div><div class="cap">'+cap+'</div></div></section>\n'

# hero bg
html=html.replace('<header class="hero">',
  '<header class="hero" style="background:linear-gradient(rgba(10,11,28,.52),rgba(10,11,28,.78)),url('+header+') center/cover">',1)

# intention figure
sig='  <div class="sig">On en repart plus léger. Comme au sortir d’une longue inspiration.</div>'
html=html.replace(sig, sig+'\n  <div class="figure"><img src="'+fig_intention+'" alt=""></div>\n  <div class="cap">Le public au cœur du rituel</div>',1)

# figure after "L'expérience"
anchor_voyage='<section class="journey"><div class="wrap">\n  <div class="kick">Le voyage</div>'
html=html.replace(anchor_voyage, figblock(gd('15_WWObM1AP2FFVWwKGpd_eAkFJzcFQP1',1600),'Le trio en scène — festival Perspectives')+anchor_voyage,1)

# 3. le Grand Rex passe au-dessus de "Pour les organisateurs"
anchor_orga='<section class="orga"><div class="wrap">\n  <div class="kick">Pour les organisateurs</div>'
assert anchor_orga in html, 'ancre orga introuvable'
html=html.replace(anchor_orga, figblock(fig_exp,'Au Grand Rex devant 2700 personnes')+anchor_orga,1)

# keystone bg (la photo d'induction est placee APRES la cle de voute)
html=html.replace('<section class="keystone"><div class="wrap">',
  '<section class="keystone" style="background:linear-gradient(rgba(11,12,30,.74),rgba(11,12,30,.88)),url('+key_bg+') center 35%/cover"><div class="wrap">',1)
html=html.replace('<!--INDUCTION_FIG-->',
  figblock(fig_journey,'L’induction — la voix qui guide, vers un état de conscience élargie'),1)

# artist photos
html=html.replace('<div class="artist">\n    <h3>David Lesage</h3>',
  '<div class="artist">\n    <img class="aphoto" src="'+david+'" alt="David Lesage">\n    <h3>David Lesage</h3>',1)
html=html.replace('<div class="artist">\n    <h3>Iris Chasles</h3>',
  '<div class="artist">\n    <img class="aphoto" src="'+iris+'" alt="Iris Chasles">\n    <h3>Iris Chasles</h3>',1)

# gallery carousel (original format, no black bands)
# les 3 portraits fermeront le carrousel
_PORTRAITS = ('David_Lesage_2025_Carre', 'iris_soa')
_JULIEN_PORTRAIT = '1JZ1VReu_akPLqEgefqjf7v7zJpk8xrGj'
_OUVERTURE = '15_WWObM1AP2FFVWwKGpd_eAkFJzcFQP1'   # perspectives 1 : ouvre le carrousel

# entrelacement proportionnel : tantot David & Iris, tantot le trio avec Julien
_duo  = [('L', t, c) for t, c in GAL if t not in _PORTRAITS]
_trio = [('U', gd(f, 1500), c) for f, c in PERSP
         if f != _JULIEN_PORTRAIT and f != _OUVERTURE]
_merged, _i, _j = [], 0, 0
while _i < len(_duo) or _j < len(_trio):
    # on avance dans les deux listes au meme rythme relatif
    if _j >= len(_trio) or (_i < len(_duo) and (_i+1)/max(len(_duo),1) <= (_j+1)/max(len(_trio),1)):
        _merged.append(_duo[_i]); _i += 1
    else:
        _merged.append(_trio[_j]); _j += 1

# ouverture + entrelacement + les 3 portraits en cloture
_final = ([('U', gd(_OUVERTURE, 1500), 'Le trio en scène — festival Perspectives')]
          + _merged
          + [('L', 'David_Lesage_2025_Carre', 'David Lesage'),
             ('L', 'iris_soa', 'Iris Chasles'),
             ('U', gd(_JULIEN_PORTRAIT, 1500), 'Julien Dub')])

slides=''
for kind, ref, cap in _final:
    src = promo(ref,1500,80) if kind=='L' else ref
    slides+='      <div class="slide"><img onclick="openIMG(this)" src="'+src+'" alt=""><span class="cap2">'+cap+'</span></div>\n'
print('carrousel:', len(_final), 'photos =', 1, 'ouverture +', len(_merged), 'entrelacees + 3 portraits')
gal=('<section class="gallery-sec"><div class="wrap">\n  <div class="kick">Galerie</div>\n'
     '  <h2 class="sec-title">En scène</h2>\n'
     '  <div class="carousel">\n'
     '    <button class="car-play" id="carplay" onclick="carStart()" aria-label="Reprendre le défilement">▶ Reprendre</button>\n'
     '    <button class="car-btn prev" onclick="carNav(-1)" aria-label="Précédent">‹</button>\n'
     '    <div class="car-track" id="cartrack">\n'+slides+'    </div>\n'
     '    <button class="car-btn next" onclick="carNav(1)" aria-label="Suivant">›</button>\n'
     '  </div>\n</div></section>\n<footer><div class="wrap">')
html=html.replace('<footer><div class="wrap">',gal,1)

with open('RITUALS_trio.html','w',encoding='utf-8') as f:
    f.write(html)
print('WROTE RITUALS_trio.html', round(len(html)/1024),'KB')

# ---- variante TRIO : photo de Julien + menu mobile ----
import base64, io as _io
from PIL import Image as _Image
_j=_Image.open('trio_img/julien_sax.jpg').convert('RGB')
_j.thumbnail((1200,1200))
_b=_io.BytesIO(); _j.save(_b,'JPEG',quality=85,optimize=True)
_ju='data:image/jpeg;base64,'+base64.b64encode(_b.getvalue()).decode()

html=open('RITUALS_trio.html',encoding='utf-8').read()
html=html.replace('__JULIEN__',_ju)
import mobile_nav
html=mobile_nav.inject(html)
open('RITUALS_trio.html','w',encoding='utf-8').write(html)
print('TRIO ok — placeholders restants:',html.count('__JULIEN__'),'| burger:', 'class="burger"' in html or '.burger{' in html)
