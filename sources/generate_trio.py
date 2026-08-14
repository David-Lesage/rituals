# -*- coding: utf-8 -*-
"""Genere /rituals-trio/index.html a partir de sources/trio_source.html.

    python3 sources/generate_trio.py            # regenere la page (par defaut)
    python3 sources/generate_trio.py --images   # refabrique les derivees, puis la page

DEUX TRAVAUX BIEN SEPARES  (meme remede que sources/generate_site.py, 14/08/2026)
---------------------------------------------------------------------------
1. GENERER LA PAGE (ce que fait ce script par defaut). Il ne lit QUE des
   fichiers presents dans le depot : `sources/trio_source.html` et les derivees
   deja optimisees de `img/rituals/` et `img/rituals-trio/`. Aucune photo
   d'origine, aucun telechargement Drive, aucune bibliotheque d'images : les
   dimensions des <picture> sont relues dans les JPEG eux-memes (`_dim_jpeg`).
   Le script tourne donc partout, sur un simple `git clone`.

2. FABRIQUER LES DERIVEES a partir des photos d'origine (section
   « FABRICATION »). Les dossiers d'entree `promo_raw/`, `web_img/`, `trio_img/`
   et `perspectives_raw/` sont HORS DEPOT, et les photos du festival
   Perspectives viennent d'un partage Google Drive : cette etape n'est faisable
   que sur la machine qui detient les originaux (ou avec le reseau). Elle est
   donc OPTIONNELLE et ne se declenche qu'avec `--images`. Son impossibilite
   n'empeche plus de regenerer la page — c'etait exactement la panne
   « photo introuvable dans web_img/ : RITUALS_00_header.jpg ».
   Elle a aussi besoin de Pillow, importe seulement a ce moment-la.

Plus aucune photo en base64 (la page pesait 4,4 Mo) et plus aucune image servie
depuis Google Drive : tout est en fichiers, en trois largeurs
(480 / 900 / 1400 px), WebP + repli JPEG, via <picture>.

Les photos communes avec /rituals vivent dans /img/rituals/ et sont partagees :
un visiteur qui voit les deux pages ne les telecharge qu'une fois. Seules les
photos propres au trio (festival Perspectives, portrait de Julien) sont dans
/img/rituals-trio/.

Sortie : ../rituals-trio/index.html  (et, avec --images, ../img/rituals*/…)
"""
import glob, os, re, sys, unicodedata, html as _html

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


def _dim_jpeg(chemin):
    """(largeur, hauteur) d'un JPEG, lues dans son marqueur SOF.

    Volontairement sans Pillow : generer la page ne doit dependre de rien
    d'autre que de la bibliotheque standard. Copie conforme de la meme fonction
    dans generate_site.py — les deux scripts doivent rester independants
    (s'importer l'un l'autre EXECUTERAIT l'autre et ecraserait sa page).
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


def derivees(dossier, name):
    """[(largeur, hauteur), ...] des derivees deja presentes dans le depot.

    Remplace l'ancien appel a la fabrication d'images : la page se regenere a
    partir de ce qui est DANS le depot. L'ordre (largeurs croissantes) est celui
    que produisait la fabrication, et dont dependent `picture()` (attributs
    width/height = plus grande variante) et le srcset.
    """
    trouves = []
    for p in glob.glob(os.path.join(dossier, name + '-*.jpg')):
        m = re.fullmatch(re.escape(name) + r'-(\d+)\.jpg', os.path.basename(p))
        if m:
            trouves.append((int(m.group(1)), p))
    if not trouves:
        sys.exit('derivee absente de %s : %s-<largeur>.jpg — la fabriquer avec '
                 '`--images` (photos d\'origine requises).' % (dossier, name))
    trouves.sort()
    ws = [w for w, _p in trouves]

    # ⚠️ Un JEU INCOMPLET est plus dangereux qu'un jeu absent : sans ce controle,
    # un fichier efface par megarde ne fait pas echouer le script — il produit
    # simplement un srcset ampute, donc une page differente de la publiee, en
    # silence. (Mesure du 14/08/2026 : retirer une seule derivee de 900 px
    # laissait le script ecrire une page degradee, code de sortie 0.)
    # Les largeurs doivent etre WIDTHS dans l'ordre, la derniere pouvant etre
    # plus petite que prevu quand l'original ne permettait pas d'aller plus haut
    # (la fabrication ne suragrandit jamais).
    attendu = list(WIDTHS[:len(ws)])
    contigu = (len(ws) <= len(WIDTHS)
               and (ws == attendu
                    or (ws[:-1] == attendu[:-1] and ws[-1] < attendu[-1])))
    if not contigu:
        sys.exit('largeurs incoherentes pour %s dans %s : %s (attendu un debut de '
                 '%s). Un fichier a du etre efface ; refabriquer avec `--images`.'
                 % (name, dossier, ws, list(WIDTHS)))
    for w, _p in trouves:                              # chaque JPEG a son WebP
        jumeau = os.path.join(dossier, '%s-%d.webp' % (name, w))
        if not os.path.exists(jumeau):
            sys.exit('WebP manquant : %s (le srcset le referencerait quand meme).'
                     % jumeau)
    return [(w, _dim_jpeg(p)[1]) for w, p in trouves]


def partagee(name):
    """Photo commune avec /rituals : elle vit dans /img/rituals/."""
    return URL_SHARED + '/' + name, derivees(DIR_SHARED, name)


def propre(name):
    """Photo propre au trio : elle vit dans /img/rituals-trio/."""
    return URL_TRIO + '/' + name, derivees(DIR_TRIO, name)


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


CAP_INTENTION = 'Le public au cœur du rituel'
CAP_REX = 'Au Grand Rex devant 2700 personnes'
CAP_INDUCTION = 'L’induction — la voix qui guide, vers un état de conscience élargie'
CAP_PERSP = 'Le trio en scène — festival Perspectives'

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


# =========================================================================== #
# FABRICATION DES DERIVEES — OPTIONNELLE, et volontairement a part.
#
# Elle transforme les photos d'origine en `img/rituals*/<nom>-<largeur>.webp|jpg`.
# Ses entrees sont HORS DEPOT (`sources/promo_raw/`, `sources/web_img/`,
# `sources/trio_img/`) ou distantes (partage Google Drive du festival
# Perspectives, mis en cache dans `sources/perspectives_raw/`). Rien ici n'est
# necessaire pour generer la page : c'est justement le piege qu'on desamorce —
# le script s'arretait sur « photo introuvable dans web_img/ » et /rituals-trio
# ne pouvait plus etre reconstruite du tout.
#
# Sans `--images`, ce bloc n'est jamais execute, Pillow n'est meme pas importe,
# et rien n'est telecharge. A relancer uniquement pour ajouter ou remplacer une
# photo. La fabrication ECRASE les derivees qu'elle produit, n'en efface aucune
# autre.
#
# RECETTES : nom de la derivee -> (dossier de sortie, provenance, cle, largeur
# max, rognage). On la garde ici parce que sans elle plus personne ne saurait
# refaire une derivee a l'identique.
#   'web'   -> sources/web_img/<cle>          (nom de fichier exact)
#   'promo' -> sources/promo_raw/*<cle>*      (jeton cherche dans le nom)
#   'trio'  -> sources/trio_img/<cle>         (nom de fichier exact)
#   'drive' -> partage Google Drive, <cle> = identifiant du fichier
# ⚠️ Les photos communes avec /rituals ont exactement les memes recettes que
#    dans generate_site.py : les deux pages partagent les MEMES fichiers de
#    img/rituals/. Modifier l'une des deux tables sans l'autre les ferait
#    diverger a la prochaine fabrication.
# =========================================================================== #

RECETTES = {
    'hero-grand-rex':           (DIR_SHARED, 'web',   'RITUALS_00_header.jpg', 1600, None),
    slug(CAP_INTENTION):        (DIR_SHARED, 'promo', '20248.', 1300, None),
    slug(CAP_REX):              (DIR_SHARED, 'web',   'RITUALS_00_header.jpg', 1500, None),
    slug(CAP_INDUCTION):        (DIR_SHARED, 'promo', 'iris_priere', 1300, None),
    'cle-de-voute-duo-theatre': (DIR_SHARED, 'promo', '20245.', 1400, None),
    'portrait-david-lesage':    (DIR_SHARED, 'promo', 'David_Lesage_2025_Carre_HD', 900, None),
    'portrait-iris-chasles':    (DIR_SHARED, 'web',   'RITUALS_06_Iris-Chasles.jpg', 700,
                                 (0.20, 0.0, 0.82, 0.78)),
    'portrait-julien-dub-au-saxophone': (DIR_TRIO, 'trio', 'julien_sax.jpg', 1200, None),
}
# les 18 photos du duo dans le carrousel viennent de promo_raw/, plafonnees a 1500 px
RECETTES.update({slug(cap): (DIR_SHARED, 'promo', tok, 1500, None) for tok, cap in GAL})
# les 13 photos du festival viennent du partage Drive, en 2000 px d'origine
RECETTES.update({PERSP_NAME[fid]: (DIR_TRIO, 'drive', fid, None, None)
                 for fid, _cap in PERSP})


def fabriquer(noms=None):
    """(Re)fabrique les derivees decrites par RECETTES. Necessite Pillow."""
    from urllib.request import urlopen
    from PIL import Image                          # importe ici, et ici seulement
    Image.MAX_IMAGE_PIXELS = None

    def ouvrir(chemin, mw, crop):
        im = Image.open(chemin).convert('RGB')
        if crop:
            w, h = im.size
            im = im.crop((int(crop[0] * w), int(crop[1] * h),
                          int(crop[2] * w), int(crop[3] * h)))
        if mw:
            im.thumbnail((mw, mw))
        return im

    def origine(provenance, cle):
        if provenance == 'promo':                  # jeton cherche dans le nom
            hits = sorted(glob.glob(os.path.join(HERE, 'promo_raw', '*' + cle + '*')))
            if not hits:
                sys.exit('photo introuvable dans promo_raw/ : ' + cle)
            return hits[0]
        if provenance == 'drive':                  # rapatriee puis mise en cache
            os.makedirs(CACHE, exist_ok=True)
            p = os.path.join(CACHE, cle + '.jpg')
            if not os.path.exists(p):
                print('    telechargement', cle)
                with urlopen('https://lh3.googleusercontent.com/d/%s=w2000' % cle,
                             timeout=90) as r, open(p, 'wb') as f:
                    f.write(r.read())
            return p
        dossier = {'web': 'web_img', 'trio': 'trio_img'}[provenance]
        p = os.path.join(HERE, dossier, cle)
        if not os.path.exists(p):
            sys.exit('photo introuvable dans %s/ : %s' % (dossier, cle))
        return p

    def variantes(im, outdir, name):
        """Ecrit name-<w>.webp et name-<w>.jpg. Retourne [(largeur, hauteur), ...]."""
        os.makedirs(outdir, exist_ok=True)
        ow, oh = im.size
        out = []
        for w in WIDTHS:
            if w > ow and out:
                break                              # jamais de suragrandissement
            ww = min(w, ow)
            hh = max(1, round(oh * ww / ow))
            r = im if (ww, hh) == (ow, oh) else im.resize((ww, hh), Image.LANCZOS)
            r.save(os.path.join(outdir, '%s-%d.webp' % (name, ww)), 'WEBP',
                   quality=Q_WEBP, method=6)
            r.save(os.path.join(outdir, '%s-%d.jpg' % (name, ww)), 'JPEG',
                   quality=Q_JPEG, optimize=True, progressive=True)
            out.append((ww, hh))
        return out

    for name in (noms or sorted(RECETTES)):
        outdir, provenance, cle, mw, crop = RECETTES[name]
        vs = variantes(ouvrir(origine(provenance, cle), mw, crop), outdir, name)
        print('  %-42s %s' % (name, ' '.join('%dx%d' % v for v in vs)))


if '--images' in sys.argv:
    print('fabrication des derivees :')
    fabriquer()


# =========================================================================== #
# GENERATION DE LA PAGE — ne lit que ce qui est dans le depot
# =========================================================================== #

# Les dimensions viennent des JPEG deja versionnes. Ces lignes sont volontairement
# APRES le bloc `--images` : sinon une derivee manquante arreterait le script avant
# meme d'avoir eu la chance de la fabriquer.
u_hero, v_hero = partagee('hero-grand-rex')
u_intent, v_intent = partagee(slug(CAP_INTENTION))
u_rex, v_rex = partagee(slug(CAP_REX))
u_induc, v_induc = partagee(slug(CAP_INDUCTION))
u_key, v_key = partagee('cle-de-voute-duo-theatre')
u_david, v_david = partagee('portrait-david-lesage')
u_iris, v_iris = partagee('portrait-iris-chasles')
u_julien, v_julien = propre('portrait-julien-dub-au-saxophone')

with open(SOURCE, 'r', encoding='utf-8') as f:
    html = f.read()

# ⚠️ DEUX TAILLES DE POLICE RAPATRIEES DU HTML FAIT MAIN (14/08/2026).
# La page publiee portait `.nav .brand{font-size:13px}` et `.cap2{font-size:13px}`
# la ou ce gabarit ecrivait 12px et 12.5px. Ce n'est pas cosmetique : c'est le
# PLANCHER TYPOGRAPHIQUE de 13 px pose lors de la passe d'accessibilite (voir
# le handoff, section « Accessibilite / SEO »), et /rituals porte les memes
# valeurs. Les remettre plus bas serait une regression d'accessibilite.
CSS_ADD = """
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

# --------------------------------------------------------------------------- #
# DEUX CORRECTIFS CSS QUI ETAIENT POSES A LA MAIN DANS LA PAGE PUBLIEE.
# Meme situation que sur /rituals : tant qu'ils n'etaient nulle part dans le
# generateur, toute regeneration les perdait. Ils sont donc rapatries ici, avec
# leur raison d'etre.
# --------------------------------------------------------------------------- #

# 1) Le style du credit photo (`.cred-fig`) n'existe pas dans la source. Sans
#    lui, la mention « Credit photo … » sous la figure du Grand Rex perd sa mise
#    en forme et sa zone tactile de 44 px. On le pose juste apres la regle de
#    focus clavier, la ou il se trouve dans la page publiee.
ANCRE_FOCUS = (':focus-visible{outline:2px solid var(--gold2);'
               'outline-offset:2px;border-radius:4px}\n')
CSS_CRED = """/* credit photo sous une figure (signature du photographe visible sur l'image) */
.cred-fig{margin-top:8px;text-align:center;font-size:15px;color:var(--muted)}
.cred-fig a{color:var(--gold);text-decoration:underline;text-decoration-color:rgba(216,178,90,.45);text-underline-offset:3px;display:inline-block;padding:11px 0}
.cred-fig a:hover{color:var(--gold2)}
"""
assert ANCRE_FOCUS in html, 'ancre :focus-visible introuvable'
if '.cred-fig{' not in html:                       # garde d'idempotence
    html = html.replace(ANCRE_FOCUS, ANCRE_FOCUS + CSS_CRED, 1)

# 2) Le bloc « lisibilite des liens » vit dans la source, donc AVANT le CSS
#    ajoute ici. Or il doit passer APRES : `.nav .links a{font-size:14.5px}`
#    doit l'emporter sur la regle de la barre de navigation posee plus bas, et
#    les soulignements sur les regles de figure. On le deplace donc en fin de
#    CSS_ADD — c'est exactement sa position dans la page publiee.
DEB_LISI = '/* --- lisibilite des liens (demande de David : liens et dates trop petits) --- */'
FIN_LISI = '  text-decoration-color:rgba(216,178,90,.4);text-underline-offset:3px}\n'
d = html.find(DEB_LISI)
assert d != -1, 'bloc « lisibilite des liens » introuvable dans la source'
f = html.find(FIN_LISI, d) + len(FIN_LISI)
BLOC_LISI = html[d:f]
html = html[:d - 1] + html[f:]                     # -1 : la ligne vide qui precede
CSS_ADD = CSS_ADD.replace('</style>', '\n' + BLOC_LISI + '\n</style>', 1)

html = html.replace('</style>', CSS_ADD, 1)


# CREDITS PHOTO. La photo du Grand Rex porte la signature du photographe,
# visible a l'oeil sur l'image : la mention et le lien sont donc obligatoires
# sous la figure. Le `.cred-fig` se place APRES la legende, dans le meme
# `.wrap` — la legende reste collee a sa photo, le credit vient dessous.
# (C'est la MEME photo que sur /rituals, d'ou le meme credit.)
CRED = {
    "MAGYE D'ART": 'https://magyedart.fr/',
}


def credit(qui):
    """Ligne « Credit photo <lien> » a poser sous la legende d'une figure."""
    return ('<div class="cred-fig">Crédit photo <a href="%s" target="_blank"'
            ' rel="noopener">%s</a></div>' % (CRED[qui], qui))


def figblock(urlbase, vs, cap, lazy=True, cred=None):
    return ('<section class="figsec"><div class="wrap"><div class="figure">'
            + picture(urlbase, vs, SIZES_FIG, cap, lazy=lazy)
            + '</div><div class="cap">' + cap + '</div>'
            + (credit(cred) if cred else '') + '</div></section>\n')


# figure de l'intention (premiere image de la page : chargement immediat)
sig = '  <div class="sig">On en repart plus léger. Comme au sortir d’une longue inspiration.</div>'
assert sig in html, 'ancre sig introuvable'
html = html.replace(sig, sig + '\n  <div class="figure">'
                    + picture(u_intent, v_intent, SIZES_FIG, CAP_INTENTION, lazy=False)
                    + '</div>\n  <div class="cap">' + CAP_INTENTION + '</div>', 1)

# le trio en scene, avant « Le voyage »
u_persp1, v_persp1 = propre(PERSP_NAME['15_WWObM1AP2FFVWwKGpd_eAkFJzcFQP1'])
anchor_voyage = '<section class="journey"><div class="wrap">\n  <div class="kick">Le voyage</div>'
assert anchor_voyage in html, 'ancre voyage introuvable'
html = html.replace(anchor_voyage,
                    figblock(u_persp1, v_persp1, CAP_PERSP) + anchor_voyage, 1)

# le Grand Rex, au-dessus de « Pour les organisateurs »
anchor_orga = '<section class="orga"><div class="wrap">\n  <div class="kick">Pour les organisateurs</div>'
assert anchor_orga in html, 'ancre orga introuvable'
html = html.replace(anchor_orga,
                    figblock(u_rex, v_rex, CAP_REX, cred="MAGYE D'ART")
                    + anchor_orga, 1)

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
        urlbase, vs = partagee(slug(cap))
    else:
        urlbase, vs = propre(PERSP_NAME[ref])
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

# Ligne vide entre le script du hamburger et le bloc du menu partage. Elle vient
# de la mise a jour du menu v1 -> v2 : `nav_menu._strip()` a retire l'ancien bloc
# en laissant le saut de ligne qui le suivait. Toutes les pages publiees l'ont ;
# on la reproduit pour qu'une regeneration ne modifie pas un octet.
html = html.replace('</script>\n</body>', '</script>\n\n</body>', 1)

# menu de navigation partage
import nav_menu
import verif_commentaires  # garde-fou commentaires HTML
html = nav_menu.inject(html, 'rituals-trio')

assert 'data:image' not in html.replace("data:image/webp'", ''), 'il reste du base64'
assert 'googleusercontent' not in html, 'il reste une URL Drive'

# --------------------------------------------------------------------------- #
# GARDE-FOUS STRUCTURELS, AVANT L'ECRITURE. Modele : generate_rythme.py.
# On compte les ancres qui doivent etre uniques : un ecart les attrape AUSSI
# BIEN en disparition qu'en duplication (le piege des quatre cartes
# identiques). On REFUSE d'ecrire une page cassee plutot que d'imprimer un
# avertissement qui defile.
# --------------------------------------------------------------------------- #
_ATTENDU_1 = (
    ('<h1', 'titre principal de la page'),
    ('data-nav="resonances-2"', 'menu partage nav_menu.py'),
    # le bouton hamburger est CREE PAR LE JS : il n'existe pas en dur dans la
    # page, on compte donc la ligne du script qui le fabrique.
    ("b.className='burger'", 'bouton hamburger de mobile_nav.py'),
    ('===== MENU MOBILE', 'feuille de style du hamburger'),
    ('.cred-fig{', 'style du credit photo (rapatrie du HTML fait main)'),
    ('<div class="cred-fig">', 'credit photo MAGYE D\'ART sous le Grand Rex'),
    ('/* --- lisibilite des liens', 'bloc « lisibilite des liens » (plancher typo)'),
    ('id="cartrack"', 'piste du carrousel'),
)
for _marqueur, _quoi in _ATTENDU_1:
    _n = html.count(_marqueur)
    if _n != 1:
        raise SystemExit('!! ABANDON : %d occurrence(s) de « %s » (%s), attendu 1. '
                         'Page NON ecrite.' % (_n, _marqueur, _quoi))

# Les trois portraits d'artistes (David, Iris, Julien) sont les seules images en
# `class="aphoto"`. C'est le portrait de Julien qui disparaissait le plus
# facilement : il passe par une balise de substitution du gabarit.
_ATTENDU_N = (
    ('<picture class="aphoto"', 3, 'portraits David / Iris / Julien'),
)
for _marqueur, _combien, _quoi in _ATTENDU_N:
    _n = html.count(_marqueur)
    if _n != _combien:
        raise SystemExit('!! ABANDON : %d occurrence(s) de « %s » (%s), attendu %d. '
                         'Page NON ecrite.' % (_n, _marqueur, _quoi, _combien))
if 'portrait-julien-dub-au-saxophone-' not in html:
    raise SystemExit('!! ABANDON : le portrait de Julien Dub n\'est pas dans la '
                     'page. Page NON ecrite.')

# Les balises de substitution de trio_source.html doivent avoir ete consommees :
# si l'une survit dans le HTML livre, c'est un bug (et verif_commentaires la
# refuserait de toute facon — elles ne sont pas dans sa liste blanche).
for _balise in ('<!--INDUCTION_FIG-->', '<!--JULIEN_PHOTO-->'):
    if _balise in html:
        raise SystemExit('!! ABANDON : la balise de substitution %s n\'a pas ete '
                         'remplacee. Page NON ecrite.' % _balise)

# 31 diapos exactement : 1 ouverture + 27 entrelacees + 3 portraits. Un ecart
# signale soit une photo perdue, soit une passe qui ajoute (les « 4 cartes »).
if html.count('<div class="slide"') != len(_final):
    raise SystemExit('!! ABANDON : %d diapos dans le carrousel, %d attendues. '
                     'Page NON ecrite.'
                     % (html.count('<div class="slide"'), len(_final)))

# Garde-fou AVANT l'ecriture : aucune note de redaction en commentaire HTML
# dans la page livree (elle serait publique et indexable).
verif_commentaires.verifier(html, TARGET)

os.makedirs(os.path.dirname(TARGET), exist_ok=True)
with open(TARGET, 'w', encoding='utf-8') as f:
    f.write(html)
print('ECRIT', TARGET, round(len(html.encode()) / 1024), 'ko  | burger:',
      'class="burger"' in html or '.burger{' in html)
