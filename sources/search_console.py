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

PROPRIETE = 'sc-domain:resonancesproductions.org'
PORTEE = 'https://www.googleapis.com/auth/webmasters.readonly'
API = 'https://searchconsole.googleapis.com/v1'
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


def _poste(url, champs):
    corps = urllib.parse.urlencode(champs).encode()
    req = urllib.request.Request(url, data=corps, method='POST')
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


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


def _api(chemin, charge=None):
    url = '%s/%s' % (API, chemin)
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

def connexion():
    """Boucle OAuth « loopback » : le navigateur revient sur localhost.

    ⚠️ C'est le seul flot encore recommande par Google pour une application de
       bureau. L'ancien « copier-coller du code » (out-of-band) est ferme
       depuis 2022 : un guide qui le propose est perime.
    """
    _garde_fou_depot()
    print('Identifiants OAuth « Application de bureau » '
          '(console.cloud.google.com -> Identifiants).')
    cid = input('  ID client     : ').strip()
    secret = input('  Code secret   : ').strip()
    if not cid or not secret:
        raise SystemExit('Abandon : il manque l’ID client ou le code secret.')

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
    rep = _api('sites')
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
    cibles = urls or ['https://www.resonancesproductions.org' + url
                      for url, _ in verif_site.PAGES]
    verdicts = {}
    for u in cibles:
        rep = _api('urlInspection/index:inspect', {
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
    rep = _api('sites/%s/searchAnalytics/query' % urllib.parse.quote(PROPRIETE, safe=''),
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
    if not args or args[0] in ('-h', '--aide'):
        print(__doc__)
    elif args[0] == '--connexion':
        connexion()
    elif args[0] == '--sites':
        sites()
    elif args[0] == '--indexation':
        indexation(args[1:] or None)
    elif args[0] == '--requetes':
        requetes(int(args[1]) if len(args) > 1 else 28)
    else:
        raise SystemExit('Option inconnue : %s (lancer sans argument pour l’aide)' % args[0])
