# REPRENDRE — Site Résonances Productions

> Handoff du projet. Complément du document de reprise complet :
> `Drive partagés/1 - RESONANCES PRODUCTIONS/SITE_WEB_DEV/HANDOFF_CLAUDE_CODE.md`.
> ⚠️ Dépôt GitHub **PUBLIC** : jamais de code d'accès ni de secret ici.
> ⚠️ ~40 Mo d'images → `git config http.postBuffer 524288000` (fait) sinon le push échoue en HTTP 400.
> ⚠️ `git` de `/usr/bin` est bloqué par la licence Xcode → `export DEVELOPER_DIR=/Library/Developer/CommandLineTools`. Correctif définitif : `sudo xcodebuild -license`.

## LES 9 PAGES EN LIGNE (2026-08-04)

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

Orphelines encore en ligne : `/solune`, `/au-nid` (suppression jamais confirmée ; exclues du sitemap et interdites dans `robots.txt`).

## ARCHITECTURE — ✅ CONSTRUITE ET EN LIGNE (04/08)

Principe qu'il a posé : **deux publics distincts** — ceux qui achètent un spectacle, et ceux qui viennent vivre quelque chose au Nid. Ils ne se croisent jamais et le site doit le refléter.
Sur le mot à employer : « spectacle » est trop pauvre (RITUALS est un *concert-rituel*), et ils sont « à la frontière de tous ces mondes ». Terme retenu en façade : **« Sur scène »**. Chaque page garde son terme précis (concert-rituel, spectacle immersif participatif, concert-cérémonie participatif). Tactique conseillée pour les programmateurs : sous le nom d'auteur, ajouter *« Se programme en : festival · salle · lieu patrimonial · événement d'entreprise »* et *« S'inscrit dans : musiques du monde · création pluridisciplinaire · spectacle participatif »* — ces lignes font le classement à leur place.

**Menu unifié, en place sur les 9 pages** (composant partagé `sources/nav_menu.py`, idempotent via `data-nav="resonances-1"`, `NAV_VERSION` à incrémenter pour régénérer ; sous-menus déroulants en desktop — un seul ouvert à la fois — et accordéons dans le panneau hamburger en mobile ; `aria-current` + parent marqué ; vérifié sur les 9 pages à 390/820/1080/1440 px, 0 débordement, écart mini brand↔liens 158 px) :

- **Accueil**
- **Sur scène** ▾ → `/rituals` (RITUALS — duo) · `/rituals-trio` (RITUALS — trio) · `/e-motion` (E-Motion) · `/david-lesage-en-concert` (David Lesage en concert)
- **Le Nid** ▾ → `/le-nid#agenda` (Agenda) · `/le-nid#instruments` (Présentation d'instruments) · `/concerts-david-lesage` (Concerts au Nid) · `/le-nid#yoga` (Atelier de yoga) · `/rythme-calebasse` (Rythme & calebasse) · `/le-soin-soa` (Le Soin Soa) · `/le-nid#psychotherapie` (Psychothérapie) · `/le-nid#cours-individuels` (Cours individuels)
- **L'association** · **Contact** · bouton **Adhérer**

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
Cibles tactiles 44 px · plancher typo 13 px (hors `<sup>`) · `:focus-visible` doré · `alt` recopiés des légendes · téléphones en `tel:` · favicon (`favicon.svg`/`.ico`/`apple-touch-icon.png`) · `og-image.jpg` 1200×630 · `og:url` · `twitter:card` · `theme-color` · **`robots.txt` + `sitemap.xml`** (9 URL, toutes vérifiées 200).

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

**Règles clés** : aucun texte publié sans validation de David · jamais toucher aux DNS email OVH · pas de `loading="lazy"` sur les slides sans ratio réservé · code portail nulle part en public · vérifier le rendu réel aux 3 largeurs avant de présenter · navigateur = extension Claude-in-Chrome, **jamais** les screenshots computer-use · artefacts de test connus : dans un iframe en arrière-plan les transitions CSS sont gelées, `naturalWidth` est peu fiable et les captures d'une page sombre peuvent être partielles → neutraliser `transition`, valider les images par `decode()` + canvas ou `curl`.

## Journal
- **2026-08-03** — Bascule Cowork → Claude Code. Clone, sources copiées, fix hamburger (cause : `backdrop-filter` du `.nav`), enrichissement Google Agenda, audit des liens /le-nid, tableau admin showcase (autre dépôt).
- **2026-08-04 (nuit)** — `robots.txt` + `sitemap.xml` · vidéos en lecteur de page (`youtube-nocookie`, Échap, src vidée, lien de secours dynamique) · fontaine Mélusine installée au Nid · The Voice : **la vraie vidéo** (audition à l'aveugle « Kothbiro » d'Ayub Ogada, chaîne officielle TF1) + 2 erreurs factuelles corrigées (ce n'était ni « Une Âme » ni 2021) · bloc « Écouter · Soutenir » (Spotify, chaîne, album « L'Alliance du Phoenix ») · **menu unifié sur les 9 pages**. ⚠️ `@DavidLesageMusique` est un **lien mort** : la seule chaîne est `@DavidLesageArtiste` — et `lesagedavid.fr` pointe vers la morte.
- **2026-08-04** — Calendrier /le-nid (filtres, boutons, abonnement) · dédoublonnages + causes corrigées dans les générateurs · adresse asso + statuts + data.gouv · Google Agenda nettoyé + 3 rappels · incident code portail dans ce handoff public (historique réécrit) · audit UX complet · quick wins accessibilité/SEO · **chantier images terminé** · hero du Nid · `/le-soin-soa` créée puis adaptée · « Showcase » renommé partout · crédits MAGYE D'ART · `/concerts-david-lesage` · `/david-lesage-en-concert` + fiche technique · `/rythme-calebasse` + appel à candidature · « Boire l'eau du concert » · robots.txt + sitemap.xml. **Tout déployé et vérifié en ligne.**
