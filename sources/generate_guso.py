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
   ⚠️ COMPLETE LE 17/08/2026 — DAVID A TRANCHE, ET L'ECART N° 8 TIENT.
   Le constat : les beta-testeurs ONT DEJA UN COMPTE et n'avaient, depuis la
   fusion du 16/08, plus AUCUN chemin vers l'application depuis cette page (le
   bouton mene au formulaire de demande, pas a l'ecran de connexion). Ils
   devaient retaper une adresse en `vercel.app` de memoire.
   Ce qui a ete pose : un LIEN TEXTE (`.hero-cnx`), « J'ai deja un compte ->
   me connecter », JUSTE SOUS la rangee `.cta`, vers `/guso-facile/app`.
   POURQUOI UN LIEN ET PAS UN BOUTON — la decision d'origine n'est pas annulee,
   elle est bornee. Le raisonnement qui l'a produite vaut toujours : ~95 % des
   visiteurs de cette page N'ONT PAS de compte, et deux boutons de meme poids
   dans le premier ecran, c'est deux gestes possibles la ou la page n'en veut
   qu'un — « demander un acces ». Le lien sert la minorite qui sait deja ce
   qu'elle vient chercher : elle le trouve parce qu'elle le cherche, elle ne
   le voit pas si elle ne le cherche pas. Hierarchie visuelle, mesuree :
   bouton dore plein > lien blog dore souligne > lien de connexion gris
   (`--muted`), 14,5 px. Il n'emprunte AUCUNE classe `btn`.
   ⚠️ ET SURTOUT : SON `href` NE PORTE PAS L'ADRESSE DE L'APPLICATION. Il pointe
   sur `/guso-facile/app`, une redirection posee dans `vercel.json` — voir
   « L'ADRESSE STABLE DE CONNEXION » plus bas. L'ancre `guso-facile.vercel.app`
   a ZERO dans `ANCRES` garantit que personne ne « simplifiera » ce lien en y
   collant l'adresse en dur.

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
   ⚠️ PERIME LE 17/08/2026 : les deux ecrans sont deployes, verifies en
   production. Les deux puces sont passees au PRESENT et reecrites avec les
   phrases de l'auteur de l'app. C'etaient les deux dernieres puces « a venir »
   de la page. Voir « LA REMISE A NIVEAU DU 17/08/2026 » plus bas.

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
     ⚠️ PERIME LE 17/08/2026 : la vue est construite et deployee — la maquette
     est restee identique, sa mention « (a venir) » est retiree. C'etait le seul
     « a venir » de la page qui ne fut pas une puce.

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
    ⚠️ COMPLETE LE 17/08/2026 — DAVID A TRANCHE : IL VEUT UN ACCES POUR LES
    GENS QUI ONT DEJA UN COMPTE. Le second BOUTON n'est toujours pas repris —
    ce qui est repris, c'est la FONCTION, sous la forme d'un LIEN texte discret
    sous la rangee `.cta` (« J'ai deja un compte -> me connecter »,
    `.hero-cnx`). La page garde donc UN SEUL bouton, et l'ecart n° 8 reste vrai
    au mot pres : l'argumentaire d'origine y est complete, pas remplace.
    Deux differences avec la version Vercel, toutes deux volontaires :
      - c'est un lien gris (`--muted`, 14,5 px) et non un bouton dore de meme
        poids que « Demander un acces » — le geste principal de la page ne se
        partage pas en deux ;
      - il ne pointe PAS sur `guso-facile.vercel.app` mais sur
        `/guso-facile/app` (voir « L'ADRESSE STABLE DE CONNEXION »).
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
⚠️ CES TROIS-LA SONT TOMBES LE 17/08/2026 — voir « LA REMISE A NIVEAU DU
   17/08/2026 » juste en dessous. `NB_A_VENIR` vaut 0.

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

------------------------------------------------------------------------------
LA REMISE A NIVEAU DU 17/08/2026 — la page ne promet plus rien
------------------------------------------------------------------------------
L'inventaire fourni la veille par la session qui developpe l'app etait EN RETARD
SUR SON PROPRE TRAVAIL : les trois dernieres fonctionnalites annoncees « (a
venir) » etaient deja deployees. VERIFICATION FAITE ICI, dans le bundle servi
par `https://guso-facile.vercel.app/index.html` (956 Ko) — pas sur parole :
    affSetVisibility  -> 2    (reglage de confidentialite par l'artiste)
    "Tout partager"   -> 13   (les trois niveaux de partage)
    Partenaire        -> 5
    Minimal           -> 9
    sdCardHtml        -> 3    (cartes d'artistes, points de vigilance)
    affSetManage      -> 2
    visibility:'full'         (le niveau est une DONNEE, pas un affichage)

CE QUI PASSE AU PRESENT (les 3 dernieres mentions « (a venir) », RETIREES)
  1. « Points de vigilance cote structure » (univers 4). `class="soon"` et
     `<i>(a venir)</i>` retires, ET LE TEXTE REECRIT : il ne disait que
     l'intention (« qui approche du seuil, qui aurait besoin d'un coup de
     main »), il dit maintenant ce que la structure voit — heures sur la
     periode, jours restants avant la date anniversaire, rythme necessaire,
     niveau d'alerte, trie par urgence. Phrase de l'auteur de l'app.
  2. « Confidentialite graduee » (univers 4). Idem, et la puce porte desormais
     LA PRECISION QUI FAIT LA DIFFERENCE : le filtrage est fait COTE SERVEUR,
     pas seulement a l'affichage — la structure ne recoit pas les donnees
     qu'elle n'a pas le droit de voir, au lieu de les recevoir et de ne pas les
     montrer. Ancre dediee dans `ANCRES` : cette phrase ne doit pas etre
     raccourcie au prochain menage de longueur.
     🚩 Elle decrit desormais LA MEME fonctionnalite que « Niveaux de partage »
     (univers 3), vue de l'autre bout. La separation stricte des deux puces
     n'avait de sens que tant que l'une etait livree et l'autre pas ; le raccord
     est ecrit dans le commentaire de la puce, et la fusion eventuelle est
     laissee a l'arbitrage de David.
  3. La note de la maquette 6 « Mes artistes » — l'argument `note=` de son appel
     a `_figure()` retire. Maquette et texte inchanges.
  4. LE SOUS-TITRE DE L'UNIVERS 4 disait « Deux points y sont encore en
     construction, marques "a venir" » : il devenait faux dans la meme minute.
     La phrase est retiree, il ne reste que « Parce qu'on avance mieux a
     plusieurs. »

CE QUI RESTE VOLONTAIREMENT NON FAIT — ET DONT LA PAGE NE PARLE PAS
  L'ECRAN PERMETTANT A UNE STRUCTURE DE SAISIR UNE DATE DANS L'ESPACE D'UN
  ARTISTE. Le droit existe en base, l'artiste peut le donner, mais l'interface
  n'existe pas : c'est le geste le plus delicat de l'application (ecrire chez
  quelqu'un d'autre) et David doit l'arbitrer. La page N'EN PARLE PAS, ni au
  present ni au futur — et on ne l'ajoute pas : une page ne gagne rien a
  annoncer ce qui n'existe pas. Meme consigne pour LE JOURNAL DES MODIFICATIONS
  et L'ANNUAIRE DES STRUCTURES, en construction. (A ne pas confondre avec
  « Nouveautes », le journal des nouveautes de l'app, lui LIVRE et illustre par
  la maquette 10.)

`NB_A_VENIR` PASSE DE 3 A 0, ET LE MECANISME RESTE ENTIER
  Le nombre, les deux ancres qui en decoulent (`<i>(à venir)</i>` et
  `<li class="soon">`), le CSS de la pastille creuse et l'argument `note=` de
  `_figure()` sont TOUS conserves — a zero, ils interdisent qu'un « a venir »
  revienne par prudence reflexe sans motif ecrit. ⚠️ UNE GARDE A DU ETRE
  REPAREE au passage : `NB_PUCES_A_VENIR` valait `NB_A_VENIR - 1`, le « 1 »
  etant la note de la maquette 6 ; a zero elle exigeait donc **-1** occurrence,
  ancre impossible a satisfaire. La soustraction porte desormais un nom,
  `NB_NOTES_A_VENIR`.

------------------------------------------------------------------------------
L'ADRESSE STABLE DE CONNEXION (17/08/2026) — `/guso-facile/app`
------------------------------------------------------------------------------
LE BUT N'EST PAS LE REFERENCEMENT. C'est de NE PLUS DEPENDRE DE `vercel.app`.
L'application vit aujourd'hui sur `https://guso-facile.vercel.app/index.html`.
David n'a pas achete de nom de domaine et ne le fera pas maintenant (beta
privee, gratuite). Le jour ou il en prendra un — ou ou l'application demenagera
— l'adresse que les beta-testeurs auront memorisee ou mise en favori doit
continuer de marcher. D'ou une adresse a NOUS, sur le domaine de l'association,
qui ne fait que rediriger :

    vercel.json :
      /guso-facile/app   -> https://guso-facile.vercel.app/index.html
      /guso-facile/app/  -> idem   (la variante a barre oblique finale,
                                          par coherence avec /Guso-Facile/)

Il y a alors UN SEUL endroit a changer le jour du demenagement : cette ligne.
Le lien du hero, lui, ne bouge jamais.

⚠️⚠️ 302 ET NON 301 — `"permanent": false`, ET C'EST LE POINT DELICAT
Les 11 redirections deja presentes dans `vercel.json` sont en 301 (`permanent:
true`) A JUSTE TITRE : elles pointent vers des pages INTERNES et DEFINITIVES
(/accueil -> /, /statuts -> /association#statuts…). Celle-ci est l'inverse : sa
destination est PROVISOIRE PAR CONSTRUCTION. Or un 301 est mis en cache par les
navigateurs quasi definitivement — le jour du changement de domaine, chaque
beta-testeur qui aurait clique une fois resterait envoye sur l'ANCIENNE adresse
par son propre navigateur, sans que rien cote serveur puisse le rattraper.
Ce serait exactement l'inverse du but recherche. Un 302 n'est pas mis en cache :
le navigateur redemande a chaque fois, donc il suit le changement.
NE PAS « harmoniser » cette ligne avec les 11 autres en la passant a `true`.

CE QUI A ETE VERIFIE, ET CE QUI NE PEUT PAS L'ETRE ICI
  - `guso-facile/` est un VRAI dossier avec un `index.html`. Aucun fichier ni
    dossier `guso-facile/app` n'existe : il n'y a donc rien a masquer.
    (Et de toute facon, chez Vercel la phase `redirects` passe AVANT le service
    des fichiers statiques : une redirection l'emporterait sur un fichier.)
  - Aucun conflit avec `/Guso-Facile` ni `/Guso-Facile/` : les `source` de
    Vercel sont sensibles a la casse, et ces deux-la n'ont pas de segment
    `connexion`.
  - ⚠️ LA REDIRECTION ELLE-MEME NE SE TESTE PAS EN LOCAL. `vercel.json` n'est lu
    que par la plateforme : un `python3 -m http.server` rendra toujours 404 sur
    `/guso-facile/app`. Ce qui est verifiable ici — et qui l'est —, c'est
    que le JSON est valide, que la destination est bien formee et que la page ne
    contient nulle part l'adresse en dur. Le premier clic reel se fait en
    production, apres publication.
  - `robots.txt` porte `Disallow: /guso-facile/app` : une adresse de
    connexion n'a aucune valeur en referencement. (L'application, de son cote,
    envoie deja `<meta name="robots" content="noindex,follow">` — releve dans le
    HTML servi le 17/08/2026. Les deux protections se cumulent.)
  - `verif_site.py` a du apprendre CE MECANISME : un lien interne vers une URL
    qui n'est pas un fichier n'est pas forcement mort, il peut etre redirige.
    Le controle ne compte donc plus comme morte une URL qui figure en `source`
    d'une redirection de `vercel.json`, et il accepte qu'une destination soit
    une adresse absolue externe. Le detail du raisonnement est ecrit LA-BAS,
    au-dessus des deux controles concernes.

------------------------------------------------------------------------------
LA FUSION DU 16/08/2026 — UNE SEULE PAGE, UN SEUL ECRAN POUR DEMANDER UN ACCES
------------------------------------------------------------------------------
LE PROBLEME, MESURE. Pour demander un acces il fallait : lire cette page
(10 897 px a 1440), cliquer « Comment demander un acces », defiler jusqu'en
bas, cliquer « Demander un acces », ATTERRIR SUR guso-facile.vercel.app/
presentation.html (8 669 px) — qui reexplique le produit autrement — et
seulement la, trouver le formulaire. Trois clics, deux domaines, deux discours.
Et au moment precis de confier son nom, son mail et son telephone, la personne
QUITTAIT LE SITE D'UNE ASSOCIATION POUR UN vercel.app. C'est la qu'on perdait
les gens.

CE QUI A CHANGE
  1. LE FORMULAIRE VIT ICI. Le bouton n'ouvre plus aucune page externe : la
     section #acces porte le formulaire lui-meme. `URL_ACCES` (qui pointait sur
     presentation.html) N'EXISTE PLUS ; deux ancres a zero occurrence
     (`presentation.html`, `guso-facile.vercel.app`) empechent qu'il revienne
     par reflexe, et l'hote `guso-facile.vercel.app` est sorti de
     `HOTES_AUTORISES`.
     ⚠️ La page Vercel RESTE EN LIGNE pour l'instant : sa redirection sera posee
     par sa session APRES verification que rien ne manque ici. On ne pointe donc
     plus vers elle, mais on ne casse rien non plus.
  2. LA SEULE REQUETE RESEAU VERS UN TIERS PART AU CLIC SUR « ENVOYER », JAMAIS
     AVANT. Aucun prechargement, aucun ping au chargement. Mesure : 0 requete
     vers supabase.co au chargement de la page (releve dans l'onglet reseau, pas
     suppose).
  3. UN SEUL BLOC ABSORBE DE presentation.html, ET DEUX REJETES COMME DOUBLONS
     (voir « CE QUI A ETE ABSORBE » ci-dessous).

CE QUI A ETE ABSORBE DE `presentation.html` (LECTURE SEULE, jamais editee)
  a) « ON VEILLE LES UNS SUR LES AUTRES », mais UN TIERS SEULEMENT.
     La section Vercel incarne trois cas : le groupe · la structure · l'artiste
     seul. DEUX SUR TROIS SONT DES DOUBLONS DE CETTE PAGE :
       - « La structure qui accompagne » (« Des Sons et Des Liens voit d'un coup
         d'oeil quels artistes approchent du seuil… ») redit MOT POUR MOT le cas
         de Sophie (« Accompagner quatre artistes sans tableur »), la maquette 6
         « Mes artistes » ET la puce « Points de vigilance cote structure »
         (« (a venir) » jusqu'au 17/08/2026, au present depuis). Trois fois la
         meme chose : NON REPRIS.
       - « L'artiste seul face a l'admin » (« L'app te dit toujours le prochain
         pas : DPAE a faire pour samedi… ») redit le paragraphe de #promesse
         (« une seule question, posee chaque jour : qu'est-ce que j'ai a faire
         maintenant ? »), la maquette 2 et l'etape 3. NON REPRIS.
       - « LE GROUPE » est le SEUL cas reellement absent d'ici : la vue groupe
         n'etait qu'une puce d'inventaire, jamais incarnee. C'est lui qui est
         repris, en bloc court, JUSTE AVANT l'encart de la Guilde qu'il
         introduit.
     ⚠️⚠️ LE PIEGE QUE CETTE SECTION PORTAIT : elle met en scene une STRUCTURE
     (« Des Sons et Des Liens ») et une PERSONNE (« Marius ») INVENTEES SANS LE
     DIRE — exactement ce que la correction « Trois situations reelles » ->
     « typiques » a deja coute a cette page. La structure inventee disparait
     avec le cas non repris ; le prenom, lui, est CONSERVE MAIS MARQUE, dans le
     meme esprit et le meme habillage que « Les prenoms sont fictifs » : une
     note `.veille-note` sous le bloc, en petit et en gris, qui dit
     « Le prenom et le groupe sont fictifs, comme dans les trois situations
     plus haut. »
     La cloture Vercel de cette section (« c'est TOI qui decides ce que tu
     partages ») N'EST PAS REPRISE : c'est « Confidentialite graduee », qui est
     « (a venir) ». L'ecrire au present ferait mentir la page.
     ⚠️ PERIME LE 17/08/2026 : « Confidentialite graduee » est livree, la phrase
     ne mentirait plus. Elle N'EST TOUJOURS PAS REPRISE, pour l'autre raison —
     la puce de l'univers 4 le dit deja, et mieux (le filtrage cote serveur).
     Une reprise ferait un troisieme endroit ou la page dit la meme chose.
  b) « OU EN EST LE PROJET » — RIEN A AJOUTER, verifie point par point. Les cinq
     points Vercel (eprouve sur du reel : 2 artistes, 65 dates, 2 saisons /
     construit par un musicien pour son propre usage / acces sur invitation ou
     cooptation, chaque demande etudiee personnellement / en echange, le jeu des
     retours / demain, probablement payant + affiliation, rien n'est chiffre) et
     sa cloture (« un outil deja solide, une porte encore etroite… ») sont TOUS
     deja dans #etat. Le seul ecart est volontaire : Vercel ecrit « Beta
     OUVERTE », ici c'est « Beta privee » — formulation validee, NE PAS
     harmoniser dans l'autre sens.
  c) LES 4 UNIVERS — RIEN NE MANQUE. Vercel en aligne 22 puces, cette page 25
     (elle porte en plus « Profil complet », « Tournee reliee », « Fiche
     structure », « Je cree mon contrat », « Faire decouvrir l'outil » et
     « L'entraide entre artistes »). Les 22 sont couvertes une a une.

LES DOUBLONS SUPPRIMES ICI, ET LA VERSION GARDEE
  - « Le formulaire "Demander un acces" recueille le nom, le prenom, l'adresse
    e-mail, le numero de telephone et la nature du demandeur — artiste ou
    structure. » -> SUPPRIME. Le formulaire est desormais SOUS LES YEUX, avec
    ses propres libelles : enumerer ses champs en prose, c'est ecrire deux fois
    la meme liste. La phrase qui la precedait (« on commence par se dire
    bonjour ») est GARDEE : elle dit le pourquoi, pas le contenu.
  - « Le bouton "Demander un acces" se trouve en haut et en bas de la page de
    presentation. » -> SUPPRIME : il n'y a plus de page de presentation, la
    phrase serait devenue FAUSSE.
  - « Le formulaire d'acces est heberge par Guso Facile ; … Le formulaire porte
    sa propre mention d'information. » -> SUPPRIME : renvoyer a une mention
    portee ailleurs n'a plus de sens quand la saisie se fait ICI. La mention
    RGPD de `presentation.html` (« Ces informations servent uniquement a creer
    ton compte et a te recontacter… Aucun demarchage, aucune revente, aucun
    partage a des tiers. Tu peux demander leur suppression a tout moment a
    contact@lesagedavid.fr. ») est RAPATRIEE a sa place, au registre neutre du
    corps de page, ET COMPLETEE du point qui manquait : elle NOMME LE
    RESPONSABLE DE TRAITEMENT — **David Lesage, createur de l'outil, PAS
    l'association**. C'est le point qui gagne le plus a la fusion : la saisie se
    fait desormais sur le domaine de l'association, il ne doit y avoir aucune
    ambiguite sur qui recoit les donnees.

LE FORMULAIRE — CE QUI A ETE APPLIQUE TEL QUEL, ET LES TROIS PIEGES
  Endpoint, en-tetes et comportement sont ceux TESTES ET VERIFIES par la session
  qui developpe l'application :
      POST https://wqhwfqasoyyeprggjxet.supabase.co/rest/v1/account_requests
      apikey + Authorization: Bearer <cle publiable> + Content-Type
  Champs : `email` (OBLIGATOIRE), `first_name`, `last_name`, `phone`,
  `kind` (artiste | structure | les_deux), `message`, `context` (jsonb — on y met
  `{origin, ts, ua}` pour tracer d'ou viennent les demandes) et, DEPUIS LE
  17/08/2026, les trois vraies colonnes de structure : `structure_name` (text),
  `structure_type` (text) et `structure_licence` (BOOLEAN).
  CORS verifie depuis notre origine : POST -> 201, prevol OPTIONS -> 200,
  `access-control-allow-origin: *`. Aucune configuration a changer.

  LES TROIS PIEGES, qui ont deja coute du temps a l'auteur :
    1. NE PAS ENVOYER `Prefer: return=representation`. La cle publiable n'a pas
       le droit de RELIRE la ligne inseree : on recupererait un 401 ALORS QUE
       L'INSERTION A REUSSI. Sans cet en-tete -> 201 propre. Garde-fou :
       `_controle_formulaire()` refuse d'ecrire si « Prefer » apparait.
    2. NE JAMAIS ENVOYER DE CHAMP `status`. La securite impose `status='new'` ;
       le fournir fait echouer la requete (protection contre l'auto-approbation).
       Meme garde-fou.
    3. TROIS CODES A GERER, EN PHRASES ET JAMAIS EN CODES :
         201 -> succes ;
         409 -> UNE DEMANDE EST DEJA EN ATTENTE POUR CET E-MAIL. C'est une BONNE
                NOUVELLE pour la personne : sa demande est bien arrivee. Le
                message doit se lire comme telle, JAMAIS comme une panne ;
         401 -> e-mail vide ou champ interdit.

  LES REGLES DU FORMULAIRE, NON NEGOCIABLES
    - AUCUNE requete vers un tiers avant le clic sur « envoyer ».
    - JavaScript minimal, ecrit a la main, EN LIGNE. Aucune bibliotheque, aucun
      <script src> (deja refuse par `_controles`).
    - Il fonctionne AU CLAVIER : de vrais <label for> lies a leurs champs, une
      erreur ASSOCIEE au champ (`aria-describedby` + `aria-invalid`), un etat
      d'envoi qui empeche le double clic (`disabled` + drapeau `envoi`), une
      confirmation lisible par un lecteur d'ecran (`role="status"` +
      `aria-live="polite"`).
    - ⚠️ CES CHAMPS SONT LES SEULS ELEMENTS FOCUSABLES AJOUTES A LA PAGE.
      `_controle_maquettes()` exige TOUJOURS zero element focusable dans les 6
      apercus d'interface : le formulaire n'est PAS dans un apercu, et le
      controle « aucun <button> hors du menu » neutralise desormais le menu ET
      le formulaire — rien d'autre.
    - LA CLE EST PUBLIABLE PAR CONCEPTION (son nom le dit : `sb_publishable_…`)
      et elle est deja publique sur la page Vercel. Elle peut donc entrer dans
      un depot public : ce n'est pas un secret qui fuit, c'est un identifiant
      d'origine, protege par les regles de securite de la base — d'ou les deux
      pieges ci-dessus, qui sont precisement ces regles a l'oeuvre. Le crochet
      `pre-commit` la laisse passer : il traque les cles JWT (`eyJhbGciOi…`),
      un motif auquel elle ne repond pas.
      ⚠️ Et c'est aussi pour cela que les trois en-tetes de la requete sont
      ecrits UNE PAR LIGNE dans le gabarit JS. Regroupes sur une seule ligne, le
      nom de l'en-tete d'identification, le deux-points et la cle forment
      exactement la suite que ce meme crochet traque pour attraper une cle
      laissee en clair — il refuserait la sauvegarde, sur une page qui n'a
      pourtant rien a cacher. Une ligne par en-tete : le motif ne se forme plus.
      NE PAS LES RECOMPACTER. (Verifie en rejouant les motifs du crochet sur le
      generateur ET sur la page livree : aucune correspondance.)

------------------------------------------------------------------------------
LE FORMULAIRE S'ENRICHIT (17/08/2026) — QUATRE OBLIGATOIRES, TROIS CONDITIONNELS
------------------------------------------------------------------------------
DEMANDE DE DAVID, MOT POUR MOT
  « Sur le formulaire pour Guso Facile : le prenom et nom sont obligatoires. Si
  la personne veut rentrer en tant que structure, une case lui demande le nom de
  sa structure et son type (asso ou autre) et lui demande si elle a la licence
  du spectacle ou pas, et c'est obligatoire. » Puis, dans la foulee : « le tel
  est aussi obligatoire ».

CE QUI EST OBLIGATOIRE MAINTENANT
  PRENOM · NOM · E-MAIL · TELEPHONE. La note precedente disait exactement
  l'inverse pour le telephone (« un formulaire qui exige le telephone perd des
  gens a l'endroit ou il ne faut pas ») : elle est REMPLACEE, pas oubliee.
  L'arbitrage a change parce que chaque demande est etudiee personnellement et
  qu'un e-mail seul ne permet pas de rappeler quelqu'un. LE MESSAGE RESTE LE
  SEUL CHAMP FACULTATIF.
  Meme mecanique que l'e-mail pour les quatre : erreur attrapee AVANT tout
  envoi, message ECRIT et rattache au champ (`aria-describedby` + `aria-invalid`
  + une boite `.f-err` par champ), focus rendu au PREMIER champ fautif, et
  AUCUNE REQUETE RESEAU tant que le formulaire n'est pas valide.
  ⚠️ La validation ne s'arrete PLUS au premier champ fautif : elle les parcourt
  tous et pose un message a cote de chacun, puis rend le focus au premier.
  S'arreter au premier obligerait a envoyer autant de fois qu'il manque de
  champs, en decouvrant les manques un par un.

LE TELEPHONE — TOLERANT, ET JAMAIS REFORMATE
  Les gens ecrivent « 06 12 34 56 78 », « +33 6 12 34 56 78 », « 0612345678 »,
  avec des points ou des tirets. TOUT CELA EST ACCEPTE : on ne valide que la
  presence d'au moins NEUF CHIFFRES, la mise en forme n'est jamais jugee. Et le
  champ n'est PAS reformate sous les doigts pendant la frappe : c'est deroutant,
  et on envoie la chaine telle qu'elle a ete saisie.

LES TROIS CHAMPS DE STRUCTURE
  Ils apparaissent pour « Structure » ET POUR « LES DEUX » — « les deux » EST
  une structure, l'oublier serait le defaut le plus facile a commettre ici.
    - NOM DE LA STRUCTURE (texte libre) ;
    - TYPE : `association` · `autre` (a l'ecran : « Association loi 1901 » et
      « Autre »). DEUX CHOIX, sans champ de precision : David a demande trois
      informations, la precision se dit dans le message, et chaque demande est
      de toute facon lue une par une ;
    - LICENCE D'ENTREPRENEUR DE SPECTACLES : `oui` · `non`.
  ⚠️ LA FORMULATION DE LA LICENCE EST LE POINT SENSIBLE. C'est celle qui
  autorise a employer des artistes. REPONDRE « NON » EST COURANT ET
  PARFAITEMENT LEGITIME : beaucoup d'associations passent par le GUSO
  PRECISEMENT parce qu'elles n'en ont pas. La question est posee au registre
  neutre, la phrase qui l'accompagne dit explicitement que la reponse ne change
  rien a la demande, et le message d'erreur du groupe le redit (« les deux
  reponses conviennent, aucune ne ferme la porte ») parce que c'est LA qu'on
  hesite. Ne jamais la reecrire en quelque chose qui se lirait comme un controle
  de conformite : ce serait faire fuir exactement les structures que l'outil
  vise.
  ⚠️ LE PIEGE CLASSIQUE DU CHAMP CONDITIONNEL — rester obligatoire apres avoir
  disparu — est rendu IMPOSSIBLE par construction : une seule fonction JS,
  `structure()`, commande a la fois l'affichage du bloc et son caractere
  obligatoire. Il ne peut pas y avoir de desaccord entre ce qu'on voit et ce
  qu'on exige. Teste dans les deux sens.
  L'apparition N'EST PAS QUE VISUELLE : le bloc porte `hidden` (il sort donc de
  l'arbre d'accessibilite ET de l'ordre de tabulation quand il est replie), et
  une zone `role="status" aria-live="polite"` annonce en une phrase ce qui vient
  d'apparaitre.

⚠️⚠️ OU PARTENT CES DONNEES — LE POINT TECHNIQUE DECISIF (REECRIT LE 17/08/2026)
  LES VRAIES COLONNES EXISTENT DESORMAIS. La session qui developpe
  l'application les a creees et demande explicitement de NE PLUS DUPLIQUER
  l'information, son motif etant : « le doublon aurait fini par diverger ».
      `structure_name`    text
      `structure_type`    text    (valeur libre : `association`, `autre`…)
      `structure_licence` BOOLEAN
  Ce qui change, point par point :
    1. les trois valeurs partent EN COLONNES, plus dans `context` ;
    2. ⚠️⚠️ `structure_licence` EST UN BOOLEEN. On envoie `true` / `false`,
       JAMAIS `"oui"`, `"non"` ni `"true"`. C'est LE piege de ce chantier :
       mesure avant d'ecrire une ligne de code, une chaine dans cette colonne
       rend `400 22P02 invalid input syntax for type boolean: "oui"` — la
       personne verrait une panne incomprehensible a la derniere etape. La
       conversion se fait a UN SEUL endroit : `(sLic === 'oui')` ;
    3. la ligne lisible ajoutee a la fin de `message` EST RETIREE. `message`
       redevient uniquement le message de la personne ; l'ancre correspondante
       est passee a ZERO pour qu'elle ne revienne pas par reflexe ;
    4. `context` garde `{origin, ts}` et recoit `ua` (le `navigator.userAgent`,
       dont l'auteur de l'app se sert pour tracer d'ou viennent les demandes).
       LES TROIS CLES DE STRUCTURE EN SONT RETIREES : elles vivent maintenant
       dans leurs colonnes ;
    5. LES TROIS COLONNES NE PARTENT QUE POUR UNE STRUCTURE (« Structure » ou
       « Les deux »). Pour un artiste seul, elles ne sont PAS ENVOYEES DU TOUT
       — ni chaine vide, ni `null` : le corps de la requete ne les porte pas.
  Les garde-fous : deux ancres a ZERO (`structure_nom`,
  `structure_licence_spectacles`) interdisent le retour des anciennes cles de
  `context` ; une ancre a ZERO interdit le retour de la ligne dans `message` ;
  et `_controle_formulaire()` compare les cles du corps de la requete a
  `COLONNES_DEMANDE`, une par une — TOUTE COLONNE INCONNUE FAIT REFUSER
  L'ECRITURE, exactement comme avant.

LA LICENCE EST UNE DECLARATION, PAS UN FAIT ETABLI
  Elle a une consequence reelle cote application : elle decide si la structure
  sera enregistree comme EMPLOYEUR (elle peut declarer des embauches, editer
  DPAE et feuillets GUSO) ou comme INTERMEDIAIRE (elle contractualise et
  encaisse, mais ne declare pas). David DEVRA LA VERIFIER avant d'ouvrir la
  creation de DPAE a une structure. La question est donc formulee comme une
  DECLARATION — « Vous declarez disposer de la licence d'entrepreneur de
  spectacles » — et non comme un fait acquis (« Vous avez la licence »).
  ⚠️ Cela ne doit RIEN changer au ton : c'est un formulaire de demande d'acces,
  pas un dossier administratif. Aucun mot de controle ni de verification a
  l'ecran, et la phrase qui desamorce reste mot pour mot (« Repondre "non" ne
  change rien a la demande… ») — elle est protegee par une ancre.

LA MENTION RGPD EST COMPLETEE
  Elle enumere les donnees transmises : les informations de structure y sont
  desormais nommees, la licence au registre declaratif. Le responsable de
  traitement ne change pas — DAVID LESAGE, createur de l'outil, PAS
  L'ASSOCIATION.

------------------------------------------------------------------------------
LA MISE EN VALEUR DU BLOG (16/08/2026) — le constat de David, et sa mesure
------------------------------------------------------------------------------
Verbatim : « le blog n'est pas du tout mis en valeur alors meme qu'il est super
riche et que ca peut etre une enorme porte d'entree. Il faut reconsiderer sa
mise en valeur. »

MESURE AVANT : la page portait DEUX liens vers le blog, et RIEN d'autre — un a
mi-page (y = 3 376 px a 1440) et un tout en bas (y = 11 234 px). Aucun dans le
premier ecran, aucun titre d'article visible nulle part. Pour decouvrir dix-huit
articles il fallait avoir lu la page entiere.

CE QUI A ETE POSE, ET OU :
  1. UN LIEN DANS LE PREMIER ECRAN — dans la rangee `.cta` du hero, A COTE du
     bouton « Demander un acces » et non a la place. C'est un LIEN, pas un
     second bouton : l'ecart n° 8 en tete de ce fichier (« le bouton d'action
     n'existe qu'UNE fois ») tient toujours. Sur ecran large il se pose sur la
     MEME ligne que le bouton — cout en hauteur : zero.
  2. LE BLOC `.mea` (« mise en avant »), en fin de section #situations, LA OU
     se trouvait le premier des deux liens. Il le remplace : sur-titre, titre,
     phrase de raccord, TROIS articles avec leur VRAI titre et leur accroche,
     puis le lien vers l'index. Un titre d'article concret vaut cent fois
     « voir le blog » — le lecteur y reconnait sa propre question.
     ⚠️ POURQUOI DANS #situations ET PAS DANS UNE SECTION A PART : la page est
     sous plafond de hauteur (voir plus bas). Une `<section>` supplementaire
     coutait 184 px de respiration (92 px en haut et en bas) pour rien, alors
     que le bloc est exactement a sa place ici : la section s'appelle « Trois
     situations typiques », le blog en raconte quinze autres. Le bloc porte
     `id="blog"` : il reste une cible d'ancre.
  3. Le lien de fin de FAQ n'a pas bouge (dossier SEO, §6).

POURQUOI CES TROIS ARTICLES-LA (`MISE_EN_AVANT`) — le raisonnement est ecrit
au-dessus de la table elle-meme.

⚠️ LA HAUTEUR EST UNE CONTRAINTE MESUREE, PAS UNE PREFERENCE. La page valait
   11 883 px a 1440 avant cette passe, et elle vient d'absorber une page
   entiere. Plafond retenu : ~12 500 px. Tout ajout se paie : c'est pour cela
   que le bloc `.mea` n'est pas une section, que ses fleches sont dessinees en
   CSS (aucun onzieme pictogramme a maintenir, `NB_PICTOS` inchange) et que le
   lien du hero se range sur la ligne du bouton.

------------------------------------------------------------------------------
LES DEUX CORRECTIONS FACTUELLES DU 16/08/2026 (inventaire des univers)
------------------------------------------------------------------------------
A) « SYNCHRONISATION » DISAIT FAUX. L'univers 3 annoncait : « ce que l'artiste
   renseigne apparait cote structure EN TEMPS REEL, et inversement ». Verifie
   dans le code de l'application par la session qui la developpe : AUCUN
   abonnement temps reel (zero `.channel(`, zero `postgres_changes`, zero
   `realtime`). L'ecriture part bien immediatement, mais LA LECTURE NE SE FAIT
   QU'AU CHARGEMENT de l'espace — deux onglets cote a cote ne se mettent pas a
   jour tout seuls. C'etait la seule promesse de la page qu'une structure
   pouvait dementir en dix secondes.
   Phrase de remplacement, validee par l'auteur de l'app et reprise TELLE
   QUELLE : « Synchronisation — les donnees sont partagees entre l'artiste et
   la structure. » Une ancre a ZERO interdit le retour de « en temps reel ».

B) SIX FONCTIONNALITES LIVREES MANQUAIENT A L'INVENTAIRE. Confirmees dans le
   code par l'auteur, une phrase chacune, reprises telles quelles (seules la
   ponctuation et le placement ont ete ajustes) :
     - « Niveaux de partage » ......... univers 3, juste apres « Synchro-
       nisation » : c'est la meme relation artiste <-> structure ;
     - « Inscription par invitation » . univers 4, juste apres « Faire
       decouvrir l'outil » — la cooptation propose, l'invitation ouvre ;
     - « Hub d'informations du groupe » univers 4, juste apres « Vue groupe » ;
     - « Guide de demarrage », « Guide integre » et « Nouveautes » .. encadre
       « Et aussi », en une ligne « prise en main ». Ces trois-la n'appar-
       tiennent a aucun des quatre univers (ce n'est ni un droit, ni une
       tournee, ni une structure, ni un cercle) : les forcer dans l'un d'eux
       aurait fausse la lecture, et l'encadre « Et aussi » existe exactement
       pour ce cas.
   ⚠️ TOUTES SONT LIVREES : au PRESENT, sans « (a venir) ». `NB_A_VENIR` reste
      a 3. (Il vaut 0 depuis le 17/08/2026 — voir plus haut.)
   ⚠️ UNE SEPTIEME EXISTE ET N'EST PAS ECRITE : la verification des dispo-
      nibilites avec kilometrage entre deux dates. Son auteur ne l'a pas
      verifiee assez finement pour en garantir la description. On ne l'invente
      pas — une de moins vaut mieux qu'une fausse. Ne pas l'ajouter « de
      memoire » : il faudra la faire confirmer.
   ⚠️ « NIVEAUX DE PARTAGE » N'EST PAS « CONFIDENTIALITE GRADUEE ». Les deux
      parlent de ce qu'une structure voit, et l'un est LIVRE quand l'autre est
      « (a venir) » : un lecteur pressé y verrait une contradiction. Ils sont
      donc dans DEUX cartes differentes (univers 3 / univers 4), et leur
      redaction les separe d'elle-meme : « Niveaux de partage » offre TROIS
      niveaux predefinis (tout / l'essentiel administratif / les totaux
      d'heures), « Confidentialite graduee » promet le reglage fin, donnee par
      donnee, dont l'ECRAN COTE ARTISTE n'existe pas encore. Ne pas les
      rapprocher, et ne pas retirer les trois niveaux de la premiere : c'est
      eux qui font la difference visible.
      ⚠️ REVISE LE 17/08/2026. L'ecran cote artiste est deploye, et la
      description que son auteur en donne est CELLE DES TROIS NIVEAUX : le
      « reglage fin, donnee par donnee » n'a jamais existe ailleurs que dans
      cette page. Les deux puces decrivent donc la MEME fonctionnalite, vue de
      deux bouts — ce que la structure recoit (univers 3), ce que l'artiste
      regle (univers 4). Elles restent dans deux cartes, mais la seconde le DIT
      (« le reglage des niveaux de partage ») au lieu de rejouer la meme
      phrase, et elle apporte ce que la premiere n'a pas : le filtrage cote
      serveur. 🚩 Leur fusion en une seule puce se defend : c'est une decision
      de contenu, elle revient a David.

------------------------------------------------------------------------------
LA NUIT DU 16/08/2026 — LE BLOG DEVIENT UNE PORTE, ET QUATRE ECRANS DE PLUS
------------------------------------------------------------------------------
TROIS DEMANDES DE DAVID, dans l'ordre ou il les a faites.

1) « LE BOUTON DU BLOG N'EST MEME PAS UN BOUTON »
   Verbatim : « le bouton "Les dix-huit articles du blog de Guso Facile" est
   minuscule, c'est meme pas un bouton, c'est une ligne. Il faudrait quelque
   chose qui donne plus envie de cliquer. »
   MESURE : les deux renvois vers le blog etaient des `<p class="blog-lien">`
   contenant un `<a>` SANS CLASSE — une ligne soulignee de 16 px, haute de
   38 px. Pour dix-huit articles qui sont probablement la premiere entree du
   site, c'etait le maillon le plus faible de la page.
   CE QUI REMPLACE : un bloc `.blog-cta` — carte cliquable pleine largeur,
   filet degrade en tete, pictogramme au trait dans son cartouche, sur-titre,
   titre en Jost 700, phrase de raccord, et une pastille flechee qui glisse au
   survol. Les DEUX renvois y passent : celui de fin de `#situations` et celui
   de fin de FAQ.
   ⚠️ LA REGLE DU BOUTON D'ACTION UNIQUE TIENT (ecart n° 8 en tete de fichier).
      Le SEUL bouton plein au degrade chaud de la page reste « Envoyer ma
      demande » dans `.acces`. Le bloc du blog est volontairement d'une AUTRE
      FAMILLE : fond de carte translucide, filet dore, pas d'aplat chaud. Il
      est fort, il n'est pas le meme geste. Ne pas lui donner `var(--grad-warm)`
      en fond « pour qu'il se voie mieux » : ce serait remettre deux boutons
      d'action sur la page.
   ⚠️ Les DEUX ancres de texte restent MOT POUR MOT celles du dossier SEO (§6,
      ancre descriptive, jamais « en savoir plus ») : « Les dix-huit articles du
      blog de Guso Facile » et « Toutes les situations concretes sur le blog de
      Guso Facile ». Elles sont simplement devenues le TITRE du bloc.

2) QUATRE APERCUS DE PLUS — la page passe de 6 a 10 maquettes
   Verbatim : « ca manque encore beaucoup de visuel pour illustrer les
   fonctions, visualiser une carte de tournee etc. »
   MESURE : la page valait ~12 800 px pour SIX apercus, soit un visuel tous les
   2 100 px. Matiere (LECTURE SEULE, jamais editee ni deplacee) :
       /Users/davidlesage/CLAUDE/GUSO-FACILE-BACKUPS/maquettes-lot2-pour-resonances.html
   Chacun est pose CONTRE la fonction qu'il illustre, jamais en galerie :
     7. Selecteur « Je regarde » .. juste sous le vis-a-vis artistes |
        structures. C'est le seul ecran qui PROUVE la double vue : un compte,
        deux casquettes. Il ferme la demonstration que les deux colonnes
        ouvrent.
     8. Carte de tournee ......... dans la rangee `.apercus`, sous « Ma
        tournee », pleine largeur — c'est l'ecran de l'univers 2 « Ta tournee,
        organisee ».
     9. « J'ai besoin d'aide » ... colle au bloc du meme nom. La maquette
        montre la QUESTION 1 et SES QUATRE REPONSES, la ou le bloc liste les
        TROIS QUESTIONS : les deux se completent au lieu de se repeter, et
        l'image leve d'elle-meme la confusion 3/4 que la page de reference
        portait (voir la note du bloc `.aide`).
    10. Journal des nouveautes .. sous l'encadre « Et aussi », dont la ligne
        « prise en main » porte la puce « Nouveautes ».
   ⚠️ LES LIBELLES NE SONT PAS REFORMULES. Ceux du selecteur (« Filtre
      d'affichage — ca ne change aucun droit, ni pour toi ni pour les autres »)
      et les QUATRE reponses de « J'ai besoin d'aide » sont repris MOT POUR MOT
      du code de l'application : c'est ce qui garantit qu'un beta-testeur
      retrouvera ces phrases a l'ecran. Une reformulation, meme meilleure,
      casserait la correspondance. Seule l'apostrophe droite est passee en
      apostrophe typographique, comme partout ailleurs sur cette page.
   ⚠️ AUCUN CHIFFRE REEL : ni les 65 dates, ni les 61 feuillets, ni les 37
      lieux — ce sont les donnees de David et d'Iris. Tous les noms de lieux,
      de structures et de personnes sont inventes, et les quatre blocs portent
      la meme mention visible « Apercu de l'interface — donnees fictives » que
      les six autres.

3) LA CARTE — LA VERSION DU FICHIER SOURCE EST CASSEE, ELLE N'EST PAS REPRISE
   ⚠️⚠️ A LIRE AVANT DE « SIMPLIFIER » LE SVG CI-DESSOUS EN REVENANT AUX DIV.
   Le trace de la carte du fichier source est fait de `<div>` PIVOTES et
   dimensionnes en POURCENTAGES (`width:19%;transform:rotate(-38deg)`). La
   largeur d'un element pivote reste relative a la LARGEUR du conteneur, alors
   que la projection du segment depend du RAPPORT largeur/hauteur : des que ce
   rapport change — et il change a chaque largeur d'ecran, le conteneur ayant
   une hauteur fixe de 250 px — LES TRAITS SE DESOLIDARISENT DES POINTS.
   Constate a l'ecran : les traits flottent a cote des points. Aucun reglage
   d'angle ne peut le rattraper, c'est une erreur de modele.
   LA CARTE EST DONC REDESSINEE EN SVG : un `viewBox="0 0 100 52"`, une
   `polyline` (plus son halo), des `circle` pour les points, des `text` pour
   les libelles. Toute la geometrie vit dans le MEME systeme de coordonnees :
   elle est independante de la taille du conteneur, par construction.
   ⚠️ TROIS ELEMENTS PORTENT DU SENS, ce ne sont PAS des ornements :
      - le point DOMICILE, distinct (prune) : le kilometrage se calcule depuis
        l'adresse du profil, la carte doit dire d'ou l'on part ;
      - le LIEU SUPPOSE, en anneau corail : ce sont les lieux que l'app a
        devines (`geo.guessed`) et qu'elle demande de confirmer ;
      - le KILOMETRAGE CUMULE « ≈ 612 km (aller) · 1 224 km aller-retour »,
        qui est la phrase de l'app, au mot pres.
   ⚠️ LA TAILLE DES LIBELLES EST UNE MESURE, PAS UN GOUT : voir le long
      commentaire au-dessus de `CSS_CARTE`. Dans un SVG a `viewBox`, une taille
      de police est une UNITE UTILISATEUR, multipliee par (largeur rendue/100).
      Elle grandit donc avec l'ecran, et surtout elle RETRECIT sur telephone.
      Trois paliers la maintiennent entre 13 et 18 px reels.

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

# ⚠️ `URL_ACCES` A DISPARU LE 16/08/2026. Elle valait
# 'https://guso-facile.vercel.app/presentation.html' : le bouton « Demander un
# acces » envoyait la personne sur un autre domaine, au moment precis ou elle
# allait confier son nom, son e-mail et son telephone. Le formulaire vit
# desormais ICI (voir « LA FUSION DU 16/08/2026 » en tete de fichier). Deux
# ancres a ZERO occurrence interdisent son retour, et l'hote est sorti de
# `HOTES_AUTORISES`.

#: Ou part la demande d'acces. Endpoint PostgREST teste et verifie par la
#: session qui developpe l'application (POST -> 201, prevol OPTIONS -> 200,
#: `access-control-allow-origin: *` depuis notre origine).
URL_DEMANDE = 'https://wqhwfqasoyyeprggjxet.supabase.co/rest/v1/account_requests'

#: L'identifiant d'origine du projet Supabase. SON NOM DIT CE QU'IL EST :
#: « publishable » — publiable. Il n'ouvre aucun droit de lecture (c'est
#: exactement pour cela qu'il ne faut pas demander `Prefer: return=represen-
#: tation` : la relecture de la ligne inseree est refusee, et l'on croirait a un
#: echec alors que l'insertion a reussi), et il est deja public sur la page
#: Vercel depuis des semaines. Il a donc parfaitement sa place dans un depot
#: public : ce n'est pas un secret, c'est l'equivalent d'une adresse.
#: Le crochet `pre-commit` le laisse passer — il traque les cles JWT
#: (« eyJhbGciOi… »), une forme a laquelle celle-ci ne repond pas.
CLE_PUBLIABLE = 'sb_publishable_vLxMMGhr5Jq_RrAQ2g_Fjg_dzdpKDbQ'


# =========================================================================
# LES TROIS ARTICLES MIS EN AVANT (16/08/2026)
# =========================================================================
# POURQUOI CEUX-LA, ET PAS LES TROIS PLUS RICHES.
# Le critere retenu est l'UNIVERSALITE, pas la profondeur : ces trois-la sont
# les questions qu'on tape dans un moteur de recherche AVANT de connaitre
# l'outil, et meme avant de se savoir concerne. Chacun se lit sans prerequis,
# et ensemble ils couvrent les trois moments d'une date :
#   1. AVANT de comprendre — « C'est quoi le GUSO » : le dispositif lui-meme.
#      Zero prerequis, c'est la porte la plus basse du blog, et c'est aussi le
#      mot qui donne son nom a l'outil.
#   2. PENDANT qu'on compte — « Combien de cachets pour 507 heures » : le
#      calcul que TOUT intermittent refait chaque annee.
#   3. APRES, quand ca coince — « Mon employeur ne m'a pas paye mon cachet » :
#      l'accident que tout le monde redoute, et la recherche la plus urgente
#      qui soit (on la tape le soir meme).
#
# CE QU'ON A ECARTE, ET POURQUOI :
#   - « Atteindre ses 507 heures sans angoisse », « Pointer France Travail en
#     5 minutes » et « Accompagner ses artistes sans tableur » sont les trois
#     articles les plus relies du blog… et ce sont MOT POUR MOT les titres des
#     trois « situations typiques » qui se trouvent JUSTE AU-DESSUS de ce bloc
#     dans la page. Les remettre en cartes aurait donne au lecteur trois fois
#     la meme chose. Le bloc les nomme autrement : la phrase de raccord dit que
#     ces trois cas-la sont racontes en entier sur le blog.
#   - les articles « structure » : excellents, mais ils ne parlent qu'a une
#     partie du public — l'inverse d'universel.
#
# ⚠️ CES TITRES ET CES ACCROCHES SONT RECOPIES, PAS REECRITS. Leur source de
#    verite est la table `ARTICLES` de `sources/generate_guso_blog.py` (cles
#    `h1` et `dek`). Ils sont DUPLIQUES ici, et non importes, parce que la
#    regle du depot interdit d'importer un `generate_*.py` (l'import ecrirait
#    ses pages). Le garde-fou `_controle_mise_en_avant()` relit donc les pages
#    d'article DEJA SUR LE DISQUE et refuse d'ecrire si un titre a diverge.
#    Les accroches TUTOIENT (« ce que tu recois ») : c'est le registre du blog,
#    et ce sont ses mots — on ne les neutralise pas, on les cite.
#
# ⚠️ AUCUN SLUG NE CHANGE, JAMAIS : ils sont alignes 1:1 avec le plan de
#    redirections du dossier SEO. Changer un slug ici casserait la migration.
#
#: (slug, rubrique, titre, accroche, duree de lecture)
MISE_EN_AVANT = (
    ('c-est-quoi-le-guso-concretement', 'GUSO',
     'C’est quoi le GUSO, concrètement ?',
     'Le guichet unique qui permet à un employeur occasionnel de déclarer un '
     'artiste en une fois. Qui déclare, ce que tu reçois, dans quels délais.',
     '6 min'),
    ('combien-de-cachets-pour-507-heures', 'Suivi des heures',
     'Combien de cachets faut-il pour atteindre 507 heures ?',
     'Un cachet vaut 12 heures, donc environ 43 cachets par an. Voici le calcul '
     'complet, avec les répétitions et les plafonds à connaître.',
     '6 min'),
    ('employeur-ne-m-a-pas-paye-mon-cachet', 'Paiement',
     'Mon employeur ne m’a pas payé mon cachet : que faire ?',
     'Relance écrite, mise en demeure, puis prud’hommes : les étapes d’un impayé, '
     'les délais à connaître et les interlocuteurs à qui s’adresser.',
     '6 min'),
)

#: nombre d'articles mis en avant. Il sert DEUX fois : autant de cartes,
#: autant de liens vers un article. Trois, et pas quatre : au-dela, la rangee
#: passe a des colonnes de 240 px ou les titres tiennent sur cinq lignes, et le
#: bloc coute plus de hauteur que la page n'en a (voir l'entete).
NB_MISE_EN_AVANT = 3

URL_BLOG = '/guso-facile/blog'


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
#
# ⚠️⚠️ 16/08/2026 — UNE SEULE GRAISSE A ETE AJOUTEE A CETTE URL : `Jost` en 700.
#    Les 29 autres pages gardent `Jost:wght@300;400;500;600`. Cette page (et son
#    blog) demandent `300;400;500;600;700` parce que leurs titres passent en Jost
#    lourd — voir « L'EXCEPTION TYPOGRAPHIQUE » dans CSS_PAGE.
#    CE QUE CA COUTE, MESURE ET NON SUPPOSE : Google sert Jost en fichier
#    VARIABLE. Les `src:` des deux URL sont RIGOUREUSEMENT LES MEMES (verifie en
#    rejouant les deux requetes avec un agent utilisateur Chrome et en comparant
#    les `src:` : trois woff2, identiques au caractere pres). La graisse 700
#    n'ajoute donc AUCUN fichier de police a telecharger — seulement trois
#    regles `@font-face` de plus dans une feuille CSS de ~1 Ko, qui pointent
#    vers des fichiers deja en cache.
#    LE SEUL COUT REEL : l'URL de la feuille differe de celle des 29 autres
#    pages, donc un visiteur qui arrive de `/` fait UNE requete CSS de plus
#    (les woff2, eux, sont deja la). C'est le prix de l'exception, il est connu
#    et il s'arrete la. Ne PAS « harmoniser » en retirant le 700 : les titres
#    retomberaient en 600 et la page reperdrait exactement ce que David
#    reprochait a la version precedente.

# --------------------------------------------------------------------------- #
# L'IMAGE DE PARTAGE (16/08/2026) — CETTE PAGE GARDE `og-image.jpg`, FAUTE DE MIEUX
# --------------------------------------------------------------------------- #
# Le reste du site a recu une image propre a chaque page. Pas celle-ci, et il
# faut dire pourquoi plutot que de bricoler.
#   - La page est en HTML/CSS pur : ses dix apercus d'interface sont DESSINES,
#     il n'existe aucun fichier image a montrer. Le depot n'en contient aucune
#     pour Guso Facile, et on ne fabrique pas d'image ici.
#   - Les seules photos disponibles sont des photos de concert. En poser une sur
#     une page de logiciel administratif ferait croire a un spectacle.
# `og-image.jpg` reste donc, et ce n'est pas absurde : elle montre des artistes
# en scene, et le lecteur vise par cette page EST un artiste intermittent — elle
# dit d'ou vient l'outil, pas ce qu'il fait.
# 🚩 Le jour ou une VRAIE capture de l'application sera disponible (recadree en
#    1200x630, sans aucune donnee personnelle a l'ecran), c'est elle qu'il
#    faudra mettre ici et sur le blog. C'est une decision de David.
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
<meta property="og:image:alt" content="Iris Chasles et David Lesage assis sur la scène du Grand Rex, face à une salle comble.">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://www.resonancesproductions.org/guso-facile">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0e0f24">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Jost:wght@300;400;500;600;700&display=swap" rel="stylesheet">
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
# ⚠️ 16/08/2026 — `.legal` : #6b6b80 -> #8b8ba6, ET CETTE PAGE ETAIT LA SEULE
#    A NE PAS L'AVOIR. Sur le pied de page #08091a, l'ancienne valeur donnait
#    3,80:1, sous le seuil de 4,5:1. `theme_chaleur.py` avait corrige ce defaut
#    le 15/08 pour tout le site — mais /guso-facile N'IMPORTE PAS ce module :
#    elle est l'ORIGINE du langage visuel et porte sa propre copie de la couche.
#    Resultat : 29 pages reparees, celle-ci oubliee, et personne ne pouvait le
#    voir en lisant `theme_chaleur.py` qui affirmait « sur les 10 pages ».
#    Trouve en mesurant les contrastes dans le navigateur, page par page.
#    #8b8ba6 = 5,96:1, et reste tout aussi discret.
CSS_BASE = (""":root{--night:#0e0f24;--night2:#141633;--ink:#eae7f3;--muted:#a9a6c4;--gold:#d8b25a;--gold2:#f0d18a;--plum:#8f7ad1;--card:#191b3d;--line:rgba(216,178,90,.26)}
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
"""
           # pied de page : #6b6b80 donnait 3,80:1 (voir la note du generateur)
           """.legal{margin-top:40px;text-align:center;color:#8b8ba6;font-size:13px}
@media(max-width:760px){.fgrid{grid-template-columns:1fr;gap:24px}section{padding:60px 0}}
p a:not(.btn):not(.adh){text-decoration:underline;text-decoration-color:rgba(216,178,90,.4);text-underline-offset:3px}
""")

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
#
# ⚠️ 16/08/2026 — CETTE PAGE NE PASSE PAS PAR `theme_chaleur.py`. Elle est
#    l'ORIGINE du langage visuel : elle porte sa propre copie du degrade, et
#    les deux fichiers doivent rester lisibles cote a cote (c'est ecrit en
#    tete de `theme_chaleur.py`). La refonte des surfaces et des accents du
#    16/08 est donc recopiee ici A L'IDENTIQUE. Le raisonnement complet, les
#    mesures et les contrastes recalcules sont dans `theme_chaleur.py` : un
#    seul endroit ou l'ecrire, deux endroits ou l'appliquer.
CSS_PAGE = ("""/* ===== Guso Facile ===== */
"""
           # --- le degrade signature, decline partout ------------------------------
           # surfaces etagees : fond -> carte = x3,30 de luminance (x2,36 avant)
           """:root{--night2:#161839;--card:#1e214a;
/* accents plus vifs — l'or primaire ne bouge pas */
--gold2:#f8d274;--plum:#9374e2;--coral:#ee8062;--plum2:#b38ff5;
--grad:linear-gradient(95deg,var(--gold2),var(--gold) 32%,var(--coral) 66%,var(--plum2));
--grad-warm:linear-gradient(100deg,var(--gold2),var(--gold) 46%,var(--coral))}
.gf-defs{position:absolute;width:0;height:0;overflow:hidden}
.ic{width:23px;height:23px;display:block;flex:0 0 auto}
.grad-t{width:fit-content;max-width:100%;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
.mark{background-image:var(--grad);background-repeat:no-repeat;background-size:100% 2px;background-position:0 100%;padding-bottom:3px}
"""
           # trois lueurs fixes : c'est ce qui enleve le fond « noir de notice »
           """body::before{content:'';position:fixed;inset:0;z-index:-1;pointer-events:none;background:radial-gradient(58vw 40vw at 10% -6%,rgba(216,178,90,.11),transparent 62%),radial-gradient(52vw 38vw at 100% 14%,rgba(238,128,98,.10),transparent 62%),radial-gradient(62vw 46vw at 46% 106%,rgba(147,116,226,.12),transparent 62%)}
"""
           # ⚠️ 92 -> 86 px LE 16/08/2026, ET C'EST UNE COMPENSATION, PAS UN REGLAGE.
           # La refonte du 14/08 avait porte la respiration des sections de 78 a 92 px
           # (« DE L'AIR », levier n° 3 ci-dessus). La mise en valeur du blog et les six
           # fonctionnalites ajoutees le 16/08 font grossir la page, qui est sous plafond
           # mesure (~12 500 px a 1440). 86 px reste tres au-dessus des 78 px d'avant la
           # refonte, l'ecart de 6 px ne se voit pas a l'oeil, et il rend 96 px sur les
           # huit sections. Meme raisonnement pour les 66 -> 62 px du telephone, plus
           # bas. Ne pas descendre en dessous : sous ~80 px la page redevient une notice.
           """section{padding:86px 0}
.divider{height:2px;background:linear-gradient(90deg,transparent,rgba(216,178,90,.42) 16%,rgba(238,128,98,.5) 50%,rgba(179,143,245,.42) 84%,transparent)}
.kick{display:inline-block;background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
.sec-title{letter-spacing:.01em}
.lead b,.body b{color:#fff}
"""
           # boutons : le principal porte le degrade chaud, le fantome un filet dore
           """.btn{border-radius:999px;padding:15px 28px}
.btn svg{width:18px;height:18px;flex:0 0 auto}
.acces .btn{background:var(--grad-warm);color:#1b1206;box-shadow:0 14px 34px -16px rgba(238,128,98,.6)}
"""
           # la fleche du bouton reprend la couleur du TEXTE : le degrade signature, clair, disparaissait sur le bouton clair (mesure a l'ecran)
           """.acces .btn svg{stroke:#1b1206}
.acces .btn:hover{box-shadow:0 20px 42px -14px rgba(238,128,98,.7)}
.btn.ghost{background:linear-gradient(180deg,rgba(255,255,255,.055),rgba(255,255,255,.02));border:1px solid rgba(248,210,116,.3);color:var(--gold2)}
.btn.ghost:hover{border-color:rgba(248,210,116,.55)}
"""
           # --- hero ----------------------------------------------------------------
           """.gf-top{padding:132px 0 78px;background:radial-gradient(900px 560px at 6% -12%,rgba(147,116,226,.22),transparent 62%),radial-gradient(760px 480px at 96% 8%,rgba(238,128,98,.14),transparent 62%),radial-gradient(720px 470px at 60% 108%,rgba(216,178,90,.13),transparent 62%),linear-gradient(180deg,#0b0c1e,var(--night))}
.gf-top h1{font-size:clamp(38px,7vw,74px);font-weight:600;line-height:1.02;letter-spacing:.02em}
.gf-claim{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(20px,2.9vw,29px);line-height:1.32;margin-top:16px;max-width:720px}
.badge{display:inline-flex;align-items:center;gap:9px;margin-top:28px;padding:9px 18px;border:1px solid rgba(248,210,116,.34);border-radius:999px;color:var(--gold2);font-size:13.5px;letter-spacing:.12em;text-transform:uppercase;font-weight:500;background:linear-gradient(90deg,rgba(216,178,90,.14),rgba(238,128,98,.10))}
.badge::before{content:'';width:7px;height:7px;border-radius:50%;background:var(--grad-warm);flex:0 0 auto}
.gf-top .cta{margin-top:32px}
.band{background:linear-gradient(180deg,#0b0c1e,#101128 55%,var(--night))}
"""
           # hero : texte a gauche, jauge des 507 h a droite (empile sous 1000 px)
           """.gf-topgrid{display:grid;gap:38px;align-items:center}
@media(min-width:1000px){.gf-topgrid{grid-template-columns:minmax(0,1fr) 400px}}
"""
           # ⚠️ LE RESSERREMENT DU 16/08/2026 — huit valeurs, une seule intention.
           # `.cas`, `.univers`, `.etapes-t`, `.veille`, `.guilde`, `.aussi` et `.etat`
           # sont passes de 42/40/38 px de marge haute a 34/32, et le panneau `.acces` de
           # 46/40 px de rembourrage vertical a 40/34. C'est la SECONDE moitie de la
           # compensation de hauteur decrite plus haut (la premiere etant les sections a
           # 86 px) : la mise en valeur du blog et les six fonctionnalites ajoutees le
           # meme jour ont fait grossir la page, qui est sous plafond mesure. Six a huit
           # pixels sur une marge de quarante ne se voient pas ; ils rendent une
           # cinquantaine de pixels au total. Ne pas descendre plus bas : c'est cette
           # respiration qui separe les blocs les uns des autres.
           # --- LA DOUBLE VUE « artistes | structures » (16/08/2026) ---------------
           # Elle REMPLACE la grille `.univers` a plat (2 x 2) : les univers 1 et 2 sont
           # desormais SOUS un en-tete « Pour les artistes », l'univers 3 sous « Pour les
           # structures », et l'univers 4 en dessous, pleine largeur, comme terrain
           # commun. Le raisonnement complet est dans l'entete du fichier.
           # ⚠️ LE POINT DE BASCULE RESTE 761 px, celui de l'ancienne grille, ET C'EST
           # UNE MESURE. Un premier essai a 901 px paraissait plus confortable — deux
           # colonnes de moins de 430 px, ca serre. Mesure faite : a 820 px la page
           # passait de 14 035 a 15 409 px, soit +1 374 px POUR LES TABLETTES SEULES,
           # parce que tout s'y empilait. Et l'ancienne grille tenait deja parfaitement
           # a 761 px en deux colonnes. On ne paie pas 1 374 px de defilement pour du
           # confort a une largeur ou rien ne debordait. Sous 761 px les deux colonnes
           # s'empilent, en-tete compris : on lit « Pour les artistes » puis ses cartes,
           # puis « Pour les structures » puis les siennes — la dualite reste lisible,
           # elle se lit simplement l'une apres l'autre.
           """.duo{display:grid;grid-template-columns:minmax(0,1fr);gap:26px;margin-top:30px}
@media(min-width:761px){.duo{grid-template-columns:repeat(2,minmax(0,1fr))}}
.duo-col{display:flex;flex-direction:column;gap:24px;min-width:0}
"""
           # l'en-tete de colonne : le filet degrade sous le titre est ce qui fait lire
           # les deux colonnes comme un vis-a-vis et non comme deux listes voisines
           """.duo-h{display:flex;gap:14px;align-items:center;padding-bottom:15px;background-image:var(--grad);background-repeat:no-repeat;background-size:100% 2px;background-position:0 100%}
.duo-t{font-size:22px;font-weight:700;color:#fff;line-height:1.16;letter-spacing:-.012em}
.duo-q{display:block;font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--plum2);margin-top:4px;font-weight:500}
"""
           # la rangee des deux apercus cote artiste, juste sous la colonne qu'ils
           # illustrent (fiche d'une date, puis enchainement des dates)
           """.apercus{display:grid;grid-template-columns:minmax(0,1fr);gap:26px;margin-top:26px}
@media(min-width:761px){.apercus{grid-template-columns:repeat(2,minmax(0,1fr))}}
"""
           # « et pour les deux » : l'univers 4 ferme la section, pleine largeur
           """.deux{margin-top:40px;padding-top:28px;background-image:linear-gradient(90deg,transparent,rgba(216,178,90,.34) 16%,rgba(238,128,98,.4) 50%,rgba(179,143,245,.34) 84%,transparent);background-repeat:no-repeat;background-size:100% 1px;background-position:0 0}
.deux .u-card{margin-top:18px}
.u-card{position:relative;overflow:hidden;background:linear-gradient(180deg,#1c1e46,#171935);border:1px solid rgba(255,255,255,.07);border-radius:22px;padding:30px 28px 26px;box-shadow:0 20px 44px -30px rgba(0,0,0,.95)}
.u-card::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad)}
.u-head{display:flex;align-items:center;gap:14px}
.u-ico,.duo-ico{flex:0 0 auto;width:44px;height:44px;display:flex;align-items:center;justify-content:center;border-radius:14px;border:1px solid rgba(248,210,116,.22);background:linear-gradient(140deg,rgba(216,178,90,.16),rgba(238,128,98,.12) 55%,rgba(147,116,226,.14))}
"""
           # le mot-cle du titre de section, peint au degrade CHAUD et non au degrade
           # complet : sur deux lettres (« et »), les quatre arrets de `--grad` se
           # compriment en une bouillie — mesure a l'ecran. `--grad-warm` n'en a que
           # trois et il reste lisible a cette echelle.
           # ⚠️⚠️ `background-image` ET SURTOUT PAS `background`. La forme raccourcie
           # REMET `background-clip` a `border-box` : le degrade cesse d'etre decoupe par
           # les lettres, et comme `-webkit-text-fill-color:transparent` de `.grad-t`
           # tient toujours, le mot disparait DANS UN RECTANGLE OR PLEIN. Vu a l'ecran au
           # premier essai, invisible en relisant le CSS.
           """.sec-title .grad-t{display:inline;background-image:var(--grad-warm)}
.u-num{letter-spacing:.28em;text-transform:uppercase;font-size:13px;font-weight:600;color:var(--gold)}
.u-card h3{font-size:27px;font-weight:600;color:#fff;line-height:1.15;margin-top:3px}
.u-sub{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--plum2);font-size:18.5px;line-height:1.4;margin-top:12px}
.u-card ul{list-style:none;margin-top:20px}
.u-card li{position:relative;padding-left:24px;margin-top:14px;color:#d7d4ea;font-size:15.5px;line-height:1.62}
.u-card li::before{content:'';position:absolute;left:1px;top:9px;width:8px;height:8px;border-radius:2px;background:var(--grad-warm);transform:rotate(45deg)}
.u-card li.soon::before{background:none;border:1.5px solid var(--plum2)}
.u-card li b{color:#fff;font-weight:500}
.u-card li i{font-style:normal;display:inline-block;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--plum2);border:1px solid rgba(179,143,245,.4);background:rgba(147,116,226,.12);border-radius:999px;padding:1px 9px;line-height:1.5}
.aussi{margin-top:34px;padding:26px 28px;border:1px solid rgba(255,255,255,.07);border-radius:20px;background:linear-gradient(180deg,rgba(28,30,70,.72),rgba(23,25,53,.5));display:flex;gap:18px;align-items:flex-start}
.aussi .ic-w,.precision .ic-w{flex:0 0 auto;line-height:0;margin-top:3px}
.aussi .ic{width:26px;height:26px}
.aussi .u-num{display:block;margin-bottom:8px}
.aussi p{color:#d7d4ea;font-size:15.5px}
.aussi .aussi-p2{margin-top:12px;padding-top:12px;border-top:1px solid rgba(248,210,116,.18)}
.aussi b{color:#fff;font-weight:500}
"""
           # --- trois situations : de vraies cartes, plus un simple filet a gauche --
           """.cas-note{color:var(--muted);font-size:15px;margin-top:14px;max-width:62ch}
.cas{display:grid;grid-template-columns:repeat(auto-fit,minmax(288px,1fr));gap:26px;margin-top:34px}
.cas article{position:relative;overflow:hidden;border:1px solid rgba(255,255,255,.07);border-radius:22px;background:linear-gradient(180deg,#1c1e46,#171935);padding:28px 26px 26px;box-shadow:0 20px 44px -30px rgba(0,0,0,.95)}
.cas article::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad)}
.cas-ico{width:44px;height:44px;display:flex;align-items:center;justify-content:center;border-radius:14px;border:1px solid rgba(248,210,116,.22);background:linear-gradient(140deg,rgba(216,178,90,.16),rgba(238,128,98,.12) 55%,rgba(147,116,226,.14));margin-bottom:16px}
.cas h3{font-size:25px;font-weight:600;color:#fff;line-height:1.18}
.cas p{color:#d7d4ea;font-size:15.5px;margin-top:11px}
"""
           # --- l'etat du projet ----------------------------------------------------
           """.etat{position:relative;overflow:hidden;margin-top:32px;border:1px solid rgba(255,255,255,.08);border-radius:24px;background:linear-gradient(180deg,rgba(28,30,70,.9),rgba(20,22,51,.6));padding:38px 36px;max-width:900px;box-shadow:0 26px 60px -40px rgba(0,0,0,.95)}
.etat::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad)}
.etat p{color:#d7d4ea;font-size:16px}
.etat p + p{margin-top:16px}
.etat .first{color:#fff;font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(21px,3vw,28px);line-height:1.3;font-style:italic}
"""
           # --- le lien avec l'association : la precision sort en encadre -----------
           """.precision{display:flex;gap:14px;align-items:flex-start;margin-top:28px;max-width:760px;padding:20px 22px;border:1px solid rgba(179,143,245,.28);border-radius:18px;background:linear-gradient(135deg,rgba(147,116,226,.12),rgba(238,128,98,.07))}
.precision .ic{width:24px;height:24px}
.precision p{color:#d7d4ea;font-size:15px;line-height:1.65;margin:0}
"""
           # --- appel a l'action : un panneau, pas une fin de page ------------------
           """.acces{position:relative;overflow:hidden;max-width:880px;border:1px solid rgba(255,255,255,.09);border-radius:26px;padding:40px 42px 34px;background:linear-gradient(135deg,rgba(216,178,90,.12),rgba(238,128,98,.10) 48%,rgba(147,116,226,.12));box-shadow:0 30px 70px -46px rgba(0,0,0,.95)}
.acces::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad)}
.mention{margin-top:20px;max-width:660px;color:var(--muted);font-size:14px;line-height:1.65}
.mention + .mention{margin-top:12px}
"""
           # --- le titre principal porte la phrase complete (dossier SEO, section 2) -
           # La marque reste en grand ; la suite passe en seconde ligne, a l'interieur du
           # MEME titre — celui que lisent Google et un lecteur d'ecran est donc entier.
           # (Ne pas ecrire la balise en toutes lettres dans ce commentaire : le
           # garde-fou compte ses occurrences dans la page livree, CSS compris.)
           """.gf-top h1 .h1-sous{display:block;font-size:clamp(17px,2.4vw,26px);font-weight:500;line-height:1.24;letter-spacing:.02em;margin-top:10px}
"""
           # --- « Trois etapes, c'est tout » : une bande legere, pas des cartes -----
           """.etapes-t{margin-top:34px}
.etapes{display:grid;grid-template-columns:minmax(0,1fr);gap:16px;margin-top:16px}
@media(min-width:761px){.etapes{grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}}
.etape{position:relative;overflow:hidden;border:1px solid rgba(255,255,255,.07);border-radius:18px;background:linear-gradient(180deg,rgba(28,30,70,.72),rgba(23,25,53,.5));padding:22px 22px 20px}
.etape::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad)}
.etape h3{font-size:21px;font-weight:600;color:#fff;line-height:1.2;margin-top:4px}
.etape .etape-d{color:#d7d4ea;font-size:15.5px;margin-top:9px}
"""
           # --- l'encart « la Guilde » (longueur retenue et adoucissements : entete) -
           """.guilde{display:flex;gap:18px;align-items:flex-start;margin-top:34px;max-width:900px;padding:28px 30px 26px;border:1px solid rgba(179,143,245,.28);border-radius:22px;background:linear-gradient(135deg,rgba(147,116,226,.13),rgba(238,128,98,.08) 62%,rgba(216,178,90,.08));box-shadow:0 24px 56px -40px rgba(0,0,0,.95)}
.guilde .ic-w{flex:0 0 auto;line-height:0;margin-top:4px}
.guilde .ic{width:26px;height:26px}
.guilde .u-num{display:block;margin-bottom:8px}
.guilde i{font-style:normal;display:inline-block;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--plum2);border:1px solid rgba(179,143,245,.4);background:rgba(147,116,226,.12);border-radius:999px;padding:1px 9px;line-height:1.5;margin-left:5px}
.guilde-claim{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(19px,2.4vw,24px);line-height:1.32}
.guilde .guilde-p{color:#d7d4ea;font-size:15.5px;margin-top:13px}
"""
           # --- la cloture de « Jouons cartes sur table » (mots de David) -----------
           # En serif italique : c'est le registre des TITRES de cette page, celui qui a
           # le droit de tutoyer. Le corps, lui, reste neutre (voir l'entete, point 3).
           """.etat .etat-fin{color:#fff;font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:clamp(19px,2.4vw,24px);line-height:1.32;margin-top:24px;padding-top:20px;border-top:1px solid rgba(216,178,90,.28)}
"""
           # --- la FAQ : REPLIEE, jamais empilee (voir l'entete) --------------------
           # <details> natif : aucun JavaScript, et le contenu d'un accordeon reste lu
           # par Google. La fleche est dessinee en CSS (deux bords tournes a 45deg) —
           # ni image, ni emoji, ni onzieme pictogramme a maintenir.
           """.faq{max-width:860px;margin-top:34px}
.faq-q{border:1px solid rgba(255,255,255,.08);border-radius:18px;background:linear-gradient(180deg,rgba(28,30,70,.72),rgba(23,25,53,.5));margin-bottom:11px;overflow:hidden}
.faq-q summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:16px;padding:15px 20px;min-height:44px}
.faq-q summary::-webkit-details-marker{display:none}
.faq-q summary h3{flex:1 1 auto;min-width:0;font-size:21px;font-weight:600;color:#fff;line-height:1.28}
.faq-q summary::after{content:'';flex:0 0 auto;width:9px;height:9px;margin-right:3px;border-right:1.6px solid var(--gold2);border-bottom:1.6px solid var(--gold2);transform:rotate(45deg) translateY(-3px)}
.faq-q[open] summary{border-bottom:1px solid rgba(216,178,90,.22)}
.faq-q[open] summary::after{transform:rotate(225deg) translateY(-3px)}
.faq-q .faq-r{color:#d7d4ea;font-size:15.5px;padding:15px 20px 18px}
"""
           # --- les deux renvois vers le blog (maillage, dossier §6) ---------------
           # ⚠️ ILS ETAIENT UNE LIGNE DE TEXTE, ILS SONT DEVENUS UN BLOC (16/08/2026,
           # nuit). Verbatim de David : « le bouton "Les dix-huit articles du blog de
           # Guso Facile" est minuscule, c'est meme pas un bouton, c'est une ligne. Il
           # faudrait quelque chose qui donne plus envie de cliquer. » C'etait exact :
           # un `<a>` sans classe, souligne, haut de 38 px, pour la porte d'entree la
           # plus riche du site.
           # ⚠️⚠️ IL NE DOIT PAS DEVENIR UN SECOND BOUTON D'ACTION. Le seul aplat au
           # degrade chaud de la page reste « Envoyer ma demande » (`.acces .btn`) —
           # voir l'ecart n° 8 en tete de fichier. Ce bloc joue donc dans une AUTRE
           # famille : fond de carte translucide, filet dore, halo au survol. Fort,
           # mais pas le meme geste. Ne pas lui poser `var(--grad-warm)` en fond.
           # Le filet de tete au degrade et la pastille flechee (dessinee en CSS,
           # aucun picto de plus a maintenir) sont ce qui le rend cliquable a l'oeil.
           """.blog-cta{position:relative;overflow:hidden;display:flex;align-items:center;gap:18px;margin-top:30px;max-width:760px;padding:22px 24px;border:1px solid rgba(248,210,116,.3);border-radius:22px;background:linear-gradient(135deg,rgba(216,178,90,.13),rgba(238,128,98,.09) 58%,rgba(147,116,226,.12));box-shadow:0 24px 56px -38px rgba(0,0,0,.95);transition:transform .2s,border-color .2s,box-shadow .2s}
.blog-cta::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad)}
.blog-cta:hover{transform:translateY(-3px);border-color:rgba(248,210,116,.6);box-shadow:0 30px 64px -34px rgba(0,0,0,.95),0 0 48px -14px rgba(238,128,98,.42)}
.blog-cta-ic{flex:0 0 auto;width:52px;height:52px;display:flex;align-items:center;justify-content:center;border-radius:16px;border:1px solid rgba(248,210,116,.26);background:linear-gradient(140deg,rgba(216,178,90,.18),rgba(238,128,98,.13) 55%,rgba(147,116,226,.16))}
.blog-cta-ic .ic{width:27px;height:27px}
.blog-cta-txt{flex:1 1 auto;min-width:0}
.blog-cta-k{display:block;font-size:13px;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--gold);margin-bottom:6px}
.blog-cta-t{display:block;font-family:'Jost',sans-serif;font-size:21px;font-weight:700;letter-spacing:-.012em;line-height:1.2;color:#fff}
.blog-cta-d{display:block;color:#cfcbe4;font-size:15px;line-height:1.55;margin-top:8px}
.blog-cta-go{flex:0 0 auto;width:40px;height:40px;border-radius:50%;border:1px solid rgba(248,210,116,.34);background:rgba(216,178,90,.1);display:flex;align-items:center;justify-content:center;transition:transform .2s,background .2s}
.blog-cta-go::after{content:'';width:9px;height:9px;margin-left:-3px;border-right:1.8px solid var(--gold2);border-bottom:1.8px solid var(--gold2);transform:rotate(-45deg)}
.blog-cta:hover .blog-cta-go{transform:translateX(3px);background:rgba(216,178,90,.2)}
"""
           # sous 560 px le bloc se plie en deux rangees : le cartouche et la fleche
           # d'abord (la ligne qui dit « ca se clique »), le texte en dessous sur toute
           # la largeur. Mesure : a 390 px, en une seule rangee, il ne restait que
           # 184 px au titre, qui tombait sur cinq lignes.
           """@media(max-width:560px){.blog-cta{flex-wrap:wrap;gap:14px;padding:20px 18px}
.blog-cta-ic{width:44px;height:44px}
.blog-cta-ic .ic{width:24px;height:24px}
.blog-cta-go{margin-left:auto}
.blog-cta-txt{flex:1 1 100%;order:2}
.blog-cta-t{font-size:19px}}
"""
           # --- la mise en valeur du blog (16/08/2026) -----------------------------
           # Le lien du hero est DANS la rangee `.cta`, a cote du bouton : au-dela de
           # ~1000 px il se pose sur la MEME ligne, donc il ne coute pas un pixel de
           # hauteur. C'est un lien souligne, jamais un second bouton — la page n'a
           # qu'UN geste possible (voir l'ecart n° 8 en tete de fichier).
           """.gf-top .cta{display:flex;flex-wrap:wrap;align-items:center;gap:8px 22px}
.hero-blog{display:inline-flex;align-items:center;gap:11px;min-height:44px;padding:11px 0;color:var(--gold2);font-size:15.5px;text-decoration:underline;text-decoration-color:rgba(248,210,116,.4);text-underline-offset:4px}
.hero-blog::before{content:'';flex:0 0 auto;width:7px;height:7px;border-radius:2px;background:var(--grad-warm);transform:rotate(45deg)}
.hero-blog:hover{text-decoration-color:var(--gold2)}
"""
           # --- le lien de connexion des beta-testeurs (17/08/2026) ----------------
           # Il est SOUS la rangee `.cta`, pas dedans : ce n'est pas un troisieme
           # geste offert a tout le monde sur la meme ligne, c'est une porte de
           # service pour ceux qui ont deja un compte.
           # COUT EN HAUTEUR, MESURE ET NON SUPPOSE (page rendue, `scrollHeight`
           # avec puis sans le bloc) : 50 px a 390 px et a 820 px — les 44 px de
           # cible tactile plus 6 px de marge —, et ZERO A 1440 px. Le zero n'est
           # pas une erreur de mesure : au-dela de 1000 px, `.gf-topgrid` passe a
           # deux colonnes et la colonne de droite (la jauge des 507 h, 400 px)
           # est la plus haute des deux ; les 50 px s'ajoutent donc a la colonne
           # de gauche sans faire grandir le hero. Le lien est gratuit sur grand
           # ecran, et il coute une demi-ligne sur telephone.
           # POURQUOI `--muted` ET PAS `--gold2` : la hierarchie du premier ecran
           # doit rester lisible d'un coup d'oeil — bouton dore plein (le geste de
           # la page) > lien blog dore (la porte d'entree editoriale) > ce lien-ci,
           # gris. Un troisieme element dore aurait mis les trois au meme rang.
           # LES DEUX MESURES, FAITES ET NON SUPPOSEES :
           #   - cible tactile : `min-height:44px` + `display:inline-flex`, la
           #     methode deja retenue pour `.offer .who a` sur /le-nid — sans le
           #     flex, un <a> en ligne ne prend que la hauteur de sa ligne de
           #     texte et le `min-height` reste sans effet ;
           #   - contraste : #a9a6c4 sur le fond REELLEMENT peint derriere le lien.
           #     Le hero a un fond OPAQUE (`linear-gradient(180deg,#0b0c1e,
           #     var(--night))` sous trois lueurs radiales), donc les lueurs fixes
           #     de `body::before` ne comptent pas ici — c'est la pile de `.gf-top`
           #     et elle seule. Le fond a ete recalcule aux QUATRE COINS ET AU
           #     CENTRE de la cible de 44 px, en refaisant le calcul des trois
           #     `radial-gradient` a partir de la geometrie rendue : #0d0e23
           #     partout, soit 8,10:1. Aucune des trois lueurs n'atteint ce point
           #     (la plus forte, la prune, est centree au-dessus du bord haut du
           #     hero et s'eteint bien avant). Plancher WCAG AA : 4,5:1 — on est
           #     a 1,8 fois le plancher, il reste de la marge si le fond du hero
           #     etait un jour eclairci.
           # Le soulignement est a 38 % d'opacite : present, jamais criard — et il
           # passe a l'or au survol, comme `.hero-blog`, pour que la page n'ait
           # qu'une seule maniere de dire « ceci est un lien ».
           """.hero-cnx{margin-top:6px}
.hero-cnx a{display:inline-flex;align-items:center;min-height:44px;color:var(--muted);font-size:14.5px;text-decoration:underline;text-decoration-color:rgba(169,166,196,.38);text-underline-offset:4px}
.hero-cnx a:hover{color:var(--gold2);text-decoration-color:var(--gold2)}
"""
           # --- LE SOMMAIRE DE LA PAGE (17/08/2026) -------------------------------
           # POURQUOI IL EXISTE, ET CE QU'IL NE FAIT PAS.
           # La page mesurait 25 455 px de haut a 390 px — une trentaine d'ecrans de
           # telephone. Quelqu'un qui SAIT ce qu'il vient chercher (« c'est combien ? »,
           # « c'est pour moi ? », « comment je demande un acces ? ») n'avait aucun
           # moyen d'y aller autrement qu'en faisant defiler. Le sommaire lui donne le
           # controle SANS RIEN CACHER : il ne replie rien, il ne deplace rien, il
           # n'enleve pas un mot. C'est la premiere des trois couches de la passe du
           # 17/08/2026 (sommaire · inventaire repliable · retour en haut), et la seule
           # qui serve AUSSI a celui qui ne clique pas : elle annonce le plan.
           #
           # ⚠️ CE N'EST PAS UNE SECONDE BARRE DE NAVIGATION, et trois choix le disent :
           #   1. il vit DANS le hero de la page, sous le lien de connexion, pas dans
           #      une bande collee en haut de l'ecran — le menu du site, lui, est en
           #      `position:fixed` avec la marque de l'association ;
           #   2. il est introduit par « Sur cette page », qui dit son perimetre en
           #      trois mots ;
           #   3. ses libelles sont des PHRASES DE LECTEUR (« Ce qu'il y a dedans »),
           #      jamais les titres de section recopies — le menu du site, lui, nomme
           #      des pages.
           # Le point isole (`li + li::before`) acheve de le faire lire comme une liste
           # en ligne et non comme une rangee de boutons : la page n'a QU'UN geste
           # (ecart n° 8 en tete de fichier), et un sommaire n'en est pas un.
           #
           # COUT EN HAUTEUR — MESURE, PAS SUPPOSE (`scrollHeight` avec puis sans) :
           #   390 px : +193 px · 820 px : +105 px · 1440 px : +0 px.
           # Le zero de 1440 n'est pas une erreur : au-dela de 1000 px `.gf-topgrid`
           # passe a deux colonnes et c'est la jauge des 507 h (400 px, a droite) qui
           # fixe la hauteur du hero — exactement le mecanisme qui rendait deja le lien
           # de connexion gratuit sur grand ecran. Le sommaire se paie donc UNIQUEMENT
           # la ou il sert le plus (le telephone), et il y rend 154 px contre les
           # 3 000 px et plus que la couche 2 fait gagner. C'est pour tenir ce budget
           # qu'il n'a ni fond, ni cadre, ni pictogramme.
           #
           # LA CIBLE TACTILE EST OBTENUE PAR `inline-flex` + `min-height:44px` — la
           # methode deja retenue pour `.hero-cnx` et pour `.offer .who a` de /le-nid :
           # sans le flex, un <a> en ligne ne prend que la hauteur de sa ligne de texte
           # et le `min-height` reste sans effet. Mesure faite, pas deduite.
           """.gf-som{margin-top:22px;padding-top:15px;border-top:1px solid var(--line)}
.gf-som-t{letter-spacing:.28em;text-transform:uppercase;font-size:13px;font-weight:600;color:var(--muted)}
.gf-som ul{list-style:none;display:flex;flex-wrap:wrap;align-items:center;gap:0 13px}
.gf-som li{display:flex;align-items:center;gap:13px}
.gf-som li+li::before{content:'·';color:var(--muted);opacity:.5}
.gf-som a{display:inline-flex;align-items:center;min-height:44px;color:var(--muted);font-size:15px}
.gf-som a:hover{color:var(--gold2);text-decoration:underline;text-decoration-color:var(--gold2);text-underline-offset:4px}
"""
           # ⚠️⚠️ `scroll-margin-top` — SANS CETTE LIGNE LE SOMMAIRE MENAIT SOUS LE
           # MENU. Le menu du site est en `position:fixed` : un lien d'ancre pose le
           # HAUT de la section a y=0, donc sous la barre. Le defaut existait deja pour
           # le bouton « Demander un acces » du hero (seule ancre de la page jusqu'ici),
           # il ne se voyait pas parce qu'on ne le suivait qu'une fois. Avec cinq liens
           # il devenait la regle.
           # LES QUATRE MESURES QUI DONNENT CES DEUX VALEURS (hauteur reellement
           # peinte par `.nav`, puis distance du premier texte au haut de la section) :
           #     320 px : barre 144 px · premier texte a 67 px de la section
           #     390 px : barre 110 px · 67 px
           #     820 px : barre  77 px · 91 px
           #    1440 px : barre  75 px · 91 px
           # Il faut donc `marge + 67 >= 144 + une respiration` sur telephone, et
           # `marge + 91 >= 77 + …` au-dela. D'ou 100 px sous 761 px et 56 px au-dela,
           # soit 19 px de degagement dans le pire cas mesure (320 px) et 70 px sur
           # grand ecran. Une valeur unique aurait fait atterrir un ecran large 100 px
           # trop tot, dans le vide du bas de la section precedente.
           # ⚠️ LE POINT DE BASCULE EST 760/761 px, celui du menu (`.nav .links
           #    a:not(.adh){display:none}` sous 760 px) — pas celui de la grille des
           #    univers. C'est la hauteur de la BARRE qu'on compense, pas la mise en
           #    page du contenu : aligner ce seuil sur un autre le rendrait faux.
           # ⚠️ Aucun effet visuel au chargement : `scroll-margin` ne s'applique QU'AUX
           #    deplacements vers une ancre. La page ne bouge pas d'un pixel.
           """section[id]{scroll-margin-top:56px}
@media(max-width:760px){section[id]{scroll-margin-top:100px}}
"""
           # Le bloc des trois articles. Il ferme #situations : un filet dore le detache
           # des trois cas d'usage sans ouvrir une section (qui aurait coute 184 px de
           # respiration — la page est sous plafond, voir l'entete).
           # ⚠️ La fleche des cartes est dessinee en CSS (deux bords tournes a -45deg),
           #    comme celle de la FAQ : aucun douzieme pictogramme a maintenir, et
           #    `NB_PICTOS` reste a 11.
           """.mea{margin-top:44px;padding-top:28px;border-top:1px solid rgba(216,178,90,.24)}
.mea-t{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(25px,3.4vw,34px);font-weight:600;color:#fff;line-height:1.14}
.mea-s{color:#d7d4ea;font-size:15.5px;margin-top:10px;max-width:78ch}
.mea-g{display:grid;grid-template-columns:repeat(auto-fit,minmax(262px,1fr));gap:20px;margin-top:22px}
.mea-c{position:relative;overflow:hidden;display:flex;flex-direction:column;border:1px solid rgba(255,255,255,.07);border-radius:20px;background:linear-gradient(180deg,#1c1e46,#171935);padding:22px 20px 19px;box-shadow:0 20px 44px -30px rgba(0,0,0,.95);transition:border-color .2s,transform .2s}
.mea-c::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:var(--grad)}
.mea-c:hover{transform:translateY(-3px);border-color:rgba(248,210,116,.34)}
.mea-r{font-size:13px;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--gold);margin-bottom:8px}
.mea-h{font-family:'Cormorant Garamond',Georgia,serif;font-size:23px;font-weight:600;color:#fff;line-height:1.2}
.mea-d{color:#cfcbe4;font-size:15px;line-height:1.58;margin-top:10px}
.mea-l{margin-top:auto;padding-top:14px;display:flex;align-items:center;gap:9px;font-size:13.5px;letter-spacing:.06em;color:var(--plum2)}
.mea-l::after{content:'';width:8px;height:8px;border-right:1.6px solid var(--gold2);border-bottom:1.6px solid var(--gold2);transform:rotate(-45deg)}
"""
           # ⚠️ le bloc GARDE ses 760 px dans `.mea`, alors que la rangee d'articles
           # au-dessus fait toute la largeur (1 028 px a 1440). Mesure a l'ecran :
           # etale sur 1 028 px, la pastille flechee se retrouvait a 500 px du texte,
           # au bout d'une bande vide — le bloc perdait ce qu'il venait gagner.
           """.mea .blog-cta{margin-top:24px}
"""
           # --- « On veille les uns sur les autres » (absorbe le 16/08/2026) --------
           # Meme habillage que l'encart de la Guilde, qu'il introduit — MOINS le
           # pictogramme : les onze icones servent chacune exactement une fois, et ce
           # bloc n'a pas besoin d'une douzieme pour exister. La note en gris sous le
           # texte reprend le registre de `.cas-note` (« Les prenoms sont fictifs ») :
           # c'est le meme signal, il doit se lire pareil.
           """.veille{margin-top:34px;max-width:900px;padding:26px 30px 24px;border:1px solid rgba(248,210,116,.24);border-radius:22px;background:linear-gradient(135deg,rgba(216,178,90,.10),rgba(238,128,98,.08) 60%,rgba(147,116,226,.10));box-shadow:0 24px 56px -40px rgba(0,0,0,.95)}
.veille .u-num{display:block;margin-bottom:8px}
.veille-claim{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(19px,2.4vw,24px);line-height:1.32}
.veille-p{color:#d7d4ea;font-size:15.5px;margin-top:13px}
.veille-note{color:var(--muted);font-size:14px;line-height:1.6;margin-top:13px}
"""
           # --- « J'ai besoin d'aide » (16/08/2026) ---------------------------------
           # Meme habillage que l'encart de la Guilde et que « On veille les uns sur les
           # autres » : ces trois blocs disent la meme chose sous trois angles (le
           # groupe, le pacte, l'appel), ils doivent se lire comme une famille.
           # ⚠️ Le marqueur des trois lignes est un NUMERO dessine en CSS
           # (`counter-reset` sur la liste, `content:counter(aide)` dans le ::before),
           # pas un pictogramme et surtout pas un emoji : la page de reference met un
           # emoji sur cette section, la charte du site l'interdit. Aucun quinzieme
           # trace a maintenir, et `NB_PICTOS` ne bouge pas.
           # ⚠️ C'ETAIT UN POINT D'INTERROGATION (`content:'?'`) jusqu'au 16/08/2026,
           # quand les lignes etaient quatre situations a cocher. Elles sont devenues
           # les TROIS questions du parcours reel : le numero est ce qui rend le
           # « 3 questions, c'est tout » annonce juste au-dessus verifiable a l'oeil.
           # Le badge lui-meme (20x20, coins a 7px, filet dore) n'a pas bouge.
           """.aide{display:flex;gap:18px;align-items:flex-start;margin-top:34px;max-width:900px;padding:28px 30px 26px;border:1px solid rgba(248,210,116,.26);border-radius:22px;background:linear-gradient(135deg,rgba(216,178,90,.12),rgba(238,128,98,.09) 58%,rgba(147,116,226,.10));box-shadow:0 24px 56px -40px rgba(0,0,0,.95)}
.aide .ic-w{flex:0 0 auto;line-height:0;margin-top:4px}
.aide .ic{width:26px;height:26px}
.aide .u-num{display:block;margin-bottom:8px}
.aide-claim{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;color:var(--gold2);font-size:clamp(19px,2.4vw,24px);line-height:1.32}
.aide-p{color:#d7d4ea;font-size:15.5px;margin-top:13px}
.aide-l{list-style:none;margin-top:15px;display:grid;gap:9px;counter-reset:aide}
.aide-l li{position:relative;padding-left:29px;color:#d7d4ea;font-size:15.5px;line-height:1.6;counter-increment:aide}
.aide-l li::before{content:counter(aide);position:absolute;left:0;top:2px;width:20px;height:20px;border-radius:7px;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600;line-height:1;color:var(--gold2);border:1px solid rgba(248,210,116,.34);background:rgba(216,178,90,.14)}
.aide-l li b{color:#fff;font-weight:500}
"""
           # --- le formulaire de demande d'acces (rapatrie le 16/08/2026) -----------
           # Il est DANS le panneau `.acces`, donc il herite du bouton chaud (`.acces
           # .btn`). Rien ne descend sous 14 px (plancher du site : 13). Les champs sont
           # a 16 px : sous 16 px, Safari sur iPhone ZOOME a la mise au point et le
           # visiteur se retrouve avec une page decalee — un formulaire qu'on remplit au
           # telephone ne peut pas se permettre ca.
           """.dmd{margin-top:30px;border:1px solid rgba(255,255,255,.10);border-radius:22px;background:linear-gradient(180deg,rgba(11,12,30,.55),rgba(11,12,30,.28));padding:28px 26px 26px}
.dmd-t{font-family:'Cormorant Garamond',Georgia,serif;font-size:27px;font-weight:600;color:#fff;line-height:1.18}
.dmd-s{color:var(--muted);font-size:15px;max-width:62ch;margin-top:6px}
.dmd-grid{display:grid;grid-template-columns:minmax(0,1fr)}
@media(min-width:601px){.dmd-grid{grid-template-columns:repeat(2,minmax(0,1fr));column-gap:18px}}
.f{margin-top:18px;min-width:0}
.dmd fieldset{border:0;padding:0}
.f label,.dmd legend{display:block;font-size:14px;letter-spacing:.05em;text-transform:uppercase;color:var(--gold2);font-weight:500;margin-bottom:7px;padding:0}
.f .opt{text-transform:none;letter-spacing:0;color:var(--muted);font-weight:400}
.dmd input[type="text"],.dmd input[type="email"],.dmd input[type="tel"],.dmd textarea{display:block;width:100%;font-family:inherit;font-size:16px;line-height:1.5;color:var(--ink);background:rgba(9,10,26,.62);border:1px solid rgba(255,255,255,.16);border-radius:13px;padding:12px 14px;min-height:48px}
.dmd textarea{min-height:98px;resize:vertical}
.dmd input:hover,.dmd textarea:hover{border-color:rgba(248,210,116,.4)}
.dmd input[aria-invalid="true"]{border-color:var(--coral)}
.f-err{display:block;color:var(--coral);font-size:14.5px;line-height:1.5}
.f-err:not(:empty){margin-top:8px}
.dmd-kind{display:flex;gap:11px;flex-wrap:wrap}
.dmd-kind label{display:inline-flex;align-items:center;gap:10px;margin:0;min-height:44px;padding:9px 19px;border:1px solid rgba(248,210,116,.3);border-radius:999px;background:linear-gradient(180deg,rgba(255,255,255,.055),rgba(255,255,255,.02));font-size:15.5px;font-weight:400;letter-spacing:0;text-transform:none;color:var(--ink);cursor:pointer}
.dmd-kind input{width:17px;height:17px;margin:0;accent-color:var(--gold)}
"""
           # la phrase d'exemple de « Les deux » — 14 px, au-dessus du plancher de 13
           """.dmd-kind-h{margin:11px 0 0;font-size:14px;line-height:1.6;color:var(--muted);max-width:60ch}
.dmd-kind label:has(input:checked){border-color:var(--gold2);background:linear-gradient(90deg,rgba(216,178,90,.16),rgba(238,128,98,.12))}
"""
           # --- LES CHAMPS DE STRUCTURE (17/08/2026) -------------------------------
           # `[hidden]` est ecrit EXPLICITEMENT : la feuille de la page pose des
           # `display:` sur beaucoup de conteneurs, et une seule regle plus specifique
           # que le style par defaut du navigateur suffirait a faire reapparaitre un
           # bloc « cache ». Un formulaire dont les champs conditionnels se voient
           # quand meme demanderait des informations sans raison — et, pire, en
           # rendrait certaines obligatoires sans que rien ne le dise.
           # ⚠️ Le fond du panneau est PLUS SOMBRE que celui du formulaire
           # (`rgba(9,10,26,.3)`), pas plus clair : le texte de la page est clair, et
           # eclaircir le fond sous un message d'erreur corail est exactement ce qui a
           # fait tomber les boutons d'agenda de `/le-nid` sous 4,5:1 le 16/08/2026.
           # ⚠️ La legende d'un groupe fautif passe en corail : la couleur ne porte
           # JAMAIS seule l'information — le message ecrit est en dessous, et
           # `aria-invalid` le dit aux technologies d'assistance.
           """.dmd [hidden]{display:none}
.dmd-avis:not(:empty){display:block;margin:12px 0 0;font-size:14px;line-height:1.6;color:var(--gold2);max-width:60ch}
.dmd-struct{margin-top:20px;padding:20px 20px 18px;border:1px solid rgba(248,210,116,.24);border-radius:18px;background:rgba(9,10,26,.3)}
.dmd-struct-t{font-size:14px;letter-spacing:.05em;text-transform:uppercase;color:var(--gold2);font-weight:500}
.dmd-struct>.f:first-of-type{margin-top:14px}
.dmd fieldset[aria-invalid="true"] legend{color:var(--coral)}
.dmd-go{margin-top:26px}
.dmd button.btn{border:0;font-family:inherit;cursor:pointer}
.dmd button.btn[disabled]{opacity:.62;cursor:default;transform:none;box-shadow:none}
.dmd-etat{font-size:15.5px;line-height:1.65;max-width:62ch}
.dmd-etat:not(:empty){margin-top:18px;padding:14px 16px;border-radius:14px;border:1px solid rgba(248,210,116,.28);background:rgba(216,178,90,.08);color:#d7d4ea}
.dmd-etat.ko:not(:empty){border-color:rgba(238,128,98,.45);background:rgba(238,128,98,.09)}
@media(max-width:760px){
  section{padding:62px 0}
  .gf-top{padding:110px 0 60px}
  .u-card{padding:26px 22px 22px}
  .cas article{padding:26px 22px 22px}
  .etat{padding:28px 24px}
  .acces{padding:32px 24px 28px}
  .aussi{padding:22px 20px;gap:14px}
  .guilde{padding:22px 20px 20px;gap:14px}
  .veille{padding:22px 20px 20px}
  .aide{padding:22px 20px 20px;gap:14px}
  .mea{margin-top:42px;padding-top:28px}
  .mea-c{padding:20px 18px 17px}
  .dmd{padding:22px 18px 20px}
  .dmd-struct{padding:18px 16px 16px}
  .etape{padding:20px 18px 18px}
  .faq-q summary{padding:14px 17px;gap:13px}
  .faq-q .faq-r{padding:14px 17px 16px}
}
@media print{.totop{display:none}.kick,.grad-t{-webkit-text-fill-color:var(--gold);color:var(--gold)}}
""")

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
CSS_MAQUETTES = (# ===== maquettes d'interface (illustrations, pas d'interface reelle) =====
                """.gf-block{margin:34px 0 0;max-width:820px}
"""
                # ⚠️ 16/08/2026 — `.univers` a laisse la place a `.duo` / `.apercus` (la double
                # vue artistes | structures). Les apercus qui vivent DANS une colonne ou dans
                # la rangee des deux aperçus artistes n'ont ni marge haute ni largeur maximale
                # propre : c'est la grille qui les cadre. L'ancienne regle `.univers .gf-wide
                # {grid-column:1/-1}` a disparu avec la grille — une colonne de flex n'a pas
                # de piste a enjamber.
                """.gf-topgrid .gf-block,.duo-col .gf-block,.apercus .gf-block{margin:0;max-width:none}
.gf-shot{position:relative;background:linear-gradient(180deg,#1d1f47,#171935);border:1px solid rgba(255,255,255,.08);border-radius:18px;padding:22px 18px 18px;margin:0 0 11px;color:var(--ink);font-size:15px;line-height:1.5;max-width:100%;overflow:hidden;box-shadow:0 24px 50px -34px rgba(0,0,0,.95)}
.gf-shot::before{content:'';position:absolute;inset:0 0 auto 0;height:2px;background:var(--grad);opacity:.85}
"""
                # la jauge du hero est l'image signature de la page : elle porte un halo
                """.gf-topgrid .gf-shot{box-shadow:0 30px 64px -34px rgba(0,0,0,.95),0 0 70px -26px rgba(238,128,98,.45)}
.gf-shot *{box-sizing:border-box}
.gf-cap{display:block;font-size:13px;line-height:1.4;color:var(--muted);letter-spacing:.02em;margin:0 0 0 4px}
.gf-cap::before{content:'';display:inline-block;width:6px;height:6px;border-radius:2px;background:var(--grad-warm);transform:rotate(45deg);margin-right:9px;vertical-align:1px}
"""
                # la note « (a venir) » d'une maquette qui illustre un ecran encore en
                # construction (16/08/2026, une seule aujourd'hui : « Mes artistes »). La
                # pastille reprend a l'identique celle des puces `.u-card li i` : c'est le
                # meme signal, il doit se lire pareil.
                """.gf-soon-note{margin:9px 0 0 4px;max-width:66ch;color:var(--muted);font-size:14px;line-height:1.6}
.gf-soon-note i{font-style:normal;display:inline-block;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--plum2);border:1px solid rgba(179,143,245,.4);background:rgba(147,116,226,.12);border-radius:999px;padding:1px 9px;line-height:1.5;margin-right:7px}
.gf-bar{display:flex;align-items:baseline;justify-content:space-between;gap:10px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:10px;margin-bottom:16px}
.gf-bar-t{font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-weight:600;color:var(--ink)}
.gf-bar-s{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
.gf-hint{font-size:13px;color:var(--muted);margin:0 0 14px}
"""
                # 1 — jauge des 507 h : anneau en conic-gradient, aucune image
                """.gf-hero{display:flex;gap:20px;align-items:center;flex-wrap:wrap}
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
"""
                # 2 — « A faire maintenant » : pastilles urgent / en retard / a venir
                """.gf-tn-head{display:flex;align-items:baseline;gap:9px;margin-bottom:12px}
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
"""
                # 3 — fiche d'une date et ses cinq etapes administratives
                """.gf-kv{display:grid;grid-template-columns:auto minmax(0,1fr);gap:7px 14px;margin:0 0 16px;font-size:15px}
.gf-kv .gf-k{color:var(--muted);font-size:13px;letter-spacing:.04em}
.gf-kv .gf-v{color:var(--ink);font-weight:500;min-width:0;overflow-wrap:anywhere}
.gf-mini{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);margin:0 0 9px}
.gf-steps{display:flex;flex-wrap:wrap;gap:8px}
.gf-step{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--line);border-radius:999px;background:var(--night2);padding:6px 12px;font-size:13px;color:var(--muted)}
.gf-step .gf-box{width:16px;height:16px;border-radius:5px;border:1px solid var(--line);display:inline-flex;align-items:center;justify-content:center;font-size:13px;line-height:1;color:var(--night);flex:0 0 auto}
.gf-step.gf-done{color:var(--ink);border-color:var(--gold)}
.gf-step.gf-done .gf-box{background:var(--gold);border-color:var(--gold)}
"""
                # 4 — recap mensuel France Travail, en cartes groupees par mois
                """.gf-recmonth{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin:0 0 10px}
.gf-reccard{border:1px solid rgba(255,255,255,.07);border-radius:13px;background:linear-gradient(180deg,#1b1d42,#15172f);padding:11px 13px;margin-bottom:9px}
.gf-recwhen{font-size:13px;color:var(--muted)}
.gf-recnums{font-size:15px;font-weight:600;color:var(--ink);font-variant-numeric:tabular-nums}
.gf-recnums em{font-style:normal;color:var(--gold2)}
.gf-recmeta{font-size:13px;color:var(--muted);overflow-wrap:anywhere}
.gf-rectot{display:flex;gap:8px 14px;align-items:baseline;flex-wrap:wrap;justify-content:space-between;border-top:1px solid rgba(216,178,90,.55);margin-top:13px;padding-top:12px}
.gf-rl{font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.gf-rv{font-size:15px;font-weight:600;color:var(--gold2);font-variant-numeric:tabular-nums}
"""
                # 5 — ma tournee : enchainement chronologique, filet + pastilles, zero image
                """.gf-route{position:relative;margin:0;padding:0 0 0 24px;list-style:none}
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
"""
                # 6 — tableau de bord d'une structure. La vigilance se lit a la FORME de la
                # pastille et a son libelle, pas seulement a la couleur (la charte n'a ni
                # vert ni rouge, et un daltonien doit pouvoir la lire).
                """.gf-art{display:flex;flex-direction:column;gap:9px}
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
""")


# --- CSS des 4 maquettes du LOT 2 (nuit du 16/08/2026) --------------------
# Repris de `GUSO-FACILE-BACKUPS/maquettes-lot2-pour-resonances.html` (LECTURE
# SEULE). Memes regles que le lot 1 :
#   - AUCUNE couleur litterale : les `var(--…)` de la charte, pour qu'une
#     retouche du theme entraine les maquettes avec elle. Le fichier source
#     porte ses propres valeurs de repli (`--panel2,#0f1319`, `--accent,#4ecdc4`,
#     un rose `#ff6b9d`) : elles sont REMPLACEES, pas adaptees — ce sont les
#     couleurs de la page Vercel, pas celles du site ;
#   - rien sous 13 px (plancher du site, verifie par `_controles`) ;
#   - toutes les rangees en `flex-wrap:wrap` avec un `flex-basis` modeste,
#     c'est ce qui les fait tenir dans 306 px de large a 390 px d'ecran ;
#   - la carte a sa propre feuille (`CSS_CARTE`), pour la raison ecrite au-
#     dessus d'elle.
CSS_LOT2 = (# ===== maquettes d'interface, lot 2 =====
            # 7 — le selecteur « Je regarde » : la preuve de la double vue.
            # La pastille de couleur double le libelle, elle ne le remplace pas
            # (or = l'artiste, prune = la structure) : un daltonien lit le texte.
            """.gf-ctx{border:1px solid rgba(255,255,255,.09);border-radius:14px;background:linear-gradient(180deg,#1b1d42,#15172f);overflow:hidden;max-width:440px}
.gf-ctx-cur{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;padding:12px 14px;border-bottom:1px solid var(--line);font-size:15px;font-weight:600;color:var(--ink)}
.gf-ctx-cur em{font-style:normal;margin-left:auto;color:var(--muted);font-weight:400;font-size:13px}
.gf-ctx-hint{padding:10px 14px;font-size:13px;line-height:1.5;color:var(--muted);border-bottom:1px solid rgba(255,255,255,.06)}
.gf-ctx-i{display:flex;align-items:flex-start;gap:11px;padding:12px 14px;border-bottom:1px solid rgba(255,255,255,.05)}
.gf-ctx-i:last-child{border-bottom:0}
.gf-ctx-i.gf-on{background:rgba(216,178,90,.08)}
.gf-ctx-d{flex:0 0 auto;width:10px;height:10px;border-radius:50%;margin-top:7px}
.gf-ctx-d.gf-art{background:var(--gold)}
.gf-ctx-d.gf-str{background:var(--plum)}
.gf-ctx-t{flex:1 1 140px;min-width:0;font-size:15px;color:var(--ink)}
.gf-ctx-t em{font-style:normal;display:block;color:var(--muted);font-size:13px}
.gf-ctx-chk{flex:0 0 auto;font-size:15px;font-weight:600;color:var(--gold2)}
"""
            # 9 — « J'ai besoin d'aide », question 1 sur 3. La barre de progression
            # est faite de trois segments egaux : c'est elle qui rend le « sur 3 »
            # verifiable a l'oeil, comme les numeros du bloc `.aide` juste au-dessus.
            """.gf-help{max-width:440px}
.gf-prog{display:flex;gap:6px;margin-bottom:15px}
.gf-prog i{flex:1 1 0;height:4px;border-radius:2px;background:rgba(255,255,255,.1)}
.gf-prog i.gf-cur{background:var(--grad-warm)}
.gf-help-q{font-family:'Jost',sans-serif;font-size:17px;font-weight:700;letter-spacing:-.01em;line-height:1.25;color:var(--ink);margin-bottom:13px}
.gf-opt{display:flex;align-items:flex-start;gap:11px;border:1px solid rgba(255,255,255,.08);border-radius:12px;background:linear-gradient(180deg,#1b1d42,#15172f);padding:11px 13px;margin-bottom:9px;font-size:15px;line-height:1.45;color:var(--ink)}
.gf-opt-n{flex:0 0 auto;width:22px;height:22px;border-radius:7px;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600;line-height:1;color:var(--gold2);border:1px solid rgba(248,210,116,.34);background:rgba(216,178,90,.14)}
.gf-help-f{font-size:13px;line-height:1.6;color:var(--muted);margin-top:14px}
"""
            # 10 — le journal des nouveautes. La version « majeure » se distingue par
            # son filet degrade en tete ET par sa bordure doree : deux signaux, jamais
            # la seule couleur.
            """.gf-cl{max-width:480px}
.gf-cl-card{position:relative;overflow:hidden;border:1px solid rgba(255,255,255,.08);border-radius:13px;background:linear-gradient(180deg,#1b1d42,#15172f);padding:13px 15px;margin-bottom:10px}
.gf-cl-card:last-child{margin-bottom:0}
.gf-cl-card.gf-major{border-color:rgba(248,210,116,.42)}
.gf-cl-card.gf-major::before{content:'';position:absolute;inset:0 0 auto 0;height:2px;background:var(--grad)}
.gf-cl-h{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;margin-bottom:6px}
.gf-cl-n{font-size:15px;font-weight:600;color:var(--ink)}
.gf-cl-d{margin-left:auto;font-size:13px;color:var(--muted)}
.gf-cl-s{font-size:13px;line-height:1.55;color:var(--muted);margin-bottom:9px}
.gf-cl-l{list-style:none;margin:0 0 10px}
.gf-cl-l li{position:relative;padding-left:16px;font-size:13px;line-height:1.55;color:#cfcbe4;margin-bottom:4px}
.gf-cl-l li::before{content:'';position:absolute;left:0;top:8px;width:6px;height:6px;border-radius:2px;background:var(--grad-warm);transform:rotate(45deg)}
.gf-cl-tag{display:inline-block;font-size:13px;letter-spacing:.06em;padding:1px 9px;border-radius:999px;border:1px solid var(--line);color:var(--muted)}
""")


# =========================================================================
# LA CARTE DE TOURNEE — POURQUOI ELLE EST EN SVG, ET POURQUOI SA POLICE A
# TROIS PALIERS
# =========================================================================
# ⚠️⚠️ 1. NE PAS REVENIR AUX <div> PIVOTES DU FICHIER SOURCE.
# La carte de `maquettes-lot2-pour-resonances.html` trace ses segments avec des
# `<div class="gf-leg" style="left:18%;top:74%;width:19%;transform:rotate(-38deg)">`.
# La LARGEUR d'un element pivote reste relative a la LARGEUR du conteneur,
# alors que la longueur apparente du segment entre deux points depend du
# RAPPORT largeur/hauteur — et ce rapport change a chaque largeur d'ecran,
# puisque le conteneur du fichier source a une hauteur FIXE de 250 px. Les
# traits se desolidarisent donc des points des qu'on n'est plus a la largeur ou
# l'auteur a regle ses angles. Constate a l'ecran. Aucun reglage ne rattrape
# ca : c'est le modele qui est faux, pas les valeurs.
# LE SVG met points ET trace dans LE MEME systeme de coordonnees
# (`viewBox="0 0 100 52"`). Le lien est alors une propriete de la figure, plus
# un reglage a maintenir.
#
# ⚠️⚠️ 2. LA TAILLE DES LIBELLES EST UNE MESURE. Dans un `viewBox`, une taille
# de police est une UNITE UTILISATEUR : a l'ecran elle vaut
# `unites x largeur_rendue / 100`. Une valeur unique donnerait donc 24 px sur
# un grand ecran et 10 px sur un telephone — sous le plancher de 13 px du site.
# Trois paliers, cales sur la largeur REELLE du conteneur (figure plafonnee a
# 556 px, moins le rembourrage de `.gf-shot` : 18 px de chaque cote au-dessus
# de 760 px d'ecran, 13 px en dessous) :
#
#   ecran      largeur rendue   unites   taille reelle
#   > 608 px      520-530 px      3.2      16,6-17,0 px
#   453-558 px    375-480 px      3.6      13,5-17,3 px
#   375-452 px    297-374 px      4.4      13,1-16,5 px
#
# `_controle_carte()` REFAIT ce calcul avant chaque ecriture et refuse la page
# si un palier descend sous 13 px.
# ⚠️ NE PAS MONTER AU-DELA DE ~4,4 UNITES : mesure a l'ecran, au-dela
#    « Festival du Causse » (centre en x=52) et « Theatre Rivage » (x=88) se
#    chevauchent. C'est la contrainte qui fixe le plus petit ecran servi : en
#    dessous de ~375 px de large, les libelles passeraient sous 13 px. Assume.
# ⚠️ `overflow:visible` sur le `<svg>` : « Theatre Rivage » deborde d'environ
#    2,5 unites a droite du cadre au dernier palier. Ce debordement tombe dans
#    le REMBOURRAGE de `.gf-shot` (13 px), pas hors de lui — `overflow:hidden`
#    rogne a la boite de rembourrage, pas a la boite de contenu. Verifie a
#    l'ecran : aucun debordement horizontal de la page.
# ⚠️ LES COORDONNEES NE BOUGENT PAS. Elles ont ete verifiees a l'ecran telles
#    quelles ; seuls les noms de classe ont ete prefixes `gf-` pour la page.
CSS_CARTE = ("""/* carte de tournee */
.gf-carte{position:relative;margin:2px 0 13px}
.gf-map{display:block;width:100%;height:auto;overflow:visible}
.gf-map .gf-halo{fill:none;stroke:var(--gold);stroke-width:3.4;opacity:.12;stroke-linecap:round;stroke-linejoin:round}
.gf-map .gf-voie{fill:none;stroke:var(--gold);stroke-width:.9;opacity:.8;stroke-linecap:round;stroke-linejoin:round}
.gf-map .gf-pt{fill:var(--gold2);stroke:var(--night);stroke-width:.8}
.gf-map .gf-pt-dom{fill:var(--plum2)}
.gf-map .gf-pt-sup{fill:var(--night);stroke:var(--coral);stroke-width:1.1}
"""
             # ⚠️ LE LISERE SOUS LES LIBELLES N'EST PAS UN EFFET. Vu a l'ecran : le
             # segment « Le Grand Pré » -> « Théâtre Rivage » passe DERRIERE le mot
             # « à confirmer », et le trait dore coupait les lettres. `paint-order`
             # fait dessiner le contour AVANT le remplissage : le mot se detache du
             # trace sans qu'on ait a deplacer quoi que ce soit — et les coordonnees
             # ne bougent pas, ce qui est la regle sur cette figure.
             """.gf-map text{paint-order:stroke;stroke:var(--card);stroke-width:.8;stroke-linejoin:round;stroke-linecap:round}
.gf-map .gf-lab{font-family:'Jost',sans-serif;font-weight:600;font-size:3.2px;fill:var(--ink)}
.gf-map .gf-lab-s{font-family:'Jost',sans-serif;font-weight:500;font-size:3.2px;fill:var(--muted)}
@media(max-width:558px){.gf-map .gf-lab,.gf-map .gf-lab-s{font-size:3.6px}}
@media(max-width:452px){.gf-map .gf-lab,.gf-map .gf-lab-s{font-size:4.4px}}
.gf-carte-km{font-size:15px;line-height:1.5;color:#d7d4ea}
.gf-carte-km b{color:var(--gold2);font-weight:600}
.gf-carte-leg{display:flex;gap:8px 18px;flex-wrap:wrap;margin-top:10px;font-size:13px;color:var(--muted)}
.gf-carte-leg span{display:inline-flex;align-items:center;gap:7px}
.gf-carte-leg i{flex:0 0 auto;width:10px;height:10px;border-radius:50%}
.gf-lg-dom{background:var(--plum2)}
.gf-lg-ok{background:var(--gold2)}
.gf-lg-sup{background:var(--night);box-shadow:inset 0 0 0 1.6px var(--coral)}
"""
             # la carte est le seul apercu qui vive DANS la rangee `.apercus` en
             # enjambant ses deux colonnes : elle illustre l'univers 2 « Ta tournee,
             # organisee », dont « Ma tournee » est le voisin immediat. Le plafond de
             # 556 px n'est pas cosmetique — c'est lui qui rend la largeur rendue
             # PREVISIBLE, donc les trois paliers de police ci-dessus calculables.
             """.apercus .gf-carte-b{grid-column:1/-1;width:100%;max-width:556px;margin:0 auto}
""")


# --- L'EXCEPTION TYPOGRAPHIQUE (16/08/2026) -------------------------------
# ⚠️⚠️ LIRE AVANT DE « RETABLIR LA COHERENCE » : CETTE PAGE N'EST PAS EN
#      CORMORANT GARAMOND, ET C'EST VOULU. LES 29 AUTRES LE RESTENT.
#
# LE CONSTAT DE DAVID, verbatim : « cette page etait presque parfaite. Je ne
# sais pas si c'est une histoire de police d'ecriture ou de couleur, mais la
# version actuelle n'a pas le meme impact psychologique. C'est flagrant. »
# Sa reference : `~/CLAUDE/GUSO FACILE/presentation.html` (LECTURE SEULE).
#
# LA COULEUR N'ETAIT PAS LE PROBLEME. Le 16/08 au matin, les surfaces avaient
# deja ete etagees et les accents satures (voir `theme_chaleur.py`) : ca n'a pas
# suffi. LE DIAGNOSTIC, MESURE SUR LES DEUX PAGES :
#
#     |                    | leur page          | la notre (avant)   |
#     |--------------------|--------------------|--------------------|
#     | police des titres  | sans-serif systeme | Cormorant Garamond |
#     | graisse            | 800                | 600                |
#     | h1 a 1440          | 58 px              | 74 px              |
#     | h2 a 1440          | 38 px              | 50 px              |
#     | interlettrage      | -1 px / -0,5 px    | normal (positif !) |
#     | interligne du h1   | 1,0                | 1,02 mais aere     |
#
# LEUR TITRE EST PLUS PETIT ET IL FRAPPE PLUS FORT, parce qu'il est LOURD,
# SERRE ET DENSE. Le notre etait grand, fin et aere : elegant, litteraire,
# institutionnel — le registre d'une association culturelle. Le leur est
# compact, assure, PRODUIT — le registre d'un logiciel dans lequel on a envie
# d'avoir confiance.
#
# POURQUOI L'EXCEPTION EST LEGITIME, ET POURQUOI ELLE DOIT LE RESTER
#   Un spectacle et un logiciel ne se vendent pas avec la meme typographie. Le
#   serif dit le patrimoine, la duree, la scene ; le sans-serif lourd dit
#   l'outil, la fiabilite, le present. `/guso-facile` est LA SEULE PAGE PRODUIT
#   du site : elle a le droit d'avoir sa voix propre A L'INTERIEUR de la charte
#   — meme palette, meme degrade signature, memes pictogrammes, meme menu, meme
#   pied de page. SEULE LA POLICE DES TITRES CHANGE.
#   ⚠️ NE PAS PROPAGER `Jost` AUX 29 AUTRES PAGES : elles presentent des
#      concerts-rituels, un lieu, une association. Les passer en sans-serif
#      lourd leur ferait perdre exactement ce que cette page-ci cherche a
#      perdre. L'exception se justifie parce qu'elle est UNE exception.
#   ⚠️ NE PAS NON PLUS « RENDRE SA COHERENCE » A CETTE PAGE EN LA REMETTANT EN
#      CORMORANT : ce serait revenir precisement a ce que David a signale.
#
# CE QUI RESTE EN CORMORANT SUR CETTE PAGE, ET POURQUOI
#   Le contraste serif/sans donne le rythme, il ne l'enleve pas. Restent donc en
#   serif italique TOUTES LES PHRASES QUI SE DISENT plutot qu'elles n'annoncent :
#   l'accroche du hero (`.gf-claim`), les sous-titres d'univers (`.u-sub`), la
#   premiere et la derniere phrase de « Jouons cartes sur table » (`.etat .first`
#   et `.etat-fin`), les accroches de la Guilde, de la veille et de « J'ai besoin
#   d'aide ». Plus le mobilier du site, partage avec les 29 autres pages : le nom
#   de l'association dans la barre, les titres du pied de page, `.fbrand`.
#   Les TITRES annoncent — ils sont en Jost. Les CITATIONS se disent — elles
#   restent en Cormorant.
#
# LES VALEURS, ET POURQUOI ELLES SONT EN `em` ET PAS EN `px`
#   L'interlettrage negatif est demande « -0,5 a -1 px selon la taille ». Ecrit
#   en px il serait FIXE : -1 px sur un h1 de 60 px vaut -1,7 %, mais -1 px sur
#   le meme h1 replie a 32 px sur telephone vaut -3,1 % — a ce niveau les
#   lettres se touchent et un titre long casse. En `em` le reglage suit la
#   taille tout seul : -0,018 em rend -1,08 px a 60 px et -0,58 px a 32 px.
#   C'est exactement la fourchette demandee, obtenue sans regler deux fois.
#
# ⚠️ AUCUNE POLICE SUPPLEMENTAIRE : `Jost` est la SECONDE police du site, deja
#    chargee sur les 30 pages (c'est la police du CORPS de texte). Seule la
#    graisse 700 a ete ajoutee a l'URL, sans un octet de police en plus — voir
#    la note detaillee au-dessus de `HEAD`.
CSS_TYPO = (# ===== l'exception typographique de la page produit (16/08/2026) =====
           # Les titres passent de Cormorant Garamond a Jost lourd et serre. Les 29
           # autres pages du site gardent le serif : le raisonnement complet est dans
           # sources/generate_guso.py, juste au-dessus de cette feuille.
           """h1,h2,h3,h4{font-family:'Jost',-apple-system,Segoe UI,Roboto,sans-serif}
"""
           # le mobilier partage avec les 29 autres pages ne bouge pas
           """footer h4{font-family:'Cormorant Garamond',Georgia,serif}
"""
           # le titre principal : plus PETIT qu'avant (74 -> 60 px), et bien plus lourd
           """.gf-top h1{font-size:clamp(34px,4.4vw,60px);font-weight:700;line-height:1.05;letter-spacing:-.018em}
.gf-top h1 .h1-sous{font-size:clamp(17px,2.05vw,23px);font-weight:600;line-height:1.22;letter-spacing:-.006em}
"""
           # les titres de section : 50 -> 40 px, graisse 700, interlettrage negatif
           """.sec-title{font-size:clamp(27px,4vw,40px);font-weight:700;line-height:1.06;letter-spacing:-.014em}
"""
           # les titres de cartes, de blocs et d'accordeons suivent la meme regle
           """.u-card h3{font-size:23px;font-weight:700;letter-spacing:-.012em;line-height:1.18}
.cas h3{font-size:22px;font-weight:700;letter-spacing:-.012em;line-height:1.2}
.mea-t{font-family:'Jost',sans-serif;font-size:clamp(24px,3vw,32px);font-weight:700;letter-spacing:-.014em;line-height:1.1}
.mea-h{font-family:'Jost',sans-serif;font-size:20px;font-weight:700;letter-spacing:-.01em;line-height:1.24}
.dmd-t{font-family:'Jost',sans-serif;font-size:24px;font-weight:700;letter-spacing:-.012em}
.etape h3{font-size:19px;font-weight:700;letter-spacing:-.01em}
.faq-q summary h3{font-size:19px;font-weight:600;letter-spacing:-.008em}
"""
           # les maquettes reproduisent une interface : elle est en sans-serif, comme
           # l'application. Un titre d'ecran en serif trahissait la reproduction.
           """.gf-bar-t{font-family:'Jost',sans-serif;font-size:19px;font-weight:600;letter-spacing:-.01em}
.gf-ring-n{font-family:'Jost',sans-serif;font-size:36px;font-weight:700;letter-spacing:-.02em}
.gf-route-tot-v{font-family:'Jost',sans-serif;font-size:24px;font-weight:700;letter-spacing:-.015em}
""")


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
# ⚠️⚠️ 17/08/2026 — LA VUE EST DEPLOYEE, LA NOTE « (a venir) » EST RETIREE.
#    HISTOIRE, parce qu'elle explique pourquoi cette maquette a un traitement a
#    part. Le 16/08/2026 elle etait LA SEULE de la page a porter un « (a venir) » :
#    la vue « Mes artistes » (chaque artiste, ses heures, son niveau de
#    vigilance) n'existait pas telle quelle, seule une to-do TRANSVERSALE
#    (DPAE / GUSO / factures) existait cote structure — l'image promettait donc
#    plus que l'application. David avait demande que la vue soit CONSTRUITE POUR
#    DE BON A PARTIR DE CETTE MAQUETTE : c'est fait.
#    VERIFIE EN PRODUCTION LE 17/08/2026, dans le bundle servi par
#    `https://guso-facile.vercel.app/index.html` : `sdCardHtml` (les cartes
#    d'artistes et leurs points de vigilance) y est present. La maquette et son
#    texte sont donc inchanges, mais l'argument `note=` a disparu.
#    ➜ LES TROIS GESTES ONT ETE FAITS CE JOUR-LA, dans cet ordre :
#         1. l'argument `note=` de cet appel a `_figure()` retire (et lui seul) ;
#         2. `NB_A_VENIR` passe a 0 (et non a 2 comme prevu ici : les deux puces
#            de l'univers 4 sont deployees le meme jour) ;
#         3. l'ancre `class="gf-soon-note"` retiree de `ANCRES`.
#       Le CSS `.gf-soon-note` RESTE en place : `_figure()` ne l'emet que si une
#       maquette demande une note, et la prochaine maquette d'un ecran non livre
#       en aura besoin. C'est le mecanisme, pas un residu.
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
  """)


# =========================================================================
# LES 4 MAQUETTES DU LOT 2 (nuit du 16/08/2026)
# =========================================================================
# Matiere : `GUSO-FACILE-BACKUPS/maquettes-lot2-pour-resonances.html` (LECTURE
# SEULE, jamais editee). Memes trois exigences que le lot 1, sans exception :
# mention visible « donnees fictives », `role="img"` + `aria-label`, ZERO
# element focusable. Elles passent toutes par `_figure()`, donc par les memes
# garde-fous.
#
# ⚠️ CE QUI A ETE CORRIGE / ADAPTE DANS LA MATIERE FOURNIE :
#   - la CARTE a ete entierement redessinee (voir `CSS_CARTE`) : son trace en
#     `<div>` pivotes se desolidarisait des points a chaque changement de
#     largeur ;
#   - les couleurs de repli du fichier source (cyan `#4ecdc4`, rose `#ff6b9d`,
#     fond `#0f1319`) sont celles de la page Vercel : elles sont REMPLACEES par
#     les `var(--…)` de la charte, jamais adaptees ;
#   - l'apostrophe droite passe en apostrophe typographique, comme partout
#     ailleurs sur cette page. C'est la SEULE retouche faite aux libelles.
#
# ⚠️⚠️ CE QUI N'A PAS ETE TOUCHE, ET NE DOIT PAS L'ETRE : les libelles repris du
#    CODE DE L'APPLICATION. « Filtre d'affichage — ca ne change aucun droit, ni
#    pour toi ni pour les autres » et les QUATRE reponses de « J'ai besoin
#    d'aide » sont les chaines de l'app, au mot pres. C'est ce qui garantit
#    qu'un beta-testeur retrouvera ces phrases a l'ecran ; une reformulation,
#    meme meilleure, casserait la correspondance.


# --- 7. LE SELECTEUR « JE REGARDE » (sous le vis-a-vis) -------------------
# Ecran reproduit : le selecteur de vue. C'est LE SEUL ecran qui PROUVE la
# double vue — les deux colonnes la racontent, celui-ci la montre : un compte,
# deux casquettes, aucune deconnexion.
# ⚠️ L'entree « Vision d'ensemble — super-admin » du vrai selecteur n'est PAS
#    reproduite : elle n'est visible que par l'administrateur, la montrer
#    laisserait croire a un troisieme mode ouvert a tous.
# ⚠️ La phrase d'avertissement est celle de l'app, MOT POUR MOT. Elle dit ce que
#    le selecteur n'est PAS (un reglage de droits), et c'est precisement ce
#    qu'un lecteur pourrait croire en voyant deux casquettes.
MAQ_SELECTEUR = _figure(
    'Sélecteur de vue de Guso Facile : un même compte bascule entre le tableau '
    'de bord d’artiste de Camille et la gestion des GUSO de sa structure, sans '
    'se déconnecter.',
    """
    <div class="gf-bar">
      <span class="gf-bar-t">Je regarde</span>
      <span class="gf-bar-s">Un seul compte, deux casquettes</span>
    </div>
    <div class="gf-ctx">
      <div class="gf-ctx-cur">Camille — mon espace<em>changer de vue</em></div>
      <p class="gf-ctx-hint">Filtre d’affichage — ça ne change aucun droit, ni pour toi ni pour les autres.</p>
      <div class="gf-ctx-i gf-on">
        <span class="gf-ctx-d gf-art"></span>
        <span class="gf-ctx-t">Camille — mon tableau de bord d’artiste
          <em>Mes heures, mes dates, mes démarches</em></span>
        <span class="gf-ctx-chk">✓</span>
      </div>
      <div class="gf-ctx-i">
        <span class="gf-ctx-d gf-str"></span>
        <span class="gf-ctx-t">Compagnie des Trois Ponts — je gère les GUSO
          <em>Les artistes que la structure accompagne</em></span>
      </div>
    </div>
  """)


# --- 8. LA CARTE DE TOURNEE (rangee `.apercus`, univers 2) ----------------
# Ecran reproduit : la carte des dates. C'est un SCHEMA, pas une capture :
# l'app affiche une vraie carte (Leaflet), qu'aucun CSS ne peut reproduire —
# et une fausse carte geographique serait mensongere. Le trace est donc
# volontairement abstrait, sans pretendre a une geographie reelle.
# ⚠️ TROIS ELEMENTS PORTENT DU SENS, ce ne sont pas des ornements :
#     1. le point DOMICILE, en prune et plus gros : le kilometrage se calcule
#        depuis l'adresse du profil, la carte doit dire d'ou l'on part ;
#     2. le LIEU SUPPOSE, en anneau corail : l'app devine certains lieux et
#        demande de les confirmer — c'est ce que dit la puce « Tournee reliee »
#        de l'univers 2 (« les lieux a confirmer sont signales ») ;
#     3. le KILOMETRAGE CUMULE, dans la formulation de l'app.
#    La legende sous la carte nomme les trois : la FORME de la pastille et son
#    libelle suffisent, la couleur ne porte jamais seule l'information.
# ⚠️ Les chiffres sont FICTIFS et n'ont aucun rapport avec la tournee de la
#    maquette 5 (« Ma tournee », 8 cachets / 1 240 km, domicile en Gironde) :
#    ce sont deux illustrations distinctes, avec des lieux distincts. Aucun
#    chiffre reel — ni les 65 dates, ni les 61 feuillets, ni les 37 lieux.
# ⚠️ Le SVG porte `aria-hidden="true"` + `focusable="false"` : c'est le
#    `role="img"` + `aria-label` du bloc qui decrit la carte, l'enoncer deux
#    fois serait du bruit. `_controle_icones()` verifie les deux attributs sur
#    TOUTES les balises <svg> de la page, celle-ci comprise.
MAQ_CARTE = _figure(
    'Carte de tournée de Guso Facile : depuis le domicile, quatre dates '
    'reliées par un tracé — Salle des Tilleuls, Festival du Causse, Le Grand '
    'Pré, puis Théâtre Rivage, lieu supposé encore à confirmer. Trajets '
    'cumulés : environ 612 kilomètres aller, 1 224 aller-retour.',
    """
    <div class="gf-bar">
      <span class="gf-bar-t">Carte de mes dates</span>
      <span class="gf-bar-s">Saison 2026 — 5 dates</span>
    </div>
    <div class="gf-carte">
      <svg class="gf-map" viewBox="0 0 100 52" aria-hidden="true" focusable="false">
        <polyline class="gf-halo" points="14,40 30,24 52,18 68,31 88,15"/>
        <polyline class="gf-voie" points="14,40 30,24 52,18 68,31 88,15"/>
        <circle class="gf-pt gf-pt-dom" cx="14" cy="40" r="1.9"/>
        <circle class="gf-pt" cx="30" cy="24" r="1.5"/>
        <circle class="gf-pt" cx="52" cy="18" r="1.5"/>
        <circle class="gf-pt" cx="68" cy="31" r="1.5"/>
        <circle class="gf-pt gf-pt-sup" cx="88" cy="15" r="1.6"/>
        <text class="gf-lab-s" x="14" y="45.5" text-anchor="middle">Chez moi</text>
        <text class="gf-lab" x="30" y="20" text-anchor="middle">Salle des Tilleuls</text>
        <text class="gf-lab" x="52" y="14" text-anchor="middle">Festival du Causse</text>
        <text class="gf-lab" x="68" y="36.5" text-anchor="middle">Le Grand Pré</text>
        <text class="gf-lab" x="88" y="11" text-anchor="middle">Théâtre Rivage</text>
        <text class="gf-lab-s" x="88" y="22.5" text-anchor="middle">à confirmer</text>
      </svg>
    </div>
    <p class="gf-carte-km">Trajets cumulés — <b>≈ 612 km</b> (aller) · 1 224 km aller-retour</p>
    <p class="gf-carte-leg">
      <span><i class="gf-lg-dom"></i>Mon domicile</span>
      <span><i class="gf-lg-ok"></i>Date confirmée</span>
      <span><i class="gf-lg-sup"></i>Lieu supposé, à confirmer</span>
    </p>
  """, classe=' gf-carte-b')


# --- 9. « J'AI BESOIN D'AIDE », QUESTION 1 SUR 3 --------------------------
# Ecran reproduit : la premiere des trois questions du parcours, avec ses
# QUATRE reponses possibles — les libelles exacts de `HELP_KINDS`.
# ⚠️⚠️ CETTE MAQUETTE REGLE, EN IMAGE, LA CONFUSION 3/4 QUE LA PAGE DE
#    REFERENCE PORTAIT. Leur page annoncait « 3 questions, c'est tout » puis
#    listait QUATRE lignes : ce n'etaient pas quatre questions, c'etaient les
#    quatre REPONSES a la premiere. Le bloc `.aide` juste au-dessus liste les
#    TROIS QUESTIONS, numerotees ; cette maquette montre la QUESTION 1 et SES
#    QUATRE REPONSES, avec « Question 1 sur 3 » ecrit dans la barre et une
#    barre de progression a trois segments. Les deux se completent au lieu de
#    se repeter — et le lecteur ne peut plus se tromper.
#    ⚠️ Ne PAS « harmoniser » en mettant trois options ici : ce serait
#       reintroduire l'erreur exacte que ce placement corrige.
# ⚠️ La derniere phrase redit ce que le bloc `.aide` dit deja de la reponse
#    « personne du tout ». C'est voulu : c'est le coeur de la fonction — on peut
#    demander de l'aide sans que ca devienne social — et une image qui montre
#    un questionnaire sans le dire laisserait croire a une alerte automatique.
MAQ_AIDE = _figure(
    'Le parcours « J’ai besoin d’aide » de Guso Facile : la première des trois '
    'questions, « Qu’est-ce qui se passe ? », avec ses quatre réponses '
    'possibles et une barre de progression à trois segments.',
    """
    <div class="gf-bar">
      <span class="gf-bar-t">J’ai besoin d’aide</span>
      <span class="gf-bar-s">Question 1 sur 3</span>
    </div>
    <div class="gf-help">
      <p class="gf-prog"><i class="gf-cur"></i><i></i><i></i></p>
      <p class="gf-help-q">Qu’est-ce qui se passe ?</p>
      <p class="gf-opt"><span class="gf-opt-n">1</span><span>Je ne sais pas quoi faire ensuite</span></p>
      <p class="gf-opt"><span class="gf-opt-n">2</span><span>Je suis en retard sur mes heures</span></p>
      <p class="gf-opt"><span class="gf-opt-n">3</span><span>Un blocage administratif précis</span></p>
      <p class="gf-opt"><span class="gf-opt-n">4</span><span>Un doute plus perso, sur ma valeur ou ma légitimité</span></p>
      <p class="gf-help-f">Ensuite : tu veux que quelqu’un le sache ? Puis : c’est urgent ?<br>
        Répondre « personne » est une réponse comme une autre — rien n’est envoyé.</p>
    </div>
  """)


# --- 10. LE JOURNAL DES NOUVEAUTES (sous « Et aussi ») --------------------
# Ecran reproduit : le journal des versions. Sa structure — titre, date, resume,
# details, etiquette, mise en avant des versions majeures — est celle de
# `renderChangelogHtml()`.
# ⚠️ LES TROIS ENTREES SONT FICTIVES, et datees de mars/fevrier EXPRES pour
#    qu'on ne les confonde pas avec le vrai historique de l'application. Ne pas
#    les remplacer par de vraies lignes de changelog : elles vieilliraient dans
#    une page qui, elle, ne se regenere pas a chaque version de l'app.
# ⚠️ Il est pose sous l'encadre « Et aussi », dont la ligne « prise en main »
#    porte la puce « Nouveautes » — c'est la fonction qu'il illustre. Le mot
#    « Nouveautes » n'est PAS repris ici en toutes lettres : la barre dit « Quoi
#    de neuf », comme l'ecran. `ANCRES` compte `<b>Nouveautés</b>` une seule
#    fois, et ce compte doit rester celui de la puce.
MAQ_NOUVEAUTES = _figure(
    'Le journal des nouveautés de Guso Facile : trois évolutions de '
    'l’application, chacune avec sa date, son résumé et son étiquette, la plus '
    'récente mise en avant.',
    """
    <div class="gf-bar">
      <span class="gf-bar-t">Quoi de neuf</span>
      <span class="gf-bar-s">L’app évolue, tu es prévenu</span>
    </div>
    <div class="gf-cl">
      <div class="gf-cl-card gf-major">
        <div class="gf-cl-h">
          <span class="gf-cl-n">Le carnet de tournée</span>
          <span class="gf-cl-d">4 mars</span>
        </div>
        <p class="gf-cl-s">Toutes tes dates sur une carte, avec les kilomètres depuis chez toi.</p>
        <ul class="gf-cl-l">
          <li>Lieux géolocalisés, et lieux supposés à confirmer</li>
          <li>Trajets cumulés, aller et aller-retour</li>
        </ul>
        <span class="gf-cl-tag">Carte</span>
      </div>
      <div class="gf-cl-card">
        <div class="gf-cl-h">
          <span class="gf-cl-n">Vérifier ses disponibilités</span>
          <span class="gf-cl-d">21 février</span>
        </div>
        <p class="gf-cl-s">Avant d’accepter une date, savoir si elle tient la route.</p>
        <span class="gf-cl-tag">Organisation</span>
      </div>
      <div class="gf-cl-card">
        <div class="gf-cl-h">
          <span class="gf-cl-n">Carnet de contacts</span>
          <span class="gf-cl-d">9 février</span>
        </div>
        <p class="gf-cl-s">Les organisateurs rencontrés, avec la dernière date jouée ensemble.</p>
        <span class="gf-cl-tag">Contacts</span>
      </div>
    </div>
  """)


# --- LE BLOC DE RENVOI VERS LE BLOG (deux exemplaires) --------------------
# Il REMPLACE les deux `<p class="blog-lien"><a>…</a></p>`, qui etaient des
# lignes de texte soulignees. Verbatim de David : « c'est meme pas un bouton,
# c'est une ligne ». Voir le commentaire au-dessus de `.blog-cta` dans
# `CSS_PAGE` pour ce qui a ete fait, et surtout pour ce qui NE DOIT PAS l'etre
# (en faire un second bouton d'action plein).
# ⚠️ LE TITRE DE CHAQUE BLOC EST L'ANCRE DESCRIPTIVE D'ORIGINE, MOT POUR MOT
#    (dossier SEO §6 : nommer la destination et ce qu'on y trouve, jamais « en
#    savoir plus »). Ne pas la raccourcir en « Le blog » sous pretexte que le
#    bloc est maintenant grand : c'est elle que lit un moteur de recherche.
# ⚠️ La phrase de raccord ne promet aucun contenu qui n'existe pas : dix-huit
#    articles, lisibles sans compte — les deux sont verifiables.

def _blog_cta(surtitre, titre, phrase):
    """Un bloc de renvoi vers le blog. Aucun element focusable en plus du lien.

    La pastille flechee porte `aria-hidden` : elle repete visuellement ce que
    le lien dit deja, l'annoncer une seconde fois serait du bruit.
    """
    return ('  <a class="blog-cta" href="%s">\n'
            '    <span class="blog-cta-ic">%s</span>\n'
            '    <span class="blog-cta-txt">\n'
            '      <span class="blog-cta-k">%s</span>\n'
            '      <span class="blog-cta-t">%s</span>\n'
            '      <span class="blog-cta-d">%s</span>\n'
            '    </span>\n'
            '    <span class="blog-cta-go" aria-hidden="true"></span>\n'
            '  </a>\n' % (URL_BLOG, _ic('articles'), surtitre, titre, phrase))


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
    # ------------------------------------------------------------------
    # AJOUTES LE 16/08/2026 — les trois traces de la double vue et de l'appel
    # ------------------------------------------------------------------
    # En-tete « Pour les artistes » : une presence, pas un avatar de logiciel.
    # ⚠️ Volontairement DIFFERENT de 'groupe' (cas 3, plusieurs artistes
    #    accompagnes) : ici il n'y en a qu'un, c'est le point de vue.
    #    La page de reference met un emoji 👤 a cet endroit — la charte du site
    #    l'interdit, et c'est aussi une demande explicite de David.
    'artiste': '<circle cx="12" cy="7.9" r="3.5"/>'
               '<path d="M5.1 20.4c0-3.8 3.1-6.3 6.9-6.3s6.9 2.5 6.9 6.3"/>',
    # En-tete « Pour les structures » : la mallette de celui qui emploie.
    # ⚠️ Volontairement DIFFERENT de 'maison' (univers 3, le fronton d'un lieu) :
    #    l'en-tete nomme un METIER, la carte nomme un espace. La page de
    #    reference met un emoji 🛠 a cet endroit.
    'structures': '<rect x="3.2" y="6.7" width="17.6" height="13.7" rx="3"/>'
                  '<path d="M9 6.7V5.3a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1.4"/>'
                  '<path d="M3.2 12.4h17.6"/>',
    # « J'ai besoin d'aide » : la bouee. Ni une main tendue (trop pathetique au
    # trait), ni un point d'interrogation (deja le marqueur des quatre lignes) :
    # un objet qu'on tend sans que personne ait a demander deux fois. La page de
    # reference met un emoji 🤗 sur cette section.
    'bouee': '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="3.4"/>'
             '<path d="M6 6l3.6 3.6"/><path d="M14.4 14.4L18 18"/>'
             '<path d="M18 6l-3.6 3.6"/><path d="M9.6 14.4L6 18"/>',
    # ------------------------------------------------------------------
    # AJOUTE LA NUIT DU 16/08/2026 — le bloc `.blog-cta`
    # ------------------------------------------------------------------
    # Le feuillet de tete d'une pile, et ses lignes de texte : dix-huit
    # articles, pas un seul. ⚠️ C'est le PREMIER pictogramme de cette page a
    # servir DEUX fois (les deux blocs de renvoi vers le blog), d'ou le compte
    # de `NB_PICTOS` qui n'est plus egal au nombre d'entrees de ce
    # dictionnaire — voir la note au-dessus de la constante.
    # ⚠️ Volontairement DIFFERENT de 'document' de `theme_chaleur.py` (un
    #    feuillet corne, les identifiants officiels d'une association) : ici
    #    c'est une PILE, et c'est ce que le bloc promet.
    'articles': '<rect x="3.3" y="6.2" width="13.4" height="14.3" rx="2.3"/>'
                '<path d="M16.7 9.3h1.5a2 2 0 0 1 2 2v7.2a2 2 0 0 1-2 2"/>'
                '<path d="M6.5 10.1h7"/><path d="M6.5 13.4h7"/><path d="M6.5 16.7h4.3"/>',
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
    # Le lot 2 (16/08/2026, nuit) et la carte. Ils arrivent APRES `CSS_MAQUETTES`
    # — dont ils reprennent `.gf-shot`, `.gf-bar` et `.gf-cap` sans les toucher —
    # et AVANT `CSS_TYPO`, qui doit rester la derniere feuille a parler des
    # titres. Aucune de leurs regles ne vise `h1`…`h4` : les deux seules polices
    # qu'ils imposent (`.gf-help-q`, `.gf-map .gf-lab`) sont sur leurs propres
    # classes, jamais sur une balise de titre.
    A(CSS_LOT2)
    A(CSS_CARTE)
    # L'exception typographique arrive EN DERNIER, apres les maquettes : elle
    # surcharge `h1,h2,h3,h4` de CSS_BASE, les tailles de CSS_PAGE ET les deux
    # titres serif de CSS_MAQUETTES. La poser plus haut la ferait ecraser par
    # ce qui suit — c'est exactement le piege que `theme_chaleur.py` documente
    # pour la couche chaleureuse commune.
    A(CSS_TYPO)
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
"""
      # Le lien du hero disait « COMMENT demander un acces » : c'etait exact
      # tant que la section #acces ne faisait qu'EXPLIQUER la marche a suivre
      # avant d'envoyer ailleurs. Depuis le 16/08/2026 elle porte le formulaire
      # lui-meme : ce lien mene donc directement a l'endroit ou l'on saisit, et
      # « Comment » serait devenu un detour annonce pour rien. Il reste une
      # ancre INTERNE — aucun clic ne quitte plus la page.
      # ⚠️ LE LIEN VERS LE BLOG EST DANS CETTE RANGEE, PAS SOUS ELLE. C'est le
      # SEUL lien du premier ecran vers les dix-huit articles — avant cette
      # passe, le premier n'arrivait qu'au pixel 3 376. Trois precautions :
      #   - c'est un LIEN souligne, pas un second bouton : la page n'a qu'un
      #     geste possible, et l'ecart n° 8 en tete de fichier tient ;
      #   - `.cta` est en flex : au-dela de ~1000 px il se pose SUR LA MEME
      #     LIGNE que le bouton, donc il ne coute pas un pixel de hauteur ;
      #   - l'ancre est DESCRIPTIVE (regle du dossier SEO, §6) : elle nomme la
      #     destination et ce qu'on y trouve, jamais « en savoir plus ».
      """  <div class="cta">
    <a class="btn ghost" href="#acces">Demander un accès</a>
    <a class="hero-blog" href="/guso-facile/blog">Le blog : dix-huit situations concrètes</a>
  </div>
"""
      # LE LIEN DE CONNEXION DES BETA-TESTEURS (17/08/2026, decision de David).
      # Depuis la fusion du 16/08, le bouton mene au FORMULAIRE DE DEMANDE : une
      # personne qui a deja un compte n'avait plus aucun chemin vers l'appli
      # depuis cette page, et devait retaper une adresse en `vercel.app`.
      # ⚠️ TROIS CHOSES A NE PAS DEFAIRE :
      #   1. C'est un <p> SOUS `.cta`, pas un troisieme enfant de `.cta` : dans
      #      la rangee flex il se serait pose sur la ligne du bouton, au meme
      #      rang que lui. La page n'a qu'UN geste principal (ecart n° 8).
      #   2. AUCUNE classe `btn`. Ce n'est pas un bouton, et ce ne doit pas en
      #      devenir un « pour qu'on le voie mieux » : les ~95 % de visiteurs
      #      sans compte n'ont rien a faire de cette porte.
      #   3. L'`href` est `/guso-facile/app`, JAMAIS l'adresse de l'appli.
      #      C'est tout l'interet : un seul endroit a changer le jour ou David
      #      prendra un domaine (voir « L'ADRESSE STABLE DE CONNEXION » en tete
      #      de fichier). L'ancre `guso-facile.vercel.app` a ZERO l'impose.
      # La fleche est le caractere « → », pas un pictogramme : la page en compte
      # 11 et `NB_PICTOS` ne bouge pas. Aucun emoji (charte du site).
      """  <p class="hero-cnx"><a href="/guso-facile/app">J’ai déjà un compte → me connecter</a></p>
"""
      # ===================================================================
      # LE SOMMAIRE DE LA PAGE (17/08/2026) — cinq ancres, aucune inventee
      # ===================================================================
      # LE CONSTAT : 25 455 px a 390 px, 15 038 px a 1440. Un lecteur qui sait
      # ce qu'il cherche devait faire defiler une trentaine d'ecrans pour le
      # trouver. Le sommaire lui rend ce controle SANS RIEN CACHER — c'est la
      # difference avec la couche 2, qui replie l'inventaire.
      #
      # ⚠️ LES CINQ ANCRES EXISTAIENT DEJA TOUTES, relevees dans la page
      #    livree et non devinees : `#promesse`, `#situations`,
      #    `#fonctionnalites`, `#faq`, `#acces`. AUCUNE n'a ete creee pour ce
      #    bloc, et aucune ne doit l'etre : le projet a deja publie des liens
      #    vers des ancres inexistantes. `controle_liens()` de verif_site.py
      #    verifie de son cote que chaque `href="#…"` trouve son `id`.
      #
      # LES LIBELLES NE RECOPIENT PAS LES TITRES DE SECTION, et c'est le point
      # qui demande le plus d'attention. Un sommaire qui repete « Garde ton
      # energie pour la scene · Trois situations typiques · Pensee pour les
      # artistes et les structures » n'aide personne a choisir : ce sont des
      # titres qui SEDUISENT, pas des titres qui SITUENT. Les cinq libelles
      # repondent chacun a une question que le lecteur se pose vraiment :
      #     #promesse        « Ce qu'il y a dedans » ? non : ce que ca CHANGE
      #                      pour lui (la section dit la charge mentale et ce
      #                      qui la remplace).
      #     #situations      « Pour qui » — Lea, Marco et Sophie repondent
      #                      exactement a « est-ce que c'est pour moi ? ».
      #     #fonctionnalites « Ce qu'il y a dedans » — c'est l'inventaire, et
      #                      c'est le mot juste depuis que la couche 2 le
      #                      replie derriere quatre titres.
      #     #faq             « Questions » — le mot que les gens cherchent ;
      #                      la section s'appelle « Les questions qu'on se pose
      #                      sur l'intermittence », trop long pour une ligne.
      #     #acces           « Demander un acces » — MOT POUR MOT le libelle du
      #                      bouton, a dessein : c'est le geste unique de la
      #                      page, il doit se nommer partout pareil.
      # ⚠️ LE DERNIER LIEN MENE A `#acces`, ET CE N'EST PAS NEGOCIABLE : l'appel
      #    a l'action doit rester atteignable en UN clic depuis le haut, quelle
      #    que soit la longueur de la page. Ce n'est pas un second bouton — un
      #    lien gris de 15 px dans une liste a points ne concurrence pas le
      #    bouton dore du hero, place trois lignes au-dessus. L'ecart n° 8 tient.
      #
      # ⚠️ `aria-label` EN FRANCAIS ET EXPLICITE sur le <nav> : la page en compte
      #    desormais DEUX (le menu du site, pose par nav_menu.py, et celui-ci).
      #    Sans etiquette, un lecteur d'ecran annonce « navigation » deux fois
      #    sans dire laquelle. Le titre visible « Sur cette page » joue le meme
      #    role pour tout le monde.
      """  <nav class="gf-som" aria-label="Sommaire de la page">
    <p class="gf-som-t">Sur cette page</p>
    <ul>
      <li><a href="#promesse">Ce que ça change</a></li>
      <li><a href="#situations">Pour qui</a></li>
      <li><a href="#fonctionnalites">Ce qu’il y a dedans</a></li>
      <li><a href="#faq">Questions</a></li>
      <li><a href="#acces">Demander un accès</a></li>
    </ul>
  </nav>
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
    # LE BLOC `.mea` — LA MISE EN VALEUR DU BLOG (16/08/2026)
    # -------------------------------------------------------------------
    # IL REMPLACE le premier des deux liens descendants (dossier SEO, §6), qui
    # tenait sur une ligne et ne montrait aucun titre. Verbatim de David : « le
    # blog n'est pas du tout mis en valeur alors meme qu'il est super riche et
    # que ca peut etre une enorme porte d'entree ». Le detail de la mesure
    # avant/apres est en tete de fichier.
    #
    # POURQUOI ICI, ET PAS DANS UNE SECTION A PART : la page est sous plafond
    # de hauteur (~12 500 px a 1440) et une `<section>` de plus coutait 184 px
    # de respiration. Or c'est exactement sa place : la section s'appelle
    # « Trois situations typiques », le blog en raconte quinze autres — et la
    # phrase de raccord le dit litteralement. Le bloc porte `id="blog"`, il
    # reste donc une cible d'ancre.
    #
    # ⚠️ LA PHRASE DE RACCORD EST VERIFIABLE, PAS DECORATIVE : les titres des
    #    trois cas d'usage ci-dessus (« Atteindre ses 507 heures sans
    #    angoisse », « Pointer France Travail en 5 minutes », « Accompagner ses
    #    artistes sans tableur ») sont MOT POUR MOT trois des dix-huit `h1` du
    #    blog. 3 + 15 = 18. Si un titre d'article changeait la, cette phrase
    #    deviendrait fausse ici : c'est l'une des raisons d'etre de
    #    `_controle_mise_en_avant()`.
    #
    # ⚠️ « sans avoir de compte » : le blog est PUBLIC, contrairement a l'app.
    #    C'est la reponse a l'hesitation de quelqu'un qui ne veut pas encore
    #    demander un acces — et c'est la raison pour laquelle ce bloc est haut
    #    dans la page et pas en pied.
    A("""
  <div class="mea" id="blog">
    <p class="kick">Le blog de Guso Facile</p>
    <h2 class="mea-t">Dix-huit autres situations, en détail</h2>
    <p class="mea-s">Les trois cas ci-dessus sont racontés en entier sur le blog, avec quinze autres :
      les heures, la répétition, le contrat, l’impayé, la tournée. En lecture libre, sans compte.</p>
    <div class="mea-g">
""")
    for slug, rubrique, titre, accroche, lecture in MISE_EN_AVANT:
        A('      <a class="mea-c" href="%s/%s">\n'
          '        <p class="mea-r">%s</p>\n'
          '        <p class="mea-h">%s</p>\n'
          '        <p class="mea-d">%s</p>\n'
          '        <span class="mea-l">%s de lecture</span>\n'
          '      </a>\n' % (URL_BLOG, slug, rubrique, titre, accroche, lecture))
    A("""    </div>
""")
    A(_blog_cta(
        'Tout le blog',
        'Les dix-huit articles du blog de Guso Facile',
        'En lecture libre, sans compte — le GUSO, les 507 heures, la DPAE, '
        'l’impayé, la tournée.'))
    A("""  </div>
""")
    A("""</div></section>
""")

    # =====================================================================
    # 4. LES FONCTIONNALITES  (section 4 du contenu fourni — verbatim)
    # =====================================================================
    # Quatre blocs, puces en point d'or. Aucun emoji, conformement a la charte.
    #
    # =====================================================================
    # ⚠️⚠️ LA DOUBLE VUE « ARTISTES | STRUCTURES » (16/08/2026)
    # =====================================================================
    # VERBATIM DE DAVID : « ce qui manque, c'est cette double vue qui montre que
    # l'app sert a la fois les artistes ou les structures ».
    #
    # LE DEFAUT, ET IL ETAIT REEL. Les quatre univers disaient deja que l'outil
    # sert les deux — mais EN FILE, jamais EN VIS-A-VIS. Une grille 2 x 2 de
    # quatre cartes toutes pareilles se lit comme un inventaire : il fallait
    # lire les quatre titres pour comprendre que la troisieme carte s'adressait
    # a quelqu'un d'autre. La page de reference porte, elle, une section « Une
    # app, deux metiers · Pensee pour les artistes ET les structures » en deux
    # colonnes cote a cote : la dualite s'y comprend EN UNE SECONDE, avant meme
    # la lecture. C'est un dispositif VISUEL, et c'est lui qu'on reprend.
    #
    # ⚠️⚠️ CE QUI A ETE FUSIONNE POUR NE RIEN DUPLIQUER — le point capital.
    # La page de reference porte CETTE section-la (13 fonctions) *ET*, plus bas,
    # ses quatre univers (22 puces) : elle ecrit donc deux fois le meme
    # inventaire, sous deux angles. ICI ON NE LE FAIT PAS. Le vis-a-vis
    # n'AJOUTE aucune puce : il REORGANISE celles qui existaient deja.
    #     avant : grille `.univers` a plat, 4 cartes en 2 x 2, sans en-tete
    #     apres : colonne « Pour les artistes » = univers 1 + univers 2
    #             colonne « Pour les structures » = univers 3 + l'apercu
    #                                               « Mes artistes »
    #             puis, pleine largeur, « et pour les deux » = univers 4
    # PAS UNE PUCE AJOUTEE, PAS UNE PUCE RETIREE, PAS UN MOT REECRIT : les 25+
    # lignes d'inventaire sont exactement les memes, dans le meme ordre. Ce qui
    # est neuf tient en trois elements : les deux en-tetes de colonne, la
    # bande « et pour les deux », et le titre de section.
    #
    # POURQUOI L'UNIVERS 4 PASSE PLEINE LARGEUR, alors qu'un commentaire du
    # 14/08/2026 s'y opposait. Le motif d'alors : « la carte 4 est justement
    # celle dont la plupart des puces sont (a venir), l'etaler sur toute la
    # largeur l'aurait mise en avant plus que les trois autres ». CE MOTIF A
    # DISPARU : depuis la remise a niveau du 16/08, il ne lui reste que DEUX
    # puces « a venir » sur sept. Et surtout la pleine largeur DIT quelque
    # chose ici : « Ton cercle, solidaire » est le seul univers qui ne
    # s'adresse ni aux artistes seuls ni aux structures seules — il est le
    # terrain commun, donc il porte les deux colonnes.
    #
    # ⚠️ LE TITRE DE SECTION A CHANGE, ET C'EST LE SEUL TEXTE REECRIT ICI.
    #    « Bien plus qu'un compteur d'heures » -> « Pensée pour les artistes et
    #    les structures », avec le « et » PEINT AU DEGRADE (`.grad-t`), comme
    #    sur la page de reference : c'est le mot-cle de la section, et c'est un
    #    bon usage de notre degrade signature.
    #    L'ancien titre n'est PAS perdu : il devient le sur-titre… non, il
    #    devient la phrase de conduite (`.lead`), parce qu'il dit encore quelque
    #    chose de vrai — il ne disait simplement pas ce qui manquait.
    #
    # LES MAQUETTES, RAPPROCHEES DE CE QU'ELLES ILLUSTRENT (demande de David :
    # « il manque des apercus visuels de l'app quand ca parle d'une fonction ») :
    #   - « Mes artistes » est desormais DANS la colonne « Pour les structures »,
    #     juste sous l'univers 3 dont elle est l'ecran ;
    #   - la fiche d'une date et l'enchainement de la tournee forment la rangee
    #     `.apercus`, immediatement sous les colonnes, cote a cote ;
    #   - la jauge des 507 h est deja dans le hero, contre la promesse des
    #     507 heures ; « A faire maintenant » est deja colle a la phrase qui le
    #     nomme, en fin de #promesse ; le recap mensuel est deja sous le cas de
    #     Marco, « Pointer France Travail en cinq minutes ». Ces trois-la
    #     n'avaient rien a gagner a bouger — verifie avant de les deplacer.
    # ⚠️ NI la Guilde NI l'espace « Gratitudes » ne sont illustres : leurs
    #    ecrans existent mais AUCUNE DONNEE n'y a ete saisie. Les illustrer
    #    montrerait un contenu invente dans un espace vide (voir l'entete).
    A("""
<div class="divider"></div>
<section id="fonctionnalites"><div class="wrap">
  <p class="kick">Une app, deux métiers</p>
  <h2 class="sec-title">Pensée pour les artistes <span class="grad-t">et</span> les structures</h2>
  <p class="lead">Bien plus qu’un compteur d’heures : les données saisies d’un côté servent l’autre.
    Chacun sa vue, un seul outil.</p>

  <div class="duo">

    <div class="duo-col" role="group" aria-labelledby="duo-artistes">
      <div class="duo-h">
        <span class="duo-ico">""" + _ic('artiste') + """</span>
        <div>
          <p class="duo-t" id="duo-artistes">Pour les artistes<span class="duo-q">Intermittent·e du spectacle</span></p>
        </div>
      </div>

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
    </div>

    <div class="duo-col" role="group" aria-labelledby="duo-structures">
      <div class="duo-h">
        <span class="duo-ico">""" + _ic('structures') + """</span>
        <div>
          <p class="duo-t" id="duo-structures">Pour les structures<span class="duo-q">Celles et ceux qui emploient et accompagnent</span></p>
        </div>
      </div>

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
"""
      # -------------------------------------------------------------------
      # « SYNCHRONISATION » — PROMESSE FAUSSE, CORRIGEE LE 16/08/2026
      # -------------------------------------------------------------------
      # La puce disait : « ce que l'artiste renseigne apparait cote structure
      # EN TEMPS REEL, et inversement ». C'est FAUX, et c'est verifie dans le
      # code de l'application : zero abonnement temps reel (aucun `.channel(`,
      # aucun `postgres_changes`, aucun `realtime`). L'ECRITURE part bien
      # immediatement ; LA LECTURE, elle, ne se fait qu'au chargement de
      # l'espace — deux onglets cote a cote ne se mettent pas a jour tout
      # seuls. C'etait la seule promesse de la page qu'une structure pouvait
      # dementir en dix secondes, et c'est le pire endroit pour ca : la page
      # publique d'une association.
      # La phrase ci-dessous est celle validee par l'auteur de l'application,
      # reprise TELLE QUELLE. Elle dit ce qui est vrai — le partage — sans
      # rien promettre sur le DELAI. Une ancre a ZERO occurrence dans `ANCRES`
      # interdit le retour de « en temps réel ».
      """        <li><b>Synchronisation</b> — les données sont partagées entre l’artiste et la structure.</li>
"""
      # -------------------------------------------------------------------
      # « NIVEAUX DE PARTAGE » — fonctionnalite LIVREE, ajoutee le 16/08/2026
      # -------------------------------------------------------------------
      # Phrase confirmee dans le code par l'auteur de l'app, reprise telle
      # quelle. Elle est POSEE ICI, juste apres « Synchronisation », parce que
      # c'est la meme relation qu'elle regle : ce que la structure voit de
      # l'artiste. Le point de vue est celui de l'ARTISTE, dans la carte des
      # structures — c'est voulu : c'est lui qui decide, et une structure qui
      # lit cette carte doit le savoir.
      # ⚠️ NE PAS LA CONFONDRE AVEC « Confidentialite graduee » (univers 4,
      #    toujours « (a venir) »). Celle-ci offre TROIS NIVEAUX PREDEFINIS et
      #    elle est livree ; l'autre promet le reglage fin, donnee par donnee,
      #    dont l'ecran cote artiste n'existe pas encore. Les deux sont dans
      #    DEUX CARTES DIFFERENTES pour cette raison exacte. Ne pas les
      #    rapprocher, et ne pas raccourcir l'enumeration des trois niveaux :
      #    c'est elle qui rend la difference visible a l'ecran.
      """        <li><b>Niveaux de partage</b> — pour chaque structure, l’artiste choisit ce qu’elle voit : tout, l’essentiel administratif, ou seulement ses totaux d’heures. Il peut en changer ou se retirer à tout moment.</li>
      </ul>
    </article>
""")

    # MAQUETTE 6 (`MAQ_STRUCTURE`) — la vue « Mes artistes » du back-office.
    #   Elle FERME LA COLONNE « Pour les structures », directement sous
    #   l'univers 3 dont elle est l'ecran. C'est le rapprochement demande par
    #   David (« il manque des apercus visuels de l'app quand ca parle d'une
    #   fonction ») : avant cette passe elle etait posee APRES l'univers 4, donc
    #   apres un univers qui ne la concerne pas.
    #   ⚠️ Elle ne porte plus `gf-wide` : la grille `.univers` qui lui donnait
    #   sa pleine largeur n'existe plus, et une colonne de flex n'a pas de piste
    #   a enjamber. Sa largeur est desormais celle de sa colonne.
    #   ⚠️ Elle garde sa note « (a venir) » : cette vue est en cours de
    #   construction (voir le commentaire au-dessus de `MAQ_STRUCTURE`).
    A(MAQ_STRUCTURE)

    # Fin de la colonne « Pour les structures », puis fin du vis-a-vis.
    # LA RANGEE `.apercus` : les deux apercus cote ARTISTE, cote a cote, juste
    # sous les colonnes. La fiche montre ce que devient UNE date une fois
    # saisie ; « Ma tournee » ce que devient la SUITE des dates. Ils tombent
    # sous la colonne des artistes, a un ecran des univers 1 et 2 qu'ils
    # illustrent.
    A("""    </div>

  </div>
""")

    # MAQUETTE 7 (`MAQ_SELECTEUR`) — le selecteur « Je regarde ». Il ferme le
    #   vis-a-vis : les deux colonnes RACONTENT la double vue, cet ecran la
    #   PROUVE — un compte, deux casquettes, aucune deconnexion. C'est pour
    #   cette raison qu'il est ici et pas dans une colonne : il n'appartient a
    #   aucune des deux, il est ce qui passe de l'une a l'autre.
    A(MAQ_SELECTEUR)

    A("""
  <div class="apercus">
""")
    A(MAQ_FICHE)
    A(MAQ_TOURNEE)
    # MAQUETTE 8 (`MAQ_CARTE`) — la carte de tournee, l'ecran de l'univers 2
    #   « Ta tournee, organisee ». Elle enjambe les deux colonnes de la rangee
    #   (`grid-column:1/-1`), juste sous « Ma tournee » qui liste les memes
    #   etapes autrement : la liste dit l'ORDRE, la carte dit la DISTANCE.
    #   ⚠️ Elle est plafonnee a 556 px, et ce plafond n'est pas un gout : c'est
    #   lui qui rend la largeur rendue previsible, donc les trois paliers de
    #   taille de ses libelles calculables. Voir `CSS_CARTE`.
    A(MAQ_CARTE)

    # LA BANDE « ET POUR LES DEUX ». L'univers 4 n'appartient a aucune des deux
    # colonnes : c'est le seul qui decrive ce qui se passe ENTRE elles. Il ferme
    # donc la section, pleine largeur, sous un filet degrade — voir le long
    # commentaire en tete de cette section pour le pourquoi du changement de
    # largeur.
    A("""  </div>

  <div class="deux">
    <p class="kick">Et pour les deux</p>
    <article class="u-card">
      <div class="u-head">
        <span class="u-ico">""" + _ic('cercle') + """</span>
        <div>
          <p class="u-num">Univers 4</p>
          <h3>Ton cercle, solidaire</h3>
        </div>
      </div>
      <p class="u-sub">Parce qu’on avance mieux à plusieurs.</p>
      <ul>
        <li><b>Vue groupe</b> — où en est chaque membre du groupe, pour se soutenir avant que la situation ne coince.</li>
"""
      # -------------------------------------------------------------------
      # « HUB D'INFORMATIONS DU GROUPE » — LIVREE, ajoutee le 16/08/2026
      # -------------------------------------------------------------------
      # Phrase confirmee dans le code par l'auteur de l'app, reprise telle
      # quelle. Elle suit « Vue groupe » : l'une dit ou en est chacun, l'autre
      # dit ou se rangent les informations communes. Meme carte, meme sujet.
      """        <li><b>Hub d’informations du groupe</b> — un espace commun où le groupe partage les informations d’une date.</li>
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
      # -------------------------------------------------------------------
      # « INSCRIPTION PAR INVITATION » — LIVREE, ajoutee le 16/08/2026
      # -------------------------------------------------------------------
      # Phrase confirmee dans le code par l'auteur de l'app, reprise telle
      # quelle. Elle suit « Faire decouvrir l'outil » parce qu'elle en est la
      # suite mecanique : la cooptation PROPOSE quelqu'un, l'invitation lui
      # OUVRE la porte. Les deux disent la meme chose que la section « Jouons
      # cartes sur table » (« l'acces se fait sur invitation ou sur
      # cooptation ») — c'est voulu, la page doit etre coherente d'un bout a
      # l'autre sur ce point.
      # ⚠️ « Inscription par invitation » a d'abord ete posee ICI, a la suite de
      # « Faire decouvrir l'outil » (la cooptation propose, l'invitation ouvre).
      # Elle est finalement DANS LA LIGNE « prise en main » de l'encadre « Et
      # aussi », pour deux raisons — l'une de sens, l'autre mesuree :
      #   - de sens : « Faire decouvrir » est ce que JE fais pour quelqu'un
      #     d'autre ; l'invitation est ce que MOI je vis en arrivant. C'est la
      #     premiere etape de la prise en main, et la ligne suit exactement cet
      #     ordre (j'arrive, on m'accueille, je cherche comment faire, je suis
      #     ce qui change) ;
      #   - mesuree : la grille des univers est a deux colonnes, et sa
      #     troisieme rangee prend la hauteur de la carte la PLUS HAUTE. Une
      #     puce de plus dans l'univers 4 coutait 114 px a la page entiere,
      #     alors que la carte voisine (univers 3) a deja 329 px de vide. La
      #     meme phrase dans « Et aussi » en coute 37. Voir l'entete : la page
      #     est sous plafond de hauteur.
      ""
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
"""
      # -------------------------------------------------------------------
      # « POINTS DE VIGILANCE COTE STRUCTURE » — LIVREE (17/08/2026)
      # -------------------------------------------------------------------
      # HISTOIRE, parce qu'elle explique la forme de la ligne : du 14 au
      # 16/08/2026 cette puce portait `class="soon"` + `<i>(a venir)</i>`, et
      # elle ne disait que l'intention (« qui approche du seuil, qui aurait
      # besoin d'un coup de main »). LE 17/08/2026, l'ecran est deploye et
      # VERIFIE EN PRODUCTION dans le bundle servi (`sdCardHtml`, cartes
      # d'artistes) : la puce passe au PRESENT et dit ce que la structure voit
      # reellement.
      # Phrase de l'auteur de l'application, reprise quasi verbatim ; seuls la
      # ponctuation et les articles ont ete ajustes au gabarit des puces.
      # ⚠️ C'est CETTE vue que la maquette 6 « Mes artistes » illustre : les
      #    deux passent au present le meme jour, ne pas en remettre une seule
      #    au futur sans l'autre.
      """        <li><b>Points de vigilance côté structure</b> — la structure voit, par artiste : ses heures sur la période, les jours restants avant la date anniversaire, le rythme nécessaire, et un niveau d’alerte. Le tout trié par urgence.</li>
"""
      # -------------------------------------------------------------------
      # « CONFIDENTIALITE GRADUEE » — LIVREE (17/08/2026)
      # -------------------------------------------------------------------
      # Au 16/08/2026 le backend existait et etait teste, mais L'ECRAN DE
      # REGLAGE COTE ARTISTE n'existait pas : la puce etait `class="soon"` +
      # « (a venir) ». Verifie en production le 17/08/2026 dans le bundle servi
      # (`affSetVisibility`, `affSetManage`, les trois libelles « Tout
      # partager » / « Partenaire » / « Minimal », et le niveau stocke comme
      # DONNEE — `visibility:'full'`) : l'ecran existe.
      #
      # ⚠️ « COTE SERVEUR » N'EST PAS UN DETAIL TECHNIQUE GRATUIT, NE PAS LE
      #    COUPER AU PROCHAIN MENAGE DE LONGUEUR. C'est la seule phrase qui
      #    distingue une vraie confidentialite d'un masquage d'affichage : la
      #    structure NE RECOIT PAS les donnees qu'elle n'a pas le droit de
      #    voir, au lieu de les recevoir et de ne pas les montrer. C'est ce qui
      #    rend la promesse serieuse sur une page publique portee par une
      #    association. Elle est ecrite en langage clair, pas en jargon.
      #
      # ⚠️ RACCORD AVEC « NIVEAUX DE PARTAGE » (univers 3). Jusqu'au 16/08/2026
      #    les deux puces etaient tenues SEPAREES parce que l'une etait livree
      #    et l'autre « (a venir) » : « Niveaux de partage » offrait les trois
      #    niveaux predefinis, « Confidentialite graduee » promettait l'ecran de
      #    reglage. Ce motif de separation a disparu — c'est la MEME
      #    fonctionnalite, vue des deux bouts : ce que la structure recoit
      #    (univers 3) et ce que l'artiste regle (univers 4). La puce ci-dessous
      #    le dit donc explicitement (« le réglage des niveaux de partage »)
      #    plutot que de rejouer la meme phrase a quinze lignes d'intervalle, et
      #    elle apporte ce que l'autre n'a pas : la garantie cote serveur.
      #    🚩 A ARBITRER PAR DAVID / L'AUTEUR DE L'APP : les deux puces peuvent
      #    desormais etre fusionnees en une seule. On ne le fait pas ici — ce
      #    serait retirer une ligne d'inventaire validee, sans mandat.
      """        <li><b>Confidentialité graduée</b> — le réglage des niveaux de partage, structure par structure : tout partager, l’essentiel administratif, ou ses totaux d’heures seuls. Le filtrage est fait côté serveur, pas seulement à l’affichage : la structure ne reçoit pas les données qu’elle n’a pas le droit de voir, au lieu de les recevoir et de ne pas les montrer. Et l’artiste peut changer d’avis, ou se retirer, quand il veut.</li>
      </ul>
    </article>
  </div>
""")

    # ===================================================================
    # « J'AI BESOIN D'AIDE » — ABSORBE LE 16/08/2026
    # ===================================================================
    # VERBATIM DE DAVID : « tu ne parles pas de la fonction j'ai besoin
    # d'aide ». Elle est LIVREE, et elle n'existait ici que sous la forme d'une
    # puce d'inventaire de dix mots, au milieu de six autres. La page de
    # reference (`~/CLAUDE/GUSO FACILE/presentation.html`, LECTURE SEULE) lui
    # consacre une section entiere : c'est la fonctionnalite la plus humaine de
    # l'outil, et c'est la seule qui parle de ce qui se passe quand ca va mal.
    #
    # ⚠️ ELLE S'ECRIT AU PRESENT — l'ecran existe, il est deploye. Aucune
    #    mention « (a venir) », `NB_A_VENIR` ne bouge pas.
    #
    # ⚠️⚠️ TOUT CE QUI EST ECRIT ICI SE LIT DANS LEUR PAGE. RIEN N'EST INVENTE.
    #    Correspondance ligne a ligne, pour que ce soit verifiable :
    #      - « un bouton dans l'app, un questionnaire ultra-rapide — 3
    #        questions, reponses simples — pour cerner ton besoin sans jamais
    #        te juger » -> le paragraphe d'ouverture ;
    #      - les TROIS questions du parcours -> voir la note datee ci-dessous :
    #        elles ne viennent PAS de leur page, mais de l'auteur de l'app ;
    #      - « selon ta reponse, l'app te donne immediatement un premier geste
    #        concret — pas une brochure, une action » -> leur premiere carte ;
    #      - « si tu le veux, l'app previent ton groupe, ta structure, ou une
    #        personne precise. Toi seul choisis qui, et quoi » -> la seconde ;
    #      - « Demander de l'aide devient un geste simple, pas un aveu » ->
    #        leur `.help-quote`, reprise TELLE QUELLE en accroche serif.
    #
    # ✅ TRANCHE LE 16/08/2026 — L'AUTEUR DE L'APP A REPONDU (il a lu le
    #    parcours dans le code). L'incoherence de leur page etait celle-ci :
    #    le titre annoncait « 3 questions, c'est tout » et listait QUATRE
    #    lignes. Le NOMBRE etait juste, c'est l'illustration qui etait fausse :
    #    les quatre lignes n'etaient pas les questions, c'etaient les REPONSES
    #    POSSIBLES A LA PREMIERE. Le parcours reel pose bien trois questions :
    #      1. Qu'est-ce qui se passe ?      (prochain pas · retard d'heures ·
    #         blocage administratif · doute plus perso sur sa valeur —
    #         ce sont les quatre anciennes lignes, remises a leur place)
    #      2. Tu veux que quelqu'un le sache ?  (groupe · structure · une
    #         personne precise · personne du tout)
    #      3. C'est urgent ?                (ca peut attendre · cette semaine ·
    #         la, maintenant)
    #    Les lignes sont NUMEROTEES 1-2-3 : c'est ce qui rend le « trois »
    #    verifiable a l'oeil, et c'est precisement ce qui manquait a leur page.
    #    `ANCRES` compte desormais le nombre annonce ET le nombre affiche.
    #
    # ⚠️⚠️ LA NUANCE DE LA QUESTION 2, A NE PAS ECRASER AU PROCHAIN MENAGE.
    #    « Personne du tout » est une REPONSE PLEINE ET ENTIERE, pas un
    #    renoncement : l'application repond alors « c'etait pour toi, prends
    #    soin de toi » et N'ENVOIE RIEN. C'est le coeur de la fonction — on
    #    peut demander de l'aide sans que ca devienne social. Elle n'est donc
    #    presentee ni comme une option par defaut, ni comme un refus, ni comme
    #    un dernier recours : l'incise est dans la ligne meme, et la phrase
    #    « On peut donc demander de l'aide sans que ca devienne social » ferme
    #    le bloc. C'est ce qui distingue cette fonction d'un bouton d'alerte,
    #    et c'est ce qui la rend utilisable par quelqu'un qui ne va pas bien.
    #
    #    La puce d'inventaire de l'univers 4 garde « trois questions simples » :
    #    elle disait deja juste, on n'y touche pas.
    #
    # ⚠️ PLACEMENT — ET CE N'EST PAS UN DETAIL DE MISE EN PAGE. Ce bloc est pose
    #    AVANT `<div class="guilde">`, jamais entre lui et `<div class="aussi">` :
    #    `_controle_guilde_encart()` delimite l'encart de la Guilde par CES DEUX
    #    BORNES-LA. Un bloc glisse entre elles tomberait sous le vocabulaire
    #    proscrit de la Guilde et ferait echouer l'ecriture pour une raison
    #    incomprehensible. Ordre retenu : univers 4 · « J'ai besoin d'aide » ·
    #    « On veille les uns sur les autres » · l'encart de la Guilde · « Et
    #    aussi » — de l'appel personnel au groupe, du groupe au pacte.
    A("""
  <div class="aide">
    <span class="ic-w">""" + _ic('bouee') + """</span>
    <div>
      <p class="u-num">« J’ai besoin d’aide » — demander, simplement</p>
      <p class="aide-claim">Demander de l’aide devient un geste simple, pas un aveu.</p>
      <p class="aide-p">Un bouton, dans l’application, ouvre un questionnaire très court — des réponses
        simples — pour cerner le besoin sans jamais juger. <b>3 questions, c’est tout :</b></p>
      <ol class="aide-l">
        <li><b>Qu’est-ce qui se passe ?</b> — ton prochain pas, un retard d’heures, un blocage
          administratif, ou un doute plus perso sur ta valeur.</li>
        <li><b>Tu veux que quelqu’un le sache ?</b> — ton groupe, ta structure, une personne
          précise… ou personne du tout, et c’est une réponse pleine et entière : l’application
          répond alors « c’était pour toi, prends soin de toi », et n’envoie rien.</li>
        <li><b>C’est urgent ?</b> — ça peut attendre, c’est pour cette semaine, ou c’est là,
          maintenant.</li>
      </ol>
      <p class="aide-p">Selon les réponses, l’application donne immédiatement un premier geste concret —
        pas une brochure, une action. Et si on le souhaite, elle prévient le groupe, la structure, ou une
        personne précise : c’est l’artiste seul qui choisit qui, et quoi. On peut donc demander de l’aide
        sans que ça devienne social.</p>
    </div>
  </div>
""")

    # MAQUETTE 9 (`MAQ_AIDE`) — le parcours, colle au bloc qui le decrit.
    #   ⚠️ Le bloc ci-dessus liste les TROIS QUESTIONS ; la maquette montre la
    #   QUESTION 1 ET SES QUATRE REPONSES. C'est ce qui leve, en image, la
    #   confusion 3/4 de la page de reference (voir la note de `MAQ_AIDE`). Ne
    #   pas ramener la maquette a trois options « pour la coherence » : les
    #   quatre lignes ne sont pas des questions.
    A(MAQ_AIDE)

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
    # ===================================================================
    # « ON VEILLE LES UNS SUR LES AUTRES » — ABSORBE LE 16/08/2026
    # ===================================================================
    # SOURCE (LECTURE SEULE, jamais editee) : la section du meme nom de
    # `/Users/davidlesage/CLAUDE/GUSO FACILE/presentation.html`. Son auteur l'a
    # lui-meme designee comme l'un des trois passages superieurs de sa page :
    # elle INCARNE au lieu d'enumerer, et c'est ce qui fait comprendre l'outil
    # en trente secondes.
    #
    # ⚠️ ON N'EN GARDE QU'UN TIERS, ET C'EST LE POINT IMPORTANT. Elle aligne
    #    trois cas ; DEUX SONT DES DOUBLONS DE CETTE PAGE :
    #      - « La structure qui accompagne » redit le cas de Sophie, la maquette
    #        6 « Mes artistes » ET la puce « Points de vigilance cote structure »
    #        (« (a venir) » jusqu'au 17/08/2026, au present depuis — les trois
    #        disent maintenant la meme chose au meme temps). Non repris.
    #      - « L'artiste seul face a l'admin » redit le paragraphe de #promesse,
    #        la maquette 2 et l'etape 3 — non repris.
    #      - « LE GROUPE » est le seul cas absent d'ici : la vue groupe n'etait
    #        qu'une puce d'inventaire, jamais incarnee. C'est celui-la.
    #    La page ne doit pas GROSSIR de tout ce qu'elle absorbe : elle mesurait
    #    deja 18 383 px a 390 px avant cette passe.
    #
    # ⚠️⚠️ LE PIEGE QUE CE BLOC PORTAIT, ET COMMENT IL EST DESAMORCE.
    #    La section Vercel met en scene une STRUCTURE (« Des Sons et Des
    #    Liens ») et une PERSONNE (« Marius ») INVENTEES SANS LE DIRE. C'est
    #    exactement ce que la correction « Trois situations REELLES » ->
    #    « typiques » a deja coute a cette page, et c'est plus grave encore ici :
    #    une structure nommee peut etre confondue avec une vraie.
    #      1. LA STRUCTURE INVENTEE DISPARAIT avec le cas non repris. On ne
    #         nomme aucune structure, ni vraie ni fausse.
    #      2. LE PRENOM EST GARDE — c'est lui qui incarne — MAIS MARQUE, dans le
    #         meme esprit ET le meme habillage que « Les prenoms sont fictifs » :
    #         une note en gris, juste sous le bloc, qui le dit en toutes lettres
    #         et renvoie explicitement aux trois situations plus haut, pour que
    #         le lecteur comprenne que c'est la meme convention.
    #
    # ⚠️ La cloture de la section Vercel (« A chaque etape, c'est TOI qui decides
    #    ce que tu partages ») N'EST PAS REPRISE : c'est « Confidentialite
    #    graduee », qui est « (a venir) ». L'ecrire au present ferait mentir la
    #    page — et ferait mentir `NB_A_VENIR` avec elle.
    #    ⚠️ REVISE LE 17/08/2026 : « Confidentialite graduee » est livree, cette
    #    phrase ne mentirait plus. ELLE N'EST TOUJOURS PAS REPRISE, pour l'autre
    #    raison — la puce de l'univers 4 le dit deja, et mieux (le filtrage cote
    #    serveur). La reprendre ferait un TROISIEME endroit ou la page redit la
    #    meme chose, sur une page sous plafond de hauteur.
    #
    # PLACEMENT : juste avant l'encart de la Guilde, qu'il introduit. L'ordre de
    # lecture devient : la puce (ce qu'on peut y faire) -> le bloc (a quoi ca
    # ressemble pour de vrai) -> l'encart (pourquoi ca existe).
    A("""
  <div class="veille">
    <p class="u-num">On veille les uns sur les autres</p>
    <p class="veille-claim">Dans un groupe, chacun a sa date anniversaire et son propre compteur — et
      personne ne voit celui des autres.</p>
    <p class="veille-p">Marius joue dans un groupe de cinq. Il a pris du retard sur ses heures sans que
      personne s’en aperçoive, lui compris. La vue groupe montre où en est chaque membre — heures
      validées, dates possibles, jours restants : ses camarades le voient venir avant que ce soit grave,
      et non le jour où ses droits tombent. On lui laisse les prochaines répétitions, on cale deux dates
      de plus. C’est ça, un groupe.</p>
    <p class="veille-note">Le prénom et le groupe sont fictifs, comme dans les trois situations plus
      haut ; la mécanique, elle, est celle de l’outil.</p>
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
"""
      # -------------------------------------------------------------------
      # LA LIGNE « PRISE EN MAIN » — trois fonctionnalites LIVREES (16/08/2026)
      # -------------------------------------------------------------------
      # Les trois phrases sont celles confirmees dans le code par l'auteur de
      # l'app, reprises telles quelles ; seule la ponctuation a ete alignee sur
      # le gabarit des puces (titre en gras, tiret cadratin, puis la phrase).
      #
      # POURQUOI ICI ET PAS DANS UN UNIVERS : elles n'appartiennent a aucun des
      # quatre. Ce n'est ni un droit, ni une tournee, ni une structure, ni un
      # cercle : c'est la vie de l'outil lui-meme. Les forcer dans l'univers 1
      # aurait fausse sa lecture (« Tes droits, maitrises »), et un cinquieme
      # univers aurait casse la grille a deux colonnes ET le compte
      # `class="u-card"` a 4. L'encadre « Et aussi » existe exactement pour ce
      # cas — et il coute quatre lignes de hauteur au lieu d'une carte entiere.
      # Elles sont dans l'ordre de ce que vit un nouveau venu : on est invite,
      # on est accueilli, on cherche comment faire, puis on suit ce qui change.
      # (« Inscription par invitation » les a rejointes pour cette raison-la et
      #  pour une raison de hauteur : voir la note de l'univers 4.)
      """      <p class="aussi-p2"><b>Inscription par invitation</b> — on rejoint la bêta par un lien
        d’invitation : création du compte, choix du mot de passe, et le code reste valable une semaine
        si on passe par sa boîte mail entre-temps. <b>Guide de démarrage</b> — à la première connexion,
        un parcours d’accueil qui explique par où commencer. <b>Guide intégré</b> — un mode d’emploi
        complet dans l’app, section par section, sans jamais avoir à en sortir. <b>Nouveautés</b> —
        chaque évolution de l’app est publiée dans un journal des versions, avec une notification à la
        première ouverture qui suit.</p>
    </div>
  </div>
""")

    # MAQUETTE 10 (`MAQ_NOUVEAUTES`) — le journal des versions, pose juste sous
    #   l'encadre « Et aussi » dont la ligne « prise en main » porte la puce
    #   « Nouveautés ». C'est la derniere fonctionnalite nommee de la section,
    #   et la seule de cette ligne qui ait un ecran a montrer (un guide de
    #   demarrage et un guide integre se raconteraient mal en vignette).
    A(MAQ_NOUVEAUTES)

    A("""</div></section>
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
    # 7. APPEL A L'ACTION — LE FORMULAIRE, SUR PLACE  (fusion du 16/08/2026)
    # =====================================================================
    # ⚠️⚠️ CE BLOC A CHANGE DE NATURE. Jusqu'au 16/08/2026 il portait UN LIEN
    # SORTANT (`target="_blank"` vers guso-facile.vercel.app/presentation.html)
    # et deux mentions qui renvoyaient a une page d'ailleurs. Il porte desormais
    # LE FORMULAIRE LUI-MEME. Motif complet en tete de fichier (« LA FUSION DU
    # 16/08/2026 ») ; en une phrase : au moment precis ou l'on confie son nom,
    # son e-mail et son telephone, on ne doit pas quitter le site d'une
    # association pour un `vercel.app`.
    #
    # CE QUI A ETE SUPPRIME ICI, ET POURQUOI (chaque suppression est un doublon)
    #  - « Le formulaire "Demander un accès" recueille le nom, le prénom,
    #    l'adresse e-mail, le numéro de téléphone et la nature du demandeur —
    #    artiste ou structure. » : le formulaire est SOUS LES YEUX, avec ses
    #    propres libelles. Enumerer ses champs en prose, c'est ecrire deux fois
    #    la meme liste. La phrase qui precede (« on commence par se dire
    #    bonjour ») est GARDEE : elle dit le pourquoi, pas le contenu.
    #  - « Le bouton "Demander un accès" se trouve en haut et en bas de la page
    #    de présentation. » : il n'y a plus de page de presentation. La phrase
    #    serait devenue FAUSSE.
    #  - « Le formulaire d'accès est hébergé par Guso Facile ; … Le formulaire
    #    porte sa propre mention d'information. » : renvoyer a une mention
    #    portee ailleurs n'a plus de sens quand la saisie se fait ICI.
    #
    # LA MENTION SUR LES DONNEES PERSONNELLES RESTE, ET GAGNE EN IMPORTANCE.
    # Elle reprend la mention RGPD de `presentation.html` (usage limite a
    # l'etude de la demande et au recontact, aucun demarchage, aucune revente,
    # aucun partage a des tiers, suppression sur demande) au registre neutre du
    # corps de page, ET elle nomme le RESPONSABLE DE TRAITEMENT :
    # ⚠️ **DAVID LESAGE, createur de l'outil — PAS L'ASSOCIATION**. C'est le
    # point qui gagne le plus a la fusion : la saisie se fait desormais sur le
    # domaine de l'association, et il ne doit y avoir AUCUNE ambiguite sur qui
    # recoit les donnees. C'est la meme prudence que « n'est pas un service de
    # l'association », appliquee la ou elle engage le plus.
    #
    # PAS DE MAQUETTE ICI, C'EST TOUJOURS DELIBERE — et pour une raison encore
    # plus forte qu'avant. Le sixieme emplacement prevu etait « la modale
    # Demander un acces ». Y coller la reproduction d'une fenetre avec des
    # champs MORTS AU CLIC, juste a cote d'un VRAI formulaire, serait la pire
    # confusion possible. `_controle_maquettes()` continue d'exiger zero element
    # focusable dans les six apercus ; le formulaire n'est pas un apercu.
    A("""
<div class="divider"></div>
<section id="acces" class="band"><div class="wrap">
  <div class="acces">
    <p class="kick">Faire connaissance</p>
    <h2 class="sec-title">Reprends la main sur ton administratif</h2>
    <p class="body">Puisque l’accès est limité, il n’y a pas d’inscription immédiate : on commence par
      se dire bonjour. Chaque demande est lue et traitée personnellement, et une réponse est apportée
      par e-mail.</p>
"""
      # -------------------------------------------------------------------
      # LE FORMULAIRE. Ecrit a la main, sans bibliotheque. Points de detail
      # qui ont chacun une raison :
      #  - `novalidate` : la validation du navigateur affiche une bulle qui
      #    disparait, dans la langue du navigateur et non dans celle de la
      #    page, et qu'un lecteur d'ecran n'annonce pas toujours. On valide
      #    donc nous-memes, avec un message ECRIT, ASSOCIE au champ.
      #  - un `<label for=…>` par champ, et l'identifiant correspondant sur le
      #    champ : c'est ce qui rend la case cliquable et ce qui fait annoncer
      #    le libelle a la prise de focus. `_controle_formulaire()` verifie le
      #    couple, un par un.
      #  - ⚠️ 17/08/2026 — LES CHAMPS OBLIGATOIRES SONT DESORMAIS QUATRE :
      #    prenom, nom, e-mail ET TELEPHONE. Demande de David, mot pour mot :
      #    « le prenom et nom sont obligatoires » puis « le tel est aussi
      #    obligatoire ». La note precedente disait l'inverse (« un formulaire
      #    qui exige le telephone perd des gens a l'endroit ou il ne faut pas »)
      #    — elle est REMPLACEE, pas oubliee : l'arbitrage a change parce que
      #    chaque demande est etudiee personnellement et qu'un e-mail seul ne
      #    permet pas de rappeler quelqu'un. Le message reste le seul champ
      #    facultatif du formulaire.
      #  - `aria-describedby` pointe le message d'erreur MEME QUAND IL EST
      #    VIDE : le lier au moment de l'erreur seulement est une source connue
      #    d'annonces manquees.
      #  - le choix artiste / structure est un vrai groupe de boutons radio
      #    dans un `<fieldset>` avec `<legend>` : flechable au clavier, annonce
      #    comme un groupe. La page Vercel employait deux `<button>` avec
      #    `aria-pressed` — cela marche a la souris, beaucoup moins au clavier.
      #
      # ⚠️ 16/08/2026 — TROISIEME OPTION « LES DEUX ». Le choix etait exclusif,
      #    et il ne decrivait donc pas une situation courante : jouer ET etre
      #    responsable de la structure qui edite ses propres feuillets GUSO.
      #    LA VALEUR ENVOYEE EST EXACTEMENT `les_deux`, ET AUCUNE AUTRE. La
      #    contrainte de la base vient d'etre elargie pour accepter les trois
      #    valeurs `artiste` · `structure` · `les_deux` ; toute autre orthographe
      #    (« les-deux », « both », « deux ») serait REJETEE et la personne
      #    verrait un message d'erreur incomprehensible. `_controle_formulaire()`
      #    verifie la chaine exacte et refuse d'ecrire la page sinon.
      #
      # ⚠️ CE QUE CETTE OPTION DIT, ET CE QU'ELLE NE DIT PAS. Elle decrit QUI
      #    EST LA PERSONNE, pas ce que l'outil sait faire. La double casquette
      #    est CODEE MAIS PAS ENCORE DEPLOYEE : rien sur cette page n'affirme
      #    que l'application la gere, et il ne faut rien ecrire de tel tant que
      #    ce n'est pas en ligne. Le libelle et sa phrase d'exemple parlent donc
      #    de la situation de la personne, jamais d'une fonctionnalite.
      #  - le `<fieldset>` porte `aria-describedby` vers la phrase d'exemple :
      #    elle est ainsi annoncee a la prise de focus du groupe, et pas
      #    seulement lue a l'ecran.
      #
      # ⚠️ 17/08/2026 — LES TROIS CHAMPS DE STRUCTURE. Demande de David :
      #    « si la personne veut rentrer en tant que structure, une case lui
      #    demande le nom de sa structure et son type (asso ou autre) et lui
      #    demande si elle a la licence du spectacle ou pas, et c'est
      #    obligatoire. »
      #    Ils apparaissent pour « Structure » ET POUR « LES DEUX » — « les
      #    deux » EST une structure, l'oublier serait le defaut le plus facile
      #    a commettre ici.
      #  - LE PIEGE CLASSIQUE DU CHAMP CONDITIONNEL : rester obligatoire apres
      #    avoir disparu. Le formulaire devient alors impossible a envoyer sans
      #    que rien n'explique pourquoi. C'est `structure()` qui decide, cote
      #    JS, ET DE L'AFFICHAGE ET DE L'EXIGENCE — une seule fonction pour les
      #    deux, il ne peut pas y avoir de desaccord entre elles.
      #  - L'APPARITION N'EST PAS QUE VISUELLE : le bloc porte `hidden` (donc il
      #    sort de l'arbre d'accessibilite ET de l'ordre de tabulation quand il
      #    est replie), et une zone `role="status"` annonce en une phrase ce qui
      #    vient d'apparaitre. Sans elle, quelqu'un qui n'y voit pas coche
      #    « Structure » et n'apprend qu'il reste trois champs qu'au moment ou
      #    l'envoi est refuse.
      #  - `aria-required="true"` est ecrit EN DUR sur les trois : ils ne sont
      #    exposes que lorsqu'ils sont reellement obligatoires, puisque `hidden`
      #    les retire entierement le reste du temps.
      #  - PAS DE `tabindex` : l'ordre de tabulation est celui du document, et
      #    le bloc est place JUSTE APRES le choix qui le fait apparaitre.
      #    (Une ancre a zero occurrence interdit `tabindex` sur toute la page.)
      #
      # ⚠️ LA LICENCE — LA FORMULATION EST LE POINT SENSIBLE DE CE BLOC.
      #    ⚠️ 17/08/2026 — ELLE EST POSEE COMME UNE DECLARATION, PAS COMME UN
      #    FAIT ETABLI : « Vous declarez disposer de la licence… » et non
      #    « Vous avez la licence ». Ce n'est pas une precaution de style :
      #    cote application, la reponse decide si la structure est enregistree
      #    comme EMPLOYEUR (elle declare les embauches, edite DPAE et feuillets)
      #    ou comme INTERMEDIAIRE (elle contractualise et encaisse, sans
      #    declarer). David DEVRA la verifier avant d'ouvrir la creation de DPAE
      #    a une structure — le formulaire recueille donc un DIRE, et le dit.
      #    ⚠️ Et cela ne change RIEN au ton : court, non bureaucratique, aucun
      #    mot de controle ni de verification a l'ecran. C'est une demande
      #    d'acces, pas un dossier administratif.
      #    C'est la licence d'entrepreneur de spectacles, celle qui autorise a
      #    employer des artistes. REPONDRE « NON » EST UNE SITUATION COURANTE ET
      #    PARFAITEMENT LEGITIME : beaucoup d'associations passent par le GUSO
      #    PRECISEMENT parce qu'elles n'en ont pas. La question est donc posee
      #    au registre neutre, et la phrase qui l'accompagne dit explicitement
      #    que la reponse ne ferme aucune porte. Ne jamais la reecrire en
      #    quelque chose qui se lirait comme un controle de conformite : ce
      #    serait faire fuir exactement les structures que l'outil vise.
      #    Le message d'erreur du groupe le redit (« les deux reponses
      #    conviennent »), parce que c'est LA qu'on hesite.
      #  - Le type n'a que DEUX choix. « Autre » n'est pas suivi d'un champ de
      #    precision : David a demande trois informations, la precision se dit
      #    dans le message, et chaque demande est de toute facon lue une par une.
      """    <form class="dmd" id="demande" novalidate>
      <p class="dmd-t">Demander un accès</p>
      <p class="dmd-s">Le prénom, le nom, l’adresse e-mail et le téléphone sont demandés ; le message reste libre.</p>
      <div class="dmd-grid">
        <div class="f">
          <label for="dmd-prenom">Prénom <span class="opt">— obligatoire</span></label>
          <input type="text" id="dmd-prenom" name="first_name" autocomplete="given-name" required aria-describedby="dmd-prenom-err">
          <span class="f-err" id="dmd-prenom-err"></span>
        </div>
        <div class="f">
          <label for="dmd-nom">Nom <span class="opt">— obligatoire</span></label>
          <input type="text" id="dmd-nom" name="last_name" autocomplete="family-name" required aria-describedby="dmd-nom-err">
          <span class="f-err" id="dmd-nom-err"></span>
        </div>
      </div>
      <div class="f">
        <label for="dmd-email">Adresse e-mail <span class="opt">— obligatoire</span></label>
        <input type="email" id="dmd-email" name="email" autocomplete="email" inputmode="email" required aria-describedby="dmd-email-err">
        <span class="f-err" id="dmd-email-err"></span>
      </div>
      <div class="f">
        <label for="dmd-tel">Téléphone <span class="opt">— obligatoire</span></label>
        <input type="tel" id="dmd-tel" name="phone" autocomplete="tel" inputmode="tel" required aria-describedby="dmd-tel-err">
        <span class="f-err" id="dmd-tel-err"></span>
      </div>
      <fieldset class="f" aria-describedby="dmd-kind-h">
        <legend>Je suis</legend>
        <div class="dmd-kind">
          <label for="dmd-artiste"><input type="radio" id="dmd-artiste" name="kind" value="artiste" checked>Artiste</label>
          <label for="dmd-structure"><input type="radio" id="dmd-structure" name="kind" value="structure">Structure</label>
          <label for="dmd-les-deux"><input type="radio" id="dmd-les-deux" name="kind" value="les_deux">Les deux</label>
        </div>
        <p class="dmd-kind-h" id="dmd-kind-h"><b>Les deux</b> — je suis artiste <b>et</b> responsable d’une structure.
          Par exemple : tu joues, et tu es aussi responsable de l’association qui édite les feuillets GUSO.</p>
        <p class="dmd-avis" id="dmd-struct-avis" role="status" aria-live="polite"></p>
      </fieldset>
      <div class="dmd-struct" id="dmd-struct" hidden>
        <p class="dmd-struct-t">Ma structure</p>
        <div class="f">
          <label for="dmd-struct-nom">Nom de la structure <span class="opt">— obligatoire</span></label>
          <input type="text" id="dmd-struct-nom" name="struct_nom" autocomplete="organization" aria-required="true" aria-describedby="dmd-struct-nom-err">
          <span class="f-err" id="dmd-struct-nom-err"></span>
        </div>
        <fieldset class="f" id="dmd-struct-type" role="radiogroup" aria-required="true" aria-describedby="dmd-struct-type-err">
          <legend>Type de structure <span class="opt">— obligatoire</span></legend>
          <div class="dmd-kind">
            <label for="dmd-type-asso"><input type="radio" id="dmd-type-asso" name="struct_type" value="association">Association loi 1901</label>
            <label for="dmd-type-autre"><input type="radio" id="dmd-type-autre" name="struct_type" value="autre">Autre</label>
          </div>
          <span class="f-err" id="dmd-struct-type-err"></span>
        </fieldset>
        <fieldset class="f" id="dmd-struct-licence" role="radiogroup" aria-required="true" aria-describedby="dmd-lic-h dmd-struct-licence-err">
          <legend>Vous déclarez disposer de la licence d’entrepreneur de spectacles <span class="opt">— obligatoire</span></legend>
          <div class="dmd-kind">
            <label for="dmd-lic-oui"><input type="radio" id="dmd-lic-oui" name="struct_licence" value="oui">Oui</label>
            <label for="dmd-lic-non"><input type="radio" id="dmd-lic-non" name="struct_licence" value="non">Non</label>
          </div>
          <p class="dmd-kind-h" id="dmd-lic-h">C’est la licence qui autorise à employer des artistes. Répondre « non » ne
            change rien à la demande : beaucoup de structures n’en ont pas, et c’est justement pour cela qu’elles
            emploient au GUSO.</p>
          <span class="f-err" id="dmd-struct-licence-err"></span>
        </fieldset>
      </div>
      <div class="f">
        <label for="dmd-message">Message <span class="opt">— facultatif</span></label>
        <textarea id="dmd-message" name="message" rows="3"></textarea>
      </div>
      <div class="dmd-go">
        <button class="btn" type="submit" id="dmd-envoi">Envoyer ma demande""" + _ic('fleche') + """</button>
      </div>
      <p class="dmd-etat" id="dmd-etat" role="status" aria-live="polite"></p>
    </form>
    <p class="mention">Aucune inscription automatique : chaque demande est étudiée personnellement, et
      la réponse arrive par e-mail.</p>
"""
      # -------------------------------------------------------------------
      # LA MENTION SUR LES DONNEES PERSONNELLES — a lire avant d'y toucher.
      # Elle nomme le RESPONSABLE DE TRAITEMENT, et ce n'est PAS l'association :
      # c'est David Lesage. La phrase « ce n'est pas l'association qui les
      # reçoit » est ecrite en toutes lettres et non sous-entendue, parce que la
      # saisie se fait desormais sur le domaine de l'association et que rien,
      # a l'ecran, ne le dirait autrement. Meme prudence que l'encadre
      # « Guso Facile n'est pas un service de l'association ».
      # ⚠️ 17/08/2026 — ELLE ENUMERE LES DONNEES TRANSMISES : les trois champs de
      # structure devaient donc y entrer, sans quoi la mention serait devenue
      # FAUSSE le jour meme ou le formulaire s'est enrichi. Le responsable de
      # traitement ne change pas : David Lesage, pas l'association.
      """    <p class="mention">Vos données : le prénom, le nom, l’adresse e-mail, le téléphone, le
      message et, pour une structure, son nom, son type et la licence d’entrepreneur de spectacles
      qu’elle déclare sont
      transmis à <b>David Lesage</b>, créateur de Guso Facile, qui en est le responsable —
      ce n’est pas l’association qui les reçoit. Ils servent uniquement à étudier votre demande et à
      vous recontacter à ce sujet : aucun démarchage, aucune revente, aucun partage à des tiers. Vous
      pouvez en demander la suppression à tout moment à
      <a href="mailto:contact@lesagedavid.fr">contact@lesagedavid.fr</a>.</p>
  </div>
</div></section>
""")

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
""")
    A(_blog_cta(
        'Le blog de Guso Facile',
        'Toutes les situations concrètes sur le blog de Guso Facile',
        'Dix-huit articles qui déroulent en entier ce que ces réponses courtes '
        'ne font qu’effleurer.'))
    A("""</div></section>
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
"""
      # ===================================================================
      # LE SCRIPT DU FORMULAIRE — la SEULE requete vers un tiers de la page
      # ===================================================================
      # ⚠️ ELLE NE PART QU'AU CLIC SUR « ENVOYER ». Rien au chargement : aucun
      # prechargement, aucun `preconnect` vers supabase, aucun ping. Mesure :
      # 0 requete vers supabase.co au chargement (relevee dans l'onglet reseau,
      # pas supposee). C'est l'exception a la regle « aucun appel externe » du
      # site, et elle s'arrete la.
      #
      # ⚠️ LES TROIS PIEGES, ecrits ici parce que c'est ici qu'on les enfreint :
      #   1. AUCUN en-tete `Prefer`. La cle publiable n'a pas le droit de
      #      relire la ligne inseree : demander `return=representation` rend un
      #      401 ALORS QUE L'INSERTION A REUSSI. Sans lui -> 201 propre.
      #   2. AUCUN champ `status` dans le corps. La securite impose
      #      `status='new'` ; le fournir fait echouer la requete (protection
      #      contre l'auto-approbation).
      #   3. LES TROIS CODES SONT RENDUS EN PHRASES, JAMAIS EN CODES. Le 409 en
      #      particulier : « une demande est deja en attente pour cet e-mail »
      #      est une BONNE nouvelle pour la personne — sa demande est arrivee.
      #      Le message doit se lire comme telle, jamais comme une panne. C'est
      #      pourquoi il n'active PAS la classe `ko` (filet corail) mais le
      #      cadre neutre, comme un succes.
      #
      # ⚠️ LES TROIS EN-TETES SONT ECRITS UNE PAR LIGNE, ET CE N'EST PAS
      #    COSMETIQUE : regroupes sur une seule ligne, le nom de l'en-tete
      #    d'identification, le deux-points et la cle forment exactement la
      #    suite que le crochet `pre-commit` traque pour attraper une cle
      #    laissee en clair. Il refuserait la sauvegarde. NE PAS RECOMPACTER.
      #
      # L'e-mail vide est attrape AVANT tout envoi : aucune requete ne part, le
      # focus revient sur le champ, et le message s'affiche a cote de lui.
      #
      # ⚠️ 17/08/2026 — CE QUI A CHANGE, ET POURQUOI CHAQUE DETAIL EST LA :
      #
      #  a) QUATRE CHAMPS OBLIGATOIRES puis, POUR UNE STRUCTURE, TROIS DE PLUS.
      #     La validation ne s'arrete PLUS au premier champ fautif : elle les
      #     parcourt tous, pose un message a cote de CHACUN, puis rend le focus
      #     au PREMIER d'entre eux. S'arreter au premier obligerait la personne
      #     a envoyer autant de fois qu'il manque de champs, en decouvrant les
      #     erreurs une par une — c'est la facon la plus sure de la perdre.
      #     La zone `role="status"` dit qu'il en reste : un lecteur d'ecran
      #     l'annonce, puis le focus enonce le premier champ et son message.
      #
      #  b) `structure()` DECIDE A LA FOIS DE L'AFFICHAGE ET DE L'EXIGENCE. Une
      #     seule fonction pour les deux : c'est ce qui rend IMPOSSIBLE le piege
      #     du champ cache resté obligatoire. Elle est vraie pour `structure`
      #     ET pour `les_deux`.
      #
      #  c) LE TELEPHONE EST VALIDE AVEC TOLERANCE, ET JAMAIS REFORMATE. Les
      #     gens ecrivent leur numero avec des espaces, des points, des tirets,
      #     un indicatif international. Refuser un numero correct parce qu'il
      #     est espace, ou le reecrire sous les doigts pendant la frappe, c'est
      #     perdre quelqu'un a la derniere etape. On ne compte donc QUE les
      #     chiffres (au moins neuf), et on envoie LA CHAINE TELLE QU'ELLE A ETE
      #     SAISIE.
      #
      #  d) ⚠️⚠️ 17/08/2026 — LES TROIS VRAIES COLONNES EXISTENT MAINTENANT.
      #     La session qui developpe l'application les a creees
      #     (`structure_name` text, `structure_type` text, `structure_licence`
      #     BOOLEAN) et demande de NE PLUS DUPLIQUER l'information. Son motif,
      #     mot pour mot : « le doublon aurait fini par diverger ». Donc :
      #       1. les trois valeurs partent EN COLONNES, plus dans `context` ;
      #       2. ⚠️⚠️ `structure_licence` EST UN BOOLEEN — `true` / `false`,
      #          JAMAIS `"oui"`, `"non"` ni `"true"`. MESURE avant d'ecrire ce
      #          code : une chaine y rend « 400 22P02 invalid input syntax for
      #          type boolean », et la personne verrait une panne
      #          incomprehensible a la derniere etape. La conversion se fait a
      #          UN SEUL endroit, `(sLic === 'oui')` ;
      #       3. la ligne « — Structure : … » ajoutee a la fin de `message`
      #          EST RETIREE : `message` redevient uniquement le message de la
      #          personne. Une ancre a ZERO interdit son retour ;
      #       4. `context` garde `{origin, ts}` et recoit `ua` — l'auteur de
      #          l'app s'en sert pour tracer d'ou viennent les demandes. Les
      #          trois cles de structure en sortent : elles ont leurs colonnes ;
      #       5. LES TROIS COLONNES NE PARTENT QUE POUR UNE STRUCTURE. Pour un
      #          artiste seul, elles ne sont pas envoyees DU TOUT — ni chaine
      #          vide, ni `null`. C'est pour cela que le corps est construit
      #          dans une variable `corps` avant l'envoi : un litteral ne sait
      #          pas omettre une cle.
      #     ⚠️ CE QUI N'A PAS CHANGE : toute colonne INCONNUE fait toujours
      #     echouer la requete, et `_controle_formulaire()` continue de comparer
      #     les cles envoyees a `COLONNES_DEMANDE`, une par une.
      """
<script>
(function(){
  var f = document.getElementById('demande');
  if (!f) return;
  var CIBLE = 'URL_DEMANDE';
  var CLE   = 'CLE_PUBLIABLE';
  var etat  = document.getElementById('dmd-etat');
  var envoi = document.getElementById('dmd-envoi');
  var bloc  = document.getElementById('dmd-struct');
  var avis  = document.getElementById('dmd-struct-avis');
  var enCours = false;
  var premier = null;
  var FORME = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/;
  var CHAMPS  = ['dmd-prenom', 'dmd-nom', 'dmd-email', 'dmd-tel', 'dmd-struct-nom'];
  var GROUPES = [['dmd-struct-type', 'struct_type'], ['dmd-struct-licence', 'struct_licence']];

  function el(id){ return document.getElementById(id); }
  function valeur(id){ var e = el(id); return e ? e.value.trim() : ''; }
  function coche(nom){ var g = f.elements[nom]; return (g && g.value) ? g.value : ''; }
  function dire(texte, souci){
    etat.textContent = texte;
    etat.className = souci ? 'dmd-etat ko' : 'dmd-etat';
  }
  function signaler(id, message, focus){
    var e = el(id);
    if (e) e.setAttribute('aria-invalid', 'true');
    var b = el(id + '-err');
    if (b) b.textContent = message;
    if (!premier) premier = el(focus || id);
  }
  function effacer(id){
    var e = el(id);
    if (e) e.removeAttribute('aria-invalid');
    var b = el(id + '-err');
    if (b) b.textContent = '';
  }
  function effacerTout(){
    var i;
    for (i = 0; i < CHAMPS.length; i++) effacer(CHAMPS[i]);
    for (i = 0; i < GROUPES.length; i++) effacer(GROUPES[i][0]);
  }

  for (var a = 0; a < CHAMPS.length; a++) {
    (function(id){
      var e = el(id);
      if (e) e.addEventListener('input', function(){ effacer(id); });
    })(CHAMPS[a]);
  }
  for (var b2 = 0; b2 < GROUPES.length; b2++) {
    (function(id, nom){
      var g = f.elements[nom];
      if (!g) return;
      for (var k = 0; k < g.length; k++) g[k].addEventListener('change', function(){ effacer(id); });
    })(GROUPES[b2][0], GROUPES[b2][1]);
  }

  /* « Les deux » EST une structure : les trois champs valent pour les deux
     valeurs. Cette fonction commande a la fois l'affichage du bloc et son
     caractere obligatoire — il ne peut donc pas y avoir de desaccord entre
     ce qu'on voit et ce qu'on exige. */
  function structure(){
    var v = f.elements.kind.value;
    return v === 'structure' || v === 'les_deux';
  }
  function basculer(){
    var on = structure();
    bloc.hidden = !on;
    avis.textContent = on
      ? 'Trois informations sur la structure viennent d’apparaître ci-dessous : son nom, son type et sa licence d’entrepreneur de spectacles.'
      : '';
    if (!on) {
      effacer('dmd-struct-nom');
      effacer('dmd-struct-type');
      effacer('dmd-struct-licence');
    }
  }
  var choix = f.elements.kind;
  for (var c = 0; c < choix.length; c++) choix[c].addEventListener('change', basculer);
  basculer();

  f.addEventListener('submit', function(ev){
    ev.preventDefault();
    if (enCours) return;
    effacerTout();
    dire('');
    premier = null;

    var prenom = valeur('dmd-prenom');
    if (!prenom) signaler('dmd-prenom', 'Merci d’indiquer un prénom.');
    var nom = valeur('dmd-nom');
    if (!nom) signaler('dmd-nom', 'Merci d’indiquer un nom.');

    var email = valeur('dmd-email');
    if (!email) signaler('dmd-email', 'Merci d’indiquer une adresse e-mail : c’est par là que la réponse arrivera.');
    else if (!FORME.test(email)) signaler('dmd-email', 'Cette adresse e-mail ne semble pas valide.');

    /* tolerance assumee : on compte les chiffres, on ne juge pas la mise en
       forme, et on n'y touche pas. */
    var tel = valeur('dmd-tel');
    var nb = (tel.match(/[0-9]/g) || []).length;
    if (!tel) signaler('dmd-tel', 'Merci d’indiquer un numéro de téléphone.');
    else if (nb < 9) signaler('dmd-tel', 'Ce numéro semble incomplet : il faut au moins neuf chiffres. Les espaces, les points et les tirets sont acceptés, l’indicatif international aussi.');

    /* trois boutons radio de meme nom : `.value` rend celui qui est coche.
       Les seules valeurs possibles sont `artiste`, `structure` et `les_deux` —
       ce sont celles que la base accepte, il n'y en a pas d'autre. */
    var nature = f.elements.kind.value || 'artiste';
    var sNom = '', sType = '', sLic = '';
    if (structure()) {
      sNom = valeur('dmd-struct-nom');
      if (!sNom) signaler('dmd-struct-nom', 'Merci d’indiquer le nom de la structure.');
      sType = coche('struct_type');
      if (!sType) signaler('dmd-struct-type', 'Merci d’indiquer le type de la structure.', 'dmd-type-asso');
      sLic = coche('struct_licence');
      if (!sLic) signaler('dmd-struct-licence', 'Merci de répondre à cette question : les deux réponses conviennent, aucune ne ferme la porte.', 'dmd-lic-oui');
    }

    if (premier) {
      dire('Il reste des informations à compléter : elles sont indiquées champ par champ dans le formulaire.', true);
      if (premier.focus) premier.focus();
      return;
    }

    var mot = valeur('dmd-message');
    var ctx = { origin: location.href, ts: new Date().toISOString(), ua: navigator.userAgent };

    var corps = {
      email: email,
      first_name: prenom,
      last_name: nom,
      phone: tel,
      kind: nature,
      message: mot || null,
      context: ctx
    };
    /* Les trois colonnes de structure NE PARTENT QUE pour une structure : pour
       un artiste seul, le corps ne les porte pas du tout — ni chaine vide, ni
       null.
       ⚠️ `structure_licence` est une colonne BOOLEENNE : on envoie true ou
       false, jamais « oui » / « non » (une chaine y fait echouer la requete, et
       la personne verrait une panne incomprehensible). La conversion se fait
       ici, a un seul endroit. */
    if (structure()) {
      corps.structure_name = sNom;
      corps.structure_type = sType;
      corps.structure_licence = (sLic === 'oui');
    }

    enCours = true;
    envoi.disabled = true;
    dire('Envoi en cours…');

    fetch(CIBLE, {
      method: 'POST',
      headers: {
        'apikey': CLE,
        'Authorization': 'Bearer ' + CLE,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(corps)
    }).then(function(rep){
      if (rep.status === 201 || rep.status === 200 || rep.status === 204) {
        f.reset();
        basculer();
        effacerTout();
        dire('C’est envoyé. Votre demande est bien arrivée : David la lit personnellement et vous répond par e-mail. Pensez à regarder vos courriers indésirables le moment venu.');
        return;
      }
      if (rep.status === 409) {
        dire('Une demande est déjà en attente pour cette adresse e-mail : elle est bien arrivée, il n’y a rien à refaire. David la traite et vous répond par e-mail.');
        return;
      }
      if (rep.status === 401 || rep.status === 403) {
        premier = null;
        signaler('dmd-email', 'Cette adresse e-mail n’a pas été acceptée. Vérifiez-la, puis réessayez.');
        dire('La demande n’a pas pu être enregistrée : vérifiez l’adresse e-mail, puis réessayez.', true);
        if (premier && premier.focus) premier.focus();
        return;
      }
      dire('L’envoi n’a pas abouti. Réessayez dans un instant, ou écrivez directement à contact@lesagedavid.fr.', true);
    }).catch(function(){
      dire('Le serveur n’a pas pu être joint. Vérifiez votre connexion et réessayez — votre saisie est conservée.', true);
    }).then(function(){
      enCours = false;
      envoi.disabled = false;
    });
  });
})();
</script>
""".replace('URL_DEMANDE', URL_DEMANDE).replace('CLE_PUBLIABLE', CLE_PUBLIABLE))
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
#: Historique : 6 le 14/08/2026 ; 10 la nuit du 16/08/2026 — David : « ça manque
#: encore beaucoup de visuel pour illustrer les fonctions, visualiser une carte
#: de tournée etc. » Mesure d'alors : ~12 800 px de page pour six apercus, soit
#: un visuel tous les 2 100 px. Les quatre nouveaux sont le selecteur « Je
#: regarde », la carte de tournee, « J'ai besoin d'aide » et le journal des
#: nouveautes — chacun COLLE a la fonction qu'il illustre, jamais en galerie.
NB_MAQUETTES = 10

#: nombre de mentions « (a venir) » attendues dans la page. IL EST LE COMPTE
#: RENDU DE L'ETAT REEL DE L'APPLICATION, pas un reglage cosmetique — chaque
#: unite doit correspondre a une fonctionnalite qu'un beta-testeur constate
#: absente. Historique : 5 au 15/08/2026 ; 3 le 16/08/2026 (ecrans de la Guilde
#: et de « Je cree mon contrat » deployes) ; **0 depuis le 17/08/2026**.
#: CE QUI A LEVE LES TROIS DERNIERS, verifie en production dans le bundle servi
#: par `https://guso-facile.vercel.app/index.html`, pas sur parole :
#:   1. « Points de vigilance cote structure » (univers 4) — `sdCardHtml`, les
#:      cartes d'artistes et leur niveau d'alerte ;
#:   2. « Confidentialite graduee » (univers 4) — `affSetVisibility`,
#:      `affSetManage`, les trois libelles de partage, et le niveau stocke comme
#:      DONNEE (`visibility:'full'`), donc filtre a la source et pas a
#:      l'affichage ;
#:   3. la note de la maquette 6 « Mes artistes » — c'est le meme ecran que le
#:      point 1 (voir le commentaire de `MAQ_STRUCTURE`).
#: ⚠️ ZERO N'EST PAS LA FIN DU MECANISME — IL RESSERVIRA. Une fonctionnalite
#: annoncee mais non livree se reecrit au FUTUR avec « (a venir) », et ce nombre
#: remonte avec elle : c'est la regle de la page, appliquee dans les DEUX sens
#: depuis le 16/08/2026. A ce jour UNE SEULE chose est volontairement non faite
#: cote application — l'ecran permettant a une STRUCTURE de saisir une date dans
#: l'espace d'un artiste (le droit existe en base, l'artiste peut le donner,
#: l'interface non ; c'est le geste le plus delicat de l'app, David doit
#: l'arbitrer). La page N'EN PARLE PAS, et ne doit pas commencer : on n'annonce
#: pas plus qu'on ne promet. Idem pour le journal des modifications et
#: l'annuaire des structures, en construction.
#: Baisser ce nombre sans qu'un ecran soit reellement livre, c'est promettre.
#: Le monter sans motif, c'est deprecier un outil qui marche.
NB_A_VENIR = 0

#: nombre de mentions « (a venir) » posees SOUS une maquette (argument `note=`
#: de `_figure()`). Elles comptent dans `NB_A_VENIR` mais ne sont PAS des puces
#: d'inventaire, d'ou cette soustraction. 1 du 16 au 16/08/2026 (l'apercu « Mes
#: artistes ») ; 0 depuis que cette vue est deployee.
NB_NOTES_A_VENIR = 0

#: nombre de puces « a venir » de l'inventaire : le total, moins les notes de
#: maquette qui n'en sont pas. Vaut 0 depuis le 17/08/2026.
#: ⚠️ ECRIT COMME UNE SOUSTRACTION, ET PAS FIGE : c'etait `NB_A_VENIR - 1`, ce
#: qui donnait -1 le jour ou le total est tombe a zero — un nombre attendu
#: negatif, donc une ancre impossible a satisfaire. Le « 1 » en dur etait la
#: note de la maquette 6 ; il porte desormais son nom.
NB_PUCES_A_VENIR = NB_A_VENIR - NB_NOTES_A_VENIR

#: (marqueur, nombre attendu, ce que c'est)
ANCRES = (
    ('<h1', 1, 'titre principal de la page'),
    # version lue dans nav_menu : ce garde-fou ne doit pas devenir faux le jour
    # ou NAV_VERSION est incrementee.
    ('data-nav="%s"' % nav_menu.NAV_VERSION, 1, 'menu partage nav_menu.py'),
    ('href="/guso-facile"', 1, 'entree « Guso Facile » du menu partage'),
    ('id="acces"', 1, 'section « Reprends la main sur ton administratif »'),
    # --- LA FUSION DU 16/08/2026 : le formulaire vit ICI ------------------
    # ⚠️ Les DEUX ancres a ZERO sont les plus importantes de ce tableau. Le
    # bouton « Demander un accès » envoyait la personne sur un autre domaine au
    # moment precis ou elle allait confier son nom, son e-mail et son telephone.
    # Ces deux lignes interdisent qu'un lien vers l'ancienne page revienne par
    # reflexe — y compris dans un commentaire, un `href` ou une mention de
    # texte. La page Vercel reste en ligne pour l'instant (sa redirection sera
    # posee par sa session APRES verification que rien ne manque ici) : on ne
    # pointe plus vers elle, mais on ne casse rien.
    ('presentation.html', 0, 'aucun lien vers l’ancienne page de présentation'),
    ('guso-facile.vercel.app', 0, 'aucun renvoi vers l’ancien domaine'),
    ('<form class="dmd"', 1, 'le formulaire de demande d’accès, sur place'),
    (URL_DEMANDE, 1, 'la destination de la demande (une seule sur la page)'),
    ('Prefer', 0, 'l’en-tête « Prefer » ferait rendre un 401 sur une insertion RÉUSSIE'),
    # Les six champs de saisie, un par un. Ce compte est le contrat du
    # formulaire : si l'un disparait, la demande part incomplete en silence.
    ('id="dmd-prenom"', 1, 'champ Prénom'),
    ('id="dmd-nom"', 1, 'champ Nom'),
    ('id="dmd-email"', 1, 'champ Adresse e-mail (le seul obligatoire)'),
    ('id="dmd-tel"', 1, 'champ Téléphone'),
    ('id="dmd-message"', 1, 'champ Message'),
    ('name="kind"', 3, 'le choix artiste / structure / les deux (trois radio)'),
    # ⚠️ LES TROIS VALEURS EXACTES ATTENDUES PAR LA BASE, une par une. La
    #    contrainte n'accepte que `artiste`, `structure` et `les_deux` : une
    #    faute de frappe ferait rejeter la demande et la personne verrait une
    #    erreur incomprehensible, sans que rien ne l'annonce ici. On verifie
    #    donc la chaine, pas seulement le nombre de boutons.
    ('value="artiste"', 1, 'la valeur envoyee pour « Artiste »'),
    ('value="structure"', 1, 'la valeur envoyee pour « Structure »'),
    ('value="les_deux"', 1, 'la valeur envoyee pour « Les deux » (jamais autre chose)'),
    ('id="dmd-kind-h"', 1, 'la phrase d’exemple de « Les deux »'),
    ('aria-describedby="dmd-kind-h"', 1,
     'le lien qui rattache cette phrase au groupe de boutons'),
    # DEUX zones d'annonce depuis le 17/08/2026 : l'etat de l'envoi, et
    # l'apparition des champs de structure. Sans la seconde, quelqu'un qui n'y
    # voit pas coche « Structure » et n'apprend qu'il reste trois champs qu'au
    # moment ou l'envoi est refuse.
    ('aria-live="polite"', 2,
     'les deux annonces : l’état de l’envoi, et l’apparition des champs de structure'),
    ('id="dmd-email-err"', 1, 'le message d’erreur de l’e-mail'),
    ('aria-describedby="dmd-email-err"', 1,
     'le lien qui rattache ce message au champ e-mail'),
    # --- LES QUATRE CHAMPS OBLIGATOIRES (17/08/2026) ----------------------
    # Chacun a son message d'erreur ECRIT et RATTACHE, exactement comme
    # l'e-mail. Une erreur flottante en bas de page n'est jamais annoncee au
    # bon moment ; c'est le couple `aria-describedby` + boite `.f-err` qui la
    # rattache. Si l'un des quatre couples saute, la page n'est pas ecrite.
    ('id="dmd-prenom-err"', 1, 'le message d’erreur du prénom'),
    ('aria-describedby="dmd-prenom-err"', 1, 'ce message est rattaché au champ Prénom'),
    ('id="dmd-nom-err"', 1, 'le message d’erreur du nom'),
    ('aria-describedby="dmd-nom-err"', 1, 'ce message est rattaché au champ Nom'),
    ('id="dmd-tel-err"', 1, 'le message d’erreur du téléphone'),
    ('aria-describedby="dmd-tel-err"', 1, 'ce message est rattaché au champ Téléphone'),
    # --- LES TROIS CHAMPS DE STRUCTURE (17/08/2026) -----------------------
    # ⚠️ `hidden` fait partie de l'ancre : le bloc doit partir REPLIE. Livre
    #    ouvert, il demanderait a un artiste seul trois informations qui ne le
    #    concernent pas — et les exigerait.
    ('id="dmd-struct" hidden', 1,
     'le bloc des champs de structure, replié au chargement'),
    ('id="dmd-struct-avis"', 1, 'la zone qui annonce l’apparition de ces champs'),
    ('id="dmd-struct-nom"', 1, 'champ Nom de la structure'),
    ('id="dmd-struct-nom-err"', 1, 'son message d’erreur'),
    ('id="dmd-struct-type"', 1, 'le groupe Type de structure'),
    ('id="dmd-struct-type-err"', 1, 'son message d’erreur'),
    ('id="dmd-struct-licence"', 1, 'le groupe Licence d’entrepreneur de spectacles'),
    ('id="dmd-struct-licence-err"', 1, 'son message d’erreur'),
    ('id="dmd-lic-h"', 1, 'la phrase qui dit que « non » ne ferme aucune porte'),
    # ⚠️ 17/08/2026 — LA QUESTION EST UNE DECLARATION, PAS UN CONSTAT. Côté
    #    application, la réponse décide si la structure est enregistrée comme
    #    EMPLOYEUR ou comme INTERMÉDIAIRE, et David devra la vérifier avant
    #    d'ouvrir la création de DPAE : le formulaire recueille un DIRE, et le
    #    dit. « Vous avez la licence » présenterait la même réponse comme un
    #    fait établi.
    ('Vous déclarez disposer de la licence d’entrepreneur de spectacles', 1,
     'la licence est demandée comme une déclaration, jamais comme un fait établi'),
    # ⚠️ LA PHRASE QUI DESAMORCE, MOT POUR MOT. C'est ELLE qui empêche la
    #    question de se lire comme un contrôle de conformité — et c'est
    #    exactement là qu'une structure sans licence hésite à continuer.
    # (fragment tenant sur UNE ligne du gabarit : une ancre a cheval sur deux
    #  lignes casserait au premier reformatage, pour rien.)
    ('change rien à la demande : beaucoup de structures n’en ont pas', 1,
     'la phrase qui désamorce la question de la licence — « répondre non ne change rien »'),
    # ⚠️ LES QUATRE VALEURS EXACTES, une par une — meme raison que pour `kind` :
    #    ce sont elles qui partent dans `context` et dans la ligne ajoutee au
    #    message. Une faute de frappe passerait inapercue jusqu'a la lecture de
    #    la demande, ou plus personne ne saurait ce que valait la reponse.
    ('value="association"', 1, 'la valeur envoyée pour « Association loi 1901 »'),
    ('value="autre"', 1, 'la valeur envoyée pour « Autre »'),
    ('value="oui"', 1, 'la valeur envoyée pour la licence — oui'),
    ('value="non"', 1, 'la valeur envoyée pour la licence — non'),
    ('name="struct_nom"', 1, 'le nom du champ Nom de la structure'),
    ('name="struct_type"', 2, 'les deux boutons du groupe Type'),
    ('name="struct_licence"', 2, 'les deux boutons du groupe Licence'),
    ('aria-required="true"', 3,
     'les trois champs de structure sont annoncés obligatoires'),
    ('role="radiogroup"', 2, 'les deux groupes de boutons de la structure'),
    # --- 17/08/2026 : LES TROIS VRAIES COLONNES ---------------------------
    # ⚠️⚠️ LA LIGNE LA PLUS IMPORTANTE DE CE GROUPE EST CELLE DU BOOLEEN.
    #    `structure_licence` est une colonne BOOLEAN : envoyer la chaine « oui »
    #    rend « 400 22P02 invalid input syntax for type boolean » — mesure, pas
    #    suppose. La conversion doit rester ECRITE ICI, a un seul endroit ; si
    #    quelqu'un remet `= sLic`, cette ancre le refuse a l'ecriture.
    ('corps.structure_name = sNom;', 1,
     'le nom de la structure part en COLONNE (plus dans `context`)'),
    ('corps.structure_type = sType;', 1,
     'le type de la structure part en COLONNE (plus dans `context`)'),
    ("corps.structure_licence = (sLic === 'oui');", 1,
     'la licence part en BOOLÉEN — jamais « oui » / « non », qui font échouer '
     'la requête en 400'),
    # ⚠️ LES DEUX ANCRES A ZERO interdisent le retour des anciennes cles de
    #    `context` : l'information vit desormais dans ses colonnes, et la
    #    dupliquer est exactement ce que l'auteur de l'application a demande
    #    d'arreter — « le doublon aurait fini par diverger ».
    ('structure_nom', 0,
     'l’ancienne clé de `context` — la colonne s’appelle `structure_name`'),
    ('structure_licence_spectacles', 0,
     'l’ancienne clé de `context` — la colonne s’appelle `structure_licence`'),
    # ⚠️ LA LIGNE LISIBLE AJOUTEE A LA FIN DE `message` EST RETIREE (17/08/2026).
    # `message` redevient UNIQUEMENT le message de la personne. Motif donne par
    # l'auteur de l'application : « le doublon aurait fini par diverger ». Cette
    # ancre a zero empeche qu'elle revienne par reflexe le jour ou quelqu'un se
    # demandera « mais comment David voit-il le nom de la structure ? » — la
    # reponse est : dans sa colonne.
    ('— Structure : «', 0,
     'la ligne lisible ajoutée au message, retirée le 17/08/2026 (plus de doublon)'),
    # La mention sur les donnees personnelles NOMME le responsable de
    # traitement, et ce n'est pas l'association. Voir le commentaire au-dessus
    # du bloc : c'est le point qui gagne le plus a la fusion.
    ('créateur de Guso Facile, qui en est le responsable', 1,
     'la mention RGPD nomme David Lesage responsable de traitement'),
    ('ce n’est pas l’association qui les reçoit', 1,
     'la mention RGPD écarte explicitement l’association'),
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
    # ⚠️ 17/08/2026 — les deux DERNIERES puces « a venir » de la page passent au
    # present, sur verification en production. Memes ancres que les deux
    # ci-dessus, et pour la meme raison : elles pinglent la puce ENTIERE (`<li>`
    # nu, pas `<li class="soon">`, et aucun `<i>(à venir)</i>` derriere le
    # `<b>`), ce qui empeche qu'on les remette « au futur » par prudence
    # reflexe.
    ('<li><b>Points de vigilance côté structure</b> —', 1,
     'points de vigilance — fonctionnalité LIVRÉE, au présent (écran déployé)'),
    ('<li><b>Confidentialité graduée</b> —', 1,
     'confidentialité graduée — fonctionnalité LIVRÉE, au présent (écran déployé)'),
    # ⚠️ LA PHRASE QUI PORTE TOUT LE POIDS DE LA PROMESSE, MOT POUR MOT. Sans
    #    elle, « confidentialité graduée » ne dit rien de plus qu'un masquage
    #    d'affichage — la structure recevrait les donnees et se contenterait de
    #    ne pas les montrer. C'est exactement la phrase que raccourcirait un
    #    menage de longueur, et c'est celle qu'il ne faut pas toucher.
    # (fragment tenant sur UNE ligne du gabarit : une ancre a cheval sur deux
    #  lignes casserait au premier reformatage, pour rien.)
    ('Le filtrage est fait côté serveur, pas seulement à l’affichage', 1,
     'le filtrage est fait à la source, pas seulement masqué à l’écran'),
    # Le compte des mentions « (a venir) » : voir NB_A_VENIR juste au-dessus, ou
    # l'etat de chaque fonctionnalite est justifie une par une. Si ce compte
    # baisse, une fonctionnalite non livree vient d'etre presentee comme
    # disponible ; s'il monte, une fonctionnalite livree vient d'etre effacee.
    # Les deux cas sont refuses a l'ecriture.
    # ⚠️ IL VAUT 0 DEPUIS LE 17/08/2026 : plus rien de ce que la page decrit
    #    n'est en attente. L'ancre reste — a zero, elle interdit qu'un « (a
    #    venir) » revienne par prudence reflexe sans que `NB_A_VENIR` soit
    #    remonte en connaissance de cause, avec le motif ecrit a cote.
    ('<i>(à venir)</i>', NB_A_VENIR, 'les mentions « à venir » des fonctionnalités non livrées'),
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
    # --- LA DOUBLE VUE « artistes | structures » (16/08/2026) ------------
    # ⚠️ CES SEPT LIGNES SONT LE CONTRAT DU VIS-A-VIS. Le dispositif ne vaut
    # que s'il est DOUBLE : une colonne sans l'autre, ou un en-tete sans son
    # groupe, et la page redit ce qu'elle disait avant — un inventaire en file.
    # C'est exactement ce que David a signale : « ce qui manque, c'est cette
    # double vue qui montre que l'app sert a la fois les artistes ou les
    # structures ».
    ('class="duo"', 1, 'la double vue artistes | structures'),
    ('class="duo-col"', 2, 'les DEUX colonnes du vis-à-vis, jamais une seule'),
    ('class="duo-ico"', 2, 'le pictogramme de chaque en-tête de colonne'),
    ('id="duo-artistes"', 1, 'le titre de la colonne « Pour les artistes »'),
    ('id="duo-structures"', 1, 'le titre de la colonne « Pour les structures »'),
    # Chaque colonne est un groupe NOMME pour les technologies d'assistance :
    # sans ce lien, un lecteur d'ecran enchaine les deux inventaires sans
    # jamais dire a qui chacun s'adresse — c'est-a-dire sans rien restituer du
    # dispositif visuel.
    ('aria-labelledby="duo-artistes"', 1, 'le groupe « artistes » est nommé'),
    ('aria-labelledby="duo-structures"', 1, 'le groupe « structures » est nommé'),
    ('class="apercus"', 1, 'la rangée des deux aperçus côté artiste'),
    ('class="deux"', 1, 'la bande « et pour les deux » (l’univers 4)'),
    # --- « J'AI BESOIN D'AIDE » (16/08/2026) -----------------------------
    # David : « tu ne parles pas de la fonction j'ai besoin d'aide ». Elle est
    # LIVREE et elle n'existait qu'en puce d'inventaire. Ces trois lignes
    # empechent que le bloc reparte au premier menage de hauteur.
    ('class="aide"', 1, 'le bloc « J’ai besoin d’aide »'),
    ('class="aide-l"', 1, 'la liste des trois questions'),
    # ⚠️ LE NOMBRE ANNONCE ET LE NOMBRE AFFICHE SONT COMPTES ENSEMBLE : c'est
    #    exactement ce qui manquait a la page de reference, qui annoncait
    #    « 3 questions, c'est tout » puis listait quatre lignes. Si l'un des
    #    deux bouge sans l'autre, l'ecriture est refusee.
    ('3 questions, c’est tout', 1, 'le nombre annoncé au-dessus de la liste'),
    ('<li><b>Qu’est-ce qui se passe ?</b>', 1, 'question 1'),
    ('<li><b>Tu veux que quelqu’un le sache ?</b>', 1, 'question 2'),
    ('<li><b>C’est urgent ?</b>', 1, 'question 3'),
    # ⚠️ « personne du tout » n'est PAS un renoncement : voir la note du bloc.
    #    Si cette formulation disparait, la question 2 se relit comme un choix
    #    entre trois destinataires, et la fonction devient un bouton d'alerte.
    ('c’était pour toi, prends soin de toi', 1,
     'la réponse de l’app quand on ne prévient personne'),
    # ⚠️ 2 -> 4 la nuit du 16/08/2026 : l'aperçu du parcours a été posé contre le
    #    bloc, et il nomme la fonction deux fois de plus (son aria-label et le
    #    titre de sa barre). Les quatre emplacements, un par un : la puce de
    #    l'univers 4, le bloc `.aide`, l'aria-label de la maquette, sa barre.
    ('J’ai besoin d’aide', 4,
     'la fonction est nommée QUATRE fois : la puce de l’univers 4, le bloc, '
     'puis l’aria-label et la barre de son aperçu'),
    # Autant de marqueurs creux que de puces « a venir » (0 depuis le
    # 17/08/2026). Ce compte double celui de `<i>(à venir)</i>` moins les notes
    # de maquette : c'est voulu, une puce pleine devant une fonctionnalite non
    # livree la ferait passer pour disponible — et une puce creuse devant une
    # fonctionnalite livree la ferait passer pour absente.
    # ⚠️ LE CSS `.u-card li.soon::before` (la pastille creuse) RESTE en place,
    #    comme `.gf-soon-note` : plus aucune puce ne porte la classe, donc plus
    #    aucun marqueur creux a l'ecran, mais l'habillage attend la prochaine
    #    fonctionnalite annoncee et non livree. C'est le mecanisme, pas un
    #    residu — et cette ancre a zero garantit qu'il ne se rallume pas seul.
    ('<li class="soon">', NB_PUCES_A_VENIR, 'les puces des fonctionnalités non livrées'),
    # ⚠️ CETTE LIGNE VALAIT ZERO JUSQU'AU 16/08/2026 (« aucun champ de saisie
    # dans la page »). Elle a valu SIX quand le formulaire a ete rapatrie, puis
    # SEPT avec la troisieme option « Les deux » du meme jour, et DOUZE depuis
    # le 17/08/2026 : 2 champs texte + e-mail + telephone + 3 boutons radio
    # `kind` + le nom de la structure + 2 boutons `struct_type` + 2 boutons
    # `struct_licence`. TOUS dans le formulaire. `_controle_formulaire()`
    # verifie qu'il n'y en a AUCUN ailleurs — en particulier aucun dans une
    # maquette d'interface, ou un visiteur croirait piloter l'outil depuis le
    # site de l'association.
    ('<input', 12, 'les douze champs de saisie du formulaire, et eux seuls'),
    ('<textarea', 1, 'le champ Message'),
    ('<form', 1, 'un seul formulaire sur la page'),
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
    # --- LA MISE EN VALEUR DU BLOG (16/08/2026) --------------------------
    # Le maillage vers le blog (dossier SEO, §6). ⚠️ `href="/guso-facile"`
    # compte 1 plus haut : la guillemet fermante l'empeche de compter
    # ceux-ci — et elle empeche aussi les trois liens d'ARTICLE de compter
    # ici, puisqu'ils portent un slug avant leur guillemet.
    # TROIS liens vers l'index, un par etage de la page : le hero (premier
    # ecran), le bloc `.mea` (fin de #situations) et la fin de FAQ. C'est le
    # compte qui dit si le probleme mesure le 16/08/2026 est regle — voir
    # l'entete : avant cette passe il valait 2, dont AUCUN dans le premier
    # ecran.
    ('href="/guso-facile/blog"', 3, 'les trois liens descendants vers le blog'),
    ('class="hero-blog"', 1, 'le lien vers le blog dans le premier écran'),
    # --- LE LIEN DE CONNEXION DES BETA-TESTEURS (17/08/2026) --------------
    # David a tranche : les gens qui ont deja un compte doivent pouvoir entrer
    # depuis cette page. Un LIEN, jamais un second bouton — l'ecart n° 8 en tete
    # de fichier tient, il est complete et non annule.
    # ⚠️ CE QUI PROTEGE VRAIMENT CE LIEN N'EST PAS ICI MAIS PLUS HAUT : l'ancre
    #    `guso-facile.vercel.app` a ZERO. Elle interdit qu'un futur passage
    #    « simplifie » ce lien en y collant l'adresse de l'application en dur —
    #    ce qui reviendrait a distribuer aux beta-testeurs une adresse qui
    #    cassera le jour du changement de domaine, precisement ce que
    #    `/guso-facile/app` existe pour eviter.
    ('class="hero-cnx"', 1, 'le lien de connexion, sous le bouton du hero'),
    ('href="/guso-facile/app"', 1,
     'l’adresse stable de connexion (redirigée par vercel.json, une seule fois)'),
    ('J’ai déjà un compte → me connecter', 1,
     'le libellé exact du lien de connexion, validé par David le 17/08/2026'),
    # --- LE SOMMAIRE DE LA PAGE (17/08/2026) -----------------------------
    # ⚠️ LES CINQ LIGNES `href="#…"` SONT LE VRAI GARDE-FOU DE CE BLOC : elles
    #    interdisent qu'un libellé soit un jour repointé sur une ancre qui
    #    n'existe pas — le défaut que ce projet a déjà publié. Elles doublent
    #    `controle_liens()` de verif_site.py, et c'est voulu : ici l'écriture
    #    est REFUSÉE, là-bas elle est seulement signalée après coup.
    # ⚠️ `href="#acces"` vaut DEUX et pas un : le bouton du hero, puis le
    #    dernier lien du sommaire. C'est la seule ancre de la page visée deux
    #    fois, parce que c'est le seul geste de la page — il doit rester à un
    #    clic du haut quelle que soit la longueur du reste.
    ('<nav class="gf-som"', 1, 'le sommaire de la page, dans le hero'),
    ('<p class="gf-som-t">Sur cette page</p>', 1,
     'le titre qui dit que ce sommaire est celui de la PAGE, pas du site'),
    ('aria-label="Sommaire de la page"', 1,
     'les deux <nav> de la page sont distingués pour les lecteurs d’écran'),
    ('href="#promesse"', 1, 'sommaire → « Ce que ça change »'),
    ('href="#situations"', 1, 'sommaire → « Pour qui »'),
    ('href="#fonctionnalites"', 1, 'sommaire → « Ce qu’il y a dedans »'),
    ('href="#faq"', 1, 'sommaire → « Questions »'),
    ('href="#acces"', 2, 'le bouton du hero ET le dernier lien du sommaire'),
    # --- LE BLOG DEVIENT UN BLOC (nuit du 16/08/2026) --------------------
    # ⚠️ DEUX blocs, et l'ancre a ZERO qui interdit le retour de la ligne de
    #    texte qu'ils remplacent. David : « c'est même pas un bouton, c'est une
    #    ligne. » Un « allègement » futur qui rendrait `.blog-lien` referait
    #    exactement le défaut signalé — sans que rien ne le dise.
    ('class="blog-cta"', 2, 'les deux blocs de renvoi vers le blog'),
    ('class="blog-lien"', 0,
     'l’ancienne ligne de texte soulignée, remplacée par le bloc `.blog-cta`'),
    ('class="blog-cta-go"', 2, 'la pastille fléchée de chaque bloc'),
    ('Les dix-huit articles du blog de Guso Facile', 1,
     'l’ancre descriptive du bloc de fin de #situations (dossier SEO, §6)'),
    ('Toutes les situations concrètes sur le blog de Guso Facile', 1,
     'l’ancre descriptive du bloc de fin de FAQ (dossier SEO, §6)'),
    ('class="mea"', 1, 'le bloc de mise en avant des articles'),
    ('id="blog"', 1, 'l’ancre du bloc de mise en avant'),
    ('class="mea-c"', NB_MISE_EN_AVANT, 'les cartes d’article mises en avant'),
    ('class="mea-h"', NB_MISE_EN_AVANT, 'le vrai titre de chaque article mis en avant'),
    ('class="mea-d"', NB_MISE_EN_AVANT, 'l’accroche de chaque article mise en avant'),
    # --- LES DEUX CORRECTIONS FACTUELLES DU 16/08/2026 -------------------
    # ⚠️ L'ancre a ZERO est la plus importante des deux : « en temps réel »
    # etait une promesse qu'une structure pouvait dementir en dix secondes
    # (aucun abonnement temps reel dans l'application — voir l'entete). Cette
    # ligne interdit qu'elle revienne par reflexe.
    ('en temps réel', 0, 'la promesse de synchronisation instantanée, retirée le 16/08/2026'),
    ('<b>Synchronisation</b> — les données sont partagées entre l’artiste et la structure.', 1,
     'la phrase de synchronisation validée par l’auteur de l’application'),
    # Les six fonctionnalites livrees ajoutees a l'inventaire le 16/08/2026.
    # Elles s'ecrivent AU PRESENT, sans « (a venir) » — comme, depuis le
    # 17/08/2026, TOUT ce que la page decrit : `NB_A_VENIR` vaut 0.
    ('<b>Niveaux de partage</b>', 1,
     'niveaux de partage — LIVRÉE (le même réglage que « Confidentialité graduée », vu du côté structure)'),
    ('<b>Inscription par invitation</b>', 1, 'inscription par invitation — LIVRÉE'),
    ('<b>Hub d’informations du groupe</b>', 1, 'hub d’informations du groupe — LIVRÉE'),
    ('<b>Guide de démarrage</b>', 1, 'guide de démarrage — LIVRÉE'),
    ('<b>Guide intégré</b>', 1, 'guide intégré — LIVRÉE'),
    ('<b>Nouveautés</b>', 1, 'journal des nouveautés — LIVRÉE'),
    ('class="aussi-p2"', 1, 'la ligne « prise en main » de l’encadré « Et aussi »'),
    ('class="guilde"', 1, 'l’encart « la Guilde »'),
    ('class="guilde-claim"', 1, 'l’accroche du manifeste de la Guilde'),
    ('class="etapes"', 1, 'la bande « trois étapes, c’est tout »'),
    ('class="etape"', 3, 'les trois étapes'),
    ('class="etat-fin"', 1, 'la phrase de clôture de « Jouons cartes sur table »'),
    ('class="h1-sous"', 1, 'la seconde ligne du <h1> (dossier SEO, section 2.1)'),
    # « On veille les uns sur les autres », absorbe le 16/08/2026. La NOTE
    # compte autant que le bloc : sans elle, un prenom invente passe pour une
    # personne reelle — le piege exact que « situations réelles » -> « typiques »
    # a deja coute a cette page.
    ('class="veille"', 1, 'le bloc « On veille les uns sur les autres »'),
    ('class="veille-note"', 1,
     'la note qui dit que le prénom et le groupe sont fictifs'),
    # --- LES 4 APERÇUS DU LOT 2 (nuit du 16/08/2026) ---------------------
    # Un marqueur par bloc : le compte global (`<figure class="gf-block`) dirait
    # seulement qu'il y en a dix, pas LESQUELS. Ces cinq lignes disent que c'est
    # bien CES écrans-là qui sont posés, et à un seul exemplaire.
    ('class="gf-ctx"', 1, 'l’aperçu du sélecteur « Je regarde »'),
    ('class="gf-help"', 1, 'l’aperçu du parcours « J’ai besoin d’aide »'),
    ('class="gf-opt"', 4,
     'les QUATRE réponses de la question 1 — ce ne sont pas les trois questions'),
    ('class="gf-cl"', 1, 'l’aperçu du journal des nouveautés'),
    # --- LA CARTE DE TOURNÉE ---------------------------------------------
    # ⚠️ LES DEUX ANCRES À ZÉRO SONT LES PLUS IMPORTANTES DE CE GROUPE. Le tracé
    #    du fichier source était fait de `<div>` PIVOTÉS dimensionnés en
    #    POURCENTAGES : les traits se désolidarisaient des points dès que le
    #    rapport largeur/hauteur du conteneur changeait, c'est-à-dire à chaque
    #    largeur d'écran. Constaté à l'écran. Ces deux lignes interdisent qu'il
    #    revienne par copier-coller — le défaut ne se voit pas en relisant le
    #    code, seulement en redimensionnant la fenêtre.
    ('class="gf-map"', 1, 'la carte de tournée, dessinée en SVG'),
    ('class="gf-leg"', 0,
     'le tracé en <div> pivotés du fichier source : il se désolidarise des '
     'points dès que le rapport largeur/hauteur change'),
    ('class="gf-pin"', 0, 'les points en <div> positionnés du fichier source'),
    ('viewBox="0 0 100 52"', 1, 'le repère unique où vivent le tracé ET les points'),
    # ⚠️ « gf-pt-dom" » et non « class="gf-pt-dom" » : ces deux cercles portent
    #    DEUX classes (`class="gf-pt gf-pt-dom"`), la forme du point commune et
    #    sa nature. Chercher l'attribut entier ne trouverait rien.
    ('gf-pt-dom"', 1,
     'le point du DOMICILE — le kilométrage se calcule depuis l’adresse du profil'),
    ('gf-pt-sup"', 1,
     'le LIEU SUPPOSÉ, que l’app a deviné et demande de confirmer'),
    ('≈ 612 km', 1, 'le kilométrage cumulé, dans la formulation de l’app'),
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

    # Aucun bouton hors du menu partage NI DU FORMULAIRE. Le reste du corps de
    # la page ne doit contenir que du texte, des liens, et des illustrations
    # inertes.
    # ⚠️ 16/08/2026 : le `<form>` est retire du texte examine EN MEME TEMPS que
    #    le `<nav>`. C'est le seul assouplissement de ce garde-fou, et il est
    #    etroit : il autorise le bouton d'envoi du formulaire de demande
    #    d'acces, RIEN D'AUTRE. Les six apercus d'interface, eux, continuent
    #    d'etre verifies un par un juste en dessous, avec la meme exigence
    #    qu'avant : zero element focusable a l'interieur.
    corps = re.sub(r'<nav\b.*?</nav>', '', html, flags=re.S)
    corps = re.sub(r'<form\b.*?</form>', '', corps, flags=re.S)
    if '<button' in corps:
        raise SystemExit('!! ABANDON : un <button> hors du menu de navigation et '
                         'hors du formulaire de demande d\'accès. Le corps de la '
                         'page n\'a aucune autre commande a offrir. Page NON ecrite.')

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
#: ⚠️ `guso-facile.vercel.app` EST SORTI DE CETTE LISTE LE 16/08/2026, en meme
#: temps que le lien qui y menait. C'est volontaire et c'est une securite : si
#: un lien vers l'ancienne page revenait un jour, la page ne serait PAS ecrite.
#: ⚠️ `wqhwfqasoyyeprggjxet.supabase.co` (16/08/2026) est le SEUL hote qui
#: recoive reellement quelque chose de cette page, et UNIQUEMENT au clic sur
#: « Envoyer ma demande » — jamais au chargement. C'est l'exception assumee a
#: la regle « zero tiers », et elle s'arrete la : ni traceur, ni police
#: supplementaire, ni iframe, ni script distant.
HOTES_AUTORISES = (
    'schema.org',
    'fonts.googleapis.com',
    'fonts.gstatic.com',
    'www.helloasso.com',
    'wqhwfqasoyyeprggjxet.supabase.co',
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


#: les champs du formulaire : (identifiant, ce que c'est). L'ordre est celui de
#: la saisie. `_controle_formulaire()` verifie pour CHACUN qu'un `<label for=…>`
#: le designe : sans ce couple, la case n'est pas cliquable, et un lecteur
#: d'ecran annonce « zone de saisie » sans dire laquelle.
CHAMPS_FORMULAIRE = (
    ('dmd-prenom', 'Prénom'),
    ('dmd-nom', 'Nom'),
    ('dmd-email', 'Adresse e-mail'),
    ('dmd-tel', 'Téléphone'),
    ('dmd-message', 'Message'),
    # les trois boutons du choix « Je suis », et les quatre de la structure :
    # un bouton radio sans <label for> n'est pas cliquable sur son libelle,
    # cible tactile la plus fine du formulaire.
    ('dmd-artiste', 'Je suis — Artiste'),
    ('dmd-structure', 'Je suis — Structure'),
    ('dmd-les-deux', 'Je suis — Les deux'),
    ('dmd-struct-nom', 'Nom de la structure'),
    ('dmd-type-asso', 'Type — Association loi 1901'),
    ('dmd-type-autre', 'Type — Autre'),
    ('dmd-lic-oui', 'Licence d’entrepreneur de spectacles — Oui'),
    ('dmd-lic-non', 'Licence d’entrepreneur de spectacles — Non'),
)

#: LES SEULES COLONNES DE LA TABLE `account_requests` QU'ON A LE DROIT
#: D'ENVOYER. Toute autre fait echouer la requete : la securite rejette les
#: champs inconnus, et c'est cette meme regle qui interdit l'auto-approbation.
#: ⚠️ 17/08/2026 — LES TROIS COLONNES DE STRUCTURE Y ENTRENT. Elles viennent
#: d'etre creees par la session qui developpe l'application, qui demande de ne
#: plus dupliquer l'information (« le doublon aurait fini par diverger ») :
#: elles ne passent donc plus par `context` ni par `message`. La garde, elle,
#: n'a PAS ete assouplie — elle refuse toujours toute colonne hors de cette
#: liste ; on a seulement inscrit les trois nouvelles.
COLONNES_DEMANDE = ('email', 'first_name', 'last_name', 'phone', 'kind',
                    'message', 'context',
                    'structure_name', 'structure_type', 'structure_licence')

#: les colonnes envoyees A CHAQUE DEMANDE, quelle que soit la nature de la
#: personne. Ce sont celles du litteral `var corps = {…}`.
COLONNES_TOUJOURS = ('email', 'first_name', 'last_name', 'phone', 'kind',
                     'message', 'context')

#: les colonnes envoyees UNIQUEMENT pour une structure (« Structure » ou « Les
#: deux »). Pour un artiste seul, le corps ne les porte PAS DU TOUT — ni chaine
#: vide, ni `null`. C'est pour cela que le corps est construit dans une variable
#: avant l'envoi : un litteral ne sait pas omettre une cle.
COLONNES_STRUCTURE = ('structure_name', 'structure_type', 'structure_licence')

#: ⚠️ LA CONVERSION EN BOOLEEN, ECRITE UNE FOIS ET VERIFIEE. `structure_licence`
#: est une colonne BOOLEAN : y envoyer la chaine « oui » rend
#: « 400 22P02 invalid input syntax for type boolean: "oui" » (mesure sur
#: l'endpoint reel avant d'ecrire ce code), et la personne verrait une panne
#: incomprehensible a la derniere etape de sa demande.
CONVERSION_LICENCE = "corps.structure_licence = (sLic === 'oui');"

#: les quatre champs OBLIGATOIRES depuis le 17/08/2026 (demande de David).
#: Chacun doit porter `required` ET `aria-describedby` vers SA boite de message.
CHAMPS_OBLIGATOIRES = (
    ('dmd-prenom', 'Prénom'),
    ('dmd-nom', 'Nom'),
    ('dmd-email', 'Adresse e-mail'),
    ('dmd-tel', 'Téléphone'),
)

#: les trois champs qui n'apparaissent QUE pour une structure — et qui ne sont
#: obligatoires QUE dans ce cas. (identifiant du porteur d'erreur, ce que c'est)
CHAMPS_STRUCTURE = (
    ('dmd-struct-nom', 'Nom de la structure'),
    ('dmd-struct-type', 'Type de structure'),
    ('dmd-struct-licence', 'Licence d’entrepreneur de spectacles'),
)


def _controle_formulaire(html):
    """Refuse d'ecrire si le formulaire de demande d'acces derape.

    C'est le seul endroit de la page ou l'on SAISIT quelque chose, et depuis le
    16/08/2026 c'est aussi le seul endroit d'ou part une requete vers un tiers.
    Les exigences, une par une, chacune avec ce qu'elle empeche :

      1. UN SEUL `<form>`, ET TOUS LES CHAMPS DEDANS. Un champ egare hors du
         formulaire ne serait jamais envoye : le visiteur le remplirait pour
         rien. Et un champ POSE DANS UNE MAQUETTE ferait croire qu'on pilote
         l'outil depuis le site de l'association.
      2. UN `<label for=…>` PAR CHAMP. Sans lui, le libelle n'est pas cliquable
         et n'est pas annonce a la prise de focus.
      3. L'E-MAIL EST `required` ET `aria-describedby` SON MESSAGE D'ERREUR.
         C'est le seul champ obligatoire — c'est par la qu'arrive la reponse —
         et l'erreur doit etre ASSOCIEE au champ, pas flottante en bas de page.
      4. UNE ZONE `aria-live` : sans elle, la confirmation d'envoi s'affiche a
         l'ecran sans jamais etre annoncee. Quelqu'un qui n'y voit pas ne
         saurait pas si sa demande est partie.
      5. AUCUN EN-TETE `Prefer` : la cle publiable n'a pas le droit de relire la
         ligne inseree ; demander `return=representation` rend un 401 ALORS QUE
         L'INSERTION A REUSSI (piege qui a deja coute du temps a l'auteur).
      6. AUCUN CHAMP `status` DANS LE CORPS ENVOYE : la securite impose
         `status='new'` ; le fournir fait echouer la requete (protection contre
         l'auto-approbation).
      7. LES TROIS CODES SONT TRAITES, ET LE 409 SE LIT COMME UNE BONNE
         NOUVELLE. « Une demande est deja en attente pour cet e-mail » veut dire
         que la demande est bien arrivee : jamais un mot de panne.
      8. LA MENTION SUR LES DONNEES NOMME DAVID LESAGE. La saisie se fait
         desormais sur le domaine de l'association : sans cette phrase, un
         visiteur croirait confier ses coordonnees a l'association.
      9. (17/08/2026) LE CORPS N'ENVOIE QUE DES COLONNES QUI EXISTENT, LES
         TROIS DE STRUCTURE UNIQUEMENT POUR UNE STRUCTURE, ET LA LICENCE EN
         BOOLEEN. Une chaine dans `structure_licence` rend un 400 : la personne
         verrait une panne incomprehensible a la derniere etape.
    """
    import re

    formulaires = re.findall(r'<form\b.*?</form>', html, re.S)
    if len(formulaires) != 1:
        raise SystemExit('!! ABANDON : %d formulaire(s), attendu 1. '
                         'Page NON ecrite.' % len(formulaires))
    form = formulaires[0]
    hors = html.replace(form, '')
    for balise in ('<input', '<textarea', '<select'):
        if balise in hors:
            raise SystemExit(
                '!! ABANDON : « %s » HORS du formulaire de demande d\'accès.\n'
                '   Un champ pose ailleurs ne serait jamais envoye — et pose dans '
                'une maquette, il ferait croire au visiteur qu\'il pilote l\'outil '
                'depuis le site de l\'association.\n   Page NON ecrite.' % balise)

    for ident, quoi in CHAMPS_FORMULAIRE:
        if 'id="%s"' % ident not in form:
            raise SystemExit('!! ABANDON : champ « %s » (id="%s") absent du '
                             'formulaire. Page NON ecrite.' % (quoi, ident))
        if 'for="%s"' % ident not in form:
            raise SystemExit(
                '!! ABANDON : le champ « %s » n\'a pas de <label for="%s">.\n'
                '   Sans ce couple, le libelle n\'est pas cliquable et n\'est pas '
                'annonce a la prise de focus.\n   Page NON ecrite.' % (quoi, ident))

    email = re.search(r'<input[^>]*id="dmd-email"[^>]*>', form)
    if not email:
        raise SystemExit('!! ABANDON : champ e-mail introuvable. Page NON ecrite.')
    if 'type="email"' not in email.group(0):
        raise SystemExit('!! ABANDON : le champ e-mail n\'a pas « type="email" » — '
                         'le clavier d\'un telephone doit proposer le @. '
                         'Page NON ecrite.')

    # 17/08/2026 — QUATRE champs obligatoires, plus un seul. Chacun porte
    # `required` ET `aria-describedby` vers SA boite de message : une erreur
    # flottante en bas de page n'est jamais annoncee au bon moment.
    for ident, quoi in CHAMPS_OBLIGATOIRES:
        m = re.search(r'<input[^>]*id="%s"[^>]*>' % ident, form)
        if not m:
            raise SystemExit('!! ABANDON : champ « %s » introuvable. '
                             'Page NON ecrite.' % quoi)
        if 'required' not in m.group(0):
            raise SystemExit(
                '!! ABANDON : le champ « %s » n\'est pas marque `required`.\n'
                '   Les quatre champs prenom, nom, e-mail et telephone sont '
                'obligatoires depuis le 17/08/2026 (demande de David).\n'
                '   Page NON ecrite.' % quoi)
        if 'aria-describedby="%s-err"' % ident not in m.group(0):
            raise SystemExit(
                '!! ABANDON : le champ « %s » n\'est pas relie a son message '
                '(aria-describedby="%s-err").\n   Sans ce lien, le message '
                's\'affiche sans jamais etre annonce.\n   Page NON ecrite.'
                % (quoi, ident))
        if 'id="%s-err"' % ident not in form:
            raise SystemExit('!! ABANDON : la boite de message du champ « %s » '
                             '(id="%s-err") est absente. Page NON ecrite.'
                             % (quoi, ident))

    # LES TROIS CHAMPS DE STRUCTURE. Ils n'existent que pour « Structure » et
    # « Les deux » — et ils ne sont obligatoires que dans ce cas, sans quoi le
    # formulaire deviendrait impossible a envoyer pour un artiste seul, sans que
    # rien ne le dise. Ce que ce controle exige :
    #   - le bloc part REPLIE (`hidden`) ;
    #   - chacun a sa boite de message et son `aria-required` ;
    #   - une zone d'annonce dit qu'ils viennent d'apparaitre.
    if 'id="dmd-struct" hidden' not in form:
        raise SystemExit(
            '!! ABANDON : le bloc des champs de structure ne part pas replie '
            '(`id="dmd-struct" hidden`).\n   Livre ouvert, il demanderait a un '
            'artiste seul trois informations qui ne le concernent pas — et il les '
            'exigerait.\n   Page NON ecrite.')
    for ident, quoi in CHAMPS_STRUCTURE:
        if 'id="%s"' % ident not in form:
            raise SystemExit('!! ABANDON : « %s » (id="%s") absent du formulaire. '
                             'Page NON ecrite.' % (quoi, ident))
        if 'id="%s-err"' % ident not in form:
            raise SystemExit('!! ABANDON : la boite de message de « %s » '
                             '(id="%s-err") est absente. Page NON ecrite.'
                             % (quoi, ident))
    if 'id="dmd-struct-avis"' not in form:
        raise SystemExit(
            '!! ABANDON : rien n\'annonce l\'apparition des champs de structure.\n'
            '   Sans cette zone, quelqu\'un qui n\'y voit pas coche « Structure » '
            'et n\'apprend qu\'il reste trois champs qu\'au moment ou l\'envoi est '
            'refuse : l\'apparition serait PUREMENT VISUELLE.\n   Page NON ecrite.')

    if 'aria-live="polite"' not in form or 'role="status"' not in form:
        raise SystemExit(
            '!! ABANDON : le formulaire n\'a pas de zone d\'annonce '
            '(role="status" + aria-live="polite").\n   Sans elle, la confirmation '
            's\'affiche sans jamais etre annoncee : quelqu\'un qui n\'y voit pas ne '
            'sait pas si sa demande est partie.\n   Page NON ecrite.')

    script = re.search(r'<script>\s*\(function\(\)\{\s*var f = document'
                       r'\.getElementById\(\'demande\'\).*?</script>', html, re.S)
    if not script:
        raise SystemExit('!! ABANDON : le script du formulaire est introuvable. '
                         'Page NON ecrite.')
    js = script.group(0)
    if 'Prefer' in js:
        raise SystemExit(
            '!! ABANDON : en-tete « Prefer » dans l\'envoi du formulaire.\n'
            '   La cle publiable n\'a pas le droit de RELIRE la ligne inseree : '
            'demander `return=representation` rend un 401 ALORS QUE L\'INSERTION A '
            'REUSSI. Sans cet en-tete, c\'est un 201 propre.\n   Page NON ecrite.')
    if re.search(r'\bstatus\s*:', js):
        raise SystemExit(
            '!! ABANDON : un champ « status » dans le corps envoye.\n'
            '   La securite impose status=\'new\' ; le fournir FAIT ECHOUER la '
            'requete — c\'est la protection contre l\'auto-approbation.\n'
            '   Page NON ecrite.')
    for code in ('201', '409', '401'):
        if code not in js:
            raise SystemExit('!! ABANDON : le code de reponse %s n\'est pas traite '
                             'par le formulaire. Page NON ecrite.' % code)
    if 'erreur ' in js or 'Erreur ' in js:
        raise SystemExit(
            '!! ABANDON : le mot « erreur » apparait dans un message du '
            'formulaire.\n   Les reponses du serveur se rendent en PHRASES, jamais '
            'en codes ni en jargon — le 409 en particulier est une BONNE nouvelle : '
            'la demande est bien arrivee.\n   Page NON ecrite.')

    # ⚠️⚠️ LE CORPS DE LA REQUETE NE CONTIENT QUE DES COLONNES QUI EXISTENT.
    # Toute colonne inconnue fait echouer la requete — la securite rejette les
    # champs qu'elle ne connait pas, et c'est cette meme regle qui interdit
    # l'auto-approbation. Le defaut serait INVISIBLE a la relecture (le code a
    # l'air juste) et ne se verrait qu'a l'envoi, sur une demande perdue.
    #
    # ⚠️ 17/08/2026 — LE CORPS EST DESORMAIS CONSTRUIT DANS UNE VARIABLE, et ce
    # n'est pas un gout de style : les trois colonnes de structure ne partent
    # QUE pour une structure, et un litteral ne sait pas omettre une cle. On
    # controle donc DEUX ensembles — celui du litteral (toujours envoye) et
    # celui des affectations conditionnelles.
    if 'body: JSON.stringify(corps)' not in js:
        raise SystemExit(
            '!! ABANDON : le corps de la requete n\'est plus l\'objet `corps`.\n'
            '   Il doit etre construit dans une variable AVANT l\'envoi : un '
            'litteral ne sait pas omettre les colonnes de structure quand la '
            'personne est un artiste seul.\n   Page NON ecrite.')
    corps = re.search(r'var corps = \{(.*?)\};', js, re.S)
    if not corps:
        raise SystemExit('!! ABANDON : le corps de la requete est introuvable. '
                         'Page NON ecrite.')
    if '{' in corps.group(1):
        raise SystemExit(
            '!! ABANDON : un objet est ecrit EN LIGNE dans le corps de la requete.\n'
            '   Les cles ne peuvent plus etre comptees de facon fiable — et c\'est '
            'exactement la que se glisse une colonne inventee. Construire l\'objet '
            'dans une variable au-dessus.\n   Page NON ecrite.')
    cles = re.findall(r'(\w+)\s*:', corps.group(1))
    if sorted(cles) != sorted(COLONNES_TOUJOURS):
        raise SystemExit(
            '!! ABANDON : le corps de la requete envoie toujours %s.\n'
            '   Les colonnes envoyees a CHAQUE demande sont %s.\n   Page NON ecrite.'
            % (', '.join(sorted(cles)), ', '.join(sorted(COLONNES_TOUJOURS))))

    # LES COLONNES CONDITIONNELLES : celles qu'on AJOUTE a `corps`. Elles ne
    # doivent exister que pour une structure — donc DANS le `if (structure())`.
    ajouts = re.findall(r'corps\.(\w+)\s*=', js)
    if sorted(ajouts) != sorted(COLONNES_STRUCTURE):
        raise SystemExit(
            '!! ABANDON : les colonnes ajoutees au corps sont %s, attendu %s.\n'
            '   Les trois informations de structure partent en COLONNES depuis le '
            '17/08/2026 — plus dans `context`, plus dans `message`.\n'
            '   Page NON ecrite.'
            % (', '.join(sorted(ajouts)) or '(aucune)',
               ', '.join(sorted(COLONNES_STRUCTURE))))
    inconnues = [c for c in cles + ajouts if c not in COLONNES_DEMANDE]
    if inconnues:
        raise SystemExit(
            '!! ABANDON : colonne(s) inconnue(s) dans le corps de la requete : %s.\n'
            '   Les SEULES colonnes de la table `account_requests` sont %s. Toute '
            'autre fait echouer la requete : la securite rejette les champs '
            'inconnus, c\'est ce qui protege de l\'auto-approbation.\n'
            '   Page NON ecrite.'
            % (', '.join(inconnues), ', '.join(sorted(COLONNES_DEMANDE))))
    # ⚠️ `if (structure())` apparait DEUX fois dans le script (la validation des
    # trois champs, puis l'ajout des trois colonnes) : on parcourt donc tous les
    # blocs et on exige qu'UN d'entre eux porte les trois affectations. Chercher
    # le premier seulement ferait echouer l'ecriture pour rien.
    blocs = re.findall(r'if \(structure\(\)\) \{(.*?)\n    \}', js, re.S)
    if not any(len(re.findall(r'corps\.\w+\s*=', b)) == 3 for b in blocs):
        raise SystemExit(
            '!! ABANDON : les trois colonnes de structure ne sont pas ajoutees a '
            'l\'INTERIEUR de `if (structure())`.\n   Envoyees pour un artiste seul, '
            'elles feraient partir trois valeurs vides que personne n\'a saisies.\n'
            '   Page NON ecrite.')

    # ⚠️⚠️ LE BOOLEEN. `structure_licence` est une colonne BOOLEAN : y envoyer
    # « oui » rend « 400 22P02 invalid input syntax for type boolean » — mesure
    # sur l'endpoint reel, pas supposition. La personne verrait une panne
    # incomprehensible a la derniere etape. La conversion est ecrite UNE fois,
    # et cette ligne verifie qu'elle y est toujours.
    if CONVERSION_LICENCE not in js:
        raise SystemExit(
            '!! ABANDON : la licence n\'est plus convertie en BOOLEEN.\n'
            '   La ligne attendue, mot pour mot : « %s ».\n   La colonne '
            '`structure_licence` est un BOOLEAN : une chaine (« oui », « non », '
            'ou meme « true ») fait ECHOUER la requete, et la personne verrait une '
            'panne incomprehensible.\n   Page NON ecrite.' % CONVERSION_LICENCE)

    # LES ANCIENNES DUPLICATIONS NE DOIVENT PAS REVENIR. L'auteur de
    # l'application a demande de les retirer, son motif etant : « le doublon
    # aurait fini par diverger ».
    if 'ctx.structure' in js:
        raise SystemExit(
            '!! ABANDON : une information de structure est ecrite dans `context`.\n'
            '   Elle vit maintenant dans ses colonnes (`structure_name`, '
            '`structure_type`, `structure_licence`) : la dupliquer est exactement '
            'ce qu\'il a ete demande d\'arreter.\n   Page NON ecrite.')
    if '— Structure : «' in js:
        raise SystemExit(
            '!! ABANDON : la ligne lisible « — Structure : … » est de retour a la '
            'fin du message.\n   `message` ne porte QUE le message de la personne '
            'depuis le 17/08/2026 : le nom, le type et la licence ont leurs '
            'colonnes.\n   Page NON ecrite.')
    if ('origin: location.href' not in js or 'ts: new Date()' not in js
            or 'ua: navigator.userAgent' not in js):
        raise SystemExit(
            '!! ABANDON : `context` ne porte plus `{origin, ts, ua}`.\n   Ces trois '
            'cles servent a tracer d\'ou viennent les demandes.\n'
            '   Page NON ecrite.')

    # UNE SEULE FONCTION decide de l'affichage ET de l'exigence des champs
    # conditionnels : c'est ce qui rend impossible le piege du champ cache reste
    # obligatoire (formulaire impossible a envoyer, sans explication).
    if "v === 'structure' || v === 'les_deux'" not in js:
        raise SystemExit(
            '!! ABANDON : la condition qui commande les champs de structure n\'est '
            'plus celle attendue.\n   Elle doit etre vraie pour « structure » ET '
            'pour « les_deux » — « les deux » EST une structure.\n'
            '   Page NON ecrite.')
    if 'bloc.hidden = !on' not in js:
        raise SystemExit(
            '!! ABANDON : le bloc de structure n\'est plus replie/deplie par la '
            'meme fonction que celle qui decide de l\'exigence.\n   Deux sources de '
            'verite = un champ cache qui bloque l\'envoi sans que rien ne le dise.\n'
            '   Page NON ecrite.')


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


#: nombre de pictogrammes POSES dans la page — des EMPLOIS, pas des entrees du
#: dictionnaire. Un ecart = un picto duplique ou disparu.
#: Historique : 10 le 14/08/2026 ; 11 le 15/08 (« guilde », pour l'encart du
#: meme nom) ; 14 le 16/08 — « artiste » et « structures » pour les deux
#: en-tetes de la double vue, « bouee » pour le bloc « J'ai besoin d'aide » ;
#: 16 la nuit du 16/08 — « articles », POSE DEUX FOIS, dans les deux blocs de
#: renvoi vers le blog.
#: ⚠️ C'EST LE PREMIER PICTOGRAMME DE LA PAGE A SERVIR DEUX FOIS : le compte
#: n'est donc plus egal au nombre de cles de `ICONES` (quinze). C'est assume —
#: les deux blocs sont le MEME geste a deux etages de la page, leur donner deux
#: dessins differents dirait qu'ils menent ailleurs.
#: ⚠️ « artiste », « structures » et « bouee » REMPLACENT DES EMOJI de la page
#: de reference (👤, 🛠, 🤗). C'est la regle du site ET une demande explicite de
#: David : des icones de signature au trait, jamais un pictogramme systeme.
NB_PICTOS = 16

#: les <svg> de la page qui ne sont NI un pictogramme NI le bloc de definitions
#: du degrade. Un seul aujourd'hui : la carte de tournee (`MAQ_CARTE`). Elle
#: passe les memes controles que les pictogrammes — `aria-hidden`,
#: `focusable="false"`, aucun `xmlns` — puisque c'est le `role="img"` de son
#: bloc qui la decrit.
NB_SVG_HORS_PICTOS = 1


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
    attendu = NB_PICTOS + 1 + NB_SVG_HORS_PICTOS
    if len(balises) != attendu:
        raise SystemExit('!! ABANDON : %d balise(s) <svg>, attendu %d (les %d '
                         'pictogrammes + le bloc de definitions du degrade + %d '
                         'figure(s) dessinee(s), aujourd\'hui la carte de tournee). '
                         'Page NON ecrite.'
                         % (len(balises), attendu, NB_PICTOS, NB_SVG_HORS_PICTOS))
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


#: les trois paliers de taille des libelles de la carte, et la largeur RENDUE la
#: plus petite a laquelle chacun s'applique.
#: (declaration CSS attendue, largeur rendue minimale en px, d'ou vient ce chiffre)
#:
#: LA LARGEUR RENDUE, D'OU ELLE SORT. La figure de la carte est plafonnee a
#: 556 px (`.apercus .gf-carte-b`), et le SVG occupe cette largeur MOINS le
#: rembourrage lateral de `.gf-shot` : 18 px de chaque cote au-dessus de 760 px
#: d'ecran, 13 px en dessous. D'ou :
#:   * au-dela de 608 px d'ecran, la largeur rendue est CONSTANTE (520-530 px) —
#:     c'est tout l'interet du plafond : elle cesse de dependre de l'ecran ;
#:   * en dessous, elle vaut `largeur_ecran - 78` (26 px de `.wrap` + 26 px de
#:     `.gf-shot`), soit 375 px a 453 px d'ecran et 297 px a 375 px d'ecran.
#: Le plus petit ecran servi est donc ~375 px. En dessous, les libelles
#: passeraient sous 13 px — et on ne peut pas grossir la police davantage :
#: au-dela de ~4,4 unites, « Festival du Causse » et « Théâtre Rivage » se
#: chevauchent (mesure a l'ecran). C'est une limite assumee, pas un oubli.
PALIERS_CARTE = (
    ('font-size:3.2px', 520, 'au-dela de 608 px d’ecran : largeur plafonnee'),
    ('font-size:3.6px', 375, 'ecran de 453 px (palier @media max-width:558px)'),
    ('font-size:4.4px', 297, 'ecran de 375 px (palier @media max-width:452px)'),
)

#: le plancher typographique du site, en pixels d'ecran.
PLANCHER_PX = 13


def _controle_carte(html):
    """Refuse d'ecrire si un libelle de la carte tombe sous le plancher de 13 px.

    C'est le pendant de l'exemption accordee dans `_controles()` : la feuille de
    la carte echappe au comptage brut des `font-size:…px` parce que ses valeurs
    sont des UNITES UTILISATEUR d'un `viewBox`, pas des pixels. On refait donc
    ici le seul calcul qui vaille — `unites x largeur_rendue / 100` — pour
    chacun des trois paliers, avec la largeur rendue la plus petite a laquelle
    il s'applique.

    ⚠️ Si le plafond de largeur de la figure, le rembourrage de `.gf-shot` ou
    les bornes des deux `@media` bougent, CE TABLEAU DOIT BOUGER AVEC. C'est la
    raison pour laquelle chaque ligne porte l'ecran d'ou vient son chiffre.
    """
    for declaration, largeur, origine in PALIERS_CARTE:
        if declaration not in CSS_CARTE:
            raise SystemExit(
                '!! ABANDON : le palier « %s » de la carte a disparu de sa feuille '
                'de style (%s).\n   Les trois paliers sont ce qui maintient ses '
                'libelles au-dessus de %d px reels a toutes les largeurs.\n'
                '   Page NON ecrite.' % (declaration, origine, PLANCHER_PX))
        unites = float(declaration.split(':')[1].rstrip('px'))
        rendu = unites * largeur / 100.0
        if rendu < PLANCHER_PX:
            raise SystemExit(
                '!! ABANDON : les libelles de la carte tomberaient a %.1f px '
                '(%s unites de viewBox sur une largeur rendue de %d px — %s).\n'
                '   Le plancher du site est de %d px. Dans un SVG a viewBox, une '
                'taille de police est multipliee par (largeur rendue / 100) : elle '
                'RETRECIT sur telephone.\n   Page NON ecrite.'
                % (rendu, declaration.split(':')[1], largeur, origine, PLANCHER_PX))
    # le SVG doit deborder librement : « Théâtre Rivage » sort d'environ 2,5
    # unites a droite du cadre au dernier palier, et ce debordement tombe dans le
    # rembourrage de `.gf-shot`, pas hors de lui. Sans cette ligne, le nom est
    # rogne — et ca ne se voit qu'a l'ecran, sur telephone.
    if 'overflow:visible' not in CSS_CARTE:
        raise SystemExit(
            '!! ABANDON : le <svg> de la carte n\'a plus `overflow:visible`.\n'
            '   Au dernier palier, « Théâtre Rivage » deborde d\'environ 2,5 unites '
            'a droite du cadre : sans cette regle il est rogne, et cela ne se voit '
            'que sur telephone.\n   Page NON ecrite.')


def _controle_mise_en_avant(html):
    """Refuse d'ecrire si le bloc `.mea` ment sur le blog.

    C'est le garde-fou de la DUPLICATION assumee : les titres et les accroches
    des trois articles sont recopies dans `MISE_EN_AVANT` alors que leur source
    de verite est la table `ARTICLES` de `generate_guso_blog.py`. On ne peut pas
    l'importer (la regle du depot l'interdit : importer un `generate_*.py`
    ecrirait ses pages). On relit donc LA PAGE D'ARTICLE DEJA SUR LE DISQUE et
    on compare son <h1> au titre affiche ici.

    Trois exigences :
      1. autant de cartes que d'entrees dans `MISE_EN_AVANT`, et trois slugs
         DISTINCTS (une carte dupliquee, c'est le piege des quatre cartes
         identiques deja vecu sur ce projet) ;
      2. chaque titre et chaque accroche figurent bien dans la page ;
      3. si `guso-facile/blog/<slug>/index.html` existe, son <h1> est le meme
         titre, a l'apostrophe pres. ⚠️ Un fichier ABSENT ne fait pas echouer :
         sur un clone neuf, `build.py` construit /guso-facile AVANT le blog, et
         refuser d'ecrire la page produit parce que le blog n'existe pas encore
         bloquerait la chaine entiere. Le jour ou le blog est la — c'est-a-dire
         toujours, dans le depot —, la comparaison se fait.
    """
    import re

    slugs = re.findall(r'<a class="mea-c" href="/guso-facile/blog/([a-z0-9-]+)">', html)
    if len(slugs) != NB_MISE_EN_AVANT:
        raise SystemExit('!! ABANDON : %d carte(s) d\'article mise(s) en avant, '
                         'attendu %d. Page NON ecrite.'
                         % (len(slugs), NB_MISE_EN_AVANT))
    if len(set(slugs)) != len(slugs):
        raise SystemExit('!! ABANDON : deux cartes mises en avant pointent le meme '
                         'article. Page NON ecrite.')
    if slugs != [m[0] for m in MISE_EN_AVANT]:
        raise SystemExit('!! ABANDON : les cartes ne sont pas celles de '
                         'MISE_EN_AVANT (%s). Page NON ecrite.' % ', '.join(slugs))

    for slug, _rub, titre, accroche, _lect in MISE_EN_AVANT:
        for morceau, quoi in ((titre, 'le titre'), (accroche, 'l\'accroche')):
            if html.count(morceau) != 1:
                raise SystemExit('!! ABANDON : %s de « %s » ne figure pas une fois '
                                 'et une seule dans la page. Page NON ecrite.'
                                 % (quoi, slug))
        page = os.path.join(OUT_DIR, 'blog', slug, 'index.html')
        if not os.path.exists(page):
            continue
        with open(page, encoding='utf-8') as f:
            m = re.search(r'<h1>(.*?)</h1>', f.read(), re.S)
        if not m:
            raise SystemExit('!! ABANDON : aucun <h1> dans %s — impossible de '
                             'verifier le titre mis en avant. Page NON ecrite.' % page)
        reel = _norm_apostrophes(m.group(1))
        if _norm_apostrophes(titre) != reel:
            raise SystemExit(
                '!! ABANDON : le titre mis en avant a diverge de l\'article.\n'
                '   ici    : %s\n   article: %s\n'
                '   Corriger MISE_EN_AVANT (ces titres sont RECOPIES de la table '
                'ARTICLES de generate_guso_blog.py, jamais reecrits).\n'
                '   Page NON ecrite.' % (titre, m.group(1)))


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
    # ⚠️ LA FEUILLE DE LA CARTE EST RETIREE AVANT LE COMPTE, ET CE N'EST PAS UNE
    #    EXEMPTION DE COMPLAISANCE. Dans un SVG a `viewBox`, `font-size:3.2px`
    #    ne designe PAS 3,2 pixels d'ecran : c'est une UNITE UTILISATEUR, qui
    #    vaut a l'ecran `3,2 x largeur_rendue / 100`. Le controle ci-dessous
    #    compare des pixels ; sur ces trois declarations il comparerait des
    #    unites, et refuserait une page dont les libelles font 17 px. Le
    #    plancher n'est pas leve pour autant : `_controle_carte()` REFAIT le
    #    calcul, palier par palier, avec la largeur rendue reelle.
    if html.count(CSS_CARTE) != 1:
        raise SystemExit('!! ABANDON : la feuille de style de la carte n\'apparait '
                         'pas une fois et une seule dans la page — le controle du '
                         'plancher de 13 px ne saurait plus quoi en retirer. '
                         'Page NON ecrite.')
    petits = [t for t in re.findall(r'font-size:\s*(\d+(?:\.\d+)?)px',
                                    html.replace(CSS_CARTE, ''))
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
    # le formulaire de demande d'acces : le seul endroit ou l'on saisit, et le
    # seul d'ou part une requete vers un tiers (16/08/2026)
    _controle_formulaire(html)
    # les pictogrammes : decoratifs, jamais annonces ni focusables
    _controle_icones(html)
    # la carte de tournee : ses libelles restent au-dessus du plancher de 13 px
    # a toutes les largeurs (le calcul, pas la supposition)
    _controle_carte(html)
    # les trois articles mis en avant : titres recopies, jamais reecrits
    _controle_mise_en_avant(html)


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
