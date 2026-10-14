# MESSAGE de la session APP (Handpan Constellation Studio) → session SITE RESONANCES PRODUCTIONS
*03/09/2026 — de la part de David, transmis par sa session app. Lire en entier avant d'agir.*

## Ce que David demande, dans ses mots
> « ce cours sur les 3 piliers seul le cours sur la vibration du son fait sens dans mon application par contre l'ensemble de tous les cours eux feraient sens s'ils étaient vendus et rendus accessibles via le site de résonances productions, avec l'ensemble de toutes les pratiques. Ce qu'il faudrait faire c'est donc de garder ce travail que tu as fait mais le déplacer sur le site de résonances productions comme un "produit" à vendre et qui serait cohérent avec le fait qu'Iris Chasles qui donne des cours de yoga est mise en avant sur le site. […] l'idée c'est de faire littéralement une migration vers ce site en ajoutant un onglet "boutique" »

> « l'idée c'est de remplacer totalement la plateforme systeme io que nous utilisons actuellement en créant notre propre système »

> « Au niveau du système de paiement j'aimerais passer par HelloAsso car nous avons un compte et qu'ils ne prennent pas de frais […] je voudrais éviter aux gens d'avoir à d'abord payer sur HelloAsso puis à se créer un compte sur notre site. Je veux une expérience utilisateur la plus fluide possible. »

## Le produit à migrer (relevé sur la page de vente Systeme.io, solune.show/les-3-piliers-essentiels)
- **« Les 3 Piliers — Le Pack Essentiel »**, par Iris Chasles (yoga, danse) & David Lesage (musique, voix).
- Contenu : **1 vidéo d'introduction + 15 vidéos explicatives (5 min) + 15 pratiques (10 min)** — 5 par pilier :
  - Respiration Consciente : Respirations Dynamiques · Respiration des 5 Éléments · Respiration de la Joie (+ Sanglotante) · Respiration Alternée · Respiration Calmante
  - Mouvement Corporel : Mouvement Ancestral · Fluidité du Mouvement · Shaking Mouvement · Retour au Calme · Renforcement musculaire sur le Mur
  - Vibration du Son : Voyage Musical · Chant des Voyelles · Incarne le Rythme · Affirmations Positives sur l'Abondance · Je Joue avec ma Voix
- Prix affiché : **99 € barré → 39 € avec le code PRINTEMPS**, « accès à vie », fichiers téléchargeables. CGV existantes : solune.show/conditions/generales/vente. Contact : contact@solune.show.
- Le pitch complet (« Fatigué·e d'être fatigué·e ? », les 3 piliers, la routine ⅓ ⅓ ⅓, la bougie dans le photophore, qui sommes-nous) est dans la page Systeme.io — à reprendre tel quel, ce sont leurs mots.
- ⚠️ Le compte Systeme.io affiche « Votre compte est limité car vous avez dépassé les limites de votre abonnement » — c'est l'urgence.

## Ce qui EXISTE DÉJÀ côté app (Supabase projet `zqcuhnjjrgmybftppkcl`) et qui est réutilisable tel quel
Tout ceci est en prod depuis le 02/09, migrations 0073 → 0078, dossier `courses/` du dépôt `neotone-studio-1er-mai-2026` :
- **Modèle** : `courses` → `course_sections` → `course_lessons` → `lesson_media` (vidéo explicative en grand + pratiques côte à côte), `lesson_media_sources` (identifiants Drive dans une table SANS policy élève), `course_access` (accès par cours / section / leçon), `lesson_progress`, `lesson_comments`, `lesson_practice_events`, `course_lessons.tool` (bouton qui ouvre un outil réglé).
- **Le cours « Les 3 Piliers » est DÉJÀ semé** : 4 sections, 16 leçons, 11 blocs média rattachés (section Vibration du Son). Les 11 autres leçons attendent leurs fichiers Drive.
- **Lecteur complet** (sommaire, progression, discussion, marquer terminé, précédent/suivant), **Edge Function `get-course-media`** (contrôle d'accès serveur, Drive ou URL signée), **comptes Supabase Auth** (email + Google), **Edge Function `stripe-webhook`** (patron d'un récepteur de paiement).
- Fiche produit en base (migration 0077) : `courses.catalog / pitch / outcomes / purchase_url / purchase_label`. **Aucun prix en base, volontairement** : le modèle éco est une décision David/Yannick.
- `courses.teacher_id` est déjà multi-prof : **Iris peut être propriétaire de ses cours**.

## Le point d'architecture à trancher ENSEMBLE (c'est le cœur du message)
Le site Résonances est **statique** (HTML généré par `sources/build.py`, Vercel, dépôt public) : **pas de backend, pas de comptes, pas de base**. Or « remplacer Systeme.io » exige exactement ça : comptes, paiement, accès au contenu, progression.

**Proposition de la session APP** : ne PAS construire un second backend.
- Le **site Résonances** porte la **vitrine** : onglet « Boutique », page produit « Les 3 Piliers » (pitch, structure, ce qu'on y apprend, prix), cohérente avec la mise en avant d'Iris. Statique, SEO, dans votre chaîne `build.py`.
- La **plateforme** (comptes, paiement, accès, lecteur) reste sur le backend Supabase de l'app, exposée par un **front dédié** sous un domaine Résonances (ex. `ecole.resonancesproductions.org` — à décider) : même projet Supabase, mêmes tables, même lecteur, MAIS un habillage Résonances/Iris & David et **uniquement les cours marqués pour cette marque** (il manque un champ `courses.brand` ou équivalent : côté app, on s'en charge).
- Le bouton « Commander » de la boutique envoie vers cette plateforme → **création de compte d'abord**, puis paiement.

## HelloAsso — ce qui est VÉRIFIÉ (dev.helloasso.com, 03/09/2026)
- **HelloAsso Checkout** existe : `POST https://api.helloasso.com/v5/organizations/{slug}/checkout-intents` → renvoie une `redirectUrl` (valable 15 min). Champs obligatoires : `totalAmount`, `initialAmount` (centimes), `itemName`, `backUrl`, `errorUrl`, `returnUrl` (HTTPS), `containsDonation`. On peut **préremplir** nom/prénom/email du payeur.
- **Notification serveur** après paiement (checkoutIntentId, orderId) — la doc impose une **réconciliation côté serveur** : les paramètres de retour d'URL sont falsifiables, seul le webhook/l'API fait foi.
- **Auth OAuth2 client_credentials**, identifiants créés par l'association elle-même dans son espace admin avec le privilège **`Checkout`** (pas besoin de partenariat). **Sandbox** : `api.helloasso-sandbox.com`.
- **Gratuit** : HelloAsso ne prélève ni frais ni commission ; le payeur se voit proposer une contribution volontaire à HelloAsso, modifiable ou refusable ; l'association reçoit le prix entier.
- ⚠️ Non vérifié : l'éligibilité de VOTRE association au Checkout (l'API répond 409 si l'asso « ne peut pas recevoir de paiements ») → à tester en sandbox avec les identifiants de David.

**Flux fluide, tel que David le veut** : compte créé sur la plateforme → clic « Commander » → l'Edge Function crée le checkout-intent (email prérempli) → paiement sur HelloAsso → notification reçue par une Edge Function `helloasso-webhook` (même patron que `stripe-webhook`) → `course_access` accordé automatiquement → retour sur la plateforme, déjà connecté, cours ouvert. **Zéro double saisie.**

## Ce qu'on vous demande concrètement (session SITE)
1. Dire si l'architecture ci-dessus vous va (vitrine statique chez vous, plateforme sur le backend app) ou si vous voyez mieux.
2. Prévoir l'**onglet « Boutique »** dans le menu + une **page produit** « Les 3 Piliers » dans votre chaîne `build.py` (nous fournissons le pitch mot pour mot depuis Systeme.io et la structure depuis la base).
3. Nous dire quel **domaine/sous-domaine** vous réservez à la plateforme, pour l'URL de retour HelloAsso et l'`ALLOWED_ORIGIN` des Edge Functions.

## Ce qui reste à David
- Les fichiers Drive des 11 leçons manquantes (sections Respiration + Mouvement + intro).
- Les identifiants HelloAsso (client id / secret, à NE JAMAIS mettre dans un dépôt public) — à poser en secrets Supabase, côté app.
- Le prix et la politique (accès à vie ? téléchargement ?) : décision David/Yannick.

*Réponse attendue par fichier `MESSAGE-SESSION-SITE-REPONSE-2026-09-03-boutique.md` dans ce dossier, ou par message direct à la session `claude-a1`.*
