# -*- coding: utf-8 -*-
"""La visionneuse photo du site, en UN seul exemplaire.

POURQUOI CE FICHIER EXISTE
--------------------------
Le 17/08/2026, `/e-motion` a recu une visionneuse : on clique une photo, elle
s'ouvre en plein ecran dans sa meilleure definition, on passe de l'une a
l'autre au balayage / aux fleches / au clavier, on zoome au clic. David a vu le
resultat et demande la meme chose partout :

    « oui applique la visionneuse sur toutes les pages comme celles de rituals
      duo et trio et le nid aussi, bref toutes les pages »

Sept pages du site portent des photos. Recopier sept fois la meme feuille de
style et le meme script, c'est se garantir une divergence : une correction du
zoom en reparerait six sur sept, et la septieme resterait cassee sans que
personne le voie. D'ou ce module : UNE definition, sept generateurs qui
l'appellent. Meme parti-pris que `sources/theme_chaleur.py`.

⚠️ CE N'EST PAS UN GENERATEUR. Il n'ecrit aucune page, il ne s'execute pas
   seul, et il n'a donc pas de ligne dans `sources/build.py` (dont le controle
   « generateur non inscrit » ne regarde que les fichiers `generate_*.py`).

COMMENT ON S'EN SERT
--------------------
Dans le generateur d'une page, DEUX morceaux a poser, et pas un seul :

    import visionneuse
    ...  + visionneuse.css('.gal-item .c') +   # avant </style>
    ...  + visionneuse.js('.gal-item img') +   # avant </body>

Les deux arguments sont des SELECTEURS CSS, et ils ne disent pas la meme chose :

  * `css(legende=...)`  : la classe de la LEGENDE posee par-dessus le bas des
    photos. Elle vaut `pointer-events:none`. Passer une chaine vide quand la
    page n'a aucune legende en surimpression. Voir l'avertissement plus bas :
    ce n'est PAS un detail cosmetique.
  * `js(selecteur=...)` : les photos a rendre cliquables, dans l'ordre du
    DOCUMENT (`querySelectorAll` rend toujours les elements dans l'ordre de la
    page, pas dans celui du selecteur).

CE QUE LA VISIONNEUSE DEMANDE A LA PAGE
---------------------------------------
Rien d'autre que les variables CSS deja posees partout par `theme_chaleur.py`
et par la feuille de style de chaque page : `--line`, `--muted`, `--gold2`.
Les deux familles typographiques ('Cormorant Garamond' pour les fleches et la
croix, 'Jost' pour le bouton de zoom) ont chacune un repli generique.

CE QU'ELLE NE FAIT PAS
----------------------
Elle n'ajoute AUCUN texte a la page publiee : le dialogue n'existe pas dans le
HTML livre, il est construit par le script. Sans JavaScript, la page est
exactement celle d'avant — les photos s'affichent, rien n'est casse, rien n'est
cliquable. C'est la regle du site.

Elle n'agrandit jamais une photo au-dela de la definition du fichier :
`plusGrande()` LIT les `srcset` deja ecrits dans la page et retient la plus
grande largeur reellement publiee. Un nom de fichier inexistant est donc
impossible par construction. Une page qui ne publie que des variantes 480 px
donnera donc une visionneuse a 480 px : c'est voulu, au-dela ce serait flou.
"""

# --------------------------------------------------------------------------
# LA FEUILLE DE STYLE
# --------------------------------------------------------------------------
# ⚠️ LA LIGNE `pointer-events:none` DE LA LEGENDE N'EST PAS COSMETIQUE. Sur
#    plusieurs pages la legende d'une photo est en `position:absolute`
#    PAR-DESSUS le bas de l'image : sans cette ligne, tout le bas de chaque
#    photo n'est pas cliquable. Mesure faite avant de l'ecrire, sur /e-motion.
#    Chaque page a SA classe de legende (`.gal-item .c`, `figcaption`, `.cap`,
#    `.dlc-cred` ...) — d'ou le parametre.
#
# ⚠️ `body.ph-lock` est en `position:fixed`, pas en `overflow:hidden`. Sur
#    iOS, `overflow:hidden` sur le body ne bloque PAS le defilement ; et la
#    page perd sa position. Le script memorise `pageYOffset`, le repose en
#    `top:-Npx`, et le rend a la fermeture — en neutralisant le temps du retour
#    le `scroll-behavior:smooth` de `html`, qui sinon animerait le retour et
#    laisserait la page ailleurs.
#
# ⚠️ z-index 1100 : au-dessus du panneau du menu mobile (1001) et de son
#    bouton hamburger (1002), sinon la visionneuse passerait dessous.
#
# ⚠️ Le defilement des photos, c'est le defilement NATIF du navigateur, avec
#    accrochage : sur telephone le balayage, son inertie et son rebond sont
#    ceux du systeme, pas une mecanique reimplementee a la main.
#
# ⚠️ Cible tactile des quatre boutons : 46 px et non 44. Mesure du 17/08/2026 :
#    a 44 px pile, l'arrondi sous-pixel du navigateur rend 43,99 px — sous le
#    seuil. Deux pixels de marge mettent la regle hors de doute a toute densite.

_CSS_AVANT_LEGENDE = """
/* visionneuse photo */
.ph{position:fixed;inset:0;z-index:1100;display:none;flex-direction:column;
  background:rgba(8,9,26,.965);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}
.ph.open{display:flex}
.ph-head{flex:0 0 auto;display:flex;align-items:center;justify-content:space-between;gap:12px;padding:8px 12px}
.ph-num{font-size:14px;letter-spacing:.2em;color:var(--muted);padding-left:8px}
.ph-tools{display:flex;gap:10px;align-items:center}
.ph-body{position:relative;flex:1 1 auto;min-height:0}
.ph-track{position:absolute;inset:0;z-index:1;display:flex;overflow-x:auto;overflow-y:hidden;
  scroll-snap-type:x mandatory;overscroll-behavior:contain;touch-action:pan-x pinch-zoom;
  scrollbar-width:none;-ms-overflow-style:none}
.ph-track::-webkit-scrollbar{width:0;height:0}
.ph-slide{flex:0 0 100%;width:100%;height:100%;scroll-snap-align:center;scroll-snap-stop:always;
  display:flex;align-items:center;justify-content:center;padding:4px 12px}
.ph-slide img{max-width:100%;max-height:100%;width:auto;height:auto;display:block;
  border-radius:18px;box-shadow:0 24px 70px rgba(0,0,0,.6);-webkit-user-drag:none;
  transform-origin:50% 50%;transition:transform .3s ease;cursor:zoom-in}
.ph-slide img.ph-zoomed{cursor:grab;border-radius:0;box-shadow:none}
.ph-cap{flex:0 0 auto;min-height:40px;padding:8px 20px 16px;text-align:center;
  color:var(--muted);font-size:14.5px;font-style:italic}
.ph-btn{background:rgba(20,22,52,.72);border:1px solid var(--line);color:var(--gold2);
  min-width:46px;min-height:46px;border-radius:999px;cursor:pointer;padding:0;
  display:inline-flex;align-items:center;justify-content:center;
  font-family:'Cormorant Garamond',Georgia,serif;font-size:30px;line-height:1}
.ph-btn:hover{color:#fff;border-color:var(--gold2)}
.ph-btn[aria-disabled="true"]{opacity:.3;cursor:default}
.ph-arw{position:absolute;top:50%;transform:translateY(-50%);z-index:2;width:52px;height:52px;font-size:34px}
.ph-arw.p{left:12px}
.ph-arw.n{right:12px}
.ph-btn.z{font-family:'Jost',sans-serif;font-size:23px}
"""

_CSS_APRES_LEGENDE = """.ph-op{cursor:zoom-in}
body.ph-lock{position:fixed;left:0;right:0;width:100%;overflow:hidden}
@media(max-width:600px){.ph-arw{width:46px;height:46px;font-size:28px}.ph-arw.p{left:4px}.ph-arw.n{right:4px}}
@media(prefers-reduced-motion:reduce){.ph-slide img{transition:none}}
"""


def css(legende=''):
    """La feuille de style de la visionneuse, a poser avant `</style>`.

    `legende` : le selecteur de la legende posee par-dessus le bas des photos,
    qu'il faut rendre transparente au clic. Chaine vide si la page n'en a pas.
    """
    regle = (legende + '{pointer-events:none}\n') if legende else ''
    return _CSS_AVANT_LEGENDE + regle + _CSS_APRES_LEGENDE


# --------------------------------------------------------------------------
# LE SCRIPT
# --------------------------------------------------------------------------
# * TOUT est construit par ce script. Le HTML livre ne contient ni le dialogue
#   ni un seul caractere de texte en plus : sans JavaScript, la page est
#   exactement celle d'avant et rien n'est casse.
# * LA PLUS GRANDE VARIANTE EST LUE DANS LA PAGE, jamais devinee : `plusGrande()`
#   parcourt les `srcset` deja ecrits (ceux des `<source>` WebP et celui de
#   l'`<img>`) et retient l'URL de plus grande largeur. Un nom de fichier
#   inexistant est donc impossible par construction. Le choix WebP/JPEG reprend
#   le test `canvas.toDataURL` de `generate_site.py` — meme technique partout.
# * LES LEGENDES SONT LES `alt` DEJA ECRITS. Rien n'est reformule ici.
# * BUTEE, PAS BOUCLE, aux deux extremites. Raison mesuree : le defilement est
#   celui du navigateur (`scroll-snap`), et un balayage ne peut PAS reboucler de
#   la derniere a la premiere. Faire reboucler les fleches aurait donne deux
#   comportements differents selon qu'on balaye ou qu'on clique. Les fleches
#   portent donc `aria-disabled` aux extremites — `aria-disabled` et non
#   `disabled`, pour qu'elles restent atteignables au clavier et ne trouent pas
#   le piege a focus.
# * LE DEFILEMENT DOUX EST RATTRAPE S'IL N'A PAS EU LIEU. Mesure du 17/08/2026 :
#   `scrollTo({behavior:'smooth'})` ne fait RIEN quand l'onglet n'est pas visible
#   (`document.visibilityState === 'hidden'`) — le compteur avancait, l'image
#   non. Et pendant une animation en cours, les evenements `scroll` ramenaient
#   l'index en arriere. D'ou `cible` : tant qu'un deplacement est en vol, les
#   evenements `scroll` ne commandent plus l'index, et 450 ms plus tard on
#   verifie que le rail est bien arrive — sinon on l'y pose sans animation.
#   ⚠️ CE VERROU SE RELACHE DE TROIS FACONS, et pas seulement au minuteur :
#   des que le rail atteint la cible, et des que le VISITEUR reprend la main
#   (`pointerdown`, `touchstart`, `wheel`). Sans cela, un balayage arrivant
#   juste apres un clic sur une fleche n'aurait pas fait bouger le compteur —
#   defaut reproduit le 17/08/2026 dans un onglet en arriere-plan, ou Chrome
#   brime les minuteurs a un par minute.
# * ZOOM SOBRE : un facteur fixe (2,2x), centre sur le point clique, deplacable
#   au glisser, borne pour que l'image ne parte jamais hors du cadre. Pas de
#   zoom continu : mieux vaut simple et partout que savant et fragile.
#   ⚠️ LA BORNE SE CALCULE SUR LE CADRE VISIBLE, PAS SUR L'IMAGE. Premiere
#   version mesuree le 17/08/2026 : bornee sur la largeur de l'image, elle
#   laissait glisser 12 px trop loin (une bande de fond apparaissait sur un
#   cote) et, pire, autorisait un deplacement VERTICAL sur une image large dont
#   la hauteur zoomee tient encore dans le cadre — l'image partait se coincer
#   en haut sans que rien de neuf n'apparaisse. `borne()` renvoie 0 des que
#   l'image zoomee ne deborde pas dans cette direction.
# * PENDANT LE ZOOM le defilement horizontal est coupe (`overflow-x:hidden`) et
#   l'image passe en `touch-action:none` : sinon le glisser et le balayage se
#   disputent le meme geste.
# * LE CLAVIER N'EST ECOUTE QUE VISIONNEUSE OUVERTE : l'ecouteur `keydown` est
#   POSE a l'ouverture et RETIRE a la fermeture. Il ne vole donc jamais les
#   fleches d'un carrousel, ni celles de la page, quand elle est fermee.

_JS_AVANT_SELECTEUR = r"""<script>
(function(){
  var SEL='"""

_JS_APRES_SELECTEUR = r"""';
  var photos=[].slice.call(document.querySelectorAll(SEL));
  if(!photos.length||!document.body.classList) return;
  var N=photos.length, ECH=2.2;
  var WEBP=(function(){try{return document.createElement('canvas').toDataURL('image/webp').indexOf('data:image/webp')===0}catch(e){return false}})();

  function plusGrande(img,ext){
    var lots=[],p=img.parentNode,best='',bw=-1,i,k,t,w;
    if(p&&p.tagName==='PICTURE'){var s=p.getElementsByTagName('source');
      for(i=0;i<s.length;i++)lots.push(s[i].getAttribute('srcset')||'');}
    lots.push(img.getAttribute('srcset')||'');
    for(i=0;i<lots.length;i++){var parts=lots[i].split(',');
      for(k=0;k<parts.length;k++){t=parts[k].replace(/^\s+|\s+$/g,'').split(/\s+/);
        if(!t[0]||t[0].slice(-ext.length).toLowerCase()!==ext) continue;
        w=parseInt(t[1]||'0',10)||0; if(w>=bw){bw=w;best=t[0];}}}
    return best;
  }
  function reduit(){return !!(window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches);}

  var dlg,track,cap,num,bP,bN,bZ,bX,slides=[],ouvert=false,idx=0,origine=null,posY=0;
  var zImg=null,zOn=false,ztx=0,zty=0,glisse=false,bouge=false,sx=0,sy=0,btx=0,bty=0;
  var minuteur=0,cible=-1,reparation=0;

  function bouton(cls,label,txt){
    var b=document.createElement('button');
    b.type='button'; b.className=cls; b.setAttribute('aria-label',label); b.textContent=txt;
    return b;
  }
  function div(cls){var e=document.createElement('div'); e.className=cls; return e;}
  function relacher(){cible=-1;}

  function construire(){
    dlg=div('ph');
    dlg.setAttribute('role','dialog');
    dlg.setAttribute('aria-modal','true');
    dlg.setAttribute('aria-label','Visionneuse de photos');
    var head=div('ph-head');
    num=document.createElement('span'); num.className='ph-num';
    var tools=document.createElement('span'); tools.className='ph-tools';
    bZ=bouton('ph-btn z','Agrandir la photo','+'); bZ.setAttribute('aria-pressed','false');
    bX=bouton('ph-btn x','Fermer la visionneuse','×');
    tools.appendChild(bZ); tools.appendChild(bX);
    head.appendChild(num); head.appendChild(tools);
    var body=div('ph-body');
    track=div('ph-track');
    bP=bouton('ph-btn ph-arw p','Photo précédente','‹');
    bN=bouton('ph-btn ph-arw n','Photo suivante','›');
    body.appendChild(track); body.appendChild(bP); body.appendChild(bN);
    cap=document.createElement('p'); cap.className='ph-cap';
    dlg.appendChild(head); dlg.appendChild(body); dlg.appendChild(cap);

    photos.forEach(function(src){
      var s=div('ph-slide'), im=document.createElement('img');
      var jpg=plusGrande(src,'.jpg')||src.currentSrc||src.getAttribute('src')||'';
      im.setAttribute('data-jpg',jpg);
      im.setAttribute('data-webp',plusGrande(src,'.webp')||jpg);
      im.alt=src.getAttribute('alt')||'';
      var w=src.getAttribute('width'), h=src.getAttribute('height');
      if(w&&h){im.setAttribute('width',w); im.setAttribute('height',h);}
      im.decoding='async';
      s.appendChild(im); track.appendChild(s); slides.push(im);
    });
    document.body.appendChild(dlg);

    bP.addEventListener('click',function(){allerA(idx-1,true);});
    bN.addEventListener('click',function(){allerA(idx+1,true);});
    bZ.addEventListener('click',function(){if(zOn)dezoom();else zoomer(.5,.5);});
    bX.addEventListener('click',fermer);
    track.addEventListener('scroll',function(){
      if(minuteur)return;
      minuteur=setTimeout(function(){minuteur=0;
        var i=Math.round(track.scrollLeft/Math.max(1,track.clientWidth));
        if(cible>=0){if(i===cible)cible=-1; return;}
        setIdx(i);},60);
    });
    track.addEventListener('wheel',relacher,{passive:true});
    track.addEventListener('touchstart',relacher,{passive:true});
    track.addEventListener('click',function(e){
      var im=e.target;
      if(im.tagName!=='IMG'){fermer();return;}
      if(bouge)return;
      if(zOn){dezoom();return;}
      var r=im.getBoundingClientRect();
      zoomer((e.clientX-r.left)/r.width,(e.clientY-r.top)/r.height);
    });
    track.addEventListener('pointerdown',function(e){
      bouge=false; relacher();
      if(!zOn||e.target!==zImg)return;
      glisse=true; sx=e.clientX; sy=e.clientY; btx=ztx; bty=zty;
      zImg.style.transition='none';
      if(zImg.setPointerCapture){try{zImg.setPointerCapture(e.pointerId);}catch(err){}}
      e.preventDefault();
    });
    track.addEventListener('pointermove',function(e){
      if(!glisse)return;
      var dx=e.clientX-sx, dy=e.clientY-sy;
      if(Math.abs(dx)>5||Math.abs(dy)>5)bouge=true;
      ztx=btx+dx/ECH; zty=bty+dy/ECH; appliquer();
    });
    function finGlisse(){if(!glisse)return; glisse=false; if(zImg)zImg.style.transition='';}
    track.addEventListener('pointerup',finGlisse);
    track.addEventListener('pointercancel',finGlisse);
    window.addEventListener('resize',function(){
      if(!ouvert)return; dezoom(); track.scrollLeft=idx*track.clientWidth;
    });
  }

  function charger(i){
    for(var k=i-1;k<=i+1;k++){
      if(k<0||k>=N)continue;
      var im=slides[k];
      if(im.getAttribute('src'))continue;
      im.src=WEBP?im.getAttribute('data-webp'):im.getAttribute('data-jpg');
    }
  }
  function setIdx(i){
    i=Math.max(0,Math.min(N-1,i));
    if(i!==idx)dezoom();
    idx=i;
    num.textContent=(i+1)+' / '+N;
    cap.textContent=slides[i].alt;
    bP.setAttribute('aria-disabled',i===0?'true':'false');
    bN.setAttribute('aria-disabled',i===N-1?'true':'false');
    charger(i);
  }
  function allerA(i,doux){
    i=Math.max(0,Math.min(N-1,i));
    if(i===idx&&cible<0)return;
    dezoom();
    cible=i;
    var g=i*track.clientWidth;
    if(track.scrollTo)track.scrollTo({left:g,behavior:(doux&&!reduit())?'smooth':'auto'});
    else track.scrollLeft=g;
    setIdx(i);
    clearTimeout(reparation);
    reparation=setTimeout(function(){
      if(cible>=0&&Math.round(track.scrollLeft/Math.max(1,track.clientWidth))!==cible)
        track.scrollLeft=cible*track.clientWidth;
      cible=-1;
    },450);
  }
  function borne(taille,cadre){
    var d=(taille*ECH-cadre)/2;
    return d>0?d/ECH:0;
  }
  function appliquer(){
    if(!zImg||!zOn)return;
    var mx=borne(zImg.clientWidth,track.clientWidth), my=borne(zImg.clientHeight,track.clientHeight);
    ztx=Math.max(-mx,Math.min(mx,ztx)); zty=Math.max(-my,Math.min(my,zty));
    zImg.style.transform='scale('+ECH+') translate('+ztx+'px,'+zty+'px)';
  }
  function zoomer(fx,fy){
    zImg=slides[idx]; zOn=true;
    ztx=-(fx-.5)*zImg.clientWidth; zty=-(fy-.5)*zImg.clientHeight;
    zImg.classList.add('ph-zoomed'); zImg.style.touchAction='none';
    track.style.overflowX='hidden';
    bZ.textContent='−'; bZ.setAttribute('aria-pressed','true');
    bZ.setAttribute('aria-label','Revenir à la taille normale');
    appliquer();
  }
  function dezoom(){
    if(!zOn)return;
    zOn=false; glisse=false;
    if(zImg){zImg.style.transform=''; zImg.style.touchAction=''; zImg.style.transition='';
      zImg.classList.remove('ph-zoomed');}
    zImg=null; ztx=0; zty=0;
    track.style.overflowX='';
    bZ.textContent='+'; bZ.setAttribute('aria-pressed','false');
    bZ.setAttribute('aria-label','Agrandir la photo');
  }
  function boutons(){
    return [bP,bN,bZ,bX].filter(function(b){return b.offsetWidth||b.offsetHeight;});
  }
  function clavier(e){
    if(!ouvert)return;
    if(e.key==='Escape'||e.key==='Esc'){e.preventDefault(); e.stopPropagation(); fermer(); return;}
    if(e.key==='ArrowLeft'){e.preventDefault(); allerA(idx-1,true); return;}
    if(e.key==='ArrowRight'){e.preventDefault(); allerA(idx+1,true); return;}
    if(e.key==='Home'){e.preventDefault(); allerA(0,true); return;}
    if(e.key==='End'){e.preventDefault(); allerA(N-1,true); return;}
    if(e.key==='Tab'){
      var f=boutons(); if(!f.length)return;
      e.preventDefault();
      var i=f.indexOf(document.activeElement);
      var j=e.shiftKey?(i<=0?f.length-1:i-1):(i<0||i===f.length-1?0:i+1);
      f[j].focus();
    }
  }
  function verrouiller(){
    posY=window.pageYOffset||document.documentElement.scrollTop||0;
    document.body.style.top=(-posY)+'px';
    document.body.classList.add('ph-lock');
  }
  function deverrouiller(){
    document.body.classList.remove('ph-lock');
    document.body.style.top='';
    var d=document.documentElement, av=d.style.scrollBehavior;
    d.style.scrollBehavior='auto';
    window.scrollTo(0,posY);
    d.style.scrollBehavior=av;
  }
  function ouvrir(i,dep){
    if(ouvert)return;
    if(!dlg)construire();
    origine=dep; ouvert=true;
    verrouiller();
    dlg.classList.add('open');
    clearTimeout(reparation); cible=-1;
    track.scrollLeft=i*track.clientWidth;
    setIdx(i);
    document.addEventListener('keydown',clavier,true);
    bX.focus();
  }
  function fermer(){
    if(!ouvert)return;
    ouvert=false;
    dezoom();
    dlg.classList.remove('open');
    document.removeEventListener('keydown',clavier,true);
    deverrouiller();
    if(origine&&origine.focus){try{origine.focus({preventScroll:true});}catch(err){origine.focus();}}
    origine=null;
  }

  photos.forEach(function(im,i){
    im.classList.add('ph-op');
    im.setAttribute('role','button');
    im.setAttribute('tabindex','0');
    im.setAttribute('aria-haspopup','dialog');
    im.addEventListener('click',function(e){e.preventDefault(); ouvrir(i,im);});
    im.addEventListener('keydown',function(e){
      if(e.key==='Enter'||e.key===' '||e.key==='Spacebar'){e.preventDefault(); ouvrir(i,im);}
    });
  });
})();
</script>
"""


def js(selecteur):
    """Le script de la visionneuse, a poser avant `</body>`.

    `selecteur` : les photos a rendre cliquables. Elles sont numerotees dans
    l'ordre du DOCUMENT, quel que soit l'ordre du selecteur.
    """
    return _JS_AVANT_SELECTEUR + selecteur + _JS_APRES_SELECTEUR
