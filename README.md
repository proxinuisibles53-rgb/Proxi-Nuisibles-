# Proxi Nuisibles — site proxinuisibles.fr

Site vitrine de Proxinuisibles (dératisation, désinsectisation, nids de frelons,
punaises de lit, débarras) en Mayenne et en Ille-et-Vilaine.

## Comment ça marche

Le site est **statique** : il n'y a ni base de données ni serveur applicatif.
Toutes les pages sont générées par un script Python, puis déposées telles quelles
à la racine de ce dépôt. Cloudflare Pages publie la racine automatiquement à
chaque envoi.

- **`public/`** : le site publié (`index.html`, `style.css`, `site.js`,
  `media/`, et un dossier par page). C'est ce dossier que Cloudflare met en ligne.
- **`_generateur/`** : le code qui produit le site. Ce dossier n'est pas publié.

## Régénérer le site

```bash
cd _generateur
python3 build.py      # écrit le site dans ./site
python3 preview.py    # produit un aperçu en un seul fichier HTML
```

Puis recopier le contenu de `_generateur/site/` dans `public/` et pousser.

## Contenu du générateur

| Fichier | Rôle |
|---|---|
| `build.py` | générateur principal : services, cibles, contacts, mentions légales, rendu HTML, CSS, sitemap |
| `communes_data.py` | communes principales (Laval, Rennes, Vitré…) |
| `communes20km.py` | communes dans un rayon de 20 km de Port-Brillet |
| `communes40_bouche.py` + `bouche40.json` | contrats boulangerie et boucherie dans un rayon de 40 km |
| `punaises_villes.py` | pages « punaises de lit » par ville |
| `frelons_villes.py` | pages « frelons et guêpes » par commune |
| `services_villes.py` | pages « désinsectisation, chenilles, taupier, dépigeonnage, piégeur agréé » par commune |
| `debarras.py` | section débarras (page principale + communes de l'axe Laval-Rennes) |
| `extras600.py` | sections complémentaires pour atteindre 600 à 800 mots par page |
| `mentions.py` | mentions EGalim, HACCP, méthodes, proofing, frise des contrats |
| `seo_deratiseur.py` | mot-clé « dératiseur » : titres, descriptions, introductions et questions des pages dératisation, publics et accueil (exécuté en dernier) |
| `assets/` | logos, médias, assistant, avis Google |

## Avis Google

Les avis affichés sur le site viennent de `_generateur/assets/avis.json`
(note moyenne, nombre total, et les avis repris de la fiche Google).
Ils sont intégrés au fichier `avis.js` lors de la génération.

## Déploiement

Cloudflare Pages est relié à ce dépôt et publie la branche `main` à chaque envoi.

Réglages du projet Cloudflare Pages :

| Réglage | Valeur |
|---|---|
| Branche de production | `main` |
| Préréglage de framework | Aucun (*None*) |
| Commande de compilation | *(vide)* |
| Répertoire de sortie | `public` |

`wrangler.jsonc` n'est utile que pour un déploiement en ligne de commande
(`npx wrangler deploy`) ; Cloudflare Pages ne s'en sert pas.
