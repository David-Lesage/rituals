# REPRENDRE — Site Résonances Productions

> Handoff du projet. Complément local du document de reprise complet :
> `Drive partagés/1 - RESONANCES PRODUCTIONS/SITE_WEB_DEV/HANDOFF_CLAUDE_CODE.md`
> (architecture, chaîne de déploiement, pièges, règles). Le lire aussi.

## ÉTAT ACTUEL (2026-08-03, fin de soirée — David en pause, reprise demain)

**Fait & déployé :**
- Dépôt cloné (`David-Lesage/rituals` → ce dossier). Push = déploiement Vercel auto sur resonancesproductions.org.
- `sources/` (générateurs + sources HTML) copiés du Drive dans le dépôt.
- ✅ §7.1 hamburger mobile corrigé + DÉPLOYÉ (`4f5e7b1`). Cause : `backdrop-filter` du `.nav` = conteneur des fixed + stacking context ; fix : `body.nav-open .nav{backdrop-filter:none;z-index:1001}` (mobile_nav.py + les 5 pages). **David n'a pas encore retesté sur son téléphone.**
- ✅ Google Agenda « Le Nid » : descriptions des 5 showcases enrichies (déroulé 5 points + enfants). Aucun autre événement/champ touché.
- ✅ Liens /le-nid audités : chaque ligne d'agenda pointe juste ; seul le bouton global `.ag-foot` (mailto) est fautif → §7.2.

**En cours (agents de fond au moment de la pause) :**
- **Agent calendrier /le-nid** (dépôt = ici) : boutons « Ajouter à mon Google Agenda » par événement (en PLUS des .ics conservés ; jamais le code portail, grep doit rester 0) + filtres par type et par mois + ancre #concerts pré-filtrée = vue « toutes les dates de concerts ». Commit local sans push attendu. → À la reprise : lire son résultat, VÉRIFIER le rendu, montrer à David avant push. Limitation actée avec David : les liens Google TEMPLATE ne peuvent pas imposer de rappels (rappels = .ics + abonnement calendrier).
- **Handpan Studio (AUTRE dépôt : `~/CLAUDE/NEOTONE STUDIO/NEOTONE 1er mai 2026/`)** : tableau de suivi des inscriptions showcase construit — commits locaux `5e8eabb` → `be7b625` → `5ec34c8`, PAS déployés ni poussés. Fichiers : `auth/showcase-panel.ts` (nouveau), `supabase/functions/confirm-showcase/index.ts` (nouveau), `auth/account-menu.ts`, `config.toml`. Données : table `site_leads` existante (aucune migration). Horaires par date dans `EVENT_HOURS` (à compléter pour toute nouvelle date) + surcharge manuelle dans le panneau.

**⏸️ EN ATTENTE DE DAVID (à lui redemander à la reprise) :**
1. **Validation finale du texte de l'email de confirmation showcase** (montré en entier dans le chat du 03/08 ; contient code portail le code portail — politique voulue —, temple/déchaussage, non fumeur, enfants, apporter à boire sans alcool/grignoter, tél 06 10 73 31 52, horaires dynamiques, réf. Google Agenda). Questions posées : liste des instruments (Neotone, Yishama, micros, Gonilélé, calebasse) exacte ? mention « gratuit et sans obligation d'achat » OK ? → Après OK : deploy EF `confirm-showcase` + build + `npx vercel --prod --yes` + `git push origin master` + changelog, puis EMAIL TEST à David avant premier vrai envoi.
2. **Nom français des showcases** (reco : « Session découverte handpan ») → à répercuter ensuite sur /le-nid, titres des 5 événements Google Agenda, generate_agenda_nid.py.
3. **§7.2 libellés** : bouton global → « Nous écrire » ? boutons par carte (yoga → HelloAsso atelier, calebasse → mailto provisoire, cours individuels → lien ?). + nettoyer les 4 liens « Agenda » dupliqués dans le menu de /le-nid.
4. **Page groupe calebasse sur lesagedavid.fr** (projet site-vitrine) : priorité appel au groupe vs vente formation ? (ma reco : groupe d'abord, formation en second bloc).
5. Décisions §9 du handoff Drive toujours ouvertes (siège social, rôle Julien, suppression /solune /au-nid, code portail agenda public, photos trio).

**Règles clés :** aucun texte publié sans validation David · jamais toucher aux DNS email OVH · pas de `loading="lazy"` sur les slides carrousel · le code portail jamais sur le site ni dans les .ics/liens publics (grep = 0) · vérifier avant de présenter · Handpan Studio : déploiement via `npx vite build` + `npx vercel --prod --yes` + push séparé + changelog.

## Journal
- **2026-08-03** — Bascule Cowork → Claude Code. Clone du dépôt, copie des sources, fix hamburger (déployé), enrichissement Google Agenda showcases, audit des liens /le-nid, construction du tableau admin showcase Handpan Studio (3 commits locaux, texte email finalisé, en attente validation), lancement agent filtres+Google Agenda sur /le-nid (en cours à la pause). David fait une pause, reprise demain.
