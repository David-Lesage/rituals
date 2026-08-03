# REPRENDRE — Site Résonances Productions

> Handoff du projet. Complément du document de reprise complet :
> `Drive partagés/1 - RESONANCES PRODUCTIONS/SITE_WEB_DEV/HANDOFF_CLAUDE_CODE.md`.
> ⚠️ Ce dépôt GitHub est PUBLIC : jamais de code d'accès ni de secret ici.
> ⚠️ ~28 Mo d'images → `git config http.postBuffer 524288000` (déjà fait ici) sinon le push échoue en HTTP 400.

## ÉTAT ACTUEL (2026-08-04) — TOUT CE QUI SUIT EST DÉPLOYÉ ET VÉRIFIÉ EN LIGNE

### Pages
`/` (accueil) · `/le-nid` · `/le-soin-soa` (NOUVELLE) · `/rituals` · `/rituals-trio` · `/e-motion`. Orphelines encore en ligne : `/solune`, `/au-nid` (suppression jamais confirmée).

### Performance — chantier images terminé
- **Toutes les images sont locales** dans `/img/` (324 fichiers, 3 largeurs × WebP + repli JPEG). Plus AUCUNE dépendance externe (28 images rapatriées : cloudfront, squarespace-cdn, Drive). Plus aucun base64.
- Poids HTML : rituals 4,6 Mo → **59 Ko** · trio 4,4 Mo (+8,4 Mo externes) → **76 Ko** · e-motion (+17,7 Mo externes) → **37 Ko**. 1ᵉʳ affichage mobile : 176 / 231 / 86 Ko.
- ⚠️ **Piège carrousel résolu** : `loading="lazy"` casse les slides (2 px) car sous 900 px le CSS met largeur ET hauteur en `auto` — les attributs `width`/`height` ne suffisent PAS. Solution en place : `--ar` (ratio) par `.slide` + `.slide{width:min(calc(460px*var(--ar)),90vw)}` + 3 premières en `eager`. **Ne pas défaire.**
- ⚠️ Autre piège : l'attribut HTML `height` agit comme longueur CSS → déformait les figures. Correctif `picture>img{height:auto}`.
- Les générateurs produisent désormais des fichiers image. Ils ne peuvent pas tourner ici (dossiers photos sources `promo_raw/`, `web_img/`, `trio_img/` absents du dépôt) et s'arrêtent proprement. `generate_agenda_nid.py` écrit dans `lenid_deploy/` (chemin inexistant) → patcher la page directement.

### Contenu / structure
- **Hero du Nid** : photo du salon en fond (`/img/le-nid/hero-nid-*`), voile `.hero::after` (radial 760×500 à 50%/46% + linéaire .60/.40/.82) + ombres de texte. Récupérée d'un lien Google Photos partagé (méthode : lire `og:image` de la page de partage, puis suffixe `=d` pour la pleine résolution).
- **`/le-soin-soa`** : contenu adapté de `irischasles.com/agenda-yoga/immersion-therapeutique-soa`, **adapté au cadre statutaire** — événement organisé par l'association, « intervenants » (Gaïa Pégourié = invitée, accord donné ; Iris et David = co-fondateurs), participation 425 € perçue par l'association et non par les intervenants, encadré « pas un acte médical », inscriptions → `contact@resonancesproductions.org`. Aucune date (édition avril 2026 passée, pas de nouvelle date). Générateur : `sources/generate_soin_soa.py` (listes `SOA_PHOTOS`/`SOA_GALERIE` → ajouter une photo = 1 ligne). Accueil ramené de 11 700 à ~5 060 px ; la carte de prestations y mène.
- **« Showcase » supprimé** → **« Présentation, découverte & essai d'instruments d'exception »** (badge court « Découverte & essai », titre d'agenda « Présentation d'instruments d'exception »). Registre premium exigé par David : instruments faits main, très petites séries, plusieurs milliers d'euros. Clé technique interne `showcase` conservée dans les `data-*`.
- **Mention de transparence** en place : gratuit, sans obligation d'achat, l'association **ne vend pas** les instruments et peut percevoir une **contribution d'affiliation** ; seuls objets vendus = **calebasses pyrogravées** faites à l'atelier. ⚠️ À valider avec le comptable : cette vente = activité commerciale (lucrativité, franchise des impôts commerciaux ~80 k€).
- **Crédits photo MAGYE D'ART** (`magyedart.fr`) sous les **4 seules photos filigranées**, sur /e-motion. Vérifié : aucune photo du trio n'est filigranée.
- **Adresse asso** : siège **2 impasse des Bleuets, 09600 Aigues-Vives** + correspondance **29 rue des Orteaux, 75020 Paris**. Liens **Statuts** (Google Doc) et **annuaire data.gouv.fr**. Phrase « statuts sur demande » supprimée.
- Agenda /le-nid : filtres type + mois, ancre `#concerts`, « + Google Agenda » par date, « + .ics » (3 rappels 1 sem/1 j/2 h), encart d'abonnement en tête (Google `calendar/r?cid=` + webcal). Garde-fous anti-doublon dans le générateur (4 cartes et 4 entrées « Agenda » avaient été dupliquées par des exécutions répétées) — **ne pas les retirer**.
- Accessibilité/SEO : cibles tactiles 44 px, plancher typo 13 px, `:focus-visible`, `alt` recopiés des légendes, `tel:`, favicon (`favicon.svg`/`.ico`/`apple-touch-icon.png`), `og-image.jpg` 1200×630, `og:url`, `twitter:card`, `theme-color`.

### Google Agenda « Le Nid » (`30716d7f…@group.calendar.google.com`, PUBLIC)
- Code portail **retiré des 20 événements** → « Le code du portail vous est communiqué avec votre confirmation d'inscription. » Flux public vérifié : **0 occurrence**. Le code ne part QUE dans l'email de confirmation.
- **3 rappels** (10080/1440/120 min, popup) sur les 42 événements. ⚠️ Limite Google actée : les rappels d'un calendrier public **ne se propagent pas aux abonnés**. Seuls les `.ics` téléchargés les embarquent.
- 5 événements renommés « Présentation d'instruments d'exception — Le Nid », descriptions enrichies (déroulé 5 points + enfants) conservées.
- Restent 2 anciens événements **passés** nommés « Showcase » (27 juin, 19 juil. 2026) — non renommés, purement cosmétique.

## EN ATTENTE DE DAVID
1. **URL de la page Facebook** (le lien du pied de page pointe vers l'accueil de Facebook) — demandée 2 fois, toujours pas fournie.
2. **Feu vert pour déployer le tableau de suivi des inscriptions** (autre dépôt, voir plus bas) + email test.
3. **Tableau de bord associatif multi-utilisateurs** : à étudier. Données déjà communes (table `site_leads`). Court terme = comptes admin dans l'app. Cible = page protégée sur le site Résonances (Supabase Auth) + connexion HelloAsso pour les autres événements (yoga/workshops n'ont AUCUNE inscription en ligne aujourd'hui). Chantier à spécifier.
4. Décisions ouvertes : suppression `/solune` et `/au-nid` · lien de réservation des présentations d'instruments (`handpan-studio.app/showroom#agenda` vs `lesagedavid.fr/showroom`) · booking /e-motion = `booking@solune.show` (autre marque) · rôle de Julien sur /rituals-trio · séance photo trio · afficher ou non les prix exacts des instruments (3 700 € / 5 300 €) · adhésion obligatoire pour le Soin Soa ? · date du Soin Soa · rendez-vous mensuel : l'adhésion est-elle vraiment requise ? (son seul bouton est « Adhérer »).
5. **Page groupe calebasse sur lesagedavid.fr** (projet `site-vitrine`) : priorité appel au groupe vs vente formation ?

## FILE D'ATTENTE — prochains chantiers décidés
1. **Menu à refondre** (touche les 6 pages) : onglet parent **« Spectacles & concerts rituels »** (validé) avec sous-menu **RITUALS — duo · RITUALS — trio · E-Motion · Concerts de David Lesage**, **RITUALS en premier** (exigence). Plus un onglet dédié **« Le Soin Soa »** (déjà présent dans le menu de sa seule page). Harmoniser sur toutes les pages + `aria-current`. NB : à 9 entrées la barre touchait le nom de l'association entre 861 et 1080 px → resserrement CSS + « Statuts » masqué sous 1000 px (déjà traité sur /le-soin-soa).
2. **Versions EN + ES** : **accueil + RITUALS duo + RITUALS trio + E-Motion**. **Le Nid non prioritaire** (décision David : page très locale, agenda/billetteries franco-français). Structure : `/en/…`, `/es/…` + sélecteur de langue + `hreflang`.
3. Reste de l'audit UX : /rituals-trio quasi introuvable, 4 cartes « Prestations » non cliquables, pages de 12 000+ px sans retour en haut, bouton « Nous contacter » en fin de /rituals et /rituals-trio, libellés de réservation hétérogènes sur /le-nid, `robots.txt`/`sitemap.xml` absents, refonte de l'accueil (photo en hero, bandeau prochaines dates, CTA principal autre qu'« Adhérer »).

## AUTRE DÉPÔT — Handpan Studio (`~/CLAUDE/NEOTONE STUDIO/NEOTONE 1er mai 2026/`)
Tableau de suivi des inscriptions + email de confirmation. Commits locaux `5e8eabb` → `be7b625` → `5ec34c8` → `ba99b5c`, **NON déployés**. Fichiers : `auth/showcase-panel.ts`, `supabase/functions/confirm-showcase/index.ts`, `auth/account-menu.ts`, `config.toml`. Données : table `site_leads` (Supabase `zqcuhnjjrgmybftppkcl`), **aucune migration nécessaire** ; RLS active → lecture `service_role` uniquement, d'où le passage par Edge Function. Horaires par date dans `EVENT_HOURS` (à compléter pour toute nouvelle date) + surcharge manuelle dans le panneau. Email validé par David : code portail, temple/déchaussage, non fumeur, copropriété d'artistes, enfants (activités + espace dédié), boire sans alcool/grignoter, focus Neotone, orientation RDV individuel payant, jauge 20 + engagement/communauté, responsabilité en cas de casse. ⚠️ La jauge de 20 n'est **pas** bloquée automatiquement. Déploiement : `npx supabase functions deploy confirm-showcase` + `npx vite build` + `npx vercel --prod --yes` + `git push` + changelog + **email test à David avant tout envoi réel**.

**Règles clés** : aucun texte publié sans validation de David · jamais toucher aux DNS email OVH · pas de `loading="lazy"` sur les slides sans ratio réservé · code portail nulle part en public · vérifier le rendu réel aux 3 largeurs avant de présenter · navigateur = extension Claude-in-Chrome, jamais les screenshots computer-use · artefact de test connu : dans un iframe en arrière-plan les transitions CSS sont gelées et `naturalWidth` est peu fiable → neutraliser `transition` avant de juger un panneau ouvert.

## Journal
- **2026-08-03** — Bascule Cowork → Claude Code. Clone, sources copiées, fix hamburger (cause : `backdrop-filter` du `.nav` = conteneur des `fixed` + stacking context), enrichissement Google Agenda, audit des liens /le-nid, tableau admin construit (autre dépôt).
- **2026-08-04** — Calendrier /le-nid (filtres, boutons, abonnement) · dédoublonnage + causes corrigées dans le générateur · adresse asso + statuts + data.gouv · Google Agenda nettoyé du code portail + 3 rappels · incident code portail dans ce handoff public (historique réécrit, force-push) · audit UX complet des 5 pages aux 3 largeurs · quick wins accessibilité/SEO · **chantier images terminé** · hero du Nid · page `/le-soin-soa` créée puis adaptée au cadre associatif · « Showcase » renommé partout (site + agenda) · crédits MAGYE D'ART. **Tout déployé.**
