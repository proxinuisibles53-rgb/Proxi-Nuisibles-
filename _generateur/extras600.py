# -*- coding: utf-8 -*-
# Contenu complémentaire (conseils, signes, déroulement) pour porter les pages communes et contrats à ~600-800 mots.
import re as _re

_COM = [
 ("Reconnaître une présence de rongeurs", [
  "Les premiers signes sont rarement visibles : des bruits de grattement la nuit dans les cloisons, le plafond ou sous le plancher, des déjections en forme de grains de riz pour les souris, plus grosses pour les rats, et une odeur d'urine persistante. Des emballages rongés, des câbles abîmés ou des traces grasses le long des murs confirment un passage régulier. Si vous remarquez l'un de ces indices à {nom}, ne tardez pas : une petite colonie s'installe vite et se multiplie.",
  "À {nom}, les rongeurs se signalent souvent par de petits indices : sacs de graines percés, placards grignotés, trous au bas des portes, crottes près des plinthes ou derrière les appareils électroménagers. Les rats laissent aussi des traces de frottement sombres le long des murs, sur leurs trajets habituels. Plus l'on agit tôt, plus le traitement est simple et rapide.",
  "Un rongeur se repère rarement à vue : il sort la nuit et évite la lumière. Ce sont les traces qui le trahissent : déjections, nids de papier ou de tissu déchiqueté, câbles rongés, bruits dans les combles ou la cave. Si vous en voyez un en plein jour à {nom}, la colonie est probablement déjà importante."]),
 ("Comprendre par où ils entrent", [
  "Une souris passe par une ouverture d'à peine un centimètre, un rat par un trou d'environ deux centimètres. Passages de canalisations, bas de portes, aérations, joints de toiture, trappes de cave ou fissures de façade : le diagnostic consiste à repérer tous ces accès. Sans cette étape, le traitement ne règle rien durablement, car de nouveaux rongeurs reviennent par les mêmes passages.",
  "Le traitement ne se limite pas à poser des appâts. Je cherche d'abord les points d'entrée : gaines techniques, jonctions entre mur et toit, portes de garage qui ne ferment pas à ras du sol, arrivées d'eau. Je vous indique ensuite ce qu'il faut boucher et avec quels matériaux, car un rongeur ronge le plâtre, le bois et certains plastiques.",
  "Tant que les accès restent ouverts, de nouveaux rongeurs arrivent. C'est pourquoi je commence toujours par une inspection complète, de la cave aux combles et des abords au jardin. Chaque ouverture est notée, puis je vous propose un plan : fermeture des accès, pose des points de contrôle, suivi des résultats."]),
 ("Limiter ce qui les attire autour de chez vous", [
  "Les rongeurs viennent chercher à manger, à boire et un abri. Rangez les graines et la nourriture des animaux dans des boîtes fermées, évitez de laisser des fruits tombés au sol, fermez le composteur, ne stockez pas de bois ou de cartons contre les murs. Ces gestes simples réduisent nettement les risques à {nom}, qu'il s'agisse d'une maison, d'une ferme ou d'un commerce.",
  "Pour décourager les rongeurs, supprimez les sources de nourriture et d'eau : poubelles fermées, mangeoires nettoyées, compost couvert, fuites réparées. Dégagez les abords des murs et débroussaillez les haies proches de la maison, car les rongeurs aiment les passages couverts. Cela ne remplace pas un traitement, mais cela l'aide à tenir dans le temps.",
  "Une maison bien tenue attire moins les rongeurs. Gardez les denrées dans des contenants hermétiques, nettoyez les miettes, vidangez les poubelles régulièrement, évitez les tas de bois ou de gravats contre les murs. Dans les fermes, protégez les stocks de grains et d'aliments, et gardez les abords propres."]),
 ("Quand agir à {nom}", [
  "L'automne est la période où les rongeurs cherchent un abri chaud : les souris entrent dans les maisons, les rats gagnent les granges, les caves et les garages. Mais une infestation peut survenir toute l'année. Si vous constatez des signes, mieux vaut me contacter sans attendre : une intervention précoce est plus rapide et moins coûteuse.",
  "Avec l'arrivée du froid, les rongeurs cherchent un refuge. C'est souvent à ce moment qu'on les découvre à {nom}, dans un grenier, un garage ou une réserve. Au printemps, ils se reproduisent à nouveau. Il n'y a donc pas de bonne saison pour attendre : plus le traitement est lancé tôt, plus la colonie est petite.",
  "Une femelle peut avoir plusieurs portées par an, et les jeunes sont rapidement autonomes. Une colonie peut ainsi grossir en quelques semaines. C'est pour cela qu'une intervention rapide fait la différence, que ce soit chez un particulier, dans une exploitation ou dans un commerce de {nom}."]),
 ("Comment se déroule mon intervention", [
  "Je me déplace pour un diagnostic gratuit : inspection des bâtiments et des abords, repérage des accès et des zones de passage. Je vous explique ce que j'ai constaté, puis je vous remets un devis. Le traitement est ensuite réalisé avec des produits adaptés, posés dans des boîtiers sécurisés, puis je vérifie les résultats lors d'un second passage.",
  "Chaque intervention suit les mêmes étapes : diagnostic sur place, explication de ce que j'ai observé, devis gratuit, traitement, puis contrôle. Je vous remets des conseils écrits pour éviter le retour des nuisibles. Je suis certifié pour l'utilisation des produits professionnels (Certibiocide n° 059860).",
  "Après le diagnostic, je choisis la méthode la plus adaptée : piégeage mécanique, appâts en boîtiers sécurisés, ou combinaison des deux. Je pose les points de contrôle aux endroits les plus fréquentés, puis je reviens vérifier. Si l'infestation est ancienne, un second ou un troisième passage peut être nécessaire."]),
 ("Sécurité des enfants et des animaux", [
  "Les produits que j'utilise sont placés dans des boîtiers fermés, hors de portée des enfants et des animaux domestiques. Je vous indique où ils se trouvent et ce qu'il ne faut pas toucher. Si vous avez des chiens, des chats ou des animaux de ferme, dites-le-moi : j'adapte les méthodes et les emplacements.",
  "La sécurité passe avant tout. Les boîtiers sont verrouillés, fixés et placés là où seuls les rongeurs peuvent entrer. Si votre animal a accès à la zone, je privilégie le piégeage mécanique ou des emplacements protégés. Je reprends l'ensemble du matériel à la fin du traitement.",
  "Je ne laisse jamais d'appât à découvert. Le matériel est fermé, repéré et suivi lors de chaque passage. Pour les familles avec de jeunes enfants ou des animaux à {nom}, je vous explique les précautions à respecter pendant le traitement."]),
]

_MET = [
 ("Pourquoi la lutte contre les nuisibles est obligatoire", [
  "Un commerce alimentaire doit maîtriser les nuisibles : c'est une exigence du règlement européen sur l'hygiène des denrées alimentaires (CE n° 852/2004) et des contrôles sanitaires. Les services départementaux de protection des populations peuvent demander à voir vos procédures. Un contrat avec un professionnel certifié et des comptes rendus écrits vous aident à prouver que la maîtrise est organisée.",
  "La présence de rongeurs ou d'insectes dans un local alimentaire expose à un risque sanitaire, à une sanction lors d'un contrôle et à une atteinte à l'image du commerce. La réglementation européenne sur l'hygiène des denrées oblige à lutter contre les nuisibles. Un contrat régulier permet d'anticiper plutôt que de subir.",
  "Les rongeurs peuvent transmettre des maladies, comme la leptospirose ou la salmonellose, et contaminer les denrées par leurs déjections. C'est pourquoi la réglementation sur l'hygiène alimentaire impose de prévenir leur présence. Dans une {m}, la prévention se prépare avant le problème, pas après."]),
 ("Les signes à surveiller dans votre {m}", [
  "Déjections près des plinthes ou dans les réserves, emballages rongés, bruits de grattement la nuit, traces grasses le long des murs, odeur d'urine : ces signes demandent une réaction rapide. Dans une {m} de {nom}, un seul rongeur aperçu en journée indique souvent une colonie déjà installée à proximité.",
  "Surveillez les coins peu fréquentés : dessous des meubles, arrière des équipements, local poubelles, réserve, cave. Des produits secs grignotés, des sacs percés ou des déjections sont des signaux d'alerte. Notez la date et le lieu de chaque observation et transmettez-les moi : cela m'aide à placer les points de contrôle.",
  "Les nuisibles se repèrent à de petits indices : déjections, odeur, emballages ouverts, traces de passage. Mais aussi à des signaux moins évidents, comme des insectes dans les stocks ou des mouches qui reviennent malgré le nettoyage. Je contrôle ces points à chaque passage dans votre {m} à {nom}."]),
 ("Ce que comprend le contrat", [
  "Le contrat comprend un diagnostic initial de vos locaux et de leurs abords, la pose et le suivi de points de contrôle, des passages à fréquence définie avec vous, l'intervention en cas de constat et un compte rendu écrit après chaque visite. Le devis est gratuit et adapté à la taille de votre commerce.",
  "Concrètement : un état des lieux au départ, des boîtiers de contrôle placés aux endroits sensibles, des passages réguliers, des interventions supplémentaires si nécessaire et un compte rendu daté après chaque visite. Vous conservez ces documents pour vos contrôles d'hygiène.",
  "Je commence par visiter les lieux, du laboratoire ou de la cuisine jusqu'aux abords. Je pose ensuite les points de contrôle, puis je passe selon la fréquence prévue. Chaque visite donne lieu à un compte rendu écrit, avec mes constats et mes recommandations."]),
 ("À quelle fréquence prévoir les passages", [
  "La fréquence dépend de la taille du commerce, de son environnement et de son historique. Un passage mensuel est courant pour une {m} ; une fréquence plus espacée peut suffire si le site est très bien protégé. Nous fixons ensemble le rythme après le diagnostic, et il peut évoluer selon les constats.",
  "Il n'y a pas de rythme unique. Dans un bâtiment ancien ou près d'un cours d'eau, je recommande souvent des passages plus rapprochés. Dans un local récent et bien fermé, un suivi plus espacé peut suffire. Je vous propose un rythme après la première visite à {nom}.",
  "Après le diagnostic, je vous propose une fréquence adaptée à votre activité. Si les constats sont bons pendant plusieurs passages, nous pouvons espacer les visites ; s'ils se dégradent, nous les rapprochons. Le contrat reste ainsi proportionné à vos besoins."]),
 ("Les bons réflexes au quotidien", [
  "Fermez les portes de livraison dès que la marchandise est rentrée, stockez les denrées sur des étagères à distance du sol et des murs, fermez les bacs à déchets, nettoyez sous les équipements et videz le local poubelles régulièrement. Ces gestes simples réduisent fortement le risque dans une {m}.",
  "Les gestes du quotidien comptent autant que le traitement : denrées en contenants fermés, sol dégagé, déchets sortis chaque soir, joints de portes en bon état, grilles d'aération protégées. Je vous remets une liste de points à surveiller adaptée à votre local à {nom}.",
  "Pour aider le traitement, évitez les cartons au sol, nettoyez les miettes et les résidus, vérifiez que les portes ferment bien et signalez toute fissure. Un local bien entretenu limite l'attrait pour les nuisibles et facilite mon travail."]),
 ("Des produits adaptés aux locaux alimentaires", [
  "J'utilise des produits et des méthodes compatibles avec les locaux alimentaires, placés dans des boîtiers fermés et à distance des denrées. Quand c'est possible, je privilégie le piégeage mécanique. Chaque point de contrôle est repéré et suivi, afin de savoir précisément où passent les nuisibles.",
  "Dans un local qui manipule des denrées, la méthode compte autant que le produit. Je place le matériel hors de portée des denrées, dans des boîtiers fermés, et je note chaque point de contrôle. Je suis titulaire du Certibiocide n° 059860, obligatoire pour les produits professionnels.",
  "Les boîtiers sont verrouillés et numérotés, placés aux endroits de passage et jamais au contact des denrées. À chaque visite, je vérifie leur état et je note ce que j'ai observé. Vous avez ainsi une traçabilité claire de ce qui a été fait."]),
]

def _hh(s, k):
    return (sum(ord(c) * (i + 3) for i, c in enumerate(s)) * (k + 5) + k * 11) % 3

def _metier_nom(path):
    for k, v in (("cuisine-collective", "cuisine collective"), ("boulangerie", "boulangerie"), ("boucherie", "boucherie"), ("traiteur", "activité de traiteur"), ("restauration-entreprise", "restaurant d'entreprise"), ("restaurant", "restaurant")):
        if k in path:
            return v
    return "commerce alimentaire"

_cibles = {}
for _f in FICHES:
    _cibles["/deratisation-%s/" % _f[0]] = ("com", _f[1])
for _p, _d in P.items():
    if _p.startswith("/contrat-deratisation-") and _d.get("kind") == "metier":
        _m = _re.search(r" à (.+?) \(", _d["h1"])
        _cibles[_p] = ("met", _m.group(1) if _m else "votre commune")
for _s in ("restaurant", "boulangerie", "boucherie", "traiteur", "cuisine-collective"):
    _p = "/deratisation-%s-laval/" % _s
    if _p in P:
        _cibles[_p] = ("met", "Laval")
for _p, _d in P.items():
    if _d.get("kind") == "ville" and _p not in _cibles:
        _m = _re.search(r"à (.+?)(?: \(| :|,|$)", _d["h1"])
        _cibles[_p] = ("com", _m.group(1) if _m else "votre commune")
for _p, (_t, _nom) in _cibles.items():
    if _p not in P:
        continue
    _pool = _COM if _t == "com" else _MET
    _m = _metier_nom(_p)
    _extra = []
    for _i, (_h2, _vars) in enumerate(_pool):
        _txt = _vars[_hh(_p, _i)]
        _extra.append((_h2.format(nom=_nom, m=_m), _txt.format(nom=_nom, m=_m)))
    P[_p]["secs"] = list(P[_p]["secs"]) + _extra

_PLUS = [
 ("Un professionnel local, installé à Port-Brillet", "Je suis installé à Port-Brillet, en Mayenne, et je me déplace dans tout le secteur de Laval, Vitré et des communes voisines. Être basé près de chez vous permet des délais courts, des passages réguliers sans surcoût de déplacement important et une vraie connaissance du terrain : habitat, cours d'eau, bâtiments anciens, zones agricoles. Je réponds directement au téléphone, sans intermédiaire."),
 ("Ce que vous pouvez faire dès maintenant", "En attendant mon passage, rangez les denrées dans des contenants fermés, sortez les déchets, dégagez le sol autour des murs et notez ce que vous avez observé : date, lieu, traces. Prenez une photo si possible et envoyez-la moi. Ne posez pas de produit vous-même sans me prévenir : un mauvais emplacement peut disperser les rongeurs ou présenter un risque pour les animaux."),
]
_old = {"vitre", "saint-berthevin", "change", "louverne", "argentre-du-plessis", "chateaubourg", "cesson-sevigne"}
for _p in list(P):
    if _cibles.get(_p, ("",))[0] == "met" and (_p.endswith("-laval/") or any(_p.endswith("-%s/" % v) for v in _old)):
        P[_p]["secs"] = list(P[_p]["secs"]) + _PLUS
