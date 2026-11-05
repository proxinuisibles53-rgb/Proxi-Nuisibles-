# -*- coding: utf-8 -*-
import re
# Pages « contrat de dératisation » métiers de la bouche, par commune (faits vérifiés : Wikipédia, Wikivoyage, inventaires du patrimoine)
VILLES = {
 "vitre": ("Vitré", "35"), "saint-berthevin": ("Saint-Berthevin", "53"), "change": ("Changé", "53"), "louverne": ("Louverné", "53"),
 "argentre-du-plessis": ("Argentré-du-Plessis", "35"), "chateaubourg": ("Châteaubourg", "35"), "cesson-sevigne": ("Cesson-Sévigné", "35"),
}
VOISINS = {
 "vitre": ["argentre-du-plessis", "chateaubourg", "saint-berthevin"], "saint-berthevin": ["vitre", "change", "louverne"],
 "change": ["saint-berthevin", "louverne"], "louverne": ["change", "saint-berthevin"],
 "argentre-du-plessis": ["vitre", "chateaubourg"], "chateaubourg": ["vitre", "cesson-sevigne", "argentre-du-plessis"],
 "cesson-sevigne": ["chateaubourg", "vitre"],
}
# (commune, type, slug_metier, libellé court, lead, [(h2, texte)x3], (question, réponse), méta)
PG = [
("vitre", "restaurant", "restaurant", "restaurant",
 "Entre la rue de la Poterie, la rue Baudrairie et la place du Marchix, les restaurants de Vitré occupent des maisons médiévales à pans de bois, avec caves, escaliers étroits et arrière-cours. Ces bâtisses anciennes sont un terrain de choix pour les souris et les rats.",
 [("Des maisons à porches, des passages pour les rongeurs", "La rue de la Poterie compte neuf maisons à porches, la plus forte concentration de Bretagne. Leurs murs épais, leurs planchers anciens et leurs caves laissent aux rongeurs de nombreux passages entre les étages, les réserves et les gaines. Je fais un repérage complet : cave, trappes, arrière-cuisine, local poubelles, arrivées de canalisations."),
  ("La Vilaine et les ruisseaux de la ville", "Vitré est drainée par la Vilaine, la Valière et plusieurs ruisseaux (la Rousselière, le Gazon, le Herveleux, le Gontier). La vallée de la Vilaine forme un poumon vert qui sépare le centre historique des quartiers nord : les rats suivent ces berges et remontent vers les cuisines. Pour un restaurant proche de ces vallons, je place les points de contrôle côté cour et à la descente de cave."),
  ("Un contrat pensé pour la saison touristique", "Avec le château, la gare et les visiteurs d'été, la fréquentation de votre salle varie fortement. Le contrat prévoit des passages réguliers, un contrôle avant la haute saison et un compte rendu écrit après chaque visite, à conserver pour vos contrôles d'hygiène.")],
 ("Intervenez-vous dans une maison ancienne du centre médiéval ?", "Oui. Je privilégie des postes posés en retrait, sans toucher aux éléments anciens, et je vous indique les ouvertures à fermer avec l'accord du propriétaire."),
 "Contrat de dératisation pour restaurants à Vitré : rue de la Poterie, place du Marchix, caves anciennes. Passages réguliers, devis gratuit."),
("vitre", "boulangerie", "boulangerie-patisserie", "boulangerie-pâtisserie",
 "Farine, sucre, beurre, œufs : une boulangerie-pâtisserie réunit tout ce que cherchent souris et insectes. Dans le centre ancien de Vitré, autour des places du Château, Notre-Dame et de la Gare, les commerces occupent des bâtiments dont les caves et les laboratoires offrent de multiples cachettes.",
 [("Laboratoire et réserve de matières premières", "Sacs de farine posés sur palette, bacs de sucre, étagères du fournil : je contrôle les plinthes, les passages de câbles et le dessous des plans de travail, là où les souris nichent. Les mites alimentaires et les teignes sont aussi traitées, car elles prospèrent dans les stocks de farine et de fruits secs."),
  ("Les ruelles et les cours du centre ancien", "Les rues de la Baudrairie, de la Poterie et d'Embas se livrent tôt le matin, souvent par des cours étroites dont les portes restent ouvertes. Ce va-et-vient est une voie d'entrée directe pour les rongeurs. Je vous aide à repérer les ouvertures à fermer et les moments où votre local est le plus exposé."),
  ("Un suivi calé sur vos horaires", "Le contrat prévoit des passages avant l'ouverture, avec des produits adaptés aux locaux alimentaires, et un compte rendu écrit pour chaque visite.")],
 ("Faut-il arrêter la production pendant l'intervention ?", "En général non : je m'adapte à votre planning, souvent avant l'ouverture, et je vous indique si une zone doit rester libre quelques heures."),
 "Contrat de dératisation pour boulangeries-pâtisseries du centre ancien de Vitré : fournil, réserves, caves. Suivi écrit, devis gratuit."),
("vitre", "third", "boucherie-traiteur", "boucherie-traiteur",
 "Chambres froides, laboratoire de découpe, cuisine de préparation : une boucherie-traiteur de Vitré doit garder des locaux irréprochables, surtout les jours de réception et de grosses commandes pour les entreprises de l'agglomération.",
 [("Chambres froides, découpe et déchets", "Les déchets d'origine animale et les sous-produits de découpe attirent rats, mouches et cafards. Je contrôle le local à déchets, les siphons, les quais et les abords de la chambre froide, et je vous conseille sur la fréquence d'enlèvement."),
  ("Un territoire agricole tout proche", "Vitré est entourée de campagne d'élevage : Vitré Communauté regroupe environ 80 000 habitants sur 868 km². Les rats passent des exploitations aux zones d'activités puis aux commerces de bouche. Je pose des points de contrôle côté extérieur pour intercepter ceux qui viennent des champs."),
  ("Traiteur : livraisons et grosses commandes", "Le matériel de réception, les caisses de transport et les véhicules de livraison sont des refuges pour les insectes. Le contrat inclut le contrôle de ces zones annexes et un passage de vérification avant vos périodes de pointe.")],
 ("Pouvez-vous intervenir avant un événement important ?", "Oui. Appelez-moi quelques jours avant : je fais un contrôle complet des locaux et des zones de stockage."),
 "Contrat de dératisation pour boucheries et traiteurs de Vitré : chambres froides, découpe, livraisons. Devis gratuit."),

("saint-berthevin", "restaurant", "restaurant", "restaurant",
 "À Saint-Berthevin, les restaurants s'étendent entre le bourg, autour de la place de l'Europe, et les zones d'activités qui entourent la commune. Les rongeurs profitent des abords : haies, lisières de la forêt de Concise et berges du Vicoin.",
 [("Entre la forêt de Concise et le Vicoin", "Le sud de la commune est occupé par la forêt de Concise, et le Vicoin traverse le territoire. Ces espaces naturels hébergent des populations de rats qui s'approchent des bâtiments à la recherche de nourriture. Je pose les points de contrôle côté extérieur, près des haies, des bennes et des locaux poubelles."),
  ("Le midi, un flux dense autour des zones d'activités", "Saint-Berthevin compte onze zones d'activités, dont celle du Millénium. Les restaurants du midi reçoivent des salariés en grand nombre en peu de temps : les bennes se remplissent vite et les portes de service restent ouvertes. Un contrat régulier permet de repérer les signes avant qu'un client les voie."),
  ("Un suivi simple pour l'exploitant", "Le contrat prévoit un passage de contrôle à fréquence définie avec vous, un compte rendu écrit et une intervention rapide en cas de constat.")],
 ("Mon restaurant est près d'un champ ou d'un bois, est-ce un risque ?", "Oui, les abords végétalisés abritent des rats. Je renforce les contrôles côté extérieur et je vous conseille sur l'entretien des abords."),
 "Contrat de dératisation pour restaurants à Saint-Berthevin : bourg, zones d'activités, abords de la forêt de Concise. Devis gratuit."),
("saint-berthevin", "boulangerie", "boulangerie", "boulangerie",
 "Le bourg de Saint-Berthevin s'est construit autour de son église du XIe siècle. Ses commerces de proximité, dont les boulangeries, servent une population en croissance, entre résidentiel et zones d'activités.",
 [("Farine, sacs et bâtis anciens du bourg", "Dans un bourg ancien, les murs en pierre et les caves offrent des cheminements aux souris. Je contrôle le fournil, la réserve de farine et les passages vers les locaux voisins, et je vous conseille sur le stockage en bacs fermés."),
  ("Le chaufournier des Brosses et les anciennes carrières", "Les fours à chaux des Brosses, classés monument historique, et les anciennes carrières de marbre rose rappellent le passé industriel de la commune. Ces sites abandonnés, leurs cavités et leurs friches servent de refuge aux rongeurs, qui rejoignent ensuite les maisons et les commerces proches."),
  ("Livraisons et étals", "Les livraisons matinales, les portes ouvertes en été et les poubelles de quartier sont les principaux points d'entrée. Je les intègre au plan de passages du contrat.")],
 ("Les rongeurs peuvent-ils contaminer la farine ?", "Oui : ils souillent les stocks avec leurs urines et leurs déjections. Les sacs doivent être stockés fermés et surélevés, et je contrôle ces points à chaque passage."),
 "Contrat de dératisation pour boulangeries à Saint-Berthevin : bourg ancien, fournil, réserves. Passages réguliers, devis gratuit."),
("saint-berthevin", "third", "restauration-entreprise", "restauration d'entreprise",
 "Avec onze zones d'activités autour du bourg, Saint-Berthevin accueille de nombreuses entreprises, entrepôts et sociétés de services qui disposent d'un restaurant ou d'une salle de pause.",
 [("Cantines, entrepôts et sites de production", "Les restaurants d'entreprise cumulent gros volumes, livraisons fréquentes et zones de stockage. J'inspecte la cuisine, les réserves, les quais de livraison et les abords du site pour repérer les points d'entrée."),
  ("Bennes et locaux poubelles", "Les zones d'activités sont entourées de terrains enherbés, de haies et de bennes. Les rats s'y installent facilement. Je place les points de contrôle à l'extérieur du bâtiment, puis je vérifie leur fréquentation à chaque passage."),
  ("Traçabilité pour vos audits", "Le contrat fournit un plan de passages, un compte rendu écrit par visite et un suivi des interventions, utiles pour vos audits internes et vos contrôles d'hygiène.")],
 ("Pouvez-vous gérer plusieurs sites ?", "Oui, je propose un plan de passages unique avec un compte rendu par site."),
 "Contrat de dératisation pour restaurants d'entreprise à Saint-Berthevin : zones d'activités, entrepôts, cantines. Suivi écrit."),

("change", "restaurant", "restaurant", "restaurant",
 "Au nord de Laval, Changé s'étend sur les deux rives de la Mayenne, avec son parc des Ondines, ses bases de loisirs et son golf. Les restaurants et les cafés de la commune profitent d'un cadre de verdure et d'eau, mais les rats surmulots longent aussi les berges.",
 [("Les berges de la Mayenne et le parc des Ondines", "Le parc des Ondines, au bord de la rivière, attire promeneurs et mouettes, et laisse des déchets alimentaires aux abords. Les rats suivent ce corridor d'eau jusqu'aux cuisines proches. Je contrôle les arrière-cours, les bennes et les regards d'eaux usées côté rivière."),
  ("Un centre sur la rive droite, des lotissements sur les deux rives", "Le centre-ville est sur la rive droite de la Mayenne, alors que les lotissements pavillonnaires s'étalent sur les deux rives. Les restaurants de quartier travaillent avec une clientèle d'habitués, et les livraisons se font souvent par la cour : un point d'entrée classique."),
  ("Restauration de loisirs", "Autour du golf et des bases de loisirs, l'activité est saisonnière et les fins de semaine sont chargées. Le contrat prévoit un contrôle avant la saison et des passages réguliers ensuite.")],
 ("Les rats peuvent-ils venir de la rivière ?", "Oui, les berges sont un couloir de circulation. Je pose des points de contrôle côté rivière et je vous indique les ouvertures à fermer."),
 "Contrat de dératisation pour restaurants à Changé : berges de la Mayenne, parc des Ondines, golf. Passages réguliers, devis gratuit."),
("change", "boulangerie", "boulangerie", "boulangerie",
 "Le centre de Changé s'organise autour de l'église Saint-Pierre, du XIXe siècle, et du château, ancien prieuré, qui abrite aujourd'hui l'hôtel de ville. C'est là que travaillent les boulangeries, au service de clients venus des lotissements voisins.",
 [("Un centre-bourg à pied", "Dans un centre-bourg, les commerces se touchent : une souris qui entre dans un local passe vite chez le voisin par les gaines et les faux plafonds. Je contrôle votre fournil et je repère les cheminements qui rejoignent les locaux voisins."),
  ("Une commune fleurie, donc riche en insectes", "Changé a reçu trois fleurs au concours des villes et villages fleuris. Massifs, haies et jardinières attirent aussi fourmis, guêpes et mouches, qui se dirigent vers les vitrines de viennoiseries. Je traite les entrées d'insectes avec des produits adaptés aux locaux alimentaires."),
  ("Un contrat à votre mesure", "Un à plusieurs passages par an selon votre configuration, avec un compte rendu écrit à chaque fois.")],
 ("Les guêpes autour de ma vitrine, c'est aussi pour vous ?", "Oui, je traite aussi les nids de guêpes et de frelons autour des commerces."),
 "Contrat de dératisation pour boulangeries à Changé : centre-bourg, église Saint-Pierre, château. Insectes et rongeurs, devis gratuit."),
("change", "third", "cuisine-collective", "cuisine collective",
 "Changé accueille des établissements de santé et de loisirs, des écoles et des entreprises des zones industrielles au nord-est de la commune : autant de cuisines qui préparent chaque jour de nombreux repas.",
 [("Cuisine collective : un cahier des charges strict", "Plans de nettoyage, températures, traçabilité : les nuisibles doivent être maîtrisés dans un cadre précis. J'intègre le suivi des rongeurs et des insectes à votre plan de maîtrise sanitaire, avec des comptes rendus datés."),
  ("Établissements de santé et accès restreints", "Dans un établissement de santé, il faut respecter les accès, les horaires de service et le choix des produits. Je m'organise avec vous pour intervenir sans gêner l'activité."),
  ("Zones industrielles au nord-est", "Les restaurants d'entreprise des zones industrielles voisines sont exposés aux rongeurs qui circulent entre entrepôts, bennes et terrains enherbés. J'y place des points de contrôle extérieurs et je les relève à chaque passage.")],
 ("Pouvez-vous respecter un plan de maîtrise sanitaire ?", "Oui, j'intègre le suivi des nuisibles à votre plan de maîtrise sanitaire, avec des comptes rendus à chaque passage."),
 "Contrat de dératisation pour cuisines collectives à Changé : établissements de santé, écoles, restauration d'entreprise. Suivi écrit."),

("louverne", "restaurant", "restaurant", "restaurant",
 "Louverné est une commune de Laval Agglomération qui mêle bourg de pavillons, anciennes carrières de marbre noir, ruisseaux et campagne. Ses restaurants et ses cafés accueillent habitants, salariés et gens de passage.",
 [("Les ruisseaux de Barbé et de la Fresne", "Deux ruisseaux, celui de Barbé et celui de la Fresne, traversent le territoire. L'eau et la végétation des berges abritent des rats surmulots qui s'approchent des arrière-cours et des bennes. Je contrôle les abords côté eau, les regards et les locaux à déchets."),
  ("Des vestiges industriels", "Les anciennes carrières de marbre noir et un ancien four à chaux près de la gare rappellent l'histoire industrielle de la commune. Ces sites abandonnés offrent des cavités et des abris aux rongeurs, qui rejoignent ensuite les bâtiments proches."),
  ("Un contrat adapté aux petites structures", "Pour un café-restaurant de commune, je propose un nombre de passages adapté, un contrôle des points sensibles et un compte rendu écrit.")],
 ("Les anciens bâtiments posent-ils plus de problèmes ?", "Souvent oui : murs en pierre, planchers, caves et fissures offrent plus d'accès. Je repère les passages et je vous conseille sur les fermetures prioritaires."),
 "Contrat de dératisation pour restaurants et cafés à Louverné : ruisseaux, anciennes carrières, bourg. Devis gratuit."),
("louverne", "boulangerie", "boulangerie", "boulangerie",
 "La borne de banlieue de 1751, classée monument historique, marquait la limite du tarif de Laval : elle rappelle que Louverné vit depuis longtemps au rythme de sa grande voisine. Ses boulangeries servent les habitants du bourg et les salariés qui font la route.",
 [("Boulangerie de bourg : farine et sacs", "Une boulangerie de commune stocke souvent ses farines dans un local annexe ou à l'arrière du magasin. Je contrôle ces zones, les palettes et le sol, et je vous conseille sur les bacs fermés et la hauteur des stocks."),
  ("Livraisons tôt le matin", "Les livraisons de farine, de beurre et d'emballages se font avant l'ouverture, portes de service ouvertes. Je repère les moments où le local est le plus exposé et j'adapte les points de contrôle."),
  ("Après les travaux, des rongeurs délogés", "Dans une commune qui accueille des lotissements, les terrassements chassent les rongeurs vers les bâtiments voisins. Un passage de contrôle après un chantier proche évite les mauvaises surprises.")],
 ("Faut-il fermer le magasin pour un passage ?", "Non : je passe avant l'ouverture ou à un moment calme, et je vous indique les zones à laisser libres."),
 "Contrat de dératisation pour boulangeries à Louverné : bourg, farines, livraisons. Passages réguliers, devis gratuit."),
("louverne", "third", "boucherie", "boucherie",
 "Boucheries et charcuteries de Louverné : chambres froides, laboratoire de découpe et déchets d'origine animale demandent une hygiène sans faille. Je sécurise vos locaux avec un traitement adapté à l'alimentaire.",
 [("Chambres froides et découpe", "J'inspecte les joints de portes, les évacuations, les passages de câbles et le local à déchets, qui sont les points d'entrée classiques en boucherie."),
  ("Ruisseaux et campagne", "Les ruisseaux de Barbé et de la Fresne, ainsi que les champs voisins, favorisent la présence de rats. Je pose des points de contrôle à l'extérieur du commerce et je relève leur fréquentation à chaque passage."),
  ("La grotte et ses chauves-souris", "Une grotte préhistorique au sud de la commune abrite des chauves-souris, des espèces protégées. Elles ne sont jamais concernées par mes traitements : je distingue les animaux protégés des nuisibles avant toute intervention.")],
 ("Les mouches posent problème en boucherie, que proposez-vous ?", "Un traitement ciblé, adapté aux locaux alimentaires, et des conseils sur les entrées, les poubelles et la gestion des déchets."),
 "Contrat de dératisation pour boucheries à Louverné : chambres froides, découpe, déchets. Rongeurs et mouches, devis gratuit."),

("argentre-du-plessis", "restaurant", "restaurant", "restaurant",
 "Argentré-du-Plessis se trouve aux confins de la Bretagne et des Pays de la Loire, dans un territoire de bocage et d'étangs. Ses restaurants accueillent habitants, ouvriers, voyageurs et promeneurs.",
 [("Étangs et plan d'eau du Moulin Neuf", "La commune compte de nombreux étangs, dont l'étang de la Verrerie, et un plan d'eau de plus de cinq hectares au Moulin Neuf, avec sentier et pelouses. L'eau attire rats et insectes. Je contrôle les arrière-cours et les poubelles côté plan d'eau."),
  ("Les moulins et le bocage", "Les moulins aux Moines, Neuf et de Salé rappellent que l'eau a toujours structuré la commune. Les haies du bocage servent de corridor aux rongeurs, qui passent des champs aux hameaux puis aux commerces. Je pose des points de contrôle près des haies et des bennes."),
  ("Hameaux dispersés", "Un restaurant isolé en hameau est plus exposé : peu de voisins, beaucoup de verdure. Le contrat prévoit des passages réguliers et un compte rendu écrit.")],
 ("Intervenez-vous dans les hameaux ?", "Oui, je me déplace dans toute la commune et dans les communes voisines."),
 "Contrat de dératisation pour restaurants à Argentré-du-Plessis : étangs, moulins, bocage. Passages réguliers, devis gratuit."),
("argentre-du-plessis", "boulangerie", "boulangerie", "boulangerie",
 "Dans le bourg d'Argentré-du-Plessis, autour de l'église Notre-Dame reconstruite entre 1775 et 1779 après un incendie, les boulangeries travaillent dans un habitat ancien, souvent remanié.",
 [("Un bourg ancien", "L'habitat d'Argentré date en grande partie du XVIe au XIXe siècle, avec des murs épais et des remaniements successifs. Les souris y trouvent des cheminements. Je contrôle les caves, les plinthes et les gaines autour du fournil."),
  ("D'anciens sites de travail du bois", "La commune a abrité des usines de menuiserie, comme l'ancienne usine Rossignol. Les bâtiments industriels vides ou en travaux peuvent héberger des rongeurs, qui rejoignent ensuite les commerces proches."),
  ("Stockage et nettoyage", "Je vous conseille sur le stockage des farines en bacs fermés, le nettoyage sous les équipements et la gestion des invendus.")],
 ("Que faire si j'aperçois une souris en journée ?", "Appelez-moi : c'est souvent le signe d'une colonie installée. Je cherche l'origine et je mets en place le traitement."),
 "Contrat de dératisation pour boulangeries à Argentré-du-Plessis : bourg ancien, farines, fournil. Devis gratuit."),
("argentre-du-plessis", "third", "traiteur", "traiteur",
 "Dans une commune de plus de 4 000 habitants répartis sur 41 km2 de bocage, un traiteur livre dans des hameaux dispersés. Son laboratoire doit rester irréprochable, entre matières premières, matériel de réception et véhicules.",
 [("Laboratoire et stockage", "Je contrôle la cuisine de production, les réserves, les chambres froides et le stockage du matériel (vaisselle, tentes, tables), qui sert souvent de refuge aux insectes et aux souris."),
  ("Livraisons : la camionnette aussi", "Les rongeurs s'invitent parfois dans les véhicules et les caisses de transport. Le contrat inclut le contrôle de ces zones annexes."),
  ("Des manoirs et des châteaux privés", "Trois châteaux privés et plusieurs manoirs jalonnent la commune. Cette ambiance de campagne ancienne s'accompagne de bâtiments en pierre où les rongeurs s'installent vite : je vous conseille sur les points à surveiller.")],
 ("Intervenez-vous avant la saison des fêtes ?", "Oui, je recommande un passage de contrôle avant les périodes de forte activité."),
 "Contrat de dératisation pour traiteurs à Argentré-du-Plessis : laboratoire, stockage, véhicules. Devis gratuit."),

("chateaubourg", "restaurant", "restaurant", "restaurant",
 "La Vilaine coupe Châteaubourg en deux d'est en ouest. Sur ses rives, un ancien moulin enjambe la rivière et abrite aujourd'hui un hôtel-restaurant : l'eau fait partie du paysage, et de l'environnement des restaurants de la commune.",
 [("Une rivière au cœur de la commune", "Les berges de la Vilaine, les ponts et les parcs offrent des corridors aux rats surmulots. Je contrôle les arrière-cours, les regards et les locaux poubelles côté rivière, et je vous conseille sur les ouvertures à fermer."),
  ("Une commune village étape", "Châteaubourg est labellisée village étape : des automobilistes s'y arrêtent à l'heure des repas. Les pics d'affluence remplissent vite les bennes, ce qui attire les nuisibles. Un contrat régulier permet de garder la maîtrise."),
  ("Une commune très commerçante", "Avec ses zones commerciales et son centre-ville, Châteaubourg multiplie les restaurants et les lieux de restauration. Les nuisibles passent facilement de l'un à l'autre : mieux vaut un suivi dans la durée.")],
 ("Mon restaurant est au bord de la Vilaine, est-ce plus risqué ?", "Oui, l'eau attire les rats. Je renforce les contrôles côté rivière et je vous indique les points à surveiller au quotidien."),
 "Contrat de dératisation pour restaurants à Châteaubourg : Vilaine, village étape, zones commerciales. Devis gratuit."),
("chateaubourg", "boulangerie", "boulangerie", "boulangerie",
 "Châteaubourg est réputée très commerçante, avec son cinéma L'Étoile, ses commerces de centre-ville et ses zones commerciales. Les boulangeries travaillent dans un tissu dense, où les nuisibles circulent vite.",
 [("Autour de l'église Saint-Pierre", "L'église Saint-Pierre, bâtie en 1893 par Arthur Regnault et inscrite aux monuments historiques, marque le cœur de la commune. Autour, les commerces sont mitoyens : je contrôle les passages entre locaux et les gaines communes."),
  ("Grandes surfaces voisines", "Les zones commerciales attirent beaucoup de passage et génèrent des déchets. Les rongeurs qui s'y nourrissent rejoignent facilement les commerces voisins. Je pose des points de contrôle côté extérieur."),
  ("L'étang de Grand Fayelle et les moucherons", "À proximité de l'étang de Grand Fayelle, de 24 hectares, mouches et moucherons sont nombreux en été. Je vous conseille sur les protections aux ouvertures et je traite les entrées d'insectes.")],
 ("Faites-vous aussi les insectes ?", "Oui : mouches, fourmis, guêpes et cafards font partie de mes prestations."),
 "Contrat de dératisation pour boulangeries et commerces de bouche à Châteaubourg : centre-ville, zones commerciales. Devis gratuit."),
("chateaubourg", "third", "traiteur", "traiteur",
 "Châteaubourg a fusionné en 2014 avec Broons-sur-Vilaine et Saint-Melaine. Un traiteur qui travaille sur ces trois anciens bourgs fait de nombreuses tournées, entre laboratoire, camionnette et salles de réception.",
 [("Trois bourgs, des tournées de livraison", "Les livraisons passent par des rues et des cours variées : les rongeurs s'invitent facilement dans les véhicules et les caisses de transport. Le contrat inclut le contrôle du laboratoire et des zones annexes."),
  ("Des bâtiments anciens dans la commune", "Le manoir des Chesnelières (XVe siècle), le manoir de Montmorel et l'ancien prieuré rappellent que la commune est ancienne. Les bâtiments en pierre sont plus exposés aux souris : je vous conseille sur les points à surveiller."),
  ("Mouches et moucherons en été", "Les étangs et la Vilaine favorisent les insectes. Je traite les entrées et je vous donne des conseils d'hygiène adaptés à un laboratoire de traiteur.")],
 ("Puis-je prévoir des passages avant les événements ?", "Oui, nous planifions ensemble les passages en fonction de votre calendrier d'événements."),
 "Contrat de dératisation pour traiteurs à Châteaubourg : laboratoire, véhicules, insectes. Devis gratuit."),

("cesson-sevigne", "restaurant", "restaurant", "restaurant",
 "À Cesson-Sévigné, la Vilaine forme plusieurs bras et îlots sur onze kilomètres de berges, du port de Cesson au cours de la Vilaine, artère principale du vieux Cesson. Les restaurants de bord de rivière profitent de ce cadre, mais aussi des rats qui aiment l'eau.",
 [("Le cours de la Vilaine et le port de Cesson", "Autour du vieux port et des vieux ponts, les rats trouvent de la nourriture et des abris. Je contrôle les arrière-cours, les regards d'eaux pluviales et les locaux poubelles côté rivière."),
  ("Les parcs de la Chalotais et de la Monniais", "Le parc de la Chalotais, bordé par un ruisseau, et le parc de la Monniais, de 39 hectares, sont des espaces verts très fréquentés. Les restaurants proches voient des rongeurs qui circulent entre les bosquets et les terrasses. Je pose des points de contrôle côté jardin et terrasse."),
  ("Une clientèle du midi et du soir", "Le contrat prévoit un passage régulier, un contrôle des zones de stockage et un compte rendu écrit à chaque visite.")],
 ("Ma terrasse donne sur un parc, y a-t-il un risque ?", "Oui, les espaces verts attirent rats et insectes. Je vous conseille sur la gestion des déchets et la fermeture des accès."),
 "Contrat de dératisation pour restaurants à Cesson-Sévigné : berges de la Vilaine, port, parcs. Passages réguliers, devis gratuit."),
("cesson-sevigne", "boulangerie", "boulangerie-patisserie", "boulangerie-pâtisserie",
 "Autour de la place de l'église, du manoir de la Chalotais (aujourd'hui la mairie) et de l'église Saint-Martin de 1904, les boulangeries-pâtisseries du vieux Cesson travaillent dans des bâtiments du XIXe siècle.",
 [("Le vieux Cesson et ses bâtiments anciens", "Certaines maisons du cours de la Vilaine conservent d'anciennes portes de commerce, des vitrines du XIXe siècle et des gerbières à poulie. Ces bâtiments aux boiseries anciennes offrent des cachettes aux souris. Je contrôle les caves, les plinthes et les combles."),
  ("Pâtisserie : sucre, beurre et produits laitiers", "Le sucre, la crème et les fruits attirent fourmis, mouches et guêpes. Je traite les insectes avec des produits adaptés aux locaux alimentaires et je vous conseille sur le stockage et le nettoyage."),
  ("Un suivi régulier", "Passages à fréquence définie avec vous, compte rendu écrit et intervention rapide en cas de constat.")],
 ("Les fourmis reviennent chaque été, comment les arrêter ?", "Il faut traiter la colonie et fermer les entrées. Je repère les voies d'accès et je mets en place un traitement par appâts adapté à votre local."),
 "Contrat de dératisation pour boulangeries-pâtisseries à Cesson-Sévigné : vieux Cesson, fournil, insectes. Devis gratuit."),
("cesson-sevigne", "third", "restauration-entreprise", "restauration d'entreprise",
 "Rennes Atalante, sa tour TDF, la station de métro Atalante (ligne B) et le musée des Transmissions Espace Ferrié : le nord-est de Cesson-Sévigné est un pôle technologique où les restaurants d'entreprise accueillent chaque midi de nombreux salariés.",
 [("Sites high-tech, cuisines exigeantes", "Les entreprises de la technopole ont des exigences de qualité élevées. J'intègre le suivi des nuisibles à vos procédures, avec un plan de passages, des points de contrôle repérés et des comptes rendus datés."),
  ("Locaux techniques et abords", "Parkings, bennes, espaces verts et locaux techniques composent les abords des bâtiments. Les rongeurs profitent de ces zones calmes. Je place les points de contrôle à l'extérieur et je vérifie leur fréquentation à chaque visite."),
  ("Audits et traçabilité", "Un suivi écrit, daté et conservé facilite vos audits qualité et vos contrôles d'hygiène.")],
 ("Pouvez-vous intervenir en dehors des horaires de bureau ?", "Oui, nous convenons d'un créneau compatible avec votre service."),
 "Contrat de dératisation pour restaurants d'entreprise à Cesson-Sévigné : Rennes Atalante, cantines, audits. Suivi écrit."),
]

def _titre(metier_lab, ville):
    t = "Contrat Dératisation %s %s | Proxinuisibles" % (metier_lab.capitalize(), ville)
    if len(t) > 60:
        t = "Dératisation %s %s | Proxinuisibles" % (metier_lab.capitalize(), ville)
    if len(t) > 60:
        t = "Dératisation %s %s | Proxinuisibles" % (re.split(r"[ -]", metier_lab)[0].capitalize(), ville)
    if len(t) > 60:
        t = t.replace("Argentré-du-Plessis", "Argentré")
    return t

_by = {}
for v, kind, slug, lab, lead, secs, faq, meta in PG:
    _by[(v, kind)] = "/contrat-deratisation-%s-%s/" % (slug, v)
by_ville = {}
for v, kind, slug, lab, lead, secs, faq, meta in PG:
    by_ville.setdefault(v, []).append(("%s" % lab.capitalize(), "/contrat-deratisation-%s-%s/" % (slug, v)))

for v, kind, slug, lab, lead, secs, faq, meta in PG:
    nom, dep = VILLES[v]
    path = "/contrat-deratisation-%s-%s/" % (slug, v)
    voisins = [("Dératisation %s à %s" % (lab, VILLES[w][0]), _by[(w, kind)]) for w in VOISINS[v] if (w, kind) in _by][:3]
    autres = [(l, u) for l, u in by_ville[v] if u != path]
    links = [("Autres contrats de dératisation à %s" % nom, autres)]
    if voisins:
        links.append(("Communes voisines", voisins))
    links.append(("Voir aussi", [("Tous les contrats métiers de bouche", "/contrats-metiers-de-bouche/"), ("Contrat annuel professionnels", "/contrat-annuel-deratisation/"), ("Professionnels", "/professionnels/")]))
    add(path, h1="Contrat de dératisation %s à %s (%s)" % (lab, nom, dep), title=_titre(lab, nom), meta=meta, lead=lead, secs=secs, faq=[faq], links=links, kind="metier")

# page d'ensemble
hub_links = [("%s (%s)" % (VILLES[v][0], VILLES[v][1]), by_ville[v]) for v in VILLES]
add("/contrats-metiers-de-bouche/", h1="Contrats de dératisation pour les métiers de la bouche autour de Laval et de Vitré",
    title="Contrats Dératisation Métiers de Bouche | Proxinuisibles",
    meta="Contrats de dératisation pour restaurants, boulangeries, boucheries, traiteurs et cuisines collectives autour de Laval et de Vitré.",
    lead="Restaurants, boulangeries, boucheries, traiteurs, restauration d'entreprise : choisissez votre commune pour voir comment j'adapte le contrat aux lieux, aux cours d'eau et aux bâtiments de votre secteur.",
    secs=[("Pourquoi une page par commune", "Une cave de maison à porches à Vitré, une terrasse au bord de la Mayenne à Changé ou un restaurant d'entreprise de la technopole de Cesson-Sévigné n'ont pas les mêmes risques. Chaque page décrit les situations propres à la commune.")],
    links=hub_links, faq=[("Comment fonctionne un contrat de dératisation ?", "Je réalise un diagnostic, je pose les points de contrôle, puis je passe à fréquence définie avec vous. Chaque visite donne lieu à un compte rendu écrit. Le devis est gratuit.")], kind="cible")

# liens depuis les pages villes existantes vers leurs contrats métiers de bouche
for _v, _slug in (("vitre", "vitre"), ("saint-berthevin", "saint-berthevin"), ("chateaubourg", "chateaubourg"), ("cesson-sevigne", "cesson-sevigne")):
    P["/deratisation-%s/" % _slug]["links"].append(("Contrats de dératisation métiers de bouche à %s" % VILLES[_v][0], by_ville[_v]))

# image du contrat de dératisation pour les professionnels : pages contrats métiers de bouche (+ famille Laval et contrat annuel)
MEDIA_EXTRA = {}
_CONTRAT_PATHS = [p for p in P if p.startswith("/contrat-deratisation-")] + ["/contrats-metiers-de-bouche/", "/contrat-annuel-deratisation/"] + \
    ["/deratisation-%s-laval/" % m for m in ("restaurant", "boulangerie", "boucherie", "traiteur", "cuisine-collective")]
for _p in _CONTRAT_PATHS:
    if _p in P:
        MEDIA_EXTRA[_p] = ("image", "contrat-deratisation-pro",
                     "Contrat de dératisation Proxinuisibles pour les professionnels, posé sur une planchette à côté d'un boîtier de dératisation, avec un technicien en tenue de la marque en arrière-plan",
                     "Le contrat de dératisation pour les professionnels : des passages réguliers et un suivi écrit.", 760)
