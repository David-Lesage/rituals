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
  - AUCUNE donnee absente des sources : pas de tarif de cachet (il n'y en a
    nulle part dans les sources), pas de jauge, pas d'effectif invente.
  - FICHE TECHNIQUE (ajoutee le 2026-08-04) : source = « Fiche technique et
    Artistique David Lesage artiste - International », presentation Drive de
    David (77 diapositives). CE QUI N'EST **PAS** PUBLIE, volontairement, et
    part uniquement dans le dossier envoye sur demande :
      * la valeur du materiel et le montant d'assurance demande -> publier
        « je voyage avec ~20 000 EUR de materiel » sur une page publique est
        une invitation au vol ;
      * le rider d'accueil (preferences alimentaires, hebergement, moustiquaire,
        ventilateur dans la chambre...) -> personnel, hors sujet ici ;
      * les dimensions de bagages avion et le detail du transport international
        -> trop operationnel.
    D'ou le bouton « Demander la fiche technique complete » (MAILTO_FT).
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

VIDEO (ajoutee le 04/08/2026) : la prestation The Voice s'ouvre dans un LECTEUR
EN SURIMPRESSION SUR LA PAGE. Consigne de David : « le but est que l'utilisateur
reste sur le site, et ce sur TOUTES les videos du site » -> plus AUCUN lien
sortant vers YouTube pour une video. Aucun script ni cookie tiers avant le clic.

IMAGES : aucune image distante servie par la page. On reutilise des declinaisons
deja presentes dans le depot (voir DLC_PHOTOS). La photo du Grand Rex porte le
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

HELLO_ASSO = ('https://www.helloasso.com/beta/associations/resonances-productions/'
              'adhesions/adhesion-resonances-productions')
MAIL = 'contact@resonancesproductions.org'
MAILTO_PROG = ('mailto:' + MAIL + '?subject=Programmation%20%E2%80%94%20David%20Lesage'
               '%20en%20concert')
MAILTO_DOSSIER = ('mailto:' + MAIL + '?subject=Dossier%20de%20pr%C3%A9sentation%20'
                  '%E2%80%94%20David%20Lesage%20en%20concert')
# Bouton de la section « Fiche technique » : le reste du rider (assurance, transport
# international, rider d'accueil) N'EST PAS publie -> il part sur demande.
MAILTO_ACOUSTIQUE = ('mailto:' + MAIL + '?subject=Version%20acoustique%20%E2%80%94%20'
                     'David%20Lesage%20en%20concert')
MAILTO_FT = ('mailto:' + MAIL + '?subject=Fiche%20technique%20compl%C3%A8te%20'
             '%E2%80%94%20David%20Lesage%20en%20concert')
TEL_TECH = '+33610733152'
TEL_TECH_TXT = '+33 6 10 73 31 52'
MAIL_TECH = 'contact@lesagedavid.fr'

# --- Video : LECTEUR EN SURIMPRESSION SUR LA PAGE ---------------------------
# Regle posee par David (04/08/2026) : « le but est que l'utilisateur reste sur le
# site, et ce sur TOUTES les videos du site » -> plus aucun lien sortant vers
# YouTube pour une video. La vignette est un BOUTON qui ouvre un lecteur dans la
# page. Aucun script tiers avant le clic : l'<iframe> nait sans src, la src n'est
# posee qu'au clic (domaine youtube-nocookie.com), puis VIDEE a la fermeture
# (sinon le son continue de jouer en fond).
# Titre verifie par oEmbed le 06/08/2026 (titre EXACT de la chaine).
# ATTENTION — erreur factuelle corrigee le 04/08 dans le HTML puis reportee ici :
# l'audition a l'aveugle de David Lesage n'est PAS « Une Âme » mais « Kothbiro »
# d'Ayub Ogada, et la captation officielle est sur la chaine TF1 de l'emission
# (seule video hors chaine de l'artiste sur cette page, assumee comme telle).
# `a831rQeGLRU` (« Une Ame 2 min The voice David Lesage ») est un autre upload,
# sur SA chaine : il sert desormais au titre « Une Âme » du repertoire.
VIDEO_TV_ID = '_v60Ow5_axY'
# Titre exact retourne par oEmbed (conserve en commentaire : le <iframe> du
# lecteur porte desormais un titre generique, il sert plusieurs videos) :
#   « Ayub Ogada - Kothbiro - David Lesage | The Voice 2022 | Blind Audition »
# Filet de securite UNIQUEMENT (iframe bloquee par une extension ou un navigateur
# restrictif) : il vit DANS le lecteur, en petit, et n'est jamais le chemin
# principal. Sans lui, la personne reste devant un cadre noir.
VIDEO_TV_SECOURS = f'https://youtu.be/{VIDEO_TV_ID}'
# Peniche Anako, Paris (ajout du 13/08/2026) : « Teaser Concert David Lesage —
# Extrait emission SuperPan Show de @JeremyNattagh ». Video publique, verifiee.
# Elle sert de PREUVE DE SCENE PARISIENNE dans la section « Scenes & festivals ».
# Meme mecanique que toutes les autres videos du site : .ytlink + data-yt ->
# lecteur en surimpression, youtube-nocookie, jamais de nouvel onglet.
# ⚠️ Le lieu (Peniche Anako) vient de David lui-meme, pas du titre de la video :
# ne pas le durcir en fait « source video » ailleurs sur le site.
VIDEO_ANAKO_ID = '0jbAjB-Swmk'
# Deux autres videos The Voice de la chaine, verifiees publiques et NON retenues
# pour ne pas surcharger la section parcours : WkZcBjZA_mU (« David Lesage
# #TheVoice Piano de Handpan #Griot Cathare ») et lewR2Fga2UM (« Kothbiro
# #TheVoice11 Intimiste Version David Lesage #Grio »).

# --- Ecouter / soutenir -----------------------------------------------------
# Liens de PLATEFORMES et de BOUTIQUE (pas des videos) : un nouvel onglet est ici
# legitime — la consigne « rester sur le site » ne concerne que les videos.
# ⚠️ CHAINE YOUTUBE — verifie le 04/08/2026, navigateur ET curl :
#   * @DavidLesageMusique  -> 404 Not Found. Ce handle N'EXISTE PAS. Ne pas le
#     remettre : c'etait un lien mort.
#   * youtube.com/c/DavidLesage -> 200, et declare lui-meme sa vanityChannelUrl :
#     @DavidLesageArtiste.
#   * @DavidLesageArtiste -> 200, « David Lesage », 340 videos, renvoie vers
#     lesagedavid.fr. C'est la chaine UCSQj4RNQCk6uwcs6agUvq-w, celle qui heberge
#     les deux videos utilisees sur le site (verifie par ownerProfileUrl).
# On retient donc le handle canonique @DavidLesageArtiste.
YT_CHAINE = 'https://www.youtube.com/@DavidLesageArtiste'
# URL nettoyee : « intl-fr » est une redirection regionale et « autoplay_ok=1 »
# un parametre de session — inutiles et fragiles dans un lien permanent.
SPOTIFY = 'https://open.spotify.com/artist/7zEAQJbalBFj8XNHrcqdbK'
# Boutique HelloAsso de l'association : l'album « L'Alliance du Phoenix ».
# ⚠️ AUCUN tarif sur la page (regle du site) : c'est la boutique qui les porte.
ALBUM_BOUTIQUE = ('https://www.helloasso.com/associations/resonances-productions/boutiques/'
                  'acheter-album-l-alliance-du-phoenix-david-lesage')

# --- Images reutilisees du depot -------------------------------------------
# cle : (dossier, base, [largeurs disponibles], largeur_intrinseque, hauteur)
DLC_PHOTOS = {
    # ⚠️ 'everness' N'EST PLUS UTILISEE sur cette page depuis le 14/08/2026 :
    # c'etait le hero, et David y est AVEC Iris. Il voulait une photo ou il est
    # SEUL -> le hero est passe a 'neotone-scene'. L'entree reste ici (la photo
    # existe toujours dans le depot et sert la galerie de /rituals) mais ne la
    # remettez pas en hero.
    'everness':   ('rituals',  'everness-festival-hongrie',                [480, 900, 1400], 1400, 667),
    'salle':      ('rituals',  'le-public-au-coeur-du-rituel',             [480, 900],        900, 501),
    'echo':       ('rituals',  'chanter-ensemble',                         [480, 900, 1400], 1400, 780),
    'proche':     ('rituals',  'une-connexion-forte-avec-le-public',       [480, 900, 1400], 1400, 786),
    'setup':      ('rituals',  'un-univers-musical-electro-organique',     [480, 900, 1400], 1400, 778),
    'portrait':   ('rituals',  'david-lesage',                             [480, 900, 1400], 1400, 1400),
    'rex':        ('rituals',  'au-grand-rex',                             [480, 900, 1400], 1400, 912),
    'aerien':     ('e-motion', 'danse-aerienne-et-musique-live-sur-scene', [480, 900, 1400], 1400, 783),
    'aerien-fest': ('e-motion', 'everness-festival',                       [480, 900],        900, 600),
    # PAS de photo du Sziget : la seule disponible dans le depot
    # (/img/e-motion/iris-et-david-sziget-festival-*) est un selfie personnel
    # d'Iris et David allonges dans l'herbe — rien de scenique. Le Sziget est
    # donc cite dans la liste des scenes, sans image.
    # --- /img/concert-scene/ : photos extraites de la fiche technique et artistique
    # (presentation Drive de David, 77 diapositives). Objectif : combler le manque
    # identifie par David — des photos ou il joue SEUL. Aucune n'est filigranee ;
    # verification faite bande haute + bande basse a pleine resolution.
    'solo-cymatique': ('concert-scene', 'david-lesage-seul-cymatique-projetee',  [480, 900, 1400], 1400, 795),
    'solo-festival':  ('concert-scene', 'david-lesage-seul-scene-de-festival',   [480, 900],        900, 600),
    'eglise':         ('concert-scene', 'concert-en-eglise-public-assis',        [480, 900, 1400], 1400, 933),
    'voix-machines':  ('concert-scene', 'david-lesage-voix-et-machines',         [480, 900, 1400], 1400, 940),
    'public-proche':  ('concert-scene', 'le-public-au-bord-du-plateau',          [480, 900, 1400], 1400, 933),
    'abbaye':         ('concert-scene', 'abbaye-a-ciel-ouvert-alet-les-bains',   [480, 900, 1400], 1400, 788),
    'plateau':        ('concert-scene', 'plateau-installe-avant-le-concert',     [480, 900, 1400], 1400, 1050),
    'setup-dessus':   ('concert-scene', 'le-setup-vu-du-dessus',                 [480, 900, 1400], 1400, 1050),
    'calebasse':      ('concert-scene', 'la-calebasse-et-les-bougies',           [480, 900, 1280], 1280, 1920),
    # --- The Voice (saison 11, 2021) : diapositives « Mise en contexte scenique
    # (The Voice 11) » de la meme presentation Drive. Publication TRANCHEE PAR
    # DAVID le 04/08/2026 (« pour les photos de TF1 je m'en fous, tu peux les
    # mettre ») malgre les logos The Voice / TF1 incrustes : ce sont des captures
    # de diffusion. Selection : les deux seules ou David est SEUL DANS LE CADRE.
    # Ecartees et disponibles si besoin : un plan large de David seul au centre du
    # plateau (bras leves, tres bleu, sujet minuscule), un plan d'ensemble des
    # quatre fauteuils, et quatre plans ou des tiers sont identifiables en gros
    # plan (deux coachs, l'animateur, un coach avec David) — a qualite egale,
    # moins de tiers dans l'image vaut mieux.
    'tv-calebasse':   ('concert-scene', 'the-voice-la-calebasse',                [480, 900, 1400], 1400, 874),
    'tv-ngoni':       ('concert-scene', 'the-voice-le-ngoni',                    [480, 900, 1400], 1400, 868),
    # Vignette de la video : c'est la vignette PUBLIEE PAR LA CHAINE pour cette
    # video (maxresdefault, 1280x720, sans bandes noires — sddefault est
    # letterboxee). Ne pas l'afficher au-dela de 1280 px.
    'tv-video':       ('concert-scene', 'the-voice-blind-audition',              [480, 900, 1280], 1280, 720),
    # --- Peniche Anako, Paris (ajout du 13/08/2026) : vignette PUBLIEE PAR LA
    # CHAINE pour la video 0jbAjB-Swmk (maxresdefault, 1280x720, vrai 16:9).
    # Rapatriee en local, jamais affichee au-dela de 1280 px. Elle porte les
    # incrustations de l'emission (« Concert David Lesage », « Extrait Superpan
    # Show Jeremy Nattagh ») : c'est la vignette d'origine, aucune signature de
    # photographe tiers, rien a crediter en plus du titre de l'emission, qui est
    # cite dans le sous-titre du bouton.
    'anako':          ('concert-scene', 'peniche-anako-teaser',                  [480, 900, 1280], 1280, 720),
    # --- SIX PHOTOS DEPOSEES PAR DAVID (14/08/2026) --------------------------
    # Toutes declinees en WebP + repli JPEG. Les largeurs listees ici sont
    # EXACTEMENT celles presentes dans le depot : ne jamais en inventer une, et
    # ne jamais afficher une image au-dela de sa resolution native.
    #
    # HERO de la page. Natif 6720x4480 : aucune contrainte de resolution, c'est
    # la seule photo solo de la page qui tienne en pleine largeur (1028 px) sur
    # un ecran a haute densite. Plan rapproche, yeux fermes, il chante, les deux
    # mains sur le Neotone (handpan electronique).
    # ⚠️ Elle montre le Neotone alors que la demande de David etait de REEQUILIBRER
    # vers les handpans acoustiques Yishama. L'equilibre est tenu ailleurs :
    # 'yishama-solo' ouvre desormais la section #acoustique, et 'ngoni' arrive
    # dans le parcours. Le hero, lui, est choisi sur la force de l'image (le
    # visage et la voix), pas sur l'instrument.
    'neotone-scene':  ('concert-scene', 'neotone-en-scene',            [480, 900, 1400, 2000, 2600], 2600, 1733),
    # Everness Festival 2023, Hongrie : David SEUL sur la grande scene, deux
    # handpans ACOUSTIQUES Yishama sur pieds. C'est l'argument visuel exact de la
    # section #acoustique, ou elle est placee.
    # ⚠️ PLAFONNEE A 900 px (natif 1024) : ne pas la mettre en pleine largeur.
    # Dans la grille .dlc-duo elle s'affiche a 504 px au plus — la seule place ou
    # elle reste nette. C'est pour ca qu'elle n'est PAS le hero.
    'yishama-solo':   ('concert-scene', 'everness-yishama-solo',       [480, 900],             900, 600),
    # Vue DEPUIS la scene, au grand angle : le plateau, la calebasse, une
    # violoncelliste, et le public nombreux assis sous les voiles d'ombrage.
    # Sert l'echelle, et la couleur acoustique (aucune machine dans le cadre).
    'vue-de-scene':   ('concert-scene', 'everness-vue-de-scene',       [480, 900, 1400, 2000], 2000, 1333),
    # ⚠️ ECART FACTUEL SIGNALE A DAVID : il a fourni cette photo comme « je donne
    # une indication vocale au public ». IL N'EST PAS DANS LE CADRE — on ne voit
    # que le public, vu du plateau. La legende ne dit donc rien de lui : elle
    # decrit ce qu'on voit et evoque l'echange vocal sans affirmer qu'on l'y voit.
    'public-echange': ('concert-scene', 'le-public-en-echange-vocal',  [480, 900, 1400, 2000], 2000, 1333),
    # N'Goni devant des neons rouges. ⚠️ SIGNEE « MAGYE D'ART Production » en bas
    # a droite -> credit obligatoire (CREDIT_MAGYE), comme les deux photos du
    # Grand Rex et les quatre de /e-motion.
    'ngoni':          ('concert-scene', 'ngoni-neons-rouges',          [480, 900, 1400, 2000], 2000, 1333),
    # Affiche officielle « EN CONCERT ». Format PORTRAIT (natif 3508x4961,
    # ratio 0,707) : elle passe en .dlc-portrait (420 px) et JAMAIS dans une
    # grille de photos de scene, dont elle casserait le rythme.
    # ⚠️ Elle porte deja le logo d'artiste : elle est donc placee en FIN de page
    # (section #programmer), loin du logo pose en tete du parcours.
    'affiche':        ('concert-scene', 'affiche-en-concert',          [480, 900, 1400, 2000], 2000, 2828),
    # --- PREMIERE PARTIE D'AMADOU & MARIAM, septembre 2022 (ajout 14/08/2026) --
    # C'est la reference la plus forte de la page et elle etait publiee sans
    # aucune image : ces deux photos la documentent enfin.
    # ⚠️ LE LIEU EST INCONNU. La source (Facebook) etait tronquee et David ne l'a
    # pas donne. N'ECRIRE AUCUN NOM DE SALLE, meme si la photo « ressemble a »
    # une salle connue. On s'en tient a « septembre 2022 ».
    # ⚠️ AMADOU & MARIAM NE SONT PAS DANS LE CADRE : ce sont deux images du set de
    # David. Ne jamais ecrire ni suggerer qu'on les y voit.
    # ⚠️ Aucune signature de photographe sur les deux (verifie) : aucun credit.
    #
    # Photo VERTICALE (natif 1080x2280, ratio 0,474 — plus verticale que tout ce
    # que porte le site). Plus grande variante : 900 px.
    # -> .dlc-tall la borne a 360 px : 360x2 = 720 device px, sous les 900 servis,
    # et 760 px de haut, ce qui reste tenable. NE PAS la recadrer en paysage, ne
    # pas l'etirer, ne pas la mettre dans .dlc-duo (elle y ferait 1 060 px de haut).
    'am-scene':       ('concert-scene', 'amadou-mariam-scene',         [480, 900],             900, 1900),
    # Plan large depuis le fond de la salle (natif 2242x1290). En .dlc-wide :
    # 860x2 = 1 720 device px, couverts par la variante 2000.
    'am-salle':       ('concert-scene', 'amadou-mariam-salle',         [480, 900, 1400, 2000], 2000, 1151),
    # --- LOGO D'ARTISTE DE DAVID LESAGE (ajout du 13/08/2026) ----------------
    # ⚠️ C'est le logo de L'ARTISTE, PAS celui de Resonances Productions. Il
    # identifie David Lesage sur SES pages (celle-ci et /concerts-david-lesage)
    # et ne doit JAMAIS remplacer le nom de l'association dans la barre de
    # navigation, ni servir de logo au site, ni de favicon.
    # Source : dossier Drive de David, 7 declinaisons PNG 3000x2120.
    # Declinaison retenue : « logo beige-etoilé » — lettres creme (#fbdaa6,
    # soit --gold2 a un cheveu pres), anneau dore, eclat en etoile. Comparees
    # sur le fond nuit #0e0f24 a la taille reelle d'affichage (360 px), c'est la
    # plus lisible de la famille doree : le « Logo Doré » perd son anneau dans le
    # fond, le « dégradé 2 » vire a l'orange sature, le blanc est propre mais
    # froid, le beige plat perd l'eclat, le noir est invisible.
    # Recadre sur son alpha (2578x1943) puis 480 et 900 px de large : jamais
    # agrandi (il est plafonne a 300 px d'affichage). PNG conserve en 24 bits
    # pour le repli : quantifie en 128 couleurs, l'eclat en etoile se casse en
    # facettes visibles.
    'logo':           ('logo',          'david-lesage-logo',                     [480, 900],        900, 678),
}

CREDIT_MAGYE = ('<span class="dlc-cred">Crédit photo <a href="https://magyedart.fr/" '
                'target="_blank" rel="noopener">MAGYE D’ART</a></span>')


def pic(key, alt, sizes, caption=None, cls='dlc-fig', loading='lazy', credit='',
        src_w=None):
    """<picture> WebP + repli JPEG, srcset complet, width/height, alt factuel.

    `src_w` : largeur du fichier mis dans l'attribut `src` (le repli des
    navigateurs sans `srcset`). Par defaut la plus grande variante. Utile quand
    la variante la plus grande est tres lourde et ne sert qu'aux ecrans a haute
    densite : le repli, lui, doit rester raisonnable.
    ⚠️ `width`/`height` restent ceux de la plus grande variante : ce sont des
    proportions (le CSS met `width:100%;height:auto`), pas une taille."""
    folder, base, widths, w, h = DLC_PHOTOS[key]
    root = f'/img/{folder}/{base}'
    webp = ', '.join(f'{root}-{x}.webp {x}w' for x in widths)
    jpg = ', '.join(f'{root}-{x}.jpg {x}w' for x in widths)
    big = f'{root}-{src_w or widths[-1]}.jpg'
    prio = ' fetchpriority="high"' if loading == 'eager' else ''
    img = (f'<picture><source type="image/webp" srcset="{webp}" sizes="{sizes}">'
           f'<img src="{big}" srcset="{jpg}" sizes="{sizes}" width="{w}" height="{h}" '
           f'loading="{loading}"{prio} decoding="async" alt="{alt}"></picture>')
    cap = f'<figcaption>{caption}{credit}</figcaption>' if caption else ''
    return f'<figure class="{cls}">{img}{cap}</figure>'


def logo_fig(cls='dlc-logo', sizes='300px'):
    """Logo d'artiste de David Lesage : WebP + repli PNG.

    PNG et pas JPEG : le logo est transparent, un repli JPEG lui collerait un
    fond blanc. Il n'est jamais affiche au-dela de 300 px (natif 2578 px de
    large avant reduction). `alt` = « David Lesage », c'est le texte du logo.
    ⚠️ Ce logo identifie L'ARTISTE, pas l'association : il n'a rien a faire
    dans la barre de navigation ni en logo de site."""
    folder, base, widths, w, h = DLC_PHOTOS['logo']
    root = f'/img/{folder}/{base}'
    webp = ', '.join(f'{root}-{x}.webp {x}w' for x in widths)
    png = ', '.join(f'{root}-{x}.png {x}w' for x in widths)
    return (f'<figure class="{cls}"><picture>'
            f'<source type="image/webp" srcset="{webp}" sizes="{sizes}">'
            f'<img src="{root}-{widths[-1]}.png" srcset="{png}" sizes="{sizes}" '
            f'width="{w}" height="{h}" loading="lazy" decoding="async" '
            f'alt="David Lesage"></picture></figure>')


def video_button(key, vid, alt, label, sub, sizes):
    """Vignette LOCALE + <button> qui ouvre le lecteur DANS LA PAGE.

    Ce n'est pas un lien : rien ne s'ouvre dans un nouvel onglet ni dans
    l'application YouTube. Tant que personne ne clique, aucune requete n'est
    faite vers un domaine tiers (l'<iframe> du lecteur nait sans src).
    Le triangle de lecture est purement CSS et aria-hidden : le libelle du
    bouton reste explicite pour les lecteurs d'ecran."""
    folder, base, widths, w, h = DLC_PHOTOS[key]
    root = f'/img/{folder}/{base}'
    webp = ', '.join(f'{root}-{x}.webp {x}w' for x in widths)
    jpg = ', '.join(f'{root}-{x}.jpg {x}w' for x in widths)
    img = (f'<picture><source type="image/webp" srcset="{webp}" sizes="{sizes}">'
           f'<img src="{root}-{widths[-1]}.jpg" srcset="{jpg}" sizes="{sizes}" '
           f'width="{w}" height="{h}" loading="lazy" decoding="async" alt="{alt}"></picture>')
    return (f'<button type="button" class="dlc-video ytlink" data-yt="{vid}">'
            f'<figure class="dlc-fig"><span class="shot">{img}'
            f'<span class="play" aria-hidden="true"></span></span>'
            f'<figcaption><span class="vlabel">{label}</span>'
            f'<span class="vsub">{sub}</span></figcaption></figure></button>')


# --- Lecteur video en surimpression -----------------------------------------
# Composant repris de /rituals, avec trois ameliorations : (1) domaine
# youtube-nocookie.com ; (2) fermeture au clavier par Echap + focus deplace sur
# le bouton de fermeture a l'ouverture et RESTITUE au declencheur a la fermeture,
# avec role="dialog" et aria-modal="true" ; (3) title de l'iframe = le vrai titre
# de la video. La classe d'ouverture est « open » — la meme dans le CSS et dans
# le JS (verifie : aucune incoherence .on/.open a reproduire).
LIGHTBOX_CSS = """
/* ===== Lecteur video en surimpression (la video reste SUR le site) ===== */
.lb{position:fixed;inset:0;background:rgba(6,7,18,.92);display:none;align-items:center;justify-content:center;z-index:1200;padding:24px}
.lb.open{display:flex}
.lb-box{position:relative;width:min(980px,100%)}
.lb-frame{position:relative;padding-top:56.25%;border-radius:12px;overflow:hidden;border:1px solid var(--line);background:#000}
.lb-frame iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.lb-close{position:absolute;top:-52px;right:0;background:none;border:none;color:#fff;font-size:34px;line-height:1;cursor:pointer;width:44px;height:44px;display:flex;align-items:center;justify-content:center}
.yt-fallback{display:block;text-align:center;color:var(--gold2);font-size:13px;margin-top:12px;text-decoration:underline}
body.lb-open{overflow:hidden}
@media print{.lb{display:none!important}}
/* ===== Vignette video : BOUTON qui ouvre le lecteur DANS LA PAGE =====
   C'est un <button> et non un lien : on remet a plat les styles par defaut du
   navigateur, sinon il herite d'un fond gris et d'un cadre. La source fait
   1280 px de large : on la borne a 560 px, largement en dessous. */
.dlc-video{display:block;max-width:560px;width:100%;margin-top:26px;background:none;border:0;padding:0;color:inherit;font:inherit;text-align:left;cursor:pointer}
.dlc-video figure{margin:0}
.dlc-video .shot{display:block;position:relative;line-height:0}
.dlc-video .play{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:62px;height:62px;border-radius:50%;background:rgba(11,12,30,.72);border:1px solid rgba(240,209,138,.62);display:flex;align-items:center;justify-content:center;transition:transform .2s,background .2s}
.dlc-video .play::before{content:"";width:0;height:0;border-left:17px solid var(--gold2);border-top:11px solid transparent;border-bottom:11px solid transparent;margin-left:5px}
.dlc-video:hover .play{background:rgba(11,12,30,.9);transform:translate(-50%,-50%) scale(1.06)}
.dlc-video figcaption{display:flex;flex-direction:column;gap:2px;justify-content:center;min-height:44px}
.dlc-video .vlabel{color:var(--gold2);font-size:16px;text-decoration:underline;text-decoration-color:rgba(216,178,90,.42);text-underline-offset:3px}
.dlc-video:hover .vlabel{color:#fff}
.dlc-video .vsub{color:var(--muted);font-size:13.5px}
/* ===== bloc « Ecouter · Soutenir » (plateformes + boutique de l'association) ==
   Sobre a dessein : trois boutons fantomes, pour ne pas concurrencer les deux
   seuls appels a l'action de cette page (« Programmer ce concert » / « Demander
   le dossier »). Sous 560 px les boutons passent en pleine largeur. */
.dlc-listen{margin-top:36px;max-width:860px;border-top:1px solid var(--line);padding-top:26px}
.dlc-listen p{max-width:none;font-size:16px}
.dlc-listen .cta{margin-top:20px}
.dlc-listen .btn{font-size:15px;padding:12px 22px}
@media(max-width:560px){.dlc-listen .btn{width:100%}}
/* ===== Grille de vignettes live (chaque vignette ouvre le lecteur DANS la page)
   Les vignettes sont natives en 1280x720 : la grille plafonne les colonnes bien
   en dessous, on ne les agrandit donc jamais au-dela de leur resolution.
   .lvc est un <button> : on remet a plat les styles par defaut du navigateur.
   Hauteur cliquable = vignette (>= 135 px) + libelle : cible tactile largement
   au-dela de 44 px. */
.lvg{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:20px;margin-top:24px;max-width:1028px}
.lvc{display:flex;flex-direction:column;gap:0;background:var(--card);border:1px solid var(--line);
  border-radius:14px;overflow:hidden;padding:0;color:inherit;font:inherit;text-align:left;
  cursor:pointer;transition:transform .2s,box-shadow .2s,border-color .2s}
.lvc:hover,.lvc:focus-visible{transform:translateY(-3px);border-color:rgba(216,178,90,.6);box-shadow:0 14px 34px rgba(0,0,0,.45)}
.lvc .shot{display:block;position:relative;line-height:0;aspect-ratio:16/9;overflow:hidden}
.lvc .shot img{display:block;width:100%;height:100%;object-fit:cover}
.lvc .play{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:52px;height:52px;
  border-radius:50%;background:rgba(11,12,30,.7);border:1px solid rgba(240,209,138,.62);
  display:flex;align-items:center;justify-content:center;transition:transform .2s,background .2s}
.lvc .play::before{content:"";width:0;height:0;border-left:15px solid var(--gold2);
  border-top:10px solid transparent;border-bottom:10px solid transparent;margin-left:4px}
.lvc:hover .play,.lvc:focus-visible .play{background:rgba(11,12,30,.9);transform:translate(-50%,-50%) scale(1.08)}
.lvc-t{display:flex;align-items:center;min-height:44px;padding:11px 15px 13px;color:var(--gold2);
  font-size:15px;line-height:1.35;text-decoration:underline;
  text-decoration-color:rgba(216,178,90,.4);text-underline-offset:3px}
.lvc:hover .lvc-t{color:#fff}
.lv-set{margin-top:34px}
.lv-set:first-of-type{margin-top:0}
.lv-set h3{font-family:'Cormorant Garamond',Georgia,serif;font-size:26px;color:#fff;font-weight:600;line-height:1.15}
.lv-set .lv-src{color:var(--muted);font-size:14px;font-style:italic;margin-top:4px}
/* ===== Lecteur Spotify differé (cree au clic, jamais au chargement) ===== */
.spf{margin-top:24px;max-width:820px}
.spf iframe{display:block;width:100%;border:0;border-radius:12px;background:var(--card)}
.dlc-block .spf-note{color:var(--muted);font-size:14px;font-style:italic;margin-top:12px;max-width:640px}
"""

LIGHTBOX_HTML = """
<div class="lb" id="ytlb" role="dialog" aria-modal="true" aria-label="Lecteur vidéo" onclick="closeYT(event)">
  <div class="lb-box">
    <button class="lb-close" type="button" onclick="closeYT(event)" aria-label="Fermer la vidéo">×</button>
    <div class="lb-frame"><!-- Le lecteur sert TOUS les declencheurs de la page (vignettes
         ET titres du repertoire) : son titre doit rester generique. -->
      <iframe id="ytif" title="Lecteur vidéo YouTube" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe></div>
    <a class="yt-fallback" href="{secours}" target="_blank" rel="noopener">La vidéo ne se lance pas ? Ouvrir sur YouTube ↗</a>
  </div>
</div>
"""

LIGHTBOX_JS = """
<script>
(function(){
  var lb=document.getElementById('ytlb'); if(!lb) return;
  var fr=document.getElementById('ytif'); if(!fr) return;
  var closeBtn=lb.querySelector('.lb-close'), back=null;
  window.openYT=function(id,trigger){
    back=trigger||document.activeElement;
    /* youtube-nocookie : moins de traceurs. La src n'existe qu'a partir d'ici. */
    fr.src='https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0&playsinline=1';
    var fb=lb.querySelector('.yt-fallback'); if(fb) fb.href='https://youtu.be/'+id;
    lb.classList.add('open');
    document.body.classList.add('lb-open');
    if(closeBtn) closeBtn.focus();
  };
  window.closeYT=function(e){
    /* On ne ferme que sur le fond ou sur la croix : un clic sur le lien de
       secours ou dans le cadre ne doit pas fermer le lecteur. */
    if(e && e.target!==lb && !(e.target.closest && e.target.closest('.lb-close'))) return;
    if(!lb.classList.contains('open')) return;
    lb.classList.remove('open');
    document.body.classList.remove('lb-open');
    fr.src='';  /* IMPERATIF : sinon la video continue de jouer en fond. */
    /* Restitution du focus au declencheur. Double appel volontaire : quand le
       lecteur YouTube avait pris le focus, Chrome remet activeElement sur <body>
       APRES la destruction de l'iframe et ecrasait un focus synchrone. */
    if(back && back.focus){ var b=back; b.focus(); setTimeout(function(){ try{ b.focus(); }catch(_){} },0); }
    back=null;
  };
  document.addEventListener('click',function(e){
    var t=e.target.closest && e.target.closest('.ytlink');
    if(t){ e.preventDefault(); openYT(t.getAttribute('data-yt'), t); }
  });
  document.addEventListener('keydown',function(e){
    if(e.key==='Escape' && lb.classList.contains('open')) closeYT();
  });
})();
</script>
"""


# --- Contenu ---------------------------------------------------------------
FICHE = [
    ('Format', 'Concert · Cérémonie · Participatif'),
    ('Durée', '1 h 30'),
    ('Instruments', 'Voix, handpan électronique, 2 à 3 handpans acoustiques, calebasse, '
                    'N’Goni 14 cordes (harpe africaine), Wavedrum, sanzula, déclencheurs '
                    'électroniques et loop station'),
    ('Accordage', 'Tous les instruments sont accordés en <b>La 432 Hz</b>'),
    ('Langues', 'Français, swahili, sanskrit'),
    ('Esthétique', 'Soul française · African spirit · Électro vibes'),
    ('Dispositif', 'Vidéoprojections · cymatique en temps réel · ambiances sonores · '
                   'échanges vocaux avec la salle'),
    ('Plateau', 'Minimum 4 m × 5 m, plat et de niveau · configuration de référence à '
                '<b>9 entrées</b> — voir la <a href="#technique">fiche technique</a>'),
    ('En option', 'Danse aérienne à l’élastique — Iris Chasles · extraits du spectacle '
                  '<a href="/e-motion">E-Motion</a>'),
    # Formule acoustique : voir la section #acoustique et son avertissement.
    # AUCUNE donnee chiffree ici — rien n'est arrete sur cette formule.
    ('Autre formule', 'Une <a href="#acoustique">version plus acoustique</a> du même '
                      'répertoire, portée surtout par les handpans acoustiques Yishama, '
                      'la voix, la calebasse et le N’Goni — sur demande'),
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
    # NUANCE IMPORTANTE, corrigee le 2026-08-04 : la fiche technique de David dit
    # « prix de batterie mention tres bien APRES UN COURT PASSAGE au Conservatoire
    # National de Toulouse ». La page laissait entendre un cursus complet.
    ('Conservatoire National de Toulouse',
     'Un court passage, et un prix de batterie mention très bien.'),
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

# ============================================================================
# « LA OU CE REPERTOIRE A RESONNE » — refonte du 13/08/2026
# ============================================================================
# Demande de David : « il manque plein de lieux et de dates. L'idee c'est de
# montrer que J'AI FAIT PLEIN DE CONCERTS et de mettre en avant les meilleurs
# lieux, festivals et lieux epiques. »
#
# SOURCES (collecte faite et verifiee en amont, hors de ce script) :
#   (A) agenda Google « CONCERTS David Lesage Artiste » (2022 -> 2026)
#   (B) page Facebook artiste, onglet « evenements passes » (2016 -> 2025)
#   (C) dossier de presentation scenique + fiche technique
#   (D) titres de videos publiques de sa chaine
#
# ⚠️ REGLES ABSOLUES POUR CETTE SECTION :
#   * AUCUNE date, AUCUN lieu, AUCUN chiffre de frequentation invente. Tout ce
#     qui est ecrit ici est recopie des sources ci-dessus.
#   * Le SEUL chiffre de public autorise est « 2 700 personnes au Grand Rex »
#     (confirme par David). Aucune autre jauge nulle part.
#   * « recensees » et pas un total absolu : les deux agendas ne couvrent pas
#     tout (2018 n'a qu'une date, 2020 deux — c'est la source qui est trouee,
#     pas la carriere). Ne JAMAIS arrondir a la hausse.
#   * PREMIERE PARTIE D'AMADOU & MARIAM : le lieu est TRONQUE dans la source
#     (il commence par « S »). On publie la reference SANS lieu. Ne pas
#     l'inventer — a faire confirmer par David.
#   * JAZZ IN MARCIAC est DEUX choses distinctes et toutes les deux vraies :
#     (1) le festival ou il a joue en 2018 et 2019 avec le groupe « Resonance »
#         -> c'est ici, dans les references de scene ;
#     (2) le COLLEGE de Jazz in Marciac, ou il s'est forme -> c'est dans
#         REPERES, section « Le parcours ». Ne pas melanger les deux.
#
# DECOMPTE (recalcule a la main a partir de CHRONO ci-dessous, verifie par
# assertion a la fin du fichier) : 69 dates datees, de 2016 a 2025, sur dix
# annees consecutives. S'y ajoutent DEUX concerts majeurs dont la date
# n'apparait dans aucun des deux agendas : le Grand Rex et le Mont Korhogo.
# PAYS avec au moins un concert date : France, Hongrie, Suisse, Belgique,
# Grece, Cote d'Ivoire = 6. (L'Espagne n'y est PAS : la chapelle du Mas Galifa
# ne nous est connue que par une video de sa chaine, sans date ni preuve de
# concert public -> elle figure dans les lieux de pierre avec cette reserve
# explicite, et n'entre pas dans le compte des pays.)
SCENES_STATS = [
    ('69', 'dates recensées, de 2016 à 2025 — dix années consécutives'),
    ('6', 'pays : France, Hongrie, Suisse, Belgique, Grèce, Côte d’Ivoire'),
    ('2 700', 'personnes au Grand Rex, à Paris'),
]

# Les references majeures, en evidence. Ordre : la plus vendeuse d'abord.
SCENES_REFS = [
    ('Première partie d’Amadou &amp; Mariam',
     'Septembre 2022'),
    ('Sziget Festival',
     'Budapest, Hongrie — août 2023'),
    ('Everness Festival',
     'Hongrie — juin 2023, puis Everness Indian Summer en septembre 2024'),
    ('Jazz in Marciac',
     'Août 2018 et août 2019, avec le groupe « Résonance »'),
    ('Le Grand Rex',
     'Paris — devant 2 700 personnes, avec le duo Solune'),
    ('The Voice, saison 11',
     'TF1 — audition à l’aveugle, seul avec ses instruments'),
    ('Mont Korhogo',
     'Côte d’Ivoire — concert solo, à l’invitation qui a suivi l’émission'),
    ('Hona Festival',
     'Naxos, Grèce — mai 2022'),
    ('HUG Fesztivál',
     'Hongrie — Hungarian Handpan &amp; Worldmusic Gathering, juillet 2022 et juillet 2023'),
]

# Deuxieme rideau : festivals, salles et theatres. Format « nom | precision ».
SCENES_LIEUX = [
    ('Castle Handpan Festival', 'Château de Frasne-le-Château — mai 2024'),
    ('Tribe Unity Festival', 'Belgique — juin 2025, avec Solune'),
    ('HangAout Festival', 'Domaine du Balbuzard — juin 2021'),
    ('Festival Été Nomade', 'Port Dienville, base nautique — juin 2024'),
    ('Salle del Castillo', 'Vevey, Suisse — février 2023'),
    ('Théâtre OZ', 'Martigny, Suisse — mars 2023'),
    ('Théâtre de l’Étang', 'Septembre 2023 — conférence, film et concert avec Arnaud Riou'),
    ('Péniche Anako', 'Paris — mars 2023'),
    ('Salle San-Subra', 'Toulouse — mai 2022'),
    ('Le Centre Élément', 'Paris — avril 2023, puis mars 2024'),
    ('Festival Arts Extatics', 'Puivert — juillet 2023'),
    ('Festival Arts Terre Sacrée', 'Rennes-les-Bains — août 2024'),
]

# Les lieux de pierre — l'argument exact de la version acoustique (# acoustique).
SCENES_PIERRE = [
    ('Abbaye d’Alet-les-Bains', 'À ciel ouvert — septembre 2022, puis août 2025 sous les étoiles'),
    ('Cloître de Saint-Geniez-d’Olt', 'Juillet 2022'),
    ('Basilique Saint-Nazaire, Carcassonne', 'Août 2017 — en trio, voix et instruments du monde'),
    ('Église Saint-Nazaire, Carcassonne', 'Juin et septembre 2017'),
    ('Église Saint-Jean-l’Évangéliste, Tourcoing', 'Septembre 2023'),
    ('Chapelle du Mas Galifa', 'Espagne — connue par une vidéo de sa chaîne, visible plus haut'),
]

# Chronologie complete, repliee dans un <details> natif (aucun JavaScript).
# Chaque ligne est recopiee des sources. Les libelles flous le restent : on
# n'ajoute pas une ville ou une salle que la source ne donne pas.
# SEULE normalisation faite : la source ecrit « Jedapama » (2024, 2025) ET
# « Jédapama » (2016, 2020) pour le MEME projet. Les deux graphies cote a cote
# dans une meme liste font negligent -> tout en « Jedapama » (graphie recente et
# majoritaire). A faire confirmer par David si l'accent est le bon.
SCENES_CHRONO = [
    ('2025', [
        ('13 juin', 'Jedapama, Le Bosc'),
        ('21 juin', 'Concert Solune, Tribe Unity Festival, Belgique'),
        ('5 juillet', 'Spectacle E-Motion, Le Dojo d’Espéraza'),
        ('18 juillet', 'Jedapama, lac de la Cavayère, Carcassonne'),
        ('16 août', 'Abbaye d’Alet-les-Bains — « une abbaye à ciel ouvert, sous les étoiles »'),
        ('27 septembre', 'Jedapama, festival de conte, Rennes-le-Château'),
        ('7 novembre', '« Concert pour l’eau », Jedapama, Alet'),
    ]),
    ('2024', [
        ('30 mars', 'E-Motion, Le Centre Élément, Paris'),
        ('26 avril', 'Festival Au cœur de l’homme'),
        ('24 mai', 'Castle Handpan Festival, Château de Frasne-le-Château'),
        ('8 juin', 'Spectacle participatif E-Motion by Solune'),
        ('28 juin', 'Festival Été Nomade, Port Dienville, base nautique'),
        ('9 août', 'Rennes-les-Bains, Festival Arts Terre Sacrée'),
        ('21 et 31 août', 'Jedapama, L’Écume des jours, Montbel'),
        ('14 septembre', 'Everness Indian Summer, Hongrie — Solune / E-Motion'),
    ]),
    ('2023', [
        ('7 janvier', 'Célébration de pleine lune « L’eau », Martigny'),
        ('4 février', 'Ecstatic Tribe United : Sacred Fire, Salle del Castillo, Vevey'),
        ('17 mars', 'Concert à la Péniche Anako, Paris'),
        ('25 mars', 'Fête de l’Être, Grange Rouge / Ferme la Zouillaz, Martigny'),
        ('26 mars', '« Dans les airs et les rythmes », Théâtre OZ, Martigny'),
        ('23 avril', 'Le Centre Élément — les cinq éléments'),
        ('17 juin', 'Duo avec Yves Mesnil, Festival Yoga &amp; pleine nature, Saint-Gervais-Mont-Blanc'),
        ('24 juin', 'Everness Festival, Hongrie'),
        ('22 juillet', 'HUG Fesztivál, Hongrie'),
        ('28 juillet', 'Festival Arts Extatics, Puivert'),
        ('14 août', 'Sziget Festival, Budapest — Everness Chill Beach'),
        ('19 août', 'Expérience immersive, Daumazan-sur-Arize, Festival Matricia'),
        ('10 septembre', 'Bungee, danse aérienne, L’Arbre aux étoiles'),
        ('22 septembre', 'Flori Pan, Tourcoing'),
        ('23 septembre', 'Église Saint-Jean-l’Évangéliste, Tourcoing'),
        ('30 septembre', 'Conférence, film et concert avec Arnaud Riou, Théâtre de l’Étang'),
        ('26 novembre', 'Sainte-Geneviève-des-Bois'),
        ('3 décembre', 'Expérience immersive, Iris &amp; David'),
    ]),
    ('2022', [
        ('2 avril', 'Concert avec Yves Mesnil'),
        ('3 avril', 'Expérience immersive 360° avec les dauphins d’Égypte, Hameau de l’Étoile'),
        ('15 avril', 'Festival virtuel « La Voie/x des hommes »'),
        ('8 mai', 'Cercle mixte et concert'),
        ('20 mai', 'David Lesage en concert à Toulouse, Salle San-Subra'),
        ('27 mai', 'Hona Festival, Naxos, Grèce'),
        ('11 juin', 'Cercle mixte et concert'),
        ('7 juillet', 'Cloître de Saint-Geniez-d’Olt'),
        ('17 juillet', 'Double concert dans une église'),
        ('30 juillet', 'HUG Fesztivál, Hongrie'),
        ('9 septembre', 'Première partie d’Amadou &amp; Mariam'),
        ('17 septembre', 'Festival des arts énergétiques « Les enfants de demain », abbaye d’Alet-les-Bains'),
        ('1<sup>er</sup> novembre', 'Mini-concert de Samhain, Latrape'),
    ]),
    ('2021', [
        ('29 mai', 'Concert handpan et voix, filmé en 360°'),
        ('4 et 12 juin', 'Doubles concerts « Loookaa &amp; David Lesage », Aigues-Vives'),
        ('20 juin', 'HangAout Festival, Domaine du Balbuzard'),
        ('9 juillet', 'Inauguration de Mama Flower'),
        ('18 juillet', 'Concert au coucher du soleil, L’Écume des jours, Montbel'),
    ]),
    ('2020', [
        ('14 août', 'Apéro-concert, Mirepoix'),
        ('4 septembre', 'Jedapama « Come Back Again », L’Écume des jours, Montbel'),
    ]),
    ('2019', [
        ('30 mai', 'Inauguration de la « Caz’Cade », avec Résonance'),
        ('30 juin', 'Handpan Festival Univers 7 Chakras — « Voyage vibratoire Résonance »'),
        ('28 juillet', 'Lac de Montbel'),
        ('31 juillet et 25 août', 'Roquefort-les-Cascades'),
        ('14 août', 'Jazz in Marciac, 15 h 15'),
        ('8 septembre', 'Concert Résonance, Spiruchonnade'),
    ]),
    ('2018', [
        ('13 août', 'Jazz in Marciac, avec le groupe « Résonance »'),
    ]),
    ('2017', [
        ('28 juin', 'Église Saint-Nazaire de Carcassonne'),
        ('9 juillet', '« Chants du cœur », Le Sing Sing'),
        ('2 août', 'Trio voix et instruments du monde, basilique Saint-Nazaire'),
        ('17 et 24 septembre', 'Église Saint-Nazaire de Carcassonne'),
    ]),
    ('2016', [
        ('3 août', 'Concerts Jedapama'),
    ]),
]

# Nombre de dates reellement portees par CHRONO. Certaines lignes en regroupent
# plusieurs (« 21 et 31 août ») : on les compte pour ce qu'elles valent, sinon
# le chiffre affiche serait FAUX (sous-estime).
CHRONO_GROUPES = {
    ('2024', '21 et 31 août'): 2,
    ('2021', '4 et 12 juin'): 2,
    ('2019', '31 juillet et 25 août'): 2,
    ('2017', '17 et 24 septembre'): 2,
}
NB_DATES = sum(CHRONO_GROUPES.get((an, quand), 1)
               for an, lignes in SCENES_CHRONO for quand, _ in lignes)
# Garde-fou : le chiffre AFFICHE et le contenu de la chronologie ne peuvent pas
# diverger. Si quelqu'un ajoute une date sans toucher au chiffre, ca casse ici.
assert NB_DATES == 69, f'decompte incoherent : {NB_DATES} dates dans CHRONO'
assert SCENES_STATS[0][0] == str(NB_DATES), 'le chiffre affiche ne suit plus CHRONO'
ANNEES_CHRONO = [an for an, _ in SCENES_CHRONO]
assert ANNEES_CHRONO == ['2025', '2024', '2023', '2022', '2021', '2020',
                         '2019', '2018', '2017', '2016'], 'amplitude changee'


def scenes_stats():
    return ('<ul class="dlc-stats">'
            + ''.join(f'<li><b>{n}</b><span>{t}</span></li>' for n, t in SCENES_STATS)
            + '</ul>')


def scenes_refs():
    return ('<ul class="dlc-refs">'
            + ''.join(f'<li><b>{n}</b><span>{t}</span></li>' for n, t in SCENES_REFS)
            + '</ul>')


def scenes_liste(items):
    return ('<ul class="dlc-lieux">'
            + ''.join(f'<li><b>{n}</b><span>{t}</span></li>' for n, t in items)
            + '</ul>')


def scenes_chrono():
    """Chronologie complete dans un <details> NATIF : elle s'ouvre et se ferme
    sans une ligne de JavaScript, et reste imprimable / trouvable par Ctrl+F
    dans les navigateurs modernes."""
    lignes = []
    for an, dates in SCENES_CHRONO:
        li = ''.join(f'<li><span class="dlc-when">{q}</span>{t}</li>' for q, t in dates)
        lignes.append(f'<dt>{an}</dt><dd><ul>{li}</ul></dd>')
    return ('<details class="dlc-more"><summary>Voir toute la chronologie recensée — '
            f'{NB_DATES} dates, de 2016 à 2025</summary>'
            f'<dl class="dlc-chrono">{"".join(lignes)}</dl></details>')

# Repertoire ecoutable SUR la page.
# 3e champ = identifiant YouTube, ou None. Regle d'attribution : on ne relie un
# titre QUE si le nom du morceau correspond clairement au titre de la video, et
# seulement des videos de la chaine de David Lesage (@DavidLesageArtiste).
# Chaque identifiant a ete valide par oEmbed (video publique + embarcable).
# La liste ne rétrécit JAMAIS : un titre sans video reste affiche, sans icone.
COMPOSITIONS = [
    # « Intro Concert David Lesage #Calebasse #Voix » (4Q7ABtumojY) existe, mais
    # rien ne prouve qu'il s'agisse de la piste « Intro » de l'album -> NON relie.
    ('Intro', None),
    ('Humano', 'Y5D0_iiVflg'),            # L'alliance du phoenix - Humano - Live Concert - Alet les bains - #432hz
    ('Transe lunaire', None),             # aucune video sur la chaine
    ('L’alchimiste', None),               # aucune video sur la chaine
    ('L’appel du vent', 's4XCQP8B11I'),   # L’appel du vent, Danse de tournoiement @iris Chasles et David Lesage @neotone
    ('Au cœur de l’homme', 'n-BOdL7KEYU'),# Au coeur de l'homme @DavidLesageArtiste @yishama_official
    # « Yishama » est le nom du morceau ET celui du facteur de handpans : toutes
    # les videos taguees @yishama_official portent un AUTRE titre -> NON relie.
    ('Yishama', None),
    # « Honorer l'eau tisseuse de lien entre les peuples » n'est pas ce morceau.
    ('Le tisseur de liens', None),
    ('Je te vois', None),                 # aucune video sur la chaine
]

REPRISES = [
    ('Sting', 'Shape of My Heart', 'Zp_zaqsRBCg'),                              # Shape of my Heart #Handpan @yishama_official @theofficialsting @craigdavid #432HZ
    ('M', 'Une Âme', 'a831rQeGLRU'),                                            # Une Ame 2 min The voice David Lesage
    ('Alicia Keys', 'Fallin’', 'WYVtBfoz7T8'),                                  # Fallin cover @AliciaKeys @yishama_official #432hz
    ('Bigflo &amp; Oli', 'Copier Coller', '2kVSLdpzt_M'),                       # Copier Coller @BigfloetOli #Cover #Handpan @yishama_official #Voix
    ('Charles Gounod', 'Ave Maria', 'pkHFaaZplik'),                             # Handpan Ave Maria Jazz Style @yishama_official
    ('Roberto Orenalla', 'L’Esprit Divin', 'ldXkWmq-Mfo'),                      # Oh toi l’esprit divin @yishama_official #handpan #voix
    ('Algonquin Water Song — chant traditionnel', 'Nibiwabo', 'p521GVsZSvM'),   # Nibiwabo Le chant de L'eau - N Goni - Foret Roquefort les cascades
]

PICO = '<span class="pico" aria-hidden="true">▸</span>'

# --- VERSIONS STUDIO : plateformes ------------------------------------------
# Ce sont des PLATEFORMES, pas des videos : un nouvel onglet est legitime ici
# (la regle « la video reste sur le site » ne concerne que les videos).
# ⚠️ iMusician : la page /releases porte les DEUX opus de « L'Alliance du
# Phoenix » (verifie le 13/08/2026 : les libelles « ...phoenix - Opus 1 » et
# « ...phoenix - Opus 2 » sont tous deux dans le HTML). L'application est une SPA
# et n'expose AUCUNE URL distincte par opus -> on lie donc la page des sorties,
# et on l'annonce comme telle. Ne pas inventer d'URL par opus.
IMUSICIAN = 'https://music.imusician.pro/artist/GtChl4dcIh/releases'
# --- LECTEUR SPOTIFY : CHARGE AU CLIC SEULEMENT -----------------------------
# Coherence avec le lecteur video : tant que personne n'a clique, AUCUNE requete
# ne part vers un domaine tiers. L'<iframe> Spotify n'existe pas dans le HTML
# livre ; elle est CREEE au clic sur le bouton (voir SPOTIFY_JS). Verifie par
# performance.getEntriesByType('resource') : zero entree *.spotify.com au
# chargement. Ne JAMAIS remettre l'iframe en dur dans le HTML.
SPOTIFY_EMBED_ID = 'artist/7zEAQJbalBFj8XNHrcqdbK'   # /embed/<ceci> -> 200

# --- VIDEOS LIVE : deux ensembles, tires de SES playlists -------------------
# David demandait « deux playlists avec des vidéos lives ». Ses playlists
# existent deja sur sa chaine (@DavidLesageArtiste) : on n'a donc RIEN invente,
# on a repris les deux qui repondent exactement a la demande —
#   * « Concerts Live David Lesage »  (PLns6mQWNwwnS6KljAheL9gCn-sIiu0HmS, 33 videos)
#   * « Yishama Handpan David Lesage » (PLns6mQWNwwnQ_KWoyklbfqtlFzIQi9iQf, 14 videos)
# La seconde sert aussi le reequilibrage demande le 13/08/2026 : le handpan
# ACOUSTIQUE Yishama y est partout, la ou le Neotone occupait toutes les photos.
# On n'affiche pas les 47 videos : 6 par ensemble, choisies sur DEUX criteres —
#   (1) vignette maxresdefault disponible (1280x720, vrai 16:9). Les vignettes
#       sd/hq sont en 4:3 letterboxe : bandes noires dans une grille 16:9.
#   (2) la vignette donne envie (demande explicite de David). Ecartees pour ce
#       motif : mH5rUuelF8o (carton de titre noir, aucune image), fKsDtOJlDx0
#       (fisheye 360 illisible), 33G59yaTzHc (dauphins, hors sujet).
# Chaque identifiant valide par oEmbed le 13/08/2026 (public + embarcable) ;
# le titre en commentaire est le titre EXACT retourne par oEmbed.
# Vignettes RAPATRIEES EN LOCAL dans /img/concert-live/ (aucune image distante),
# natif 1280x720 -> jamais affichees au-dela (sinon flou).
# Aucune n'est signee ni filigranee par un photographe tiers : ce sont les
# vignettes publiees par David sur sa propre chaine, avec ses propres
# incrustations (son nom, la marque Yishama). Rien a crediter.
LIVE_CONCERTS = [
    ('Y5D0_iiVflg', 'live-humano-abbaye-alet-les-bains',
     'Vue depuis le fond de l’abbaye à ciel ouvert d’Alet-les-Bains : un public nombreux '
     'assis sur des chaises entre les murs de pierre, l’artiste seul debout au fond ; '
     'titre incrusté « L’Alliance du Phoenix — Humano ».',
     'Humano — Abbaye d’Alet-les-Bains'),
    # « Extrait Concert David Lesage 2022 2023 »
    ('-ReJnKAr274', 'live-extrait-concert-lieu-de-pierre',
     'Plateau installé au pied d’un haut mur de pierre éclairé de doré : deux handpans sur '
     'pieds au centre, des rangées de chaises vides et un projecteur en contre-jour ; '
     'titre incrusté « Extrait Concert David Lesage ».',
     'Extrait de concert'),
    ('WUvCwdBYwXw', 'live-valse-do-mar-everness-festival',
     'Grande scène de festival dans des faisceaux violets et verts : cinq musiciens assis '
     'en arc de cercle, violon, guitare et percussions, des retours de scène au premier plan.',
     'Valse do Mar — Everness Festival'),
    ('qEbFXDE8o9o', 'live-les-gardiens-du-silence-hangaout-festival',
     'Scène de festival éclairée de bleu et de violet : l’artiste debout derrière ses '
     'instruments, un pupitre devant lui ; titre incrusté « Les gardiens du silence — '
     'David Lesage, Live HangAout Festival ».',
     'Les gardiens du silence — HangAout Festival'),
    ('JA-riZgq92M', 'live-appel-des-144000-voute-aux-chandelles',
     'Sous une voûte de pierre éclairée à la bougie, l’artiste assis derrière deux handpans '
     'posés sur pieds, entre deux chandeliers allumés.',
     'L’appel des 144 000 — voix et handpan'),
    ('3akajIK-oHk', 'live-chapelle-mas-galifa-espagne',
     'Une petite chapelle de pierre sous un ciel bleu vif, un arbre au-dessus ; l’artiste '
     'debout devant la porte, de profil.',
     'Chapelle du Mas Galifa, Espagne'),
]

LIVE_YISHAMA = [
    ('81yKSB3dIK0', 'yishama-angel-voice',
     'L’artiste assis devant une grande baie vitrée, penché sur un handpan acoustique en '
     'bronze posé sur un pied, une main levée ; incrustations « Yishama Pantam » et '
     '« Angel Voice ».',
     'Angel Voice — handpan acoustique'),
    ('Zp_zaqsRBCg', 'yishama-shape-of-my-heart',
     'Deux handpans acoustiques en bronze au premier plan devant un mur de pierre éclairé '
     'par deux appliques, l’artiste assis derrière ; incrustations « Shape Of my Heart », '
     '« Yishama » et « David Lesage ».',
     'Shape of My Heart — Sting'),
    ('pkHFaaZplik', 'yishama-ave-maria-jazz',
     'L’artiste devant un mur de pierre, les mains sur un handpan acoustique en bronze ; '
     'incrustations « Ave Maria Jazz impro Handpan » et logo Yishama.',
     'Ave Maria — improvisation jazz'),
    ('n-BOdL7KEYU', 'yishama-au-coeur-de-l-homme',
     'L’artiste debout derrière deux handpans acoustiques en métal clair posés sur pieds, '
     'dans une pièce claire ; titre incrusté « Au cœur de l’homme ».',
     'Au cœur de l’homme — composition'),
    ('LKnqMESCE-g', 'yishama-derbouka-duo',
     'Deux musiciens assis face à face devant un mur de pierre, chacun derrière un handpan '
     'acoustique en bronze, une flamme entre eux.',
     'Derbouka — en duo'),
    ('WYVtBfoz7T8', 'yishama-fallin',
     'Gros plan sur des mains au-dessus d’un handpan acoustique en métal clair, et portrait '
     'de l’artiste souriant à côté.',
     'Fallin’ — Alicia Keys'),
]


def rep_li(titre, vid, artiste=None):
    """Une ligne du repertoire. Avec identifiant : un bouton qui ouvre le lecteur
    DANS la page (jamais un lien sortant). Sans : le meme texte, sans icone."""
    sub = f'<span>{artiste}</span>' if artiste else ''
    if not vid:
        return f'<li><span class="rep-t">{titre}</span>{sub}</li>'
    lab = titre.replace('&amp;', 'et')
    # Pas de <span> autour du titre : `.dlc-card li span` le passerait en dore
    # et en 13.5 px. Le texte nu est un item de flex anonyme, c'est suffisant.
    return (f'<li><button type="button" class="ytlink rep-t" data-yt="{vid}"'
            f' aria-label="Écouter « {lab} » — le lecteur s’ouvre sur cette page">'
            f'{titre}{PICO}</button>{sub}</li>')


REP_HINT = ('<p class="rep-hint">Les titres suivis de ' + PICO
            + ' s’écoutent ici même : le lecteur s’ouvre dans la page.</p>')

# Largeurs natives des vignettes live : 1280x720. Ne JAMAIS depasser 1280.
LIVE_WIDTHS = [480, 900, 1280]
LIVE_SIZES = ('(max-width:560px) calc(100vw - 52px), '
              '(max-width:900px) calc(50vw - 44px), 330px')


def live_card(vid, slug, alt, label):
    """Une vignette live : <button> qui ouvre le lecteur DANS la page.

    Meme mecanique que video_button (.ytlink + data-yt), en format grille.
    Jamais de lien sortant, jamais de nouvel onglet."""
    root = f'/img/concert-live/{slug}'
    webp = ', '.join(f'{root}-{x}.webp {x}w' for x in LIVE_WIDTHS)
    jpg = ', '.join(f'{root}-{x}.jpg {x}w' for x in LIVE_WIDTHS)
    img = (f'<picture><source type="image/webp" srcset="{webp}" sizes="{LIVE_SIZES}">'
           f'<img src="{root}-900.jpg" srcset="{jpg}" sizes="{LIVE_SIZES}" '
           f'width="1280" height="720" loading="lazy" decoding="async" alt="{alt}"></picture>')
    return (f'<button type="button" class="lvc ytlink" data-yt="{vid}">'
            f'<span class="shot">{img}<span class="play" aria-hidden="true"></span></span>'
            f'<span class="lvc-t">{label}</span></button>')


def live_grid(items):
    return f'<div class="lvg">{"".join(live_card(*i) for i in items)}</div>'


def live_feature(slug, vid, alt, label, sub, sizes):
    """Une vignette live en GRAND format, avec legende — pour illustrer une
    section. Meme mecanique que video_button, mais la source est une vignette de
    /img/concert-live/ (native 1280x720, jamais agrandie au-dela)."""
    root = f'/img/concert-live/{slug}'
    webp = ', '.join(f'{root}-{x}.webp {x}w' for x in LIVE_WIDTHS)
    jpg = ', '.join(f'{root}-{x}.jpg {x}w' for x in LIVE_WIDTHS)
    img = (f'<picture><source type="image/webp" srcset="{webp}" sizes="{sizes}">'
           f'<img src="{root}-900.jpg" srcset="{jpg}" sizes="{sizes}" width="1280" '
           f'height="720" loading="lazy" decoding="async" alt="{alt}"></picture>')
    return (f'<button type="button" class="dlc-video ytlink" data-yt="{vid}">'
            f'<figure class="dlc-fig"><span class="shot">{img}'
            f'<span class="play" aria-hidden="true"></span></span>'
            f'<figcaption><span class="vlabel">{label}</span>'
            f'<span class="vsub">{sub}</span></figcaption></figure></button>')


# --- Lecteur Spotify : cree AU CLIC seulement -------------------------------
# Voir SPOTIFY_EMBED_ID. Le bouton est un vrai <button> (cible 48 px) ; au clic
# il est remplace par l'iframe. Aucun script ni cookie Spotify avant ce clic.
SPOTIFY_HTML = """
  <div class="spf" data-sp="{sp}">
    <button type="button" class="btn ghost spf-btn">Écouter le lecteur Spotify</button>
    <p class="spf-note">Le lecteur ne se charge qu’à votre demande : rien n’est envoyé à Spotify avant que vous n’appuyiez sur ce bouton.</p>
  </div>
"""

SPOTIFY_JS = """
<script>
/* Lecteur Spotify differé : l'<iframe> N'EXISTE PAS avant le clic, donc aucune
   requete vers spotify.com au chargement de la page (meme principe que le
   lecteur video). Ne pas « optimiser » en posant l'iframe dans le HTML. */
(function(){
  document.addEventListener('click',function(e){
    var b=e.target.closest && e.target.closest('.spf-btn'); if(!b) return;
    var box=b.closest('.spf'); if(!box || box.dataset.loaded) return;
    box.dataset.loaded='1';
    var f=document.createElement('iframe');
    f.src='https://open.spotify.com/embed/'+box.dataset.sp;
    f.title='Lecteur Spotify — David Lesage';
    f.loading='lazy'; f.width='100%'; f.height='352'; f.style.border='0';
    f.setAttribute('allow','clipboard-write; encrypted-media; fullscreen; picture-in-picture');
    b.replaceWith(f);
  });
})();
</script>
"""

CITATIONS = ['Une musique qui tisse des liens', 'Des rythmes envoûtants',
             'Des paroles profondes', 'Des refrains incantatoires',
             'Des envolées jazz d’une voix céleste']

# ===========================================================================
# FICHE TECHNIQUE — source : presentation Drive « Fiche technique et Artistique
# David Lesage artiste - International ». Voir l'avertissement en tete de fichier
# pour ce qui est volontairement EXCLU de la page.
# ===========================================================================

# Patch d'entrees de la configuration de reference (9 entrees). Repris de la
# diapositive « Input Patch Liste David Lesage » (version festival / minimaliste,
# plan de scene « Stage plan minimalist — Total Input : 9 »).
PATCH_9 = [
    ('1', 'Voix', 'Micro serre-tête DPA D:Fine 4088 + système HF '
                  '(récepteur mini-jack 3,5 mm)'),
    ('2', 'Sanzula / kalimba', 'Micro AKG C214, ou boîte de direct'),
    ('3', 'Handpan électronique', 'DI — pied de handpan'),
    ('4', 'Wavedrum (percussion électronique)', 'DI — pied de Wavedrum'),
    ('5', 'Kick électronique', 'DI stéréo — déclencheur Roland'),
    ('6', 'Caisse claire et hi-hat électroniques', 'DI stéréo — déclencheurs Roland'),
    ('7', 'N’Goni 14 cordes', 'Micro contact AKG C411'),
    ('8', 'Calebasse', 'Micro Shure Beta 91A, placé sous la calebasse'),
    ('9', 'Ordinateur — bandes et projections',
          'Entrée mini-jack 3,5 mm + arrivée HDMI sur scène'),
]

# Plateau : diapositive « Stage plan » + « Recapitulatif materiel demande ».
PLATEAU = [
    ('Dimensions', 'Plateau plat et de niveau, <b>4 m × 5 m minimum</b>'),
    ('Hauteur', 'Environ 40 cm du sol'),
    ('Praticable', '1 praticable de batterie 3 m × 3 m — sur roulettes si le plateau '
                   'doit changer rapidement'),
    ('Tapis', '1 tapis rond de 2 m de diamètre'),
    ('Électricité', '1 multiprise 8 prises aux normes françaises, avec protection '
                    'contre les surtensions'),
    ('Console', '<b>Enregistrement multipiste demandé</b> sur la console'),
    ('Projection', '1 vidéoprojecteur + écran + câble HDMI si une projection est '
                   'prévue — elle est lancée depuis la scène'),
]

RETOURS = [
    ('Retour principal', 'Un système <b>Bose S1 + Sub1</b>, placé 1 à 3 m derrière '
                         'l’artiste. Il l’apporte lui-même quand le contexte le permet.'),
    ('À défaut', 'Un retour de scène standard <b>plus un petit caisson de basse</b>, '
                 'placé derrière l’artiste, pour rendre l’impact des kicks électroniques.'),
    ('Intention', 'Être pleinement immergé dans le son et disposer d’un peu de pression '
                  'acoustique — c’est ce qui tient le jeu de tout le set.'),
    ('Click', 'Un retour in-ear HF, réservé au click.'),
]

# « Materiel demande par l'artiste » : diapositives 4 et 61 a 64.
DEMANDE = [
    '1 système HF pour le micro serre-tête DPA — l’artiste apporte les adaptateurs '
    'Shure, Sennheiser et AKG',
    '3 pieds de cymbale ride avec perchette orientable (supports des déclencheurs et '
    'de l’iPad)',
    '3 pieds de handpan',
    '1 pied de N’Goni / kora, capable d’accueillir une calebasse de 55 cm',
    '1 pied support d’ordinateur, en position debout',
    '1 pied de Wavedrum + bras d’extension pour poser la loop station',
    '1 micro Shure Beta 91A',
    '1 kick électronique Roland KT-10',
    '1 coussin de type zafu, pour jouer la calebasse',
    '1 bouteille d’eau, une petite serviette et un ventilateur sur scène',
]

# « Liste du materiel apporte par l'artiste » : diapositive 70.
APPORTE = [
    '3 handpans — dont le handpan électronique — avec leurs coques de transport',
    'Le N’Goni 14 cordes et son accordeur',
    'La Wavedrum, les déclencheurs Roland BT1 et le sampler Roland TM2',
    'La loop station Roland RC-505 MK2',
    'Le MacBook Pro, la carte son et l’iPad',
    'La calebasse, son tapis et ses œufs, et la sanzula',
    'Tous les micros sauf exceptions : le serre-tête DPA D:Fine 4088, 3 micros contact '
    'AKG C411, 3 micros col de cygne',
]

TOC = [
    ('#fiche', 'En un regard'),
    ('#dispositif', 'Le dispositif'),
    ('#salle', 'Ce que fait une salle qui chante'),
    ('#parcours', 'Le parcours'),
    ('#scenes', 'Scènes &amp; festivals'),
    ('#repertoire', 'Le répertoire'),
    ('#studio', 'Écouter les versions studio'),
    ('#live', 'Voir deux ensembles de vidéos live'),
    ('#acoustique', 'Une version plus acoustique'),
    ('#option', 'En option : la danse aérienne'),
    ('#technique', 'Fiche technique'),
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
/* figure au format portrait (affiche) : bornee a 420 px, jamais en grille */
.dlc-portrait{max-width:420px;margin-top:30px}
/* figure TRES verticale (ratio 0,474) : bornee plus court encore, sinon elle
   ferait presque 900 px de haut. 360 px est aussi la largeur qui la garde nette
   (360x2 = 720 device px, sous les 900 px de sa plus grande variante). */
.dlc-tall{max-width:360px;margin-top:30px}
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
.dlc-card h3,.dlc-card h4{font-family:'Cormorant Garamond',Georgia,serif;font-size:24px;color:#fff;font-weight:600;line-height:1.15}
.dlc-card .sub{color:var(--muted);font-size:14px;font-style:italic;margin-top:3px}
.dlc-card ul{list-style:none;margin-top:16px}
.dlc-card li{color:#d7d4ea;font-size:15.5px;padding:7px 0;border-bottom:1px solid rgba(255,255,255,.05);line-height:1.5}
.dlc-card li:last-child{border-bottom:0}
.dlc-card li span{color:var(--gold2);display:block;font-size:13.5px;letter-spacing:.04em}
/* ===== Titres du repertoire ecoutables SUR la page =====
   Un titre relie devient un <button class="ytlink"> : le gestionnaire delegue
   deja en place (.ytlink + data-yt) ouvre le lecteur en surimpression. Jamais
   de lien sortant ici. Les titres sans video gardent EXACTEMENT le meme style
   via .rep-t : seule l'icone ▸ distingue ce qui s'ecoute.
   .rep-t doit surcharger `.dlc-card li span` (qui met le sous-titre en dore) :
   la specificite d'une classe l'emporte sur celle d'un element, donc OK.
   Hauteur de rangee = 7 + 30 + 7 = 44 px : cible tactile respectee. */
.dlc-card li .rep-t{display:flex;align-items:center;gap:9px;width:100%;min-height:30px;
  color:#d7d4ea;font-family:inherit;font-size:15.5px;letter-spacing:normal;line-height:1.5;
  background:none;border:0;padding:0;margin:0;text-align:left}
.dlc-card li button.rep-t{cursor:pointer;transition:color .18s}
.dlc-card li button.rep-t:hover,.dlc-card li button.rep-t:focus-visible{color:#fff}
.pico{flex:0 0 auto;display:inline-flex;align-items:center;justify-content:center;
  width:19px;height:19px;border-radius:50%;border:1px solid rgba(216,178,90,.5);
  color:var(--gold);font-size:9px;line-height:1;padding-left:1px;
  transition:background .18s,color .18s,border-color .18s}
.dlc-card li button.rep-t:hover .pico,.dlc-card li button.rep-t:focus-visible .pico{
  background:var(--gold);border-color:var(--gold);color:#1a1608}
/* `.dlc-block p{color:#d7d4ea}` (0,1,1) battait `.rep-hint` (0,1,0) : la mention
   restait couleur de corps de texte. Selecteur prefixe -> (0,2,0), il gagne. */
.dlc-block .rep-hint{display:flex;align-items:center;gap:8px;flex-wrap:wrap;
  color:var(--gold2);font-size:14.5px;font-style:italic;margin-top:14px}
/* citations du dossier */
.dlc-cites{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px;max-width:880px;list-style:none}
.dlc-cites li{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:17.5px;line-height:1.4;background:rgba(216,178,90,.08);border:1px solid var(--line);border-radius:30px;padding:8px 20px}
/* ===== « La ou ce repertoire a resonne » (refonte du 13/08/2026) ===========
   Quatre etages, du plus lisible au plus dense : une ligne chiffree, les
   references majeures en grille, deux listes (scenes / lieux de pierre), puis
   tout le volume replie dans un <details>. L'ancienne liste a plat
   (.dlc-scenes) n'existe plus sur cette page. */
.dlc-stats{list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));
  gap:24px 26px;margin-top:30px;max-width:1028px;padding:24px 0;
  border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.dlc-stats li{display:flex;flex-direction:column;gap:6px}
.dlc-stats b{font-family:'Cormorant Garamond',Georgia,serif;font-weight:600;line-height:1;
  font-size:clamp(32px,4.4vw,44px);color:var(--gold2)}
.dlc-stats span{color:#d7d4ea;font-size:14.5px;line-height:1.5}
/* `.dlc-block p{color:#d7d4ea}` (0,1,1) battrait `.dlc-srcnote` (0,1,0) :
   selecteur prefixe -> (0,2,0), il gagne (meme piege que .rep-hint). */
.dlc-block .dlc-srcnote{color:var(--muted);font-size:14px;font-style:italic;
  margin-top:16px;max-width:820px;line-height:1.6}
/* references majeures */
.dlc-refs{list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(252px,1fr));
  gap:14px;margin-top:26px}
.dlc-refs li{background:var(--card);border:1px solid rgba(255,255,255,.06);
  border-left:2px solid var(--gold);border-radius:13px;padding:18px 20px}
.dlc-refs b{display:block;font-family:'Cormorant Garamond',Georgia,serif;font-size:22px;
  color:#fff;font-weight:600;line-height:1.18}
.dlc-refs span{display:block;color:var(--muted);font-size:14.5px;line-height:1.5;margin-top:6px}
/* listes secondaires : nom a gauche, precision a droite. Pas de capitales ici
   (contrairement a l'ancienne .dlc-scenes) : les precisions portent des dates
   et des villes, illisibles en petites capitales espacees. */
.dlc-lieux{list-style:none;margin-top:22px;max-width:880px;display:grid;gap:2px}
.dlc-lieux li{display:flex;gap:4px 22px;align-items:baseline;flex-wrap:wrap;
  padding:12px 0;border-bottom:1px solid rgba(255,255,255,.06)}
.dlc-lieux li:last-child{border-bottom:0}
.dlc-lieux li b{flex:1 1 250px;min-width:0;color:#fff;font-weight:500;font-size:16px;line-height:1.45}
.dlc-lieux li span{flex:1 1 250px;min-width:0;color:var(--muted);font-size:14.5px;line-height:1.5}
/* chronologie repliee : <details> NATIF, zero JavaScript */
.dlc-more{margin-top:34px;max-width:920px;border:1px solid var(--line);border-radius:14px;
  background:rgba(25,27,61,.5)}
.dlc-more>summary{display:flex;align-items:center;gap:12px;min-height:52px;
  padding:12px 22px;cursor:pointer;color:var(--gold2);font-size:16px;line-height:1.4;
  list-style:none}
/* les deux formes de marqueur natif, sinon Safari garde son triangle */
.dlc-more>summary::marker{content:''}
.dlc-more>summary::-webkit-details-marker{display:none}
.dlc-more>summary::after{content:'';width:7px;height:7px;flex:0 0 auto;
  border-right:1.6px solid currentColor;border-bottom:1.6px solid currentColor;
  transform:translateY(-2px) rotate(45deg);transition:transform .22s}
.dlc-more[open]>summary::after{transform:translateY(1px) rotate(-135deg)}
.dlc-more>summary:hover{color:#fff}
.dlc-chrono{padding:2px 22px 20px;display:grid;grid-template-columns:minmax(0,96px) minmax(0,1fr);gap:0}
.dlc-chrono dt{font-family:'Cormorant Garamond',Georgia,serif;font-size:25px;color:var(--gold2);
  font-weight:600;padding:15px 20px 15px 0;border-top:1px solid rgba(255,255,255,.07);line-height:1.25}
.dlc-chrono dd{padding:14px 0 15px;border-top:1px solid rgba(255,255,255,.07)}
.dlc-chrono dt:first-of-type,.dlc-chrono dd:first-of-type{border-top:0}
.dlc-chrono ul{list-style:none}
.dlc-chrono li{color:#d7d4ea;font-size:15.5px;line-height:1.55;padding:5px 0}
.dlc-chrono .dlc-when{display:inline-block;min-width:112px;color:var(--gold);font-size:13px;
  letter-spacing:.06em;text-transform:uppercase;font-weight:600;margin-right:8px}
@media(max-width:640px){
  .dlc-chrono{grid-template-columns:1fr;padding:2px 17px 18px}
  .dlc-chrono dt{padding:16px 0 2px}
  .dlc-chrono dd{border-top:0;padding:0 0 12px}
  .dlc-chrono .dlc-when{display:block;min-width:0;margin:0 0 1px}
  .dlc-more>summary{padding:12px 17px}
}
/* ===== Logo d'artiste de David Lesage ======================================
   ⚠️ Logo de L'ARTISTE, pas de l'association : il identifie David Lesage en
   tete de la section qui parle de lui, et ne remplace RIEN dans la barre de
   navigation. Natif 2578x1943 reduit a 900 px : plafonne a 300 px, il n'est
   jamais affiche au-dela de sa resolution. */
.dlc-logo{margin:24px 0 0;max-width:300px}
.dlc-logo img{display:block;width:100%;height:auto}
/* deux figures cote a cote */
.dlc-duo{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin-top:30px;align-items:start}
/* ===== fiche technique ===== */
.dlc-sub{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(23px,3vw,30px);color:#fff;font-weight:600;line-height:1.2;margin-top:46px}
.dlc-conf{background:var(--card);border:1px solid rgba(255,255,255,.06);border-top:2px solid var(--gold);border-radius:14px;padding:24px 26px}
.dlc-conf h4{font-family:'Cormorant Garamond',Georgia,serif;font-size:24px;color:#fff;font-weight:600;line-height:1.15}
.dlc-conf p{color:#d7d4ea;font-size:15.5px;margin-top:10px;line-height:1.65;max-width:none}
.dlc-conf.reco{border-top-color:var(--gold2);box-shadow:0 0 0 1px rgba(216,178,90,.22)}
.dlc-tag{display:inline-block;font-size:13px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:#1a1608;background:var(--gold);border-radius:20px;padding:4px 13px;margin-bottom:12px}
.dlc-tag.alt{background:transparent;color:var(--gold2);border:1px solid var(--line)}
/* listes « demande / apporte » */
.dlc-list{list-style:none;margin-top:16px}
.dlc-list li{color:#d7d4ea;font-size:15.5px;line-height:1.55;padding:9px 0 9px 20px;border-bottom:1px solid rgba(255,255,255,.05);position:relative}
.dlc-list li:last-child{border-bottom:0}
.dlc-list li::before{content:'';position:absolute;left:2px;top:16px;width:6px;height:6px;border-radius:50%;background:var(--gold)}
/* tableau du patch d'entrees.
   POINT DE RISQUE MOBILE : un tableau a colonnes deborde sous 480 px. Deux
   garde-fous cumules : (1) le conteneur .dlc-tw est en overflow-x:auto (filet de
   securite) ; (2) sous 700 px le tableau est REMIS EN PILE (une carte par ligne,
   intitules de colonnes restitues par td::before/data-label) -> plus aucun
   defilement horizontal a lire, donc plus aucun risque de debordement. */
.dlc-tw{margin-top:22px;max-width:900px;overflow-x:auto;-webkit-overflow-scrolling:touch;border:1px solid rgba(255,255,255,.08);border-radius:14px;background:var(--card)}
.dlc-tab{width:100%;border-collapse:collapse;min-width:600px;font-size:15.5px}
.dlc-tab caption{text-align:left;color:var(--gold);font-size:13px;letter-spacing:.16em;text-transform:uppercase;font-weight:600;padding:17px 18px 3px}
.dlc-tab th,.dlc-tab td{text-align:left;padding:12px 18px;border-top:1px solid rgba(255,255,255,.07);vertical-align:top;line-height:1.5}
.dlc-tab thead th{color:var(--gold2);font-size:13px;letter-spacing:.12em;text-transform:uppercase;font-weight:600}
.dlc-tab tbody td{color:#d7d4ea}
.dlc-tab tbody th{color:var(--gold2);font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-weight:600;width:56px}
@media(max-width:700px){
  .dlc-tw{overflow:visible;border:0;background:transparent;border-radius:0;max-width:none}
  .dlc-tab{display:block;min-width:0;font-size:16px}
  /* la <caption> reste en display:table-caption dans un parent devenu block :
     elle se reduisait a la largeur d'un mot (un mot par ligne). */
  .dlc-tab caption{display:block;width:100%;padding:0 0 12px}
  .dlc-tab thead{display:none}
  .dlc-tab tbody,.dlc-tab tr,.dlc-tab td,.dlc-tab tbody th{display:block;width:auto}
  .dlc-tab tr{background:var(--card);border:1px solid rgba(255,255,255,.07);border-left:2px solid var(--gold);border-radius:12px;padding:15px 17px;margin-bottom:11px}
  .dlc-tab tbody th{border-top:0;padding:0;font-size:19px}
  .dlc-tab td{border-top:0;padding:0}
  .dlc-tab td::before{content:attr(data-label);display:block;color:var(--gold);font-size:13px;letter-spacing:.12em;text-transform:uppercase;font-weight:600;margin-top:10px;margin-bottom:1px}
}
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
""" + LIGHTBOX_CSS

TITLE = ('David Lesage en concert — concert-cérémonie participatif pour grandes scènes '
         'et festivals · Résonances Productions')
DESC = ('Voix, handpan, calebasse, N’Goni et électronique : une expérience immersive de '
        'musique live d’1 h 30, à programmer sur grande scène, en festival ou dans un '
        'lieu d’exception. Première partie d’Amadou &amp; Mariam, Sziget et Everness '
        'Festival (Hongrie), Jazz in Marciac, Grand Rex, abbaye d’Alet-les-Bains, salle '
        'San-Subra à Toulouse, Vevey, Côte d’Ivoire. Fiche technique : '
        'configuration de référence à 9 entrées, plateau 4 m × 5 m. Option danse '
        'aérienne à l’élastique.')

HTML = f"""<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="David Lesage en concert — grandes scènes &amp; festivals">
<meta property="og:description" content="Concert — Cérémonie — Participatif : 1 h 30 de musique live immersive. Voix, handpan, calebasse, Ngoni, électronique ; cymatique et vidéoprojections ; option danse aérienne à l’élastique. À programmer.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.resonancesproductions.org/david-lesage-en-concert">
<meta property="og:image" content="https://www.resonancesproductions.org/img/concert-scene/neotone-en-scene-1400.jpg">
<meta property="og:image:width" content="1400">
<meta property="og:image:height" content="933">
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
  <p class="body">Le format réunit instruments traditionnels et modernité, et alterne deux régimes : des séquences d’<b>écoute active</b>, et des séquences <b>participatives</b> où la salle devient une partie de l’œuvre — elle chante en écho, et voit à l’écran l’empreinte de sa propre voix. Un musicien, chanteur et compositeur passé par le Conservatoire National de Toulouse et le collège de Jazz in Marciac, à l’ambitus vocal de cinq octaves, passé par <i>The Voice</i>, par les scènes du <b>Sziget</b> et de l’<b>Everness Festival</b>, en Hongrie, et par la <b>première partie d’Amadou &amp; Mariam</b>.</p>
  <div class="cta" style="margin-top:26px"><a class="btn" href="{MAILTO_PROG}">Programmer ce concert</a><a class="btn ghost" href="{MAILTO_DOSSIER}">Demander le dossier</a></div>
  {pic('neotone-scene',
       'David Lesage seul sur scène, en plan rapproché, les yeux fermés en train de chanter dans un micro serre-tête, les deux mains posées sur un Neotone — le handpan électronique, coque de bois clair et pastilles sombres. Deux micros sur pied l’encadrent, un contrôleur Korg est posé au premier plan ; en fond, un décor de fils tendus violets, verts et rouges devant de la végétation.',
       '(max-width:1080px) calc(100vw - 52px), 1028px',
       'Seul en scène, en plein air : la voix et les mains au centre du dispositif.',
       cls='dlc-fig dlc-hero-fig', loading='eager', src_w=1400)}
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
  <div class="dlc-duo">
    {pic('solo-cymatique',
         'David Lesage seul au centre d’un plateau, derrière ses instruments, devant un très grand écran où est projetée une figure cymatique verte et dorée en forme de fleur.',
         '(max-width:860px) calc(100vw - 52px), 500px',
         'La figure dessinée par la voix, projetée en direct sur l’écran de scène.')}
    {pic('public-proche',
         'David Lesage debout sur scène, une calebasse posée devant lui ; au premier plan, le public assis au sol sur des tapis, à un mètre du plateau, entre des lampes-boules blanches.',
         '(max-width:860px) calc(100vw - 52px), 500px',
         'Le public installé au bord du plateau, dans une configuration assise.')}
  </div>
  <!-- ⚠️ HONNETETE DE LEGENDE. David a fourni cette photo en la decrivant comme
       « je donne une indication vocale au public (echanges vocaux) ». Or IL N'EST
       PAS DANS LE CADRE : on ne voit que le public, vu depuis le plateau. La
       legende ci-dessous ne dit donc rien de sa presence — elle decrit ce qu'on
       voit et evoque l'echange vocal par son point de depart (la scene), sans
       affirmer qu'on l'y voit. NE PAS la reecrire en « David donne une
       indication au public » : ce serait faux. -->
  {pic('public-echange',
       'Vu depuis le bord du plateau : un public très nombreux assis dans l’herbe et sur des gradins de bois, sous de grandes voiles d’ombrage tendues entre les arbres ; au premier plan, l’angle de la scène et quelques objets posés dessus.',
       '(max-width:900px) calc(100vw - 52px), 860px',
       'Le public, vu depuis le plateau — c’est de là que part l’échange vocal.',
       cls='dlc-fig dlc-wide', src_w=1400)}
</div></section>

<div class="divider"></div>

<section class="dlc-block band" id="parcours"><div class="wrap">
  <div class="dlc-h">Le parcours</div>
  <h2 class="sec-title">Autodidacte, Marciac, cinq octaves</h2>
  {logo_fig()}
  <div class="dlc-split">
    <div>
      <p>Musicien, chanteur et compositeur français. Un <b>artiste curieux</b> et un <b>musicien autodidacte</b>. Ses instruments : la <b>voix</b>, le <b>handpan</b>, la <b>calebasse</b>, le <b>Ngoni</b> — la harpe africaine —, la wave drum et des déclencheurs électroniques.</p>
      <p>Son intention : des musiques <b>électro-organiques</b>, qui mêlent instruments acoustiques, musique électronique et voix humaine. Trois mots pour le situer : <b>soul française</b>, <b>African spirit</b>, <b>électro vibes</b>.</p>
      <p>Il est passionné par l’<b>impact de la vibration sur le vivant</b> — la <b>cymatique</b> — et travaille tous ses instruments en <b>La 432 Hz</b>. Ce qu’il cherche, de scène en scène : une <b>quête du son primordial, celui qui rassemble tous les êtres</b>.</p>
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
  <div class="dlc-duo">
    {pic('voix-machines',
         'David Lesage seul en scène, éclairé de bleu-vert, la main levée près du visage en train de chanter, debout derrière ses handpans posés sur des pieds et un ordinateur portable.',
         '(max-width:860px) calc(100vw - 52px), 500px',
         'La voix, au centre du dispositif — cinq octaves et un micro serre-tête.')}
    {pic('calebasse',
         'David Lesage assis en tailleur derrière une grande calebasse posée sur un tapis rond rouge, les mains sur la calebasse, entouré de dizaines de petites bougies alignées au sol.',
         '(max-width:860px) calc(100vw - 52px), 500px',
         'La calebasse, frappée au poing, jouée assis sur un coussin.')}
  </div>
  <!-- Troisieme instrument du parcours, apres la voix et la calebasse : le
       N'Goni. Photo posee en pleine largeur (860 px) et non ajoutee comme
       troisieme colonne du .dlc-duo ci-dessus : la grille aurait retreci les
       deux figures existantes a 329 px, et cette image sombre a besoin de place.
       ⚠️ SIGNEE « MAGYE D'ART Production » en bas a droite -> credit obligatoire. -->
  {pic('ngoni',
       'David Lesage seul, assis au sol sur une peau claire, jouant le N’Goni — la harpe africaine, caisse de calebasse et cordes tendues sur un long manche — devant trois néons rouges verticaux et des palmes, dans une lumière chaude ; une seconde calebasse posée à sa droite.',
       '(max-width:900px) calc(100vw - 52px), 860px',
       'Le N’Goni, la harpe africaine à caisse de calebasse : rencontré en 2012, toujours au répertoire du concert.',
       cls='dlc-fig dlc-wide', credit=CREDIT_MAGYE, src_w=1400)}

  <h3 class="dlc-sub">The Voice, saison 11</h3>
  <p>Pour son audition à l’aveugle de <i>The Voice</i> saison 11, sur TF1, David Lesage monte seul en scène avec ses propres instruments : la calebasse, les handpans et le N’Goni 14 cordes. Il y chante <i>Kothbiro</i>, d’Ayub Ogada, en luo — un titre toujours au répertoire du concert. La prestation est publique sur la chaîne officielle de l’émission.</p>
  {video_button('tv-video', VIDEO_TV_ID,
                'Vignette de la vidéo : David Lesage seul sur le plateau bleu de The Voice, un micro '
                'serre-tête au visage, entouré de ses handpans sur pieds, de son N’Goni 14 cordes et '
                'd’une calebasse. Logos The Voice et TF1 incrustés.',
                'Voir son audition à l’aveugle — « Kothbiro »',
                '« Ayub Ogada - Kothbiro - David Lesage | The Voice 2022 | Blind Audition » — le lecteur s’ouvre sur cette page.',
                '(max-width:900px) calc(100vw - 52px), 560px')}
  <div class="dlc-duo">
    {pic('tv-calebasse',
         'David Lesage seul sur le plateau de The Voice, penché sur une grande calebasse posée '
         'devant lui, les deux mains dessus, dans une lumière bleue ; à sa droite ses handpans '
         'sur pieds. Logos The Voice et TF1 incrustés sur l’image.',
         '(max-width:860px) calc(100vw - 52px), 500px',
         'Sur le plateau de The Voice : la calebasse, frappée au poing. Capture de la '
         'diffusion TF1.')}
    {pic('tv-ngoni',
         'David Lesage seul sur le plateau de The Voice, debout derrière deux handpans posés sur '
         'pieds, jouant le N’Goni 14 cordes tenu contre lui, dans une lumière bleue et verte. '
         'Logos The Voice et TF1 incrustés sur l’image.',
         '(max-width:860px) calc(100vw - 52px), 500px',
         'Le même dispositif, sur un plateau de télévision : handpans, N’Goni et déclencheurs. '
         'Capture de la diffusion TF1.')}
  </div>
</div></section>

<section class="dlc-block" id="scenes"><div class="wrap">
  <div class="dlc-h">Scènes &amp; festivals</div>
  <h2 class="sec-title">Là où ce répertoire a résonné</h2>
  <p>Ce n’est pas un projet en rodage. Le même répertoire s’est joué sur de grandes scènes de festival, en première partie d’un groupe de renommée internationale, dans des théâtres, des salles, et dans beaucoup de lieux de pierre — à des échelles et sous des acoustiques très différentes.</p>
  {scenes_stats()}
  <p class="dlc-srcnote">Décompte établi sur deux sources : l’agenda de l’artiste et l’historique de ses annonces publiques. Aucune des deux ne couvre l’intégralité de son parcours — le total réel est plus élevé. La saison 2026 est en cours.</p>

  <h3 class="dlc-sub">Les références</h3>
  {scenes_refs()}
  <p>David Lesage est passé par l’émission <i>The Voice</i> ; c’est à sa suite qu’il a été invité pour un concert solo en Côte d’Ivoire. À Marciac, les deux choses sont vraies et distinctes : c’est là qu’il s’est formé, au <b>collège de Jazz in Marciac</b>, et c’est là qu’il a joué, en <b>2018 et 2019</b>, avec le groupe « Résonance ».</p>
  <!-- PREMIERE PARTIE D'AMADOU & MARIAM (ajout du 14/08/2026). Placees juste
       apres la liste des references, dont la premiere entree est precisement
       celle-la : c'etait la reference la plus forte de la page et la seule sans
       aucune image.
       Traitement : les deux photos sont EMPILEES et non mises cote a cote. Leurs
       formats sont trop dissemblables (0,474 contre 1,738) : dans une grille a
       deux colonnes, la verticale aurait ecrase la paysage et laisse un grand
       vide sous elle. Empilees, chacune garde le traitement de son format.
       ⚠️ AUCUN NOM DE SALLE : le lieu n'est pas connu (source tronquee). On dit
       « septembre 2022 », rien de plus.
       ⚠️ AMADOU & MARIAM NE SONT PAS DANS LE CADRE : les legendes attribuent
       explicitement ce qu'on voit au set de David. Ne pas les reecrire. -->
  {pic('am-scene',
       'David Lesage seul au centre d’une grande scène de salle, la tête levée en train de chanter et une main en l’air, derrière un handpan clair posé sur un pied ; autour de lui son installation — pupitre, ordinateur, claviers, batterie — dans des faisceaux de lumière verte et blanche et de la fumée ; au premier plan, sa calebasse posée sur un tapis rond rouge.',
       'min(calc(100vw - 52px), 360px)',
       'Septembre 2022, en première partie d’Amadou &amp; Mariam : le set de David Lesage, seul en scène.',
       cls='dlc-fig dlc-tall')}
  {pic('am-salle',
       'Plan large depuis le fond de la salle : la scène éclairée en bleu et violet au loin, les instruments dessus, et au premier plan les silhouettes du public en contre-jour sur plusieurs rangs.',
       '(max-width:900px) calc(100vw - 52px), 860px',
       'La même soirée, vue du fond de la salle.',
       cls='dlc-fig dlc-wide', src_w=1400)}

  <h3 class="dlc-sub">Festivals, salles et théâtres</h3>
  {scenes_liste(SCENES_LIEUX)}
  {video_button('anako', VIDEO_ANAKO_ID,
                'Vignette de la vidéo : deux musiciens assis face à face sur une petite scène '
                'éclairée de rouge et d’orange, chacun penché sur un handpan, une batterie et '
                'des micros entre eux. Textes incrustés « Concert David Lesage », « ça '
                'ressemble à quoi ? / What does it look like? » et « Extrait Superpan Show '
                'Jérémy Nattagh ».',
                'Voir un extrait — concert à la Péniche Anako, Paris',
                '« Teaser Concert David Lesage — Extrait émission SuperPan Show de '
                'Jérémy Nattagh » — le lecteur s’ouvre sur cette page.',
                '(max-width:900px) calc(100vw - 52px), 560px')}

  <h3 class="dlc-sub">Les lieux de pierre</h3>
  <p>Abbayes, cloître, basilique, églises, chapelle : c’est le terrain où ce répertoire est le plus chez lui, et c’est exactement pour ces lieux-là qu’existe la <a href="#acoustique">version plus acoustique</a> du même programme.</p>
  {scenes_liste(SCENES_PIERRE)}

  {scenes_chrono()}
  <div class="dlc-duo">
    {pic('solo-festival',
         'David Lesage seul debout au centre d’une scène de festival en plein air, jouant deux handpans posés sur des pieds, devant une toile tendue multicolore et des faisceaux de lumière verte.',
         '(max-width:900px) calc(100vw - 52px), 340px',
         'En festival, seul en scène : handpans, déclencheurs et machines.')}
    {pic('abbaye',
         'Intérieur d’une abbaye en ruine, à ciel ouvert, éclairé en bleu et en orange ; au fond le plateau et ses instruments, au premier plan un public nombreux assis face à la scène.',
         '(max-width:900px) calc(100vw - 52px), 340px',
         'Abbaye à ciel ouvert d’Alet-les-Bains : jouer sans toit, avec l’acoustique de la pierre.')}
    {pic('eglise',
         'Vue d’ensemble d’une église transformée en salle de concert : David Lesage seul sur l’estrade au milieu de ses instruments, une figure cymatique projetée au-dessus de lui, et le public assis au sol sur des tapis parmi des bougies.',
         '(max-width:900px) calc(100vw - 52px), 340px',
         'En église : plateau bas, public assis, projection au-dessus de la scène.')}
  </div>
  {pic('rex',
       'Vue de scène du Grand Rex : deux artistes assis au sol au centre du plateau, face à une salle comble sur deux niveaux, dans les faisceaux de deux projecteurs en contre-jour.',
       '(max-width:900px) calc(100vw - 52px), 860px',
       'Au Grand Rex, devant 2 700 personnes.',
       cls='dlc-fig dlc-wide', credit=CREDIT_MAGYE)}
</div></section>

<div class="divider"></div>

<section class="dlc-block band" id="repertoire"><div class="wrap">
  <div class="dlc-h">Le répertoire</div>
  <h2 class="sec-title">« L’Alliance du Phoenix », et quelques reprises</h2>
  <p>Le concert puise dans les compositions de l’artiste — l’album <b>« L’Alliance du Phoenix »</b>, dix titres en deux opus, <b>100 % auto-produit</b> — et dans quelques reprises, ramenées au handpan et à la voix.</p>
  {REP_HINT}
  <div class="dlc-cols">
    <div class="dlc-card">
      <h3>Compositions</h3>
      <div class="sub">« L’Alliance du Phoenix », en deux opus</div>
      <ul>{''.join(rep_li(t, v) for t, v in COMPOSITIONS)}</ul>
    </div>
    <div class="dlc-card">
      <h3>Reprises</h3>
      <div class="sub">Au handpan et à la voix</div>
      <ul>{''.join(rep_li(t, v, a) for a, t, v in REPRISES)}</ul>
    </div>
  </div>
  <p>Cinq formules, empruntées au dossier de présentation, pour dire ce que cette musique cherche :</p>
  <ul class="dlc-cites">{''.join(f'<li>« {c} »</li>' for c in CITATIONS)}</ul>
  <div class="dlc-listen" id="studio">
    <div class="dlc-h">Les versions studio</div>
    <h3 class="sec-title" style="font-size:clamp(24px,3.4vw,34px)">Écouter les enregistrements</h3>
    <p>Les titres ci-dessus s’écoutent ici en <b>vidéo</b>. Leurs <b>versions studio</b> sont sur les plateformes : le profil Spotify de l’artiste réunit ses sorties et ses reprises, et les <b>deux opus</b> de « L’Alliance du Phoenix » sont réunis sur une même page chez son distributeur.</p>
    {SPOTIFY_HTML.format(sp=SPOTIFY_EMBED_ID)}
    <div class="cta">
      <a class="btn ghost" href="{SPOTIFY}" target="_blank" rel="noopener">Le profil Spotify ↗</a>
      <a class="btn ghost" href="{IMUSICIAN}" target="_blank" rel="noopener">Les deux opus chez son distributeur ↗</a>
    </div>
  </div>
  <!-- VIDEOS LIVE : deux ensembles tires de SES playlists (voir LIVE_CONCERTS /
       LIVE_YISHAMA). Chaque vignette ouvre le lecteur DANS la page : aucun
       nouvel onglet, aucune requete tierce avant le clic. -->
  <div class="dlc-listen" id="live">
    <div class="dlc-h">En vidéo</div>
    <h3 class="sec-title" style="font-size:clamp(24px,3.4vw,34px)">Deux ensembles de vidéos live</h3>
    <p>De quoi juger du live sans quitter cette page. Deux sélections tirées de ses propres playlists : les <b>concerts filmés</b>, et les <b>handpans acoustiques Yishama</b>. Chaque vignette ouvre le lecteur ici même.</p>
    <div class="lv-set">
      <h3>En concert</h3>
      <div class="lv-src">Six vidéos de sa playlist « Concerts Live David Lesage » — festivals, abbayes, chapelles.</div>
      {live_grid(LIVE_CONCERTS)}
    </div>
    <div class="lv-set">
      <h3>Handpans acoustiques Yishama</h3>
      <div class="lv-src">Six vidéos de sa playlist « Yishama Handpan David Lesage » — le même répertoire, sans les machines.</div>
      {live_grid(LIVE_YISHAMA)}
    </div>
  </div>
  <div class="dlc-listen">
    <div class="dlc-h">Écouter · Soutenir</div>
    <p>De quoi instruire un dossier sans nous attendre : le répertoire est en ligne sur les plateformes, et les captations de concert sur la chaîne de l’artiste.</p>
    <p><b>« L’Alliance du Phoenix »</b> représente un an de création et il est <b>100 % auto-produit</b> : dix compositions originales en deux opus, un album de reprises, le livret des paroles, une affiche A3 dédicacée. La boutique de l’association le diffuse en téléchargement ou sur une clé USB en bois de vingt-neuf titres — un support à connaître si vous cherchez un objet pour votre billetterie ou votre boutique de salle.</p>
    <div class="cta">
      <a class="btn ghost" href="{YT_CHAINE}" target="_blank" rel="noopener">La chaîne YouTube de David Lesage ↗</a>
      <a class="btn ghost" href="{ALBUM_BOUTIQUE}" target="_blank" rel="noopener">Commander l’album — téléchargement ou clé USB ↗</a>
    </div>
  </div>
</div></section>

<!-- VERSION PLUS ACOUSTIQUE (ajout du 13/08/2026, demande de David).
     ⚠️ AUCUNE INFORMATION PRECISE N'EXISTE sur cette formule : ni duree, ni
     instrumentarium arrete, ni patch, ni contrainte de plateau. On n'en invente
     AUCUNE, et on ne recycle SURTOUT PAS les chiffres de la fiche technique de
     la configuration principale (9 entrees, 4x5 m, Bose S1+Sub1) : ils ne
     valent pas pour cette formule. Le texte dit exactement ce qu'on sait — la
     meme musique tiree vers les handpans ACOUSTIQUES Yishama, la voix, la
     calebasse et le N'Goni, avec moins d'electronique — et renvoie a un
     echange. NE RIEN AJOUTER ICI qui ressemble a une fiche ou a un engagement. -->
<section class="dlc-block" id="acoustique"><div class="wrap">
  <div class="dlc-h">Autre formule</div>
  <h2 class="sec-title">Une version plus acoustique</h2>
  <div class="dlc-split">
    <div>
      <p>Le même répertoire existe dans une <b>direction plus acoustique</b> : porté d’abord par les <b>handpans acoustiques Yishama</b>, la voix, la calebasse et le <b>N’Goni</b> — avec beaucoup moins d’électronique.</p>
      <p>C’est une <b>option de programmation</b>, pensée pour les lieux où la pierre, le bois et le silence font déjà la moitié du travail : églises, chapelles, abbayes, lieux patrimoniaux, petites jauges assises. Ce sont exactement les <a href="#scenes">lieux de pierre déjà joués</a> — abbaye d’Alet-les-Bains, cloître de Saint-Geniez-d’Olt, basilique et église Saint-Nazaire de Carcassonne.</p>
      <p>Cette formule se construit <b>avec vous</b> : sa durée, son instrumentarium exact et ses besoins techniques ne sont pas figés et se décident au cas par cas — la <a href="#technique">fiche technique</a> publiée plus bas est celle de la configuration principale, elle ne s’applique pas telle quelle ici.</p>
      <div class="cta" style="margin-top:22px"><a class="btn ghost" href="{MAILTO_ACOUSTIQUE}">Parler de la version acoustique</a></div>
    </div>
    {live_feature('yishama-angel-voice', '81yKSB3dIK0',
                  'Vignette : l’artiste assis devant une grande baie vitrée, penché sur un '
                  'handpan acoustique en bronze posé sur un pied, une main levée ; '
                  'incrustations « Yishama Pantam » et « Angel Voice ».',
                  'Le handpan acoustique, seul',
                  '« Angel Voice handpan @yishama_official » — le lecteur s’ouvre sur cette page.',
                  '(max-width:860px) calc(100vw - 52px), 340px')}
  </div>
  <!-- LES DEUX PHOTOS D'EVERNESS (ajout du 14/08/2026). Elles sont ICI et pas
       ailleurs parce que c'est ici qu'elles argumentent : jusqu'a present cette
       section ne montrait qu'une vignette de video ou le handpan acoustique est
       seul, sans personne. La premiere donne enfin une PHOTO DE SCENE ou David
       joue les handpans ACOUSTIQUES Yishama ; la seconde donne l'echelle du
       public. C'est le reequilibrage demande par David — le hero, lui, montre le
       Neotone.
       ⚠️ RESOLUTION : 'yishama-solo' plafonne a 900 px. La grille .dlc-duo la
       borne a 504 px d'affichage : c'est la seule largeur ou elle reste nette.
       NE PAS la passer en .dlc-wide (860 px) ni en hero.
       ⚠️ Le texte ci-dessus ne dit PAS que ces concerts etaient « la version
       acoustique » : rien ne l'etablit. Les legendes decrivent la scene et les
       instruments, rien de plus. -->
  <div class="dlc-duo">
    {pic('yishama-solo',
         'David Lesage seul debout au centre d’une grande scène en plein air, les mains sur deux handpans acoustiques Yishama posés sur pieds ; derrière lui une immense toile de fils tendus multicolores traversée de faisceaux de lumière verte, devant lui une calebasse sur un tapis rond rouge, et sur la droite des toiles peintes et une cymbale.',
         '(max-width:632px) calc(100vw - 52px), (max-width:1080px) calc(50vw - 36px), 504px',
         'Les deux handpans acoustiques Yishama sur pieds, sur la grande scène de l’Everness Festival, en Hongrie.')}
    {pic('vue-de-scene',
         'Vue prise depuis la scène, au grand angle : au premier plan le plateau et ses instruments, David Lesage assis au sol de dos derrière une calebasse et, derrière lui, une violoncelliste sur une chaise ; à droite, un public nombreux assis dans l’herbe sous de grandes voiles d’ombrage.',
         '(max-width:632px) calc(100vw - 52px), (max-width:1080px) calc(50vw - 36px), 504px',
         'Vue depuis la scène : le plateau, la calebasse, un violoncelle — et le public à quelques mètres.',
         src_w=1400)}
  </div>
</div></section>

<div class="divider"></div>

<section class="dlc-block band" id="option"><div class="wrap">
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

<section class="dlc-block band" id="technique"><div class="wrap">
  <div class="dlc-h">Fiche technique</div>
  <h2 class="sec-title">Ce qu’il faut pour l’accueillir</h2>
  <p>L’essentiel est ici, pour que vous puissiez évaluer la faisabilité sans attendre. David Lesage <b>tend vers une simplification de son setup</b> : la <b>configuration à 9 entrées</b> est celle qu’il privilégie, et c’est celle à retenir par défaut. La configuration étendue reste possible sur les plateaux qui s’y prêtent.</p>
  <p>Tous les instruments sont accordés en <b>La 432 Hz</b>.</p>

  <h3 class="dlc-sub">Les deux configurations</h3>
  <div class="dlc-cols">
    <div class="dlc-conf reco">
      <span class="dlc-tag">Configuration de référence</span>
      <h4>9 entrées</h4>
      <p>Voix, handpan électronique, Wavedrum, déclencheurs (kick, caisse claire, hi-hat), N’Goni 14 cordes, calebasse, sanzula, et le son de l’ordinateur. C’est la version que l’artiste privilégie, en salle comme en festival.</p>
    </div>
    <div class="dlc-conf">
      <span class="dlc-tag alt">Option étendue</span>
      <h4>Jusqu’à 14 entrées</h4>
      <p>La même base, à laquelle s’ajoutent 2 à 3 <b>handpans acoustiques</b> repris au micro — un micro col de cygne et un micro contact par instrument — et, le cas échéant, les entrées des invités : voix d’Iris Chasles, tambour chamanique, cordes.</p>
    </div>
  </div>

  <h3 class="dlc-sub">Patch d’entrées — configuration à 9 entrées</h3>
  <div class="dlc-tw">
    <table class="dlc-tab">
      <caption>Micros et boîtes de direct</caption>
      <thead><tr><th scope="col">N°</th><th scope="col">Source</th><th scope="col">Micro ou DI</th></tr></thead>
      <tbody>{''.join(f'<tr><th scope="row">{n}</th><td data-label="Source">{s}</td><td data-label="Micro ou DI">{m}</td></tr>' for n, s, m in PATCH_9)}</tbody>
    </table>
  </div>

  <h3 class="dlc-sub">Le plateau</h3>
  <dl class="dlc-id">{''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in PLATEAU)}</dl>

  <h3 class="dlc-sub">Les retours de scène</h3>
  <dl class="dlc-id">{''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in RETOURS)}</dl>

  <div class="dlc-duo">
    {pic('setup-dessus',
         'Vue plongeante du setup installé sur deux tapis persans : un handpan électronique et un pad de percussion sur pieds, une loop station, deux ordinateurs portables ouverts, une tablette, deux enceintes de retour posées au sol et une calebasse.',
         '(max-width:860px) calc(100vw - 52px), 500px',
         'Le setup vu du dessus : tapis rond, retours derrière l’artiste, machines à portée de main.')}
    {pic('plateau',
         'Grande salle claire à colonnes et hautes fenêtres, vue depuis la scène : au premier plan le plateau installé sur des tapis avec handpans, ordinateurs, calebasse et enceintes de retour, et au fond le parquet vide de la salle.',
         '(max-width:860px) calc(100vw - 52px), 500px',
         'Un plateau installé avant l’ouverture des portes — 4 m × 5 m suffisent.')}
  </div>

  <h3 class="dlc-sub">Demandé à l’organisateur</h3>
  <div class="dlc-cols">
    <div class="dlc-card">
      <h4>Matériel et pieds</h4>
      <div class="sub">À fournir sur place, ou équivalent supérieur</div>
      <ul class="dlc-list">{''.join(f'<li>{x}</li>' for x in DEMANDE)}</ul>
    </div>
    <div class="dlc-card">
      <h4>Apporté par l’artiste</h4>
      <div class="sub">Rien à prévoir de votre côté</div>
      <ul class="dlc-list">{''.join(f'<li>{x}</li>' for x in APPORTE)}</ul>
    </div>
  </div>

  <div class="dlc-note">
    <div class="dlc-h">Contact technique</div>
    <p><b>David Lesage</b> — <a href="tel:{TEL_TECH}">{TEL_TECH_TXT}</a> (téléphone, WhatsApp, Telegram) · <a href="mailto:{MAIL_TECH}">{MAIL_TECH}</a></p>
    <p>Il répond directement à votre ingénieur du son et à la personne en charge de la projection.</p>
  </div>

  <div class="dlc-prog">
    <h3>La fiche technique complète</h3>
    <p>Plans de scène détaillés, patchs des autres configurations, feuille d’accordage du N’Goni, conditions d’assurance et de transport : tout cela figure dans la fiche technique complète, que nous vous adressons sur demande.</p>
    <div class="cta" style="margin-top:22px"><a class="btn" href="{MAILTO_FT}">Demander la fiche technique complète</a></div>
  </div>
</div></section>

<div class="divider"></div>

<section class="dlc-block" id="programmer"><div class="wrap">
  <div class="dlc-h">Programmation</div>
  <h2 class="sec-title">Programmer ce concert</h2>
  <p>La production est portée par <b>Résonances Productions</b>, association loi 1901 dédiée à l’art du spectacle vivant. Écrivez-nous : nous vous répondons avec le dossier de présentation et les précisions adaptées à votre lieu, à votre jauge et à vos dates.</p>
  <div class="dlc-prog">
    <h3>Un mot suffit pour commencer</h3>
    <p>Dites-nous simplement qui vous êtes, le lieu, et la période envisagée.</p>
    <div class="cta" style="margin-top:22px"><a class="btn" href="{MAILTO_PROG}">Programmer ce concert</a><a class="btn ghost" href="{MAILTO_DOSSIER}">Demander le dossier</a></div>
    <p style="margin-top:20px"><a href="mailto:{MAIL}">{MAIL}</a></p>
  </div>
  <!-- AFFICHE OFFICIELLE (ajout du 14/08/2026). Placee EN FIN DE PAGE, dans la
       section de programmation, parce que c'est la qu'elle est un objet de
       communication et non une photo de scene : la personne qui lit ce bloc est
       celle qui aura a annoncer la date.
       ⚠️ Elle porte deja le logo d'artiste en haut a droite : elle est donc
       tenue A DISTANCE du logo pose en tete de la section #parcours — les mettre
       cote a cote ferait doublon.
       ⚠️ Format PORTRAIT (natif 3508x4961) : .dlc-portrait la borne a 420 px,
       elle n'entre dans aucune grille de photos de scene.
       ⚠️ La legende ne promet RIEN (ni fichier haute definition, ni personnalisation
       de l'affiche) : aucun engagement de ce genre n'a ete valide. -->
  {pic('affiche',
       'Affiche « EN CONCERT » de David Lesage : portrait de profil, yeux baissés, longs cheveux éclairés d’orange, devant un handpan vu de face dans une brume dorée ; en haut à droite, le logo « David Lesage » ; au centre, le titre « EN CONCERT » souligné d’un trait doré, sur fond noir.',
       'min(calc(100vw - 52px), 420px)',
       'L’affiche officielle du concert.',
       cls='dlc-fig dlc-portrait', src_w=900)}
  <div class="dlc-cross">
    <p>Vous cherchez plutôt une soirée à Paris ? Le même répertoire se joue aussi en version intimiste, au Nid, dans le 20<sup>e</sup> arrondissement : <a href="/concerts-david-lesage">les concerts de David Lesage au Nid</a>.</p>
  </div>
</div></section>

<a class="totop" href="#top" aria-label="Revenir en haut de la page">↑</a>
{LIGHTBOX_HTML.format(secours=VIDEO_TV_SECOURS)}
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
{LIGHTBOX_JS}
{SPOTIFY_JS}
</body></html>"""

HTML = mobile_nav.inject(HTML)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, 'david-lesage-en-concert')
os.makedirs(OUT_DIR, exist_ok=True)
OUT = os.path.join(OUT_DIR, 'index.html')
open(OUT, 'w', encoding='utf-8').write(HTML)
print('WROTE', OUT, round(len(HTML) / 1024), 'KB')
