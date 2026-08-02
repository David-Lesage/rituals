# -*- coding: utf-8 -*-
"""Injecte un menu hamburger mobile dans une page HTML deja construite.

Fonctionne sur les 5 pages du site : chacune possede un <nav class="nav">
contenant un <div class="links"> ; on ajoute un bouton hamburger, on bascule
les liens dans un panneau plein ecran sur mobile, et on gere l'ouverture/fermeture.
"""

CSS = """
/* ===== MENU MOBILE (hamburger) ===== */
.burger{display:none;background:none;border:1px solid rgba(216,178,90,.34);border-radius:10px;width:44px;height:44px;padding:0;cursor:pointer;position:relative;z-index:1002;flex:0 0 auto}
.burger span{display:block;width:20px;height:2px;background:var(--gold2);margin:4px auto;border-radius:2px;transition:transform .28s,opacity .2s}
.burger[aria-expanded="true"] span:nth-child(1){transform:translateY(6px) rotate(45deg)}
.burger[aria-expanded="true"] span:nth-child(2){opacity:0}
.burger[aria-expanded="true"] span:nth-child(3){transform:translateY(-6px) rotate(-45deg)}
@media(max-width:860px){
  .burger{display:block}
  .nav{flex-wrap:wrap}
  .nav .links{position:fixed;top:0;left:0;right:0;bottom:0;z-index:1001;
    background:rgba(10,11,28,.98);backdrop-filter:blur(14px);
    flex-direction:column;justify-content:center;align-items:center;gap:6px !important;
    padding:80px 26px 40px;
    opacity:0;visibility:hidden;transform:translateY(-12px);
    transition:opacity .3s,transform .3s,visibility .3s;
    overflow-y:auto}
  .nav .links.open{opacity:1;visibility:visible;transform:none}
  /* on annule les regles qui masquaient les liens en mobile */
  .nav .links a,.nav .links a.hide-s,.nav .links a:not(.adh){display:block !important;
    font-size:21px !important;letter-spacing:.06em;padding:14px 18px;text-align:center;
    font-family:'Cormorant Garamond',Georgia,serif;color:#eae7f3 !important;width:100%;max-width:340px}
  .nav .links a:active{color:var(--gold2) !important}
  .nav .links a.adh{margin-top:18px;background:var(--gold);color:#1a1608 !important;
    border-radius:30px;font-family:'Jost',sans-serif;font-size:16px !important;padding:14px 30px;width:auto}
  /* .nav porte un backdrop-filter : il devient le bloc conteneur des descendants
     position:fixed ET un contexte d'empilement -> le panneau restait enferme dans la
     barre et passait sous le contenu. On neutralise le filtre et on remonte le nav
     uniquement quand le menu est ouvert. */
  body.nav-open .nav{backdrop-filter:none !important;-webkit-backdrop-filter:none !important;z-index:1001 !important}
  body.nav-open{overflow:hidden}
}
@media print{.burger{display:none}}
"""

JS = """
<script>
(function(){
  var nav=document.querySelector('.nav'); if(!nav) return;
  var links=nav.querySelector('.links'); if(!links) return;
  var b=document.createElement('button');
  b.className='burger'; b.type='button';
  b.setAttribute('aria-label','Ouvrir le menu');
  b.setAttribute('aria-expanded','false');
  b.innerHTML='<span></span><span></span><span></span>';
  nav.appendChild(b);
  function set(open){
    b.setAttribute('aria-expanded',open?'true':'false');
    b.setAttribute('aria-label',open?'Fermer le menu':'Ouvrir le menu');
    links.classList.toggle('open',open);
    document.body.classList.toggle('nav-open',open);
  }
  b.addEventListener('click',function(){ set(b.getAttribute('aria-expanded')!=='true'); });
  links.addEventListener('click',function(e){ if(e.target.tagName==='A') set(false); });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape') set(false); });
  window.addEventListener('resize',function(){ if(window.innerWidth>860) set(false); });
})();
</script>
"""


def inject(html: str) -> str:
    """Ajoute le CSS et le JS du menu mobile a une page HTML."""
    if 'class="burger"' in html or '.burger{' in html:
        return html  # deja injecte
    if '</style>' in html:
        html = html.replace('</style>', CSS + '</style>', 1)
    if '</body>' in html:
        html = html.replace('</body>', JS + '</body>', 1)
    else:
        html += JS
    return html


if __name__ == '__main__':
    import sys
    for path in sys.argv[1:]:
        with open(path, encoding='utf-8') as f:
            src = f.read()
        out = inject(src)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(out)
        print(('OK   ' if out != src else 'SKIP ') + path)
