# -*- coding: utf-8 -*-
import base64, io, glob
import os
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

def enc(im,q):
    b=io.BytesIO(); im.convert('RGB').save(b,'JPEG',quality=q,optimize=True)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
def find(tok): return sorted(glob.glob('promo_raw/*'+tok+'*'))[0]
def promo(tok,mw,q=80,crop=None):
    im=Image.open(find(tok)).convert('RGB')
    if crop:
        w,h=im.size; im=im.crop((int(crop[0]*w),int(crop[1]*h),int(crop[2]*w),int(crop[3]*h)))
    im.thumbnail((mw,mw)); return enc(im,q)
def web(fn,mw,q=80,crop=None):
    im=Image.open('web_img/'+fn).convert('RGB')
    if crop:
        w,h=im.size; im=im.crop((int(crop[0]*w),int(crop[1]*h),int(crop[2]*w),int(crop[3]*h)))
    im.thumbnail((mw,mw)); return enc(im,q)

header=web('RITUALS_00_header.jpg',1700,84)
public=promo('20248.',1300)
faceaface=promo('everness_faceaface',1300)
priere=promo('iris_priere',1300)
key=promo('20245.',1500)
david=promo('David_Lesage_2025_Carre',1000,86)
iris=web('RITUALS_06_Iris-Chasles.jpg',760,84,crop=(0.20,0.0,0.82,0.78))


# ---- photos Perspective (formation trio) ----
_PD = open('/tmp/photodir.txt').read()
def persp(fn, mw, q=84):
    im=Image.open(os.path.join(_PD,fn)).convert('RGB'); im.thumbnail((mw,mw)); return enc(im,q)
trio_scene = persp('perspectives 1 .jpg', 1700)
julien_port = persp('Julien Dub Portrait 16:9.jpg', 1000)
PERSP_GAL = [('perspectives 2 .jpg','Julien Dub au saxophone'),
 ('perspectives 5 .jpg','Julien & David — le souffle et le rythme'),
 ('perspectives 6 .jpg','La danse collective'),
 ('perspectives 7 .jpg','Iris & David — l’instant de la prière'),
 ('perspectives 8 .jpg','Iris Chasles — le chant qui relie'),
 ('perspectives 12 .jpg','Le final, tous ensemble')]

GAL=[('202417.','Le corps en mouvement'),('202418.','Une connexion forte avec le public'),
('202419.','Danser la vie'),('202420.','Everness Festival, Hongrie'),('202422.','S’ouvrir, s’offrir'),
('202423.','L’élan'),('202424.','Deux êtres, une intention'),('Solune_31','Le tournoiement de la beauté'),
('202428.','Un univers musical électro-organique'),('202443.','Respirer en mouvement'),
('202444.','Retrouver son enfant intérieur'),('202450.','Être touché dans son cœur'),
('202451.','Chanter la joie'),('202452.','Chanter ensemble'),('19-42-24','Touchée par la grâce'),
('David_Lesage_2025_Carre','David Lesage'),('RITUALS_07_duo','David & Iris')]
GALI=[(promo(t,1100),c) for t,c in GAL]
_PG=[(persp(f,1100),c) for f,c in PERSP_GAL]
_m=[];_i=_j=0
while _i<len(GALI) or _j<len(_PG):
    if _j>=len(_PG) or (_i<len(GALI) and (_i+1)/max(len(GALI),1)<=(_j+1)/max(len(_PG),1)):
        _m.append(GALI[_i]);_i+=1
    else:
        _m.append(_PG[_j]);_j+=1
GALI=[(trio_scene,'Le trio en scène — festival Perspectives')]+_m+[(julien_port,'Julien Dub')]

QUOTES=['Je suis repartie émerveillée, ressourcée.',
'J’ai vécu un moment de légèreté, d’amour, de joie, de partage — c’était vraiment un voyage magnifique !',
'J’ai vécu une expérience puissante. Mêlant plusieurs pratiques — le chant, la danse, la respiration — ce spectacle est avant tout et surtout VIVANT !',
'Beaucoup d’émotions m’ont traversé. Je n’ai jamais vécu cela auparavant.',
'Votre spectacle m’a rassuré et me donne espoir en l’Amour.',
'J’ai été en apesanteur comme jamais — spectacle inventif et tellement original.',
'Expérience incroyable, émerveillement et enchantement.',
'Un moment suspendu, magique, inattendu, porté par deux êtres d’une beauté et d’une bonté rares.',
'Spectacle à avoir absolument dans sa programmation tant il est original, novateur et bénéfique. Engagé, profond et surtout féerique !',
'Et au final, tous debout, le visage rayonnant, applaudissant sans discontinuer !',
'Spectacle très surprenant, on est transporté dans un autre monde.',
'On en ressort bouleversé et, en même temps, apaisé. Il est ludique et joyeux.']

CSS="""
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
:root{--night:#0e0f24;--night2:#12132b;--ink:#eae7f3;--muted:#a9a6c4;--gold:#d8b25a;--gold2:#f0d18a;--plum:#8f7ad1;--card:#191b3d;--line:rgba(216,178,90,.30)}
html,body{background:#0e0f24}
body{color:var(--ink);font-family:Helvetica,Arial,sans-serif;font-size:11pt;line-height:1.6}
h1,h2,h3,.serif{font-family:Georgia,'Times New Roman',serif}
b{color:#fff}
.page{width:210mm;min-height:297mm;padding:20mm;background:var(--night);position:relative;overflow:hidden;page-break-after:always}
.page.tight{padding:16mm 18mm}
.kick{letter-spacing:.32em;text-transform:uppercase;font-size:8.5pt;font-weight:bold;color:var(--gold);margin-bottom:8pt}
.title{font-family:Georgia,serif;font-size:30pt;color:#fff;font-weight:bold;line-height:1.05;margin-bottom:6pt}
.lead{color:var(--muted);font-size:12pt;margin-bottom:6pt}
p{margin-bottom:9pt;color:#d7d4ea}
.sig{font-family:Georgia,serif;font-style:italic;color:var(--gold2);font-size:15pt;text-align:center;margin-top:14pt}
/* cover */
.cover{padding:0;display:flex;align-items:center;justify-content:center;text-align:center;
background:linear-gradient(rgba(10,11,28,.55),rgba(10,11,28,.8)),url(__HEADER__);background-size:cover;background-position:center}
.cover .ci{padding:20mm}
.cover .k{letter-spacing:.34em;text-transform:uppercase;font-size:10pt;color:var(--gold2);font-weight:bold}
.cover h1{font-family:Georgia,serif;font-size:66pt;color:#fff;letter-spacing:.06em;margin:6pt 0}
.cover .sub{font-family:Georgia,serif;font-style:italic;color:var(--gold2);font-size:18pt}
.cover .names{letter-spacing:.28em;text-transform:uppercase;font-size:10pt;color:#e7e4f5;margin-top:14pt}
.cover .tag{font-family:Georgia,serif;font-style:italic;color:#efeaf6;font-size:14pt;margin-top:16pt;line-height:1.4}
.bigq{font-family:Georgia,serif;font-size:22pt;color:#fff;line-height:1.25;margin-bottom:14pt}
.bigq em{color:var(--gold2);font-style:italic}
.fig{margin-top:12pt;border:1px solid var(--line);border-radius:8pt;overflow:hidden}
.fig img{width:100%;display:block}
.cap{color:var(--muted);font-size:8.5pt;font-style:italic;margin-top:5pt;text-align:center}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:7mm;margin-top:10pt}
.card{background:var(--card);border:1px solid rgba(255,255,255,.07);border-radius:8pt;padding:12pt}
.card .n{font-family:Georgia,serif;font-size:20pt;color:var(--gold)}
.card h3{color:#fff;font-size:12pt;margin:4pt 0}
.card p{color:var(--muted);font-size:9.5pt;margin:0}
.steps{margin-top:10pt;border-left:2px solid var(--line);padding-left:14pt}
.step{margin-bottom:12pt}
.step .t{color:var(--gold2);font-size:8pt;letter-spacing:.2em;text-transform:uppercase;font-weight:bold}
.step h3{font-family:Georgia,serif;font-size:14pt;color:#fff;margin:1pt 0}
.step p{color:var(--muted);font-size:10pt;margin:0}
.key{padding:0;display:flex;align-items:center;justify-content:center;text-align:center;
background:linear-gradient(rgba(11,12,30,.78),rgba(11,12,30,.9)),url(__KEY__);background-size:cover;background-position:center 35%}
.key .ci{padding:24mm}
.artist{display:grid;grid-template-columns:42mm 1fr;gap:8mm;align-items:start;margin-top:12pt}
.artist img{width:100%;border-radius:8pt;border:1px solid var(--line)}
.artist h3{font-family:Georgia,serif;font-size:20pt;color:#fff}
.artist .role{color:var(--gold);font-size:8.5pt;letter-spacing:.1em;text-transform:uppercase;font-weight:bold;margin:3pt 0 6pt}
.artist p{color:#d3d0e8;font-size:10pt}
.third{margin-top:12pt;border:1px dashed var(--line);border-radius:8pt;padding:10pt;color:var(--muted);font-size:10pt}
.quotes{columns:2;column-gap:7mm;margin-top:10pt}
.q{break-inside:avoid;background:var(--card);border-left:3px solid var(--gold);border-radius:6pt;padding:9pt 11pt;margin-bottom:7pt;font-family:Georgia,serif;font-style:italic;font-size:11pt;color:#e7e4f5}
.gal{display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:10pt}
.gal .it{break-inside:avoid}
.gal img{width:100%;height:52mm;object-fit:cover;border-radius:6pt;border:1px solid rgba(255,255,255,.08);display:block}
.gal .c{color:var(--muted);font-size:8.5pt;font-style:italic;margin-top:3pt}
table{width:100%;border-collapse:collapse;font-size:8.5pt;margin-top:8pt}
th{text-align:left;color:var(--gold);text-transform:uppercase;letter-spacing:.08em;font-size:7.5pt;padding:5pt 6pt;border-bottom:1px solid var(--line);background:rgba(255,255,255,.03)}
td{padding:5pt 6pt;border-bottom:1px solid rgba(255,255,255,.06);color:#d3d0e8}
.two{display:grid;grid-template-columns:1fr 1fr;gap:7mm;margin-top:10pt}
.sc{background:var(--card);border:1px solid var(--line);border-radius:8pt;padding:12pt}
.sc h3{font-family:Georgia,serif;color:var(--gold2);font-size:13pt;margin-bottom:4pt}
.sc p{color:var(--muted);font-size:9.5pt;margin:0}
.contact{text-align:center}
.contact h2{font-family:Georgia,serif;font-size:26pt;color:#fff;margin-bottom:14pt}
.contact .c{margin:8pt 0;color:#d3d0e8;font-size:11pt}
.contact .c b{color:var(--gold2);font-family:Georgia,serif;font-size:14pt;display:block}
.footer{position:absolute;bottom:12mm;left:0;right:0;text-align:center;color:var(--muted);font-size:8pt;font-style:italic}
"""

def cards():
    it=[('I','La respiration','Se déposer, ralentir, accorder son souffle à celui du groupe pour ouvrir un état de conscience élargie.'),
        ('II','Le mouvement','Danse libre du public et danse de tournoiement d’Iris : le corps se délie, l’énergie circule.'),
        ('III','L’induction','La voix d’Iris guide, comme une hypnose douce, dans les transitions comme au cœur des morceaux.'),
        ('IV','Les chants collectifs','Affirmations positives et mantras portés par tous — que l’on sache chanter ou non.'),
        ('V','Les affirmations','Déposer une intention, la vibrer ensemble, repartir avec un élan clair et partagé.')]
    return ''.join(f'<div class="card"><div class="n">{n}</div><h3>{t}</h3><p>{d}</p></div>' for n,t,d in it)
def steps():
    it=[('Ouverture','L’appel & le lien','Brise-glace en musique : on occupe l’espace, on se regarde (eyes contact). Le lien se crée.'),
        ('Immersion','Le voyage sonore','Handpan, voix, percussions électro et acoustiques, nappes électro ; le public se laisse traverser.'),
        ('Élan','Le chant collectif','Affirmations positives et mantras portés par tous : la salle devient un seul chœur.'),
        ('Bascule','La transe douce','Respiration guidée et mouvement libre ou suggéré.'),
        ('Cœur','La prière','La clé de voûte : guidés par le souffle, un élan de communion, une parole intime que le collectif porte plus haut.'),
        ('Libération','Le final dansant','La musique électro organique s’intensifie, le collectif danse et chante ; on repart léger.')]
    return ''.join(f'<div class="step"><div class="t">{t}</div><h3>{h}</h3><p>{d}</p></div>' for t,h,d in it)
def patch():
    rows=[['1','Voix 1 — David (chant)','Micro DPA serre-tête HF','Micro : artiste · Système : orga'],
    ['2','Voix 2 — Iris','Micro main HF','Organisation'],['3','Voix 3 — Julien','Micro main HF','Organisation'],
    ['4','Handpan électronique','DI (ligne)','Artiste'],['5','Harpe africaine (Ngoni)','Micro AKG C411 / DI','Artiste'],
    ['6','Looper (RC-505 MK2)','DI stéréo','Artiste'],['7','Kick & pad — Erae 2 (Ableton)','DI / ligne','Artiste'],
    ['8','Calebasse','Micro Shure Beta 91A','Artiste'],['9','Corde (guitare / violoncelle)','DI / micro','Artiste / orga'],
    ['10','MacBook Pro (Ableton Live)','DI stéréo','Artiste']]
    body=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return '<table><thead><tr><th>#</th><th>Source</th><th>Micro / DI</th><th>Fourni par</th></tr></thead><tbody>'+body+'</tbody></table>'
def galpages():
    out=''
    for i in range(0,len(GALI),6):
        chunk=GALI[i:i+6]
        cells=''.join(f'<div class="it"><img src="{src}"><div class="c">{c}</div></div>' for src,c in chunk)
        first = i==0
        head='<div class="kick">Galerie</div><div class="title">En scène</div>' if first else ''
        out+=f'<section class="page tight">{head}<div class="gal">{cells}</div></section>'
    return out
def quotes():
    return ''.join(f'<div class="q">« {q} »</div>' for q in QUOTES)

HTML=f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<section class="page cover"><div class="ci">
  <div class="k">Concert — Rituel</div>
  <h1>RITUALS</h1>
  <div class="sub">une prière chantée</div>
  <div class="names">David Lesage &nbsp;·&nbsp; Iris Chasles &nbsp;·&nbsp; Julien Dub</div>
  <div class="tag">Il ne se regarde pas. Il se traverse.<br>Le public devient souffle, voix et battement.</div>
</div></section>

<section class="page"><div class="kick">Note d’intention</div>
  <div class="bigq">Il y a des soirs où l’on ne va pas <em>voir</em> un concert.<br>On y <em>entre</em>.</div>
  <p>RITUALS n’est pas un spectacle que l’on suit depuis un fauteuil. C’est <b>une expérience qui se vit de l’intérieur</b> — une traversée où chacun cesse d’être spectateur pour <b>devenir acteur de ce qui se vit</b>. Né dans la lignée du spectacle-rituel E-motion du duo Solune (Iris Chasles et David Lesage), il en garde le cœur — <b>musique, mouvement, respiration et guidances</b> — dans une <b>forme allégée et en trio</b>, pensée pour les scènes qui n’ont pas l’infrastructure d’un grand spectacle de danse aérienne.</p>
  <p>Deux forces le portent : la <b>musique live</b>, menée par David et Julien, et l’<b>induction par la voix</b>, tenue par Iris. Ensemble, elles poussent loin la dimension d’<b>état de conscience élargie</b> — sans jamais peser.</p>
  <p>La dimension spirituelle est forte, mais tenue à distance de tout code : <b>ni new age</b>, ni référence à une école ou une croyance. Rien n’est imposé — tout est <b>invitation</b>, à la mesure de chacun. Le sacré n’exclut pas la joie : le rituel garde <b>le goût du jeu, du fun et de la détente</b>, jusqu’à <b>un final dansant</b> où le collectif se relâche ensemble. Une <b>communion simple, sincère et universelle</b>.</p>
  <div class="fig"><img src="{public}"></div><div class="cap">Le public au cœur du rituel</div>
  <div class="sig">On en repart plus léger. Comme au sortir d’une longue inspiration.</div>
</section>

<section class="page"><div class="kick">L’expérience</div><div class="title">Un concert-rituel en cinq portes</div>
  <p class="lead">L’expérience alterne écoute active et temps participatifs, guidés avec douceur et portés par la musique.</p>
  <div class="grid2">{cards()}</div>
  <div class="fig">{'<img src="'+faceaface+'">'}</div><div class="cap">Iris &amp; David, face à face — le dialogue de deux présences</div>
</section>

<section class="page"><div class="kick">Le voyage</div><div class="title">D’un univers à l’autre</div>
  <p class="lead">Des temps dansants et rythmés, d’autres méditatifs et introspectifs. Durée : 75 à 90 min, modulable jusqu’à 2h.</p>
  <div class="steps">{steps()}</div>
</section>

<section class="page key"><div class="ci">
  <div class="kick" style="color:var(--gold2)">La clé de voûte</div>
  <div class="bigq" style="max-width:150mm;margin:0 auto">Au centre du rituel, un moment que l’on ne raconte pas : on le <em>traverse</em>. Une communion sincère — où certains lâchent enfin, où certains pleurent, touchés là où cela avait besoin d’être vu et apaisé.</div>
</div></section>

<section class="page"><div class="kick">Les artistes</div><div class="title">Trois souffles, un rituel</div>
  <div class="artist"><img src="{david}"><div>
    <h3>David Lesage</h3><div class="role">Voix · Handpan électronique · Harpe africaine Ngoni · Pads · Percussions</div>
    <p>Chanteur, musicien et compositeur, David porte la dimension musicale du projet. Son univers mêle soul française, spiritualité des musiques du monde et vibrations électroniques. Sa voix dialogue avec le handpan électronique, la harpe africaine (Ngoni), les pads et les percussions. Créateur d’expériences immersives et de soins sonores. (Vu à The Voice 11.)</p>
  </div></div>
  <div class="artist"><img src="{iris}"><div>
    <h3>Iris Chasles</h3><div class="role">Induction & Voix · Calebasse · Danse de tournoiement</div>
    <p>Sa fonction première : l’induction. Par la voix, Iris amène le public vers un état de conscience élargie. Elle apporte aussi un soutien rythmique à la calebasse et à la voix. Psychopraticienne en intelligence relationnelle, yoga-thérapeute et danseuse, elle veille à ce que chaque proposition reste une invitation, douce et sécurisante.</p>
  </div></div>
  <div class="art"><img src="{julien_port}"><div><h3>Julien Dub</h3><div class="role">Saxophone soprano · Flûtes · Percussions · Guitare · Claviers · Voix</div><p>Son parcours l’a mené des <b>musiques du monde</b> — gnawa, latines, réunionnaises — au jazz, à la funk et au rocksteady, de Paris jusqu’en Inde. Il participe activement à la scène créative parisienne.</p><p>Dans RITUALS, il apporte le <b>souffle</b> : saxophone soprano et flûtes, percussions, guitare, claviers et secondes voix — une matière mélodique et aérienne qui dialogue avec le handpan et la voix.</p></div></div>
</section>

<section class="page"><div class="kick">Ils l’ont vécu</div><div class="title">Ce qu’en disent les publics</div>
  <div class="quotes">{quotes()}</div>
</section>

{galpages()}

<section class="page"><div class="kick">Pour les organisateurs</div><div class="title">S’adapter à votre scène</div>
  <p class="lead">Forme modulable, de la scène intime au grand plateau. Pour festivals de musique, danse, spectacle vivant, bien-être — mais aussi théâtres, cinémas, salles de concert et lieux immersifs.</p>
  <div class="two">
    <div class="sc"><h3>Version cercle — scène intime</h3><p>Enveloppante, en proximité (idéale sous tente / petite scène). Chuchotements, prière chantée, communion resserrée.</p></div>
    <div class="sc"><h3>Version grand plateau</h3><p>Plus ample et rythmée, pour porter le rituel à l’échelle de plusieurs centaines de personnes, jusqu’au final dansant.</p></div>
  </div>
  <div class="kick" style="margin-top:14pt">Fiche technique — patch son (≈ 10 entrées)</div>
  {patch()}
  <p class="cap" style="text-align:left;margin-top:6pt">1 ingénieur son + matériel pro (façade + retours) fournis par l’organisation. Retours : 3 wedges + 1 in-ear HF (artiste). Loges chauffées, hébergement des 3 artistes et repas (3 dont 1 végétarien, midi et soir) à la charge de l’organisateur. Fiche détaillée sur demande.</p>
</section>

<section class="page contact"><div style="margin-top:40mm">
  <div class="kick" style="text-align:center">Contact & diffusion</div>
  <h2>Parlons de votre événement</h2>
  <div class="c"><b>Résonances Productions</b>contact@resonancesproductions.org<br>www.resonancesproductions.org</div>
  <div class="c"><b>David Lesage</b>06 10 73 31 52<br>lesagedavid.fr · @david.lesage.artiste</div>
  <div class="c"><b>Iris Chasles</b>06 89 05 47 58<br>irischasles.com · @iris_chasles</div>
  <div class="c"><b>Julien Dub</b>juliendub.com · @julien_dub_</div>
  <div class="sig" style="margin-top:24pt">RITUALS — Concert-Rituel en trio · David Lesage, Iris Chasles & Julien Dub</div>
</div><div class="footer">Résonances Productions — Art du spectacle vivant</div></section>

</body></html>"""
html=HTML.replace('__HEADER__',header).replace('__KEY__',key)
open('plaquette_trio.html','w',encoding='utf-8').write(html)
print('WROTE plaquette_trio.html', round(len(html)/1024),'KB')
