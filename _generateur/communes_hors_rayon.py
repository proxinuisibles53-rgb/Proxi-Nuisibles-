# -*- coding: utf-8 -*-
# Pages dératisation des communes situées au-delà du rayon de 20 km, mais qui
# ne sont pas des villes principales.
#
# Elles ne peuvent pas entrer dans communes20km.py : ce fichier annonce
# « communes où j'interviens à moins de 20 km » sur la page d'accueil et sur
# les zones d'intervention, et ces communes sont entre 23 et 49 km de
# Port-Brillet. Elles n'entrent pas non plus dans CITIES, réservé aux villes
# principales qui alimentent le pied de page et le areaServed du balisage.
#
# Torcé : repérée parce qu'elle avait deux contrats métiers de bouche et une
# page chenilles sans page dératisation. Les trois communes du couloir rennais
# (Chantepie, Noyal-sur-Vilaine, Thorigné-Fouillard) apparaissaient dans la
# Search Console sans aucune page ; toutes trois sont plus proches de
# Port-Brillet que Rennes, déjà couverte.

_HR = []


def _HRV(slug, nom, dep, lead, secs, faq, voisins, autres):
    _HR.append((slug, nom, dep, lead, secs, faq, voisins, autres))


_HRV("torce", "Torcé", "35",
 "Torcé est une commune de la campagne vitréenne, un bourg et des hameaux au milieu des champs. "
 "Rats dans les hangars et les stocks, souris dans les maisons et les dépendances : voici ce que je "
 "rencontre le plus souvent dans le secteur, et comment j'interviens.",
 [("Un bourg de mille habitants entouré de champs",
   "Torcé compte un peu plus de mille habitants sur quatorze kilomètres carrés, dans la campagne qui sépare Vitré de Châteaubourg. Le bâti se limite au bourg et à quelques hameaux : partout ailleurs, ce sont des champs, des haies et des chemins.\n"
   "C'est la configuration classique où les rongeurs ne traversent jamais de zone construite. Ils passent d'une haie à un hangar, d'un hangar à une dépendance, et finissent dans une maison sans que personne ait rien vu venir."),
  ("Les bâtiments agricoles d'abord",
   "Sur une commune à cette densité, les premiers lieux touchés sont les bâtiments d'exploitation : stocks de céréales, hangars, étables, poulaillers. Un silo mal fermé ou un sac entamé suffit à nourrir une colonie tout l'hiver.\n"
   "J'inspecte les abords avant les bâtiments, parce que c'est dehors que tout se joue : les points d'entrée, les tas de bois contre un mur, les gaines non rebouchées. Je traite ensuite avec la méthode qui convient au site, et je repasse contrôler."),
  ("Entre Vitré et Châteaubourg, et à l'est de la Mayenne",
   "Torcé est tournée vers Vitré, dont elle dépend pour les commerces et les services. Les gares de Saint-Aubin-des-Landes, de Vitré et de Châteaubourg sont les plus proches, et l'axe routier Rennes-Laval passe à quelques minutes.\n"
   "Je viens depuis Port-Brillet, de l'autre côté de la limite départementale. Le déplacement est compris dans le tarif, et je donne le prix avant de venir."),
  ("Autres nuisibles à Torcé",
   "Je traite aussi les nids de guêpes et de frelons dans les haies, les toitures et les bâtiments agricoles, les taupes dans les prairies et les pelouses, les pigeons dans les granges, et les fourmis et les cafards dans les habitations.\n"
   "Dans les jardins plantés de pins et le long des haies de chênes, j'interviens également sur les chenilles processionnaires : voir ma page <a href='/chenilles-processionnaires-torce/'>chenilles processionnaires à Torcé</a>.")],
 [("Torcé fait-elle partie de votre secteur ?",
   "Oui. Je me déplace depuis Port-Brillet, en Mayenne, et j'interviens des deux côtés de la limite départementale, jusqu'à Vitré, Châteaubourg et La Guerche-de-Bretagne."),
  ("Intervenez-vous dans les fermes et les hameaux ?",
   "Oui, dans le bourg comme dans les hameaux et les exploitations isolées. Donnez-moi l'adresse, je m'y rends."),
  ("Je tiens un commerce de bouche à Torcé, que proposez-vous ?",
   "Un contrat avec le nombre de passages adapté au site et le registre sanitaire à jour. Voir mes pages <a href='/contrat-deratisation-boulangerie-torce/'>boulangerie</a> et <a href='/contrat-deratisation-boucherie-torce/'>boucherie</a> à Torcé.")],
 [("Dératisation à Étrelles", "/deratisation-etrelles/"),
  ("Dératisation à Argentré-du-Plessis", "/deratisation-argentre-du-plessis/"),
  ("Dératisation à Châteaubourg", "/deratisation-chateaubourg/"),
  ("Dératisation à Vitré", "/deratisation-vitre/")],
 [("Chenilles processionnaires à Torcé", "/chenilles-processionnaires-torce/")])


_HRV("chantepie", "Chantepie", "35",
 "Chantepie s'est construite vite aux portes de Rennes : résidences récentes, quartiers pavillonnaires "
 "et zones d'activité. Rats délogés par les chantiers, souris dans les pavillons, rongeurs dans les "
 "locaux poubelles des copropriétés : voici ce que je rencontre et comment j'interviens.",
 [("Une commune qui s'est construite vite",
   "Chantepie compte aujourd'hui plus de dix mille habitants, contre quelques milliers il y a trente ans. Cette croissance se voit dans le bâti : des résidences collectives récentes, des quartiers pavillonnaires et des zones d'activité, tous construits sur ce qui était de la campagne.\n"
   "Les chantiers et les terrassements dérangent les rongeurs installés dans les talus et les friches. Délogés, ils se réfugient dans le premier bâtiment venu : un garage, un local technique, un vide sanitaire."),
  ("Copropriétés et locaux poubelles",
   "Dans les résidences, le point sensible est presque toujours le local poubelles et ses abords : conteneurs mal refermés, sacs posés à côté, gaines techniques ouvertes. Un rat qui y trouve à manger revient, et finit par remonter par les colonnes.\n"
   "Pour un syndic ou un bailleur, je traite l'ensemble de la résidence plutôt que l'appartement qui a signalé le problème : traiter un seul logement ne règle jamais une infestation de parties communes."),
  ("Pavillons, jardins et composteurs",
   "Dans les quartiers pavillonnaires, les rats viennent pour la nourriture : composteur ouvert, poulailler, croquettes laissées dehors, mangeoire à oiseaux. Les souris, elles, entrent à l'automne par les gaines, les seuils de porte de garage et les trappes de combles.\n"
   "Je commence par le tour de la maison. C'est dehors que se trouvent les points d'entrée, et les boucher est ce qui évite que ça recommence l'hiver suivant."),
  ("Autres nuisibles à Chantepie",
   "J'interviens aussi sur les nids de guêpes et de frelons dans les haies, les façades et les loggias — voir ma page <a href='/frelons-guepes-chantepie/'>frelons et guêpes à Chantepie</a> — ainsi que sur les cafards, les fourmis et les punaises de lit dans les logements.")],
 [("Chantepie fait-elle partie de votre zone ?",
   "Oui. J'interviens sur tout le couloir Laval-Rennes, et Chantepie est plus proche de ma base que Rennes même."),
  ("Je suis syndic, intervenez-vous en copropriété ?",
   "Oui. Je traite les parties communes, les locaux poubelles et les logements concernés, avec un compte rendu écrit après chaque passage."),
  ("Des travaux ont fait sortir des rats, que faire ?",
   "C'est fréquent sur une commune en chantier. Ne bouchez rien dans l'urgence : appelez-moi, je repère d'abord par où ils circulent, sinon on les enferme à l'intérieur.")],
 [("Dératisation à Rennes", "/deratisation-rennes/"),
  ("Dératisation à Cesson-Sévigné", "/deratisation-cesson-sevigne/"),
  ("Dératisation à Châteaubourg", "/deratisation-chateaubourg/")],
 [("Frelons et guêpes à Chantepie", "/frelons-guepes-chantepie/")])


_HRV("noyal-sur-vilaine", "Noyal-sur-Vilaine", "35",
 "Noyal-sur-Vilaine réunit un bourg ancien, des lotissements et d'importantes zones d'activité sur "
 "l'axe Rennes-Vitré. Rats près de la rivière et des entreprises, souris dans le bâti ancien : voici "
 "ce que je rencontre et comment j'interviens.",
 [("La rivière, les fossés et les prairies",
   "La Vilaine traverse la commune. Les berges, les fossés et les prairies humides sont le terrain de prédilection du rat surmulot, qui y creuse ses galeries et remonte ensuite vers les jardins, les dépendances et les bâtiments.\n"
   "Près de l'eau, je choisis les emplacements et les dispositifs avec précaution, pour protéger la faune et les animaux domestiques. C'est une contrainte réelle, et elle change la façon de traiter."),
  ("Les zones d'activité de l'axe Rennes-Vitré",
   "Noyal-sur-Vilaine accueille des entreprises et des sites agroalimentaires le long de la quatre-voies. Pour ces établissements, la présence de rongeurs n'est pas seulement un désagrément : c'est un point de contrôle sanitaire, avec un registre à tenir et des passages à justifier.\n"
   "Je propose des contrats avec le nombre de passages adapté au site, un plan des postes et un compte rendu écrit à chaque intervention."),
  ("Un bourg ancien et des lotissements",
   "Dans le bourg, les murs épais, les caves et les combles des maisons anciennes offrent aux souris quantité de passages, surtout à l'approche de l'hiver. Dans les lotissements plus récents, elles entrent par les gaines, les seuils de garage et les trappes.\n"
   "Je repère les cheminements avant de traiter, puis je vous indique les ouvertures à fermer. C'est ce travail-là qui évite la récidive."),
  ("Autres nuisibles à Noyal-sur-Vilaine",
   "Je traite aussi les nids de guêpes et de frelons — voir ma page <a href='/frelons-guepes-noyal-sur-vilaine/'>frelons et guêpes à Noyal-sur-Vilaine</a> — et les punaises de lit par la chaleur, sur ma page <a href='/punaises-de-lit-noyal-sur-vilaine/'>punaises de lit à Noyal-sur-Vilaine</a>.")],
 [("Intervenez-vous pour les entreprises de la zone d'activité ?",
   "Oui, avec un contrat adapté au site : nombre de passages, plan des postes, registre et compte rendu écrit à chaque intervention."),
  ("Y a-t-il plus de rats près de la Vilaine ?",
   "Souvent, oui. Les berges et les fossés abritent des populations de surmulots qui remontent vers les habitations. Je tiens compte de la proximité de l'eau dans le choix des emplacements."),
  ("Noyal-sur-Vilaine est-elle dans votre secteur ?",
   "Oui. J'interviens sur tout l'axe Laval-Rennes, et la commune est sur ce trajet.")],
 [("Dératisation à Rennes", "/deratisation-rennes/"),
  ("Dératisation à Châteaubourg", "/deratisation-chateaubourg/"),
  ("Dératisation à Cesson-Sévigné", "/deratisation-cesson-sevigne/"),
  ("Dératisation à Vitré", "/deratisation-vitre/")],
 [("Frelons et guêpes à Noyal-sur-Vilaine", "/frelons-guepes-noyal-sur-vilaine/"),
  ("Punaises de lit à Noyal-sur-Vilaine", "/punaises-de-lit-noyal-sur-vilaine/")])


_HRV("thorigne-fouillard", "Thorigné-Fouillard", "35",
 "Thorigné-Fouillard est une commune résidentielle adossée à la forêt de Rennes. Rats attirés par les "
 "composteurs et les abris de jardin, souris dans les combles et les garages : voici ce que je "
 "rencontre et comment j'interviens.",
 [("La lisière de la forêt de Rennes",
   "La commune est bordée par le massif forestier, et cette lisière change tout. Les talus, les fossés et les chemins servent de corridors aux rongeurs, qui rejoignent les jardins puis les maisons sans jamais traverser de zone construite.\n"
   "Les maisons les plus proches des bois sont les plus souvent concernées, et pas seulement par les rats et les souris : les mulots et les loirs s'invitent aussi dans les combles à l'automne."),
  ("Lotissements, composteurs et abris de jardin",
   "Thorigné-Fouillard est faite de lotissements et de maisons individuelles avec jardin. Ce qui attire les rats, c'est la nourriture accessible : composteur ouvert, poulailler familial, croquettes du chien laissées dehors, mangeoire à oiseaux sous laquelle les graines tombent.\n"
   "Je commence par le tour du terrain. Déplacer un composteur ou fermer un abri règle parfois le problème mieux qu'un traitement, et je vous le dirai si c'est le cas."),
  ("Écoles, équipements et espaces communaux",
   "Une commune familiale comme celle-ci compte des écoles, des salles, des terrains de sport et des espaces verts. Sur ces sites, le traitement doit tenir compte de la présence d'enfants et d'animaux : emplacements sécurisés, dispositifs fermés, passages programmés hors fréquentation.\n"
   "J'interviens pour les particuliers comme pour les collectivités et les gestionnaires de site, avec un compte rendu écrit."),
  ("Autres nuisibles à Thorigné-Fouillard",
   "J'interviens aussi sur les nids de guêpes et de frelons, nombreux du fait de la forêt — voir ma page <a href='/frelons-guepes-thorigne-fouillard/'>frelons et guêpes à Thorigné-Fouillard</a> — sur les <a href='/chenilles-processionnaires-thorigne-fouillard/'>chenilles processionnaires</a> et sur les <a href='/punaises-de-lit-thorigne-fouillard/'>punaises de lit</a>.")],
 [("Y a-t-il plus de rongeurs près de la forêt ?",
   "C'est souvent le cas : les lisières abritent des populations qui s'approchent des maisons. Je pose des points de contrôle à l'extérieur et je vous conseille sur l'entretien des abords."),
  ("Intervenez-vous dans les écoles et les équipements communaux ?",
   "Oui, avec des dispositifs fermés, des emplacements sécurisés et des passages programmés en dehors des heures de fréquentation."),
  ("Thorigné-Fouillard est-elle dans votre zone ?",
   "Oui. J'interviens sur tout le couloir Laval-Rennes, et la commune est plus proche de ma base que Rennes même.")],
 [("Dératisation à Cesson-Sévigné", "/deratisation-cesson-sevigne/"),
  ("Dératisation à Rennes", "/deratisation-rennes/"),
  ("Dératisation à Châteaubourg", "/deratisation-chateaubourg/")],
 [("Frelons et guêpes à Thorigné-Fouillard", "/frelons-guepes-thorigne-fouillard/"),
  ("Chenilles processionnaires à Thorigné-Fouillard", "/chenilles-processionnaires-thorigne-fouillard/"),
  ("Punaises de lit à Thorigné-Fouillard", "/punaises-de-lit-thorigne-fouillard/")])


_SERVICES_HR = [("Frelons et guêpes", "/frelons-guepes/"), ("Frelon asiatique", "/frelon-asiatique/"),
                ("Désinsectisation", "/desinsectisation/"), ("Blattes et cafards", "/blattes-cafards/"),
                ("Fourmis", "/fourmis/"), ("Mouches", "/mouches/"), ("Puces", "/puces/"),
                ("Punaises de lit", "/punaises-de-lit/"),
                ("Chenilles processionnaires", "/chenilles-processionnaires/"), ("Taupier", "/taupier/"),
                ("Dépigeonnage", "/depigeonnage/"), ("Piégeur agréé", "/piegeur-agree/")]

_hr_ajoutees = []
for _slug, _nom, _dep, _lead, _secs, _faq, _vois, _autres in _HR:
    _path = "/deratisation-%s/" % _slug
    if _path in P:
        continue
    _links = [("Autres services à %s" % _nom, list(_autres) + _SERVICES_HR)]
    _vois = [(l, u) for l, u in _vois if u in P]
    if _vois:
        _links.append(("Communes voisines", _vois))
    _links.append(("Voir aussi", [("Zones d'intervention", "/zones-intervention/"), ("Particuliers", "/particuliers/"),
                                  ("Agriculteurs", "/agriculteurs/"), ("Professionnels", "/professionnels/"),
                                  ("Devis gratuit", "/contact/")]))
    add(_path,
        h1="Dératisation à %s (%s) : rats, souris et autres nuisibles" % (_nom, _dep),
        title="Dératiseur à %s (%s) : rats et souris" % (_nom, _dep),
        meta="Dératisation à %s (%s) : rats, souris et autres nuisibles dans les maisons, les résidences et les locaux professionnels. Devis gratuit." % (_nom, _dep),
        lead=_lead, secs=_secs, faq=_faq, links=_links, kind="ville")
    _hr_ajoutees.append(("Dératisation %s" % _nom, _path))

    # La page de la commune pour les autres prestations pointe vers celle-ci.
    for _p in ("/chenilles-processionnaires-%s/" % _slug, "/frelons-guepes-%s/" % _slug,
               "/punaises-de-lit-%s/" % _slug, "/contrat-deratisation-boulangerie-%s/" % _slug,
               "/contrat-deratisation-boucherie-%s/" % _slug):
        _d = P.get(_p)
        if not _d:
            continue
        _ls = list(_d.get("links") or [])
        for _i, (_t, _l) in enumerate(_ls):
            if _t.startswith("Autres services"):
                if not any(u == _path for _, u in _l):
                    _ls[_i] = (_t, [("Dératisation à %s" % _nom, _path)] + list(_l))
                break
        else:
            _ls.insert(0, ("Autres services à %s" % _nom, [("Dératisation à %s" % _nom, _path)]))
        _d["links"] = _ls

# Pas de rubrique à part : on glisse ces communes dans la liste principale de
# la page « zones d'intervention ».
if _hr_ajoutees:
    for _i, (_t, _l) in enumerate(P["/zones-intervention/"]["links"]):
        if _t == "Les communes":
            P["/zones-intervention/"]["links"][_i] = (_t, list(_l) + _hr_ajoutees)
            break
