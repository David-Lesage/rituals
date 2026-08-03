# -*- coding: utf-8 -*-
"""Genere la section AGENDA de la page /le-nid a partir du calendrier Google 'Le Nid'.

Les evenements sont recuperes via le connecteur Google Calendar puis figes ici.
Pour actualiser : relancer la lecture du calendrier et mettre a jour EVENTS.
"""
import datetime as dt
import urllib.parse

CAL_ID = '30716d7f4373d33769612165eb0607e5b33fd533b984df2df61fe9518ab32eae@group.calendar.google.com'
CAL_SUB = ('https://calendar.google.com/calendar/r?cid=MzA3MTZkN2Y0MzczZDMzNzY5NjEyMTY1'
           'ZWIwNjA3ZTViMzNmZDUzM2I5ODRkZjJkZjYxZmU5NTE4YWIzMmVhZUBncm91cC5jYWxlbmRhci5nb29nbGUuY29t')
# Flux iCal public du meme calendrier (Apple Calendrier, Outlook, Thunderbird...)
CAL_WEBCAL = ('webcal://calendar.google.com/calendar/ical/'
              + urllib.parse.quote(CAL_ID, safe='') + '/public/basic.ics')

# (date ISO, heure debut, heure fin, type, titre, note)
EVENTS = [
    ('2026-08-23', '16:00', '19:00', 'showcase', 'Présentation d’instruments d’exception', ''),
    ('2026-09-04', '18:30', '23:30', 'mensuel', 'Rendez-vous mensuel au Nid', ''),
    ('2026-09-06', '16:30', '19:00', 'yoga',     'Atelier de yoga', 'avec Iris Chasles'),
    ('2026-09-19', '16:00', '19:00', 'showcase', 'Présentation d’instruments d’exception', ''),
    ('2026-09-20', '10:00', '12:00', 'rythme',   'Workshop rythme à la calebasse', 'avec David Lesage'),
    ('2026-09-26', '17:00', '19:00', 'residence','Sortie de résidence', 'restitution du travail en trio'),
    ('2026-09-26', '20:00', '22:00', 'concert',  'Concert — David, Iris & Julien', 'le trio en concert'),
    ('2026-10-02', '18:30', '23:30', 'mensuel',  'Rendez-vous mensuel au Nid', ''),
    ('2026-10-04', '16:30', '19:00', 'yoga',     'Atelier de yoga', 'avec Iris Chasles'),
    ('2026-10-10', '19:00', '21:00', 'concert',  'Concert — David Lesage solo', ''),
    ('2026-10-17', '15:00', '17:00', 'rythme',   'Workshop rythme à la calebasse', 'avec David Lesage'),
    ('2026-10-18', '16:00', '19:00', 'showcase', 'Présentation d’instruments d’exception', ''),
    ('2026-11-07', '18:30', '23:30', 'mensuel',  'Rendez-vous mensuel au Nid', ''),
    ('2026-11-08', '16:30', '19:00', 'yoga',     'Atelier de yoga', 'avec Iris Chasles'),
    ('2026-11-14', '16:00', '19:00', 'showcase', 'Présentation d’instruments d’exception', ''),
    ('2026-11-15', '15:00', '17:00', 'rythme',   'Workshop rythme à la calebasse', 'avec David Lesage'),
    ('2026-11-28', '18:00', '20:00', 'concert',  'Concert — David Lesage solo', ''),
    ('2026-12-04', '18:30', '23:30', 'mensuel',  'Rendez-vous mensuel au Nid', ''),
    ('2026-12-05', '15:00', '18:00', 'showcase', 'Présentation d’instruments d’exception', ''),
    ('2026-12-06', '16:30', '19:00', 'yoga',     'Atelier de yoga', 'avec Iris Chasles'),
]

LIEU = 'Le Nid, 29 rue des Orteaux, 75020 Paris'
# Libelle de lieu utilise dans les liens Google Agenda (tirets cadratins comme sur le site)
LIEU_GCAL = 'Le Nid — 29 rue des Orteaux, 75020 Paris'
# NB : le lien Google "action=TEMPLATE" ne permet PAS d'imposer des rappels
# (contrairement au .ics et a ses VALARM) : limitation assumee.
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
 'showcase': 'Presentation, decouverte et essai d\'instruments d\'exception : le Neotone (handpan electronique de facture professionnelle), des handpans acoustiques Yishama, la calebasse, le Gonilele (petite harpe africaine) et des micros concus pour le handpan. Des instruments faits main, produits en tres petites series, dont la valeur atteint plusieurs milliers d\'euros. David Lesage les presente, les fait sonner devant vous, repond aux questions, puis les met entre vos mains. Gratuit, sur inscription, environ 2 h. Aucune experience requise.',
 'residence':'Sortie de residence : restitution publique du travail mene en trio.',
}

# Versions accentuees, utilisees uniquement pour les liens Google Agenda
# (les .ics restent sur les chaines sans accents, par compatibilite).
DESCR_FR = {
 'mensuel':  'Le rendez-vous mensuel du Nid : un temps convivial qui mélange pratique, musique et partage, dans un cadre intime. Réservé aux adhérents de l’association.',
 'concert':  'Un concert en format intime : voix, handpan électronique, harpe africaine (Ngoni), calebasse et percussions électro-organiques.',
 'yoga':     'Atelier de yoga guidé par Iris Chasles : yoga postural, respiration et méditation. Pratique accessible à tous les niveaux.',
 'rythme':   'Workshop rythme à la calebasse avec David Lesage : les bases, les frappes, la pulsation collective. Aucun prérequis musical.',
 'showcase': 'Présentation, découverte & essai d’instruments d’exception : le Neotone (handpan électronique de facture professionnelle), des handpans acoustiques Yishama, la calebasse, le Gonilélé (petite harpe africaine) et des micros conçus pour le handpan. Des instruments faits main, produits en très petites séries, dont la valeur atteint plusieurs milliers d’euros. David Lesage les présente, les fait sonner devant vous, répond à toutes les questions, puis les met entre vos mains. Gratuit, sur inscription, environ 2 h. Aucune expérience requise.',
 'residence':'Sortie de résidence : restitution publique du travail mené en trio.',
}
ACCES_PUBLIC_FR = ('Au fond de la cour, porte verte, 3e étage. '
                   'Le code du portail vous est communiqué avec votre confirmation d’inscription.')
JAUGE_FR = ('Jauge limitée : chaque événement est sur invitation ou sur inscription préalable. '
            'Merci de réserver avant de venir.')

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
    # NB : cle technique 'showcase' conservee (interne). Libelle visible = badge court
    # (contrainte de place dans l'agenda) ; le nom complet de la categorie est
    # « Présentation, découverte & essai d'instruments d'exception ».
    'showcase':  ('Découverte &amp; essai', '#6f9bd1', SHOWROOM, 'Réserver ↗'),
    'residence': ('Sortie de résidence', '#c98fb0', MAILTO,   'Réserver'),
}

# ---------------------------------------------------------------------------
# SURCHARGE DU LIEN DE RESERVATION, EVENEMENT PAR EVENEMENT
# ---------------------------------------------------------------------------
# Par defaut, le lien de reservation vient du TYPE (dict TYPES ci-dessus) :
# tous les concerts partagent le meme lien, tous les ateliers yoga le meme, etc.
# Mais deux evenements du MEME type peuvent avoir des billetteries differentes.
# On les surcharge ici, en indexant par (date ISO, heure de debut) — la paire
# qui identifie un evenement de facon unique dans EVENTS.
#
# Valeur acceptee : soit une URL seule (le libelle du bouton reste celui du type),
# soit un couple (url, libelle_du_bouton) pour changer aussi le texte du bouton.
#
# La surcharge se propage automatiquement PARTOUT : bouton « Reserver » de la
# ligne d'agenda, ligne « Reservation : … » de la description du lien
# « + Google Agenda » (DESCR_FR) et description embarquee dans le .ics.
#
# Billetterie HelloAsso des concerts de David Lesage EN SOLO (uniquement).
CONCERT_SOLO = ('https://www.helloasso.com/associations/resonances-productions/'
                'evenements/concert-intimiste-david-lesage-au-coeur-de-paris-1')
URL_PAR_EVENT = {
    ('2026-10-10', '19:00'): CONCERT_SOLO,   # Concert — David Lesage solo
    ('2026-11-28', '18:00'): CONCERT_SOLO,   # Concert — David Lesage solo
    # A COMPLETER quand David fournira les liens :
    #   ('2026-09-26', '20:00'): '…'  # Concert du trio (David, Iris & Julien) :
    #       ce n'est PAS l'evenement HelloAsso du concert solo. En attendant, il
    #       garde le lien par defaut du type 'concert'.
    #   workshops rythme a la calebasse (20/09, 17/10, 15/11) : billetterie
    #       HelloAsso a creer ; ils restent sur le mailto pour l'instant.
}


def reservation(iso, h1, typ):
    """Retourne (url, libelle_du_bouton) pour un evenement donne.

    Surcharge par evenement si elle existe (URL_PAR_EVENT), sinon valeur du type.
    """
    _lab, _col, url, btn = TYPES[typ]
    over = URL_PAR_EVENT.get((iso, h1))
    if isinstance(over, tuple):
        url, btn = over
    elif over:
        url = over
    return url, btn


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


def gcal_url(titre, start_utc, end_utc, typ, url):
    """Lien 'Ajouter a mon Google Agenda' (action=TEMPLATE), fiable sur smartphone.

    Jamais de code portail ici : uniquement la phrase publique.
    """
    details = (DESCR_FR[typ] + '\n\n'
               + 'Réservation : ' + url_public(url) + '\n\n'
               + ACCES_PUBLIC_FR + '\n' + JAUGE_FR)
    q = urllib.parse.urlencode({
        'action': 'TEMPLATE',
        'text': titre,
        'dates': start_utc + '/' + end_utc,
        'details': details,
        'location': LIEU_GCAL,
        'ctz': 'Europe/Paris',
    }, quote_via=urllib.parse.quote)
    return 'https://calendar.google.com/calendar/render?' + q


# --- encart d'abonnement au calendrier (en tete de l'agenda) ---
SUB_BLOCK = (
    '  <div class="ag-sub">\n'
    '    <div class="ag-sub-txt">\n'
    '      <span class="ag-sub-kick">Le plus simple</span>\n'
    '      <h3>Recevez toutes les dates du Nid dans votre agenda</h3>\n'
    '      <ul>\n'
    '        <li>Toutes les dates du Nid apparaissent directement dans votre agenda personnel.</li>\n'
    '        <li>Les nouvelles dates et les changements d’horaire s’y ajoutent tout seuls : '
    'vous n’avez plus besoin de revenir sur le site.</li>\n'
    '        <li>Vous réglez vos rappels une seule fois — une semaine, un jour et 2 h avant — '
    'et ils s’appliquent à toutes les dates.</li>\n'
    '        <li>Vous pouvez vous désabonner quand vous le souhaitez.</li>\n'
    '      </ul>\n'
    '    </div>\n'
    '    <div class="ag-sub-act">\n'
    f'      <a class="btn ag-sub-btn" href="{CAL_SUB}" target="_blank" rel="noopener">'
    'S’abonner avec Google Agenda</a>\n'
    f'      <a class="ag-sub-alt" href="{CAL_WEBCAL}">Apple Calendrier, Outlook ou autre</a>\n'
    '      <span class="ag-sub-note">Gratuit, sans inscription.</span>\n'
    '    </div>\n'
    '  </div>')


def build():
    # regroupement par mois, dans l'ordre chronologique
    groupes = []
    for iso, h1, h2, typ, titre, note in EVENTS:
        d = dt.date.fromisoformat(iso)
        cle = (d.year, d.month)
        if not groupes or groupes[-1][0] != cle:
            groupes.append((cle, []))
        # on garde iso : c'est la cle (avec l'heure) de la surcharge de billetterie
        groupes[-1][1].append((iso, d, h1, h2, typ, titre, note))

    # legende
    leg = ''.join(
        f'<span class="ag-leg"><i style="background:{c}"></i>{lab}</span>'
        for lab, c, _u, _t in TYPES.values())

    # --- barre de filtres (masquee sans JS : tout reste visible) ---
    types_presents = [t for t in TYPES if any(e[3] == t for e in EVENTS)]
    f_types = ''.join(
        f'<button class="ag-f" type="button" data-f="type" data-v="{t}" '
        f'style="--c:{TYPES[t][1]}">{TYPES[t][0]}</button>'
        for t in types_presents)
    f_mois = ''.join(
        f'<button class="ag-f" type="button" data-f="mois" data-v="{an:04d}-{mo:02d}">'
        f'{MOIS[mo-1]}</button>'
        for (an, mo), _evs in groupes)

    out = ['<section class="agenda" id="agenda"><div class="wrap">',
           '  <span class="ag-anchor" id="concerts"></span>',
           '  <div class="kick">L’agenda</div>',
           '  <h2 class="sec-title">Les prochaines dates</h2>',
           '  <p class="lead">Rendez-vous mensuels, concerts, ateliers et workshops — au Nid, 29 rue des Orteaux, Paris 20<sup>e</sup>.</p>',
           SUB_BLOCK,
           f'  <div class="ag-legend">{leg}</div>',
           '  <div class="ag-filters" aria-label="Filtrer l’agenda">',
           '    <div class="ag-frow"><span class="ag-flab">Type</span>'
           '<button class="ag-f is-on" type="button" data-f="type" data-v="">Tous</button>'
           + f_types + '</div>',
           '    <div class="ag-frow"><span class="ag-flab">Mois</span>'
           '<button class="ag-f is-on" type="button" data-f="mois" data-v="">Tous</button>'
           + f_mois + '</div>',
           '    <p class="ag-fnone" hidden>Aucune date ne correspond à ces filtres. '
           '<button class="ag-freset" type="button">Tout afficher</button></p>',
           '  </div>']

    for (an, mois), evs in groupes:
        out.append(f'  <div class="ag-group" data-mois="{an:04d}-{mois:02d}">')
        out.append(f'  <div class="ag-month">{MOIS[mois-1]} {an}</div>')
        out.append('  <div class="ag-list">')
        for iso, d, h1, h2, typ, titre, note in evs:
            lab, col = TYPES[typ][0], TYPES[typ][1]
            # lien de reservation : surcharge par evenement, sinon defaut du type
            url, btn = reservation(iso, h1, typ)
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
                    f' data-t="{esc_attr(titre)}" data-d="{esc_attr(desc)}"'
                    f' data-typ="{typ}" data-mois="{d.year:04d}-{d.month:02d}"')
            note_html = f'<span class="ag-note">{note}</span>' if note else ''
            g = esc_attr(gcal_url(titre, utc(h1), utc(h2), typ, url))
            out.append(
                f'    <div class="ag-item" style="--c:{col}"{data}>'
                f'<div class="ag-date"><span class="ag-d">{d.day}</span>'
                f'<span class="ag-j">{jour[:3]}.</span></div>'
                f'<div class="ag-body"><span class="ag-type">{lab}</span>'
                f'<h3>{titre}</h3>{note_html}</div>'
                f'<div class="ag-hour">{h1}<span>→ {h2}</span></div>'
                f'<div class="ag-actions">'
                f'<a class="ag-btn" href="{url}"{ext}>{btn}</a>'
                f'<a class="ag-gcal" href="{g}" target="_blank" rel="noopener" '
                f'title="Ajouter cette date a mon Google Agenda">+ Google Agenda ↗</a>'
                f'<button class="ag-cal" type="button" title="Telecharger le fichier .ics (Apple, Outlook…) avec rappels">+ .ics</button>'
                f'</div></div>')
        out.append('  </div>')
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
        '    <a class="btn" href="mailto:contact@resonancesproductions.org?subject=Le%20Nid%20—%20réservation">Réserver une place</a>',
        '  </div>',
        '  <p class="ag-tip">« + Google Agenda » ajoute la date directement dans votre Google Agenda '
        '(pratique sur smartphone). « + .ics » télécharge un fichier compatible Apple Calendrier, '
        'Outlook et Google Agenda, avec trois rappels automatiques '
        '(une semaine, un jour et 2 h avant).</p>',
        '</div></section>', '']
    return '\n'.join(out)


CSS = """
/* ===== AGENDA DU NID ===== */
.agenda{background:linear-gradient(180deg,var(--night),#0b0c1e)}
.ag-legend{display:flex;flex-wrap:wrap;gap:10px 20px;margin-top:26px}
/* --- encart abonnement calendrier --- */
.ag-sub{display:grid;grid-template-columns:1fr auto;gap:22px 34px;align-items:center;margin-top:28px;
  background:linear-gradient(135deg,rgba(216,178,90,.10),rgba(255,255,255,.03));
  border:1px solid rgba(216,178,90,.34);border-radius:16px;padding:24px 28px}
.ag-sub-kick{display:block;color:var(--gold);font-size:13px;letter-spacing:.16em;
  text-transform:uppercase;font-weight:600}
.ag-sub h3{margin:7px 0 12px;font-family:'Cormorant Garamond',Georgia,serif;font-size:25px;
  color:#fff;font-weight:600;line-height:1.25}
.ag-sub ul{list-style:none;margin:0;padding:0;display:grid;gap:7px}
.ag-sub li{position:relative;padding-left:18px;color:#d3d0e8;font-size:14.5px;line-height:1.55}
.ag-sub li::before{content:'';position:absolute;left:0;top:.6em;width:6px;height:6px;
  border-radius:50%;background:var(--gold)}
.ag-sub-act{display:flex;flex-direction:column;align-items:stretch;gap:10px;text-align:center;min-width:212px}
.ag-sub-btn{white-space:nowrap}
.ag-sub-alt{color:var(--gold2);font-size:16px;text-decoration:underline;text-underline-offset:4px;
  display:inline-flex;align-items:center;justify-content:center;min-height:44px}
.ag-sub-note{color:var(--muted);font-size:14px}
@media(max-width:760px){
  .ag-sub{grid-template-columns:1fr;padding:20px 18px;gap:18px}
  .ag-sub h3{font-size:22px}
  .ag-sub-act{min-width:0}
  .ag-sub-btn{padding:14px 18px;white-space:normal}
}
.ag-leg{display:inline-flex;align-items:center;gap:8px;color:var(--muted);font-size:14px}
.ag-leg i{width:9px;height:9px;border-radius:50%;display:inline-block;flex:0 0 auto}
.ag-month{margin-top:40px;margin-bottom:16px;color:var(--gold);font-family:'Cormorant Garamond',Georgia,serif;
  font-size:31px;font-weight:600;text-transform:capitalize;border-bottom:1px solid var(--line);padding-bottom:10px}
.ag-list{display:grid;gap:10px}
.ag-anchor{display:block;height:0;scroll-margin-top:90px}
/* --- filtres : masques sans JS (tout reste visible), affiches par .ag-js --- */
.ag-filters{display:none;flex-direction:column;gap:10px;margin-top:22px}
.agenda.ag-js .ag-filters{display:flex}
.ag-frow{display:flex;flex-wrap:wrap;align-items:center;gap:10px}
.ag-flab{color:var(--gold);font-size:14px;letter-spacing:.16em;text-transform:uppercase;
  font-weight:600;margin-right:4px;min-width:44px}
.ag-f{border:1px solid rgba(255,255,255,.16);background:rgba(255,255,255,.04);color:#d3d0e8;
  border-radius:24px;padding:9px 18px;min-height:44px;font-size:15px;cursor:pointer;font-family:inherit;
  display:inline-flex;align-items:center;
  text-transform:capitalize;transition:background .2s,color .2s,border-color .2s}
.ag-f:hover{border-color:var(--c,var(--gold));color:#fff}
.ag-f.is-on{background:var(--c,var(--gold));border-color:var(--c,var(--gold));color:#12121f;font-weight:600}
.ag-fnone{color:var(--muted);font-size:15px;font-style:italic;margin:6px 0 0}
.ag-freset{background:none;border:none;color:var(--gold2,var(--gold));font:inherit;font-size:16px;
  text-decoration:underline;text-underline-offset:3px;cursor:pointer;padding:0 2px;
  display:inline-flex;align-items:center;min-height:44px}
.ag-item[hidden],.ag-group[hidden]{display:none}
.ag-actions{display:flex;flex-wrap:wrap;align-items:center;gap:8px;justify-content:flex-end}
.ag-gcal{display:inline-flex;align-items:center;justify-content:center;min-height:44px;
  border:1px solid rgba(255,255,255,.20);background:rgba(255,255,255,.05);
  color:#e6e3f5;border-radius:24px;padding:9px 17px;font-size:16px;text-decoration:none;
  white-space:nowrap;transition:background .2s,color .2s,border-color .2s}
.ag-gcal:hover{background:var(--gold);color:#1a1608;border-color:var(--gold)}
.ag-item{display:grid;grid-template-columns:82px minmax(0,1fr) auto auto;align-items:center;gap:16px;
  background:var(--card);border:1px solid rgba(255,255,255,.07);border-left:3px solid var(--c);
  border-radius:12px;padding:14px 20px;transition:transform .2s,border-color .2s}
.ag-item:hover{transform:translateX(3px);border-color:var(--line);border-left-color:var(--c)}
.ag-date{text-align:center;line-height:1}
.ag-d{display:block;font-family:'Cormorant Garamond',Georgia,serif;font-size:40px;color:#fff;font-weight:600}
.ag-j{display:block;font-size:15px;color:var(--muted);text-transform:uppercase;letter-spacing:.10em;margin-top:5px}
.ag-body h3{font-size:19px;color:#fff;font-weight:600;margin:3px 0 0;font-family:'Cormorant Garamond',Georgia,serif}
.ag-type{font-size:14px;letter-spacing:.16em;text-transform:uppercase;color:var(--c);font-weight:600}
.ag-note{display:block;color:var(--muted);font-size:13.5px;font-style:italic;margin-top:2px}
.ag-hour{text-align:right;color:#d3d0e8;font-size:16px;white-space:nowrap}
.ag-hour span{display:block;color:var(--muted);font-size:14px}
.ag-btn{display:inline-flex;align-items:center;justify-content:center;min-height:44px;
  border:1px solid var(--c);background:rgba(255,255,255,.05);color:var(--c);border-radius:24px;
  padding:9px 20px;font-size:16px;font-weight:500;text-decoration:none;white-space:nowrap;
  transition:background .2s,color .2s}
.ag-btn:hover{background:var(--c);color:#12121f}
.ag-foot{display:flex;flex-wrap:wrap;gap:14px;margin-top:38px}
.ag-tip{color:var(--muted);font-size:15px;margin-top:16px;font-style:italic}
.ag-cal{display:inline-flex;align-items:center;justify-content:center;min-height:44px;
  border:1px solid rgba(255,255,255,.20);background:rgba(255,255,255,.05);color:#e6e3f5;
  border-radius:24px;padding:9px 17px;font-size:16px;cursor:pointer;white-space:nowrap;
  font-family:inherit;transition:background .2s,color .2s,border-color .2s}
.ag-cal:hover{background:var(--gold);color:#1a1608;border-color:var(--gold)}
.ag-access{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px;margin-top:40px}
.ag-access>div{background:var(--card);border:1px solid rgba(255,255,255,.07);border-radius:14px;
  padding:20px 22px;color:#d3d0e8;font-size:14.5px;line-height:1.6}
.ag-access span{display:block;color:var(--gold);font-size:13px;letter-spacing:.16em;
  text-transform:uppercase;font-weight:600;margin-bottom:8px}
.ag-access i{color:var(--muted);font-size:13px}
/* --- largeurs intermediaires (<=1000 px) : les actions passent sur leur propre
   ligne pour laisser respirer le titre (sinon la colonne du titre se tasse a
   ~200 px et chaque intitule casse sur 3 lignes). On empile, on ne rapetissit pas. --- */
@media(max-width:1000px){
  .ag-item{grid-template-columns:82px minmax(0,1fr) auto}
  .ag-actions{grid-column:1/-1;justify-self:stretch;justify-content:flex-start;margin-top:10px}
}
@media(max-width:640px){
  .ag-item{grid-template-columns:66px 1fr;gap:8px 14px;padding:15px 16px}
  .ag-cal{grid-column:2;justify-self:start}
  .ag-hour{grid-column:2;text-align:left;margin-top:2px;font-size:16px}
  .ag-hour span{display:inline;margin-left:4px}
  .ag-btn{grid-column:2;justify-self:start;margin-top:6px}
  .ag-actions{grid-column:1/-1;justify-self:stretch;justify-content:flex-start;margin-top:10px;gap:8px 8px}
  .ag-actions .ag-btn,.ag-actions .ag-cal{grid-column:auto;margin-top:0}
  .ag-flab{min-width:100%}
  .ag-d{font-size:34px}
  .ag-month{font-size:27px}
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
        'BEGIN:VALARM','TRIGGER:-P1W','ACTION:DISPLAY','DESCRIPTION:'+esc(it.t)+' dans une semaine','END:VALARM',
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
      b.textContent='\\u2713 Ajoute'; setTimeout(function(){b.textContent='+ .ics';},2500);
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


FILTER_JS = """
<script>
/* Filtres de l'agenda du Nid : par type et par mois. Vanilla, sans dependance.
   Sans JS la barre reste masquee (CSS) et toutes les dates sont visibles. */
(function(){
  var sec=document.querySelector('.agenda'); if(!sec) return;
  var bar=sec.querySelector('.ag-filters'); if(!bar) return;
  sec.classList.add('ag-js');
  var items=[].slice.call(sec.querySelectorAll('.ag-item'));
  var groups=[].slice.call(sec.querySelectorAll('.ag-group'));
  var none=sec.querySelector('.ag-fnone');
  var state={type:'',mois:''};

  function apply(){
    var n=0;
    items.forEach(function(it){
      var ok=(!state.type||it.dataset.typ===state.type)&&(!state.mois||it.dataset.mois===state.mois);
      it.hidden=!ok; if(ok) n++;
    });
    groups.forEach(function(g){
      g.hidden=!g.querySelector('.ag-item:not([hidden])');
    });
    [].forEach.call(bar.querySelectorAll('.ag-f'),function(b){
      var on=state[b.dataset.f]===b.dataset.v;
      b.classList.toggle('is-on',on);
      b.setAttribute('aria-pressed',on?'true':'false');
    });
    if(none) none.hidden=(n>0);
  }

  bar.addEventListener('click',function(e){
    var r=e.target.closest('.ag-freset');
    if(r){ state.type=''; state.mois=''; apply(); return; }
    var b=e.target.closest('.ag-f'); if(!b) return;
    state[b.dataset.f]=b.dataset.v; apply();
  });

  /* ancre #concerts : pre-active le filtre "toutes les dates de concerts" */
  function go(){ var a=document.getElementById('concerts'); if(a) a.scrollIntoView(); }
  function fromHash(){
    if(location.hash==='#concerts'){
      state.type='concert'; state.mois=''; apply(); go();
      if(document.readyState!=='complete'){ window.addEventListener('load',go,{once:true}); }
    }
  }
  window.addEventListener('hashchange',fromHash);
  apply(); fromHash();
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
    # ... et des blocs injectes dans les cartes du programme.
    # Sans ce nettoyage, chaque nouvelle execution du script REAJOUTE la carte
    # Showcase et les encarts « Prochaines dates » (ils ne sont pas idempotents),
    # d'ou les cartes dupliquees observees sur la page.
    html = re.sub(r'[ \t]*<div class="offer-dates"><span>Prochaines dates</span>.*?</div>\n?',
                  '', html, flags=re.S)
    html = re.sub(r'[ \t]*<div class="offer offer--rare">.*?\n[ \t]*</div>\n',
                  '', html, flags=re.S)
    # ancienne version de la meme carte (avant le renommage « Showcase / Scene ouverte »)
    html = re.sub(r'[ \t]*<div class="offer">\s*<div class="t">Scène ouverte</div>.*?\n[ \t]*</div>\n',
                  '', html, flags=re.S)
    # /!\ NE PAS toucher a <section class="figs"> (blocs photo des propositions :
    # rendez-vous mensuels, atelier de yoga, workshop calebasse) ni a son CSS
    # « ===== BLOCS ILLUSTRES DES PROPOSITIONS ===== ». Ils sont ecrits a la main
    # dans la page et volontairement places AVANT le bloc « ===== AGENDA DU NID ===== »
    # pour echapper au nettoyage CSS ci-dessus.

    # CSS
    html = html.replace('</style>', CSS + '</style>', 1)

    # section : juste apres le programme, avant le divider qui precede "Le lieu"
    anchor = '<div class="divider"></div>\n\n<section class="lieu">'
    assert anchor in html, 'ancre lieu introuvable'
    html = html.replace(anchor, '<div class="divider"></div>\n\n' + build() + '\n<div class="divider"></div>\n\n<section class="lieu">', 1)

    # lien dans la nav + remplacement de la note "calendrier en cours"
    # /!\ ce script est relance sur la page deja generee : sans ce garde-fou,
    # chaque execution rajoutait une entree "Agenda" dans le menu (4 a l'arrivee).
    if 'href="#agenda">Agenda</a>' not in html:
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

    # Chaque ancre est prise DANS la carte concernee (fin de son texte + ligne
    # « Avec … »), jamais sur l'ouverture de la carte SUIVANTE comme avant : un
    # marqueur du type `<div class="offer">\n      <div class="t">…` casse des qu'on
    # ajoute quoi que ce soit en tete de carte (photo, badge…). Ancres locales =
    # une carte peut evoluer sans casser l'injection des dates d'une autre.
    for ancre, typ in (
        ('au plus près du public.</p>\n      <div class="who">Avec David Lesage</div>', 'concert'),
        ('retrouver de l’espace intérieur.</p>\n      <div class="who">Avec Iris Chasles</div>', 'yoga'),
        ('on entre dans le rythme par le corps et l’écoute.</p>\n      <div class="who">Avec David Lesage</div>', 'rythme'),
    ):
        if ancre in html:
            html = html.replace(ancre, ancre + dates_courtes(typ), 1)
        else:
            print('ATTENTION : ancre « prochaines dates » introuvable pour', typ)

    # carte « Présentation, découverte & essai d'instruments d'exception »
    # (anciennement « Scène ouverte / Showcase »). Le lien de reservation vient
    # de la SEULE constante SHOWROOM ci-dessus : un seul endroit a changer.
    carte_showcase = ('''    <div class="offer offer--rare">
      <div class="t">Présentation, découverte &amp; essai</div>
      <h3>Instruments d’exception</h3>
      <div class="offer-meta">Gratuit · sur inscription · environ 2 h</div>
      <p>Une occasion rare de rencontrer des instruments que l’on ne croise presque jamais : le <b>Neotone</b>, handpan électronique de facture professionnelle, des <b>handpans acoustiques Yishama</b>, la <b>calebasse</b>, le <b>Gonilélé</b> (petite harpe africaine), et des <b>micros conçus pour le handpan</b> — micro de contact anti-larsen et micro multifonction pour le studio et la scène.</p>
      <p>Ce sont des instruments <b>faits main, produits en très petites séries</b>, dont la valeur atteint plusieurs milliers d’euros. David Lesage les présente et les fait sonner devant vous — le son brut, puis les effets et la voix, l’application <b>Handpan Studio</b> projetée à l’écran — répond à toutes les questions, puis met les instruments entre vos mains.</p>
      <p>Aucune expérience requise : la plupart des personnes présentes n’ont jamais tenu un handpan. Jauge limitée, inscription préalable nécessaire.</p>
      ''' + dates_courtes('showcase') + '''
      <div class="who">Réservation en ligne : <a href="''' + SHOWROOM + '''" target="_blank" rel="noopener">réserver ma place ↗</a></div>
      <p class="offer-fine"><b>En toute transparence.</b> Ces présentations sont gratuites et sans obligation d’achat. L’association accueille et valorise ces rencontres, animées par David Lesage ; <b>elle ne vend pas les instruments présentés</b> et peut percevoir une contribution d’affiliation lorsqu’une personne décide d’acquérir un instrument auprès du fabricant. Les seuls objets vendus par l’association sont les <b>calebasses pyrogravées</b>, façonnées dans son atelier.</p>
    </div>
''')
    anc = '  </div>\n\n  <div class="note">'
    if anc in html:
        html = html.replace(anc, carte_showcase + anc, 1)

    CSS_DATES = ('''
.offer-dates{margin-top:14px;padding-top:12px;border-top:1px solid rgba(255,255,255,.08);color:#d3d0e8;font-size:16px}
.offer-dates span{display:block;color:var(--gold);font-size:14px;letter-spacing:.16em;text-transform:uppercase;font-weight:600;margin-bottom:5px}
.offer-dates a{color:var(--gold2);font-size:16px;font-weight:500;text-decoration:underline;text-underline-offset:4px;
  display:inline-flex;align-items:center;min-height:44px}
/* carte « instruments d'exception » : pleine largeur, registre premium */
.offer--rare{grid-column:1/-1;background:linear-gradient(135deg,rgba(216,178,90,.10),rgba(255,255,255,.03));
  border-color:rgba(216,178,90,.34)}
.offer--rare h3{margin-bottom:6px}
.offer--rare .offer-meta{color:var(--gold2);font-size:14px;font-style:italic;margin:0 0 14px}
.offer--rare p{max-width:78ch}
.offer--rare p+p{margin-top:12px}
.offer--rare b{color:#efeaf6;font-weight:600}
.offer-fine{margin-top:18px;padding-top:14px;border-top:1px solid rgba(255,255,255,.10);
  color:var(--muted);font-size:13px;line-height:1.65;max-width:78ch}
.offer-fine b{color:var(--gold2);font-weight:600}
''')
    html = html.replace('</style>', CSS_DATES + '</style>', 1)
    if 'ag-cal' in html and 'BEGIN:VCALENDAR' not in html:
        html = html.replace('</body>', ICS_JS + '</body>', 1)
    if 'ag-filters' in html and 'ag-freset' not in html.split('<script>')[-1]:
        html = html.replace('</body>', FILTER_JS + '</body>', 1)

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
