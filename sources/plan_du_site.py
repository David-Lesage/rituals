# -*- coding: utf-8 -*-
"""Tient `sitemap.xml` a jour : les memes pages, avec leur VRAIE date.

POURQUOI — DEFAUT TROUVE LE 18/09/2026
--------------------------------------
Le plan du site etait ecrit A LA MAIN, et il avait vieilli sans que personne
ne le voie :

  * ONZE des trente et une adresses n'avaient AUCUNE date (`<lastmod>`) —
    justement les pages principales : l'accueil, /le-nid, /rituals, /e-motion…
  * les vingt autres annoncaient toutes « 2026-08-15 », alors que des pages
    avaient ete modifiees les 16 et 18 septembre.

Google se sert du `<lastmod>` pour decider s'il revient voir une page. Un plan
qui annonce « rien n'a change depuis le 15 aout » demande poliment a Google de
ne pas repasser. C'est genant en temps normal ; ca l'est beaucoup plus quand
on vient de corriger les balises canoniques de dix pages et qu'on attend
justement une nouvelle exploration.

CE QUI EST ECRIT, ET D'OU CA VIENT
----------------------------------
  * la liste des adresses : `verif_site.PAGES`, jamais recopiee — la meme table
    que les onze controles et que `canonique.py` ;
  * la date : celle du DERNIER COMMIT qui a touche le fichier de la page, lue
    dans git. Elle n'est donc ni inventee, ni saisie a la main, ni « la date du
    jour » (qui ferait mentir les trente pages qui n'ont pas bouge) ;
  * `changefreq` et `priority` : CONSERVEES telles qu'elles etaient. Google
    declare publiquement les ignorer, mais elles ne genent pas, et les
    supprimer serait defaire un reglage que personne n'a demande de defaire.

⚠️ IDEMPOTENT. `build.py` construit tout deux fois et exige le meme resultat a
   l'octet pres : si ce fichier ecrivait une valeur differente a chaque appel
   (une date du jour, par exemple), la verification echouerait a chaque fois.
"""

import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(HERE)
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import verif_site  # noqa: E402

PLAN = os.path.join(RACINE, 'sitemap.xml')
SITE = 'https://www.resonancesproductions.org'


def _historique_tronque():
    """Le depot n'a-t-il qu'un bout de son historique ? (clone « superficiel »)

    ⚠️ CE CAS N'EST PAS THEORIQUE. Le workflow de l'agenda clonait le depot
       avec `fetch-depth: 1` — un seul commit. `git log` aurait alors renvoye
       LA MEME DATE pour les trente et une pages, toutes les nuits. Le
       workflow demande desormais l'historique complet ; ce garde-fou est la
       pour le jour ou quelqu'un le remettrait en superficiel sans savoir ce
       qui en depend. Dans ce cas on NE TOUCHE PAS aux dates existantes :
       laisser une date un peu vieille est sans commune mesure avec en ecrire
       trente et une fausses.
    """
    try:
        r = subprocess.run(['git', 'rev-parse', '--is-shallow-repository'],
                           cwd=RACINE, capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return True                       # dans le doute, on ne touche a rien
    return (r.stdout or '').strip() != 'false'


def _date_git(fichier):
    """La date du dernier commit qui a touche ce fichier (AAAA-MM-JJ), ou None.

    ⚠️ ON NE PREND PAS LA DATE DU FICHIER SUR LE DISQUE (`os.path.getmtime`) :
       chaque `build.py` reecrit les 31 pages, elles auraient donc TOUTES la
       date du jour — exactement le mensonge qu'on veut eviter. Le dernier
       commit, lui, dit quand le contenu a reellement change.
    """
    try:
        r = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', fichier],
                           cwd=RACINE, capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return None
    date = (r.stdout or '').strip()
    return date if re.fullmatch(r'\d{4}-\d{2}-\d{2}', date) else None


def _reglages_existants():
    """{adresse: (changefreq, priority)} lus dans le plan actuel."""
    if not os.path.exists(PLAN):
        return {}
    with open(PLAN, encoding='utf-8') as f:
        plan = f.read()
    out = {}
    for bloc in re.findall(r'<url>(.*?)</url>', plan, re.S):
        loc = re.search(r'<loc>\s*([^<]+?)\s*</loc>', bloc)
        if not loc:
            continue
        cf = re.search(r'<changefreq>\s*([^<]+?)\s*</changefreq>', bloc)
        pr = re.search(r'<priority>\s*([^<]+?)\s*</priority>', bloc)
        out[loc.group(1)] = (cf.group(1) if cf else None,
                             pr.group(1) if pr else None)
    return out


def _dates_existantes():
    """{adresse: date} deja inscrites dans le plan actuel."""
    if not os.path.exists(PLAN):
        return {}
    with open(PLAN, encoding='utf-8') as f:
        plan = f.read()
    out = {}
    for bloc in re.findall(r'<url>(.*?)</url>', plan, re.S):
        loc = re.search(r'<loc>\s*([^<]+?)\s*</loc>', bloc)
        lm = re.search(r'<lastmod>\s*([^<]+?)\s*</lastmod>', bloc)
        if loc and lm:
            out[loc.group(1)] = lm.group(1)
    return out


def construire():
    """Le texte complet du plan du site."""
    reglages = _reglages_existants()
    tronque = _historique_tronque()
    anciennes = _dates_existantes()
    lignes = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, fichier in verif_site.PAGES:
        adresse = SITE + url
        cf, pr = reglages.get(adresse, (None, None))
        lignes.append('  <url>')
        lignes.append('    <loc>%s</loc>' % adresse)
        date = anciennes.get(adresse) if tronque else _date_git(fichier)
        if date:
            lignes.append('    <lastmod>%s</lastmod>' % date)
        if cf:
            lignes.append('    <changefreq>%s</changefreq>' % cf)
        if pr:
            lignes.append('    <priority>%s</priority>' % pr)
        lignes.append('  </url>')
    lignes.append('</urlset>')
    return '\n'.join(lignes) + '\n'


def ecrire():
    """Reecrit le plan du site. Renvoie True s'il a change."""
    neuf = construire()
    ancien = ''
    if os.path.exists(PLAN):
        with open(PLAN, encoding='utf-8') as f:
            ancien = f.read()
    if neuf == ancien:
        return False
    with open(PLAN, 'w', encoding='utf-8') as f:
        f.write(neuf)
    return True


if __name__ == '__main__':
    print('Plan du site mis a jour.' if ecrire()
          else 'Plan du site : deja a jour, rien a ecrire.')
