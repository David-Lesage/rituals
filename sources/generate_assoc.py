# -*- coding: utf-8 -*-
import math

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
background:radial-gradient(1100px 720px at 50% -6%,rgba(143,122,209,.28),transparent 60%),radial-gradient(900px 600px at 85% 108%,rgba(216,178,90,.14),transparent 60%),radial-gradient(700px 500px at 10% 92%,rgba(90,75,138,.28),transparent 60%),var(--night)}
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
.assoc{background:radial-gradient(900px 500px at 88% -10%,rgba(143,122,209,.10),transparent 60%),var(--night)}
/* prestations */
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin-top:44px}
.card{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:16px;padding:28px;transition:transform .25s,border-color .25s;position:relative;display:block}
.card:hover{transform:translateY(-5px);border-color:var(--line)}
.card .t{color:var(--gold);font-size:13px;letter-spacing:.16em;text-transform:uppercase;font-weight:600}
.card h3{font-family:'Cormorant Garamond',serif;font-size:26px;color:#fff;margin:8px 0 10px;font-weight:600}
.card p{color:var(--muted);font-size:15px}
.card .go{color:var(--gold2);font-size:13px;margin-top:14px;display:inline-block}
.card.feature{background:linear-gradient(160deg,rgba(143,122,209,.16),var(--card));border-color:var(--line)}
/* engagements */
.eng{background:linear-gradient(180deg,var(--night),#0b0c1e)}
.vals{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:18px;margin-top:40px}
.val{border-top:1px solid var(--line);padding-top:16px}
.val h3{font-family:'Cormorant Garamond',serif;color:var(--gold2);font-size:20px;font-weight:600}
.val p{color:var(--muted);font-size:14.5px;margin-top:6px}
/* adhesion */
.adhesion{text-align:center;background:radial-gradient(800px 460px at 50% 40%,rgba(216,178,90,.12),transparent 65%),#0b0c1e}
.adhesion .big{font-family:'Cormorant Garamond',serif;font-size:clamp(26px,4vw,40px);color:#fff;font-weight:500;max-width:760px;margin:0 auto}
/* statuts */
.statuts .box{margin-top:34px;background:var(--card);border:1px solid rgba(255,255,255,.07);border-radius:16px;padding:28px;max-width:900px}
.statuts .box p{color:#d3d0e8;margin-bottom:12px}
.statuts .box .art{color:var(--gold);font-size:13px;letter-spacing:.12em;text-transform:uppercase;font-weight:600}
.statuts .box .jo{color:var(--muted);font-size:13.5px;border-left:2px solid var(--gold);padding-left:14px;margin-top:16px}
.statuts .box .jo a{color:var(--gold);text-decoration:none;border-bottom:1px solid rgba(216,178,90,.4)}
/* ===== Le Soin Soa ===== */
.soa{background:radial-gradient(900px 560px at 10% -8%,rgba(143,122,209,.13),transparent 62%),radial-gradient(700px 460px at 92% 102%,rgba(216,178,90,.10),transparent 62%),linear-gradient(180deg,#0b0c1e,var(--night));scroll-margin-top:70px}
.soa .tagline{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(19px,2.8vw,26px);margin-top:10px}
.soa-hero{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,320px);gap:34px;align-items:start;margin-top:32px}
.soa-hero .lead{margin-top:0}
.soa-fig{margin:0;border-radius:16px;overflow:hidden;border:1px solid var(--line);background:var(--card)}
.soa-fig img{display:block;width:100%;height:auto}
.soa-fig figcaption{color:var(--muted);font-size:13px;line-height:1.5;padding:12px 16px 14px;border-top:1px solid rgba(255,255,255,.06)}
.soa-block{margin-top:52px}
.soa-h{color:var(--gold);font-size:13px;letter-spacing:.22em;text-transform:uppercase;font-weight:600;margin-bottom:10px}
.soa-block h3{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(24px,3.2vw,32px);color:#fff;font-weight:600;line-height:1.15}
.soa-block p{max-width:820px;color:#d7d4ea;margin-top:14px}
.soa-cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin-top:26px}
.soa-who{background:var(--card);border:1px solid rgba(255,255,255,.06);border-left:2px solid var(--gold);border-radius:14px;padding:22px 24px}
.soa-who .t{color:var(--gold);font-size:13px;letter-spacing:.14em;text-transform:uppercase;font-weight:600}
.soa-who h4{font-family:'Cormorant Garamond',Georgia,serif;font-size:23px;color:#fff;font-weight:600;margin:6px 0 8px}
.soa-who p{color:var(--muted);font-size:15px;margin:0}
.soa-quote{margin:40px 0 0;font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(21px,3vw,28px);line-height:1.35;border-left:2px solid var(--gold);padding-left:22px;max-width:760px}
.soa-list{list-style:none;margin-top:18px;max-width:820px}
.soa-list li{color:#d7d4ea;font-size:16px;padding:9px 0 9px 26px;position:relative;border-bottom:1px solid rgba(255,255,255,.05)}
.soa-list li:last-child{border-bottom:0}
.soa-list li::before{content:"";position:absolute;left:4px;top:19px;width:6px;height:6px;border-radius:50%;background:var(--gold)}
.soa-list.no li::before{background:none;border:1px solid var(--muted);width:7px;height:7px;top:18px;border-radius:0;transform:rotate(45deg)}
.soa-prog{margin-top:26px;display:grid;gap:18px}
.soa-day{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:14px;padding:22px 24px}
.soa-day h4{font-family:'Cormorant Garamond',Georgia,serif;color:var(--gold2);font-size:21px;font-weight:600;margin-bottom:8px}
.soa-day ul{list-style:none}
.soa-day li{color:var(--muted);font-size:15px;padding:6px 0;display:flex;gap:14px;align-items:baseline;flex-wrap:wrap}
.soa-day li b{color:var(--gold);font-weight:600;font-size:13.5px;letter-spacing:.06em;min-width:104px;flex:0 0 auto}
.soa-day li span{flex:1 1 220px;min-width:0}
.soa-note{color:var(--muted);font-size:14.5px;margin-top:14px;border-left:2px solid var(--gold);padding-left:14px;max-width:760px}
.soa-price{margin-top:26px;background:linear-gradient(160deg,rgba(216,178,90,.12),var(--card));border:1px solid var(--line);border-radius:16px;padding:28px;max-width:820px}
.soa-price .amount{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(34px,5vw,46px);color:#fff;font-weight:600;line-height:1}
.soa-price .amount small{font-family:'Jost',sans-serif;font-size:14px;color:var(--muted);letter-spacing:.16em;text-transform:uppercase;display:block;font-weight:600;margin-bottom:6px}
.soa-price p{color:#d7d4ea;font-size:15px;margin-top:12px}
.soa-gal{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px;margin-top:30px;align-items:start}
.soa-gal .soa-fig img{aspect-ratio:1/1;object-fit:cover;object-position:center}
@media(max-width:860px){.soa-hero{grid-template-columns:1fr;gap:26px}}
@media(max-width:560px){.soa-day li{display:block;padding:9px 0}.soa-day li b{display:block;margin-bottom:1px}}
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

PREST=[
 ('feature','Concert-Rituel','RITUALS','Une prière chantée où le public devient souffle, voix et battement. Musique live, chant collectif et induction, par David Lesage &amp; Iris Chasles. Disponible en <b>duo</b> ou en <b>trio</b> avec saxophones et flûtes.','Découvrir la page','/rituals'),
 ('feature','Spectacle immersif participatif','« E-Motion »','Spectacle immersif et participatif avec <b>danse aérienne à l’élastique</b> et <b>musique live</b>, par <b>ID duo</b> (Iris Chasles &amp; David Lesage). Chant, guidances et pratiques corporelles autour des cinq éléments — le public devient acteur de la représentation.','Découvrir la page','/e-motion'),
 ('','Paris 20ᵉ · Un lieu pour éclore','Le Nid','Un cocon de sécurité qui permet à l’être d’éclore à lui-même : accompagnement psychothérapeutique avec Iris Chasles, concerts de David Lesage, yoga, rythme à la calebasse et cours individuels.','Voir le programme','/le-nid'),
 ('','Musique & voix','David Lesage','Handpan électronique, harpe africaine (Ngoni), voix, percussions et électro : soul française et spiritualité des musiques du monde. Vu à The Voice 11.','',''),
 ('','Soin d’incarnation · Paris 20ᵉ','Le Soin Soa','Un soin holistique né de la rencontre de trois approches complémentaires : le <b>toucher thérapeutique</b>, l’<b>intelligence relationnelle</b> et l’<b>alchimie vocale</b>. Une immersion d’un week-end au Nid, en tout petit groupe.','En savoir plus','#soin-soa'),
 ('','Transmission','Ateliers & formations','Souffle, voix, mouvement et présence : transmettre des outils simples et concrets pour mieux vivre au quotidien.','',''),
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

# ===================== LE SOIN SOA =====================
# Contenu adapte de la page d'Iris Chasles (co-fondatrice) :
# https://www.irischasles.com/agenda-yoga/immersion-therapeutique-soa
#
# --- AJOUTER UNE PHOTO (c'est tout ce qu'il y a a faire) -------------------
# 1) Deposer l'original quelque part, puis generer les declinaisons :
#
#      python3 - <<'EOF'
#      from PIL import Image
#      OUT='/Users/davidlesage/CLAUDE/resonances-site/img/soin-soa/'
#      im=Image.open('MON-ORIGINAL.jpg').convert('RGB'); w0,h0=im.size
#      for w in [480,900,1400]:
#          if w>w0: continue
#          r=im.resize((w,round(h0*w/w0)),Image.LANCZOS)
#          r.save(f'{OUT}mon-nom-{w}.webp','WEBP',quality=80,method=6)
#          r.save(f'{OUT}mon-nom-{w}.jpg','JPEG',quality=82,optimize=True,progressive=True)
#      print(w0,h0)
#      EOF
#
# 2) Ajouter une entree dans SOA_PHOTOS ci-dessous (base = nom sans la largeur,
#    widths = les largeurs reellement generees, w/h = dimensions de l'original).
# 3) La glisser dans SOA_GALERIE (ou l'appeler par son nom dans le HTML).
# --------------------------------------------------------------------------
IMGDIR='/img/soin-soa'
SOA_PHOTOS={
 'affiche':dict(base='affiche-soa',widths=[480,900,1400],w=1600,h=1600,
   alt='Affiche du Soin Soa, soin d’incarnation : motif doré rayonnant sur fond noir, avec les noms d’Iris Chasles, Gaïa Pégourié et David Lesage.',
   cap=''),
 'trois-soins':dict(base='trois-soins',widths=[480,900],w=1024,h=1024,
   alt='Triptyque des trois soins : des mains qui massent un dos, un échange assis face à face, et des mains sur un handpan près d’un bol de cristal.',
   cap='Les trois espaces du soin : le corps, la psyché, le son.'),
 'cercle':dict(base='cercle-au-nid',widths=[480,768],w=768,h=1344,
   alt='Cercle de partage au Nid : six personnes assises sur des coussins autour de trois thérapeutes et de bols chantants, dans un grand atelier d’artiste lumineux.',
   cap='Le cercle de partage au Nid — six participants, trois thérapeutes.'),
 'facade':dict(base='facade-le-nid',widths=[480,600],w=600,h=450,
   alt='Façade vitrée du Nid, ancien atelier d’artiste sur trois niveaux, vue depuis la cour pavée plantée.',
   cap='Le Nid — un ancien atelier d’artiste, dans une cour pavée du 20ᵉ.'),
}
SOA_GALERIE=['trois-soins','cercle','facade']

def soa_fig(key,sizes,cls='soa-fig'):
    p=SOA_PHOTOS[key]; ws=p['widths']; big=ws[-1]
    h=round(p['h']*big/p['w'])
    webp=', '.join(f'{IMGDIR}/{p["base"]}-{w}.webp {w}w' for w in ws)
    jpg=', '.join(f'{IMGDIR}/{p["base"]}-{w}.jpg {w}w' for w in ws)
    cap=f'<figcaption>{p["cap"]}</figcaption>' if p['cap'] else ''
    return (f'<figure class="{cls}"><picture>'
            f'<source type="image/webp" srcset="{webp}" sizes="{sizes}">'
            f'<img src="{IMGDIR}/{p["base"]}-{big}.jpg" srcset="{jpg}" sizes="{sizes}"'
            f' width="{big}" height="{h}" loading="lazy" decoding="async" alt="{p["alt"]}">'
            f'</picture>{cap}</figure>')

def soa_galerie():
    return '<div class="soa-gal">'+''.join(
        soa_fig(k,'(max-width:700px) 92vw, (max-width:1080px) 46vw, 340px') for k in SOA_GALERIE)+'</div>'

SOA_EQUIPE=[
 ('Toucher thérapeutique','Gaïa Pégourié','Experte du toucher thérapeutique et formée au bio-décodage, elle accompagne la libération des mémoires corporelles. Son approche relie le corps et les émotions pour révéler leur langage profond, et met en lumière ce que le corps exprime en silence.'),
 ('Intelligence relationnelle','Iris Chasles','Psychopraticienne à Paris, formée en Intelligence Relationnelle® et en psychopathologie. Son travail porte sur les traumas et les mémoires engrammées, avec une approche neurobiologique de la régulation du système nerveux.'),
 ('Alchimie vocale & musique vivante','David Lesage','Improvisateur formé au jazz et au conservatoire, il utilise la voix comme outil de transformation. Avec ses instruments vibratoires — handpan, harpe africaine, tambour chamanique, bols de cristal et d’or — il façonne en temps réel un espace sonore sur-mesure.'),
]
SOA_PERMET=[
 'Libérer des blocages profonds, physiques ou émotionnels.',
 'Dissoudre des schémas de répétition ou d’auto-sabotage.',
 'Ramener de la tendresse et du lien là où il y a eu de la solitude.',
 'Lever les inhibitions et retrouver la spontanéité du vivant.',
 'Se sentir en cohérence entre son corps, son cœur et sa conscience.',
]
SOA_NEPAS=[
 'Ce n’est pas de l’effleurage.',
 'Ce n’est pas un soin « bien-être » au sens classique.',
 'Ce n’est pas une cérémonie chamanique.',
 'Ce n’est pas un rituel mystique désincarné.',
 'Ce n’est pas une expérience hors du réel.',
]
SOA_ESPACES=[
 '<b>L’Espace Corps</b>, avec Gaïa — massage et libération de la mémoire cellulaire.',
 '<b>L’Espace Psyché</b>, avec Iris — Intelligence Relationnelle® pour réguler et intégrer.',
 '<b>Le Cœur du Cercle</b>, avec David — soin vibratoire et vocal.',
]
SOA_PROG=[
 ('Vendredi soir',[
   ('18h – 20h','Cercle d’ouverture et intentions de travail.'),
 ]),
 ('Samedi — la journée de soin',[
   ('08h00','Yoga et mise en corps (pratique posturale).'),
   ('09h00','Petit-déjeuner partagé.'),
   ('10h – 13h','Cycle de soins, groupe 1. Pendant que trois personnes reçoivent leurs soins individuels (corps, psyché, son), les trois autres sont en soutien vibratoire et reçoivent le soin par le son avec David.'),
   ('13h – 15h','Pause déjeuner consciente et repos au Nid.'),
   ('15h – 18h','Cycle de soins, groupe 2 : rotation des rôles.'),
   ('18h – 19h','Temps d’intégration personnelle.'),
   ('19h00','Dîner partagé et intégration collective.'),
   ('Nuitée','Sommeil sur place, essentiel au processus de digestion psychique.'),
 ]),
 ('Dimanche',[
   ('08h00','Pratique de mouvements corporels libres et intuitifs en musique.'),
   ('09h00','Petit-déjeuner partagé.'),
   ('10h00','Débriefing de groupe et clôture du processus.'),
   ('12h00','Dernier repas partagé.'),
   ('13h00','Départ.'),
 ]),
]
SOA_INCLUS=[
 'L’expertise de trois thérapeutes dédiés à votre processus tout au long du week-end.',
 'Trois séances individuelles d’une heure chacune : massage mémoire cellulaire, Intelligence Relationnelle® et alchimie vocale.',
 'L’accès au Nid et l’hébergement au sein de ce lieu.',
]
SOA_MAIL=('mailto:irischaslesyoga@gmail.com'
          '?subject=Demande%20d%E2%80%99inscription%20au%20Soin%20Soa')

def soa_ul(items,cls='soa-list'):
    return f'<ul class="{cls}">'+''.join(f'<li>{i}</li>' for i in items)+'</ul>'
def soa_equipe():
    return '<div class="soa-cols">'+''.join(
        f'<div class="soa-who"><div class="t">{t}</div><h4>{n}</h4><p>{p}</p></div>'
        for t,n,p in SOA_EQUIPE)+'</div>'
def soa_prog():
    out=''
    for day,rows in SOA_PROG:
        li=''.join(f'<li><b>{h}</b><span>{txt}</span></li>' for h,txt in rows)
        out+=f'<div class="soa-day"><h4>{day}</h4><ul>{li}</ul></div>'
    return f'<div class="soa-prog">{out}</div>'

SOA=f"""<section class="soa" id="soin-soa"><div class="wrap">
  <div class="kick">Soin d’incarnation · Le Nid, Paris 20<sup>e</sup></div>
  <h2 class="sec-title">Le Soin Soa</h2>
  <div class="tagline">« Renaître à soi au cœur de l’intime »</div>
  <div class="soa-hero">
    <div>
      <p class="lead">Un soin holistique raffiné, né de la rencontre subtile de trois approches complémentaires : le <b>toucher thérapeutique</b>, l’<b>intelligence relationnelle</b> et l’<b>alchimie vocale</b>.</p>
      <p class="body">Trois praticiens réunis autour de vous, le temps d’un week-end d’immersion au Nid, dans un tout petit groupe de six personnes.</p>
    </div>
    {soa_fig('affiche','(max-width:860px) 92vw, 320px')}
  </div>
  {soa_equipe()}

  <div class="soa-block">
    <div class="soa-h">À qui s’adresse ce soin</div>
    <h3>Un soin pour les êtres déjà engagés sur un chemin de conscience</h3>
    <p>Ce soin ne s’adresse pas à tout le monde. Il est destiné à celles et ceux qui marchent déjà sur un chemin intérieur, qui connaissent la valeur du travail de conscience, et qui sentent qu’il reste des zones d’eux-mêmes encore inaccessibles — souvent gardées par des protecteurs intérieurs.</p>
    <p><b>Ce n’est pas un soin pour débuter.</b> C’est une expérience de descente, vers des couches plus profondes de soi, là où les mots ne suffisent plus.</p>
    {soa_ul(SOA_NEPAS,'soa-list no')}
  </div>

  <div class="soa-block">
    <div class="soa-h">Le cadre</div>
    <h3>Un espace de sécurité et d’intégrité</h3>
    <p>Notre approche est <b>trauma-informée</b> : elle tient compte de la manière dont le corps, la psyché et le système nerveux se protègent après des expériences vécues comme trop intenses ou trop précoces.</p>
    <p>Nous travaillons avec une conscience fine du <b>trauma complexe</b> — celui qui n’est pas toujours visible, ni même reconnu comme tel. Ce qui fait qu’un trauma est un trauma, ce n’est pas l’événement lui-même : c’est la mémoire souffrante restée engrammée dans le corps et la psyché, quelque chose qui ne s’est pas digéré et qui continue de vibrer dans le présent, souvent de manière très inconsciente. C’est pourquoi nous avançons avec une <b>grande délicatesse</b>, en respectant les rythmes internes, les mécanismes de défense et les parts qui se sont construites pour protéger.</p>
    <p>Ici, aucune posture haute, aucune relation d’emprise. Nous ne sommes ni des gourous ni des figures d’autorité spirituelle. Nous ne projetons pas nos croyances sur vous et nous ne prenons pas le pouvoir sur votre expérience. Ce que nous faisons, c’est <b>écouter</b> : votre corps, votre psyché, votre rythme propre. Nous vous aidons à rendre explicite ce qui cherche à se dire, à nommer l’indicible. Nous vous rejoignons là où vous êtes, sans chercher à vous pousser ailleurs, et nous prenons soin des différentes parts de vous qui demandent à être vues, reconnues, accueillies.</p>
    <p class="soa-quote">Ici, on ne cherche pas à s’évader, mais à s’habiter pleinement.</p>
  </div>

  <div class="soa-block">
    <div class="soa-h">L’intention</div>
    <h3>Trois approches qui dialoguent</h3>
    <p>Le toucher thérapeutique (Gaïa), l’intelligence relationnelle (Iris), la musique vivante et la voix (David) : le corps est touché, le cœur entendu, l’âme mise en vibration. Ce soin cherche à ouvrir un espace pour :</p>
    {soa_ul(SOA_PERMET)}
  </div>

  <div class="soa-block">
    <div class="soa-h">Comment ça se passe</div>
    <h3>Une ouverture, trois soins, un cercle</h3>
    <p><b>L’ouverture.</b> Chaque session débute par un cercle d’ouverture où nous sommes tous les trois présents à vos côtés. Par des chants, des paroles et des partages, nous posons un cadre de haute sécurité et de profondeur. C’est le moment où le groupe se lie et où l’espace du Nid devient un lieu entièrement dédié au travail.</p>
    <p><b>Vos trois soins individuels.</b> Chaque participant reçoit <b>trois séances individuelles d’une heure</b>, tout en restant baigné dans l’énergie du groupe. Les trois espaces du Nid sont activés simultanément :</p>
    {soa_ul(SOA_ESPACES)}
    <p><b>Le rôle du groupe.</b> Lorsque vous n’êtes pas en soin individuel avec Gaïa ou Iris, vous rejoignez le cœur du cercle autour de David. <b>En soutien</b> : assis ou allongés, vous devenez les gardiens du cadre pour la personne qui reçoit le soin vibratoire — votre présence consciente renforce la sécurité de son processus. <b>En réception</b> : vous bénéficiez vous-même de l’infusion des sons (handpan, harpe, chants), un temps de repos profond et d’intégration par la vibration. Il ne se passe jamais « rien » : vous êtes en permanence porté par le processus.</p>
    {soa_galerie()}
  </div>

  <div class="soa-block">
    <div class="soa-h">Le déroulé du week-end</div>
    <h3>Du vendredi soir au dimanche après-midi</h3>
    <p>L’immersion est <b>limitée à six participants</b>, pour préserver l’intimité et la qualité du cadre.</p>
    {soa_prog()}
  </div>

  <div class="soa-block">
    <div class="soa-h">Le lieu</div>
    <h3>Le Nid, un sanctuaire de lumière au cœur de Paris</h3>
    <p>Le soin a lieu au <b>Nid</b>, l’espace de pratique d’Iris Chasles, dans une cour pavée pittoresque du 20<sup>e</sup> arrondissement. C’est un atelier d’artiste niché au sein d’une copropriété habitée exclusivement par des créateurs : dès que l’on franchit le porche de la cour, le tumulte parisien s’efface pour laisser place au silence et à la poésie des pierres anciennes.</p>
    <p>Le Nid se distingue par ses <b>grands volumes</b> et sa <b>hauteur sous plafond</b> généreuse, qui offrent une sensation d’espace et de liberté rare. Baigné de lumière naturelle, il a été pensé comme un véritable cocon « trauma-informé » : un lieu où le système nerveux peut enfin se déposer en toute sécurité. Le lieu lui-même devient un partenaire du processus.</p>
    <div class="cta" style="margin-top:24px"><a class="btn ghost" href="/le-nid">Découvrir Le Nid →</a></div>
  </div>

  <div class="soa-block">
    <div class="soa-h">Les repas</div>
    <h3>L’esprit de l’auberge espagnole</h3>
    <p>Nous avons fait le choix conscient de ne pas faire appel à un service de traiteur extérieur, pour deux raisons : <b>préserver le sanctuaire</b>, en maintenant le Nid comme un espace clos et protégé, sans intrusion extérieure, du début à la fin du week-end ; et vous laisser une <b>autonomie douce</b>, au contact de vos propres besoins alimentaires et de votre rythme, sans menu imposé.</p>
    <p>En pratique, nous vous invitons à apporter des plats à partager préparés à l’avance (<b>4 repas et 2 petits-déjeuners</b>), simples et nourrissants. L’idée est de limiter l’usage de la cuisine pour privilégier le silence et la digestion, physique comme psychique. Ce partage de nourriture renforce la convivialité horizontale et authentique du groupe, tout en permettant à chacun de rester dans son propre cocon sensoriel.</p>
  </div>

  <div class="soa-block">
    <div class="soa-h">Un cheminement partagé</div>
    <h3>Venir une fois, ou revenir</h3>
    <p>Nous avons à cœur de favoriser la constitution d’un <b>groupe de travail sur la durée</b>, composé de personnes prêtes à aller en profondeur et à se rencontrer vraiment. Chaque session peut être vécue de manière autonome, mais nous encourageons la régularité au sein de ce groupe : se retrouver plusieurs fois permet d’ancrer le travail dans le temps et de vivre un processus d’intégration concret, incarné et évolutif.</p>
    <p>Ce soin repose sur une <b>alliance thérapeutique</b> : vous venez avec votre présence et votre conscience, nous vous offrons un cadre sécure, bienveillant et précis pour accompagner votre cheminement, qu’il soit ponctuel ou suivi.</p>
  </div>

  <div class="soa-block">
    <div class="soa-h">Participation</div>
    <h3>Valeur et engagement</h3>
    <p>Cette immersion est conçue comme une parenthèse d’exception, où vous bénéficiez d’une attention constante. Votre participation inclut :</p>
    {soa_ul(SOA_INCLUS)}
    <div class="soa-price">
      <div class="amount"><small>Participation</small>425 €</div>
      <p><b>Acompte de 150 €</b> pour valider votre place (non remboursable ni échangeable) — <b>6 places</b>.</p>
      <p>Option nuitée supplémentaire au Nid : <b>+ 25 €</b>.</p>
      <div class="cta" style="margin-top:20px"><a class="btn" href="{SOA_MAIL}">Demander mon inscription</a></div>
    </div>
  </div>
</div></section>"""
# ===================== /LE SOIN SOA =====================

VALS=[
 ('Le vivant','Placer l’humain, la nature et la vibration au cœur de chaque projet.'),
 ('La créativité','Accompagner et produire des artistes, dans tous les domaines.'),
 ('Le bien-être','Proposer des expériences qui apaisent, relient et élèvent.'),
 ('L’indépendance','Une démarche libre, inclusive, sans appartenance religieuse, philosophique ou politique.'),
]
def vals():
    return ''.join(f'<div class="val"><h3>{h}</h3><p>{p}</p></div>' for h,p in VALS)

HELLO='https://www.helloasso.com/associations/resonances-productions'

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
  <meta property="og:image" content="https://www.resonancesproductions.org/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
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
  <h2 class="sec-title">Mettre l’art au service du vivant</h2>
  <p class="body">L’Association <b>Résonances Productions</b> (loi 1901) a pour objectif l’<b>accompagnement</b>, la <b>promotion</b>, la <b>production</b> et le <b>soutien d’artistes</b> dans tous les domaines, ainsi que d’initier ou de soutenir des actions autour d’alternatives de toutes natures — écologiques, économiques, culturelles, techniques et humaines.</p>
  <p class="body">Elle s’appuie sur plusieurs supports (lettres d’information, site internet, plateformes multimédias, format papier…) et plusieurs moyens : journalisme, publications, formations, organisation d’événements. Les activités de l’association s’exercent <b>indépendamment de toute appartenance religieuse, philosophique ou politique</b>.</p>
</div></section>

<div class="divider"></div>

<section id="prestations"><div class="wrap">
  <div class="kick">Nos prestations</div>
  <h2 class="sec-title">Créations, spectacles & expériences</h2>
  <p class="lead">De la scène au soin sonore, l’association porte des projets qui relient l’art, le corps et la conscience.</p>
  <div class="grid">{cards()}</div>
</div></section>

<div class="divider"></div>

{SOA}

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

<section class="statuts" id="statuts"><div class="wrap">
  <div class="kick">Cadre légal</div>
  <h2 class="sec-title">Les statuts</h2>
  <div class="box">
    <div class="art">Article 1 — Constitution & dénomination</div>
    <p>Association régie par la loi du 1<sup>er</sup> juillet 1901 et le décret du 16 août 1901, sous la dénomination « <b>Résonances Productions</b> ».</p>
    <div class="art">Article 2 — Objet</div>
    <p>« L’accompagnement, la promotion, la production et le soutien dans tous les domaines ainsi que d’initier ou de soutenir des actions à propos d’alternatives de toutes natures (écologiques, économiques, culturelles, techniques et humaines). Elle utilisera pour cela plusieurs supports (lettres d’information, site internet, plateforme multimédias, format papier etc.) et de plusieurs moyens (journalisme, publications, formations, organisations d’évènements etc.). Les activités de l’association s’exercent indépendamment de toute appartenance religieuse, philosophique ou politique. L’association pourra réaliser toutes opérations avec les tiers liées directement ou indirectement à son objet. »</p>
    <p class="jo">Objet officiel tel que déclaré au <b>Journal officiel des associations</b>. Déclaration à la sous-préfecture de Pamiers, publiée le 28 octobre 2017 — n° RNA <b>W092002501</b>. <a href="https://www.journal-officiel.gouv.fr/document/associations_b/201700430125" target="_blank" rel="noopener">Consulter l’annonce officielle (JOAFE)</a></p>
    
    <p class="jo"><a href="https://docs.google.com/document/d/1NxsbvaqHsA9VOXlN7cvsav7cxFwhsK4XCpowHb75o1w/edit?usp=sharing" target="_blank" rel="noopener">Statuts de l’association</a></p>
        <p class="jo"><a href="https://annuaire-entreprises.data.gouv.fr/entreprise/resonances-productions-919514075" target="_blank" rel="noopener">Fiche officielle de l’association (annuaire des entreprises — data.gouv.fr)</a></p>
  </div>
</div></section>

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
  <div class="legal">© {2026} Résonances Productions · resonancesproductions.org</div>
</div></footer>

</body></html>"""

open('assoc_index.html','w',encoding='utf-8').write(HTML)
print('WROTE assoc_index.html', round(len(HTML)/1024),'KB')
