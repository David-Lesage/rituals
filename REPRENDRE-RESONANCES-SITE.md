# REPRENDRE — Site Résonances Productions

> Handoff du projet. Complément du document de reprise complet :
> `Drive partagés/1 - RESONANCES PRODUCTIONS/SITE_WEB_DEV/HANDOFF_CLAUDE_CODE.md`.
> ⚠️ Dépôt GitHub **PUBLIC** : jamais de code d'accès ni de secret ici.
> ⚠️ ~40 Mo d'images → `git config http.postBuffer 524288000` (fait) sinon le push échoue en HTTP 400.
> ⚠️ `git` de `/usr/bin` est bloqué par la licence Xcode → `export DEVELOPER_DIR=/Library/Developer/CommandLineTools`. Correctif définitif : `sudo xcodebuild -license`.

---

# 🟢 COMMENT ON MODIFIE LE SITE — la marche à suivre (14/08/2026)

*Cette section est écrite pour David. Pas besoin d'être développeur pour la suivre.*

## Ce qui se passe quand tu demandes une modification

Quatre étapes, toujours les mêmes, toujours dans cet ordre :

| | Quoi | La commande |
|---|---|---|
| 1 | On modifie **la source**, pas la page | (dans `sources/`) |
| 2 | On **reconstruit** le site | `python3 sources/build.py` |
| 3 | On **vérifie** les 10 pages | `python3 sources/verif_site.py` |
| 4 | On **sauvegarde et on publie** | `git add …` puis `git commit` puis `git push` |

Puis **Vercel met le site en ligne tout seul, environ 40 secondes après le `push`**.
Il n'y a rien d'autre à faire, aucun bouton à cliquer nulle part.

> **`git push` = publier.** Sur ce projet, pousser et mettre en ligne sont la même
> chose. C'est pour ça qu'il y a maintenant une vérification automatique juste avant
> (voir plus bas).

## Pourquoi on ne modifie jamais le fichier HTML directement

La plupart des pages ne sont pas écrites à la main : elles sont **fabriquées** par un
script Python, à partir d'une source. Si on corrige une faute directement dans la page,
la correction disparaît **à la prochaine reconstruction** — le script réécrit la page en
entier par-dessus. C'est déjà arrivé.

Pour savoir si une page a un générateur :

```bash
python3 sources/build.py --liste
```

Le tableau dit, pour chacune des 10 pages, quel script la fabrique. Les seules pages
qu'on a le droit de modifier à la main sont celles marquées **« aucun générateur »**.

## Les deux commandes à connaître

```bash
python3 sources/build.py               # reconstruit tout le site
python3 sources/build.py --page le-nid  # ou juste une page
```

`build.py` connaît l'ordre des opérations (quel script, faut-il reposer le menu
derrière, faut-il recopier un fichier intermédiaire). Il construit **chaque page deux
fois et compare** : si le résultat n'est pas identique, c'est qu'un bloc s'ajoute à
chaque passage — le défaut qui avait produit quatre entrées « Agenda » dans le menu et
quatre cartes identiques. Dans ce cas il **s'arrête et remet tout comme avant**.

```bash
python3 sources/verif_site.py          # vérifie les 10 pages
```

Neuf contrôles, un par incident déjà vécu sur ce projet. Il ne modifie rien.
Il finit par **« 10/10 pages conformes »** quand tout va bien.

## La sécurité automatique — tu n'as rien à lancer

Deux garde-fous se déclenchent tout seuls (activés une fois pour toutes par
`git config core.hooksPath .githooks`) :

- **au moment de `git commit`** : refuse un fichier `Icon` de Google Drive, un fichier
  de plus de 10 Mo qui n'est pas une image, ou tout ce qui ressemble à une clé ou à un
  **code d'accès** (le dépôt est public — un code de portail a déjà fuité deux fois).
- **au moment de `git push`** : lance la vérification des 10 pages et **refuse de publier**
  si quoi que ce soit cloche. Une page cassée ne peut plus partir en ligne.

## Comment vérifier que la mise en ligne a bien eu lieu

1. Attendre ~40 secondes après le `push`.
2. Ouvrir `https://www.resonancesproductions.org/` (ou la page modifiée) et **recharger
   en forçant** : `Cmd + Shift + R`. Sans ça, le navigateur peut afficher l'ancienne
   version gardée en mémoire.
3. Si le changement n'apparaît pas, vérifier que le push est bien parti :
   `git log origin/main --oneline -1` doit afficher ta dernière sauvegarde.

## Que faire si une vérification bloque

Le message dit **ce qui ne va pas et sur quelle page**, en français, une ligne par
problème. Dans l'ordre :

1. Lire la ou les lignes qui commencent par `>`.
2. Corriger **la source** dans `sources/` (jamais la page HTML si elle a un générateur).
3. `python3 sources/build.py` puis `python3 sources/verif_site.py`.
4. Quand c'est `10/10`, refaire `git commit` et `git push`.

**En cas d'urgence absolue**, on peut passer outre avec `git commit --no-verify` ou
`git push --no-verify` — mais ce qui a été signalé se retrouve alors en ligne. À ne
faire qu'en sachant précisément pourquoi.

## Sur une nouvelle copie du dépôt (nouvel ordinateur, nouveau clone)

Une seule commande à taper une fois, sinon les garde-fous ne se déclenchent pas :

```bash
git config core.hooksPath .githooks
```

---

## LES 10 PAGES EN LIGNE (2026-08-14)

| URL | Rôle | Public |
|---|---|---|
| `/` | Accueil association | mixte |
| `/rituals` | Concert-rituel duo | programmateurs |
| `/rituals-trio` | Concert-rituel trio (avec Julien Dub) | programmateurs |
| `/e-motion` | Spectacle immersif participatif (ID duo) | programmateurs |
| `/david-lesage-en-concert` | **Concerts solo — grandes scènes & festivals** + fiche technique | programmateurs |
| `/concerts-david-lesage` | **Concerts solo — version intimiste au Nid** | particuliers Paris |
| `/le-nid` | Le lieu, programme, agenda | particuliers Paris |
| `/le-soin-soa` | Week-end d'immersion (Iris, Gaïa, David) | particuliers |
| `/rythme-calebasse` | Workshops + appel à candidature groupe de pratique | particuliers |
| `/association` | **L'association** : objet, valeurs, statuts, mentions légales, adresses, adhésion, contact | mixte |
| `/guso-facile` | **Outil web d'administratif de l'intermittence** (bêta privée) | **artistes intermittents** et structures qui les emploient |

### ⚠️ `/guso-facile` — la formulation est délibérée, ne pas la « corriger »

La page dit que Guso Facile est **« créé par David Lesage, relayé par Résonances
Productions »**, et **jamais « porté par »**. Ce n'est pas une maladresse :

- l'infrastructure est **entièrement personnelle** (projets Supabase et Vercel sur les
  comptes propres de David, dépôt git privé à son nom, e-mails via son Workspace
  `contact@lesagedavid.fr`) ;
- les données traitées sont **sensibles** : numéros de sécurité sociale, IBAN, salaires,
  feuillets GUSO de personnes réelles ;
- le modèle payant + affiliation envisagé est, en l'état, hors du champ associatif.

Écrire « porté par l'association » sur le site public d'une association, à propos d'un
outil qui traite des numéros de sécurité sociale, serait une approximation au pire
endroit possible. Un portage associatif demanderait une **décision explicite, actée en
procès-verbal**. Les mots retenus sont donc : « créé par », « relaie », « n'est pas un
service de l'association ». Le raisonnement complet est en tête de
`sources/generate_guso.py`. **Ne toucher à aucune de ces formulations.**

Orphelines encore en ligne : `/solune`, `/au-nid` (suppression jamais confirmée ; exclues du sitemap et interdites dans `robots.txt`).

## ARCHITECTURE — ✅ CONSTRUITE ET EN LIGNE (04/08)

Principe qu'il a posé : **deux publics distincts** — ceux qui achètent un spectacle, et ceux qui viennent vivre quelque chose au Nid. Ils ne se croisent jamais et le site doit le refléter.
Sur le mot à employer : « spectacle » est trop pauvre (RITUALS est un *concert-rituel*), et ils sont « à la frontière de tous ces mondes ». Terme retenu en façade : **« Sur scène »**. Chaque page garde son terme précis (concert-rituel, spectacle immersif participatif, concert-cérémonie participatif). Tactique conseillée pour les programmateurs : sous le nom d'auteur, ajouter *« Se programme en : festival · salle · lieu patrimonial · événement d'entreprise »* et *« S'inscrit dans : musiques du monde · création pluridisciplinaire · spectacle participatif »* — ces lignes font le classement à leur place.

**Menu unifié, en place sur les 30 pages** (composant partagé `sources/nav_menu.py`, idempotent via `data-nav="resonances-4"`, `NAV_VERSION` à incrémenter pour régénérer ; sous-menus déroulants en desktop — un seul ouvert à la fois — et accordéons dans le panneau hamburger en mobile ; `aria-current` + parent marqué ; vérifié sur les 10 pages à 390/820/1440 px, 0 débordement) :

- **Accueil**
- **Sur scène** ▾ → `/rituals` (RITUALS — duo) · `/rituals-trio` (RITUALS — trio) · `/e-motion` (E-Motion) · `/david-lesage-en-concert` (David Lesage en concert)
- **Le Nid** ▾ → `/le-nid` (Le Nid — Paris 20ᵉ) · `/le-nid#agenda` (Agenda) · `/le-nid#instruments` (Présentation d'instruments) · `/concerts-david-lesage` (Concerts au Nid) · `/le-nid#yoga` (Atelier de yoga) · `/rythme-calebasse` (Rythme & calebasse) · `/le-soin-soa` (Le Soin Soa) · `/le-nid#psychotherapie` (Psychothérapie) · `/le-nid#cours-individuels` (Cours individuels)
- **L'association** ▾ → **`/association` (L'association)** · **`/guso-facile` (Guso Facile)**
- **Contact** · bouton **Adhérer**

**Pourquoi « Guso Facile » est sous « L'association » (décision du 14/08/2026)** — ce
n'est ni un spectacle (« Sur scène ») ni une activité du lieu (« Le Nid ») : c'est un
outil pour les artistes. Trois places étaient possibles ; le raisonnement complet est
écrit dans `sources/nav_menu.py`, juste au-dessus de la table `ASSO`. En bref :
*(a)* pas dans « Le Nid », qui décrit ce qui se vit **au** Nid, à Paris ; *(b)* pas en
entrée de premier niveau, parce que la barre en compte déjà six et que la contrainte est
**mesurée** — entre 861 et 1080 px les liens venaient toucher le nom de l'association ;
un sous-menu ne coûte que la largeur du chevron ; *(c)* donc sous « L'association », qui
devient déroulant **sur le modèle exact de « Le Nid »** (première entrée du panneau = la
section elle-même, comme « Le Nid — Paris 20ᵉ »).
⚠️ Nuance assumée : ce rangement de navigation **ne dit pas** que l'outil est porté par
l'association — la page, elle, porte la formulation prudente validée (voir plus haut).
Si David préfère une entrée de premier niveau, c'est **une ligne à changer** dans
`build_links()` + `MENU_ENTREES_ATTENDUES` dans `verif_site.py`, et un `NAV_VERSION` à
incrémenter.

### ⚠️ `/association` est une VRAIE PAGE depuis le 15/08/2026 — et les ancres qui vont avec

David avait remarqué que **« Accueil » et « L'association » menaient tous les deux à la
page d'accueil** (le second vers `/#association`). Derrière ce doublon de menu, un
problème de fond : **l'accueil faisait cinq métiers** (`#association`, `#statuts`,
`#adherer`, `#contact`, `#prestations`) en plus de présenter les spectacles. Il a
tranché pour la solution de fond.

**Ce qui a déménagé de `/` vers `/association`** : le 2ᵉ paragraphe de l'objet, et toute
la section « Cadre légal · Les statuts » (les deux articles, le renvoi au Journal
officiel avec le n° RNA, le lien vers le document des statuts, la fiche data.gouv.fr).
**Ce qui reste sur `/`** : la présentation courte (1ᵉʳ paragraphe de l'objet, pas un mot
changé) + un bouton « En savoir plus sur l'association », les quatre engagements, les
prestations, l'adhésion, le pied de page.

**Les ancres, une par une** :

| Ancre | Décision | Pourquoi |
|---|---|---|
| `/#association` | **reste sur l'accueil** | le bloc court y est toujours ; c'est la cible historique du menu jusqu'à `resonances-3` |
| `/#adherer` | **reste** | la section « Adhésion » n'a pas bougé. `/association#adherer` existe **en plus** |
| `/#contact` | **reste** | c'est le pied de page, présent sur les 30 pages |
| `/#prestations` | **reste** | les six cartes n'ont pas bougé |
| `/#statuts` | **part** sur `/association#statuts` | mesuré avant de trancher : **aucune page ne pointait vers `/#statuts`** dans son corps de texte. Seuls subsistaient 3 sélecteurs CSS `.nav .links a[href="/#statuts"]`, vestiges d'un menu remplacé depuis — retirés. Le seul renvoi réel était la redirection `/statuts` de `vercel.json`, qui vise maintenant `/association#statuts` |

⚠️ **Une redirection Vercel ne peut RIEN pour un lien interne** : `/#statuts` écrit dans
une page n'est jamais une requête vers `/statuts`, c'est une requête vers `/` suivie d'un
saut côté navigateur. Rediriger ne répare que les URL tapées à la main. C'est pourquoi le
choix s'est fait ancre par ancre, et pas « on redirigera ».

⚠️ **Les textes partagés entre `/` et `/association` vivent dans
`sources/textes_association.py`** — ce n'est PAS un générateur (il n'écrit aucune page,
il n'a donc pas de ligne dans `build.py`, dont le contrôle ne regarde que les
`generate_*.py`). Une correction de David n'a qu'un seul endroit où se faire.

⚠️ **`association_href` n'existe plus** dans `nav_menu.build_links()` / `inject()` :
l'entrée porte un href en dur. Pour revenir à l'ancre d'accueil, remettre `None` dans
`ASSO[0]`, restaurer les quatre lignes (historique git) et incrémenter `NAV_VERSION`.

### Google Search Console (15/08/2026)

`<meta name="google-site-verification" content="iPTmSfVj…">` est dans le `<head>` de
**l'accueil, et de nulle part ailleurs** : elle vérifie la propriété « préfixe d'URL »,
et Google ne la lit que sur la page demandée — une pose suffit. Un dixième contrôle
(`google`) dans `verif_site.py` refuse toute copie sur une autre page, et
`generate_association.py` refuse d'écrire si la balise s'y trouve. David pose en
parallèle un TXT dans la zone DNS OVH pour la propriété « domaine » ; les deux méthodes
coexistent, et un enregistrement `google-site-verification` **existe déjà** dans cette
zone.

Les ancres `#psychotherapie`, `#concerts-au-nid`, `#yoga`, `#calebasse-workshop`, `#cours-individuels`, `#instruments` **existent déjà** sur `/le-nid` (+ `#agenda`, `#concerts` pré-filtre concerts). Prérequis fait.
⚠️ Contrainte mesurée : à 9 entrées la barre touchait le nom de l'association entre 861 et 1080 px → resserrement CSS + `white-space:nowrap` déjà en place sur certaines pages. Un menu déroulant règle le problème de fond.

## ÉTAT PAR CHANTIER

### Performance (terminé)
Toutes les images locales dans `/img/` (WebP + repli JPEG, 3-4 largeurs). Plus aucune dépendance externe. rituals 4,6 Mo → **59 Ko** · trio → **76 Ko** · e-motion (17,7 Mo d'images distantes) → **37 Ko**. 1ᵉʳ affichage mobile : 176 / 231 / 86 Ko.
⚠️ **Piège carrousel** : `loading="lazy"` casse les slides (2 px) car sous 900 px le CSS met largeur ET hauteur en `auto`. Solution en place : `--ar` (ratio) par `.slide` + `.slide{width:min(calc(460px*var(--ar)),90vw)}` + 3 premières en `eager`. **Ne pas défaire.**
⚠️ L'attribut HTML `height` agit comme longueur CSS → corrigé par `picture>img{height:auto}`.
⚠️ `margin:0 auto` sur un enfant de grille annule `stretch` → une `<picture>` s'effondrait à 1,25 px. Corrigé par `width:100%`.
Générateurs : produisent des fichiers image. Ils ne tournent pas ici (dossiers photos sources absents) sauf `generate_rythme.py` (ses originaux sont versionnés dans `sources/rythme_img/`).

### Accessibilité / SEO (terminé)
Cibles tactiles 44 px · plancher typo 13 px (hors `<sup>`) · `:focus-visible` doré · `alt` recopiés des légendes · téléphones en `tel:` · favicon (`favicon.svg`/`.ico`/`apple-touch-icon.png`) · `og-image.jpg` 1200×630 · `og:url` · `twitter:card` · `theme-color` · **`robots.txt` + `sitemap.xml`** (10 URL depuis le 14/08/2026).

### Contenu (terminé)
- **Hero du Nid** : photo du salon en fond, voile radial + linéaire, ombres de texte.
- **« Showcase » supprimé partout** → **« Présentation, découverte & essai d'instruments d'exception »** (badge « Découverte & essai », titre d'agenda « Présentation d'instruments d'exception »). Registre premium exigé : instruments faits main, très petites séries, plusieurs milliers d'euros. Clé technique interne `showcase` conservée dans les `data-*`.
- **Mention de transparence** : gratuit, sans obligation d'achat, l'association **ne vend pas** les instruments, peut percevoir une **contribution d'affiliation** ; seuls objets vendus = **calebasses pyrogravées**.
- **Blocs photo pleine largeur** sur `/le-nid` : rendez-vous mensuels (2 photos), atelier de yoga (3 photos), workshop calebasse (1 photo plafonnée à 554 px, source 1151 px).
- **Le Soin Soa** : cadrage associatif (événement organisé par l'association ; Gaïa = intervenante invitée, accord donné ; Iris et David = co-fondateurs) · intitulés d'origine restaurés (**Massage Mémoire cellulaire / Régulation Neuro-émotionnelle / Alchimie Vocale**) · citation « une voie royale s'ouvre » · **nouveau déroulé** (les 3 intervenants démarrent simultanément, parcours individualisés, pause, temps entre participants) · **aucun prix**, renvoi vers **demande de devis** · jauge idéale **6 personnes engagées**, formats régulier OU ponctuel · encadré « ce n'est pas un acte médical » · aucune date.
- **Crédits photo MAGYE D'ART** (`magyedart.fr`) : 4 photos filigranées sur `/e-motion` + **les 2 photos du Grand Rex** sur rituals et trio (signature en bas à droite, découverte tardivement).
- **Adresse asso** : siège **2 impasse des Bleuets, 09600 Aigues-Vives** + correspondance **29 rue des Orteaux, 75020 Paris**. Liens **Statuts** (Google Doc) et **annuaire data.gouv.fr**. Boutons « Adhérer » → **page d'adhésion directe** HelloAsso.
- **Accueil** : 6 cartes (RITUALS · E-Motion · Le Nid · David Lesage · Le Soin Soa · Événements & création). Les cartes « Bains sonores » et « Ateliers & formations » ont été retirées (aucune proposition concrète). ⚠️ **Incident** : la restauration de « Bains sonores » avait été insérée *dans* la carte « Ateliers & formations », cassant le HTML — réparé.
- **`/concerts-david-lesage`** : « **Boire l'eau du concert** » — partenariat **AquaDyn Auroville** + **Rebirth Water Group**, fontaine **Mélusine** (brevet son et lumière attribué à ses concepteurs) installée **au Nid**, son du concert envoyé en direct dans l'eau. ⚠️ **Aucune vertu de l'eau affirmée** : le mot de David, « expérimente », fait office de mode d'emploi. La 2ᵉ photo a été prise lors d'un événement extérieur (salle voûtée) : sa légende ne doit pas suggérer le Nid.
- **`/david-lesage-en-concert`** : fiche technique publiée (2 configurations, **9 entrées** en référence, patch, plateau 4×5 m, retours Bose S1+Sub1, matériel demandé / apporté, contact technique) + bouton « Demander la fiche technique complète ». **Sziget** et **Grand Rex (2 700 personnes)** confirmés et ajoutés. Correction : « **après un court passage** au Conservatoire », et **autodidacte**. 9 photos extraites de sa présentation dont 4 où **il joue seul**.
- **`/rythme-calebasse`** : contenu Now Groove (gourde, 2012, infra-basses, œufs = charleston + caisse claire, calebasses signature d'Afrique de l'Ouest retravaillées par Kamou) · workshops au Nid (2 h, instrument fourni, 3 dates) · format « intervention jusqu'à 50 personnes » présenté séparément · **appel à candidature** groupe de pratique 1 an, 1 workshop/mois, ~4 places · **formulaire par email** (compose un `mailto` + panneau « copier le message », repli sans JS). Écarté : « c'est prouvé scientifiquement », hémisphères du cerveau, états de transe. Aucun tarif (la source n'en publie aucun).

### Google Agenda « Le Nid » (`30716d7f…@group.calendar.google.com`, PUBLIC)
Code portail retiré des 20 événements · 3 rappels (10080/1440/120 min, popup) sur les 42 · 5 événements renommés « Présentation d'instruments d'exception — Le Nid ».
⚠️ **Limite Google actée** : les rappels d'un calendrier public **ne se propagent pas aux abonnés**. Seuls les `.ics` téléchargés les embarquent (3 VALARM : 1 sem / 1 j / 2 h).
🔴 **ALERTE NON RÉSOLUE — action de David requise** : le code du portail est en clair **3 fois**, sur `https://sites.google.com/lesagedavid.fr/soin-incarnation-soa/accueil`, page publique sans authentification. Je ne peux pas éditer Google Sites. À remplacer par « le code du portail vous est communiqué avec votre confirmation d'inscription ».

### Liens & billetteries
- Adhésion : `helloasso.com/beta/associations/resonances-productions/adhesions/adhesion-resonances-productions`
- Concerts (3 dates : 26/09, 10/10, 28/11, toutes au Nid) : `helloasso.com/associations/resonances-productions/evenements/concert-intimiste-david-lesage-au-coeur-de-paris-1` — tarifs 24 € soutien / 19 € standard / 14 € inclusif (**non affichés sur le site**, par choix).
- Atelier yoga : `helloasso.com/associations/resonances-productions/evenements/atelier-mensuel-au-nid`
- Album **« L'Alliance du Phoenix »** (10 compositions, 2 opus, 100 % auto-produit ; téléchargement dès 20 € ou clé USB 40 €) : `helloasso.com/associations/resonances-productions/boutiques/acheter-album-l-alliance-du-phoenix-david-lesage`
- Spotify : `https://open.spotify.com/artist/7zEAQJbalBFj8XNHrcqdbK`
- YouTube : `https://www.youtube.com/@DavidLesageMusique` ⚠️ **divergence** : `youtube.com/c/DavidLesage` existe aussi (fiche technique + Linktree). Deux chaînes actives dispersent l'audience — à trancher.
- Vidéos : cymatique `mPUrsusmYyQ` · The Voice « Une Âme » `a831rQeGLRU` · autres The Voice publiques : `WkZcBjZA_mU`, `lewR2Fga2UM` · teaser E-Motion `wjJ44RDENQM`.
- Facebook : `facebook.com/resonancesproductions`
- ⚠️ Workshops calebasse : encore en `mailto`, billetterie HelloAsso à créer.
- Mécanisme **`URL_PAR_EVENT`** dans `generate_agenda_nid.py` : surcharge du lien de réservation par (date, heure). Prêt pour les exceptions à venir.

### Vidéos — règle posée par David
**Toutes les vidéos doivent se lire SUR le site**, jamais dans un nouvel onglet ni dans l'appli YouTube. Composant `.lb` / `openYT()` en surimpression (déjà présent sur rituals, trio, e-motion), en cours de généralisation + passage à `youtube-nocookie.com`, fermeture par Échap, `src` vidée à la fermeture. Un lien de secours discret reste **dans** le lecteur (iframe bloquée = personne coincée sinon). Les liens de **plateformes** (Spotify, chaîne YouTube, boutique) restent en nouvel onglet : ce n'est pas la même chose.

## EN ATTENTE DE DAVID
1. 🔴 **Retirer le code du portail de la page Google Sites du Soin Soa** (voir alerte ci-dessus).
2. **Trancher entre les deux chaînes YouTube.**
3. **Durée des séances du Soin Soa** : 50 min (sa page) ou 1 h (ancienne page) ? **Durée du week-end** : samedi 8 h 30 → dimanche 14 h (1 nuit) ou vendredi soir → dimanche (2 nuits) ? Le nombre de repas à apporter en dépend. **Yoga du matin et mouvements libres du dimanche** : encore d'actualité ? **« Le Cœur du Cercle »** : appellation à revoir si les 3 intervenants sont désormais chacun en individuel.
4. **Numéro de mobile publié en clair** sur `/david-lesage-en-concert` (contact technique) : garder ou n'afficher que l'email ?
5. **Déroulé de concert** : proposition d'un bloc « comment se construit l'heure trente » en 6 temps, sans titres ni minutage figés (le déroulé de Korhogo est marqué « non définitif »). À construire ?
6. **Droit à l'image** : la photo `atelier-cercle` de `/rythme-calebasse` montre ~15 participants reconnaissables (déjà publique sur son site Google). Une photo d'atelier a été écartée car signée « Stéphanie D… » — utilisable avec crédit.
7. **Carte « Événements & création »** de l'accueil : même défaut que celles retirées (aucune proposition concrète, aucun lien). À retirer ?
8. **Légendes en attente** : yoga (« Yoga postural, respiration et méditation — dans la grande pièce du Nid, en petit groupe. ») · calebasse (« On apprend le rythme en cercle, calebasse entre les mains — aucun prérequis. ») · proposition « voir en images » à côté des « tout voir ».
9. **Photos manquantes** : David seul sur grande scène (celles du dépôt sont en duo) · moment cymatique (l'écran) · scène du Sziget (celle du dépôt est un selfie) · setup au Nid · concert solo au Nid · workshop calebasse en meilleure résolution · cours individuels et psychothérapie.
10. **Tarifs des rendez-vous individuels** (50 € / 70 € d'après le site) à afficher dans l'email showcase ?
11. **Rendez-vous mensuel** : l'adhésion est-elle vraiment requise ? (son seul bouton est « Adhérer »).
12. Décisions anciennes : suppression `/solune` et `/au-nid` · booking `/e-motion` = `booking@solune.show` (autre marque, comme « SOLUNE présente » sur la bannière) · rôle de Julien sur `/rituals-trio` · séance photo trio · afficher les prix des instruments (3 700 € / 5 300 €) ?
13. ⚠️ **À voir avec le comptable** : l'association a désormais **trois activités commerciales** (album, calebasses pyrogravées, billetteries) → lucrativité, franchise des impôts commerciaux (~80 k€), tenue de comptabilité.

## FILE D'ATTENTE
1. ~~Refonte du menu~~ ✅ **FAIT** (04/08). Liens utiles perdus au passage, à replacer dans le corps des pages : `/e-motion#programmer` (bouton « Programmer ce spectacle »), et sur l'accueil `#prestations` et `#statuts`.
2. **Versions EN + ES** : accueil + RITUALS duo + RITUALS trio + E-Motion (+ probablement les 2 pages concerts). **Le Nid non prioritaire** (page très locale). Structure : `/en/…`, `/es/…` + sélecteur de langue + `hreflang`.
3. Reste de l'audit : bouton « Nous contacter » en fin de rituals/trio · libellés de réservation hétérogènes sur `/le-nid` · pages de 12 000+ px sans retour en haut · refonte de l'accueil (photo en hero, bandeau prochaines dates, CTA principal autre qu'« Adhérer ») · liens d'évitement (aucune page n'en a réellement).
4. **Now School Academy** — chantier structurel. Ma recommandation : la **structure** = l'association (« formations » est dans l'objet statutaire) ; la **marque** = David Lesage / Now School ; la **plateforme** = **ne pas construire un 4ᵉ système**, mais une branche de contenus dans **Handpan Studio**, qui a déjà comptes, droits d'accès, contenus réservés, Stripe et espace admin. Le bricolage actuel (Google Sites + vidéos sur Telegram + HelloAsso) reproduit tout ça à la main sans données exploitables. À cadrer par un cahier des charges.
5. **Tableau de bord associatif multi-utilisateurs** : données déjà communes (table `site_leads`). Court terme = comptes admin dans l'app. Cible = page protégée (Supabase Auth) + connexion HelloAsso pour les événements qui n'ont pas d'inscription en ligne.

## AUTRE DÉPÔT — Handpan Studio (`~/CLAUDE/NEOTONE STUDIO/NEOTONE 1er mai 2026/`)
Tableau de suivi des inscriptions + email de confirmation. Commits locaux `5e8eabb` → `be7b625` → `5ec34c8` → `ba99b5c`, **NON déployés**. Fichiers : `auth/showcase-panel.ts`, `supabase/functions/confirm-showcase/index.ts`, `auth/account-menu.ts`, `config.toml`. Données : table `site_leads` (Supabase `zqcuhnjjrgmybftppkcl`), aucune migration ; RLS active → lecture `service_role`, d'où l'Edge Function. Horaires dans `EVENT_HOURS`. Email validé par David (code portail, temple/déchaussage, non fumeur, copropriété d'artistes, enfants, boire sans alcool/grignoter, focus Neotone, RDV individuel payant, jauge 20, engagement/communauté, responsabilité en cas de casse). ⚠️ Jauge de 20 **non bloquée**. Déploiement : `npx supabase functions deploy confirm-showcase` + `npx vite build` + `npx vercel --prod --yes` + push + changelog + **email test à David avant tout envoi réel**.

### ⚠️ PIÈGE — les commentaires HTML dans les pages livrées (réglé le 14/08/2026)

Des notes de rédaction écrites en commentaires HTML (`<!-- LE GESTE (ajout du 13/08)… -->`,
« ⚠️ AUCUNE INFORMATION PRÉCISE N'EXISTE sur cette formule… ») partaient **dans les pages
publiques** : invisibles à l'écran, mais lisibles par n'importe qui via « afficher le code source »,
et indexables. **44 commentaires, 16 148 caractères** au total, dont **18 (10 182 car.) sur la seule
page `/david-lesage-en-concert`**. Dépôt public + site d'association : ça ne doit plus arriver.

- **Les notes n'ont pas été détruites, elles ont été déplacées** — en commentaires Python `#`, dans
  le générateur, **juste au-dessus du code qui émet le bloc**. Pour `generate_concert_scene.py` et
  `generate_concert_dl.py`, le gabarit est désormais écrit en **plusieurs littéraux adjacents**
  (concaténés par Python) précisément pour qu'on puisse glisser les notes *entre* eux.
- ~~`/e-motion` n'a aucun générateur~~ → **corrigé le 14/08/2026** : la page a désormais
  **`sources/generate_emotion.py`**, qui la reproduit à l'octet près et appelle lui-même
  `mobile_nav.inject()` puis `nav_menu.inject()`. Ses notes y sont parties. La copie périmée
  `sources/emotion_final.html` a été **supprimée**.
- ~~`generate_site.py` ne peut plus tourner~~ → **corrigé le 14/08/2026** : il tourne de nouveau
  sur un simple clone. La fabrication des images dérivées (qui, elle, a toujours besoin des photos
  d'origine hors dépôt) est passée derrière l'option **`--images`** ; sans elle, la page se
  régénère normalement, seconde photo du Grand Rex comprise.
- **`sources/notes_pages_sans_generateur.py` est désormais vide de notes** : les 10 pages publiées
  ont toutes un générateur. Le fichier reste en place — c'est là que devra aller la note d'une
  future page éditée à la main (`build.py` signale ces pages sous « PAGES SANS GÉNÉRATEUR »).

**LISTE BLANCHE — les 2 seuls commentaires HTML autorisés dans une page.** Ils sont **fonctionnels**,
les retirer casse le site :

| Marqueur | Pourquoi il est indispensable |
|---|---|
| `<!-- nav_menu.py (resonances-4) -->` | `JS_MARK` de `nav_menu.py` : **garde d'idempotence** testée par `inject()`. Sans lui le menu se réinjecte à chaque passe (l'incident des entrées de menu en double). Porte aussi `NAV_VERSION`, relue pour nettoyer un ancien menu. |
| `<!-- fin nav_menu.py -->` | `JS_END` : **borne de fin** utilisée par `_strip()` pour retirer le JS d'une ancienne version du menu. Sans elle le nettoyage ne sait plus où s'arrêter. |

> ✅ **Incrémenter `NAV_VERSION` ne demande RIEN dans `verif_commentaires.py`** (vérifié le
> 14/08/2026 au passage `resonances-2 → resonances-3`) : le motif de la liste blanche est écrit
> **sans le numéro** — `<!-- nav_menu\.py \([^)>]*\) -->`. Ne jamais y figer un numéro : le jour
> où la version bougerait sans que ce fichier suive, **toutes** les pages seraient refusées à
> l'écriture. `verif_site.py`, lui, lit désormais `nav_menu.NAV_VERSION` directement (il avait
> divergé une fois).

(`<!--INDUCTION_FIG-->` et `<!--JULIEN_PHOTO-->` de `sources/trio_source.html` sont des **balises de
substitution**, remplacées par `generate_trio.py` : elles n'atteignent jamais la page. Si l'une
apparaissait dans le HTML livré, ce serait un bug — d'où leur absence de la liste blanche.)

**Le garde-fou : `sources/verif_commentaires.py`.**

```bash
python3 sources/verif_commentaires.py     # les 10 pages d'un coup ; $? = 1 si problème
```

À lancer **avant tout déploiement**. Il est aussi appelé **avant chaque écriture de fichier** dans
`generate_site.py`, `generate_trio.py`, `generate_concert_dl.py`, `generate_concert_scene.py`,
`generate_rythme.py`, `generate_agenda_nid.py`, `generate_soin_soa.py`, `generate_assoc.py`,
`nav_menu.py` (`apply_to_file`) et `mobile_nav.py` : tout commentaire hors liste blanche — ou tout
marqueur autorisé dépassant **60 caractères** — **abandonne l'écriture**, la page sur disque reste
intacte. Même parti-pris que le garde-fou structurel de `generate_rythme.py`. Testé en le cassant
exprès : écriture refusée, page inchangée.

### ⚠️ PIÈGES DE LA CHAÎNE DE FABRICATION (mesurés le 14/08/2026)

Tout ce qui suit a été **vérifié en exécutant**, pas déduit. C'est ce que `sources/build.py`
encode dans son tableau ; cette section est là pour la prochaine session.

| Page | Générateur | Écrit où | Menu à reposer ? | État mesuré |
|---|---|---|---|---|
| `/` | `generate_assoc.py` | `assoc_index.html` puis à recopier | non | ✅ **débloqué le 14/08** |
| `/rituals` | `generate_site.py` | directement | non | ✅ réparé le 14/08 |
| `/rituals-trio` | `generate_trio.py` | directement | non | ✅ **débloqué le 14/08** |
| `/e-motion` | `generate_emotion.py` | directement | non | ✅ créé le 14/08 |
| `/david-lesage-en-concert` | `generate_concert_scene.py` | directement | **OUI** | ✅ |
| `/concerts-david-lesage` | `generate_concert_dl.py` | directement | **OUI** | ✅ |
| `/le-nid` | `generate_agenda_nid.py` | directement (source : `sources/lenid_source.html`) | non | ✅ **débloqué le 14/08** |
| `/le-soin-soa` | `generate_soin_soa.py` | `sources/soin_soa_final.html` puis à recopier | non | ✅ |
| `/rythme-calebasse` | `generate_rythme.py` | directement | non | ✅ |
| `/guso-facile` | `generate_guso.py` | directement | non | ✅ **inscrit le 14/08** |

**Les 10 générateurs tournent, et reproduisent leur page à l'octet près.** Plus aucune
ligne `bloque=` dans `sources/build.py`. Deux `build.py` de suite ne changent plus un
seul octet.

**Ce qui les bloquait, et comment ça a été levé** (gardé comme mémoire des pièges) :

- **`generate_assoc.py` (l'accueil)** — les accolades CSS d'un bloc de style inséré dans
  une f-string n'étaient pas doublées (`NameError: name 'font' is not defined`).
- **`generate_agenda_nid.py` (`/le-nid`)** — il *retouchait* une page qu'il allait chercher
  dans `lenid_deploy/index.html`, dossier disparu. Il part maintenant d'une vraie source
  versionnée, **`sources/lenid_source.html`**. ⚠️ Il contient toujours des `re.sub` de
  nettoyage parce qu'il n'est pas idempotent de nature : ne pas les retirer.
- **`generate_trio.py` (`/rituals-trio`)** — cherchait ses photos dans `web_img/`, hors dépôt.
  Même remède que `generate_site.py` : la fabrication des images est passée derrière l'option
  **`--images`**, la page se régénère depuis les dérivées déjà présentes dans `img/`.

**Autres pièges vérifiés :**

- ⚠️ **`generate_concert_scene.py` et `generate_concert_dl.py` ne posent pas le menu.** Il faut
  lancer `python3 sources/nav_menu.py <page>/index.html` **derrière** eux — sinon la page part
  sans menu. Écart mesuré sans cette passe : 217 et 218 lignes. `build.py` le fait tout seul.
- ⚠️ **Ne JAMAIS faire `import generate_concert_scene`** (ni `generate_concert_dl`) : ces scripts
  travaillent au moment de l'import et **réécrivent la page sans le menu**. `build.py` les lance
  en sous-processus, jamais par import.
- ✅ **`le-soin-soa/index.html` avait été retouché à la main après génération** — rapatrié
  le 14/08/2026 dans `sources/generate_soin_soa.py` (fonction `_rapatrier_retouches`). Trois
  écarts, **aucun effet visuel**, tous reproduits pour que la page redevienne identique à
  l'octet : (1) les 3 lignes de CSS `.who-site` descendues en fin de feuille de style ;
  (2)+(3) deux **lignes vides fossiles** devant les marqueurs du menu, restes de la montée
  `resonances-1 → resonances-2` faite sur le fichier (`nav_menu._strip()` laisse le saut de
  ligne qui précédait). Même technique que `generate_trio.py`. La page n'est plus signalée
  « MISE À JOUR ». La fonction **refuse d'écrire** si une ancre a bougé (testé).
- ⚠️ **Les lignes vides devant `/* == nav_menu.py … */` et `<!-- nav_menu.py … -->` sont des
  fossiles à préserver** : elles ne sont pas sur toutes les pages (mesuré : présentes sur
  `/`, rituals, trio, e-motion, le-nid, le-soin-soa ; absentes ailleurs). Chaque générateur
  reproduit celles de SA page. Ne pas « harmoniser ».
- ⚠️ **git échappe les noms de fichiers contenant un caractère invisible.** `sources/Icon` suivi
  d'un retour chariot sort `"sources/Icon\r"` dans `git diff --name-only`. Toute recherche sur le
  vrai nom échoue : il faut `-z`. C'est ce qui avait laissé passer un fichier `Icon` au premier
  essai du crochet `pre-commit`.
- ⚠️ **Fichiers `Icon` de Google Drive : 26 sur le disque, 1 seul était suivi par git** (plus 3
  `.DS_Store`). Tous sortis du suivi le 14/08, aucun effacé. Le motif `Icon?` du `.gitignore` vise
  le nom exact + un caractère : il ne touche ni `favicon.ico`, ni `apple-touch-icon.png`, ni un
  futur `icons.ts` — le piège documenté.
- ⚠️ **Sur `/le-nid`, les attributs `width`/`height` des images portent les dimensions de la photo
  d'ORIGINE** (4032 px pour une photo d'iPhone), pas la largeur d'affichage : c'est le couple
  `srcset`+`sizes` qui décide. `verif_site.py` en tient compte — il ne contrôle `width` que sur les
  images sans `sizes`, et vérifie surtout que **chaque largeur annoncée dans un `srcset` correspond
  au vrai fichier** (c'est ça, « une image affichée au-delà de sa définition »).
- **Trois portraits de `/le-soin-soa`** (260 px affichés à 150 px = 1,73× au lieu de 2×) sont dans
  une liste d'exceptions explicite de `verif_site.py`, avec leur raison. Ils seraient nets sur écran
  Retina avec une variante 300 px. Toute **nouvelle** image sous le seuil fera échouer le contrôle.
- **`/solune` et `/au-nid`** : toujours dans le dépôt, absents du `sitemap.xml`, interdits dans
  `robots.txt`. Cohérence vérifiée automatiquement. Leur suppression n'a jamais été tranchée par
  David : **on n'y touche pas**, `build.py` les rappelle à chaque passage.

**Règles clés** : aucun texte publié sans validation de David · jamais toucher aux DNS email OVH · pas de `loading="lazy"` sur les slides sans ratio réservé · code portail nulle part en public · vérifier le rendu réel aux 3 largeurs avant de présenter · navigateur = extension Claude-in-Chrome, **jamais** les screenshots computer-use · artefacts de test connus : dans un iframe en arrière-plan les transitions CSS sont gelées, `naturalWidth` est peu fiable et les captures d'une page sombre peuvent être partielles → neutraliser `transition`, valider les images par `decode()` + canvas ou `curl`.

## Journal
- **2026-08-15 (soir)** — **`/association` créée : le doublon de menu réglé à la racine.**
  *(1)* `sources/generate_association.py` → `association/index.html` (objet, valeurs,
  statuts, mentions légales RNA/SIRET/APE, siège + correspondance, adhésion, contact).
  Zéro JS de page, zéro image, zéro iframe, zéro tiers. Il appelle lui-même
  `mobile_nav.inject()` puis `nav_menu.inject('association')`, et **refuse d'écrire** sur
  une ancre manquante/dupliquée, un `target=_blank` sans `noopener`, un hôte hors liste,
  un texte sous 13 px, un emoji, ou la balise Google.
  *(2)* Menu : **`NAV_VERSION` → `resonances-4`**, « L'association » → `/association`,
  clé `association` dans `PAGE_KEYS` (via `ASSO`) et `_PATH_KEYS`. **18 entrées** de menu,
  inchangé. Vérifié AVANT la montée : plus aucun générateur ne code un numéro en dur.
  *(3)* Accueil déchargé (voir la section dédiée plus haut) ; 6 règles CSS `.statuts …`
  + 2 règles `.jo a` retirées avec la section ; 3 sélecteurs `[href="/#statuts"]` morts
  retirés de `generate_concert_dl/scene` et `generate_soin_soa`.
  *(4)* `build.py`, `sitemap.xml` (0.6 mensuel), `verif_site.py` + `verif_commentaires.py`
  **29 → 30 pages**, `vercel.json` (`/statuts` → `/association#statuts`, plus
  `/l-association` et `/mentions-legales`).
  **Mesuré** : `build.py` → 30 pages, deux exécutions sans un octet de différence, aucune
  page « MISE À JOUR » à la 2ᵉ passe ; `verif_site.py` **30/30** code 0 ;
  `verif_commentaires.py` 30/30 ; **25 des 29 pages existantes sont identiques** une fois
  le bloc de menu neutralisé (les 3 autres = la ligne CSS morte, + l'accueil qui change
  volontairement) ; **les 138 fragments de texte de l'ancien accueil se retrouvent tous**
  sur `/` ou `/association`, le seul texte nouveau étant le libellé du bouton ;
  0 débordement à 390/820/1440 px sur les 30 pages, 1 seul `<h1>`, hamburger vérifié à
  l'ouverture ET à la fermeture, `aria-current` juste, 0 lien mort, 0 ancre morte,
  balise Google **1 seule occurrence sur tout le site**.
  ⚠️ Reste ouvert : la page ne nomme **ni directeur de la publication ni hébergeur** —
  aucun des deux n'a été validé par David. On n'invente pas une mention légale.
- **2026-08-03** — Bascule Cowork → Claude Code. Clone, sources copiées, fix hamburger (cause : `backdrop-filter` du `.nav`), enrichissement Google Agenda, audit des liens /le-nid, tableau admin showcase (autre dépôt).
- **2026-08-04 (nuit)** — `robots.txt` + `sitemap.xml` · vidéos en lecteur de page (`youtube-nocookie`, Échap, src vidée, lien de secours dynamique) · fontaine Mélusine installée au Nid · The Voice : **la vraie vidéo** (audition à l'aveugle « Kothbiro » d'Ayub Ogada, chaîne officielle TF1) + 2 erreurs factuelles corrigées (ce n'était ni « Une Âme » ni 2021) · bloc « Écouter · Soutenir » (Spotify, chaîne, album « L'Alliance du Phoenix ») · **menu unifié sur les 9 pages**. ⚠️ `@DavidLesageMusique` est un **lien mort** : la seule chaîne est `@DavidLesageArtiste` — et `lesagedavid.fr` pointe vers la morte.
- **2026-08-04** — Calendrier /le-nid (filtres, boutons, abonnement) · dédoublonnages + causes corrigées dans les générateurs · adresse asso + statuts + data.gouv · Google Agenda nettoyé + 3 rappels · incident code portail dans ce handoff public (historique réécrit) · audit UX complet · quick wins accessibilité/SEO · **chantier images terminé** · hero du Nid · `/le-soin-soa` créée puis adaptée · « Showcase » renommé partout · crédits MAGYE D'ART · `/concerts-david-lesage` · `/david-lesage-en-concert` + fiche technique · `/rythme-calebasse` + appel à candidature · « Boire l'eau du concert » · robots.txt + sitemap.xml. **Tout déployé et vérifié en ligne.**
- **2026-08-14 (soir)** — **`/guso-facile` raccordée au site, et la chaîne de fabrication est complète.**
  *(1)* Les trois `bloque=` restants de `sources/build.py` retirés (accueil, `/rituals-trio`, `/le-nid`) :
  leurs générateurs étaient réparés depuis, `build.py` les sautait encore en silence avec un message
  périmé. **Les 10 générateurs tournent et reproduisent leur page à l'octet près.**
  *(2)* Menu : `NAV_VERSION` → **`resonances-3`**, « L'association » devient **déroulant** et accueille
  **« Guso Facile »** (raisonnement du placement dans `nav_menu.py` et plus haut dans ce fichier) ;
  `guso-facile` ajoutée à `PAGE_KEYS` et `_PATH_KEYS` ; `generate_guso.py` passe désormais la clé
  `'guso-facile'` (donc `aria-current`). **18 entrées** de menu attendues (`verif_site.py`).
  *(3)* `sitemap.xml` (10 URL), `vercel.json` (redirections **`/Guso-Facile` → `/guso-facile`**, l'URL
  ayant été communiquée avec des majuscules et les chemins Vercel étant sensibles à la casse),
  `verif_site.py` et `verif_commentaires.py` passés à 10 pages. `robots.txt` : rien à changer (`Allow: /`).
  *(4)* **Deux failles de robustesse comblées** : `generate_site.py` portait la même que `generate_trio.py`
  — une dérivée d'image manquante produisait un `srcset` amputé **en sortant en code 0** ; il exige
  maintenant un jeu de largeurs contigu **et** le jumeau WebP de chaque JPEG, et **refuse d'écrire** sinon
  (testé dans les deux sens, page inchangée, code 1). Exception documentée : `grand-rex-bras-leves`
  a 4 largeurs (jusqu'à 2000 px), préparées à la main → table `LARGEURS_PARTICULIERES`.
  Et la retouche manuelle de `le-soin-soa/index.html` est rapatriée dans son générateur.
  *(5)* Cinq générateurs codaient `data-nav="resonances-2"` **en dur** dans leurs garde-fous : ils lisent
  maintenant `nav_menu.NAV_VERSION`. Idem pour `verif_site.py`. Une montée de version ne casse plus rien.
  *(6)* **Nouveau faux positif du contrôle « code d'accès »** : sur `/guso-facile`, « un badge
  « droits sécurisés » dès 507 heures » (mot `badge` + nombre). Traité par une entrée de liste blanche
  **documentée** dans `CODES_HORS_SOUPCON`, jamais par un `--no-verify`.
  **Mesuré** : `build.py` → 10 pages, deux exécutions de suite sans un octet de différence ;
  `verif_site.py` → **10/10 conformes** ; les 9 pages existantes **ne diffèrent de leur version
  précédente que par leur bloc de menu** (comparaison menu neutralisé : identiques) ; **0 débordement
  horizontal à 390 / 820 / 1440 px sur les 10 pages** (mesuré en iframe de largeur imposée —
  ⚠️ `resize_window` de l'extension répond « succès » sans effet, le volet reste à sa largeur) ;
  hamburger vérifié à l'ouverture **et** à la fermeture, un seul menu et un seul `<h1>` par page,
  0 lien mort, 0 ancre morte.
