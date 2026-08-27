# -*- coding: utf-8 -*-
"""L'agenda Google du Nid ecrit le site, tout seul, toutes les nuits.

    python3 sources/synchro_agenda.py               # ESSAI : dit tout, n'ecrit rien
    python3 sources/synchro_agenda.py --appliquer   # ecrit, reconstruit, verifie

CE QUE CE FICHIER REMPLACE
--------------------------
Les dates du site etaient RECOPIEES A LA MAIN dans `EVENTS`
(`generate_agenda_nid.py`). C'est de la que venaient les contradictions entre
l'agenda et le site — le 20/08/2026, /le-nid annoncait 18h30 la ou l'agenda
Google disait 19h00. Et une page fabriquee le 20 aout ne sait pas qu'on est le
27 : `sources/dates_a_venir.py` (la « rustine de niveau 1 ») fait bien
disparaitre les dates finies dans le navigateur, mais le HTML livre ne gagne
JAMAIS de date nouvelle. Il ne fait qu'en perdre.

Ce script est le niveau 2. Chaque nuit, sans personne et sans aucune IA :

    flux public .ics de l'agenda Google
              |
              +--  on ne garde que les evenements A VENIR
              +--  ... dont le titre figure dans CORRESPONDANCE ci-dessous
              |
              v
    EVENTS, reecrit dans sources/generate_agenda_nid.py
              |
              +--  build.py           (les 31 pages, deux passes)
              +--  verif_site.py      (31/31, sinon on remet tout comme avant)
              +--  verif_commentaires.py
              |
              v
    git commit + git push  (fait par le workflow, pas par ce script)
              |
              v
    Vercel publie tout seul, ~40 s plus tard

⚠️ CE SCRIPT NE TOUCHE JAMAIS A GIT. Il lit, il ecrit deux fichiers de
   `sources/`, il reconstruit et il verifie. Le commit et la publication sont
   la responsabilite de `.github/workflows/agenda-du-nid.yml`. On peut donc le
   lancer a la main sans rien risquer de publier.

╔══════════════════════════════════════════════════════════════════════════╗
║  POURQUOI IL Y A AUTANT DE GARDE-FOUS                                     ║
╚══════════════════════════════════════════════════════════════════════════╝
Un script qui publie tout seul sur un site public, sans relecture humaine, est
dangereux — et le danger n'est pas theorique sur ce projet :

  * l'agenda du Nid a DEJA contenu 13 evenements PRIVES ;
  * le code du portail a DEJA fuite deux fois sur ce depot, qui est PUBLIC ;
  * les descriptions de l'agenda Google contiennent encore la phrase « Le code
    du portail vous est communique avec votre confirmation ».

D'ou les cinq regles ci-dessous. Aucune n'est negociable.

1. RIEN DU FLUX N'EST PUBLIE, SAUF UNE DATE ET DEUX HEURES.
   Le titre affiche sur le site et sa note (« avec Iris Chasles ») ne viennent
   PAS de l'agenda : ils sont ecrits une fois pour toutes dans CORRESPONDANCE.
   Les descriptions, les lieux, les invites et les identifiants d'evenements ne
   sont meme pas conserves par le lecteur de flux : ils sont jetes a la lecture.
   Le script le VERIFIE ensuite (`_controle_fuite`) plutot que de le croire.

2. LISTE BLANCHE DE TITRES, PAS DE DEVINETTE.
   Un evenement est publie si — et seulement si — son titre est DANS la table
   CORRESPONDANCE. Pas de « ca ressemble a un concert » : une correspondance
   exacte, ou rien. Tout titre inconnu est IGNORE et SIGNALE.
   ⚠️ Consequence pratique, a dire a David : pour ajouter une date au site, le
      plus sur est de DUPLIQUER un evenement existant dans Google Agenda et de
      changer sa date. Le titre est alors exact par construction.

3. EN CAS DE DOUTE, ON NE PUBLIE PAS. Un evenement sans heure (« journee
   entiere »), un evenement qui se repete (RRULE), un evenement annule : ignore
   et signale. Jamais publie « au cas ou ».

4. UN CHANGEMENT MASSIF ARRETE TOUT. Si une execution devait faire disparaitre
   plus de la moitie des dates, ou en ajouter un nombre aberrant, le script
   s'arrete sans rien ecrire. Un agenda vide par erreur — ou un flux tronque —
   ne doit pas vider le site.

5. LA CHAINE DE VERIFICATION DU PROJET PASSE AVANT TOUT. `build.py` (deux
   passes), `verif_site.py` (31/31) et `verif_commentaires.py`. Si l'un des
   trois echoue, les fichiers modifies sont REMIS EXACTEMENT COMME AVANT, le
   site est reconstruit dans son etat d'origine, et le script sort en erreur :
   le workflow ne commite rien.

╔══════════════════════════════════════════════════════════════════════════╗
║  AJOUTER UN NOUVEAU TYPE D'EVENEMENT AU SITE                             ║
╚══════════════════════════════════════════════════════════════════════════╝
1. Ecrire une ligne dans CORRESPONDANCE : le titre EXACT tel qu'il est dans
   Google Agenda, puis le type, le titre a afficher et la note.
2. Le type doit exister dans `TYPES` de `generate_agenda_nid.py` (c'est lui qui
   porte la couleur, le libelle du badge et le lien de reservation). Le script
   RELIT cette liste et refuse de demarrer si un type invente s'y glisse.
3. Lancer l'essai, lire ce qu'il dit, puis `--appliquer`.

LES OPTIONS
-----------
    --appliquer          ecrire pour de vrai (defaut : essai, aucune ecriture)
    --flux FICHIER|URL   lire un autre flux (un fichier .ics local, pour tester)
    --date AAAA-MM-JJ    faire comme si on etait ce jour-la, heure de Paris
    --rapport FICHIER    ecrire les signalements dans ce fichier (le workflow
                         s'en sert pour prevenir David ; vide = rien a signaler)
"""
import argparse
import datetime as dt
import os
import re
import subprocess
import sys
import unicodedata
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(HERE)
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import dates_a_venir  # le calcul d'heure de Paris, en un seul exemplaire  # noqa: E402
import verif_site  # ses motifs de fuite de donnees, reutilises tels quels  # noqa: E402

#: le fichier qui porte la liste des dates du site
AGENDA = os.path.join(HERE, 'generate_agenda_nid.py')
#: les deux balises qui encadrent la liste. Ce qui est entre elles est REECRIT.
# ⚠️ TOUT CE QUI SE TROUVE ENTRE CES DEUX BALISES EST REECRIT A CHAQUE
# SYNCHRONISATION. Les commentaires places la-dedans sont EFFACES.
#
# Constate le 27/08/2026, une heure apres la mise en service : une note de
# quatre lignes expliquant pourquoi le concert du 28 novembre n'est plus
# annonce « solo » avait ete ecrite au milieu du bloc. La premiere execution
# reelle l'a supprimee — sans rien casser, mais en emportant la memoire du
# POURQUOI. Sur ce projet, le pourquoi vaut autant que le quoi : c'est lui
# qui empeche de defaire dans six mois une decision prise aujourd'hui.
#
# 🚨 REGLE : une note qui doit survivre se met AU-DESSUS de la balise DEBUT,
# jamais entre les deux. Le bloc synchronise ne contient que des donnees.
DEBUT = '# --- DEBUT DES DATES SYNCHRONISEES (ecrit par sources/synchro_agenda.py) ---'
FIN = '# --- FIN DES DATES SYNCHRONISEES ---'


# --------------------------------------------------------------------------- #
#                          LA LISTE BLANCHE
# --------------------------------------------------------------------------- #
#
#   ┌──────────────────────────────────────────────────────────────────────┐
#   │  A GAUCHE : le titre EXACT de l'evenement dans Google Agenda.        │
#   │  A DROITE : ce que le site en fait — son type, son titre, sa note.   │
#   │  Un titre absent de ce tableau N'EST PAS PUBLIE. Il est signale.     │
#   └──────────────────────────────────────────────────────────────────────┘
#
# ⚠️ LE TITRE AFFICHE SUR LE SITE N'EST PAS CELUI DE L'AGENDA, ET C'EST VOULU.
# 🚨 PRINCIPE POSE PAR DAVID LE 27/08/2026, il tranche les futurs desaccords :
#
#    « on garde toujours ce que dit l'agenda Google comme etant la derniere
#      source de verite, la plus a jour »
#
#    Quand l'agenda et le site divergent, C'EST LE SITE QU'ON CORRIGE. Premiere
#    application le 27/08 : l'agenda annoncait « + Guest Lucie au violon » pour
#    le 28 novembre, le site ecrivait « solo » — le site a ete corrige.
#
#    ⚠️ CE PRINCIPE NE VEUT PAS DIRE QUE LE SCRIPT RECOPIE LES TITRES. Il ne le
#    fera jamais : un titre d'agenda peut contenir un nom, un numero, une note
#    perso. Le mecanisme est celui-ci, et il est deja en place :
#      - David modifie un titre dans son agenda ;
#      - ce titre n'est plus dans la table ci-dessous ;
#      - l'evenement est ECARTE et SIGNALE (mail GitHub) — il ne disparait pas
#        du site pour autant, l'ancienne ligne reste tant qu'on n'a pas tranche ;
#      - un humain lit le signalement et met la table a jour.
#    Autrement dit : l'agenda fait foi, mais un humain valide la formulation
#    avant qu'elle soit publique. C'est le seul assemblage qui respecte a la
#    fois le principe de David et le depot PUBLIC.
#
#    L'agenda dit « Concert de David Lesage — Le Nid + Guest Lucie au violon » ;
#    le site ecrit « Concert — David Lesage solo ». L'agenda dit « Concert
#    Sortie de residence — Le Nid » ; le site ecrit « Sortie de residence ».
#    C'est de la redaction, elle a ete validee, elle ne se devine pas depuis un
#    titre de calendrier. C'est aussi ce qui garantit qu'un emoji, un nom
#    d'invite ou une note personnelle glisses dans un titre d'agenda ne peuvent
#    PAS atterrir sur le site.
#
# ⚠️ LA COMPARAISON EST TOLERANTE SUR LA TYPOGRAPHIE, PAS SUR LES MOTS : les
#    espaces multiples, la casse et l'apostrophe droite/courbe sont neutralisees
#    (`_cle()`), rien d'autre. « Atelier yoga » ne vaut PAS « Atelier de yoga » :
#    ce sont deux titres differents, et deviner lequel David voulait dire est
#    exactement ce qu'on refuse de faire.
CORRESPONDANCE = {
    # --- les rendez-vous mensuels ---
    'INSTATIC Dance — Le Nid':
        ('mensuel', 'INSTATIC Dance', 'avec Iris & David'),
    'Rendez-vous mensuel au Nid':
        ('mensuel', 'Rendez-vous mensuel au Nid', ''),
    # --- les concerts ---
    'Concert de David Lesage — Le Nid':
        ('concert', 'Concert — David Lesage solo', ''),
    # ⚠️ Meme evenement, meme intitule sur le site. L'agenda porte en plus le
    #    nom de l'invitee ; le site n'a jamais annonce cette date autrement que
    #    « David Lesage solo ». On ne change pas une annonce publiee sans que
    #    David le decide : la ligne reproduit ce qui est en ligne aujourd'hui.
    'Concert de David Lesage — Le Nid + Guest Lucie au violon':
        ('concert', 'Concert — David Lesage', 'avec Lucie au violon'),
    'Concert RITUALS trio — David, Iris & Julien — Le Nid':
        ('concert', 'Concert — David, Iris & Julien', 'le trio en concert'),
    'Concert Sortie de résidence — Le Nid':
        ('residence', 'Sortie de résidence', 'restitution du travail en trio'),
    # --- les ateliers ---
    'Atelier de yoga — Le Nid':
        ('yoga', 'Atelier de yoga', 'avec Iris Chasles'),
    # ⚠️ « Groupe de pratique », et surtout PAS « atelier » : David a tranche le
    #    17/08/2026, ces rendez-vous ne sont pas ouverts a la seance, on les
    #    rejoint sur candidature. Le libelle et le bouton en dependent.
    'Groupe de pratique rythme calebasse engagé — Le Nid':
        ('rythme', 'Groupe de pratique rythme calebasse engagé',
         'avec David Lesage · sur candidature'),
    'Présentation d’instruments d’exception — Le Nid':
        ('showcase', 'Présentation d’instruments d’exception', ''),
}

#: les titres qu'on IGNORE VOLONTAIREMENT, avec la raison. Ils ne sont pas
#: publies ET ils ne declenchent pas d'alerte — c'est la seule difference avec
#: un titre inconnu.
#: ⚠️ N'y mettre QUE des evenements dont on est sur qu'ils n'ont rien a faire
#:    sur le site (un rendez-vous personnel, un rappel interne). Un evenement
#:    range ici disparait en silence : c'est exactement ce qu'on veut eviter
#:    pour une vraie date. Dans le doute, ne rien ecrire ici — le signalement
#:    est fait pour ca.
#: Exemple de ligne :  'Menage du Nid': 'organisation interne, pas un evenement',
IGNORER = {}


# --------------------------------------------------------------------------- #
# LES CHIFFRES DES GARDE-FOUS
# --------------------------------------------------------------------------- #
#: on refuse d'appliquer si la moitie (ou plus) des dates a venir disparaissait
#: d'un coup. Un flux tronque, un agenda vide par erreur, une panne de Google
#: qui renvoie une page a moitie ecrite : tout ca ressemble a « il n'y a plus
#: rien », et il ne faut surtout pas le recopier sur le site.
#: (Le cas normal — une seule date qui passe — ne fait jamais perdre la moitie
#: de la liste tant qu'il reste au moins deux dates a venir, et le site en porte
#: une vingtaine.)
PERTE_MAX = 0.5
#: on refuse aussi une arrivee massive : un agenda dont quelqu'un aurait
#: reimporte tout l'historique, par exemple. David peut tres bien poser une
#: saison entiere d'un coup — dans ce cas le script refuse, le dit, et un humain
#: applique une fois a la main. Mieux vaut ce derangement-la que l'inverse.
AJOUTS_MAX = 15


# --------------------------------------------------------------------------- #
# LECTURE DU FLUX .ics
# --------------------------------------------------------------------------- #
#: LES SEULES PROPRIETES QUE LE LECTEUR CONSERVE. Tout le reste — DESCRIPTION,
#: LOCATION, ATTENDEE, ORGANIZER, UID, X-* — est jete a la lecture, avant meme
#: d'exister en memoire. C'est la premiere barriere contre la publication d'une
#: donnee personnelle : on ne filtre pas ce qu'on a garde, on ne garde pas.
GARDEES = ('DTSTART', 'DTEND', 'SUMMARY', 'RRULE', 'STATUS')


def _texte_ical(v):
    """Deplie les echappements du format iCalendar (RFC 5545)."""
    out, i = [], 0
    while i < len(v):
        c = v[i]
        if c == '\\' and i + 1 < len(v):
            suivant = v[i + 1]
            out.append({'n': '\n', 'N': '\n'}.get(suivant, suivant))
            i += 2
        else:
            out.append(c)
            i += 1
    return ''.join(out)


def lire_flux(brut):
    """Le texte d'un .ics -> une liste de dictionnaires a cinq clefs maximum."""
    # depliage des lignes longues (RFC 5545 : une ligne coupee reprend par une
    # espace ou une tabulation)
    texte = brut.replace('\r\n', '\n').replace('\r', '\n')
    texte = re.sub(r'\n[ \t]', '', texte)
    if 'BEGIN:VCALENDAR' not in texte:
        raise Refus('le flux recu n’est pas un calendrier iCalendar '
                    '(pas de « BEGIN:VCALENDAR »). Rien n’a ete touche.')
    evenements = []
    for corps in re.findall(r'BEGIN:VEVENT\n(.*?)\nEND:VEVENT', texte, re.S):
        ev = {}
        for ligne in corps.split('\n'):
            if ':' not in ligne:
                continue
            gauche, valeur = ligne.split(':', 1)
            nom = gauche.split(';', 1)[0].strip().upper()
            if nom not in GARDEES:
                continue          # <- la donnee personnelle s'arrete ici
            ev[nom] = (gauche, _texte_ical(valeur).strip())
        if ev:
            evenements.append(ev)
    if not evenements:
        raise Refus('le flux ne contient aucun evenement. C’est peut-etre une '
                    'panne passagere de Google : on ne vide pas le site '
                    'la-dessus. Rien n’a ete touche.')
    return evenements


# --------------------------------------------------------------------------- #
# HEURES : le flux est en UTC, le site publie des heures de Paris
# --------------------------------------------------------------------------- #
# ⚠️ LE CALCUL DU DECALAGE N'EST PAS REECRIT ICI. Il vit dans
#    `dates_a_venir._offset_paris()`, qui connait le vrai changement d'heure
#    (dernier dimanche de mars, dernier dimanche d'octobre). Un second calcul,
#    meme juste, serait un second calcul a corriger.

def _en_paris(quand_utc):
    """Un instant UTC -> l'heure de Paris correspondante."""
    # premiere approximation avec le decalage du jour UTC, puis on recalcule
    # avec le jour de Paris obtenu : les deux ne different qu'autour de minuit,
    # ou aucun evenement du Nid ne commence.
    dec = dates_a_venir._offset_paris(quand_utc.date())
    local = quand_utc + dt.timedelta(hours=dec)
    dec2 = dates_a_venir._offset_paris(local.date())
    return quand_utc + dt.timedelta(hours=dec2)


def _instant(gauche, valeur):
    """Une valeur DTSTART/DTEND -> un instant UTC, ou None si on ne sait pas.

    On n'accepte QUE la forme UTC (« 20260904T170000Z »), celle que Google
    publie pour un agenda public. Une date sans heure (« journee entiere ») ou
    une heure attachee a un fuseau nomme renvoie None : l'evenement sera ignore
    et signale, jamais publie avec un horaire suppose.
    """
    if 'VALUE=DATE' in gauche.upper():
        return None
    if not re.fullmatch(r'\d{8}T\d{6}Z', valeur):
        return None
    return dt.datetime.strptime(valeur, '%Y%m%dT%H%M%SZ')


class Refus(Exception):
    """Un garde-fou s'est declenche. On n'ecrit rien, on explique, on sort."""


# --------------------------------------------------------------------------- #
# COMPARAISON DES TITRES
# --------------------------------------------------------------------------- #

def _cle(titre):
    """Le titre, debarrasse de ce qui n'est que de la typographie.

    Espaces multiples, casse, forme de l'apostrophe et decomposition Unicode.
    RIEN D'AUTRE : ni accents, ni ponctuation, ni « mots vides ». Chaque
    tolerance en plus est une chance de publier le mauvais evenement.
    """
    t = unicodedata.normalize('NFC', titre)
    t = t.replace('\u2019', "'").replace('\u02bc', "'").replace('\u2018', "'")
    t = re.sub(r'\s+', ' ', t).strip()
    return t.casefold()


TABLE = {_cle(k): v for k, v in CORRESPONDANCE.items()}
TABLE_IGNORE = {_cle(k): v for k, v in IGNORER.items()}


# --------------------------------------------------------------------------- #
# LA LISTE ACTUELLE, LUE DANS LE GENERATEUR
# --------------------------------------------------------------------------- #

def _source_agenda():
    with open(AGENDA, encoding='utf-8') as f:
        return f.read()


def types_connus(src):
    """Les types que le site sait afficher, LUS dans `TYPES`, jamais recopies."""
    bloc = re.search(r'^TYPES = \{(.*?)^\}', src, re.M | re.S)
    if not bloc:
        raise Refus('le dictionnaire TYPES est introuvable dans '
                    'generate_agenda_nid.py. Rien n’a ete touche.')
    return set(re.findall(r"^\s*'([a-z]+)':", bloc.group(1), re.M))


def evenements_actuels(src):
    """Les lignes de EVENTS telles qu'elles sont ecrites aujourd'hui."""
    bloc = _bloc_actuel(src)
    return re.findall(
        r"\('(\d{4}-\d{2}-\d{2})',\s*'(\d\d:\d\d)',\s*'(\d\d:\d\d)',\s*'([a-z]+)'",
        bloc)


def _bloc_actuel(src):
    if DEBUT not in src or FIN not in src:
        raise Refus('les balises « DEBUT / FIN DES DATES SYNCHRONISEES » sont '
                    'introuvables dans generate_agenda_nid.py. Sans elles, on '
                    'ne sait pas quoi remplacer. Rien n’a ete touche.')
    return src.split(DEBUT, 1)[1].split(FIN, 1)[0]


def surcharges(src):
    """Les billetteries surchargees par evenement : {(date, heure): 1}."""
    bloc = re.search(r'^URL_PAR_EVENT = \{(.*?)^\}', src, re.M | re.S)
    if not bloc:
        return {}
    return {(d, h) for d, h in
            re.findall(r"\('(\d{4}-\d{2}-\d{2})',\s*'(\d\d:\d\d)'\)",
                       bloc.group(1))}


# --------------------------------------------------------------------------- #
# ECRITURE DU BLOC
# --------------------------------------------------------------------------- #

def _litteral(texte):
    """Le texte, en chaine Python entre apostrophes droites.

    On REFUSE plutot que d'echapper une contre-oblique ou un retour a la ligne :
    ces caracteres n'ont rien a faire dans un titre d'evenement, et les
    accepter serait ouvrir une porte pour une valeur qu'on n'a pas prevue.
    """
    if '\\' in texte or '\n' in texte:
        raise Refus('le texte « %s » contient un caractere interdit dans un '
                    'titre publie. Rien n’a ete touche.' % texte[:40])
    return "'" + texte.replace("'", "\\'") + "'"


def bloc(evs, largeur):
    lignes = ['EVENTS = [']
    for iso, h1, h2, typ, titre, note in evs:
        lignes.append("    (%s, %s, %s, %-*s %s, %s)," % (
            _litteral(iso), _litteral(h1), _litteral(h2),
            largeur, _litteral(typ) + ',', _litteral(titre), _litteral(note)))
    lignes.append(']')
    return '\n'.join(lignes)


def _controle_fuite(texte, table):
    """Rien d'autre que la table n'a pu atteindre le bloc. On le VERIFIE.

    Deux passes, volontairement redondantes :
      1. chaque titre et chaque note publies sont, mot pour mot, une valeur de
         CORRESPONDANCE — donc ecrits par un humain, pas repris du flux ;
      2. les motifs de fuite du projet (`verif_site`) sont repasses sur le bloc :
         code d'acces, telephone, adresse email. C'est le controle qui a deja
         attrape un code de portail deux fois.
    """
    autorises = set()
    for typ, titre, note in table.values():
        autorises |= {typ, titre, note}
    for _iso, _h1, _h2, typ, titre, note in texte:
        for morceau in (typ, titre, note):
            if morceau not in autorises:
                raise Refus('« %s » n’est pas un texte de la table de '
                            'correspondance : il vient donc du flux. C’est '
                            'exactement ce qui ne doit jamais arriver. Rien '
                            'n’a ete touche.' % morceau[:60])


def _controle_motifs(bloc_texte):
    """Les motifs de fuite de `verif_site.py`, repasses sur le bloc ecrit."""
    pbs = []
    mots = '|'.join(re.escape(m) for m in verif_site.MOTS_CODE)
    re_code = re.compile(r'(?i)\b(%s)\b([^<>]{0,45}?)'
                         r'\b([A-Za-z]{0,3}[0-9]{3,6}[A-Za-z]{0,2})\b' % mots)
    for m in re_code.finditer(bloc_texte):
        contexte = ' '.join(m.group(0).split())
        if not any(x in contexte.lower() for x in verif_site.CODES_HORS_SOUPCON):
            pbs.append('code d’acces possible : « %s »' % contexte[:80])
    for m in set(re.findall(r'[\w.+-]+@[\w.-]+\.[a-z]{2,}', bloc_texte, re.I)):
        if m.lower() not in verif_site.EMAILS_AUTORISES:
            pbs.append('adresse email non prevue : « %s »' % m)
    for m in set(re.findall(r'(?:\+33[\s.\-]?|0)[1-9](?:[\s.\-]?\d{2}){4}',
                            bloc_texte)):
        pbs.append('numero de telephone : « %s »' % m)
    if pbs:
        raise Refus('le bloc a ecrire contient ce qui ne doit jamais etre '
                    'publie : %s. Rien n’a ete touche.' % ' · '.join(pbs))


# --------------------------------------------------------------------------- #
# LA CHAINE DE VERIFICATION DU PROJET
# --------------------------------------------------------------------------- #

def _lancer(script, *args):
    return subprocess.run([sys.executable, os.path.join(HERE, script)]
                          + list(args), cwd=RACINE,
                          capture_output=True, text=True)


def chaine_de_verification(dit):
    """build.py (deux passes) + verif_site.py + verif_commentaires.py.

    Renvoie None si tout passe, sinon le message a afficher. `build.py` fait
    deja tourner `verif_site.py` a la fin et remet les pages en etat s'il
    echoue ; on le relance ensuite pour avoir son code de sortie en propre, et
    on ajoute `verif_commentaires.py`, qui n'est pas dans sa chaine.
    """
    for script, quoi in (('build.py', 'la reconstruction du site'),
                         ('verif_site.py', 'la verification des 31 pages'),
                         ('verif_commentaires.py',
                          'le controle des commentaires HTML')):
        dit('  · %s…' % quoi)
        r = _lancer(script)
        if r.returncode != 0:
            sortie = (r.stdout or '') + (r.stderr or '')
            return '%s a echoue :\n%s' % (quoi, sortie.strip()[-2500:])
    return None


# --------------------------------------------------------------------------- #
# LE PROGRAMME
# --------------------------------------------------------------------------- #

def flux_par_defaut(src):
    """L'adresse du flux public, CONSTRUITE depuis le CAL_ID du generateur.

    ⚠️ L'identifiant fait 79 caracteres. Le recopier ici, c'est se donner une
    chance de se tromper d'une lettre et de synchroniser le site sur un
    calendrier vide. Il est donc LU chez son auteur, comme le fait deja
    `generate_rdv_mensuels._calendrier()`.
    """
    m = re.search(r"^CAL_ID = '([^']+)'", src, re.M)
    if not m:
        raise Refus('CAL_ID est introuvable dans generate_agenda_nid.py : on '
                    'ne sait pas quel calendrier lire. Rien n’a ete touche.')
    return ('https://calendar.google.com/calendar/ical/'
            + urllib.parse.quote(m.group(1), safe='') + '/public/basic.ics')


def charger(adresse):
    if not adresse.startswith(('http://', 'https://')):
        with open(adresse, encoding='utf-8') as f:
            return f.read()
    requete = urllib.request.Request(
        adresse, headers={'User-Agent': 'resonances-site/synchro-agenda'})
    with urllib.request.urlopen(requete, timeout=60) as r:
        if r.status != 200:
            raise Refus('le flux a repondu %s. Rien n’a ete touche.' % r.status)
        return r.read().decode('utf-8', 'replace')


def trier(evs):
    return sorted(evs, key=lambda e: (e[0], e[1]))


def main(argv=None):
    ap = argparse.ArgumentParser(
        description='Ecrit les dates du site depuis l’agenda Google du Nid.')
    ap.add_argument('--appliquer', action='store_true',
                    help='ecrire pour de vrai (defaut : essai, aucune ecriture)')
    ap.add_argument('--flux', help='un autre flux (fichier .ics local ou URL)')
    ap.add_argument('--date', help='faire comme si on etait ce jour-la (AAAA-MM-JJ)')
    ap.add_argument('--rapport', help='fichier ou ecrire les signalements')
    args = ap.parse_args(argv)

    lignes = []

    def dit(texte=''):
        lignes.append(texte)
        print(texte, flush=True)

    signalements = []
    try:
        code = _travailler(args, dit, signalements)
    except Refus as e:
        dit()
        dit('  REFUS — %s' % e)
        dit()
        code = 1

    if args.rapport:
        with open(args.rapport, 'w', encoding='utf-8') as f:
            f.write('\n'.join(signalements))
    resume = os.environ.get('GITHUB_STEP_SUMMARY')
    if resume:
        with open(resume, 'a', encoding='utf-8') as f:
            f.write('```\n' + '\n'.join(lignes) + '\n```\n')
    return code


def _travailler(args, dit, signalements):
    src = _source_agenda()
    connus = types_connus(src)
    inconnus = sorted({t for t, _ti, _n in CORRESPONDANCE.values()} - connus)
    if inconnus:
        raise Refus('la table de correspondance parle de type(s) que le site ne '
                    'sait pas afficher : %s. Les types possibles sont %s (dict '
                    'TYPES de generate_agenda_nid.py). Rien n’a ete touche.'
                    % (', '.join(inconnus), ', '.join(sorted(connus))))

    if args.date:
        jour = dt.date.fromisoformat(args.date)
        maintenant = dt.datetime(jour.year, jour.month, jour.day, 4, 0) \
            - dt.timedelta(hours=dates_a_venir._offset_paris(jour))
    else:
        maintenant = dt.datetime.now(dt.timezone.utc).replace(tzinfo=None)

    adresse = args.flux or flux_par_defaut(src)
    dit()
    dit('  SYNCHRONISATION DE L’AGENDA DU NID')
    dit('  ' + '-' * 74)
    dit('  Mode      : %s' % ('APPLIQUER (les fichiers seront ecrits)'
                              if args.appliquer
                              else 'ESSAI — rien ne sera ecrit'))
    dit('  Flux      : %s' % adresse)
    dit('  Reference : %sZ (le « maintenant » du tri)'
        % maintenant.strftime('%Y-%m-%dT%H:%M:%S'))
    dit()

    brut = charger(adresse)
    evenements = lire_flux(brut)
    dit('  %d evenement(s) dans le flux.' % len(evenements))

    retenus, ecartes, a_signaler = [], [], []
    for ev in evenements:
        titre = ev.get('SUMMARY', ('', ''))[1]
        court = ' '.join(titre.split())[:58] or '(sans titre)'
        if ev.get('STATUS', ('', ''))[1].upper() == 'CANCELLED':
            ecartes.append((court, 'annule dans l’agenda'))
            continue
        if 'DTSTART' not in ev or 'DTEND' not in ev:
            a_signaler.append((court, 'pas d’heure de debut ou de fin'))
            continue
        debut = _instant(*ev['DTSTART'])
        fin = _instant(*ev['DTEND'])
        if debut is None or fin is None:
            a_signaler.append((court, 'journee entiere, ou fuseau non reconnu — '
                                      'le site a besoin d’un horaire'))
            continue
        if fin <= maintenant:
            ecartes.append((court, 'deja termine'))
            continue
        if 'RRULE' in ev:
            a_signaler.append((court, 'evenement qui se repete (RRULE) — non gere'))
            continue
        cle = _cle(titre)
        if cle in TABLE_IGNORE:
            ecartes.append((court, 'ignore volontairement : %s' % TABLE_IGNORE[cle]))
            continue
        if cle not in TABLE:
            a_signaler.append((court, 'titre absent de la liste blanche'))
            continue
        typ, affiche, note = TABLE[cle]
        d1, d2 = _en_paris(debut), _en_paris(fin)
        if d1.date() != d2.date():
            a_signaler.append((court, 'commence et finit des jours differents — '
                                      'le site ne sait pas afficher ca'))
            continue
        retenus.append((d1.date().isoformat(), d1.strftime('%H:%M'),
                        d2.strftime('%H:%M'), typ, affiche, note))
    retenus = trier(retenus)

    # ------------------------------------------------------------------ #
    # CE QUI EST IGNORE, ET CE QUI EST SIGNALE
    # ------------------------------------------------------------------ #
    dit('  %d retenu(s) · %d ecarte(s) sans alerte · %d a signaler.'
        % (len(retenus), len(ecartes), len(a_signaler)))
    if a_signaler:
        dit()
        dit('  ⚠️  EVENEMENTS A VENIR QUI N’IRONT PAS SUR LE SITE')
        for court, pourquoi in a_signaler:
            dit('      · « %s » — %s' % (court, pourquoi))
            signalements.append('« %s » : %s' % (court, pourquoi))
        dit('      Si l’un d’eux doit paraitre, ajouter son titre EXACT dans')
        dit('      CORRESPONDANCE (sources/synchro_agenda.py). Tant qu’il n’y')
        dit('      est pas, il n’est PAS publie — c’est la regle.')

    # ------------------------------------------------------------------ #
    # LES GARDE-FOUS DE VOLUME
    # ------------------------------------------------------------------ #
    anciens = evenements_actuels(src)
    anciens_a_venir = [e for e in anciens
                       if _fin_utc(e[0], e[2]) > maintenant]
    avant = {(e[0], e[1], e[2], e[3]) for e in anciens}
    apres = {(e[0], e[1], e[2], e[3]) for e in retenus}
    ajouts = sorted(apres - avant)
    retraits = sorted(avant - apres)

    if not retenus and anciens_a_venir:
        raise Refus('le flux ne donne AUCUNE date a venir alors que le site en '
                    'annonce %d. On ne vide pas le site sur un flux qui a '
                    'peut-etre ete tronque. Rien n’a ete touche.'
                    % len(anciens_a_venir))
    if len(retenus) < len(anciens_a_venir) * PERTE_MAX:
        raise Refus('il ne resterait que %d date(s) sur les %d que le site '
                    'annonce encore : plus de la moitie disparaitrait d’un '
                    'coup. C’est le signe d’un flux incomplet, pas d’un agenda '
                    'qui change. Rien n’a ete touche.'
                    % (len(retenus), len(anciens_a_venir)))
    if len(ajouts) > AJOUTS_MAX:
        raise Refus('%d dates seraient ajoutees d’un coup (maximum accepte : '
                    '%d). Si c’est normal — une saison entiere posee dans '
                    'l’agenda — il faut appliquer une fois a la main, en '
                    'regardant. Rien n’a ete touche.' % (len(ajouts), AJOUTS_MAX))

    # ------------------------------------------------------------------ #
    # LES BILLETTERIES SURCHARGEES PAR EVENEMENT
    # ------------------------------------------------------------------ #
    # Elles sont indexees par (date, heure de debut). Si une date garde son
    # jour mais change d'heure, la clef ne mord plus : le bouton « Reserver »
    # retomberait en silence sur le lien par defaut du type. Un concert qui
    # perd sa billetterie sans que personne ne le voie, c'est exactement le
    # genre de degat qu'une automatisation ne doit pas pouvoir faire.
    heures = {}
    for iso, h1, _h2, _t, _ti, _n in retenus:
        heures.setdefault(iso, set()).add(h1)
    casse = [(d, h) for d, h in surcharges(src)
             if d in heures and h not in heures[d]]
    if casse:
        raise Refus('la billetterie du %s est enregistree pour %s, mais '
                    'l’agenda donne maintenant %s. Le bouton « Reserver » '
                    'retomberait sur le lien generique du type. Corriger '
                    'URL_PAR_EVENT dans generate_agenda_nid.py, puis relancer. '
                    'Rien n’a ete touche.'
                    % (casse[0][0], casse[0][1],
                       ' ou '.join(sorted(heures[casse[0][0]]))))

    # ------------------------------------------------------------------ #
    # CE QUI CHANGERAIT
    # ------------------------------------------------------------------ #
    dit()
    if not ajouts and not retraits:
        dit('  Rien ne change : les %d date(s) du site sont deja celles de '
            'l’agenda.' % len(retenus))
    else:
        dit('  CE QUI CHANGERAIT')
        for e in retraits:
            dit('      - %s  %s-%s  %s' % e)
        for e in ajouts:
            dit('      + %s  %s-%s  %s' % e)

    _controle_fuite(retenus, TABLE)
    largeur = max(len(t) for t in connus) + 3
    nouveau = bloc(retenus, largeur)
    _controle_motifs(nouveau)

    _autres_pages(dit, retenus, maintenant)

    ancien_bloc = _bloc_actuel(src)
    if ancien_bloc.strip() == nouveau.strip():
        dit()
        dit('  Le fichier est deja a jour. Rien a faire.')
        return 0

    if not args.appliquer:
        dit()
        dit('  ESSAI TERMINE — AUCUN FICHIER N’A ETE TOUCHE.')
        dit('  Pour appliquer :  python3 sources/synchro_agenda.py --appliquer')
        dit()
        return 0

    # ------------------------------------------------------------------ #
    # ECRITURE, PUIS LA CHAINE. AU MOINDRE ECHEC, ON REMET TOUT COMME AVANT.
    # ------------------------------------------------------------------ #
    dit()
    dit('  ECRITURE ET VERIFICATION')
    with open(AGENDA, 'w', encoding='utf-8') as f:
        f.write(src.replace(DEBUT + ancien_bloc + FIN,
                            DEBUT + '\n' + nouveau + '\n' + FIN, 1))
    probleme = chaine_de_verification(dit)
    if probleme:
        with open(AGENDA, 'w', encoding='utf-8') as f:
            f.write(src)
        dit()
        dit('  REFUS — %s' % probleme)
        dit()
        dit('  generate_agenda_nid.py a ete REMIS COMME AVANT ; on reconstruit')
        dit('  le site dans son etat d’origine.')
        rattrapage = chaine_de_verification(dit)
        if rattrapage:
            dit('  ⚠️ LA RECONSTRUCTION D’ORIGINE ECHOUE AUSSI — regarder a la '
                'main : %s' % rattrapage[:300])
        return 1

    dit()
    dit('  FAIT. %d date(s) publiees, %d ajoutee(s), %d retiree(s).'
        % (len(retenus), len(ajouts), len(retraits)))
    dit('  Le site est reconstruit et verifie. Le commit, lui, est le travail')
    dit('  du workflow (ou le tien).')
    dit()
    return 0


def _fin_utc(iso, heure):
    """La fin d'un evenement du site, en instant UTC."""
    texte = dates_a_venir.fin_utc(dt.date.fromisoformat(iso), heure)
    return dt.datetime.strptime(texte, '%Y-%m-%dT%H:%M:%SZ')


# --------------------------------------------------------------------------- #
# LES DEUX PAGES QUI PORTENT ENCORE LEURS PROPRES DATES
# --------------------------------------------------------------------------- #
# ⚠️ POUR INFORMATION SEULEMENT — CE BLOC NE MODIFIE RIEN ET N'ALERTE JAMAIS.
# `/rythme-calebasse` et `/concerts-david-lesage` gardent une petite liste de
# dates ecrite a la main dans leur generateur. Ce ne sont pas des oublis : la
# premiere ne montre que le groupe de pratique, la seconde ne montre que les
# concerts intimistes (elle n'annonce pas la sortie de residence en trio, par
# exemple). Les aligner automatiquement demanderait de trancher ce que chaque
# page doit montrer — une decision de David, pas d'un script.
# Ce qu'on peut faire sans rien decider : le DIRE, a chaque execution.
AUTRES = (
    ('generate_rythme.py', 'rythme', '/rythme-calebasse'),
    ('generate_concert_dl.py', 'concert', '/concerts-david-lesage'),
)


def _autres_pages(dit, retenus, maintenant):
    for fichier, typ, page in AUTRES:
        chemin = os.path.join(HERE, fichier)
        if not os.path.exists(chemin):
            continue
        with open(chemin, encoding='utf-8') as f:
            texte = f.read()
        # Les deux fichiers ecrivent leurs dates differemment (« 2026-09-20 »
        # ici, « 2026-10-10T19:00 » la) : on ne prend que le jour.
        ecrites = sorted({d for d in
                          re.findall(r"'(\d{4}-\d{2}-\d{2})(?:T\d\d:\d\d)?'", texte)
                          if _fin_utc(d, None) > maintenant})
        agenda = sorted({e[0] for e in retenus if e[3] == typ
                         if _fin_utc(e[0], e[2]) > maintenant})
        if ecrites != agenda:
            dit()
            dit('  (pour information) %s porte ses propres dates : %s'
                % (page, ', '.join(ecrites) or 'aucune'))
            dit('      l’agenda annonce, pour ce type : %s'
                % (', '.join(agenda) or 'aucune'))
            dit('      Cette page se met a jour a la main. Aucune alerte.')


if __name__ == '__main__':
    sys.exit(main())
