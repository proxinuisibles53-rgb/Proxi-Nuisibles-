# -*- coding: utf-8 -*-
# Pages « dératisation » des communes situées à moins de 20 km de Port-Brillet (distances centre à centre, calcul sur contours officiels)
# (slug, nom, dép, km, lead, [(h2, texte)x3], [(q, r)x2], [voisins])
FICHES = []
def F(*a): FICHES.append(a)

F("olivet", "Olivet", "53", 2.2,
  "Olivet est un village d'environ 400 habitants, à deux kilomètres de Port-Brillet, où l'entreprise est installée. Fermes, bois, étangs et hameaux dispersés : voici ce qu'il faut savoir sur les rongeurs et les autres nuisibles du secteur.",
  [("Pourquoi des rongeurs à Olivet", "Olivet est une commune rurale à habitat dispersé : un peu plus de 400 habitants sur une dizaine de kilomètres carrés. Les fermes, les granges et les maisons isolées sont séparées par des haies, des bois et des étangs. Les rats et les souris passent d'un bâtiment à l'autre sans jamais traverser de zone bâtie, ce qui rend les infestations discrètes et la prévention plus difficile."),
   ("L'abbaye de Clermont et les bâtiments en pierre", "L'ancienne abbaye cistercienne de Clermont, fondée en 1152, a été installée au milieu des bois et des étangs, et son enclos conserve encore des aménagements hydrauliques. Cette ambiance de pierre, d'eau et de végétation se retrouve dans les propriétés anciennes de la commune : murs épais, caves, dépendances. Ce sont des lieux où souris et rats s'installent volontiers, et où je vous conseille sur les ouvertures à fermer."),
   ("Autres nuisibles à Olivet", "Les arbres, les haies et les vieux vergers abritent des nids de guêpes et de frelons, parfois dans les toitures ou les appentis. Les prairies et les jardins attirent aussi les taupes. J'interviens pour tous ces nuisibles, sans que vous ayez à chercher plusieurs prestataires.")],
  [("Olivet fait-elle partie de votre secteur proche ?", "Oui : Olivet se trouve à environ 2 km de Port-Brillet, où je suis installé. Les déplacements sont très courts, même pour une petite intervention."),
   ("Intervenez-vous dans les fermes isolées d'Olivet ?", "Oui. J'inspecte les bâtiments, les stocks et les abords, puis je propose un traitement adapté à l'exploitation.")],
  ["port-brillet-voisins", "la-brulatte", "le-genest-saint-isle", "saint-ouen-des-toits"])

F("la-brulatte", "La Brûlatte", "53", 3.6,
  "La Brûlatte compte environ 670 habitants sur plus de 15 km², à moins de quatre kilomètres de Port-Brillet. Le bourg et ses nombreux hameaux sont entourés de champs et de bois : un cadre où les rongeurs ne manquent jamais de passages.",
  [("Une commune agricole à habitat dispersé", "Plus de la moitié du territoire est agricole et environ 44 % relève d'espaces naturels : le bâti ne représente qu'à peu près 3 % de la surface communale. Hangars, étables, silos et maisons de hameau se trouvent donc au contact direct des champs et des haies, d'où les rats et les souris arrivent facilement."),
   ("Un cadre naturel à respecter", "La Brûlatte abrite deux zones naturelles d'intérêt écologique, faunistique et floristique (ZNIEFF). Dans une commune qui garde le souvenir de la forêt qui la couvrait autrefois, je choisis des produits et des emplacements adaptés au lieu, en privilégiant la protection des abords et des animaux domestiques."),
   ("Autres nuisibles à La Brûlatte", "Les granges et les bâtiments agricoles attirent les pigeons, qui salissent les toitures et les stocks. Dans les jardins du bourg et des hameaux, les nids de guêpes se logent dans les haies, les murs et les abris. Je traite aussi les taupes dans les prairies et les pelouses.")],
  [("La Brûlatte est-elle proche de votre base ?", "Oui, à environ 3,6 km de Port-Brillet. Vous êtes parmi les communes que je rejoins le plus vite."),
   ("Intervenez-vous dans les hameaux de La Brûlatte ?", "Oui. Les hameaux sont fréquents sur la commune : donnez-moi l'adresse, je m'y rends.")],
  ["olivet", "port-brillet-voisins", "le-genest-saint-isle", "saint-pierre-la-cour"])

F("launay-villiers", "Launay-Villiers", "53", 3.8,
  "Launay-Villiers est une petite commune d'environ 350 habitants, voisine immédiate de Port-Brillet, où je suis installé. Entre château, hameaux et prairies bordées par le Vicoin, voici les nuisibles que je rencontre le plus souvent dans le secteur.",
  [("Pourquoi des rongeurs à Launay-Villiers", "Avec ses 9 km² et son habitat dispersé, Launay-Villiers est faite de fermes, de maisons de hameau et de dépendances anciennes. Le Vicoin forme la limite ouest de la commune : les berges et les haies servent de couloir aux rats surmulots, qui rejoignent ensuite les granges, les poulaillers et les garages."),
   ("Des bâtiments anciens en pierre", "Le château de Villiers, dont il reste des vestiges du XIVe siècle avec son pigeonnier, et l'église de la Trinité, du XVIIe siècle, rappellent que la commune compte beaucoup de bâtiments anciens. Dans les murs épais, les combles et les dépendances, les souris et les loirs trouvent des passages. Je vous explique quelles ouvertures fermer et comment protéger les stocks."),
   ("Autres nuisibles à Launay-Villiers", "Les toitures anciennes et les pigeonniers désaffectés attirent les pigeons, dont les fientes abîment les charpentes. Les nids de frelons se cachent souvent dans les vieux arbres et les dépendances. Je traite aussi les taupes dans les prairies de la commune.")],
  [("Intervenez-vous à Launay-Villiers pour un seul nid de guêpes ?", "Oui. La commune est à moins de quatre kilomètres de Port-Brillet : le déplacement est court, même pour une petite intervention."),
   ("Peut-on traiter des loirs dans un grenier ?", "Oui, je commence par un diagnostic : repérage des passages, des dégâts et des déjections, puis je propose la solution adaptée, souvent mêlant fermeture des accès et piégeage.")],
  ["saint-pierre-la-cour", "le-bourgneuf-la-foret", "bourgon", "olivet"])

F("saint-pierre-la-cour", "Saint-Pierre-la-Cour", "53", 4.6,
  "Saint-Pierre-la-Cour compte environ 2 300 habitants sur près de 16 km², à moins de cinq kilomètres de Port-Brillet. Entre bourg résidentiel, étangs et carrière de la cimenterie, la commune offre aux rongeurs et aux insectes des terrains très variés.",
  [("Pourquoi des rongeurs à Saint-Pierre-la-Cour", "La commune réunit un bourg de lotissements, des hameaux agricoles et plusieurs étangs : les deux étangs du Moulin Neuf et l'étang de la Forge, de 33 hectares. L'eau et les berges herbeuses attirent les rats surmulots, qui s'approchent des jardins, des composteurs et des abris à poules. Dans les lotissements récents, les souris s'installent dans les garages et les combles."),
   ("Une cimenterie et une grande carrière", "La cimenterie installée sur la commune, avec sa très grande carrière, s'accompagne d'activités et de bâtiments techniques. Les locaux d'entreprise, les stockages et les abords des sites industriels sont des lieux où les rongeurs circulent. Je propose aux professionnels des contrôles réguliers avec un compte rendu écrit."),
   ("Autres nuisibles à Saint-Pierre-la-Cour", "L'étang de la Forge est classé zone naturelle d'intérêt écologique, notamment pour la châtaigne d'eau : je choisis des produits et des emplacements adaptés aux abords sensibles. Dans les jardins, les nids de guêpes et de frelons sont fréquents, de même que les taupes dans les pelouses.")],
  [("Saint-Pierre-la-Cour fait-elle partie de votre secteur proche ?", "Oui, à environ 4,6 km de Port-Brillet. Je me rends vite chez les particuliers comme chez les professionnels."),
   ("Intervenez-vous près des étangs ?", "Oui. Les abords de plans d'eau demandent des précautions : je choisis le matériel et les emplacements pour protéger la faune et les animaux domestiques.")],
  ["launay-villiers", "la-brulatte", "la-gravelle", "bourgon"])

F("le-bourgneuf-la-foret", "Le Bourgneuf-la-Forêt", "53", 4.9,
  "Le Bourgneuf-la-Forêt compte environ 1 770 habitants sur près de 29 km², à cinq kilomètres de Port-Brillet. Étangs, parc, château et bocage : un territoire rural où les rongeurs et les insectes ne manquent pas de refuges.",
  [("Pourquoi des rongeurs au Bourgneuf-la-Forêt", "Le Vicoin prend sa source sur la commune, et plusieurs étangs ponctuent le paysage, dont celui de Morfelon avec son coin pique-nique et son parcours botanique. L'eau, les roselières et les haies sont des couloirs de circulation pour les rats surmulots, qui rejoignent ensuite les jardins, les poulaillers et les bâtiments agricoles. Les souris, elles, s'invitent dans les maisons dès les premiers froids."),
   ("La Vallée des Étangs et le château de Fresnay", "Une partie de la commune appartient au site classé de la Vallée des Étangs, que le Bourgneuf partage avec Launay-Villiers et Port-Brillet. Le château de Fresnay, du XVIIIe siècle, avec son canal, son vivier et son pigeonnier, illustre la richesse du bâti ancien et de ses dépendances. Dans ces cadres sensibles, je choisis des emplacements discrets et des produits adaptés pour protéger la faune et les animaux domestiques."),
   ("Autres nuisibles au Bourgneuf-la-Forêt", "Avec 28 km² de bocage, les fermes et les hangars accueillent aussi les pigeons et les étourneaux. Je traite les nids de frelons et de guêpes dans les arbres et sous les toitures, ainsi que les taupes dans les prairies et les pelouses.")],
  [("Le Bourgneuf-la-Forêt est-il dans votre zone proche ?", "Oui, à environ 5 km de Port-Brillet. Je m'y rends facilement, que ce soit dans le bourg ou dans un hameau."),
   ("Intervenez-vous dans les exploitations agricoles de la commune ?", "Oui. J'inspecte les bâtiments, les stocks et les points d'eau, puis je propose un traitement adapté à l'exploitation.")],
  ["launay-villiers", "saint-ouen-des-toits", "la-baconniere", "olivet"])

F("le-genest-saint-isle", "Le Genest-Saint-Isle", "53", 5.4,
  "Le Genest-Saint-Isle compte environ 2 200 habitants sur 18,6 km², à cinq kilomètres de Port-Brillet. Née du rapprochement du Genest et de Saint-Isle, la commune mêle bourg résidentiel, bocage et vallée du Vicoin.",
  [("Deux bourgs, deux ambiances", "Le Genest et Saint-Isle ont fusionné en 1972. Le Genest est un bourg plus résidentiel, avec sa gare et son église Saint-Sulpice. Saint-Isle, petit bourg perché au sommet d'une colline, descend jusqu'au Vicoin et s'intègre au bocage. Dans le premier, les souris profitent des garages et des combles de pavillons. Dans le second, les rats viennent de la rivière et des haies."),
   ("Le Vicoin et le bocage", "Le Vicoin borde la commune, et les prairies en pente, les haies et les fossés forment des couloirs pour les rongeurs. Les fermes, les hangars et les maisons de hameau en profitent : rats près des stocks de céréales, souris dans les dépendances. Je repère l'origine du passage avant de proposer un traitement."),
   ("Autres nuisibles au Genest-Saint-Isle", "Avec une densité plus forte qu'à la campagne profonde, la commune compte beaucoup de jardins de lotissement où les nids de guêpes et les fourmis sont fréquents. Je traite aussi les nids de frelons dans les arbres, les chenilles processionnaires sur les pins de jardin et les taupes dans les pelouses.")],
  [("Intervenez-vous au Genest comme à Saint-Isle ?", "Oui. Les deux bourgs sont à quelques kilomètres de Port-Brillet : indiquez-moi l'adresse, je me déplace dans les deux."),
   ("Que faire si j'entends des bruits dans mon plafond ?", "Ne mettez pas de produit au hasard : je viens identifier l'animal (souris, rat, loir) puis je propose une solution adaptée, avec fermeture des accès.")],
  ["olivet", "la-brulatte", "saint-ouen-des-toits", "la-gravelle"])

F("saint-ouen-des-toits", "Saint-Ouën-des-Toits", "53", 5.8,
  "Saint-Ouën-des-Toits compte environ 1 800 habitants sur 21 km², à moins de six kilomètres de Port-Brillet. Entre bocage, vieux bourg et site de la Closerie des Poiriers, la commune offre aux nuisibles un terrain varié.",
  [("Pourquoi des rongeurs à Saint-Ouën-des-Toits", "À la lisière de la région forestière qui s'étend vers la Bretagne, Saint-Ouën-des-Toits est faite de bois, de haies et de fermes. Les rats et les souris passent facilement des lisières aux hangars, aux granges et aux maisons de hameau. Dans le bourg, les anciennes bâtisses en pierre et leurs dépendances offrent d'autres abris."),
   ("Un passé qui laisse des vieilles pierres", "La commune abrite la Closerie des Poiriers, où vécut Jean Chouan et sa famille, devenue musée de la Chouannerie. Elle a aussi un château du Moyen Âge, l'une des dix châtellenies du comté de Laval, dont subsistent des ruines de remparts visibles depuis un sentier de promenade. Ces bâtiments anciens et leurs abords rappellent que les maisons en pierre épaisse sont plus exposées aux souris et aux loirs."),
   ("Autres nuisibles à Saint-Ouën-des-Toits", "Je traite aussi les nids de frelons et de guêpes dans les arbres et les toitures, les pigeons dans les granges et les taupes dans les prairies. Pour un bâtiment ouvert au public ou une exploitation, je propose un suivi à fréquence définie avec compte rendu écrit.")],
  [("Saint-Ouën-des-Toits fait-elle partie de votre secteur proche ?", "Oui, à environ 6 km de Port-Brillet. Je me déplace rapidement dans le bourg comme dans les hameaux."),
   ("Intervenez-vous dans un musée ou un bâtiment ouvert au public ?", "Oui, avec un diagnostic préalable et des méthodes adaptées à la fréquentation du lieu. Appelez-moi pour en parler.")],
  ["olivet", "le-genest-saint-isle", "le-bourgneuf-la-foret", "saint-germain-le-fouilloux"])

F("la-gravelle", "La Gravelle", "53", 6.3,
  "La Gravelle est un petit village d'environ 560 habitants, à l'extrême ouest de la Mayenne, en limite d'Ille-et-Vilaine. Elle se trouve à 6 km de Port-Brillet, sur l'axe Laval-Rennes : un lieu de passage où les nuisibles se déplacent comme les voyageurs.",
  [("Pourquoi des rongeurs à La Gravelle", "La rivière Oudon prend sa source sur la commune : les fossés, les ruisseaux naissants et les prairies humides sont des couloirs de circulation pour les rats surmulots. Ils rejoignent ensuite les maisons du bourg, les jardins et les bâtiments agricoles. Dans les maisons plus anciennes, les souris s'invitent dans les caves et les combles."),
   ("Un axe de passage et une zone d'activités", "La commune est située sur l'axe autoroutier entre Rennes et Laval, et la zone d'activités des Pavés y accueille des entreprises. Entrepôts, ateliers et locaux de restauration sont des cibles pour les rongeurs. Je propose des contrôles réguliers avec compte rendu écrit pour les professionnels."),
   ("Autres nuisibles à La Gravelle", "Dans un village où les jardins touchent les champs, les nids de guêpes et de frelons sont fréquents dans les haies, les appentis et les arbres. Je traite aussi les taupes dans les pelouses et les prairies, ainsi que les fourmis et les cafards dans les logements.")],
  [("La Gravelle est-elle dans votre zone d'intervention ?", "Oui, elle se trouve à environ 6 km de Port-Brillet. Je me déplace aussi dans les communes voisines d'Ille-et-Vilaine."),
   ("Intervenez-vous pour les entreprises de la zone d'activités ?", "Oui. Je propose un diagnostic, la pose de points de contrôle et des passages réguliers, avec un compte rendu écrit à chaque visite.")],
  ["saint-pierre-la-cour", "la-brulatte", "breal-sous-vitre", "loiron-ruille"])

F("loiron-ruille", "Loiron-Ruillé", "53", 7.2,
  "Loiron-Ruillé compte environ 2 750 habitants sur près de 40 km² : c'est l'une des plus grandes communes du secteur, à sept kilomètres de Port-Brillet. Née en 2016 de la fusion de Loiron et de Ruillé-le-Gravelais, elle réunit deux bourgs anciens et un vaste bocage.",
  [("Deux bourgs, un grand territoire agricole", "Loiron, à l'est, est le bourg le plus important, avec son église Saint-Gervais-et-Saint-Protais dont les parties les plus anciennes datent du XIe siècle. Ruillé-le-Gravelais, plus à l'ouest, est traversé par l'Oudon. Autour des deux bourgs, fermes, hangars, silos et prairies offrent aux rats et aux souris des cheminements ininterrompus, des haies jusqu'aux bâtiments."),
   ("Des bâtiments anciens en pierre", "La maison de la Forge, du XVe siècle, avec sa porte ogivale, la chapelle de la Charbonnerie ou le châtelier de Loiron rappellent que le bourg compte beaucoup de constructions anciennes. Dans ces murs épais, les caves, les combles et les dépendances sont des abris pour les souris, les loirs et parfois les rats. Je vous conseille sur les ouvertures à fermer avant de traiter."),
   ("Autres nuisibles à Loiron-Ruillé", "Les commerces et les restaurants du bourg ont besoin d'un suivi régulier, surtout les commerces de bouche. Dans les jardins et les fermes, je traite aussi les nids de guêpes et de frelons, les pigeons dans les granges et les taupes dans les prairies.")],
  [("Loiron-Ruillé est-elle dans votre secteur proche ?", "Oui, à environ 7 km de Port-Brillet. Je me déplace à Loiron, à Ruillé et dans les hameaux."),
   ("Proposez-vous un contrat pour les commerces de Loiron ?", "Oui. Pour un restaurant, une boulangerie ou un commerce de bouche, je propose des passages réguliers et un compte rendu écrit à chaque visite.")],
  ["la-gravelle", "saint-cyr-le-gravelais", "la-baconniere", "bourgon"])

F("bourgon", "Bourgon", "53", 7.4,
  "Bourgon compte un peu plus de 600 habitants répartis sur 21 km², à sept kilomètres de Port-Brillet. L'habitat y est très dispersé et l'élevage occupe une grande place : un cadre où les rongeurs trouvent facilement de quoi se nourrir.",
  [("Une commune d'élevage à habitat très dispersé", "Les exploitations pratiquent la polyculture et l'élevage de bovins, de porcs et de volailles. Stockage de céréales, aliments du bétail, litières et eau : ce sont autant d'attraits pour les rats et les souris. Avec des fermes et des hameaux éloignés les uns des autres, un problème de rongeurs peut s'installer longtemps avant d'être vu."),
   ("Ruisseaux, moulins et limite d'Ille-et-Vilaine", "Au sud, un chemin marque la limite entre la Mayenne et l'Ille-et-Vilaine. Au bord du ruisseau, l'ancien moulin de Bourgon et celui de Choiseau rappellent le rôle de l'eau dans la vie de la commune. Ces abords humides, avec leurs bâtiments en pierre, sont des endroits où les rats et les souris s'installent volontiers."),
   ("Autres nuisibles à Bourgon", "Dans les exploitations, les pigeons et les étourneaux s'invitent dans les bâtiments d'élevage. Je traite aussi les nids de guêpes et de frelons dans les arbres du bocage, ainsi que les taupes dans les prairies.")],
  [("Intervenez-vous dans les exploitations d'élevage de Bourgon ?", "Oui. Je contrôle les bâtiments, les stocks et les points d'eau, je pose des points de dératisation et je propose des passages réguliers."),
   ("Bourgon est-elle loin de votre base ?", "Non : elle se trouve à environ 7 km de Port-Brillet. Les déplacements restent courts, même dans les hameaux les plus isolés.")],
  ["launay-villiers", "saint-pierre-la-cour", "le-bourgneuf-la-foret", "la-chapelle-erbree"])

F("la-baconniere", "La Baconnière", "53", 7.6,
  "La Baconnière a gagné plus de 800 habitants depuis 1990 : près de 2 000 aujourd'hui, sur 27 km². À huit kilomètres de Port-Brillet, entre bocage, lotissements récents et route de Laval à Ernée, la commune cumule les terrains favorables aux rongeurs.",
  [("Une commune qui s'agrandit", "Les nouveaux lotissements se sont développés autour du bourg, au contact direct des champs et des haies. Les travaux de terrassement chassent les rongeurs vers les maisons voisines, et les souris profitent des garages, des combles et des vides techniques des constructions récentes. Un traitement préventif après un chantier proche évite bien des surprises."),
   ("Anciens fours à chaux et carrières d'argile", "Le blason de la commune rappelle d'anciens fours à chaux et des carrières d'argile, et la commune repose sur le bassin houiller de Laval. Ces anciens sites d'extraction, avec leurs talus, leurs friches et leurs cavités, servent de refuge aux rats, qui rejoignent ensuite les bâtiments proches. Le bourg, traversé par la route départementale de Laval à Ernée, voit aussi passer beaucoup de véhicules et de livraisons."),
   ("Autres nuisibles à La Baconnière", "Dans les lotissements et les jardins, les nids de guêpes et de frelons, les fourmis et les taupes sont les demandes les plus fréquentes. Les fermes de la commune ont aussi des problèmes de pigeons dans les hangars et de rongeurs dans les stocks.")],
  [("La Baconnière est-elle dans votre secteur ?", "Oui, à environ 8 km de Port-Brillet. Je me déplace dans le bourg, les lotissements et les hameaux."),
   ("Peut-on faire traiter les rongeurs après des travaux ?", "Oui. Je repère les passages, je pose des points de contrôle et je ferme les accès quand c'est possible, pour éviter que les rongeurs s'installent durablement.")],
  ["saint-ouen-des-toits", "le-bourgneuf-la-foret", "saint-hilaire-du-maine", "chailland"])

F("saint-cyr-le-gravelais", "Saint-Cyr-le-Gravelais", "53", 9.7,
  "Saint-Cyr-le-Gravelais est un petit village d'environ 570 habitants sur près de 20 km², à moins de dix kilomètres de Port-Brillet. Le bourg est entouré de prairies, de hameaux et de fossés bordant l'Oudon : un cadre très favorable aux rats et aux souris.",
  [("Pourquoi des rongeurs à Saint-Cyr-le-Gravelais", "L'Oudon forme une partie de la limite nord de la commune. Les berges, les fossés et les haies servent de couloirs aux rats surmulots, qui rejoignent ensuite les fermes, les granges et les maisons de hameau. Avec moins de trente habitants au kilomètre carré, les bâtiments sont isolés, ce qui donne aux rongeurs de longs moments de tranquillité avant d'être repérés."),
   ("Une église qui rappelle la peste de 1751", "À l'intérieur de l'église Saint-Cyr-et-Sainte-Julitte, la statue de saint Sébastien commémore la protection que la paroisse aurait obtenue lors d'une épidémie de peste en 1751. Cette histoire rappelle que les rats ont longtemps été associés aux grandes épidémies. Aujourd'hui encore, une infestation de rats n'est jamais anodine : ils souillent les stocks et peuvent transmettre des maladies."),
   ("Autres nuisibles à Saint-Cyr-le-Gravelais", "Les haies, les vergers et les dépendances abritent des nids de guêpes et de frelons. Je traite aussi les taupes dans les prairies et les pelouses, les pigeons dans les granges et les fourmis ou les cafards dans les habitations.")],
  [("Intervenez-vous dans une commune aussi petite ?", "Oui. Quelle que soit la taille de la commune, je me déplace : Saint-Cyr-le-Gravelais est à moins de dix kilomètres de Port-Brillet."),
   ("Que faire si je trouve des déjections dans ma grange ?", "Ne balayez pas à sec : portez des gants, humidifiez et nettoyez avec précaution. Appelez-moi pour un diagnostic : je repère l'espèce et les accès avant de traiter.")],
  ["la-gravelle", "loiron-ruille", "montjean", "beaulieu-sur-oudon"])

F("breal-sous-vitre", "Bréal-sous-Vitré", "35", 7.9,
  "Bréal-sous-Vitré est un petit village d'environ 610 habitants, à l'extrême est de l'Ille-et-Vilaine, à huit kilomètres de Port-Brillet. Collé à la Mayenne et à la lisière de la forêt du Pertre, il offre aux rongeurs et aux insectes un mélange de bois, de champs et de bourg.",
  [("Entre forêt du Pertre et carrière de Saint-Pierre-la-Cour", "La commune est située tout près de la grande carrière de Saint-Pierre-la-Cour et à la lisière nord de la forêt du Pertre. Les lisières, les friches et les talus sont des zones de passage pour les rats, qui rejoignent ensuite les maisons du bourg, les dépendances et les fermes. Avec seulement 5,75 km², le bourg et les hameaux sont proches des champs : les rongeurs n'ont jamais loin à aller."),
   ("Un bourg ancien qui garde la mémoire du passé", "Le cimetière médiéval de Bréal-sous-Vitré, avec ses tombes-coffres en ardoise, a fait l'objet d'une étude historique et archéologique approfondie. Cette ancienneté se retrouve dans les maisons et les dépendances en pierre, où les souris trouvent les mêmes cachettes que dans tous les bâtiments anciens : murs épais, combles, caves."),
   ("Autres nuisibles à Bréal-sous-Vitré", "Je traite aussi les nids de guêpes et de frelons dans les haies et sous les toitures, les taupes dans les pelouses et les prairies, ainsi que les fourmis, les puces et les cafards dans les logements.")],
  [("Intervenez-vous en Ille-et-Vilaine comme en Mayenne ?", "Oui. Bréal-sous-Vitré est à environ 8 km de Port-Brillet : la frontière départementale ne change rien à mes déplacements."),
   ("Y a-t-il un risque de rats près de la forêt ?", "Oui. Les lisières sont des zones de passage. Je pose des points de contrôle côté extérieur et je vous conseille sur l'entretien des abords.")],
  ["la-gravelle", "saint-pierre-la-cour", "mondevert", "erbree"])

F("la-chapelle-erbree", "La Chapelle-Erbrée", "35", 9.6,
  "La Chapelle-Erbrée compte environ 700 habitants sur 12 km², dans les Marches de Bretagne, à moins de dix kilomètres de Port-Brillet. Entre la limite de la Mayenne, les hauteurs de campagne et l'étang de Haute-Vilaine, la commune réunit tout ce qui attire rats et souris.",
  [("L'étang de Haute-Vilaine et ses abords", "L'étang de Haute-Vilaine, partagé avec Saint-M'Hervé, sert à la fois à limiter les crues et de réserve d'eau potable. Les berges, les roselières et les fossés qui l'alimentent sont des couloirs naturels pour les rats surmulots, qui rejoignent ensuite les fermes et les maisons de la commune. Près d'une réserve d'eau potable, je choisis des emplacements et des produits adaptés, jamais au hasard."),
   ("Une commune de hauteur, entre Bretagne et Mayenne", "Le bourg est installé sur une hauteur, au milieu d'un bocage où les fermes, les granges et les hangars sont dispersés. Les rongeurs passent de la haie au bâtiment sans traverser de zone urbaine, et les bâtiments anciens en pierre offrent aux souris des caves, des combles et des murs épais pour s'installer."),
   ("Autres nuisibles à La Chapelle-Erbrée", "Dans les jardins et les fermes, les nids de guêpes et de frelons sont fréquents sous les toitures et dans les arbres. Je traite aussi les taupes dans les prairies, les pigeons dans les granges et les fourmis ou les cafards dans les logements.")],
  [("La Chapelle-Erbrée est-elle dans votre zone d'intervention ?", "Oui, à environ 10 km de Port-Brillet. Je me déplace en Ille-et-Vilaine comme en Mayenne."),
   ("Peut-on traiter les rongeurs près d'un plan d'eau ?", "Oui, avec des précautions : emplacements protégés, produits adaptés et suivi régulier. Je vous explique chaque étape.")],
  ["bourgon", "breal-sous-vitre", "erbree", "saint-m-herve"])

F("mondevert", "Mondevert", "35", 10.2,
  "Mondevert est une petite commune dense de 5 km², avec environ 800 habitants, à dix kilomètres de Port-Brillet. Bourg, lotissements, vergers et bois se côtoient sur un territoire très compact : un cadre où les nuisibles passent facilement du jardin à la maison.",
  [("Un territoire compact, du bois au bourg", "Mondevert n'a été créée qu'en 1790, par démembrement d'Erbrée, dont elle n'était auparavant qu'une trève. Elle s'étend sur un peu plus de 500 hectares, avec des prés, des pâtures, des vergers et des jardins en abondance. Avec environ 160 habitants au km², les maisons voisines partagent haies, murs et jardins : les souris et les rats passent d'un terrain à l'autre sans effort."),
   ("Le bois de la Hupperie et ses batraciens", "La présence de batraciens dans le bois de la Hupperie a conduit le département à déplacer le tracé du contournement du bourg. Cet attachement à la nature locale rappelle qu'il faut traiter avec précaution : je choisis des emplacements et des produits qui protègent les animaux domestiques et la faune sauvage autour des habitations."),
   ("Autres nuisibles à Mondevert", "Les vergers et les jardins attirent les guêpes, les frelons et les fourmis, surtout à la fin de l'été. Je traite aussi les taupes dans les pelouses, les chenilles processionnaires sur les pins et les cafards ou les puces dans les logements.")],
  [("Mondevert est-elle dans votre secteur ?", "Oui, à environ 10 km de Port-Brillet. Je me déplace en Ille-et-Vilaine comme en Mayenne."),
   ("Les rongeurs peuvent-ils passer d'un jardin à l'autre ?", "Oui, surtout dans les secteurs denses. Un diagnostic précis permet de traiter la cause plutôt que l'effet.")],
  ["breal-sous-vitre", "erbree", "argentre-du-plessis", "la-chapelle-erbree"])

F("la-croixille", "La Croixille", "53", 10.2,
  "La Croixille compte environ 630 habitants sur près de 20 km², à dix kilomètres de Port-Brillet. Son bourg est perché au sommet d'une colline, au milieu de prairies et de champs : les zones urbanisées n'occupent qu'environ 1 % du territoire.",
  [("Un territoire presque entièrement agricole", "Les prairies couvrent près de 58 % de la commune et les terres arables près de 39 %. Fermes, étables, hangars et silos y sont isolés les uns des autres, au contact direct des haies. Les rats s'y installent près des stocks d'aliments et des points d'eau, et les souris gagnent les maisons de hameau dès que les nuits fraîchissent."),
   ("Des châteaux, une église et beaucoup de pierres", "L'église Saint-Jean-Baptiste, qui date en partie du XVIe siècle, le château de la Rongère, du XVIIe siècle, et le château de la Barillière témoignent de l'ancienneté du bâti. Dans les murs épais, les greniers et les dépendances en pierre, les souris, les loirs et parfois les rats trouvent des abris durables. Je vous conseille sur les ouvertures à fermer et sur le choix du traitement."),
   ("Autres nuisibles à La Croixille", "Sur les hauteurs du bourg, les vieux arbres et les toitures abritent des nids de frelons et de guêpes. Je traite aussi les taupes dans les prairies, les pigeons dans les hangars et les fourmis ou les puces dans les habitations.")],
  [("La Croixille est-elle trop loin de Port-Brillet ?", "Non : elle est à environ 10 km. Je me déplace régulièrement dans ce secteur."),
   ("Intervenez-vous dans les fermes isolées ?", "Oui. J'inspecte les bâtiments, les stocks, les points d'eau et les accès, puis je propose un traitement et un suivi adaptés.")],
  ["bourgon", "le-bourgneuf-la-foret", "saint-m-herve", "prince"])

F("saint-germain-le-fouilloux", "Saint-Germain-le-Fouilloux", "53", 11.4,
  "Saint-Germain-le-Fouilloux compte environ 1 170 habitants sur 15 km², à onze kilomètres de Port-Brillet. Entre vallée, bois du Fouilloux et bourg à l'église romane, la commune mêle patrimoine ancien et nature préservée.",
  [("Une vallée et un bois qui donnent leur nom au village", "Le château, le bois et la vallée du Fouilloux ont donné leur nom à la commune, dont l'altitude varie de 55 à 146 mètres. Cette alternance de bois, de vallons et de prairies fournit aux rats et aux souris des couloirs de passage entre les lisières et les maisons. Les fermes isolées et les hameaux sont les premiers concernés."),
   ("Église du XIIe siècle et château du XVIIIe", "L'église Saint-Germain, d'origine romane, abrite des stalles du XVIIe siècle classées, et le château du Fouilloux date du XVIIIe siècle. Les bâtiments anciens de ce type, avec leurs combles, leurs caves et leurs dépendances, offrent aux souris, aux loirs et parfois aux rats des abris durables. Je vous conseille sur les points d'entrée à fermer."),
   ("Autres nuisibles à Saint-Germain-le-Fouilloux", "Je traite aussi les nids de guêpes et de frelons dans les arbres et les dépendances, les chenilles processionnaires sur les pins des jardins et les taupes dans les pelouses et les prairies.")],
  [("Intervenez-vous à Saint-Germain-le-Fouilloux ?", "Oui. La commune se trouve à environ 11 km de Port-Brillet, et je m'y déplace régulièrement."),
   ("Peut-on traiter des loirs dans un grenier ?", "Oui. Je commence par un diagnostic, puis je propose la solution adaptée, avec fermeture des accès pour éviter le retour.")],
  ["saint-ouen-des-toits", "le-bourgneuf-la-foret", "change", "andouille"])

F("erbree", "Erbrée", "35", 11.4,
  "Erbrée compte environ 1 700 habitants sur plus de 35 km², à quelques kilomètres à l'est de Vitré, à onze kilomètres de Port-Brillet. Dans les Marches de Bretagne, la commune est faite de champs, d'étangs, de bois et de châteaux.",
  [("Un territoire essentiellement agricole", "Sur 3 552 hectares, plus de 2 000 sont des terres labourables, et des prés, des bois, des vergers et des étangs complètent le paysage. Les corps de ferme, les silos et les stocks de céréales sont des cibles de choix pour les rats et les souris. Les haies et les fossés servent de couloirs entre les champs et les bâtiments."),
   ("L'étang de Paintourteau et les cours d'eau", "L'étang de Paintourteau, de 70 hectares, est l'un des étangs historiques d'Ille-et-Vilaine. Les berges, les roselières et les ruisseaux alentour sont des lieux de passage pour les rats surmulots, qui s'approchent ensuite des maisons et des fermes. Près des étangs et des zones naturelles, je choisis des emplacements et des produits qui protègent la faune."),
   ("Châteaux, manoirs et vieilles maisons", "Les châteaux des Nétumières et des Bretonnières, le Bois-Blin, la Picotière : la commune compte de nombreuses demeures anciennes. Dans les murs épais, les combles et les dépendances, les souris, les loirs et parfois les rats s'installent facilement. Je repère les passages avant de proposer un traitement, et je conseille sur la fermeture des accès.")],
  [("Erbrée est-elle dans votre secteur ?", "Oui, à environ 11 km de Port-Brillet. Je me déplace en Ille-et-Vilaine comme en Mayenne."),
   ("Intervenez-vous dans les exploitations agricoles d'Erbrée ?", "Oui. Je contrôle les bâtiments, les stocks et les points d'eau, puis je propose un traitement et un suivi adaptés.")],
  ["mondevert", "la-chapelle-erbree", "etrelles", "argentre-du-plessis"])

F("saint-hilaire-du-maine", "Saint-Hilaire-du-Maine", "53", 11.6,
  "Saint-Hilaire-du-Maine compte environ 800 habitants sur plus de 30 km², entre Ernée et Laval, à douze kilomètres de Port-Brillet. Avec moins de 30 habitants au km², c'est une commune de hameaux, de logis anciens et de bocage.",
  [("Une grande commune peu dense", "Sur 31 km², la population est très dispersée : fermes, logis et maisons de hameau sont séparés par des haies, des champs et des chemins creux. Les rats et les souris progressent d'un bâtiment à l'autre sans jamais traverser de zone bâtie, ce qui rend les infestations discrètes. Les stocks de céréales, les poulaillers et les granges sont les premiers touchés."),
   ("Logis, templerie et bâtiments anciens", "Le Logis du Poirier, inscrit aux monuments historiques, le hameau de la Templerie, ancien fief templier avec son église du XIIIe siècle, ou la charpente du XIIIe siècle de l'église paroissiale rappellent l'ancienneté du bâti. Dans les murs épais, les combles et les dépendances en pierre, les souris, les loirs et parfois les rats s'installent facilement. Je repère les passages avant de traiter."),
   ("Autres nuisibles à Saint-Hilaire-du-Maine", "Je traite aussi les nids de guêpes et de frelons dans les arbres et les toitures anciennes, les pigeons dans les granges et les taupes dans les prairies, ainsi que les fourmis et les cafards dans les habitations.")],
  [("Saint-Hilaire-du-Maine est-elle dans votre zone ?", "Oui, à environ 12 km de Port-Brillet. Je me rends dans le bourg comme dans les hameaux les plus isolés."),
   ("Pouvez-vous intervenir dans un logis ancien ?", "Oui. Je privilégie des emplacements discrets, sans toucher aux éléments anciens, et je vous indique les ouvertures à fermer avec l'accord du propriétaire.")],
  ["la-baconniere", "le-bourgneuf-la-foret", "chailland", "juvigne"])

F("le-pertre", "Le Pertre", "35", 11.8,
  "Le Pertre est la commune la plus orientale d'Ille-et-Vilaine et de Bretagne : environ 1 360 habitants, à douze kilomètres de Port-Brillet, à la limite de la Mayenne et au bord d'une grande forêt. Les rongeurs y trouvent à la fois les bois, les champs et le bourg.",
  [("Aux portes de la forêt du Pertre", "La forêt du Pertre, qui s'étend en partie sur la commune, est un vaste réservoir pour les rongeurs. Les lisières, les clairières et les fossés servent de corridors vers les habitations. Les maisons proches des bois sont plus souvent touchées : rats près des composteurs et des abris, souris dans les garages et les combles."),
   ("Une commune frontière", "Le Pertre est limitrophe de la Mayenne : La Gravelle, Saint-Cyr-le-Gravelais, Beaulieu-sur-Oudon, Méral et Cuillé se trouvent juste à l'est et au sud. Pour les nuisibles, la frontière départementale n'existe pas : ils circulent librement d'une commune à l'autre. Je travaille de part et d'autre, ce qui me permet de repérer les infestations qui se déplacent."),
   ("Autres nuisibles au Pertre", "Dans les jardins plantés de pins, des chenilles processionnaires peuvent s'installer. Je traite aussi les nids de guêpes et de frelons, les taupes dans les pelouses et les prairies et les fourmis dans les habitations.")],
  [("Le Pertre est-il dans votre secteur ?", "Oui, à environ 12 km de Port-Brillet. Je me déplace en Ille-et-Vilaine comme en Mayenne."),
   ("Y a-t-il plus de rongeurs près de la forêt ?", "C'est souvent le cas : les lisières abritent des populations qui s'approchent des maisons. Je pose des points de contrôle à l'extérieur et je vous conseille sur l'entretien des abords.")],
  ["la-gravelle", "saint-cyr-le-gravelais", "brielles", "argentre-du-plessis"])

F("saint-m-herve", "Saint-M'Hervé", "35", 12.3,
  "Saint-M'Hervé compte environ 1 350 habitants sur près de 30 km², entre Vitré et Laval, à douze kilomètres de Port-Brillet. Entre la Vilaine, le barrage de Haute-Vilaine et un bocage dense, la commune est un terrain de passage pour les rongeurs.",
  [("L'eau, le barrage et les prairies", "La commune est baignée par la Vilaine, et le barrage de Haute-Vilaine retient une grande réserve d'eau. Les berges, les fossés et les prairies humides sont des couloirs pour les rats surmulots, qui rejoignent ensuite les fermes, les granges et les maisons du bourg. Près des plans d'eau, je choisis des emplacements et des produits qui protègent la faune et les animaux domestiques."),
   ("Des maisons anciennes et d'anciens fours à chaux", "La maison de la Gélinière, de la fin du XVIe siècle, et celle de la Maserie, du XVIIe, témoignent de l'ancienneté de l'habitat. Plusieurs fours à chaux ont aussi marqué l'histoire industrielle de la commune. Ces bâtiments en pierre, avec leurs combles, leurs caves et leurs dépendances, offrent des abris aux souris, aux loirs et parfois aux rats."),
   ("Autres nuisibles à Saint-M'Hervé", "Dans les jardins, les nids de guêpes et de frelons apparaissent dans les haies, les abris et les arbres. Je traite aussi les taupes dans les pelouses et les prairies, les pigeons dans les granges et les fourmis dans les habitations.")],
  [("Saint-M'Hervé est-elle dans votre zone d'intervention ?", "Oui, à environ 12 km de Port-Brillet. Je me rends dans le bourg comme dans les hameaux."),
   ("Intervenez-vous près du barrage et des étangs ?", "Oui, avec des précautions adaptées : emplacements protégés, produits choisis pour limiter les risques pour la faune et les animaux domestiques.")],
  ["la-chapelle-erbree", "erbree", "bourgon", "la-croixille"])

F("montjean", "Montjean", "53", 12.7,
  "Montjean compte un peu plus de 1 000 habitants, à treize kilomètres de Port-Brillet. Son bourg roman et son château du XIIIe siècle dominent un secteur de campagne, d'élevage et de hameaux.",
  [("Un bourg ancien autour d'une église romane", "L'église Saint-Martin, de style roman, a été construite à partir du XIe siècle et remaniée au XIXe. Autour d'elle, les maisons et les commerces du bourg s'appuient sur des murs épais, des caves et des combles anciens. Les souris y trouvent des passages dans les cloisons et les vides techniques, surtout à l'approche de l'hiver."),
   ("Un château du XIIIe siècle et un environnement agricole", "Le château de Montjean, qui remonte au XIIIe siècle, rappelle l'ancienneté de la commune. Autour du bourg, les fermes, les hangars et les stocks de céréales attirent rats et souris, qui passent des haies aux bâtiments. Je contrôle les accès, je pose des points de contrôle discrets et je vous conseille sur le stockage."),
   ("Autres nuisibles à Montjean", "Je traite aussi les nids de guêpes et de frelons dans les arbres et les toitures, les pigeons dans les granges et les taupes dans les prairies, ainsi que les fourmis et les cafards dans les habitations.")],
  [("Montjean est-elle dans votre secteur ?", "Oui, à environ 13 km de Port-Brillet. Je me déplace régulièrement dans ce secteur de la Mayenne."),
   ("Intervenez-vous dans les commerces du bourg ?", "Oui. Pour un restaurant, une boulangerie ou un commerce de bouche, je propose des passages réguliers et un compte rendu écrit.")],
  ["ahuille", "beaulieu-sur-oudon", "saint-cyr-le-gravelais", "juvigne"])

F("ahuille", "Ahuillé", "53", 12.7,
  "Ahuillé compte environ 1 850 habitants sur près de 30 km², à treize kilomètres de Port-Brillet et à dix kilomètres de Laval. Entre prairies, étangs et forêt de Concise, la commune garde une forte identité agricole à deux pas de l'agglomération.",
  [("Peu de bâti, beaucoup de campagne", "Sur environ 2 900 hectares, quelque 250 sont boisés et à peine 35 sont urbanisés. Le reste est occupé par des prairies, des pâturages et des étangs, où l'on pratique la polyculture et l'élevage de bovins et de porcins. Le bourg et ses lotissements sont donc entourés de champs : les rats et les souris passent des fermes aux maisons sans effort."),
   ("La forêt de Concise et les étangs", "La départementale 500 sillonne les prairies et borde la forêt de Concise, un massif privé. Lisières, étangs et fossés servent de couloirs de circulation pour les rats surmulots, qui rejoignent ensuite les jardins, les composteurs et les bâtiments agricoles. Ahuillé compte aussi un site naturel classé : je choisis donc des emplacements et des produits adaptés pour protéger la faune."),
   ("Autres nuisibles à Ahuillé", "Dans les lotissements et les fermes, je traite les nids de guêpes et de frelons, les taupes dans les pelouses et les prairies, les pigeons dans les granges et les fourmis dans les habitations. Pour les exploitations, je propose un suivi à fréquence définie avec compte rendu écrit.")],
  [("Ahuillé est-elle dans votre zone d'intervention ?", "Oui, à environ 13 km de Port-Brillet. Je me déplace régulièrement entre Port-Brillet, Laval et Ahuillé."),
   ("Y a-t-il plus de rongeurs près de la forêt et des étangs ?", "Souvent oui : les lisières et les berges sont des zones de passage. Je pose des points de contrôle à l'extérieur et je vous conseille sur l'entretien des abords.")],
  ["saint-berthevin", "montjean", "courbeveille", "montigne-le-brillant"])

F("juvigne", "Juvigné", "53", 13.5,
  "Juvigné est une grande commune de plus de 60 km², pour environ 1 330 habitants : moins de 22 habitants au km². À treize kilomètres de Port-Brillet, entre Fougères et Laval, c'est un village fleuri entouré d'élevage et de bocage.",
  [("Une commune d'élevage très étendue", "Juvigné est connue pour son élevage de bovins et son paysage de bocage. Avec 62 km² et une densité aussi faible, les fermes, les hangars et les stabulations sont dispersés. Les stocks de céréales, les aliments du bétail et les points d'eau attirent rats et souris, qui passent des haies aux bâtiments sans traverser de zone bâtie."),
   ("Un patrimoine rural et ancien", "Le château du Feu, inscrit aux monuments historiques, le château de Juvigné, le sanctuaire gallo-romain et le musée du moteur et de l'outil à la ferme montrent l'ancienneté de la vie rurale dans la commune. Les bâtiments anciens en pierre, avec leurs combles et leurs dépendances, sont des abris durables pour les souris, les loirs et parfois les rats."),
   ("Autres nuisibles à Juvigné", "Pour un village fleuri, les massifs, les haies et les jardins attirent aussi guêpes, frelons et fourmis. Je traite également les taupes dans les prairies, les pigeons dans les granges et les cafards ou les puces dans les habitations.")],
  [("Juvigné est-elle trop loin de Port-Brillet ?", "Non : elle se trouve à environ 13 km. Je me rends dans le bourg comme dans les hameaux."),
   ("Intervenez-vous dans les exploitations d'élevage ?", "Oui. J'inspecte les bâtiments, les stocks et les points d'eau, puis je propose un traitement et un suivi adaptés à l'exploitation.")],
  ["saint-hilaire-du-maine", "la-croixille", "le-bourgneuf-la-foret", "montenay"])

F("saint-germain-le-guillaume", "Saint-Germain-le-Guillaume", "53", 13.9,
  "Saint-Germain-le-Guillaume compte environ 510 habitants sur 13 km², à quatorze kilomètres de Port-Brillet. Au carrefour de trois routes départementales, entre Chailland, Andouillé et La Bigottière, c'est un petit bourg de bocage où les nuisibles circulent librement.",
  [("Un bourg de carrefour entouré de bocage", "Le bourg s'est construit au croisement des routes départementales 123, 131 et 165, avec une église gothique du milieu du XIXe siècle. Autour, les haies, les prairies et les hameaux offrent aux rongeurs de nombreux chemins entre les champs et les maisons. Les souris profitent des garages et des combles dès les premiers froids."),
   ("Des châteaux et des demeures anciennes", "Le château du Mesnil-Barré, celui de la Sicorie et celui du Tertre jalonnent le territoire. Ces demeures anciennes, leurs communs et leurs dépendances en pierre sont des lieux où les souris, les loirs et parfois les rats s'installent facilement. Je repère les passages avant de traiter et je conseille sur les fermetures."),
   ("Autres nuisibles à Saint-Germain-le-Guillaume", "Je traite aussi les nids de guêpes et de frelons dans les arbres et les dépendances, les pigeons dans les granges et les taupes dans les prairies et les pelouses.")],
  [("Intervenez-vous dans un si petit village ?", "Oui. Quelle que soit la taille de la commune, je me déplace : Saint-Germain-le-Guillaume est à environ 14 km de Port-Brillet."),
   ("Peut-on traiter un nid de frelons dans un arbre ?", "Oui, selon la hauteur et l'accès. Je viens d'abord constater le nid, puis je propose la méthode adaptée.")],
  ["andouille", "chailland", "la-bigottiere", "la-baconniere"])

F("andouille", "Andouillé", "53", 14.2,
  "Andouillé compte environ 2 300 habitants, à quatorze kilomètres de Port-Brillet et à quinze kilomètres de Laval, entre l'Ernée et la Mayenne. Bourg ancien, rivières, site industriel d'autrefois et campagne : la commune cumule beaucoup d'atouts pour les rongeurs.",
  [("Deux rivières et un bourg ancien", "Deux cours d'eau se trouvent à proximité du village : l'Ernée et la Mayenne. Les berges, les chemins de halage et les fossés servent de corridors aux rats surmulots, qui remontent vers les jardins, les commerces et les maisons du bourg. Andouillé était déjà un bourg important à l'époque mérovingienne : on y trouve encore des bâtiments anciens en pierre, avec caves et combles où les souris s'installent."),
   ("Un passé industriel au bord de la Mayenne", "Les anciennes usines de l'amiante du Cap, fondées au XIXe siècle par Frédéric Chaplet, ont marqué le site de Rochefort, sur la rive de la Mayenne. Les anciens sites industriels, avec leurs friches, leurs bâtiments vides et leurs talus, servent de refuge aux rongeurs, qui rejoignent ensuite les zones habitées. La zone d'activités de la Malardrerie rassemble aujourd'hui des entreprises qui ont besoin d'un suivi régulier."),
   ("Autres nuisibles à Andouillé", "Dans les jardins et les fermes, je traite les nids de guêpes et de frelons, les taupes, les pigeons dans les granges et les fourmis ou les cafards dans les habitations. Pour les commerces et les entreprises, je propose des passages réguliers avec compte rendu écrit.")],
  [("Andouillé est-elle dans votre zone d'intervention ?", "Oui, à environ 14 km de Port-Brillet. Je me déplace régulièrement entre Port-Brillet, Andouillé et Laval."),
   ("Intervenez-vous pour les entreprises de la zone d'activités ?", "Oui. Je propose un diagnostic, la pose de points de contrôle et des passages réguliers, avec un compte rendu à chaque visite.")],
  ["saint-germain-le-guillaume", "saint-germain-le-fouilloux", "la-baconniere", "saint-jean-sur-mayenne"])

F("change", "Changé", "53", 12.3,
  "Changé s'étend de part et d'autre de la Mayenne, juste au nord de Laval, à douze kilomètres de Port-Brillet. Parc des Ondines, bases de loisirs, golf et centre-bourg se côtoient dans une commune où l'eau est partout.",
  [("Les berges de la Mayenne", "Le centre-ville est sur la rive droite de la Mayenne, et des lotissements pavillonnaires s'étendent sur les deux rives. Les berges, le parc des Ondines et les plans d'eau attirent promeneurs, oiseaux et rats surmulots. Ceux-ci remontent vers les jardins, les composteurs et les arrière-cours des commerces."),
   ("Un centre ancien et des quartiers récents", "Le château de Changé, ancien prieuré, abrite aujourd'hui l'hôtel de ville, et l'église Saint-Pierre date du XIXe siècle. Dans les bâtiments anciens du centre, les souris profitent des caves et des combles. Dans les lotissements, elles s'installent dans les garages et les vides techniques."),
   ("Entreprises, santé et loisirs", "Changé accueille des zones industrielles au nord-est, une clinique, un golf et des bases de loisirs. Restaurants, cuisines collectives et locaux d'entreprise ont besoin d'un suivi régulier avec compte rendu écrit : c'est exactement ce que je propose, avec un contrat adapté à votre activité.")],
  [("Changé est-elle dans votre secteur ?", "Oui, à environ 12 km de Port-Brillet. Je me déplace régulièrement entre Port-Brillet et Laval."),
   ("Proposez-vous un contrat pour les restaurants de Changé ?", "Oui. Vous trouverez le détail sur la page « Contrat de dératisation restaurant à Changé ».")],
  ["saint-berthevin", "louverne", "saint-germain-le-fouilloux", "laval"])

F("louverne", "Louverné", "53", 18.7,
  "Louverné est une commune de Laval Agglomération d'environ 4 300 habitants, à dix-neuf kilomètres de Port-Brillet. Ruisseaux, anciennes carrières de marbre noir et lotissements en font un terrain de passage pour les rongeurs.",
  [("Les ruisseaux de Barbé et de la Fresne", "Deux ruisseaux traversent le territoire : celui de Barbé et celui de la Fresne. Leurs berges et la végétation qui les borde sont des couloirs pour les rats surmulots, qui rejoignent les jardins, les composteurs et les arrière-cours des commerces."),
   ("Des vestiges industriels et un patrimoine ancien", "Les anciennes carrières de marbre noir et un ancien four à chaux près de la gare rappellent le passé industriel de la commune. La borne de banlieue de 1751, qui marquait la limite du tarif de Laval, témoigne de son histoire. Les cavités et les friches de ces sites servent de refuge aux rongeurs."),
   ("Châteaux, grotte et espèces protégées", "Les châteaux de la Bigottière et de Ronceray jalonnent la campagne. Une grotte préhistorique au sud de la commune abrite des chauves-souris, espèces protégées : je les distingue des nuisibles avant toute intervention.")],
  [("Louverné est-elle dans votre zone d'intervention ?", "Oui, à environ 19 km de Port-Brillet. Je me déplace régulièrement dans l'agglomération lavalloise."),
   ("Proposez-vous un contrat pour les commerces de bouche ?", "Oui. Vous trouverez le détail sur les pages « Contrat de dératisation » de Louverné.")],
  ["change", "saint-berthevin", "laval"])

F("argentre-du-plessis", "Argentré-du-Plessis", "35", 15.3,
  "Argentré-du-Plessis compte environ 4 100 habitants sur 41 km², à quinze kilomètres de Port-Brillet, aux confins de la Bretagne et des Pays de la Loire. Étangs, moulins, bocage et bourg ancien : un territoire où les rongeurs ne manquent pas d'abris.",
  [("Étangs, moulins et bocage", "La commune compte de nombreux étangs, dont celui de la Verrerie, et un plan d'eau de plus de cinq hectares au Moulin Neuf. Les moulins aux Moines, Neuf et de Salé rappellent le rôle de l'eau. Les berges et les haies sont des couloirs pour les rats surmulots, qui rejoignent les fermes et les hameaux."),
   ("Un patrimoine ancien en pierre", "Le château du Plessis, le manoir de la Fauconnerie, la chapelle Saint-Pierre sur le chemin des Saulniers et l'église Notre-Dame, reconstruite entre 1775 et 1779, témoignent de l'ancienneté du bâti. Les caves et les combles de ces bâtiments sont des abris pour les souris et les loirs."),
   ("Entreprises, commerces et ancienne industrie du bois", "La commune a abrité des usines de menuiserie, comme l'ancienne usine Rossignol. Aujourd'hui, restaurants, boulangeries et traiteurs ont besoin d'un suivi régulier : vous trouverez le détail sur les pages « Contrat de dératisation » d'Argentré-du-Plessis.")],
  [("Argentré-du-Plessis est-elle dans votre secteur ?", "Oui, à environ 15 km de Port-Brillet. Je me déplace en Ille-et-Vilaine comme en Mayenne."),
   ("Intervenez-vous dans les hameaux ?", "Oui, dans tous les hameaux de la commune.")],
  ["vitre", "mondevert", "erbree", "le-pertre"])

def _G(slug, nom, dep, km, hab, surf, voisins, trait_titre, trait, ask_loc):
    """Fiche courte: faits vérifiés (habitants, surface) + particularité locale."""
    kms = str(km).replace(".", ",")
    F(slug, nom, dep, km,
      "%s compte %s sur %s km², à %s km de Port-Brillet. %s Voici les nuisibles que je rencontre le plus souvent dans le secteur et ce que je peux faire pour vous." % (nom, hab, surf, kms, ask_loc),
      [("Pourquoi des rongeurs à %s" % nom, "Avec %s sur %s km², %s est une commune où le bâti alterne avec les champs, les haies et les dépendances. Les rats et les souris passent facilement des prairies aux granges, aux garages et aux maisons, surtout à l'automne quand les températures baissent." % (hab, surf, nom)),
       (trait_titre, trait),
       ("Autres nuisibles à %s" % nom, "Nids de guêpes et de frelons dans les toitures, les haies et les abris de jardin, taupes dans les prairies et les pelouses, pigeons sur les bâtiments agricoles et anciens : j'interviens pour tous ces nuisibles, sans que vous ayez à chercher plusieurs prestataires.")],
      [("%s fait-elle partie de votre zone d'intervention ?" % nom, "Oui, %s se trouve à environ %s km de Port-Brillet, où je suis installé. Je me déplace chez les particuliers, les agriculteurs et les professionnels." % (nom, kms)),
       ("Quel délai pour une intervention à %s ?" % nom, "Pour un nid de guêpes ou de frelons, j'essaie d'intervenir au plus vite. Pour les rongeurs, je commence par un diagnostic sur place, puis je propose un traitement adapté et un devis gratuit.")],
      voisins)

_G("chailland", "Chailland", "53", 14.6, "environ 1 200 habitants", "35,9",
   ["la-bigottiere", "ernee", "saint-pierre-des-landes", "montenay"],
   "Petite Cité de Caractère au bord de l'Ernée",
   "Chailland est classée Petite Cité de Caractère. Ses forges ont fonctionné pendant environ trois siècles à partir de 1550, et il subsiste des rangées de petites maisons ouvrières le long de la rivière, ainsi que des lavoirs et des moulins. L'Ernée et le Vaumourin traversent la commune : ces bords d'eau et ces vieux murs de pierre sont des endroits où les rats surmulots, les souris et les loirs trouvent des passages. Je vous indique les ouvertures à fermer et les emplacements à surveiller.",
   "Une commune de charme entre rivières et forêt.")
_G("cosse-le-vivien", "Cossé-le-Vivien", "53", 19.8, "plus de 3 100 habitants", "44",
   ["astille", "saint-poix", "meral", "beaulieu-sur-oudon"],
   "Un bourg actif traversé par l'Oudon",
   "Cossé-le-Vivien est l'une des plus grandes communes de ce secteur, et l'Oudon la traverse en son milieu. La commune est connue pour le musée consacré à l'œuvre de Robert Tatin. Le bourg compte commerces, restaurants et artisans de bouche, pour lesquels je propose un suivi régulier avec compte rendu écrit, et des fermes dans la campagne alentour. Les berges de l'Oudon sont un couloir de passage pour les rats surmulots.",
   "Bourg actif de mon secteur.")
_G("beaulieu-sur-oudon", "Beaulieu-sur-Oudon", "53", 13.9, "environ 480 habitants", "19,7",
   ["meral", "cosse-le-vivien", "la-croixille", "chailland"],
   "Les bords de l'Oudon",
   "L'Oudon traverse la commune et en forme une partie de la limite sud-est. Les berges, les haies et les prairies humides sont des lieux de passage pour les rats surmulots, qui remontent ensuite vers les fermes, les poulaillers et les garages. Je pose les postes d'appâtage à l'abri des animaux domestiques et je vous explique comment limiter les attraits : stockage des grains, composteur, eaux stagnantes.",
   "Petite commune rurale au bord de l'Oudon.")
_G("l-huisserie", "L'Huisserie", "53", 18.9, "plusieurs milliers d'habitants", "14,7",
   ["saint-berthevin", "laval", "montigne-le-brillant", "saint-jean-sur-mayenne"],
   "Une commune de l'agglomération de Laval",
   "L'Huisserie fait partie de l'agglomération de Laval et s'étend sur environ 15 km². Lotissements, zones d'activités et commerces côtoient encore des espaces agricoles. Ce mélange attire les souris dans les maisons récentes, les rats autour des commerces et des restaurants, et les pigeons sur les bâtiments d'activité. Pour les professionnels, je propose un contrat de suivi avec compte rendu écrit après chaque passage.",
   "Voisine de Laval, c'est un secteur où je me déplace régulièrement.")
_G("etrelles", "Étrelles", "35", 19.2, "environ 2 700 habitants", "27,2",
   ["argentre-du-plessis", "vitre", "erbree", "mondevert"],
   "Une commune en forte croissance",
   "La population d'Étrelles a plus que doublé depuis 1968, passant d'environ 1 250 à près de 2 700 habitants. Les lotissements récents, les chantiers de construction et les terrains vagues font partie des situations où les rongeurs profitent des travaux et des terres remuées. L'église Saint-Pierre-et-Saint-Paul et les maisons anciennes du bourg ont leurs propres points faibles : combles, caves et dépendances. J'adapte le traitement à chaque bâtiment.",
   "Commune d'Ille-et-Vilaine située dans mon secteur.")
_G("meral", "Méral", "53", 18.8, "un peu plus de 1 000 habitants", "29,5",
   ["cosse-le-vivien", "beaulieu-sur-oudon", "astille", "saint-poix"],
   "Une commune rurale limitée par l'Oudon",
   "L'Oudon forme une partie de la limite nord-est de Méral, une commune de près de 30 km² où les fermes et les hameaux sont nombreux. La chapelle de la commune rappelle l'ancienneté du bâti. Dans les granges, les étables et les stockages de céréales, les rats et les souris trouvent nourriture et abri : pour les exploitations, je propose un diagnostic des bâtiments puis un programme de lutte adapté.",
   "Commune rurale de l'est du secteur.")
_G("astille", "Astillé", "53", 19.7, "près de 900 habitants", "20,7",
   ["cosse-le-vivien", "saint-poix", "meral", "beaulieu-sur-oudon"],
   "Une commune qui s'agrandit",
   "La population d'Astillé est passée d'environ 490 habitants en 1968 à près de 900 aujourd'hui. Les maisons récentes côtoient les fermes et les bâtiments anciens. Dans les nouveaux lotissements, les souris s'installent par les passages de canalisations ; dans les fermes, les rats profitent des stocks et des abris. Je vous aide à repérer les accès et à choisir la solution la plus adaptée.",
   "Commune du Pays de Craon, située dans mon secteur.")
_G("saint-pierre-des-landes", "Saint-Pierre-des-Landes", "53", 19.5, "environ 900 habitants", "40,9",
   ["chailland", "montenay", "la-bigottiere", "ernee"],
   "Une grande commune rurale avec un étang de pêche",
   "Saint-Pierre-des-Landes s'étend sur près de 41 km² pour environ 900 habitants : c'est l'une des communes les plus étendues du secteur et les fermes y sont éloignées les unes des autres. Un étang de pêche et l'église Notre-Dame-de-l'Assomption de Mégaudais font partie des repères locaux. Les abords d'étang attirent les rats surmulots ; j'installe le matériel à l'abri des animaux domestiques et de la faune.",
   "Commune étendue, située dans mon secteur.")
_G("chatillon-en-vendelais", "Châtillon-en-Vendelais", "35", 19.2, "environ 1 800 habitants", "32",
   ["balaze", "prince", "mondevert", "la-chapelle-erbree"],
   "Une commune bretonne",
   "Châtillon-en-Vendelais compte environ 1 800 habitants sur 32 km². L'église Saint-Georges marque le bourg ; autour, fermes et hameaux sont nombreux. Les haies et les bâtiments agricoles forment un terrain favorable aux rats et aux souris, et les granges attirent les pigeons. Je propose un diagnostic gratuit avant tout traitement.",
   "Commune d'Ille-et-Vilaine située dans mon secteur.")
_G("gennes-sur-seiche", "Gennes-sur-Seiche", "35", 18.5, "environ 940 habitants", "18,5",
   ["argentre-du-plessis", "etrelles", "erbree", "vitre"],
   "Une petite commune rurale d'Ille-et-Vilaine",
   "Gennes-sur-Seiche est une petite commune d'environ 940 habitants, sur un territoire de 18,5 km². L'habitat y est surtout composé de maisons individuelles et de fermes. Les souris s'installent dans les combles et les garages dès l'automne, et les rats fréquentent les poulaillers et les abris de jardin. J'interviens pour un seul nid de guêpes comme pour un traitement complet.",
   "Commune d'Ille-et-Vilaine, dans mon secteur élargi.")
_G("montautour", "Montautour", "35", 14.8, "environ 270 habitants", "6,9",
   ["erbree", "vitre", "mondevert", "le-pertre"],
   "Une très petite commune d'Ille-et-Vilaine",
   "Montautour est une des plus petites communes du secteur, avec environ 270 habitants sur 6,9 km². Les maisons y sont dispersées et entourées de champs et de haies : les rongeurs passent facilement des cultures aux bâtiments. Je me déplace même pour une petite intervention, avec un devis gratuit.",
   "Petite commune d'Ille-et-Vilaine située dans mon secteur.")
_G("brielles", "Brielles", "35", 15.6, "environ 680 habitants", "11,4",
   ["prince", "balaze", "etrelles", "argentre-du-plessis"],
   "Une commune rurale d'Ille-et-Vilaine",
   "Brielles compte environ 680 habitants sur 11,4 km². Après une baisse à la fin du XXe siècle, la population est repartie à la hausse. Les maisons récentes côtoient des fermes ; les rats et les souris profitent des stocks et des abris pour passer l'hiver. Je vous explique comment limiter les risques autour de l'habitation.",
   "Commune d'Ille-et-Vilaine située dans mon secteur.")
_G("saint-jean-sur-mayenne", "Saint-Jean-sur-Mayenne", "53", 16.3, "environ 1 700 habitants", "17,8",
   ["laval", "l-huisserie", "montigne-le-brillant", "saint-berthevin"],
   "Une commune de l'agglomération lavalloise sur la Mayenne",
   "Saint-Jean-sur-Mayenne fait partie de Laval Agglomération. Comme son nom l'indique, la commune est au bord de la rivière Mayenne : les berges attirent les rats surmulots, qui peuvent rejoindre les jardins, les caves et les garages voisins. Je propose aux particuliers un diagnostic simple et aux professionnels un suivi régulier avec compte rendu écrit.",
   "Commune proche de Laval.")
F("courbeveille", "Courbeveille", "53", 15.9,
  "Courbeveille est une commune rurale de la Mayenne, à environ 16 km de Port-Brillet. Voici les nuisibles que je rencontre le plus souvent dans le secteur et ce que je peux faire pour vous.",
  [("Pourquoi des rongeurs à Courbeveille", "Courbeveille est une commune rurale : fermes, hameaux et maisons individuelles y sont entourés de champs et de haies. Les rats et les souris passent facilement des cultures aux granges, aux garages et aux maisons, surtout à l'automne."),
   ("Agriculteurs et particuliers", "Pour les exploitations, je propose un diagnostic des bâtiments, des stocks et des abords, puis un programme de lutte adapté. Pour les particuliers, je repère les accès et je vous explique comment les fermer."),
   ("Autres nuisibles à Courbeveille", "Nids de guêpes et de frelons dans les toitures et les haies, taupes dans les prairies, pigeons sur les bâtiments agricoles : j'interviens pour tous ces nuisibles.")],
  [("Courbeveille fait-elle partie de votre zone d'intervention ?", "Oui, à environ 16 km de Port-Brillet. Je me déplace chez les particuliers, les agriculteurs et les professionnels."),
   ("Quel délai pour une intervention à Courbeveille ?", "Pour un nid de guêpes ou de frelons, j'essaie d'intervenir au plus vite. Pour les rongeurs, je fais un diagnostic sur place puis un devis gratuit.")],
  ["chailland", "saint-jean-sur-mayenne", "montigne-le-brillant", "laval"])

_G("montigne-le-brillant", "Montigné-le-Brillant", "53", 16.3, "environ 1 400 habitants", "18",
   ["l-huisserie", "saint-jean-sur-mayenne", "courbeveille", "laval"],
   "Une commune de l'agglomération avec une église Saint-Georges",
   "Montigné-le-Brillant fait partie de Laval Agglomération et compte environ 1 400 habitants sur 18 km². L'église Saint-Georges marque le bourg, entouré de lotissements et de fermes. Les rongeurs profitent des chantiers et des terres remuées ; les combles et caves des bâtiments anciens sont aussi des points d'entrée. J'adapte le traitement à chaque bâtiment.",
   "Commune de l'agglomération de Laval.")
_G("prince", "Princé", "35", 16.4, "environ 400 habitants", "12,4",
   ["brielles", "balaze", "chatillon-en-vendelais", "etrelles"],
   "Une petite commune d'Ille-et-Vilaine",
   "Princé compte environ 400 habitants sur 12,4 km². Après un creux à la fin des années 1990, la population est repartie à la hausse. L'habitat est dispersé et les rongeurs circulent entre les champs, les haies et les bâtiments. Je me déplace pour tout type d'intervention, avec un devis gratuit.",
   "Petite commune d'Ille-et-Vilaine.")
_G("la-bigottiere", "La Bigottière", "53", 17.1, "environ 490 habitants", "18,4",
   ["chailland", "saint-pierre-des-landes", "ernee", "montenay"],
   "Une commune rurale de Mayenne",
   "La Bigottière compte environ 490 habitants sur 18,4 km². Cette commune rurale est composée de fermes, de hameaux et de maisons isolées. Les bâtiments d'élevage et les stockages de céréales sont les premiers touchés par les rats et les souris ; je propose un diagnostic des bâtiments et un plan de lutte adapté à l'exploitation.",
   "Commune rurale de Mayenne.")
_G("balaze", "Balazé", "35", 17.3, "environ 2 200 habitants", "36,7",
   ["chatillon-en-vendelais", "prince", "brielles", "vitre"],
   "Une commune étendue autour de l'église Saint-Martin",
   "Balazé compte environ 2 200 habitants et s'étend sur près de 37 km². L'église Saint-Martin marque le bourg, entouré de lotissements, de fermes et de hameaux. Les rongeurs profitent de la proximité entre champs et habitations ; les restaurants, commerces et exploitations peuvent bénéficier d'un suivi régulier avec compte rendu écrit.",
   "Commune d'Ille-et-Vilaine située dans mon secteur.")
_G("saint-poix", "Saint-Poix", "53", 18.0, "environ 380 habitants", "7,4",
   ["cosse-le-vivien", "astille", "meral", "beaulieu-sur-oudon"],
   "Une petite commune du Pays de Craon",
   "Saint-Poix est une petite commune d'environ 380 habitants sur 7,4 km², proche de Cossé-le-Vivien. Les maisons et les fermes sont entourées de champs : les souris entrent dans les maisons à l'automne, les rats fréquentent les bâtiments agricoles. Je vous propose un devis gratuit après diagnostic.",
   "Petite commune du Pays de Craon.")
_G("montenay", "Montenay", "53", 18.7, "environ 1 300 habitants", "37,2",
   ["chailland", "saint-pierre-des-landes", "la-bigottiere", "ernee"],
   "Une grande commune rurale",
   "Montenay compte environ 1 300 habitants sur plus de 37 km². Le bourg, avec son ancienne mairie, est entouré de fermes et de hameaux. Les granges, les silos et les bâtiments d'élevage sont les premiers touchés par les rongeurs ; je vous propose un diagnostic gratuit et un plan de lutte adapté.",
   "Commune rurale de Mayenne.")
_G("montflours", "Montflours", "53", 18.9, "environ 250 habitants", "7,9",
   ["l-huisserie", "chailland", "montigne-le-brillant", "courbeveille"],
   "Un petit village rural",
   "Montflours est un petit village d'environ 250 habitants sur 7,9 km². Les maisons sont entourées de champs et de haies, et la mairie marque le bourg. Les rongeurs passent facilement des cultures aux bâtiments : je me déplace pour tout type d'intervention.",
   "Petite commune rurale de Mayenne.")

# ---------- Rendu des pages communes ----------
_NOMS = {f[0]: f[1] for f in FICHES}
_NOMS.update({c[0]: c[1] for c in CITIES})
def _titre_commune(nom, dep):
    for t in ("Dératisation à %s (%s) | Proxinuisibles" % (nom, dep), "Dératisation à %s | Proxinuisibles" % nom, "Dératisation %s | Proxinuisibles" % nom):
        if len(t) <= 60:
            return t
    return "Dératisation %s" % nom
for slug, nom, dep, km, lead, secs, faq, voisins in FICHES:
    path = "/deratisation-%s/" % slug
    if path in P:
        continue
    vlinks = [("Dératisation à %s" % _NOMS[v], "/deratisation-%s/" % v) for v in voisins if v in _NOMS and ("/deratisation-%s/" % v) in P or v in CN]
    vlinks = [(l, u) for l, u in vlinks if u != path]
    links = [("Autres services à %s" % nom, [("Frelons et guêpes", "/frelons-guepes/"), ("Frelon asiatique", "/frelon-asiatique/"), ("Désinsectisation", "/desinsectisation/"), ("Blattes et cafards", "/blattes-cafards/"), ("Fourmis", "/fourmis/"), ("Mouches", "/mouches/"), ("Puces", "/puces/"), ("Punaises de lit", "/punaises-de-lit/"), ("Chenilles processionnaires", "/chenilles-processionnaires/"), ("Taupier", "/taupier/"), ("Dépigeonnage", "/depigeonnage/"), ("Piégeur agréé", "/piegeur-agree/")])]
    if vlinks:
        links.append(("Communes voisines", vlinks))
    links.append(("Voir aussi", [("Zones d'intervention", "/zones-intervention/"), ("Particuliers", "/particuliers/"), ("Agriculteurs", "/agriculteurs/"), ("Professionnels", "/professionnels/"), ("Devis gratuit", "/contact/")]))
    add(path, h1="Dératisation à %s (%s) : rats, souris et autres nuisibles" % (nom, dep), title=_titre_commune(nom, dep),
        meta="Dératisation et lutte contre les nuisibles à %s (%s), à %s km de Port-Brillet : rats, souris, frelons, taupes. Devis gratuit." % (nom, dep, str(km).replace(".", ",")),
        lead=lead, secs=secs, faq=faq, links=links, kind="ville")

_nouvelles = sorted((f[3], f[1], "/deratisation-%s/" % f[0]) for f in FICHES)
P["/zones-intervention/"]["links"].append(("Autres communes à moins de 20 km de Port-Brillet", [("%s (%s km)" % (n, str(k).replace(".", ","))) and ("Dératisation %s" % n, u) for k, n, u in _nouvelles]))
