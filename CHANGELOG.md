# Journal des modifications

## 2026-11-09
- Favicon refait : la tête de la mascotte sur fond vert foncé, au lieu du rat
  entier déformé (l'ancienne icône n'était pas carrée et devenait illisible).
  Cadrage resserré pour les petites tailles, et ajout de l'icône pour l'écran
  d'accueil des mobiles (apple-touch-icon, 192 et 512 px) et de la couleur de
  barre d'adresse.
- Contrôle des liens internes corrigé : il vérifie maintenant aussi les fichiers
  (icônes, feuille de style) au lieu de les signaler à tort.

## 2026-11-07
- Bouton de retour en haut refait : rond discret avec un anneau orange qui se
  remplit selon la progression dans la page, placé au-dessus de la mascotte.
- Fil d'Ariane repris sur les 317 pages : libellés courts (« Laval », « Boulangerie
  à Fougères ») au lieu des titres SEO tronqués, et niveau parent ajouté pour les
  pages punaises de lit, frelons, débarras, chenilles, dépigeonnage et taupier.

## 2026-11-06 (soir)
- Mot-clé « dératiseur » (`_generateur/seo_deratiseur.py`) : titre, H1, description,
  introduction, un court passage et une question « Que fait un dératiseur ? » sur les
  59 pages « Dératisation + commune » et sur la page Dératisation ; titre, H1 et
  introduction des pages particuliers, agriculteurs, professionnels, agences et syndics,
  zones, contact, qui suis-je et accueil ; phrase d'introduction sur les pages contrats.
- 50 pages « prestation + commune » (`_generateur/services_villes.py`) :
  désinsectisation (12), chenilles processionnaires (10), taupier (10),
  dépigeonnage (8), piégeur agréé (10). Liens depuis chaque page prestation et
  depuis « Zones d'intervention » ; fil d'Ariane vers la prestation.
- Carte interactive sur « Zones d'intervention » : la Mayenne et l'Ille-et-Vilaine
  colorées en entier, Port-Brillet comme point de départ. Leaflet 1.9.4 servi par
  le site (`/leaflet/`), contours dans `assets/zone.geojson`
  (source : github.com/gregoiredavid/france-geojson). Mentions légales complétées.

## 2026-11-06
- Page « Dépigeonnage » : ajout du piégeage en cage (méthode, cadre, lien avec les
  protections) et de deux questions fréquentes.
- Menu « Mes services » : Dératisation, Désinsectisation et Piégeur agréé ressortent
  en orange avec un chevron, comme Débarras.
- Menu « Mes services » réordonné : Dératisation, Désinsectisation, les insectes,
  Taupier, Contrat annuel pro, puis Dépigeonnage, Piégeur agréé et Débarras.
  L'accueil et le pied de page gardent leur ordre.
- Bouton « Haut » en bas à gauche de l'écran : apparaît après 400 px de
  défilement et ramène en haut de page. Il ne gêne pas la mascotte, qui reste
  en bas à droite.

## 2026-11-05 — Mise en ligne
- Formulaire de contact basculé de FormSubmit vers Web3Forms (pas d'activation
  à cliquer) ; mentions légales mises à jour en conséquence.
- Site en ligne sur https://www.proxinuisibles.fr via Cloudflare Pages,
  relié à ce dépôt (branche `main`, dossier `public`).
- Le domaine est enregistré chez OVH mais géré par Cloudflare
  (serveurs de noms `augustus` et `jessica.ns.cloudflare.com`).
- Redirection de `proxinuisibles.fr` vers `https://www.proxinuisibles.fr` en 301
  (enregistrement AAAA `@` vers `100::` proxié + Redirect Rule Cloudflare).
- Formulaire de contact vérifié et fonctionnel.
- Reste à faire : supprimer le second enregistrement SPF (`include:sendgrid.net`),
  envoyer le sitemap dans la Search Console, nettoyer les restes de l'ancien
  hébergeur (`autoconfig`, `autodiscover`, DKIM `mandrill` et `smtpapi`).

## 2026-11-05 (soir)
- Vidéo de nid primaire en fond du haut de page sur « Frelons et guêpes ».
- Photo du badigeon en fond du haut de page sur « Mouches » ; la miniature de
  l'encart est retirée, sa légende passe dans le texte.
- « Débarras » revient dans le menu « Mes services », en orange avec un chevron.
- Menu « Mes services » resserré : il tient en entier sur un écran d'ordinateur
  portable (419 px au lieu de 575 px).

## 2026-11-05
- Site déplacé dans `public/` : Cloudflare publie ce dossier, le générateur reste privé.
- Première mise en ligne du dépôt : 267 pages, plus le générateur dans `_generateur/`.
- Hauts de page : la vidéo (ou la photo) remplace le bloc de couleur sur les pages
  qui en ont une ; dégradé avec lueur orange sur les autres. Page d'accueil laissée
  sans vidéo, en attente d'une vidéo dédiée.
- Nouvel onglet « Débarras » au premier niveau du menu.
- Section débarras : page principale plus 16 communes de l'axe Laval-Rennes,
  avec le traitement des nuisibles réalisé dans le même passage.
- Fouine développée sur les pages « Piégeur agréé » et « Agences et syndics ».
- 31 pages « frelons et guêpes » par commune, 15 pages « punaises de lit » par ville.
- Nouvelles pages : frelon asiatique, mouches (avec l'encart badigeon), puces,
  blattes et cafards, fourmis.
- Horaires, délai d'intervention, moyens de paiement et déplacement compris
  ajoutés sur la page contact, sur l'accueil et dans les données lues par Google.
- Avis Google réels affichés en bandeau défilant (5 avis, note 5/5, 118 avis).
- Encart du groupement Experts Guêpes et Frelons, avec logo et lien.
- Formulaire de contact (prénom, nom, e-mail, téléphone, message).
- Mentions légales complétées : hébergeur, assurance MAAF, données du formulaire,
  transferts hors Union européenne, cookies.
