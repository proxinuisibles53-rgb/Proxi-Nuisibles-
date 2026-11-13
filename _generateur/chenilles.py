# -*- coding: utf-8 -*-
# Page « Chenilles processionnaires » : renforcée pour la saison du pin
# (novembre 2026 - février 2027). Priorité donnée à l'échenillage, puis
# à l'écopiège, dont la pose doit précéder la descente.
# Exécuté après mentions.py et services_villes.py.

_ch = P["/chenilles-processionnaires/"]

_ch["title"] = "Chenilles processionnaires en Mayenne : échenillage"
_ch["meta"] = ("Échenillage et pose d'écopièges contre les chenilles processionnaires du pin, "
               "en Mayenne et Ille-et-Vilaine. Coupe des cocons en hiver, devis gratuit.")
_ch["lead"] = ("Un cocon blanc et soyeux au bout d'une branche de pin, une file de chenilles au pied "
               "d'un arbre ? Je coupe les cocons et je pose des écopièges sur les troncs, en Mayenne "
               "et en Ille-et-Vilaine. N'y touchez pas vous-même : les poils urticants se dispersent "
               "au moindre geste, et le vent les porte plus loin qu'on ne croit.")

# ---------- sections ajoutées en tête, dans l'ordre de la saison ----------
_nouvelles = [
    ("Le calendrier de la saison, et pourquoi il commande tout",
     "La processionnaire du pin suit un cycle fixe, et chaque méthode n'a qu'une fenêtre d'emploi. "
     "C'est ce qui décide de ce qu'on peut faire pour vous aujourd'hui, et de ce qu'il sera trop tard "
     "de faire dans six semaines.\n"
     "- <strong>Juillet et août</strong> : les papillons pondent sur les aiguilles. Rien à faire à ce stade.\n"
     "- <strong>Automne</strong> : les chenilles éclosent et commencent à tisser leurs abris.\n"
     "- <strong>D'octobre à janvier</strong> : pose des écopièges autour des troncs. Ils doivent être "
     "en place avant la descente, sans quoi ils ne servent à rien pour l'année en cours.\n"
     "- <strong>De novembre à février</strong> : les cocons d'hiver sont visibles dans la cime. "
     "C'est la période de l'échenillage, et c'est aussi le moment où vous les repérez depuis votre jardin.\n"
     "- <strong>De février à avril</strong> selon l'année et la météo : les chenilles descendent en file "
     "le long du tronc pour s'enfouir et se transformer. À partir de là, l'écopiège posé fait son travail ; "
     "un écopiège posé trop tard, non.\n"
     "Si vous hésitez entre les deux, appelez-moi : en décembre et en janvier, je combine souvent les deux "
     "sur le même arbre, la coupe pour ce qui est accessible et le piège pour le reste."),

    ("L'échenillage, de la coupe à l'évacuation",
     "Échenillage est le nom technique de la coupe des cocons. Concrètement, je coupe la branche qui porte "
     "le cocon, je l'enferme aussitôt dans un sac fermé, et je l'évacue pour destruction. Rien ne tombe au sol, "
     "rien ne reste dans votre jardin.\n"
     "Je porte une protection complète, parce que les poils se libèrent dès qu'on touche au cocon et qu'ils "
     "restent urticants longtemps, même sur un cocon vide ou tombé. C'est précisément pour cela que je vous "
     "déconseille de monter sur une échelle avec un sécateur : ce n'est pas la hauteur le danger, c'est le "
     "nuage de poils au-dessus de votre tête.\n"
     "Lors du diagnostic, je regarde la hauteur et l'accès. Quand un cocon est hors de portée en sécurité, "
     "je vous le dis franchement et on bascule sur l'écopiège, qui traitera l'arbre à la descente."),

    ("Un risque pour la santé reconnu par la loi",
     "Depuis le décret n° 2022-686 du 25 avril 2022, les chenilles processionnaires du pin et du chêne "
     "figurent parmi les espèces dont la prolifération est nuisible à la santé humaine. Le préfet de "
     "département peut fixer par arrêté les mesures applicables là où l'espèce est présente.\n"
     "Ce que ça veut dire pour vous : il n'existe pas d'obligation nationale et uniforme de traiter vos arbres, "
     "mais un arrêté préfectoral ou un règlement municipal peut en imposer sur votre commune. Si vous êtes "
     "propriétaire, bailleur, syndic ou responsable d'un établissement recevant du public, renseignez-vous "
     "auprès de votre mairie avant de décider de ne rien faire."),

    ("Écoles, crèches, campings, terrains de sport et copropriétés",
     "Un pin infesté au bord d'une cour de récréation, d'une aire de jeux ou d'un terrain de sport, et ce sont "
     "des dizaines de personnes exposées, dont des enfants qui ramassent tout ce qu'ils trouvent.\n"
     "J'interviens pour les communes, les écoles, les campings, les résidences et les syndics, avec un compte "
     "rendu écrit à chaque passage, exploitable par un gestionnaire ou présentable en conseil syndical. "
     "Sur un parc arboré, je repère d'abord l'ensemble des arbres concernés, puis je vous propose un plan de "
     "traitement hiérarchisé plutôt qu'un devis arbre par arbre."),
]

# « La coupe des cocons » et « Quand traiter » font double emploi avec les
# sections ci-dessus ; elles restent sur les pages communes.
_ch["secs"] = _nouvelles + [s for s in _ch["secs"]
                            if s[0] not in ("Quand traiter", "La coupe des cocons, ou échenillage")]

# ---------- questions réellement posées ----------
_ch["faq"] = [
    ("Quand faut-il intervenir contre les chenilles processionnaires ?",
     "L'échenillage se pratique de novembre à février, quand les cocons sont visibles dans la cime. "
     "Les écopièges se posent d'octobre à janvier : ils doivent être en place avant la descente des "
     "chenilles, qui démarre selon l'année entre février et avril. Un écopiège posé après le début de "
     "la procession ne sert plus à rien pour la saison."),
    ("Suis-je obligé de faire traiter mes arbres ?",
     "Il n'y a pas d'obligation nationale générale. Mais depuis le décret du 25 avril 2022, les "
     "processionnaires sont classées parmi les espèces nuisibles à la santé humaine, et le préfet peut "
     "fixer par arrêté des mesures applicables sur un secteur donné. Renseignez-vous auprès de votre "
     "mairie, qui saura si un arrêté s'applique chez vous."),
    ("Combien coûte un échenillage ?",
     "Cela dépend du nombre de cocons, de la hauteur des arbres et de l'accès. Un pin de jardin avec deux "
     "cocons accessibles et un parc de résidence avec quinze arbres n'ont rien à voir. Je me déplace, "
     "je regarde, et je vous annonce le prix avant de commencer. Le diagnostic et le devis sont gratuits, "
     "le déplacement est compris."),
    ("Les cocons sont très haut dans l'arbre, pouvez-vous quand même intervenir ?",
     "Je regarde la hauteur et l'accessibilité lors du diagnostic. Quand je peux couper en sécurité, je coupe. "
     "Quand l'arbre dépasse ce que je peux atteindre sans risque, je vous le dis et je propose l'écopiège, "
     "qui prend les chenilles à la descente quelle que soit la hauteur du cocon."),
    ("Un cocon est tombé au sol dans mon jardin, que faire ?",
     "N'y touchez pas, même avec des gants de jardinage, et éloignez les enfants et les animaux de la zone. "
     "Les poils restent urticants longtemps après la chute, et un simple coup de râteau ou de souffleur les "
     "remet en suspension. Appelez-moi, je viens le récupérer et l'évacuer."),
] + list(_ch["faq"])
