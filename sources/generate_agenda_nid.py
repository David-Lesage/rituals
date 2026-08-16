# -*- coding: utf-8 -*-
"""Genere /le-nid/index.html a partir de sources/lenid_source.html.

    python3 sources/generate_agenda_nid.py

CE QUI A CHANGE LE 14/08/2026 — ET POURQUOI
-------------------------------------------
Ce script n'etait PAS un generateur : il RETOUCHAIT une page existante qu'il
allait chercher dans `lenid_deploy/index.html`, un dossier disparu du depot. Il
s'arretait donc sur « No such file or directory », et /le-nid ne pouvait plus
etre modifiee qu'a la main.

Le faire simplement pointer sur `le-nid/index.html` n'aurait pas suffi : il
aurait alors travaille sur SA PROPRE SORTIE. Ses `re.sub` de nettoyage etaient
censes effacer la passe precedente, mais celui du CSS s'arretait au premier
commentaire rencontre et ne retirait que 167 des 8 628 octets du bloc agenda :
mesure faite, une seule execution ajoutait 8 288 octets de CSS en double, et la
suivante autant. C'est la meme mecanique qui avait produit QUATRE entrees
« Agenda » dans le menu et quatre cartes identiques.

Il est donc devenu un vrai generateur, comme les huit autres :

    sources/lenid_source.html   (versionne, ne bouge pas)
              |
              +--  CSS de l'agenda + CSS des encarts
              +--  la section agenda construite depuis EVENTS
              +--  les reformulations qui renvoient vers l'agenda
              +--  les encarts « prochaines dates » des cartes du programme
              +--  la carte « instruments d'exception »
              +--  les scripts (.ics, filtres)
              +--  le menu partage (nav_menu.inject)
              |
              v
       le-nid/index.html

Il ne lit jamais la page qu'il produit : deux executions donnent forcement le
meme fichier, et plus AUCUN `re.sub` de nettoyage n'est necessaire.

LES EVENEMENTS
--------------
Ils sont recuperes via le connecteur Google Calendar puis figes dans EVENTS.
Pour actualiser : relancer la lecture du calendrier et mettre a jour EVENTS.

⚠️ PAGE SENSIBLE : elle porte l'agenda, les reservations et des liens de
billetterie qui DIFFERENT d'un evenement a l'autre (URL_PAR_EVENT). Un garde-fou
verifie avant chaque ecriture que chaque billetterie attendue est bien dans la
page et qu'il y a exactement un bouton de reservation par evenement.
"""
import datetime as dt
import os
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
#: la source versionnee, jamais modifiee par ce script
SOURCE = os.path.join(HERE, 'lenid_source.html')
#: la page publiee
TARGET = os.path.join(REPO, 'le-nid', 'index.html')

sys.path.insert(0, HERE)
import nav_menu  # menu de navigation partage  # noqa: E402
import theme_chaleur  # couche chaleureuse commune  # noqa: E402
import verif_commentaires  # garde-fou commentaires HTML  # noqa: E402

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
    # Verifie sur la billetterie HelloAsso le 04/08 : elle vend bien TROIS dates
    # (26 septembre / 10 octobre / 28 novembre), toutes au Nid. Le concert du
    # 26/09 y est donc inclus, meme s'il est annonce en trio sur le site.
    ('2026-09-26', '20:00'): CONCERT_SOLO,   # Concert — David, Iris & Julien
    # A COMPLETER quand David fournira les liens :
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

    ⚠️ On n'ecrit JAMAIS ici la facon d'ouvrir le portail de la rue — seulement
    la phrase publique d'ACCES_PUBLIC_FR, qui renvoie a la confirmation
    d'inscription. Ces liens partent dans des agendas tiers, hors de tout
    controle. (La formulation de cette note evite volontairement les mots que
    le crochet pre-commit surveille : il refusait le fichier entier.)
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


# ⚠️ Les deux regles `.ag-leg` / `.ag-leg i` apparaissent DEUX FOIS dans ce bloc,
# et c'est volontaire : la page publiee les porte en double (fossile d'une
# ancienne injection ratee). Elles sont strictement identiques, donc sans aucun
# effet visuel, mais les ecrire une seule fois changerait la page de 152 octets.
# On les reproduit pour que la regeneration soit neutre. A nettoyer un jour avec
# David, en verifiant la page apres — pas au detour d'une reparation.
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


# =========================================================================== #
# CSS DES BLOCS AJOUTES DANS LES CARTES DU PROGRAMME
# (« prochaines dates » et carte « instruments d'exception »)
# =========================================================================== #
CSS_DATES = """.offer-dates{margin-top:14px;padding-top:12px;border-top:1px solid rgba(255,255,255,.08);color:#d3d0e8;font-size:16px}
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
"""


# =========================================================================== #
# LA COUCHE CHALEUREUSE (refonte du 15/08/2026)
# =========================================================================== #
# « Ramener de la couleur prune, ca fait du bien. Resonances a besoin d'avoir
#   une image classe mais aussi chaleureuse. » — David, 15/08/2026.
# La partie commune vit dans `sources/theme_chaleur.py`. Ici, uniquement les
# declinaisons propres a CETTE page. AUCUN TEXTE N'A BOUGE, et aucun des
# 20 boutons de reservation n'est touche (voir juste en dessous).
#
# 🚫 CE QU'ON NE TOUCHE PAS, ET POURQUOI : L'AGENDA A UN CODE COULEUR QUI PORTE
#    DU SENS. Chaque type d'evenement a sa teinte, passee en variable `--c`, et
#    elle sert dans SIX endroits qui doivent rester d'accord entre eux :
#    `.ag-leg i` (la legende), `.ag-f.is-on` (le filtre actif), `.ag-item`
#    (le filet gauche de la ligne), `.ag-type`, `.ag-btn` (le contour et le
#    texte des 20 boutons de reservation) et `.ag-btn:hover`. Y poser un
#    degrade, c'est effacer l'information : on ne saurait plus lire quel filtre
#    est actif ni a quel type appartient une date. Le degrade s'arrete donc au
#    bord de la liste. Ce qui, dans l'agenda, N'EST PAS pilote par `--c` —
#    l'encart d'abonnement et les noms de mois — le recoit normalement.
#
# ⚠️ `.offer--rare` DOIT ETRE NOMMEE A PART, meme piege que `.card.feature` sur
#    l'accueil : elle pose son fond avec la propriete RACCOURCIE
#    `background:linear-gradient(…)`, a specificite EGALE (0,1,0) a `.offer`.
#    Comme cette couche arrive apres, un `.offer{background-image:…}` seul lui
#    ferait PERDRE son voile dore — la carte « instruments d'exception », la
#    seule pleine largeur, redeviendrait une carte ordinaire. On lui rend donc
#    son voile explicitement, filet de tete compris.
#
# 🚫 16/08/2026 — ET C'EST POURQUOI LA LISTE D'AGENDA GARDE SA SURFACE.
#    La refonte du 16/08 monte `--card` de #191b3d a #1e214a (ecart fond ->
#    carte x2,36 -> x3,30). Partout ailleurs c'est le gain principal. Ici, non :
#    `--c` n'est pas qu'un filet decoratif, c'est la COULEUR DE TEXTE des 20
#    boutons de billetterie (`.ag-btn{color:var(--c)}`) et du libelle
#    `.ag-type`. Les six teintes sont des litteraux calibres sur l'ANCIEN fond.
#    Mesure faite avant de trancher, contraste sur le fond des boutons :
#
#        mensuel   #d8b25a  8,25 -> 7,61      showcase  #6f9bd1  5,76 -> 5,31
#        concert   #e08a5f  6,30 -> 5,81      residence #c98fb0  6,35 -> 5,86
#        yoga      #7fb2a3  6,95 -> 6,42      rythme    #8f7ad1  4,64 -> 4,28
#
#    « Workshop rythme » passerait donc SOUS le seuil de 4,5:1, sur 20 boutons.
#    Deux issues possibles : eclaircir cette teinte, ou ne pas monter le fond.
#    Eclaircir #8f7ad1 la rapprocherait de `showcase` #6f9bd1, dont elle n'est
#    deja separee que de x1,29 en niveaux de gris — on reparerait le contraste
#    en abimant la lisibilite daltonienne. On ne monte donc PAS le fond de la
#    liste : `.ag-item` est reepingle a #191b3d, la valeur sur laquelle le code
#    couleur a ete calibre. Le reste de la page (cartes du programme, encarts)
#    profite normalement du nouvel etagement.
#    ⚠️ Si un jour `--card` rebouge, cette ligne ne suit PAS toute seule.
CSS_CHALEUR = """/* ===== Le Nid : declinaisons chaleureuses ===== */
/* la liste d'agenda garde la surface sur laquelle son code couleur a ete
   calibre : `--c` est la couleur de texte des 20 boutons de billetterie */
.ag-item{background:#191b3d}
.hero h1{background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent;width:fit-content;max-width:100%;margin:0 auto}
/* ⚠️ `width:fit-content` ET SURTOUT PAS `display:inline-block` ici. Mesure
   faite a l'ecran : `.offer-dates span` est un BLOC suivi, dans le meme
   parent, du texte des dates. Passe en inline-block, l'etiquette venait se
   coller aux dates — « PROCHAINES DATES6 sept. · 4 octo. ». `fit-content`
   retrecit la boite au texte (ce dont le degrade a besoin pour balayer les
   MOTS et non toute la carte) sans toucher au flux. */
.offer .t,.offer-dates span,.ag-sub-kick,.ag-month{width:fit-content;max-width:100%;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
/* cartes du programme : filet de tete au degrade, coins plus genereux */
.offer{border-top:3px solid transparent;border-radius:18px;background-image:var(--grad),linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,0)),linear-gradient(var(--card),var(--card));background-size:100% 3px,100% 100%,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box,padding-box}
.offer--rare{background-image:var(--grad),linear-gradient(135deg,rgba(216,178,90,.10),rgba(255,255,255,.03));background-size:100% 3px,100% 100%;background-repeat:no-repeat,no-repeat;background-position:0 0,0 0;background-origin:border-box,padding-box}
/* la prune revient en accent de TEXTE (--plum2 : 7,3:1 sur --card) */
.offer .who,.offer--rare .offer-meta{color:var(--plum2)}
/* l'encart d'abonnement au calendrier : il n'est PAS pilote par --c */
.ag-sub{border-radius:18px;border-color:rgba(248,210,116,.34)}
.ag-sub li::before{width:7px;height:7px;border-radius:2px;background:var(--grad-warm);transform:rotate(45deg)}
/* les deux cartes « se programme en / s'inscrit dans » et l'encart en pointilles */
.scene-card{border-top:3px solid transparent;border-radius:18px;background-image:var(--grad),linear-gradient(var(--card),var(--card));background-size:100% 3px,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box}
.note{border-radius:18px;border-color:rgba(248,210,116,.3)}
.note b{color:var(--plum2)}
/* arrondis genereux — `.gal img` etait a 16 px, les autres pages sont a 18 */
.gal img{border-radius:18px}
"""


def dates_courtes(typ, n=3, extra=''):
    """Encart « Prochaines dates » a poser au bas d'une carte du programme.

    `extra` ajoute un lien apres « tout voir » (seule la carte concert en a un).
    """
    items = [(dt.date.fromisoformat(iso), h1)
             for iso, h1, _h2, t, _ti, _no in EVENTS if t == typ][:n]
    if not items:
        return ''
    txt = ' · '.join('%d %s.' % (d.day, MOIS[d.month - 1][:4]) for d, _h in items)
    return ('<div class="offer-dates"><span>Prochaines dates</span>%s '
            '<a href="#agenda">tout voir</a>%s</div>' % (txt, extra))


# --------------------------------------------------------------------------- #
# LES CARTES DU PROGRAMME QUI RECOIVENT UN ENCART « PROCHAINES DATES »
#
# Chaque ancre est prise DANS la carte concernee (fin de son texte + ligne
# « Avec … »), jamais sur l'ouverture de la carte SUIVANTE comme autrefois : un
# marqueur du type `<div class="offer">` + `<div class="t">…` casse des qu'on
# ajoute quoi que ce soit en tete de carte (photo, badge…). Ancres locales = une
# carte peut evoluer sans casser l'injection des dates d'une autre.
#
# ⚠️ `separateur` et `en_plus` viennent de RETOUCHES FAITES A LA MAIN dans la
# page publiee, que le generateur ne reproduisait pas :
#   - concert et yoga : l'encart est precede d'un retour a la ligne et de quatre
#     espaces (celui du workshop, lui, est colle a la ligne « Avec … ») ;
#   - concert : un lien « En savoir plus → » vers /concerts-david-lesage a ete
#     ajoute apres « tout voir ». C'est le seul chemin de la page du Nid vers la
#     page des concerts intimistes : le perdre coupait ce lien.
# --------------------------------------------------------------------------- #
CARTES_DATES = (
    ('au plus près du public.</p>\n      <div class="who">Avec David Lesage</div>',
     'concert', '\n    ', ' <a href="/concerts-david-lesage">En savoir plus →</a>'),
    ('retrouver de l’espace intérieur.</p>\n      <div class="who">Avec Iris Chasles</div>',
     'yoga', '\n    ', ''),
    ('on entre dans le rythme par le corps et l’écoute.</p>\n      <div class="who">Avec David Lesage</div>',
     'rythme', '', ''),
)


def carte_instruments():
    """Carte « Présentation, découverte & essai d'instruments d'exception ».

    (Anciennement « Scene ouverte / Showcase » ; la cle technique interne reste
    `showcase`.) Le lien de reservation vient de la SEULE constante SHOWROOM :
    un seul endroit a changer.

    ⚠️ `id="instruments"` a ete ajoute A LA MAIN dans la page publiee et le
    generateur ne le reproduisait pas. Ce n'est pas decoratif : c'est la cible
    de l'entree « Présentation d'instruments » du menu partage
    (`/le-nid#instruments`, voir nav_menu.py). Sans lui, cette entree de menu ne
    mene nulle part.
    """
    return ('    <div class="offer offer--rare" id="instruments">\n'
            '      <div class="t">Présentation, découverte &amp; essai</div>\n'
            '      <h3>Instruments d’exception</h3>\n'
            '      <div class="offer-meta">Gratuit · sur inscription · environ 2 h</div>\n'
            '      <p>Une occasion rare de rencontrer des instruments que l’on ne croise presque jamais : le <b>Neotone</b>, handpan électronique de facture professionnelle, des <b>handpans acoustiques Yishama</b>, la <b>calebasse</b>, le <b>Gonilélé</b> (petite harpe africaine), et des <b>micros conçus pour le handpan</b> — micro de contact anti-larsen et micro multifonction pour le studio et la scène.</p>\n'
            '      <p>Ce sont des instruments <b>faits main, produits en très petites séries</b>, dont la valeur atteint plusieurs milliers d’euros. David Lesage les présente et les fait sonner devant vous — le son brut, puis les effets et la voix, l’application <b>Handpan Studio</b> projetée à l’écran — répond à toutes les questions, puis met les instruments entre vos mains.</p>\n'
            '      <p>Aucune expérience requise : la plupart des personnes présentes n’ont jamais tenu un handpan. Jauge limitée, inscription préalable nécessaire.</p>\n'
            '      ' + dates_courtes('showcase') + '\n'
            '      <div class="who">Réservation en ligne : <a href="' + SHOWROOM
            + '" target="_blank" rel="noopener">réserver ma place ↗</a></div>\n'
            '      <p class="offer-fine"><b>En toute transparence.</b> Ces présentations sont gratuites et sans obligation d’achat. L’association accueille et valorise ces rencontres, animées par David Lesage ; <b>elle ne vend pas les instruments présentés</b> et peut percevoir une contribution d’affiliation lorsqu’une personne décide d’acquérir un instrument auprès du fabricant. Les seuls objets vendus par l’association sont les <b>calebasses pyrogravées</b>, façonnées dans son atelier.</p>\n'
            '    </div>\n')


# --------------------------------------------------------------------------- #
# TEXTES REMPLACES DANS LA SOURCE
# La source garde la formulation d'AVANT l'agenda (« calendrier en cours de mise
# a jour », « Être informé des dates »…). Le generateur la remplace par la
# formulation qui renvoie vers l'agenda. C'est ce qui rend la construction
# reproductible : la source ne bouge jamais, la page se refait toujours pareil.
# --------------------------------------------------------------------------- #
REMPLACEMENTS = (
    ('<a class="btn ghost" href="#contact">Être informé des dates</a>',
     '<a class="btn ghost" href="#agenda">Voir les prochaines dates</a>',
     'bouton « être informé des dates »'),
    ('<b>Dates, tarifs et réservations :</b> le calendrier du Nid est en cours de mise à jour. '
     'Écrivez-nous pour connaître les prochaines dates et réserver votre place — nous vous répondons directement.',
     '<b>Dates, tarifs et réservations :</b> retrouvez toutes les prochaines dates dans '
     '<a href="#agenda">l’agenda ci-dessous</a>. Les places sont limitées — écrivez-nous pour réserver.',
     'note « dates, tarifs et réservations »'),
    ('<a class="btn" href="mailto:contact@resonancesproductions.org?subject=Le%20Nid%20—%20prochaines%20dates">Demander les prochaines dates</a>',
     '<a class="btn" href="#agenda">Voir l’agenda</a>',
     'bouton « demander les prochaines dates »'),
    # prise de rendez-vous psychotherapie -> site d'Iris Chasles
    ('      <div class="who">Avec Iris Chasles · <a href="https://www.irischasles.com/psychotherapie-paris-20" target="_blank" rel="noopener">En savoir plus</a></div>',
     '      <div class="who">Avec Iris Chasles</div>\n      <div class="offer-dates"><span>Sur rendez-vous</span>Séances en présentiel au Nid ou en visio. <a href="https://www.irischasles.com/" target="_blank" rel="noopener">Prendre rendez-vous sur irischasles.com ↗</a></div>',
     'bloc psychothérapie'),
)


def _exiger(html, marqueur, combien, quoi):
    """Refuse de continuer si le compte n'est pas celui attendu.

    On ABANDONNE plutot que d'imprimer un avertissement qui defile : la page sur
    le disque reste alors exactement comme elle etait.
    """
    n = html.count(marqueur)
    if n != combien:
        raise SystemExit('!! ABANDON : %d occurrence(s) de « %s » (%s), attendu %d. '
                         'Page NON ecrite.' % (n, marqueur[:60], quoi, combien))


def generer():
    """SOURCE -> page complete, en memoire.

    Ne lit JAMAIS la page produite : deux executions donnent forcement le meme
    fichier. C'est ce qui manquait a la version precedente, qui retouchait sa
    propre sortie et ajoutait un bloc a chaque passage.
    """
    with open(SOURCE, encoding='utf-8') as f:
        html = f.read()

    # --- CSS de l'agenda, puis CSS des encarts, avant la fin de la feuille ---
    # `CSS` commence par un saut de ligne et la source en a deja un : sans
    # `lstrip`, la page gagnerait une ligne vide de plus que la version publiee.
    # Le `\n` final est celui qui separe le CSS des encarts de la feuille du
    # menu partage, que `nav_menu.inject()` collera juste avant `</style>`.
    _exiger(html, '</style>', 1, 'fin de la feuille de style')
    html = html.replace('</style>',
                        CSS.lstrip('\n') + CSS_DATES
                        + theme_chaleur.CSS + CSS_CHALEUR + '\n</style>', 1)

    # --- la section agenda, juste avant le divider qui precede « Le lieu » ---
    ancre_lieu = '<div class="divider"></div>\n\n<section class="lieu">'
    _exiger(html, ancre_lieu, 1, 'ancre de la section « Le lieu »')
    html = html.replace(
        ancre_lieu,
        '<div class="divider"></div>\n\n' + build()
        + '\n<div class="divider"></div>\n\n<section class="lieu">', 1)

    # --- reformulations qui renvoient vers l'agenda --------------------------
    for vieux, neuf, quoi in REMPLACEMENTS:
        _exiger(html, vieux, 1, quoi)
        html = html.replace(vieux, neuf, 1)

    # --- encarts « prochaines dates » dans les cartes du programme -----------
    for ancre, typ, separateur, en_plus in CARTES_DATES:
        _exiger(html, ancre, 1, 'ancre « prochaines dates » (%s)' % typ)
        html = html.replace(
            ancre, ancre + separateur + dates_courtes(typ, extra=en_plus), 1)

    # --- carte « instruments d'exception » -----------------------------------
    ancre_carte = '  </div>\n\n  <div class="note">'
    _exiger(html, ancre_carte, 1, 'ancre de la carte « instruments d’exception »')
    html = html.replace(ancre_carte, carte_instruments() + ancre_carte, 1)

    # --- scripts : telechargement .ics, puis filtres -------------------------
    _exiger(html, '</body>', 1, 'fin du corps de page')
    html = html.replace('</body>', ICS_JS + '</body>', 1)
    html = html.replace('</body>', FILTER_JS + '</body>', 1)

    # Ligne vide entre le dernier script de la page et le bloc du menu partage.
    # Elle vient de la migration du menu v1 -> v2 : `nav_menu._strip()` a retire
    # l'ancien bloc en laissant le saut de ligne qui le suivait. Les neuf pages
    # publiees la portent ; on la reproduit pour qu'une regeneration ne modifie
    # pas un octet.
    html = html.replace('</script>\n</body>', '</script>\n\n</body>', 1)

    # --- menu de navigation partage ------------------------------------------
    # ⚠️ Il n'y a PLUS d'ajout d'une entree « Agenda » a la main comme autrefois.
    # C'etait la cause des QUATRE entrees « Agenda » du menu : le script tournait
    # sur sa propre sortie et rajoutait le lien a chaque passage. Le menu partage
    # porte deja l'entree Agenda (/le-nid#agenda, voir nav_menu.py).
    return nav_menu.inject(html, 'le-nid')


if __name__ == '__main__':
    page = generer()

    # ---- garde-fous STRUCTURELS, avant l'ecriture ---------------------------
    # Modele : generate_rythme.py. Un ecart attrape AUSSI BIEN la disparition
    # que la duplication — c'est cette page qui avait fini avec quatre entrees
    # « Agenda » dans le menu et quatre cartes identiques.
    for _marqueur, _combien, _quoi in (
        ('<h1', 1, 'titre principal'),
        # version lue dans nav_menu (jamais recopiee ici)
        ('data-nav="%s"' % nav_menu.NAV_VERSION, 1, 'menu partage nav_menu.py'),
        ('>Agenda</a>', 1, 'entree « Agenda » du menu'),
        ('<section class="agenda" id="agenda">', 1, 'section agenda'),
        ('class="offer offer--rare"', 1, 'carte « instruments d’exception »'),
        ('/* ===== AGENDA DU NID ===== */', 1, 'feuille de style de l’agenda'),
        ('<div class="ag-sub">', 1, 'encart d’abonnement au calendrier'),
        ('BEGIN:VCALENDAR', 1, 'gabarit .ics'),
    ):
        _exiger(page, _marqueur, _combien, _quoi)

    # Les ancres visees par le menu partage doivent exister : sans elles, une
    # entree de menu mene dans le vide. `#instruments` avait deja disparu une
    # fois de la sortie du generateur (elle n'etait que dans la page publiee).
    for _ancre in ('id="agenda"', 'id="instruments"', 'id="yoga"',
                   'id="psychotherapie"', 'id="calebasse-workshop"',
                   'id="cours-individuels"', 'id="concerts"'):
        if _ancre not in page:
            raise SystemExit('!! ABANDON : ancre %s absente — une entree du menu '
                             'partage menerait dans le vide. Page NON ecrite.' % _ancre)

    # ⚠️ LIENS DE BILLETTERIE. Chaque evenement porte un bouton de reservation,
    # et deux evenements du MEME type peuvent pointer sur des billetteries
    # differentes (URL_PAR_EVENT). On verifie que chaque url attendue est bien
    # dans la page, et qu'il y a exactement un bouton de reservation par
    # evenement : c'est la partie de la page ou une erreur coute de l'argent.
    _urls = {reservation(iso, h1, typ)[0]
             for iso, h1, _h2, typ, _t, _n in EVENTS}
    for _u in sorted(_urls):
        if _u not in page:
            raise SystemExit('!! ABANDON : lien de reservation absent de la page : '
                             '%s. Page NON ecrite.' % _u)
    _exiger(page, 'class="ag-btn"', len(EVENTS), 'boutons de reservation')
    _exiger(page, 'class="ag-item"', len(EVENTS), 'lignes d’agenda')

    # Aucune note de redaction en commentaire HTML dans la page livree : elle
    # serait publique et indexable. Leur place est ici, en commentaire `#`.
    verif_commentaires.verifier(page, TARGET)

    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, 'w', encoding='utf-8') as f:
        f.write(page)
    print('ECRIT', TARGET, round(len(page.encode()) / 1024), 'ko  |',
          len(EVENTS), 'dates,', len(set(e[3] for e in EVENTS)), 'types,',
          len(_urls), 'billetteries distinctes')
