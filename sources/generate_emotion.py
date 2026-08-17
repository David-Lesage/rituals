# -*- coding: utf-8 -*-
"""Genere la page /e-motion (spectacle immersif participatif, ID duo).

    python3 sources/generate_emotion.py       # depuis la racine du depot

POURQUOI CE FICHIER EXISTE
--------------------------
/e-motion etait la seule page publiee SANS generateur : elle ne pouvait plus
etre modifiee qu'a la main, sans filet. Et sa seule « source »,
`sources/emotion_final.html`, etait PERIMEE — elle portait encore le menu
`resonances-1` : regenerer la page a partir de la aurait CASSE le menu. Cette
copie trompeuse est supprimee, ce fichier la remplace.

COMMENT LA PAGE SE FABRIQUE
---------------------------
1. GABARIT : la page complete, mais SANS le menu hamburger et SANS le menu
   partage — les deux sont poses par leurs composants, pour qu'une montee de
   version du menu (`NAV_VERSION`) se propage ici comme ailleurs.
2. `mobile_nav.inject()` puis `nav_menu.inject()`. Le script appelle nav_menu
   LUI-MEME : une seule commande a lancer, pas de passe a oublier — c'est le
   parti-pris de `generate_rythme.py`, et c'est le plus sur.
3. Garde-fous structurels, puis `verif_commentaires`, AVANT l'ecriture : on
   refuse d'ecrire une page cassee ou porteuse de notes de redaction, plutot
   que d'imprimer un avertissement que personne ne lit.

Le script est idempotent par construction : il repart du gabarit a chaque fois,
il n'ajoute jamais a la page precedente. Deux executions de suite ne changent
rien, une passe supplementaire de `nav_menu.py` non plus.

Sortie : `e-motion/index.html`, identique A L'OCTET PRES a la page publiee.

CE QU'IL NE FAUT SURTOUT PAS PERDRE DANS CETTE PAGE
---------------------------------------------------
- Les CREDITS PHOTO « Credit photo MAGYE D'ART » (magyedart.fr) sous les quatre
  photos filigranees de la galerie, avec leur structure `.gal-ph` : la legende
  s'ancre a la PHOTO, le credit se pose DESSOUS. C'est un correctif fait expres
  pour regler un chevauchement legende/credit — ne pas « simplifier ».
- Le LECTEUR VIDEO qui ouvre les videos DANS la page (`openYT()` / `#ytlb`),
  jamais dans un nouvel onglet. Regle posee par David pour tout le site.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mobile_nav          # menu hamburger mobile             # noqa: E402
import nav_menu            # menu de navigation partage        # noqa: E402
import theme_chaleur       # couche chaleureuse commune        # noqa: E402
import visionneuse         # visionneuse photo commune         # noqa: E402
import verif_commentaires  # garde-fou commentaires HTML       # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, 'e-motion')
OUT_HTML = os.path.join(OUT_DIR, 'index.html')


# --------------------------------------------------------------------------- #
# LA SECTION « AU GRAND REX » (17/08/2026)
# --------------------------------------------------------------------------- #
# Onze photos du Grand Rex (Paris), fournies par David et publiees a sa demande.
#
# POURQUOI CES ONZE-LA, ET PAS TREIZE. David en avait retrouve treize.
#  - Une est ECARTEE : son filigrane « MAGYE D'ART Production » est repete en
#    mosaique sur toute l'image, par-dessus les visages — c'est une epreuve de
#    previsualisation, pas un tirage. Decision prise avec David.
#  - Une autre est un DOUBLON de `img/rituals/grand-rex-bras-leves-*`, deja
#    publiee sur /rituals : c'est le meme cliche (la salle projetee sur l'ecran
#    geant, l'equipe bras leves), simplement en definition superieure. Verifie a
#    l'oeil, pas au md5 : les fichiers du depot sont redimensionnes, leur
#    empreinte ne peut pas correspondre. On ne republie pas.
#
# LES DEUX PHOTOGRAPHES. Le nom est LISIBLE sur le filigrane, en bas a droite de
# chaque image : huit portent « MAGYE D'ART », trois « Nadine Court
# PHOTOGRAPHE ». Le credit est donc pose photo par photo, jamais en bloc.
# ⚠️ Le site de Nadine Court affiche « Nadine Tremblay ». On credite « Nadine
#    Court », le nom qu'elle a SIGNE sur l'image — meme regle que sur /rituals.
# ⚠️ Les filigranes discrets restent visibles sur les photos publiees : arbitre
#    par David (« tant pis pour les filigranes, la photographe est citee avec le
#    lien vers son site »). Ne pas y revenir.
#
# CE QU'ON NE DIT PAS. La legende de la section est la mention seule, telle que
# David l'a ecrite : « Grand Rex, Paris — 2 700 personnes. » Pas de « dans le
# cadre de », pas de nom de production, pas de contexte. Consigne ferme :
# « on n'a pas besoin de tout justifier tout le temps ».
#
# LES NOMS DE PERSONNES. Seul David Lesage est nomme, la ou il est formellement
# identifiable (cheveux longs, ngoni sur calebasse, micro-casque). Les autres
# artistes sont DECRITS, jamais nommes : le projet a deja publie une
# identification erronee sur /rituals, corrigee apres coup. Dans le doute, on
# decrit ce qu'on voit.
#
# STRUCTURE. Exactement celle de la galerie du dessus, ne pas la « simplifier » :
#     .gal-item  >  .gal-ph (la photo + sa legende `.c`)  +  .cred (le credit)
# C'est aussi ce qui met ces photos DANS LA VISIONNEUSE sans toucher a son
# selecteur : elle prend `.gal-item img`. Une structure hors de ce moule serait
# la structure a corriger, pas le selecteur.
#
# LES DERIVEES. Fabriquees a part (Pillow, LANCZOS, WebP q80 / JPEG q82
# progressif — les reglages de `generate_site.py`), en 480/900/1400 px, plus une
# 2000 px quand l'original le permet : la visionneuse zoome dans la PLUS GRANDE
# variante du `srcset`, donc une 2000 px vaut un zoom net. Les deux photos
# verticales (1440 px de large a l'origine) s'arretent a 1400 — on ne fabrique
# jamais une variante plus grande que la source, elle serait floue.
# Les originaux ne sont pas dans le depot : comme `grand-rex-bras-leves`, cette
# serie n'a pas de recette rejouable ici.

#: photographes cites, et leur site. Meme table que `generate_site.py`.
CRED_PHOTO = {
    "MAGYE D'ART": 'https://magyedart.fr/',
    'Nadine Court': 'https://kairos-photo-artisan.com/',
}

#: (nom de fichier, largeurs disponibles, hauteur de la plus grande, photographe,
#: legende affichee sous la photo, texte alternatif).
#: L'ordre est celui de la page : la salle d'abord, puis le plateau.
PHOTOS_REX = (
    ('grand-rex-la-salle-debout', (480, 900, 1400, 2000), 1331, 'Nadine Court',
     'La respiration de la joie, guidée par Iris Chasles',
     'La mise en mouvement de la respiration de la joie de 2 700 personnes, guidée '
     'par Iris Chasles : la salle du Grand Rex debout, au premier rang les bras '
     'tendus vers la scène ; derrière, les deux balcons pleins jusqu’en haut, '
     'découpés par les projecteurs.'),
    ('grand-rex-le-plateau-et-l-ecran', (480, 900, 1400, 2000), 1331, 'Nadine Court',
     'Iris guide, David impulse le rythme',
     'Sur le plateau du Grand Rex, Iris Chasles en rouge guide les gestes de la '
     'salle, tandis que David Lesage, assis derrière sa calebasse, impulse le '
     'rythme pour que tout le monde soit ensemble dans le même geste ; autour '
     'd’eux une dizaine d’artistes en tenue sombre, et au-dessus l’écran géant qui '
     'les reprend en gros plan.'),
    ('grand-rex-au-milieu-des-tambours', (480, 900, 1400, 2000), 1331, 'Nadine Court',
     'À la calebasse, avec le chœur des tambours',
     'David Lesage et Iris Chasles à la calebasse, entourés du chœur des tambours '
     'de l’Academy de l’Act : tout autour d’eux, debout, des musiciennes et des '
     'musiciens tiennent des tambours sur cadre, mailloche levée. Au premier plan, '
     'des silhouettes floues.'),
    ('grand-rex-chant-et-ngoni', (480, 900, 1400, 2000), 1333, "MAGYE D'ART",
     'Le public répond en écho',
     'Arnaud Riou au tambour ; David Lesage, micro-casque au visage, fait chanter '
     'la salle en l’accompagnant au ngoni, en échanges vocaux auxquels le public '
     'répond en écho ; Iris Chasles à la calebasse.'),
    ('grand-rex-le-ngoni-dans-la-lumiere', (480, 900, 1400, 2000), 1333, "MAGYE D'ART",
     'Le ngoni dans la lumière',
     'David Lesage, à genoux et micro-casque au visage, joue du ngoni dans une '
     'lumière vert et or ; au premier plan, le mouvement flou d’une danseuse '
     'traverse le cadre.'),
    ('grand-rex-ngoni-et-lumieres-rouges', (480, 900, 1400, 2000), 1333, "MAGYE D'ART",
     'Devant les colonnes de lumière',
     'David Lesage, assis en tailleur sur une peau blanche et souriant, joue du '
     'ngoni monté sur calebasse ; derrière lui deux colonnes de lumière rouge et '
     'des palmes, une seconde calebasse posée à sa droite.'),
    ('grand-rex-danse-en-rouge', (480, 900, 1400, 2000), 1333, "MAGYE D'ART",
     'Iris Chasles, en rouge sur le plateau',
     'Iris Chasles, en tunique rouge et en grande fente sur le plateau du Grand '
     'Rex, tenue par son baudrier à l’élastique qui descend des cintres ; derrière '
     'elle, un fond bleu profond.'),
    ('grand-rex-bras-ouverts', (480, 900, 1400, 2000), 1333, "MAGYE D'ART",
     'Comme deux oiseaux',
     'Comme deux oiseaux, David Lesage et Iris Chasles saluent le public avec '
     'grâce, dans le silence — un moment suspendu : debout l’un derrière l’autre '
     'sur le plateau du Grand Rex, bras grands ouverts vers le haut, le même geste '
     'repris à deux ; Iris Chasles, devant, porte une tunique rouge.'),
    ('grand-rex-suspendue-tete-en-bas', (480, 900, 1400), 2100, "MAGYE D'ART",
     'Iris Chasles vole, en grand écart',
     'Vue depuis la salle : Iris Chasles, en rouge, vole très haut au-dessus du '
     'plateau du Grand Rex — tête en bas et jambes ouvertes en grand écart, tenue '
     'par son baudrier à l’élastique ; au premier plan, les têtes du public dans '
     'l’ombre.'),
    ('grand-rex-jupe-en-tournoiement', (480, 900, 1400), 2100, "MAGYE D'ART",
     'Iris Chasles, la danse de tournoiement',
     'La danse de tournoiement : Iris Chasles, en haut vert et longue jupe orange, '
     'tourne sur elle-même sur le plateau du Grand Rex, un bras levé et l’autre '
     'tendu ; la jupe s’ouvre en corolle. À gauche un grand tambour sur pied, à '
     'droite la queue d’un piano.'),
    ('grand-rex-devant-la-lune', (480, 900, 1400, 2000), 1333, "MAGYE D'ART",
     'Iris Chasles devant la lune',
     'Photo en noir et blanc : Iris Chasles, micro-casque au visage et bras '
     'ouverts, se détache devant l’immense lune projetée sur l’écran du Grand '
     'Rex.'),
)

#: la meme valeur que les items de la galerie du dessus. Ecrite une fois.
SIZES_GAL = '(max-width:700px) calc(100vw - 52px), 485px'


def _item_rex(nom, largeurs, hauteur, qui, legende, alt):
    """Un `.gal-item` : la photo, sa legende, puis le credit du photographe."""
    def lot(ext):
        return ', '.join('/img/e-motion/%s-%d.%s %dw' % (nom, w, ext, w)
                         for w in largeurs)
    return (
        '    <div class="gal-item"><div class="gal-ph"><picture>'
        '<source type="image/webp" srcset="%s" sizes="%s">'
        '<img src="/img/e-motion/%s-900.jpg" srcset="%s" sizes="%s"'
        ' width="%d" height="%d" alt="%s" loading="lazy" decoding="async">'
        '</picture><span class="c">%s</span></div>'
        '<span class="cred">Crédit photo <a href="%s" target="_blank"'
        ' rel="noopener">%s</a></span></div>\n'
        % (lot('webp'), SIZES_GAL, nom, lot('jpg'), SIZES_GAL,
           largeurs[-1], hauteur, alt, legende, CRED_PHOTO[qui], qui))


# La mention est celle de David, mot pour mot, et elle est SEULE : c'est la
# legende de la section, pas une explication de texte.
SECTION_GRAND_REX = (
    '\n<section class="gal" id="grand-rex"><div class="wrap">\n'
    '  <div class="kick">Sur scène</div>\n'
    '  <h2 class="sec-title">Au Grand Rex</h2>\n'
    '  <p class="lead">Grand Rex, Paris — 2 700 personnes.</p>\n'
    '  <div class="gal-grid">\n'
    + ''.join(_item_rex(*p) for p in PHOTOS_REX)
    + '  </div>\n'
    '</div></section>\n')


# --------------------------------------------------------------------------- #
# LE GABARIT
#
# Il est ecrit en plusieurs litteraux ADJACENTS (Python les concatene) : cela
# permet de glisser les notes de redaction ENTRE eux, en commentaires `#`, juste
# au-dessus du bloc qu'elles expliquent. Elles ne partent donc pas dans la page
# publiee — le depot est public, et un commentaire HTML se lit avec « afficher
# le code source ». Voir `sources/verif_commentaires.py`.
#
# ⚠️ Le `<div class="links">` du gabarit est un PLACEHOLDER : `nav_menu.inject()`
# remplace ce bloc en entier par le menu partage. Ne pas y ajouter de liens, ils
# seraient perdus a la generation suivante.
# --------------------------------------------------------------------------- #

# L'IMAGE DE PARTAGE (16/08/2026) : la page l'avait deja, mais SANS ses
# dimensions — les seules des 30 pages a manquer. Elles sont ajoutees ici
# (mesurees sur le fichier), avec un `og:image:alt`.
# 🚩 A signaler a David : cette image est une AFFICHE VERTICALE (ratio 0,71).
#    Les apercus de partage attendent du paysage (~1,91:1) et rognent le reste
#    au petit bonheur — le titre de l'affiche peut disparaitre. Une version
#    paysage de l'affiche, ou une photo du spectacle, serait meilleure. On ne la
#    fabrique pas ici : le depot n'en contient aucune.
#
# ALIGNEMENT SUR SOLUNE (17/08/2026) — pourquoi le titre, le texte et l'image
# d'apercu de CETTE page ne sont plus ceux du reste du site.
# David tient un second site dedie au spectacle, `www.solune.show/le-spectacle`,
# et il migre progressivement vers Resonances. Il a demande que l'apercu partage
# (WhatsApp, Facebook, SMS) de `/e-motion` reprenne l'affiche et le texte de
# Solune, pour qu'un lien envoye depuis l'un ou l'autre site montre la meme
# chose. D'ou trois changements, tous CONFINES AU `<head>` — le contenu visible
# de la page n'a pas bouge d'un caractere :
#
# 1. UNE IMAGE D'APERCU DEDIEE, `apercu-partage-e-motion-1400.jpg`. C'est la
#    NOUVELLE affiche 2026, fabriquee a partir de l'export d'impression de David
#    (4961x7016) reduit a 1400x1980 en JPEG qualite 55 : 291 736 octets, sous la
#    barre des 300 Ko au-dela de laquelle WhatsApp renonce a charger l'apercu.
#    ⚠️ Fichier SEPARE, expres. `affiche-e-motion-*.jpg` reste l'ancienne
#    affiche et sert AILLEURS : c'est elle qui s'affiche DANS la page (bloc
#    `<picture>` de la section affiche, en 480/900/1400 + WebP). Remplacer ce
#    fichier-la aurait change la page visible, ce qui n'etait pas demande.
#    ⚠️ Pas de WebP pour l'apercu, et pas de declinaisons 480/900 : plusieurs
#    messageries ne rendent pas le WebP (le controle `partage` de verif_site.py
#    le refuse expres), et cette image ne sert qu'a l'apercu, jamais a
#    l'affichage responsive.
#
# 2. LE TITRE passe a celui de Solune, « E-Motion LE SPECTACLE PARTICIPATIF ».
#    🚩 A signaler a David : la mention « · ID duo » disparait de l'apercu. Le
#    nom du duo n'apparait donc plus dans la vignette de partage — il reste dans
#    le `<title>` de la page, dans `og:image:alt` et dans le contenu. Si le duo
#    doit rester visible au partage, c'est un arbitrage a rendre.
#
# 3. LE TEXTE reprend celui de Solune, avec deux reserves assumees :
#    - Solune ecrit « Envole toi vers l'inattendu ! » sans trait d'union. C'est
#      une faute ; Resonances ecrivait deja correctement « Envole-toi ». On garde
#      la forme correcte, on ne recopie pas la faute.
#    - le texte de Solune fait ~380 caracteres ; WhatsApp et Facebook coupent
#      vers 160-200. Recopie tel quel il finirait en « … » au milieu d'une
#      phrase. On garde donc les MOTS de David, dans son ordre, mais on ne
#      retient que ce qui tient avant la coupure : l'accroche, la phrase qui dit
#      l'essentiel du spectacle (le spectateur devient acteur) et la chute
#      « Une expérience immersive des sens » — qui etait deja le texte de
#      Resonances. La phrase du milieu (« La légèreté de la danse et la
#      puissance de la musique s'unissent aux pratiques corporelles, guidances
#      et chants… ») est celle qui aurait ete tronquee ; elle est deja dite en
#      entier dans le `<meta name="description">` juste au-dessus et dans le
#      corps de la page. Longueur retenue : 149 caracteres.
GABARIT = (
("""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>E-MOTION — Spectacle participatif · ID duo, Iris Chasles &amp; David Lesage</title>
<meta name="description" content="E-Motion, le spectacle immersif et participatif d’ID duo (Iris Chasles &amp; David Lesage) : danse aérienne à l’élastique, musique live, chant, pratiques corporelles et guidances. Une expérience immersive des sens où chaque spectateur devient acteur.">
<meta property="og:title" content="E-Motion LE SPECTACLE PARTICIPATIF">
<meta property="og:description" content="Envole-toi vers l'inattendu ! « Notre spectacle transforme chaque spectateur en acteur d'une expérience unique ! » Une expérience immersive des sens.">
<meta property="og:image" content="https://www.resonancesproductions.org/img/e-motion/apercu-partage-e-motion-1400.jpg">
<meta property="og:image:width" content="1400">
<meta property="og:image:height" content="1980">
<meta property="og:image:alt" content="Affiche 2026 du spectacle E-Motion — danse aérienne et musique live, par ID duo (Iris Chasles et David Lesage), avec l’accroche « Envole-toi vers l’inattendu ».">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="preload" as="image" type="image/webp" href="/img/e-motion/banniere-e-motion-1200.webp" fetchpriority="high">
<style>
:root{--night:#0e0f24;--ink:#eae7f3;--muted:#a9a6c4;--gold:#d8b25a;--gold2:#f0d18a;--plum:#8f7ad1;--card:#191b3d;--line:rgba(216,178,90,.26)}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--night);color:var(--ink);font-family:'Jost',-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.75;font-size:17px;-webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2,h3,.serif{font-family:'Cormorant Garamond',Georgia,serif}
.wrap{max-width:1040px;margin:0 auto;padding:0 26px}
.kick{letter-spacing:.34em;text-transform:uppercase;font-size:13px;font-weight:600;color:var(--gold);margin-bottom:14px}
section{padding:86px 0;position:relative}
.sec-title{font-size:clamp(30px,5vw,50px);font-weight:600;line-height:1.08;color:#fff}
.lead{font-size:19px;color:var(--muted);max-width:750px}
p.body{max-width:750px;color:#d7d4ea;margin-top:16px}
b{color:#fff;font-weight:500}
.divider{height:1px;background:linear-gradient(90deg,transparent,var(--line),transparent);margin:0 auto;max-width:1040px}
a{color:var(--gold2)}

/* NAV */
.nav{position:fixed;top:0;left:0;right:0;z-index:50;display:flex;align-items:center;justify-content:space-between;padding:11px 26px;background:rgba(14,15,36,.82);backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.06)}
.nav .brand{font-family:'Cormorant Garamond',serif;letter-spacing:.16em;text-transform:uppercase;font-size:15px;color:#fff;text-decoration:none;display:inline-block;padding:10px 0}
.nav .links{display:flex;gap:20px;align-items:center}
"""
# liens plus grands + zone tactile ~44 px + soulignement discret qui montre
# qu'ils sont cliquables
""".nav .links a{color:#cfcbe6;text-decoration:none;font-size:15.5px;display:inline-block;padding:9px 2px;
  border-bottom:1px solid rgba(216,178,90,.28)}
.nav .links a:hover{color:var(--gold2);border-bottom-color:var(--gold2)}
@media(max-width:700px){.nav .links a.hide-s{display:none}}

"""
# HERO — banniere graphique officielle affichee EN ENTIER (contain, pas cover).
# La bannière porte deja le titre, le sous-titre et les noms : on ne la met donc
# pas en fond derriere le texte (titre en double + illisible), et son format
# 1640x624 (2,63:1) serait massacre par un recadrage en cover sur mobile.
""".hero{display:block;text-align:center;padding:92px 0 58px;position:relative;overflow:hidden;
  background:radial-gradient(900px 460px at 50% 4%,rgba(147,116,226,.16),transparent 64%),var(--night)}
.hero .banner{width:100%;max-width:1640px;margin:0 auto}
.hero .banner img{width:100%;height:auto;display:block}
.hero .inner{position:relative;z-index:2;padding:34px 24px 0}
"""
# texte accessible mais masque visuellement (le visuel le porte deja)
""".sr-only{position:absolute!important;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;
  clip:rect(0 0 0 0);clip-path:inset(50%);white-space:nowrap;border:0}
.hero .kick{color:var(--gold2)}
.hero h1{font-size:clamp(56px,15vw,150px);font-weight:600;letter-spacing:.07em;color:#fff;line-height:.92;text-shadow:0 8px 50px rgba(0,0,0,.55)}
.hero .sub{font-size:clamp(18px,3.2vw,29px);font-style:italic;color:var(--gold2);margin-top:6px}
.hero .names{letter-spacing:.32em;text-transform:uppercase;font-size:13.5px;color:#e7e4f5;margin-top:24px;font-weight:500}
.hero .tag{max-width:620px;margin:26px auto 0;color:#efeaf6;font-style:italic;font-family:'Cormorant Garamond',serif;font-weight:500;font-size:23px;line-height:1.4}
.scroll{margin-top:44px;font-size:13px;letter-spacing:.3em;color:var(--muted);text-transform:uppercase}

.intention{background:radial-gradient(900px 500px at 88% -10%,rgba(147,116,226,.12),transparent 60%),var(--night)}
.big-quote{font-family:'Cormorant Garamond',serif;font-size:clamp(27px,4.2vw,42px);line-height:1.25;color:#fff;font-weight:500;max-width:880px}
.big-quote em{color:var(--gold2);font-style:italic}
.sig{margin-top:34px;color:var(--gold2);font-family:'Cormorant Garamond',serif;font-style:italic;font-size:24px;text-align:center}

.grid{display:grid;gap:18px;margin-top:42px;grid-template-columns:repeat(auto-fit,minmax(178px,1fr))}
.card{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:14px;padding:26px 24px;transition:transform .25s,border-color .25s}
.card:hover{transform:translateY(-4px);border-color:var(--line)}
.card .n{font-family:'Cormorant Garamond',serif;font-size:30px;color:var(--gold);line-height:1}
.card h3{font-size:21px;color:#fff;margin:10px 0 8px;font-weight:600}
.card p{color:var(--muted);font-size:14.5px}

.keystone{text-align:center;background:radial-gradient(800px 500px at 50% 50%,rgba(147,116,226,.18),transparent 65%),#0b0c1e}
.keystone .big-quote{margin:0 auto}

.artist{max-width:820px;margin:40px auto 0;padding:26px 0;border-top:1px solid rgba(255,255,255,.08);position:relative}
.artist h3{font-size:32px;color:#fff;font-weight:600}
.artist .role{color:var(--gold);font-size:13px;letter-spacing:.14em;text-transform:uppercase;margin:6px 0 12px;font-weight:600}
.artist p{color:#d3d0e8}
.aphoto{width:210px;border-radius:16px;border:1px solid var(--line);float:right;margin:2px 0 16px 28px}

.figure{margin-top:38px;border-radius:16px;overflow:hidden;border:1px solid var(--line)}
.figure img{width:100%;display:block}
.cap{color:var(--muted);font-size:13.5px;margin-top:10px;text-align:center;font-style:italic}
.figsec{padding:14px 0}

/* AFFICHE */
.affiche{background:linear-gradient(180deg,#0b0c1e,var(--night));text-align:center}
.affiche-wrap{margin-top:38px;display:flex;justify-content:center}
.affiche img{max-width:100%;width:auto;max-height:80vh;border-radius:14px;border:1px solid var(--line);box-shadow:0 20px 60px rgba(0,0,0,.55);display:block}

/* GALERIE danse aérienne */
.gal{background:linear-gradient(180deg,var(--night),#0b0c1e)}
.gal-grid{margin-top:40px;columns:2;column-gap:18px}
.gal-item{break-inside:avoid;margin-bottom:18px;position:relative;border-radius:13px;overflow:hidden;border:1px solid rgba(255,255,255,.08)}
.gal-item img{width:100%;height:auto;display:block}
"""
# .gal-ph = le cadre de la PHOTO seule. C'est lui qui porte position:relative,
# pour que la legende .c se cale en bas de l'image et non en bas de tout
# l'element : la bande de credit qui suit reste ainsi visible et cliquable.
""".gal-ph{position:relative;display:block}
.gal-item .cred{display:block;font-size:14.5px;color:var(--muted);padding:3px 12px 4px;text-align:center;
  background:rgba(0,0,0,.34);font-style:normal;position:relative;z-index:1}
.gal-item .cred a{display:inline-block;padding:10px 4px;font-size:15px;font-weight:500;color:var(--gold2);
  text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px}
.gal-item .cred a:hover{color:#fff;text-decoration-color:var(--gold2)}
.gal-item .c{position:absolute;left:0;right:0;bottom:0;background:linear-gradient(transparent,rgba(0,0,0,.8));color:#fff;font-size:13.5px;padding:26px 14px 11px;text-align:center;font-style:italic}
.credit{margin-top:22px;color:var(--muted);font-size:13px;font-style:italic;text-align:center}
@media(max-width:700px){.gal-grid{columns:1}}

.quotes{columns:2;column-gap:24px;margin-top:36px}
.q{break-inside:avoid;background:var(--card);border-left:3px solid var(--gold);border-radius:10px;padding:18px 22px;margin-bottom:20px;color:#e7e4f5;font-family:'Cormorant Garamond',serif;font-size:21px;font-style:italic;line-height:1.4}

.orga{background:#0b0c1e}
.two{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:34px}
.scene-card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:26px}
.scene-card h3{font-family:'Cormorant Garamond',serif;font-size:26px;color:var(--gold2);font-weight:600}
.scene-card p{color:var(--muted);margin-top:10px;font-size:15.5px}
.btnrow{display:flex;flex-wrap:wrap;gap:14px;margin-top:34px}
.btn{display:inline-block;background:var(--gold);color:#1a1608;padding:16px 34px;border-radius:30px;text-decoration:none;font-weight:600;font-size:16.5px;min-height:44px}
.btn.ghost{background:transparent;color:var(--gold2);border:1px solid var(--line)}

/* focus clavier visible (accessibilite) */
:focus-visible{outline:2px solid var(--gold2);outline-offset:2px;border-radius:4px}
footer{background:#08091a;padding:72px 0 60px;text-align:center;border-top:1px solid var(--line)}
"""
# zone tactile confortable (~44px) sur les liens du pied de page
"""footer a{display:inline-block;padding:13px 0;line-height:1.3}
footer a.btn,footer a.adh{padding:14px 30px}
footer h2{font-size:38px;color:#fff;font-weight:600}
.contacts{display:flex;flex-wrap:wrap;justify-content:center;gap:16px 44px;margin-top:26px}
.contacts .c b{color:var(--gold2);display:block;font-size:18px;font-family:'Cormorant Garamond',serif;font-weight:600}
.contacts .c span{color:var(--muted);font-size:16px;display:block}
"""
# coordonnees cliquables : plus grandes et clairement soulignees
""".contacts .c span a{font-size:16.5px;font-weight:500;color:var(--gold2);text-decoration:underline;
  text-decoration-thickness:1px;text-underline-offset:4px}
.contacts .c span a:hover{color:#fff}
.sign{margin-top:40px;color:var(--muted);font-style:italic;font-family:'Cormorant Garamond',serif;font-size:17px}

@media(max-width:760px){.quotes{columns:1}.two{grid-template-columns:1fr}section{padding:64px 0}.aphoto{float:none;width:62%;display:block;margin:0 auto 16px}}

/* teaser video */
.teaser{background:linear-gradient(180deg,#0b0c1e,var(--night));text-align:center}
.tz{margin-top:38px;max-width:900px;margin-left:auto;margin-right:auto;position:relative;border-radius:16px;overflow:hidden;border:1px solid var(--line);cursor:pointer;background:#000}
.tz img{width:100%;display:block;opacity:.62;transition:opacity .3s,transform .5s}
.tz:hover img{opacity:.8;transform:scale(1.02)}
.tz .play{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:88px;height:88px;border-radius:50%;background:rgba(216,178,90,.94);display:flex;align-items:center;justify-content:center;box-shadow:0 10px 40px rgba(0,0,0,.5);transition:transform .25s}
.tz:hover .play{transform:translate(-50%,-50%) scale(1.08)}
.tz .play::after{content:'';border-left:24px solid #14100a;border-top:15px solid transparent;border-bottom:15px solid transparent;margin-left:7px}
.lb{position:fixed;inset:0;background:rgba(6,7,18,.9);display:none;align-items:center;justify-content:center;z-index:200;padding:24px}
.lb.open{display:flex}
.lb-box{position:relative;width:min(980px,100%)}
.lb-frame{position:relative;padding-top:56.25%;border-radius:12px;overflow:hidden;border:1px solid var(--line);background:#000}
.lb-frame iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.lb-close{position:absolute;top:-48px;right:0;background:none;border:none;color:#fff;font-size:34px;line-height:1;cursor:pointer}
.yt-fallback{display:block;text-align:center;color:var(--gold2);font-size:15.5px;margin-top:10px;padding:10px 0;text-decoration:underline;text-underline-offset:4px}

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
# L'affiche est pilotee par sa hauteur (max-height:80vh). On reserve donc sa
# place sur le <picture> a partir de son rapport largeur/hauteur (--ar) :
# largeur = min(place disponible, 80vh x --ar), exactement la geometrie d'avant.
# Surtout pas de display:flex ici : l'image serait etiree en hauteur.
""".affiche picture{width:min(100%,calc(80vh * var(--ar,0.71)));margin:0 auto}
.affiche picture>img{width:100%;height:auto;max-width:100%;max-height:none}
"""
# L'ancienne photo de hero (hero-iris-et-david) n'est plus en fond ici :
# elle est desormais affichee dans la presentation des artistes, en <picture>.
)
# --------------------------------------------------------------------------
# LA COUCHE CHALEUREUSE (refonte du 15/08/2026)
# --------------------------------------------------------------------------
# « Ramener de la couleur prune, ca fait du bien. Resonances a besoin d'avoir
#   une image classe mais aussi chaleureuse. » — David, 15/08/2026.
# La partie commune vit dans `sources/theme_chaleur.py` ; elle est concatenee
# ici, EN FIN de feuille de style, pour surcharger sans rien reecrire.
# AUCUN TEXTE N'A BOUGE.
#
# ⚠️ ELLE ENTRE AVANT `</style>`, ET C'EST VOULU : `nav_menu.inject()` insere
#    SON css juste avant ce meme `</style>`, donc apres nous. Verifie : il ne
#    declare que des selecteurs de menu (`.nav …`, `.nm-*`), aucun de ceux
#    d'ici. Le menu garde sa pastille « Adherer » en or plein.
# ⚠️ PAS DE TITRE PEINT AU DEGRADE SUR CETTE PAGE : son `<h1>` est en
#    `sr-only` (le titre est incruste dans l'image de banniere) et les
#    `.sec-title` restent blancs, comme sur /le-soin-soa. Ce qui porte le
#    degrade, ce sont les sur-titres `.kick`, les filets et les puces.
+ theme_chaleur.CSS +
("""/* ===== E-Motion : declinaisons chaleureuses ===== */
"""
# les cartes des cinq elements : filet de tete au degrade, coins plus doux.
# Le filet est PEINT sur la bordure (background-image cadre sur `border-box`)
# plutot qu'ajoute en pseudo-element : `.card` s'anime deja au survol
# (`transform:translateY(-4px)`), un `::before` positionne s'y ajouterait mal,
# et la boite ne bouge ainsi pas d'un pixel.
""".card{border-top:3px solid transparent;border-radius:18px;background-image:var(--grad),linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,0)),linear-gradient(var(--card),var(--card));background-size:100% 3px,100% 100%,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box,padding-box}
.card:hover{border-color:transparent}
/* le grand chiffre de chaque carte, peint au degrade */
.card .n{display:inline-block;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
"""
# citations : le trait or plein de 3 px devient le degrade vertical
""".q{border-left-color:transparent;border-radius:14px;background-image:var(--grad-v),linear-gradient(var(--card),var(--card));background-size:3px 100%,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box}
"""
# les deux cartes « se programme en / s'inscrit dans » : filet de tete
""".scene-card{border-top:3px solid transparent;border-radius:18px;background-image:var(--grad),linear-gradient(var(--card),var(--card));background-size:100% 3px,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box}
"""
# la prune revient en accent de TEXTE (--plum2 : 7,3:1 sur --card)
""".artist .role{color:var(--plum2)}
"""
# le filet qui separe les deux artistes : degrade, comme le .divider
""".artist{border-top-color:transparent;background-image:linear-gradient(90deg,transparent,rgba(216,178,90,.42) 16%,rgba(238,128,98,.5) 50%,rgba(179,143,245,.42) 84%,transparent);background-repeat:no-repeat;background-size:100% 2px;background-position:0 0}
/* arrondis genereux, memes valeurs que sur /guso-facile */
.figure,.tz,.affiche img,.aphoto,picture.aphoto,.gal-item,.lb-frame{border-radius:18px}
"""
# la pastille de lecture du teaser : degrade chaud au lieu de l'or plein
""".tz .play{background:var(--grad-warm)}
""")
# --------------------------------------------------------------------------
# LA VISIONNEUSE PHOTO (17/08/2026) — la feuille de style
# --------------------------------------------------------------------------
# « Les photos ne sont pas cliquables. » — David. Il veut voir une photo en
# grand, zoomer dedans, et faire defiler les photos. Cette page a ete la
# premiere ; le 17/08/2026 la visionneuse est passee dans un module commun,
# `sources/visionneuse.py`, pour que les sept pages a photos du site en aient
# EXACTEMENT la meme. Toutes les explications de fond sont la-bas ; ici il ne
# reste que ce qui est propre a /e-motion.
#
# ⚠️ L'ARGUMENT `.gal-item .c` N'EST PAS COSMETIQUE. La legende des photos de
#    la galerie est en `position:absolute` PAR-DESSUS le bas de l'image : sans
#    la ligne `pointer-events:none` que cet argument produit, tout le bas de
#    chaque photo n'est pas cliquable. Mesure faite avant de l'ecrire.
+ visionneuse.css('.gal-item .c')
+ """
</style>
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="alternate icon" href="/favicon.ico" sizes="any">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <meta name="theme-color" content="#0e0f24">
  <meta property="og:url" content="https://www.resonancesproductions.org/e-motion">
  <meta name="twitter:card" content="summary_large_image">
</head>
<body>

<nav class="nav">
  <a class="brand" href="/">Résonances Productions</a>
  <div class="links">
    <a href="/">Accueil</a>
  </div>
</nav>

<header class="hero">
  <picture class="banner"><source type="image/webp" srcset="/img/e-motion/banniere-e-motion-800.webp 800w, /img/e-motion/banniere-e-motion-1200.webp 1200w, /img/e-motion/banniere-e-motion-1640.webp 1640w" sizes="100vw"><img src="/img/e-motion/banniere-e-motion-1200.jpg" srcset="/img/e-motion/banniere-e-motion-800.jpg 800w, /img/e-motion/banniere-e-motion-1200.jpg 1200w, /img/e-motion/banniere-e-motion-1640.jpg 1640w" sizes="100vw" width="1640" height="624" alt="E-MOTION — spectacle participatif de danse aérienne et musique live, avec David Lesage et Iris Chasles (SOLUNE présente)" loading="eager" fetchpriority="high" decoding="sync"></picture>
  <div class="inner">
    <div class="kick">ID duo — Spectacle immersif participatif</div>
"""

# --- en-tete de la page : le bloc `.inner` du <header> (h1 + sous-titre) ------
#
# Le titre et le sous-titre sont deja incrustes dans l'image de banniere
# au-dessus. On les garde dans le code — un <h1> unique, pour le referencement
# et les lecteurs d'ecran — mais masques visuellement (`sr-only`), pour ne pas
# les afficher deux fois.
"""    <h1 class="sr-only">E-MOTION</h1>
    <div class="sub sr-only">danse aérienne à l’élastique &amp; musique live</div>
    <div class="names">Iris Chasles · David Lesage</div>
    <div class="tag">Envole-toi vers l’inattendu !</div>
    <div class="scroll">Défiler ↓</div>
  </div>
</header>

<section class="intention"><div class="wrap">
  <div class="kick">L’intention</div>
  <div class="big-quote">Notre spectacle transforme chaque spectateur en <em>acteur d’une expérience unique</em>.</div>
  <p class="body">La légèreté de la <b>danse</b> et la puissance de la <b>musique</b> s’unissent aux <b>pratiques corporelles</b>, <b>guidances</b> et <b>chants</b> pour créer un moment inoubliable au sommet de l’<b>audace</b>.</p>
  <p class="body">Tu es invité·e en voyage dans l’univers immersif des <b>5 éléments</b>. Prépare-toi à être touché·e et à être acteur de propositions inclusives. Laisse-toi guider et embarque dans une expérience joyeuse, puissante et profonde.</p>
  <div class="sig">Envole-toi vers l’inattendu.</div>
</div></section>

<section class="teaser" id="teaser"><div class="wrap">
  <div class="kick">Le teaser</div>
  <h2 class="sec-title">Voir E-Motion en mouvement</h2>
  <p class="lead" style="margin:16px auto 0">Une minute pour saisir ce qui se joue sur scène.</p>
  <div class="tz" onclick="openYT('wjJ44RDENQM')" role="button" tabindex="0" aria-label="Lire le teaser du spectacle E-Motion">
    <picture><source type="image/webp" srcset="/img/e-motion/danse-aerienne-et-musique-live-sur-scene-480.webp 480w, /img/e-motion/danse-aerienne-et-musique-live-sur-scene-900.webp 900w, /img/e-motion/danse-aerienne-et-musique-live-sur-scene-1400.webp 1400w" sizes="(max-width:952px) calc(100vw - 52px), 900px"><img src="/img/e-motion/danse-aerienne-et-musique-live-sur-scene-900.jpg" srcset="/img/e-motion/danse-aerienne-et-musique-live-sur-scene-480.jpg 480w, /img/e-motion/danse-aerienne-et-musique-live-sur-scene-900.jpg 900w, /img/e-motion/danse-aerienne-et-musique-live-sur-scene-1400.jpg 1400w" sizes="(max-width:952px) calc(100vw - 52px), 900px" width="1400" height="783" alt="Teaser du spectacle E-Motion" loading="eager" decoding="async"></picture>
    <div class="play"></div>
  </div>
</div></section>

<section class="affiche"><div class="wrap">
  <div class="kick">L’affiche</div>
  <h2 class="sec-title">E-Motion</h2>
  <div class="affiche-wrap">
    <picture style="--ar:0.7071"><source type="image/webp" srcset="/img/e-motion/affiche-e-motion-480.webp 480w, /img/e-motion/affiche-e-motion-900.webp 900w, /img/e-motion/affiche-e-motion-1400.webp 1400w" sizes="(max-width:760px) calc(100vw - 52px), 620px"><img src="/img/e-motion/affiche-e-motion-900.jpg" srcset="/img/e-motion/affiche-e-motion-480.jpg 480w, /img/e-motion/affiche-e-motion-900.jpg 900w, /img/e-motion/affiche-e-motion-1400.jpg 1400w" sizes="(max-width:760px) calc(100vw - 52px), 620px" width="1400" height="1980" alt="Affiche du spectacle E-Motion" loading="lazy" decoding="async"></picture>
  </div>
</div></section>

<div class="divider"></div>

<section><div class="wrap">
  <div class="kick">L’expérience</div>
  <h2 class="sec-title">Ce qui compose le spectacle</h2>
  <p class="lead">Cinq langages se répondent sur scène — et le public y prend part.</p>
  <div class="grid">
    <div class="card"><div class="n">01</div><h3>Danse aérienne</h3><p>La danse aérienne à l’élastique (bungee dance) d’Iris Chasles : le corps suspendu, le monde à l’envers, la légèreté.</p></div>
    <div class="card"><div class="n">02</div><h3>Musique live</h3><p>L’univers de David Lesage : voix, handpan électronique, calebasse, Ngoni, wave drum et déclencheurs électroniques.</p></div>
    <div class="card"><div class="n">03</div><h3>Chant</h3><p>Le chant traverse le spectacle et devient collectif : le public trouve sa voix et la mêle à celle de la scène.</p></div>
    <div class="card"><div class="n">04</div><h3>Pratiques corporelles</h3><p>Respiration, mouvement, ancrage : des propositions simples et inclusives, accessibles à tous les corps.</p></div>
    <div class="card"><div class="n">05</div><h3>Guidances</h3><p>Des guidances inspirées du yoga, portées par la voix, qui ouvrent l’espace intérieur pendant la traversée.</p></div>
  </div>
</div></section>

<section class="gal"><div class="wrap">
  <div class="kick">Galerie</div>
  <h2 class="sec-title">La danse aérienne</h2>
  <p class="lead">Le corps suspendu à l’élastique — la signature visuelle d’E-Motion.</p>
"""

# --- la galerie et ses credits photo -----------------------------------------
#
# Quatre des photos portent le filigrane de MAGYE D'ART (magyedart.fr) : la
# mention est obligatoire, et elle a ete decouverte tardivement.
# La structure est VOLONTAIRE, ne pas la « simplifier » :
#     .gal-item  >  .gal-ph (la photo + sa legende `.c`)  +  .cred (le credit)
# `.gal-ph` porte `position:relative` pour que la legende se cale en bas de
# L'IMAGE et non en bas de tout l'element ; sans cela la bande de credit passait
# sous la legende, illisible et non cliquable.
"""  <div class="gal-grid">
    <div class="gal-item"><div class="gal-ph"><picture><source type="image/webp" srcset="/img/e-motion/danse-aerienne-et-musique-live-sur-scene-480.webp 480w, /img/e-motion/danse-aerienne-et-musique-live-sur-scene-900.webp 900w, /img/e-motion/danse-aerienne-et-musique-live-sur-scene-1400.webp 1400w" sizes="(max-width:700px) calc(100vw - 52px), 485px"><img src="/img/e-motion/danse-aerienne-et-musique-live-sur-scene-900.jpg" srcset="/img/e-motion/danse-aerienne-et-musique-live-sur-scene-480.jpg 480w, /img/e-motion/danse-aerienne-et-musique-live-sur-scene-900.jpg 900w, /img/e-motion/danse-aerienne-et-musique-live-sur-scene-1400.jpg 1400w" sizes="(max-width:700px) calc(100vw - 52px), 485px" width="1400" height="783" alt="Danse aérienne à l'élastique et musique live sur scène" loading="lazy" decoding="async"></picture><span class="c">Sur scène : la danse aérienne et la musique live se répondent</span></div></div>
    <div class="gal-item"><div class="gal-ph"><picture><source type="image/webp" srcset="/img/e-motion/suspendue-l-elastique-porte-le-mouvement-480.webp 480w, /img/e-motion/suspendue-l-elastique-porte-le-mouvement-900.webp 900w" sizes="(max-width:700px) calc(100vw - 52px), 485px"><img src="/img/e-motion/suspendue-l-elastique-porte-le-mouvement-900.jpg" srcset="/img/e-motion/suspendue-l-elastique-porte-le-mouvement-480.jpg 480w, /img/e-motion/suspendue-l-elastique-porte-le-mouvement-900.jpg 900w" sizes="(max-width:700px) calc(100vw - 52px), 485px" width="900" height="900" alt="Iris Chasles en danse aérienne à l'élastique" loading="lazy" decoding="async"></picture><span class="c">Suspendue — l’élastique porte le mouvement</span></div></div>
    <div class="gal-item"><div class="gal-ph"><picture><source type="image/webp" srcset="/img/e-motion/everness-festival-480.webp 480w, /img/e-motion/everness-festival-900.webp 900w" sizes="(max-width:700px) calc(100vw - 52px), 485px"><img src="/img/e-motion/everness-festival-900.jpg" srcset="/img/e-motion/everness-festival-480.jpg 480w, /img/e-motion/everness-festival-900.jpg 900w" sizes="(max-width:700px) calc(100vw - 52px), 485px" width="900" height="600" alt="Iris Chasles en danse aérienne à l’élastique, Everness Festival" loading="lazy" decoding="async"></picture><span class="c">Everness Festival</span></div></div>
    <div class="gal-item"><div class="gal-ph"><picture><source type="image/webp" srcset="/img/e-motion/l-envol-sous-les-arbres-480.webp 480w, /img/e-motion/l-envol-sous-les-arbres-900.webp 900w, /img/e-motion/l-envol-sous-les-arbres-1400.webp 1400w" sizes="(max-width:700px) calc(100vw - 52px), 485px"><img src="/img/e-motion/l-envol-sous-les-arbres-900.jpg" srcset="/img/e-motion/l-envol-sous-les-arbres-480.jpg 480w, /img/e-motion/l-envol-sous-les-arbres-900.jpg 900w, /img/e-motion/l-envol-sous-les-arbres-1400.jpg 1400w" sizes="(max-width:700px) calc(100vw - 52px), 485px" width="1400" height="1400" alt="Iris Chasles dans les airs avec la bungee dance, David Lesage à la musique" loading="lazy" decoding="async"></picture><span class="c">L’envol, sous les arbres</span></div></div>
    <div class="gal-item"><div class="gal-ph"><picture><source type="image/webp" srcset="/img/e-motion/la-danse-de-tournoiement-480.webp 480w, /img/e-motion/la-danse-de-tournoiement-900.webp 900w" sizes="(max-width:700px) calc(100vw - 52px), 485px"><img src="/img/e-motion/la-danse-de-tournoiement-900.jpg" srcset="/img/e-motion/la-danse-de-tournoiement-480.jpg 480w, /img/e-motion/la-danse-de-tournoiement-900.jpg 900w" sizes="(max-width:700px) calc(100vw - 52px), 485px" width="900" height="900" alt="Iris Chasles dans la danse de tournoiement, sur scène" loading="lazy" decoding="async"></picture><span class="c">La danse de tournoiement</span></div></div>
    <div class="gal-item"><div class="gal-ph"><picture><source type="image/webp" srcset="/img/e-motion/suspendue-bras-ouverts-480.webp 480w, /img/e-motion/suspendue-bras-ouverts-900.webp 900w, /img/e-motion/suspendue-bras-ouverts-1400.webp 1400w" sizes="(max-width:700px) calc(100vw - 52px), 485px"><img src="/img/e-motion/suspendue-bras-ouverts-900.jpg" srcset="/img/e-motion/suspendue-bras-ouverts-480.jpg 480w, /img/e-motion/suspendue-bras-ouverts-900.jpg 900w, /img/e-motion/suspendue-bras-ouverts-1400.jpg 1400w" sizes="(max-width:700px) calc(100vw - 52px), 485px" width="1400" height="914" alt="Iris Chasles suspendue à l'élastique, bras ouverts" loading="lazy" decoding="async"></picture><span class="c">Suspendue, bras ouverts</span></div><span class="cred">Crédit photo <a href="https://magyedart.fr/" target="_blank" rel="noopener">MAGYE D'ART</a></span></div>
    <div class="gal-item"><div class="gal-ph"><picture><source type="image/webp" srcset="/img/e-motion/l-elastique-en-noir-et-blanc-480.webp 480w, /img/e-motion/l-elastique-en-noir-et-blanc-900.webp 900w" sizes="(max-width:700px) calc(100vw - 52px), 485px"><img src="/img/e-motion/l-elastique-en-noir-et-blanc-900.jpg" srcset="/img/e-motion/l-elastique-en-noir-et-blanc-480.jpg 480w, /img/e-motion/l-elastique-en-noir-et-blanc-900.jpg 900w" sizes="(max-width:700px) calc(100vw - 52px), 485px" width="900" height="1321" alt="Iris Chasles en danse aérienne à l’élastique, en noir et blanc" loading="lazy" decoding="async"></picture><span class="c">L’élastique, en noir et blanc</span></div><span class="cred">Crédit photo <a href="https://magyedart.fr/" target="_blank" rel="noopener">MAGYE D'ART</a></span></div>
    <div class="gal-item"><div class="gal-ph"><picture><source type="image/webp" srcset="/img/e-motion/sur-grande-scene-480.webp 480w, /img/e-motion/sur-grande-scene-900.webp 900w, /img/e-motion/sur-grande-scene-1400.webp 1400w" sizes="(max-width:700px) calc(100vw - 52px), 485px"><img src="/img/e-motion/sur-grande-scene-900.jpg" srcset="/img/e-motion/sur-grande-scene-480.jpg 480w, /img/e-motion/sur-grande-scene-900.jpg 900w, /img/e-motion/sur-grande-scene-1400.jpg 1400w" sizes="(max-width:700px) calc(100vw - 52px), 485px" width="1400" height="916" alt="Iris Chasles en danse aérienne sur la grande scène du Grand Rex, à Paris" loading="lazy" decoding="async"></picture><span class="c">Sur grande scène</span></div><span class="cred">Crédit photo <a href="https://magyedart.fr/" target="_blank" rel="noopener">MAGYE D'ART</a></span></div>
    <div class="gal-item"><div class="gal-ph"><picture><source type="image/webp" srcset="/img/e-motion/le-ciel-en-toile-de-fond-480.webp 480w, /img/e-motion/le-ciel-en-toile-de-fond-900.webp 900w, /img/e-motion/le-ciel-en-toile-de-fond-1400.webp 1400w" sizes="(max-width:700px) calc(100vw - 52px), 485px"><img src="/img/e-motion/le-ciel-en-toile-de-fond-900.jpg" srcset="/img/e-motion/le-ciel-en-toile-de-fond-480.jpg 480w, /img/e-motion/le-ciel-en-toile-de-fond-900.jpg 900w, /img/e-motion/le-ciel-en-toile-de-fond-1400.jpg 1400w" sizes="(max-width:700px) calc(100vw - 52px), 485px" width="1400" height="885" alt="David Lesage et Iris Chasles face à face au Grand Rex, devant l’écran de ciel" loading="lazy" decoding="async"></picture><span class="c">Le ciel en toile de fond</span></div><span class="cred">Crédit photo <a href="https://magyedart.fr/" target="_blank" rel="noopener">MAGYE D'ART</a></span></div>
    <div class="gal-item"><div class="gal-ph"><picture><source type="image/webp" srcset="/img/e-motion/le-tournoiement-de-la-beaute-480.webp 480w, /img/e-motion/le-tournoiement-de-la-beaute-900.webp 900w" sizes="(max-width:700px) calc(100vw - 52px), 485px"><img src="/img/e-motion/le-tournoiement-de-la-beaute-900.jpg" srcset="/img/e-motion/le-tournoiement-de-la-beaute-480.jpg 480w, /img/e-motion/le-tournoiement-de-la-beaute-900.jpg 900w" sizes="(max-width:700px) calc(100vw - 52px), 485px" width="900" height="900" alt="Iris Chasles, danse de tournoiement" loading="lazy" decoding="async"></picture><span class="c">Le tournoiement de la beauté</span></div></div>
  </div>
  <p class="credit">Crédits photo : Magye d’Art Production et archives du duo.</p>
</div></section>
"""

# --- « Au Grand Rex » ---------------------------------------------------------
#
# POURQUOI ICI, et pas ailleurs. La page raconte, dans l'ordre : l'intention, le
# teaser, l'affiche, ce qui compose le spectacle, la galerie de la danse
# aerienne, le coeur du spectacle, les artistes, ce qu'en dit le public,
# programmer E-Motion.
# La serie du Grand Rex se pose JUSTE APRES la galerie et AVANT « le coeur du
# spectacle », pour trois raisons :
#  1. elle garde les photos ensemble — le regard ne fait qu'une seule traversee
#     d'images au lieu de deux separees par du texte ;
#  2. elle vient apres ce qui MONTRE le spectacle et avant ce qui l'AFFIRME
#     (« Une experience immersive des sens »), puis avant « Ce qu'en dit le
#     public » : la preuve d'echelle precede la promesse, puis les temoignages ;
#  3. un programmateur qui fait defiler la page voit la salle pleine avant
#     d'arriver au bloc « Programmer E-Motion », tout en bas.
# Elle n'est PAS fondue dans la galerie du dessus : celle-ci a son titre a elle,
# « La danse aerienne ». Deux sujets, deux sections.
+ SECTION_GRAND_REX + """
<section class="keystone"><div class="wrap">
  <div class="kick">Le cœur du spectacle</div>
  <div class="big-quote">Une expérience <em>immersive</em> des sens — où l’on ne reste pas assis.</div>
  <div class="sig">L’effet waouh est garanti.</div>
</div></section>

<div class="divider"></div>

<section><div class="wrap">
  <div class="kick">Les artistes</div>
  <h2 class="sec-title">ID duo — Iris &amp; David</h2>
  <p class="lead">« Nous sommes des artistes et artisans du monde dans lequel nous voulons vivre ! »</p>
  <p class="body">On ne veut <b>plus de doctrine</b>, on veut <b>une approche organique et joyeuse</b> avec un <b>cadre simple et contenant</b>. Iris fait de la danse aérienne (bungee dance) et David chante et joue de la musique. Nous avons créé un spectacle dans lequel nous invitons les spectateurs à faire l’expérience de ces trois piliers.</p>

  """

# --- presentation des artistes : la premiere `.figure` -----------------------
#
# C'est l'ancienne image de fond du hero (`hero-iris-et-david`), redescendue
# ici. Elle n'est donc plus le fond du hero : ne pas la reintroduire en haut.
"""<div class="figure"><picture><source type="image/webp" srcset="/img/e-motion/hero-iris-et-david-480.webp 480w, /img/e-motion/hero-iris-et-david-900.webp 900w, /img/e-motion/hero-iris-et-david-1400.webp 1400w" sizes="(max-width:1040px) calc(100vw - 52px), 988px"><img src="/img/e-motion/hero-iris-et-david-900.jpg" srcset="/img/e-motion/hero-iris-et-david-480.jpg 480w, /img/e-motion/hero-iris-et-david-900.jpg 900w, /img/e-motion/hero-iris-et-david-1400.jpg 1400w" sizes="(max-width:1040px) calc(100vw - 52px), 988px" width="1400" height="712" alt="Iris Chasles et David Lesage entourés de leurs instruments, au centre Élément, à Paris" loading="lazy" decoding="async"></picture></div>
  <div class="cap">Iris &amp; David — le duo et ses instruments</div>

  <div class="artist">
    <picture class="aphoto"><source type="image/webp" srcset="/img/e-motion/portrait-iris-chasles-480.webp 480w" sizes="(max-width:760px) 62vw, 210px"><img src="/img/e-motion/portrait-iris-chasles-480.jpg" srcset="/img/e-motion/portrait-iris-chasles-480.jpg 480w" sizes="(max-width:760px) 62vw, 210px" width="480" height="650" alt="Iris Chasles" loading="lazy" decoding="async"></picture>
    <h3>Iris Chasles</h3>
    <div class="role">Danseuse aérienne · Professeure de yoga</div>
    <p>Danseuse aérienne et professeure de yoga, Iris fait le lien entre Terre et Ciel. Dès l’âge de 8 ans, elle se passionne pour le cirque. Ce fut une école extraordinaire, où elle apprend le plaisir du beau mouvement, la pleine conscience du placement de son corps dans les airs, la confiance en elle et la découverte du monde à l’envers.</p>
    <p style="margin-top:12px">C’est tout naturellement que la danse aérienne à l’élastique apparaît dans sa vie alors qu’elle enseigne depuis des années le yoga. Et c’est sur scène que la danse aérienne et les guidances inspirées du yoga s’unissent harmonieusement.</p>
  </div>

  <div class="artist">
    <picture class="aphoto"><source type="image/webp" srcset="/img/e-motion/portrait-david-lesage-480.webp 480w, /img/e-motion/portrait-david-lesage-900.webp 900w" sizes="(max-width:760px) 62vw, 210px"><img src="/img/e-motion/portrait-david-lesage-900.jpg" srcset="/img/e-motion/portrait-david-lesage-480.jpg 480w, /img/e-motion/portrait-david-lesage-900.jpg 900w" sizes="(max-width:760px) 62vw, 210px" width="900" height="1350" alt="David Lesage" loading="lazy" decoding="async"></picture>
    <h3>David Lesage</h3>
    <div class="role">Voix · Musique live</div>
    <p>L’univers musical de David est un mélange de musique électronique et de musiques traditionnelles africaines : soul française, African spirit, électro vibes. La portée est un message clair, profond et qui vibre en chacun de nous.</p>
    <p style="margin-top:12px">Sous une humilité déconcertante, David Lesage présente avec excellence la grande technicité de son répertoire abouti ; rythmes envoûtants et envolées jazz d’une voix céleste. Entre voix, handpan électronique, calebasse, Ngoni, wave drum et déclencheurs électroniques. À découvrir en live absolument.</p>
  </div>
</div></section>

<section class="figsec"><div class="wrap">
  <div class="figure"><picture><source type="image/webp" srcset="/img/e-motion/iris-et-david-sziget-festival-480.webp 480w, /img/e-motion/iris-et-david-sziget-festival-900.webp 900w" sizes="(max-width:1040px) calc(100vw - 52px), 988px"><img src="/img/e-motion/iris-et-david-sziget-festival-900.jpg" srcset="/img/e-motion/iris-et-david-sziget-festival-480.jpg 480w, /img/e-motion/iris-et-david-sziget-festival-900.jpg 900w" sizes="(max-width:1040px) calc(100vw - 52px), 988px" width="900" height="1200" alt="Iris Chasles et David Lesage" loading="lazy" decoding="async"></picture></div>
  <div class="cap">Iris &amp; David — Sziget Festival</div>
</div></section>

<div class="divider"></div>

<section><div class="wrap">
  <div class="kick">Ils l’ont vécu</div>
  <h2 class="sec-title">Ce qu’en dit le public</h2>
  <div class="quotes">
    <div class="q">« Je suis repartie émerveillée, ressourcée. »</div>
    <div class="q">« J’ai vécu un moment de légèreté, d’amour, de joie, de partage — c’était vraiment un voyage magnifique ! »</div>
    <div class="q">« Beaucoup d’émotions m’ont traversé. Je n’ai jamais vécu cela auparavant. »</div>
    <div class="q">« Votre spectacle m’a rassuré et me donne espoir en l’AMOUR. »</div>
    <div class="q">« J’ai été en apesanteur comme jamais, spectacle inventif et tellement original. »</div>
    <div class="q">« Expérience incroyable, émerveillement et enchantement. »</div>
    <div class="q">« Un moment suspendu, magique, inattendu, porté par 2 êtres d’une beauté et bonté rares. »</div>
    <div class="q">« Spectacle à avoir absolument dans sa programmation tant il est original, novateur et bénéfique. Engagé, profond et surtout féerique ! »</div>
    <div class="q">« Et au final, tous debout, le visage rayonnant, applaudissant sans discontinuer ! »</div>
    <div class="q">« Spectacle très surprenant, on est transporté dans un autre monde. »</div>
    <div class="q">« J’ai vécu une expérience puissante. Mêlant plusieurs pratiques dont le chant, la danse et la respiration, ce spectacle est avant tout et surtout VIVANT ! J’en suis reparti nourri et apaisé, avec l’impression d’avoir fait cœur et corps avec les 300 personnes présentes. »</div>
    <div class="q">« On en ressort bouleversé et en même temps apaisé. »</div>
    <div class="q">« Il est ludique et joyeux. »</div>
  </div>
</div></section>

<div class="divider"></div>

<section class="orga" id="programmer"><div class="wrap">
  <div class="kick">Organisateurs &amp; programmateurs</div>
  <h2 class="sec-title">Programmer E-Motion</h2>
  <p class="lead">Un spectacle pensé pour les festivals, théâtres, salles et lieux immersifs — partout où l’on cherche à faire vivre au public autre chose qu’un fauteuil.</p>
  <div class="two">
    <div class="scene-card">
      <h3>Pour quels lieux</h3>
      <p>Festivals, théâtres, salles de spectacle, dojos et lieux immersifs. Le spectacle nécessite une hauteur sous plafond et un point d’accroche compatibles avec la danse aérienne à l’élastique.</p>
    </div>
    <div class="scene-card">
      <h3>Dossier &amp; fiche technique</h3>
      <p>Le dossier de présentation et la fiche technique complète sont transmis sur demande aux professionnels. Contactez-nous et nous vous les envoyons.</p>
    </div>
  </div>
  <div class="btnrow">
    <a class="btn" href="mailto:booking@solune.show?subject=Programmation%20du%20spectacle%20E-Motion">Demander le dossier</a>
  </div>
</div></section>

<footer><div class="wrap">
  <h2>Accueillir E-Motion</h2>
  <div class="contacts">
    <div class="c"><b>Booking</b><span><a href="mailto:booking@solune.show">booking@solune.show</a></span></div>
    <div class="c"><b>Téléphone</b><span><a href="tel:+33689054758">+33 6 89 05 47 58</a></span></div>
    <div class="c"><b>Association</b><span><a href="/">Résonances Productions</a></span></div>
  </div>
  <div class="sign">ID duo — Iris Chasles &amp; David Lesage</div>
</div></footer>


<div class="lb" id="ytlb" onclick="closeYT(event)">
  <div class="lb-box">
    <button class="lb-close" onclick="closeYT(event)" aria-label="Fermer">&times;</button>
    <div class="lb-frame"><iframe id="ytif" title="Teaser — Spectacle E-Motion" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe></div>
    <a class="yt-fallback" href="https://youtu.be/wjJ44RDENQM" target="_blank" rel="noopener">La vidéo ne se lance pas ? Ouvrir sur YouTube ↗</a>
  </div>
</div>
"""

# --- le lecteur video --------------------------------------------------------
#
# REGLE POSEE PAR DAVID, valable pour tout le site : une video se lit SUR le
# site, jamais dans un nouvel onglet ni dans l'application YouTube. D'ou ce
# lecteur en surimpression (`openYT()` / `#ytlb`), ferme par Echap ou par un
# clic hors du cadre, avec le `src` de l'iframe VIDE a la fermeture (sinon la
# video continue de jouer en arriere-plan).
# ⚠️ Cette page charge encore `www.youtube.com`. Le passage a
# `youtube-nocookie.com` est en cours de generalisation sur le site : quand il
# arrivera ici, il se fera DANS ce gabarit (une seule chaine a changer).
# Le lien `.yt-fallback` reste DANS le lecteur, discret : si l'iframe est
# bloquee (extension, reseau d'entreprise), le visiteur a une porte de sortie.
# Les liens de PLATEFORME (chaine YouTube, Spotify, billetterie) restent, eux,
# en nouvel onglet : ce n'est pas la meme chose.
"""<script>
function openYT(id){document.getElementById('ytif').src='https://www.youtube.com/embed/'+id+'?autoplay=1&rel=0&playsinline=1';document.getElementById('ytlb').classList.add('open');document.body.style.overflow='hidden';}
function closeYT(e){if(!e||e.target.id==='ytlb'||e.target.classList.contains('lb-close')){document.getElementById('ytlb').classList.remove('open');document.getElementById('ytif').src='';document.body.style.overflow='';}}
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeYT();});
document.querySelectorAll('.tz').forEach(function(t){t.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();openYT('wjJ44RDENQM');}});});
</script>
"""
# --- la visionneuse photo ----------------------------------------------------
#
# Le script vit dans `sources/visionneuse.py` — voir la-bas pour le detail
# (defilement natif accroche, butee aux extremites, zoom borne sur le cadre,
# piege a focus, verrou du corps de page). Ce qui est propre a /e-motion :
#
# CE QUI EST CLIQUABLE, ET POURQUOI PAS TOUT : les 27 photos de la page, dans
# leur ordre d'apparition (banniere, affiche, les 10 de la galerie, les 11 du
# Grand Rex, la photo du duo, les 2 portraits, Sziget). L'ordre est celui du
# DOCUMENT, pas celui du selecteur : `querySelectorAll` rend toujours les
# elements dans l'ordre de la page. La 28e balise <img> de la page est la vignette
# du TEASER : elle porte deja un clic, celui qui ouvre la video. Lui ajouter la
# visionneuse aurait mis deux actions sur un meme pixel. Son fichier est de
# toute facon le meme que la 1re photo de la galerie, deja dans la visionneuse.
+ visionneuse.js(
    '.hero .banner img, .affiche img, .gal-item img, .figure img, picture.aphoto img')
+ """</body></html>
""")


# --------------------------------------------------------------------------- #
# ASSEMBLAGE
# --------------------------------------------------------------------------- #

#: `mobile_nav.inject()` colle son CSS tout en fin de feuille de style. Dans la
#: page publiee il se trouve plus haut, juste apres les regles du lecteur video
#: et avant le bloc « images locales responsives ». On l'y remet, pour qu'une
#: regeneration ne deplace pas une ligne.
ANCRE_HAMBURGER = (
    '.yt-fallback{display:block;text-align:center;color:var(--gold2);'
    'font-size:15.5px;margin-top:10px;padding:10px 0;text-decoration:underline;'
    'text-underline-offset:4px}\n')


def build_html():
    """Le gabarit, plus le menu hamburger, plus le menu partage."""
    html = mobile_nav.inject(GABARIT)

    # remise en place du CSS du hamburger (voir ANCRE_HAMBURGER)
    if html.count(mobile_nav.CSS) != 1 or html.count(ANCRE_HAMBURGER) != 1:
        raise SystemExit('!! ABANDON : ancre du CSS du hamburger introuvable ou '
                         'en double. Page NON ecrite.')
    html = html.replace(mobile_nav.CSS, '', 1)
    html = html.replace(ANCRE_HAMBURGER, ANCRE_HAMBURGER + mobile_nav.CSS, 1)

    # Ligne vide entre le script du hamburger et le bloc du menu partage. Elle
    # vient de la mise a jour du menu v1 -> v2 : `nav_menu._strip()` a retire
    # l'ancien bloc en laissant le saut de ligne qui le suivait. Toutes les
    # pages publiees l'ont ; on la reproduit pour ne pas modifier un octet.
    html = html.replace('</script>\n</body>', '</script>\n\n</body>', 1)

    # menu de navigation partage : remplace le <div class="links"> du gabarit
    return nav_menu.inject(html, 'e-motion')


#: (marqueur, nombre attendu, ce que le marqueur protege). Meme parti-pris que
#: le garde-fou structurel de `generate_rythme.py` : refuser d'ecrire plutot
#: qu'avertir. Il attrape aussi bien la DISPARITION que la DUPLICATION — le
#: projet a deja produit quatre entrees de menu identiques par regenerations
#: successives.
GARDE_FOUS = (
    # version lue dans nav_menu : ce garde-fou ne doit pas devenir faux le
    # jour ou NAV_VERSION est incrementee.
    ('data-nav="%s"' % nav_menu.NAV_VERSION, 1, 'menu partage nav_menu.py'),
    ('.burger{', 3, 'CSS du menu hamburger'),
    ('<h1', 1, 'titre unique de la page'),
    # 10 pour la galerie « La danse aerienne » + 11 pour « Au Grand Rex ».
    ('class="gal-ph"', 21, 'cadres photo de la galerie'),
    # 4 dans la galerie du haut + 8 sur les onze photos du Grand Rex ; les 3
    # autres sont signees Nadine Court. Perdre un credit, c'est publier une
    # photo signee sans citer qui l'a prise.
    ('magyedart.fr', 12, "credits photo MAGYE D'ART"),
    ('kairos-photo-artisan.com', 3, 'credits photo Nadine Court'),
    ('id="grand-rex"', 1, 'section Grand Rex'),
    # DEUX occurrences depuis le 17/08/2026, et c'est voulu : la ligne de section
    # (« Grand Rex, Paris — 2 700 personnes. ») et la description de la premiere
    # photo, ou David a demande mot pour mot « la mise en mouvement de la
    # respiration de la joie de 2 700 personnes, guidee par Iris Chasles ». Le
    # garde-fou reste a un compte EXACT : si une troisieme apparait, c'est qu'on
    # a recopie la mention quelque part, et l'ecriture doit etre refusee.
    ('2 700 personnes', 2, 'la mention du Grand Rex'),
    ('id="ytlb"', 1, 'lecteur video en surimpression'),
    ('id="ytif"', 1, 'iframe du lecteur video'),
    # La visionneuse photo tient a DEUX choses : sa feuille de style et son
    # script. Perdre l'une des deux ne casserait rien a l'ecran — les photos
    # cesseraient simplement d'etre cliquables, en silence. D'ou ces deux
    # marqueurs. Le troisieme protege la ligne qui rend cliquable le BAS des
    # photos de la galerie (la legende passe par-dessus).
    ('.ph{position:fixed', 1, 'feuille de style de la visionneuse photo'),
    ("var SEL='.hero .banner img", 1, 'script de la visionneuse photo'),
    ('.gal-item .c{pointer-events:none}', 1, 'bas des photos de galerie cliquable'),
)


def main():
    html = build_html()

    for marqueur, attendu, role in GARDE_FOUS:
        n = html.count(marqueur)
        if n != attendu:
            raise SystemExit(
                '!! ABANDON : %d occurrence(s) de « %s » (%s), attendu %d. '
                'Page NON ecrite (le fichier sur disque est inchange).'
                % (n, marqueur, role, attendu))

    # Aucune note de redaction en commentaire HTML dans la page livree : elle
    # serait publique et indexable. Leur place est ci-dessus, en `#`.
    verif_commentaires.verifier(html, OUT_HTML)

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)
    print('[page]   %s  (%.1f Ko)' % (OUT_HTML, len(html.encode('utf-8')) / 1024))


if __name__ == '__main__':
    main()
