# -*- coding: utf-8 -*-
# Mot-clé « dératiseur » : titre Google, description, introduction, un court passage et une question
# sur toutes les pages dératisation, plus les pages « publics » et la page d'accueil.
# Exécuté en dernier (après mentions.py) : il retouche les pages déjà déclarées dans P.
import re as _re
import zlib as _zlib


def _fit(cands, maxi):
    cands = [c for c in cands if c]
    for c in cands:
        if len(c) <= maxi:
            return c
    return cands[-1]


def _insere_apres_premiere(d, sec):
    s = list(d["secs"])
    s.insert(1 if s else 0, sec)
    d["secs"] = s


def _faq_debut(d, q, a):
    if any(x[0] == q for x in d["faq"]):
        return
    d["faq"] = [(q, a)] + list(d["faq"])


# ---------- 1. Page « Dératisation » ----------
_d = P["/deratisation/"]
_d["title"] = _fit(["Dératiseur et Dératisation Mayenne et 35 | Proxinuisibles", "Dératiseur Mayenne et Ille-et-Vilaine | Proxinuisibles"], 60)
_d["meta"] = _fit(["Dératiseur en Mayenne et Ille-et-Vilaine : dératisation de rats et souris dans les maisons, fermes et commerces. Diagnostic et devis gratuits.",
                   "Dératiseur en Mayenne et Ille-et-Vilaine : rats, souris, rongeurs. Diagnostic et devis gratuits."], 158)
_d["lead"] = "Vous cherchez un dératiseur professionnel ? " + _d["lead"]
_insere_apres_premiere(_d, ("Un dératiseur professionnel, installé à Port-Brillet",
    "Je suis dératiseur indépendant, installé à Port-Brillet, en Mayenne, et je travaille dans la lutte contre les nuisibles depuis 2016. Un dératiseur ne se contente pas de poser du produit : je cherche d'abord pourquoi les rongeurs sont là, par où ils entrent et ce qui les attire.\nJe traite ensuite avec la méthode adaptée (chimique, mécanique ou multicapture), je ferme les accès quand c'est possible et je repasse contrôler. Je suis titulaire du Certibiocide n° 059860 et j'utilise des produits homologués, dans le respect de la loi EGalim."))
_faq_debut(_d, "Que fait un dératiseur ?",
    "Un dératiseur identifie les rongeurs, repère par où ils entrent, les élimine avec la méthode adaptée, puis ferme les accès et contrôle le résultat. Je réalise moi-même toutes ces étapes, du diagnostic au suivi.")
_faq_debut(_d, "Combien coûte un dératiseur ?",
    "Le prix dépend de l'ampleur de l'infestation et des lieux : je ne propose pas de tarif unique. Le diagnostic et le devis sont gratuits, et le déplacement est compris.")

# ---------- 2. Pages « Dératisation + commune » ----------
_VAR = [
 "Je suis dératiseur professionnel, installé à Port-Brillet, en Mayenne. À {nom}, je commence par un diagnostic gratuit : je cherche les passages, les traces et les sources de nourriture, puis je choisis la méthode adaptée (chimique, mécanique ou multicapture) et je ferme les accès pour éviter le retour des rongeurs.",
 "Faire appel à un dératiseur, c'est d'abord comprendre pourquoi les rongeurs sont là. À {nom}, je repère les points d'entrée, je traite avec des produits homologués dans le respect de la loi EGalim, puis je repasse vérifier que l'infestation est terminée. Je suis titulaire du Certibiocide n° 059860.",
 "Dératiseur indépendant, je travaille dans la lutte contre les nuisibles depuis 2016. J'interviens à {nom} chez les particuliers, les agriculteurs et les professionnels, avec un seul interlocuteur du premier appel au suivi et un tarif annoncé avant ma venue, déplacement compris.",
]
_n_com = 0
for _p, _d in P.items():
    _m = _re.match(r"^/deratisation-([a-z0-9-]+)/$", _p)
    if not _m or _d.get("kind") != "ville":
        continue
    _h = _re.match(r"^Dératisation à (.+?) \((\d\d)\)", _d["h1"])
    if not _h:
        continue
    nom, dep = _h.group(1), _h.group(2)
    _d["title"] = _fit(["Dératiseur et Dératisation à %s (%s) | Proxinuisibles" % (nom, dep),
                        "Dératiseur et Dératisation %s | Proxinuisibles" % nom,
                        "Dératiseur à %s (%s) | Proxinuisibles" % (nom, dep),
                        "Dératiseur à %s | Proxinuisibles" % nom,
                        "Dératiseur %s | Proxinuisibles" % nom], 60)
    _km = _re.search(r"à ([\d,]+) km de Port-Brillet", _d["meta"])
    _d["meta"] = _fit((["Dératiseur à %s (%s) : dératisation et lutte contre les nuisibles, à %s km de Port-Brillet. Rats, souris, frelons, taupes. Devis gratuit." % (nom, dep, _km.group(1))] if _km else [])
                      + ["Dératiseur à %s (%s) : " % (nom, dep) + _d["meta"][0].lower() + _d["meta"][1:] if not _km else "",
                       "Dératiseur à %s (%s) : dératisation de rats, souris et autres nuisibles. Devis gratuit, déplacement compris." % (nom, dep),
                       "Dératiseur à %s : dératisation de rats et souris. Devis gratuit." % nom], 158)
    _d["lead"] = "Vous cherchez un dératiseur à %s ? " % nom + _d["lead"]
    _t = _VAR[_zlib.crc32(_p.encode()) % 3].format(nom=nom)
    _insere_apres_premiere(_d, ("Un dératiseur à %s, installé à Port-Brillet" % nom, _t))
    _faq_debut(_d, "Que fait un dératiseur à %s ?" % nom,
               "Un dératiseur identifie les rongeurs, repère par où ils entrent, les élimine avec la méthode adaptée, puis ferme les accès et contrôle le résultat. À %s, je réalise moi-même ces étapes, du diagnostic au suivi." % nom)
    _n_com += 1

# ---------- 3. Pages contrats métiers de bouche et contrat annuel ----------
for _p, _d in P.items():
    if _d.get("kind") == "metier" or _p in ("/contrats-metiers-de-bouche/", "/contrat-annuel-deratisation/"):
        if "dératiseur" not in _d["lead"].lower():
            _d["lead"] = _d["lead"].rstrip() + " Dératiseur professionnel installé à Port-Brillet, j'assure moi-même le diagnostic, les passages et le compte rendu écrit."

# ---------- 4. Pages « publics » ----------
_d = P["/particuliers/"]
_d["title"] = _fit(["Dératiseur Particuliers Mayenne et 35 | Proxinuisibles", "Dératiseur Particuliers | Proxinuisibles"], 60)
_d["lead"] = "Un dératiseur et anti-nuisibles à votre porte. " + _d["lead"]

_d = P["/agriculteurs/"]
_d["title"] = _fit(["Dératiseur Agriculteurs et Éleveurs | Proxinuisibles"], 60)
_d["lead"] = "Vous cherchez un dératiseur pour votre exploitation ? " + _d["lead"]

_d = P["/professionnels/"]
_d["title"] = _fit(["Dératiseur Professionnels Laval | Proxinuisibles", "Dératiseur Professionnels | Proxinuisibles"], 60)
_d["lead"] = "Vous cherchez un dératiseur pour votre établissement ? " + _d["lead"]

_d = P["/agences-syndics/"]
_d["title"] = _fit(["Dératiseur Agences et Syndics | Proxinuisibles"], 60)
_d["lead"] = "Un dératiseur pour vos logements et vos parties communes. " + _d["lead"]

_d = P["/contrat-annuel-deratisation/"]
_d["title"] = _fit(["Dératiseur : Contrat Annuel Pro | Proxinuisibles", "Contrat Annuel Dératisation Pro | Proxinuisibles"], 60)

_d = P["/qui-suis-je/"]
_d["title"] = _fit(["Qui suis-je ? Gwendal, dératiseur | Proxinuisibles", "Qui suis-je ? | Anti-Nuisibles Mayenne | Proxinuisibles"], 60)
_d["meta"] = _fit(["Gwendal, dératiseur à la tête de Proxinuisibles : dératisation, nids de frelons et désinsectisation en Mayenne et Ille-et-Vilaine."], 158)
_d["lead"] = "Je suis dératiseur et je dirige Proxinuisibles depuis la Mayenne : j'interviens chez les particuliers, les agriculteurs et les professionnels."

_d = P["/zones-intervention/"]
_d["title"] = _fit(["Dératiseur Mayenne et 35 : zones d'intervention | Proxinuisibles", "Zones d'intervention Mayenne et 35 | Proxinuisibles"], 60)
_d["lead"] = "Dératiseur, désinsectisation, frelons : j'interviens dans toute la Mayenne et en Ille-et-Vilaine, de Laval à Rennes."

_d = P["/contact/"]
_d["title"] = _fit(["Devis Dératiseur et Anti-Nuisibles Laval | Proxinuisibles", "Devis Dératiseur Laval | Proxinuisibles"], 60)

_d = P["/questions-frequentes/"]
_faq_debut(_d, "Que fait un dératiseur ?",
           "Un dératiseur identifie les rongeurs, repère par où ils entrent, les élimine avec la méthode adaptée, puis ferme les accès et contrôle le résultat. Je réalise moi-même ces étapes, du diagnostic au suivi.")

# ---------- 5. Accueil ----------
_d = P["/"]
_d["title"] = _fit(["Dératiseur, Dératisation, Désinsectisation | Proxinuisibles", "Dératiseur, Désinsectisation, Frelons | Proxinuisibles"], 60)
_d["meta"] = _fit(["Dératiseur et anti-nuisibles en Mayenne et Ille-et-Vilaine : rats, insectes, frelons, guêpes, punaises de lit. Intervention rapide, devis gratuit."], 158)
_d["lead"] = "Dératiseur professionnel : rats, souris, insectes, frelons, guêpes, punaises de lit. J'interviens chez les particuliers, les agriculteurs et les professionnels en Mayenne et en Ille-et-Vilaine. Devis gratuit."
