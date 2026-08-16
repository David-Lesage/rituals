# -*- coding: utf-8 -*-
"""Generateur de la page /guso-facile (Resonances Productions).

Ecrit `guso-facile/index.html`. Aucune image, aucune ressource tierce
supplementaire, aucun script externe.

------------------------------------------------------------------------------
D'OU VIENT LE TEXTE
------------------------------------------------------------------------------
Le contenu redactionnel a ete redige et valide ailleurs :

    /Users/davidlesage/CLAUDE/GUSO-FACILE-BACKUPS/contenu-page-resonances.md
    (8 sections, fourni par la session qui developpe Guso Facile — LECTURE SEULE,
     ne jamais l'editer depuis ici)

Ce generateur MET EN FORME ce texte, il ne le reecrit pas. Les seules
modifications apportees sont listees ci-dessous, chacune avec sa raison.

------------------------------------------------------------------------------
⚠️⚠️ LE POINT LE PLUS SENSIBLE DE CETTE PAGE : LE LIEN OUTIL <-> ASSOCIATION
------------------------------------------------------------------------------
La formulation qui relie Guso Facile a Resonances Productions est
VOLONTAIREMENT PRUDENTE. Ne pas la « corriger » en « porte par l'association »
ou « projet de l'association » sans savoir ce que cela engage.

Les faits, au 14/08/2026 :
  - l'infrastructure de Guso Facile est ENTIEREMENT PERSONNELLE : projet
    Supabase et projet Vercel sur les comptes propres de David Lesage, depot git
    prive a son nom, envoi d'e-mails via son Workspace contact@lesagedavid.fr ;
  - les donnees traitees sont SENSIBLES : numeros de securite sociale, IBAN,
    salaires, feuillets GUSO de personnes reelles ;
  - le modele payant + affiliation envisage est, en l'etat, hors du champ
    associatif.

Conclusion : aujourd'hui Guso Facile est un PROJET PERSONNEL de David Lesage,
que l'association RELAIE. Un portage associatif demanderait une decision
explicite, probablement actee en proces-verbal.

Ecrire « porte par Resonances Productions » sur le site public d'une
association, a propos d'un outil qui traite des numeros de securite sociale et
des IBAN, serait une approximation au pire endroit possible. Les mots retenus
sont donc : « cree par », « relaie », « n'est pas un service de l'association ».

------------------------------------------------------------------------------
LES ECARTS AU CONTENU FOURNI (liste exhaustive, pour arbitrage par David)
------------------------------------------------------------------------------
1. Kicker. Fourni : « Un outil de Resonances Productions ».
   Ecrit    : « Cree par David Lesage · relaye par l'association ».
   Raison   : voir ci-dessus. « Un outil de » = revendication de propriete.

2. Meta description. Fourni : « Guso Facile : l'outil de Resonances Productions
   qui allege… ». Ecrit : « …un outil cree par David Lesage, relaye par
   Resonances Productions, qui allege… ». Meme raison.

3. Titre de la section 3. Fourni : « Pourquoi Resonances Productions ».
   Ecrit : « Pourquoi Resonances Productions le relaie ». Meme raison.

4. Section 3, phrase d'ouverture AJOUTEE (mot pour mot celle validee) :
   « Guso Facile est un outil cree par David Lesage, musicien intermittent et
   co-fondateur de l'association. Resonances Productions le relaie parce qu'il
   sert directement son objet : le soutien aux artistes. »

5. Section 3, fin du paragraphe. Fourni : « Guso Facile est ne de ce constat, et
   en est le prolongement direct. L'outil est mis gratuitement a disposition des
   artistes accompagnes par l'association, et son developpement continue de se
   nourrir de leurs retours. »
   Ecrit : « Guso Facile est ne de ce constat, et son developpement continue de
   se nourrir des retours des artistes qui l'utilisent. »
   Raison : « prolongement direct » (de l'association) et « mis a disposition
   par l'association » sont deux affirmations de portage associatif.

6. Section 3, encadre AJOUTE : « Precision : Guso Facile n'est pas un service de
   l'association. L'outil, son hebergement et les donnees qu'il traite relevent
   de son createur. » — a supprimer d'un mot si David le juge inutile ; il rend
   la page coherente avec la mention sous le bouton.

7. Badge « Beta privee · places limitees » : le contenu le placait dans la
   section 6. Il est REMONTE DANS LE HERO (et n'apparait qu'une fois) parce que
   l'acces limite doit se voir sans avoir a faire defiler : un visiteur ne doit
   jamais croire qu'il peut s'inscrire immediatement. La section 6 garde son
   encadre a filet or et sa phrase explicite.

8. Le bouton d'action n'existe qu'UNE fois, dans la section « Manifester son
   interet ». Le hero renvoie vers cette section par une ancre interne (#acces).
   Aucun mot du contenu n'est change ; c'est une decision de mise en page,
   coherente avec « on commence par se dire bonjour ».

Rien d'autre n'a bouge : ni un chiffre, ni un fait, ni le niveau d'engagement
des formulations sur la beta, le futur payant et l'affiliation — c'est
delibere, ces trois sujets sont prudents par construction.

------------------------------------------------------------------------------
MISE A JOUR DU 14/08/2026 (soir) — 4 titres corriges, 3 blocs ajoutes
------------------------------------------------------------------------------
Apport de la session qui developpe Guso Facile. Regle qui a guide chaque
formulation : CE QUI EST LIVRE S'ECRIT AU PRESENT, CE QUI NE L'EST PAS S'ECRIT
AU FUTUR ET PORTE « (a venir) ». Un beta-testeur verifie en trois clics.

a) Les 4 univers portaient des intitules APPROCHANTS. Les vrais, releves dans
   le code de l'application, sont desormais ecrits mot pour mot, VIRGULE
   COMPRISE (c'est elle qui donne le rythme) :
       « Suivi des droits »          -> « Tes droits, maitrises »
       « Organisation de tournee »   -> « Ta tournee, organisee »
       « Espace structure »          -> « Ta structure, connectee »
       « Entraide entre artistes »   -> « Ton cercle, solidaire »
   SEULS les titres ont bouge ; le contenu des cartes est inchange.

b) « Faire decouvrir l'outil » (cooptation) — fonctionnalite LIVREE, ajoutee
   dans l'univers 4, AU PRESENT, sans mention « a venir ».

c) « L'entraide entre artistes » (la Guilde) — fonctionnalite NON LIVREE (la
   base existe, l'ecran non), ajoutee dans l'univers 4, AU FUTUR et marquee
   « (a venir) ». ⚠️ Bloc le plus sensible de la page apres celui du lien avec
   l'association : voir la CONTRAINTE REDACTIONNELLE STRICTE ecrite juste
   au-dessus de lui dans le gabarit, et le garde-fou `_controle_guilde()`.
   ⚠️ PERIME LE 16/08/2026 : l'ecran existe et est deploye — le bloc est passe
   au PRESENT. La contrainte de vocabulaire, elle, n'a pas bouge d'un mot.
   Voir « LA REMISE A NIVEAU DU 16/08/2026 » plus bas.

d) « Je cree mon contrat » — fonctionnalite NON LIVREE (le modele en 12
   rubriques existe en base, l'ecran non), ajoutee dans l'univers 2, AU FUTUR
   et marquee « (a venir) ».
   ⚠️ PERIME LE 16/08/2026 : l'ecran existe, la puce est passee au PRESENT.

e) « Points de vigilance cote structure » et « Confidentialite graduee »
   etaient DEJA presents et DEJA marques « (a venir) » : rien a faire.
   (Toujours vrai au 16/08/2026 : ce sont deux des trois « a venir » restants.)

Le reste de la page n'a pas ete touche — en particulier « cree par David
Lesage · relaye par l'association », « Pourquoi Resonances Productions le
relaie », l'encadre « n'est pas un service de l'association », le titre
« Trois situations typiques » et sa note sur les prenoms fictifs, le badge
« Beta privee · places limitees » du hero, le bouton unique et les deux
mentions sur les donnees personnelles.

------------------------------------------------------------------------------
LE RACCORDEMENT AU SITE (fait le 14/08/2026)
------------------------------------------------------------------------------
La page n'est plus isolee. Ce qui a ete pose, et ou :
  - `sources/nav_menu.py` : entree « Guso Facile » dans un sous-menu
    « L’association » devenu deroulant (le pourquoi de ce placement est
    documente dans ce fichier-la), cle `guso-facile`, NAV_VERSION passee a
    `resonances-3` pour que les 9 autres pages recoivent le nouveau menu ;
  - `sources/build.py` : la ligne /guso-facile (ecrit=None, passe_menu=False,
    ce script posant lui-meme le menu) ;
  - `sitemap.xml`, `vercel.json` (redirection /Guso-Facile -> /guso-facile,
    l'URL ayant ete communiquee avec des majuscules), et les listes de pages
    de `verif_site.py` / `verif_commentaires.py`, passees a 10.

------------------------------------------------------------------------------
LES 6 MAQUETTES D'INTERFACE (posees le 14/08/2026 — la page ne montrait rien)
------------------------------------------------------------------------------
Verdict de David : « tres plate, elle ne montre rien de l'app ». Le texte
n'etait pas en cause : il manquait le visuel. Six blocs HTML/CSS PURS (aucune
image, aucun script, aucune capture d'ecran) reproduisent des ecrans reels de
l'application avec des donnees INVENTEES.

  Matiere d'origine (LECTURE SEULE, ne jamais editer ni deplacer) :
      /Users/davidlesage/CLAUDE/GUSO-FACILE-BACKUPS/maquettes-pour-resonances.html
  Elle est fournie par la session qui developpe Guso Facile.

CE QUI EST INTEGRE, ET OU
  1. Jauge des 507 h ............ HERO, colonne de droite (grille 1fr / 400px
                                  au-dela de 1000 px, empilee en dessous)
  2. « A faire maintenant » ..... fin de #promesse
  3. Fiche de date .............. #fonctionnalites, dans la grille des univers,
                                  juste apres les univers 1 et 2
  5. Ma tournee ................. idem, a cote de la fiche de date
  6. Tableau de bord structure .. idem, pleine largeur, apres l'univers 4
  4. Recap mensuel France Travail #situations, sous les trois cas d'usage
     (il illustre litteralement le cas de Marco, « Pointer France Travail en
      cinq minutes »)

LES TROIS EXIGENCES QUI NE SE NEGOCIENT PAS
  a) CHAQUE bloc porte, en <figcaption class="gf-cap">, la mention VISIBLE
     « Aperçu de l’interface — données fictives ». Une reproduction credible
     sans mention est indistinguable d'une vraie capture : cette page a deja
     du corriger « situations reelles » pour exactement ce motif.
  b) CE SONT DES ILLUSTRATIONS, PAS DES INTERFACES. Zero <button>, zero
     <input>, zero <a>, zero [tabindex] a l'interieur d'un bloc : un visiteur
     ne doit pas croire qu'il peut cliquer. Chaque bloc porte role="img" +
     aria-label. Garde-fou : `_controle_maquettes()`.
  c) RIEN QUI N'EXISTE PAS. La Guilde et « Je cree mon contrat » ne sont PAS
     illustrees : la page les ecrit au futur, les illustrer les ferait passer
     pour livrees.
     ⚠️ 16/08/2026 — les deux ecrans existent desormais, la page les ecrit au
     PRESENT, et la regle (c) TIENT TOUJOURS, pour une autre raison : AUCUNE
     DONNEE n'y a encore ete saisie. Une maquette de la Guilde montrerait des
     retours inventes dans un espace vide — exactement la promesse de contenu
     que `MOTS_INTERDITS_ABONDANCE` interdit d'ecrire en toutes lettres. Ne
     pas les illustrer tant qu'elles ne sont pas reellement peuplees.
     ⚠️ 16/08/2026 (suite) — la maquette 6 « Mes artistes », elle, montre une
     vue qui N'EXISTE PAS ENCORE telle quelle : elle est conservee (David a
     demande qu'elle serve de modele a la construction) mais elle porte
     desormais sa propre mention « (a venir) ». Voir `MAQ_STRUCTURE`.

CE QUI A ETE CORRIGE DANS LA MATIERE FOURNIE (l'auteur n'a pu tester que son
propre fichier, jamais dans cette page) :
  - Maquette 1, l'anneau etait MAL CALE : l'arc « dates possibles » allait de
    293deg a 336deg, soit 43 degres pour 43 HEURES — l'auteur a pris des heures
    pour des degres. 43 h sur 507 valent 30,5deg : l'arc s'arrete desormais a
    323deg ((412+43)/507 = 89,7 %).
  - Maquette 3, la liste des etapes affichait DEUX FOIS « Salaire reçu » et
    omettait « Actualisation France Travail », alors que son propre aria-label
    et sa note de livraison annoncent les cinq etapes de l'app. Corrige.
  - Maquette 4, le CSS DE LA VERSION EN CARTES N'EXISTAIT PAS dans le fichier
    source : seul restait celui de l'ancienne version en tableau (.gf-tw,
    .gf-tbl, .gf-th), qui ne stylait plus rien. Le bloc en cartes est donc
    habille ici (.gf-recmonth / .gf-reccard / .gf-rectot…), et le CSS de
    tableau, devenu inutile, n'a pas ete repris.
  - Maquette 5, LE KILOMETRAGE : retire le matin, RETABLI LE SOIR (14/08/2026).
    La note de livraison de l'auteur disait « L'espace Ma tournee de l'app
    liste les dates et les contacts, mais NE CALCULE PAS de kilometrage » ; par
    prudence le total avait donc ete retire, et la contradiction avec la puce
    « Carte des dates » de l'univers 2 laissee a l'arbitrage.
    VERIFICATION FAITE DEPUIS DANS LE CODE DE L'APPLICATION : la fonction est
    LIVREE. `haversineKm()` est appelee, le panneau affiche « ≈ X km parcourus
    (aller-retour) », les info-bulles donnent le kilometrage par date, et le
    journal de test releve « 7 dates localisees, ≈ 3 050 km (A/R) », haversine
    valide sur Paris -> Lyon = 391 km. La note de livraison etait en retard sur
    l'application. Le total « 1 240 km » est donc revenu dans la maquette, la
    puce de l'univers 2 a retrouve sa formulation complete, et l'aria-label de
    ce bloc — le SEUL des six a avoir bouge — annonce desormais le chiffre.
  - Maquette 6, l'aria-label annoncait un indicateur « vert, orange ou rouge »
    alors que la charte n'a ni vert ni rouge et que le rendu emploie la FORME
    de la pastille + un libelle. Un lecteur d'ecran entendait donc des couleurs
    absentes. Reecrit avec les trois libelles reellement affiches.
  - Les deux emoji (🔔 et 🎤) ont ete retires : la charte de la page l'interdit
    (« Aucun emoji », voir le commentaire de la section 4). La classe .gf-ico
    qui les portait a disparu avec eux.
  - Donnees harmonisees entre les six blocs pour qu'un lecteur attentif ne
    trouve pas de contradiction : Association Chant Libre est a Limoges
    partout (la maquette 4 la mettait a Pau), et la tournee ne liste que des
    dates qui existent dans les autres blocs.

MISE EN PAGE — la grille des univers passe a DEUX COLONNES
  Elle etait en `auto-fit minmax(320px,1fr)` : a 1440 px cela donnait TROIS
  cartes sur la premiere ligne et la QUATRIEME toute seule sur la deuxieme, en
  colonne de 328 px pour 1224 px de haut. L'ajout des maquettes n'aurait fait
  qu'aggraver ce desequilibre. Elle est desormais a une colonne sous 761 px et
  a DEUX colonnes au-dela : les univers se lisent 2 + 2, et les illustrations
  s'inserent naturellement entre les deux rangees (la vue structure prenant la
  pleine largeur, `.gf-wide`). Deux colonnes plutot qu'un `grid-column:1/-1`
  sur la seule carte 4 : la carte 4 est justement celle dont la plupart des
  puces sont « (a venir) », l'etaler sur toute la largeur l'aurait mise en
  avant plus que les trois autres.

------------------------------------------------------------------------------
LA REFONTE VISUELLE DU 14/08/2026 (soir) — « on s'adresse a des artistes »
------------------------------------------------------------------------------
Verdict de David, apres la mise en ligne : « la page de promo est TROP FROIDE.
En reprenant les codes couleur de Resonances Productions on a perdu quelque
chose, et meme dans la facon dont c'est presente. On s'adresse a des artistes,
il faut les seduire. Quelque chose d'avenant. PAS UN ENIEME LOGICIEL CHIANT ET
MOCHE. » Sa reference : `guso-facile.vercel.app/presentation.html`, « vraiment
plus avenante » dans son organisation ET ses couleurs.

Il avait raison : la page etait juste, rigoureuse… et austere. Elle ressemblait
a une notice, pas a une invitation. Ce qui a change, et RIEN D'AUTRE :

1. UN DEGRADE SIGNATURE, tire de la palette maison + UNE couleur d'appoint.
       --grad = or clair (#f0d18a) -> or (#d8b25a) 32% -> CORAIL (#e08a72) 66%
                -> prune claire (#b3a2e4)
   Le corail `--coral #e08a72` est la seule couleur ajoutee. Elle est chaude,
   elle tient entre l'or et la prune, et elle affiche 7,2:1 sur `--night` (donc
   utilisable meme en texte courant). La prune claire `--plum2 #b3a2e4` n'est
   pas un ajout de charte mais une CORRECTION DE CONTRASTE : le `--plum`
   d'origine tombait a 4,6:1 sur `--card`, tout juste ; `--plum2` est a 7,3:1.
   `--plum` reste, pour les aplats decoratifs (anneau de la jauge, pastilles).
   Le degrade revient : filet de 3 px en tete de chaque carte, texte des
   sur-titres et du <h1>, soulignement des mots-cles (`.mark`), marqueur de
   puce en losange, bouton principal, filets de separation, halo de la jauge.
   ⚠️ Il existe en DEUX exemplaires — CSS (`--grad`) et SVG (`#gf-ink`) — parce
   qu'un degrade CSS ne peut pas peindre le trait d'une icone. Les deux sont
   comptes par `ANCRES` : si l'un disparait, la page perd sa chaleur d'un seul
   cote, et c'est precisement ce qui ne se voit pas tout de suite.

2. DES FORMES DOUCES. Rayons de 18 a 26 px (contre 14/16/18), fonds de
   panneaux legerement degrades (jamais un aplat sec), ombres portees basses et
   larges, halos par `box-shadow` — et JAMAIS par un pseudo-element deborde,
   qui aurait pu creer un debordement horizontal. Plus d'air : sections a
   92 px (66 px sur telephone) au lieu de 78/60.

3. QUATRE TITRES DE SECTION REECRITS — « ils doivent tutoyer et promettre » :
       « Ce que l'outil resout »   -> « Garde ton energie pour la scene »
       « Ce que fait l'outil »     -> « Bien plus qu'un compteur d'heures »
       « Ou en est le projet »     -> « Jouons cartes sur table »
       « Manifester son interet »  -> « Reprends la main sur ton administratif »
       (+ le sur-titre « Appel a l'action » -> « Faire connaissance »)
   Le tutoiement des titres n'est pas une incoherence avec le corps de page,
   qui reste neutre : les QUATRE intitules d'univers tutoient deja (« Tes
   droits, maitrises »…). Les titres accueillent, le corps informe.
   ⚠️ AUCUN CORPS DE TEXTE N'A ETE TOUCHE, et aucune formulation protegee : ni
   « cree par David Lesage · relaye par l'association », ni « Pourquoi
   Resonances Productions le relaie », ni « n'est pas un service de
   l'association », ni « Trois situations typiques » et sa note sur les
   prenoms fictifs, ni le badge « Beta privee · places limitees », ni le bouton
   unique, ni les deux mentions sur les donnees personnelles, ni le bloc
   Guilde, ni aucune mention « (a venir) ».

4. DIX PICTOGRAMMES DESSINES A LA MAIN (voir la section « LES PICTOGRAMMES »).
   ZERO EMOJI — regle du site, et demande explicite de David.

5. L'ORDRE DES SECTIONS A CHANGE (deux blocs deplaces, texte inchange) :
       avant : hero · promesse · LIEN ASSOCIATION · fonctionnalites ·
               situations · etat · acces
       apres : hero · promesse · SITUATIONS · fonctionnalites ·
               LIEN ASSOCIATION · etat · acces
   Motif : sur la page qui a seduit David, ce qui vient tot ce sont des GENS,
   l'inventaire vient apres. Lea, Marco et Sophie repondent a « est-ce que
   c'est pour moi ? » ; les 25 puces des univers repondent a « qu'est-ce qu'il
   y a dedans ? » — on ne lit la seconde question que si l'on a dit oui a la
   premiere. Et le lien avec l'association est du CADRE : il tombait pile a
   l'endroit ou un artiste decide s'il continue de lire. Il forme desormais un
   bloc coherent avec l'etat du projet (« d'ou ca vient, ou ca en est »), juste
   avant le seul bouton de la page. Sa « Precision » finale y GAGNE en
   visibilite : elle passe de mention grise a encadre a filet prune.
   Ces deux deplacements sont chacun UN BLOC a remonter si David prefere.

------------------------------------------------------------------------------
L'ABSORPTION DU 15/08/2026 — la page devient LA VERSION DE REFERENCE
------------------------------------------------------------------------------
`guso-facile.vercel.app/presentation.html` porte desormais un `canonical` vers
CETTE page : c'est elle que Google doit indexer, donc tout ce qui ne vivait que
sur Vercel devait etre rapatrie. Matiere (LECTURE SEULE, ne jamais editer) :

    /Users/davidlesage/CLAUDE/GUSO FACILE/presentation.html
    /Users/davidlesage/CLAUDE/GUSO-FACILE-BACKUPS/dossier-seo-guso-facile.md
    /Users/davidlesage/CLAUDE/GUSO-FACILE-BACKUPS/manifeste-la-guilde.md

CE QUI A ETE RAPATRIE (et pourquoi la page ne gonfle pas pour autant)
  1. LA FAQ — 6 questions/reponses, en TEXTE VISIBLE (section #faq, en fin de
     page, apres l'appel a l'action). ⚠️ Elle n'est pas decorative : le bloc
     JSON-LD `FAQPage` pose plus bas n'est LEGITIME QUE SI les 6 Q/R figurent
     reellement dans la page — sinon c'est une violation des consignes Google.
     Le garde-fou `_controle_jsonld()` verifie exactement cela, question par
     question ET reponse par reponse.
     ⚠️ Elles sont REPLIEES dans des <details> natifs, PAS empilees : la page
     mesurait deja 15 151 px de haut a 390 px, et six paragraphes ouverts en
     auraient ajoute ~1 800. Un <details> est du HTML pur (aucun JavaScript,
     regle de la maison) et Google indexe le contenu d'un accordeon.
  2. « Trois etapes, c'est tout » — le mode d'emploi en trois temps, absent de
     la page, present sur Vercel. Bande compacte en fin de #promesse.
  3. Deux puces d'inventaire reellement manquantes : « Profil complet »
     (univers 1) et « Fiche structure » (univers 3). Elles vivaient dans la
     section « Pensee pour les artistes et les structures » de Vercel, pas
     dans ses quatre univers — d'ou l'oubli.
  4. La phrase de cloture de « Ou en est le projet » : « un outil deja solide,
     une porte encore etroite… ». Mots de David, rendus en serif (registre des
     titres) pour ne pas introduire de tutoiement dans un CORPS de texte.
  5. LA GUILDE (voir la section dediee ci-dessous).
  6. Les liens vers le blog (voir « LE MAILLAGE » ci-dessous).

CE QUI A ETE LAISSE SUR VERCEL, ET POURQUOI
  - « Pensee pour les artistes et les structures » (deux colonnes artistes /
    structures) : c'est un RESUME des univers 1 et 3, deja integralement
    presents ici. Le reprendre, c'est ecrire deux fois le meme inventaire.
  - « On veille les uns sur les autres » (le groupe / la structure /
    l'artiste seul) : couvert par l'univers 4, l'univers 3 et les trois cas
    d'usage. Et il nomme une structure (« Des Sons et Des Liens ») et une
    personne (« Marius ») inventees : sur le site public d'une ASSOCIATION,
    des exemples nominatifs non signales comme fictifs sont exactement ce que
    la correction « situations reelles » -> « typiques » a deja coute.
  - La section detaillee « J'ai besoin d'aide » (3 questions, un conseil,
    prevenir qui l'on veut) : deja resumee en une puce de l'univers 4.
  - La bande « Le probleme » (5 pictogrammes : 507 h, DPAE, GUSO, factures,
    France Travail) : deja dite en prose dans #promesse, mieux.
  - Le second bouton « Se connecter » du hero : la page n'a QU'UN bouton, par
    decision — voir l'ecart n°8 plus haut.
  - « Beta OUVERTE » de Vercel : ici c'est « Beta PRIVEE », formulation
    validee. Ne pas harmoniser dans ce sens-la.

LE SEO — SECTION 2 DU DOSSIER, APPLIQUEE
  - `<title>` : « Guso Facile — gerer son intermittence et ses 507 h » (50 car.,
    valeur exacte du dossier). L'ancien titre portait « · Resonances
    Productions » ; le dossier ne le reprend pas et la balise est deja a la
    bonne longueur — on suit le dossier.
  - `meta description` : valeur exacte du dossier (154 car.).
  - `h1` : « Guso Facile — la gestion de l'intermittence, simplifiee ». Il ne
    valait que « Guso Facile », ce que le dossier designe comme « la principale
    faiblesse restante ». La marque reste en grand, la suite passe en seconde
    ligne plus petite DANS le meme <h1> (le texte du titre est donc complet
    pour Google et pour un lecteur d'ecran).
  - JSON-LD : bloc du dossier COLLE TEL QUEL (Organization + WebApplication +
    FAQPage + BreadcrumbList). Il est parse par `json.loads()` avant chaque
    ecriture : un JSON-LD casse vaut moins que pas de JSON-LD du tout.
  - `<main>` ajoute (le dossier le rappelle en tete de sa section 2).

LE MAILLAGE (section 6 du dossier)
  DEUX liens descendants vers `/guso-facile/blog`, tous deux a ancre
  DESCRIPTIVE (jamais « en savoir plus ») : un a la suite des cas d'usage,
  un en fin de FAQ — c'est le placement de la page Vercel.
  ⚠️ Le blog est construit par un AUTRE generateur (`generate_guso_blog.py`) :
  tant que `guso-facile/blog/` n'existe pas, `verif_site.py` signale a juste
  titre « lien interne mort ». Ce n'est pas un defaut de cette page.

------------------------------------------------------------------------------
LA GUILDE — QUELLE LONGUEUR, ET CE QUI A ETE ADOUCI
------------------------------------------------------------------------------
Le manifeste (`manifeste-la-guilde.md`) existe en TROIS longueurs. Retenue
ici : l'ACCROCHE (version tres courte) comme phrase d'ouverture + l'ENCART
(version courte) comme corps. PAS la version longue : ceci est une page
produit, pas un manifeste — et la page mesure deja 15 000 px sur telephone.
La version longue fera un tres bon article de blog.

⚠️ CE BLOC EST SOUMIS AU MEME INTERDIT QUE LA PUCE « L'entraide entre
artistes » : meme vocabulaire proscrit — les HUIT MOTS, inchanges depuis le
14/08/2026 — et, depuis le 16/08/2026, meme interdit d'ABONDANCE (l'ecran
existe, il est vide : on decrit une capacite, jamais un contenu).
Garde-fou : `_controle_guilde_encart()`, jumeau de `_controle_guilde()`.

CE QUI A ETE ADOUCI PAR RAPPORT AU MANIFESTE (esprit garde, charge retiree) :
  - « dans ce metier, l'abus est ordinaire. Pas spectaculaire : ORDINAIRE. »
    -> « ce qui manque le plus souvent n'est pas la bonne foi : c'est le
    cadre ». Le manifeste s'adresse a des membres connectes ; ici la phrase
    serait lue par un programmateur sur le site d'une association, comme un
    constat general d'abus porte par elle.
  - « personne ne reste seul face a un abus » -> « personne ne reste seul ».
    Meme motif, et l'accroche y gagne en rythme.
  - « Pas d'appreciation, pas de recit, pas de reglement de comptes. Ce n'est
    ni un espace therapeutique, ni un tribunal » -> « Rien que des faits,
    aucun commentaire libre, aucun tribunal. » Trois negations valent mieux
    que six : au-dela, se defendre devient se justifier.
  - AJOUTE (demande explicite des « Notes d'emploi » du manifeste) : « Cet
    espace sera reserve aux membres connectes de Guso Facile » — sinon on cree
    de la frustration chez un lecteur qui cliquerait pour voir.
  - Aucun lieu, aucune personne nommes : les phrases citees restent generiques,
    comme l'exige le manifeste lui-meme.

------------------------------------------------------------------------------
LA REMISE A NIVEAU DU 16/08/2026 — la page rattrape l'application
------------------------------------------------------------------------------
David a teste l'app et constate que LA PAGE ANNONCE « A VENIR » DES
FONCTIONNALITES QUI EXISTENT. Etat des lieux fourni par la session qui
developpe Guso Facile, releve DANS LE CODE. Regle inchangee, appliquee dans les
DEUX SENS : ce qui est livre s'ecrit au PRESENT, ce qui ne l'est pas s'ecrit au
FUTUR avec « (a venir) » — un beta-testeur verifie en trois clics.

CE QUI PASSE AU PRESENT (mentions « (a venir) » RETIREES)
  1. « Je cree mon contrat » (univers 2) — l'ecran existe et est deploye.
     `class="soon"` et `<i>(a venir)</i>` retires, texte inchange pour le reste.
  2. « L'entraide entre artistes » (univers 4, la puce Guilde) — idem.
     Deux verbes remis au present : « on partagera » -> « on partage »,
     « l'outil proposera » -> « l'outil propose ». RIEN D'AUTRE.
  3. L'ENCART « la Guilde » — « (a venir) » retire de son titre, et les deux
     futurs de son dernier paragraphe passes au present : « La Guilde fera
     donc » -> « fait donc », « Cet espace sera reserve » -> « est reserve ».
     La phrase « membres connectes » reste (exigence du manifeste, verifiee).
  4. Le sous-titre de l'univers 4 disait « Cet univers est en cours de
     deploiement » — c'etait vrai quand quatre de ses six puces attendaient.
     Il n'en reste que deux : la phrase le dit maintenant, sans annuler tout
     l'univers.

⚠️⚠️ LA NUANCE QUI COMMANDE TOUTE LA REDACTION DE CES DEUX BLOCS
     Les ecrans existent, MAIS AUCUNE DONNEE N'Y A ENCORE ETE SAISIE : zero
     lieu, zero retour. On decrit donc une CAPACITE (« on partage… »,
     « l'espace est reserve aux membres connectes… »), JAMAIS UN CONTENU
     (« consulte les retours d'artistes sur des centaines de lieux » serait
     promettre un espace vide, ce qui est pire qu'un « a venir » de trop).
     Ce n'est plus un principe seulement redactionnel : c'est un garde-fou,
     `MOTS_INTERDITS_ABONDANCE`, applique aux deux memes blocs.

CE QUI RESTE AU FUTUR (3 mentions « (a venir) », voir NB_A_VENIR)
  a) « Points de vigilance cote structure » (univers 4) — la vue qui dirait qui
     approche du seuil n'existe pas.
  b) « Confidentialite graduee » (univers 4) — le backend existe et il est
     teste, mais L'ECRAN DE REGLAGE COTE ARTISTE N'EXISTE PAS.
  c) NOUVEAU : la maquette 6, l'apercu « Mes artistes » (voir le commentaire
     au-dessus de `MAQ_STRUCTURE`).

L'ESPACE « GRATITUDES » (avis des utilisateurs) n'a jamais ete construit — et
il n'est mentionne NULLE PART sur cette page. On ne l'ajoute donc pas : une
page ne gagne rien a annoncer ce qui n'existe pas encore.

LE GARDE-FOU `_controle_guilde()` A CHANGE, ET C'EST DELIBERE
  Il EXIGEAIT la presence de « (a venir) » dans le bloc Guilde : cette exigence
  serait devenue fausse. Elle est remplacee par le controle d'abondance
  ci-dessus. ⚠️ SA PARTIE ESSENTIELLE EST INTACTE : les HUIT MOTS PROSCRITS
  (noter, notation, signaler, denoncer, avis, evaluation, blacklist,
  reputation) restent interdits dans ce bloc et dans l'encart, pour la raison
  ecrite plus haut — la page est publique et decrit des artistes qui affirment
  des faits sur des employeurs identifiables. Ne pas affaiblir cette
  protection, ne pas l'etendre au reste de la page (« signaler un bug » reste
  legitime dans « Et aussi », « Evaluation d'une proposition » dans l'univers
  2).

Usage : python3 sources/generate_guso.py   (depuis la racine du depot)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mobile_nav            # hamburger mobile              # noqa: E402
import nav_menu              # menu de navigation partage    # noqa: E402
import verif_commentaires    # garde-fou commentaires HTML   # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, 'guso-facile')
OUT_HTML = os.path.join(OUT_DIR, 'index.html')

#: URL exacte du formulaire, validee. `target="_blank"` OBLIGATOIREMENT
#: accompagne de `rel="noopener"` (regle du site, verifiee par un garde-fou
#: plus bas).
URL_ACCES = 'https://guso-facile.vercel.app/presentation.html'


# =========================================================================
# LE GABARIT
# =========================================================================
# Le squelette (head, variables de couleur, nav, boutons, footer, retour en
# haut) est celui des 9 pages du site, repris a l'identique de
# `le-soin-soa/index.html` : meme charte, meme comportement, aucune divergence
# a maintenir. Seul le bloc « ===== Guso Facile ===== » est propre a la page.
#
# ⚠️ Les deux <link> vers fonts.googleapis.com sont ceux des 9 autres pages.
#    Ce ne sont PAS des polices supplementaires : c'est exactement la meme
#    feuille, deja chargee partout sur le site. Sans elle, Cormorant Garamond
#    et Jost tombent sur Georgia / system-ui et la page ne ressemble plus aux
#    autres. Ne rien ajouter d'autre : aucun script tiers, aucune iframe,
#    aucun traceur.

HEAD = """<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Guso Facile — gérer son intermittence et ses 507 h</title>
<meta name="description" content="Suivi des 507 heures, DPAE, feuillets GUSO, factures et pointage France Travail réunis dans une seule application claire, pour les artistes intermittents.">
<meta property="og:title" content="Guso Facile — l’administratif de l’intermittence, simplifié">
<meta property="og:description" content="Suivi des 507 heures, DPAE, feuillets GUSO, factures, pointage France Travail : un outil web pour les artistes intermittents et les structures qui les accompagnent. Bêta privée, sur invitation ou cooptation.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.resonancesproductions.org/guso-facile">
<meta property="og:image" content="https://www.resonancesproductions.org/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://www.resonancesproductions.org/guso-facile">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0e0f24">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
"""

# --- les donnees structurees (JSON-LD) ------------------------------------
# ⚠️ BLOC COLLE TEL QUEL depuis la section 2.1 de
#    `GUSO-FACILE-BACKUPS/dossier-seo-guso-facile.md` (LECTURE SEULE). Ne pas
#    le « nettoyer » : chaque champ y a ete pese, et c'est la seule exception
#    a la regle « aucun script » de cette page (un <script type="application/
#    ld+json"> n'execute rien, ce sont des donnees).
#
# TROIS POINTS A NE PAS PERDRE DE VUE :
#  a) LE `FAQPage` N'EST LEGITIME QUE SI LES 6 Q/R SONT VISIBLES DANS LA PAGE.
#     Annoncer a Google une FAQ absente de l'ecran est une violation explicite
#     de ses consignes, sanctionnable. La section #faq les porte, et
#     `_controle_jsonld()` refuse d'ecrire si une seule question — ou une seule
#     reponse — manque au texte visible.
#  b) IL EST PARSE PAR `json.loads()` AVANT CHAQUE ECRITURE. Un JSON-LD casse
#     vaut moins que pas de JSON-LD : Google ignore le bloc entier, et l'erreur
#     ne se voit NULLE PART a l'ecran.
#  c) `schema.org` a du etre ajoute a `HOTES_AUTORISES` : le controle des hotes
#     externes lit les `https://schema.org/…` du vocabulaire comme un domaine
#     tiers. C'est le controle qui est bon ; l'URL, elle, n'est jamais chargee
#     (c'est un identifiant de vocabulaire, pas une ressource).
JSONLD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.resonancesproductions.org/#organization",
      "name": "Résonances Productions",
      "url": "https://www.resonancesproductions.org/"
    },
    {
      "@type": "WebApplication",
      "@id": "https://www.resonancesproductions.org/guso-facile#app",
      "name": "Guso Facile",
      "url": "https://www.resonancesproductions.org/guso-facile",
      "applicationCategory": "BusinessApplication",
      "applicationSubCategory": "Gestion administrative de l'intermittence du spectacle",
      "operatingSystem": "Tout navigateur web",
      "browserRequirements": "Navigateur web moderne, aucune installation",
      "inLanguage": "fr-FR",
      "description": "Application web qui réunit le suivi des 507 heures, les DPAE, les feuillets GUSO, les factures et le pointage France Travail des artistes intermittents et des structures qui les accompagnent.",
      "image": "https://www.resonancesproductions.org/og-image.jpg",
      "author": {
        "@type": "Person",
        "name": "David Lesage",
        "url": "https://www.resonancesproductions.org/david-lesage-en-concert"
      },
      "creator": {
        "@type": "Person",
        "name": "David Lesage",
        "url": "https://www.resonancesproductions.org/david-lesage-en-concert"
      },
      "publisher": {
        "@id": "https://www.resonancesproductions.org/#organization"
      },
      "audience": {
        "@type": "Audience",
        "audienceType": "Artistes intermittents du spectacle et structures de production",
        "geographicArea": {
          "@type": "Country",
          "name": "France"
        }
      },
      "featureList": [
        "Suivi glissant des 507 heures avec date anniversaire",
        "Bloc « À faire maintenant » : DPAE, feuillets GUSO et factures à échéance",
        "Récap mensuel pour l'actualisation France Travail (1 GUSO = 1 ligne)",
        "Dates partagées entre plusieurs artistes, avec DPAE nominative",
        "Évaluateur de date : bon plan, à négocier, à éviter",
        "Carte des trajets, carnet de contacts et mails types de tournée",
        "Back-office transversal pour les structures qui accompagnent des artistes"
      ],
      "isAccessibleForFree": true,
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "EUR",
        "availability": "https://schema.org/LimitedAvailability",
        "description": "Phase de test — accès sur demande."
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.resonancesproductions.org/guso-facile#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "C'est quoi le GUSO ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Le GUSO est le Guichet unique du spectacle occasionnel : le dispositif qui permet à un employeur dont le spectacle n'est pas l'activité principale de déclarer et de rémunérer un artiste ou un technicien en une seule démarche. C'est lui qui produit le feuillet remis à l'artiste après la date."
          }
        },
        {
          "@type": "Question",
          "name": "Combien d'heures faut-il pour être intermittent ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Il faut réunir 507 heures de travail sur les 12 mois qui précèdent sa date anniversaire pour ouvrir ou renouveler ses droits au titre des annexes 8 et 10 de l'assurance chômage. Le calcul est glissant : chaque jour, les heures les plus anciennes sortent du compte."
          }
        },
        {
          "@type": "Question",
          "name": "Combien de cachets pour atteindre 507 heures ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Un cachet équivaut à 12 heures. Il faut donc environ 43 cachets pour atteindre les 507 heures, si l'on ne compte que des cachets — les heures de répétition et de technique s'y ajoutent et réduisent d'autant ce nombre."
          }
        },
        {
          "@type": "Question",
          "name": "C'est quoi une DPAE, et qui doit la faire ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "La DPAE est la déclaration préalable à l'embauche. Elle est faite par la structure employeuse, avant le début du contrat, à partir des nom, prénom et date de naissance de l'artiste. Sur une date jouée à deux, il en faut une par artiste."
          }
        },
        {
          "@type": "Question",
          "name": "Une session de studio compte-t-elle dans les 507 heures ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Oui. Une session d'enregistrement relève de l'édition phonographique (convention collective 2121) et n'est pas déclarée via un GUSO, mais elle compte comme un cachet, soit 12 heures, dans le total des 507 heures."
          }
        },
        {
          "@type": "Question",
          "name": "Comment obtenir un accès à Guso Facile ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "L'application est en phase de test : l'accès se fait sur demande, via le formulaire « Demander un accès ». Chaque demande est étudiée personnellement par David Lesage, son créateur."
          }
        }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Résonances Productions",
          "item": "https://www.resonancesproductions.org/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Guso Facile",
          "item": "https://www.resonancesproductions.org/guso-facile"
        }
      ]
    }
  ]
}
</script>
"""


# --- socle commun aux 9 pages (couleurs, typo, nav, boutons, footer) ------
CSS_BASE = """:root{--night:#0e0f24;--night2:#141633;--ink:#eae7f3;--muted:#a9a6c4;--gold:#d8b25a;--gold2:#f0d18a;--plum:#8f7ad1;--card:#191b3d;--line:rgba(216,178,90,.26)}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--night);color:var(--ink);font-family:'Jost',-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.75;font-size:17px;-webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2,h3,h4,.serif{font-family:'Cormorant Garamond',Georgia,serif}
a{color:inherit;text-decoration:none}
.wrap{max-width:1080px;margin:0 auto;padding:0 26px}
.kick{letter-spacing:.32em;text-transform:uppercase;font-size:13px;font-weight:600;color:var(--gold);margin-bottom:14px}
section{padding:78px 0;position:relative}
.sec-title{font-size:clamp(30px,5vw,50px);font-weight:600;line-height:1.08;color:#fff}
.lead{font-size:19px;color:var(--muted);max-width:760px;margin-top:16px}
p.body{max-width:820px;color:#d7d4ea;margin-top:16px}
b{color:#fff;font-weight:500}
.divider{height:1px;background:linear-gradient(90deg,transparent,var(--line),transparent);max-width:1080px;margin:0 auto}
/* nav */
.nav{position:fixed;top:0;left:0;right:0;z-index:40;display:flex;align-items:center;justify-content:space-between;padding:16px 26px;background:rgba(14,15,36,.6);backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.05)}
.nav .brand{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:19px;letter-spacing:.12em;color:#fff;text-transform:uppercase}
.nav .links{display:flex;align-items:center;gap:19px;font-size:13.5px;letter-spacing:.04em}
.nav .links a{color:var(--muted);transition:color .2s}
.nav .links a:hover{color:var(--gold2)}
.nav .adh{color:#1a1608!important;background:var(--gold);padding:8px 16px;border-radius:30px;font-weight:600}
@media(max-width:760px){.nav .links a:not(.adh){display:none}}
@media(min-width:861px) and (max-width:1080px){.nav{padding:16px 18px}.nav .brand{font-size:17px;white-space:nowrap}.nav .links{gap:9px;font-size:13px}.nav .adh{padding:8px 13px}}
.nav .links a[aria-current="page"]{color:var(--gold2)}
.btn{display:inline-flex;align-items:center;gap:8px;background:var(--gold);color:#1a1608;font-weight:600;padding:14px 26px;border-radius:40px;font-size:15px;transition:transform .2s,box-shadow .2s}
.btn:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(216,178,90,.28)}
.btn.ghost{background:transparent;color:var(--gold2);border:1px solid var(--line)}
.cta{display:flex;gap:14px;flex-wrap:wrap}
/* retour en haut */
.totop{position:fixed;right:18px;bottom:18px;z-index:35;width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:rgba(25,27,61,.92);border:1px solid var(--line);color:var(--gold2);font-size:19px;opacity:0;visibility:hidden;transition:opacity .3s,visibility .3s,transform .2s}
.totop.on{opacity:1;visibility:visible}
.totop:hover{transform:translateY(-2px)}
/* focus clavier visible (accessibilite) */
:focus-visible{outline:2px solid var(--gold2);outline-offset:2px;border-radius:4px}
footer{background:#08091a;padding:70px 0 56px;border-top:1px solid var(--line)}
.fgrid{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:34px}
footer h4{font-family:'Cormorant Garamond',serif;color:#fff;font-size:22px;font-weight:600;margin-bottom:10px}
footer p,footer a{color:var(--muted);font-size:16px}
footer a{display:inline-block;padding:13px 0;line-height:1.3}
footer a.btn,footer a.adh{padding:14px 30px}
footer a:hover{color:var(--gold2)}
footer a:not(.btn):not(.adh){text-decoration:underline;text-decoration-color:rgba(216,178,90,.35);text-underline-offset:3px}
.fbrand{letter-spacing:.12em;text-transform:uppercase;color:var(--gold2);font-family:'Cormorant Garamond',serif;font-size:20px;font-weight:600}
.legal{margin-top:40px;text-align:center;color:#6b6b80;font-size:13px}
@media(max-width:760px){.fgrid{grid-template-columns:1fr;gap:24px}section{padding:60px 0}}
p a:not(.btn):not(.adh){text-decoration:underline;text-decoration-color:rgba(216,178,90,.4);text-underline-offset:3px}
"""

# --- CSS propre a la page -------------------------------------------------
# ⚠️ CETTE FEUILLE EST CELLE DE LA REFONTE DU 14/08/2026 (soir). Le principe
# n'est plus « sobre et sombre » mais « chaleureux SANS quitter la famille » :
# le squelette (CSS_BASE) reste celui des 9 autres pages a l'octet pres, et
# toute la chaleur passe par CETTE feuille-ci. Voir l'entete du fichier,
# section « LA REFONTE VISUELLE ».
#
# Les quatre leviers, dans l'ordre de leur poids visuel :
#   1. LE DEGRADE SIGNATURE `--grad` — or clair -> or -> corail -> prune. Il
#      revient en filet de 3 px sur chaque carte, en texte sur les sur-titres,
#      en soulignement des mots-cles, en marqueur de puce et en bouton.
#   2. DES FORMES DOUCES — rayons de 18 a 26 px, fonds de panneaux LEGEREMENT
#      degrades (jamais un aplat sec), ombres portees basses et larges.
#   3. DE L'AIR — sections a 92 px (66 px sur telephone) au lieu de 78/60.
#   4. DES HALOS — trois lueurs fixes tres basses en opacite derriere la page.
#
# ⚠️ Rien ne descend sous 13 px (plancher typographique du site, verifie par
#    `_controles`). ⚠️ Aucune couleur de texte introduite ici n'est sous 4,5:1
#    sur son fond : `--coral` = 7,2:1 sur `--night`, `--plum2` = 7,3:1 sur
#    `--card` (le `--plum` d'origine y etait a 4,6:1, tout juste — d'ou
#    `--plum2` pour TOUS les textes, `--plum` restant aux aplats decoratifs).
CSS_PAGE = """/* ===== Guso Facile ===== */
/* --- le degrade signature, decline partout ------------------------------ */
:root{--coral:#e08a72;--plum2:#b3a2e4;
--grad:linear-gradient(95deg,var(--gold2),var(--gold) 32%,var(--coral) 66%,var(--plum2));
--grad-warm:linear-gradient(100deg,var(--gold2),var(--gold) 46%,var(--coral))}
.gf-defs{position:absolute;width:0;height:0;overflow:hidden}
.ic{width:23px;height:23px;display:block;flex:0 0 auto}
.grad-t{width:fit-content;max-width:100%;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
.mark{background-image:var(--grad);background-repeat:no-repeat;background-size:100% 2px;background-position:0 100%;padding-bottom:3px}
/* trois lueurs fixes : c'est ce qui enleve le fond « noir de notice » */
body::before{content:'';position:fixed;inset:0;z-index:-1;pointer-events:none;background:radial-gradient(58vw 40vw at 10% -6%,rgba(216,178,90,.11),transparent 62%),radial-gradient(52vw 38vw at 100% 14%,rgba(224,138,114,.10),transparent 62%),radial-gradient(62vw 46vw at 46% 106%,rgba(143,122,209,.12),transparent 62%)}
section{padding:92px 0}
.divider{height:2px;background:linear-gradient(90deg,transparent,rgba(216,178,90,.42) 16%,rgba(224,138,114,.5) 50%,rgba(179,162,228,.42) 84%,transparent)}
.kick{display:inline-block;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
.sec-title{letter-spacing:.01em}
.lead b,.body b{color:#fff}
/* boutons : le principal porte le degrade chaud, le fantome un filet dore */
.btn{border-radius:999px;padding:15px 28px}
.btn svg{width:18px;height:18px;flex:0 0 auto}
.acces .btn{background:var(--grad-warm);color:#1b1206;box-shadow:0 14px 34px -16px rgba(224,138,114,.6)}
/* la fleche du bouton reprend la couleur du TEXTE : le degrade signature, clair, disparaissait sur le bouton clair (mesure a l'ecran) */
.acces .btn svg{stroke:#1b1206}
.acces .btn:hover{box-shadow:0 20px 42px -14px rgba(224,138,114,.7)}
.btn.ghost{background:linear-gradient(180deg,rgba(255,255,255,.055),rgba(255,255,255,.02));border:1px solid rgba(240,209,138,.3);color:var(--gold2)}
.btn.ghost:hover{border-color:rgba(240,209,138,.55)}
/* --- hero ---------------------------------------------------------------- */
.gf-top{padding:132px 0 78px;background:radial-gradient(900px 560px at 6% -12%,rgba(143,122,209,.22),transparent 62%),radial-gradient(760px 480px at 96% 8%,rgba(224,138,114,.14),transparent 62%),radial-gradient(720px 470px at 60% 108%,rgba(216,178,90,.13),transparent 62%),linear-gradient(180deg,#0b0c1e,var(--night))}
.gf-top h1{font-size:clamp(38px,7vw,74px);font-weight:600;line-height:1.02;letter-spacing:.02em}
.gf-claim{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(20px,2.9vw,29px);line-height:1.32;margin-top:16px;max-width:720px}
.badge{display:inline-flex;align-items:center;gap:9px;margin-top:28px;padding:9px 18px;border:1px solid rgba(240,209,138,.34);border-radius:999px;color:var(--gold2);font-size:13.5px;letter-spacing:.12em;text-transform:uppercase;font-weight:500;background:linear-gradient(90deg,rgba(216,178,90,.14),rgba(224,138,114,.10))}
.badge::before{content:'';width:7px;height:7px;border-radius:50%;background:var(--grad-warm);flex:0 0 auto}
.gf-top .cta{margin-top:32px}
.band{background:linear-gradient(180deg,#0b0c1e,#101128 55%,var(--night))}
/* hero : texte a gauche, jauge des 507 h a droite (empile sous 1000 px) */
.gf-topgrid{display:grid;gap:38px;align-items:center}
@media(min-width:1000px){.gf-topgrid{grid-template-columns:minmax(0,1fr) 400px}}
/* --- les quatre univers — DEUX colonnes, jamais trois (voir l'entete) ---- */
.univers{display:grid;grid-template-columns:minmax(0,1fr);gap:26px;margin-top:42px}
@media(min-width:761px){.univers{grid-template-columns:repeat(2,minmax(0,1fr))}}
.u-card{position:relative;overflow:hidden;background:linear-gradient(180deg,#1c1e46,#171935);border:1px solid rgba(255,255,255,.07);border-radius:22px;padding:30px 28px 26px;box-shadow:0 20px 44px -30px rgba(0,0,0,.95)}
.u-card::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad)}
.u-head{display:flex;align-items:center;gap:14px}
.u-ico{flex:0 0 auto;width:44px;height:44px;display:flex;align-items:center;justify-content:center;border-radius:14px;border:1px solid rgba(240,209,138,.22);background:linear-gradient(140deg,rgba(216,178,90,.16),rgba(224,138,114,.12) 55%,rgba(143,122,209,.14))}
.u-num{letter-spacing:.28em;text-transform:uppercase;font-size:13px;font-weight:600;color:var(--gold)}
.u-card h3{font-size:27px;font-weight:600;color:#fff;line-height:1.15;margin-top:3px}
.u-sub{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--plum2);font-size:18.5px;line-height:1.4;margin-top:12px}
.u-card ul{list-style:none;margin-top:20px}
.u-card li{position:relative;padding-left:24px;margin-top:14px;color:#d7d4ea;font-size:15.5px;line-height:1.62}
.u-card li::before{content:'';position:absolute;left:1px;top:9px;width:8px;height:8px;border-radius:2px;background:var(--grad-warm);transform:rotate(45deg)}
.u-card li.soon::before{background:none;border:1.5px solid var(--plum2)}
.u-card li b{color:#fff;font-weight:500}
.u-card li i{font-style:normal;display:inline-block;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--plum2);border:1px solid rgba(179,162,228,.4);background:rgba(143,122,209,.12);border-radius:999px;padding:1px 9px;line-height:1.5}
.aussi{margin-top:40px;padding:26px 28px;border:1px solid rgba(255,255,255,.07);border-radius:20px;background:linear-gradient(180deg,rgba(28,30,70,.72),rgba(23,25,53,.5));display:flex;gap:18px;align-items:flex-start}
.aussi .ic-w,.precision .ic-w{flex:0 0 auto;line-height:0;margin-top:3px}
.aussi .ic{width:26px;height:26px}
.aussi .u-num{display:block;margin-bottom:8px}
.aussi p{color:#d7d4ea;font-size:15.5px}
/* --- trois situations : de vraies cartes, plus un simple filet a gauche -- */
.cas-note{color:var(--muted);font-size:15px;margin-top:14px;max-width:62ch}
.cas{display:grid;grid-template-columns:repeat(auto-fit,minmax(288px,1fr));gap:26px;margin-top:42px}
.cas article{position:relative;overflow:hidden;border:1px solid rgba(255,255,255,.07);border-radius:22px;background:linear-gradient(180deg,#1c1e46,#171935);padding:28px 26px 26px;box-shadow:0 20px 44px -30px rgba(0,0,0,.95)}
.cas article::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad)}
.cas-ico{width:44px;height:44px;display:flex;align-items:center;justify-content:center;border-radius:14px;border:1px solid rgba(240,209,138,.22);background:linear-gradient(140deg,rgba(216,178,90,.16),rgba(224,138,114,.12) 55%,rgba(143,122,209,.14));margin-bottom:16px}
.cas h3{font-size:25px;font-weight:600;color:#fff;line-height:1.18}
.cas p{color:#d7d4ea;font-size:15.5px;margin-top:11px}
/* --- l'etat du projet ---------------------------------------------------- */
.etat{position:relative;overflow:hidden;margin-top:38px;border:1px solid rgba(255,255,255,.08);border-radius:24px;background:linear-gradient(180deg,rgba(28,30,70,.9),rgba(20,22,51,.6));padding:38px 36px;max-width:900px;box-shadow:0 26px 60px -40px rgba(0,0,0,.95)}
.etat::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad)}
.etat p{color:#d7d4ea;font-size:16px}
.etat p + p{margin-top:16px}
.etat .first{color:#fff;font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(21px,3vw,28px);line-height:1.3;font-style:italic}
/* --- le lien avec l'association : la precision sort en encadre ----------- */
.precision{display:flex;gap:14px;align-items:flex-start;margin-top:28px;max-width:760px;padding:20px 22px;border:1px solid rgba(179,162,228,.28);border-radius:18px;background:linear-gradient(135deg,rgba(143,122,209,.12),rgba(224,138,114,.07))}
.precision .ic{width:24px;height:24px}
.precision p{color:#d7d4ea;font-size:15px;line-height:1.65;margin:0}
/* --- appel a l'action : un panneau, pas une fin de page ------------------ */
.acces{position:relative;overflow:hidden;max-width:880px;border:1px solid rgba(255,255,255,.09);border-radius:26px;padding:46px 42px 40px;background:linear-gradient(135deg,rgba(216,178,90,.12),rgba(224,138,114,.10) 48%,rgba(143,122,209,.12));box-shadow:0 30px 70px -46px rgba(0,0,0,.95)}
.acces::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad)}
.acces .cta{margin-top:30px}
.mention{margin-top:20px;max-width:660px;color:var(--muted);font-size:14px;line-height:1.65}
.mention + .mention{margin-top:12px}
/* --- le titre principal porte la phrase complete (dossier SEO, section 2) - */
/* La marque reste en grand ; la suite passe en seconde ligne, a l'interieur du
   MEME titre — celui que lisent Google et un lecteur d'ecran est donc entier.
   (Ne pas ecrire la balise en toutes lettres dans ce commentaire : le
   garde-fou compte ses occurrences dans la page livree, CSS compris.) */
.gf-top h1 .h1-sous{display:block;font-size:clamp(17px,2.4vw,26px);font-weight:500;line-height:1.24;letter-spacing:.02em;margin-top:10px}
/* --- « Trois etapes, c'est tout » : une bande legere, pas des cartes ----- */
.etapes-t{margin-top:40px}
.etapes{display:grid;grid-template-columns:minmax(0,1fr);gap:16px;margin-top:16px}
@media(min-width:761px){.etapes{grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}}
.etape{position:relative;overflow:hidden;border:1px solid rgba(255,255,255,.07);border-radius:18px;background:linear-gradient(180deg,rgba(28,30,70,.72),rgba(23,25,53,.5));padding:22px 22px 20px}
.etape::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad)}
.etape h3{font-size:21px;font-weight:600;color:#fff;line-height:1.2;margin-top:4px}
.etape .etape-d{color:#d7d4ea;font-size:15.5px;margin-top:9px}
/* --- l'encart « la Guilde » (longueur retenue et adoucissements : entete) - */
.guilde{display:flex;gap:18px;align-items:flex-start;margin-top:40px;max-width:900px;padding:28px 30px 26px;border:1px solid rgba(179,162,228,.28);border-radius:22px;background:linear-gradient(135deg,rgba(143,122,209,.13),rgba(224,138,114,.08) 62%,rgba(216,178,90,.08));box-shadow:0 24px 56px -40px rgba(0,0,0,.95)}
.guilde .ic-w{flex:0 0 auto;line-height:0;margin-top:4px}
.guilde .ic{width:26px;height:26px}
.guilde .u-num{display:block;margin-bottom:8px}
.guilde i{font-style:normal;display:inline-block;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--plum2);border:1px solid rgba(179,162,228,.4);background:rgba(143,122,209,.12);border-radius:999px;padding:1px 9px;line-height:1.5;margin-left:5px}
.guilde-claim{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(19px,2.4vw,24px);line-height:1.32}
.guilde .guilde-p{color:#d7d4ea;font-size:15.5px;margin-top:13px}
/* --- la cloture de « Jouons cartes sur table » (mots de David) ----------- */
/* En serif italique : c'est le registre des TITRES de cette page, celui qui a
   le droit de tutoyer. Le corps, lui, reste neutre (voir l'entete, point 3). */
.etat .etat-fin{color:#fff;font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:clamp(19px,2.4vw,24px);line-height:1.32;margin-top:24px;padding-top:20px;border-top:1px solid rgba(216,178,90,.28)}
/* --- la FAQ : REPLIEE, jamais empilee (voir l'entete) -------------------- */
/* <details> natif : aucun JavaScript, et le contenu d'un accordeon reste lu
   par Google. La fleche est dessinee en CSS (deux bords tournes a 45deg) —
   ni image, ni emoji, ni onzieme pictogramme a maintenir. */
.faq{max-width:860px;margin-top:34px}
.faq-q{border:1px solid rgba(255,255,255,.08);border-radius:18px;background:linear-gradient(180deg,rgba(28,30,70,.72),rgba(23,25,53,.5));margin-bottom:11px;overflow:hidden}
.faq-q summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:16px;padding:15px 20px;min-height:44px}
.faq-q summary::-webkit-details-marker{display:none}
.faq-q summary h3{flex:1 1 auto;min-width:0;font-size:21px;font-weight:600;color:#fff;line-height:1.28}
.faq-q summary::after{content:'';flex:0 0 auto;width:9px;height:9px;margin-right:3px;border-right:1.6px solid var(--gold2);border-bottom:1.6px solid var(--gold2);transform:rotate(45deg) translateY(-3px)}
.faq-q[open] summary{border-bottom:1px solid rgba(216,178,90,.22)}
.faq-q[open] summary::after{transform:rotate(225deg) translateY(-3px)}
.faq-q .faq-r{color:#d7d4ea;font-size:15.5px;padding:15px 20px 18px}
/* --- les deux liens descendants vers le blog (maillage, dossier §6) ------ */
.blog-lien{margin-top:32px;font-size:16px}
.blog-lien a{display:inline-flex;align-items:center;gap:11px;color:var(--gold2);padding:11px 0;text-decoration:underline;text-decoration-color:rgba(240,209,138,.4);text-underline-offset:4px}
.blog-lien a::before{content:'';flex:0 0 auto;width:7px;height:7px;border-radius:2px;background:var(--grad-warm);transform:rotate(45deg)}
.blog-lien a:hover{text-decoration-color:var(--gold2)}
@media(max-width:760px){
  section{padding:66px 0}
  .gf-top{padding:110px 0 60px}
  .u-card{padding:26px 22px 22px}
  .cas article{padding:26px 22px 22px}
  .etat{padding:28px 24px}
  .acces{padding:32px 24px 28px}
  .aussi{padding:22px 20px;gap:14px}
  .guilde{padding:22px 20px 20px;gap:14px}
  .etape{padding:20px 18px 18px}
  .faq-q summary{padding:14px 17px;gap:13px}
  .faq-q .faq-r{padding:14px 17px 16px}
}
@media print{.totop{display:none}.kick,.grad-t{-webkit-text-fill-color:var(--gold);color:var(--gold)}}
"""

# --- CSS des 6 maquettes d'interface --------------------------------------
# Repris de `GUSO-FACILE-BACKUPS/maquettes-pour-resonances.html` (LECTURE
# SEULE), avec les corrections listees dans l'entete du fichier. Regles :
#   - aucune couleur litterale : uniquement les var(--…) de la charte, pour
#     qu'une retouche du theme entraine les maquettes avec elle ;
#   - rien sous 13 px (plancher typographique du site, verifie par _controles) ;
#   - `.gf-shot{overflow:hidden}` : une maquette ne peut pas pousser la page,
#     quoi qu'il arrive a l'interieur ;
#   - toutes les rangees sont en `flex-wrap:wrap` avec un `flex-basis` modeste :
#     c'est ce qui les fait tenir dans une colonne de 306 px a 390 px de large.
# Le `:root` du fichier d'origine n'est PAS repris (les variables existent deja
# sur le site), ni son cadre de page `.gf-page-*` (decor de son fichier de
# test), ni le CSS de l'ancienne version en tableau de la maquette 4.
CSS_MAQUETTES = """/* ===== maquettes d'interface (illustrations, pas d'interface reelle) ===== */
.gf-block{margin:34px 0 0;max-width:820px}
.gf-topgrid .gf-block,.univers .gf-block{margin:0;max-width:none}
.univers .gf-wide{grid-column:1/-1}
.gf-shot{position:relative;background:linear-gradient(180deg,#1d1f47,#171935);border:1px solid rgba(255,255,255,.08);border-radius:18px;padding:22px 18px 18px;margin:0 0 11px;color:var(--ink);font-size:15px;line-height:1.5;max-width:100%;overflow:hidden;box-shadow:0 24px 50px -34px rgba(0,0,0,.95)}
.gf-shot::before{content:'';position:absolute;inset:0 0 auto 0;height:2px;background:var(--grad);opacity:.85}
/* la jauge du hero est l'image signature de la page : elle porte un halo */
.gf-topgrid .gf-shot{box-shadow:0 30px 64px -34px rgba(0,0,0,.95),0 0 70px -26px rgba(224,138,114,.45)}
.gf-shot *{box-sizing:border-box}
.gf-cap{display:block;font-size:13px;line-height:1.4;color:var(--muted);letter-spacing:.02em;margin:0 0 0 4px}
.gf-cap::before{content:'';display:inline-block;width:6px;height:6px;border-radius:2px;background:var(--grad-warm);transform:rotate(45deg);margin-right:9px;vertical-align:1px}
/* la note « (a venir) » d'une maquette qui illustre un ecran encore en
   construction (16/08/2026, une seule aujourd'hui : « Mes artistes »). La
   pastille reprend a l'identique celle des puces `.u-card li i` : c'est le
   meme signal, il doit se lire pareil. */
.gf-soon-note{margin:9px 0 0 4px;max-width:66ch;color:var(--muted);font-size:14px;line-height:1.6}
.gf-soon-note i{font-style:normal;display:inline-block;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--plum2);border:1px solid rgba(179,162,228,.4);background:rgba(143,122,209,.12);border-radius:999px;padding:1px 9px;line-height:1.5;margin-right:7px}
.gf-bar{display:flex;align-items:baseline;justify-content:space-between;gap:10px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:10px;margin-bottom:16px}
.gf-bar-t{font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-weight:600;color:var(--ink)}
.gf-bar-s{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
.gf-hint{font-size:13px;color:var(--muted);margin:0 0 14px}
/* 1 — jauge des 507 h : anneau en conic-gradient, aucune image */
.gf-hero{display:flex;gap:20px;align-items:center;flex-wrap:wrap}
.gf-ring{position:relative;flex:0 0 auto;width:146px;height:146px;border-radius:50%;background:conic-gradient(var(--gold) 0 293deg,var(--plum) 293deg 323deg,var(--night2) 323deg 360deg);display:flex;align-items:center;justify-content:center;margin:0 auto}
.gf-ring-in{width:112px;height:112px;border-radius:50%;background:var(--card);display:flex;flex-direction:column;align-items:center;justify-content:center;border:1px solid var(--line)}
.gf-ring-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:38px;line-height:1;font-weight:600;color:var(--gold2)}
.gf-ring-l{font-size:13px;color:var(--muted);margin-top:3px}
.gf-hero-txt{flex:1 1 200px;min-width:0}
.gf-hero-l{font-size:15px;margin:0 0 6px}
.gf-hero-l b{color:var(--gold2);font-weight:600}
.gf-tag{display:inline-block;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--gold);border:1px solid var(--line);border-radius:999px;padding:1px 8px;margin-left:5px}
.gf-anniv{font-size:13px;color:var(--muted);border-left:2px solid var(--gold);padding-left:10px;margin-top:12px}
.gf-split{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px}
.gf-split-c{flex:1 1 140px;min-width:0;background:linear-gradient(180deg,#1b1d42,#15172f);border:1px solid rgba(255,255,255,.07);border-radius:13px;padding:11px 13px}
.gf-split-v{font-size:19px;font-weight:600;color:var(--gold2)}
.gf-split-v.gf-poss{color:var(--plum2)}
.gf-split-k{font-size:13px;color:var(--muted)}
.gf-legend{display:flex;gap:16px;flex-wrap:wrap;margin-top:12px;font-size:13px;color:var(--muted)}
.gf-dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:6px;vertical-align:baseline}
.gf-dot-gold{background:var(--gold)}
.gf-dot-plum{background:var(--plum)}
.gf-dot-empty{background:var(--night2);border:1px solid var(--line)}
/* 2 — « A faire maintenant » : pastilles urgent / en retard / a venir */
.gf-tn-head{display:flex;align-items:baseline;gap:9px;margin-bottom:12px}
.gf-tn-t{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
.gf-tn-n{margin-left:auto;font-size:13px;font-weight:600;color:#1b1206;background:var(--grad-warm);border-radius:999px;padding:1px 9px}
.gf-tn-row{display:flex;align-items:center;gap:11px;flex-wrap:wrap;border:1px solid rgba(255,255,255,.07);border-radius:13px;background:linear-gradient(180deg,#1b1d42,#15172f);padding:12px 13px;margin-bottom:9px}
.gf-tn-pill{flex:0 0 auto;width:10px;height:10px;border-radius:50%}
.gf-tn-pill.gf-urgent{background:var(--gold)}
.gf-tn-pill.gf-late{background:var(--plum)}
.gf-tn-pill.gf-soon{background:transparent;border:2px solid var(--gold)}
.gf-tn-main{flex:1 1 150px;min-width:0}
.gf-tn-lbl{display:block;font-size:15px;font-weight:600;color:var(--ink)}
.gf-tn-meta{display:block;font-size:13px;color:var(--muted)}
.gf-tn-when{flex:0 0 auto;font-size:13px;letter-spacing:.06em;text-transform:uppercase;border:1px solid var(--line);border-radius:999px;padding:2px 9px;color:var(--muted)}
.gf-tn-when.gf-urgent{color:#1b1206;background:var(--grad-warm);border-color:transparent;font-weight:600}
.gf-tn-when.gf-late{color:var(--gold2)}
/* 3 — fiche d'une date et ses cinq etapes administratives */
.gf-kv{display:grid;grid-template-columns:auto minmax(0,1fr);gap:7px 14px;margin:0 0 16px;font-size:15px}
.gf-kv .gf-k{color:var(--muted);font-size:13px;letter-spacing:.04em}
.gf-kv .gf-v{color:var(--ink);font-weight:500;min-width:0;overflow-wrap:anywhere}
.gf-mini{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);margin:0 0 9px}
.gf-steps{display:flex;flex-wrap:wrap;gap:8px}
.gf-step{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--line);border-radius:999px;background:var(--night2);padding:6px 12px;font-size:13px;color:var(--muted)}
.gf-step .gf-box{width:16px;height:16px;border-radius:5px;border:1px solid var(--line);display:inline-flex;align-items:center;justify-content:center;font-size:13px;line-height:1;color:var(--night);flex:0 0 auto}
.gf-step.gf-done{color:var(--ink);border-color:var(--gold)}
.gf-step.gf-done .gf-box{background:var(--gold);border-color:var(--gold)}
/* 4 — recap mensuel France Travail, en cartes groupees par mois */
.gf-recmonth{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin:0 0 10px}
.gf-reccard{border:1px solid rgba(255,255,255,.07);border-radius:13px;background:linear-gradient(180deg,#1b1d42,#15172f);padding:11px 13px;margin-bottom:9px}
.gf-recwhen{font-size:13px;color:var(--muted)}
.gf-recnums{font-size:15px;font-weight:600;color:var(--ink);font-variant-numeric:tabular-nums}
.gf-recnums em{font-style:normal;color:var(--gold2)}
.gf-recmeta{font-size:13px;color:var(--muted);overflow-wrap:anywhere}
.gf-rectot{display:flex;gap:8px 14px;align-items:baseline;flex-wrap:wrap;justify-content:space-between;border-top:1px solid rgba(216,178,90,.55);margin-top:13px;padding-top:12px}
.gf-rl{font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.gf-rv{font-size:15px;font-weight:600;color:var(--gold2);font-variant-numeric:tabular-nums}
/* 5 — ma tournee : enchainement chronologique, filet + pastilles, zero image */
.gf-route{position:relative;margin:0;padding:0 0 0 24px;list-style:none}
.gf-route::before{content:'';position:absolute;left:5px;top:9px;bottom:9px;width:1px;background:var(--line)}
.gf-stop{position:relative;padding:0 0 15px}
.gf-stop:last-child{padding-bottom:0}
.gf-stop::before{content:'';position:absolute;left:-23px;top:6px;width:11px;height:11px;border-radius:50%;background:var(--night2);border:1px solid var(--gold)}
.gf-stop.gf-cur::before{background:var(--gold)}
.gf-stop.gf-tbc::before{border-style:dashed}
.gf-stop-top{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
.gf-stop-city{font-size:15px;font-weight:600;color:var(--ink)}
.gf-stop-st{margin-left:auto;font-size:13px;letter-spacing:.06em;text-transform:uppercase;white-space:nowrap;color:var(--gold);border:1px solid var(--line);border-radius:999px;padding:1px 9px}
.gf-stop.gf-tbc .gf-stop-st{color:var(--plum2)}
.gf-stop-meta{display:block;font-size:13px;color:var(--muted)}
.gf-route-tot{display:flex;gap:8px 20px;align-items:baseline;flex-wrap:wrap;margin-top:16px;border-top:1px solid rgba(216,178,90,.4);padding-top:13px}
.gf-route-tot span{display:block}
.gf-route-tot-p{flex:1 1 130px;min-width:0}
.gf-route-tot-v{font-family:'Cormorant Garamond',Georgia,serif;font-size:26px;line-height:1.15;color:var(--gold2)}
.gf-route-tot-k{font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
/* 6 — tableau de bord d'une structure. La vigilance se lit a la FORME de la
   pastille et a son libelle, pas seulement a la couleur (la charte n'a ni
   vert ni rouge, et un daltonien doit pouvoir la lire). */
.gf-art{display:flex;flex-direction:column;gap:9px}
.gf-art-row{display:flex;align-items:center;gap:12px;flex-wrap:wrap;border:1px solid rgba(255,255,255,.07);border-radius:13px;background:linear-gradient(180deg,#1b1d42,#15172f);padding:12px 13px}
.gf-av{flex:0 0 auto;width:34px;height:34px;border-radius:50%;border:1px solid var(--line);display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:600;color:var(--gold2);background:var(--card)}
.gf-art-txt{flex:1 1 130px;min-width:0}
.gf-art-n{display:block;font-size:15px;font-weight:600}
.gf-art-m{display:block;font-size:13px;color:var(--muted)}
.gf-art-h{flex:0 0 auto;text-align:right;font-variant-numeric:tabular-nums}
.gf-art-hv{font-size:15px;font-weight:600;color:var(--gold2)}
.gf-art-hk{display:block;font-size:13px;color:var(--muted)}
.gf-mbar{flex:1 1 100%;height:5px;margin-top:3px;border-radius:3px;background:var(--night);border:1px solid var(--line);overflow:hidden}
.gf-mbar i{display:block;height:100%;background:var(--grad-warm)}
.gf-vig{flex:0 0 auto;display:inline-flex;align-items:center;gap:6px;font-size:13px;letter-spacing:.05em;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:2px 9px}
.gf-vig-s{width:10px;height:10px;border-radius:50%;flex:0 0 auto}
.gf-vig.gf-ok .gf-vig-s{background:var(--gold)}
.gf-vig.gf-warn .gf-vig-s{background:transparent;border:2px solid var(--gold)}
.gf-vig.gf-bad .gf-vig-s{background:transparent;border:2px solid var(--plum);box-shadow:inset 0 0 0 2px var(--plum)}
.gf-vig.gf-bad{color:var(--ink);border-color:var(--plum2)}
@media(max-width:760px){.gf-shot{padding:15px 13px 13px}}
"""


# =========================================================================
# LES 6 MAQUETTES — le HTML de chaque bloc
# =========================================================================
# ⚠️ REGLE ABSOLUE POUR CES SIX BLOCS : ce sont des ILLUSTRATIONS.
#    Aucun <a>, <button>, <input>, <select>, <textarea>, aucun [tabindex] :
#    rien de focusable, rien de cliquable, rien qui laisse croire au visiteur
#    qu'il manipule le logiciel depuis le site de l'association. Le garde-fou
#    `_controle_maquettes()` refuse d'ecrire la page au premier ecart.
#    Le gabarit est toujours le meme :
#        <figure class="gf-block">
#          <div class="gf-shot" role="img" aria-label="…"> … </div>
#          <figcaption class="gf-cap">Aperçu de l’interface — données fictives</figcaption>
#        </figure>
#    <figure>/<figcaption> plutot que <section> : c'est exactement une
#    illustration accompagnee de sa legende, et cela evite au passage
#    d'heriter du `section{padding:78px 0}` du site.

#: la mention VISIBLE, identique sur les six blocs. Elle n'est pas decorative :
#: une reproduction credible sans mention est indistinguable d'une vraie
#: capture d'ecran. Comptee par `_controle_maquettes()`.
MENTION_FICTIVE = 'Aperçu de l’interface — données fictives'


def _figure(aria, corps, classe='', note=''):
    """Enveloppe un bloc de maquette : role=img + aria-label + mention visible.

    `note` (16/08/2026) : un paragraphe FACULTATIF pose SOUS la legende, pour
    une maquette qui illustre un ecran encore en construction. Il est volontai-
    rement SEPARE du `<figcaption>` : les six legendes doivent rester identiques
    au caractere pres, c'est ce que compte `ANCRES` — une legende qui varie, et
    le controle « chaque maquette porte sa mention de donnees fictives » ne
    detecte plus rien.
    """
    bloc = ('<figure class="gf-block%s">\n'
            '  <div class="gf-shot" role="img" aria-label="%s">%s</div>\n'
            '  <figcaption class="gf-cap">%s</figcaption>\n'
            % (classe, aria, corps, MENTION_FICTIVE))
    if note:
        bloc += '  <p class="gf-soon-note">%s</p>\n' % note
    return bloc + '</figure>\n'


# --- 1. LA JAUGE DES 507 H (hero) ----------------------------------------
# Ecran reproduit : tableau de bord, bloc « Ou j'en suis — periode en cours ».
# C'est l'image signature de l'outil, d'ou sa place dans le hero.
# ⚠️ L'ANNEAU : 412/507 = 81,26 % -> 293deg pour l'arc « heures validees ».
#    Les 43 h de dates possibles valent 43/507 x 360 = 30,5deg, DONC l'arc
#    prune s'arrete a 323deg. Le fichier d'origine ecrivait 336deg (= 293+43),
#    en prenant des heures pour des degres : la jauge annoncait visuellement
#    ~12 % de dates possibles au lieu de 8,5 %. Corrige ici.
# Coherence des donnees fictives (Camille Ferrand) : 28 cachets x 12 h = 336 h,
# + 76 h de repetitions = 412 h. Reste 95 h = 8 cachets, ou 4 cachets + 47 h.
MAQ_JAUGE = _figure(
    'Tableau de bord de Guso Facile : la jauge des 507 heures, 412 heures '
    'validées sur 507, il reste 95 heures à trouver avant la date anniversaire '
    'du 16 août.',
    """
    <div class="gf-bar">
      <span class="gf-bar-t">Où j’en suis — période en cours</span>
      <span class="gf-bar-s">Camille Ferrand</span>
    </div>
    <p class="gf-hint">Période du 17 août 2025 au 16 août 2026 — les 12 mois qui comptent pour les 507 h.</p>
    <div class="gf-hero">
      <div class="gf-ring">
        <div class="gf-ring-in">
          <span class="gf-ring-n">412</span>
          <span class="gf-ring-l">/ 507 h</span>
        </div>
      </div>
      <div class="gf-hero-txt">
        <p class="gf-hero-l">J’ai effectué <b>412 h</b> sur <b>507 h</b><span class="gf-tag">confirmé</span></p>
        <p class="gf-hero-l">Il me reste <b>95 h</b> à trouver</p>
        <p class="gf-hero-l">dans <b>47 jours</b></p>
        <p class="gf-anniv">Date anniversaire le <b>16 août</b> — soit environ 8 cachets, ou 4 cachets et 47 h de répétitions.</p>
      </div>
    </div>
    <div class="gf-split">
      <div class="gf-split-c">
        <div class="gf-split-v">412 h</div>
        <div class="gf-split-k">heures validées — 24 dates confirmées</div>
      </div>
      <div class="gf-split-c">
        <div class="gf-split-v gf-poss">+ 43 h</div>
        <div class="gf-split-k">dates possibles — 3 options à confirmer</div>
      </div>
      <div class="gf-split-c">
        <div class="gf-split-v">28 · 76 h</div>
        <div class="gf-split-k">cachets · heures de répétition</div>
      </div>
    </div>
    <p class="gf-legend">
      <span><span class="gf-dot gf-dot-gold"></span>heures validées</span>
      <span><span class="gf-dot gf-dot-plum"></span>dates possibles</span>
      <span><span class="gf-dot gf-dot-empty"></span>reste à trouver</span>
    </p>
  """)


# --- 2. « A FAIRE MAINTENANT » (fin de #promesse) -------------------------
# Ecran reproduit : bloc #todoNow du tableau de bord, echeances triees par
# urgence. Il repond litteralement a la derniere phrase du paragraphe qui le
# precede : « qu'est-ce que j'ai a faire maintenant ? ».
# L'emoji 🔔 du fichier d'origine a ete retire (charte : aucun emoji).
MAQ_TODO = _figure(
    'Bloc « À faire maintenant » de Guso Facile : trois échéances '
    'administratives triées par urgence — une DPAE à faire dans 2 jours, un '
    'feuillet GUSO en retard et une facture encore à envoyer.',
    """
    <div class="gf-tn-head">
      <span class="gf-tn-t">À faire maintenant</span>
      <span class="gf-tn-n">3</span>
    </div>
    <div class="gf-tn-row">
      <span class="gf-tn-pill gf-urgent"></span>
      <span class="gf-tn-main">
        <span class="gf-tn-lbl">DPAE à faire</span>
        <span class="gf-tn-meta">Théâtre du Pont Tournant, Bordeaux · 12 juin 2026</span>
      </span>
      <span class="gf-tn-when gf-urgent">dans 2 j</span>
    </div>
    <div class="gf-tn-row">
      <span class="gf-tn-pill gf-late"></span>
      <span class="gf-tn-main">
        <span class="gf-tn-lbl">Feuillet GUSO à éditer</span>
        <span class="gf-tn-meta">Le Rocher de Palmer, Cenon · 14 mars 2026</span>
      </span>
      <span class="gf-tn-when gf-late">en retard</span>
    </div>
    <div class="gf-tn-row">
      <span class="gf-tn-pill gf-soon"></span>
      <span class="gf-tn-main">
        <span class="gf-tn-lbl">Facture à envoyer</span>
        <span class="gf-tn-meta">Festival Ouvre-Boîte, Pau · 2 mai 2026</span>
      </span>
      <span class="gf-tn-when gf-late">en attente</span>
    </div>
  """)


# --- 3. LA FICHE D'UNE DATE (grille des univers) --------------------------
# Ecran reproduit : la fenetre de detail d'une date, avec ses CINQ etapes
# administratives — celles de l'app, exactement : DPAE, feuillet GUSO, facture
# reglee, salaire recu, actualisation France Travail.
# ⚠️ Le fichier d'origine listait DEUX FOIS « Salaire recu » (une cochee, une
#    non) et omettait « Actualisation France Travail », alors que son propre
#    aria-label annonce cinq etapes dont trois cochees. Corrige ici.
# L'emoji 🎤 du titre a ete retire (charte : aucun emoji).
MAQ_FICHE = _figure(
    'Fiche d’une date dans Guso Facile : concert au Rocher de Palmer à Cenon '
    'le 14 mars 2026, 2 cachets soit 24 heures, avec les cinq étapes '
    'administratives dont trois sont cochées.',
    """
    <div class="gf-bar">
      <span class="gf-bar-t">Concert — Le Rocher de Palmer, Cenon</span>
      <span class="gf-bar-s">14 mars 2026</span>
    </div>
    <p class="gf-hint">Camille Ferrand · artiste (annexe 10) · date confirmée</p>
    <div class="gf-kv">
      <div class="gf-k">Période</div><div class="gf-v">14 mars 2026</div>
      <div class="gf-k">Lieu</div><div class="gf-v">Le Rocher de Palmer — Cenon (33)</div>
      <div class="gf-k">Cachets</div><div class="gf-v">2 cachets = 24 h</div>
      <div class="gf-k">Répétition</div><div class="gf-v">0 h</div>
      <div class="gf-k">Total comptabilisé</div><div class="gf-v">24 h</div>
      <div class="gf-k">Salaire brut</div><div class="gf-v">1 084,00 €</div>
    </div>
    <p class="gf-mini">Étapes administratives</p>
    <div class="gf-steps">
      <span class="gf-step gf-done"><span class="gf-box">✓</span>DPAE</span>
      <span class="gf-step gf-done"><span class="gf-box">✓</span>Feuillet GUSO</span>
      <span class="gf-step gf-done"><span class="gf-box">✓</span>Salaire reçu</span>
      <span class="gf-step"><span class="gf-box"></span>Facture réglée</span>
      <span class="gf-step"><span class="gf-box"></span>Actualisation France Travail</span>
    </div>
  """)


# --- 4. LE RECAP MENSUEL FRANCE TRAVAIL (#situations) ---------------------
# Ecran reproduit : la fenetre « Recap mensuel », qui groupe les declarations
# par mois — UNE CARTE par declaration, comme dans l'app (buildRecap).
# ⚠️ Le fichier d'origine avait ete refait en cartes, MAIS SANS SON CSS : seul
#    subsistait celui de l'ancienne version en tableau. Les classes .gf-rec*
#    sont donc habillees ici (voir CSS_MAQUETTES).
# ⚠️ « Association Chant Libre » est a LIMOGES (le fichier d'origine la mettait
#    a Pau dans ce bloc et a Limoges dans la tournee).
# Comptes verifies : 2+1+2 = 5 cachets ; 24+12+33 = 69 h ;
#                    1084,00 + 528,00 + 1246,50 = 2 858,50 €.
# Place sous les trois cas d'usage parce qu'il illustre LITTERALEMENT celui de
# Marco (« Le recapitulatif mensuel lui donne une ligne par GUSO »).
MAQ_RECAP = _figure(
    'Récapitulatif mensuel de Guso Facile pour mars 2026 : les déclarations du '
    'mois, chacune avec sa date, ses cachets, ses heures et son salaire brut, '
    'puis le total du mois à reporter sur l’actualisation France Travail.',
    """
    <div class="gf-bar">
      <span class="gf-bar-t">Mes activités à déclarer</span>
      <span class="gf-bar-s">Récap mensuel</span>
    </div>
    <p class="gf-recmonth">Mars 2026</p>
    <div class="gf-reccard">
      <div class="gf-recwhen">14 mars 2026</div>
      <div class="gf-recnums">2 cachets · 24 h · <em>1 084,00 €</em></div>
      <div class="gf-recmeta">Le Rocher de Palmer, Cenon</div>
    </div>
    <div class="gf-reccard">
      <div class="gf-recwhen">21 mars 2026</div>
      <div class="gf-recnums">1 cachet · 12 h · <em>528,00 €</em></div>
      <div class="gf-recmeta">Association Chant Libre, Limoges</div>
    </div>
    <div class="gf-reccard">
      <div class="gf-recwhen">27 au 29 mars 2026</div>
      <div class="gf-recnums">2 cachets · 33 h · <em>1 246,50 €</em></div>
      <div class="gf-recmeta">Scène Nationale, Bayonne · 9 h de répétition</div>
    </div>
    <div class="gf-rectot">
      <span class="gf-rl">Total du mois</span>
      <span class="gf-rv">5 cachets · 69 h · 2 858,50 € bruts</span>
    </div>
  """)


# --- 5. MA TOURNEE (grille des univers) -----------------------------------
# Ecran reproduit : l'espace « Ma tournee » — les dates enchainees
# chronologiquement, les lieux encore a confirmer signales.
# ⚠️⚠️ LE KILOMETRAGE : RETIRE LE 14/08/2026 AU MATIN, RETABLI LE MEME SOIR.
#    HISTOIRE COMPLETE, parce que le sujet a deja coute deux allers-retours :
#      - la note de livraison du fichier d'origine affirmait « L'espace Ma
#        tournee de l'app liste les dates et les contacts, mais NE CALCULE PAS
#        de kilometrage » ; par prudence, le total « 1 240 km » avait donc ete
#        retire de la maquette, et la contradiction avec la puce « Carte des
#        dates » de l'univers 2 (qui l'ecrit au present) laissee a l'arbitrage ;
#      - VERIFICATION FAITE DEPUIS DANS LE CODE DE L'APPLICATION : la fonction
#        est bien LIVREE. `haversineKm()` est appelee, le panneau affiche
#        « ≈ X km parcourus (aller-retour) », les info-bulles donnent le
#        kilometrage par date, et le journal de test releve « 7 dates
#        localisees, ≈ 3 050 km (A/R) », haversine valide sur Paris -> Lyon
#        = 391 km.
#    La note de livraison etait donc en retard sur l'application. Le total est
#    remis dans la maquette ET la puce de l'univers 2 est revenue a sa
#    formulation complete : les deux disent de nouveau la meme chose.
#    ⚠️ L'aria-label de CE bloc a ete complete en consequence (il annonce
#    desormais le kilometrage). C'est la seule maquette dont le libelle a
#    bouge : un lecteur d'ecran ne doit pas manquer un chiffre affiche.
# Coherence du chiffre fictif : domicile en Gironde, aller-retour cumule des
# CINQ dates confirmees (Cenon, Limoges, Bayonne, Pau, Bordeaux) — l'option de
# La Rochelle, non confirmee, n'est pas comptee. L'ordre de grandeur reel de
# ces cinq trajets est d'environ 1 300 km : 1 240 km est plausible et reste
# une donnee fictive, comme le dit la mention sous le bloc.
# Les six etapes ne citent que des dates et des lieux qui existent DEJA dans
# les autres maquettes (Cenon, Limoges, Bayonne, Pau, Bordeaux), plus une
# option a confirmer, seule facon d'illustrer « les lieux a confirmer sont
# signales » sans contredire les autres blocs.
MAQ_TOURNEE = _figure(
    'Espace « Ma tournée » de Guso Facile : six étapes reliées '
    'chronologiquement, de Cenon à La Rochelle, dont cinq dates confirmées et '
    'une option encore à confirmer, soit 8 cachets et environ 1 240 kilomètres '
    'parcourus depuis le domicile, aller-retour compris.',
    """
    <div class="gf-bar">
      <span class="gf-bar-t">Ma tournée — saison 2026</span>
      <span class="gf-bar-s">6 étapes</span>
    </div>
    <ul class="gf-route">
      <li class="gf-stop">
        <span class="gf-stop-top">
          <span class="gf-stop-city">Cenon</span>
          <span class="gf-stop-st">confirmée</span>
        </span>
        <span class="gf-stop-meta">14 mars · Le Rocher de Palmer · 2 cachets</span>
      </li>
      <li class="gf-stop">
        <span class="gf-stop-top">
          <span class="gf-stop-city">Limoges</span>
          <span class="gf-stop-st">confirmée</span>
        </span>
        <span class="gf-stop-meta">21 mars · Association Chant Libre · 1 cachet</span>
      </li>
      <li class="gf-stop">
        <span class="gf-stop-top">
          <span class="gf-stop-city">Bayonne</span>
          <span class="gf-stop-st">confirmée</span>
        </span>
        <span class="gf-stop-meta">27 au 29 mars · Scène Nationale · 2 cachets</span>
      </li>
      <li class="gf-stop">
        <span class="gf-stop-top">
          <span class="gf-stop-city">Pau</span>
          <span class="gf-stop-st">confirmée</span>
        </span>
        <span class="gf-stop-meta">2 mai · Festival Ouvre-Boîte · 2 cachets</span>
      </li>
      <li class="gf-stop gf-cur">
        <span class="gf-stop-top">
          <span class="gf-stop-city">Bordeaux</span>
          <span class="gf-stop-st">confirmée</span>
        </span>
        <span class="gf-stop-meta">12 juin · Théâtre du Pont Tournant · 1 cachet</span>
      </li>
      <li class="gf-stop gf-tbc">
        <span class="gf-stop-top">
          <span class="gf-stop-city">La Rochelle</span>
          <span class="gf-stop-st">à confirmer</span>
        </span>
        <span class="gf-stop-meta">3 juillet · lieu non encore arrêté · option</span>
      </li>
    </ul>
    <p class="gf-route-tot">
      <span class="gf-route-tot-p">
        <span class="gf-route-tot-v">8 cachets</span>
        <span class="gf-route-tot-k">sur 5 dates confirmées · 1 option à confirmer</span>
      </span>
      <span class="gf-route-tot-p">
        <span class="gf-route-tot-v">1 240 km</span>
        <span class="gf-route-tot-k">parcourus depuis le domicile · aller-retour</span>
      </span>
    </p>
  """)


# --- 6. LE TABLEAU DE BORD D'UNE STRUCTURE (grille des univers) -----------
# Ecran reproduit : la vue « Mes artistes » du back-office structure.
# Il illustre l'univers 3 ET le cas de Sophie ; place en PLEINE LARGEUR de la
# grille (.gf-wide) parce que ses rangees sont larges par nature.
# ⚠️ L'aria-label d'origine annoncait un indicateur « vert, orange ou rouge » :
#    la charte n'a ni vert ni rouge, le rendu emploie la FORME de la pastille
#    (pleine / contour / contour epais) et un libelle. Un lecteur d'ecran
#    entendait donc des couleurs absentes de l'ecran. Reecrit avec les trois
#    libelles reellement affiches.
# Barres : 412/507 = 81 % · 348 = 69 % · 261 = 51 % · 154 = 30 %.
#
# ⚠️⚠️ 16/08/2026 — CETTE MAQUETTE EST LA SEULE A PORTER UN « (a venir) ».
#    C'est le point ou la page promettait PLUS que l'application. Verifie dans
#    le code : cette vue « Mes artistes » (chaque artiste, ses heures, son
#    niveau de vigilance) N'EXISTE PAS TELLE QUELLE. Ce qui existe cote
#    structure est une to-do TRANSVERSALE (DPAE / GUSO / factures), utile mais
#    qui ne dit rien de l'etat de sante de chaque artiste. La puce « Points de
#    vigilance cote structure » de l'univers 4 dit deja « (a venir) » — l'image,
#    elle, disait le contraire.
#    LA MAQUETTE ET SON TEXTE SONT CONSERVES A DESSEIN : David a demande que
#    cette vue soit CONSTRUITE POUR DE BON A PARTIR DE CETTE MAQUETTE. C'est en
#    cours cote application.
#    ➜ QUOI RETIRER LE JOUR DU DEPLOIEMENT (on sera prevenu) :
#         1. l'argument `note=` de cet appel a `_figure()` (et lui seul) ;
#         2. faire passer `NB_A_VENIR` de 3 a 2 dans `ANCRES` ;
#         3. retirer l'ancre `class="gf-soon-note"` de `ANCRES`.
#       Le CSS `.gf-soon-note` peut rester : `_figure()` ne l'emet que si une
#       maquette demande une note, et une autre en aura peut-etre besoin.
MAQ_STRUCTURE = _figure(
    'Tableau de bord d’une structure dans Guso Facile : quatre artistes, leur '
    'compteur d’heures sur 507 et leur niveau de vigilance — bon rythme, à '
    'surveiller ou seuil menacé.',
    """
    <div class="gf-bar">
      <span class="gf-bar-t">Mes artistes</span>
      <span class="gf-bar-s">Espace structure</span>
    </div>
    <p class="gf-hint">Chaque artiste, ses heures sur la période, et le niveau de vigilance avant sa date anniversaire.</p>
    <div class="gf-art">
      <div class="gf-art-row">
        <span class="gf-av">CF</span>
        <span class="gf-art-txt">
          <span class="gf-art-n">Camille Ferrand</span>
          <span class="gf-art-m">Chanteuse · anniversaire le 16 août</span>
        </span>
        <span class="gf-art-h"><span class="gf-art-hv">412 h</span><span class="gf-art-hk">/ 507 h</span></span>
        <span class="gf-vig gf-ok"><span class="gf-vig-s"></span>bon rythme</span>
        <span class="gf-mbar"><i style="width:81%"></i></span>
      </div>
      <div class="gf-art-row">
        <span class="gf-av">NB</span>
        <span class="gf-art-txt">
          <span class="gf-art-n">Nadia Belkacem</span>
          <span class="gf-art-m">Violoncelliste · anniversaire le 3 octobre</span>
        </span>
        <span class="gf-art-h"><span class="gf-art-hv">348 h</span><span class="gf-art-hk">/ 507 h</span></span>
        <span class="gf-vig gf-ok"><span class="gf-vig-s"></span>bon rythme</span>
        <span class="gf-mbar"><i style="width:69%"></i></span>
      </div>
      <div class="gf-art-row">
        <span class="gf-av">TR</span>
        <span class="gf-art-txt">
          <span class="gf-art-n">Tomas Riveiro</span>
          <span class="gf-art-m">Percussionniste · anniversaire le 21 juillet</span>
        </span>
        <span class="gf-art-h"><span class="gf-art-hv">261 h</span><span class="gf-art-hk">/ 507 h</span></span>
        <span class="gf-vig gf-warn"><span class="gf-vig-s"></span>à surveiller</span>
        <span class="gf-mbar"><i style="width:51%"></i></span>
      </div>
      <div class="gf-art-row">
        <span class="gf-av">EV</span>
        <span class="gf-art-txt">
          <span class="gf-art-n">Émile Vasseur</span>
          <span class="gf-art-m">Ingénieur du son · anniversaire le 9 juin</span>
        </span>
        <span class="gf-art-h"><span class="gf-art-hv">154 h</span><span class="gf-art-hk">/ 507 h</span></span>
        <span class="gf-vig gf-bad"><span class="gf-vig-s"></span>seuil menacé</span>
        <span class="gf-mbar"><i style="width:30%"></i></span>
      </div>
    </div>
  """, classe=' gf-wide',
    note='<i>(à venir)</i> Cet aperçu montre une vue en cours de construction. '
         'L’espace structure réunit aujourd’hui, tous artistes confondus, les '
         'DPAE, les feuillets GUSO et les factures à faire ; le suivi artiste '
         'par artiste, avec ses heures et son niveau de vigilance, n’est pas '
         'encore livré.')


# =========================================================================
# LES PICTOGRAMMES — dix icones dessinees a la main, en SVG en ligne
# =========================================================================
# ⚠️ AUCUN EMOJI SUR CETTE PAGE. C'est la charte du site, et c'est surtout une
#    demande explicite de David : sortir des emoji « enfantins » au profit
#    d'icones de signature, au trait. La page de reference qui l'a seduit en
#    comptait 71 — on obtient la meme chaleur avec dix traits fins, sans le
#    registre puéril ni la loterie du rendu emoji (qui change d'un systeme a
#    l'autre, et qu'un lecteur d'ecran enonce a voix haute).
#
# TROIS CONTRAINTES TECHNIQUES, chacune pour une raison mesuree :
#
#  a) AUCUN `xmlns` sur ces <svg>. Inutile en HTML (l'analyseur place lui-meme
#     les balises dans l'espace de noms SVG), et surtout : `xmlns` vaut
#     « http://www.w3.org/2000/svg », que le garde-fou des hotes externes de
#     `_controles` lirait comme un domaine tiers et refuserait. Le controle est
#     bon, c'est l'attribut qui est superflu — on ne desarme pas le garde-fou.
#
#  b) `aria-hidden="true"` + `focusable="false"` sur CHAQUE icone. Elles
#     doublent un texte qui est deja la : les enoncer une seconde fois serait
#     du bruit, et sans `focusable="false"` d'anciens moteurs les inserent dans
#     l'ordre de tabulation. Garde-fou : `_controle_icones()`.
#
#  c) UNE SEULE definition de degrade pour toutes (`#gf-ink`), posee en tete de
#     page dans un <svg> de taille nulle. `gradientUnits="userSpaceOnUse"` et
#     non le defaut `objectBoundingBox` : sans cela chaque trace recevrait le
#     degrade entier sur SA boite englobante, et deux icones cote a cote ne
#     seraient plus dans la meme lumiere. Les couleurs y sont ecrites en clair
#     (un attribut `stop-color` ne lit pas les variables CSS de facon fiable) :
#     ce sont exactement --gold2, --gold, --coral et --plum2.
#     La couleur ecrite APRES l'url() est le repli du paint server SVG 1.1 : si
#     le degrade n'etait pas resolu, l'icone reste doree au lieu de disparaitre.

SVG_DEFS = ('<svg class="gf-defs" aria-hidden="true" focusable="false">'
            '<defs><linearGradient id="gf-ink" gradientUnits="userSpaceOnUse" '
            'x1="3" y1="4" x2="21" y2="20">'
            '<stop offset="0" stop-color="#f0d18a"/>'
            '<stop offset=".42" stop-color="#d8b25a"/>'
            '<stop offset=".74" stop-color="#e08a72"/>'
            '<stop offset="1" stop-color="#b3a2e4"/>'
            '</linearGradient></defs></svg>\n')

#: le trace de chacune des dix icones. Grille de 24, trait de 1,4 px, bouts et
#: raccords arrondis : c'est ce qui donne le trait « fin et chaleureux » plutot
#: que le pictogramme d'application administrative.
ICONES = {
    # univers 1 — « Tes droits, maitrises » : un cadran et son aiguille.
    'jauge': '<path d="M3.6 18a8.4 8.4 0 1 1 16.8 0"/><path d="M12 18l4.4-5.4"/>'
             '<circle cx="12" cy="18" r="1.15"/>',
    # univers 2 — « Ta tournee, organisee » : deux reperes relies par la route.
    'route': '<path d="M7.4 4.6a2.7 2.7 0 0 1 2.7 2.7c0 2-2.7 4.6-2.7 4.6S4.7 9.3 4.7 7.3a2.7 2.7 0 0 1 2.7-2.7Z"/>'
             '<circle cx="7.4" cy="7.3" r=".9"/>'
             '<path d="M16.6 12.3a2.7 2.7 0 0 1 2.7 2.7c0 2-2.7 4.6-2.7 4.6s-2.7-2.6-2.7-4.6a2.7 2.7 0 0 1 2.7-2.7Z"/>'
             '<path d="M9.9 11.6c1.7 1.3 2.3 2.7 4.5 3.5" stroke-dasharray="2 2.6"/>',
    # univers 3 — « Ta structure, connectee » : un fronton, pas un gratte-ciel.
    'maison': '<path d="M3.4 20.4h17.2"/><path d="M5.6 20.4V9.8L12 5.6l6.4 4.2v10.6"/>'
              '<path d="M9.6 20.4v-4.8h4.8v4.8"/><path d="M9.6 12.2h4.8"/>',
    # univers 4 — « Ton cercle, solidaire » : trois presences reliees.
    'cercle': '<circle cx="12" cy="5.6" r="2.1"/><circle cx="5.7" cy="16.4" r="2.1"/>'
              '<circle cx="18.3" cy="16.4" r="2.1"/>'
              '<path d="M10.4 7.4 7.2 14.2"/><path d="M13.6 7.4l3.2 6.8"/><path d="M7.8 16.4h8.4"/>',
    # l'encart « la Guilde » — deux anneaux qui se recouvrent : l'alliance,
    # pas la chaine. Volontairement DIFFERENT de 'cercle' (trois presences
    # reliees, univers 4) : l'un dit le groupe, l'autre dit le pacte.
    'guilde': '<circle cx="9.2" cy="12" r="5.3"/><circle cx="14.8" cy="12" r="5.3"/>',
    # cas 1 — atteindre ses 507 heures : le sablier, pas le chronometre.
    'sablier': '<path d="M7.2 3.6h9.6"/><path d="M7.2 20.4h9.6"/>'
               '<path d="M8.4 3.6v3.1c0 2 3.6 3.6 3.6 5.3s-3.6 3.3-3.6 5.3v3.1"/>'
               '<path d="M15.6 3.6v3.1c0 2-3.6 3.6-3.6 5.3s3.6 3.3 3.6 5.3v3.1"/>',
    # cas 2 — pointer France Travail : le mois, et la coche.
    'calendrier': '<rect x="3.5" y="5.2" width="17" height="15.2" rx="3"/>'
                  '<path d="M3.5 9.9h17"/><path d="M8.2 3.6v3.1"/><path d="M15.8 3.6v3.1"/>'
                  '<path d="M9 14.8l2.2 2.2 4-4.3"/>',
    # cas 3 — accompagner quatre artistes : un groupe, pas un organigramme.
    'groupe': '<circle cx="9.2" cy="8.4" r="3.1"/>'
              '<path d="M3.8 19.6c0-3 2.4-5.1 5.4-5.1s5.4 2.1 5.4 5.1"/>'
              '<path d="M16.2 6.2a3.1 3.1 0 0 1 0 6.1"/>'
              '<path d="M17.3 14.8c1.9.7 3 2.4 3 4.8"/>',
    # « Et aussi » — l'etincelle, seul picto ouvertement decoratif de la page.
    'etincelle': '<path d="M11.6 3.6l1.8 4.9 4.9 1.8-4.9 1.8-1.8 4.9-1.8-4.9-4.9-1.8 4.9-1.8Z"/>'
                 '<path d="M18.4 15.4l.7 1.9 1.9.7-1.9.7-.7 1.9-.7-1.9-1.9-.7 1.9-.7Z"/>',
    # la precision « pas un service de l'association » : le cadre, protecteur.
    'bouclier': '<path d="M12 3.5l7 2.5v5.2c0 4.2-2.8 7.4-7 9.3-4.2-1.9-7-5.1-7-9.3V6z"/>'
                '<path d="M9.3 12.1l2 2 3.5-3.9"/>',
    # le bouton unique de la page : la fleche qui invite, sans insister.
    'fleche': '<path d="M4.6 12h13.6"/><path d="M13.1 6.4L18.8 12l-5.7 5.6"/>',
}


def _ic(nom, classe='ic'):
    """Une icone en ligne, decorative (le texte qu'elle accompagne suffit)."""
    return ('<svg class="%s" viewBox="0 0 24 24" fill="none" '
            'stroke="url(#gf-ink) #e3bd7c" stroke-width="1.5" '
            'stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true" focusable="false">%s</svg>' % (classe, ICONES[nom]))


# =========================================================================
# LA FAQ — 6 QUESTIONS/REPONSES EN TEXTE VISIBLE
# =========================================================================
# ⚠️ CE BLOC N'EST PAS DECORATIF. Le `FAQPage` du JSON-LD n'est LEGITIME que si
#    ces 6 questions/reponses figurent REELLEMENT, en texte, dans la page :
#    annoncer a Google une FAQ absente de l'ecran est une violation explicite
#    de ses consignes. `_controle_jsonld()` verifie question par question ET
#    reponse par reponse, en normalisant la seule difference volontaire :
#    l'apostrophe. Le dossier SEO ecrit « C'est », le site ecrit « C’est ».
#
# ⚠️ REPLIEES, PAS EMPILEES. La page mesurait deja 15 151 px de haut a 390 px
#    avant cet ajout ; six reponses ouvertes en auraient ajoute pres de 1 800.
#    `<details>`/`<summary>` sont du HTML natif — aucun JavaScript (regle de la
#    maison), et Google indexe le contenu d'un accordeon. La question reste
#    en `<h3>` a l'interieur du `<summary>` (le modele de contenu de <summary>
#    accepte un titre), comme le demande le dossier SEO.
#
# Texte repris MOT POUR MOT de `presentation.html` (section #faq), qui est
# aussi celui du JSON-LD. Ne pas le reformuler d'un cote sans l'autre.
FAQ = (
    ('C’est quoi le GUSO ?',
     'Le GUSO est le Guichet unique du spectacle occasionnel : le dispositif qui '
     'permet à un employeur dont le spectacle n’est pas l’activité principale de '
     'déclarer et de rémunérer un artiste ou un technicien en une seule démarche. '
     'C’est lui qui produit le feuillet remis à l’artiste après la date.'),
    ('Combien d’heures faut-il pour être intermittent ?',
     'Il faut réunir 507 heures de travail sur les 12 mois qui précèdent sa date '
     'anniversaire pour ouvrir ou renouveler ses droits au titre des annexes 8 et 10 '
     'de l’assurance chômage. Le calcul est glissant : chaque jour, les heures les '
     'plus anciennes sortent du compte.'),
    ('Combien de cachets pour atteindre 507 heures ?',
     'Un cachet équivaut à 12 heures. Il faut donc environ 43 cachets pour atteindre '
     'les 507 heures, si l’on ne compte que des cachets — les heures de répétition et '
     'de technique s’y ajoutent et réduisent d’autant ce nombre.'),
    ('C’est quoi une DPAE, et qui doit la faire ?',
     'La DPAE est la déclaration préalable à l’embauche. Elle est faite par la '
     'structure employeuse, avant le début du contrat, à partir des nom, prénom et '
     'date de naissance de l’artiste. Sur une date jouée à deux, il en faut une par '
     'artiste.'),
    ('Une session de studio compte-t-elle dans les 507 heures ?',
     'Oui. Une session d’enregistrement relève de l’édition phonographique (convention '
     'collective 2121) et n’est pas déclarée via un GUSO, mais elle compte comme un '
     'cachet, soit 12 heures, dans le total des 507 heures.'),
    ('Comment obtenir un accès à Guso Facile ?',
     'L’application est en phase de test : l’accès se fait sur demande, via le '
     'formulaire « Demander un accès ». Chaque demande est étudiée personnellement par '
     'David Lesage, son créateur.'),
)


def _faq_html():
    """Les 6 Q/R en accordeons natifs. Aucun script, aucun [tabindex] ajoute."""
    return ''.join(
        '    <details class="faq-q">\n'
        '      <summary><h3>%s</h3></summary>\n'
        '      <p class="faq-r">%s</p>\n'
        '    </details>\n' % (q, r) for q, r in FAQ)


def build_html():
    """Construit la page complete (sans le menu : il est injecte apres)."""
    B = []
    A = B.append

    A(HEAD)
    A(CSS_BASE)
    A(CSS_PAGE)
    A(CSS_MAQUETTES)
    # Les donnees structurees ferment le <head>. Elles sont posees APRES
    # `</style>` a dessein : `mobile_nav.inject()` et `nav_menu.inject()`
    # ajoutent leur CSS en remplacant la PREMIERE occurrence de `</style>` —
    # rien ne doit s'intercaler entre le CSS de la page et cette balise.
    A('</style>\n')
    A(JSONLD)
    A('</head>\n')
    A('<body id="top">\n')

    # --- barre de navigation ---------------------------------------------
    # Ce <div class="links"> est un GABARIT MINIMAL : `nav_menu.inject()` le
    # remplace integralement par le menu partage des 9 pages. Ne pas essayer
    # d'y ecrire les entrees a la main.
    A("""
<nav class="nav">
  <a href="/" class="brand">Résonances Productions</a>
  <div class="links">
    <a href="/">Accueil</a>
  </div>
</nav>
""")

    # =====================================================================
    # 1. TITRE ET ACCROCHE  (section 1 du contenu fourni)
    # =====================================================================
    # Kicker MODIFIE : « Un outil de Resonances Productions » -> « Cree par
    # David Lesage · relaye par l'association ». Voir l'entete du fichier :
    # l'outil n'est pas porte par l'association a ce jour.
    #
    # Le badge « Beta privee · places limitees » est ICI et non dans la
    # section 6 : l'acces limite doit se voir sans faire defiler la page.
    #
    # MAQUETTE 1 (`MAQ_JAUGE`) — « le tableau de bord avec la jauge des
    #   507 heures », l'image signature de l'outil. Elle est en colonne de
    #   DROITE de ce hero (grille `minmax(0,1fr) 400px` au-dela de 1000 px,
    #   empilee sous le bouton en dessous : l'outil est beaucoup utilise sur
    #   telephone, et la jauge doit y rester la premiere chose qu'on voit
    #   apres le titre).
    #   Ce n'est PAS une capture d'ecran : aucune image n'entre sur cette page
    #   (l'anneau est un `conic-gradient`). Voir l'entete du fichier.
    # Le degrade signature entre en scene des le titre : c'est lui, et non les
    # fonds, qui porte la chaleur de la page (`.grad-t`). Les deux `.mark` sont
    # les seuls soulignements degrades du hero — un par phrase, pas davantage :
    # au-dela, le procede se voit et ne souligne plus rien.
    # AUCUN MOT n'est modifie ici : `<span class="mark">` n'enveloppe que du
    # texte deja valide.
    A(SVG_DEFS)
    # `<main>` : rappel de la section 2 du dossier SEO (« <main>, <article>,
    # <nav> présents »). Il enveloppe tout le contenu editorial, du hero a la
    # FAQ — le menu et le pied de page restent dehors, c'est tout son interet.
    A('<main>\n')
    # ⚠️ LE <h1> A CHANGE LE 15/08/2026 (dossier SEO, section 2.1). Il ne
    #    portait que « Guso Facile », ce que le dossier designe comme « la
    #    principale faiblesse restante » de la page : c'est le signal on-page
    #    le plus fort apres le <title>. Le titre recommande est ecrit ENTIER
    #    dans la balise — la marque en grand, la suite en seconde ligne plus
    #    petite (`.h1-sous`). Aucun texte n'est masque : `textContent` vaut
    #    bien « Guso Facile — la gestion de l’intermittence, simplifiée ».
    A("""
<header class="gf-top"><div class="wrap"><div class="gf-topgrid">
  <div>
  <p class="kick">Créé par David Lesage · relayé par l’association</p>
  <h1 class="grad-t">Guso Facile <span class="h1-sous">— la gestion de l’intermittence, simplifiée</span></h1>
  <p class="gf-claim">L’intermittence est <span class="mark">un métier</span>. La paperasse ne devrait pas en être un deuxième.</p>
  <p class="lead">Guso Facile est un outil web qui prend en charge le suivi administratif du spectacle
    vivant — heures, déclarations, feuillets, factures — pour que les artistes gardent leur énergie
    <span class="mark">là où elle compte</span>.</p>
  <p class="badge">Bêta privée · places limitées</p>
  <div class="cta">
    <a class="btn ghost" href="#acces">Comment demander un accès</a>
  </div>
  </div>
""")
    A(MAQ_JAUGE)
    A("""</div></div></header>
""")

    # =====================================================================
    # 2. LA PROMESSE  (section 2 du contenu fourni — verbatim)
    # =====================================================================
    # MAQUETTE 2 (`MAQ_TODO`) — « A faire maintenant » : DPAE, feuillets et
    #   factures classes par urgence. Elle est posee EN FIN de cette section,
    #   juste sous la phrase qui la nomme (« qu'est-ce que j'ai a faire
    #   maintenant ? ») : c'est la reponse en image a la question du texte.
    A("""
<div class="divider"></div>
<section id="promesse"><div class="wrap">
  <p class="kick">La promesse</p>
  <h2 class="sec-title">Garde ton énergie pour la scène</h2>
  <p class="body">La charge mentale de l’intermittence ne vient pas des heures jouées, mais de tout ce
    qui les entoure : savoir où l’on en est de ses 507 heures, ne pas rater une DPAE, retrouver le
    feuillet GUSO du mois dernier, relancer une facture impayée, et pointer juste chaque fin de mois à
    France Travail. Guso Facile rassemble tout cela en un seul endroit et transforme cette liste diffuse
    en une seule question, posée chaque jour : qu’est-ce que j’ai à faire maintenant ?</p>
  <p class="body">Concrètement, l’artiste saisit ses dates ; l’outil en déduit les heures acquises, les
    échéances, les documents à produire et les sommes à encaisser. Rien à installer : cela fonctionne
    dans un navigateur, sur ordinateur comme sur téléphone.</p>
""")
    A(MAQ_TODO)

    # -------------------------------------------------------------------
    # « Trois etapes, c'est tout » — RAPATRIE DE presentation.html (15/08)
    # -------------------------------------------------------------------
    # Ce bloc n'existait que sur Vercel. Il repond a la seule question que le
    # texte de #promesse laisse en suspens : « oui, mais concretement, je fais
    # quoi ? ». Trois lignes, pas une carte de plus — la page mesure deja
    # 15 000 px sur telephone.
    # ⚠️ Il est place APRES la maquette « À faire maintenant », pas avant :
    #    cette maquette doit rester COLLEE au paragraphe qui la nomme
    #    (« qu'est-ce que j'ai a faire maintenant ? »), c'est tout son sens.
    # ⚠️ Les mots de David sont au TUTOIEMENT sur Vercel (« Tu te concentres
    #    sur ton art »). Ils sont remis au registre NEUTRE du corps de cette
    #    page-ci — regle posee lors de la refonte : les titres tutoient, le
    #    corps informe. Le sens et l'ordre des trois etapes sont intacts.
    A("""
  <p class="kick etapes-t">Comment ça marche — trois étapes, c’est tout</p>
  <div class="etapes">
    <div class="etape">
      <p class="u-num">Étape 1</p>
      <h3>Renseigner son profil</h3>
      <p class="etape-d">Identité, coordonnées bancaires, numéro GUSO, conditions idéales : une seule
        fois, réutilisés partout.</p>
    </div>
    <div class="etape">
      <p class="u-num">Étape 2</p>
      <h3>Ajouter ses dates</h3>
      <p class="etape-d">Concerts, cachets, contrats : l’outil en déduit les heures, les échéances et
        les documents à produire.</p>
    </div>
    <div class="etape">
      <p class="u-num">Étape 3</p>
      <h3>Se laisser guider</h3>
      <p class="etape-d">« À faire maintenant » dit quoi faire, et quand. Le reste du temps est pour
        la musique.</p>
    </div>
  </div>
""")
    A("""</div></section>
""")

    # =====================================================================
    # 3e A L'ECRAN — CAS D'USAGE  (section 5 du contenu fourni — verbatim)
    # =====================================================================
    # ⚠️ SECTION DEPLACEE le 14/08/2026 (refonte visuelle) : elle etait en 5e
    # position, apres l'inventaire des fonctionnalites. Elle est desormais la
    # TROISIEME, juste apres la promesse et AVANT les quatre univers. Motif :
    # sur la page qui a seduit David, ce qui vient tot, ce sont des gens
    # (« On veille les uns sur les autres »), et l'inventaire vient apres. Ici
    # Lea, Marco et Sophie repondent a « est-ce que c'est pour moi ? » ; les
    # 25 puces des univers repondent a « qu'est-ce qu'il y a dedans ? » — on ne
    # lit la seconde question que si l'on a dit oui a la premiere.
    # Le TEXTE de la section n'a pas bouge d'un mot ; seuls son rang et son
    # habillage (cartes a filet degrade, pictogramme) ont change.
    #
    # Lea, Marco et Sophie sont des personnages ENTIEREMENT FICTIFS, confirme
    # le 14/08/2026 par la session qui developpe Guso Facile : les seules
    # personnes reelles de l'app sont David, Iris, Yannick et Christophe.
    # Aucun nom de beta-testeur, aucune coordonnee, aucune donnee reelle ne
    # doit apparaitre ici (depot PUBLIC).
    #
    # ⚠️ LE TITRE DISAIT « Trois situations REELLES » — c'etait FAUX, corrige
    #   le 14/08/2026. Des personnages inventes presentes comme des cas reels,
    #   sous le nom d'une association, c'est un faux temoignage. Le titre dit
    #   desormais « typiques », et la mention « Les prenoms sont fictifs »
    #   figure sous le titre. NE PAS REMETTRE « reelles » : ce serait
    #   retablir l'approximation, sur le point le plus sensible de la page.
    #
    # MAQUETTE 4 (`MAQ_RECAP`) — le recapitulatif mensuel utilise pour le
    #   pointage France Travail. Il illustre LITTERALEMENT le cas de Marco
    #   (« Le recapitulatif mensuel lui donne une ligne par GUSO »), d'ou sa
    #   place a la suite des trois cas, et non dans la section precedente.
    #   Dans l'app le recap s'affiche en CARTES groupees par mois : c'est
    #   cette version-la qui est reproduite, pas un tableau.
    A("""
<div class="divider"></div>
<section id="situations" class="band"><div class="wrap">
  <p class="kick">Cas d’usage</p>
  <h2 class="sec-title">Trois situations typiques</h2>
  <p class="cas-note">Les prénoms sont fictifs ; les situations, elles, sont celles que l’outil rencontre au quotidien.</p>

  <div class="cas">
    <article>
      <span class="cas-ico">""" + _ic('sablier') + """</span>
      <h3>Atteindre ses 507 heures sans angoisse</h3>
      <p>En mars, Léa était à 380 heures et se réveillait la nuit. La jauge lui a montré, non pas le
        chiffre manquant, mais ce qu’il représentait en dates concrètes ; et la projection lui a dit ce
        que ses dates encore incertaines changeraient si elles se confirmaient. Le compte à rebours est
        devenu un plan, mois par mois.</p>
    </article>
    <article>
      <span class="cas-ico">""" + _ic('calendrier') + """</span>
      <h3>Pointer France Travail en cinq minutes</h3>
      <p>Chaque 28 du mois, Marco redoutait son actualisation : retrouver les feuillets, recompter les
        cachets, espérer ne pas se tromper. Le récapitulatif mensuel lui donne une ligne par GUSO, avec
        les heures et le brut déjà calculés. Il recopie, il valide, c’est terminé.</p>
    </article>
    <article>
      <span class="cas-ico">""" + _ic('groupe') + """</span>
      <h3>Accompagner quatre artistes sans tableur</h3>
      <p>Sophie gère quatre artistes au sein d’une structure. Elle voyait passer les DPAE dans ses mails
        et tenait un tableur qui n’était jamais à jour. Le back-office lui affiche désormais, sur un seul
        écran, toutes les déclarations, tous les feuillets et toutes les factures à faire, classés par
        échéance et tous artistes confondus.</p>
    </article>
  </div>
""")
    A(MAQ_RECAP)

    # -------------------------------------------------------------------
    # PREMIER des deux liens descendants vers le blog (dossier SEO, §6)
    # -------------------------------------------------------------------
    # Regle du dossier : ancre DESCRIPTIVE, jamais « en savoir plus » ni
    # « lire la suite ». Placement repris de la page Vercel, qui pose le meme
    # lien juste apres ses cas d'usage : trois situations donnent envie d'en
    # lire d'autres, et il y en a dix-huit de l'autre cote.
    # ⚠️ `/guso-facile/blog` est construit par `generate_guso_blog.py`, un
    #    AUTRE generateur. Tant que le dossier n'existe pas, `verif_site.py`
    #    signale un « lien interne mort » — a juste titre, et ce n'est pas un
    #    defaut de cette page-ci.
    A("""
  <p class="blog-lien"><a href="/guso-facile/blog">D’autres cas d’usage concrets sur le blog de Guso Facile</a></p>
""")
    A("""</div></section>
""")

    # =====================================================================
    # 4. LES FONCTIONNALITES  (section 4 du contenu fourni — verbatim)
    # =====================================================================
    # Quatre blocs, intitules en Cormorant Garamond, puces en point d'or.
    # Aucun emoji, conformement a la charte.
    #
    # LES TROIS MAQUETTES DE CETTE SECTION sont des elements de la grille
    # `.univers`, pas des blocs poses a cote d'elle : la grille est a DEUX
    # colonnes au-dela de 761 px, la lecture donne donc
    #     univers 1 | univers 2
    #     fiche de date | ma tournee
    #     univers 3 | univers 4
    #     tableau de bord structure (pleine largeur)
    # et, en une colonne sur telephone, le meme ordre a la verticale.
    # ⚠️ NI la Guilde NI « Je cree mon contrat » ne sont illustrees : ces deux
    #    fonctionnalites sont « (a venir) » (la base existe, l'ecran non). Les
    #    mettre en image les ferait passer pour livrees, ce que trois clics
    #    d'un beta-testeur suffiraient a dementir.
    A("""
<div class="divider"></div>
<section id="fonctionnalites"><div class="wrap">
  <p class="kick">Les fonctionnalités</p>
  <h2 class="sec-title">Bien plus qu’un compteur d’heures</h2>

  <div class="univers">

    <article class="u-card">
      <div class="u-head">
        <span class="u-ico">""" + _ic('jauge') + """</span>
        <div>
          <p class="u-num">Univers 1</p>
          <h3>Tes droits, maîtrisés</h3>
        </div>
      </div>
      <p class="u-sub">Ne plus jamais perdre une heure ni rater une échéance.</p>
      <ul>
        <li><b>Jauge des 507 heures</b> — la progression vers l’ouverture de droits, toujours visible.</li>
        <li><b>« À faire maintenant »</b> — DPAE, feuillets GUSO et factures à venir, classés par urgence (J-3, J-7).</li>
        <li><b>Alertes de cohérence</b> — un badge « droits sécurisés » dès 507 heures, et un signalement cliquable dès qu’une incohérence se glisse dans les dates saisies.</li>
        <li><b>Récapitulatif mensuel</b> — GUSO, cachets, heures et brut mois par mois, prêt à reporter dans l’actualisation France Travail.</li>
        <li><b>Bilan imprimable</b> — un contrôle de cohérence complet de la période, exporté en un document propre.</li>
        <li><b>Graphique annuel</b> — les heures acquises, et ce que les dates encore « possibles » ajouteraient à la projection.</li>
"""
      # -------------------------------------------------------------------
      # « Profil complet » — RAPATRIE DE presentation.html (15/08/2026)
      # -------------------------------------------------------------------
      # Fonctionnalite LIVREE, donc au present, sans mention « a venir ».
      # Elle manquait ici parce qu'elle ne figure PAS dans les quatre univers
      # de la page Vercel : elle vit dans sa section « Pour les artistes »,
      # qui resume les memes univers autrement. C'est le seul endroit ou
      # l'inventaire des univers etait reellement incomplet cote artiste.
      # « IBAN » est ecrit « coordonnees bancaires », comme partout ailleurs
      # sur cette page (et le mot brut cotoie mal le controle anti-IBAN).
      """        <li><b>Profil complet</b> — identité, coordonnées bancaires, instruments et contrats, renseignés une seule fois et prêts à partager avec une structure.</li>
      </ul>
    </article>

    <article class="u-card">
      <div class="u-head">
        <span class="u-ico">""" + _ic('route') + """</span>
        <div>
          <p class="u-num">Univers 2</p>
          <h3>Ta tournée, organisée</h3>
        </div>
      </div>
      <p class="u-sub">Développer, relancer, négocier — et savoir avant de dire oui.</p>
      <ul>
        <li><b>Carte des dates</b> — les concerts géolocalisés, avec le calcul des kilomètres parcourus depuis le domicile, utile pour les frais.</li>
        <li><b>Tournée reliée</b> — les dates s’enchaînent chronologiquement sur la carte, les lieux à confirmer sont signalés, les adresses en autocomplétion.</li>
        <li><b>Carnet de contacts</b> — les organisateurs rassemblés automatiquement, avec l’historique des dates jouées ensemble.</li>
        <li><b>Modèles de mails</b> — relance, présentation, remerciement, pré-remplis avec la dernière date jouée avec l’interlocuteur.</li>
        <li><b>Évaluation d’une proposition</b> — l’offre reçue comparée aux conditions idéales de l’artiste, avec un verdict vert, jaune ou rouge avant de s’engager.</li>
        <li><b>Suivi de négociation</b> — statut du contrat, échéance de signature, informations manquantes, et une demande d’informations prête à envoyer.</li>
"""
      # -------------------------------------------------------------------
      # « Je cree mon contrat » — FONCTIONNALITE LIVREE (corrige le 16/08/2026)
      # -------------------------------------------------------------------
      # HISTOIRE, parce qu'elle explique la forme de la ligne : au 14/08/2026 le
      # modele d'engagement en 12 rubriques existait EN BASE mais l'ECRAN non ;
      # la puce etait donc `class="soon"` + `<i>(a venir)</i>`. LE 16/08/2026,
      # l'etat des lieux releve dans le code dit que L'ECRAN EXISTE ET EST
      # DEPLOYE. La mention est donc retiree, et la puce reprend le marqueur
      # plein des fonctionnalites livrees. Le TEXTE n'a pas bouge d'un mot : il
      # etait deja formule cote CAPACITE (« pour poser un cadre clair »), pas
      # cote contenu — il passe au present sans retouche.
      # Cette ligne est placee dans l'univers 2 (« Ta tournee, organisee »)
      # parce que c'est la que se traite la relation a l'organisateur :
      # evaluation de la proposition, puis suivi de negociation, puis contrat.
      """        <li><b>Je crée mon contrat</b> — un modèle d’engagement en 12 rubriques, personnalisable, pour poser un cadre clair avec l’organisateur.</li>
      </ul>
    </article>
""")

    # MAQUETTE 3 (`MAQ_FICHE`) — la fiche d'une date et ses cinq etapes
    #   administratives, et MAQUETTE 5 (`MAQ_TOURNEE`) — l'enchainement
    #   chronologique des dates. Elles closent la rangee des univers 1 et 2 :
    #   la premiere montre ce que devient UNE date une fois saisie, la seconde
    #   ce que devient la SUITE des dates. (Le kilometrage annonce dans le
    #   fichier d'origine a ete retire : voir l'entete, il ne correspond a
    #   aucune fonction livree.)
    A(MAQ_FICHE)
    A(MAQ_TOURNEE)

    A("""
    <article class="u-card">
      <div class="u-head">
        <span class="u-ico">""" + _ic('maison') + """</span>
        <div>
          <p class="u-num">Univers 3</p>
          <h3>Ta structure, connectée</h3>
        </div>
      </div>
      <p class="u-sub">Pour celles et ceux qui emploient et accompagnent les artistes.</p>
      <ul>
        <li><b>Back-office transversal</b> — toutes les DPAE, feuillets GUSO et factures à faire, tous artistes confondus, au même endroit.</li>
        <li><b>Fiches artistes</b> — état civil, numéro de sécurité sociale, numéro GUSO, accessibles en un clic pour remplir une DPAE sans rien redemander.</li>
        <li><b>DPAE regroupées</b> — les dates proches (à sept jours près) rassemblées pour tout déclarer d’un coup.</li>
        <li><b>Factures et salaires</b> — dépôt des factures, marquage « facture réglée » et « salaire reçu » : qui est payé, ce qui reste dû.</li>
        <li><b>Multi-artistes</b> — conditions idéales, coordonnées bancaires, contrats, plusieurs artistes gérés côte à côte.</li>
        <li><b>Fiche structure</b> — SIRET, coordonnées bancaires et coordonnées postales centralisés, réutilisés partout.</li>
        <li><b>Synchronisation</b> — ce que l’artiste renseigne apparaît côté structure en temps réel, et inversement.</li>
      </ul>
    </article>

    <article class="u-card">
      <div class="u-head">
        <span class="u-ico">""" + _ic('cercle') + """</span>
        <div>
          <p class="u-num">Univers 4</p>
          <h3>Ton cercle, solidaire</h3>
        </div>
      </div>
      <p class="u-sub">Parce qu’on avance mieux à plusieurs. Deux points y sont encore en construction, marqués « à venir ».</p>
      <ul>
        <li><b>Vue groupe</b> — où en est chaque membre du groupe, pour se soutenir avant que la situation ne coince.</li>
        <li><b>« J’ai besoin d’aide »</b> — trois questions simples, un premier conseil concret, et la possibilité de prévenir qui l’on veut.</li>
"""
      # -------------------------------------------------------------------
      # « Faire decouvrir l'outil » (cooptation) — FONCTIONNALITE LIVREE
      # -------------------------------------------------------------------
      # Celle-ci EST en production (etat au 14/08/2026) : elle s'ecrit donc au
      # PRESENT, sans mention « a venir ». Texte repris quasi verbatim de la
      # session qui developpe Guso Facile ; seule la ponctuation a ete alignee
      # sur le gabarit des puces (titre en <b>, tiret cadratin, puis la
      # phrase). Ne pas la reformuler en promesse commerciale : la derniere
      # phrase (« Chaque acces reste une decision, jamais une inscription
      # automatique ») dit la meme chose que les deux mentions sous le bouton
      # de la section « Manifester son interet » — c'est voulu, la page doit
      # etre coherente d'un bout a l'autre sur ce point.
      """        <li><b>Faire découvrir l’outil</b> — un membre peut recommander Guso Facile à un autre artiste : il renseigne ses coordonnées, l’application prépare un message qu’il peut modifier, et la demande arrive chez David, qui l’étudie personnellement. Chaque accès reste une décision, jamais une inscription automatique.</li>
"""
      # ===================================================================
      # ⚠️⚠️ « L'ENTRAIDE ENTRE ARTISTES » (la Guilde) — CONTRAINTE
      #        REDACTIONNELLE STRICTE. LIRE AVANT DE TOUCHER A CE BLOC.
      # ===================================================================
      # 1. FONCTIONNALITE LIVREE DEPUIS LE 16/08/2026 — mais LIVREE NE VEUT PAS
      #    DIRE PEUPLEE. L'ecran existe et il est deploye (au 14/08 seule la
      #    base existait : le bloc etait alors `class="soon"` + « (a venir) »),
      #    SEULEMENT AUCUNE DONNEE N'Y A ENCORE ETE SAISIE : zero lieu, zero
      #    retour. La puce decrit donc une CAPACITE — ce qu'un membre peut y
      #    faire — et JAMAIS UN CONTENU. Ecrire « consulte les retours
      #    d'artistes sur des centaines de lieux » promettrait un espace vide :
      #    c'est pire qu'un « a venir » de trop, et c'est refuse a l'ecriture
      #    par `MOTS_INTERDITS_ABONDANCE`.
      #    Seuls DEUX VERBES ont bouge le 16/08 : « on partagera » -> « on
      #    partage », « l'outil proposera » -> « l'outil propose ». Rien
      #    d'autre : le texte etait deja ecrit cote capacite.
      #
      # 2. LE POINT DELICAT : cette fonctionnalite fait porter a des artistes
      #    des AFFIRMATIONS FACTUELLES SUR DES EMPLOYEURS IDENTIFIABLES. Elle
      #    est reservee aux membres connectes, mais LA PAGE QUI LA DECRIT EST
      #    PUBLIQUE ET INDEXEE. Si ce paragraphe se lit comme « une plateforme
      #    qui note les employeurs du spectacle », un programmateur mecontent
      #    ecrira a l'association — qui n'heberge meme pas l'outil.
      #
      # 3. VOCABULAIRE INTERDIT DANS CE BLOC, sans exception ni synonyme
      #    deguise :
      #        noter · notation · signaler · denoncer · avis · evaluation ·
      #        blacklist · reputation
      #    (Ces mots existent ailleurs sur la page — « signaler un bug »,
      #     « Evaluation d'une proposition » — c'est normal : l'interdit porte
      #     sur CE bloc, et le garde-fou `_controle_guilde()` plus bas ne
      #     controle que lui.)
      #
      # 4. POINTS D'APPUI a utiliser si le texte doit un jour etre retravaille :
      #        - reserve aux MEMBRES CONNECTES : jamais public, jamais indexe ;
      #        - uniquement des FAITS BINAIRES (contrat fourni / pas fourni,
      #          paye dans les delais / non) ;
      #        - AUCUN commentaire libre, AUCUN espace de debat ;
      #        - la sortie proposee est constructive (un modele de contrat a
      #          poser la prochaine fois), pas punitive.
      #
      # 5. Le texte ci-dessous est celui VALIDE par la session qui developpe
      #    Guso Facile, repris quasi verbatim. Seule la ponctuation a ete
      #    adaptee au gabarit des puces. Ne pas le « fluidifier ».
      """        <li><b>L’entraide entre artistes</b> — entre membres, on partage ce qui s’est
          concrètement passé sur une date : le contrat a-t-il été fourni, le paiement est-il arrivé dans les
          délais, les conditions annoncées ont-elles été tenues. Rien que des faits, jamais d’appréciation.
          L’idée n’est pas de juger qui que ce soit, mais de s’informer entre pairs — comme on le fait déjà
          de bouche à oreille, en tournée ou en loge. Et quand le cadre a manqué, l’outil propose plutôt
          d’aider à le poser la prochaine fois, avec un modèle de contrat prêt à personnaliser.</li>
        <li class="soon"><b>Points de vigilance côté structure</b> <i>(à venir)</i> — qui approche du seuil, qui aurait besoin d’un coup de main.</li>
        <li class="soon"><b>Confidentialité graduée</b> <i>(à venir)</i> — chaque artiste choisit exactement ce que chaque structure voit de ses données.</li>
      </ul>
    </article>
""")

    # MAQUETTE 6 (`MAQ_STRUCTURE`) — la vue « Mes artistes » du back-office.
    #   Pleine largeur de la grille (`.gf-wide`) : ses rangees sont larges par
    #   nature, et c'est l'ecran qui parle aux STRUCTURES — donc aussi a
    #   l'association elle-meme, qui accompagne des artistes.
    A(MAQ_STRUCTURE)

    # ===================================================================
    # ⚠️⚠️ L'ENCART « LA GUILDE » — MEME CONTRAINTE REDACTIONNELLE STRICTE
    #        QUE LA PUCE « L'entraide entre artistes ». LIRE AVANT DE TOUCHER.
    # ===================================================================
    # SOURCE : `GUSO-FACILE-BACKUPS/manifeste-la-guilde.md` (LECTURE SEULE),
    # qui existe en TROIS longueurs. Retenues ici : l'ACCROCHE (version tres
    # courte) en phrase d'ouverture, puis l'ENCART (version courte) en corps.
    # PAS la version longue : ceci est une page produit, pas un manifeste, et
    # la page mesure deja 15 000 px sur telephone. La version longue fera un
    # excellent article de blog.
    #
    # 1. FONCTIONNALITE LIVREE DEPUIS LE 16/08/2026 (au 14/08 seule la base
    #    existait, et le titre portait `<i>(à venir)</i>` : la mention est
    #    retiree). ⚠️ LIVREE NE VEUT PAS DIRE PEUPLEE : aucune donnee n'y a
    #    encore ete saisie, zero lieu, zero retour. L'encart decrit donc ce que
    #    la Guilde PERMET, jamais ce qu'elle CONTIENT. Trois futurs sont passes
    #    au present ce jour-la, et eux seuls : « La Guilde fera donc deux
    #    choses » -> « fait donc deux choses », « Cet espace sera reserve » ->
    #    « est reserve ». Le reste du texte est celui du manifeste, intact.
    #
    # 2. LE POINT DELICAT, identique a celui de la puce : des artistes y
    #    portent des AFFIRMATIONS FACTUELLES SUR DES EMPLOYEURS
    #    IDENTIFIABLES, et LA PAGE QUI LE DECRIT EST PUBLIQUE ET INDEXEE. Ce
    #    bloc ne doit jamais se lire comme « une plateforme qui note les
    #    employeurs du spectacle ».
    #
    # 3. VOCABULAIRE INTERDIT ICI, sans exception ni synonyme deguise :
    #        noter · notation · signaler · denoncer · avis · evaluation ·
    #        blacklist · reputation
    #    + depuis le 16/08/2026 le vocabulaire d'ABONDANCE (centaines, milliers,
    #    « deja repertories », « consulter les retours »…), qui promettrait un
    #    contenu que l'espace n'a pas encore.
    #    Garde-fou : `_controle_guilde_encart()`, jumeau de `_controle_guilde()`.
    #
    # 4. CE QUI A ETE ADOUCI PAR RAPPORT AU MANIFESTE (esprit garde) :
    #      - « dans ce metier, l'abus est ordinaire. Pas spectaculaire :
    #        ORDINAIRE. » -> « ce qui manque le plus souvent n'est pas la bonne
    #        foi : c'est le cadre. » Le manifeste parle a des membres
    #        connectes ; ici la phrase serait lue par un programmateur, sur le
    #        site d'une association, comme un constat d'abus porte par elle.
    #      - « personne ne reste seul face a un abus » -> « personne ne reste
    #        seul ». Meme motif, et l'accroche y gagne en rythme.
    #      - « Pas d'appreciation, pas de recit, pas de reglement de comptes.
    #        Ce n'est ni un espace therapeutique, ni un tribunal » -> « Rien
    #        que des faits, aucun commentaire libre, aucun tribunal. » Trois
    #        negations valent mieux que six : au-dela, se defendre devient se
    #        justifier.
    #      - AJOUTE, demande explicite des « Notes d'emploi » du manifeste :
    #        « Cet espace sera reserve aux membres connectes de Guso Facile »
    #        — sinon on cree de la frustration chez un lecteur qui cliquerait.
    #      - Aucun lieu, aucune personne nommes : les deux phrases citees sont
    #        generiques et le restent, comme l'exige le manifeste.
    #
    # 5. PLACEMENT : juste apres la grille des univers, donc juste apres
    #    l'univers 4 « Ton cercle, solidaire » dont il donne le nom et le
    #    pourquoi. La puce dit CE QUE ce sera ; l'encart dit POURQUOI. Aucune
    #    des deux ne se suffit : la puce sans le motif est un gadget, le motif
    #    sans la puce est un discours.
    A("""
  </div>

  <div class="guilde">
    <span class="ic-w">""" + _ic('guilde') + """</span>
    <div>
      <p class="u-num">Ce cercle a un nom — la Guilde</p>
      <p class="guilde-claim">Une guilde d’artistes qui se soutiennent. On pose le cadre avant, on se dit
        les faits après, personne ne reste seul.</p>
      <p class="guilde-p">Une guilde, c’est un groupe de gens du même métier qui se protègent
        mutuellement. Dans le spectacle, ce qui manque le plus souvent n’est pas la bonne foi : c’est le
        cadre. Pas de contrat, des conditions dites à l’oral, un montant « on verra ». Et il suffit
        parfois d’une phrase — « tu vas jouer devant du monde, ça va te faire connaître » — pour que la
        valeur s’inverse : celui qui apporte son travail se retrouve à recevoir une faveur. Cela
        fonctionne, parce qu’un artiste a besoin de jouer pour exister.</p>
      <p class="guilde-p">La Guilde fait donc deux choses : donner de quoi <b>poser le cadre avant</b> —
        contrat, conditions, délais de paiement — et permettre de <b>se dire les faits après</b>, entre
        membres : payé ou non, dans les délais ou non, conditions annoncées tenues ou non. Rien que des
        faits, aucun commentaire libre, aucun tribunal. Cet espace est réservé aux membres connectés de
        Guso Facile.</p>
    </div>
  </div>

  <div class="aussi">
    <span class="ic-w">""" + _ic('etincelle') + """</span>
    <div>
      <p class="u-num">Et aussi</p>
      <p>Export et import des données · fonctionne sur mobile sans installation · liens directs vers une
        date · comptes sécurisés · un bouton pour signaler un bug depuis n’importe quel écran.</p>
    </div>
  </div>
</div></section>
""")

    # =====================================================================
    # 5e A L'ECRAN — LE LIEN AVEC L'ASSOCIATION  (section 3, CORRIGEE)
    # =====================================================================
    # ⚠️ SECTION DEPLACEE le 14/08/2026 (refonte visuelle) : elle etait la
    # TROISIEME, entre la promesse et les fonctionnalites. Elle est desormais
    # la CINQUIEME, juste avant « Ou en est le projet ». Motif : c'est du
    # CADRE (qui porte quoi, qui heberge quoi), pas de la seduction — et elle
    # tombait pile a l'endroit ou un artiste decide s'il continue de lire. Le
    # cadre se lit tres bien juste avant l'etat du projet, avec lequel il
    # forme un bloc coherent (« voila d'ou ca vient, voila ou ca en est »),
    # et juste avant le seul bouton de la page.
    # ⚠️ AUCUN MOT n'a change : ni le titre, ni la phrase d'ouverture, ni la
    # precision finale — qui gagne meme en visibilite (elle passe de mention
    # grise en pied de section a encadre a filet prune). Si David prefere
    # cette section plus haut, c'est un seul bloc a remonter.
    #
    # ⚠️ SECTION LA PLUS SENSIBLE DE LA PAGE. Lire l'entete du fichier avant
    # d'y toucher : « porte par », « projet de l'association », « mis a
    # disposition par l'association » sont FAUX a ce jour et seraient
    # ecrits sur le site public d'une association a propos d'un outil qui
    # traite des numeros de securite sociale et des IBAN.
    #
    # L'argumentaire du contenu fourni est conserve tel quel — il est bon :
    # un outil qui simplifie l'administratif des intermittents entre
    # pleinement dans l'objet d'une structure de soutien aux artistes. Seul
    # le lien juridique est corrige.
    A("""
<div class="divider"></div>
<section id="association-lien" class="band"><div class="wrap">
  <p class="kick">Le lien avec l’association</p>
  <h2 class="sec-title">Pourquoi Résonances Productions le relaie</h2>
  <p class="body">Guso Facile est un outil <b>créé par David Lesage</b>, musicien intermittent et
    co-fondateur de l’association. Résonances Productions le <b>relaie</b> parce qu’il sert directement
    son objet : le soutien aux artistes.</p>
  <p class="body">L’objet de Résonances Productions est le soutien et la promotion des artistes. Ce
    soutien est d’abord artistique, mais il est aussi, très concrètement, administratif : une grande
    part du temps que l’association passe auprès des artistes qu’elle accompagne est consacrée à des
    déclarations, des feuillets et des échéances. Guso Facile est né de ce constat, et son développement
    continue de se nourrir des retours des artistes qui l’utilisent.</p>
  <div class="precision">
    <span class="ic-w">""" + _ic('bouclier') + """</span>
    <p>Précision : Guso Facile n’est pas un service de l’association. L’outil, son
      hébergement et les données qu’il traite relèvent de son créateur.</p>
  </div>
</div></section>
""")

    # =====================================================================
    # 6. L'ETAT DU PROJET  (section 6 du contenu fourni — verbatim)
    # =====================================================================
    # ⚠️ NE PAS DURCIR CES FORMULATIONS. Le futur payant (« probablement
    # payant », « rien n'est chiffre a ce jour ») et l'affiliation (« un
    # systeme est prevu », « par exemple sous la forme de ») sont ecrits au
    # conditionnel EXPRES : rien n'est arrete, et une promesse commerciale
    # ferme sur le site d'une association serait un probleme.
    A("""
<div class="divider"></div>
<section id="etat"><div class="wrap">
  <p class="kick">L’état du projet</p>
  <h2 class="sec-title">Jouons cartes sur table</h2>

  <div class="etat">
    <p class="first">Guso Facile est aujourd’hui en bêta privée, avec un nombre de places limité.</p>
    <p>Ce n’est pas un prototype. L’outil a été construit par un musicien intermittent pour son propre
      usage, et il a été éprouvé en interne pendant des mois sur des données réelles : celles de deux
      artistes professionnels, soit 65 dates de concerts, de répétitions et de sessions studio sur deux
      saisons complètes, avec les feuillets GUSO, les factures et le pointage France Travail
      correspondants. Il a donc déjà tourné en conditions réelles avant d’être ouvert à d’autres.</p>
    <p>L’accès se fait sur invitation ou sur cooptation, et chaque demande est étudiée personnellement.
      En contrepartie de cet accès, il est demandé aux bêta-testeurs de jouer le jeu des retours :
      signaler les bugs, proposer des améliorations, dire ce qui manque. C’est le seul engagement
      demandé.</p>
    <p>À terme, l’outil sera probablement payant — le développer et le maintenir demande du temps. Un
      système d’affiliation est prévu pour récompenser celles et ceux qui le font découvrir, par exemple
      sous la forme d’un tarif préférentiel sur leur propre abonnement. Rien n’est chiffré à ce jour, et
      les bêta-testeurs seront prévenus bien en amont.</p>
"""
      # -------------------------------------------------------------------
      # La cloture — RAPATRIEE DE presentation.html (15/08/2026), verbatim
      # -------------------------------------------------------------------
      # Mots de David. Elle manquait ici : la section s'arretait sur le futur
      # payant, c'est-a-dire sur la seule reserve de tout le bloc. Cette
      # phrase referme « Jouons cartes sur table » sur ce qu'elle voulait dire.
      # ⚠️ Elle TUTOIE (« avec toi »). C'est assume et c'est pour cela qu'elle
      #    est rendue en SERIF ITALIQUE, le registre des titres de cette page
      #    — les titres accueillent et tutoient, le corps informe et reste
      #    neutre. Si David prefere, c'est UNE ligne a retirer.
      """    <p class="etat-fin">En résumé : un outil déjà solide, une porte encore étroite, et une envie
      sincère de le construire avec toi.</p>
  </div>
</div></section>
""")

    # =====================================================================
    # 7. APPEL A L'ACTION  (section 7 du contenu fourni)
    # =====================================================================
    # UN SEUL bouton sur toute la page, ici. `target="_blank"` + `rel="noopener"`
    # (le lien sort du site : c'est un service distinct, pas une page du site).
    #
    # Les DEUX mentions sous le bouton sont indispensables :
    #  - la premiere dit comment se passe la demande (aucune inscription
    #    automatique) ;
    #  - la seconde nomme le RESPONSABLE DE TRAITEMENT des donnees. La page
    #    oriente en effet vers une collecte de nom, prenom, e-mail, telephone
    #    et nature du demandeur, hebergee ailleurs que sur le site de
    #    l'association. Elle renvoie a la mention portee par le formulaire
    #    lui-meme (usage limite a la creation du compte et au recontact, pas
    #    de demarchage, pas de revente, pas de partage a des tiers,
    #    suppression sur demande) sans la recopier.
    #
    # PAS DE MAQUETTE ICI, C'EST DELIBERE. Le sixieme emplacement prevu etait
    # « la modale Demander un acces », a poser a cote du bouton. Ecarte : c'est
    # le seul endroit de la page ou l'on CLIQUE vraiment, et y coller la
    # reproduction d'une fenetre avec ses champs — non focusables, donc morts
    # au clic — juste a cote du vrai bouton, c'est fabriquer une hesitation
    # a l'endroit exact ou il ne doit pas y en avoir. Cinq maquettes qui
    # montrent l'outil valent mieux qu'une sixieme qui brouille l'action.
    A(("""
<div class="divider"></div>
<section id="acces" class="band"><div class="wrap">
  <div class="acces">
    <p class="kick">Faire connaissance</p>
    <h2 class="sec-title">Reprends la main sur ton administratif</h2>
    <p class="body">Puisque l’accès est limité, il n’y a pas d’inscription immédiate : on commence par
      se dire bonjour. Le formulaire « Demander un accès » recueille le nom, le prénom, l’adresse
      e-mail, le numéro de téléphone et la nature du demandeur — artiste ou structure. Chaque demande
      est ensuite lue et traitée personnellement, et une réponse est apportée par e-mail.</p>
    <div class="cta">
      <a class="btn" href="URL_ACCES" target="_blank" rel="noopener">Demander un accès""" + _ic('fleche') + """</a>
    </div>
    <p class="mention">Le bouton « Demander un accès » se trouve en haut et en bas de la page de
      présentation. Aucune inscription automatique : chaque demande est étudiée personnellement.</p>
    <p class="mention">Le formulaire d’accès est hébergé par Guso Facile ; les informations transmises
      sont traitées par David Lesage, créateur de l’outil, uniquement pour l’étude de votre demande.
      Le formulaire porte sa propre mention d’information.</p>
  </div>
</div></section>
""").replace('URL_ACCES', URL_ACCES))

    # =====================================================================
    # 8. LA FAQ  (rapatriee de presentation.html le 15/08/2026)
    # =====================================================================
    # POURQUOI ELLE EST ICI, ET PAS AVANT LE BOUTON : la page n'a qu'UN geste
    # possible, et il ne doit pas etre precede de six questions. La FAQ est du
    # contenu de reference — on la lit quand on hesite encore, ou quand on
    # arrive dessus depuis une recherche. Sur `presentation.html` elle passe
    # avant l'appel a l'action ; ici l'appel a l'action est un panneau qui
    # conclut, et l'enterrer sous la FAQ lui ferait perdre sa place.
    #
    # ⚠️ `id="faq"` est l'ancre citee par le `@id` du bloc `FAQPage` du
    #    JSON-LD (« …/guso-facile#faq »). Ne pas la renommer sans changer
    #    l'autre.
    #
    # SECOND des deux liens descendants vers le blog (dossier SEO, §6), avec
    # l'ancre descriptive de la page Vercel.
    A("""
<div class="divider"></div>
<section id="faq"><div class="wrap">
  <p class="kick">Questions fréquentes</p>
  <h2 class="sec-title">Les questions qu’on se pose sur l’intermittence</h2>
  <p class="lead">Les réponses courtes aux questions qui reviennent le plus — sur le GUSO, les
    507 heures et les démarches.</p>
  <div class="faq">
""" + _faq_html() + """  </div>
  <p class="blog-lien"><a href="/guso-facile/blog">Toutes les situations concrètes sur le blog de Guso Facile</a></p>
</div></section>
</main>
""")

    # --- retour en haut + pied de page ------------------------------------
    # Pied de page identique aux 9 pages, a une correction pres : le lien
    # Facebook pointe sur /resonancesproductions (comme sur l'accueil) et non
    # sur https://www.facebook.com/ , qui traine encore sur plusieurs pages.
    A("""
<a class="totop" href="#top" aria-label="Revenir en haut de la page">↑</a>

<footer id="contact"><div class="wrap">
  <div class="fgrid">
    <div>
      <div class="fbrand">Résonances Productions</div>
      <p style="margin-top:8px">Association loi 1901 — Art du spectacle vivant.<br>« l’humain, la vibration »</p>
    </div>
    <div>
      <h4>Contact</h4>
      <p><a href="mailto:contact@resonancesproductions.org">contact@resonancesproductions.org</a></p>
      <p><b>Siège social</b><br>2 impasse des Bleuets<br>09600 Aigues-Vives</p>
      <p><b>Adresse de correspondance</b><br>29 rue des Orteaux<br>75020 Paris</p>
      <p style="margin-top:8px"><a href="https://www.facebook.com/resonancesproductions" target="_blank" rel="noopener">Facebook</a></p>
    </div>
    <div>
      <h4>Informations</h4>
      <p>SIRET : 919 514 075 00010</p>
      <p>Code APE : 9001Z<br>Arts du spectacle vivant</p>
      <p style="margin-top:8px"><a href="https://www.helloasso.com/associations/resonances-productions" target="_blank" rel="noopener">Adhérer / soutenir</a></p>
      <p style="margin-top:8px"><a href="https://docs.google.com/document/d/1NxsbvaqHsA9VOXlN7cvsav7cxFwhsK4XCpowHb75o1w/edit?usp=sharing" target="_blank" rel="noopener">Statuts de l’association</a></p>
    </div>
  </div>
  <div class="legal">© 2026 Résonances Productions · resonancesproductions.org</div>
</div></footer>

<script>
(function(){
  var b=document.querySelector('.totop'); if(!b) return;
  function upd(){ b.classList.toggle('on', window.scrollY>700); }
  upd(); window.addEventListener('scroll',upd,{passive:true});
})();
</script>
""")
    A('</body></html>\n')

    return ''.join(B)


# =========================================================================
# GARDE-FOUS + ECRITURE
# =========================================================================
# Parti-pris maison (celui de `generate_rythme.py`) : on REFUSE D'ECRIRE
# plutot que d'imprimer un avertissement qui defile et que personne ne lit.
# Chaque ancre ci-dessous est unique PAR CONSTRUCTION : si le compte change,
# c'est qu'un bloc a ete duplique (le piege des 4 cartes identiques) ou qu'il
# a disparu. Les deux cas sont attrapes.

#: nombre de maquettes d'interface posees dans la page. Il sert TROIS fois :
#: autant de blocs, autant de mentions « données fictives », autant de
#: role="img". Si l'un des trois comptes s'ecarte, la page n'est pas ecrite.
NB_MAQUETTES = 6

#: nombre de mentions « (a venir) » attendues dans la page. IL EST LE COMPTE
#: RENDU DE L'ETAT REEL DE L'APPLICATION, pas un reglage cosmetique — chaque
#: unite doit correspondre a une fonctionnalite qu'un beta-testeur constate
#: absente. Historique : 5 au 15/08/2026 ; 3 depuis le 16/08/2026, l'ecran de
#: la Guilde et celui de « Je cree mon contrat » ayant ete deployes entre-temps.
#: LES TROIS RESTANTS, un par un :
#:   1. « Points de vigilance cote structure » (univers 4) — la vue qui dirait
#:      qui approche du seuil n'existe pas ;
#:   2. « Confidentialite graduee » (univers 4) — le backend existe et il est
#:      teste, mais l'ECRAN DE REGLAGE COTE ARTISTE n'existe pas ;
#:   3. la note de la maquette 6 « Mes artistes » — l'apercu illustre une vue
#:      en cours de construction (voir le commentaire de `MAQ_STRUCTURE`).
#: Baisser ce nombre sans qu'un ecran soit reellement livre, c'est promettre.
#: Le monter sans motif, c'est deprecier un outil qui marche.
NB_A_VENIR = 3

#: nombre de puces « a venir » de l'inventaire. Il vaut NB_A_VENIR MOINS la note
#: de la maquette 6, qui n'est pas une puce : 3 - 1 = 2.
NB_PUCES_A_VENIR = NB_A_VENIR - 1

#: (marqueur, nombre attendu, ce que c'est)
ANCRES = (
    ('<h1', 1, 'titre principal de la page'),
    # version lue dans nav_menu : ce garde-fou ne doit pas devenir faux le jour
    # ou NAV_VERSION est incrementee.
    ('data-nav="%s"' % nav_menu.NAV_VERSION, 1, 'menu partage nav_menu.py'),
    ('href="/guso-facile"', 1, 'entree « Guso Facile » du menu partage'),
    ('id="acces"', 1, 'section « Reprends la main sur ton administratif »'),
    (URL_ACCES, 1, 'bouton « Demander un accès » (un seul sur la page)'),
    ('id="etat"', 1, 'section « Jouons cartes sur table »'),
    ('class="badge"', 1, 'badge « Bêta privée · places limitées »'),
    ('class="u-card"', 4, 'les 4 univers de fonctionnalités'),
    # Les intitules EXACTS des 4 univers, virgule comprise. Ils ont ete releves
    # dans le code de l'application le 14/08/2026 : la page portait jusque-la
    # des titres approchants (« Suivi des droits », « Organisation de tournee »,
    # « Espace structure », « Entraide entre artistes »). La virgule donne son
    # rythme a chaque intitule — ce n'est pas une coquille, ne pas la retirer.
    ('<h3>Tes droits, maîtrisés</h3>', 1, 'titre exact de l’univers 1'),
    ('<h3>Ta tournée, organisée</h3>', 1, 'titre exact de l’univers 2'),
    ('<h3>Ta structure, connectée</h3>', 1, 'titre exact de l’univers 3'),
    ('<h3>Ton cercle, solidaire</h3>', 1, 'titre exact de l’univers 4'),
    # Les trois blocs ajoutes le 14/08/2026 (voir les commentaires au-dessus de
    # chacun d'eux dans le gabarit).
    ('<b>Faire découvrir l’outil</b>', 1, 'cooptation — fonctionnalité LIVRÉE, au présent'),
    # ⚠️ 16/08/2026 — ces deux-la sont passees de « À VENIR » a LIVRÉE. Les
    # ancres ci-dessous pinglent la puce ENTIERE (`<li>` nu, pas
    # `<li class="soon">`, et pas de `<i>(à venir)</i>` derriere le `<b>`) :
    # c'est ce qui empeche qu'on les remette en « a venir » par reflexe.
    ('<li><b>L’entraide entre artistes</b> —', 1,
     'la Guilde — fonctionnalité LIVRÉE, au présent (écran déployé)'),
    ('<li><b>Je crée mon contrat</b> —', 1,
     'modèle de contrat — fonctionnalité LIVRÉE, au présent (écran déployé)'),
    # Le compte des mentions « (a venir) » : voir NB_A_VENIR juste au-dessus,
    # ou les trois fonctionnalites concernees sont nommees une par une. Si ce
    # compte baisse, une fonctionnalite non livree vient d'etre presentee comme
    # disponible ; s'il monte, une fonctionnalite livree vient d'etre effacee.
    # Les deux cas sont refuses a l'ecriture.
    ('<i>(à venir)</i>', NB_A_VENIR, 'les mentions « à venir » des fonctionnalités non livrées'),
    # La note de la maquette 6 « Mes artistes » : le seul « a venir » de la page
    # qui ne soit pas une puce. Elle marque le point ou la page promettait plus
    # que l'application (voir `MAQ_STRUCTURE`). A retirer le jour ou cette vue
    # sera deployee — on sera prevenu.
    ('class="gf-soon-note"', 1,
     'la mention « à venir » de l’aperçu « Mes artistes »'),
    # le hamburger est cree en JS par mobile_nav.py : c'est son CSS qui
    # atteste sa presence. `.burger span{` n'existe qu'une fois (`.burger{`
    # apparait 3 fois : regle de base + media 860 + media print).
    ('.burger span{', 1, 'CSS du hamburger (mobile_nav.py)'),
    ('id="contact"', 1, 'pied de page / ancre Contact'),
    # --- les 6 maquettes d'interface (14/08/2026) ------------------------
    # Trois comptes qui doivent rester egaux : un bloc = une mention visible
    # « données fictives » = un role="img". Si l'un decroche, soit un bloc a
    # ete duplique, soit une mention a saute — et une reproduction credible
    # sans mention est indistinguable d'une vraie capture d'ecran.
    ('<figure class="gf-block', NB_MAQUETTES, 'les maquettes d’interface'),
    ('<div class="gf-shot" role="img"', NB_MAQUETTES,
     'chaque maquette est une IMAGE pour les technologies d’assistance'),
    ('<figcaption class="gf-cap">' + MENTION_FICTIVE + '</figcaption>',
     NB_MAQUETTES, 'la mention visible « Aperçu de l’interface — données fictives »'),
    # Ce sont des illustrations, pas des interfaces : rien de focusable, rien
    # de saisissable NULLE PART sur la page hors du menu.
    # ⚠️ MESURE, pas supposition : la page contient bien 3 <button>, et
    #    seulement 3 — les trois ouvertures de sous-menu (« Sur scene »,
    #    « Le Nid », « L’association ») posees par nav_menu.py, plus le
    #    hamburger qui, lui, est cree en JavaScript et n'apparait donc pas
    #    sous forme de balise dans le fichier livre. Le compte est verifie
    #    HORS DU MENU par `_controle_maquettes()`, pour qu'un sous-menu de
    #    plus ou de moins ne fasse pas echouer l'ecriture pour rien.
    # --- la refonte visuelle du 14/08/2026 (soir) ------------------------
    # Le degrade signature est defini UNE fois pour le CSS et UNE fois pour les
    # SVG. Si l'un des deux disparait, la page perd sa chaleur d'un cote
    # seulement — le pire des cas, parce qu'il ne se voit pas tout de suite.
    ('--grad:linear-gradient', 1, 'le degrade signature (version CSS)'),
    ('id="gf-ink"', 1, 'le degrade signature (version SVG, partagee)'),
    ('class="u-ico"', 4, 'le pictogramme de chacun des 4 univers'),
    ('class="cas-ico"', 3, 'le pictogramme de chacun des 3 cas d’usage'),
    # Autant de marqueurs creux que de puces « a venir » (2 depuis le
    # 16/08/2026). Ce compte double celui de `<i>(à venir)</i>` moins la note de
    # maquette : c'est voulu, une puce pleine devant une fonctionnalite non
    # livree la ferait passer pour disponible — et une puce creuse devant une
    # fonctionnalite livree la ferait passer pour absente.
    ('<li class="soon">', NB_PUCES_A_VENIR, 'les puces des fonctionnalités non livrées'),
    ('<input', 0, 'aucun champ de saisie dans la page'),
    ('tabindex', 0, 'aucun ordre de tabulation force'),
    # --- l'absorption du 15/08/2026 --------------------------------------
    # Le JSON-LD : un seul bloc, et il ferme le <head>. Sa validite, elle, est
    # controlee par `_controle_jsonld()` — ici on ne compte que sa presence.
    ('<script type="application/ld+json">', 1, 'les données structurées (JSON-LD)'),
    ('<main>', 1, 'le conteneur <main> (rappel de la section 2 du dossier SEO)'),
    ('</main>', 1, 'la fermeture de <main>'),
    # La FAQ VISIBLE. Ce compte n'est pas cosmetique : sans ces six blocs, le
    # `FAQPage` annonce a Google une FAQ qui n'existe pas a l'ecran.
    ('id="faq"', 1, 'la section « Questions fréquentes »'),
    ('<details class="faq-q">', len(FAQ), 'les 6 questions/réponses visibles'),
    ('<p class="faq-r">', len(FAQ), 'les 6 réponses visibles'),
    # Le maillage vers le blog (dossier SEO, §6) : deux liens, ancres
    # descriptives. ⚠️ `href="/guso-facile"` compte 1 juste au-dessus : la
    # guillemet fermante l'empeche de compter ces deux-la.
    ('href="/guso-facile/blog"', 2, 'les deux liens descendants vers le blog'),
    ('class="guilde"', 1, 'l’encart « la Guilde »'),
    ('class="guilde-claim"', 1, 'l’accroche du manifeste de la Guilde'),
    ('class="etapes"', 1, 'la bande « trois étapes, c’est tout »'),
    ('class="etape"', 3, 'les trois étapes'),
    ('class="etat-fin"', 1, 'la phrase de clôture de « Jouons cartes sur table »'),
    ('class="h1-sous"', 1, 'la seconde ligne du <h1> (dossier SEO, section 2.1)'),
)

#: ce qu'aucune maquette ne doit contenir : elles ILLUSTRENT l'outil, elles ne
#: le rejouent pas. Un visiteur qui peut poser le focus dans une reproduction
#: croit manipuler le logiciel depuis le site de l'association.
_FOCUSABLES = (
    r'<a\b', r'<button\b', r'<input\b', r'<select\b', r'<textarea\b',
    r'<iframe\b', r'<details\b', r'<summary\b', r'<audio\b', r'<video\b',
    r'\btabindex\s*=', r'\bcontenteditable\b', r'\bonclick\b',
)


def _controle_maquettes(html):
    """Refuse d'ecrire si une maquette n'est pas une simple illustration.

    Trois exigences, bloc par bloc (le compte global, lui, est dans ANCRES) :
      - un `role="img"` ET un `aria-label` non vide : sans quoi un lecteur
        d'ecran enonce une bouillie de chiffres hors contexte ;
      - la mention visible « données fictives », exactement une fois ;
      - AUCUN element focusable a l'interieur.
    """
    import re

    # Aucun bouton hors du menu partage. Le corps de la page ne doit contenir
    # que du texte, des liens, et des illustrations inertes.
    corps = re.sub(r'<nav\b.*?</nav>', '', html, flags=re.S)
    if '<button' in corps:
        raise SystemExit('!! ABANDON : un <button> hors du menu de navigation. '
                         'Le corps de la page n\'a aucune commande a offrir : le '
                         'seul geste possible est le lien « Demander un accès ». '
                         'Page NON ecrite.')

    blocs = re.findall(r'<figure class="gf-block[^"]*">(.*?)</figure>', html, re.S)
    if len(blocs) != NB_MAQUETTES:
        raise SystemExit('!! ABANDON : %d bloc(s) <figure class="gf-block"> refermé(s) '
                         'correctement, attendu %d. Page NON ecrite.'
                         % (len(blocs), NB_MAQUETTES))

    for i, bloc in enumerate(blocs, 1):
        m = re.search(r'role="img" aria-label="([^"]{20,})"', bloc)
        if not m:
            raise SystemExit('!! ABANDON : maquette %d — role="img" ou aria-label '
                             'manquant (ou trop court pour decrire l\'ecran). '
                             'Page NON ecrite.' % i)
        if bloc.count(MENTION_FICTIVE) != 1:
            raise SystemExit(
                '!! ABANDON : maquette %d — la mention « %s » doit y figurer une '
                'fois et une seule. Sans elle, une reproduction credible de '
                'l\'interface est indistinguable d\'une vraie capture d\'ecran ; '
                'cette page a deja du corriger « situations reelles » pour ce '
                'motif exact. Page NON ecrite.' % (i, MENTION_FICTIVE))
        for motif in _FOCUSABLES:
            trouve = re.search(motif, bloc, re.I)
            if trouve:
                raise SystemExit(
                    '!! ABANDON : maquette %d — element focusable ou interactif '
                    '« %s ».\n   Les maquettes sont des ILLUSTRATIONS : un visiteur '
                    'ne doit pas pouvoir croire qu\'il pilote l\'outil depuis le '
                    'site de l\'association.\n   Page NON ecrite.'
                    % (i, trouve.group(0)))

#: seuls domaines externes autorises. Tout autre `https://` dans la page fait
#: echouer l'ecriture : zero traceur, zero script tiers, zero iframe.
#: fonts.googleapis.com / fonts.gstatic.com sont ceux des 9 pages existantes —
#: ce n'est pas une police SUPPLEMENTAIRE, c'est la meme feuille, deja chargee
#: partout sur le site.
#: ⚠️ `schema.org` (15/08/2026) n'est PAS une ressource chargee : c'est
#: l'identifiant du vocabulaire des donnees structurees, ecrit dans le JSON-LD
#: (`"@context"`, `"availability"`). Le controle des hotes le lit comme un
#: domaine tiers — le controle est bon, c'est le cas qui est particulier. Aucun
#: octet n'est demande a ce domaine par le navigateur.
HOTES_AUTORISES = (
    'schema.org',
    'fonts.googleapis.com',
    'fonts.gstatic.com',
    'www.helloasso.com',
    'guso-facile.vercel.app',
    'www.facebook.com',
    'docs.google.com',
    'www.resonancesproductions.org',
)


#: Le vocabulaire proscrit dans le bloc « L'entraide entre artistes ».
#: (motif, mot tel qu'il est interdit). Voir le long commentaire au-dessus du
#: bloc dans le gabarit : la fonctionnalite fait porter a des artistes des
#: affirmations factuelles sur des employeurs identifiables, sur une page
#: PUBLIQUE. Le bloc ne doit jamais se lire comme « une plateforme qui note les
#: employeurs du spectacle ».
#: ⚠️ L'interdit porte sur CE BLOC SEULEMENT : « signaler un bug » et
#: « Evaluation d'une proposition » sont legitimes ailleurs sur la page.
#: ⚠️⚠️ CES HUIT MOTS SONT LE CŒUR DU GARDE-FOU. Ils n'ont pas bouge d'une
#: lettre depuis le 14/08/2026, et la remise a niveau du 16/08 — qui a fait
#: passer les deux blocs Guilde au present — n'y a pas touche non plus. Ne
#: jamais les affaiblir ni les elargir au reste de la page.
MOTS_INTERDITS_GUILDE = (
    (r'\bnot(?:e|es|er|ée?s?|ation|ations)\b', 'noter / notation'),
    (r'\bsignal\w*', 'signaler'),
    (r'\bdénonc\w*|\bdenonc\w*', 'dénoncer'),
    (r'\bavis\b', 'avis'),
    (r'\bévalu\w*|\bevalu\w*', 'évaluation'),
    (r'\bblacklist\w*', 'blacklist'),
    (r'\bréputation\w*|\breputation\w*', 'réputation'),
)

#: LE SECOND INTERDIT, POSE LE 16/08/2026 — le vocabulaire d'ABONDANCE.
#:
#: Il remplace, dans les deux blocs Guilde, l'exigence « la mention (a venir)
#: doit y figurer » : cette exigence protegeait contre une SUR-PROMESSE DE
#: DISPONIBILITE (« l'ecran existe » alors qu'il n'existait pas). L'ecran
#: existe desormais et il est deploye — l'exigence serait devenue fausse, et
#: aurait purement et simplement empeche la page de dire la verite.
#:
#: Mais le risque n'a pas disparu, IL S'EST DEPLACE : l'espace est LIVRE ET
#: VIDE — zero lieu, zero retour saisis. La sur-promesse possible n'est plus
#: « ca existe », c'est « c'est deja rempli ». Ecrire « consulte les retours
#: d'artistes sur des centaines de lieux » ferait cliquer un beta-testeur vers
#: un ecran vide : plus decevant qu'un « a venir » de trop, et sur une page
#: publique portee par une association.
#: D'ou la regle : DECRIRE UNE CAPACITE (« on partage… », « l'espace est
#: reserve aux membres connectes… »), JAMAIS UN CONTENU.
#:
#: ⚠️ Comme les huit autres, cet interdit ne porte QUE sur les deux blocs
#: Guilde. Le reste de la page a parfaitement le droit de compter (« 65 dates
#: de concerts », « quatre artistes »…) : ces chiffres-la decrivent des faits
#: verifies, pas le remplissage d'un espace vide.
MOTS_INTERDITS_ABONDANCE = (
    (r'\bcentaines?\b', 'centaines (de lieux, de retours…)'),
    (r'\bmilliers?\b', 'milliers'),
    (r'\bdizaines?\b', 'dizaines'),
    (r'\bnombreux\b|\bnombreuses\b', 'nombreux / nombreuses'),
    (r'\bconsult\w*', 'consulter (le contenu existant)'),
    (r'\bdéjà\s+(?:renseign|répertori|référenc|recens|document|rempli)\w*',
     'déjà renseignés / répertoriés'),
    (r'\bbase\s+de\s+lieux\b', 'base de lieux'),
    (r'\bhistorique\s+des\s+lieux\b', 'historique des lieux'),
)

#: ce qui identifie le bloc Guilde dans la page livree.
_MARQUEUR_GUILDE = '<b>L’entraide entre artistes</b>'

#: ce qui delimite l'ENCART « la Guilde » ajoute le 15/08/2026. Il tombe sous
#: exactement le meme interdit que la puce : meme vocabulaire proscrit, meme
#: obligation de « (a venir) ». Deux blocs, un seul jeu de regles.
#: (ouverture, borne de fin). La borne de fin est le bloc SUIVANT dans la page,
#: pas un `</div>` : compter des `</div>` imbriques a la main est exactement le
#: genre de fragilite qui finit par controler le mauvais texte en silence.
_ENCART_OUVRE = '<div class="guilde">'
_ENCART_SUIVANT = '<div class="aussi">'


def _controle_guilde(html):
    """Refuse d'ecrire si le bloc « Guilde » derape.

    Deux exigences, toutes deux liees au fait que la page est PUBLIQUE alors
    que la fonctionnalite, elle, est reservee aux membres connectes :
      - aucun mot du vocabulaire PROSCRIT n'y apparait (les huit mots, coeur
        du garde-fou depuis le 14/08/2026 — voir MOTS_INTERDITS_GUILDE) ;
      - aucun mot du vocabulaire d'ABONDANCE non plus : l'ecran est livre mais
        VIDE, on decrit une capacite, jamais un contenu.

    ⚠️ CE QUI A CHANGE LE 16/08/2026, ET POURQUOI. Cette fonction EXIGEAIT la
    presence de « (a venir) » dans le bloc. C'etait juste tant que l'ecran
    n'existait pas ; l'ecran est deploye depuis, et l'exigence serait devenue
    un garde-fou qui FORCE LE MENSONGE — il aurait refuse d'ecrire une page
    disant la verite. Elle est remplacee par `MOTS_INTERDITS_ABONDANCE`, qui
    couvre le risque tel qu'il se pose maintenant (promettre un contenu que
    l'espace n'a pas). LES HUIT MOTS PROSCRITS, EUX, N'ONT PAS BOUGE : c'est la
    partie du garde-fou qui protege l'association, et elle n'est pas negociable.
    """
    import re

    debut = html.find(_MARQUEUR_GUILDE)
    if debut < 0:
        raise SystemExit('!! ABANDON : bloc « Guilde » introuvable. Page NON ecrite.')
    # `<li` et non `<li>` : depuis la refonte du 14/08/2026 les puces « a
    # venir » portent `class="soon"`. Chercher `<li>` exactement ferait
    # remonter la borne a la puce PRECEDENTE (la cooptation) et controlerait
    # un texte qui n'est pas celui de la Guilde.
    ouvre = html.rfind('<li', 0, debut)
    ferme = html.find('</li>', debut)
    if ouvre < 0 or ferme < 0:
        raise SystemExit('!! ABANDON : bloc « Guilde » mal delimite (pas de <li>…</li> '
                         'autour). Page NON ecrite.')
    bloc = html[ouvre:ferme + len('</li>')]

    for motif, mot in MOTS_INTERDITS_GUILDE:
        m = re.search(motif, bloc, re.I)
        if m:
            raise SystemExit(
                '!! ABANDON : mot interdit « %s » (ici : « %s ») dans le bloc '
                '« L\'entraide entre artistes ».\n'
                '   Ce bloc decrit des artistes qui affirment des faits sur des '
                'employeurs identifiables, sur une page PUBLIQUE. Il ne doit jamais '
                'se lire comme une plateforme de notation des employeurs.\n'
                '   Points d\'appui : membres connectes uniquement, faits binaires, '
                'aucun commentaire libre.\n'
                '   Page NON ecrite.' % (mot, m.group(0)))

    for motif, mot in MOTS_INTERDITS_ABONDANCE:
        m = re.search(motif, bloc, re.I)
        if m:
            raise SystemExit(
                '!! ABANDON : vocabulaire d\'abondance « %s » (ici : « %s ») dans le '
                'bloc « L\'entraide entre artistes ».\n'
                '   L\'ecran est livre, mais AUCUNE DONNEE n\'y a encore ete saisie : '
                'zero lieu, zero retour. Promettre un contenu enverrait un '
                'beta-testeur vers un espace vide.\n'
                '   Ecrire ce que la fonctionnalite PERMET (« on partage… »), jamais '
                'ce qu\'elle CONTIENDRAIT.\n'
                '   Page NON ecrite.' % (mot, m.group(0)))


def _controle_guilde_encart(html):
    """Meme controle que `_controle_guilde()`, mais sur l'ENCART « la Guilde ».

    Deux blocs de la page decrivent la meme fonctionnalite : la puce
    « L'entraide entre artistes » (univers 4) et cet encart (15/08/2026). Ils
    tombent sous UN SEUL jeu de regles — il aurait ete absurde de proteger le
    premier et de laisser le second libre, alors que c'est l'encart qui porte
    le texte le plus long et le plus argumente.

    ⚠️ 16/08/2026 : comme son jumeau, il n'exige plus « (a venir) » (l'ecran est
    deploye) mais refuse desormais le vocabulaire d'ABONDANCE. Les huit mots
    proscrits et l'exigence « membres connectes » sont inchanges.
    """
    import re

    debut = html.find(_ENCART_OUVRE)
    if debut < 0:
        raise SystemExit('!! ABANDON : encart « la Guilde » introuvable. '
                         'Page NON ecrite.')
    fin = html.find(_ENCART_SUIVANT, debut)
    if fin < 0:
        raise SystemExit('!! ABANDON : encart « la Guilde » mal delimite (le bloc '
                         '« Et aussi » qui doit le suivre est introuvable). '
                         'Page NON ecrite.')
    bloc = html[debut:fin]

    # Demande explicite des « Notes d'emploi » du manifeste : dire que l'espace
    # est reserve aux membres connectes, sinon on cree de la frustration chez
    # un lecteur qui cliquerait pour voir.
    if 'membres connectés' not in bloc:
        raise SystemExit(
            '!! ABANDON : l\'encart « la Guilde » ne precise plus que l\'espace sera '
            'reserve aux MEMBRES CONNECTES. C\'est une demande explicite du '
            'manifeste (`manifeste-la-guilde.md`, « Notes d\'emploi ») : sans elle, '
            'la page promet a un visiteur un espace qu\'il ne verra jamais. '
            'Page NON ecrite.')

    for motif, mot in MOTS_INTERDITS_GUILDE:
        m = re.search(motif, bloc, re.I)
        if m:
            raise SystemExit(
                '!! ABANDON : mot interdit « %s » (ici : « %s ») dans l\'encart '
                '« la Guilde ».\n'
                '   Cet encart decrit des artistes qui affirmeront des faits sur des '
                'employeurs identifiables, sur une page PUBLIQUE. Il ne doit jamais '
                'se lire comme une plateforme de notation des employeurs.\n'
                '   Points d\'appui : membres connectes uniquement, faits binaires, '
                'aucun commentaire libre, sortie constructive (poser le cadre la '
                'prochaine fois).\n'
                '   Page NON ecrite.' % (mot, m.group(0)))

    for motif, mot in MOTS_INTERDITS_ABONDANCE:
        m = re.search(motif, bloc, re.I)
        if m:
            raise SystemExit(
                '!! ABANDON : vocabulaire d\'abondance « %s » (ici : « %s ») dans '
                'l\'encart « la Guilde ».\n'
                '   L\'ecran est livre, mais AUCUNE DONNEE n\'y a encore ete saisie : '
                'zero lieu, zero retour. Decrire ce que la Guilde PERMET, jamais ce '
                'qu\'elle CONTIENDRAIT.\n'
                '   Page NON ecrite.' % (mot, m.group(0)))


def _sans_balises(html):
    """Le texte visible de la page : sans <script>, sans <style>, sans balises.

    Sert au controle du JSON-LD : c'est exactement ce qu'un visiteur lit, donc
    exactement ce que Google exige de trouver quand un `FAQPage` est declare.
    """
    import re

    txt = re.sub(r'<script\b.*?</script>', ' ', html, flags=re.S | re.I)
    txt = re.sub(r'<style\b.*?</style>', ' ', txt, flags=re.S | re.I)
    txt = re.sub(r'<[^>]+>', ' ', txt)
    return txt


def _norm_apostrophes(txt):
    """Apostrophe droite, espaces normalises.

    UNE seule difference est admise entre le JSON-LD et le texte a l'ecran :
    le dossier SEO ecrit « C'est », le site ecrit « C’est ». Tout le reste doit
    coincider mot pour mot — sinon le `FAQPage` decrit une page qui n'existe
    pas. On normalise donc l'apostrophe et les espaces, rien d'autre.
    """
    import re

    for mauvais in ('’', 'ʼ', '′'):
        txt = txt.replace(mauvais, "'")
    txt = txt.replace(' ', ' ').replace(' ', ' ')
    return re.sub(r'\s+', ' ', txt).strip()


def _controle_jsonld(html):
    """Refuse d'ecrire si les donnees structurees sont cassees ou mensongeres.

    DEUX exigences, et la seconde est la plus importante :

      1. LE BLOC DOIT ETRE DU JSON VALIDE. Un JSON-LD casse vaut MOINS que pas
         de JSON-LD du tout : Google ignore le bloc entier, et l'erreur ne se
         voit nulle part a l'ecran. On le parse ici, avant toute ecriture.

      2. LE `FAQPage` DOIT DIRE LA VERITE. Declarer une FAQ que la page
         n'affiche pas est une violation explicite des consignes Google,
         sanctionnable — et c'est exactement le piege que cette page a deja
         connu ailleurs (« situations reelles » pour des personnages fictifs).
         Chaque question ET chaque reponse du bloc est donc cherchee dans le
         TEXTE VISIBLE de la page.
    """
    import json
    import re

    blocs = re.findall(r'<script type="application/ld\+json">(.*?)</script>',
                       html, re.S)
    if len(blocs) != 1:
        raise SystemExit('!! ABANDON : %d bloc(s) JSON-LD, attendu 1. '
                         'Page NON ecrite.' % len(blocs))
    try:
        data = json.loads(blocs[0])
    except ValueError as err:
        raise SystemExit('!! ABANDON : le JSON-LD n\'est pas du JSON valide '
                         '(%s).\n   Un JSON-LD casse vaut moins que pas de JSON-LD : '
                         'Google ignore le bloc entier et rien ne se voit a l\'ecran. '
                         'Page NON ecrite.' % err)

    graphe = data.get('@graph')
    if not isinstance(graphe, list):
        raise SystemExit('!! ABANDON : JSON-LD sans « @graph ». Page NON ecrite.')
    types = [n.get('@type') for n in graphe]
    for attendu in ('Organization', 'WebApplication', 'FAQPage', 'BreadcrumbList'):
        if attendu not in types:
            raise SystemExit('!! ABANDON : JSON-LD sans noeud « %s » (presents : %s). '
                             'Page NON ecrite.' % (attendu, ', '.join(map(str, types))))

    visible = _norm_apostrophes(_sans_balises(html))
    faq = [n for n in graphe if n.get('@type') == 'FAQPage'][0]
    questions = faq.get('mainEntity') or []
    if len(questions) != len(FAQ):
        raise SystemExit('!! ABANDON : %d question(s) dans le FAQPage, %d dans la '
                         'page. Page NON ecrite.' % (len(questions), len(FAQ)))
    for q in questions:
        for quoi, texte in (('question', q.get('name', '')),
                            ('réponse', (q.get('acceptedAnswer') or {}).get('text', ''))):
            if _norm_apostrophes(texte) not in visible:
                raise SystemExit(
                    '!! ABANDON : cette %s du bloc FAQPage est ABSENTE du texte '
                    'visible de la page :\n   « %s »\n'
                    '   Declarer a Google une FAQ que la page n\'affiche pas est une '
                    'violation explicite de ses consignes. Soit on ecrit les 6 Q/R a '
                    'l\'ecran, soit on retire le FAQPage — jamais l\'un sans '
                    'l\'autre. Page NON ecrite.' % (quoi, texte[:90]))


#: nombre de pictogrammes POSES dans la page. Le dictionnaire `ICONES` en
#: definit onze depuis le 15/08/2026 (le onzieme, « guilde », habille l'encart
#: du meme nom), chacun servant exactement une fois — plus le <svg> de taille
#: nulle qui porte la definition du degrade. Un ecart = un picto duplique ou
#: disparu.
NB_PICTOS = 11


def _controle_icones(html):
    """Refuse d'ecrire si un pictogramme cesse d'etre purement decoratif.

    Les icones DOUBLENT un texte qui est deja la. Trois exigences :
      - `aria-hidden="true"` : sinon un lecteur d'ecran annonce « image » (ou
        pire, epelle le trace) avant chaque titre deja lu ;
      - `focusable="false"` : d'anciens moteurs inserent les <svg> dans l'ordre
        de tabulation, ce qui ajoute dix arrets pour rien au clavier ;
      - aucun `xmlns` : inutile en HTML, et il vaut « http://www.w3.org/… »,
        que le controle des hotes externes lirait comme un domaine tiers. Le
        message ci-dessous evite de chercher pourquoi la page est refusee.
    """
    import re

    balises = re.findall(r'<svg\b[^>]*>', html)
    if len(balises) != NB_PICTOS + 1:
        raise SystemExit('!! ABANDON : %d balise(s) <svg>, attendu %d (les %d '
                         'pictogrammes + le bloc de definitions du degrade). '
                         'Page NON ecrite.'
                         % (len(balises), NB_PICTOS + 1, NB_PICTOS))
    for b in balises:
        if 'aria-hidden="true"' not in b or 'focusable="false"' not in b:
            raise SystemExit('!! ABANDON : pictogramme sans aria-hidden="true" ou '
                             'sans focusable="false" :\n   %s\n   Ces icones doublent '
                             'un texte deja present : les annoncer ou les rendre '
                             'atteignables au clavier n\'ajoute que du bruit. '
                             'Page NON ecrite.' % b)
        if 'xmlns' in b:
            raise SystemExit('!! ABANDON : attribut xmlns sur un <svg> en ligne. Il '
                             'est inutile en HTML et vaut une URL w3.org, que le '
                             'controle des hotes externes refuserait avec un message '
                             'incomprehensible. Retirer l\'attribut. Page NON ecrite.')
    for interdit in ('<image', '<foreignObject'):
        if interdit in html:
            raise SystemExit('!! ABANDON : « %s » dans un SVG — la page n\'embarque '
                             'ni image ni contenu importe. Page NON ecrite.' % interdit)


def _controles(html):
    """Leve SystemExit au moindre ecart. Appele AVANT l'ecriture."""
    import re

    for marqueur, attendu, quoi in ANCRES:
        n = html.count(marqueur)
        if n != attendu:
            raise SystemExit(
                '!! ABANDON : %d occurrence(s) de « %s » (%s), attendu %d. '
                'Page NON ecrite.' % (n, marqueur, quoi, attendu))

    # tout `target="_blank"` doit porter `rel="noopener"` (regle du site)
    for m in re.finditer(r'<a\b[^>]*>', html):
        balise = m.group(0)
        if 'target="_blank"' in balise and 'rel="noopener"' not in balise:
            raise SystemExit('!! ABANDON : target="_blank" sans rel="noopener" :\n   %s\n'
                             '   Page NON ecrite.' % balise)

    # aucun hote externe hors liste blanche
    for hote in set(re.findall(r'https?://([^/"\'\s>]+)', html)):
        if hote not in HOTES_AUTORISES:
            raise SystemExit('!! ABANDON : hote externe non autorise « %s ». '
                             'Page NON ecrite.' % hote)

    # aucune iframe, aucun script distant
    for interdit in ('<iframe', '<script src', 'googletagmanager', 'analytics'):
        if interdit in html:
            raise SystemExit('!! ABANDON : « %s » dans la page (zero tiers). '
                             'Page NON ecrite.' % interdit)

    # plancher typographique du site : jamais sous 13 px
    petits = [t for t in re.findall(r'font-size:\s*(\d+(?:\.\d+)?)px', html)
              if float(t) < 13]
    if petits:
        raise SystemExit('!! ABANDON : taille(s) de texte sous le plancher de 13 px : %s. '
                         'Page NON ecrite.' % ', '.join(petits))

    # aucune donnee personnelle glissee dans la page (depot PUBLIC)
    for motif, quoi in ((r'\b\d{13}\b', 'numero de securite sociale'),
                        (r'\bFR\d{2}[ ]?\d', 'IBAN')):
        if re.search(motif, html):
            raise SystemExit('!! ABANDON : ce qui ressemble a un %s dans la page. '
                             'Page NON ecrite.' % quoi)

    # le bloc le plus sensible de la page depuis le 14/08/2026 — DEUX blocs
    # depuis le 15/08 : la puce de l'univers 4 et l'encart « la Guilde ».
    _controle_guilde(html)
    _controle_guilde_encart(html)
    # les donnees structurees : valides, et fideles a ce que la page affiche
    _controle_jsonld(html)
    # les 6 maquettes : illustrations, jamais interfaces
    _controle_maquettes(html)
    # les 11 pictogrammes : decoratifs, jamais annonces ni focusables
    _controle_icones(html)


def main():
    html = build_html()
    html = mobile_nav.inject(html)          # 1. le hamburger d'abord
    # 2. puis le menu partage. Depuis le 14/08/2026 « guso-facile » est une cle
    #    de nav_menu.PAGE_KEYS : l'entree du sous-menu « L’association » porte
    #    donc `aria-current="page"` sur cette page, et le parent est marque.
    html = nav_menu.inject(html, 'guso-facile')

    _controles(html)
    # Aucune note de redaction en commentaire HTML dans la page livree : elle
    # serait publique et indexable. Sa place est ici, en commentaire `#`.
    verif_commentaires.verifier(html, OUT_HTML)

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)
    print('[page]   %s  (%.1f Ko)' % (OUT_HTML, len(html.encode('utf-8')) / 1024))


if __name__ == '__main__':
    main()
