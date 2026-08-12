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
VIDEO (revu le 04/08/2026) : la video de cymatique s'ouvre dans un LECTEUR EN
SURIMPRESSION SUR LA PAGE. Consigne de David : « le but est que l'utilisateur
reste sur le site, et ce sur TOUTES les videos du site » -> plus AUCUN lien
sortant vers YouTube pour une video. Tant que personne ne clique, aucun script
ni cookie tiers n'est charge (l'iframe nait sans src) ; au clic la src pointe
vers youtube-nocookie.com ; a la fermeture elle est VIDEE. La vignette n'existe
qu'en 480x360 : ne jamais l'afficher plus large (cf. .cdl-video).
La seconde video de David (chant des voyelles avec CymaScope, note par note)
fait partie du programme PAYANT « Les Trois Piliers » : NE PAS l'integrer ni la
lier.
MANQUENT : des photos dediees d'un concert SOLO AU NID (David seul, public au
sol).
FONTAINE — TRANCHE PAR DAVID le 04/08/2026 : « j'ai besoin de simplifier et de
garder la Melusine au Nid ». La fontaine est donc presentee comme INSTALLEE AU
NID (elle n'accompagne pas les tournees). La 2e photo (fontaine-melusine-*) a
en revanche ete prise AILLEURS (salle voutee en pierre, evenement exterieur) :
sa legende le dit et ne nomme ni ne suggere le Nid. NE PAS la relegender « au
Nid ».

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
# --- Video : LECTEUR EN SURIMPRESSION SUR LA PAGE ---------------------------
# Regle posee par David (04/08/2026) : « le but est que l'utilisateur reste sur le
# site, et ce sur TOUTES les videos du site » -> plus aucun lien sortant vers
# YouTube pour une video. La vignette est un BOUTON qui ouvre un lecteur dans la
# page (voir LIGHTBOX_HTML / LIGHTBOX_JS).
# Aucun script tiers n'est charge avant le clic : l'<iframe> nait sans src, et la
# src n'est posee qu'au clic — puis VIDEE a la fermeture (sinon le son continue).
# Domaine youtube-nocookie.com : moins de traceurs que youtube.com.
# Titres verifies par oEmbed le 04/08/2026 (titres EXACTS de la chaine).
VIDEO_CYMA_ID = 'mPUrsusmYyQ'
# Titre exact retourne par oEmbed (conserve en commentaire : le <iframe> du
# lecteur porte desormais un titre generique, il sert plusieurs videos) :
#   « Chant des voyelles live concert David Lesage #cymatics #cymascope #cymatique »
# Filet de securite UNIQUEMENT : si l'iframe est bloquee (extension, navigateur
# restrictif), sans ce lien la personne est coincee devant un cadre noir. Il vit
# DANS le lecteur, en petit, et n'est jamais le chemin principal.
VIDEO_CYMA_SECOURS = f'https://youtu.be/{VIDEO_CYMA_ID}'
# Peniche Anako, Paris (ajout du 13/08/2026) : « Teaser Concert David Lesage —
# Extrait emission SuperPan Show de @JeremyNattagh ». Video publique, verifiee.
# Elle sert la PREUVE PARISIENNE de cette page : on l'a deja entendu a Paris,
# ailleurs qu'au Nid. Meme mecanique que les autres videos (.ytlink + data-yt
# -> lecteur en surimpression, youtube-nocookie, aucun nouvel onglet).
# ⚠️ Le lieu vient de David lui-meme, pas du titre de la video. Et la vignette
# montre DEUX musiciens : on ne decrit donc pas la video comme un concert solo,
# et on n'affirme rien sur qui joue quoi ce soir-la.
VIDEO_ANAKO_ID = '0jbAjB-Swmk'
MELUSINE = 'https://aquadynauroville.com/site/accueil-25/fontaine-melusine/'

# --- Ecouter / soutenir -----------------------------------------------------
# Liens de PLATEFORMES (pas des videos) : un nouvel onglet est ici legitime.
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
# URL nettoyee : le segment « intl-fr » est une redirection regionale et
# « autoplay_ok=1 » un parametre de session — inutiles dans un lien permanent.
SPOTIFY = 'https://open.spotify.com/artist/7zEAQJbalBFj8XNHrcqdbK'
# Boutique HelloAsso de l'association : l'album « L'Alliance du Phoenix ».
# ⚠️ AUCUN tarif sur la page (regle du site) : c'est la boutique qui les porte.
ALBUM_BOUTIQUE = ('https://www.helloasso.com/associations/resonances-productions/boutiques/'
                  'acheter-album-l-alliance-du-phoenix-david-lesage')

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
    # Peniche Anako, Paris (ajout du 13/08/2026). Vignette publiee par la chaine
    # pour la video 0jbAjB-Swmk (maxresdefault 1280x720, vrai 16:9), rapatriee
    # en local. Le fichier vit dans /img/concert-scene/ : il sert AUSSI a
    # /david-lesage-en-concert, on ne duplique pas les octets.
    # Bornee par .cdl-video (480 px max) -> jamais affichee au-dela du natif.
    'anako': ('concert-scene', 'peniche-anako-teaser', [480, 900, 1280], 1280, 720),
    # --- LOGO D'ARTISTE DE DAVID LESAGE (ajout du 13/08/2026) ----------------
    # ⚠️ Logo de L'ARTISTE, PAS de Resonances Productions. Il identifie David
    # Lesage en tete de la section « L'artiste » et ne doit JAMAIS remplacer le
    # nom de l'association dans la barre de navigation, ni servir de logo au
    # site, ni de favicon.
    # Source : dossier Drive de David, 7 declinaisons PNG 3000x2120 ; retenue =
    # « logo beige-etoilé » (lettres creme #fbdaa6 ~ --gold2, anneau dore, eclat
    # en etoile), la plus lisible de la famille doree sur le fond nuit #0e0f24.
    # Recadre sur son alpha (2578x1943) puis 480 / 900 px ; PNG et pas JPEG,
    # sinon la transparence devient un rectangle blanc.
    'logo': ('logo', 'david-lesage-logo', [480, 900], 900, 678),
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


def logo_fig(cls='cdl-logo', sizes='280px'):
    """Logo d'artiste de David Lesage : WebP + repli PNG.

    PNG et pas JPEG : le logo est transparent. Jamais affiche au-dela de 280 px
    (natif 2578 px avant reduction). `alt` = « David Lesage » : c'est le texte
    que le logo dessine.
    ⚠️ Logo de L'ARTISTE, pas de l'association — rien a voir avec la barre de
    navigation, qui garde le nom « Resonances Productions »."""
    folder, base, widths, w, h = CDL_PHOTOS['logo']
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

    Ce n'est plus un lien : rien ne s'ouvre dans un nouvel onglet ni dans
    l'application YouTube. Tant que personne ne clique, aucune requete n'est
    faite vers un domaine tiers (l'<iframe> du lecteur nait sans src).
    Le triangle de lecture est purement CSS et aria-hidden : le libelle du
    bouton reste explicite pour les lecteurs d'ecran."""
    folder, base, widths, w, h = CDL_PHOTOS[key]
    root = f'/img/{folder}/{base}'
    webp = ', '.join(f'{root}-{x}.webp {x}w' for x in widths)
    jpg = ', '.join(f'{root}-{x}.jpg {x}w' for x in widths)
    img = (f'<picture><source type="image/webp" srcset="{webp}" sizes="{sizes}">'
           f'<img src="{root}-{widths[-1]}.jpg" srcset="{jpg}" sizes="{sizes}" '
           f'width="{w}" height="{h}" loading="lazy" decoding="async" alt="{alt}"></picture>')
    return (f'<button type="button" class="cdl-video ytlink" data-yt="{vid}">'
            f'<figure class="cdl-fig"><span class="shot">{img}'
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
    # Pas de <span> autour du titre : `.cdl-card li span` le passerait en dore
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
    return (f'<button type="button" class="cdl-video ytlink" data-yt="{vid}">'
            f'<figure class="cdl-fig"><span class="shot">{img}'
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

# ============================================================================
# « LA OU CE REPERTOIRE A RESONNE » — mise a jour du 13/08/2026
# ============================================================================
# ⚠️ TRAITEMENT VOLONTAIREMENT LEGER SUR CETTE PAGE. Le public d'ici est un
# particulier parisien qui hesite a venir un soir : il ne lit PAS un CV, et une
# chronologie de 69 dates le ferait fuir. La preuve de parcours complete (ligne
# chiffree, references, lieux de pierre, chronologie annee par annee dans un
# <details>) vit sur /david-lesage-en-concert, page programmateurs.
# Ici : SIX references qui rassurent, une phrase de volume en mots et pas en
# tableau, et une preuve PARISIENNE (la Peniche Anako, en video). Rien de plus.
# Si on est tente d'ajouter une septieme ligne : ne pas le faire.
#
# Meme regle de fond que sur l'autre page : aucune date, aucun lieu, aucun
# chiffre invente ; le seul chiffre de public autorise est « 2 700 personnes au
# Grand Rex » (confirme par David).
SCENES = [
    ('Le Grand Rex, Paris — devant 2 700 personnes', 'France'),
    ('Sziget Festival', 'Hongrie'),
    ('Everness Festival', 'Hongrie'),
    ('Jazz in Marciac', 'France'),
    ('Abbaye à ciel ouvert d’Alet-les-Bains', 'France'),
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
    ('#acoustique', 'Certains soirs, plus acoustique'),
    ('#invitee', 'Une invitée, certains soirs'),
    ('#artiste', 'L’artiste'),
    ('#repertoire', 'Le répertoire'),
    ('#studio', 'Écouter les versions studio'),
    ('#live', 'Voir deux ensembles de vidéos live'),
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
/* ===== Titres du repertoire ecoutables SUR la page =====
   Un titre relie devient un <button class="ytlink"> : le gestionnaire delegue
   deja en place (.ytlink + data-yt) ouvre le lecteur en surimpression. Jamais
   de lien sortant ici. Les titres sans video gardent EXACTEMENT le meme style
   via .rep-t : seule l'icone ▸ distingue ce qui s'ecoute.
   .rep-t doit surcharger `.cdl-card li span` (qui met le sous-titre en dore) :
   la specificite d'une classe l'emporte sur celle d'un element, donc OK.
   Hauteur de rangee = 7 + 30 + 7 = 44 px : cible tactile respectee. */
.cdl-card li .rep-t{display:flex;align-items:center;gap:9px;width:100%;min-height:30px;
  color:#d7d4ea;font-family:inherit;font-size:15.5px;letter-spacing:normal;line-height:1.5;
  background:none;border:0;padding:0;margin:0;text-align:left}
.cdl-card li button.rep-t{cursor:pointer;transition:color .18s}
.cdl-card li button.rep-t:hover,.cdl-card li button.rep-t:focus-visible{color:#fff}
.pico{flex:0 0 auto;display:inline-flex;align-items:center;justify-content:center;
  width:19px;height:19px;border-radius:50%;border:1px solid rgba(216,178,90,.5);
  color:var(--gold);font-size:9px;line-height:1;padding-left:1px;
  transition:background .18s,color .18s,border-color .18s}
.cdl-card li button.rep-t:hover .pico,.cdl-card li button.rep-t:focus-visible .pico{
  background:var(--gold);border-color:var(--gold);color:#1a1608}
/* `.cdl-block p{color:#d7d4ea}` (0,1,1) battait `.rep-hint` (0,1,0) : la mention
   restait couleur de corps de texte. Selecteur prefixe -> (0,2,0), il gagne. */
.cdl-block .rep-hint{display:flex;align-items:center;gap:8px;flex-wrap:wrap;
  color:var(--gold2);font-size:14.5px;font-style:italic;margin-top:14px}
/* citations du dossier */
.cdl-cites{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px;max-width:880px;list-style:none}
.cdl-cites li{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:17.5px;line-height:1.4;background:rgba(216,178,90,.08);border:1px solid var(--line);border-radius:30px;padding:8px 20px}
/* ===== Boire l'eau du concert =====
   Section volontairement PLAIN (pas .band) pour ne pas casser l'alternance
   band / non-band des sections suivantes : elle prend a la place un halo bleu
   qui lui est propre. Encadree de deux .divider comme les autres. */
.cdl-water{background:radial-gradient(760px 500px at 86% 4%,rgba(70,132,214,.17),transparent 64%),radial-gradient(620px 420px at 4% 98%,rgba(143,122,209,.11),transparent 62%)}
.cdl-duo{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px;margin-top:30px;max-width:820px;align-items:start}
/* ===== Vignette video : BOUTON qui ouvre le lecteur DANS LA PAGE =====
   La source ne fait que 480 px de large : on ne l'agrandit JAMAIS au-dela.
   C'est un <button> (et non plus un lien) : on remet donc a plat les styles
   par defaut du navigateur, sinon il herite d'un fond gris et d'un cadre. */
.cdl-video{display:block;max-width:480px;width:100%;margin-top:26px;background:none;border:0;padding:0;color:inherit;font:inherit;text-align:left;cursor:pointer}
.cdl-video figure{margin:0}
.cdl-video .shot{display:block;position:relative;line-height:0}
.cdl-video .play{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:62px;height:62px;border-radius:50%;background:rgba(11,12,30,.72);border:1px solid rgba(240,209,138,.62);display:flex;align-items:center;justify-content:center;transition:transform .2s,background .2s}
.cdl-video .play::before{content:"";width:0;height:0;border-left:17px solid var(--gold2);border-top:11px solid transparent;border-bottom:11px solid transparent;margin-left:5px}
.cdl-video:hover .play{background:rgba(11,12,30,.9);transform:translate(-50%,-50%) scale(1.06)}
.cdl-video figcaption{display:flex;flex-direction:column;gap:2px;justify-content:center;min-height:44px}
.cdl-video .vlabel{color:var(--gold2);font-size:16px;text-decoration:underline;text-decoration-color:rgba(216,178,90,.42);text-underline-offset:3px}
.cdl-video:hover .vlabel{color:#fff}
.cdl-video .vsub{color:var(--muted);font-size:13.5px}
/* ===== Logo d'artiste de David Lesage (ajout du 13/08/2026) ================
   ⚠️ Logo de L'ARTISTE, pas de l'association : il identifie David Lesage en
   tete de la section qui parle de lui. Il ne remplace RIEN dans la barre de
   navigation et n'est pas le logo du site. Natif 2578x1943 reduit a 900 px,
   plafonne a 280 px d'affichage : jamais agrandi au-dela du natif. */
.cdl-logo{margin:22px 0 0;max-width:280px}
.cdl-logo img{display:block;width:100%;height:auto}
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
/* meme traitement pour le lien en ligne de la section « acoustique » :
   17px * 1.75 = 29.75 -> 24px de boite + 2 x 11 = 46 px, cible respectee. */
#acoustique p a{display:inline-block;padding:11px 0}
/* meme traitement pour le lien partenaire de la section « eau » : cible >= 44 px
   (17px * 1.75 = 29.75 + 2 x 11 = 51.75). */
.cdl-water p a{display:inline-block;padding:11px 0}
/* ===== bloc « Ecouter · Soutenir » (plateformes + boutique de l'association) ==
   Volontairement SOBRE : trois boutons fantomes, pas trois pavos dores — ce ne
   sont pas les appels a l'action principaux de la page (« Reserver ma place » ;
   trois boutons dores auraient concurrence le seul qui compte ici)
   le reste). Sous 560 px les boutons passent en pleine largeur pour rester
   confortablement cliquables. */
.cdl-listen{margin-top:36px;max-width:820px;border-top:1px solid var(--line);padding-top:26px}
.cdl-listen p{max-width:none;font-size:16px}
.cdl-listen .cta{margin-top:20px}
.cdl-listen .btn{font-size:15px;padding:12px 22px}
@media(max-width:560px){.cdl-listen .btn{width:100%}}
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
.cdl-block .spf-note{color:var(--muted);font-size:14px;font-style:italic;margin-top:12px;max-width:640px}
""" + LIGHTBOX_CSS

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
  <p class="body">Ce sont des concerts <b>intimistes, à petite jauge</b> : on y est en tout petit comité, à taille humaine — jamais dans une salle, toujours dans une pièce.</p>
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
      <p><b>La jauge est volontairement petite.</b> Le Nid n’est pas une salle de spectacle : c’est une pièce, et le nombre de places suit la pièce — pas l’inverse. Ces soirées se jouent donc <b>en tout petit comité</b>, à taille humaine. C’est un choix, pas une contrainte : personne n’est au fond, personne ne regarde de loin.</p>
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
      {video_button('video', VIDEO_CYMA_ID,
                    'Vignette de la vidéo : vue grand-angle d’un concert, une figure de cymatique '
                    'projetée sur l’écran derrière les instruments ; titre incrusté sur l’image, '
                    '« Le chant des voyelles, live concert David Lesage — Cymatique en temps réel ».',
                    'Lancer la vidéo',
                    '« Chant des voyelles live concert David Lesage » — le lecteur s’ouvre sur '
                    'cette page.',
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
         'Gros plan sur la fontaine, lors d’une précédente installation à l’occasion '
         'd’un événement extérieur.')}
  </div>
  <p>Ce dispositif existe grâce à un partenariat avec <b>AquaDyn Auroville</b> et <b>Rebirth Water Group</b>, concepteurs de la <a href="{MELUSINE}" target="_blank" rel="noopener">fontaine Mélusine ↗</a> — un appareil bâti autour du son et de la lumière, dont ses concepteurs revendiquent le brevet. L’exemplaire <b>installé au Nid</b> a été spécialement modifié pour recevoir le signal audio du concert.</p>
  <p>Sur la pancarte posée à côté, un seul mot fait office de mode d’emploi : <b>« expérimente »</b>. Rien ne vous est promis, rien ne vous est démontré : on vous tend un gobelet, et vous en faites ce que vous voulez — le boire, ou passer votre tour.</p>
</div></section>

<div class="divider"></div>

<!-- FORMULE PLUS ACOUSTIQUE (ajout du 13/08/2026, demande de David).
     ⚠️ AUCUNE INFORMATION PRECISE N'EXISTE sur cette formule : ni duree, ni
     instrumentarium arrete, ni contrainte technique. On n'en invente donc
     AUCUNE. Le texte dit exactement ce qu'on sait : la meme musique, tiree vers
     les handpans ACOUSTIQUES Yishama, la voix, la calebasse et le N'Goni, avec
     moins d'electronique — et le fait que ce n'est pas annonce date par date.
     NE RIEN AJOUTER ICI qui ressemble a une garantie ou a une fiche. -->
<section class="cdl-block" id="acoustique"><div class="wrap">
  <div class="cdl-h">Une autre couleur</div>
  <h2 class="sec-title">Certains soirs, plus acoustique</h2>
  <div class="cdl-split">
    <div>
      <p>La même musique peut se jouer dans une <b>couleur plus acoustique</b> : les <b>handpans acoustiques Yishama</b> au premier plan, la voix, la calebasse et le N’Goni — et les machines qui s’effacent presque.</p>
      <p>Ce n’est pas une autre soirée. C’est la même, tirée vers le métal nu, le bois et la peau : moins d’électronique, plus de résonance de la pièce.</p>
      <p>Cette direction se cherche encore, et elle n’est pas annoncée date par date. Si c’est ce que vous venez chercher, <a href="mailto:contact@resonancesproductions.org?subject=Concert%20de%20David%20Lesage%20—%20version%20acoustique">dites-le nous</a> : nous vous dirons ce qui est prévu pour la prochaine date.</p>
    </div>
    {live_feature('yishama-angel-voice', '81yKSB3dIK0',
                  'Vignette : l’artiste assis devant une grande baie vitrée, penché sur un '
                  'handpan acoustique en bronze posé sur un pied, une main levée ; '
                  'incrustations « Yishama Pantam » et « Angel Voice ».',
                  'Le handpan acoustique, seul',
                  '« Angel Voice handpan @yishama_official » — le lecteur s’ouvre sur cette page.',
                  '(max-width:860px) calc(100vw - 52px), 340px')}
  </div>
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
  {logo_fig()}
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
  <p>La soirée puise dans ses compositions — l’album <b>« L’Alliance du Phoenix »</b>, dix titres en deux opus — et dans quelques reprises, ramenées au handpan et à la voix.</p>
  {REP_HINT}
  <div class="cdl-cols">
    <div class="cdl-card">
      <h3>Compositions</h3>
      <div class="sub">« L’Alliance du Phoenix », en deux opus</div>
      <ul>{''.join(rep_li(t, v) for t, v in COMPOSITIONS)}</ul>
    </div>
    <div class="cdl-card">
      <h3>Reprises</h3>
      <div class="sub">Au handpan et à la voix</div>
      <ul>{''.join(rep_li(t, v, a) for a, t, v in REPRISES)}</ul>
    </div>
  </div>
  <p>Cinq formules, empruntées au dossier de présentation du spectacle, pour dire ce que cette musique cherche :</p>
  <ul class="cdl-cites">{''.join(f'<li>« {c} »</li>' for c in CITATIONS)}</ul>
  <div class="cdl-listen" id="studio">
    <div class="cdl-h">Les versions studio</div>
    <h3 class="sec-title" style="font-size:clamp(24px,3.4vw,34px)">Écouter les enregistrements</h3>
    <p>Les titres ci-dessus s’écoutent ici en <b>vidéo</b>. Leurs <b>versions studio</b>, elles, vivent sur les plateformes : le profil Spotify de David Lesage réunit ses sorties et ses reprises, et les <b>deux opus</b> de « L’Alliance du Phoenix » sont réunis sur une même page chez son distributeur.</p>
    {SPOTIFY_HTML.format(sp=SPOTIFY_EMBED_ID)}
    <div class="cta">
      <a class="btn ghost" href="{SPOTIFY}" target="_blank" rel="noopener">Le profil Spotify ↗</a>
      <a class="btn ghost" href="{IMUSICIAN}" target="_blank" rel="noopener">Les deux opus chez son distributeur ↗</a>
    </div>
  </div>
  <!-- VIDEOS LIVE : deux ensembles tires de SES playlists (voir LIVE_CONCERTS /
       LIVE_YISHAMA). Chaque vignette ouvre le lecteur DANS la page : aucun
       nouvel onglet, aucune requete tierce avant le clic. -->
  <div class="cdl-listen" id="live">
    <div class="cdl-h">En vidéo</div>
    <h3 class="sec-title" style="font-size:clamp(24px,3.4vw,34px)">Deux ensembles de vidéos live</h3>
    <p>Deux sélections tirées de ses propres playlists : les <b>concerts filmés</b>, et les <b>handpans acoustiques Yishama</b>. Chaque vignette ouvre le lecteur ici même — vous ne quittez pas cette page.</p>
    <div class="lv-set">
      <h3>En concert</h3>
      <div class="lv-src">Six vidéos de sa playlist « Concerts Live David Lesage ».</div>
      {live_grid(LIVE_CONCERTS)}
    </div>
    <div class="lv-set">
      <h3>Handpans acoustiques Yishama</h3>
      <div class="lv-src">Six vidéos de sa playlist « Yishama Handpan David Lesage » — la même musique, sans les machines.</div>
      {live_grid(LIVE_YISHAMA)}
    </div>
  </div>
  <div class="cdl-listen">
    <div class="cdl-h">Écouter · Soutenir</div>
    <p>Vous pouvez écouter ce répertoire avant de venir — et repartir avec, après.</p>
    <p><b>« L’Alliance du Phoenix »</b> a demandé un an de création et il est <b>100 % auto-produit</b> : dix compositions originales en deux opus, un album de reprises, le livret des paroles, une affiche A3 dédicacée. L’association le diffuse dans sa boutique, en téléchargement ou sur une clé USB en bois qui réunit les vingt-neuf titres. L’acheter, c’est financer directement la suite.</p>
    <div class="cta">
      <a class="btn ghost" href="{YT_CHAINE}" target="_blank" rel="noopener">La chaîne YouTube de David Lesage ↗</a>
      <a class="btn ghost" href="{ALBUM_BOUTIQUE}" target="_blank" rel="noopener">Commander l’album — téléchargement ou clé USB ↗</a>
    </div>
  </div>
</div></section>

<section class="cdl-block" id="scenes"><div class="wrap">
  <div class="cdl-h">Sur scène</div>
  <h2 class="sec-title">Là où ce répertoire a résonné</h2>
  <p>Ce que vous entendrez au Nid n’est pas un format de salon : c’est le répertoire que David Lesage joue ailleurs, sur de grandes scènes et dans des lieux de pierre. <b>Près de soixante-dix dates</b> depuis 2016, en France, en Hongrie, en Suisse, en Belgique, en Grèce et en Côte d’Ivoire.</p>
  <ul class="cdl-scenes">{''.join(f'<li><b>{n}</b><span>{p}</span></li>' for n, p in SCENES)}</ul>
  <p>Il est également passé par l’émission <i>The Voice</i> en 2021. À Paris, on l’a entendu notamment sur la <b>Péniche Anako</b> — en voici un extrait, qui donne une idée de l’ambiance mieux que n’importe quelle description.</p>
  {video_button('anako', VIDEO_ANAKO_ID,
                'Vignette de la vidéo : deux musiciens assis face à face sur une petite scène '
                'éclairée de rouge et d’orange, chacun penché sur un handpan, une batterie et '
                'des micros entre eux. Textes incrustés « Concert David Lesage », « ça '
                'ressemble à quoi ? / What does it look like? » et « Extrait Superpan Show '
                'Jérémy Nattagh ».',
                'Un extrait de concert, à Paris',
                '« Teaser Concert David Lesage — Extrait émission SuperPan Show de '
                'Jérémy Nattagh » — le lecteur s’ouvre sur cette page.',
                '(max-width:560px) calc(100vw - 52px), 480px')}
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
{LIGHTBOX_HTML.format(secours=VIDEO_CYMA_SECOURS)}
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
{LIGHTBOX_JS}
{SPOTIFY_JS}
</body></html>"""

HTML = mobile_nav.inject(HTML)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, 'concerts-david-lesage')
os.makedirs(OUT_DIR, exist_ok=True)
OUT = os.path.join(OUT_DIR, 'index.html')
open(OUT, 'w', encoding='utf-8').write(HTML)
print('WROTE', OUT, round(len(HTML) / 1024), 'KB')
