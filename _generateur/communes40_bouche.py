# -*- coding: utf-8 -*-
# Pages « contrat de dératisation » boulangerie et boucherie : 51 communes à moins de 40 km de Port-Brillet
# (communes les plus peuplées ; distances à vol d'oiseau, centre à centre). Texte volontairement sans affirmation sur les commerces locaux.
import json as _json
_B40 = _json.load(open("/home/claude/bouche40.json", encoding="utf-8"))
_DEP = {"53": "Mayenne", "35": "Ille-et-Vilaine"}
_NOM40 = {s: n for n, s, d_, k, nb in _B40}

_TXT = {
 "boulangerie": {
  "label": "boulangerie", "plur": "boulangeries",
  "s1": [
   ("Farine, sucre, beurre : ce qui attire les nuisibles", "Une boulangerie réunit tout ce que cherchent les souris : sacs de farine, bacs de sucre, graines, chaleur du fournil. Je contrôle les plinthes, les passages de câbles, le dessous des plans de travail et la réserve, là où les rongeurs nichent le plus souvent."),
   ("Fournil et réserve de matières premières", "Dans le laboratoire comme dans la réserve, les sacs posés au sol, les palettes contre les murs et les angles peu accessibles sont les premiers points de passage des souris. Je repère les accès et je vous indique ce qu'il faut déplacer ou fermer."),
   ("Un commerce alimentaire très exposé", "Les produits secs, la chaleur et les livraisons tôt le matin font de la boulangerie un commerce que les rongeurs repèrent vite. Mon diagnostic porte sur le laboratoire, la réserve, le local poubelles et la cour."),
   ("Stocks, laboratoire et arrière-boutique", "Les souris cherchent la farine, les graines et la chaleur. Je vérifie les zones de stockage, les gaines techniques, les trappes et les arrivées de canalisations, puis je pose des points de contrôle adaptés aux locaux alimentaires."),
  ],
  "s2": [
   ("Livraisons tôt le matin et portes ouvertes", "Les livraisons de farine et de matières premières se font souvent tôt, porte arrière ouverte. Ce va-et-vient est une voie d'entrée directe pour les rongeurs ; je vous aide à repérer les ouvertures et les moments où votre local est le plus exposé."),
   ("Les abords du commerce", "Cour, local poubelles, bacs à déchets et conduits d'évacuation : les rongeurs passent par les abords avant d'entrer. Je pose les points de contrôle à l'extérieur et je vérifie leur fréquentation à chaque visite."),
   ("Mites alimentaires et insectes des stocks", "Dans les stocks de farine et de fruits secs, les mites alimentaires et d'autres insectes prospèrent. Je les traite lors du même passage que la dératisation, avec des produits adaptés aux locaux alimentaires."),
   ("Vieux murs, caves et arrière-cours", "Les bâtiments anciens et les caves offrent aux souris de nombreux passages. Je vous indique les ouvertures à fermer et j'adapte les emplacements aux contraintes du bâtiment."),
  ],
  "s3": [
   ("Un contrat calé sur vos horaires", "Je passe en dehors des heures de production, souvent avant l'ouverture, avec des produits adaptés aux locaux alimentaires. Un compte rendu écrit est remis après chaque visite."),
   ("Un suivi écrit pour vos contrôles", "Chaque passage donne lieu à un compte rendu daté, que vous pouvez conserver pour vos contrôles d'hygiène. La fréquence des visites est définie avec vous."),
   ("Des passages réguliers, sans arrêt de production", "En général, vous n'avez pas à arrêter la production : je m'adapte à votre planning et je vous indique si une zone doit rester libre quelques heures."),
   ("Diagnostic puis fréquence adaptée", "Je commence par un diagnostic gratuit, puis nous fixons ensemble la fréquence des passages selon la taille du commerce et son environnement."),
  ],
  "faq": [("Faut-il arrêter la production pendant l'intervention ?", "En général non : je m'adapte à votre planning, souvent avant l'ouverture, et je vous indique si une zone doit rester libre quelques heures."),
          ("Le diagnostic est-il gratuit ?", "Oui. Je me déplace, je contrôle les locaux et les abords, puis je vous remets un devis gratuit."),
          ("Recevrai-je un justificatif après chaque passage ?", "Oui, un compte rendu écrit et daté après chaque visite, que vous pouvez conserver pour vos contrôles.")],
 },
 "boucherie": {
  "label": "boucherie-charcuterie", "plur": "boucheries",
  "s1": [
   ("Viande, charcuterie et chambres froides", "Chambres froides, laboratoire de découpe, réserve et arrière-boutique : ces locaux attirent surtout les rats et les souris, qui cherchent chaleur, déchets et nourriture. Je contrôle les passages de canalisations, les gaines, les plinthes et les angles peu accessibles."),
   ("Laboratoire de découpe et local déchets", "Les déchets de découpe, les emballages et les bacs à déchets sont une source de nourriture pour les rats. Je vérifie le local poubelles, la cour et les évacuations, puis je pose des points de contrôle adaptés aux locaux alimentaires."),
   ("Un commerce alimentaire très surveillé", "Dans une boucherie-charcuterie, la propreté est un enjeu constant et la présence d'un rongeur ne doit pas passer inaperçue. Mon diagnostic porte sur le laboratoire, les chambres froides, les réserves et les abords."),
   ("Rats et souris près des locaux froids", "Les compresseurs, les gaines et les arrivées d'eau créent des passages que les rongeurs utilisent facilement. Je repère ces accès et je vous indique ce qu'il faut fermer."),
  ],
  "s2": [
   ("Livraisons et abords du commerce", "Les livraisons de viande et de produits frais passent souvent par une cour ou une porte arrière. Ces abords sont un point d'entrée possible pour les rongeurs ; je pose les points de contrôle à l'extérieur et je les vérifie à chaque visite."),
   ("Locaux annexes et traiteur", "Si votre commerce comprend un atelier traiteur ou des zones de préparation, ces locaux sont aussi contrôlés lors de la même visite."),
   ("Bâtiments anciens, caves et réserves", "Les murs épais, les caves et les arrière-cours offrent des passages aux rongeurs. J'adapte les emplacements aux contraintes du bâtiment et je vous indique les ouvertures à fermer."),
   ("Insectes et autres nuisibles", "Mouches, blattes et autres insectes peuvent aussi se développer près des déchets et des zones humides. Je les traite lors du même passage, avec des produits adaptés aux locaux alimentaires."),
  ],
  "s3": [
   ("Un suivi écrit pour vos contrôles", "Chaque passage donne lieu à un compte rendu daté, que vous pouvez conserver pour vos contrôles d'hygiène. La fréquence des visites est définie avec vous."),
   ("Un contrat calé sur vos horaires", "Je passe en dehors des heures de vente, avec des produits adaptés aux locaux alimentaires, et je vous remets un compte rendu écrit après chaque visite."),
   ("Diagnostic puis fréquence adaptée", "Je commence par un diagnostic gratuit, puis nous fixons ensemble la fréquence des passages selon la taille du commerce et son environnement."),
   ("Des passages réguliers, sans gêner la vente", "Je m'adapte à votre planning pour ne pas gêner la clientèle, et je vous indique si une zone doit rester libre quelques heures."),
  ],
  "faq": [("Intervenez-vous dans les chambres froides ?", "Je contrôle leurs abords, leurs gaines et leurs accès. Les produits sont choisis pour les locaux alimentaires et placés à l'abri des denrées."),
          ("Le diagnostic est-il gratuit ?", "Oui. Je me déplace, je contrôle les locaux et les abords, puis je vous remets un devis gratuit."),
          ("Recevrai-je un justificatif après chaque passage ?", "Oui, un compte rendu écrit et daté après chaque visite, que vous pouvez conserver pour vos contrôles.")],
 },
}

def _h(slug, k):
    return (sum(ord(c) * (i + 1) for i, c in enumerate(slug)) + k * 7) % 4

def _t40(metier, nom):
    for t in ("Contrat Dératisation %s %s | Proxinuisibles" % (metier.capitalize(), nom), "Dératisation %s %s | Proxinuisibles" % (metier.capitalize(), nom),
              "Dératisation %s %s" % (metier.capitalize(), nom), "Dératisation %s" % nom):
        if len(t) <= 60:
            return t

_by40 = {}
for nom, slug, dep, km, nb in _B40:
    for m in ("boulangerie", "boucherie"):
        if any(p.startswith("/contrat-deratisation-%s" % m) and p.endswith("-%s/" % slug) for p in P):
            continue
        _by40[(m, slug)] = "/contrat-deratisation-%s-%s/" % (m, slug)

def _existing(m, slug):
    for p in P:
        if p.startswith("/contrat-deratisation-%s" % m) and p.endswith("-%s/" % slug):
            return p
    return None

for nom, slug, dep, km, nb in _B40:
    for m in ("boulangerie", "boucherie"):
        if (m, slug) not in _by40:
            continue
        TX = _TXT[m]; lab = TX["label"]; path = _by40[(m, slug)]
        kms = str(km).replace(".", ",")
        lieu = "à Port-Brillet, où je suis installé" if km < 0.5 else "à %s km de Port-Brillet, où je suis installé" % kms
        lead = "Vous tenez une %s à %s (%s) ? Je suis installé à Port-Brillet, %s. Je vous propose un contrat de dératisation avec diagnostic gratuit, passages réguliers et compte rendu écrit après chaque visite." % (lab, nom, _DEP[dep], "à %s km de chez vous" % kms if km >= 0.5 else "dans votre commune")
        secs = [TX["s1"][_h(slug, 1)], TX["s2"][_h(slug, 2)], TX["s3"][_h(slug, 3)],
                ("Intervention à %s" % nom, "%s se trouve %s. Je me déplace chez les commerçants de la commune pour un diagnostic gratuit, puis je vous remets un devis. Pour une urgence, appelez-moi directement." % (nom, lieu))]
        faq = [TX["faq"][_h(slug, 4) % 3], ("Intervenez-vous à %s ?" % nom, "Oui. %s est dans mon secteur d'intervention, en %s." % (nom, _DEP[dep]))]
        other = "boucherie" if m == "boulangerie" else "boulangerie"
        autres = []
        o = _by40.get((other, slug)) or _existing(other, slug)
        if o:
            autres.append(("Contrat de dératisation %s à %s" % (_TXT[other]["label"], nom), o))
        if "/deratisation-%s/" % slug in P:
            autres.append(("Dératisation à %s" % nom, "/deratisation-%s/" % slug))
        vois = []
        for w in nb:
            u = _by40.get((m, w)) or _existing(m, w)
            if u:
                vois.append(("%s à %s" % (TX["label"].capitalize(), _NOM40[w]), u))
        links = []
        if autres:
            links.append(("Autres pages pour %s" % nom, autres))
        if vois:
            links.append(("Communes proches", vois))
        links.append(("Voir aussi", [("Tous les contrats métiers de bouche", "/contrats-metiers-de-bouche/"), ("Contrat annuel professionnels", "/contrat-annuel-deratisation/"), ("Professionnels", "/professionnels/"), ("Devis gratuit", "/contact/")]))
        add(path, h1="Contrat de dératisation %s à %s (%s)" % (lab, nom, dep), title=_t40(lab if len(lab) < 12 else m, nom),
            meta="Contrat de dératisation pour %s à %s (%s) : diagnostic gratuit, passages réguliers, compte rendu écrit. Devis gratuit." % (TX["plur"], nom, dep),
            lead=lead, secs=secs, faq=faq, links=links, kind="metier")
        MEDIA_EXTRA[path] = MEDIA_EXTRA.get("/contrats-metiers-de-bouche/")

# page d'ensemble : listes par métier
for m in ("boulangerie", "boucherie"):
    P["/contrats-metiers-de-bouche/"]["links"].append(("%s : communes à moins de 40 km" % _TXT[m]["plur"].capitalize(),
        [(_NOM40[s], u) for (mm, s), u in _by40.items() if mm == m]))
