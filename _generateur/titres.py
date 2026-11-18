# -*- coding: utf-8 -*-
# Réécriture des titres de référencement, novembre 2026.
#
# Constat Search Console (3 mois) : des pages affichées en première page sans
# aucun clic. « entreprise dépigeonnage » 283 affichages, position 8, 0 clic.
# « chenilles laval » 108 affichages, position 8, 0 clic. Le classement n'est
# pas le problème : c'est le titre affiché qui ne donne aucune raison de venir.
#
# Trois corrections :
#  1. « | Proxinuisibles » retiré de 281 titres. Google affiche déjà le nom du
#     site au-dessus du titre (déclaré dans le JSON-LD WebSite), donc ces
#     16 caractères répétaient ce qui est déjà à l'écran, sur 52 en moyenne.
#  2. Majuscules de titre (« Nid de Frelons Argentré-du-Plessis ») remplacées
#     par une écriture normale : en français, les capitales partout font
#     fabriqué à la chaîne.
#  3. Les caractères récupérés servent à dire ce qu'on fait et ce que ça coûte
#     (« devis gratuit », « traitement thermique », « échenillage »).
#
# Les pages déjà retravaillées à la main (accueil Laval, chenilles) ne sont pas
# touchées.

import re as _re
import unicodedata as _ud

_MAXT = 60

# Pages dont le titre a été écrit à la main : on n'y touche pas.
_GARDE = {"/deratisation-laval/"}


def _slug(s):
    s = _ud.normalize("NFD", s)
    s = "".join(c for c in s if _ud.category(c) != "Mn")
    s = s.lower().replace("’", "").replace("'", "")
    return _re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def _commune_dep(meta):
    """Retrouve (commune, département) dans la méta déjà écrite."""
    m = _re.search(r"à ([^(:,]+?) \((\d{2})\)", meta)
    return (m.group(1).strip(), m.group(2)) if m else None


def _a(v):
    """« à Laval », mais « au Genest-Saint-Isle » et « aux Hayes »."""
    if v.startswith("Le "):
        return "au " + v[3:]
    if v.startswith("Les "):
        return "aux " + v[4:]
    return "à " + v


def _pose(path, gabarits):
    """Pose le premier gabarit qui tient en 60 caractères."""
    for t in gabarits:
        if len(t) <= _MAXT:
            P[path]["title"] = t
            return True
    return False


# ---------- pages principales (écrites une par une) ----------
_HUB = {
    "/": "Dératiseur et anti-nuisibles en Mayenne et Ille-et-Vilaine",
    "/deratisation/": "Dératiseur en Mayenne et Ille-et-Vilaine : rats et souris",
    "/frelons-guepes/": "Destruction de nid de frelons et de guêpes (53 et 35)",
    "/frelon-asiatique/": "Frelon asiatique : destruction du nid (53 et 35)",
    # Le titre disait « en Mayenne » alors que quatre pages communes existent
    # en Ille-et-Vilaine et que tout le corps de la page couvre les deux.
    "/chenilles-processionnaires/": "Chenilles processionnaires (53 et 35) : échenillage",
    "/desinsectisation/": "Désinsectisation : cafards, puces, fourmis, mouches",
    "/blattes-cafards/": "Se débarrasser des cafards et des blattes (53 et 35)",
    "/fourmis/": "Traitement des fourmis en Mayenne et Ille-et-Vilaine",
    "/mouches/": "Invasion de mouches : badigeon actif de mai à décembre",
    "/puces/": "Traitement des puces en Mayenne et Ille-et-Vilaine",
    "/punaises-de-lit/": "Punaises de lit : traitement thermique (53 et 35)",
    "/taupier/": "Taupier en Mayenne et Ille-et-Vilaine : piégeage",
    "/depigeonnage/": "Entreprise de dépigeonnage en Mayenne et Ille-et-Vilaine",
    "/piegeur-agree/": "Piégeur agréé : fouines et ragondins (53 et 35)",
    "/debarras/": "Débarras de maison à Laval, Vitré et Rennes",
    "/contrat-annuel-deratisation/": "Contrat annuel de dératisation pour professionnels",
    "/contrats-metiers-de-bouche/": "Contrat de dératisation pour les métiers de bouche",
    "/particuliers/": "Dératiseur pour particuliers en Mayenne et Ille-et-Vilaine",
    "/professionnels/": "Dératisation pour professionnels à Laval et alentours",
    "/agriculteurs/": "Dératisation pour agriculteurs et éleveurs (53 et 35)",
    "/agences-syndics/": "Anti-nuisibles pour agences immobilières et syndics",
    "/contact/": "Demander un devis gratuit : contact et horaires",
    "/zones-intervention/": "Zones d’intervention en Mayenne et Ille-et-Vilaine",
    "/qui-suis-je/": "Qui suis-je ? Gwendal, dératiseur à Port-Brillet",
    "/questions-frequentes/": "Questions fréquentes sur les nuisibles et traitements",
    "/avis/": "Avis clients vérifiés sur Google",
    "/mentions-legales/": "Mentions légales",
}

# ---------- familles « prestation + commune » ----------
# Du plus informatif au plus court : on garde le premier qui tient.
_FAM = [
    ("/deratisation-", lambda v, d: [
        "Dératiseur %s (%s) : rats et souris, devis gratuit" % (_a(v), d),
        "Dératiseur %s (%s) : rats et souris" % (_a(v), d),
        "Dératiseur %s (%s) : rats" % (_a(v), d),
        "Dératiseur %s (%s)" % (_a(v), d)]),
    ("/frelons-guepes-", lambda v, d: [
        "Nid de frelons ou de guêpes %s (%s) : devis gratuit" % (_a(v), d),
        "Destruction de nid de frelons et guêpes %s (%s)" % (_a(v), d),
        "Nid de frelons et de guêpes %s (%s)" % (_a(v), d),
        "Nid de frelons %s (%s)" % (_a(v), d)]),
    ("/punaises-de-lit-", lambda v, d: [
        "Punaises de lit %s (%s) : traitement thermique" % (_a(v), d),
        "Punaises de lit %s (%s) : traitement" % (_a(v), d),
        "Punaises de lit %s (%s)" % (_a(v), d)]),
    ("/desinsectisation-", lambda v, d: [
        "Désinsectisation %s (%s) : cafards, puces, fourmis" % (_a(v), d),
        "Désinsectisation %s (%s) : cafards et puces" % (_a(v), d),
        "Désinsectisation %s (%s)" % (_a(v), d)]),
    ("/chenilles-processionnaires-", lambda v, d: [
        "Chenilles processionnaires %s (%s) : échenillage" % (_a(v), d),
        "Chenilles processionnaires %s (%s)" % (_a(v), d),
        "Chenilles processionnaires %s" % _a(v)]),
    ("/taupier-", lambda v, d: [
        "Taupier %s (%s) : piégeage des taupes, devis gratuit" % (_a(v), d),
        "Taupier %s (%s) : piégeage des taupes" % (_a(v), d),
        "Taupier %s (%s) : piégeage" % (_a(v), d),
        "Taupier %s (%s)" % (_a(v), d)]),
    ("/piegeur-agree-", lambda v, d: [
        "Piégeur agréé %s (%s) : fouines et ragondins" % (_a(v), d),
        "Piégeur agréé %s (%s) : fouines" % (_a(v), d),
        "Piégeur agréé %s (%s)" % (_a(v), d)]),
    ("/depigeonnage-", lambda v, d: [
        "Dépigeonnage %s (%s) : pics, filets, devis gratuit" % (_a(v), d),
        "Dépigeonnage %s (%s) : pics et filets" % (_a(v), d),
        "Dépigeonnage %s (%s)" % (_a(v), d)]),
    ("/debarras-", lambda v, d: [
        "Débarras %s (%s) : maison, cave, grenier" % (_a(v), d),
        "Débarras de maison %s (%s)" % (_a(v), d),
        "Débarras %s (%s)" % (_a(v), d)]),
]

# ---------- contrats métiers de bouche ----------
_METIER = {
    "restaurant": "restaurant", "restauration": "restaurant",
    "restaurant-entreprise": "restaurant d’entreprise",
    "restauration-entreprise": "restauration d’entreprise",
    "restauration-collective": "restauration collective",
    "boulangerie": "boulangerie", "boulangerie-patisserie": "boulangerie",
    "patisserie": "pâtisserie",
    "boucherie": "boucherie", "boucherie-traiteur": "boucherie",
    "boucherie-charcuterie": "boucherie", "charcuterie": "charcuterie",
    "traiteur": "traiteur", "cuisine-collective": "cuisine collective",
    "poissonnerie": "poissonnerie", "fromagerie": "fromagerie",
    "primeur": "primeur", "epicerie": "épicerie", "cave": "cave",
    "creperie": "crêperie", "pizzeria": "pizzeria", "brasserie": "brasserie",
}

# Index commune -> département, bâti à partir des métas qui portent déjà le
# numéro. Il sert aux pages dont la méta mentionne la commune sans son
# département (« à Louverné : bourg, farines… »).
_DEP = {}
for _p in P:
    _lu = _commune_dep(P[_p].get("meta", ""))
    if _lu:
        _DEP.setdefault(_slug(_lu[0]), _lu)

# Quelques descriptions reprises pour coller au mot que les gens tapent.
_META = {
    "/depigeonnage/":
        "Entreprise de dépigeonnage en Mayenne et Ille-et-Vilaine : pics, "
        "filets et câbles pour façades, toitures et bâtiments. Devis gratuit.",
    "/chenilles-processionnaires-laval/":
        "Chenilles processionnaires à Laval (53) : écopièges sur les troncs, "
        "coupe des cocons en hiver, aspiration sans insecticide sur les chênes.",
}
for _p, _m in _META.items():
    if _p in P:
        P[_p]["meta"] = _m

_fait = 0
_rate = []

for _p in list(P):
    if _p in _GARDE:
        continue
    _d = P[_p]
    if "title" not in _d:
        continue

    if _p in _HUB:
        _d["title"] = _HUB[_p]
        _fait += 1
        continue

    _lu = _commune_dep(_d.get("meta", ""))
    if not _lu:
        # Méta sans numéro de département : on reconnaît la commune par la fin
        # de l'URL, du segment le plus long au plus court.
        _seg = _p.strip("/").split("-")
        for _n in range(len(_seg), 0, -1):
            _cand = "-".join(_seg[-_n:])
            if _cand in _DEP:
                _lu = _DEP[_cand]
                break
    if not _lu:
        # toujours rien : on se contente d'ôter la marque répétée
        if "| Proxinuisibles" in _d["title"]:
            _d["title"] = _d["title"].split(" | Proxinuisibles")[0]
            _fait += 1
        continue
    _v, _dep = _lu
    _av = _a(_v)

    if _p.startswith("/contrat-deratisation-") or _p.startswith("/deratisation-"):
        _pre = "/contrat-deratisation-" if _p.startswith("/contrat-") else "/deratisation-"
        _reste = _p[len(_pre):].strip("/")
        # Le nom de commune de la méta (« Château-Gontier-sur-Mayenne ») ne
        # correspond pas toujours au segment d'URL : on reconnaît le métier par
        # le début de l'URL, du libellé le plus long au plus court.
        _ms = ""
        for _k in sorted(_METIER, key=len, reverse=True):
            if _reste == _k or _reste.startswith(_k + "-"):
                _ms = _k
                break
        if not _ms and _pre == "/contrat-deratisation-":
            _vs = _slug(_v)
            _ms = _reste[:-(len(_vs) + 1)] if _reste.endswith("-" + _vs) else _reste
        if _ms:
            _lib = _METIER.get(_ms, _ms.replace("-", " "))
            if _pose(_p, ["Dératisation %s %s (%s) : contrat annuel" % (_lib, _av, _dep),
                          "Dératisation %s %s (%s)" % (_lib, _av, _dep),
                          "Dératisation %s %s" % (_lib, _av),
                          "Contrat dératisation %s (%s)" % (_lib, _dep)]):
                _fait += 1
            else:
                _rate.append(_p)
            continue

    for _pref, _gab in _FAM:
        if _p.startswith(_pref):
            if _pose(_p, _gab(_v, _dep)):
                _fait += 1
            else:
                _rate.append(_p)
            break
    else:
        if "| Proxinuisibles" in _d["title"]:
            _d["title"] = _d["title"].split(" | Proxinuisibles")[0]
            _fait += 1

print("titres réécrits :", _fait, "| trop longs :", _rate)
