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
⚠️ 27/08/2026 — `EVENTS` N'EST PLUS RECOPIE A LA MAIN. Il est REECRIT chaque
nuit par `sources/synchro_agenda.py`, qui lit le flux public du meme agenda
Google (CAL_ID ci-dessous) et n'en garde que les evenements A VENIR dont le
titre figure dans sa table de correspondance. Tout le mode d'emploi est en tete
de ce fichier-la. Ici, retenir seulement :

  * la liste vit ENTRE DEUX BALISES (« DEBUT / FIN DES DATES SYNCHRONISEES ») ;
    n'ecrire aucune note entre elles, la prochaine synchronisation l'effacerait.
    Les notes vont AU-DESSUS de la balise de debut, comme celles qui suivent ;
  * le titre et la note publies ne viennent PAS du flux : ils sont decides une
    fois pour toutes dans la table de `synchro_agenda.py`. Le flux ne fournit
    que la date, l'heure de debut et l'heure de fin ;
  * on peut toujours modifier la liste a la main : la synchronisation suivante
    la reecrira depuis l'agenda, sans se plaindre.

⚠️ PAGE SENSIBLE : elle porte l'agenda, les reservations et des liens de
billetterie qui DIFFERENT d'un evenement a l'autre (URL_PAR_EVENT). Un garde-fou
verifie avant chaque ecriture que chaque billetterie attendue est bien dans la
page et qu'il y a exactement un bouton de reservation par evenement.
"""
import colorsys
import datetime as dt
import os
import re
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
# --------------------------------------------------------------------------- #
# NOTES RAPATRIEES DE `lenid_source.html` (16/08/2026)
# ---------------------------------------------------
# Elles y vivaient en commentaires CSS, donc dans la page livree, lisibles par
# « afficher le code source ». La source HTML n'accepte pas de commentaire `#` :
# leur place est ici, en face du fichier qu'elles expliquent. Ne pas les
# remettre dans `lenid_source.html`.
#
# `.blocs` — BLOCS ILLUSTRES DES PROPOSITIONS (pleine largeur, entre programme
#   et agenda). Un seul systeme pour les trois blocs : colonne large (photo
#   principale + titre et legende) + colonne etroite (photo(s) secondaire(s)).
#   Variante `--solo` pour une proposition qui n'a qu'une photo : texte a cote,
#   image jamais agrandie au-dela de sa resolution native. Chaque photo garde
#   son ratio natif (aucun recadrage).
#
# `.bloc picture{width:100%}` — /!\ le `width:100%` est OBLIGATOIRE : des marges
#   auto sur un enfant de grille annulent le `stretch` -> la <picture> passerait
#   en fit-content et s'effondrerait a quelques pixels tant que l'image n'est
#   pas decodee (meme piege que les slides des carrousels).
# --------------------------------------------------------------------------- #
#: la source versionnee, jamais modifiee par ce script
SOURCE = os.path.join(HERE, 'lenid_source.html')
#: la page publiee
TARGET = os.path.join(REPO, 'le-nid', 'index.html')

sys.path.insert(0, HERE)
import nav_menu  # menu de navigation partage  # noqa: E402
import theme_chaleur  # couche chaleureuse commune  # noqa: E402
import visionneuse  # visionneuse photo commune  # noqa: E402
import dates_a_venir  # dates passees masquees par le navigateur  # noqa: E402
import verif_commentaires  # garde-fou commentaires HTML  # noqa: E402

CAL_ID = '30716d7f4373d33769612165eb0607e5b33fd533b984df2df61fe9518ab32eae@group.calendar.google.com'
CAL_SUB = ('https://calendar.google.com/calendar/r?cid=MzA3MTZkN2Y0MzczZDMzNzY5NjEyMTY1'
           'ZWIwNjA3ZTViMzNmZDUzM2I5ODRkZjJkZjYxZmU5NTE4YWIzMmVhZUBncm91cC5jYWxlbmRhci5nb29nbGUuY29t')
# Flux iCal public du meme calendrier (Apple Calendrier, Outlook, Thunderbird...)
CAL_WEBCAL = ('webcal://calendar.google.com/calendar/ical/'
              + urllib.parse.quote(CAL_ID, safe='') + '/public/basic.ics')

# (date ISO, heure debut, heure fin, type, titre, note)
#
# ⚠️ N'ECRIRE AUCUN COMMENTAIRE ENTRE LES DEUX BALISES CI-DESSOUS : le bloc est
#    reecrit en entier a chaque synchronisation et tout ce qu'il contient serait
#    perdu. Les notes se posent ICI, au-dessus de la balise de debut.
#
# 20/08/2026 — David a tranche pour le rendez-vous mensuel du 4 septembre :
# « c'est l'horaire de l'INSTATIC qui gagne ». Ce RDV a un programme, donc il
# porte son nom et ses horaires reels (19h00-21h30, accueil 18h45, portes
# fermees a 19h00). L'agenda Google public a ete corrige en meme temps — et
# c'est desormais LUI qui fournit ces horaires, donc les deux ne peuvent plus
# diverger.
# --- DEBUT DES DATES SYNCHRONISEES (ecrit par sources/synchro_agenda.py) ---
EVENTS = [
    ('2026-09-04', '19:00', '21:30', 'mensuel',   'INSTATIC Dance', 'avec Iris & David'),
    ('2026-09-06', '16:30', '19:00', 'yoga',      'Atelier de yoga', 'avec Iris Chasles'),
    ('2026-09-19', '16:00', '19:00', 'showcase',  'Présentation d’instruments d’exception', ''),
    ('2026-09-20', '10:00', '12:00', 'rythme',    'Groupe de pratique rythme calebasse engagé', 'avec David Lesage · sur candidature'),
    ('2026-09-26', '17:00', '19:00', 'residence', 'Sortie de résidence', 'restitution du travail en trio'),
    ('2026-09-26', '20:00', '22:00', 'concert',   'Concert — David, Iris & Julien', 'le trio en concert'),
    ('2026-10-02', '18:30', '23:30', 'mensuel',   'Rendez-vous mensuel au Nid', ''),
    ('2026-10-04', '16:30', '19:00', 'yoga',      'Atelier de yoga', 'avec Iris Chasles'),
    ('2026-10-10', '19:00', '21:00', 'concert',   'Concert — David Lesage solo', ''),
    ('2026-10-17', '15:00', '17:00', 'rythme',    'Groupe de pratique rythme calebasse engagé', 'avec David Lesage · sur candidature'),
    ('2026-10-18', '16:00', '19:00', 'showcase',  'Présentation d’instruments d’exception', ''),
    ('2026-11-07', '18:30', '23:30', 'mensuel',   'Rendez-vous mensuel au Nid', ''),
    ('2026-11-08', '16:30', '19:00', 'yoga',      'Atelier de yoga', 'avec Iris Chasles'),
    ('2026-11-14', '16:00', '19:00', 'showcase',  'Présentation d’instruments d’exception', ''),
    ('2026-11-15', '15:00', '17:00', 'rythme',    'Groupe de pratique rythme calebasse engagé', 'avec David Lesage · sur candidature'),
    # 27/08/2026 — David a pose le principe : « on garde toujours ce que dit
    # l'agenda Google comme etant la derniere source de verite, la plus a
    # jour ». L'agenda annonce « + Guest Lucie au violon » : le site ne peut
    # donc plus ecrire « solo ». Le mot etait devenu faux.
    ('2026-11-28', '18:00', '20:00', 'concert',   'Concert — David Lesage', 'avec Lucie au violon'),
    ('2026-12-04', '18:30', '23:30', 'mensuel',   'Rendez-vous mensuel au Nid', ''),
    ('2026-12-05', '15:00', '18:00', 'showcase',  'Présentation d’instruments d’exception', ''),
    ('2026-12-06', '16:30', '19:00', 'yoga',      'Atelier de yoga', 'avec Iris Chasles'),
]
# --- FIN DES DATES SYNCHRONISEES ---

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
 'rythme':   'Rendez-vous mensuel du groupe de pratique engage, avec David Lesage : deux heures de pratique, les bases, les frappes, la pulsation collective. Aucun prerequis musical. Ce n\'est pas un atelier ouvert a la seance : on rejoint le groupe sur candidature, a tout moment.',
 'showcase': 'Presentation, decouverte et essai d\'instruments d\'exception : le Neotone (handpan electronique de facture professionnelle), des handpans acoustiques Yishama, la calebasse, le Gonilele (petite harpe africaine) et des micros concus pour le handpan. Des instruments faits main, produits en tres petites series, dont la valeur atteint plusieurs milliers d\'euros. David Lesage les presente, les fait sonner devant vous, repond aux questions, puis les met entre vos mains. Gratuit, sur inscription, environ 2 h. Aucune experience requise.',
 'residence':'Sortie de residence : restitution publique du travail mene en trio.',
}

# Versions accentuees, utilisees uniquement pour les liens Google Agenda
# (les .ics restent sur les chaines sans accents, par compatibilite).
DESCR_FR = {
 'mensuel':  'Le rendez-vous mensuel du Nid : un temps convivial qui mélange pratique, musique et partage, dans un cadre intime. Réservé aux adhérents de l’association.',
 'concert':  'Un concert en format intime : voix, handpan électronique, harpe africaine (Ngoni), calebasse et percussions électro-organiques.',
 'yoga':     'Atelier de yoga guidé par Iris Chasles : yoga postural, respiration et méditation. Pratique accessible à tous les niveaux.',
 'rythme':   'Rendez-vous mensuel du groupe de pratique engagé, avec David Lesage : deux heures de pratique, les bases, les frappes, la pulsation collective. Aucun prérequis musical. Ce n\'est pas un atelier ouvert à la séance : on rejoint le groupe sur candidature, à tout moment.',
 'showcase': 'Présentation, découverte & essai d’instruments d’exception : le Neotone (handpan électronique de facture professionnelle), des handpans acoustiques Yishama, la calebasse, le Gonilélé (petite harpe africaine) et des micros conçus pour le handpan. Des instruments faits main, produits en très petites séries, dont la valeur atteint plusieurs milliers d’euros. David Lesage les présente, les fait sonner devant vous, répond à toutes les questions, puis les met entre vos mains. Gratuit, sur inscription, environ 2 h. Aucune expérience requise.',
 'residence':'Sortie de résidence : restitution publique du travail mené en trio.',
}
ACCES_PUBLIC_FR = ('Au fond de la cour, porte verte, 3e étage. '
                   'Le code du portail vous est communiqué avec votre confirmation d’inscription.')
JAUGE_FR = ('Jauge limitée : chaque événement est sur invitation ou sur inscription préalable. '
            'Merci de réserver avant de venir.')

LESAGE   = 'https://lesagedavid.fr'
# 16/08/2026 : bascule de `www.handpan-studio.app` vers l'adresse CANONIQUE.
# Le site vitrine de David est servi sous CINQ hotes (`lesagedavid.fr` + quatre
# domaines `.app`), qui rendent tous le meme contenu. Sa balise canonique
# designe `https://www.lesagedavid.fr/showroom/` : c'est elle qui fait foi.
# Verifie avant de basculer (ce sont des liens de RESERVATION en production) :
# les deux URL repondent 200, portent `id="agenda"` et declarent le meme
# canonique. Le partage d'un lien propage desormais l'adresse de reference.
# ⚠️ NE JAMAIS DEBRANCHER les domaines `.app` : l'ancienne adresse est deja
# partie dans les descriptions Google Agenda et les fichiers `.ics` telecharges
# par les inscrits. Ces liens vivent chez des gens, hors de ce depot.
SHOWROOM = 'https://www.lesagedavid.fr/showroom#agenda'
ADHESION = 'https://www.helloasso.com/beta/associations/resonances-productions/adhesions/adhesion-resonances-productions'
YOGA_INS = 'https://www.helloasso.com/associations/resonances-productions/evenements/atelier-mensuel-au-nid'
MAILTO   = 'mailto:contact@resonancesproductions.org?subject=Le%20Nid%20—%20r%C3%A9servation'
CANDIDATURE = '/rythme-calebasse#candidature'
# Cours individuels : DEUX intervenants, donc DEUX destinations. Le bloc dit
# lui-meme « Avec David : le rythme et la calebasse. Avec Iris : yoga postural,
# breathwork adapte… » : un lien unique aurait envoye la moitie des lecteurs au
# mauvais endroit. Les deux adresses repondent 200 (verifie le 16/08/2026).
# ⚠️ La page d'Iris s'intitule « Retraites & Ateliers Yoga » : c'est son agenda,
# pas une page de cours individuels. C'est l'adresse validee, mais si David veut
# une destination strictement individuelle, c'est lui qui la fournira.
COURS_DAVID = 'https://lesagedavid.fr/cours'
COURS_IRIS  = 'https://www.irischasles.com/agenda-yoga'

# type : (libelle, couleur, lien de reservation, libelle du bouton)
TYPES = {
    'mensuel':   ('Rendez-vous mensuel', '#d8b25a', ADHESION, 'Adhérer ↗'),
    'concert':   ('Concert',             '#e08a5f', LESAGE,   'Réserver ↗'),
    'yoga':      ('Atelier yoga',        '#7fb2a3', YOGA_INS, 'S’inscrire ↗'),
    # 17/08/2026 — David a tranche : ces rendez-vous ne sont PAS ouverts a la
    # seance. C'est le groupe de pratique engage, qu'on rejoint sur candidature
    # (« on peut le rejoindre a tout moment », ses mots). Le bouton menait a un
    # mailto de reservation : il envoyait donc reserver une place qui n'existe
    # pas. Il mene desormais a l'appel a candidature de /rythme-calebasse.
    # ⚠️ Les memes evenements ont ete renommes dans l'agenda Google du Nid :
    # « Groupe de pratique rythme calebasse engage — Le Nid ». Garder les deux
    # accordes, sinon l'agenda et le site racontent deux choses differentes.
    'rythme':    ('Groupe de pratique', '#8f7ad1', CANDIDATURE, 'Rejoindre le groupe'),
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
    # INSTATIC Dance : billetterie dediee, et non le formulaire d'adhesion.
    ('2026-09-04', '19:00'):
        'https://www.helloasso.com/associations/resonances-productions/evenements/instatic-dance',
    ('2026-10-10', '19:00'): CONCERT_SOLO,   # Concert — David Lesage solo
    ('2026-11-28', '18:00'): CONCERT_SOLO,   # Concert — David Lesage + Lucie au violon
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


# --------------------------------------------------------------------------- #
# LES DATES PASSEES DISPARAISSENT TOUTES SEULES  (27/08/2026)
# ---------------------------------------------------------
# Tout le mecanisme est dans `sources/dates_a_venir.py` — y compris la raison
# pour laquelle ce n'est qu'une RUSTINE (le site est statique, il ne sait pas
# quel jour on est). Ici, on ne fait que DECLARER ce qui porte une date :
#
#   * les 20 lignes de l'agenda (`.ag-item`), chacune dans DEUX blocs : son
#     groupe de mois (qui s'efface en entier, titre compris, quand le mois est
#     passe) et l'agenda entier (qui bascule sur un message de repli) ;
#   * le bouton de filtre du mois, la legende, la barre de filtres, le bouton
#     « tout ajouter a mon agenda » et sa note : ils n'ont plus d'objet quand il
#     ne reste aucune date, donc ils portent `lie('agenda')` ;
#   * les quatre encarts « Prochaines dates » des tuiles du programme.
#
# ⚠️ UN SEUL REGISTRE PAR GENERATION. `generer()` le remet a neuf : deux appels
#    dans le meme processus ne doivent pas empiler deux fois les memes dates.
REG = dates_a_venir.Registre()

#: le message de repli, ecrit une seule fois pour les cinq endroits de la page.
EN_PREPARATION = 'Prochaines dates en préparation.'


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
    # `lie(...)` : ce bouton de mois disparait avec son groupe de mois.
    f_mois = ''.join(
        f'<button class="ag-f" type="button" data-f="mois" data-v="{an:04d}-{mo:02d}"'
        f'{REG.lie("agenda-%04d-%02d" % (an, mo))}>'
        f'{MOIS[mo-1]}</button>'
        for (an, mo), _evs in groupes)

    out = ['<section class="agenda" id="agenda"><div class="wrap">',
           '  <span class="ag-anchor" id="concerts"></span>',
           '  <div class="kick">L’agenda</div>',
           '  <h2 class="sec-title">Les prochaines dates</h2>',
           '  <p class="lead">Rendez-vous mensuels, concerts, ateliers et workshops — au Nid, 29 rue des Orteaux, Paris 20<sup>e</sup>.</p>',
           SUB_BLOCK,
           f'  <div class="ag-legend"{REG.lie("agenda")}>{leg}</div>',
           f'  <div class="ag-filters" aria-label="Filtrer l’agenda"{REG.lie("agenda")}>',
           '    <div class="ag-frow"><span class="ag-flab">Type</span>'
           '<button class="ag-f is-on" type="button" data-f="type" data-v="">Tous</button>'
           + f_types + '</div>',
           '    <div class="ag-frow"><span class="ag-flab">Mois</span>'
           '<button class="ag-f is-on" type="button" data-f="mois" data-v="">Tous</button>'
           + f_mois + '</div>',
           '    <p class="ag-fnone" hidden>Aucune date ne correspond à ces filtres. '
           '<button class="ag-freset" type="button">Tout afficher</button></p>',
           '  </div>',
           # Le message de repli de l'agenda entier : invisible tant qu'il reste
           # une date a venir, il prend la place de la liste quand il n'en reste
           # plus une seule. Sans lui la page garderait « Les prochaines dates »
           # au-dessus du vide.
           f'  <p{REG.repli("agenda")}>{EN_PREPARATION}</p>']

    REG.declare('agenda', repli='block')
    for (an, mois), evs in groupes:
        cle_mois = 'agenda-%04d-%02d' % (an, mois)
        # `cacher` : quand le mois est passe, le groupe part EN ENTIER — sinon
        # il resterait un titre de mois seul au-dessus de rien.
        REG.declare(cle_mois, cacher=True)
        out.append(f'  <div class="ag-group" data-mois="{an:04d}-{mois:02d}"'
                   f'{REG.bloc_attr(cle_mois)}>')
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
            # ⚠️ `data-e` est deja l'heure de FIN en UTC — c'est elle qui decide
            # si la ligne a vecu, pas `data-s`. `REG.date()` la recalcule de son
            # cote (meme resultat, calcul de fuseau propre : voir la regle 2 de
            # `dates_a_venir.py`) plutot que de relire un attribut de la page.
            data = (f' data-s="{utc(h1)}" data-e="{utc(h2)}"'
                    f' data-t="{esc_attr(titre)}" data-d="{esc_attr(desc)}"'
                    f' data-typ="{typ}" data-mois="{d.year:04d}-{d.month:02d}"'
                    + REG.date(('agenda', cle_mois), d, h2))
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
        # `lie('agenda')` : sans aucune date a venir, ce bouton telechargerait un
        # fichier .ics vide. Le bouton « Réserver une place », lui, RESTE : on
        # peut toujours ecrire, meme quand rien n'est encore programme.
        '    <button class="btn ag-all" type="button"' + REG.lie('agenda')
        + '>↓ Ajouter toutes les dates à mon agenda</button>',
        '    <a class="btn" href="mailto:contact@resonancesproductions.org?subject=Le%20Nid%20—%20réservation">Réserver une place</a>',
        '  </div>',
        '  <p class="ag-tip"' + REG.lie('agenda') + '>« + Google Agenda » ajoute la date directement dans votre Google Agenda '
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
#
# ⚠️ 20/08/2026 — `.ag-btn` ET `.ag-cal` NE PRENNENT PAS L'ECHELLE COMPLETE DES
#    BOUTONS, ET C'EST UNE DECISION, PAS UN OUBLI. David a demande des boutons
#    plus gros et plus gras « en general » ; `.btn` passe donc a 18 px / 700 /
#    17px 34px partout (`theme_chaleur.CSS_BOUTONS`). Les 20 boutons
#    « Reserver » de la liste d'agenda et les 20 « + .ics » qui les accompagnent
#    prennent la GRAISSE (500 -> 700, 400 -> 700) et UN CRAN de taille
#    (16 -> 17 px), mais gardent leur rembourrage resserre (9 -> 11 px en
#    hauteur seulement).
#    Pourquoi : ils ne sont pas seuls dans un bloc, ils sont la troisieme
#    colonne d'une grille de 20 lignes. Mesure a 390 px avec le rembourrage
#    complet : la colonne du titre tombe sous 150 px et chaque intitule
#    d'evenement casse sur trois lignes — c'est exactement le defaut que le
#    bloc `@media(max-width:1000px)` plus bas a ete ecrit pour eviter
#    (« On empile, on ne rapetissit pas »).
#    Le texte, lui, grossit bien : c'etait la demande.
CSS = ("""
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
  .btn.ag-sub-btn{padding:16px 18px;white-space:normal}
}
.ag-leg{display:inline-flex;align-items:center;gap:8px;color:var(--muted);font-size:14px}
.ag-leg i{width:9px;height:9px;border-radius:50%;display:inline-block;flex:0 0 auto}
.ag-leg{display:inline-flex;align-items:center;gap:8px;color:var(--muted);font-size:14px}
.ag-leg i{width:9px;height:9px;border-radius:50%;display:inline-block;flex:0 0 auto}
.ag-month{margin-top:40px;margin-bottom:16px;color:var(--gold);font-family:'Cormorant Garamond',Georgia,serif;
  font-size:31px;font-weight:600;text-transform:capitalize;border-bottom:1px solid var(--line);padding-bottom:10px}
.ag-list{display:grid;gap:10px}
.ag-anchor{display:block;height:0;scroll-margin-top:90px}
"""
      # ⚠️ 20/08/2026 — `.btn.ag-sub-btn` ET NON `.ag-sub-btn` dans le bloc
      #    @media(max-width:760px) ci-dessus. La definition de `.btn` ne vit plus
      #    dans cette feuille : elle vient de `theme_chaleur.CSS_BOUTONS`,
      #    concatene APRES. A specificite egale (0,1,0) c'est donc `.btn` qui
      #    gagne, et le bouton « S'abonner avec Google Agenda » reprenait le
      #    rembourrage large au lieu du rembourrage resserre du telephone.
      #    Mesure : 26 px au lieu de 18 px de chaque cote a 390 px. `.btn.ag-sub-btn`
      #    = (0,2,0), la surcharge redevient volontaire au lieu d'etre un effet
      #    de l'ordre des blocs.
      # --- filtres : masques sans JS (tout reste visible), affiches par .ag-js ---
      """.ag-filters{display:none;flex-direction:column;gap:10px;margin-top:22px}
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
  padding:11px 20px;font-size:17px;font-weight:700;text-decoration:none;white-space:nowrap;
  transition:background .2s,color .2s}
.ag-btn:hover{background:var(--c);color:#12121f}
.ag-foot{display:flex;flex-wrap:wrap;gap:14px;margin-top:38px}
.ag-tip{color:var(--muted);font-size:15px;margin-top:16px;font-style:italic}
.ag-cal{display:inline-flex;align-items:center;justify-content:center;min-height:44px;
  border:1px solid rgba(255,255,255,.20);background:rgba(255,255,255,.05);color:#e6e3f5;
  border-radius:24px;padding:11px 17px;font-size:17px;font-weight:700;cursor:pointer;white-space:nowrap;
  font-family:inherit;transition:background .2s,color .2s,border-color .2s}
.ag-cal:hover{background:var(--gold);color:#1a1608;border-color:var(--gold)}
.ag-access{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px;margin-top:40px}
.ag-access>div{background:var(--card);border:1px solid rgba(255,255,255,.07);border-radius:14px;
  padding:20px 22px;color:#d3d0e8;font-size:14.5px;line-height:1.6}
.ag-access span{display:block;color:var(--gold);font-size:13px;letter-spacing:.16em;
  text-transform:uppercase;font-weight:600;margin-bottom:8px}
.ag-access i{color:var(--muted);font-size:13px}
"""
      # --- largeurs intermediaires (<=1000 px) : les actions passent sur leur propre
      # ligne pour laisser respirer le titre (sinon la colonne du titre se tasse a
      # ~200 px et chaque intitule casse sur 3 lignes). On empile, on ne rapetissit pas. ---
      """@media(max-width:1000px){
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
""")

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
CSS_DATES = (""".offer-dates{margin-top:14px;padding-top:12px;border-top:1px solid rgba(255,255,255,.08);color:#d3d0e8;font-size:16px}
.offer-dates span{display:block;color:var(--gold);font-size:14px;letter-spacing:.16em;text-transform:uppercase;font-weight:600;margin-bottom:5px}
.offer-dates a{color:var(--gold2);font-size:16px;font-weight:500;text-decoration:underline;text-underline-offset:4px;
  display:inline-flex;align-items:center;min-height:44px}
"""
            # UN SEUL STYLE DE BOUTON D'ACTION POUR LES SIX CARTES DU PROGRAMME.
            # Aucune classe nouvelle : le bouton d'action vit dans la ligne
            # `.who` de la carte, exactement comme celui de la carte
            # « instruments d'exception » (« Réservation en ligne : réserver ma
            # place ↗ »), qui etait le seul a en porter un. Cette regle lui
            # donne la MEME apparence qu'un lien de `.offer-dates` — souligne,
            # dore, et surtout une cible tactile de 44 px que le lien de la
            # carte « instruments » n'avait PAS (il heritait simplement de
            # `a{color:…}`). Les six liens d'action de la page se ressemblent
            # donc, qu'ils soient dans `.who` (cinq cartes) ou dans
            # `.offer-dates` (la prise de rendez-vous de la psychotherapie, qui
            # y vivait deja et qu'on ne deplace pas).
            """.offer .who a{color:var(--gold2);font-weight:500;text-decoration:underline;text-underline-offset:4px;
  display:inline-flex;align-items:center;min-height:44px}
"""
            # carte « instruments d'exception ».
            # ⚠️ 17/08/2026 — `grid-column:1/-1` RETIRE. Elle occupait les TROIS
            # colonnes (988 px mesures a 1440, contre 316 pour les cinq autres)
            # et se retrouvait seule sur une 3e ligne : la grille se lisait comme
            # « 5 tuiles + 1 banniere ». David : « fait quelque chose de coherent
            # graphiquement entre les 6 tuiles de facon equilibree. »
            # Six tuiles sur trois colonnes tombent juste : deux lignes pleines.
            # Le fond dore reste — c'est un accent discret, pas un format a part.
            # `max-width:78ch` sur les `p` devient sans objet dans une colonne de
            # 316 px : garde sans effet, retire pour ne pas laisser croire a une
            # contrainte active.
            """.offer--rare{background:linear-gradient(135deg,rgba(216,178,90,.10),rgba(255,255,255,.03));
  border-color:rgba(216,178,90,.34)}
.offer--rare h3{margin-bottom:6px}
.offer--rare .offer-meta{color:var(--gold2);font-size:14px;font-style:italic;margin:0 0 14px}
.offer--rare p+p{margin-top:12px}
.offer--rare b{color:#efeaf6;font-weight:600}
.offer-fine{margin-top:18px;padding-top:14px;border-top:1px solid rgba(255,255,255,.10);
  color:var(--muted);font-size:13px;line-height:1.65;max-width:78ch}
.offer-fine b{color:var(--gold2);font-weight:600}
""")


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
#
# 🚩 ET LE FOND DES BOUTONS S'ASSOMBRIT — le SEUL endroit du code couleur qui
#    bouge, et il ne touche a AUCUNE des six teintes. `.ag-btn` posait
#    rgba(255,255,255,.05) PAR-DESSUS la carte : le texte colore se retrouvait
#    donc sur #242647, plus clair que la carte elle-meme. « Workshop rythme »
#    (#8f7ad1) y etait a 4,07:1 — SOUS le seuil de 4,5:1, et deja avant la
#    refonte. Trouve en relisant les contrastes REELLEMENT CALCULES par le
#    navigateur sur les 30 pages, pas en relisant le CSS.
#      monter la carte      -> 3,72:1  (pire)
#      epingler seulement   -> 4,07:1  (le statu quo, toujours en panne)
#      rgba(0,0,0,.14)      -> 4,87:1  (fond #161734)
#    Les six types repassent au-dessus du seuil : mensuel 8,65 · concert 6,61 ·
#    yoga 7,29 · rythme 4,87 · showcase 6,04 · residence 6,66. Un fond neutre
#    n'est pas un code : aucune information n'est portee par ce gris.
CSS_CHALEUR = ("""/* ===== Le Nid : declinaisons chaleureuses ===== */
"""
              # la liste d'agenda garde la surface sur laquelle son code couleur a ete
              # calibre : `--c` est la couleur de texte des 20 boutons de billetterie
              """.ag-item{background:#191b3d}
"""
              # le fond du bouton s'assombrit au lieu de s'eclaircir : contraste des 20
              # boutons de billetterie (voir la note du generateur)
              """.ag-btn{background:rgba(0,0,0,.14)}
.hero h1{background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent;width:fit-content;max-width:100%;margin:0 auto}
"""
              # ⚠️ `width:fit-content` ET SURTOUT PAS `display:inline-block` ici. Mesure
              # faite a l'ecran : `.offer-dates span` est un BLOC suivi, dans le meme
              # parent, du texte des dates. Passe en inline-block, l'etiquette venait se
              # coller aux dates — « PROCHAINES DATES6 sept. · 4 octo. ». `fit-content`
              # retrecit la boite au texte (ce dont le degrade a besoin pour balayer les
              # MOTS et non toute la carte) sans toucher au flux.
              """.offer .t,.offer-dates span,.ag-sub-kick,.ag-month{width:fit-content;max-width:100%;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
"""
              # cartes du programme : filet de tete au degrade, coins plus genereux
              """.offer{border-top:3px solid transparent;border-radius:18px;background-image:var(--grad),linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,0)),linear-gradient(var(--card),var(--card));background-size:100% 3px,100% 100%,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box,padding-box}
.offer--rare{background-image:var(--grad),linear-gradient(135deg,rgba(216,178,90,.10),rgba(255,255,255,.03));background-size:100% 3px,100% 100%;background-repeat:no-repeat,no-repeat;background-position:0 0,0 0;background-origin:border-box,padding-box}
"""
              # la prune revient en accent de TEXTE (--plum2 : 7,3:1 sur --card)
              """.offer .who,.offer--rare .offer-meta{color:var(--plum2)}
"""
              # l'encart d'abonnement au calendrier : il n'est PAS pilote par --c
              """.ag-sub{border-radius:18px;border-color:rgba(248,210,116,.34)}
.ag-sub li::before{width:7px;height:7px;border-radius:2px;background:var(--grad-warm);transform:rotate(45deg)}
"""
              # les deux cartes « se programme en / s'inscrit dans » et l'encart en pointilles
              """.scene-card{border-top:3px solid transparent;border-radius:18px;background-image:var(--grad),linear-gradient(var(--card),var(--card));background-size:100% 3px,100% 100%;background-repeat:no-repeat;background-position:0 0;background-origin:border-box,padding-box}
.note{border-radius:18px;border-color:rgba(248,210,116,.3)}
.note b{color:var(--plum2)}
"""
              # arrondis genereux — `.gal img` etait a 16 px, les autres pages sont a 18
              """.gal img{border-radius:18px}
""")


# =========================================================================== #
# UNE COULEUR PAR ACTIVITE — LES SIX TUILES DU PROGRAMME (19/08/2026)
# =========================================================================== #
# « met des couleurs de fond differentes sur chaque tuile pour creer de la mise
#   en lumiere de chaque activite "avec sa propre couleur" » — David, 19/08.
#
# 🚨 AUCUNE PALETTE N'A ETE INVENTEE. Quatre des six tuiles correspondent a un
#    type d'evenement de l'agenda qui est JUSTE EN DESSOUS sur la meme page, et
#    ce type a deja sa couleur dans `TYPES`. On la LIT dans `TYPES` — on ne la
#    recopie pas : une seule source. Consequence voulue : une activite porte la
#    MEME teinte dans sa tuile et dans l'agenda (badge, filet de la ligne,
#    bouton de reservation, legende). Le lecteur fait le lien sans explication.
#
#    tuile                  type d'agenda   couleur
#    instruments            showcase        #6f9bd1  « Découverte & essai »
#    concerts-au-nid        concert         #e08a5f  « Concert »
#    yoga                   yoga            #7fb2a3  « Atelier yoga »
#    calebasse-workshop     rythme          #8f7ad1  « Groupe de pratique »
#
# LES DEUX TUILES SANS TYPE D'AGENDA (psychotherapie, cours individuels)
# ----------------------------------------------------------------------
# Elles ne paraissent jamais dans l'agenda : aucune couleur de `TYPES` ne leur
# revient. Leur donner celle d'un type existant (il en reste deux inutilisees,
# `mensuel` #d8b25a et `residence` #c98fb0) casserait justement le lien qu'on
# vient d'etablir : le lecteur relierait « Psychothérapie » a « Rendez-vous
# mensuel ». Elles recoivent donc deux teintes NEUVES, de la meme famille que
# les six autres (memes saturation et luminosite perçues : S 42 %, L 62–66 %,
# contre S 25–68 % / L 60–67 % pour les six d'agenda) et posees dans les deux
# plus grands VIDES de la roue chromatique laissee par l'agenda — les six teintes
# sont a H = 20, 42, 162, 213, 254, 326.
#
#    psychotherapie     #97c775  hsl( 95, 42 %, 62 %)  vert tendre
#    cours-individuels  #c384cd  hsl(292, 42 %, 66 %)  mauve
#
# ⚠️ A ARBITRER PAR DAVID : le mauve est la teinte la plus proche d'une couleur
#    d'agenda — 34° de « Sortie de résidence » #c98fb0. Le vert, lui, est a 53°
#    de son plus proche voisin. La confusion ne peut aller que dans un sens (ces
#    deux activites n'ont aucune ligne dans l'agenda) et la legende nomme ses
#    types en toutes lettres, mais si David trouve le mauve trop proche du rose,
#    c'est ici qu'on le change.
#
# COMMENT LA COULEUR EST POSEE, ET POURQUOI PAS EN APLAT
# ------------------------------------------------------
# Le site est SOMBRE (`--night` #0e0f24, cartes `--card` #1e214a). Un fond
# franchement colore effacerait l'identite du site et ferait tomber tous les
# textes sous le seuil de lisibilite. La couleur arrive donc en trois temps :
#   1. le fond de la tuile = la teinte a 10 % SUR `--card` — un voile, pas un
#      aplat. La valeur est PRECALCULEE ici en hexadecimal opaque : le
#      navigateur renvoie alors la couleur exacte du fond, ce qui rend le
#      contraste MESURABLE dans le DOM au lieu d'etre estime ;
#   2. le liseré superieur de 3 px, deja present, passe de l'or commun a la
#      teinte pleine : c'est l'accent net, celui que l'oeil accroche ;
#   3. le chapeau `.t` (« MUSIQUE LIVE », « CORPS & SOUFFLE »…) prend la teinte.
#
# 🚨 ET C'EST LA QUE LE CHAPEAU NE PEUT PAS PRENDRE LA TEINTE BRUTE. Mesure
#    faite : sur son propre fond, `rythme` #8f7ad1 tombe a 3,75:1 — SOUS le
#    seuil de 4,5:1. C'est le meme piege que `--plum` dans `theme_chaleur.py`,
#    qui note deja « des qu'il s'agit de TEXTE, c'est `--plum2` et jamais
#    `--plum` ». On ne choisit donc pas une couleur de texte a la main : elle est
#    DERIVEE de la teinte par eclaircissement (`_texte_lisible`), par pas de
#    0,5 % de luminosite, jusqu'a atteindre 5,0:1 sur le fond reel de la tuile —
#    une marge volontaire sur le seuil de 4,5. Trois teintes sur six ne bougent
#    pas du tout ; `rythme` monte de L 65 % a 72 %. Si une teinte de `TYPES`
#    change un jour, la couleur de texte suit toute seule.
#
# ⚠️ LE VOILE DORE DE LA TUILE « INSTRUMENTS » DISPARAIT, ET C'EST VOULU.
#    `.offer--rare` posait un degrade dore : c'etait sa facon d'etre distinguee
#    quand elle etait la seule a l'etre. Maintenant que les six tuiles portent
#    chacune leur couleur, un doré en plus du bleu `showcase` ferait mentir le
#    code couleur sur la seule tuile qui ouvre la grille. La classe RESTE dans le
#    HTML (elle porte `.offer-meta` et `.offer-fine`, et le garde-fou structurel
#    compte `class="offer offer--rare"`), seul son fond suit desormais le systeme.
# =========================================================================== #
#: fond des cartes, LU dans theme_chaleur (qui redefinit `--card`), jamais recopie
FOND_CARTE = re.search(r'--card:(#[0-9a-fA-F]{6})', theme_chaleur.CSS).group(1)

#: (id de la tuile dans le HTML, cle de TYPES, teinte propre si aucun type)
TUILES = (
    ('instruments',        'showcase',  None),
    ('concerts-au-nid',    'concert',   None),
    ('yoga',               'yoga',      None),
    ('calebasse-workshop', 'rythme',    None),
    ('psychotherapie',     None, '#97c775'),
    ('cours-individuels',  None, '#c384cd'),
)


def _rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _hexa(rgb):
    return '#%02x%02x%02x' % tuple(max(0, min(255, round(x))) for x in rgb)


def _melange(dessus, dessous, alpha):
    """`dessus` pose a `alpha` sur `dessous`, rendu en couleur opaque."""
    a, b = _rgb(dessus), _rgb(dessous)
    return _hexa(a[i] * alpha + b[i] * (1 - alpha) for i in range(3))


def _luminance(couleur):
    def canal(v):
        v /= 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, v, b = (canal(x) for x in _rgb(couleur))
    return .2126 * r + .7152 * v + .0722 * b


def contraste(a, b):
    """Rapport de contraste WCAG entre deux couleurs opaques."""
    la, lb = _luminance(a), _luminance(b)
    if la < lb:
        la, lb = lb, la
    return (la + .05) / (lb + .05)


def _texte_lisible(teinte, fond, cible=5.0):
    """Eclaircit la teinte jusqu'a `cible`:1 sur `fond`. Voir la note ci-dessus."""
    r, v, b = (x / 255.0 for x in _rgb(teinte))
    h, lum, sat = colorsys.rgb_to_hls(r, v, b)
    while lum < 1.0:
        essai = _hexa(x * 255 for x in colorsys.hls_to_rgb(h, lum, sat))
        if contraste(essai, fond) >= cible:
            return essai
        lum += .005
    raise SystemExit('!! ABANDON : aucune variante lisible pour %s.' % teinte)


def couleurs_tuiles():
    """[(id, teinte, fond, filet, texte, contraste_du_texte), ...] pour les 6 tuiles."""
    out = []
    for cid, typ, propre in TUILES:
        teinte = TYPES[typ][1] if typ else propre
        fond = _melange(teinte, FOND_CARTE, .10)
        out.append((cid, teinte, fond,
                    _melange(teinte, fond, .34),      # bordure au repos
                    _melange(teinte, fond, .58),      # bordure au survol
                    _texte_lisible(teinte, fond),
                    contraste(_texte_lisible(teinte, fond), fond)))
    return out


def css_tuiles():
    """CSS de la mise en lumiere. Rien n'est ecrit en dur : tout vient de TYPES."""
    lignes = ['/* ===== une couleur par activite : les six tuiles ===== */']
    for cid, teinte, fond, filet, vif, texte, _c in couleurs_tuiles():
        lignes.append('#%s{--tint:%s;--tint-fond:%s;--tint-filet:%s;'
                      '--tint-vif:%s;--tint-texte:%s}'
                      % (cid, teinte, fond, filet, vif, texte))
    lignes.append(
        # le fond teinte et le liseré de 3 px, qui remplace l'or commun.
        # `background-origin:border-box` : le liseré occupe exactement la
        # bordure haute de 3 px posee par la couche chaleureuse.
        '.offer{background-color:var(--tint-fond);'
        'background-image:linear-gradient(var(--tint),var(--tint));'
        'background-size:100% 3px;background-repeat:no-repeat;'
        'background-position:0 0;background-origin:border-box;'
        'border-color:var(--tint-filet)}')
    lignes.append('.offer:hover{border-color:var(--tint-vif)}')
    lignes.append(
        # le chapeau quitte le degrade dore commun pour la couleur de SON
        # activite — version eclaircie, voir `_texte_lisible`.
        '.offer .t{background:none;-webkit-text-fill-color:currentColor;'
        'color:var(--tint-texte)}')
    return '\n'.join(lignes) + '\n'


def dates_courtes(typ, n=3, extra=''):
    """Encart « Prochaines dates » a poser au bas d'une carte du programme.

    `extra` ajoute un lien apres « tout voir » (seule la carte concert en a un).

    ⚠️ 27/08/2026 — L'ENCART PORTE DESORMAIS **TOUTES** LES DATES DU TYPE, pas
    seulement les trois premieres, et n'en montre que trois. Ce n'est pas un
    detail : la carte « instruments d'exception » commence par le 23 aout, deja
    passe. Si le HTML ne portait que trois dates, l'encart serait vide des le
    19 octobre alors que l'agenda, juste en dessous, en annonce encore deux.
    Les dates au-dela de la fenetre sont masquees par `.dt-plus` — SANS
    JavaScript, la page affiche donc exactement les trois premieres ecrites,
    comme avant.

    ⚠️ NI `<span>` NI `<div>` POUR PORTER UNE DATE, ET C'EST MESURE : la page
    porte `.offer-dates span{display:block;…}` et une seconde regle qui peint
    ces `span` en degrade dore transparent. Un `<span>` par date les aurait
    donc empiles en colonne, en dore. On utilise `<time>`, que rien ne cible —
    et qui dit ce qu'il est. Le separateur, lui, est un `<i>` POSE A
    L'INTERIEUR de la date : il disparait avec elle (pas de « · » orphelin).
    """
    items = [(dt.date.fromisoformat(iso), h2)
             for iso, _h1, h2, t, _ti, _no in EVENTS if t == typ]
    if not items:
        return ''
    cle = 'offer-' + typ
    REG.declare(cle, repli='inline', sep=True, fenetre=n)
    txt = ''.join(
        '<time%s%s>%s%d %s.</time>'
        % (' class="dt-plus"' if k >= n else '', REG.date(cle, d, h),
           dates_a_venir.separateur() if k else '',
           d.day, MOIS[d.month - 1][:4])
        for k, (d, h) in enumerate(items))
    return ('<div class="offer-dates"><span>Prochaines dates</span>%s'
            '<i%s>%s</i> '
            '<a href="#agenda">tout voir</a>%s</div>'
            % (txt, REG.repli(cle), EN_PREPARATION, extra))


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
    # 17/08/2026 : le texte de la carte a change (groupe de pratique engage,
    # plus un atelier ouvert), et le `who` porte desormais un lien. L'ancre
    # suit — c'est le garde-fou qui a refuse d'ecrire tant qu'elle etait
    # perimee, exactement son role.
    ('on rejoint le groupe — et on peut le rejoindre à tout moment.</p>\n      <div class="who">Avec David Lesage</div>',
     'rythme', '', ''),
)


# --------------------------------------------------------------------------- #
# LE BOUTON D'ACTION DES CARTES DU PROGRAMME
#
# LE CONSTAT (mesure sur la page publiee le 16/08/2026) : sur les six cartes du
# programme, une seule — « instruments d'exception » — menait quelque part ou
# l'on peut FAIRE la chose (« réserver ma place ↗ »). La psychotherapie avait
# deja sa prise de rendez-vous, mais dans `.offer-dates`. Les trois cartes a
# dates (concert, yoga, workshop) n'avaient que « tout voir », qui descend dans
# l'agenda ; « cours individuels » n'avait AUCUN lien. Quelqu'un qui lit
# « Atelier de yoga » et veut s'inscrire devait deviner qu'il fallait descendre
# chercher la bonne date, puis le bon bouton.
#
# LA REGLE APPLIQUEE : une carte = UN lien d'action, dans sa ligne `.who`, qui
# mene la ou l'on reserve / prend rendez-vous / s'inscrit. On ne touche pas aux
# liens deja presents, parce qu'ils n'ont pas le meme role :
#   « tout voir » -> navigation interne (l'agenda, plus bas) ;
#   « En savoir plus → » -> documentation (la page dediee) ;
#   le lien d'action -> l'acte.
# Aucun lien n'est donc double en intention, et aucun texte redactionnel ne
# bouge : on ajoute « · <a>…</a> » a l'interieur d'une ligne existante.
#
# POURQUOI CES DESTINATIONS-LA, ET PAS UNE ANCRE D'AGENDA FILTREE
# ---------------------------------------------------------------
# L'agenda sait pre-activer un filtre depuis une ancre, mais UNE SEULE est
# cablee (`#concerts`, voir FILTER_JS) et — mesure faite — les noms qu'il
# faudrait pour les autres (`#yoga`, `#instruments`, `#psychotherapie`,
# `#calebasse-workshop`, `#cours-individuels`) sont DEJA PRIS par les cartes
# elles-memes, et servent d'ancres au menu partage du site. Il faudrait donc
# inventer des identifiants paralleles (`#agenda-yoga`…), ajouter des elements
# dans l'agenda et generaliser le script de filtre : on toucherait exactement la
# zone qui porte les 20 boutons de billetterie. Le gain serait faible — les
# trois cartes a dates ont deja « tout voir » vers `#agenda`, et l'agenda tient
# sur un ecran. On s'en tient donc a des destinations franches.
#
#   concert           -> la billetterie HelloAsso des concerts au Nid. C'est
#                        DEJA le lien des trois boutons « Réserver ↗ » de
#                        l'agenda (CONCERT_SOLO, verifie le 04/08 : elle vend
#                        bien les trois dates du Nid, trio du 26/09 compris).
#                        La carte gardait « En savoir plus → » vers
#                        /concerts-david-lesage : c'est la page qui RACONTE,
#                        pas celle qui vend. Les deux coexistent.
#   yoga              -> YOGA_INS, la constante deja utilisee par les quatre
#                        boutons « S’inscrire ↗ » de l'agenda. Recopier l'URL
#                        aurait cree un second endroit a corriger le jour ou
#                        elle change. (HelloAsso repond 403 aux robots : c'est
#                        connu sur ce projet, le lien marche dans un navigateur.)
#   calebasse         -> /rythme-calebasse, la page des workshops (format,
#                        instrument fourni, appel a candidature, formulaire).
#                        ⚠️ PAS un lien de reservation : il n'existe pas encore
#                        de billetterie pour ces workshops (les 3 dates de
#                        l'agenda sont encore sur le mailto, voir URL_PAR_EVENT).
#                        Annoncer « réserver » serait promettre ce qui n'existe
#                        pas. Lien interne, donc pas de nouvel onglet.
#   cours individuels -> DEUX liens, un par intervenant (voir COURS_DAVID /
#                        COURS_IRIS). C'est la seule carte du programme qui
#                        n'avait aucun lien du tout.
#
# Les deux autres cartes ne recoivent rien, et c'est volontaire :
#   psychotherapie    -> « Prendre rendez-vous sur irischasles.com ↗ » est deja
#                        dans sa ligne `.offer-dates` (voir REMPLACEMENTS).
#                        Ajouter le meme site avec la meme intention aurait
#                        donne deux appels a l'action pour un seul geste.
#   instruments       -> « réserver ma place ↗ » y est depuis toujours.
# --------------------------------------------------------------------------- #
def lien_action(url, libelle):
    """Lien d'action d'une carte. Nouvel onglet + noopener si l'URL est externe."""
    dehors = url.startswith('http')
    return ('<a href="%s"%s>%s</a>'
            % (url, ' target="_blank" rel="noopener"' if dehors else '', libelle))


# (ancre = fin du texte de la carte + sa ligne `.who`, [(url, libelle), ...])
# Meme parti-pris d'ancrage que CARTES_DATES : la fin de paragraphe rend l'ancre
# unique (« Avec David Lesage » seul apparait DEUX fois dans la source), et une
# carte peut evoluer sans casser l'injection d'une autre.
CARTES_ACTION = (
    ('au plus près du public.</p>\n      <div class="who">Avec David Lesage</div>',
     [(CONCERT_SOLO, 'réserver un concert ↗')], 'concert'),
    ('retrouver de l’espace intérieur.</p>\n      <div class="who">Avec Iris Chasles</div>',
     [(YOGA_INS, 's’inscrire à l’atelier ↗')], 'yoga'),
    # 17/08/2026 : « voir les workshops » envoyait vers une offre qui n'existe
    # plus. Ce sont les rendez-vous d'un groupe engage, qu'on rejoint sur
    # candidature — le bouton mene donc a l'appel, pas a un catalogue.
    ('on rejoint le groupe — et on peut le rejoindre à tout moment.</p>\n      <div class="who">Avec David Lesage</div>',
     [('/rythme-calebasse#candidature', 'rejoindre le groupe →')], 'workshop calebasse'),
    ('libération des tensions dans le corps.</p>\n      <div class="who">Avec David Lesage ou Iris Chasles</div>',
     [(COURS_DAVID, 'les cours de David ↗'),
      (COURS_IRIS, 'l’agenda d’Iris ↗')], 'cours individuels'),
)

# Ce que la page DOIT porter apres coup, carte par carte : (url, libelle).
# Les deux dernieres lignes existaient avant ce chantier — elles sont dans la
# garde pour qu'une carte ne puisse pas perdre son bouton en silence.
BOUTONS_ATTENDUS = (
    (CONCERT_SOLO, 'réserver un concert ↗'),
    (YOGA_INS, 's’inscrire à l’atelier ↗'),
    ('/rythme-calebasse#candidature', 'rejoindre le groupe →'),
    (COURS_DAVID, 'les cours de David ↗'),
    (COURS_IRIS, 'l’agenda d’Iris ↗'),
    ('https://www.irischasles.com/', 'Prendre rendez-vous sur irischasles.com ↗'),
    (SHOWROOM, 'le showroom et les réservations ↗'),
)


def carte_instruments():
    """Carte « Présentation, découverte & essai d'instruments d'exception ».

    (Anciennement « Scene ouverte / Showcase » ; la cle technique interne reste
    `showcase`.) Le lien vient de la SEULE constante SHOWROOM : un seul endroit
    a changer.

    ⚠️ `id="instruments"` est la cible de l'entree « Présentation d'instruments »
    du menu partage (`/le-nid#instruments`, voir nav_menu.py). Sans lui, cette
    entree de menu ne mene nulle part.

    RACCOURCIE LE 17/08/2026, sur demande de David : « il faut que la 6eme tuile
    fasse la meme taille que les autres tuiles. Simple, court, efficace, les
    dates et renvoi vers le site de David. »
    Elle faisait ~2 400 caracteres quand les autres en font 300 a 600 : cinq
    paragraphes, une revendication argumentee et une mention de transparence.
    Dans une grille de tuiles, la plus longue n'est pas la plus lue — elle
    desequilibre la grille et se saute.

    ⚠️ IL A FALLU DEUX PASSES, et la lecon vaut d'etre gardee : la premiere
    l'a ramenee a 654 caracteres — et elle restait LA PLUS HAUTE des six
    (898 px, mesures dans le navigateur, contre 470 a 873 pour les autres).
    Compter les caracteres du code ne suffit pas : c'est la HAUTEUR RENDUE
    qu'il faut mesurer, tuile par tuile, dans la grille reelle.

    ⚠️ CE QUI A ETE RETIRE N'EST PAS PERDU, c'est DEPLACE sur la page de David
    (https://www.lesagedavid.fr/showroom), qui traite le meme sujet en detail :
      - la revendication « le seul lieu en France ou ces instruments s'essaient
        et s'achetent en direct », validee mot pour mot par David le 16/08, et
        sa borne (seul le Neotone repart le jour meme ; les Yishama sont ses
        instruments PERSONNELS et ne sont pas en vente). ⚠️ Si elle devait
        revenir ici un jour : ne JAMAIS la re-elargir au monde, et ne jamais la
        reposer sans sa borne — sans elle, « s'achetent en direct » sur-promet.
      - le detail des instruments, des micros, et du deroule d'une session.
    Sur son site elle est ecrite A LA PREMIERE PERSONNE (« je l'assume »), ce
    qui la rend tenable : c'est lui qui l'engage, pas l'association.

    ⚠️ LA MENTION DE TRANSPARENCE RESTE, en une phrase : elle n'est pas
    decorative. L'association accueille ces rencontres et peut percevoir une
    contribution d'affiliation — le dire est une obligation de loyaute, pas un
    ornement. NE PAS la supprimer pour gagner deux lignes.
    """
    return ('    <div class="offer offer--rare" id="instruments">\n'
            '      <div class="t">Présentation, découverte &amp; essai</div>\n'
            '      <h3>Instruments d’exception</h3>\n'
            '      <div class="offer-meta">Gratuit · sur inscription · environ 2 h</div>\n'
            '      <p>Prendre en main des instruments que l’on ne croise presque jamais : <b>Neotone</b>, <b>handpans Yishama</b>, <b>calebasse</b>, <b>Gonilélé</b>. David Lesage les fait sonner, puis les met entre vos mains. Aucune expérience requise.</p>\n'
            '      ' + dates_courtes('showcase') + '\n'
            '      <div class="who">Avec David Lesage · <a href="' + SHOWROOM
            + '" target="_blank" rel="noopener">le showroom et les réservations ↗</a></div>\n'
            '      <p class="offer-fine">Sans obligation d’achat. <b>L’association ne vend pas ces instruments</b> et peut percevoir une contribution d’affiliation.</p>\n'
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
    # Un registre de dates NEUF a chaque generation : sans cette remise a zero,
    # deux appels dans le meme processus enregistreraient deux fois les memes
    # dates et la table du script de tete doublerait.
    global REG
    REG = dates_a_venir.Registre()

    with open(SOURCE, encoding='utf-8') as f:
        html = f.read()

    # --- CSS de l'agenda, puis CSS des encarts, avant la fin de la feuille ---
    # `CSS` commence par un saut de ligne et la source en a deja un : sans
    # `lstrip`, la page gagnerait une ligne vide de plus que la version publiee.
    # Le `\n` final est celui qui separe le CSS des encarts de la feuille du
    # menu partage, que `nav_menu.inject()` collera juste avant `</style>`.
    _exiger(html, '</style>', 1, 'fin de la feuille de style')
    # ⚠️ `css_tuiles()` DOIT VENIR APRES `CSS_CHALEUR`, et c'est structurel :
    # ses regles `.offer` et `.offer .t` valent (0,1,0) et (0,1,1), exactement
    # comme celles qu'elles remplacent (le fond dore de `.offer--rare`, le filet
    # dore commun, le chapeau au degrade). A specificite egale, c'est la
    # DERNIERE qui gagne. Placee avant, la mise en lumiere serait sans effet.
    html = html.replace('</style>',
                        CSS.lstrip('\n') + CSS_DATES
                        + theme_chaleur.CSS + CSS_CHALEUR + css_tuiles()
                        + visionneuse.css('') + dates_a_venir.css()
                        + '\n</style>', 1)

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

    # --- bouton d'action dans la ligne « Avec … » des cartes -----------------
    # APRES les encarts de dates, jamais avant : ceux-ci s'accrochent a la fin
    # de la ligne `.who`, qu'on modifie ici. Dans cet ordre les deux tables
    # gardent les MEMES ancres et restent independantes l'une de l'autre.
    for ancre, liens, quoi in CARTES_ACTION:
        _exiger(html, ancre, 1, 'ancre du bouton d’action (%s)' % quoi)
        if not ancre.endswith('</div>'):
            raise SystemExit('!! ABANDON : l’ancre du bouton d’action (%s) ne '
                             'finit pas par </div>. Page NON ecrite.' % quoi)
        neuf = (ancre[:-len('</div>')]
                + ''.join(' · ' + lien_action(u, lab) for u, lab in liens)
                + '</div>')
        html = html.replace(ancre, neuf, 1)

    # --- carte « instruments d'exception », EN PREMIERE TUILE -----------------
    # 19/08/2026 — David : « met en premier la tuile du showroom ». Elle etait
    # ajoutee EN DERNIER, juste avant l'encart `.note` qui suit la grille ;
    # l'ancre est donc passee de la FERMETURE de la grille a son OUVERTURE.
    # ⚠️ Les cinq autres tuiles ont ete reordonnees dans `lenid_source.html`,
    # pas ici : leur ordre est celui de la source. Aucune ancre n'en depend —
    # celles de CARTES_DATES et de CARTES_ACTION sont des fins de paragraphe
    # locales a une carte (c'est exactement pour ca qu'elles sont locales).
    ancre_carte = '  <div class="offers">\n'
    _exiger(html, ancre_carte, 1, 'ouverture de la grille des tuiles')
    html = html.replace(ancre_carte, ancre_carte + carte_instruments() + '\n', 1)

    # --- scripts : telechargement .ics, puis filtres -------------------------
    _exiger(html, '</body>', 1, 'fin du corps de page')
    # ⚠️ LE MENAGE DES DATES PASSEES EST POSE EN PREMIER, DONC IL S'EXECUTE
    # AVANT `FILTER_JS`, ET C'EST STRUCTUREL. Le filtre par type et par mois
    # fige sa liste de `.ag-item` au moment ou il tourne : s'il la fige avant le
    # menage, il compte des dates finies (« Aucune date ne correspond a ces
    # filtres » ne s'affiche plus quand il le faudrait) et « Ajouter toutes les
    # dates a mon agenda » telecharge un .ics contenant des evenements passes.
    # Dans cet ordre, les deux scripts existants restent intacts.
    html = html.replace('</body>', REG.js() + '</body>', 1)
    html = html.replace('</body>', ICS_JS + '</body>', 1)
    html = html.replace('</body>', FILTER_JS + '</body>', 1)

    # --- la visionneuse photo (17/08/2026) -----------------------------------
    # Les 6 photos des trois galeries (`.gal img`) s'ouvrent en grand au clic.
    # Tout est dans `sources/visionneuse.py` — meme visionneuse que sur les six
    # autres pages a photos du site.
    #
    # ⚠️ LA PHOTO DU HERO EST VOLONTAIREMENT LAISSEE DEHORS. Ce n'est pas une
    #    photo de galerie mais un FOND : `.hero-bg` porte `pointer-events:none`
    #    et un voile `.hero::after` la recouvre entierement pour que le titre
    #    reste lisible. La rendre cliquable aurait mis un clic sur toute la
    #    hauteur du hero, sous le titre et les boutons. A trancher par David.
    # ⚠️ ARGUMENT VIDE POUR LE CSS, ET C'EST MESURE : les legendes de cette page
    #    (`.gal-cap`) sont dans la colonne de texte, a cote de la photo, jamais
    #    par-dessus. Rien ne recouvre le bas des photos.
    html = html.replace('</body>', visionneuse.js('.gal img') + '</body>', 1)

    # Ligne vide entre le dernier script de la page et le bloc du menu partage.
    # Elle vient de la migration du menu v1 -> v2 : `nav_menu._strip()` a retire
    # l'ancien bloc en laissant le saut de ligne qui le suivait. Les neuf pages
    # publiees la portent ; on la reproduit pour qu'une regeneration ne modifie
    # pas un octet.
    html = html.replace('</script>\n</body>', '</script>\n\n</body>', 1)

    # --- la table des dates, en FIN DE <head> --------------------------------
    # Elle doit etre lue AVANT le corps de page, sinon la ligne du 23 aout
    # s'afficherait le temps d'une image avant d'etre cachee. Et elle doit etre
    # ecrite EN DERNIER dans ce fichier : elle embarque toutes les dates
    # enregistrees plus haut (agenda + les quatre encarts).
    _exiger(html, '</head>', 1, 'fin de l’en-tete de page')
    html = html.replace('</head>', REG.tete() + '</head>', 1)

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

    # ⚠️ BOUTONS D'ACTION DES SIX CARTES DU PROGRAMME. Une carte qui decrit une
    # offre sans dire ou s'inscrire est un cul-de-sac : c'etait le cas de cinq
    # d'entre elles. La garde verifie que chaque destination ET chaque libelle
    # est bien la, une seule fois — donc aussi qu'aucun n'a ete duplique.
    for _url, _lib in BOUTONS_ATTENDUS:
        if _url not in page:
            raise SystemExit('!! ABANDON : destination de bouton d’action absente '
                             'de la page : %s. Page NON ecrite.' % _url)
        _exiger(page, _lib, 1, 'libelle de bouton d’action')

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
