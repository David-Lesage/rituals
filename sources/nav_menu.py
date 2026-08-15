# -*- coding: utf-8 -*-
"""Menu de navigation PARTAGE du site Resonances Productions.

Remplace le <div class="links"> d'une page deja construite par le menu unique
valide par David (architecture « deux publics ») :

    Accueil · Sur scene ▾ · Le Nid ▾ · L’association ▾ · Contact · [Adherer]

------------------------------------------------------------------------------
UTILISATION
------------------------------------------------------------------------------
    import nav_menu
    html = mobile_nav.inject(html)          # 1. le hamburger d'abord
    html = nav_menu.inject(html, 'rituals') # 2. puis le menu

    inject(html: str, current: str | None = None, *,
           contact_href: str | None = None) -> str

* `html`     : page complete. Doit contenir un `<nav class="nav">` avec un
               `<div class="links"> ... </div>` (c'est ce bloc qui est remplace),
               un `</style>` (le CSS y est insere juste avant, donc en dernier :
               il gagne sur `.nav .links a{font-size:14.5px}`) et un `</body>`.
* `current`  : page affichee, une des CLES de PAGE_KEYS ci-dessous :
               'home', 'rituals', 'rituals-trio', 'e-motion',
               'david-lesage-en-concert', 'le-nid', 'concerts-david-lesage',
               'rythme-calebasse', 'le-soin-soa', 'association', 'guso-facile'.
               None => aucune entree marquee.
               La cle pose `aria-current="page"` sur la bonne entree et marque
               visuellement l'entree parente (`.nm-active`).
* `contact_href` : surcharge facultative. Par defaut la fonction AUTO-DETECTE :
               si la page contient `id="contact"` le lien Contact devient
               `#contact` (ancre locale), sinon `/#contact`.
               (Il y avait un `association_href` jumeau jusqu'au 15/08/2026 ;
               il a disparu avec le passage de l'entree « L’association » a la
               vraie page `/association` — voir la note au-dessus de `ASSO`.)

Fonction pratique pour un fichier deja ecrit sur le disque :

    nav_menu.apply_to_file('/chemin/vers/index.html', 'rituals')  # -> True/False

En ligne de commande (la cle est deduite du chemin, ou donnee avec `=`) :

    python3 sources/nav_menu.py index.html rituals/index.html
    python3 sources/nav_menu.py le-nid/index.html=le-nid

------------------------------------------------------------------------------
IDEMPOTENCE (garde-fou explicite)
------------------------------------------------------------------------------
Le bloc genere porte `data-nav="NAV_VERSION"`. Si ce marqueur est deja present,
`inject()` renvoie le HTML INCHANGE : relancer un generateur ne duplique donc
ni les entrees, ni le CSS, ni le JS. Pour forcer une regeneration apres une
modification de ce fichier, incrementer NAV_VERSION : `inject()` remplace alors
proprement l'ancien bloc (le scanner de `</div>` compte les `<div>` imbriques)
et retire l'ancien CSS/JS delimites par les marqueurs CSS_MARK / JS_MARK.

------------------------------------------------------------------------------
PIEGES CONNUS DU PROJET (ne pas les reintroduire)
------------------------------------------------------------------------------
* `.nav` porte `backdrop-filter` : il est bloc conteneur des descendants
  `position:fixed` ET contexte d'empilement. Les panneaux de sous-menu sont
  donc `position:absolute` dans un `.nm-item{position:relative}` (jamais fixed)
  et le correctif `body.nav-open .nav{backdrop-filter:none!important}` de
  mobile_nav.py reste indispensable : NE PAS LE SUPPRIMER.
* En mobile, `mobile_nav.py` centre le panneau (`justify-content:center`) : avec
  les deux accordeons ouverts le debut du contenu devenait inatteignable. On
  repasse en `flex-start` + marges `auto` sur les enfants extremes (les marges
  auto se resolvent a 0 quand il y a debordement -> le panneau defile bien).
* Le panneau de sous-menu est OPAQUE (`--card`) et `z-index:1200`.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verif_commentaires  # garde-fou commentaires HTML  # noqa: E402

#: ⚠️ A INCREMENTER a chaque modification du menu, sinon `inject()` considere
#: que le menu deja pose est le bon et ne le remplace PAS (garde d'idempotence).
#: Deux fichiers suivent ce numero et doivent etre mis a jour en meme temps :
#:   * `verif_site.py` (marqueurs uniques + controle du menu) — il le lit
#:     directement dans ce module depuis le 14/08/2026, donc rien a y faire ;
#:   * `verif_commentaires.py` — sa liste blanche accepte deja n'importe quel
#:     numero (`<!-- nav_menu\.py \([^)>]*\) -->`), rien a y faire non plus.
#: resonances-3 (14/08/2026) : « L’association » devient un menu deroulant pour
#: accueillir « Guso Facile ».
#: resonances-4 (15/08/2026) : « L’association » ne renvoie plus a l'ancre
#: `/#association` de l'accueil mais a la VRAIE page `/association`. David avait
#: remarque que « Accueil » et « L’association » menaient au meme endroit.
#: ⚠️ Cinq generateurs lisent `nav_menu.NAV_VERSION` dans leurs garde-fous
#:    depuis le 14/08/2026 (ils codaient `resonances-2` en dur avant, et une
#:    montee de version les faisait tous refuser d'ecrire). Verifie AVANT cette
#:    montee : plus aucune occurrence de « resonances-2 » ni « resonances-3 » en
#:    dur dans sources/. `verif_site.py` et `verif_commentaires.py` suivent aussi
#:    tout seuls (le motif de la liste blanche est ecrit SANS le numero).
NAV_VERSION = 'resonances-4'
CSS_MARK = '/* == nav_menu.py (%s) == */' % NAV_VERSION
CSS_END = '/* == fin nav_menu.py == */'
#: ⚠️ CES DEUX MARQUEURS SONT FONCTIONNELS — ne jamais les retirer du HTML.
#: `JS_MARK` est la garde d'idempotence testee par `inject()` : sans lui le menu
#: se reinjecte a chaque passe (l'incident des entrees de menu en double). Il
#: porte aussi NAV_VERSION, relue pour nettoyer un ancien menu. `JS_END` est la
#: borne de fin utilisee par `_strip()` pour ce nettoyage. Ce sont les deux
#: seuls commentaires HTML autorises dans une page livree — liste blanche dans
#: `sources/verif_commentaires.py`.
JS_MARK = '<!-- nav_menu.py (%s) -->' % NAV_VERSION
JS_END = '<!-- fin nav_menu.py -->'

ADHESION = ('https://www.helloasso.com/beta/associations/resonances-productions'
            '/adhesions/adhesion-resonances-productions')

# (libelle, href, cle de page)
SCENE = [
    ('RITUALS — duo', '/rituals', 'rituals'),
    ('RITUALS — trio', '/rituals-trio', 'rituals-trio'),
    ('E-Motion', '/e-motion', 'e-motion'),
    ('David Lesage en concert', '/david-lesage-en-concert', 'david-lesage-en-concert'),
]
NID = [
    ('Le Nid — Paris 20ᵉ', '/le-nid', 'le-nid'),
    ('Agenda', '/le-nid#agenda', 'le-nid'),
    ('Présentation d’instruments', '/le-nid#instruments', 'le-nid'),
    ('Concerts au Nid', '/concerts-david-lesage', 'concerts-david-lesage'),
    ('Atelier de yoga', '/le-nid#yoga', 'le-nid'),
    ('Rythme & calebasse', '/rythme-calebasse', 'rythme-calebasse'),
    ('Le Soin Soa', '/le-soin-soa', 'le-soin-soa'),
    ('Psychothérapie', '/le-nid#psychotherapie', 'le-nid'),
    ('Cours individuels', '/le-nid#cours-individuels', 'le-nid'),
]


# --------------------------------------------------------------------------- #
# OU RANGER « GUSO FACILE » — decision du 14/08/2026, et sa raison
# --------------------------------------------------------------------------- #
# Guso Facile n'est ni un spectacle (« Sur scene ») ni une activite du lieu
# (« Le Nid ») : c'est un outil pour les artistes intermittents. Trois places
# etaient possibles ; voici pourquoi c'est un sous-menu de « L’association ».
#
#  * PAS dans « Le Nid » : ce sous-menu decrit ce qui se vit AU Nid, a Paris.
#    Un outil web n'y a pas sa place, et le public n'est pas le meme.
#  * PAS en entree de premier niveau : la barre en compte deja six, et la
#    contrainte est MESUREE — entre 861 et 1080 px les liens venaient toucher
#    le nom de l'association (d'ou les deux paliers de resserrement CSS plus
#    bas). Une septieme entree rouvrirait ce probleme ; un sous-menu ne coute
#    que la largeur du chevron.
#  * DONC sous « L’association », qui devient deroulant sur le modele exact de
#    « Le Nid » : la premiere entree du panneau reste la page/section elle-meme
#    (comme « Le Nid — Paris 20ᵉ »), l'outil vient dessous.
#
# ⚠️ Nuance assumee : ranger l'outil sous « L’association » ne dit PAS qu'il est
#    porte par elle. Le libelle est un rangement de navigation ; la page, elle,
#    porte la formulation prudente validee (« cree par David Lesage, relaye par
#    Resonances Productions », « n'est pas un service de l'association »). Cette
#    formulation est le point sensible du dossier : ne pas la deplacer ici.

# --------------------------------------------------------------------------- #
# « L’ASSOCIATION » MENE A UNE VRAIE PAGE — changement du 15/08/2026
# --------------------------------------------------------------------------- #
# Jusqu'a `resonances-3`, cette entree pointait vers l'ancre `/#association` :
# « Accueil » et « L’association » menaient donc tous les deux a la page
# d'accueil. David l'a remarque et a tranche pour la solution de fond — une page
# `/association` qui rassemble l'objet, les valeurs, les statuts, les mentions
# legales, les adresses, l'adhesion et le contact.
#
# ⚠️ CE QUI A DISPARU AVEC CE CHANGEMENT : le parametre `association_href` de
#    `build_links()` et `inject()`, et son auto-detection (`#association` si la
#    page portait `id="association"`, `/#association` sinon). L'entree porte
#    desormais un href EN DUR, donc la valeur calculee n'aurait plus ete lue
#    nulle part : la laisser aurait fait croire, a la prochaine session, qu'un
#    `id="association"` pose sur une page change encore le menu. `contact_href`,
#    lui, reste utile et fonctionne toujours de la meme facon.
#    Pour revenir en arriere : remettre `None` en href ci-dessous, et remettre
#    les quatre lignes de `association_href` (voir l'historique git de ce
#    fichier), puis incrementer NAV_VERSION.
#
#: (libelle, href, cle de page)
ASSO = [
    ('L’association', '/association', 'association'),
    ('Guso Facile', '/guso-facile', 'guso-facile'),
]

#: cles acceptees par `current` -> utile pour valider / documenter.
#: `association` y est entree le 15/08/2026, par la table ASSO ci-dessus : il n'y
#: a rien a ajouter ici, la liste se deduit des trois tables.
PAGE_KEYS = (['home'] + [k for _, _, k in SCENE] + [k for _, _, k in NID]
             + [k for _, _, k in ASSO if k])


CSS = CSS_MARK + """
/* ===== MENU PARTAGE : sous-menus « Sur scene » et « Le Nid » ===== */
.nav .links{flex-wrap:nowrap}
.nav .links a[aria-current="page"]{color:var(--gold2)}
.nav .links>a[aria-current="page"]{border-bottom:1px solid rgba(216,178,90,.62);padding-bottom:2px}
@media(min-width:861px){.nav .links a:not(.adh),.nm-top{font-size:15px}}
.nm-item{position:relative;display:flex;align-items:center;padding:15px 0;margin:-15px 0}
.nm-top{font-family:'Jost',system-ui,-apple-system,sans-serif;font-weight:400;background:none;
  border:0;padding:0;margin:0;cursor:pointer;color:var(--muted);display:inline-flex;
  align-items:center;gap:7px;letter-spacing:.04em;line-height:1.35;font-size:15px;
  white-space:nowrap;transition:color .2s}
.nm-top:hover,.nm-top:focus-visible{color:var(--gold2)}
.nm-item.nm-open>.nm-top{color:var(--gold2)}
.nm-lbl{border-bottom:1px solid transparent;padding-bottom:2px}
.nm-top.nm-active{color:var(--gold2)}
.nm-top.nm-active .nm-lbl{border-bottom-color:rgba(216,178,90,.62)}
.nm-caret{width:6px;height:6px;flex:0 0 auto;border-right:1.6px solid currentColor;
  border-bottom:1.6px solid currentColor;transform:translateY(-2px) rotate(45deg);
  transition:transform .22s}
.nm-item.nm-open>.nm-top .nm-caret{transform:translateY(1px) rotate(-135deg)}
.nm-sub{background:var(--card)}
@media(min-width:861px){
  .nm-sub{position:absolute;top:100%;left:50%;min-width:252px;max-width:min(330px,90vw);
    transform:translateX(-50%) translateY(3px);
    background:var(--card);border:1px solid rgba(216,178,90,.28);border-radius:14px;
    box-shadow:0 24px 48px rgba(0,0,0,.6);padding:8px;z-index:1200;
    display:flex;flex-direction:column;gap:1px;
    opacity:0;visibility:hidden;pointer-events:none;
    transition:opacity .18s,transform .18s,visibility .18s}
  .nm-item.nm-open>.nm-sub{opacity:1;visibility:visible;pointer-events:auto;
    transform:translateX(-50%) translateY(0)}
  .nav .links .nm-sub a{display:flex;align-items:center;min-height:44px;
    padding:10px 14px;border-radius:9px;font-size:15px;line-height:1.3;
    font-family:'Jost',system-ui,-apple-system,sans-serif;
    color:#dedaf0;text-align:left;text-decoration:none;white-space:normal}
  .nav .links .nm-sub a:hover,.nav .links .nm-sub a:focus-visible{
    background:rgba(216,178,90,.15);color:var(--gold2)}
  .nav .links .nm-sub a[aria-current="page"]{color:var(--gold2);background:rgba(216,178,90,.10)}
  /* zone tampon : le survol ne doit pas casser entre le parent et le panneau */
  .nm-item.nm-open::after{content:'';position:absolute;top:100%;left:-30px;right:-30px;height:8px}
  /* bouton Adherer : 4 des 7 pages n'avaient pas de regle .nav .adh */
  .nav .links a.adh{color:#1a1608 !important;background:var(--gold);
    padding:8px 16px;border-radius:30px;font-weight:600;font-size:15px;
    font-family:'Jost',system-ui,-apple-system,sans-serif;white-space:nowrap;
    border-bottom:0;min-height:0}
  .nav .links a.adh:hover,.nav .links a.adh:focus-visible{background:var(--gold2)}
}
/* barre serree quand la place manque (le nom de l'association ne doit jamais etre touche) */
@media(min-width:861px) and (max-width:1120px){
  .nav{padding-left:18px;padding-right:18px}
  .nav .brand{white-space:nowrap;font-size:16px}
  .nav .links{gap:13px}
  .nav .links a.adh{padding-left:13px;padding-right:13px}
}
@media(min-width:861px) and (max-width:980px){
  .nav .links{gap:10px}
  .nav .links a:not(.adh),.nm-top{font-size:14px}
  .nav .brand{font-size:14px;letter-spacing:.1em}
}
/* ---- mobile : les sous-menus deviennent des accordeons ---- */
@media(max-width:860px){
  /* flex-wrap:nowrap est INDISPENSABLE : le panneau est en flex-direction:column,
     autoriser le retour a la ligne le decoupe en 2-3 COLONNES au lieu de defiler. */
  .nav .links{flex-wrap:nowrap !important;justify-content:flex-start !important}
  .nav .links>:first-child{margin-top:auto}
  .nav .links>:last-child{margin-bottom:auto}
  .nm-item{display:block;width:100%;max-width:340px;position:static;padding:0;margin:0}
  .nav .links .nm-top{display:flex;width:100%;justify-content:center;gap:11px;
    min-height:52px;padding:12px 18px;border-radius:12px;
    font-family:'Cormorant Garamond',Georgia,serif;font-size:21px;letter-spacing:.06em;
    color:#eae7f3;white-space:normal;text-align:center}
  .nav .links .nm-item.nm-open>.nm-top{color:var(--gold2)}
  .nav .links .nm-top .nm-caret{width:8px;height:8px}
  .nm-sub{display:none;background:transparent;border:0;padding:2px 0 12px;margin:0}
  .nm-item.nm-open>.nm-sub{display:block}
  .nav .links .nm-sub a{display:flex !important;align-items:center;justify-content:center;
    min-height:44px;width:100% !important;max-width:none !important;
    padding:10px 14px !important;border-radius:10px;
    font-family:'Jost',system-ui,-apple-system,sans-serif !important;
    font-size:16.5px !important;letter-spacing:.02em;color:#cfcbe6 !important;
    text-align:center}
  .nav .links .nm-sub a[aria-current="page"]{color:var(--gold2) !important}
  .nav .links .nm-sub a:active{background:rgba(216,178,90,.14)}
}
@media print{.nm-sub{display:none}}
""" + CSS_END + "\n"


JS = JS_MARK + """
<script>
/* Sous-menus du menu partage (voir sources/nav_menu.py).
   Desktop : survol + clic + clavier. Mobile : accordeons dans le panneau du hamburger. */
(function(){
  var nav=document.querySelector('.nav'); if(!nav) return;
  var links=nav.querySelector('.links[data-nav]'); if(!links) return;
  if(links.getAttribute('data-nav-ready')==='1') return;   /* garde-fou anti-doublon */
  links.setAttribute('data-nav-ready','1');
  var items=Array.prototype.slice.call(links.querySelectorAll('.nm-item'));
  if(!items.length) return;
  var mq=window.matchMedia('(min-width:861px)');
  var timer=null;
  function desktop(){ return mq.matches; }
  function sub(it){ return it.querySelector('.nm-sub'); }
  function top(it){ return it.querySelector('.nm-top'); }
  function shut(it){
    it.classList.remove('nm-open');
    top(it).setAttribute('aria-expanded','false');
    var s=sub(it); if(s) s.style.marginLeft='';
  }
  function shutAll(except){
    items.forEach(function(o){ if(o!==except) shut(o); });
  }
  /* garde le panneau dans la fenetre (la barre se resserre entre 861 et 1120px) */
  function place(it){
    var s=sub(it); if(!s) return;
    s.style.marginLeft='0px';
    var r=s.getBoundingClientRect(), pad=12, d=0;
    if(r.right>window.innerWidth-pad) d=(window.innerWidth-pad)-r.right;
    if(r.left+d<pad) d=pad-r.left;
    if(d) s.style.marginLeft=Math.round(d)+'px';
  }
  function show(it,focusIdx){
    /* desktop : un seul panneau a la fois. mobile : les deux accordeons
       peuvent rester ouverts (le panneau defile). */
    if(desktop()) shutAll(it);
    it.classList.add('nm-open');
    top(it).setAttribute('aria-expanded','true');
    if(desktop()) place(it);
    if(focusIdx!=null){
      var a=sub(it).querySelectorAll('a');
      if(a.length){ (focusIdx<0?a[a.length-1]:a[focusIdx]).focus(); }
    }
  }
  items.forEach(function(it){
    var btn=top(it), panel=sub(it);
    btn.addEventListener('click',function(e){
      e.preventDefault(); e.stopPropagation();
      if(it.classList.contains('nm-open')) shut(it); else show(it,null);
    });
    btn.addEventListener('keydown',function(e){
      if(e.key==='ArrowDown'){ e.preventDefault(); show(it,0); }
      else if(e.key==='ArrowUp'){ e.preventDefault(); show(it,-1); }
      else if(e.key==='Escape'){ shut(it); }
    });
    it.addEventListener('mouseenter',function(){
      if(!desktop()) return; clearTimeout(timer); show(it,null);
    });
    it.addEventListener('mouseleave',function(){
      if(!desktop()) return;
      clearTimeout(timer);
      timer=setTimeout(function(){ shut(it); },220);
    });
    it.addEventListener('focusout',function(e){
      if(!desktop()) return;
      if(!e.relatedTarget || !it.contains(e.relatedTarget)) shut(it);
    });
    if(panel){
      panel.addEventListener('keydown',function(e){
        var a=Array.prototype.slice.call(panel.querySelectorAll('a'));
        var i=a.indexOf(document.activeElement);
        if(e.key==='ArrowDown'){ e.preventDefault(); a[(i+1)%a.length].focus(); }
        else if(e.key==='ArrowUp'){ e.preventDefault(); a[(i-1+a.length)%a.length].focus(); }
        else if(e.key==='Home'){ e.preventDefault(); a[0].focus(); }
        else if(e.key==='End'){ e.preventDefault(); a[a.length-1].focus(); }
        else if(e.key==='Escape'){ e.preventDefault(); shut(it); btn.focus(); }
        else if(e.key==='Tab' && !e.shiftKey && i===a.length-1){ shut(it); }
      });
    }
  });
  document.addEventListener('keydown',function(e){
    if(e.key!=='Escape') return;
    var o=links.querySelector('.nm-item.nm-open');
    if(o){ var b=top(o); shutAll(null); if(b && desktop()) b.focus(); }
  });
  document.addEventListener('click',function(e){
    if(!links.contains(e.target)) shutAll(null);
  });
  window.addEventListener('resize',function(){ shutAll(null); });
})();
</script>
""" + JS_END + "\n"


# --------------------------------------------------------------------------- #
# construction du HTML du menu
# --------------------------------------------------------------------------- #

def _first_key_index(children, current):
    """Index du 1er enfant portant la cle `current` (une seule entree marquee,
    sinon /le-nid aurait 4 aria-current).

    ⚠️ `current is None` doit renvoyer None SANS comparer. Depuis le 15/08/2026
    plus aucune entree ne porte une cle `None` (« L’association » est devenue une
    vraie page), mais la garde reste : le jour ou une entree de menu redeviendra
    une simple ancre sans page — c'etait le cas de « L’association » jusqu'a
    `resonances-3` —, `None == None` marquerait cette entree comme page courante
    sur TOUTE page appelee avec `current=None`.
    """
    if current is None:
        return None
    for i, (_, _, key) in enumerate(children):
        if key == current:
            return i
    return None


def _group(label, sub_id, children, current, indent='    '):
    active = _first_key_index(children, current)
    o = []
    o.append('%s<div class="nm-item">' % indent)
    o.append('%s  <button type="button" class="nm-top%s" aria-expanded="false"'
             ' aria-haspopup="true" aria-controls="%s">'
             '<span class="nm-lbl">%s</span><span class="nm-caret" aria-hidden="true"></span>'
             '</button>' % (indent, ' nm-active' if active is not None else '', sub_id, label))
    o.append('%s  <div class="nm-sub" id="%s" role="group" aria-label="%s">' % (indent, sub_id, label))
    for i, (lbl, href, _) in enumerate(children):
        cur = ' aria-current="page"' if i == active else ''
        o.append('%s    <a href="%s"%s>%s</a>' % (indent, href, cur, lbl))
    o.append('%s  </div>' % indent)
    o.append('%s</div>' % indent)
    return '\n'.join(o)


def build_links(current=None, contact_href='/#contact'):
    """Renvoie le `<div class="links" data-nav="...">…</div>` complet."""
    i = '    '
    home_cur = ' aria-current="page"' if current == 'home' else ''
    out = ['  <div class="links" data-nav="%s">' % NAV_VERSION]
    out.append('%s<a href="/"%s>Accueil</a>' % (i, home_cur))
    out.append(_group('Sur scène', 'nm-sub-scene', SCENE, current, i))
    out.append(_group('Le Nid', 'nm-sub-nid', NID, current, i))
    out.append(_group('L’association', 'nm-sub-asso', ASSO, current, i))
    out.append('%s<a href="%s">Contact</a>' % (i, contact_href))
    out.append('%s<a class="adh" href="%s" target="_blank" rel="noopener">Adhérer</a>'
               % (i, ADHESION))
    out.append('  </div>')
    return '\n'.join(out)


# --------------------------------------------------------------------------- #
# remplacement dans la page
# --------------------------------------------------------------------------- #

_OPEN = re.compile(r'<div class="links"[^>]*>')


def _replace_links_block(html, new_block):
    """Remplace le premier <div class="links"...> ... </div> en comptant les
    <div> imbriques (le nouveau bloc en contient : un remplacement naif par
    regex non gourmande couperait au mauvais endroit)."""
    m = _OPEN.search(html)
    if not m:
        raise ValueError('aucun <div class="links"> trouve dans la page')
    i = m.end()
    depth = 1
    tag = re.compile(r'<(/?)div\b', re.I)
    while depth:
        t = tag.search(html, i)
        if not t:
            raise ValueError('</div> de fermeture de .links introuvable')
        depth += -1 if t.group(1) else 1
        i = t.end()
    end = html.index('>', i) + 1
    # on avale l'indentation qui precede le bloc pour garder une mise en page propre
    start = m.start()
    j = start
    while j > 0 and html[j - 1] in ' \t':
        j -= 1
    if j > 0 and html[j - 1] == '\n':
        start = j
    return html[:start] + new_block + html[end:]


def _strip(html, mark, end):
    """Retire un bloc delimite (upgrade de NAV_VERSION)."""
    a = html.find(mark)
    if a == -1:
        return html
    b = html.find(end, a)
    if b == -1:
        return html
    return html[:a] + html[b + len(end):]


def inject(html, current=None, contact_href=None):
    """Applique le menu partage a une page HTML complete.

    Voir le docstring du module pour la description des parametres.
    Idempotent : si `data-nav="<NAV_VERSION>"` est deja present, renvoie `html`.
    """
    if current is not None and current not in PAGE_KEYS:
        raise ValueError('cle de page inconnue : %r (attendu : %s)'
                         % (current, ', '.join(PAGE_KEYS)))
    if 'data-nav="%s"' % NAV_VERSION in html:
        return html                       # <<< garde-fou anti-duplication

    # une ancienne version du menu ? on nettoie son CSS / JS avant de reinjecter
    old = re.search(r'/\* == nav_menu\.py \(([^)]*)\) == \*/', html)
    if old:
        html = _strip(html, old.group(0), CSS_END)
        oldjs = re.search(r'<!-- nav_menu\.py \(([^)]*)\) -->', html)
        if oldjs:
            html = _strip(html, oldjs.group(0), JS_END)
        # le bloc .links de l'ancienne version est remplace ci-dessous par
        # _replace_links_block (son regex accepte l'attribut data-nav).

    if contact_href is None:
        contact_href = '#contact' if 'id="contact"' in html else '/#contact'

    html = _replace_links_block(html, build_links(current, contact_href))

    if '</style>' in html:
        html = html.replace('</style>', CSS + '</style>', 1)
    else:
        raise ValueError('la page n’a pas de </style> ou inserer le CSS du menu')
    if '</body>' in html:
        html = html.replace('</body>', JS + '</body>', 1)
    else:
        html += JS
    return html


# --------------------------------------------------------------------------- #
# helpers fichiers / CLI
# --------------------------------------------------------------------------- #

#: deduction de la cle de page a partir du chemin
_PATH_KEYS = {
    'index.html': 'home',
    'rituals': 'rituals',
    'rituals-trio': 'rituals-trio',
    'e-motion': 'e-motion',
    'david-lesage-en-concert': 'david-lesage-en-concert',
    'le-nid': 'le-nid',
    'concerts-david-lesage': 'concerts-david-lesage',
    'rythme-calebasse': 'rythme-calebasse',
    'le-soin-soa': 'le-soin-soa',
    'association': 'association',
    'guso-facile': 'guso-facile',
}


def key_for_path(path):
    """'le-nid/index.html' -> 'le-nid' ; 'index.html' -> 'home' ; sinon None."""
    parts = [p for p in path.replace('\\', '/').split('/') if p]
    for p in reversed(parts):
        if p in _PATH_KEYS and p != 'index.html':
            return _PATH_KEYS[p]
    if parts and parts[-1] == 'index.html':
        return 'home'
    return None


def apply_to_file(path, current=None):
    """Injecte le menu dans un fichier. Renvoie True s'il a ete modifie."""
    with open(path, encoding='utf-8') as f:
        src = f.read()
    out = inject(src, current)
    if out == src:
        return False
    # Derniere barriere avant l'ecriture : `nav_menu.py` est le dernier script a
    # repasser sur la plupart des pages, c'est donc ici qu'on attrape une note
    # de redaction laissee en commentaire HTML — y compris sur une page editee
    # a la main. Si elle est la, on n'ecrit pas.
    verif_commentaires.verifier(out, path)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(out)
    return True


if __name__ == '__main__':
    import sys
    for arg in sys.argv[1:]:
        path, _, key = arg.partition('=')
        key = key or key_for_path(path)
        changed = apply_to_file(path, key or None)
        print(('OK   ' if changed else 'SKIP ') + path + '  [' + str(key) + ']')
