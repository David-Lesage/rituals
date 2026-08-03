# -*- coding: utf-8 -*-
"""Genere la page dediee /le-soin-soa (fichier le-soin-soa/index.html).

Contenu adapte de la page d'Iris Chasles (co-fondatrice) :
https://www.irischasles.com/agenda-yoga/immersion-therapeutique-soa
Le texte est repris MOT POUR MOT depuis l'ancienne section #soin-soa de
l'accueil (commit 74e407a) : on ne fait que le remettre en page.

ADAPTATION STATUTAIRE (validee par David le 03/08/2026) : la page presente
un EVENEMENT ORGANISE PAR L'ASSOCIATION, pas une offre de soin privee.
  - sur-titre « Evenement organise par Resonances Productions »
  - encadre de cadrage (objet de l'association, Article 2 des statuts)
  - « praticiens » / « therapeutes » -> « intervenants » ; Iris = co-fondatrice,
    Gaia = intervenante invitee
  - la participation est percue PAR L'ASSOCIATION (organisation + lieu +
    remuneration des intervenants), pas par les intervenants a titre personnel
  - encadre « Le cadre et ses limites » (pas un acte medical)
  - contact d'inscription = contact@resonancesproductions.org
Regle de registre : AUCUNE promesse de resultat therapeutique (guerison,
liberation durable, equivalent d'un cycle therapeutique). Aucune date affichee.

Usage :
    python3 sources/generate_soin_soa.py
    -> ecrit sources/soin_soa_final.html, a copier dans le-soin-soa/index.html

--- AJOUTER UNE PHOTO (c'est tout ce qu'il y a a faire) -------------------
1) Deposer l'original quelque part, puis generer les declinaisons :

     python3 - <<'EOF'
     from PIL import Image
     OUT='/Users/davidlesage/CLAUDE/resonances-site/img/soin-soa/'
     im=Image.open('MON-ORIGINAL.jpg').convert('RGB'); w0,h0=im.size
     for w in [480,900,1400]:
         if w>w0: continue
         r=im.resize((w,round(h0*w/w0)),Image.LANCZOS)
         r.save(f'{OUT}mon-nom-{w}.webp','WEBP',quality=80,method=6)
         r.save(f'{OUT}mon-nom-{w}.jpg','JPEG',quality=82,optimize=True,progressive=True)
     print(w0,h0)
     EOF

2) Ajouter une entree dans SOA_PHOTOS ci-dessous (base = nom sans la largeur,
   widths = les largeurs reellement generees, w/h = dimensions de l'original).
3) La glisser dans SOA_GALERIE (ou l'appeler par son nom dans le HTML) :
   - vignette carree de la galerie  -> ajouter la cle a SOA_GALERIE
   - figure large dans le fil du texte -> soa_fig('ma-cle', '...', cls='soa-fig soa-wide')
   - portrait d'un intervenant -> generer un carre (140 + 260 px), puis mettre la
     cle en 5e position de la ligne correspondante de SOA_EQUIPE (chaine vide =
     ligne sans photo). L'alt d'un portrait = le nom de la personne.
--------------------------------------------------------------------------
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mobile_nav  # noqa: E402

CSS = """
:root{--night:#0e0f24;--night2:#141633;--ink:#eae7f3;--muted:#a9a6c4;--gold:#d8b25a;--gold2:#f0d18a;--plum:#8f7ad1;--card:#191b3d;--line:rgba(216,178,90,.26)}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--night);color:var(--ink);font-family:'Jost',-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.75;font-size:17px;-webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2,h3,h4,.serif{font-family:'Cormorant Garamond',Georgia,serif}
a{color:inherit;text-decoration:none}
.wrap{max-width:1080px;margin:0 auto;padding:0 26px}
.kick{letter-spacing:.32em;text-transform:uppercase;font-size:13px;font-weight:600;color:var(--gold);margin-bottom:14px}
section{padding:78px 0;position:relative}
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
/* 9 entrees de menu : on resserre entre 861 et 1080 px (sous 861 px = hamburger).
   On ne descend jamais sous 13 px (plancher typographique du site) : dans la bande
   la plus etroite on masque plutot « Statuts », qui reste dans le pied de page. */
@media(min-width:861px) and (max-width:1080px){.nav{padding:16px 18px}.nav .brand{font-size:17px;white-space:nowrap}.nav .links{gap:9px;font-size:13px}.nav .adh{padding:8px 13px}}
@media(min-width:861px) and (max-width:1000px){.nav .links a[href="/#statuts"]{display:none}}
.nav .links a[aria-current="page"]{color:var(--gold2)}
.btn{display:inline-flex;align-items:center;gap:8px;background:var(--gold);color:#1a1608;font-weight:600;padding:14px 26px;border-radius:40px;font-size:15px;transition:transform .2s,box-shadow .2s}
.btn:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(216,178,90,.28)}
.btn.ghost{background:transparent;color:var(--gold2);border:1px solid var(--line)}
.cta{display:flex;gap:14px;flex-wrap:wrap}
/* ===== Le Soin Soa ===== */
.soa-top{padding:128px 0 70px;background:radial-gradient(900px 560px at 10% -8%,rgba(143,122,209,.20),transparent 62%),radial-gradient(700px 460px at 92% 102%,rgba(216,178,90,.12),transparent 62%),linear-gradient(180deg,#0b0c1e,var(--night))}
.soa-top h1{font-size:clamp(38px,7vw,72px);font-weight:600;line-height:1.02;color:#fff;letter-spacing:.02em}
.band{background:linear-gradient(180deg,#0b0c1e,var(--night))}
.tagline{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(19px,2.8vw,28px);margin-top:12px}
.soa-hero{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,320px);gap:34px;align-items:start;margin-top:32px}
.soa-hero .lead{margin-top:0}
.soa-fig{margin:0;border-radius:16px;overflow:hidden;border:1px solid var(--line);background:var(--card)}
.soa-fig img{display:block;width:100%;height:auto}
.soa-fig figcaption{color:var(--muted);font-size:13px;line-height:1.5;padding:12px 16px 14px;border-top:1px solid rgba(255,255,255,.06)}
.soa-h{color:var(--gold);font-size:13px;letter-spacing:.22em;text-transform:uppercase;font-weight:600;margin-bottom:10px}
.soa-block h3{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(24px,3.2vw,32px);color:#fff;font-weight:600;line-height:1.15}
.soa-block p{max-width:820px;color:#d7d4ea;margin-top:16px}
.soa-cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin-top:30px}
.soa-who{background:var(--card);border:1px solid rgba(255,255,255,.06);border-left:2px solid var(--gold);border-radius:14px;padding:22px 24px}
.soa-who .t{color:var(--gold);font-size:13px;letter-spacing:.14em;text-transform:uppercase;font-weight:600}
.soa-who h3{font-family:'Cormorant Garamond',Georgia,serif;font-size:23px;color:#fff;font-weight:600;margin:6px 0 2px}
.soa-who .role{color:var(--gold2);font-size:13.5px;font-style:italic;margin-bottom:9px}
.soa-who p{color:var(--muted);font-size:15px;margin:0}
/* Les intervenants : une LIGNE par personne (mise en page d'origine, preferee par
   David) — portrait carre a gauche, nom en dore + intitule de role + statut, puis
   la bio. Empilement portrait au-dessus du texte sous 620 px. */
.soa-team{display:grid;gap:18px;margin-top:30px}
.soa-line{display:flex;gap:24px;align-items:flex-start;background:var(--card);border:1px solid rgba(255,255,255,.06);border-left:2px solid var(--gold);border-radius:14px;padding:22px 24px}
.who-ph{display:block;flex:0 0 auto;width:150px;height:150px;border-radius:12px;overflow:hidden;border:1px solid var(--line);box-shadow:0 8px 22px rgba(0,0,0,.38);background:var(--night2)}
.who-ph img{display:block;width:100%;height:100%;object-fit:cover;object-position:center}
.who-txt{min-width:0}
.who-txt h3{font-family:'Cormorant Garamond',Georgia,serif;font-size:26px;line-height:1.15;font-weight:600;color:var(--gold2);margin:0}
.who-txt .disc{color:#fff;font-size:15.5px;letter-spacing:.04em;margin-top:2px}
.who-txt .role{color:var(--muted);font-size:13.5px;font-style:italic;margin-top:3px}
.who-txt p{color:#d7d4ea;font-size:15.5px;margin:12px 0 0}
@media(max-width:620px){.soa-line{flex-direction:column;gap:16px;padding:20px}
  .who-ph{width:140px;height:140px}}
/* figure large dans le fil du texte (meme colonne que les paragraphes) */
.soa-wide{max-width:820px;margin-top:26px}
/* ===== Hero : l'affiche sur fond NOIR PUR =====================================
   Le visuel hero-soa-* a ses 4 coins en #000 : la section de hero est donc en
   #000 elle aussi et l'affiche n'a NI cadre NI arrondi NI fond de carte, sinon
   la couture redevient visible. Le raccord vers le bleu nuit du reste de la page
   se fait par .hero-fade juste apres le </header>. */
.hero-black{background:#000}
.hero-black .soa-hero{grid-template-columns:minmax(0,1fr) minmax(0,520px);gap:40px;align-items:center;margin-top:26px}
.hero-poster{border:0;border-radius:0;background:transparent;overflow:visible}
.hero-poster img{width:100%;height:auto}
.hero-fade{height:130px;background:linear-gradient(180deg,#000,var(--night))}
@media(max-width:860px){.hero-black .soa-hero{grid-template-columns:1fr;gap:28px}
  /* en mobile l'affiche passe AU-DESSUS du texte : c'est elle le hero */
  .hero-black .soa-hero>div{order:2}.hero-poster{order:1}}
@media(max-width:700px){
  /* pleine largeur : on annule les 26 px de .wrap pour gagner en lisibilite
     (le fond de l'affiche etant noir, le raccord reste invisible) */
  .hero-poster{width:calc(100% + 52px);max-width:none;margin-left:-26px;margin-right:-26px}}
/* encadres de cadrage (statut de l'evenement, limites) */
.soa-note{background:var(--card);border:1px solid rgba(255,255,255,.07);border-left:2px solid var(--gold);border-radius:14px;padding:19px 22px;margin-top:22px;max-width:820px}
.soa-note p{color:#d7d4ea;font-size:15.5px;margin:0;line-height:1.7}
.soa-note p+p{margin-top:10px}
.soa-quote{margin:34px 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(21px,3vw,28px);line-height:1.35;border-left:2px solid var(--gold);padding-left:22px;max-width:760px}
.soa-list{list-style:none;margin-top:20px;max-width:820px}
.soa-list li{color:#d7d4ea;font-size:16px;padding:9px 0 9px 26px;position:relative;border-bottom:1px solid rgba(255,255,255,.05)}
.soa-list li:last-child{border-bottom:0}
.soa-list li::before{content:"";position:absolute;left:4px;top:19px;width:6px;height:6px;border-radius:50%;background:var(--gold)}
.soa-list.no li::before{background:none;border:1px solid var(--muted);width:7px;height:7px;top:18px;border-radius:0;transform:rotate(45deg)}
.soa-prog{margin-top:26px;display:grid;gap:18px}
.soa-day{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:14px;padding:22px 24px}
.soa-day h3{font-family:'Cormorant Garamond',Georgia,serif;color:var(--gold2);font-size:21px;font-weight:600;margin-bottom:8px}
.soa-day ul{list-style:none}
.soa-day li{color:var(--muted);font-size:15px;padding:6px 0;display:flex;gap:14px;align-items:baseline;flex-wrap:wrap}
.soa-day li b{color:var(--gold);font-weight:600;font-size:13.5px;letter-spacing:.06em;min-width:104px;flex:0 0 auto}
.soa-day li span{flex:1 1 220px;min-width:0}
.soa-price{margin-top:30px;background:linear-gradient(160deg,rgba(216,178,90,.12),var(--card));border:1px solid var(--line);border-radius:16px;padding:28px;max-width:820px}
.soa-price .amount{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(34px,5vw,46px);color:#fff;font-weight:600;line-height:1}
.soa-price .amount small{font-family:'Jost',sans-serif;font-size:14px;color:var(--muted);letter-spacing:.16em;text-transform:uppercase;display:block;font-weight:600;margin-bottom:6px}
.soa-price p{color:#d7d4ea;font-size:15px;margin-top:12px}
.soa-gal{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px;margin-top:30px;align-items:start}
.soa-gal .soa-fig img{aspect-ratio:1/1;object-fit:cover;object-position:center}
/* sommaire */
.toc{margin-top:44px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:22px 0}
.toc .soa-h{margin-bottom:14px}
.toc ol{list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:2px 26px;counter-reset:toc}
.toc li{counter-increment:toc}
.toc a{display:block;color:var(--muted);font-size:15px;padding:9px 0;min-height:44px;transition:color .2s}
.toc a::before{content:counter(toc,decimal-leading-zero);color:var(--gold);font-size:12px;letter-spacing:.1em;margin-right:10px}
.toc a:hover{color:var(--gold2)}
/* retour en haut */
.totop{position:fixed;right:18px;bottom:18px;z-index:35;width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:rgba(25,27,61,.92);border:1px solid var(--line);color:var(--gold2);font-size:19px;opacity:0;visibility:hidden;transition:opacity .3s,visibility .3s,transform .2s}
.totop.on{opacity:1;visibility:visible}
.totop:hover{transform:translateY(-2px)}
@media(max-width:860px){.soa-hero{grid-template-columns:1fr;gap:26px}}
@media(max-width:560px){.soa-day li{display:block;padding:9px 0}.soa-day li b{display:block;margin-bottom:1px}}
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
/* --- lisibilite des liens (demande de David : liens et dates trop petits) ---
   Ce bloc doit rester EN DERNIER : il surcharge les tailles ci-dessus. */
.jo a{font-size:15px;display:inline-block;padding:6px 0;text-decoration:underline;
  text-decoration-color:rgba(216,178,90,.45);text-underline-offset:3px}
.jo a:hover{text-decoration-color:var(--gold2)}
footer p,footer a{font-size:16px}
footer a{padding:13px 0}
footer a:not(.btn):not(.adh){text-decoration:underline;text-decoration-color:rgba(216,178,90,.35);
  text-underline-offset:3px}
.nav .links a{font-size:14.5px}
.nav .links a.adh{font-size:15px}
p a:not(.btn):not(.adh){text-decoration:underline;
  text-decoration-color:rgba(216,178,90,.4);text-underline-offset:3px}
"""

IMGDIR = '/img/soin-soa'
SOA_PHOTOS = {
 # Hero : meme visuel que 'affiche', en meilleure resolution et sur fond noir PUR
 # (#000 sur les 4 coins, verifie) -> le carre se fond sans couture dans la
 # section de hero, qui est elle aussi en #000. Ne pas remplacer par une version
 # sur fond bleu nuit : la couture redeviendrait visible.
 'hero': dict(base='hero-soa', widths=[480, 900, 1400, 1619], w=1619, h=1619,
   alt='Affiche du Soin Soa sur fond noir : un motif doré en forme d’ailes rayonnantes, le titre « SOA — Soin d’incarnation », la citation « Renaître à soi au cœur de l’intime » et les noms des trois intervenants, Iris Chasles, Gaïa Pégourié et David Lesage.',
   cap=''),
 # 'affiche' n'est plus affichee dans la page (remplacee par 'hero'), mais les
 # fichiers restent sur le disque : affiche-soa-1400.jpg sert d'og:image.
 'affiche': dict(base='affiche-soa', widths=[480, 900, 1400], w=1600, h=1600,
   alt='Affiche du Soin Soa, soin d’incarnation : motif doré rayonnant sur fond noir, avec les noms d’Iris Chasles, Gaïa Pégourié et David Lesage.',
   cap=''),
 'trois-soins': dict(base='trois-soins', widths=[480, 900], w=1024, h=1024,
   alt='Triptyque des trois soins : des mains qui massent un dos, un échange assis face à face, et des mains sur un handpan près d’un bol de cristal.',
   cap='Les trois espaces du soin : le corps, la psyché, le son.'),
 'cercle': dict(base='cercle-au-nid', widths=[480, 768], w=768, h=1344,
   alt='Cercle de partage au Nid : six personnes assises sur des coussins autour de trois intervenants et de bols chantants, dans un grand atelier d’artiste lumineux.',
   cap='Le cercle de partage au Nid — six participants, trois intervenants.'),
 'facade': dict(base='facade-le-nid', widths=[480, 600], w=600, h=450,
   alt='Façade vitrée du Nid, ancien atelier d’artiste sur trois niveaux, vue depuis la cour pavée plantée.',
   cap='Le Nid — un ancien atelier d’artiste, dans une cour pavée du 20ᵉ.'),
 'espace-corps': dict(base='espace-corps', widths=[480, 900, 1400], w=4032, h=2268,
   alt='Espace de soin : une table de massage noire dressée près de la fenêtre et, au premier plan, une table de bois où sont alignés plusieurs jeux de diapasons thérapeutiques, à côté d’un grand cristal de quartz.',
   cap='L’Espace Corps — la table de soin, les diapasons et les cristaux.'),
 # Portraits des intervenants : carres, deux largeurs (140 + 260 px).
 # Attribution verifiee deux fois : chaque nom est ecrit a cote de sa photo dans
 # les documents sources. Reperes : Gaia = feuillage vert, Iris = exterieur dore,
 # David = studio sombre. Ne jamais reattribuer sans cette verification.
 'portrait-gaia': dict(base='portrait-gaia-pegourie', widths=[140, 260], w=260, h=260,
   alt='Gaïa Pégourié', cap=''),
 'portrait-iris': dict(base='portrait-iris-chasles', widths=[140, 260], w=260, h=260,
   alt='Iris Chasles', cap=''),
 'portrait-david': dict(base='portrait-david-lesage', widths=[140, 260], w=260, h=260,
   alt='David Lesage', cap=''),
}
SOA_GALERIE = ['trois-soins', 'cercle', 'facade']


def soa_fig(key, sizes, cls='soa-fig', lazy=True, priority=False):
    p = SOA_PHOTOS[key]; ws = p['widths']; big = ws[-1]
    h = round(p['h'] * big / p['w'])
    webp = ', '.join(f'{IMGDIR}/{p["base"]}-{w}.webp {w}w' for w in ws)
    jpg = ', '.join(f'{IMGDIR}/{p["base"]}-{w}.jpg {w}w' for w in ws)
    cap = f'<figcaption>{p["cap"]}</figcaption>' if p['cap'] else ''
    load = 'lazy' if lazy else 'eager'
    prio = ' fetchpriority="high"' if priority else ''
    return (f'<figure class="{cls}"><picture>'
            f'<source type="image/webp" srcset="{webp}" sizes="{sizes}">'
            f'<img src="{IMGDIR}/{p["base"]}-{big}.jpg" srcset="{jpg}" sizes="{sizes}"'
            f' width="{big}" height="{h}" loading="{load}"{prio} decoding="async" alt="{p["alt"]}">'
            f'</picture>{cap}</figure>')


def soa_portrait(key, sizes='150px'):
    """Portrait carre d'un intervenant (pas de figcaption : l'alt = le nom)."""
    p = SOA_PHOTOS[key]; ws = p['widths']; big = ws[-1]
    webp = ', '.join(f'{IMGDIR}/{p["base"]}-{w}.webp {w}w' for w in ws)
    jpg = ', '.join(f'{IMGDIR}/{p["base"]}-{w}.jpg {w}w' for w in ws)
    return (f'<picture class="who-ph">'
            f'<source type="image/webp" srcset="{webp}" sizes="{sizes}">'
            f'<img src="{IMGDIR}/{p["base"]}-{big}.jpg" srcset="{jpg}" sizes="{sizes}"'
            f' width="{big}" height="{big}" loading="lazy" decoding="async" alt="{p["alt"]}">'
            f'</picture>')


def soa_galerie():
    return '<div class="soa-gal">' + ''.join(
        soa_fig(k, '(max-width:700px) 92vw, (max-width:1080px) 46vw, 340px') for k in SOA_GALERIE) + '</div>'


# (intitule de role, nom, qualite / rattachement, biographie, cle du portrait)
# Les intitules de role sont ceux des intervenants eux-memes (repris de la
# presentation d'origine) : ne pas les reformuler.
# La cle du portrait renvoie a SOA_PHOTOS ; mettre '' pour une ligne sans photo.
SOA_EQUIPE = [
 ('Massage Mémoire cellulaire', 'Gaïa Pégourié', 'Intervenante invitée',
  'Experte du toucher thérapeutique et formée au bio-décodage, elle accompagne la libération des mémoires corporelles. Son approche relie le corps et les émotions pour révéler leur langage profond, et met en lumière ce que le corps exprime en silence.',
  'portrait-gaia'),
 ('Régulation Neuro-émotionnelle', 'Iris Chasles', 'Co-fondatrice de Résonances Productions',
  'Psychopraticienne à Paris, formée en Intelligence Relationnelle® et en psychopathologie. Son travail porte sur les traumas et les mémoires engrammées, avec une approche neurobiologique de la régulation du système nerveux.',
  'portrait-iris'),
 ('Alchimie Vocale', 'David Lesage', 'Co-fondateur de Résonances Productions',
  'Improvisateur formé au jazz et au conservatoire, il utilise la voix comme outil de transformation. Avec ses instruments vibratoires — handpan, harpe africaine, tambour chamanique, bols de cristal et d’or — il façonne en temps réel un espace sonore sur-mesure.',
  'portrait-david'),
]
SOA_PERMET = [
 'Libérer des blocages profonds, physiques ou émotionnels.',
 'Dissoudre des schémas de répétition ou d’auto-sabotage.',
 'Ramener de la tendresse et du lien là où il y a eu de la solitude.',
 'Lever les inhibitions et retrouver la spontanéité du vivant.',
 'Se sentir en cohérence entre son corps, son cœur et sa conscience.',
]
SOA_NEPAS = [
 'Ce n’est pas de l’effleurage.',
 'Ce n’est pas un soin « bien-être » au sens classique.',
 'Ce n’est pas une cérémonie chamanique.',
 'Ce n’est pas un rituel mystique désincarné.',
 'Ce n’est pas une expérience hors du réel.',
]
SOA_ESPACES = [
 '<b>L’Espace Corps</b>, avec Gaïa — massage et libération de la mémoire cellulaire.',
 '<b>L’Espace Psyché</b>, avec Iris — Intelligence Relationnelle® pour réguler et intégrer.',
 '<b>Le Cœur du Cercle</b>, avec David — soin vibratoire et vocal.',
]
SOA_PROG = [
 ('Vendredi soir', [
   ('18h – 20h', 'Cercle d’ouverture et intentions de travail.'),
 ]),
 ('Samedi — la journée de soin', [
   ('08h00', 'Yoga et mise en corps (pratique posturale).'),
   ('09h00', 'Petit-déjeuner partagé.'),
   ('10h – 13h', 'Cycle de soins, groupe 1. Pendant que trois personnes reçoivent leurs soins individuels (corps, psyché, son), les trois autres sont en soutien vibratoire et reçoivent le soin par le son avec David.'),
   ('13h – 15h', 'Pause déjeuner consciente et repos au Nid.'),
   ('15h – 18h', 'Cycle de soins, groupe 2 : rotation des rôles.'),
   ('18h – 19h', 'Temps d’intégration personnelle.'),
   ('19h00', 'Dîner partagé et intégration collective.'),
   ('Nuitée', 'Sommeil sur place, essentiel au processus de digestion psychique.'),
 ]),
 ('Dimanche', [
   ('08h00', 'Pratique de mouvements corporels libres et intuitifs en musique.'),
   ('09h00', 'Petit-déjeuner partagé.'),
   ('10h00', 'Débriefing de groupe et clôture du processus.'),
   ('12h00', 'Dernier repas partagé.'),
   ('13h00', 'Départ.'),
 ]),
]
SOA_INCLUS = [
 'L’expertise de trois intervenants dédiés à votre processus tout au long du week-end.',
 'Trois séances individuelles d’une heure chacune : massage mémoire cellulaire, Intelligence Relationnelle® et alchimie vocale.',
 'L’accès au Nid et l’hébergement au sein de ce lieu.',
]
SOA_MAIL = ('mailto:contact@resonancesproductions.org'
            '?subject=Le%20Soin%20Soa%20%E2%80%94%20demande%20d%E2%80%99inscription')


def soa_ul(items, cls='soa-list'):
    return f'<ul class="{cls}">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


def soa_equipe():
    """Une ligne par intervenant : portrait carre a gauche, texte a droite."""
    out = ''
    for t, n, r, p, ph in SOA_EQUIPE:
        out += (f'<div class="soa-line">{soa_portrait(ph) if ph else ""}'
                f'<div class="who-txt"><h3>{n}</h3><div class="disc">{t}</div>'
                f'<div class="role">{r}</div><p>{p}</p></div></div>')
    return f'<div class="soa-team">{out}</div>'


def soa_prog():
    out = ''
    for day, rows in SOA_PROG:
        li = ''.join(f'<li><b>{h}</b><span>{txt}</span></li>' for h, txt in rows)
        out += f'<div class="soa-day"><h3>{day}</h3><ul>{li}</ul></div>'
    return f'<div class="soa-prog">{out}</div>'


# Sommaire : (ancre, libelle) — doit suivre l'ordre des sections ci-dessous.
TOC = [
 ('intervenants', 'Les intervenants'),
 ('a-qui', 'À qui s’adresse ce soin'),
 ('cadre', 'Le cadre : sécurité et intégrité'),
 ('intention', 'L’intention : trois approches'),
 ('deroulement', 'Comment ça se passe'),
 ('programme', 'Le déroulé du week-end'),
 ('lieu', 'Le lieu : Le Nid'),
 ('repas', 'Les repas'),
 ('cheminement', 'Venir une fois, ou revenir'),
 ('participation', 'Participation & inscription'),
]


def toc():
    li = ''.join(f'<li><a href="#{a}">{t}</a></li>' for a, t in TOC)
    return ('<nav class="toc" aria-label="Sommaire de la page">'
            f'<div class="soa-h">Sommaire</div><ol>{li}</ol></nav>')


HELLO = 'https://www.helloasso.com/associations/resonances-productions'

HTML = f"""<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Le Soin Soa — soin d’incarnation au Nid, Paris 20ᵉ · Résonances Productions</title>
<meta name="description" content="Le Soin Soa : un week-end d’immersion organisé par Résonances Productions au Nid (Paris 20ᵉ), à la rencontre de trois approches — toucher thérapeutique, intelligence relationnelle et alchimie vocale. Six participants, trois intervenants.">
<meta property="og:title" content="Le Soin Soa — soin d’incarnation au Nid, Paris 20ᵉ">
<meta property="og:description" content="Trois approches complémentaires — toucher thérapeutique, intelligence relationnelle et alchimie vocale — le temps d’un week-end d’immersion au Nid, en groupe de six. Un événement organisé par Résonances Productions.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.resonancesproductions.org/le-soin-soa">
<meta property="og:image" content="https://www.resonancesproductions.org/img/soin-soa/affiche-soa-1400.jpg">
<meta property="og:image:width" content="1400">
<meta property="og:image:height" content="1400">
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
    <a href="/le-nid">Le Nid</a>
    <a href="/le-soin-soa" aria-current="page">Le Soin Soa</a>
    <a href="/#statuts">Statuts</a>
    <a href="#contact">Contact</a>
    <a class="adh" href="{HELLO}" target="_blank" rel="noopener">Adhérer</a>
  </div>
</nav>

<header class="soa-top hero-black"><div class="wrap">
  <div class="kick">Événement organisé par Résonances Productions · Le Nid, Paris 20<sup>e</sup></div>
  <h1>Le Soin Soa</h1>
  <div class="tagline">« Renaître à soi au cœur de l’intime »</div>
  <div class="soa-hero">
    <div>
      <p class="lead">Un soin holistique raffiné, né de la rencontre subtile de trois approches complémentaires : le <b>toucher thérapeutique</b>, l’<b>intelligence relationnelle</b> et l’<b>alchimie vocale</b>.</p>
      <p class="body">Trois intervenants réunis autour de vous, le temps d’un week-end d’immersion au Nid, dans un tout petit groupe de six personnes.</p>
      <div class="soa-note"><p>Résonances Productions organise au Nid un <b>week-end d’immersion</b> en tout petit groupe, réunissant trois intervenants autour de la relation au corps, à la parole et au son. Une action inscrite dans l’objet de l’association : soutenir des <b>alternatives humaines</b> et proposer des formats de transmission et d’expérience.</p></div>
      <div class="cta" style="margin-top:26px"><a class="btn" href="{SOA_MAIL}">Demander mon inscription</a><a class="btn ghost" href="#programme">Voir le déroulé →</a></div>
    </div>
    {soa_fig('hero', '(max-width:700px) 100vw, (max-width:860px) 92vw, 520px',
             cls='soa-fig hero-poster', lazy=False, priority=True)}
  </div>
  {toc()}
</div></header>
<div class="hero-fade" aria-hidden="true"></div>

<section class="soa-block" id="intervenants"><div class="wrap">
  <div class="soa-h">Les intervenants</div>
  <h2 class="sec-title">Trois intervenants réunis autour de vous</h2>
  {soa_equipe()}
  <p class="soa-quote">Cette union crée une synergie rare : lorsque le corps est touché, que le cœur est entendu, que la psyché s’éclaire, et que l’âme est mise en vibration, une voie royale s’ouvre. Un espace unique pour se révéler à soi, une véritable re-naissance qu’aucune approche isolée ne peut atteindre.</p>
</div></section>

<div class="divider"></div>

<section class="soa-block band" id="a-qui"><div class="wrap">
  <div class="soa-h">À qui s’adresse ce soin</div>
  <h2 class="sec-title">Un soin pour les êtres déjà engagés sur un chemin de conscience</h2>
  <p>Ce soin ne s’adresse pas à tout le monde. Il est destiné à celles et ceux qui marchent déjà sur un chemin intérieur, qui connaissent la valeur du travail de conscience, et qui sentent qu’il reste des zones d’eux-mêmes encore inaccessibles — souvent gardées par des protecteurs intérieurs.</p>
  <p><b>Ce n’est pas un soin pour débuter.</b> C’est une expérience de descente, vers des couches plus profondes de soi, là où les mots ne suffisent plus.</p>
  {soa_ul(SOA_NEPAS, 'soa-list no')}
</div></section>

<section class="soa-block" id="cadre"><div class="wrap">
  <div class="soa-h">Le cadre</div>
  <h2 class="sec-title">Un espace de sécurité et d’intégrité</h2>
  <p>Notre approche est <b>trauma-informée</b> : elle tient compte de la manière dont le corps, la psyché et le système nerveux se protègent après des expériences vécues comme trop intenses ou trop précoces.</p>
  <p>Nous travaillons avec une conscience fine du <b>trauma complexe</b> — celui qui n’est pas toujours visible, ni même reconnu comme tel. Ce qui fait qu’un trauma est un trauma, ce n’est pas l’événement lui-même : c’est la mémoire souffrante restée engrammée dans le corps et la psyché, quelque chose qui ne s’est pas digéré et qui continue de vibrer dans le présent, souvent de manière très inconsciente. C’est pourquoi nous avançons avec une <b>grande délicatesse</b>, en respectant les rythmes internes, les mécanismes de défense et les parts qui se sont construites pour protéger.</p>
  <p>Ici, aucune posture haute, aucune relation d’emprise. Nous ne sommes ni des gourous ni des figures d’autorité spirituelle. Nous ne projetons pas nos croyances sur vous et nous ne prenons pas le pouvoir sur votre expérience. Ce que nous faisons, c’est <b>écouter</b> : votre corps, votre psyché, votre rythme propre. Nous vous aidons à rendre explicite ce qui cherche à se dire, à nommer l’indicible. Nous vous rejoignons là où vous êtes, sans chercher à vous pousser ailleurs, et nous prenons soin des différentes parts de vous qui demandent à être vues, reconnues, accueillies.</p>
  <p class="soa-quote">Ici, on ne cherche pas à s’évader, mais à s’habiter pleinement.</p>
  <div class="soa-note"><p><b>Le cadre.</b> Ce week-end est une proposition d’expérience et d’accompagnement. <b>Ce n’est pas un acte médical ni un traitement, et il ne remplace pas un suivi médical ou psychologique.</b> Si vous suivez un traitement ou traversez une période de fragilité, parlez-en avec nous avant de vous inscrire : nous en discuterons ensemble en toute confidentialité.</p></div>
</div></section>

<div class="divider"></div>

<section class="soa-block band" id="intention"><div class="wrap">
  <div class="soa-h">L’intention</div>
  <h2 class="sec-title">Trois approches qui dialoguent</h2>
  <p>Le toucher thérapeutique (Gaïa), l’intelligence relationnelle (Iris), la musique vivante et la voix (David) : le corps est touché, le cœur entendu, l’âme mise en vibration. Ce soin cherche à ouvrir un espace pour :</p>
  {soa_ul(SOA_PERMET)}
</div></section>

<section class="soa-block" id="deroulement"><div class="wrap">
  <div class="soa-h">Comment ça se passe</div>
  <h2 class="sec-title">Une ouverture, trois soins, un cercle</h2>
  <p><b>L’ouverture.</b> Chaque session débute par un cercle d’ouverture où nous sommes tous les trois présents à vos côtés. Par des chants, des paroles et des partages, nous posons un cadre de haute sécurité et de profondeur. C’est le moment où le groupe se lie et où l’espace du Nid devient un lieu entièrement dédié au travail.</p>
  <p><b>Vos trois soins individuels.</b> Chaque participant reçoit <b>trois séances individuelles d’une heure</b>, tout en restant baigné dans l’énergie du groupe. Les trois espaces du Nid sont activés simultanément :</p>
  {soa_ul(SOA_ESPACES)}
  {soa_fig('espace-corps', '(max-width:880px) 92vw, 820px', cls='soa-fig soa-wide')}
  <p><b>Le rôle du groupe.</b> Lorsque vous n’êtes pas en soin individuel avec Gaïa ou Iris, vous rejoignez le cœur du cercle autour de David. <b>En soutien</b> : assis ou allongés, vous devenez les gardiens du cadre pour la personne qui reçoit le soin vibratoire — votre présence consciente renforce la sécurité de son processus. <b>En réception</b> : vous bénéficiez vous-même de l’infusion des sons (handpan, harpe, chants), un temps de repos profond et d’intégration par la vibration. Il ne se passe jamais « rien » : vous êtes en permanence porté par le processus.</p>
  {soa_galerie()}
</div></section>

<div class="divider"></div>

<section class="soa-block band" id="programme"><div class="wrap">
  <div class="soa-h">Le déroulé du week-end</div>
  <h2 class="sec-title">Du vendredi soir au dimanche après-midi</h2>
  <p>L’immersion est <b>limitée à six participants</b>, pour préserver l’intimité et la qualité du cadre.</p>
  {soa_prog()}
</div></section>

<section class="soa-block" id="lieu"><div class="wrap">
  <div class="soa-h">Le lieu</div>
  <h2 class="sec-title">Le Nid, un sanctuaire de lumière au cœur de Paris</h2>
  <p>Le soin a lieu au <b>Nid</b>, l’espace de pratique d’Iris Chasles, dans une cour pavée pittoresque du 20<sup>e</sup> arrondissement. C’est un atelier d’artiste niché au sein d’une copropriété habitée exclusivement par des créateurs : dès que l’on franchit le porche de la cour, le tumulte parisien s’efface pour laisser place au silence et à la poésie des pierres anciennes.</p>
  <p>Le Nid se distingue par ses <b>grands volumes</b> et sa <b>hauteur sous plafond</b> généreuse, qui offrent une sensation d’espace et de liberté rare. Baigné de lumière naturelle, il a été pensé comme un véritable cocon « trauma-informé » : un lieu où le système nerveux peut enfin se déposer en toute sécurité. Le lieu lui-même devient un partenaire du processus.</p>
  <div class="cta" style="margin-top:24px"><a class="btn ghost" href="/le-nid">Découvrir Le Nid →</a></div>
</div></section>

<div class="divider"></div>

<section class="soa-block band" id="repas"><div class="wrap">
  <div class="soa-h">Les repas</div>
  <h2 class="sec-title">L’esprit de l’auberge espagnole</h2>
  <p>Nous avons fait le choix conscient de ne pas faire appel à un service de traiteur extérieur, pour deux raisons : <b>préserver le sanctuaire</b>, en maintenant le Nid comme un espace clos et protégé, sans intrusion extérieure, du début à la fin du week-end ; et vous laisser une <b>autonomie douce</b>, au contact de vos propres besoins alimentaires et de votre rythme, sans menu imposé.</p>
  <p>En pratique, nous vous invitons à apporter des plats à partager préparés à l’avance (<b>4 repas et 2 petits-déjeuners</b>), simples et nourrissants. L’idée est de limiter l’usage de la cuisine pour privilégier le silence et la digestion, physique comme psychique. Ce partage de nourriture renforce la convivialité horizontale et authentique du groupe, tout en permettant à chacun de rester dans son propre cocon sensoriel.</p>
</div></section>

<section class="soa-block" id="cheminement"><div class="wrap">
  <div class="soa-h">Un cheminement partagé</div>
  <h2 class="sec-title">Venir une fois, ou revenir</h2>
  <p>Nous avons à cœur de favoriser la constitution d’un <b>groupe de travail sur la durée</b>, composé de personnes prêtes à aller en profondeur et à se rencontrer vraiment. Chaque session peut être vécue de manière autonome, mais nous encourageons la régularité au sein de ce groupe : se retrouver plusieurs fois permet d’ancrer le travail dans le temps et de vivre un processus d’intégration concret, incarné et évolutif.</p>
  <p>Ce soin repose sur une <b>alliance thérapeutique</b> : vous venez avec votre présence et votre conscience, nous vous offrons un cadre sécure, bienveillant et précis pour accompagner votre cheminement, qu’il soit ponctuel ou suivi.</p>
</div></section>

<div class="divider"></div>

<section class="soa-block band" id="participation"><div class="wrap">
  <div class="soa-h">Participation</div>
  <h2 class="sec-title">Valeur et engagement</h2>
  <p>Cette immersion est conçue comme une parenthèse d’exception, où vous bénéficiez d’une attention constante. Votre participation inclut :</p>
  {soa_ul(SOA_INCLUS)}
  <div class="soa-price">
    <div class="amount"><small>Participation</small>425 €</div>
    <p>Dont un <b>acompte de 150 € à l’inscription</b> (non remboursable ni échangeable). Cette participation couvre l’organisation du week-end, la mise à disposition du lieu et la rémunération des intervenants. Elle est perçue par l’association dans le cadre de ses activités, et non par les intervenants à titre personnel. <b>6 places.</b></p>
    <p>Option nuitée supplémentaire au Nid : <b>+ 25 €</b>.</p>
    <div class="cta" style="margin-top:20px"><a class="btn" href="{SOA_MAIL}">Demander mon inscription</a></div>
  </div>
</div></section>

<a class="totop" href="#top" aria-label="Revenir en haut de la page">↑</a>

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
      <p style="margin-top:8px"><a href="{HELLO}" target="_blank" rel="noopener">Adhérer / soutenir</a></p>
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

</body></html>"""

HTML = mobile_nav.inject(HTML)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'soin_soa_final.html')
open(OUT, 'w', encoding='utf-8').write(HTML)
print('WROTE', OUT, round(len(HTML) / 1024), 'KB')
