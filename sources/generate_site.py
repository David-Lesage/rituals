# -*- coding: utf-8 -*-
"""Genere la page /rituals/index.html a partir de sources/rituals_source.html.

    python3 sources/generate_site.py            # regenere la page (par defaut)
    python3 sources/generate_site.py --images   # refabrique les derivees, puis la page

DEUX TRAVAUX BIEN SEPARES
-------------------------
1. GENERER LA PAGE (ce que fait ce script par defaut). Il ne lit QUE des
   fichiers presents dans le depot : `sources/rituals_source.html` et les
   derivees deja optimisees de `img/rituals/`. Aucune photo d'origine, aucune
   bibliotheque d'images : les dimensions des <picture> sont relues dans les
   fichiers JPEG eux-memes (voir `_dim_jpeg`). Le script tourne donc partout,
   sur un simple `git clone`.

2. FABRIQUER LES DERIVEES a partir des photos d'origine (section
   « FABRICATION »). Les dossiers d'entree `promo_raw/` et
   `web_img/` sont HORS DEPOT : cette etape n'est faisable que sur la machine
   qui detient les originaux, elle est donc OPTIONNELLE et ne se declenche
   qu'avec `--images`. Son impossibilite n'empeche plus de regenerer la page.
   Elle a aussi besoin de Pillow, importe seulement a ce moment-la.

Les photos ne sont PLUS encodees en base64 dans la page (la page pesait 4,6 Mo).
Elles vivent en fichiers dans /img/rituals/ en trois largeurs
(480 / 900 / 1400 px), en WebP + repli JPEG, et sont referencees par <picture>
avec srcset / sizes / width / height / loading / decoding.

Sortie : ../rituals/index.html  (et, avec --images, ../img/rituals/*.webp|jpg)
"""
import glob, os, re, sys, unicodedata, html as _html

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import theme_chaleur  # couche chaleureuse commune  # noqa: E402
import visionneuse    # visionneuse photo commune     # noqa: E402

IMG_DIR = os.path.join(REPO, 'img', 'rituals')
IMG_URL = '/img/rituals'
SOURCE = os.path.join(HERE, 'rituals_source.html')
TARGET = os.path.join(REPO, 'rituals', 'index.html')

WIDTHS = (480, 900, 1400)
Q_WEBP = 80
Q_JPEG = 82

#: photos dont le jeu de derivees n'est PAS celui de WIDTHS. Une seule a ce
#: jour : `grand-rex-bras-leves` a ete preparee A LA MAIN, hors de ce script,
#: en quatre largeurs dont une de 2000 px que la fabrication automatique ne
#: produit pas (elle plafonne a 1400). Voir le bloc « bras leves » plus bas.
#: Toute autre photo doit avoir exactement WIDTHS : c'est ce que verifie
#: `derivees()`.
LARGEURS_PARTICULIERES = {
    'grand-rex-bras-leves': (480, 900, 1400, 2000),
}

# largeur d'affichage reelle, pour que le navigateur choisisse la bonne variante
SIZES_FIG = '(max-width:1040px) calc(100vw - 52px), 988px'
SIZES_SLIDE = '(max-width:900px) 86vw, 700px'
SIZES_APHOTO = '(max-width:600px) 62vw, 210px'

SLUGS = {
    # ⚠️ Nom de fichier volontairement long (17/08/2026) : il dit QUI est sur la
    # photo et OU elle a ete prise. Un nom de fichier est lu par Google Images et
    # par les lecteurs d'ecran quand l'image ne charge pas ; `au-grand-rex` ne
    # disait ni le nom des artistes ni la ville. Ne pas le « raccourcir » : c'est
    # exactement ce qu'on est venu chercher. Le TEXTE affiche (la legende
    # `CAP_REX`), lui, n'a pas change.
    'Au Grand Rex devant 2700 personnes':
        'iris-chasles-et-david-lesage-au-grand-rex-paris',
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


def _dim_jpeg(chemin):
    """(largeur, hauteur) d'un JPEG, lues dans son marqueur SOF.

    Volontairement sans Pillow : generer la page ne doit dependre de rien
    d'autre que de la bibliotheque standard.
    """
    with open(chemin, 'rb') as f:
        d = f.read()
    i = 2                                          # on saute le SOI (FFD8)
    while i < len(d) - 9:
        if d[i] != 0xFF:
            i += 1
            continue
        m = d[i + 1]
        if m == 0xFF:                               # octets de bourrage
            i += 1
            continue
        if m in (0x01, 0xD8, 0xD9) or 0xD0 <= m <= 0xD7:
            i += 2                                  # marqueurs sans charge utile
            continue
        taille = int.from_bytes(d[i + 2:i + 4], 'big')
        # SOF0..SOF15, sauf DHT (C4), JPG (C8) et DAC (CC)
        if 0xC0 <= m <= 0xCF and m not in (0xC4, 0xC8, 0xCC):
            return (int.from_bytes(d[i + 7:i + 9], 'big'),
                    int.from_bytes(d[i + 5:i + 7], 'big'))
        i += 2 + taille
    raise ValueError('dimensions introuvables : ' + chemin)


def derivees(name):
    """[(largeur, hauteur), ...] des derivees deja presentes dans img/rituals/.

    Remplace l'ancien appel a la fabrication d'images : la page se regenere a
    partir de ce qui est DANS le depot. L'ordre (largeurs croissantes) est celui
    que produisait la fabrication, et dont dependent `picture()` (attributs
    width/height = plus grande variante) et le srcset.
    """
    trouves = []
    for p in glob.glob(os.path.join(IMG_DIR, name + '-*.jpg')):
        m = re.fullmatch(re.escape(name) + r'-(\d+)\.jpg',
                         os.path.basename(p))
        if m:
            trouves.append((int(m.group(1)), p))
    if not trouves:
        sys.exit('derivee absente de %s : %s-<largeur>.jpg — la fabriquer avec '
                 '`--images` (photos d\'origine requises).' % (IMG_DIR, name))
    trouves.sort()
    ws = [w for w, _p in trouves]
    largeurs = LARGEURS_PARTICULIERES.get(name, WIDTHS)

    # ⚠️ Un JEU INCOMPLET est plus dangereux qu'un jeu absent : sans ce controle,
    # un fichier efface par megarde ne fait pas echouer le script — il produit
    # simplement un srcset ampute, donc une page differente de la publiee, en
    # silence. (Mesure du 14/08/2026 : retirer une seule derivee de 900 px
    # laissait le script ecrire une page degradee, code de sortie 0.) Meme
    # remede que `generate_trio.py`, qui portait exactement la meme faille.
    # Les largeurs doivent etre WIDTHS dans l'ordre, la derniere pouvant etre
    # plus petite que prevu quand l'original ne permettait pas d'aller plus haut
    # (la fabrication ne suragrandit jamais).
    attendu = list(largeurs[:len(ws)])
    contigu = (len(ws) <= len(largeurs)
               and (ws == attendu
                    or (ws[:-1] == attendu[:-1] and ws[-1] < attendu[-1])))
    if not contigu:
        sys.exit('largeurs incoherentes pour %s dans %s : %s (attendu un debut de '
                 '%s). Un fichier a du etre efface ; refabriquer avec `--images`.'
                 % (name, IMG_DIR, ws, list(largeurs)))
    for w, _p in trouves:                              # chaque JPEG a son WebP
        jumeau = os.path.join(IMG_DIR, '%s-%d.webp' % (name, w))
        if not os.path.exists(jumeau):
            sys.exit('WebP manquant : %s (le srcset le referencerait quand meme).'
                     % jumeau)
    return [(w, _dim_jpeg(p)[1]) for w, p in trouves]


def picture(name, vs, sizes, alt, cls='', extra='', img_extra='', lazy=True,
            repli=None):
    """Bloc <picture> : WebP d'abord, JPEG en repli pour les vieux navigateurs.

    `repli` force la largeur du `src` de secours (celui que servent les
    navigateurs sans srcset). Par defaut on prend la variante la plus proche de
    900 px ; une seule photo y deroge, voir le bloc « bras leves ».
    """
    base = IMG_URL + '/' + name
    webp = ', '.join('%s-%d.webp %dw' % (base, w, w) for w, h in vs)
    jpeg = ', '.join('%s-%d.jpg %dw' % (base, w, w) for w, h in vs)
    dw = repli or min(vs, key=lambda v: abs(v[0] - 900))[0]   # repli sans srcset
    c = ' class="%s"' % cls if cls else ''
    return ('<picture%s%s><source type="image/webp" srcset="%s" sizes="%s">'
            '<img%s src="%s-%d.jpg" srcset="%s" sizes="%s" width="%d" height="%d"'
            ' alt="%s" loading="%s" decoding="async"></picture>'
            % (c, extra, webp, sizes, img_extra, base, dw, jpeg, sizes,
               vs[-1][0], vs[-1][1], alt, 'lazy' if lazy else 'eager'))


# ---------------------------------------------------------------- photos source
CAP_INTENTION = 'Le public au cœur du rituel'
CAP_REX = 'Au Grand Rex devant 2700 personnes'
CAP_INDUCTION = 'L’induction — la voix qui guide, vers un état de conscience élargie'

# RECETTES — d'ou vient chaque derivee de img/rituals/, et comment elle a ete
# fabriquee : (dossier d'origine, jeton ou nom de fichier, largeur max, rognage).
# Les dossiers `promo_raw/` et `web_img/` sont HORS DEPOT : cette table ne sert
# QU'A la fabrication (`--images`, tout en bas). La generation de la page, elle,
# ne lit que les fichiers deja presents dans img/rituals/. On la garde ici parce
# que sans elle plus personne ne saurait refaire une derivee a l'identique.
# ⚠️ `grand-rex-bras-leves` n'y figure pas : cette photo a ete fournie et
# preparee a la main (4 largeurs, jusqu'a 2000 px) ; son original n'a jamais
# transite par ce script. La fabrication n'efface rien, elle ne la menace pas.
# ⚠️ FUSION DU 17/08/2026 — `hero-grand-rex` a disparu de cette table et du depot.
#    Sa recette etait ('web', 'RITUALS_00_header.jpg', 1600, None) : le MEME
#    original que `slug(CAP_REX)` ci-dessous, a 100 px de plafond pres. Les deux
#    jeux de derivees etaient donc la meme photo aux memes dimensions (mesure :
#    480/900/1400 identiques, ecart moyen 1,3 a 2,0 sur 255 — du bruit de
#    recompression). Le fond du hero et la figure du Grand Rex partagent
#    desormais un seul jeu de fichiers. Ne pas re-creer `hero-grand-rex`.
RECETTES = {
    slug(CAP_INTENTION):        ('promo', '20248.', 1300, None),
    slug(CAP_REX):              ('web',   'RITUALS_00_header.jpg', 1500, None),
    slug(CAP_INDUCTION):        ('promo', 'iris_priere', 1300, None),
    'cle-de-voute-duo-theatre': ('promo', '20245.', 1400, None),
    'portrait-david-lesage':    ('promo', 'David_Lesage_2025_Carre_HD', 900, None),
    'portrait-iris-chasles':    ('web',   'RITUALS_06_Iris-Chasles.jpg', 700,
                                 (0.20, 0.0, 0.82, 0.78)),
}

v_intention = derivees(slug(CAP_INTENTION))
v_rex = derivees(slug(CAP_REX))  # sert AUSSI de fond au hero (fusion du 17/08)
v_induction = derivees(slug(CAP_INDUCTION))
v_keystone = derivees('cle-de-voute-duo-theatre')
v_david = derivees('portrait-david-lesage')
v_iris = derivees('portrait-iris-chasles')

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

# les 20 photos du carrousel viennent toutes de promo_raw/, plafonnees a 1500 px
RECETTES.update({slug(cap): ('promo', tok, 1500, None) for tok, cap in GAL})


# =========================================================================== #
# FABRICATION DES DERIVEES — OPTIONNELLE, et volontairement a part.
#
# Elle transforme les photos d'origine (`sources/promo_raw/`, `sources/web_img/`,
# HORS DEPOT, plusieurs centaines de Mo) en `img/rituals/<nom>-<largeur>.webp|jpg`.
# Rien ici n'est necessaire pour generer la page : c'est justement le piege qu'on
# vient de desamorcer. Sans `--images`, ce bloc n'est jamais execute, Pillow n'est
# meme pas importe, et l'absence des dossiers d'origine ne bloque plus personne.
#
# A relancer uniquement pour ajouter ou remplacer une photo, sur la machine qui
# detient les originaux. La fabrication ECRASE les derivees qu'elle produit et
# n'EFFACE jamais les autres (dont `grand-rex-bras-leves`, preparee a la main).
# =========================================================================== #

def fabriquer(noms=None):
    """(Re)fabrique les derivees decrites par RECETTES. Necessite Pillow."""
    from PIL import Image                          # importe ici, et ici seulement
    Image.MAX_IMAGE_PIXELS = None

    def ouvrir(chemin, mw, crop):
        im = Image.open(chemin).convert('RGB')
        if crop:
            w, h = im.size
            im = im.crop((int(crop[0] * w), int(crop[1] * h),
                          int(crop[2] * w), int(crop[3] * h)))
        im.thumbnail((mw, mw))
        return im

    def origine(dossier, cle):
        if dossier == 'web':                       # nom de fichier exact
            p = os.path.join(HERE, 'web_img', cle)
            if not os.path.exists(p):
                sys.exit('photo introuvable dans web_img/ : ' + cle)
            return p
        hits = sorted(glob.glob(os.path.join(HERE, 'promo_raw', '*' + cle + '*')))
        if not hits:
            sys.exit('photo introuvable dans promo_raw/ : ' + cle)
        return hits[0]

    def variantes(im, name):
        """Ecrit name-<w>.webp et name-<w>.jpg. Retourne [(largeur, hauteur), ...]."""
        os.makedirs(IMG_DIR, exist_ok=True)
        ow, oh = im.size
        out = []
        for w in WIDTHS:
            if w > ow and out:
                break                              # jamais de suragrandissement
            ww = min(w, ow)
            hh = max(1, round(oh * ww / ow))
            r = im if (ww, hh) == (ow, oh) else im.resize((ww, hh), Image.LANCZOS)
            r.save(os.path.join(IMG_DIR, '%s-%d.webp' % (name, ww)), 'WEBP',
                   quality=Q_WEBP, method=6)
            r.save(os.path.join(IMG_DIR, '%s-%d.jpg' % (name, ww)), 'JPEG',
                   quality=Q_JPEG, optimize=True, progressive=True)
            out.append((ww, hh))
        return out

    for name in (noms or sorted(RECETTES)):
        dossier, cle, mw, crop = RECETTES[name]
        vs = variantes(ouvrir(origine(dossier, cle), mw, crop), name)
        print('  %-38s %s' % (name, ' '.join('%dx%d' % v for v in vs)))


if '--images' in sys.argv:
    print('fabrication des derivees :')
    fabriquer()


# =========================================================================== #
# GENERATION DE LA PAGE — ne lit que ce qui est dans le depot
# =========================================================================== #

with open(SOURCE, 'r', encoding='utf-8') as f:
    html = f.read()

# ------------------------------------------------------------------------- CSS
# --------------------------------------------------------------------------
# LA VISIONNEUSE PHOTO (17/08/2026)
# --------------------------------------------------------------------------
# Les 26 photos de la page s'ouvrent en grand au clic. Tout est dans
# `sources/visionneuse.py` — meme visionneuse que sur les six autres pages a
# photos du site. Elle REMPLACE l'ancienne (`openIMG` / `#imglb`), retiree plus
# bas : celle-la n'avait ni defilement d'une photo a l'autre, ni zoom, ni piege
# a focus, ni retour du focus sur la photo de depart, ni verrou de la page.
#
# ⚠️ `.cap2` N'EST PAS UN ARGUMENT COSMETIQUE. La legende de chaque diapo du
#    carrousel est en `position:absolute` PAR-DESSUS le bas de l'image (le
#    degrade noir) : sans la ligne `pointer-events:none` que cet argument
#    produit, tout le bas de chaque photo du carrousel n'est pas cliquable.
#    Mesure faite par `elementFromPoint` sur les 26 photos.
CSS_VISIONNEUSE = visionneuse.css('.cap2')

CSS_ADD = ("""
.nav{position:fixed;top:0;left:0;right:0;z-index:60;display:flex;align-items:center;justify-content:space-between;padding:16px 26px;background:rgba(14,15,36,.82);backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.06)}
.nav .brand{font-family:'Cormorant Garamond',serif;letter-spacing:.14em;text-transform:uppercase;font-size:13.5px;color:#fff;text-decoration:none}
.nav .brand:hover{color:var(--gold2)}
.nav .links{display:flex;align-items:center;gap:20px}
.nav .links a{color:var(--muted);text-decoration:none;font-size:14px}
.nav .links a:hover{color:var(--gold2)}
@media(max-width:700px){.nav .links a.hide-s{display:none}.nav .brand{font-size:13px}}
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
.cap2{position:absolute;left:0;right:0;bottom:0;background:linear-gradient(transparent,rgba(0,0,0,.78));color:#fff;font-size:13px;padding:24px 14px 10px;text-align:center;font-style:italic}
.car-btn{position:absolute;top:50%;transform:translateY(-50%);z-index:3;background:rgba(18,19,43,.72);color:#fff;border:1px solid var(--line);width:46px;height:46px;border-radius:50%;font-size:22px;cursor:pointer}
.car-btn.prev{left:-4px}.car-btn.next{right:-4px}
.car-play{display:none;position:absolute;top:-52px;right:0;z-index:4;align-items:center;gap:6px;background:var(--gold);color:#1a1608;border:none;padding:8px 16px;border-radius:20px;font-size:13px;font-weight:600;cursor:pointer}
@media(max-width:900px){.slide img{height:auto;width:auto;max-width:86vw;max-height:62vh}}
@media(max-width:600px){.aphoto{float:none;width:62%;display:block;margin:0 auto 16px}.car-btn{display:none}}

"""
          # ===== IMAGES LOCALES RESPONSIVES (WebP + repli JPEG) =====
          # <picture> ne doit rien changer a la mise en page : il se comporte comme un bloc
          # transparent et l'<img> garde exactement les regles CSS d'origine.
          """picture{display:block}
"""
          # Les attributs width/height valent aussi comme indication de style : sans
          # height:auto explicite, la hauteur en attribut s'appliquerait comme une
          # longueur CSS et deformerait l'image (cas des .figure, du teaser, etc.).
          """picture>img{height:auto}
picture.aphoto{overflow:hidden}
picture.aphoto>img{width:100%;height:auto;display:block;border-radius:inherit}

"""
          # Le carrousel : chaque diapo RESERVE sa largeur a partir de son rapport
          # largeur/hauteur (--ar). Sans cela, loading="lazy" ferait s'effondrer les
          # diapos non encore chargees a ~1 px et le defilement serait casse.
          # La geometrie reste celle d'avant : hauteur 460 px en grand ecran, et sur
          # petit ecran l'image tient dans 86vw x 62vh.
          """.slide{width:min(calc(460px * var(--ar,1.5)),90vw)}
.slide picture{width:100%}
.slide img{height:auto;width:100%;max-width:100%;aspect-ratio:var(--ar,1.5)}
@media(max-width:900px){
  .slide{width:min(86vw,calc(62vh * var(--ar,1.5)))}
  .slide img{height:auto;width:100%;max-width:100%;max-height:none}
}
@media print{.slide{width:100%!important}.slide picture{width:100%!important}}
__BG__""") + theme_chaleur.CSS + theme_chaleur.CSS_RITUALS + CSS_VISIONNEUSE + """</style>"""


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
                          bg_rules('hero', slug(CAP_REX), v_rex,
                                   GRAD_HERO, 'center/cover')
                          + bg_rules('keystone', 'cle-de-voute-duo-theatre',
                                     v_keystone, GRAD_KEY, 'center 35%/cover'))

# --------------------------------------------------------------------------- #
# DEUX CORRECTIFS CSS QUI ETAIENT POSES A LA MAIN DANS LA PAGE PUBLIEE.
# Tant qu'ils n'etaient nulle part dans le generateur, toute regeneration les
# perdait. Ils sont donc rapatries ici, avec leur raison d'etre.
# --------------------------------------------------------------------------- #

# 1) Le style du credit photo (`.cred-fig`) n'existe pas dans la source. Sans
#    lui, les mentions « Credit photo … » sous les figures perdent leur mise en
#    forme et leur zone tactile de 44 px. On le pose juste apres la regle de
#    focus clavier, la ou il se trouve dans la page publiee.
ANCRE_FOCUS = (':focus-visible{outline:2px solid var(--gold2);'
               'outline-offset:2px;border-radius:4px}\n')
CSS_CRED = (# credit photo sous une figure (signature du photographe visible sur l'image)
           """.cred-fig{margin-top:8px;text-align:center;font-size:15px;color:var(--muted)}
.cred-fig a{color:var(--gold);text-decoration:underline;text-decoration-color:rgba(216,178,90,.45);text-underline-offset:3px;display:inline-block;padding:11px 0}
.cred-fig a:hover{color:var(--gold2)}
""")
assert ANCRE_FOCUS in html, 'ancre :focus-visible introuvable'
if '.cred-fig{' not in html:                       # garde d'idempotence
    html = html.replace(ANCRE_FOCUS, ANCRE_FOCUS + CSS_CRED, 1)

# 2) Le bloc « lisibilite des liens » vit dans la source, donc AVANT le CSS
#    ajoute ici. Or il doit passer APRES : `.nav .links a{font-size:14.5px}`
#    doit l'emporter sur la regle de la barre de navigation posee plus bas, et
#    les soulignements sur les regles de figure. On le deplace donc en fin de
#    CSS_ADD — c'est exactement sa position dans la page publiee.
# Le libelle a ete RACCOURCI le 16/08/2026 : il est le marqueur cherche par
# `find()` ci-dessous ET une ancre comptee par les garde-fous, donc il part
# dans la page livree. Son texte d'origine — « demande de David : liens et
# dates trop petits » — est la vraie raison d'etre du bloc, et elle est
# ecrite juste au-dessus. Il doit rester identique a celui de la source.
DEB_LISI = '/* --- lisibilite des liens --- */'
FIN_LISI = '  text-decoration-color:rgba(216,178,90,.4);text-underline-offset:3px}\n'
d = html.find(DEB_LISI)
assert d != -1, 'bloc « lisibilite des liens » introuvable dans la source'
f = html.find(FIN_LISI, d) + len(FIN_LISI)
BLOC_LISI = html[d:f]
html = html[:d - 1] + html[f:]                     # -1 : la ligne vide qui precede
CSS_ADD = CSS_ADD.replace('</style>', '\n' + BLOC_LISI + '\n</style>', 1)

html = html.replace('</style>', CSS_ADD, 1)


# CREDITS PHOTO. Certaines photos portent la signature du photographe, visible a
# l'oeil sur l'image : la mention et le lien sont donc obligatoires sous la
# figure. Le `.cred-fig` se place APRES la legende, dans le meme `.wrap` — la
# legende reste collee a sa photo, le credit vient dessous. C'est un correctif
# volontaire : place autrement, le credit chevauchait la legende.
CRED = {
    "MAGYE D'ART": 'https://magyedart.fr/',
    'Nadine Court': 'https://kairos-photo-artisan.com/',
}


def credit(qui):
    """Ligne « Credit photo <lien> » a poser sous la legende d'une figure."""
    return ('<div class="cred-fig">Crédit photo <a href="%s" target="_blank"'
            ' rel="noopener">%s</a></div>' % (CRED[qui], qui))


def figblock(name, vs, cap, lazy=True, alt=None, cred=None, repli=None):
    """Figure pleine largeur : photo + legende (+ credit photo si signee)."""
    return ('<section class="figsec"><div class="wrap"><div class="figure">'
            + picture(name, vs, SIZES_FIG, alt or cap, lazy=lazy, repli=repli)
            + '</div><div class="cap">' + cap + '</div>'
            + (credit(cred) if cred else '') + '</div></section>\n')


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
                    figblock(slug(CAP_REX), v_rex, CAP_REX,
                             cred="MAGYE D'ART") + anchor_voyage, 1)

# figure de l'induction, avant la cle de voute
assert '<section class="keystone"><div class="wrap">' in html
html = html.replace('<section class="keystone"><div class="wrap">',
                    figblock(slug(CAP_INDUCTION), v_induction, CAP_INDUCTION)
                    + '<section class="keystone"><div class="wrap">', 1)

# ------------------------------------------------------------------------- #
# GRAND REX, SECONDE PHOTO (ajout du 14/08/2026, fournie par David).
#
# Ce bloc etait ajoute A LA MAIN dans `rituals/index.html` : le generateur ne le
# produisait pas, et une regeneration faisait donc DISPARAITRE la photo. Il est
# desormais emis ici, a sa place, a partir des derivees deja presentes dans
# `img/rituals/` — plus rien a refaire a la main, plus rien a perdre.
#
# Placee ICI, juste apres la cle de voute, parce qu'elle montre exactement ce
# que la citation decrit : la salle entiere prise dans le meme geste.
# ⚠️ Elle ne remplace PAS la photo du Grand Rex (plus haut, desormais
# `iris-chasles-et-david-lesage-au-grand-rex-paris`) : les deux angles sont
# opposes — celui-la est pris DEPUIS LA SALLE et montre le plateau, l'ecran
# geant et les bras leves, la ou l'autre — qui sert aussi de fond au hero — est
# pris DEPUIS LA SCENE. Trois sections les separent : aucune repetition.
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
#
# ⚠️ Cette photo a ete preparee a la main : 4 largeurs, dont une de 2000 px que
# la fabrication automatique ne produit pas (elle plafonne a 1400). Son `src` de
# secours est en 1400 px, pas en 900 comme les autres — d'ou `repli=1400`. Elle
# n'a pas de recette dans RECETTES : son original n'est pas dans le depot.
# ------------------------------------------------------------------------- #
# ⚠️ LES TROIS NOMS DE LA LEGENDE (17/08/2026, demande de David).
# La legende ne citait qu'Arnaud Riou, alors que la description longue (`alt`)
# nommait deja les trois. David a demande que la legende VISIBLE nomme aussi
# Iris Chasles et lui-meme. Ils sont donnes de gauche a droite, dans l'ordre ou
# on les voit sur la photo — pas dans un ordre de preseance.
# 🚨 REGLE FERME DE DAVID, VALABLE SUR TOUT LE SITE : on ne nomme que David
#    Lesage, Iris Chasles et Arnaud Riou, et PERSONNE D'AUTRE. Les autres
#    intervenants de la rangee restent « une rangee d'intervenants en noir »
#    dans l'`alt` et ne sont pas nommes ici. Le site a deja publie une
#    identification erronee par le passe (cf. l'avertissement plus haut sur le
#    joueur de tambour).
CAP_BRAS_LEVES = ('Le même geste, sur scène et dans la salle — projeté en direct'
                  ' sur l’écran du Grand Rex. À gauche, <b>David Lesage</b>'
                  ' derrière ses calebasses ; au centre, <b>Iris Chasles</b> ;'
                  ' à droite, <b>Arnaud Riou</b> au tambour sur cadre.')
ALT_BRAS_LEVES = ('Sur la scène du Grand Rex : David Lesage assis au sol à gauche,'
                  ' derrière deux calebasses ; une rangée d’intervenants en noir'
                  ' les bras levés ; Iris Chasles au centre en tailleur rouge,'
                  ' bras levés ; à droite, Arnaud Riou, cheveux gris et barbe'
                  ' blanche, qui frappe un grand tambour sur cadre. Au-dessus'
                  ' d’eux, un écran géant montre la salle comble sur plusieurs'
                  ' niveaux, debout, bras levés.')

# ancre : la fin de la section « cle de voute » (la citation « … apaisé. »).
# `<div class="divider">` seul ne conviendrait pas, la page en compte deux.
ancre_keystone = 'apaisé.</div>\n</div></section>\n\n'
assert html.count(ancre_keystone) == 1, 'ancre de la cle de voute non unique'
if 'grand-rex-bras-leves' not in html:             # garde d'idempotence
    html = html.replace(
        ancre_keystone,
        ancre_keystone + figblock('grand-rex-bras-leves',
                                  derivees('grand-rex-bras-leves'),
                                  CAP_BRAS_LEVES, alt=ALT_BRAS_LEVES,
                                  cred='Nadine Court', repli=1400) + '\n', 1)

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
    vs = derivees(name)
    ar = round(vs[-1][0] / vs[-1][1], 4)
    # Plus de `onclick="openIMG(this)"` ni de `data-full` : la visionneuse
    # commune n'a besoin d'aucun attribut en plus. Elle lit la plus grande
    # variante DANS les `srcset` deja ecrits par `picture()`.
    slides += ('      <div class="slide" style="--ar:%s">' % ar
               + picture(name, vs, SIZES_SLIDE, cap, lazy=i >= 3)
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

# ---------------------------------------- l'ANCIENNE visionneuse est RETIREE
# `sources/rituals_source.html` porte encore la visionneuse rudimentaire de
# 2024 : un calque `#imglb`, une image `#imgbig`, et deux fonctions `openIMG` /
# `closeIMG`. Elle ouvrait la photo, et c'est tout : ni defilement d'une photo
# a l'autre, ni zoom, ni piege a focus, ni retour du focus sur la photo de
# depart, ni verrou du corps de page. La visionneuse commune la remplace.
# Les trois morceaux sont retires ICI, dans le generateur, plutot que dans la
# source : la source reste la page telle qu'elle a ete ecrite, et le jour ou on
# voudra revenir en arriere, il n'y a qu'un bloc a supprimer.
# ⚠️ NE PAS CONFONDRE `.imglb` (photos, retire) ET `.lb` (le lecteur video
#    YouTube, garde) : deux calques differents, deux roles differents.
ANCIENNE_CSS = (
    '.imglb{position:fixed;inset:0;background:rgba(6,7,18,.93);display:none;'
    'align-items:center;justify-content:center;z-index:60;padding:20px;'
    'cursor:zoom-out}\n.imglb.open{display:flex}\n'
    '.imglb img{max-width:96vw;max-height:92vh;border-radius:10px;'
    'border:1px solid var(--line)}\n')
ANCIENNE_HTML = ('<div class="imglb" id="imglb" onclick="closeIMG()">'
                 '<img id="imgbig" src="" alt=""></div>\n')
ANCIEN_JS = ("function openIMG(img){document.getElementById('imgbig').src=img.src;"
             "document.getElementById('imglb').classList.add('open');}\n"
             "function closeIMG(){document.getElementById('imglb')"
             ".classList.remove('open');"
             "document.getElementById('imgbig').src='';}\n")
for _mort, _quoi in ((ANCIENNE_CSS, "feuille de style de l'ancienne visionneuse"),
                     (ANCIENNE_HTML, "calque de l'ancienne visionneuse"),
                     (ANCIEN_JS, "script de l'ancienne visionneuse")):
    assert html.count(_mort) == 1, '%s : introuvable ou en double' % _quoi
    html = html.replace(_mort, '', 1)
# la regle d'impression cachait l'ancien calque : elle cache maintenant le neuf
assert html.count('  .lb,.imglb{display:none!important}\n') == 1
html = html.replace('  .lb,.imglb{display:none!important}\n',
                    '  .lb,.ph{display:none!important}\n', 1)
assert 'openIMG' not in html and 'imglb' not in html and 'imgbig' not in html, \
    "il reste une trace de l'ancienne visionneuse"

# ------------------------------------------- prechargement du fond du hero (LCP)
html = html.replace('<style>',
                    '<link rel="preload" as="image" type="image/webp"'
                    ' href="%s/%s-%d.webp" fetchpriority="high">\n<style>'
                    % (IMG_URL, slug(CAP_REX), v_rex[-1][0]), 1)

# menu mobile (hamburger) : absent de la source, injecte ici
sys.path.insert(0, HERE)
import mobile_nav
html = mobile_nav.inject(html)

# `mobile_nav.inject()` colle son CSS tout en fin de feuille de style. Dans la
# page publiee il se trouve plus haut, juste apres les regles de mise en page
# mobile de la galerie — position heritee d'une epoque ou CSS_ADD s'arretait la.
# On l'y remet : ainsi le bloc « lisibilite des liens », qui doit rester le
# dernier a parler taille de police, garde le dernier mot.
ANCRE_HAMBURGER = ('@media(max-width:600px){.aphoto{float:none;width:62%;'
                   'display:block;margin:0 auto 16px}.car-btn{display:none}}\n')
assert html.count(mobile_nav.CSS) == 1, 'CSS du hamburger introuvable ou en double'
assert html.count(ANCRE_HAMBURGER) == 1, 'ancre du hamburger non unique'
html = html.replace(mobile_nav.CSS, '', 1)
html = html.replace(ANCRE_HAMBURGER, ANCRE_HAMBURGER + mobile_nav.CSS, 1)

# ------------------------------------------------------- la visionneuse photo
# Les 26 photos de la page, dans l'ordre du document : les 4 grandes images de
# section (`.figure`), les 2 portraits des artistes (`picture.aphoto`) et les
# 20 photos du carrousel (`.slide`).
# ⚠️ LE CARROUSEL RESTE. Son role est de faire defiler les photos DANS la page ;
#    la visionneuse s'ajoute par-dessus. Les deux ne se marchent pas dessus :
#    la visionneuse n'ecoute le clavier QUE pendant qu'elle est ouverte (son
#    ecouteur `keydown` est pose a l'ouverture et retire a la fermeture), donc
#    elle ne prend jamais les fleches du carrousel quand elle est fermee.
# ⚠️ LE DEFILEMENT AUTOMATIQUE DU CARROUSEL EST MIS EN PAUSE quand on ouvre une
#    photo. Au clic c'etait deja le cas : `carPause` est deja branche sur le
#    `pointerdown` du rail. AU CLAVIER, non — d'ou les trois lignes ci-dessous.
#    Sans elles, le carrousel continuait d'avancer derriere la visionneuse et la
#    page se retrouvait ailleurs a la fermeture.
PAUSE_JS = ('<script>\n'
            "(function(){var t=document.getElementById('cartrack'); if(!t)return;\n"
            "  t.addEventListener('keydown',function(e){\n"
            "    if(e.key==='Enter'||e.key===' '||e.key==='Spacebar')carPause();});\n"
            '})();\n</script>\n')
html = html.replace('</body>',
                    visionneuse.js('.figure img, picture.aphoto img, .slide img')
                    + PAUSE_JS + '</body>', 1)

# Ligne vide entre le dernier script de la page et le bloc du menu partage. Elle
# vient de la mise a jour du menu v1 -> v2 : `nav_menu._strip()` a retire
# l'ancien bloc en laissant le saut de ligne qui le suivait. Toutes les pages
# publiees l'ont ; on la reproduit pour qu'une regeneration ne modifie pas un
# octet.
html = html.replace('</script>\n</body>', '</script>\n\n</body>', 1)

# menu de navigation partage (Accueil / Sur scene / Le Nid / L'association / Contact)
import nav_menu
html = nav_menu.inject(html, 'rituals')

assert 'data:image' not in html.replace("data:image/webp'", ''), 'il reste du base64'

# Garde-fou AVANT l'ecriture : aucune note de redaction en commentaire HTML
# dans la page livree (elle serait publique et indexable).
import verif_commentaires
verif_commentaires.verifier(html, TARGET)

# La visionneuse tient a DEUX choses : sa feuille de style et son script.
# Perdre l'une des deux ne casserait rien a l'ecran — les photos cesseraient
# simplement d'etre cliquables, en silence. Le troisieme marqueur protege la
# ligne qui rend cliquable le BAS des photos du carrousel (la legende `.cap2`
# passe par-dessus).
for _m, _r in (('.ph{position:fixed', 'feuille de style de la visionneuse'),
               ("var SEL='.figure img", 'script de la visionneuse'),
               ('.cap2{pointer-events:none}', 'bas des photos du carrousel cliquable')):
    assert html.count(_m) == 1, '%s : %d occurrence(s), attendu 1' % (_r, html.count(_m))

os.makedirs(os.path.dirname(TARGET), exist_ok=True)
with open(TARGET, 'w', encoding='utf-8') as f:
    f.write(html)
print('ECRIT', TARGET, round(len(html.encode()) / 1024), 'ko  +',
      len(os.listdir(IMG_DIR)), 'fichiers dans', IMG_DIR)
