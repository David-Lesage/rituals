# -*- coding: utf-8 -*-
"""Google Search Console, en ligne de commande. SANS AUCUNE DEPENDANCE.

    python3 sources/search_console.py --sites          # les proprietes accessibles
    python3 sources/search_console.py --indexation     # l'etat des 31 pages
    python3 sources/search_console.py --requetes 28    # ce que les gens tapent

CE QUE CE FICHIER N'EST PAS
---------------------------
⚠️ IL NE FAIT PAS PARTIE DE LA FABRICATION DU SITE. `build.py` ne l'importe
   pas, le workflow de l'agenda ne l'appelle pas, `verif_site.py` l'ignore. Une
   panne ici ne peut donc PAS empecher le site d'etre publie. C'est un outil de
   diagnostic, rien d'autre — et c'est pour ca qu'il peut se permettre de
   parler au reseau, ce que la chaine de construction ne fait jamais.

POURQUOI OAUTH ET PAS UN COMPTE DE SERVICE
------------------------------------------
Les deux marchent. OAuth a ete choisi pour trois raisons concretes :

  1. ZERO DEPENDANCE. Un compte de service impose de signer un jeton en RS256,
     donc d'installer une bibliotheque de cryptographie (`google-auth`,
     `cryptography`…). Le rafraichissement OAuth, lui, est un simple POST en
     HTTPS : `urllib` et `json` de la bibliotheque standard suffisent. Ce depot
     a deja paye DEUX FOIS le prix d'une dependance presente sur le Mac et
     absente ailleurs (Pillow, en aout puis en septembre 2026).
  2. RIEN A AJOUTER DANS SEARCH CONSOLE. Un compte de service doit etre ajoute
     a la main comme utilisateur de la propriete, et c'est l'etape que tout le
     monde oublie — on croit que ca ne marche pas alors qu'il manque un droit.
     En OAuth, l'acces est celui du compte Google de David, tel quel.
  3. REVOCABLE EN UN CLIC, depuis myaccount.google.com/permissions.

🚨 LES SECRETS NE VIVENT JAMAIS DANS LE DEPOT. CE DEPOT EST PUBLIC, et un code
   d'acces y a deja fuite DEUX FOIS. Le fichier d'identifiants est donc range
   hors du depot, dans ~/.config/resonances/search-console.json, et ce chemin
   n'est PAS negociable. Le script refuse de demarrer s'il trouve un fichier
   d'identifiants a l'interieur du depot.

MISE EN ROUTE (une seule fois, cote Google — David seul peut le faire)
----------------------------------------------------------------------
  1. console.cloud.google.com -> creer (ou choisir) un projet.
  2. « APIs & Services » -> « Enable APIs » -> activer « Google Search
     Console API ».
  3. « Identifiants » -> « Creer des identifiants » -> « ID client OAuth » ->
     type « Application de bureau ».
  4. Noter l'ID client et le code secret, puis :
         python3 sources/search_console.py --connexion
     Le script ouvre le navigateur, David approuve, et le jeton est range.
Ensuite, plus jamais : le jeton de rafraichissement se renouvelle tout seul.
"""

import getpass
import http.server
import json
import os
import re
import secrets
import sys
import threading
import urllib.parse
import urllib.request
import webbrowser

HERE = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(HERE)
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import verif_site  # noqa: E402  (la liste des 31 pages, jamais recopiee)

#: hors du depot, volontairement. Voir la note en tete de fichier.
IDENTIFIANTS = os.path.expanduser('~/.config/resonances/search-console.json')

#: ⚠️ LA PROPRIETE PAR DEFAUT, PAS LA SEULE. David a plusieurs sites
#: (resonancesproductions.org, lesagedavid.fr, handpanstudio.app…). En OAuth,
#: l'acces suit SON COMPTE : toutes les proprietes dont il est proprietaire
#: dans Search Console sont accessibles sans rien ajouter ici. `--sites` les
#: liste ; `--site <propriete>` bascule sur l'une d'elles.
PROPRIETE = 'sc-domain:resonancesproductions.org'
PORTEE = 'https://www.googleapis.com/auth/webmasters.readonly'
# ⚠️ SEARCH CONSOLE A DEUX API, A DEUX ADRESSES DIFFERENTES, et s'y tromper
#    donne un 404 en HTML (pas un message JSON lisible — vecu le 18/09/2026) :
#      * WEBMASTERS : la liste des proprietes et les statistiques de recherche.
#        C'est l'ancienne API « webmasters/v3 », toujours la seule pour ca.
#      * INSPECTION : l'etat d'indexation page par page, plus recente.
WEBMASTERS = 'https://www.googleapis.com/webmasters/v3'
INSPECTION = 'https://searchconsole.googleapis.com/v1'
JETON = 'https://oauth2.googleapis.com/token'


# --------------------------------------------------------------------------- #
# IDENTIFIANTS
# --------------------------------------------------------------------------- #

def _garde_fou_depot():
    """Refuse de tourner si des identifiants trainent dans le depot public."""
    suspects = []
    for dossier, _, fichiers in os.walk(RACINE):
        if '/.git' in dossier or '/node_modules' in dossier:
            continue
        for f in fichiers:
            if re.search(r'(client_secret|search-console).*\.json$', f):
                suspects.append(os.path.join(dossier, f))
    if suspects:
        raise SystemExit(
            '!! ABANDON : des identifiants semblent ranges DANS le depot, qui est\n'
            '   PUBLIC :\n     %s\n'
            '   Deplace-les vers %s, puis relance.'
            % ('\n     '.join(suspects), IDENTIFIANTS))


def _lire():
    if not os.path.exists(IDENTIFIANTS):
        raise SystemExit(
            'Aucun identifiant : %s est absent.\n'
            'Lance d\'abord :  python3 sources/search_console.py --connexion'
            % IDENTIFIANTS)
    with open(IDENTIFIANTS, encoding='utf-8') as f:
        return json.load(f)


def _ecrire(donnees):
    os.makedirs(os.path.dirname(IDENTIFIANTS), exist_ok=True)
    with open(IDENTIFIANTS, 'w', encoding='utf-8') as f:
        json.dump(donnees, f, indent=2)
    os.chmod(IDENTIFIANTS, 0o600)      # lisible par David seul


#: ce que Google repond vraiment, traduit. Un `invalid_client` brut n'aide
#: personne : il faut dire QUOI verifier.
_EXPLICATIONS = {
    'invalid_client':
        'Le code secret ne correspond pas a cet ID client.\n'
        '   Les deux doivent venir de LA MEME fenetre « Client OAuth cree ».\n'
        '   Le plus sur : creer un nouveau client (Application de bureau) et\n'
        '   copier l’ID PUIS le secret dans cette meme fenetre, sans la fermer.',
    'invalid_grant':
        'Le code d’autorisation a expire ou a deja servi. Relance simplement\n'
        '   la connexion : un code n’est valable que quelques minutes.',
    'unauthorized_client':
        'Ce client n’a pas le droit d’utiliser ce mode d’autorisation.\n'
        '   Verifier qu’il est bien de type « Application de bureau ».',
    'access_denied':
        'L’autorisation a ete refusee dans le navigateur, ou le compte utilise\n'
        '   n’appartient pas a l’organisation autorisee (application « Interne »).',
}


def _poste(url, champs):
    """POST en formulaire. Traduit les refus de Google au lieu de les jeter.

    ⚠️ SANS CE `try`, UNE ERREUR D'IDENTIFIANT SORTAIT EN TRACE PYTHON DE
       QUINZE LIGNES (vecu le 18/09/2026 : « HTTPError: HTTP Error 401 »).
       David n'a aucune raison de lire une pile d'appels pour apprendre qu'il
       a colle le mauvais code secret.
    """
    corps = urllib.parse.urlencode(champs).encode()
    req = urllib.request.Request(url, data=corps, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        brut = e.read().decode('utf-8', 'replace')
        try:
            detail = json.loads(brut)
        except ValueError:
            detail = {}
        code = detail.get('error', '')
        message = ['', '!! Google a refuse (%s%s).'
                   % (e.code, ' — ' + code if code else '')]
        if code in _EXPLICATIONS:
            message.append('   ' + _EXPLICATIONS[code])
        elif detail.get('error_description'):
            message.append('   ' + detail['error_description'])
        else:
            message.append('   ' + brut[:300])
        raise SystemExit('\n'.join(message))


def _acces():
    """Un jeton d'acces valide, renouvele au besoin. Sans dependance."""
    ids = _lire()
    rep = _poste(JETON, {
        'client_id': ids['client_id'],
        'client_secret': ids['client_secret'],
        'refresh_token': ids['refresh_token'],
        'grant_type': 'refresh_token',
    })
    return rep['access_token']


def _api(url, charge=None):
    donnees = json.dumps(charge).encode() if charge is not None else None
    req = urllib.request.Request(
        url, data=donnees, method='POST' if charge is not None else 'GET',
        headers={'Authorization': 'Bearer ' + _acces(),
                 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode('utf-8', 'replace')[:400]
        raise SystemExit('!! L’API a repondu %s :\n   %s' % (e.code, detail))


# --------------------------------------------------------------------------- #
# CONNEXION (une seule fois)
# --------------------------------------------------------------------------- #

def _depuis_json(chemin):
    """(id, secret) lus dans le fichier JSON telecharge depuis Google Cloud.

    ⚠️ POURQUOI CETTE VOIE EXISTE, ET POURQUOI C'EST LA MEILLEURE. Le copier-
       coller a echoue DEUX FOIS le 18/09/2026 : une fois la commande de
       lancement collee dans le champ « ID client », une fois le secret d'un
       AUTRE client colle avec le bon ID (401 invalid_client). Ces chaines
       melangent l, I, 1, O et 0, et rien a l'ecran ne dit qu'on s'est trompe.
       Le fichier telecharge, lui, contient les deux valeurs APPARIEES et
       exactes, et personne ne les retape.
    """
    chemin = os.path.expanduser(chemin)
    if not os.path.exists(chemin):
        raise SystemExit('!! Fichier introuvable : %s' % chemin)
    with open(chemin, encoding='utf-8') as f:
        try:
            brut = json.load(f)
        except ValueError:
            raise SystemExit('!! %s n’est pas un fichier JSON lisible.' % chemin)
    bloc = brut.get('installed') or brut.get('web') or {}
    cid, secret = bloc.get('client_id'), bloc.get('client_secret')
    if not cid or not secret:
        raise SystemExit(
            '!! Ce JSON ne ressemble pas a un client OAuth Google : il devrait\n'
            '   contenir une section « installed » avec client_id et\n'
            '   client_secret. Telecharge-le depuis la liste des clients\n'
            '   (console.cloud.google.com -> Clients -> icone de telechargement).')
    return cid, secret


def connexion(json_client=None):
    """Boucle OAuth « loopback » : le navigateur revient sur localhost.

    ⚠️ C'est le seul flot encore recommande par Google pour une application de
       bureau. L'ancien « copier-coller du code » (out-of-band) est ferme
       depuis 2022 : un guide qui le propose est perime.
    """
    _garde_fou_depot()
    if json_client:
        cid, secret = _depuis_json(json_client)
        print('  Identifiants lus dans %s' % json_client)
        return _boucle_oauth(cid, secret)

    # ⚠️ SI L'ID CLIENT EST DEJA CONNU, ON NE LE REDEMANDE PAS. Il n'est pas
    #    secret (il est meme dans l'URL de la fiche du client), et c'est la
    #    moitie des occasions de se tromper en moins : le 18/09/2026, deux
    #    tentatives ont echoue sur un copier-coller, dont une sur l'ID.
    if os.path.exists(IDENTIFIANTS):
        with open(IDENTIFIANTS, encoding='utf-8') as f:
            deja = json.load(f)
        if deja.get('client_id') and not deja.get('refresh_token'):
            print('  ID client deja enregistre : %s…' % deja['client_id'][:28])
            secret = getpass.getpass(
                '  Code secret   : (invisible, colle et Entree) ').strip()
            if not secret.startswith('GOCSPX-'):
                raise SystemExit(
                    '!! Ce n’est pas un code secret : il commence par « GOCSPX- ».')
            return _boucle_oauth(deja['client_id'], secret)
    print('Le plus sur : telecharger le JSON du client, puis :')
    print('  python3 sources/search_console.py --connexion ~/Downloads/client_secret_….json')
    print()
    print('Identifiants OAuth « Application de bureau » '
          '(console.cloud.google.com -> Identifiants).')
    cid = input('  ID client     : ').strip()
    # ⚠️ `getpass` ET PAS `input` POUR LE SECRET : `input` l'affiche en clair et
    #    le laisse dans l'historique visible du terminal, ou il peut etre relu
    #    (ou capture par-dessus l'epaule, ou dans une capture d'ecran). La
    #    frappe est invisible — c'est normal, le collage fonctionne quand meme.
    secret = getpass.getpass('  Code secret   : (invisible, colle et Entree) ').strip()

    # Erreur vecue le 18/09/2026 : David a colle la COMMANDE de lancement dans
    # le champ « ID client ». On le dit tout de suite plutot que d'echouer plus
    # tard sur un « invalid_client » incomprehensible.
    if not cid.endswith('.apps.googleusercontent.com'):
        raise SystemExit(
            '!! Ce n’est pas un ID client : il doit se terminer par\n'
            '   « .apps.googleusercontent.com ».\n'
            '   Recu : %.60s…\n'
            '   Utilise l’icone « copier » a droite de l’ID client, dans Chrome.'
            % cid)
    if secret == cid or secret.endswith('.apps.googleusercontent.com'):
        raise SystemExit(
            '!! Tu as colle l’ID client une seconde fois. Le code secret est\n'
            '   l’AUTRE valeur de la fenetre, celle qui commence par « GOCSPX- ».')
    if not secret.startswith('GOCSPX-'):
        raise SystemExit(
            '!! Ce n’est pas un code secret : il commence normalement par\n'
            '   « GOCSPX- ». Utilise la deuxieme icone « copier » dans Chrome.')
    if not cid or not secret:
        raise SystemExit('Abandon : il manque l’ID client ou le code secret.')
    return _boucle_oauth(cid, secret)


def _boucle_oauth(cid, secret):
    etat = secrets.token_urlsafe(16)
    recu = {}

    class Retour(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            recu.update({k: v[0] for k, v in params.items()})
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(
                '<h2>C’est bon.</h2><p>Tu peux fermer cet onglet et revenir '
                'au terminal.</p>'.encode('utf-8'))

        def log_message(self, *a):
            pass                        # pas de bruit dans le terminal

    serveur = http.server.HTTPServer(('127.0.0.1', 0), Retour)
    port = serveur.server_address[1]
    redirection = 'http://127.0.0.1:%d/' % port

    url = 'https://accounts.google.com/o/oauth2/v2/auth?' + urllib.parse.urlencode({
        'client_id': cid, 'redirect_uri': redirection, 'response_type': 'code',
        'scope': PORTEE, 'access_type': 'offline', 'prompt': 'consent',
        'state': etat,
    })
    print('\nUne page Google va s’ouvrir. Si elle ne s’ouvre pas, colle ceci :\n%s\n' % url)
    threading.Thread(target=webbrowser.open, args=(url,), daemon=True).start()
    serveur.handle_request()

    if recu.get('state') != etat:
        raise SystemExit('!! ABANDON : reponse inattendue (l’etat ne correspond pas).')
    if 'code' not in recu:
        raise SystemExit('!! Refus de Google : %s' % recu.get('error', '(sans detail)'))

    rep = _poste(JETON, {
        'client_id': cid, 'client_secret': secret, 'code': recu['code'],
        'grant_type': 'authorization_code', 'redirect_uri': redirection,
    })
    if 'refresh_token' not in rep:
        raise SystemExit('!! Google n’a pas renvoye de jeton de rafraichissement. '
                         'Revoque l’acces sur myaccount.google.com/permissions '
                         'puis recommence.')
    _ecrire({'client_id': cid, 'client_secret': secret,
             'refresh_token': rep['refresh_token']})
    print('Connecte. Jeton range dans %s (lisible par toi seul).' % IDENTIFIANTS)


# --------------------------------------------------------------------------- #
# LES TROIS LECTURES
# --------------------------------------------------------------------------- #

def sites():
    """Les proprietes auxquelles le compte connecte a acces."""
    rep = _api(WEBMASTERS + '/sites')
    for s in rep.get('siteEntry', []):
        print('  %-52s %s' % (s['siteUrl'], s.get('permissionLevel', '')))
    if not rep.get('siteEntry'):
        print('  (aucune propriete — le compte connecte n’a acces a rien)')


def indexation(urls=None):
    """L'etat d'indexation, page par page, via l'API d'inspection d'URL.

    ⚠️ CETTE API EST LIMITEE A 2 000 APPELS PAR JOUR ET 600 PAR MINUTE. Avec
       31 pages on est tres loin du plafond, mais ne pas la mettre dans une
       boucle automatique qui tournerait toutes les heures.
    """
    from urllib.parse import urljoin
    if urls:
        cibles = urls
    elif PROPRIETE == 'sc-domain:resonancesproductions.org':
        cibles = ['https://www.resonancesproductions.org' + url
                  for url, _ in verif_site.PAGES]
    else:
        raise SystemExit(
            'Pour une autre propriete que resonancesproductions.org, donne les\n'
            'adresses a inspecter :\n'
            '  python3 sources/search_console.py --site %s --indexation '
            'https://…/une-page' % PROPRIETE)
    verdicts = {}
    for u in cibles:
        rep = _api(INSPECTION + '/urlInspection/index:inspect', {
            'inspectionUrl': u, 'siteUrl': PROPRIETE, 'languageCode': 'fr'})
        r = rep.get('inspectionResult', {}).get('indexStatusResult', {})
        verdict = r.get('coverageState', '(inconnu)')
        verdicts.setdefault(verdict, []).append((u, r))
    for verdict in sorted(verdicts, key=lambda v: -len(verdicts[v])):
        lignes = verdicts[verdict]
        print('\n  %s — %d page(s)' % (verdict, len(lignes)))
        for u, r in lignes:
            canon = r.get('googleCanonical', '')
            ecart = ''
            if canon and canon.rstrip('/') != u.rstrip('/'):
                ecart = '   ⚠️ Google retient : %s' % canon
            print('     · %s%s' % (u.replace('https://www.resonancesproductions.org', '') or '/', ecart))
    print('\n  (« Submitted and indexed » = tout va bien.)')


def requetes(jours=28, combien=25):
    """Ce que les gens tapent pour tomber sur le site."""
    import datetime as dt
    fin = dt.date.today()
    debut = fin - dt.timedelta(days=jours)
    rep = _api('%s/sites/%s/searchAnalytics/query'
               % (WEBMASTERS, urllib.parse.quote(PROPRIETE, safe='')),
               {'startDate': debut.isoformat(), 'endDate': fin.isoformat(),
                'dimensions': ['query'], 'rowLimit': combien})
    lignes = rep.get('rows', [])
    if not lignes:
        print('  Aucune donnee sur %d jours (le site est jeune, c’est normal).' % jours)
        return
    print('  %-42s %6s %6s %7s %6s' % ('REQUETE', 'clics', 'impr.', 'CTR', 'pos.'))
    for l in lignes:
        print('  %-42s %6d %6d %6.1f%% %6.1f'
              % (l['keys'][0][:42], l['clicks'], l['impressions'],
                 l['ctr'] * 100, l['position']))


if __name__ == '__main__':
    args = sys.argv[1:]
    # `--site <propriete>` peut preceder n'importe quelle commande : il change
    # la propriete interrogee pour cet appel, sans toucher au fichier.
    if len(args) >= 2 and args[0] == '--site':
        PROPRIETE = args[1]
        args = args[2:]
    if not args or args[0] in ('-h', '--aide'):
        print(__doc__)
    elif args[0] == '--connexion':
        connexion(args[1] if len(args) > 1 else None)
    elif args[0] == '--sites':
        sites()
    elif args[0] == '--indexation':
        indexation(args[1:] or None)
    elif args[0] == '--requetes':
        requetes(int(args[1]) if len(args) > 1 else 28)
    else:
        raise SystemExit('Option inconnue : %s (lancer sans argument pour l’aide)' % args[0])
