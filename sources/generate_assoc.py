# -*- coding: utf-8 -*-
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
#: build.py recopie ce fichier en index.html a la racine (voir son TABLEAU).
SORTIE = os.path.join(REPO, 'assoc_index.html')

sys.path.insert(0, HERE)
import mobile_nav  # noqa: E402
import nav_menu  # menu de navigation partage  # noqa: E402
import textes_association as T  # textes partages avec /association  # noqa: E402
import theme_chaleur  # couche chaleureuse commune  # noqa: E402
import verif_commentaires  # garde-fou commentaires HTML  # noqa: E402

# --------------------------------------------------------------------------- #
# CE QUE CETTE PAGE A CEDE A /association LE 15/08/2026
# --------------------------------------------------------------------------- #
# David avait remarque que « Accueil » et « L’association » menaient tous les
# deux ici. Derriere ce doublon de menu, un probleme de fond : CETTE PAGE
# FAISAIT CINQ METIERS (`#association`, `#statuts`, `#adherer`, `#contact`,
# `#prestations`) en plus de presenter les six cartes de spectacles.
#
# Sont partis vers `sources/generate_association.py` -> `/association` :
#   * le DEUXIEME paragraphe de l'objet (supports et moyens) ;
#   * TOUTE la section « Cadre legal · Les statuts » — les deux articles, le
#     renvoi au Journal officiel avec le n° RNA, le lien vers le document des
#     statuts et la fiche de l'annuaire des entreprises (data.gouv.fr).
#     L'ancre `#statuts` a donc quitte cette page. Mesure faite avant de
#     trancher : AUCUNE page du site ne pointait vers `/#statuts` dans son
#     corps de texte. Le seul renvoi reel etait la redirection `/statuts` de
#     `vercel.json`, qui vise maintenant `/association#statuts`.
#
# Sont RESTES ici, et les ancres avec :
#   * `#association` — la presentation courte (OBJET_P1, inchange) suivie du
#     bouton « En savoir plus sur l’association » ;
#   * `#prestations`, `#adherer`, `#contact`, et les quatre engagements.
#
# ⚠️ Les textes communs aux deux pages vivent dans
#    `sources/textes_association.py`. Ne pas les recopier ici : une correction
#    de David doit n'avoir qu'un seul endroit ou se faire.

# Flower of life (19 circles) SVG
def flower(r=60):
    pts=[(0,0)]
    for k in range(6):
        a=math.radians(60*k); pts.append((r*math.cos(a), r*math.sin(a)))
    for k in range(6):
        a=math.radians(30+60*k); pts.append((r*math.sqrt(3)*math.cos(a), r*math.sqrt(3)*math.sin(a)))
    for k in range(6):
        a=math.radians(60*k); pts.append((2*r*math.cos(a), 2*r*math.sin(a)))
    circles=''.join(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}"/>' for x,y in pts)
    vb=2*r+r  # margin
    return (f'<svg class="flower" viewBox="{-vb} {-vb} {2*vb} {2*vb}" xmlns="http://www.w3.org/2000/svg">'
            f'<g fill="none" stroke="var(--gold)" stroke-width="1.1">{circles}</g></svg>')

FL=flower()

# ⚠️ RETRAIT DU 15/08/2026 — six regles CSS de moins dans le bloc ci-dessous.
# Le groupe `/* statuts */` y figurait :
#     .statuts .box{margin-top:34px;…;border-radius:16px;padding:28px;max-width:900px}
#     .statuts .box p{…}  .statuts .box .art{…}  .statuts .box .jo{…}
#     .statuts .box .jo a{…}
# Il habillait la section « Cadre legal · Les statuts », partie sur /association.
# Les regles ne sont pas perdues : leur equivalent vit dans
# `sources/generate_association.py` (bloc CSS_PAGE, classes `.box`, `.art`, `.jo`).
# Deux autres groupes ont suivi pour la meme raison : `.statuts .box .art` et
# `.statuts .box .jo` dans CSS_CHALEUR, et les deux regles `.jo a` de CSS_LISI.
# Une feuille de style qui decrit une section absente de la page est exactement ce
# qui fait perdre une demi-heure a la session suivante.
CSS="""
:root{--night:#0e0f24;--night2:#141633;--ink:#eae7f3;--muted:#a9a6c4;--gold:#d8b25a;--gold2:#f0d18a;--plum:#8f7ad1;--card:#191b3d;--line:rgba(216,178,90,.26)}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--night);color:var(--ink);font-family:'Jost',-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.75;font-size:17px;-webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2,h3,.serif{font-family:'Cormorant Garamond',Georgia,serif}
a{color:inherit;text-decoration:none}
.wrap{max-width:1080px;margin:0 auto;padding:0 26px}
.kick{letter-spacing:.32em;text-transform:uppercase;font-size:13px;font-weight:600;color:var(--gold);margin-bottom:14px}
section{padding:90px 0;position:relative}
.sec-title{font-size:clamp(30px,5vw,50px);font-weight:600;line-height:1.08;color:#fff}
.lead{font-size:19px;color:var(--muted);max-width:760px;margin-top:16px}
p.body{max-width:820px;color:#d7d4ea;margin-top:16px}
b{color:#fff;font-weight:500}
.divider{height:1px;background:linear-gradient(90deg,transparent,var(--line),transparent);max-width:1080px;margin:0 auto}
/* nav */
.nav{position:fixed;top:0;left:0;right:0;z-index:40;display:flex;align-items:center;justify-content:space-between;padding:16px 26px;background:rgba(14,15,36,.6);backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.05)}
.nav .brand{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:19px;letter-spacing:.12em;color:#fff;text-transform:uppercase}
.nav .links{display:flex;align-items:center;gap:19px;font-size:13.5px;letter-spacing:.04em}
.nav .links a{color:var(--muted);transition:color .2s}
.nav .links a:hover{color:var(--gold2)}
.nav .adh{color:#1a1608!important;background:var(--gold);padding:8px 16px;border-radius:30px;font-weight:600}
@media(max-width:760px){.nav .links a:not(.adh){display:none}}
/* hero */
.hero{min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:120px 24px 80px;position:relative;overflow:hidden;
background:radial-gradient(1100px 720px at 50% -6%,rgba(147,116,226,.28),transparent 60%),radial-gradient(900px 600px at 85% 108%,rgba(216,178,90,.14),transparent 60%),radial-gradient(700px 500px at 10% 92%,rgba(90,75,138,.28),transparent 60%),var(--night)}
.flower{position:absolute;top:50%;left:50%;transform:translate(-50%,-54%);width:min(560px,86vw);opacity:.16;pointer-events:none}
.hero .inner{position:relative;z-index:2}
.hero h1{font-family:'Cormorant Garamond',serif;font-size:clamp(40px,8vw,86px);font-weight:600;letter-spacing:.06em;color:#fff;line-height:1;text-shadow:0 6px 40px rgba(0,0,0,.4)}
.hero .tag{font-family:'Cormorant Garamond',serif;font-style:italic;color:var(--gold2);font-size:clamp(20px,3.4vw,30px);margin-top:12px}
.hero .sub{max-width:640px;margin:22px auto 0;color:#e7e4f5;font-size:18px}
.hero .cta{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:34px}
.btn{display:inline-flex;align-items:center;gap:8px;background:var(--gold);color:#1a1608;font-weight:600;padding:14px 26px;border-radius:40px;font-size:15px;transition:transform .2s,box-shadow .2s}
.btn:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(216,178,90,.28)}
.btn.ghost{background:transparent;color:var(--gold2);border:1px solid var(--line)}
/* association */
.assoc{background:radial-gradient(900px 500px at 88% -10%,rgba(147,116,226,.10),transparent 60%),var(--night)}
/* prestations */
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin-top:44px}
.card{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:16px;padding:28px;transition:transform .25s,border-color .25s;position:relative;display:block}
.card:hover{transform:translateY(-5px);border-color:var(--line)}
.card .t{color:var(--gold);font-size:13px;letter-spacing:.16em;text-transform:uppercase;font-weight:600}
.card h3{font-family:'Cormorant Garamond',serif;font-size:26px;color:#fff;margin:8px 0 10px;font-weight:600}
.card p{color:var(--muted);font-size:15px}
.card .go{color:var(--gold2);font-size:13px;margin-top:14px;display:inline-block}
.card.feature{background:linear-gradient(160deg,rgba(147,116,226,.16),var(--card));border-color:var(--line)}
/* engagements */
.eng{background:linear-gradient(180deg,var(--night),#0b0c1e)}
.vals{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:18px;margin-top:40px}
.val{border-top:1px solid var(--line);padding-top:16px}
.val h3{font-family:'Cormorant Garamond',serif;color:var(--gold2);font-size:20px;font-weight:600}
.val p{color:var(--muted);font-size:14.5px;margin-top:6px}
/* adhesion */
.adhesion{text-align:center;background:radial-gradient(800px 460px at 50% 40%,rgba(216,178,90,.12),transparent 65%),#0b0c1e}
.adhesion .big{font-family:'Cormorant Garamond',serif;font-size:clamp(26px,4vw,40px);color:#fff;font-weight:500;max-width:760px;margin:0 auto}
/* footer */
/* focus clavier visible (accessibilite) */
:focus-visible{outline:2px solid var(--gold2);outline-offset:2px;border-radius:4px}
footer{background:#08091a;padding:70px 0 56px;border-top:1px solid var(--line)}
.fgrid{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:34px}
footer h4{font-family:'Cormorant Garamond',serif;color:#fff;font-size:22px;font-weight:600;margin-bottom:10px}
footer p,footer a{color:var(--muted);font-size:14.5px}
/* zone tactile confortable (~44px) sur les liens du pied de page */
footer a{display:inline-block;padding:13px 0;line-height:1.3}
footer a.btn,footer a.adh{padding:14px 30px}
footer a:hover{color:var(--gold2)}
.fbrand{letter-spacing:.12em;text-transform:uppercase;color:var(--gold2);font-family:'Cormorant Garamond',serif;font-size:20px;font-weight:600}
.legal{margin-top:40px;text-align:center;color:#6b6b80;font-size:13px}
@media(max-width:760px){.fgrid{grid-template-columns:1fr;gap:24px}section{padding:66px 0}}
"""

# --------------------------------------------------------------------------
# LA COUCHE CHALEUREUSE (refonte du 15/08/2026)
# --------------------------------------------------------------------------
# « Ramener de la couleur prune, ca fait du bien. Resonances a besoin d'avoir
#   une image classe mais aussi chaleureuse. » — David, 15/08/2026.
# La partie commune vit dans `sources/theme_chaleur.py`. Ici, seules les
# declinaisons propres aux classes de CETTE page. AUCUN TEXTE N'A BOUGE.
#
# ⚠️ Ce bloc est une CHAINE ORDINAIRE, comme CSS_LISI plus bas, et pour la meme
#    raison : la panne historique de ce fichier venait d'un CSS colle DANS la
#    f-string `HTML=f"""…"""`, ou Python lit chaque accolade comme une
#    expression. On le concatene a CSS avant la f-string ; celle-ci ne voit
#    plus qu'une variable.
# ⚠️ `.hero h1` : `width:fit-content` SEUL casserait le centrage du hero (la
#    boite se retrecit au texte et se colle a gauche). D'ou `margin:0 auto`.
#    C'est ce qui permet au degrade de courir sur la LARGEUR DES MOTS et non
#    sur toute la page — sans quoi le titre, centre, ne prendrait que la
#    teinte du milieu et le balayage or -> corail -> prune ne se verrait pas.
# ⚠️ POURQUOI ON PEINT LA BORDURE des cartes plutot que d'ajouter un
#    pseudo-element : `.card` s'anime deja au survol (`translateY(-5px)`) et
#    `.card.feature` porte un fond en degrade. Un `::before` positionne
#    demanderait un `overflow:hidden` qui rognerait les coins arrondis. La
#    bordure peinte ne deplace rien.
CSS_CHALEUR = """/* ===== Accueil : declinaisons chaleureuses ===== */
.hero h1{background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent;width:fit-content;max-width:100%;margin:0 auto}
/* sur-titre des cartes de prestations, peint au degrade */
.card .t{display:inline-block;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
/* cartes de prestations : filet de tete au degrade, coins plus genereux */
.card{border-top:3px solid transparent;border-radius:18px;background-image:var(--grad),linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,0)),linear-gradient(var(--card),var(--card));background-size:100% 3px,100% 100%,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box,padding-box}
/* ⚠️ LA REGLE QUI SUIT DOIT REPETER TOUTES LES LONGHANDS. Mesure faite a
   l'ecran : sans elles, les deux cartes « feature » recevaient le degrade EN
   APLAT SUR TOUTE LEUR SURFACE et leur texte devenait illisible. Raison :
   `.card.feature{background:…}` plus haut est une PROPRIETE RACCOURCIE, qui
   remet `background-size/repeat/position/origin` a leur valeur initiale — et
   elle est plus specifique (0,2,0) que le `.card{background-size:…}` d'ici
   (0,1,0). Le `100% 3px` du filet etait donc ecrase par un `auto`. */
.card.feature{border-color:transparent;background-image:var(--grad),linear-gradient(160deg,rgba(147,116,226,.16),var(--card));background-size:100% 3px,100% 100%;background-repeat:no-repeat,no-repeat;background-position:0 0,0 0;background-origin:border-box,padding-box;background-attachment:scroll,scroll}
.card:hover{border-color:transparent}
/* les quatre engagements : le trait dore de tete devient le filet degrade */
.val{border-top-color:transparent;background-image:linear-gradient(90deg,rgba(216,178,90,.5),rgba(238,128,98,.5) 55%,rgba(179,143,245,.45));background-repeat:no-repeat;background-size:100% 2px;background-position:0 0}
/* la prune revient en accent de TEXTE (--plum2 : 8,6:1 sur --night) */
.val h3{color:var(--plum2)}
"""

CSS = CSS + theme_chaleur.CSS + CSS_CHALEUR

PREST=[
 ('feature','Concert-Rituel','RITUALS','Une prière chantée où le public devient souffle, voix et battement. Musique live, chant collectif et induction, par David Lesage &amp; Iris Chasles. Disponible en <b>duo</b> ou en <b>trio</b> avec saxophones et flûtes.','Découvrir la page','/rituals'),
 ('feature','Spectacle immersif participatif','« E-Motion »','Spectacle immersif et participatif avec <b>danse aérienne à l’élastique</b> et <b>musique live</b>, par <b>ID duo</b> (Iris Chasles &amp; David Lesage). Chant, guidances et pratiques corporelles autour des cinq éléments — le public devient acteur de la représentation.','Découvrir la page','/e-motion'),
 ('','Paris 20ᵉ · Un lieu pour éclore','Le Nid','Un cocon de sécurité qui permet à l’être d’éclore à lui-même : accompagnement psychothérapeutique avec Iris Chasles, concerts de David Lesage, yoga, rythme à la calebasse et cours individuels.','Voir le programme','/le-nid'),
 # La carte « David Lesage » a recu son lien A LA MAIN dans index.html : ici
 # elle n'en avait pas, donc elle n'etait pas cliquable, et une regeneration
 # aurait fait perdre le lien vers la page des concerts au Nid.
 ('','Musique & voix','David Lesage','Handpan électronique, harpe africaine (Ngoni), voix, percussions et électro : soul française et spiritualité des musiques du monde. Vu à The Voice 11.','Voir les concerts','/concerts-david-lesage'),
 ('','Soin d’incarnation · Paris 20ᵉ','Le Soin Soa','Un soin holistique né de la rencontre de trois approches complémentaires : le <b>toucher thérapeutique</b>, l’<b>intelligence relationnelle</b> et l’<b>alchimie vocale</b>. Une immersion d’un week-end au Nid, en tout petit groupe.','En savoir plus','/le-soin-soa'),
 # ⚠️ DEUX CARTES ONT ETE RETIREES DE LA PAGE PUBLIEE, a la main. Ne pas les
 # remettre sans l'accord de David :
 #   « Sons & vibrations / Bains sonores & soins vibratoires »
 #   « Transmission / Ateliers & formations »
 # Motif : aucune proposition concrete derriere, aucun lien, aucune date — une
 # carte qui ne mene nulle part sur la page d'accueil d'une association.
 # ⚠️ Incident deja vecu : une tentative de restauration de « Bains sonores »
 # avait ete inseree A L'INTERIEUR de la carte « Ateliers & formations » et
 # cassait le HTML. Si elles doivent revenir un jour, c'est ICI, en ajoutant un
 # n-uplet complet a cette liste — jamais dans le HTML.
 # La carte « Événements & création » ci-dessous a le meme defaut (aucun lien) ;
 # son sort est encore en attente de decision (point 7 du handoff). Elle reste.
 ('','Rencontres','Événements & création','Imaginer et soutenir des espaces de partage, de créativité, de bien-être et d’élévation de la conscience.','',''),
]

def cards():
    out=''
    for cls,t,h,p,go,href in PREST:
        tag=f'<span class="go">{go} →</span>' if go else ''
        ext=' target="_blank" rel="noopener"' if href.startswith('http') else ''
        op=f'<a class="card {cls}" href="{href}"{ext}>' if href else f'<div class="card {cls}">'
        cl='</a>' if href else '</div>'
        out+=f'{op}<div class="t">{t}</div><h3>{h}</h3><p>{p}</p>{tag}{cl}'
    return out

# Le contenu detaille du Soin Soa vit desormais dans sa page dediee :
#   sources/generate_soin_soa.py  ->  le-soin-soa/index.html
# (l'accueil n'en garde que la carte de prestations ci-dessus, qui y renvoie).

# Les quatre engagements sont partages avec `/association` (ils y figurent sous
# le meme intitule) : une seule ecriture, dans textes_association.py.
VALS = T.VALS
def vals():
    return ''.join(f'<div class="val"><h3>{h}</h3><p>{p}</p></div>' for h,p in VALS)

# ⚠️ CE BLOC EST UNE CHAINE ORDINAIRE, PAS UNE f-STRING. C'ETAIT LA PANNE.
# Il etait ecrit tel quel dans le gabarit `HTML=f"""…"""` plus bas. Python y lit
# toute accolade comme le debut d'une expression a evaluer : la premiere regle,
# `.jo a{font-size:15px…}`, devenait donc l'expression « font-size:15px… » et le
# script s'arretait sur « NameError: name 'font' is not defined », avant d'avoir
# rien ecrit. Resultat : le generateur de la page la PLUS VUE du site ne tournait
# plus du tout, et l'accueil ne pouvait plus etre modifie qu'a la main.
# On SORT le CSS de la f-string plutot que de doubler ses accolades : les doubler
# rendrait le CSS illisible, et la prochaine regle ajoutee ici reintroduirait la
# panne. Sorti de la f-string, on peut y coller du CSS tel quel sans y penser.
# ⚠️ Meme regle pour tout futur bloc de CSS : hors de la f-string.
# ⚠️ Les deux regles `.jo a` de ce bloc sont parties le 15/08/2026 avec la
#    section des statuts : plus aucun element de cette page ne porte `.jo`.
#    Elles sont reprises telles quelles dans `generate_association.py`.
CSS_LISI = """/* --- lisibilite des liens (demande de David : liens et dates trop petits) --- */
footer p,footer a{font-size:16px}
footer a{padding:13px 0}
footer a:not(.btn):not(.adh){text-decoration:underline;text-decoration-color:rgba(216,178,90,.35);
  text-underline-offset:3px}
.nav .links a{font-size:14.5px}
.nav .links a.adh{font-size:15px}
p a:not(.btn):not(.adh){text-decoration:underline;
  text-decoration-color:rgba(216,178,90,.4);text-underline-offset:3px}
"""

# Meme URL que `nav_menu.ADHESION` et que le bouton de `/association` : elle est
# ecrite une fois dans textes_association.py.
HELLO = T.HELLOASSO

# --------------------------------------------------------------------------- #
# GOOGLE SEARCH CONSOLE — la balise de verification, ICI ET NULLE PART AILLEURS
# --------------------------------------------------------------------------- #
# Code fourni par David le 15/08/2026. Il verifie la propriete « prefixe d'URL »
# (https://www.resonancesproductions.org/) : Google ne lit la balise que sur la
# page demandee, donc UNE pose sur l'accueil suffit. La repeter sur les 30 pages
# ne verifierait rien de plus et rendrait son retrait hasardeux le jour ou il
# faudra le faire. `sources/generate_association.py` REFUSE d'ecrire sa page si
# la balise s'y trouve — le garde-fou est du cote de la page qui ne doit pas la
# porter, pas du cote de celle qui la porte.
# ⚠️ David pose en parallele un enregistrement TXT dans la zone DNS OVH pour la
#    propriete « domaine ». Les deux methodes coexistent sans conflit, et un
#    enregistrement `google-site-verification` existe deja dans cette zone : ne
#    pas le remplacer en croyant faire le menage.
HTML=f"""<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Résonances Productions — Association loi 1901 · Art du spectacle vivant</title>
<meta name="description" content="Résonances Productions : association loi 1901 qui accompagne, promeut et soutient des artistes. Concert-rituel RITUALS, spectacles, bains sonores, ateliers et événements — l'humain, la vibration.">
<meta property="og:title" content="Résonances Productions">
<meta property="og:description" content="L'humain, la vibration — accompagnement, promotion et soutien d'artistes.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="alternate icon" href="/favicon.ico" sizes="any">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <meta name="theme-color" content="#0e0f24">
  <meta name="twitter:card" content="summary_large_image">
  <meta property="og:url" content="https://www.resonancesproductions.org/">
  <meta property="og:image" content="https://www.resonancesproductions.org/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="google-site-verification" content="iPTmSfVj4xlmO8MwL_FnR4VJS583WHokrohFreY6pjk">
</head>
<body>

<nav class="nav">
  <a href="#top" class="brand">Résonances Productions</a>
  <div class="links">
    <a href="#association">L’association</a>
    <a href="#prestations">Prestations</a>
    <a href="/rituals">RITUALS</a>
    <a href="/e-motion">E-Motion</a>
    <a href="/le-nid">Le Nid</a>
    <a href="#statuts">Statuts</a>
    <a href="#contact">Contact</a>
    <a class="adh" href="{HELLO}" target="_blank" rel="noopener">Adhérer</a>
  </div>
</nav>

<header class="hero" id="top">
  {FL}
  <div class="inner">
    <div class="kick">Association loi 1901 · Art du spectacle vivant</div>
    <h1>Résonances<br>Productions</h1>
    <div class="tag">l’humain · la vibration</div>
    <p class="sub">L’accompagnement, la promotion et le soutien d’artistes — au service du vivant et de l’élévation de la conscience.</p>
    <div class="cta">
      <a class="btn" href="{HELLO}" target="_blank" rel="noopener">Adhérer à l’association</a>
      <a class="btn ghost" href="/rituals">Découvrir RITUALS</a>
    </div>
  </div>
</header>

<section class="assoc" id="association"><div class="wrap">
  <div class="kick">L’association</div>
  <h2 class="sec-title">{T.OBJET_TITRE}</h2>
  <p class="body">{T.OBJET_P1}</p>
  <div class="cta" style="margin-top:28px"><a class="btn ghost" href="/association">En savoir plus sur l’association</a></div>
</div></section>

<div class="divider"></div>

<section id="prestations"><div class="wrap">
  <div class="kick">Nos prestations</div>
  <h2 class="sec-title">Créations, spectacles & expériences</h2>
  <p class="lead">De la scène au soin sonore, l’association porte des projets qui relient l’art, le corps et la conscience.</p>
  <div class="grid">{cards()}</div>
</div></section>

<div class="divider"></div>


<section class="eng"><div class="wrap">
  <div class="kick">Nos engagements</div>
  <h2 class="sec-title">Ce qui nous anime</h2>
  <div class="vals">{vals()}</div>
</div></section>

<section class="adhesion" id="adherer"><div class="wrap">
  <div class="kick" style="color:var(--gold2)">Adhésion</div>
  <div class="big">Soutenez la création et rejoignez l’aventure. Votre adhésion nous permet de financer nos actions et de couvrir nos projets.</div>
  <div class="cta" style="justify-content:center;margin-top:30px"><a class="btn" href="{HELLO}" target="_blank" rel="noopener">Adhérer sur HelloAsso</a></div>
</div></section>

<div class="divider"></div>

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
      <p style="margin-top:8px"><a href="https://www.facebook.com/resonancesproductions" target="_blank" rel="noopener">Facebook</a></p>
    </div>
    <div>
      <h4>Informations</h4>
      <p>SIRET : 919 514 075 00010</p>
      <p>Code APE : 9001Z<br>Arts du spectacle vivant</p>
      <p style="margin-top:8px"><a href="{HELLO}" target="_blank" rel="noopener">Adhérer / soutenir</a></p>
      <p style="margin-top:8px"><a href="https://docs.google.com/document/d/1NxsbvaqHsA9VOXlN7cvsav7cxFwhsK4XCpowHb75o1w/edit?usp=sharing" target="_blank" rel="noopener">Statuts de l’association</a></p>
    </div>
  </div>
  <div class="legal">© {2026} Résonances Productions · resonancesproductions.org</div>
</div></footer>

</body></html>"""

HTML = mobile_nav.inject(HTML)

# Le bloc « lisibilite des liens » doit rester le DERNIER a parler taille de
# police : `.nav .links a{font-size:14.5px}` doit l'emporter sur la regle de la
# barre de navigation, et `mobile_nav.inject()` vient justement de coller sa
# propre feuille de style en fin de <style>. On pose donc CSS_LISI derriere lui
# — c'est exactement son ordre dans la page publiee. (Le CSS de `nav_menu`,
# ajoute ensuite, est cadre par ses propres selecteurs et ne rentre pas en
# conflit.)
assert HTML.count('</style>') == 1, 'une seule feuille de style attendue'
if '/* --- lisibilite des liens' not in HTML:          # garde d'idempotence
    HTML = HTML.replace('</style>', '\n' + CSS_LISI + '\n</style>', 1)

# Ligne vide entre le script du hamburger et le bloc du menu partage. Elle vient
# de la mise a jour du menu v1 -> v2 : `nav_menu._strip()` a retire l'ancien bloc
# en laissant le saut de ligne qui le suivait. Les neuf pages publiees l'ont ; on
# la reproduit pour qu'une regeneration ne modifie pas un octet.
HTML = HTML.replace('</script>\n</body>', '</script>\n\n</body>', 1)

HTML = nav_menu.inject(HTML, 'home')

# --------------------------------------------------------------------------- #
# GARDE-FOUS STRUCTURELS, AVANT L'ECRITURE. Modele : generate_rythme.py.
# On compte les ancres qui doivent etre uniques et les six cartes de
# prestations : un ecart les attrape AUSSI BIEN en disparition qu'en
# duplication (le piege des quatre cartes identiques). On REFUSE d'ecrire une
# page cassee plutot que d'imprimer un avertissement qui defile.
# --------------------------------------------------------------------------- #
_ATTENDU = (
    ('<h1', 1, 'titre principal'),
    # version lue dans nav_menu : ce garde-fou ne doit pas devenir faux le
    # jour ou NAV_VERSION est incrementee.
    ('data-nav="%s"' % nav_menu.NAV_VERSION, 1, 'menu partage nav_menu.py'),
    # le bouton hamburger est CREE PAR LE JS : on compte la ligne qui le fabrique
    ("b.className='burger'", 1, 'bouton hamburger de mobile_nav.py'),
    ('/* --- lisibilite des liens', 1, 'bloc « lisibilite des liens »'),
    ('id="association"', 1, 'ancre #association'),
    ('id="prestations"', 1, 'ancre #prestations'),
    ('id="adherer"', 1, 'ancre #adherer'),
    # ⚠️ `id="statuts"` NE DOIT PLUS ETRE ICI : la section a demenage vers
    #    /association le 15/08/2026. Si elle revenait sur l'accueil, deux pages
    #    porteraient la meme ancre et la redirection `/statuts` de vercel.json
    #    (qui vise desormais `/association#statuts`) deviendrait ambigue. On
    #    verifie donc son ABSENCE, pas sa presence.
    ('id="statuts"', 0, 'ancre #statuts — partie sur /association'),
    ('class="statuts"', 0, 'section des statuts — partie sur /association'),
    # le pont vers la nouvelle page : sans lui, /association ne serait
    # atteignable que par le menu.
    ('<a class="btn ghost" href="/association">En savoir plus sur l’association</a>',
     1, 'bouton « En savoir plus » vers /association'),
    # la balise de verification Google Search Console : ICI, et sur aucune des
    # 29 autres pages (generate_association.py refuse d'ecrire si elle y est).
    ('name="google-site-verification"', 1, 'verification Google Search Console'),
    ('<svg class="flower"', 1, 'fleur de vie du hero'),
    ('<circle ', 19, 'les 19 cercles de la fleur de vie'),
    # SIX cartes, pas huit : voir la note sur PREST. Ce compte est la pour que
    # les deux cartes retirees ne reviennent pas par accident, et pour attraper
    # une carte perdue.
    ('class="card', len(PREST), 'cartes de prestations'),
)
for _marqueur, _combien, _quoi in _ATTENDU:
    _n = HTML.count(_marqueur)
    if _n != _combien:
        raise SystemExit('!! ABANDON : %d occurrence(s) de « %s » (%s), attendu %d. '
                         'Page NON ecrite.' % (_n, _marqueur, _quoi, _combien))

# La carte « David Lesage » doit rester cliquable (son lien avait ete pose a la
# main). Une carte sans href est rendue en <div> : elle ne mene nulle part.
if '<a class="card " href="/concerts-david-lesage">' not in HTML:
    raise SystemExit('!! ABANDON : la carte « David Lesage » n\'est pas un lien '
                     'vers /concerts-david-lesage. Page NON ecrite.')

# Garde-fou AVANT l'ecriture : aucune note de redaction en commentaire HTML
# (ce fichier est recopie tel quel dans index.html a la racine).
verif_commentaires.verifier(HTML, SORTIE)
# Chemin ABSOLU : ce script etait lance depuis n'importe ou et ecrivait son
# `assoc_index.html` dans le repertoire courant. build.py, lui, va le chercher a
# la racine du depot pour le recopier en index.html.
open(SORTIE,'w',encoding='utf-8').write(HTML)
print('WROTE', SORTIE, round(len(HTML)/1024),'KB')
