# -*- coding: utf-8 -*-
"""Les TEXTES de l'association, en UN seul exemplaire.

POURQUOI CE FICHIER EXISTE
--------------------------
Le 15/08/2026, la page `/association` a ete creee parce que « Accueil » et
« L’association » menaient tous les deux a la page d'accueil (le second vers
l'ancre `/#association`). Le probleme de fond etait ailleurs : l'accueil faisait
CINQ metiers (`#association`, `#statuts`, `#adherer`, `#contact`,
`#prestations`) en plus de presenter les spectacles.

Une partie du texte a donc DEMENAGE de l'accueil vers `/association`, et une
autre partie est desormais VISIBLE SUR LES DEUX PAGES (l'objet en version
courte sur l'accueil, en entier sur `/association` ; les quatre engagements aux
deux endroits). Recopier ces phrases dans deux generateurs, c'est se garantir
qu'une correction de David n'en corrigerait qu'une sur deux — exactement le
scenario que `sources/theme_chaleur.py` evite deja pour le style.

D'ou ce module : UNE ecriture, DEUX generateurs qui l'appellent.

    sources/generate_assoc.py        -> /                (accueil)
    sources/generate_association.py  -> /association

⚠️ CE N'EST PAS UN GENERATEUR. Il n'ecrit aucune page, il ne s'execute pas seul,
   et il n'a donc pas de ligne dans `sources/build.py` (dont le controle
   « generateur non inscrit » ne regarde que les fichiers `generate_*.py`).
   Comme `theme_chaleur` et `nav_menu`, on peut l'importer sans risque —
   contrairement aux `generate_*.py`, qui travaillent au moment de l'import.

⚠️ CES CHAINES SONT DU HTML, pas du texte brut : elles contiennent des <b>, un
   <sup> et des <a>. Elles sont inserees telles quelles dans les gabarits. Toute
   modification ici change DEUX pages a la fois — c'est le but.

⚠️ LES CHIFFRES SONT CEUX DE L'ASSOCIATION, PAS DES EXEMPLES. Ils viennent de la
   page d'accueil publiee, ou ils figurent depuis le 04/08/2026. Ne pas les
   « arrondir » : le SIRET porte bien ses 14 chiffres (SIREN 919 514 075 + NIC
   00010), et c'est ce qu'affiche le pied de page des pages du site.
"""

# --------------------------------------------------------------------------- #
# L'OBJET
# --------------------------------------------------------------------------- #
# `OBJET_P1` est la presentation COURTE : elle reste sur l'accueil (avec le lien
# « En savoir plus ») et ouvre `/association`. `OBJET_P2` a quitte l'accueil.

OBJET_TITRE = 'Mettre l’art au service du vivant'

OBJET_P1 = (
    'L’Association <b>Résonances Productions</b> (loi 1901) a pour objectif '
    'l’<b>accompagnement</b>, la <b>promotion</b>, la <b>production</b> et le '
    '<b>soutien d’artistes</b> dans tous les domaines, ainsi que d’initier ou de '
    'soutenir des actions autour d’alternatives de toutes natures — écologiques, '
    'économiques, culturelles, techniques et humaines.'
)

OBJET_P2 = (
    'Elle s’appuie sur plusieurs supports (lettres d’information, site internet, '
    'plateformes multimédias, format papier…) et plusieurs moyens : journalisme, '
    'publications, formations, organisation d’événements. Les activités de '
    'l’association s’exercent <b>indépendamment de toute appartenance religieuse, '
    'philosophique ou politique</b>.'
)


# --------------------------------------------------------------------------- #
# LES VALEURS  (« Nos engagements · Ce qui nous anime » sur l'accueil)
# --------------------------------------------------------------------------- #
# Elles restent sur l'accueil ET figurent sur `/association` : ce sont les
# valeurs de l'association, une page qui la presente sans elles serait creuse.
# Quatre lignes courtes, donc aucun risque de « contenu duplique » au sens de
# Google — mais la source, elle, est unique.

VALS = (
    ('Le vivant',
     'Placer l’humain, la nature et la vibration au cœur de chaque projet.'),
    ('La créativité',
     'Accompagner et produire des artistes, dans tous les domaines.'),
    ('Le bien-être',
     'Proposer des expériences qui apaisent, relient et élèvent.'),
    ('L’indépendance',
     'Une démarche libre, inclusive, sans appartenance religieuse, philosophique '
     'ou politique.'),
)


# --------------------------------------------------------------------------- #
# LES STATUTS  (bloc integralement DEMENAGE de l'accueil le 15/08/2026)
# --------------------------------------------------------------------------- #
# ⚠️ L'article 2 est une CITATION des statuts deposes : il est entre guillemets
#    et reproduit l'orthographe du document officiel (« organisations
#    d’evenements », « plateforme multimedias » au singulier). Ce ne sont pas des
#    coquilles a corriger — c'est le texte depose.

# ⚠️ L'esperluette est ecrite EN CLAIR (`&`) et non `&amp;` : c'est exactement
#    ce que la page d'accueil publiait depuis le 04/08/2026. Le texte demenage
#    MOT POUR MOT, caractere pour caractere — c'est ce qui permet de prouver
#    qu'aucune phrase n'a ete perdue au passage.
STATUTS_ART1_TITRE = 'Article 1 — Constitution & dénomination'
STATUTS_ART1 = (
    'Association régie par la loi du 1<sup>er</sup> juillet 1901 et le décret du '
    '16 août 1901, sous la dénomination « <b>Résonances Productions</b> ».'
)

STATUTS_ART2_TITRE = 'Article 2 — Objet'
STATUTS_ART2 = (
    '« L’accompagnement, la promotion, la production et le soutien dans tous les '
    'domaines ainsi que d’initier ou de soutenir des actions à propos '
    'd’alternatives de toutes natures (écologiques, économiques, culturelles, '
    'techniques et humaines). Elle utilisera pour cela plusieurs supports '
    '(lettres d’information, site internet, plateforme multimédias, format papier '
    'etc.) et de plusieurs moyens (journalisme, publications, formations, '
    'organisations d’évènements etc.). Les activités de l’association s’exercent '
    'indépendamment de toute appartenance religieuse, philosophique ou politique. '
    'L’association pourra réaliser toutes opérations avec les tiers liées '
    'directement ou indirectement à son objet. »'
)

#: les trois renvois officiels, dans l'ordre ou ils etaient sur l'accueil.
URL_JOAFE = ('https://www.journal-officiel.gouv.fr/document/associations_b/'
             '201700430125')
URL_STATUTS_DOC = ('https://docs.google.com/document/d/'
                   '1NxsbvaqHsA9VOXlN7cvsav7cxFwhsK4XCpowHb75o1w/edit?usp=sharing')
URL_DATAGOUV = ('https://annuaire-entreprises.data.gouv.fr/entreprise/'
                'resonances-productions-919514075')

STATUTS_JO = (
    'Objet officiel tel que déclaré au <b>Journal officiel des associations</b>. '
    'Déclaration à la sous-préfecture de Pamiers, publiée le 28 octobre 2017 — '
    'n° RNA <b>W092002501</b>. <a href="%s" target="_blank" rel="noopener">'
    'Consulter l’annonce officielle (JOAFE)</a>' % URL_JOAFE
)

STATUTS_LIEN_DOC = ('<a href="%s" target="_blank" rel="noopener">Statuts de '
                    'l’association</a>' % URL_STATUTS_DOC)

STATUTS_LIEN_DATAGOUV = ('<a href="%s" target="_blank" rel="noopener">Fiche '
                         'officielle de l’association (annuaire des entreprises '
                         '— data.gouv.fr)</a>' % URL_DATAGOUV)


# --------------------------------------------------------------------------- #
# LES MENTIONS LEGALES
# --------------------------------------------------------------------------- #
# ⚠️ CE QUI N'EST PAS ECRIT ICI L'EST VOLONTAIREMENT. Une page de mentions
#    legales cite d'ordinaire un directeur de la publication et un hebergeur ;
#    ni l'un ni l'autre n'a ete valide par David. On n'invente pas une mention
#    legale : la question est signalee dans le rapport, pas comblee.
#
# ⚠️ Le siege social (Ariege) et l'adresse de correspondance (Paris 20e) sont
#    DEUX adresses differentes, et les deux sont publiques depuis le 04/08/2026
#    (pied de page de toutes les pages). Ne pas en supprimer une en croyant
#    corriger une incoherence.
#
# ⚠️ Ces libelles cotoient des nombres : `verif_site.controle_donnees` cherche
#    un mot du genre « code / badge / acces » suivi de chiffres, parce qu'un code
#    de portail a deja fuite DEUX FOIS sur ce projet. « Code APE : 9001Z » est
#    couvert par la liste blanche `CODES_HORS_SOUPCON` ('code ape'). Si un futur
#    libelle ajoutait « accès », « entrée » ou « badge » a cote d'un nombre, la
#    publication serait refusee — c'est voulu.

MENTIONS = (
    ('Forme juridique',
     'Association loi 1901 à but non lucratif, déclarée à la sous-préfecture de '
     'Pamiers et publiée au <i>Journal officiel des associations</i> le '
     '28 octobre 2017.'),
    ('N° RNA', 'W092002501'),
    ('SIRET', '919 514 075 00010'),
    ('Code APE', '9001Z — Arts du spectacle vivant'),
)

SIEGE_LIGNES = ('2 impasse des Bleuets', '09600 Aigues-Vives')
CORRESPONDANCE_LIGNES = ('29 rue des Orteaux', '75020 Paris')

EMAIL = 'contact@resonancesproductions.org'


# --------------------------------------------------------------------------- #
# L'ADHESION
# --------------------------------------------------------------------------- #
# ⚠️ L'URL est la page d'adhesion DIRECTE de HelloAsso (decision du 04/08/2026),
#    pas la vitrine de l'association. `nav_menu.ADHESION` porte la meme valeur
#    pour le bouton du menu ; les deux doivent rester identiques.

HELLOASSO = ('https://www.helloasso.com/beta/associations/resonances-productions'
             '/adhesions/adhesion-resonances-productions')

ADHESION_ACCROCHE = (
    'Soutenez la création et rejoignez l’aventure. Votre adhésion nous permet de '
    'financer nos actions et de couvrir nos projets.'
)


# --------------------------------------------------------------------------- #
# LE LIEN VERS /guso-facile  —  l'ancre, en UN seul exemplaire
# --------------------------------------------------------------------------- #
# POURQUOI ELLE EST ICI. Le dossier SEO (section 6) demande nommement « au moins
# un lien vers /guso-facile depuis l'accueil de Resonances » : sans lien entrant
# depuis une page que Google connait deja, une nouvelle section met beaucoup plus
# longtemps a etre decouverte. Jusqu'ici, /guso-facile et ses 19 pages de blog
# n'etaient atteintes QUE par l'entree de menu.
#
# L'accueil et /association portent chacun leur phrase — elles sont differentes,
# parce que les deux contextes le sont. Seule l'ANCRE est commune : c'est elle
# qui doit rester identique d'une page a l'autre (meme libelle, meme URL), et
# c'est elle qui casserait le maillage si l'URL bougeait a un seul endroit.
#
# ⚠️ L'ANCRE DIT OU ELLE MENE. Regle du dossier SEO : jamais « cliquez ici »,
#    jamais « en savoir plus ». Le libelle porte le nom de l'outil ET ce qu'il
#    fait.
#
# 🚩 LA FORMULATION EST DELIBEREE, DANS LES DEUX PHRASES QUI L'ENTOURENT.
#    Guso Facile est « cree par David Lesage, relaye par l'association » — JAMAIS
#    « notre outil », JAMAIS « porte par », JAMAIS « notre application ».
#    L'infrastructure est personnelle (Supabase, Vercel, depot git, e-mails au
#    nom de David) et les donnees traitees sont sensibles : numeros de securite
#    sociale, IBAN, salaires, feuillets GUSO de personnes reelles. Ecrire
#    « porte par l'association » sur le site public d'une association, a propos
#    d'un outil pareil, serait une approximation au pire endroit possible. Le
#    raisonnement complet est en tete de `sources/generate_guso.py` — fichier
#    qu'on ne touche pas d'ici.

GUSO_URL = '/guso-facile'

GUSO_ANCRE = 'Guso Facile — l’administratif de l’intermittence'

GUSO_LIEN = '<a href="%s">%s</a>' % (GUSO_URL, GUSO_ANCRE)
