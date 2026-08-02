const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,Table,TableRow,TableCell,WidthType,BorderStyle,AlignmentType}=require('docx');
const OUT='/sessions/pensive-cool-lamport/mnt/outputs/';
const GOLD='B8912E', INK='1F2033', SOFT='6B6B7A', LINE='CFCADB', NIGHT='1B1C3B';
const S='Calibri', SER='Georgia';

const t=(x,o={})=>new TextRun({text:x,font:o.f||S,size:o.s||20,bold:o.b,italics:o.i,color:o.c||INK,break:o.break});
const p=(runs,o={})=>new Paragraph({spacing:{after:o.after??110,line:o.line??268},alignment:o.al,children:(Array.isArray(runs)?runs:[runs]).map(r=>typeof r==='string'?t(r,o):r)});
const h=(x)=>new Paragraph({spacing:{before:240,after:100},children:[new TextRun({text:x.toUpperCase(),font:SER,bold:true,size:24,color:NIGHT,characterSpacing:20})],border:{bottom:{color:LINE,style:BorderStyle.SINGLE,size:6,space:4}}});
const kick=(x)=>new Paragraph({spacing:{after:40},children:[new TextRun({text:x.toUpperCase(),font:S,bold:true,size:16,color:GOLD,characterSpacing:60})]});
const NB={top:{style:BorderStyle.NONE},bottom:{style:BorderStyle.NONE},left:{style:BorderStyle.NONE},right:{style:BorderStyle.NONE},insideHorizontal:{style:BorderStyle.NONE},insideVertical:{style:BorderStyle.NONE}};

function masthead(sub){
  return [
    new Paragraph({spacing:{after:6},children:[new TextRun({text:'RITUALS',font:SER,bold:true,size:52,color:NIGHT,characterSpacing:30})]}),
    p([t('Concert-Rituel en trio · David Lesage · Iris Chasles · Julien Dub',{c:SOFT,s:20,i:true})],{after:6}),
    p([t(sub,{c:GOLD,s:18,b:true})],{after:180}),
  ];
}

/* patch + matériel tables */
function cell(txt,w,bold,head){return new TableCell({width:{size:w,type:WidthType.DXA},margins:{top:60,bottom:60,left:100,right:100},shading:head?{fill:'F3EFE3'}:undefined,children:[p([t(txt,{b:bold||head,s:17,c:head?INK:INK})],{after:0,line:240})]});}
function row(cells,widths,head){return new TableRow({children:cells.map((c,i)=>cell(c,widths[i],false,head))});}
function tbl(header,rows,widths){
  const total=widths.reduce((a,b)=>a+b,0);
  return new Table({width:{size:total,type:WidthType.DXA},columnWidths:widths,
    borders:{top:{style:BorderStyle.SINGLE,size:4,color:LINE},bottom:{style:BorderStyle.SINGLE,size:4,color:LINE},left:{style:BorderStyle.NONE},right:{style:BorderStyle.NONE},insideHorizontal:{style:BorderStyle.SINGLE,size:4,color:LINE},insideVertical:{style:BorderStyle.NONE}},
    rows:[row(header,widths,true),...rows.map(r=>row(r,widths))]});
}

/* ---------- 1. COMMUNIQUÉ / PRÉSENTATION ---------- */
const communique=[
  ...masthead('Communiqué / présentation — « une prière chantée » · formation trio'),
  p([t('Il ne se regarde pas. Il se traverse. Le public devient souffle, voix et battement.',{f:SER,i:true,s:26,c:NIGHT})],{after:160}),

  h('Note d’intention'),
  p('Il y a des soirs où l’on ne va pas voir un concert. On y entre.'),
  p('RITUALS n’est pas un spectacle que l’on suit depuis un fauteuil. C’est une expérience qui se vit de l’intérieur — une traversée où chacun cesse d’être spectateur pour devenir acteur de ce qui se vit. Né dans la lignée du spectacle-rituel E-motion du duo Solune (Iris Chasles et David Lesage), il en garde le cœur — musique, mouvement, respiration et guidances — dans une forme allégée et en trio, pensée pour les scènes qui n’ont pas l’infrastructure d’un grand spectacle de danse aérienne.'),
  p('Deux forces le portent : la musique live, menée par David et Julien, et l’induction par la voix, tenue par Iris. Ensemble, elles poussent loin la dimension d’état de conscience élargie — sans jamais peser.'),
  p('La dimension spirituelle est forte, mais tenue à distance de tout code : ni new age, ni référence à une école ou une croyance, ni cérémonie sévère. Rien n’est imposé — tout est invitation, à la mesure de chacun. Le sacré n’exclut pas la joie : le rituel garde le goût du jeu, du fun et de la détente, jusqu’à un final dansant où le collectif se relâche ensemble. Une communion simple, sincère et universelle.'),
  p([t('On en repart plus léger. Comme au sortir d’une longue inspiration.',{f:SER,i:true,s:22,c:GOLD})],{al:AlignmentType.CENTER,after:160}),

  h('L’expérience — cinq portes'),
  p([t('La respiration',{b:true}),t(' · se déposer et s’accorder au groupe.  ',{}),t('Le mouvement',{b:true}),t(' · danse libre du public et danse de tournoiement d’Iris.  ',{}),t('L’induction',{b:true}),t(' · la voix qui guide, comme une hypnose douce.  ',{}),t('Les chants collectifs',{b:true}),t(' · mantras et affirmations portés par tous.  ',{}),t('Les affirmations',{b:true}),t(' · déposer une intention, la vibrer ensemble.',{})]),
  p([t('Le voyage passe d’un univers à l’autre — temps dansants et rythmés, temps méditatifs et introspectifs — jusqu’à une clé de voûte : un moment que l’on ne raconte pas, on le traverse. Une communion sincère, où certains lâchent enfin, où certains pleurent. Durée : 75 à 90 min, modulable jusqu’à 2h.',{})]),

  h('Ils l’ont vécu'),
  p([t('Ce qu’en disent les publics',{b:true,s:19})],{after:70}),
  ...[
   'Je suis repartie émerveillée, ressourcée.',
   'J’ai vécu un moment de légèreté, d’amour, de joie, de partage — c’était vraiment un voyage magnifique !',
   'J’ai vécu une expérience puissante. Mêlant plusieurs pratiques — le chant, la danse, la respiration — ce spectacle est avant tout et surtout VIVANT ! J’en suis reparti nourri et apaisé, avec l’impression d’avoir fait cœur et corps avec les 300 personnes présentes.',
   'Beaucoup d’émotions m’ont traversé. Je n’ai jamais vécu cela auparavant.',
   'Votre spectacle m’a rassuré et me donne espoir en l’Amour.',
   'J’ai été en apesanteur comme jamais — spectacle inventif et tellement original.',
   'Expérience incroyable, émerveillement et enchantement.',
   'Un moment suspendu, magique, inattendu, porté par deux êtres d’une beauté et d’une bonté rares.',
   'Spectacle à avoir absolument dans sa programmation tant il est original, novateur et bénéfique. Engagé, profond et surtout féerique !',
   'Et au final, tous debout, le visage rayonnant, applaudissant sans discontinuer !',
   'Spectacle très surprenant, on est transporté dans un autre monde.',
   'On en ressort bouleversé et, en même temps, apaisé. Il est ludique et joyeux.',
  ].map(q=>p([t('« '+q+' »',{i:true,c:SOFT,s:17})],{after:60})),

  h('Contact'),
  p([t('Résonances Productions — contact@resonancesproductions.org — www.resonancesproductions.org',{s:18,b:true})]),
  p([t('David Lesage — 06 10 73 31 52 — lesagedavid.fr · @david.lesage.artiste',{s:18})]),
  p([t('Iris Chasles — 06 89 05 47 58 — irischasles.com · @iris_chasles',{s:18})]),
  p([t('Julien Dub — juliendub.com · @julien_dub_',{s:18})]),
  p([t('Page de présentation : resonancesproductions.org/rituals-trio',{s:18,c:SOFT})]),
];

/* ---------- 2. BIOGRAPHIES ---------- */
const bios=[
  ...masthead('Biographies — formation trio'),
  h('David Lesage'),
  p([t('Voix · Handpan électronique · Harpe africaine Ngoni · Pads · Percussions',{c:GOLD,b:true,s:18})],{after:60}),
  p('Chanteur, musicien et compositeur, David porte la dimension musicale du projet. Son univers mêle soul française, spiritualité des musiques du monde et vibrations électroniques. Sa voix, ample et céleste, dialogue avec le handpan électronique, la harpe africaine (Ngoni), les pads et les percussions, jusqu’aux nappes électro qui ouvrent l’espace du rituel. Créateur d’expériences immersives et de soins sonores. (Vu à The Voice 11.)'),
  p([t('lesagedavid.fr · @david.lesage.artiste',{c:SOFT,s:18})],{after:160}),
  h('Iris Chasles'),
  p([t('Induction & Voix · Calebasse · Danse de tournoiement',{c:GOLD,b:true,s:18})],{after:60}),
  p('Sa fonction première : l’induction. Par la voix, Iris amène le public vers un état de conscience élargie — dans les transitions, au cœur des morceaux, dans les pratiques et les jeux. Elle apporte aussi un soutien rythmique à la calebasse et à la voix. Psychopraticienne en intelligence relationnelle, yoga-thérapeute et danseuse, elle veille à ce que chaque proposition reste une invitation, douce et sécurisante.'),
  p([t('irischasles.com · @iris_chasles',{c:SOFT,s:18})],{after:160}),
  h('Julien Dub'),
  p([t('Saxophone soprano · Flûtes · Percussions · Guitare · Claviers · Voix',{c:GOLD,b:true,s:18})],{after:60}),
  p('Son parcours l’a mené des musiques du monde — gnawa, latines, réunionnaises — au jazz, à la funk et au rocksteady, de Paris jusqu’en Inde. Il participe activement à la scène créative parisienne.'),
  p('Dans RITUALS, il apporte le souffle : saxophone soprano et flûtes, percussions, guitare, claviers et secondes voix. Une matière mélodique et aérienne qui vient dialoguer avec le handpan et la voix — et porter les envolées du rituel.'),
  p([t('juliendub.com · @julien_dub_',{c:SOFT,s:18})],{after:160}),
  h('La formation'),
  p('Sur scène, ils sont trois. Le projet reste porté par David & Iris ; Julien en élargit la palette sonore. RITUALS existe aussi en formule duo : resonancesproductions.org/rituals'),
];

/* ---------- 3. FICHE TECHNIQUE ---------- */
const fiche=[
  ...masthead('Fiche technique — formation trio'),
  p([t('Concert-Rituel en trio — musique et chant en live, danse, guidance, respiration guidée, chant participatif · 3 artistes sur scène (David Lesage, Iris Chasles & Julien Dub) · durée 75 à 90 min, modulable jusqu’à 2h.',{s:19})]),
  p([t('Plateau : sol propre et plan ; si possible, une zone libre pour la danse de tournoiement. Un espace plat de 2 m de diamètre suffit pour intégrer la danse de tournoiement.',{s:19,c:SOFT})],{after:140}),
  h('Son & régie'),
  p('1 ingénieur son avec son matériel professionnel (façade + caisson de basses, et retours). Environ 12 entrées. Les artistes apportent leurs instruments et certains micros ; les systèmes HF, la diffusion et la régie son et lumière sont fournis par l’organisation.'),
  tbl(['#','Source','Micro / DI','Fourni par'],[
    ['1','Voix 1 — David (chant)','Micro DPA serre-tête HF','Micro : artiste · Système HF : orga'],
    ['2','Voix 2 — Iris (induction / chant)','Micro main HF','Organisation'],
    ['3','Voix 3 — Julien (chant)','Micro main HF','Organisation'],
    ['4','Handpan électronique','DI (ligne)','Artiste'],
    ['5','Harpe africaine (Ngoni)','Micro AKG C411 / DI','Artiste'],
    ['6','Looper (RC-505 MK2)','DI stéréo (2)','Artiste'],
    ['7','Kick & pad — Erae 2 (Ableton Live)','DI / ligne','Artiste'],
    ['8','Calebasse','Micro Shure Beta 91A','Artiste'],
    ['9','Saxophone','Micro clip DPA 4099 et SD Systems','Micro : artiste · sinon orga'],
    ['10','Flûtes','Micro statique (SM81 / KM184) ou clip','Organisation'],
    ['11','MacBook Pro (Ableton Live)','DI stéréo (2)','Artiste'],
  ],[700,3400,3100,2600]),
  p([t('Retours : 3 wedges de scène + 1 sortie in-ear HF (système apporté par l’artiste).',{c:SOFT,s:18})],{after:140}),
  h('Matériel apporté par les artistes'),
  tbl(['Élément','Détail'],[
    ['Handpan électronique','Neotone'],
    ['Harpe africaine','Ngoni (+ micro AKG C411)'],
    ['Looper','RC-505 MK2'],
    ['Pad / contrôleur','Erae 2 (piloté par Ableton Live)'],
    ['Calebasse','Percussion acoustique + micro Shure Beta 91A'],
    ['Saxophone','Soprano (Julien)'],
    ['Flûte','Flûte traversière (Julien)'],
    ['Micro voix','DPA serre-tête — David (système HF non fourni)'],
    ['In-ear','1 système in-ear HF'],
    ['Informatique','MacBook Pro (Ableton Live)'],
  ],[3400,6400]),
  h('Lumière — plan de feu souhaité'),
  p('L’enjeu est de créer un écrin enveloppant et tamisé : on ne cherche pas à éclairer un concert, mais à tenir un espace intime où le public ose fermer les yeux, respirer et danser. Le plan ci-dessous est une base ; nous nous adaptons au parc de la salle.'),
  tbl(['Fonction','Matériel indicatif','Intention'],[
    ['Contres (priorité)','4 à 6 découpes ou PAR LED en contre-jour','Silhouetter les artistes et la danse de tournoiement'],
    ['Douches','3 douches serrées (une par artiste)','Isoler chaque musicien pendant les temps méditatifs'],
    ['Latéraux','2 × 2 PAR LED ou découpes en pied','Sculpter les volumes et le mouvement'],
    ['Face','2 à 4 découpes, très basse intensité, gradables','Rester lisible aux moments de parole — jamais plein feu'],
    ['Ambiance / couleur','4 à 8 PAR LED RGBW en salle et sur cyclo','Teintes ambrées, violines et bleu nuit'],
    ['Zone tournoiement','1 douche + 2 contres sur le cercle de 2 m','Un puits de lumière pour la figure du tournoiement'],
    ['Bougies LED','30 à 60 bougies LED au sol, en cercle','Délimiter l’espace rituel, sans risque incendie'],
    ['Guirlandes','Guirlandes guinguette ou micro-LED chaudes','Ambiance féerique et intimiste'],
    ['Machine à brume','1 hazer discret (si autorisé)','Révéler les faisceaux et donner de la matière aux contres'],
  ],[2600,3900,3300]),
  p([t('Régie lumière assurée par l’organisation. Conduite simple en 5 à 6 états, calée avant la représentation ; possibilité de fonctionner en ambiances fixes. À éviter : stroboscopes, changements brusques et lumière blanche froide plein feu.',{c:SOFT,s:18})],{after:140}),
  h('Loges, hébergement & repas'),
  p('Loges fermées et chauffées. Hébergement des 3 artistes à la charge de l’organisateur. Repas midi et soir : 3 repas dont 1 végétarien, pendant toute la durée de la présence des artistes sur place.'),
  p([t('Fiche technique détaillée, patch et plans de scène disponibles sur demande.',{c:SOFT,s:18,i:true})]),
];

function doc(children){return new Document({styles:{default:{document:{run:{font:S,size:20,color:INK}}}},sections:[{properties:{page:{margin:{top:1100,bottom:1000,left:1100,right:1100}}},children}]});}

Promise.all([
  Packer.toBuffer(doc(communique)).then(b=>fs.writeFileSync(OUT+'01_Communique_RITUALS_TRIO.docx',b)),
  Packer.toBuffer(doc(bios)).then(b=>fs.writeFileSync(OUT+'02_Biographies_RITUALS_TRIO.docx',b)),
  Packer.toBuffer(doc(fiche)).then(b=>fs.writeFileSync(OUT+'03_Fiche_technique_RITUALS_TRIO.docx',b)),
]).then(()=>console.log('WROTE presskit docs'));
