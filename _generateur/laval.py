# -*- coding: utf-8 -*-
# Page « Dératisation à Laval » : page au plus fort potentiel du site.
# 238 affichages sur « dératisation laval » pour 3 clics (Search Console,
# 3 mois au 12/11/2026) : le travail porte sur le titre, la description
# et la profondeur locale, pas sur le volume.
# Exécuté en dernier, après seo_deratiseur.py.

_lv = P["/deratisation-laval/"]

# ---------- Titre et description : ce que l'internaute lit dans Google ----------
# Le nom du site est désormais déclaré séparément (schéma WebSite), la marque
# n'a donc plus à occuper la fin du titre.
_lv["title"] = "Dératiseur à Laval : intervention rapide, devis gratuit"
_lv["meta"] = ("Dératiseur indépendant près de Laval : rats et souris en maison, commerce ou "
               "immeuble. En général sous 24 à 48 h, urgences en priorité. Devis gratuit.")

_lv["lead"] = ("Rats ou souris à Laval ? Je suis dératiseur indépendant, installé à Port-Brillet, "
               "à vingt minutes du centre. J'interviens en général sous 24 à 48 heures, plus vite en cas "
               "d'urgence réelle, chez les particuliers, "
               "dans les commerces et dans les copropriétés, avec un diagnostic et un devis gratuits.")

# ---------- Sections proprement lavalloises ----------
# Elles remplacent les deux premières sections génériques issues de la boucle
# des villes, pour que cette page dise quelque chose que les autres ne disent pas.
_lv["secs"] = [
    ("La Mayenne traverse la ville, et les rats suivent l'eau",
     "Le surmulot, le gros rat gris des villes, ne s'éloigne jamais longtemps d'un point d'eau. "
     "À Laval, la rivière coupe la ville en deux et ses berges courent d'Avesnières jusqu'au nord, "
     "avec des quais, des murs anciens et des réseaux qui débouchent dessus. C'est un couloir "
     "de circulation permanent.\n"
     "Concrètement, les maisons et les commerces situés à moins de cent mètres de la Mayenne sont "
     "les plus exposés, et le rez-de-chaussée ou la cave est presque toujours le point d'entrée. "
     "Quand j'interviens dans ces rues, je regarde d'abord les regards d'eaux usées, les vides "
     "sanitaires et le bas des murs, avant même de parler de traitement."),

    ("Le centre ancien : des caves qui communiquent",
     "Dans le vieux Laval, les maisons se touchent, les caves se partagent des murs vieux de "
     "plusieurs siècles et les réseaux ont été repris dix fois. Une souris passe d'un immeuble "
     "à l'autre sans jamais sortir.\n"
     "C'est pour cette raison que traiter un seul logement donne souvent un résultat de courte "
     "durée dans ces rues : les rongeurs reviennent par le voisin. Je vous le dis franchement "
     "quand c'est le cas, et je vous explique ce qu'il faut demander au syndic ou au propriétaire "
     "pour que le problème soit traité là où il se trouve."),

    ("Pavillons, lotissements et jardins des quartiers",
     "Hilard, Grenoux, Bourny, Saint-Nicolas, Thévalles, Les Fourches, le Pavement, Laval Nord : "
     "les quartiers pavillonnaires posent un problème différent du centre. Ici, ce ne sont pas "
     "les murs mitoyens mais le jardin qui attire : composteur, poulailler, mangeoire à oiseaux, "
     "sac de croquettes dans le garage, abri de jardin au fond du terrain.\n"
     "Les rongeurs s'installent dehors, puis entrent à l'automne quand les températures tombent. "
     "Sur ces interventions, une bonne partie de mon travail consiste à vous montrer ce qui, "
     "autour de la maison, leur sert de garde-manger — parce que sans ça, le traitement ne tient pas."),

    ("Commerces, restaurants et métiers de bouche du centre",
     "Une boulangerie, une boucherie ou un restaurant du centre-ville n'a pas droit à l'à-peu-près : "
     "un contrôle sanitaire, un avis en ligne ou une photo suffisent à faire des dégâts.\n"
     "Pour ces établissements, je travaille sur la base d'un contrat de 1 à 12 passages par an "
     "selon le site, avec un plan de postes d'appâtage, un registre tenu à jour et un compte rendu "
     "à chaque visite, exploitable en contrôle HACCP. J'utilise des produits homologués, dans le "
     "respect de la loi EGalim."),

    ("Immeubles et copropriétés : traiter les parties communes",
     "Dans un immeuble, le local poubelles, les gaines techniques et les caves forment un réseau "
     "que les rongeurs empruntent d'un étage à l'autre. Intervenir dans un seul appartement "
     "revient le plus souvent à déplacer le problème.\n"
     "Je travaille régulièrement avec des syndics et des agences du secteur : je traite les parties "
     "communes, je sécurise les accès et je fournis un compte rendu écrit que le gestionnaire peut "
     "transmettre aux copropriétaires ou aux locataires."),

    ("Mon intervention, du premier appel au contrôle",
     "Vous m'appelez, vous me décrivez ce que vous voyez : des crottes, des bruits la nuit, un sac "
     "éventré, une odeur. Je vous dis au téléphone si ça relève d'une intervention ou non, "
     "sans vous faire venir pour rien.\n"
     "Sur place, je cherche d'abord par où ils entrent et ce qui les attire. Je traite ensuite avec "
     "la méthode adaptée — chimique, mécanique ou multicapture — je ferme les accès quand c'est "
     "possible, et je repasse contrôler. Le déplacement est compris dans le tarif."),
] + [sec for sec in _lv["secs"] if sec[0] not in (
    # écartées : génériques (boucle des villes) ou redites des sections ci-dessus
    "Pourquoi des rongeurs à Laval",
    "Les cas classiques à Laval",
    "Mon intervention",
    "Comment se déroule mon intervention",
)]

# ---------- Questions réellement tapées dans Google ----------
_lv["faq"] = [
    ("Quel est le prix d'une dératisation à Laval ?",
     "Il n'y a pas de tarif unique : le prix dépend de l'espèce, de l'ampleur de l'infestation, "
     "de la surface et du nombre de passages nécessaires. Une souris isolée dans un pavillon et "
     "une colonie de rats dans une cave d'immeuble n'ont rien à voir. Le diagnostic et le devis "
     "sont gratuits, le déplacement est compris, et je vous annonce le prix avant de commencer."),
    ("Sous quel délai intervenez-vous à Laval ?",
     "Je vise 24 à 48 heures et j'y arrive la plupart du temps, mais ce n'est pas une garantie : "
     "tout dépend de mon planning et de la saison. Les urgences réelles passent devant. Je suis "
     "installé à Port-Brillet, à une vingtaine de minutes de Laval, et joignable de 8 h à 21 h en "
     "semaine et de 9 h à 18 h le week-end : pour un cas pressant, appelez-moi plutôt que d'écrire."),
    ("Intervenez-vous dans tous les quartiers de Laval ?",
     "Oui, du centre-ville à Avesnières, Hilard, Grenoux, Bourny, Saint-Nicolas, Thévalles, "
     "Les Fourches, le Pavement et Laval Nord, ainsi que dans les communes voisines comme "
     "Saint-Berthevin, Changé, Louverné, Bonchamp-lès-Laval ou L'Huisserie."),
    ("Le traitement est-il dangereux pour mes enfants ou mes animaux ?",
     "Les appâts sont placés dans des postes sécurisés qui ne s'ouvrent qu'avec une clé, et "
     "positionnés hors de portée. Je vous indique l'emplacement exact de chaque poste et ce qu'il "
     "faut surveiller. Quand la configuration ne permet pas de garantir cette sécurité, j'emploie "
     "des pièges mécaniques ou des multicaptures à la place."),
    ("Faut-il traiter tout l'immeuble ou seulement mon logement ?",
     "Dans un immeuble, les rongeurs circulent par les gaines, les caves et le local poubelles. "
     "Traiter un seul appartement règle rarement le problème durablement. Je vous dis après "
     "diagnostic si les parties communes doivent être vues, et je fournis un compte rendu écrit "
     "pour le syndic."),
    ("Comment savoir si ce sont des rats ou des souris ?",
     "Les crottes donnent la réponse : celles de souris font 3 à 6 mm et ressemblent à des grains "
     "de riz noirs, celles de rat 1,5 à 2 cm. Le bruit diffère aussi — la souris trottine la nuit "
     "dans les cloisons et les combles, le rat se fait entendre plus bas, en cave ou en sous-sol. "
     "Décrivez-moi ce que vous voyez au téléphone, je vous le dirai."),
] + [f for f in _lv["faq"] if "ongeurs" in f[0] or "ratiseur" in f[0]]

# ---------- Liens internes utiles depuis cette page ----------
_liens = list(_lv["links"])
_liens.insert(0, ("Dératisation des métiers de bouche à Laval", [
    ("Boulangerie et pâtisserie", "/deratisation-boulangerie-laval/"),
    ("Boucherie et charcuterie", "/deratisation-boucherie-laval/"),
    ("Restaurant", "/deratisation-restaurant-laval/"),
    ("Traiteur", "/deratisation-traiteur-laval/"),
    ("Cuisine collective", "/deratisation-cuisine-collective-laval/"),
    ("Contrats annuels", "/contrats-metiers-de-bouche/"),
]))
_lv["links"] = _liens
