# -*- coding: utf-8 -*-
"""Genere la section AGENDA de la page /le-nid a partir du calendrier Google 'Le Nid'.

Les evenements sont recuperes via le connecteur Google Calendar puis figes ici.
Pour actualiser : relancer la lecture du calendrier et mettre a jour EVENTS.
"""
import datetime as dt

CAL_ID = '30716d7f4373d33769612165eb0607e5b33fd533b984df2df61fe9518ab32eae@group.calendar.google.com'
CAL_SUB = ('https://calendar.google.com/calendar/u/0?cid=MzA3MTZkN2Y0MzczZDMzNzY5NjEyMTY1'
           'ZWIwNjA3ZTViMzNmZDUzM2I5ODRkZjJkZjYxZmU5NTE4YWIzMmVhZUBncm91cC5jYWxlbmRhci5nb29nbGUuY29t')

# (date ISO, heure debut, heure fin, type, titre, note)
EVENTS = [
    ('2026-08-23', '16:00', '19:00', 'showcase', 'Showcase', ''),
    ('2026-09-04', '18:30', '23:30', 'mensuel', 'Rendez-vous mensuel au Nid', ''),
    ('2026-09-06', '16:30', '19:00', 'yoga',     'Atelier de yoga', 'avec Iris Chasles'),
    ('2026-09-19', '16:00', '19:00', 'showcase', 'Showcase', ''),
    ('2026-09-20', '10:00', '12:00', 'rythme',   'Workshop rythme à la calebasse', 'avec David Lesage'),
    ('2026-09-26', '17:00', '19:00', 'residence','Sortie de résidence', 'restitution du travail en trio'),
    ('2026-09-26', '20:00', '22:00', 'concert',  'Concert — David, Iris & Julien', 'le trio en concert'),
    ('2026-10-02', '18:30', '23:30', 'mensuel',  'Rendez-vous mensuel au Nid', ''),
    ('2026-10-04', '16:30', '19:00', 'yoga',     'Atelier de yoga', 'avec Iris Chasles'),
    ('2026-10-10', '19:00', '21:00', 'concert',  'Concert — David Lesage solo', ''),
    ('2026-10-17', '15:00', '17:00', 'rythme',   'Workshop rythme à la calebasse', 'avec David Lesage'),
    ('2026-10-18', '16:00', '19:00', 'showcase', 'Showcase', ''),
    ('2026-11-07', '18:30', '23:30', 'mensuel',  'Rendez-vous mensuel au Nid', ''),
    ('2026-11-08', '16:30', '19:00', 'yoga',     'Atelier de yoga', 'avec Iris Chasles'),
    ('2026-11-14', '16:00', '19:00', 'showcase', 'Showcase', ''),
    ('2026-11-15', '15:00', '17:00', 'rythme',   'Workshop rythme à la calebasse', 'avec David Lesage'),
    ('2026-11-28', '18:00', '20:00', 'concert',  'Concert — David Lesage solo', ''),
    ('2026-12-04', '18:30', '23:30', 'mensuel',  'Rendez-vous mensuel au Nid', ''),
    ('2026-12-05', '15:00', '18:00', 'showcase', 'Showcase', ''),
    ('2026-12-06', '16:30', '19:00', 'yoga',     'Atelier de yoga', 'avec Iris Chasles'),
]

LIEU = 'Le Nid, 29 rue des Orteaux, 75020 Paris'
# NB : le code portail n'est PAS diffuse publiquement (site + .ics telechargeables).
ACCES_PUBLIC = ('Au fond de la cour, porte verte, 3e etage. '
                'Le code du portail vous est communique avec votre confirmation d\'inscription.')
JAUGE = ('Jauge limitee : chaque evenement est sur invitation ou sur inscription prealable. '
         'Merci de reserver avant de venir.')

DESCR = {
 'mensuel':  'Le rendez-vous mensuel du Nid : un temps convivial qui melange pratique, musique et partage, dans un cadre intime. Reserve aux adherents de l\'association.',
 'concert':  'Un concert en format intime : voix, handpan electronique, harpe africaine (Ngoni), calebasse et percussions electro-organiques.',
 'yoga':     'Atelier de yoga guide par Iris Chasles : yoga postural, respiration et meditation. Pratique accessible a tous les niveaux.',
 'rythme':   'Workshop rythme a la calebasse avec David Lesage : les bases, les frappes, la pulsation collective. Aucun prerequis musical.',
 'showcase': 'Format court et intime : la decouverte d\'un projet en cours, d\'une creation ou d\'un artiste invite, au plus pres.',
 'residence':'Sortie de residence : restitution publique du travail mene en trio.',
}

LESAGE   = 'https://lesagedavid.fr'
SHOWROOM = 'https://www.handpan-studio.app/showroom#agenda'
ADHESION = 'https://www.helloasso.com/beta/associations/resonances-productions/adhesions/adhesion-resonances-productions'
YOGA_INS = 'https://www.helloasso.com/associations/resonances-productions/evenements/atelier-mensuel-au-nid'
MAILTO   = 'mailto:contact@resonancesproductions.org?subject=Le%20Nid%20—%20r%C3%A9servation'

# type : (libelle, couleur, lien de reservation, libelle du bouton)
TYPES = {
    'mensuel':   ('Rendez-vous mensuel', '#d8b25a', ADHESION, 'Adhérer ↗'),
    'concert':   ('Concert',             '#e08a5f', LESAGE,   'Réserver ↗'),
    'yoga':      ('Atelier yoga',        '#7fb2a3', YOGA_INS, 'S’inscrire ↗'),
    'rythme':    ('Workshop rythme',     '#8f7ad1', MAILTO,   'Réserver'),
    'showcase':  ('Showcase',            '#6f9bd1', SHOWROOM, 'Réserver ↗'),
    'residence': ('Sortie de résidence', '#c98fb0', MAILTO,   'Réserver'),
}

JOURS = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin',
        'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']


def esc_attr(x):
    return (x.replace('&', '&amp;').replace('"', '&quot;')
             .replace('<', '&lt;').replace('>', '&gt;'))


def url_public(u):
    if u.startswith('mailto:'):
        return 'contact@resonancesproductions.org'
    return u


def build():
    # regroupement par mois, dans l'ordre chronologique
    groupes = []
    for iso, h1, h2, typ, titre, note in EVENTS:
        d = dt.date.fromisoformat(iso)
        cle = (d.year, d.month)
        if not groupes or groupes[-1][0] != cle:
            groupes.append((cle, []))
        groupes[-1][1].append((d, h1, h2, typ, titre, note))

    # legende
    leg = ''.join(
        f'<span class="ag-leg"><i style="background:{c}"></i>{lab}</span>'
        for lab, c, _u, _t in TYPES.values())

    out = ['<section class="agenda" id="agenda"><div class="wrap">',
           '  <div class="kick">L’agenda</div>',
           '  <h2 class="sec-title">Les prochaines dates</h2>',
           '  <p class="lead">Rendez-vous mensuels, concerts, ateliers et workshops — au Nid, 29 rue des Orteaux, Paris 20<sup>e</sup>.</p>',
           f'  <div class="ag-legend">{leg}</div>']

    for (an, mois), evs in groupes:
        out.append(f'  <div class="ag-month">{MOIS[mois-1]} {an}</div>')
        out.append('  <div class="ag-list">')
        for d, h1, h2, typ, titre, note in evs:
            lab, col, url, btn = TYPES[typ]
            ext = ' target="_blank" rel="noopener"' if url.startswith('http') else ''
            jour = JOURS[d.weekday()]
            # heure de Paris -> UTC (heure d'ete jusqu'au dernier dimanche d'octobre)
            offset = 2 if (d.month, d.day) < (10, 25) else 1
            def utc(h):
                hh, mm = map(int, h.split(':'))
                return (dt.datetime(d.year, d.month, d.day, hh, mm)
                        - dt.timedelta(hours=offset)).strftime('%Y%m%dT%H%M%SZ')
            desc = DESCR[typ] + ' | ' + ACCES_PUBLIC + ' | ' + JAUGE + ' | Reservation : ' + url_public(url)
            data = (f' data-s="{utc(h1)}" data-e="{utc(h2)}"'
                    f' data-t="{esc_attr(titre)}" data-d="{esc_attr(desc)}"')
            note_html = f'<span class="ag-note">{note}</span>' if note else ''
            out.append(
                f'    <div class="ag-item" style="--c:{col}"{data}>'
                f'<div class="ag-date"><span class="ag-d">{d.day}</span>'
                f'<span class="ag-j">{jour[:3]}.</span></div>'
                f'<div class="ag-body"><span class="ag-type">{lab}</span>'
                f'<h3>{titre}</h3>{note_html}</div>'
                f'<div class="ag-hour">{h1}<span>→ {h2}</span></div>'
                f'<a class="ag-btn" href="{url}"{ext}>{btn}</a>'
                f'<button class="ag-cal" type="button" title="Ajouter a mon agenda avec rappel">+ Agenda</button>'
                f'</div>')
        out.append('  </div>')

    out += [
        '  <div class="ag-access">',
        '    <div><span>Le lieu</span><b>Le Nid</b> — 29 rue des Orteaux, 75020 Paris<br>'
        'Au fond de la cour, porte verte, puis 3<sup>e</sup> étage.<br>'
        '<i>Le code du portail vous est communiqué avec votre confirmation.</i></div>',
        '    <div><span>Accès</span>Métro Alexandre Dumas, Buzenval ou Maraîchers.</div>',
        '    <div><span>Jauge limitée</span>Chaque événement se tient <b>sur invitation ou sur inscription</b>. '
        'Merci de réserver avant de venir : les places partent vite.</div>',
        '  </div>',
        '  <div class="ag-foot">',
        '    <button class="btn ag-all" type="button">↓ Ajouter toutes les dates à mon agenda</button>',
        f'    <a class="btn ghost" href="{CAL_SUB}" target="_blank" rel="noopener">↗ S’abonner au calendrier Google</a>',
        '    <a class="btn" href="mailto:contact@resonancesproductions.org?subject=Le%20Nid%20—%20réservation">Réserver une place</a>',
        '  </div>',
        '  <p class="ag-tip">« + Agenda » télécharge un fichier compatible Google Agenda, Apple Calendrier et Outlook, avec deux rappels automatiques (la veille et 2 h avant).</p>',
        '</div></section>', '']
    return '\n'.join(out)


CSS = """
/* ===== AGENDA DU NID ===== */
.agenda{background:linear-gradient(180deg,var(--night),#0b0c1e)}
.ag-legend{display:flex;flex-wrap:wrap;gap:10px 20px;margin-top:26px}
.ag-leg{display:inline-flex;align-items:center;gap:7px;color:var(--muted);font-size:13px}
.ag-leg i{width:9px;height:9px;border-radius:50%;display:inline-block;flex:0 0 auto}
.ag-month{margin-top:40px;margin-bottom:12px;color:var(--gold);font-family:'Cormorant Garamond',Georgia,serif;
  font-size:24px;font-weight:600;text-transform:capitalize;border-bottom:1px solid var(--line);padding-bottom:8px}
.ag-list{display:grid;gap:10px}
.ag-item{display:grid;grid-template-columns:64px 1fr auto auto;align-items:center;gap:18px;
  background:var(--card);border:1px solid rgba(255,255,255,.07);border-left:3px solid var(--c);
  border-radius:12px;padding:14px 20px;transition:transform .2s,border-color .2s}
.ag-item:hover{transform:translateX(3px);border-color:var(--line);border-left-color:var(--c)}
.ag-date{text-align:center;line-height:1}
.ag-d{display:block;font-family:'Cormorant Garamond',Georgia,serif;font-size:30px;color:#fff;font-weight:600}
.ag-j{display:block;font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.12em;margin-top:3px}
.ag-body h3{font-size:19px;color:#fff;font-weight:600;margin:3px 0 0;font-family:'Cormorant Garamond',Georgia,serif}
.ag-type{font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--c);font-weight:600}
.ag-note{display:block;color:var(--muted);font-size:13.5px;font-style:italic;margin-top:2px}
.ag-hour{text-align:right;color:#d3d0e8;font-size:15px;white-space:nowrap}
.ag-hour span{display:block;color:var(--muted);font-size:12px}
.ag-btn{display:inline-block;border:1px solid var(--c);color:var(--c);border-radius:20px;
  padding:7px 15px;font-size:12.5px;text-decoration:none;white-space:nowrap;transition:background .2s,color .2s}
.ag-btn:hover{background:var(--c);color:#12121f}
.ag-foot{display:flex;flex-wrap:wrap;gap:14px;margin-top:38px}
.ag-tip{color:var(--muted);font-size:13.5px;margin-top:16px;font-style:italic}
.ag-cal{border:1px solid rgba(255,255,255,.16);background:rgba(255,255,255,.04);color:#d3d0e8;
  border-radius:20px;padding:7px 14px;font-size:12.5px;cursor:pointer;white-space:nowrap;
  font-family:inherit;transition:background .2s,color .2s,border-color .2s}
.ag-cal:hover{background:var(--gold);color:#1a1608;border-color:var(--gold)}
.ag-access{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px;margin-top:40px}
.ag-access>div{background:var(--card);border:1px solid rgba(255,255,255,.07);border-radius:14px;
  padding:20px 22px;color:#d3d0e8;font-size:14.5px;line-height:1.6}
.ag-access span{display:block;color:var(--gold);font-size:10.5px;letter-spacing:.16em;
  text-transform:uppercase;font-weight:600;margin-bottom:8px}
.ag-access i{color:var(--muted);font-size:13px}
@media(max-width:640px){
  .ag-item{grid-template-columns:52px 1fr;gap:8px 14px;padding:13px 16px}
  .ag-cal{grid-column:2;justify-self:start}
  .ag-hour{grid-column:2;text-align:left;margin-top:2px;font-size:14px}
  .ag-hour span{display:inline;margin-left:4px}
  .ag-btn{grid-column:2;justify-self:start;margin-top:6px}
  .ag-d{font-size:26px}
}
"""

ICS_JS = """
<script>
(function(){
  function esc(s){return String(s).replace(/([,;\\\\])/g,'\\\\$1').replace(/\\n/g,'\\\\n');}
  var LIEU='Le Nid, 29 rue des Orteaux, 75020 Paris';
  function ics(items,name){
    var L=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Resonances Productions//Le Nid//FR',
           'CALSCALE:GREGORIAN','METHOD:PUBLISH','X-WR-CALNAME:Le Nid'];
    var now=new Date().toISOString().replace(/[-:]/g,'').split('.')[0]+'Z';
    items.forEach(function(it,i){
      L.push('BEGIN:VEVENT','UID:lenid-'+it.s+'-'+i+'@resonancesproductions.org',
        'DTSTAMP:'+now,'DTSTART:'+it.s,'DTEND:'+it.e,
        'SUMMARY:'+esc(it.t),'LOCATION:'+esc(LIEU),'DESCRIPTION:'+esc(it.d),
        'BEGIN:VALARM','TRIGGER:-P1D','ACTION:DISPLAY','DESCRIPTION:'+esc(it.t)+' demain','END:VALARM',
        'BEGIN:VALARM','TRIGGER:-PT2H','ACTION:DISPLAY','DESCRIPTION:'+esc(it.t)+' dans 2 heures','END:VALARM',
        'END:VEVENT');
    });
    L.push('END:VCALENDAR');
    var b=new Blob([L.join('\\r\\n')],{type:'text/calendar;charset=utf-8'});
    var a=document.createElement('a');
    a.href=URL.createObjectURL(b); a.download=name; document.body.appendChild(a); a.click();
    setTimeout(function(){URL.revokeObjectURL(a.href);a.remove();},400);
  }
  function read(el){return {s:el.dataset.s,e:el.dataset.e,t:el.dataset.t,d:el.dataset.d};}
  document.addEventListener('click',function(ev){
    var b=ev.target.closest('.ag-cal'); if(b){
      var it=read(b.closest('.ag-item'));
      ics([it], 'le-nid-'+it.t.toLowerCase().replace(/[^a-z0-9]+/g,'-').slice(0,40)+'.ics');
      b.textContent='\\u2713 Ajoute'; setTimeout(function(){b.textContent='+ Agenda';},2500);
      return;
    }
    var all=ev.target.closest('.ag-all'); if(all){
      ics([].map.call(document.querySelectorAll('.ag-item'),read),'agenda-le-nid.ics');
      all.textContent='\\u2713 Agenda telecharge'; setTimeout(function(){all.textContent='\\u2193 Ajouter toutes les dates a mon agenda';},2800);
    }
  });
})();
</script>
"""


if __name__ == '__main__':
    p = 'lenid_deploy/index.html'
    with open(p, encoding='utf-8') as f:
        html = f.read()

    # nettoyage d'une eventuelle version precedente
    import re
    html = re.sub(r'<section class="agenda" id="agenda">.*?</div></section>\n', '', html, flags=re.S)
    html = re.sub(r'/\* ===== AGENDA DU NID ===== \*/.*?(?=\n/\* |\n</style>)', '', html, flags=re.S)

    # CSS
    html = html.replace('</style>', CSS + '</style>', 1)

    # section : juste apres le programme, avant le divider qui precede "Le lieu"
    anchor = '<div class="divider"></div>\n\n<section class="lieu">'
    assert anchor in html, 'ancre lieu introuvable'
    html = html.replace(anchor, '<div class="divider"></div>\n\n' + build() + '\n<div class="divider"></div>\n\n<section class="lieu">', 1)

    # lien dans la nav + remplacement de la note "calendrier en cours"
    html = html.replace('<a href="#contact">Contact</a>',
                        '<a class="hide-s" href="#agenda">Agenda</a>\n    <a href="#contact">Contact</a>', 1)
    html = html.replace('<a class="btn ghost" href="#contact">Être informé des dates</a>',
                        '<a class="btn ghost" href="#agenda">Voir les prochaines dates</a>', 1)
    old_note = ('<b>Dates, tarifs et réservations :</b> le calendrier du Nid est en cours de mise à jour. '
                'Écrivez-nous pour connaître les prochaines dates et réserver votre place — nous vous répondons directement.')
    html = html.replace(old_note,
                        '<b>Dates, tarifs et réservations :</b> retrouvez toutes les prochaines dates dans '
                        '<a href="#agenda">l’agenda ci-dessous</a>. Les places sont limitées — écrivez-nous pour réserver.', 1)
    html = html.replace('<a class="btn" href="mailto:contact@resonancesproductions.org?subject=Le%20Nid%20—%20prochaines%20dates">Demander les prochaines dates</a>',
                        '<a class="btn" href="#agenda">Voir l’agenda</a>', 1)

    # --- prochaines dates dans les cartes du programme ---
    import collections
    prochaine = collections.OrderedDict()
    for iso, h1, _h2, typ, _t, _n in EVENTS:
        prochaine.setdefault(typ, []).append((dt.date.fromisoformat(iso), h1))

    def dates_courtes(typ, n=3):
        items = prochaine.get(typ, [])[:n]
        if not items:
            return ''
        txt = ' · '.join(f'{d.day} {MOIS[d.month-1][:4]}.' for d, _h in items)
        return (f'<div class="offer-dates"><span>Prochaines dates</span>{txt} '
                f'<a href="#agenda">tout voir</a></div>')

    for marqueur, typ in (
        ('<div class="who">Avec David Lesage</div>\n    </div>\n\n    <div class="offer">\n      <div class="t">Corps &amp; souffle</div>', 'concert'),
        ('<div class="who">Avec Iris Chasles</div>\n    </div>\n\n    <div class="offer">\n      <div class="t">Transmission</div>', 'yoga'),
    ):
        if marqueur in html:
            html = html.replace(marqueur, marqueur.replace('</div>\n\n    <div class="offer">',
                dates_courtes(typ) + '</div>\n\n    <div class="offer">', 1), 1)

    # workshop calebasse (derniere carte 'Avec David Lesage' du bloc transmission)
    html = html.replace('on entre dans le rythme par le corps et l’écoute.</p>\n      <div class="who">Avec David Lesage</div>',
        'on entre dans le rythme par le corps et l’écoute.</p>\n      <div class="who">Avec David Lesage</div>' + dates_courtes('rythme'), 1)

    # carte Showcase ajoutee au programme
    carte_showcase = ('''    <div class="offer">
      <div class="t">Scène ouverte</div>
      <h3>Showcase</h3>
      <p>Un format court et intime : on découvre un projet en cours, une création, un artiste invité — au plus près, dans le salon du Nid.</p>
      ''' + dates_courtes('showcase') + '''
      <div class="who">Réservation sur <a href="https://www.handpan-studio.app/showroom#agenda" target="_blank" rel="noopener">handpan-studio.app</a></div>
    </div>
''')
    anc = '  </div>\n\n  <div class="note">'
    if anc in html:
        html = html.replace(anc, carte_showcase + anc, 1)

    CSS_DATES = ('''
.offer-dates{margin-top:14px;padding-top:12px;border-top:1px solid rgba(255,255,255,.08);color:#d3d0e8;font-size:13.5px}
.offer-dates span{display:block;color:var(--gold);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;font-weight:600;margin-bottom:4px}
.offer-dates a{color:var(--gold2);font-size:12.5px;text-decoration:underline;text-underline-offset:2px}
''')
    html = html.replace('</style>', CSS_DATES + '</style>', 1)
    if 'ag-cal' in html and 'BEGIN:VCALENDAR' not in html:
        html = html.replace('</body>', ICS_JS + '</body>', 1)

    # prise de rendez-vous psychotherapie -> site d'Iris
    _old_psy = '      <div class="who">Avec Iris Chasles · <a href="https://www.irischasles.com/psychotherapie-paris-20" target="_blank" rel="noopener">En savoir plus</a></div>'
    _new_psy = '      <div class="who">Avec Iris Chasles</div>\n      <div class="offer-dates"><span>Sur rendez-vous</span>Séances en présentiel au Nid ou en visio. <a href="https://www.irischasles.com/" target="_blank" rel="noopener">Prendre rendez-vous sur irischasles.com ↗</a></div>'
    if _old_psy in html:
        html = html.replace(_old_psy, _new_psy, 1)
    else:
        print('ATTENTION : bloc psychotherapie introuvable')

    with open(p, 'w', encoding='utf-8') as f:
        f.write(html)
    print('agenda injecte :', len(EVENTS), 'dates,', len(set(e[3] for e in EVENTS)), 'types')
