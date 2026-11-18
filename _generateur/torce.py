# -*- coding: utf-8 -*-
# Page dératisation de Torcé (35).
#
# Torcé avait deux pages contrats métiers de bouche et une page chenilles, mais
# aucune page dératisation. Elle ne pouvait pas entrer dans communes20km.py :
# la commune est à environ 23 km de Port-Brillet à vol d'oiseau, et ce fichier
# annonce « moins de 20 km » sur la page d'accueil et les zones d'intervention.
# Elle n'entre pas non plus dans CITIES, réservé aux villes principales qui
# alimentent le pied de page et le areaServed du balisage.

_T_SECS = [
 ("Un bourg de mille habitants entouré de champs",
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
  "Dans les jardins plantés de pins et le long des haies de chênes, j'interviens également sur les chenilles processionnaires : voir ma page <a href='/chenilles-processionnaires-torce/'>chenilles processionnaires à Torcé</a>."),
]

_T_FAQ = [
 ("Torcé fait-elle partie de votre secteur ?",
  "Oui. Je me déplace depuis Port-Brillet, en Mayenne, et j'interviens des deux côtés de la limite départementale, jusqu'à Vitré, Châteaubourg et La Guerche-de-Bretagne."),
 ("Intervenez-vous dans les fermes et les hameaux ?",
  "Oui, dans le bourg comme dans les hameaux et les exploitations isolées. Donnez-moi l'adresse, je m'y rends."),
 ("Je tiens un commerce de bouche à Torcé, que proposez-vous ?",
  "Un contrat avec le nombre de passages adapté au site et le registre sanitaire à jour. Voir mes pages <a href='/contrat-deratisation-boulangerie-torce/'>boulangerie</a> et <a href='/contrat-deratisation-boucherie-torce/'>boucherie</a> à Torcé."),
]

_T_LINKS = [
 ("Autres services à Torcé", [("Frelons et guêpes", "/frelons-guepes/"), ("Frelon asiatique", "/frelon-asiatique/"),
   ("Désinsectisation", "/desinsectisation/"), ("Blattes et cafards", "/blattes-cafards/"), ("Fourmis", "/fourmis/"),
   ("Mouches", "/mouches/"), ("Puces", "/puces/"), ("Punaises de lit", "/punaises-de-lit/"),
   ("Chenilles processionnaires à Torcé", "/chenilles-processionnaires-torce/"), ("Taupier", "/taupier/"),
   ("Dépigeonnage", "/depigeonnage/"), ("Piégeur agréé", "/piegeur-agree/")]),
 ("Communes voisines", [("Dératisation à Étrelles", "/deratisation-etrelles/"),
   ("Dératisation à Argentré-du-Plessis", "/deratisation-argentre-du-plessis/"),
   ("Dératisation à Châteaubourg", "/deratisation-chateaubourg/"),
   ("Dératisation à Vitré", "/deratisation-vitre/")]),
 ("Voir aussi", [("Zones d'intervention", "/zones-intervention/"), ("Particuliers", "/particuliers/"),
   ("Agriculteurs", "/agriculteurs/"), ("Professionnels", "/professionnels/"), ("Devis gratuit", "/contact/")]),
]

if "/deratisation-torce/" not in P:
    add("/deratisation-torce/",
        h1="Dératisation à Torcé (35) : rats, souris et autres nuisibles",
        title="Dératiseur à Torcé (35) : rats et souris, devis gratuit",
        meta="Dératisation à Torcé (35), entre Vitré et Châteaubourg : rats dans les bâtiments agricoles, souris dans les maisons et les hameaux. Devis gratuit.",
        lead="Torcé est une commune de la campagne vitréenne, un bourg et des hameaux au milieu des champs. "
             "Rats dans les hangars et les stocks, souris dans les maisons et les dépendances : voici ce que je "
             "rencontre le plus souvent dans le secteur, et comment j'interviens.",
        secs=_T_SECS, faq=_T_FAQ, links=_T_LINKS, kind="ville")
    # Les trois autres pages de Torcé pointent vers la nouvelle, pour qu'elle
    # ne dépende pas du seul lien de la page « zones d'intervention ».
    for _p in ("/chenilles-processionnaires-torce/",
               "/contrat-deratisation-boulangerie-torce/",
               "/contrat-deratisation-boucherie-torce/"):
        _d = P.get(_p)
        if not _d:
            continue
        _ls = list(_d.get("links") or [])
        for _i, (_t, _l) in enumerate(_ls):
            if _t.startswith("Autres services"):
                if not any(u == "/deratisation-torce/" for _, u in _l):
                    _ls[_i] = (_t, [("Dératisation à Torcé", "/deratisation-torce/")] + list(_l))
                break
        else:
            _ls.insert(0, ("Autres services à Torcé",
                           [("Dératisation à Torcé", "/deratisation-torce/")]))
        _d["links"] = _ls

    # Pas de rubrique à part pour une seule commune : on glisse Torcé dans la
    # liste principale des communes de la page « zones d'intervention ».
    for _i, (_t, _l) in enumerate(P["/zones-intervention/"]["links"]):
        if _t == "Les communes":
            P["/zones-intervention/"]["links"][_i] = (
                _t, list(_l) + [("Dératisation Torcé", "/deratisation-torce/")])
            break
