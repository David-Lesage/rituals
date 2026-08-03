# REPRENDRE — Site Résonances Productions

> Handoff du projet. Complément local du document de reprise complet :
> `Drive partagés/1 - RESONANCES PRODUCTIONS/SITE_WEB_DEV/HANDOFF_CLAUDE_CODE.md`
> (architecture, chaîne de déploiement, pièges, règles). Le lire aussi.
> ⚠️ Ce dépôt GitHub est PUBLIC : ne jamais écrire de code d'accès ni de secret ici.

## ÉTAT ACTUEL (2026-08-04)

### Déployé et vérifié en ligne
- Dépôt cloné (`David-Lesage/rituals` → ce dossier). Push = déploiement Vercel auto.
- ✅ §7.1 hamburger mobile (cause : `backdrop-filter` du `.nav` = conteneur des `fixed` + stacking context ; fix `body.nav-open .nav{backdrop-filter:none;z-index:1001}`). **David n'a pas encore retesté sur son téléphone.**
- ✅ Agenda /le-nid : filtres par TYPE et par MOIS, ancre `#concerts` pré-filtrée (= vue « toutes les dates de concerts »), bouton **« + Google Agenda »** par date (20 liens) + **« + .ics »** conservé avec **3 rappels (1 sem / 1 j / 2 h)**.
- ✅ Encart d'abonnement au calendrier mis en avant en tête d'agenda (Google + webcal Apple/Outlook). Lien Google en `calendar/r?cid=` (ne force plus le 1er compte connecté).
- ✅ Dédoublonnage /le-nid : 3 cartes « Scène ouverte/Showcase » + 3 encarts « Prochaines dates » en trop supprimés. **Cause corrigée dans `generate_agenda_nid.py`** (injections non idempotentes : il réinjectait à chaque exécution). ⚠️ Même famille de bug encore présente sur les **4 entrées « Agenda » du menu** (en cours de correction).
- ✅ Adresse asso : **siège social 2 impasse des Bleuets, 09600 Aigues-Vives** + **correspondance 29 rue des Orteaux, 75020 Paris** (remplace 6 rue de la Condamine). Liens **« Statuts de l'association »** (Google Doc) sous l'Article 2 de l'accueil et en pied de page.

### Google Agenda « Le Nid » (`30716d7f…@group.calendar.google.com`)
- ✅ Descriptions des 5 showcases enrichies (déroulé 5 points + paragraphe enfants).
- ✅ **Code portail retiré des 20 événements** → « Le code du portail vous est communiqué avec votre confirmation d'inscription. » Flux public vérifié : 0 occurrence. Le code part désormais **uniquement dans l'email de confirmation**. Calendrier public conservé.
- ✅ 3 rappels (10080 / 1440 / 120 min, popup) sur les 42 événements. **Limite Google actée : les rappels d'un calendrier public ne se propagent PAS aux abonnés** (chacun a les siens). Seuls les `.ics` téléchargés embarquent les rappels.
- ⚠️ Incident traité : le code portail avait été écrit par erreur dans ce fichier handoff et poussé sur ce dépôt **public** ; retiré + historique réécrit + force-push, clone neuf vérifié propre. Le code doit être considéré comme ayant été exposé (le flux du calendrier l'exposait déjà avant).

### Quick wins UX déployés (04/08)
- ✅ Une seule entrée « Agenda » dans le menu de /le-nid + **garde-fou dans le générateur** (même bug d'injection non idempotente que les cartes).
- ✅ Cibles tactiles : filtres d'agenda `min-height:44px`, liens de pied de page à 44-45 px sur les 5 pages.
- ✅ Plancher typographique 13 px (badges 14 px) — seuls restent les `<sup>` (« 3ᵉ étage »), légitimes.
- ✅ `:focus-visible` doré sur les 5 pages.
- ✅ `alt` des photos recopiés depuis les légendes affichées (25/26 sur rituals, 38/39 sur trio ; le seul `alt` vide restant est la visionneuse dynamique).
- ✅ Téléphones en `tel:` sur rituals et rituals-trio.
- ✅ Favicon (`favicon.svg` cercles concentriques or/nuit + `favicon.ico` + `apple-touch-icon.png` 180×180), `theme-color`, `og:url`, `twitter:card`, **`og-image.jpg` 1200×630** (photo de salle comble extraite du base64 de rituals) sur les 4 pages qui n'en avaient pas.
- Vérifié aux 3 largeurs (390/820/1440) sur les 5 pages : 0 débordement horizontal, carrousels intacts (20 et 31 slides, aucune à 2 px, aucun `loading="lazy"`), hamburger OK (artefact connu : dans un iframe en arrière-plan les transitions CSS sont gelées → tester en neutralisant `transition`).
- ⚠️ NON FAIT volontairement : **lien d'évitement** (aucun n'existait réellement sur /rituals contrairement à l'audit → créerait un texte visible à valider) · **lien Facebook mort** laissé tel quel (David doit fournir l'URL) · `og:image` de /e-motion toujours sur le CDN tiers cloudfront.

### En cours
- **Agent quick wins techniques** (ce dépôt) : 1 seule entrée « Agenda » dans le menu + cause dans le générateur · cibles tactiles 44 px & plancher typo 13/14 px · `:focus-visible` + liens d'évitement · `alt` des photos rituals/trio recopiés depuis les légendes visibles · téléphones en `tel:` · favicon + `og:image`/`og:url`/`twitter:card` + `theme-color` · lien Facebook mort signalé sans invention d'URL. Commits locaux incrémentaux, **pas de push** (une 1re tentative a été perdue sur erreur API 529).
- **Handpan Studio (AUTRE dépôt `~/CLAUDE/NEOTONE STUDIO/NEOTONE 1er mai 2026/`)** : tableau de suivi des inscriptions showcase + email de confirmation. Commits locaux `5e8eabb` → `be7b625` → `5ec34c8` → `ba99b5c`, **non déployés**. Fichiers : `auth/showcase-panel.ts`, `supabase/functions/confirm-showcase/index.ts`, `auth/account-menu.ts`, `config.toml`. Données : table `site_leads` existante (aucune migration). Horaires par date dans `EVENT_HOURS` (à compléter pour toute nouvelle date) + surcharge manuelle dans le panneau. Email = code portail + temple/déchaussage + non fumeur + copropriété d'artistes + enfants (activités + espace dédié) + boire sans alcool/grignoter + focus Neotone + orientation RDV individuel payant + jauge 20 + engagement/communauté + responsabilité en cas de casse.

## FILE D'ATTENTE — chantiers décidés (04/08), à faire dans cet ordre
1. **Images (EN COURS)** : rapatrier TOUTES les images en local (fini cloudfront / squarespace / Drive) + extraire les ~60 base64 → fichiers WebP + fallback JPEG, `srcset` responsive (480/900/1400), `width`/`height`, `loading="lazy"` sauf 2-3 premières. ⚠️ Piège carrousel (`lazy` → slides à 2 px) : réserver les dimensions. Générateurs à mettre à jour sinon régression. Contenu strictement intact.
2. **« Le Soin Soa » (EN COURS)** : encart « Bains sonores & soins vibratoires » de l'accueil alimenté depuis `https://www.irischasles.com/agenda-yoga/immersion-therapeutique-soa` (texte + images rapatriées en local, structure extensible — David fournira d'autres photos). Titre imposé : « Le Soin Soa ». Texte à faire valider. Vigilance registre : pas de promesse thérapeutique.
3. **Menu à refondre** (touche les 5 pages → après le chantier images) : un seul onglet parent au lieu de 2 entrées RITUALS. Proposition faite à David : **« Spectacles & concerts »** (son idée initiale : « Concerts Rituels grand public ») avec sous-menu **RITUALS — duo · RITUALS — trio · E-Motion · Concerts de David Lesage**, RITUALS en premier (exigence de David). Harmoniser le menu sur les 5 pages + état actif `aria-current` (l'audit signalait des menus différents partout).
4. **Versions EN + ES** (après le menu) : **accueil + RITUALS duo + RITUALS trio + E-Motion**. **Le Nid non prioritaire** (décision David du 04/08 — page très locale ; agenda/billetteries franco-français). Structure retenue : `/en/…` et `/es/…` + sélecteur de langue dans le menu + `hreflang`.

## ⏸️ EN ATTENTE DE DÉCISION DE DAVID
1. **Validation du texte de l'email de confirmation showcase** → puis deploy EF `confirm-showcase` + build + `npx vercel --prod --yes` + `git push` + changelog + **email test à David avant tout envoi réel**. Sous-questions : ajouter les prix des RDV individuels (50 € / 70 € d'après le site) ? La jauge de 20 n'est **pas** bloquée automatiquement (aucun contrôle) — vouloir un blocage/alerte = chantier à part.
2. **Nom français de « Showcase »** (reco : « Session découverte handpan ») → à répercuter sur /le-nid, les 5 titres Google Agenda, `generate_agenda_nid.py`.
3. **Libellés de réservation /le-nid** : harmoniser en « Réserver » + mention de destination ; renommer le bouton global `.ag-foot` (mailto) en « Nous écrire » ; **le rendez-vous mensuel exige-t-il vraiment l'adhésion ?** (aujourd'hui son seul bouton est « Adhérer ») ; les 3 concerts pointent vers l'accueil de lesagedavid.fr, pas vers la date.
4. ~~Extraction des images en WebP~~ → décidé, voir file d'attente ci-dessus. Détail du piège : (gain ≈ −90 % au 1er affichage ; 3,4 Mo transférés aujourd'hui, ≈3 s d'écran vide en 4G, ≈14 s en réseau faible). ⚠️ Piège : `loading="lazy"` sur les slides casse le carrousel (2 px) → réserver les dimensions (`width`/`height` ou `aspect-ratio`) et garder les 2-3 premières en `eager`.
5. **Refonte de l'accueil** (contenu → validation) : accroche orientée visiteur, photo en hero (0 image aujourd'hui), bandeau « prochaines dates », statuts résumés + lien, CTA principal « Voir les prochaines dates » au lieu d'« Adhérer ».
6. **Bouton « Nous contacter »** en fin de /rituals et /rituals-trio (pages commerciales sans aucun bouton de contact).
7. **URL de la page Facebook** (le lien du pied de page pointe vers l'accueil de Facebook).
8. Décisions anciennes : suppression de `/solune` et `/au-nid` (HTTP 200, indexables) · adresse de booking de /e-motion = `booking@solune.show` (autre marque) · rôle de Julien sur /rituals-trio · séance photo trio.
9. **Page groupe calebasse sur lesagedavid.fr** (projet `site-vitrine`) : priorité appel au groupe vs vente formation ? (reco : groupe d'abord, formation en second bloc).

## Audit UX du 04/08 — synthèse
Points forts : identité visuelle homogène sur les 5 pages (palette/polices/composants), zéro débordement horizontal aux 3 largeurs, hamburger OK partout, carrousels tactiles, contrastes AA, un seul h1 par page, titres/descriptions soignés.
Top 5 problèmes : (1) poids des pages RITUALS · (2) 4× « Agenda » dans le menu /le-nid · (3) 5 libellés de réservation différents + « Adhérer » comme seule porte du RDV mensuel · (4) accueil centré association, sans photo, CTA « Adhérer » · (5) aucun favicon ni image de partage.
Autres : menus différents d'une page à l'autre + aucun état actif · /rituals-trio quasi introuvable · 4 cartes « Prestations » non cliquables · pages de 12 000-14 500 px sans retour en haut · cibles tactiles 31 px et textes à 10,5 px · `alt` vides · pas de `robots.txt`/`sitemap.xml`.

**Règles clés :** aucun texte publié sans validation David · jamais toucher aux DNS email OVH · pas de `loading="lazy"` sur les slides carrousel · code portail jamais sur le site/dans les .ics/liens publics/ce dépôt · vérifier (build + rendu réel) avant de présenter · navigateur = extension Claude-in-Chrome, jamais les screenshots computer-use · Handpan Studio : `npx vite build` + `npx vercel --prod --yes` + push séparé + changelog.

## Journal
- **2026-08-03** — Bascule Cowork → Claude Code. Clone du dépôt, copie des sources, fix hamburger (déployé), enrichissement Google Agenda showcases, audit des liens /le-nid, construction du tableau admin showcase Handpan Studio.
- **2026-08-04** — Reprise. Calendrier /le-nid (filtres, boutons Google Agenda, encart d'abonnement) vérifié et déployé · dédoublonnage des cartes + cause corrigée dans le générateur · nouvelle adresse asso + liens statuts · Google Agenda nettoyé du code portail + 3 rappels · incident code portail dans le handoff public traité (historique réécrit) · audit UX complet des 5 pages aux 3 largeurs · lancement des quick wins techniques.
