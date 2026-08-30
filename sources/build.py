# -*- coding: utf-8 -*-
"""Reconstruit le site. UNE seule commande, rien a retenir.

    python3 sources/build.py                     # tout le site
    python3 sources/build.py --page le-nid       # une seule page
    python3 sources/build.py --liste             # juste afficher le tableau

POURQUOI CE FICHIER EXISTE
--------------------------
Le site est fabrique par une quinzaine de scripts, et l'ordre dans lequel on les
lance n'est pas devinable :

  * certains generateurs posent eux-memes le menu de navigation ;
  * d'autres NON — il faut repasser `nav_menu.py` derriere eux, sinon le menu
    disparait de la page ;
  * certains n'ecrivent pas la page finale mais un fichier intermediaire dans
    `sources/`, qu'il faut recopier ;
  * certains ne peuvent plus tourner du tout (leurs photos d'origine ne sont pas
    dans le depot).

Tout cela vivait dans la memoire de celui qui lancait les commandes. Ca a casse
plusieurs fois. C'est maintenant ecrit dans le TABLEAU ci-dessous, et c'est ce
tableau qui commande.

CE QUE LE SCRIPT GARANTIT
-------------------------
1. L'ORDRE. Generateur, puis copie, puis menu — dans le bon sens, page par page.
2. L'IDEMPOTENCE. Chaque page est construite DEUX FOIS et les deux resultats
   sont compares. S'ils different, c'est qu'une passe ajoute quelque chose a
   chaque fois : c'est exactement ce qui avait produit quatre entrees « Agenda »
   dans le menu et quatre cartes identiques. Le script s'arrete.
3. LA VERIFICATION. `verif_site.py` passe sur les 10 pages a la fin.
4. LE RETOUR EN ARRIERE. Avant de commencer, chaque page est mise de cote. Si
   quoi que ce soit echoue, TOUTES les pages sont remises exactement comme
   avant. Un build rate ne laisse jamais le site a moitie reconstruit.
"""

import argparse
import hashlib
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(HERE)


# --------------------------------------------------------------------------- #
#                                  LE TABLEAU
# --------------------------------------------------------------------------- #
# Une ligne par page publiee. A lire de gauche a droite : la page, le script qui
# la fabrique, ce que ce script ecrit vraiment, et s'il faut repasser le menu
# derriere lui.
#
#   nom          nom court a donner a --page
#   fichier      la page telle qu'elle est publiee, depuis la racine du depot
#   generateur   le script de sources/ qui la fabrique (None = aucune)
#   ecrit        ce que le generateur ecrit REELLEMENT, si ce n'est pas la page
#                (il faudra recopier). None = il ecrit directement la page.
#   passe_menu   True  -> le generateur NE pose PAS le menu, il faut lancer
#                         `nav_menu.py` derriere lui, sinon la page part sans
#                         menu (le piege historique de ce projet).
#                False -> le generateur appelle deja nav_menu.inject() lui-meme,
#                         une passe de plus ne servirait a rien.
#   bloque       None si la page est reconstructible ici ; sinon la raison,
#                affichee telle quelle. La page n'est alors PAS touchee.
#
# ⚠️ Un generateur qui apparait dans sources/ sans etre inscrit ici est signale
#    en fin de build : il faut lui ajouter sa ligne.

TABLEAU = (
    dict(
        nom='accueil', fichier='index.html',
        generateur='generate_assoc.py', ecrit='assoc_index.html',
        passe_menu=False,
        # 14/08/2026 : le generateur a ete repare (les accolades du CSS insere
        # n'etaient pas doublees dans une f-string : « NameError: name 'font'
        # is not defined »). Il reproduit desormais assoc_index.html a l'octet
        # pres, et build.py le recopie sur index.html.
        bloque=None,
    ),
    dict(
        nom='rituals', fichier='rituals/index.html',
        generateur='generate_site.py', ecrit=None,
        passe_menu=False,
        # 14/08/2026 : le generateur a ete repare et reproduit desormais la
        # page publiee a l'octet pres, photos comprises. Il n'a plus besoin des
        # dossiers photos hors depot.
        bloque=None,
    ),
    dict(
        nom='rituals-trio', fichier='rituals-trio/index.html',
        generateur='generate_trio.py', ecrit=None,
        passe_menu=False,
        # 14/08/2026 : repare comme /rituals — la fabrication des images
        # derivees (qui a besoin des photos d'origine hors depot) est passee
        # derriere l'option `--images`. Sans elle, la page se regenere a
        # l'octet pres a partir de sources/trio_source.html.
        bloque=None,
    ),
    dict(
        nom='e-motion', fichier='e-motion/index.html',
        generateur='generate_emotion.py', ecrit=None,
        passe_menu=False,  # il appelle nav_menu.inject() lui-meme
        bloque=None,      # si le generateur existe, on s'en sert ; sinon la
                          # page est signalee comme maintenue a la main
                          # (c'etait le cas jusqu'au 14/08/2026).
    ),
    dict(
        nom='david-lesage-en-concert', fichier='david-lesage-en-concert/index.html',
        generateur='generate_concert_scene.py', ecrit=None,
        passe_menu=True,  # ⚠️ ce generateur ne pose PAS le menu
        bloque=None,
    ),
    dict(
        nom='concerts-david-lesage', fichier='concerts-david-lesage/index.html',
        generateur='generate_concert_dl.py', ecrit=None,
        passe_menu=True,  # ⚠️ ce generateur ne pose PAS le menu
        bloque=None,
    ),
    dict(
        nom='le-nid', fichier='le-nid/index.html',
        generateur='generate_agenda_nid.py', ecrit=None,
        passe_menu=False,
        # 14/08/2026 : ce n'est plus une retouche d'une page introuvable. Le
        # generateur part maintenant de sources/lenid_source.html, versionne
        # dans le depot, et reproduit /le-nid a l'octet pres.
        bloque=None,
    ),
    # Creee le 20/08/2026 : la page qui annonce TOUS les rendez-vous mensuels du
    # Nid, avec « une proposition d'activite differente a chaque fois ». Les
    # dates viennent de l'agenda de /le-nid ; le generateur RELIT
    # `generate_agenda_nid.py` en texte (jamais par import : ce module reecrit
    # /le-nid rien qu'en etant importe) et refuse d'ecrire si elles ont diverge.
    dict(
        nom='rendez-vous-mensuels', fichier='rendez-vous-mensuels/index.html',
        generateur='generate_rdv_mensuels.py', ecrit=None,
        passe_menu=False,  # il appelle mobile_nav puis nav_menu.inject() lui-meme
        bloque=None,
    ),
    dict(
        nom='le-soin-soa', fichier='le-soin-soa/index.html',
        generateur='generate_soin_soa.py', ecrit='sources/soin_soa_final.html',
        passe_menu=False,
        bloque=None,
    ),
    dict(
        nom='rythme-calebasse', fichier='rythme-calebasse/index.html',
        generateur='generate_rythme.py', ecrit=None,
        passe_menu=False,  # il appelle nav_menu.inject() lui-meme
        bloque=None,
    ),
    # Creee le 15/08/2026 : « Accueil » et « L’association » menaient tous les
    # deux a l'accueil. La page reprend l'objet, les valeurs, les statuts (qui
    # ont QUITTE l'accueil), les mentions legales, les adresses, l'adhesion et
    # le contact. Elle importe `textes_association` — un module de textes
    # partage avec `generate_assoc.py`, pas un generateur : l'importer n'ecrit
    # aucune page, et il n'a donc pas de ligne dans ce tableau.
    dict(
        nom='association', fichier='association/index.html',
        generateur='generate_association.py', ecrit=None,
        passe_menu=False,  # il appelle mobile_nav puis nav_menu.inject() lui-meme
        bloque=None,
    ),
    dict(
        nom='guso-facile', fichier='guso-facile/index.html',
        generateur='generate_guso.py', ecrit=None,
        passe_menu=False,  # il appelle mobile_nav puis nav_menu.inject() lui-meme
        bloque=None,
    ),
    # Le blog de Guso Facile : UN generateur pour 19 pages (l'index + 18
    # articles). `fichier` ne nomme que l'index — c'est lui que le controle
    # d'idempotence compare —, mais le generateur reecrit bien les 19 a chaque
    # passage. Il importe `theme_chaleur` : c'est un module de style, pas un
    # generateur, l'importer n'ecrit aucune page.
    dict(
        nom='guso-facile-blog', fichier='guso-facile/blog/index.html',
        generateur='generate_guso_blog.py', ecrit=None,
        passe_menu=False,  # il appelle mobile_nav puis nav_menu.inject() lui-meme
        bloque=None,
    ),
)

#: dossiers presents dans le depot mais hors du site : aucun generateur, aucune
#: entree de menu, absents du plan du site.
#:
#: ⚠️ VIDE DEPUIS LE 17/08/2026, et c'est normal. `/solune` et `/au-nid` y
#: figuraient ; David a tranche leur suppression, ils n'existent plus sur le
#: disque et sont devenus des REDIRECTIONS 301 (voir vercel.json et SUPPRIMEES
#: dans verif_site.py). La table est restee garnie dix jours de trop : chaque
#: construction annoncait « DOSSIERS ORPHELINS — encore dans le depot » pour des
#: dossiers effaces. Un rapport qui decrit un site qui n'existe plus est pire
#: que pas de rapport du tout : on cesse de le lire.
#:
#: Le controle plus bas verifie desormais que ce qui est annonce ici existe
#: VRAIMENT : une entree perimee fait echouer la construction au lieu de
#: s'afficher pour rien.
ORPHELINES = {}

#: scripts de sources/ qui ne fabriquent aucune page du site : ils sont ignores
#: par le controle « generateur non inscrit » plus bas.
HORS_SITE = {
    'generate_plaquette_trio.py': 'plaquette PDF du trio (hors site)',
    # 30/08/2026 — page de promo du duo David Lesage & Lucie, VOLONTAIREMENT
    # invisible : aucune entree de menu, absente du sitemap et de
    # verif_site.PAGES, interdite aux moteurs. Seules les agences a qui David
    # donne l'adresse doivent la trouver. Elle n'a donc pas sa place dans le
    # TABLEAU (qui ne decrit que les pages PUBLIEES) et build.py ne doit ni la
    # reconstruire ni la sauvegarder. Pour la refaire :
    #     python3 sources/generate_duo_lucie.py
    'generate_duo_lucie.py': 'page de promo du duo David & Lucie '
                             '(hors site, non referencee)',
}

#: fichiers remis en etat si le build echoue.
A_SAUVEGARDER = tuple(l['fichier'] for l in TABLEAU) + (
    'assoc_index.html', 'sources/soin_soa_final.html',
)


# --------------------------------------------------------------------------- #
# Petits outils
# --------------------------------------------------------------------------- #

def _dit(message=''):
    # flush systematique : `verif_site.py` est lance en sous-processus et ecrit
    # sur la meme sortie. Sans ca, ses lignes s'intercalent n'importe ou.
    print(message, flush=True)


def _empreinte(chemin):
    if not os.path.exists(chemin):
        return None
    with open(chemin, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def _lancer(script, *args):
    """Lance un script de sources/ dans un processus separe.

    JAMAIS par `import` : plusieurs de ces scripts font leur travail au moment
    ou on les importe (`generate_concert_scene.py` reecrit la page rien qu'en
    etant importe, et sans le menu). Un sous-processus, c'est net.
    """
    return subprocess.run(
        [sys.executable, os.path.join(HERE, script)] + list(args),
        cwd=RACINE, capture_output=True, text=True)


class Echec(Exception):
    """Le build s'arrete ; tout est remis en etat."""


# --------------------------------------------------------------------------- #
# Construction d'une page
# --------------------------------------------------------------------------- #

def _une_passe(ligne):
    """Generateur -> copie -> menu. Renvoie l'empreinte de la page produite."""
    script = ligne['generateur']
    r = _lancer(script)
    if r.returncode != 0:
        derniere = (r.stderr or r.stdout or '').strip().splitlines()
        raise Echec('le script sources/%s s\'est arrete en erreur.\n     %s'
                    % (script, derniere[-1] if derniere else '(sans message)'))

    if ligne['ecrit']:
        source = os.path.join(RACINE, ligne['ecrit'])
        if not os.path.exists(source):
            raise Echec('sources/%s devait produire %s : le fichier n\'est pas la.'
                        % (script, ligne['ecrit']))
        shutil.copyfile(source, os.path.join(RACINE, ligne['fichier']))

    if ligne['passe_menu']:
        r = _lancer('nav_menu.py', ligne['fichier'])
        if r.returncode != 0:
            derniere = (r.stderr or r.stdout or '').strip().splitlines()
            raise Echec('la pose du menu a echoue sur %s.\n     %s'
                        % (ligne['fichier'], derniere[-1] if derniere else ''))

    return _empreinte(os.path.join(RACINE, ligne['fichier']))


def _construire(ligne, avant):
    """Construit la page DEUX fois et exige le meme resultat."""
    fichier = ligne['fichier']
    quoi = 'menu repose derriere' if ligne['passe_menu'] else 'menu pose par le script'
    _dit('  · %-26s sources/%-26s (%s)' % (ligne['nom'], ligne['generateur'], quoi))

    premiere = _une_passe(ligne)
    seconde = _une_passe(ligne)

    if premiere != seconde:
        raise Echec(
            'la page %s n\'est pas stable : la construire deux fois de suite ne\n'
            '     donne pas le meme fichier. Un bloc s\'ajoute a chaque passage.\n'
            '     C\'est ce qui avait produit quatre entrees « Agenda » dans le\n'
            '     menu et quatre cartes identiques. Rien n\'a ete publie.' % fichier)

    apres = _empreinte(os.path.join(RACINE, fichier))
    return 'inchangee' if apres == avant else 'MISE A JOUR'


# --------------------------------------------------------------------------- #
# Sauvegarde / restauration
# --------------------------------------------------------------------------- #

def _sauvegarder():
    coffre = {}
    for rel in A_SAUVEGARDER:
        chemin = os.path.join(RACINE, rel)
        if os.path.exists(chemin):
            with open(chemin, 'rb') as f:
                coffre[rel] = f.read()
    return coffre


def _restaurer(coffre):
    remis = 0
    for rel, contenu in coffre.items():
        chemin = os.path.join(RACINE, rel)
        actuel = None
        if os.path.exists(chemin):
            with open(chemin, 'rb') as f:
                actuel = f.read()
        if actuel != contenu:
            with open(chemin, 'wb') as f:
                f.write(contenu)
            remis += 1
    return remis


# --------------------------------------------------------------------------- #
# Affichages
# --------------------------------------------------------------------------- #

def afficher_tableau():
    _dit()
    _dit('  QUI FABRIQUE QUOI')
    _dit('  ' + '-' * 74)
    for l in TABLEAU:
        chemin = os.path.join(HERE, l['generateur']) if l['generateur'] else None
        present = chemin and os.path.exists(chemin)
        if l['bloque']:
            etat = 'bloque'
        elif not present:
            etat = 'aucun generateur'
        else:
            etat = 'automatique'
        _dit('  %-26s %-30s %s' % (l['nom'], l['generateur'] or '—', etat))
        if l['ecrit']:
            _dit('  %-26s   ecrit %s, puis recopie' % ('', l['ecrit']))
        if l['passe_menu']:
            _dit('  %-26s   ⚠ menu a reposer derriere (nav_menu.py)' % '')
    _dit('  ' + '-' * 74)
    for nom, pourquoi in sorted(ORPHELINES.items()):
        _dit('  /%-25s orpheline — %s' % (nom, pourquoi))
    _dit()


def _signaler_non_reconstructibles(lignes):
    """Les pages qu'on ne touche pas, et pourquoi. Jamais en silence."""
    manuelles, bloquees = [], []
    for l in lignes:
        if l['bloque']:
            bloquees.append(l)
        elif not os.path.exists(os.path.join(HERE, l['generateur'] or '')):
            manuelles.append(l)
    if manuelles:
        _dit()
        _dit('  PAGES SANS GENERATEUR — modifiees a la main, jamais par ce script')
        for l in manuelles:
            _dit('  · %s  (le fichier sources/%s n\'existe pas)'
                 % (l['nom'], l['generateur']))
        _dit('    Pour ces pages, on edite directement le HTML. C\'est le seul cas')
        _dit('    ou c\'est permis.')
    if bloquees:
        _dit()
        _dit('  PAGES NON RECONSTRUCTIBLES ICI — laissees intactes')
        for l in bloquees:
            _dit('  · %s  (sources/%s)' % (l['nom'], l['generateur']))
            for morceau in _replier(l['bloque'], 68):
                _dit('      %s' % morceau)
    for nom in sorted(ORPHELINES):
        if not os.path.isdir(os.path.join(RACINE, nom)):
            raise SystemExit(
                "!! ABANDON : ORPHELINES annonce le dossier /%s, qui n'existe "
                "pas sur le disque. Retire-le de la table — sinon chaque "
                "construction decrit un site qui n'est plus le vrai." % nom)
    if ORPHELINES:
        _dit()
        _dit('  DOSSIERS ORPHELINS — encore dans le depot, hors du site')
        for nom, pourquoi in sorted(ORPHELINES.items()):
            _dit('  · /%s — %s' % (nom, pourquoi))
        _dit('    Absents du plan du site et interdits aux moteurs de recherche.')
        _dit('    Leur suppression n\'a jamais ete tranchee : on n\'y touche pas.')


def _replier(texte, largeur):
    mots, ligne, out = texte.split(), '', []
    for mot in mots:
        if len(ligne) + len(mot) + 1 > largeur:
            out.append(ligne)
            ligne = mot
        else:
            ligne = (ligne + ' ' + mot).strip()
    if ligne:
        out.append(ligne)
    return out


def _generateurs_non_inscrits():
    """Un generateur est apparu dans sources/ sans ligne dans le tableau ?"""
    inscrits = {l['generateur'] for l in TABLEAU if l['generateur']}
    inscrits |= set(HORS_SITE)
    trouves = sorted(f for f in os.listdir(HERE)
                     if f.startswith('generate_') and f.endswith('.py'))
    return [f for f in trouves if f not in inscrits]


# --------------------------------------------------------------------------- #
# Programme principal
# --------------------------------------------------------------------------- #

def main(argv=None):
    ap = argparse.ArgumentParser(
        description='Reconstruit le site de Resonances Productions.')
    ap.add_argument('--page', help='ne reconstruire qu\'une page (son nom court)')
    ap.add_argument('--liste', action='store_true',
                    help='afficher le tableau et sortir, sans rien reconstruire')
    args = ap.parse_args(argv)

    if args.liste:
        afficher_tableau()
        return 0

    lignes = list(TABLEAU)
    if args.page:
        voulu = args.page.strip('/')
        lignes = [l for l in TABLEAU if l['nom'] == voulu]
        if not lignes:
            _dit()
            _dit('  Page inconnue : « %s ».' % args.page)
            _dit('  Noms possibles : %s' % ', '.join(l['nom'] for l in TABLEAU))
            _dit()
            return 2

    _dit()
    _dit('  CONSTRUCTION DU SITE')
    _dit('  ' + '-' * 74)

    a_faire = [l for l in lignes
               if not l['bloque']
               and os.path.exists(os.path.join(HERE, l['generateur'] or ''))]

    coffre = _sauvegarder()
    resultats = {}
    try:
        if not a_faire:
            _dit('  (aucune page reconstructible dans cette selection)')
        for l in a_faire:
            resultats[l['nom']] = _construire(
                l, _empreinte(os.path.join(RACINE, l['fichier'])))
    except Echec as e:
        remis = _restaurer(coffre)
        _dit()
        _dit('  ARRET : %s' % e)
        _dit()
        _dit('  %s Le site sur le disque est dans l\'etat ou il etait avant'
             % ('Aucun fichier n\'avait ete modifie.' if not remis
                else '%d fichier(s) remis exactement comme avant.' % remis))
        _dit('  cette commande : rien n\'est casse, rien n\'a ete publie.')
        _dit()
        return 1

    for nom, etat in resultats.items():
        _dit('    %-26s %s' % (nom, etat))

    _signaler_non_reconstructibles(lignes)

    orphelins = _generateurs_non_inscrits()
    if orphelins:
        _dit()
        _dit('  GENERATEUR NON INSCRIT AU TABLEAU')
        for f in orphelins:
            _dit('  · sources/%s existe mais aucune page ne le reclame.' % f)
        _dit('    Ajouter sa ligne en haut de sources/build.py, sinon la page')
        _dit('    qu\'il fabrique ne sera jamais reconstruite.')

    # ------------------------------------------------------------------ #
    # Verification finale : rien ne reste sur le disque si elle echoue.
    # ------------------------------------------------------------------ #
    _dit()
    _dit('  ' + '-' * 74)
    # `len(TABLEAU)` est le nombre de GENERATEURS (13), pas de pages (31) :
    # le message annoncait « Verification des 13 pages » depuis toujours.
    # On lit le vrai compte la ou il fait foi, dans verif_site.PAGES.
    try:
        import verif_site
        _nb = len(verif_site.PAGES)
    except Exception:
        _nb = len(TABLEAU)
    _dit('  Verification des %d pages…' % _nb)
    r = subprocess.run([sys.executable, os.path.join(HERE, 'verif_site.py')],
                       cwd=RACINE)
    if r.returncode != 0:
        remis = _restaurer(coffre)
        _dit('  ARRET : la verification a trouve un probleme (voir ci-dessus).')
        _dit('  %s Rien n\'a ete ecrit.'
             % ('Aucun fichier n\'avait ete modifie.' if not remis
                else '%d fichier(s) remis exactement comme avant.' % remis))
        _dit()
        return 1

    changees = [n for n, e in resultats.items() if e != 'inchangee']
    _dit('  ' + '-' * 74)
    if changees:
        _dit('  SITE RECONSTRUIT. Pages modifiees : %s' % ', '.join(changees))
    else:
        _dit('  SITE RECONSTRUIT. Aucune page n\'a change.')
    _dit()
    _dit('  Etape suivante — publier :')
    _dit('      git add <les fichiers modifies>')
    _dit('      git commit -m "…"')
    _dit('      git push')
    _dit('  Vercel met le site en ligne tout seul, environ 40 secondes apres.')
    _dit()
    return 0


if __name__ == '__main__':
    sys.exit(main())
