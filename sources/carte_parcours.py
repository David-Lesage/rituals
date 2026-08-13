# -*- coding: utf-8 -*-
"""
CARTE DU PARCOURS — SVG ecrit a la main, zero dependance, zero requete reseau.
===============================================================================
Genere la cartographie historique inseree dans /david-lesage-en-concert.

REGLES QUI ONT COMMANDE CE FICHIER (ne pas les defaire) :

 1. AUCUNE bibliotheque, AUCUNE tuile, AUCUN appel reseau. Le site est statique
    et sans tracker : une carte Google/OSM y introduirait une requete tierce et
    un cookie. Tout est calcule ici, en Python, a la generation, et sort en
    coordonnees EN DUR dans le SVG.

 2. AUCUN GeoJSON recopie. Le contour de la France ci-dessous (FRANCE_OUTLINE)
    est un trace SCHEMATIQUE ecrit a la main, point par point, a partir de
    reperes geographiques usuels (Dunkerque, Brest, Hendaye, Nice...). Il n'est
    pas issu d'un fichier sous licence. Il sert de repere visuel, pas de mesure :
    ce qui compte est la lisibilite des POINTS.

 3. DONNEES : recopiees de `parcours_lieux.json` (50 lieux agreges par ville,
    14/08/2026), lui-meme issu de `parcours_consolide.json`. Elles sont figees
    ici pour que le depot reste autonome : le JSON d'origine est un fichier de
    travail temporaire, hors depot.
      -> 50 lieux, dont 45 GEOLOCALISES et 5 sans coordonnees.
      -> MISE A JOUR DU 14/08/2026, apres le second export Facebook : 47 -> 50
         lieux et 38 -> 45 points. Le gain vient de 58 COORDONNEES GPS DE
         PREMIERE MAIN (saisies par les organisateurs eux-memes), prioritaires
         sur le geocodage Nominatim. Cinq lieux qui n'avaient AUCUN point en ont
         un (Le Sing Sing -> absorbe par Toulouse, Hameau de l'Etoile ->
         Saint-Martin-de-Londres, Domaine du Balbuzard -> Condat-en-Combraille,
         Sainte-Genevieve-des-Bois -> Essonne, HUG Fesztival -> Papateszer) et
         trois communes nouvelles apparaissent (Flourens, Centres,
         Cambon-et-Salvergues). Naxos est corrigee de 9,3 km (le geocodage
         renvoyait le centroide de l'ILE, pas la ville).
      -> ⚠️ SIX COORDONNEES FACEBOOK ONT ETE ECARTEES en amont (documentees dans
         le fichier de travail `lieux.py`, liste `REJETES`), dont un point qui
         tombait AU QUEBEC (« Planete Terre », interview en ligne) et le Sziget
         place 12 km du mauvais cote de Budapest. NE PAS les reintroduire.
      -> ⚠️ 11/09/2021 : le nouvel export situe ce concert a CROS (30) et non a
         SAINT-HIPPOLYTE-DU-FORT (4,2 km, meme code postal 30170). On garde
         SAINT-HIPPOLYTE-DU-FORT en attendant la confirmation de David : cette
         carte est publique, on n'y deplace pas une ville sur une deduction.
      -> les 5 sans coordonnees NE DISPARAISSENT PAS : ils sont listes en clair
         sous la carte (LIEUX_SANS_COORD). Une carte qui les avalerait en
         silence ferait mentir le total.

 4. `nb` = nombre d'EVENEMENTS recenses dans la ville, tous types confondus
    (concerts, spectacles, mais aussi ateliers, cercles, conferences). Ce n'est
    donc PAS le decompte des 112 dates de scene : la legende de la figure le dit
    explicitement. Ne jamais presenter le total des points comme un nombre de
    concerts.
    ⚠️ Marciac (+3) et Carcassonne (+1) portent les arbitrages de David du
    13/08/2026, qui restent `a-confirmer` dans `parcours_consolide.json` : le
    JSON dit 19 et 5, la carte affiche 22 et 6. Ne pas « corriger » ces deux
    nombres vers le JSON.

 5. Hors Europe : le Mont Korhogo (Cote d'Ivoire) est geolocalise mais reste
    HORS des deux cartes — un planisphere pour un seul point serait illisible.
    Il est traite par une mention en texte.
"""

import math

# ---------------------------------------------------------------------------
# 1. LES LIEUX GEOLOCALISES  (nom, departement, pays, lat, lon, nb, annees)
#    Recopie de parcours_lieux.json — ordre : du plus joue au moins joue.
# ---------------------------------------------------------------------------
LIEUX_GEO = [
    ('Marciac', '32', 'France', 43.52406, 0.16115, 22, '2009-2019'),
    ('Paris', '75', 'France', 48.86560, 2.37180, 11, '2023-2026'),
    ('Toulouse', '31', 'France', 43.61174, 1.39219, 8, '2010-2023'),
    ('Carcassonne', '11', 'France', 43.21304, 2.34911, 6, '2017-2025'),
    ('Budapest', None, 'Hongrie', 47.49788, 19.04024, 5, '2022-2024'),
    ('Dienville', '10', 'France', 48.34909, 4.53258, 5, '2024'),
    ('Montbel', '09', 'France', 42.97890, 1.96980, 5, '2019-2024'),
    ('Festes-et-Saint-André', '11', 'France', 42.96750, 2.14350, 4, '2022-2025'),
    ('Alet-les-Bains', '11', 'France', 42.99500, 2.25610, 3, '2022-2025'),
    ('Frasne-le-Château', '70', 'France', 47.46330, 5.89490, 3, '2024'),
    ('Martigny', None, 'Suisse', 46.10312, 7.07274, 3, '2023'),
    ('Mirepoix', '09', 'France', 43.08850, 1.87380, 3, '2017-2021'),
    ('Roquefort-les-Cascades', '09', 'France', 42.95818, 1.76306, 3, '2019'),
    ('Tourcoing', '59', 'France', 50.70590, 3.15610, 3, '2023'),
    ('Aigues-Vives', '09', 'France', 42.99630, 1.87510, 2, '2021'),
    # NOUVELLE COMMUNE (2e export) : Salon sante nature, 17/09/2016.
    ('Flourens', '31', 'France', 43.59477, 1.56233, 2, '2016'),
    ('Pamiers', '09', 'France', 43.12270, 1.60360, 2, '2022'),
    # NOUVELLE CLE : le « Hameau de l'Etoile » n'avait aucun point ; il rejoint
    # sa commune, desormais geolocalisee (code postal 34380 dans l'adresse).
    ('Saint-Martin-de-Londres', '34', 'France', 43.81940, 3.69890, 2, '2022'),
    ('Bambecque', '59', 'France', 50.90126, 2.54768, 1, '2026'),
    # NOUVELLE COMMUNE (2e export) : spectacle E-Motion, 08/06/2024.
    ('Cambon-et-Salvergues', '34', 'France', 43.62097, 2.85554, 1, '2024'),
    # NOUVELLE COMMUNE (2e export) : experience immersive, 03/12/2023.
    ('Centrès', '12', 'France', 44.16386, 2.40763, 1, '2023'),
    # NOUVELLE CLE : le « Domaine du Balbuzard » n'avait aucun point ; il rejoint
    # sa commune (reverse-geocodage du point Facebook -> Puy-de-Dome 63380).
    ('Condat-en-Combraille', '63', 'France', 45.84458, 2.56181, 1, '2021'),
    ('Daumazan-sur-Arize', '09', 'France', 43.14400, 1.30750, 1, '2023'),
    ('Espéraza', '11', 'France', 42.93450, 2.22380, 1, '2025'),
    ('Estrée-Cauchy', '62', 'France', 50.39838, 2.60894, 1, '2023'),
    ('Fatouville-Grestain', '27', 'France', 49.40542, 0.32745, 1, '2023'),
    ('Latrape', '31', 'France', 43.24537, 1.28654, 1, '2022'),
    ('Lavaur', '81', 'France', 43.69893, 1.81519, 1, '2009'),
    ('Le Bosc', '09', 'France', 42.94712, 1.45959, 1, '2025'),
    # COORDONNEE CORRIGEE (14/08/2026) : l'ancien point etait le centroide de
    # l'ILE de Naxos, a 9,3 km de la ville. Point Facebook (adresse « Naxos,
    # 84300 Naxos ») confirme a 400 m par une requete Nominatim ciblee.
    ('Naxos', None, 'Grèce', 37.10220, 25.38030, 1, '2022'),
    ('Perpignan', '66', 'France', 42.69853, 2.89531, 1, '2023'),
    ('Plaisance', '32', 'France', 43.60638, 0.04895, 1, '2014'),
    ('Puivert', '11', 'France', 42.91991, 2.04645, 1, '2023'),
    # NOUVELLE COMMUNE : HUG Fesztival 2022, enfin situe. Reserve honnete : le
    # point Facebook tombe a ~15 km a l'est du bourg geocode par Nominatim et son
    # reverse-geocodage renvoie la commune voisine (meme code postal 8430). A
    # l'echelle d'une carte de pays, sans effet.
    ('Pápateszér', None, 'Hongrie', 47.35934, 17.89593, 1, '2022'),
    ('Rennes-le-Château', '11', 'France', 42.92725, 2.26275, 1, '2025'),
    ('Rennes-les-Bains', '11', 'France', 42.92050, 2.32060, 1, '2024'),
    ('Saint-Geniez-d’Olt', '12', 'France', 44.46580, 2.97440, 1, '2022'),
    ('Saint-Gervais-les-Bains', '74', 'France', 45.89285, 6.71133, 1, '2023'),
    # ⚠️ NE PAS remplacer par Cros (30) sans l'accord de David : voir la regle 3.
    ('Saint-Hippolyte-du-Fort', '30', 'France', 43.96436, 3.85644, 1, '2021'),
    ('Sainte-Camelle', '09', 'France', 43.26900, 1.80548, 1, '2016'),
    # Departement tranche par David (13/08/2026) : Essonne (91), et non le
    # Loiret. Le 2e export apporte en plus un point GPS de premiere main, dont le
    # reverse-geocodage confirme 91700. La SALLE reste inconnue : rien d'invente.
    ('Sainte-Geneviève-des-Bois', '91', 'France', 48.63780, 2.33240, 1, '2023'),
    ('Siófok', None, 'Hongrie', 46.90717, 18.05416, 1, '2024'),
    ('Vevey', None, 'Suisse', 46.46030, 6.84187, 1, '2023'),
    ('Villefort', '11', 'France', 42.95395, 2.03187, 1, '2023'),
    # HORS EUROPE — geolocalise mais volontairement absent des deux cartes.
    ('Korhogo', None, 'Côte d’Ivoire', 9.45807, -5.63163, 1, ''),
]
HORS_EUROPE = {'Korhogo'}

# ---------------------------------------------------------------------------
# 2. LES 5 LIEUX SANS COORDONNEES — affiches en texte sous la carte.
#    (libelle publiable, pays, nb d'evenements, annees)
#    Ils etaient 8 : le second export Facebook (14/08/2026) en a sorti trois —
#    le Domaine du Balbuzard, le Hameau de l'Etoile et Le Sing Sing ont rejoint
#    leur commune, desormais geolocalisee. Restent ceux que Facebook ne contient
#    pas du tout : la Hongrie sans ville, l'Ardeche, la Belgique, le Mas Galifa
#    et la Reflex Straw House. Ces cinq-la ne sortiront pas de cette source.
# ---------------------------------------------------------------------------
LIEUX_SANS_COORD = [
    ('Hongrie, ville non précisée par les sources', 'Hongrie', 6, '2023-2024'),
    ('Reflex Straw House, Hongrie', 'Hongrie', 1, '2023'),
    ('Belgique, ville non précisée', 'Belgique', 1, '2025'),
    ('Chapelle du Mas Galifa, Espagne', 'Espagne', 1, 'sans date'),
    ('Ardèche, commune inconnue', 'France', 1, '2014'),
]

# Garde-fous de coherence avec parcours_lieux.json du 14/08/2026
# (50 lieux / 45 geolocalises / 5 sans coordonnees), Cros non applique.
assert len(LIEUX_GEO) == 45, f'attendu 45 lieux geolocalises, {len(LIEUX_GEO)} trouves'
assert len(LIEUX_SANS_COORD) == 5, 'attendu 5 lieux sans coordonnees'
NB_LIEUX = len(LIEUX_GEO) + len(LIEUX_SANS_COORD)
assert NB_LIEUX == 50, f'attendu 50 lieux au total, {NB_LIEUX} trouves'

# ---------------------------------------------------------------------------
# 3. CONTOUR SCHEMATIQUE DE LA FRANCE — ecrit a la main (lon, lat).
#    Sens horaire depuis Dunkerque. Une trentaine de points : assez pour que la
#    forme soit reconnue au premier coup d'oeil, pas assez pour pretendre a une
#    precision cartographique — et c'est voulu (cf. regle 2 en tete de fichier).
# ---------------------------------------------------------------------------
FRANCE_OUTLINE = [
    (2.37, 51.03),   # Dunkerque
    (3.06, 50.63),   # Lille
    (4.20, 50.09),   # Ardennes
    (4.85, 49.79),
    (5.77, 49.52),   # Longwy
    (6.30, 49.16),
    (7.35, 49.15),
    (7.75, 48.58),   # Strasbourg
    (7.59, 47.56),   # Mulhouse / Bale
    (6.85, 47.12),
    (6.10, 46.28),   # Geneve
    (6.86, 45.83),   # Mont-Blanc
    (7.00, 45.10),
    (6.63, 44.90),   # Brianconnais
    (7.00, 44.25),
    (7.52, 43.78),   # Menton
    (6.30, 43.12),   # Var
    (5.37, 43.30),   # Marseille
    (4.85, 43.35),   # Fos
    (4.05, 43.45),   # Camargue
    (3.30, 43.28),   # Sete
    (3.03, 42.44),   # Cerbere
    (1.72, 42.50),   # Andorre
    (0.65, 42.72),   # Luchon
    (-0.75, 42.95),  # Pyrenees atlantiques
    (-1.79, 43.35),  # Hendaye
    (-1.25, 44.65),  # Arcachon
    (-1.03, 45.62),  # Royan
    (-1.15, 46.16),  # La Rochelle
    (-2.20, 47.28),  # Saint-Nazaire
    (-2.75, 47.50),  # embouchure de la Vilaine
    (-3.12, 47.48),  # Quiberon
    (-4.09, 47.80),  # Penmarc'h
    (-4.79, 48.04),  # Pointe du Raz
    (-4.55, 48.29),  # rade de Brest
    (-4.77, 48.45),  # Le Conquet
    (-4.35, 48.68),  # Ploudalmezeau
    (-3.55, 48.68),  # Tregor
    (-2.76, 48.51),  # Saint-Brieuc
    (-1.98, 48.68),  # Saint-Malo
    (-1.57, 48.63),  # baie du Mont-Saint-Michel
    (-1.60, 49.10),  # Granville
    (-1.79, 49.30),  # Carteret
    (-1.94, 49.66),  # cap de la Hague
    (-1.28, 49.68),  # Barfleur
    (-1.10, 49.35),  # baie des Veys
    (-0.30, 49.30),  # Ouistreham
    (0.11, 49.49),   # Le Havre
    (1.08, 49.93),   # Dieppe
    (1.85, 50.96),   # Calais
]

CORSE_OUTLINE = [
    (9.35, 42.98), (9.55, 42.62), (9.45, 42.05), (9.28, 41.42),
    (8.78, 41.55), (8.58, 42.28), (8.72, 42.62), (9.10, 42.70),
]

# ---------------------------------------------------------------------------
# 4. Projection : equirectangulaire corrigee par cos(latitude moyenne).
#    A l'echelle de la France comme de l'Europe de l'Ouest, c'est visuellement
#    indiscernable d'un Mercator et ca ne deforme pas les distances nord-sud.
# ---------------------------------------------------------------------------
class Vue:
    def __init__(self, lon0, lon1, lat0, lat1, largeur, marge):
        self.lon0, self.lon1, self.lat0, self.lat1 = lon0, lon1, lat0, lat1
        self.marge = marge
        self.k = math.cos(math.radians((lat0 + lat1) / 2))
        self.ech = largeur / ((lon1 - lon0) * self.k)
        self.w = largeur + 2 * marge
        self.h = (lat1 - lat0) * self.ech + 2 * marge

    def xy(self, lon, lat):
        x = self.marge + (lon - self.lon0) * self.k * self.ech
        y = self.marge + (self.lat1 - lat) * self.ech
        return round(x, 1), round(y, 1)


def _path(vue, pts, ferme=True):
    d = []
    for i, (lon, lat) in enumerate(pts):
        x, y = vue.xy(lon, lat)
        d.append(('M' if i == 0 else 'L') + f'{x} {y}')
    if ferme:
        d.append('Z')
    return ' '.join(d)


def rayon(nb):
    """Rayon croissant avec le nombre d'evenements. En racine carree : c'est la
    SURFACE du disque qui suit le nombre, comme le veut la perception."""
    return round(3.1 + 2.05 * math.sqrt(nb), 2)


# ---------------------------------------------------------------------------
# 5. Placement des etiquettes : quatre positions essayees dans l'ordre, la
#    premiere qui n'entre en collision avec rien est retenue. Si les quatre
#    sont prises, l'etiquette est ABANDONNEE (le point reste, et la ville est
#    de toute facon nommee dans la liste sous la carte). C'est le seul moyen
#    d'avoir une carte lisible avec la grappe Ariege/Aude.
# ---------------------------------------------------------------------------
def _place_labels(cands, vue, taille, obstacles=()):
    """cands : liste de (nom, x, y, r) triee par importance decroissante.
    `obstacles` : boites (x0,y0,x1,y1) deja occupees — on y met les DISQUES, pour
    qu'aucune etiquette ne se pose par-dessus un point."""
    poses, boites = [], list(obstacles)
    larg_car = taille * 0.52
    for nom, x, y, r in cands:
        w, h = len(nom) * larg_car + 4, taille + 3
        # QUATRE positions cardinales, puis QUATRE diagonales en repli.
        # ⚠️ Les diagonales ont ete ajoutees le 14/08/2026 : avec les nouvelles
        # coordonnees GPS, Toulouse (3e ville la plus jouee) et Siofok perdaient
        # leur etiquette faute de place, alors que la legende les annonce. Avec
        # huit essais, les six villes francaises les plus jouees et les six lieux
        # europeens retrouvent tous une etiquette. Ne pas retirer les diagonales
        # sans revenir verifier la liste des etiquettes reellement posees.
        d = 0.72                      # decalage diagonal, en fraction du rayon
        essais = [
            (x + r + 5, y + h * 0.32, 'start'),
            (x - r - 5 - w, y + h * 0.32, 'start'),
            (x - w / 2, y - r - 5, 'start'),
            (x - w / 2, y + r + h, 'start'),
            (x + r * d + 5, y - r * d - 4, 'start'),
            (x - r * d - 5 - w, y - r * d - 4, 'start'),
            (x + r * d + 5, y + r * d + h, 'start'),
            (x - r * d - 5 - w, y + r * d + h, 'start'),
            # Dessus / dessous, mais DECALES : le bord de l'etiquette est aligne
            # sur un bord du disque au lieu d'etre centre dessus. C'est ce qui
            # sauve Toulouse, dont l'etiquette (85 px) ne rentre nulle part
            # centree, prise entre Marciac a l'ouest, Lavaur a l'est et Centres
            # au nord-est.
            (x - w + r, y - r - 5, 'start'),
            (x - r, y - r - 5, 'start'),
            (x - w + r, y + r + h, 'start'),
            (x - r, y + r + h, 'start'),
        ]
        for bx, by, anc in essais:
            b = (bx, by - h, bx + w, by + 2)
            if b[0] < 1 or b[2] > vue.w - 1 or b[1] < 1 or b[3] > vue.h - 1:
                continue
            if any(not (b[2] < o[0] or b[0] > o[2] or b[3] < o[1] or b[1] > o[3])
                   for o in boites):
                continue
            boites.append(b)
            poses.append((nom, round(bx, 1), round(by, 1), anc))
            break
    return poses


def _esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('’', '&#8217;'))


def _pt(nom, x, y, r, infobulle, cls='cp-pt'):
    return (f'<g class="{cls}"><title>{_esc(infobulle)}</title>'
            f'<circle cx="{x}" cy="{y}" r="{r}"/></g>')


# ---------------------------------------------------------------------------
# 6. Vue principale : la France
# ---------------------------------------------------------------------------
def _svg_france():
    vue = Vue(-5.4, 8.6, 41.2, 51.5, largeur=548, marge=13)
    fr = [l for l in LIEUX_GEO if l[2] == 'France']
    fr.sort(key=lambda l: (-l[5], l[0]))

    pts, cands, disques = [], [], []
    for nom, dep, _pays, lat, lon, nb, annees in fr:
        x, y = vue.xy(lon, lat)
        r = rayon(nb)
        ou = f'{nom} ({dep})' if dep else nom
        bulle = f'{ou} — {nb} événement' + ('s' if nb > 1 else '')
        if annees:
            bulle += f' · {annees}'
        pts.append((nb, _pt(nom, x, y, r, bulle)))
        disques.append((x - r - 1, y - r - 1, x + r + 1, y + r + 1))
        # ETIQUETTES : seules les SIX villes les plus jouees en portent une —
        # exactement les six que la legende nomme en clair sous la carte. Deux
        # raisons : (1) avec les 32, la grappe Ariege / Aude devenait un pate
        # illisible ; (2) le texte d'un SVG se reduit avec le SVG, et il faut
        # donc peu d'etiquettes mais assez grandes pour rester lisibles (13
        # unites -> ~14 a 20 px rendus sur ecran large). Sous 700 px les
        # etiquettes sont masquees par CSS : elles seraient illisibles, et elles
        # n'apporteraient rien puisque la legende porte les memes six noms.
        if nb >= 5:
            cands.append((f'{nom} · {nb}', x, y, r))
        # ETAT MESURE AU 14/08/2026 : cinq des six etiquettes trouvent une place
        # (Marciac, Paris, Toulouse, Carcassonne, Dienville). MONTBEL est au coeur
        # de la grappe Ariege / Aude et son etiquette est ABANDONNEE — c'est le
        # comportement voulu de _place_labels, pas un bug : son point reste, et la
        # legende sous la carte la nomme avec son nombre. Ne pas forcer une
        # etiquette qui recouvrirait cinq autres points.

    # les gros points passent DERRIERE les petits : un point 1 evenement pose sur
    # un point 19 reste visible.
    pts.sort(key=lambda p: -p[0])
    labels = _place_labels(cands, vue, 13.0, obstacles=disques)

    return f'''<svg class="cp-svg" viewBox="0 0 {round(vue.w)} {round(vue.h)}" role="img"
     aria-labelledby="cp-fr-t cp-fr-d" preserveAspectRatio="xMidYMid meet">
  <title id="cp-fr-t">Carte de France des villes où David Lesage s’est produit</title>
  <desc id="cp-fr-d">Contour schématique de la France. Chaque disque doré marque une ville ; son diamètre croît avec le nombre d’événements recensés. Les plus gros disques sont Marciac dans le Gers, avec vingt-deux événements, Paris avec onze, Toulouse avec huit, Carcassonne avec six, puis Dienville et Montbel avec cinq chacun. Une grappe dense de villes se trouve dans l’Ariège et l’Aude, au sud-ouest ; le nord-est en compte quelques-unes, dont Tourcoing et Bambecque tout au nord. La liste complète des villes figure en toutes lettres sous la carte.</desc>
  <path class="cp-terre" d="{_path(vue, FRANCE_OUTLINE)}"/>
  <path class="cp-terre" d="{_path(vue, CORSE_OUTLINE)}"/>
  <g class="cp-pts">{''.join(h for _, h in pts)}</g>
  <g class="cp-lab">{''.join(f'<text x="{x}" y="{y}" text-anchor="{a}">{_esc(n)}</text>' for n, x, y, a in labels)}</g>
</svg>'''


# ---------------------------------------------------------------------------
# 7. Encart : l'Europe
#    Aucun contour recopie ici non plus : la silhouette de la France (le meme
#    trace qu'au-dessus) sert d'ancre, et une grille de meridiens / paralleles
#    tous les 5 degres donne l'echelle. Dessiner de memoire des contours d'Italie
#    ou de Grece serait faux ET moins lisible.
# ---------------------------------------------------------------------------
def _svg_europe():
    vue = Vue(-7.0, 27.5, 36.0, 52.5, largeur=418, marge=12)
    grille = []
    for lon in range(-5, 30, 5):
        x0, y0 = vue.xy(lon, 36.0)
        x1, y1 = vue.xy(lon, 52.5)
        grille.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}"/>')
    for lat in range(40, 55, 5):
        x0, y0 = vue.xy(-7.0, lat)
        x1, y1 = vue.xy(27.5, lat)
        grille.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}"/>')

    petits, gros, cands, disques = [], [], [], []
    for nom, dep, pays, lat, lon, nb, annees in LIEUX_GEO:
        if nom in HORS_EUROPE:
            continue
        x, y = vue.xy(lon, lat)
        if pays == 'France':
            petits.append(f'<circle cx="{x}" cy="{y}" r="1.9"/>')
            disques.append((x - 3, y - 3, x + 3, y + 3))
        else:
            r = max(3.4, rayon(nb) * 0.82)
            bulle = f'{nom} ({pays}) — {nb} événement' + ('s' if nb > 1 else '')
            if annees:
                bulle += f' · {annees}'
            gros.append((nb, _pt(nom, x, y, r, bulle)))
            # Le pays n'est PAS dans l'etiquette (les cinq libelles se
            # chevauchaient) : il est dans l'infobulle ET en clair dans la
            # legende sous la carte.
            cands.append((nom, x, y, r))
            disques.append((x - r - 1, y - r - 1, x + r + 1, y + r + 1))
    gros.sort(key=lambda p: -p[0])
    labels = _place_labels(cands, vue, 12.0, obstacles=disques)

    return f'''<svg class="cp-svg" viewBox="0 0 {round(vue.w)} {round(vue.h)}" role="img"
     aria-labelledby="cp-eu-t cp-eu-d" preserveAspectRatio="xMidYMid meet">
  <title id="cp-eu-t">Encart : les scènes européennes hors de France</title>
  <desc id="cp-eu-d">Même projection, cadre élargi à l’Europe. La silhouette de la France sert de repère, sur une grille de méridiens et de parallèles tous les cinq degrés. Les villes françaises y sont réduites à de petits points. Six lieux hors de France sont marqués : Budapest, Pápateszér et Siófok en Hongrie, à l’est ; Martigny et Vevey en Suisse ; et Naxos, en Grèce, au sud-est. Six dates hongroises supplémentaires, dont les sources ne précisent pas la ville, et une date en Belgique ne peuvent pas être placées ; elles sont citées sous la carte.</desc>
  <g class="cp-grille">{''.join(grille)}</g>
  <path class="cp-terre cp-terre-fine" d="{_path(vue, FRANCE_OUTLINE)}"/>
  <g class="cp-pts cp-pts-min">{''.join(petits)}</g>
  <g class="cp-pts">{''.join(h for _, h in gros)}</g>
  <g class="cp-lab cp-lab-eu">{''.join(f'<text x="{x}" y="{y}" text-anchor="{a}">{_esc(n)}</text>' for n, x, y, a in labels)}</g>
</svg>'''


# ---------------------------------------------------------------------------
# 8. Le bloc complet : figure + legende + les lieux non placables, en clair.
# ---------------------------------------------------------------------------
def _liste_sans_coord():
    li = ''.join(
        f'<li><b>{_esc(nom)}</b><span>{nb} événement{"s" if nb > 1 else ""}'
        f' · {_esc(an)}</span></li>'
        for nom, _pays, nb, an in LIEUX_SANS_COORD)
    return f'<ul class="cp-hors">{li}</ul>'


def carte_html():
    """Le bloc entier, pret a inserer. Aucune requete, aucun script."""
    return f'''<figure class="cp-fig">
  <div class="cp-cadre">
    <div class="cp-main">{_svg_france()}</div>
    <div class="cp-encart">
      <div class="cp-encart-t">L’Europe, en encart</div>
      {_svg_europe()}
    </div>
  </div>
  <figcaption>
    <b>50 lieux distincts, dans 7 pays.</b> Chaque disque est une ville ; son diamètre
    croît avec le nombre d’événements que les sources y recensent — concerts et
    spectacles, mais aussi ateliers, cercles et conférences, et les quelques scènes
    dont la date exacte n’est plus connue. Les six villes les plus jouées :
    <b>Marciac</b> (Gers) 22, <b>Paris</b> 11, <b>Toulouse</b> 8,
    <b>Carcassonne</b> 6, <b>Dienville</b> (Aube) 5, <b>Montbel</b> (Ariège) 5.
    Hors de France, six villes sont placées dans l’encart : <b>Budapest</b>,
    <b>Pápateszér</b> et <b>Siófok</b> (Hongrie), <b>Martigny</b> et <b>Vevey</b>
    (Suisse), <b>Naxos</b> (Grèce). <b>45 des 50 lieux sont géolocalisés</b> : 44
    sont dessinés ici, le 45<sup>e</sup> étant hors du cadre européen — voir la note
    sous la carte. Seules les villes les plus jouées portent leur nom dessus ; les
    autres gardent leur point et sont nommées dans la chronologie.
  </figcaption>
  <div class="cp-note">
    <p><b>Les 5 lieux que la carte ne peut pas placer.</b> Les sources ne les situent
    pas à la commune : ils ne sont pas sur la carte, mais ils sont bien dans le
    parcours, et les voici. Ils étaient huit : trois ont enfin trouvé leur commune.</p>
    {_liste_sans_coord()}
    <p>Hors du cadre européen, une date de plus : un concert solo au <b>Mont Korhogo,
    en Côte d’Ivoire</b>. Un planisphère entier pour un seul point serait illisible :
    elle est donc citée ici plutôt que dessinée.</p>
  </div>
</figure>'''


# ---------------------------------------------------------------------------
# 9. Styles. Palette de la page (or / nuit) : aucune couleur nouvelle, tout
#    passe par les variables CSS deja definies en tete de la feuille.
# ---------------------------------------------------------------------------
CSS_CARTE = """
/* ===== Carte du parcours (SVG ecrit a la main, aucune dependance) ========= */
.cp-fig{margin:30px 0 0;max-width:920px}
.cp-cadre{display:grid;grid-template-columns:minmax(0,1fr);gap:18px;
  background:radial-gradient(120% 100% at 20% 0,rgba(143,122,209,.14),transparent 60%),var(--card);
  border:1px solid var(--line);border-radius:16px;padding:20px 20px 22px}
.cp-svg{display:block;width:100%;height:auto;max-width:100%}
.cp-main{min-width:0}
.cp-encart{min-width:0;border-top:1px solid rgba(255,255,255,.08);padding-top:16px}
.cp-encart-t{color:var(--gold);font-size:12px;letter-spacing:.18em;text-transform:uppercase;
  font-weight:600;margin-bottom:10px}
.cp-terre{fill:rgba(216,178,90,.07);stroke:rgba(216,178,90,.42);stroke-width:1.1;
  stroke-linejoin:round}
.cp-terre-fine{fill:rgba(216,178,90,.09);stroke:rgba(216,178,90,.34);stroke-width:.8}
.cp-grille line{stroke:rgba(255,255,255,.07);stroke-width:.6}
.cp-pts circle{fill:var(--gold2);fill-opacity:.62;stroke:var(--gold);stroke-width:.9}
.cp-pts-min circle{fill:var(--gold2);fill-opacity:.34;stroke:none}
.cp-pt{transition:none}
.cp-pt:hover circle{fill-opacity:.95;stroke:#fff}
.cp-lab text{fill:#e6e2f5;font-family:'Jost',sans-serif;font-size:13px;
  paint-order:stroke;stroke:rgba(14,15,36,.85);stroke-width:2.4px;stroke-linejoin:round}
.cp-lab-eu text{font-size:12px;fill:var(--gold2)}
.cp-fig figcaption{color:#d7d4ea;font-size:14.5px;line-height:1.65;padding:14px 2px 0}
.cp-note{margin-top:16px;background:rgba(25,27,61,.55);border:1px solid rgba(255,255,255,.07);
  border-left:2px solid var(--gold);border-radius:14px;padding:18px 20px}
.cp-note p{color:#d7d4ea;font-size:14.5px;line-height:1.65;margin:0;max-width:none}
.cp-note p+p{margin-top:12px}
.cp-hors{list-style:none;margin:12px 0;display:grid;gap:2px}
.cp-hors li{display:flex;gap:2px 18px;align-items:baseline;flex-wrap:wrap;padding:8px 0;
  border-bottom:1px solid rgba(255,255,255,.06)}
.cp-hors li:last-child{border-bottom:0}
.cp-hors li b{flex:1 1 220px;min-width:0;color:#fff;font-weight:500;font-size:15px;line-height:1.45}
.cp-hors li span{flex:0 1 190px;min-width:0;color:var(--muted);font-size:13.5px;line-height:1.5}
/* MISE EN PAGE : la vue France occupe TOUTE la largeur du cadre, l'encart Europe
   se place dessous, borne a 460 px. Raison mesuree : le texte d'un SVG se reduit
   avec le SVG. Cote a cote, la carte de France ne faisait que 500 px de large
   pour un viewBox de 574 -> les etiquettes tombaient a 8 px rendus, sous le
   plancher typographique de 13 px du site. En pleine largeur elle atteint
   840 px, soit ~19 px rendus. */
.cp-encart{max-width:460px}
/* Sous 700 px les etiquettes du SVG seraient illisibles (la carte ne fait plus
   que ~300 px de large) : on les masque. Aucune information n'est perdue — la
   legende sous la carte nomme les memes villes avec leur nombre, et la
   chronologie juste au-dessus nomme toutes les autres. */
@media(max-width:700px){.cp-lab{display:none}}
@media(max-width:560px){
  .cp-cadre{padding:14px 13px 16px}
  .cp-note{padding:16px 15px}
}
"""
