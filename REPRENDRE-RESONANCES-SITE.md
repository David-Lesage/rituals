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

# 🗓️ L'AGENDA GOOGLE MET LE SITE À JOUR TOUT SEUL (27/08/2026)

*Cette section est écrite pour David. Aucune commande à taper, aucun jargon.*

## En une phrase

**Ton agenda Google « Le Nid » est devenu la seule source des dates du site.**
Chaque nuit, vers 5 h du matin, le site va le lire, se refabrique et se republie tout
seul. Tu n'as plus rien à me demander : tu ajoutes une date dans ton agenda, elle est
en ligne le lendemain matin. Une date passée disparaît de la même façon.

Ça tourne sur GitHub, c'est **gratuit** (le dépôt est public), et **aucune IA n'est en
marche** : c'est du code qui fait toujours exactement la même chose.

## Pour qu'une date apparaisse sur le site : duplique un événement existant

C'est la seule chose à retenir.

> Dans Google Agenda, **ouvre un événement du même genre qui existe déjà**, fais
> « Dupliquer », et change la date et l'heure. **Ne touche pas au titre.**

Pourquoi : le site ne publie que les événements dont le titre est dans une liste
connue. Un titre reconnu = la date paraît. Un titre inconnu = **elle ne paraît pas**,
et je (ou GitHub) te préviens. C'est volontaire, et c'est ce qui protège le site.

**Les neuf titres reconnus aujourd'hui** (à gauche ce que dit ton agenda, à droite ce
que le site affiche) :

| Dans ton agenda Google | Sur le site |
|---|---|
| `Rendez-vous mensuel au Nid` | Rendez-vous mensuel au Nid |
| `INSTATIC Dance — Le Nid` | INSTATIC Dance · *avec Iris & David* |
| `Concert de David Lesage — Le Nid` | Concert — David Lesage solo |
| `Concert de David Lesage — Le Nid + Guest Lucie au violon` | Concert — David Lesage solo |
| `Concert RITUALS trio — David, Iris & Julien — Le Nid` | Concert — David, Iris & Julien |
| `Concert Sortie de résidence — Le Nid` | Sortie de résidence |
| `Atelier de yoga — Le Nid` | Atelier de yoga · *avec Iris Chasles* |
| `Groupe de pratique rythme calebasse engagé — Le Nid` | Groupe de pratique rythme calebasse engagé |
| `Présentation d'instruments d'exception — Le Nid` | Présentation d'instruments d'exception |

Tu vois que **le titre du site n'est pas celui de l'agenda**. C'est voulu : ce sont des
textes qu'on a écrits et validés ensemble. Ça veut aussi dire qu'un emoji, un nom
d'invité ou une note perso glissés dans un titre d'agenda **ne peuvent pas** se
retrouver sur le site.

## Ce qui n'ira JAMAIS sur le site

- **Tout ce dont le titre n'est pas dans le tableau ci-dessus.** Si tu notes « RDV
  médecin » ou « Anniversaire Iris » dans cet agenda, c'est ignoré. (Testé : ils sont
  bien restés dehors.) Cet agenda a déjà contenu 13 événements privés — c'est
  exactement pour ça que la règle est aussi stricte.
- **Les descriptions de tes événements.** Elles ne sont même pas lues. C'est important :
  elles contiennent la phrase sur le code du portail.
- **Les lieux, les invités, les adresses e-mail.** Jamais lus non plus.
- **Un événement « journée entière »** (sans horaire) : le site a besoin d'une heure de
  début et d'une heure de fin. Mets un horaire.
- **Un événement qui se répète** (« tous les mois »). Crée-les un par un ou duplique-les.

## Comment savoir qu'une date n'est pas passée

Quand un événement à venir n'est pas reconnu, **GitHub t'envoie un e-mail** disant que
la tâche « Agenda du Nid » a échoué. Le site, lui, a bien été mis à jour pour tout le
reste. Dans l'e-mail, un lien mène à la page où c'est écrit noir sur blanc : quel
événement, et pourquoi.

Pour aller voir toi-même à n'importe quel moment :
**github.com/David-Lesage/rituals → onglet « Actions » → « Agenda du Nid »**. Chaque
nuit y laisse une ligne. Vert = tout est passé, rouge = quelque chose est à regarder.

## Si une date n'apparaît pas — les trois choses à vérifier, dans l'ordre

1. **L'orthographe du titre** dans ton agenda. Une lettre en trop et ce n'est plus le
   même titre. (Les accents comptent ; les espaces en double et les majuscules, non.)
2. **L'événement a-t-il un horaire ?** Une « journée entière » n'est pas publiable.
3. **Est-ce que la nuit est passée ?** La mise à jour a lieu vers 5 h du matin. Une date
   ajoutée à 22 h paraît le lendemain matin, pas dans la minute.

Et si tu veux la publier **tout de suite** sans attendre la nuit : onglet « Actions » →
« Agenda du Nid » → bouton **« Run workflow »**. Ça prend deux minutes.

## Pour l'arrêter

Onglet **« Actions »** du dépôt → « Agenda du Nid » → le menu **« … »** en haut à droite
→ **« Disable workflow »**. Le site reste exactement dans l'état de la dernière nuit ;
rien n'est perdu, rien n'est effacé. On peut le réactiver au même endroit.

## Ce que ça ne fait PAS (à savoir)

- **Ça ne rédige rien.** Une nouvelle soirée mensuelle apparaît avec la mention
  « Programme en cours d'élaboration », et elle reste comme ça tant que le texte n'est
  pas écrit. C'est le seul travail humain qui reste.
- **Ça ne crée pas de billetterie.** Si tu déplaces un concert qui a un lien HelloAsso,
  la mise à jour **s'arrête et te prévient** plutôt que de publier un bouton
  « Réserver » qui mènerait au mauvais endroit.
- **Ça ne touche pas à deux pages qui portent encore leurs propres dates** :
  `/rythme-calebasse` et `/concerts-david-lesage`. Elles se mettent à jour à la main.
  Le script le rappelle à chaque passage, sans jamais rien changer chez elles.
- **Ça ne rattrape pas les textes qui vieillissent** : par exemple, la phrase de
  présentation de `/concerts-david-lesage` cite « 10 octobre et 28 novembre 2026 ».

## Une seule chose à faire de ton côté, une seule fois

Après la mise en ligne de ce chantier, va sur
**github.com/David-Lesage/rituals → onglet « Actions »** et vérifie que les
« workflows » sont **activés** (GitHub demande parfois de cliquer un bouton vert la
première fois sur un dépôt qui n'en avait jamais eu). Ensuite, plus rien.

## Pour la prochaine session (technique)

- Le script : **`sources/synchro_agenda.py`**. Il s'explique en tête de fichier. Mode
  essai par défaut (`python3 sources/synchro_agenda.py`), `--appliquer` pour agir,
  `--flux <fichier.ics>` pour rejouer un faux flux, `--date AAAA-MM-JJ` pour simuler un
  autre jour. **Il ne touche jamais à git.**
- La tâche planifiée : **`.github/workflows/agenda-du-nid.yml`**, `cron: '17 3 * * *'`.
- La liste blanche : le dictionnaire **`CORRESPONDANCE`**. Un type nouveau doit exister
  dans `TYPES` de `generate_agenda_nid.py` — le script le vérifie et refuse sinon.
- `EVENTS` de `generate_agenda_nid.py` vit entre deux balises
  `# --- DEBUT/FIN DES DATES SYNCHRONISEES ---`. **Ne rien écrire entre elles** : c'est
  réécrit à chaque passage. Les notes vont au-dessus.
- `/rendez-vous-mensuels` **lit** ses dates dans `EVENTS` et ne garde que le texte de
  chaque soirée (`CONTENUS`, rangé par date). Une soirée passée n'efface jamais son
  texte.

---

## LES 31 PAGES EN LIGNE (2026-08-20)

| URL | Rôle | Public |
|---|---|---|
| `/` | Accueil association | mixte |
| `/rituals` | Concert-rituel duo | programmateurs |
| `/rituals-trio` | Concert-rituel trio (avec Julien Dub) | programmateurs |
| `/e-motion` | Spectacle immersif participatif (ID duo) | programmateurs |
| `/david-lesage-en-concert` | **Concerts solo — grandes scènes & festivals** + fiche technique | programmateurs |
| `/concerts-david-lesage` | **Concerts solo — version intimiste au Nid** | particuliers Paris |
| `/le-nid` | Le lieu, programme, agenda | particuliers Paris |
| `/rendez-vous-mensuels` | **Les RDV Mensuels au Nid** : le projet, puis le programme et un encart par date | particuliers Paris |
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

### 🔑 `/guso-facile/app` — l'adresse de connexion des bêta-testeurs (17/08/2026)

*Une seule ligne à changer le jour où l'application déménage. C'est tout l'intérêt.*

**Le problème.** L'application Guso Facile vit sur `https://guso-facile.vercel.app/index.html`.
David n'a pas acheté de nom de domaine et ne le fera pas maintenant (bêta privée, gratuite).
Les bêta-testeurs, eux, **ont déjà un compte** : depuis la fusion du 16/08 le bouton de la page
mène au **formulaire de demande**, pas à l'écran de connexion — ils n'avaient plus aucun chemin,
et devaient retaper une adresse en `vercel.app` de mémoire.

**Ce qui a été posé.** Une adresse à nous, sur le domaine de l'association, qui ne fait que
rediriger (dans `vercel.json`) :

| Adresse | Envoie vers | Type |
|---|---|---|
| `/guso-facile/app` | `https://guso-facile.vercel.app/index.html` | **302** (temporaire) |
| `/guso-facile/app/` | idem | **302** (temporaire) |

Et, sur la page, un **lien texte discret** sous le bouton — « J'ai déjà un compte → me connecter » —
dont le `href` vaut `/guso-facile/app`, **jamais l'adresse de l'application**.

**⚠️ Pourquoi 302 et pas 301, et pourquoi il ne faut pas « harmoniser ».**
Les 11 autres redirections du fichier sont en **301** (permanentes) et c'est juste : elles pointent
vers des pages **internes et définitives** (`/accueil` → `/`, `/statuts` → `/association#statuts`…).
Celle-ci est l'inverse : **sa destination est provisoire par construction**. Or un 301 est mis en
cache par les navigateurs quasi définitivement — le jour où David prendra un domaine, chaque
bêta-testeur qui aurait cliqué une seule fois resterait envoyé sur l'**ancienne** adresse par son
propre navigateur, sans que rien côté serveur puisse le rattraper. Ce serait exactement l'inverse
du but recherché. **Ne pas passer cette ligne à `"permanent": true`.**

**Le jour du déménagement** (nouveau domaine, ou app déplacée) : changer la `destination` des deux
lignes dans `vercel.json`, `python3 sources/build.py`, `python3 sources/verif_site.py`, pousser.
Rien d'autre. Les favoris et les adresses mémorisées continuent de marcher.

**Ce qui ne se teste pas en local.** `vercel.json` n'est lu que par la plateforme : un
`python3 -m http.server` rendra toujours **404** sur `/guso-facile/app`. Le premier clic réel
se fait **en production**, après publication. Ce qui est vérifiable hors ligne — et qui l'est — :
le JSON est valide, la destination est bien formée, et la page ne contient nulle part l'adresse en dur.

**Référencement.** `robots.txt` porte `Disallow: /guso-facile/app` : une adresse de connexion
n'a aucune valeur en référencement. (L'application envoie déjà, de son côté,
`<meta name="robots" content="noindex,follow">`.) Elle n'est pas non plus dans `sitemap.xml`.

**Ce que `verif_site.py` a appris au passage.** Deux contrôles ne connaissaient pas ce mécanisme et
auraient refusé le site à tort : « liens » comptait comme **mort** tout lien interne sans fichier
correspondant (une URL redirigée n'est pas morte), et « plan » exigeait qu'une redirection pointe
vers une page **interne** (une destination peut être une adresse absolue externe). Les deux savent
maintenant lire les redirections de `vercel.json` — **sans rien desserrer** : seule une URL
réellement déclarée en `source` est acceptée, et le jour où la redirection disparaîtrait du fichier,
le lien de la page redeviendrait signalé comme mort.

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
🗓️ **DEPUIS LE 27/08/2026, CET AGENDA EST LA SOURCE UNIQUE DES DATES DU SITE** — il est lu
chaque nuit et le site se republie tout seul. Mode d'emploi complet : section « 🗓️ L'AGENDA
GOOGLE MET LE SITE À JOUR TOUT SEUL » en haut de ce fichier. ⚠️ Ne plus modifier `EVENTS` à
la main en pensant que ça durera : la nuit suivante réécrit tout depuis l'agenda.
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
0. 🗓️ **Concert du 28 novembre : « solo » ou « + Guest Lucie au violon » ?** L'agenda Google
   annonce « Concert de David Lesage — Le Nid **+ Guest Lucie au violon** », le site écrit
   « Concert — David Lesage solo ». Les deux se contredisent. La synchronisation reproduit
   **ce qui est déjà en ligne** ; changer l'annonce est une décision de David. (Une fois
   tranché : une ligne de `CORRESPONDANCE` dans `sources/synchro_agenda.py`.)
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
13. 🔴 **Photos trop petites pour la visionneuse** — les **3 portraits de `/le-soin-soa` (260 px)**
    d'abord : à cette taille l'agrandissement est quasi nul. Puis `portrait-iris-chasles` (480 px,
    sur 3 pages) et `portrait-julien-dub-au-saxophone` (480 px). Fournir des variantes 900 px, ou
    décider de sortir ces photos de la visionneuse.
14. **Visionneuse — arbitrages laissés ouverts** : les 3 portraits 260 px restent-ils cliquables
    (cohérence) ou en sortent-ils ? · la photo du haut de `/le-nid` est un **fond** (recouverte
    par le voile qui rend le titre lisible) → laissée dehors, sinon un clic couvrirait toute
    l'entête sous le titre et les boutons · les 15 vignettes vidéo et le logo des deux pages
    « concert » restent à leur seul rôle.
15. **E-Motion, aperçu de partage (17/08)** : le titre de partage est celui de Solune et ne porte
    plus **« · ID duo »** (le nom du duo reste dans le `<title>`, dans `og:image:alt` et dans la
    page). Le récupérer ? Et l'affiche garde le logo **« SOLUNE présente »** en tête : à trancher
    avec l'avancée de la migration vers Résonances.
14. **`/guso-facile` est devenue très longue** : **25 455 px à 390 px de large**, 15 038 px à
    1440, alors que l'en-tête du générateur annonce un plafond visé de ~12 500 px. Dépassé bien
    avant l'ajout du lien de connexion (+50 px). Soit on relève le plafond et on le réécrit, soit
    on décide une passe de raccourcissement. Rien n'est cassé.
15. **L'app Guso Facile n'est pas installable sur l'écran d'accueil** (chantier dans l'AUTRE
    dépôt, signalé à la session `GUSO FACILE V4`) : aucun `manifest.json` (404), pas de service
    worker, pas d'`apple-touch-icon`, pas de `theme-color`. « Ajouter à l'écran d'accueil » ne
    donne qu'un marque-page, pas une icône d'application. C'était la piste la plus utile pour
    simplifier la vie des bêta-testeurs — elle ne se règle pas depuis ce dépôt.
16. ⚠️ **À voir avec le comptable** : l'association a désormais **trois activités commerciales** (album, calebasses pyrogravées, billetteries) → lucrativité, franchise des impôts commerciaux (~80 k€), tenue de comptabilité.

## FILE D'ATTENTE
0. 🔗 **Page de passage pour les liens d'invitation VIP de Guso Facile** — bloquée en attente de
   la réponse de la session `GUSO FACILE V4`. Adresse pressentie
   `/guso-facile/invitation#invite=<token>`. **Lire d'abord l'entrée « PIÈGE MESURÉ : une
   redirection Vercel AVALE le fragment » du journal** : une redirection ne suffit pas, il faut
   une page HTML qui relaie `location.hash` en JS. Ne pas figer l'adresse avant l'accord de
   l'autre session — une fois diffusée aux bêta-testeurs, elle ne bouge plus.
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

### 2026-08-27 (2) — NIVEAU 2 : l'agenda Google écrit le site tout seul (NON POUSSÉ)

**La demande de David** : *« est-ce que ça peut être écrit et automatisé en fonction du
Google Agenda tout seul, **sans qu'un agent ait besoin de vérifier tous les jours** ? »*
Réponse : oui, et **sans aucune IA en fonctionnement**. Code déterministe, tâche
planifiée GitHub Actions, zéro token, zéro secret, gratuit (dépôt public).

**Ce qui a été construit** (mode d'emploi complet pour David : section
« 🗓️ L'AGENDA GOOGLE MET LE SITE À JOUR TOUT SEUL » en haut de ce fichier) :

| Fichier | Rôle |
|---|---|
| `sources/synchro_agenda.py` | lit le flux `.ics` public, réécrit `EVENTS`, reconstruit, vérifie |
| `.github/workflows/agenda-du-nid.yml` | le lance chaque nuit à 03:17 UTC + bouton manuel |
| `sources/generate_rdv_mensuels.py` | ne recopie plus les dates : il les **lit** dans `EVENTS` |

**LE MÉCANISME DE LISTE BLANCHE — c'est le cœur, et c'est un choix argumenté.** Un
événement est publié si, et seulement si, **son titre exact est dans le dictionnaire
`CORRESPONDANCE`**, qui donne aussi le type, le titre affiché et la note. Trois raisons
d'avoir écarté les autres pistes :

- *deviner le type depuis le titre* → interdit par le brief, et faux dès qu'un titre
  bouge d'un mot ;
- *demander à David de préfixer ses événements* (`[SITE:concert]`) → l'agenda est
  **public** et des gens y sont abonnés : ils verraient le code technique ;
- *la couleur de l'événement, ou ses catégories* → Google ne les exporte pas dans le
  flux `.ics` public. Mesuré : les seules propriétés présentes sont `DTSTART`, `DTEND`,
  `SUMMARY`, `STATUS`, `DESCRIPTION`, `LOCATION`, `UID`, `SEQUENCE`, `TRANSP`, `CREATED`,
  `LAST-MODIFIED`, `DTSTAMP`.

Le geste demandé à David est donc le plus simple possible : **dupliquer un événement
existant** dans Google Agenda et changer la date. Le titre est alors exact par
construction.

🚨 **CE QUI VIENT DU FLUX : UNE DATE, UNE HEURE DE DÉBUT, UNE HEURE DE FIN. RIEN
D'AUTRE.** Le titre publié et sa note viennent de la table, donc d'un humain. Le lecteur
de flux **jette** `DESCRIPTION`, `LOCATION`, `UID` et tout le reste à la lecture : il ne
filtre pas ce qu'il a gardé, il ne garde pas. Prouvé après coup sur la sortie réelle :
les 19 lignes écrites ne contiennent **aucun** texte absent de la table, et ni
« portail », ni « confirmation », ni « Orteaux », ni `@`, ni `http`.

**LES GARDE-FOUS, ET CE QU'ILS ONT REFUSÉ EN ESSAI** :

| Situation simulée | Ce que le script a fait |
|---|---|
| « RDV medecin », « Anniversaire Iris » ajoutés au flux | ignorés + **signalés**, site publié quand même |
| événement « journée entière » | ignoré + signalé (pas d'horaire = pas publiable) |
| flux vide | **REFUS**, rien écrit |
| flux tronqué (3 dates sur 19) | **REFUS** — plus de la moitié disparaîtrait |
| fichier qui n'est pas un calendrier | **REFUS** |
| 18 dates ajoutées d'un coup | **REFUS** (plafond 15, à appliquer à la main) |
| concert déplacé de 19:00 à 18:00 | **REFUS** — la clé `URL_PAR_EVENT` ne mordrait plus, le bouton « Réserver » retomberait sur le lien générique |
| `build.py` / `verif_site.py` / `verif_commentaires.py` en échec | fichier **remis comme avant**, site reconstruit dans son état d'origine, code de sortie 1 → **le workflow ne commite pas** |

Cette dernière ligne a été **observée pour de vrai** pendant les essais (une simulation
au 10 septembre a fait tomber un garde-fou de `generate_rdv_mensuels.py`) : le script a
remis `generate_agenda_nid.py` en état et rebâti le site d'origine tout seul.

**POURQUOI `/rendez-vous-mensuels` A DÛ ÊTRE REPRISE EN MÊME TEMPS.** Elle recopiait les
quatre dates mensuelles et un garde-fou exigeait qu'elles soient **mot pour mot** celles
de l'agenda. Dès la première soirée passée, la génération se serait arrêtée — tous les
soirs, pour toujours. Elle **lit** maintenant ses dates dans `EVENTS` et ne garde en
propre que le **texte** de chaque soirée (`CONTENUS`, rangé par date). Conséquences :

- une soirée ajoutée à l'agenda apparaît toute seule, en « Programme en cours
  d'élaboration », avec son ancre `soiree-<date>` et son encart ;
- une soirée passée disparaît **sans que son texte soit effacé** ;
- trois garde-fous écrits en dur (« attendu 3 jauges », « attendu 2 liens de
  billetterie », les quatre ancres figées dans `verif_site.py`) comptent désormais ce
  que les soirées **réellement publiées** contiennent. C'étaient trois impasses.

⚠️ **UNE PHRASE DE LA PAGE ALLAIT MENTIR** : « Quatre rendez-vous sont posés jusqu'en
décembre. Le programme du 4 septembre est écrit… ». Ses **nombres et ses dates** sont
maintenant calculés ; **ses mots sont ceux de David**, non réécrits. Avec les données du
27/08 elle rend le texte publié **au caractère près** ; au 5 septembre elle donne
« Trois rendez-vous sont posés jusqu'en décembre. Leur programme sera annoncé ici. »

**Vérifications faites** :
- essai sur le **vrai** flux : 30 événements lus, **19 retenus**, 11 écartés sans alerte
  (10 passés + …), **0 à signaler**. Le seul changement : le 23 août, passé, disparaît ;
- application réelle : `EVENTS` passe de 20 à 19 lignes, **identiques à celles écrites à
  la main** (seul l'alignement des colonnes est normalisé) → la synchro reproduit
  exactement le travail manuel ;
- `/le-nid` : le groupe « août 2026 » part en entier (titre + liste + bouton de filtre du
  mois), 20 → 19 `.ag-item`, aucune date apparue par surprise ;
- `build.py` deux passes, `verif_site.py` **31/31 code 0**, `verif_commentaires.py`
  **31/31 code 0** ;
- scénario du 5 septembre rejoué (INSTATIC retirée d'`EVENTS`, « aujourd'hui » simulé) :
  page reconstruite, encart et jauge partis proprement, **31/31** ;
- scénario « plus aucune soirée mensuelle » : la page se réduit à
  « Prochaines dates en préparation. », **31/31** ;
- YAML du workflow relu par un analyseur, et le shell de chacun de ses pas par `bash -n`.

**CE QUI N'A PAS ÉTÉ AUTOMATISÉ, DÉLIBÉRÉMENT** :
- `/rythme-calebasse` et `/concerts-david-lesage` gardent leur petite liste de dates
  écrite à la main. Les aligner demanderait de **décider** ce que chaque page doit
  montrer (la seconde n'annonce pas la sortie de résidence en trio, par exemple) : c'est
  un arbitrage de David. Le script **le dit à chaque passage**, pour information, et
  **n'alerte jamais** là-dessus ;
- la META description de `/concerts-david-lesage` (« Prochaines dates : 10 octobre et
  28 novembre 2026 ») vieillira toujours ;
- la rédaction d'une soirée mensuelle reste humaine, par construction.

⚠️ **POUR DAVID, À TRANCHER** : l'agenda Google annonce le 28 novembre comme
« Concert de David Lesage — Le Nid **+ Guest Lucie au violon** », alors que le site écrit
« Concert — David Lesage solo ». La table reproduit **ce qui est en ligne aujourd'hui**
(on ne change pas une annonce publiée sans lui) — mais les deux se contredisent.

⚠️ **PAS POUSSÉ.** Et **rien ne tournera** tant que le workflow n'est pas sur `main` :
GitHub ne lit les tâches planifiées que sur la branche par défaut.


### 2026-08-27 — Les dates passées disparaissent toutes seules (rustine niveau 1, NON POUSSÉ)

**Le constat de David** : *« quand les dates sont dépassées, la date reste visible. Je voudrais
qu'elle disparaisse pour que seules les dates à venir restent, **sans avoir à te le demander**.
Que ce soit automatique. »* `/le-nid` affichait encore le 23 août, passé depuis quatre jours.

**La cause, mesurée** : le site est STATIQUE. Aucun filtrage n'existait — ni à la génération, ni
dans le navigateur (le seul `new Date()` de `/le-nid` servait à fabriquer le `.ics`).

🚨 **CE QUI A ÉTÉ POSÉ EST UNE RUSTINE, ET C'EST ÉCRIT EN TÊTE DU MODULE.** Le HTML livré contient
toujours TOUTES les dates ; c'est le navigateur qui masque celles qui sont finies. La page ne
gagne donc jamais de nouvelle date toute seule, elle ne fait qu'en perdre. **Le niveau 2 reste à
faire** : reconstruction automatique depuis l'agenda Google (tâche planifiée → `build.py` →
republication). Ne pas prendre ce chantier pour terminé.

**Un seul fichier porte le mécanisme : `sources/dates_a_venir.py`** (modèle `visionneuse.py` /
`retour_haut.py` — quatre générateurs l'appellent, personne ne recopie). Ce n'est PAS un
générateur : aucune ligne dans `build.py`.

**Les quatre décisions qui tiennent tout :**
1. **Une date est passée à la FIN de l'événement**, jamais à son début. INSTATIC (19h00–21h30)
   reste affichée pendant la soirée et part à 21h31. Quand la fin est inconnue (les trois soirées
   mensuelles sans horaire arrêté), on prend **la fin de la journée, heure de Paris** — on garde
   trop longtemps plutôt que de faire disparaître un événement en cours.
2. **Le fuseau est calculé en Python, pas dans le navigateur.** Chaque fin devient un INSTANT
   ABSOLU (UTC) via `_offset_paris()` (vrai changement d'heure : dernier dimanche de mars /
   d'octobre). Le navigateur ne compare que deux instants — juste depuis n'importe où. Vérifié :
   Paris, New York, Tokyo et Kiritimati donnent **le même résultat au même instant**, y compris
   quand le fuseau est déjà au lendemain.
   ⚠️ Le raccourci historique de `generate_agenda_nid.py` (`offset = 2 if (month,day) < (10,25)`)
   n'a PAS été touché : il alimente des `.ics` déjà téléchargés par des gens.
3. **Aucun clignotement** : le masquage est écrit par un script en FIN de `<head>`, donc avant la
   première peinture. Mesuré : aucune date passée n'a jamais occupé un pixel (espion sur
   30 frames). Le script de ménage, lui, ne fait que retirer du DOM ce qui est déjà invisible.
4. **Jamais un bloc vide sous son titre** : chaque liste est un BLOC ; quand tout est passé, un
   repli sobre s'affiche (« Prochaines dates en préparation. ») et ce qui n'a plus d'objet
   disparaît (légende, barre de filtres, bouton « tout ajouter à mon agenda »).

**⚠️ SUR `/le-nid`, LE MÉNAGE EST POSÉ AVANT `FILTER_JS`, ET C'EST STRUCTUREL.** Le filtre fige sa
liste de `.ag-item` quand il s'exécute : posé après, il compterait des dates finies (« Aucune date
ne correspond » ne s'afficherait plus au bon moment) et le `.ics` « toutes les dates » exporterait
des événements passés. Dans cet ordre, `ICS_JS` et `FILTER_JS` n'ont pas bougé d'une ligne.

**⚠️ LE FILET ORPHELIN, sur `/rendez-vous-mensuels`** : les quatre encarts sont séparés par des
`.divider`. Le filet est désormais attaché à l'encart qui le PRÉCÈDE et porte les mêmes attributs
de date. Les dates passées étant toujours les premières de la liste, il ne reste jamais un trait
seul. L'inverse (filet attaché à l'encart suivant) laisserait un trait sous le programme.

**⚠️ LE SÉPARATEUR ORPHELIN, sur `/le-nid`** : dans « 4 sept. · 19 sept. », le « · » est écrit
À L'INTÉRIEUR de la date qu'il précède, et la feuille générée efface celui de la première date
encore à venir.

**⚠️ NI `<span>` NI `<div>` pour porter une date dans `.offer-dates`** : la page porte
`.offer-dates span{display:block}` + une seconde règle qui les peint en dégradé doré. Un `<span>`
par date les aurait empilés en colonne, en doré. C'est `<time>` qui est utilisé — que rien ne
cible. Le séparateur est un `<i>`.

**⚠️ LES ENCARTS « PROCHAINES DATES » PORTENT MAINTENANT TOUTES LES DATES DU TYPE**, et n'en
montrent que trois (classe `.dt-plus` + fenêtre). Sinon la carte « instruments d'exception »
serait vide dès le 19 octobre alors que l'agenda en annonce encore deux. Sans JavaScript, ce sont
les trois premières écrites — la page d'avant, à l'identique.

**CE QUI N'A DÉLIBÉRÉMENT PAS ÉTÉ FILTRÉ** (et ne doit pas l'être) :
- `/david-lesage-en-concert`, `.dlc-chrono` : **112 dates de scène de 2009 à 2026**. C'est une
  chronologie du PASSÉ, et c'est elle que le contrôle `chiffres` compare au nombre annoncé.
  Vérifié à l'affichage, aujourd'hui et en 2027 : **112 annoncées = 112 rendues**.
- `/guso-facile` et les 18 articles du blog : les dates y sont des **données fictives** d'aperçu
  d'interface (« 14 mars 2026 · Le Rocher de Palmer ») et des **dates de publication**.
- `/e-motion`, `/rituals`, `/rituals-trio`, `/le-soin-soa`, `/association`, `/` : aucune date
  d'événement (vérifié par balayage des 31 pages).

**L'INVENTAIRE — 45 dates masquables sur 4 pages :**

| Page | Ce qui porte une date | Combien |
|---|---|---|
| `/le-nid` | lignes d'agenda `.ag-item` | 20 |
| `/le-nid` | encarts « Prochaines dates » (concert 3, yoga 4, rythme 3, showcase 5) | 15 |
| `/rendez-vous-mensuels` | lignes `.rdv-row` + encarts `.rdv-block` (+ leurs filets) | 4 + 4 |
| `/rythme-calebasse` | `.date` du groupe de pratique | 3 |
| `/concerts-david-lesage` | `.cdl-date` | 2 |

**Vérifications (Chrome sans interface, pilote CDP, mesures DOM — aucune capture d'écran) :**
- `build.py` deux passes → « Aucune page n'a changé » ; `verif_site.py` **31/31**, code 0 ;
  `verif_commentaires.py` **31/31**, code 0.
- **Diff du texte visible, JavaScript DÉSACTIVÉ : VIDE** sur les 4 pages (311/135/201/210 lignes,
  identiques au caractère près).
- **Simulations de « aujourd'hui »** : 27/08 (le 23 août a disparu, 20 → 19 lignes) · veille
  d'INSTATIC (visible) · **pendant** INSTATIC à 20h00 et à 21h29 (visible) · 21h31 (parti) ·
  lendemain (parti) · **15/01/2027, tout est passé** (0 ligne, repli affiché, légende + filtres +
  bouton « tout ajouter » effacés, un seul filet restant).
- Filtres de l'agenda après ménage : Tous → 19, septembre → 6, showcase+septembre → 1,
  résidence+décembre → 0 **avec** le message « Aucune date ne correspond ».
- `.ics` « toutes les dates » : 19 événements, **20260823 absent**.
- **0 débordement horizontal** à 390 / 820 / 1440 sur 6 pages × 2 « aujourd'hui ».
- Console **vide** (le seul message, `allowfullscreen`, est présent à l'identique AVANT).

**À signaler, non corrigé (hors périmètre) :**
- `dates_courtes()` écrit « 18 **octo.** », « 14 **nove.** », « 5 **déce.** » — un `[:4]` sur le
  nom du mois, **défaut d'avant ce chantier**, laissé tel quel pour ne pas mélanger deux sujets.
- `/concerts-david-lesage` : la META description dit « Prochaines dates : 10 octobre et
  28 novembre 2026 ». Elle vieillira, et aucune rustine navigateur ne peut la rattraper.
- `/rendez-vous-mensuels` : l'horaire des trois soirées reste **non tranché** (voir 20/08). Faute
  d'heure de fin, elles restent affichées jusqu'à minuit le jour J.

⚠️ **PAS POUSSÉ.**


### 2026-08-20 (3) — Les boutons grossissent sur les 31 pages, et `.btn` n'est plus écrit qu'une fois

**La demande de David**, en deux messages : « le texte du bouton "réserver ma place" est trop
petit, mets-le en gras et grossis-le », puis « et de tous les boutons en général par conséquent ».

**Ce qu'on a trouvé en ouvrant le capot, et qui était le vrai sujet.** `.btn` était écrit **onze
fois**, et les onze avaient **déjà divergé** — ce n'est pas le grossissement qui a créé l'écart :

| Échelle | Où |
|---|---|
| 15 px / 600 / `14px 26px` / r40 | accueil, `/association`, `/le-soin-soa`, `/rendez-vous-mensuels`, `/guso-facile`, les 19 pages du blog |
| 16 px / 600 / `14px 28px` / r40 / mh48 | `/concerts-david-lesage`, `/david-lesage-en-concert` |
| 16 px / 600 / `15px 26px` / r40 / mh48 | `/rythme-calebasse` |
| 16,5 px / 600 / `16px 34px` / r30 / mh44, en `inline-block` | `/e-motion` |
| 17 px / 600 / `14px 30px` / r30 / mh48 | `/le-nid` (dans `sources/lenid_source.html`) |

Le même libellé « Réserver » faisait donc **15 px sur une page et 17 px sur l'autre**. C'est
exactement la divergence que `sources/theme_chaleur.py` a été écrit pour empêcher, et elle était
invisible en lisant un seul fichier. ⚠️ La liste de onze qui circulait citait `theme_chaleur.py`
(qui ne portait qu'un `border-radius`) et **oubliait `sources/lenid_source.html`** — c'est un
fichier HTML, pas un générateur, et aucun `grep sources/*.py` ne le voit.

**Où vit la définition maintenant** : `theme_chaleur.CSS_BOUTONS`, **une seule** déclaration de
sélecteur `.btn` pour les 31 pages, plus sa variante `@media(max-width:520px)`. Les valeurs sont
dans des constantes Python (`BOUTON_TAILLE`, `BOUTON_GRAISSE`, `BOUTON_MARGE`, …) : une seule
écriture déplace les boutons du site entier.

**Deux exceptions, traitées explicitement — c'est là que ça se joue :**
- **`/guso-facile` n'importe pas `theme_chaleur.CSS`** (elle est l'origine du langage visuel et
  porte sa propre copie de la couche chaleureuse). Elle importe désormais `CSS_BOUTONS`, et lui
  seul. Sans ça elle serait restée la 31ᵉ page à l'ancienne taille, exactement comme elle avait
  été oubliée pour `.legal` le 16/08.
- **`/rituals` et `/rituals-trio` n'ont PAS un seul `class="btn"`** dans leur corps (vérifié).
  Leur unique bouton d'appel à l'action est `.dlbtn` (« Télécharger le kit presse »), défini dans
  les deux sources HTML jumelles. Il prend l'échelle via `theme_chaleur.CSS_RITUALS`, en **lisant
  les mêmes constantes**. Sans cette ligne, deux pages sur 31 seraient restées à 15 px sans que
  rien ne le signale.

**La nouvelle échelle** — celle de `.btn-resa`, validée par David en la voyant :

| Famille | Avant | Après | Pourquoi |
|---|---|---|---|
| `.btn`, `.dlbtn` (appel à l'action) | 15 → 17 px / 600 | **18 px / 700 / `17px 34px`** (17 px / `16px 26px` sous 520 px) | la demande |
| `.cdl-listen .btn`, `.dlc-listen .btn`, `.rdv-act .btn` (secondaire) | 14,5–15 px / 600 | **16 px / 700 / `13px 24px`** | trois côte à côte sous un paragraphe ; au rembourrage complet ils passent sur trois lignes dès 820 px |
| `.ag-btn`, `.ag-cal` (les 20 lignes de l'agenda) | 16 px / 500 et 400 | **17 px / 700**, rembourrage `11px 20px` / `11px 17px` | ils sont la 3ᵉ colonne d'une grille de 20 lignes : au rembourrage complet, la colonne du titre tombe sous 150 px à 390 px et chaque intitulé casse sur trois lignes |
| `.car-btn`, `.totop`, `.lb-close`, `.burger`, `.ag-f` | — | **inchangés** | ce ne sont pas des appels à l'action mais des commandes d'interface ; leur cible tactile fait déjà ≥ 44 px et leur glyphe 20 à 34 px. Grossir `.totop` aggraverait le croisement documenté avec les liens de sommaire |
| `.nav .adh` (« Adhérer » de la barre fixe) | 15 px / 600 | **inchangé — décision** | voir ci-dessous |

**`.btn-resa` est SUPPRIMÉE** (CSS et balisage). Elle portait 18 px / 700 / `17px 34px` sur les
deux boutons de billetterie ; c'est devenu l'échelle de `.btn`. Deux classes qui produisent la
même apparence, c'est le défaut que tout ce chantier corrige. **Ne pas la réintroduire « un cran
au-dessus »** : sur `/rendez-vous-mensuels` la hiérarchie passe désormais par la **couleur** et la
**place** — le bouton de réservation est le seul bouton plein (dégradé chaud) de son bloc, les
autres sont des `.ghost` à filet.

**⚠️ `.nav .adh` n'a PAS été touchée, et c'est un choix.** Trois raisons : (1) c'est un item de
barre de navigation, aligné sur ses six voisins à 15 px — la grossir seule la désaligne ;
(2) c'est une **deuxième famille de duplication**, à dix copies et **déjà divergente** elle aussi
(`padding:8px 16px` sur huit pages, `padding:0 17px` sur les deux pages concert ; point de rupture
à 1080 px partout sauf 1340 px sur `/david-lesage-en-concert`) — la traiter ici aurait mélangé
deux sujets dans un commit ; (3) la barre est **fixe et partagée par les 31 pages**, c'est le
point le plus risqué du site. **Chantier à part, à ouvrir sur le même modèle que `.btn`.**

**La seule page où le grossissement a cassé quelque chose**, et comment c'est rattrapé :
`/rendez-vous-mensuels`, bouton « S'abonner avec Google Agenda » (28 caractères). À 390 px
l'encart `.rdv-abo` laisse 288 px utiles ; à 17 px / 700 avec 26 px de rembourrage le libellé en
demande 302 et passait **sur deux lignes** (54 px de haut avant, 92 px après). Remède : `padding:
16px 18px` sous 520 px → 281 px, une seule ligne. C'est **exactement** le remède que `/le-nid`
applique déjà au même libellé (`.btn.ag-sub-btn`). ⚠️ **Sous ~380 px il passera sur deux lignes
quoi qu'on fasse** (mesure à 360 px : 258 px utiles, le texte seul en demande 245) — ce n'est pas
à corriger en rognant encore, rien ne déborde et raccourcir voudrait dire changer un texte.

**Vérifications (Chrome sans interface, pilote CDP, mesures DOM — pas de capture d'écran) :**
- `build.py` deux passes → « Aucune page n'a changé » ; `verif_site.py` **31/31**, code 0 ;
  `verif_commentaires.py` 31/31, code 0.
- **0 débordement horizontal sur 31 pages × 15 largeurs** (320, 360, 390, 480, 520, 560, 640,
  761, 800, 820, 860, 1000, 1080, 1200, 1340, 1440), soit 496 couples page × largeur.
- **0 recouvrement** : chaque bouton amené au centre de l'écran, `elementFromPoint` sur son
  centre et ses quatre coins, aux trois largeurs.
- **Diff du texte visible : vide** sur les 31 pages, aux 15 largeurs.
- Console **vide** partout.
- Libellés sur deux lignes à 390 px : quatre, et **les quatre l'étaient déjà avant** (« Commander
  l'album… » ×2, « Demander la fiche technique complète », « ↓ Ajouter toutes les dates… »).

**Compte des définitions** : sélecteur exactement `.btn` — **11 → 1** (plus sa variante mobile).

**Restent à signaler, non corrigés (hors périmètre) :**
- `.nav .adh` : 10 copies déjà divergentes (ci-dessus).
- `.btn:hover`, `.btn.ghost` et `footer a.btn` : ~9 copies chacune. Elles ne portent **ni taille
  ni graisse**, et les deux premières sont repeintes juste après par la couche chaleureuse — donc
  sans effet visible aujourd'hui. Même remède le jour où on y touchera.
- `.dlbtn` : encore défini deux fois (`rituals_source.html`, `trio_source.html`) pour tout ce qui
  n'est pas la taille.
- **`sources/home_generated.html` et `sources/lenid_final.html` sont des fossiles** : aucun
  générateur ni `build.py` ne les lit (vérifié), et ils portent encore l'ancien `.btn`. Ils
  induiront en erreur la prochaine recherche `grep`. À supprimer avec David.
- `/david-lesage-en-concert` : la pastille « retour en haut » croise **14 liens de sommaire** à
  390 px et 6 à 820 px (mesuré). **Aucun bouton** n'est concerné, et le grossissement n'a rien
  changé à ce compte — mais le défaut documenté est toujours là.

### 2026-08-20 (2) — `/rendez-vous-mensuels` : nouvelle structure, dictée par David après relecture

**La page était déjà en ligne et Iris la relisait.** David l'a rouverte et a dicté un autre
ordre, en deux temps dans la même heure. C'est le SECOND qui fait foi, et il est écrit en tête
de `sources/generate_rdv_mensuels.py` avec ses mots :

1. le chapeau, qui se termine sur « Toujours sur réservation, toujours avec des intervenants
   différents » ;
2. **UN BOUTON, et rien d'autre** — « Voir les prochaines dates », ancre vers `#programme` tout
   en bas. *« Juste un bouton »* : pas deux, pas un bouton plus une liste, pas un aperçu ;
3. **l'intention** développée — la partie qu'on vient lire ;
4. **le programme**, tout en bas : les 4 dates puis **un encart par date**.

**Le raisonnement de David, à respecter** : qui découvre doit pouvoir lire l'intention sans être
coupé par un tableau de dates ; qui vient chercher une date a un bouton immédiat pour sauter.

**Ce qui a changé au fond**
- **Chaque date a désormais SON encart** : `#instatic`, `#soiree-2026-10-02`, `#soiree-2026-11-07`,
  `#soiree-2026-12-04`. Avant, trois des quatre dates ne menaient nulle part.
- **Toute la ligne d'une date est un lien** (`a.rdv-go`) : cible de 128 à 299 px de haut. Le
  « bouton » qu'on y voit est un `<span class="btn ghost">` — un `<a>` dans un `<a>` est invalide.
- **UNE seule structure de données**, `SOIREES`, en tête du générateur, avec le mode d'emploi en
  trois lignes pour compléter une soirée plus tard (remplir `titre`, `horaire`, `prix`, `faits`,
  `recit`, `resa`… ; la présence de `titre` bascule tout seul la ligne ET l'encart en version
  complète).
- **Jauge INSTATIC 20 → 25 personnes** (David). Écrite UNE fois, dans la constante `JAUGE` ;
  `_controle_jauge()` refuse d'écrire la page si un autre chiffre apparaît devant « places » ou
  « personnes ». ⚠️ Le TARIF vaut toujours **20 €** — les deux valaient 20, un seul a changé.
- **« Être prévenu du programme » ne fait plus un e-mail** : il pointe vers **l'abonnement à
  l'agenda du Nid**, avec le même geste que `/le-nid` (bouton Google Agenda + lien Apple/Outlook).
  `CAL_SUB` et `CAL_WEBCAL` sont **relus en texte** dans `generate_agenda_nid.py`, jamais recopiés.
- **SUPPRIMÉ : la section « Ce qui se prépare »** (`#a-venir`) et ses 4 formats sans date. Entrée
  retirée de `MARQUEURS_UNIQUES` dans `verif_site.py`. ⚠️ Si ce bloc revient, la précision de
  David sur la roue du consentement revient avec : « pas de sexualité ».
- **SUPPRIMÉ : les deux photos** et, avec elles, la **visionneuse** (`visionneuse.py` n'est plus
  importé). Aucun fichier effacé dans `img/` ; `og:image` inchangée.
- **La phrase longue des soirées non programmées est remplacée** par les mots de David :
  « Programme en cours d'élaboration ».

🚨 **L'HORAIRE DES TROIS SOIRÉES RESTE NON TRANCHÉ** — l'agenda dit 18:30–23:30, INSTATIC dit
19h00–21h30. La page écrit **« À préciser »** et n'invente rien. Constante `HORAIRE_INCONNU`.

**Nouveaux garde-fous du générateur** : `_controle_ordre()` (le bouton avant l'intention, avant le
programme, avant le premier encart), `_controle_jauge()`, un lien et un seul par ancre de date,
autant de lignes cliquables que de soirées, et **zéro `<img>` dans le corps**.

**Mesuré** (DOM, pas capture) : hauteur 9 939 px (390) · 7 111 px (820) · 6 733 px (1440), contre
9 156 / 6 436 / 6 093 avant. 0 débordement horizontal aux trois largeurs. Les 5 ancres atterrissent
avec leur sur-titre **46 à 87 px sous la barre fixe**. Contrastes des composants nouveaux :
5,95:1 à 18,9:1. Aucun texte sous 13 px. Console vide, 1 seule ressource chargée (les polices).

⚠️ **PAS POUSSÉ.**


### 2026-08-20 — une 31ᵉ page : « Les RDV Mensuels au Nid » (commit `6482005`, NON poussé)

Demande de David : une page qui annonce **tous** les rendez-vous mensuels, « avec une
proposition d'activité différente à chaque fois ». Le programme est en cours d'élaboration,
les **dates existent déjà**.

**L'ordre des blocs est le sien, pas une proposition** : *« il faut que la première chose
qu'on voit ce soit les dates, le titre de l'atelier, horaire, prix et un bouton cliquable
"en savoir plus" qui en fait est une ancre »*. Donc : (1) le programme en un coup d'œil,
(2) l'intention, (3) les encarts détaillés. Ne pas « améliorer » cet ordre.

**Le slug : `/rendez-vous-mensuels`**, pas `/rdv-mensuels`. Le site écrit déjà
« Rendez-vous mensuel » en toutes lettres partout (badge de l'agenda `TYPES['mensuel']`,
tuile de la grille, les 4 événements du Google Agenda public) : `RDV` aurait introduit un
troisième vocabulaire pour la même chose. Le libellé de menu, lui, est bien
**« Les RDV Mensuels »** — les mots de David.

**Menu** : entrée dans le sous-menu « Le Nid », **juste après « Agenda »** (les deux entrées
qui parlent de dates se suivent). `NAV_VERSION` → **`resonances-5`**. Les 30 pages existantes
ne changent **que** par cette ligne : diff du texte visible = un seul ajout, « Les RDV
Mensuels », sur chacune ; 4 lignes de HTML modifiées par page (3 marqueurs de version + la
nouvelle entrée), rien d'autre.

**Ce qui a été mis au courant du passage de 30 à 31 pages** (rien n'a été désactivé) :
`verif_site.py` (`PAGES`, en-têtes, `MENU_ENTREES_ATTENDUES` **18 → 19**, marqueurs de
structure de la nouvelle page), `verif_commentaires.py` (`PAGES`), `build.py` (une ligne au
TABLEAU), `sitemap.xml`.

**Le générateur refuse d'écrire** si : une date diverge de `EVENTS` dans
`generate_agenda_nid.py` (relu **en texte**, jamais importé — ce module réécrit `/le-nid`
rien qu'en étant importé), si une ancre « En savoir plus » ne mène nulle part, s'il y a plus
de boutons « En savoir plus » que de soirées au programme connu, ou si la précision « pas de
sexualité » de la roue du consentement a disparu.

🚨 **TROIS CONTRADICTIONS NON TRANCHÉES — elles attendent David :**
1. **Horaires.** L'agenda annonce **18:30–23:30** pour les 4 dates ; le texte d'INSTATIC écrit
   par David dit **19h00–21h30**, accueil 18h45, portes fermées à 19h00. La page affiche
   l'horaire du texte de David pour INSTATIC et **aucun horaire** pour les 3 autres.
   ⚠️ Si David tranche pour 19h00–21h30, c'est `generate_agenda_nid.py` (`EVENTS`) qu'il faut
   corriger — et le Google Agenda public avec.
2. **Adhésion vs billetterie.** L'agenda dit les RDV mensuels « Réservés aux adhérents » et son
   seul bouton est « Adhérer ». INSTATIC est à **20 €** avec billetterie HelloAsso publique.
   La page ne dit rien de l'adhésion. C'est la question 11 de « EN ATTENTE DE DAVID ».
3. **Lien HelloAsso INSTATIC** : 403 aux tests automatisés = comportement habituel de HelloAsso
   face aux robots, **pas** une preuve qu'il est cassé. Publié tel quel, à cliquer une fois en
   vrai.

**Informations qui manquent** (les 3 soirées d'octobre, novembre, décembre) : titre, intervenant,
horaire, tarif, description, billetterie. Et pour les 4 formats cités sans détail (Workshop Sexto,
Concert intimiste, La roue du consentement, Scène ouverte) : **tout**. Rien n'a été inventé.

**Mesuré** : hauteur 9 137 px (390) · 6 421 px (820) · 6 079 px (1440) ; 0 débordement horizontal
aux trois largeurs ; les 4 ancres atterrissent **76 à 87 px sous la barre fixe** (`scroll-margin-top`
56/100 px, valeurs de `/guso-facile`) ; contrastes des nouveaux composants **≥ 5,95:1** ; plancher
typo 13 px respecté (deux règles étaient à 12 px, corrigées avant publication) ; console vide ;
menu mobile OK (cible 49 px, 0 débordement panneau ouvert).

**Aucun fichier ajouté dans `img/`** : les deux photos sont celles des RDV mensuels déjà publiées
sur `/le-nid` (`soiree-au-nid-*`, `soiree-mensuel-2-*`). `og:image` =
`/img/le-nid/soiree-au-nid-1400.jpg`, 1400×646 mesurés.

⚠️ **PAS POUSSÉ** : David doit valider les textes avant publication.


### 2026-08-17 — 🚨 `git push` NE SUFFIT PLUS À PUBLIER — lire avant toute mise en ligne

**La section « COMMENT ON MODIFIE LE SITE » en tête de ce fichier dit que Vercel met le site en
ligne tout seul ~40 s après le `push`. Ce n'est plus vrai depuis la nuit du 17/08.**

**Ce qui se passe réellement** : à chaque `git push`, Vercel construit bien un déploiement
(`● Ready`, `Production`) — **mais ne le rattache plus au domaine**. `vercel inspect` montre une
section `Aliases` **vide**. Le domaine reste figé sur un ancien déploiement, et le site paraît en
retard alors que tout est publié. Constaté sur plusieurs commits d'affilée : une page avait le
nouveau titre pendant qu'une autre n'avait pas les nouveaux textes.

**Contournement utilisé cette nuit** (à refaire à CHAQUE publication tant que ce n'est pas réparé) :

```
npx vercel ls rituals | grep -E "rituals-" | head -1     # le plus recent — VERIFIER L'AGE
npx vercel alias set <url-du-deploiement> www.resonancesproductions.org
```

⚠️ **Le projet Vercel du site s'appelle `rituals`** (nom historique), pas « resonances ».

🚨 **PIÈGE VÉCU, à ne pas refaire** : un `sed -n '5p'` censé attraper « la première ligne » a
désigné un déploiement **vieux de 2 h**. Le domaine a pointé ~1 min sur une version antérieure —
**le site a régressé en production**. Toujours **relire l'âge** de la ligne (`24s`, `1m`) avant
d'aliaser, et **revérifier en ligne après**, par `curl`, un contenu qu'on vient de publier.

🚨 **NE PAS lancer `npx vercel --prod` à la racine du projet** : il ne connaît pas le projet
`rituals` et **crée un projet Vercel parasite** nommé d'après le dossier (`resonances-site`),
plus un `.vercel/` local qui pointe dessus. Arrivé le 17/08 ; projet et dossier supprimés,
`.gitignore` complété. Si ça se reproduit : `npx vercel project rm <nom>` — interactif, et
**ne pas** tenter `yes |` (la commande boucle et produit des dizaines de Mo de sortie).

**À réparer au calme** : soit relier proprement le dossier au projet `rituals`
(`npx vercel link`), soit voir au tableau de bord pourquoi `main` ne promeut plus en production.
Tant que ce n'est pas fait, **une publication n'est finie que lorsque l'alias est posé ET vérifié
en ligne**.

---

### 2026-08-19 — `/le-nid` : le showroom en tête, et une couleur par activité sur les six tuiles

Demande de David : « met en premier la tuile du showroom et met des couleurs de fond différentes
sur chaque tuile pour créer de la mise en lumière de chaque activité "avec sa propre couleur"
Vibe ) integrer une petite photo serait un plus — il faut que ça reste compacte impactant et
efficace ».

**L'ordre.** La tuile « instruments » était injectée EN DERNIER, juste avant l'encart `.note` qui
suit la grille. L'ancre d'injection de `generate_agenda_nid.py` est passée de la FERMETURE de la
grille à son **OUVERTURE** (`  <div class="offers">\n`). Les cinq autres ont été réordonnées dans
`sources/lenid_source.html`, jamais dans le générateur. Aucune ancre n'a bougé : celles de
`CARTES_DATES` et `CARTES_ACTION` sont des fins de paragraphe **locales à une carte** — c'est
exactement pour ça qu'elles avaient été rendues locales.
Ordre retenu : **ligne 1 = ce à quoi on vient à une date** (instruments · concerts · yoga),
**ligne 2 = ce dans quoi on s'engage** (groupe calebasse · psychothérapie · cours individuels).

**Les couleurs viennent de `TYPES`, elles ne sont pas recopiées.** Quatre tuiles sur six ont un
type d'événement dans l'agenda de la MÊME page : la teinte est lue dans `TYPES`, donc une activité
porte la même couleur dans sa tuile et dans l'agenda (badge, filet, bouton, légende). Les deux
tuiles sans type d'agenda (psychothérapie, cours individuels) reçoivent deux teintes **neuves**,
posées dans les deux plus grands vides de la roue laissée par l'agenda — leur donner une couleur
de `TYPES` inutilisée (`mensuel`, `residence`) aurait fait relier « Psychothérapie » à
« Rendez-vous mensuel ».

🚨 **Le chapeau ne peut pas porter la teinte BRUTE.** Mesuré : `rythme` #8f7ad1 tombe à **3,75:1**
sur son propre fond — même piège que `--plum` dans `theme_chaleur.py` (« dès qu'il s'agit de TEXTE,
c'est `--plum2` »). La couleur de texte est donc **dérivée** par éclaircissement
(`_texte_lisible`) jusqu'à 5,0:1 sur le fond réel, jamais choisie à la main : si une teinte de
`TYPES` change, le texte suit tout seul.

**Fond précalculé en hexadécimal opaque, et c'est délibéré** : la teinte à 10 % sur `--card` est
calculée en Python (`--card` **lu** dans `theme_chaleur.CSS`, pas recopié). Le navigateur renvoie
alors la couleur EXACTE du fond, donc le contraste se **mesure** dans le DOM au lieu de s'estimer.
Six tuiles mesurées : minimum **4,75:1** (le libellé « PROCHAINES DATES », dégradé doré, arrêt
corail), tous les autres textes ≥ 4,90.

⚠️ **Le voile doré de `.offer--rare` disparaît, c'est voulu** : la classe reste (elle porte
`.offer-meta` / `.offer-fine`, et le garde-fou structurel la compte), mais son fond suit désormais
le système. Un doré en plus du bleu `showcase` ferait mentir le code couleur sur la tuile qui ouvre
la grille.
⚠️ `css_tuiles()` doit rester **après** `CSS_CHALEUR` dans la feuille : mêmes spécificités, c'est la
dernière règle qui gagne.

**Hauteurs : inchangées au pixel** aux trois largeurs (390 : 3 527 px · 820 : 1 936 · 1 440 :
1 530 pour `.offers`). Les deux lignes ont simplement échangé leur hauteur (665 / 846 à 1 440).
Le texte visible est **strictement le même** : le diff est une permutation, multiensemble de lignes
identique. 29 autres pages inchangées (md5).

**AUCUNE PHOTO POSÉE, et c'est un refus argumenté.** Inventaire fait : seules **yoga**
(`atelier-yoga-*`) et **calebasse** (`workshop-calebasse-*`) ont une photo dédiée et vraie.
Le showroom, la psychothérapie et les cours individuels n'ont **rien**, et les concerts n'ont que
des photos prises **ailleurs** (festivals, églises), pas au Nid. Habiller 2 tuiles sur 6 donne une
grille bancale, et poser une photo de concert sur « psychothérapie » serait mentir en image.
**Photos à demander à David** (voir le rapport de session) : une séance de découverte d'instruments
au Nid, une vue du cabinet / d'une séance de psychothérapie, un cours individuel.

---

### 2026-08-17 — `/guso-facile` raccourcie de 12,7 % sur téléphone (3 couches)

Décidé avec David : réduire le défilement **sans rien cacher de ce qui convainc**.
Commits `aace928` (sommaire) → `1199902` (repli) → `3775d58` (module retour-en-haut).

| Largeur | Avant | Après | Gain |
|---|---|---|---|
| 390 px | 25 455 px | **22 222 px** | **−12,7 %** |
| 820 px | 16 648 px | 15 450 px | −7,2 % |
| 1440 px | 15 038 px | 14 098 px | −6,3 % |

**Couche 1 — sommaire** : 5 liens vers des ancres **qui existaient déjà** (`#promesse` « Ce que
ça change », `#situations` « Pour qui », `#fonctionnalites` « Ce qu'il y a dedans », `#faq`
« Questions », `#acces` « Demander un accès »). Coût : +193 px à 390, **0 à 1440**.
⚠️ **Défaut trouvé et corrigé au passage : les ancres atterrissaient SOUS le menu fixe** (barre
de 110 px à 390 px). `scroll-margin-top` posé. Le défaut existait déjà pour « Demander un accès ».

**Couche 2 — repli de l'INVENTAIRE seulement** : les 29 puces des 4 univers, derrière « Les 7 /
8 fonctionnalités ». **Titres et sous-titres des cartes restent ouverts** — c'est là que la carte
dit ce qu'elle change. 🚨 **Règle à tenir : on replie ce qui s'inventorie, jamais ce qui
convainc.** Un titre fermé n'est presque jamais ouvert ; replier un argument, c'est le perdre.
`<details>`/`<summary>` natifs, zéro JS. La **FAQ était déjà repliée** depuis le 15/08 (d'où un
gain plus faible qu'espéré) et son **JSON-LD `FAQPage` est inchangé à l'octet**.

**Couche 3 — `sources/retour_haut.py`** : le bouton existait déjà sur `/guso-facile`, **recopié à
l'identique dans 5 générateurs**. Extrait en module partagé (modèle `visionneuse.py`), extraction
prouvée neutre (md5 identique). **7 pages ne l'ont toujours pas** : `/`, `/association`,
`/rituals`, `/rituals-trio`, `/e-motion`, `/le-nid`, le blog. Import + 3 appels, marche à suivre
écrite dans le module ; les 4 autres générateurs devront migrer avec preuve md5.

**Signalés, non corrigés** : la pastille « retour en haut » occupe la colonne 326–372 à 390 px et
**croise 15 éléments interactifs** sur leur extrémité droite (3 cartes d'article, 2 blocs blog,
6 titres de FAQ — tous antérieurs — et les 4 nouveaux titres repliables) ; **jamais** un champ du
formulaire ni le bouton d'envoi, et rien à 1440. · La **barre de menu est anormalement haute sur
téléphone** : 144 px à 320, 110 à 390, contre 75 à 1440, alors que ses éléments visibles font
44 px — c'est elle qui impose le `scroll-margin-top`. · **Sans JavaScript, le hamburger n'existe
pas** (créé par `mobile_nav.py`) : sur téléphone le menu du site devient inatteignable. Antérieur.

---

### 2026-08-17 — `/solune` et `/au-nid` supprimées, avec redirections

Sur décision de David (`c7f17df`) : invisibles (aucun lien du site n'y menait) et déjà remplacées
dans les faits. Elles ne disparaissent pas sèchement — **redirections 301** `/solune` →
`/e-motion` et `/au-nid` → `/le-nid`, pour qu'un lien externe ou un signet n'atterrisse pas sur
une erreur.
🚨 **Leurs `Disallow:` ont été RETIRÉS de `robots.txt`, et c'est volontaire** : un `Disallow`
empêche Google d'aller **constater** la redirection, donc de reporter le référencement sur la
page qui remplace. Le contrôle `plan` refuse maintenant l'écriture si l'un des trois éléments
manque (dossier encore présent / redirection absente / `Disallow` remis) — voir `SUPPRIMEES` dans
`verif_site.py`. **Il ne reste plus aucune page sans générateur.**

---

### 2026-08-17 — une seule photo du Grand Rex, sous un nom qui dit qui est dessus

**Deux jeux de fichiers contenaient la même photo** : `au-grand-rex-{480,900,1400}` et
`hero-grand-rex-{480,900,1400}` (JPEG + WebP). Confirmé avant toute suppression, sur les
**6 paires** : mêmes dimensions (480×313, 900×586, 1400×912), écart moyen 1,3 à 2,0 sur 255,
99 % des pixels sous 13, et sur une miniature 64×64 (qui efface le bruit de compression)
écart max 9/255. Explication trouvée dans le code : les deux **recettes** partaient du même
original `RITUALS_00_header.jpg`, à 100 px de plafond près (1600 vs 1500).

**Ce n'était PAS une suppression mais une fusion** : `hero-grand-rex` servait de **fond au
hero** de `/rituals` et `/rituals-trio` (règle CSS + `<link rel=preload>` du LCP), pendant que
`au-grand-rex` servait de **figure** sur ces deux pages plus `/david-lesage-en-concert`.

**Nom retenu** : `iris-chasles-et-david-lesage-au-grand-rex-paris-{480,900,1400}.{jpg,webp}`.
Un nom de fichier est lu par Google Images et par les lecteurs d'écran quand l'image ne charge
pas ; `au-grand-rex` ne disait ni qui ni où. Plus long que tout le reste du dossier (46
caractères contre 36 au maximum jusqu'ici) — **assumé, ne pas raccourcir**.

**Modifié** : `generate_site.py`, `generate_trio.py` (tables `SLUGS` + `RECETTES`, variables
`v_hero`/`u_hero` supprimées au profit de `v_rex`/`u_rex`), `generate_concert_scene.py`
(table `PHOTOS`, clé `rex`), `generate_assoc.py` (un commentaire seul — `/` ne référençait pas
l'image, vérifié : 0 `<img>` sur l'accueil, `md5` inchangé).

**Preuves** : diff du **texte visible** sur les 33 fichiers HTML = **vide** ; les 3 pages
touchées sont **identiques à l'octet** une fois le nom de fichier normalisé ; les 30 autres
fichiers ont un `md5` inchangé ; 6 URL en 200 en local (JPEG + WebP × 3 largeurs), les 6
anciennes en 404 ; 146 / 206 / 302 URL d'images déclarées par page, toutes récupérées ET
décodées (`createImageBitmap`), 0 cassée, console vide. **460,3 Ko économisés.**

⚠️ **`grand-rex-bras-leves-*` n'a pas été touchée** — c'est l'autre photo du même soir.

⚠️ **Un `grep "au-grand-rex"` renvoie forcément des résultats** : c'est un morceau du nouveau
nom. Le contrôle qui a du sens est `grep "hero-grand-rex"` → il ne reste que **5 lignes de
commentaire** (dans `generate_site.py` ×2, `generate_trio.py` ×2, `generate_assoc.py` ×1) qui
disent « ne pas re-créer ce fichier ». Aucune référence de chemin nulle part.

---

### 2026-08-17 — la visionneuse photo sur TOUT le site, et le Grand Rex sur `/e-motion`

Publié en une fois : `663c5ce` → `9f87415` (10 commits). 30/30 à chaque étape.

**1. Une visionneuse photo commune — `sources/visionneuse.py`**

Écrite d'abord pour `/e-motion`, puis **extraite en module partagé** sur le modèle de
`theme_chaleur.py`. Deux paramètres : `css(legende)` (le sélecteur de la légende à rendre
transparente au clic) et `js(selecteur)` (les photos cliquables). L'extraction a été prouvée
neutre : md5 de `e-motion/index.html` identique avant/après.

Posée ensuite **une page à la fois**, en vérifiant entre chaque (règle anti-régression du
projet — ne jamais traiter ces 7 pages d'un bloc) :

| Page | Photos | Sélecteur | Légende neutralisée |
|---|---|---|---|
| `/e-motion` | 27 | `.gal-item .gal-ph img` … | `.gal-item .c` |
| `/david-lesage-en-concert` | 34 / 50 | `.dlc-fig > picture img, .slide > picture img` | — |
| `/rituals-trio` | 38 | `.figure img, picture.aphoto img, .slide img` | `.cap2` |
| `/rituals` | 26 | idem | `.cap2` |
| `/concerts-david-lesage` | 9 / 25 | `.cdl-fig > picture img` | — |
| `/le-soin-soa` | 9 | `.soa-fig img, .who-ph img` | — |
| `/le-nid` | 6 / 7 | `.gal img` | — |
| `/rythme-calebasse` | 5 | `.hero-fig img, .fig img` | — |

⚠️ **`/rituals` et `/rituals-trio` : l'ancienne visionneuse a été SUPPRIMÉE** (`openIMG`,
`#imglb`, `#imgbig`, CSS `.imglb`, attributs `data-full`). Elle ouvrait bien une photo mais
sans navigation, sans zoom, sans piège à focus et sans rendre la position de la page. Les
générateurs refusent désormais d'écrire si l'un des morceaux retirés réapparaît (`assert`).

⚠️ **Les carrousels sont tous conservés** — ils défilent DANS la page, c'est leur rôle. Sur
`/rituals` et `/rituals-trio` (défilement automatique), la lecture se met en pause à
l'ouverture d'une photo au clavier ; au clic c'était déjà le cas via le `pointerdown` du rail.

**Écarts entre le périmètre annoncé et le réel, comptés et non devinés** : `/concerts-david-lesage`
n'a **aucun carrousel** ; sur ses 25 `<img>`, 15 sont des **vignettes de vidéo** (déjà cliquables
pour lancer la vidéo) et 1 est un logo → 9 vraies photos. Idem `/david-lesage-en-concert` :
50 `<img>` = 23 diapos + 11 grandes images + 15 vignettes vidéo + 1 logo → 34. **Règle appliquée
partout : jamais deux actions sur le même pixel.**

**Retour réel de David (ce que les agents ne pouvaient PAS vérifier)** : testé **sur ordinateur
ET sur mobile** — défilement fluide, **zoom « super utile »**, photos du Grand Rex « au top ».
⚠️ **Les captures d'écran sont inexploitables sur ce projet** (fenêtre non au premier plan →
`visibilityState: "hidden"` → images uniformément noires). Tout le reste est mesuré par le DOM.
C'est structurel : sur ce site, **le seul contrôle visuel fiable est celui de David**.

**2. Onze photos du Grand Rex sur `/e-motion`** (`16a1146`)

Section `#grand-rex` après la galerie de danse aérienne, avant « Le cœur du spectacle ».
Mention **sobre** et seule : « Grand Rex, Paris — 2 700 personnes. »
13 fichiers fournis − 1 filigrane en mosaïque plein cadre (épreuve non exploitable)
− 1 doublon = **11 publiées**. Poids ajouté **6,78 Mo** (84 fichiers, 480/900/1400/2000,
JPEG + WebP ; 3,1 Mo pour les 2000 px, qui font la netteté du zoom).

⚠️ **Le doublon** : `NadineCourt-493.jpg` **est** `img/rituals/grand-rex-bras-leves-*`, déjà en
ligne sur `/rituals`, `/rituals-trio` et `/david-lesage-en-concert`. Non republiée.

**Crédits, relevés filigrane par filigrane : 8 MAGYE D'ART (`magyedart.fr`) · 3 Nadine Court
(`kairos-photo-artisan.com`).** Rappel : son site affiche « Nadine **Tremblay** », on crédite
« Nadine **Court** », le nom signé sur l'image.

**3. Les noms sur les photos** (`9f87415`)

🚨 **RÈGLE POSÉE PAR DAVID, à appliquer partout** : on ne nomme que **David Lesage, Iris
Chasles et Arnaud Riou** — et Arnaud Riou seulement s'il est à l'image. Personne d'autre.
(Le site a déjà publié une identification erronée par le passé.)

Les descriptions reprennent **ses mots** : la respiration de la joie de 2 700 personnes guidée
par Iris · le chœur des tambours de l'**Academy de l'Act** · le public qui répond **en écho**
au ngoni · le salut **comme deux oiseaux**, dans le silence.

⚠️ **Erreur de fait corrigée** : une description disait qu'Iris « retient d'une main le
mousqueton de l'élastique ». **Faux — elle est tenue par son baudrier**, elle ne tient rien.
C'est ce texte que lisent les lecteurs d'écran et Google. Le mot « mousqueton » ne doit plus
réapparaître comme un geste de la main.

⚠️ **Le garde-fou `('2 700 personnes', 1)` est passé à `2`** dans `generate_emotion.py` — la
ligne de section **et** la description de la première photo. Il reste un compte **exact** :
une troisième occurrence = recopie accidentelle = écriture refusée.

**Correspondance des numéros** : David commente en faisant défiler la visionneuse et **numérote
avec son compteur** (1→27 sur `/e-motion`). Utile à savoir pour toute demande future : lui
envoyer une planche contact **numérotée dans l'ordre exact de la visionneuse**.

**Images trop petites pour un vrai agrandissement** (la visionneuse n'agrandit jamais au-delà
de la définition du fichier — au-delà, c'est flou) :
- 🔴 `/le-soin-soa` : les **3 portraits (Gaïa, Iris, David) ne font que 260 px** — cas le plus criant
- `/le-soin-soa` : `facade-le-nid` 600 px · `cercle-au-nid` 768 px (aussi sur `/concerts-david-lesage`)
- `/rituals`, `/rituals-trio`, `/e-motion` : `portrait-iris-chasles` **480 px** ·
  `/rituals-trio` : `portrait-julien-dub-au-saxophone` 480 px

---

### 2026-08-17 — nuit — session récupérée après une coupure réseau, 3 chantiers publiés

**Contexte de reprise.** La session « Site Résonances productions + Le Nid » (et son fork) s'est
figée après une coupure réseau : le chat de David tournait dans le vide ~40 min. Les deux
sessions étaient en réalité **à l'arrêt**, aucun agent ne tournait. Le travail n'était pas perdu :
`origin/main` == `HEAD`, arbre propre. Le rapport d'agent qui annonçait « commité, non poussé »
pour `e9b0196` et `2361779` était **périmé** — les deux étaient bien en ligne. Reprise faite en
lisant ce fichier + le code, sans avoir eu à interroger David : c'est exactement ce à quoi il sert.
Message de passage de relais envoyé à l'ancienne session pour qu'elle ne réédite rien.

**Publié** (`3c59244` → `25ff51f` → `11d9ba1`, poussés d'un coup, 30/30 vertes) :

1. **Lien de connexion des bêta-testeurs** sur `/guso-facile` (voir l'entrée suivante).
2. **Adresse renommée `/guso-facile/connexion` → `/guso-facile/app`.** Arbitré avec David.
   `/connexion` **ment dès la deuxième visite** : un bêta-testeur déjà connecté arrive sur son
   tableau de bord, pas sur un formulaire. `/mon-compte` promet une page de profil alors que
   l'app est un outil de gestion complet. `/app` reste vrai dans tous les cas, se dicte au
   téléphone, et prépare `app.<domaine>` le jour d'un vrai nom de domaine. **Le libellé lu par
   les gens n'a pas changé** (« J'ai déjà un compte → me connecter ») : seule l'adresse derrière
   est devenue neutre.
3. **Aperçu de partage d'E-Motion** — nouvelle affiche + texte de Solune. Voir plus bas.

**Décision de David sur le nom de domaine** : il n'en achète pas maintenant (l'app est en bêta
privée et ne rapporte rien). Raisonnement validé : **une page de connexion n'a aucune valeur en
référencement** — elle est même en `Disallow`. Le domaine ne servirait donc pas le SEO. C'est
l'adresse stable en 302 qui apporte la valeur, et elle est gratuite.

---

### 2026-08-17 — ⚠️ ERREUR DE MESURE CORRIGÉE : une redirection Vercel transmet BIEN le fragment

> **Cette entrée a d'abord affirmé le contraire** (« PIÈGE MESURÉ : une redirection AVALE le
> fragment »). **C'était faux, et la fausse conclusion a été transmise à David et à la session
> `GUSO FACILE V4` avant d'être rattrapée.** Le texte est conservé ici en tant que leçon de
> méthode, pas effacé.

**Ce qui est vrai, mesuré en production dans des onglets NEUFS (chargement complet) :**

| URL ouverte | URL finale | Ce que l'application affiche |
|---|---|---|
| `resonancesproductions.org/guso-facile/app#invite=TESTCLAUDE0000` | `…/index.html` (sans `#`) | **« Tu es invité·e sur Guso Facile … 🎟️ accès VIP »** |
| `guso-facile.vercel.app/index.html#invite=TESTCLAUDE0000` | `…/index.html` (sans `#`) | **le même écran d'invitation** |

**Les deux chemins fonctionnent.** Une simple redirection suffit pour les liens d'invitation.

**Les deux erreurs de méthode, à ne pas refaire sur ce projet :**

1. **L'app Guso Facile efface elle-même `#invite=…` de son URL dès qu'elle l'a lu** (bon
   comportement : le jeton ne traîne ni dans l'historique ni dans un copier-coller). La barre
   d'adresse est donc vide **dans les deux cas** — elle ne prouve rien.
   🚨 **Le seul indicateur valable est CE QUE MONTRE L'ÉCRAN**, pas l'URL.
2. Le test « de contrôle » avait été fait **depuis un onglet déjà posé sur la même page** : un
   changement de fragment dans le même document **ne recharge pas** l'application, le fragment
   restait donc visible. D'où la fausse asymétrie.
   🚨 **Comparer deux navigations, c'est les faire toutes les deux dans un onglet NEUF.**

**Ce qui a été construit puis annulé** : une page de passage en JavaScript (`ba2bc85`) qui lisait
`location.hash` et le recollait — annulée par `50e76e8`. Elle répondait à un problème inexistant,
elle ne marchait pas sans JavaScript, et elle imposait un 12ᵉ contrôle dédié. La redirection nue
est plus simple ET plus robuste.

**En place depuis `50e76e8`** (302, comme `/guso-facile/app`, mêmes raisons) :
`/guso-facile/invitation` → `https://guso-facile.vercel.app/index.html`, avec `Disallow` dans
`robots.txt`. **Adresse à donner à l'app** :
`https://www.resonancesproductions.org/guso-facile/invitation#invite=<token>`

⚠️ **Ne PAS passer le jeton en paramètre de requête (`?invite=`)** : ça marcherait aussi, mais un
paramètre part dans les journaux serveur et les en-têtes `Referer`, alors qu'un fragment n'est
jamais envoyé au serveur. Le choix du fragment est un choix de confidentialité.

**Seconde moitié du chantier, hors de ce dépôt** : c'est l'app qui fabrique le lien. Session
`GUSO FACILE V4 - 16 Aout 2026` contactée le 17/08, **puis re-contactée pour la correction**.
Elle attend confirmation de l'adresse retenue avant de changer sa chaîne de base.

---

### 2026-08-17 — E-Motion : l'aperçu de partage montre la nouvelle affiche (`25ff51f`)

David migre progressivement le spectacle de `solune.show` vers Résonances et voulait que la
vignette WhatsApp de `/e-motion` reprenne celle de Solune.

- **Image** : `img/e-motion/apercu-partage-e-motion-1400.jpg`, **1400×1980, 291 736 octets**
  (< 300 Ko, seuil pratique des messageries). Fichier **NOUVEAU et séparé** :
  `affiche-e-motion-1400.jpg` sert toujours dans le `<picture>` de la page et n'a pas bougé.
  **Pas de WebP** — WhatsApp et Facebook le gèrent mal, et le contrôle `partage` le refuse.
- **Source** : `~/Desktop/Affiche Solune/Affiche Emotion Aperçus Site 2026.jpg` (4961×7016).
  L'ancienne affiche portait `www.solune.show` imprimé en bas — signalé à David comme
  contradictoire en pleine migration ; il l'a remplacé par l'accroche.
  ⚠️ **Deux fautes avaient été relevées dans le premier export** (« Envole toi » sans trait
  d'union, « innattendu » avec deux `n`) **et corrigées par David avant publication.** Si
  l'affiche est ré-exportée un jour, revérifier cette ligne : elle est en gros, en bas.
- **Texte** : `og:title` = « E-Motion LE SPECTACLE PARTICIPATIF » (celui de Solune) ;
  `og:description` ramenée à **149 caractères** pour tenir avant la troncature des messageries,
  en gardant les mots de David dans son ordre.
- **Le logo « SOLUNE présente » reste imprimé en haut de l'affiche** — cohérent (le spectacle
  est de marque Solune, cf. `booking@solune.show`), mais à trancher avec l'avancée de la migration.
- L'aperçu reste une **affiche verticale** (ratio 0,71) là où les messageries attendent du
  paysage (~1,91:1) : elles rognent. Une déclinaison paysage réglerait le sujet.

⚠️ **Le cache des aperçus** : WhatsApp et Facebook gardent l'ancienne vignette plusieurs jours.
Tester dans une conversation **neuve**, ou forcer via le Sharing Debugger de Facebook. Un aperçu
« qui n'a pas changé » n'est pas une preuve que le site est en retard.

**`/le-nid` n'avait rien à changer** : son `og:image` est **déjà** `hero-nid-1200.jpg`, la photo
du salon qui ouvre la page (il n'y a pas d'image de fond CSS sur cette page). Demande de David du
17/08 close sans modification — si l'aperçu paraît autre, c'est le cache.

**Hors périmètre, signalé non corrigé** : `/solune/index.html` (page orpheline, hors des 30)
porte un `og:image` **hébergé sur un CDN externe** (`d1yei2z3i6k35z.cloudfront.net`). Elle
échouerait au contrôle `partage`. À traiter avec le sort de cette page.

---

### 2026-08-17 — les bêta-testeurs peuvent enfin se connecter depuis la page

**Décision de David** : ceux qui ont déjà un compte doivent avoir un accès. Sans affaiblir
l'unique appel à l'action de `/guso-facile` (« Demander un accès »), qui s'adresse aux ~95 %
de visiteurs qui n'en ont pas.

Trois choses posées, une enquête rendue :

1. **`/guso-facile/app`** — l'adresse stable, en **302**. Détail et mode d'emploi dans la
   section dédiée plus haut. Ce n'est pas du référencement, c'est **ne plus dépendre de
   `vercel.app`** : une seule ligne à changer le jour du déménagement.
2. **Un lien texte, pas un second bouton**, sous le bouton du hero : « J'ai déjà un compte →
   me connecter ». Gris (`--muted`), 14,5 px, aucune classe `btn`. **Mesuré, pas supposé** :
   cible tactile **44,00 px** exactement (la méthode `inline-flex` + `min-height` déjà retenue
   pour `.offer .who a` sur `/le-nid`), contraste **8,10:1** sur le fond réellement peint
   derrière lui (plancher AA : 4,5:1), **0 px** de débordement horizontal à 390 / 820 / 1440.
   Coût en hauteur : **50 px** à 390 et 820 px, **0 px à 1440** (au-delà de 1000 px le hero est
   en deux colonnes et c'est la jauge des 507 h, à droite, qui fixe la hauteur).
   L'« écart n° 8 » de `generate_guso.py` (un seul bouton, par décision) est **complété, pas
   supprimé** : l'argumentaire d'origine reste, la décision de David est datée à la suite.
3. **`Disallow: /guso-facile/app`** dans `robots.txt`.
4. **Enquête PWA (aucun code touché)** : `https://guso-facile.vercel.app/` **ne déclare aucun
   manifeste**. Ni `<link rel="manifest">`, ni `apple-touch-icon`, ni `theme-color`, ni
   `apple-mobile-web-app-capable`, ni service worker — le mot « manifest » n'apparaît pas une
   seule fois dans la page (1 000 794 octets relevés). Les six fichiers habituels répondent
   **404** (`manifest.json`, `manifest.webmanifest`, `site.webmanifest`, `sw.js`,
   `service-worker.js`, `apple-touch-icon.png`). Tout le `<head>` tient en : `charset`,
   `viewport`, `<title>`, `favicon.svg`, `description`, `robots noindex,follow`, les balises
   Open Graph / Twitter, et deux `<script src>` externes (pdf.js sur cdnjs, supabase-js sur
   jsdelivr). **L'app n'est donc pas installable en tant qu'application** : « Ajouter à l'écran
   d'accueil » ne créerait qu'un raccourci qui rouvre le navigateur, sans icône propre ni
   affichage plein écran. Il n'y a **pas** de mode d'emploi à envoyer aux bêta-testeurs pour
   l'instant. ⚠️ Guso Facile est un **autre dépôt** : rien n'a été modifié, et le chantier
   (manifeste + icônes + `theme-color`) est à mener **là-bas**, pas ici.

### 2026-08-17 — `/guso-facile` : les trois dernières « (à venir) » tombent

L'inventaire fourni la veille par la session qui développe l'app était **en retard sur son
propre travail** : les trois fonctionnalités encore annoncées « (à venir) » étaient déjà
déployées. Vérification refaite ici dans le **bundle servi** par
`https://guso-facile.vercel.app/index.html` (956 Ko), pas sur parole : `affSetVisibility` ×2,
« Tout partager » ×13, `Partenaire` ×5, `Minimal` ×9, `sdCardHtml` ×3, `affSetManage` ×2, et
`visibility:'full'` — le niveau de partage est une **donnée**, pas un simple affichage.

**Ce qui passe au présent** (tout dans `sources/generate_guso.py`) :

| Passage | Avant | Après |
|---|---|---|
| Sous-titre univers 4 | « …à plusieurs. Deux points y sont encore en construction, marqués « à venir ». » | « Parce qu'on avance mieux à plusieurs. » |
| Points de vigilance | `<li class="soon">` + `(à venir)` — « qui approche du seuil… » | au présent : heures sur la période, jours restants, rythme nécessaire, niveau d'alerte, **trié par urgence** |
| Confidentialité graduée | `<li class="soon">` + `(à venir)` — « chaque artiste choisit exactement… » | au présent, avec **le filtrage côté serveur** : la structure **ne reçoit pas** les données qu'elle n'a pas le droit de voir |
| Aperçu « Mes artistes » | note `.gf-soon-note` sous la maquette | note retirée, maquette inchangée |

⚠️ **« côté serveur » n'est pas un détail technique** : c'est ce qui distingue une vraie
confidentialité d'un masquage d'affichage. Une ancre dédiée dans `ANCRES` interdit de la
raccourcir au prochain ménage de longueur.

**`NB_A_VENIR` : 3 → 0, mécanisme intact.** Le nombre, les deux ancres qui en découlent, le CSS
de la pastille creuse (`.u-card li.soon::before`) et l'argument `note=` de `_figure()` sont tous
**conservés** : à zéro ils interdisent qu'un « (à venir) » revienne par prudence réflexe sans
motif écrit. ⚠️ **Une garde était cassée** : `NB_PUCES_A_VENIR = NB_A_VENIR - 1` donnait **-1**,
donc une ancre impossible à satisfaire. La soustraction porte maintenant un nom
(`NB_NOTES_A_VENIR`).

🚩 **Ce qui reste volontairement non fait, et dont la page ne parle pas** : l'écran permettant à
une **structure de saisir une date dans l'espace d'un artiste**. Le droit existe en base,
l'artiste peut le donner, **l'interface non** — c'est le geste le plus délicat de l'app (écrire
chez quelqu'un d'autre) et **David doit l'arbitrer**. La page n'en parle ni au présent ni au
futur, et **on ne l'ajoute pas**. Idem pour le **journal des modifications** et l'**annuaire des
structures**, en construction. (À ne pas confondre avec « Nouveautés », le journal des
nouveautés de l'app, lui livré et illustré par la maquette 10.)

🚩 **À arbitrer par David** : « Niveaux de partage » (univers 3) et « Confidentialité graduée »
(univers 4) décrivent désormais **la même fonctionnalité**, vue des deux bouts. Elles étaient
tenues séparées parce que l'une était livrée et l'autre pas ; ce motif a disparu. La seconde le
dit explicitement (« le réglage des niveaux de partage ») au lieu de rejouer la même phrase, et
apporte la garantie côté serveur — **leur fusion en une seule puce se défend.**

**Mesuré** : générateur lancé 2× → **diff nul** · `verif_site.py` **30/30, code 0** ·
`verif_commentaires.py` 30/30, code 0 · `build.py` → 30 pages, **les 12 entrées « inchangée »**,
aucune « MISE À JOUR » · **0 mention « (à venir) » sur tout le site** (le seul « à venir »
restant est « factures à venir » de l'univers 1 — une échéance, pas un marqueur) · 0
`li.soon`, 0 `.gf-soon-note` dans la page · **0 débordement à 390 / 820 / 1440** (mesuré en
iframe de largeur imposée, transitions neutralisées) · 10 aperçus, 10 mentions « données
fictives », **0 focusable** dedans · formulaire intact (4 champs obligatoires + 3 de structure
repliés, valeurs `artiste`/`structure`/`les_deux`), **0 requête vers supabase au chargement**
(1 seule requête : la feuille de polices) · 0 lien mort · badge « Bêta privée », « créé par…
relayé par », « le relaie », « n'est pas un service de l'association », « Trois situations
typiques », « Les prénoms sont fictifs », « On veille les uns sur les autres » + sa note :
**tous présents** · « porté par » et « en temps réel » : **absents** · **0 des 8 mots proscrits**
dans le bloc Guilde · Jost 700 · hauteur +2 px à 1440, +80 px à 390.
**Gardes testées en les cassant** : `NB_A_VENIR` remis à 1 → écriture refusée, page inchangée ;
`class="soon"` remis sur une puce → écriture refusée, page inchangée.

### 2026-08-16 — nuit — le site passe de 10 à 30 pages

**Ce qui est en ligne et vérifié** (chaque étape poussée et contrôlée en production) :

- **`/association`** créée : l'objet, les valeurs, les statuts, les mentions légales (RNA, SIRET,
  code APE), les deux adresses, la fiche data.gouv, l'adhésion, le contact. Elle **supprime le
  doublon de menu** signalé par David (« Accueil » et « L'association » menaient tous deux à `/`).
  Redirections posées : `/statuts`, `/mentions-legales`, `/l-association`.
- **`/guso-facile`** : fusion de la page Vercel (le parcours d'inscription ne traverse plus deux
  domaines), **formulaire de demande d'accès rapatrié** (envoi direct, 3 options `artiste` /
  `structure` / `les_deux`, aucune requête avant le clic), **10 aperçus d'interface** en HTML/CSS,
  dont une **carte de tournée en SVG**, la double vue artistes/structures, « J'ai besoin d'aide ».
- **`/guso-facile/blog`** : 18 articles + index, **encadré « Où vérifier » sur les 18** et
  **7 réserves** « Point à vérifier auprès de… » — décision de David : *l'association ne prend pas
  la responsabilité d'affirmer une vérité non vérifiable, mais on peut en parler*.
- **Refonte graphique des 30 pages** : écart fond → carte **×2,36 → ×3,30**, saturation des accents
  **44 % → 52 %**. `/guso-facile` et son blog passent en **Jost 700 resserré** (les 28 autres gardent
  Cormorant) : une page produit a sa voix propre.
- **4 liens entrants** vers Guso Facile et le blog depuis `/`, `/association` et la page
  programmateurs. Il n'y en avait **aucun** hors menu.
- **Vérification Google Search Console** posée sur l'accueil (balise unique, un contrôle l'exige).

**Deux défauts de fond corrigés, à ne pas laisser revenir** :

1. **Notes de travail livrées au public.** Le garde-fou ne regardait que les commentaires **HTML** ;
   **1 408 commentaires CSS / 153 000 caractères** passaient par l'autre porte, emoji compris.
   `verif_commentaires.py` **couvre désormais les deux**. 5 marqueurs CSS sont **fonctionnels**
   (bornes relues par `nav_menu._strip()`, `find()` de `generate_site.py`/`generate_trio.py`,
   compteurs de `generate_agenda_nid.py` et `generate_trio.py`) : les supprimer casserait
   4 générateurs **en silence**.
2. **272 fichiers `Icon\r` de Google Drive dans `.git/`** (jusque dans `refs/` et `objects/`),
   `git log --all` en échec. Nettoyés. ⚠️ **Drive synchronise `~/CLAUDE` : ça reviendra.**
   Exclure `.git` de la synchronisation réglerait la cause.

**Règles de rédaction acquises cette nuit — chacune a coûté une correction** :

- **« créé par David Lesage · relayé par l'association »**, jamais « porté par » : l'infrastructure de
  Guso Facile est personnelle, les données traitées sensibles. Un portage associatif demanderait une
  décision actée. David : *« tout est ouvert, ce n'est pas le moment de décider »*.
- **Ce qui est livré s'écrit au présent, ce qui ne l'est pas porte « (à venir) »** — vérifié auprès de
  la session qui développe l'app, dans les deux sens (2 mentions étaient fausses par excès de
  prudence, 1 manquait).
- **« Trois situations typiques »**, jamais « réelles » : les personnages sont fictifs.
- **Bloc Guilde** : 8 mots proscrits (noter, notation, signaler, dénoncer, avis, évaluation,
  blacklist, réputation) **et** vocabulaire d'abondance interdit (centaines, milliers, « consulter
  les retours ») — l'espace est **livré mais vide**.
- **Jamais « en temps réel »** : vérifié dans le code, la synchronisation ne l'est pas.

**Leçon de méthode.** Trois défauts n'ont été trouvés qu'**en regardant l'écran**, aucun compteur ne
les voyait : une carte dont les traits ne reliaient pas les points, un dégradé posé en aplat plein
sur du texte, une étiquette collée à la date suivante. *Un DOM correct et une page juste ne sont pas
la même chose.*

**En attente de David** : les légendes des blocs photo **yoga** et **calebasse** de `/le-nid`
(proposées depuis le 04/08) · le **directeur de la publication** et l'**hébergeur** pour
`/association` · la **redirection** de `guso-facile.vercel.app/presentation.html` vers `/guso-facile`
(tout est prêt des deux côtés) · l'appel au **GUSO** sur l'articulation DPAE (remplacerait 3 réserves
par une phrase ferme) · 3 dates de son parcours (Roquefort-les-Cascades 29/07/2019, La maison de
Tonino 15/09/2019, Live inédit 01/07/2020).

- **2026-08-16** — **Refonte graphique : les surfaces s'étagent, les accents s'affirment.**
  Point de départ : David compare `/guso-facile` à `~/CLAUDE/GUSO FACILE/presentation.html`
  et trouve notre page « encore un peu trop sombre ». **Mesuré avant de toucher :
  le diagnostic spontané était faux.** Les deux fonds sont quasi identiques
  (`#0f1419` chez eux, `#0e0f24` chez nous). Ce qui diffère, c'est *(a)* l'écart
  de luminance fond → carte (×3,30 chez eux, **×2,36** chez nous : nos plans
  s'aplatissaient) et *(b)* la saturation HSV des accents (58 % contre **44 %**).
  - **Palette, dans `sources/theme_chaleur.py` (une écriture, 30 pages)** —
    `--night` inchangé ; `--night2` `#141633`→`#161839` (×1,71→**×1,99**) ;
    `--card` `#191b3d`→`#1e214a` (×2,36→**×3,30**). Accents : `--gold2`
    `#f0d18a`→`#f8d274`, `--plum` `#8f7ad1`→`#9374e2`, `--plum2`
    `#b3a2e4`→`#b38ff5`, `--coral` `#e08a72`→`#ee8062` (moyenne 44,1 %→**52,1 %**).
    **`--gold` NON touché** : accent primaire déjà à 58,3 %, et sa forme
    translucide `rgba(216,178,90,…)` compte **133 littéraux** + `--line`.
    ⚠️ La couche est concaténée EN FIN de feuille : elle **redéfinit** `--night2`,
    `--card`, `--gold2` et `--plum` par-dessus le `:root` de chaque générateur.
    `/guso-facile` n'importe PAS ce module (elle est l'origine du langage visuel)
    → **la même palette y est recopiée à l'identique**, à garder synchronisée.
    Les **116 littéraux `rgba()`** des 4 accents modifiés ont été resynchronisés.
  - ⚠️ **On ne monte pas au-delà de ~42 % sur `--plum2`** : au-delà elle devient un
    violet fluo (`#aa8cff`, testé). « Premium » a primé sur l'arrondi à 55 %.
  - 🚩 **L'agenda de `/le-nid` ne suit PAS le nouvel étagement, et c'est voulu.**
    `--c` est la couleur de **texte** des 20 boutons de billetterie ; les six
    teintes sont calibrées sur l'ancien fond. `.ag-item` est **réépinglé à
    `#191b3d`**. Si `--card` rebouge un jour, **cette ligne ne suit pas toute seule**.
  - **Trois contrastes en panne trouvés en MESURANT LE RENDU** (contrastes réels
    calculés par le navigateur sur les 30 pages, alphas composés), **tous
    antérieurs** à la refonte : `/guso-facile` `.legal` **3,80:1** (seule page où
    le correctif du 15/08 n'était jamais arrivé — elle n'importe pas
    `theme_chaleur`) → `#8b8ba6` ; `/rythme-calebasse` légende de `.fig.on-white`
    **2,10:1** (gris clair sur blanc cassé) → `#4a4760` ; `/le-nid` les 20 boutons
    `.ag-btn` **4,07:1** (leur `rgba(255,255,255,.05)` éclaircissait le fond sous
    le texte coloré) → fond `rgba(0,0,0,.14)`, les six types repassent le seuil.
  - **Formulaire `/guso-facile` : 3ᵉ option « Les deux »**, valeur **exactement
    `les_deux`** (les seules valeurs acceptées sont `artiste`·`structure`·`les_deux`).
    ⚠️ **Rien n'affirme que l'app gère la double casquette** : codée, pas déployée.
  - **Sur-titres** : le rythme en trois temps a été cherché **sans présumer du nom
    de la classe** — `/rythme-calebasse` porte les siens en `.h-min`, pas `.kick`.
    Résultat : il était **déjà en place partout** sauf sur les 3 blocs photo de
    `/le-nid`, qui ont reçu « Une fois par mois », « Corps & souffle »,
    « Transmission ». Les 111 `<h2>` des 18 articles sont des **intertitres de
    prose**, pas des titres de section : volontairement laissés nus.
  - ⚠️ **Piège rencontré** : `generate_guso_blog.py` figeait `--coral:#e08a72` et
    `--plum2:#b3a2e4` **en dur** dans un garde-fou → les 19 pages du blog refusées
    à l'écriture. Même piège que `NAV_VERSION`. Il **lit** maintenant la valeur
    dans `theme_chaleur.CSS`. **Ne jamais figer une valeur dans un garde-fou.**
  - ⚠️ **Piège rencontré** : des notes écrites en **commentaires CSS** partent dans
    la page (3 `⚠️` livrés). Les notes vont en **commentaires Python**. Compte de
    symboles des 30 pages revenu à **39**, identique à avant le chantier.
  - **Mesuré** : `build.py` 30 pages, 2 passes sans un octet d'écart ·
    `verif_site.py` **30/30** code 0 · `verif_commentaires.py` 30/30 · **0
    débordement à 390/820/1440** sur les 30 · 1 `<h1>`, 1 menu, 0 image cassée ·
    hamburger ouvre ET referme · carrousels **20 et 31 diapos, mini 307 px**,
    3 `eager` · **0 paire de contraste sous son seuil**, la plus basse 4,64:1 ·
    **texte des 30 pages identique** hors les 3 sur-titres et la 3ᵉ option.
  - 🔴 **EN ATTENTE DE DAVID** : les blocs photo **yoga** et **calebasse** de
    `/le-nid` n'ont toujours pas de légende (donc pas de 3ᵉ temps). Les deux textes
    proposés sont au point 8 de « EN ATTENTE » ci-dessus depuis le 04/08 — **un mot
    de David suffit à les poser.**
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

---

## 30/08/2026 — Page CACHÉE du duo David Lesage & Lucie (session dédiée)

> Écrit par une **session Claude séparée**, ouverte exprès par David pour ce seul sujet, afin de ne pas
> mélanger ce contexte avec le reste du site. Rien du site existant n'a été modifié : `verif_site.py`
> reste à **31/31 pages conformes**, et les 31 pages publiées n'ont pas été touchées.

**Ce que c'est.** Une page de communication professionnelle destinée aux agences parisiennes et
internationales, pour le duo en émergence **David Lesage + Lucie** (violoniste électrique). Bilingue
FR/EN sur une seule adresse. Elle contient les 5 morceaux enregistrés le 28/08/2026 dans un lecteur
audio, 11 photos du shooting du même jour, les deux biographies et le contact.

**Adresse** (choisie par David, sensible à la casse sur Vercel) :
`https://www.resonancesproductions.org/David-Lesage-Lucie-Electric-Violoniste`

**Elle est VOLONTAIREMENT invisible. Quatre verrous, il faut les quatre :**

| | Verrou | Où |
|---|---|---|
| 1 | Aucune entrée de menu — le générateur n'appelle NI `nav_menu.py` NI `mobile_nav.py` | `sources/generate_duo_lucie.py` |
| 2 | Absente de `sitemap.xml` **et** de `verif_site.PAGES` — donc invisible au contrôle, qui ne regarde que les 31 pages publiées | — |
| 3 | `Disallow:` dans `robots.txt` **et** `<meta name="robots" content="noindex, nofollow, noarchive, noimageindex">` dans la page. Les deux : robots.txt empêche l'exploration, pas l'indexation d'une adresse apprise ailleurs | `robots.txt` |
| 4 | Inscrite dans `HORS_SITE` de `sources/build.py` — `build.py` ne la reconstruit pas, ne la sauvegarde pas, et ne la signale plus comme « générateur non inscrit » | `sources/build.py` |

⚠️ **Le contrôle de `verif_site.py` accepte ce `Disallow`** : il ne refuse un `Disallow` que sur une page
présente dans `PAGES`. C'est l'inverse exact du cas `/solune` documenté plus haut dans ce fichier (une
page **supprimée** qui redirige ne doit surtout PAS être en `Disallow`, sinon Google ne voit jamais le 301).
Ici il n'y a rien à rediriger : la page existe et ne doit simplement pas être trouvée.

**Comment on la reconstruit** (elle n'est PAS dans `build.py`) :

```bash
python3 sources/generate_duo_lucie.py
```

**Fichiers ajoutés / touchés** — et rien d'autre :
- `sources/generate_duo_lucie.py` *(nouveau)*
- `David-Lesage-Lucie-Electric-Violoniste/index.html` + `media/photos/` (11 JPEG) + `media/audio/` (5 MP3) *(nouveau, ~41 Mo)*
- `robots.txt` : un `Disallow` ajouté, commenté
- `sources/build.py` : **une entrée** ajoutée dans `HORS_SITE`

**Les médias.** Sources dans le Drive partagé `1 - Lucie & David / Captation Vidéo Audio /
CAPTATION 28 AOUT 2026 - PARIS`. Les MP3 du dépôt sont des **ré-encodages web** (LAME VBR `-q:a 5`,
7 à 9,6 Mo pièce) des masters : le crochet `pre-commit` refuse tout fichier non-image de plus de 10 Mo,
et les masters d'origine (jusqu'à 18 Mo) ne passaient pas. **Les masters restent sur le Drive** — on ne
les remplace pas par ceux du dépôt. Mix retenu : « sortie de table + micro d'ambiance Hisong » partout
où il existe (choix de David) ; *Ave Maria* n'existe qu'en sortie de table.

**Ce qui a été écarté volontairement, et pourquoi — à ne pas « corriger » sans demander :**
- **Le nom de famille de Lucie n'est PAS écrit.** Il n'apparaît nulle part dans le corps visible de ses
  sites (seulement dans des métadonnées), et elle se présente commercialement sous son seul prénom.
  À confirmer avec elle avant de l'ajouter.
- **L'année de fondation du Quatuor Les Muses n'est pas donnée** : son site dit 2007, la page Yamaha 2010.
- Tous les faits de parcours des deux musiciens viennent de leurs **propres sites publiés**. Rien n'a été
  inventé ni arrondi. Le duo **n'a pas de nom** : la page dit « David Lesage & Lucie ».

**Reste à faire / en attente :**
- ⏳ **Montage vidéo** de la captation du 28/08 : la page annonce « montage en cours, rushes sur demande ».
  Quand la vidéo existera, elle a sa place dans la section « Écouter ».
- ⏳ Un **nom de duo**, s'il en naît un : il faudra reprendre le titre du hero, le `<title>` et l'Open Graph.
- ⚠️ **Le dépôt GitHub est PUBLIC.** La page est introuvable sur le site, mais ses photos et ses MP3 sont
  lisibles par n'importe qui sur `github.com/David-Lesage/rituals`, et l'historique git les garde même
  après suppression. Point signalé à David le 30/08.

### 30/08/2026, même jour — deuxième passe, sur retours de David

Retours arrivés après la mise en ligne, tous appliqués :

- **Ni téléphone ni adresse postale** sur la page. Elle circule chez des tiers : le courriel suffit à
  une agence. Remplacés par « Paris — disponibles à l'international ». **Ne pas les remettre.**
- **Portrait de David** : son portrait officiel (`img/rituals/david-lesage-900.webp`, recopié dans
  `media/photos/david.webp`) à la place d'une photo du shooting où le duo apparaissait. Les deux cartes
  sont passées en format carré, avec `object-position:50% 26%` pour ne pas couper les visages.
- **Portrait de Lucie** : recadrage de `AQ1B0102.JPG` (`crop=1720:2700:1900:400` avec ffmpeg — sips
  recadre depuis le CENTRE, ce qui rend ses offsets inutilisables ici). L'ancienne photo ne lui allait pas.
- **« 112 dates de scène » retiré** — David : « 112 dates c'est peu ». Remplacé par les **sept pays** nommés.
- **Nouvelle section « Références »**, deux colonnes SÉPARÉES : les scènes de David à gauche, les marques
  de Lucie à droite. ⚠️ Ne jamais fusionner les deux listes : ce serait attribuer à l'un ce que l'autre a
  fait. Les 28 marques sont celles que **Lucie publie elle-même** sur violonisteelectrique.com (Chanel,
  Dior, Louis Vuitton, Patek Philippe, Google, Airbus…). Des **noms en texte, jamais de logos** (marques
  déposées), et rien de cliquable : ce sont des références, pas des partenariats à suggérer.
- **Mini-bios réécrites** pour montrer les domaines d'excellence de chacun (« Ses trois terrains »).
- **Instrumentarium** : `wavedrum` remplacé par l'**Erae 2**, le multipad lumineux d'Embodme ;
  **2 Neotone et 2 Yishama** (et non « deux à trois ») ; **anglais ajouté** aux langues chantées.
- **Handpan électronique mis en avant** comme argument de tournée (toutes les gammes dans un instrument,
  tient en soute, sortie directe console) **sans fermer la porte à l'acoustique** : les Yishama restent
  annoncés « quand la salle et le format s'y prêtent ».
- **432 Hz présenté comme une couleur, pas un dogme** : la page dit explicitement que le duo se joue
  aussi en 440.
