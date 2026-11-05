# -*- coding: utf-8 -*-
# Mentions réglementaires et méthodes (demandées par Gwendal) : produits homologués / loi EGalim, méthodes de dératisation, HACCP.
_PREF = ("/deratisation", "/contrat-deratisation", "/contrat-annuel-deratisation", "/contrats-metiers-de-bouche", "/desinsectisation", "/blattes-cafards", "/fourmis")
_MET = ("restaurant", "boulangerie", "boucherie", "traiteur", "cuisine-collective")

def _est_bouche(p):
    return p.startswith("/contrat-deratisation-") or p.startswith("/contrats-metiers-de-bouche") or any(p == "/deratisation-%s-laval/" % m for m in _MET)

def _est_derat(p):
    return not p.startswith(("/desinsectisation", "/blattes-cafards", "/fourmis"))

_S_EGALIM = ("Des produits homologués, dans le respect de la loi EGalim",
             "J'utilise des produits homologués, dans le respect de la loi EGalim. Je suis titulaire du Certibiocide n° 059860, obligatoire pour utiliser des produits professionnels. Chaque produit est choisi selon le nuisible, le lieu et les personnes ou animaux présents, puis posé de façon sécurisée.")
_S_METH = ("Trois méthodes de dératisation, combinées selon la situation",
           "Je n'utilise pas une seule méthode : je choisis, ou je combine, selon le lieu et l'ampleur de l'infestation.\n- La méthode chimique : produits homologués, placés dans des boîtiers sécurisés et repérés.\n- La méthode mécanique : pièges posés sur les passages des rongeurs, utiles quand on veut limiter le recours aux produits.\n- La multicapture : pièges à captures multiples, adaptés aux souris et aux zones sensibles.\nLe diagnostic me permet de dire laquelle convient le mieux à votre situation.")
_S_HACCP = ("Je respecte les normes HACCP et la loi EGalim",
            "Mon intervention s'inscrit dans votre démarche HACCP : points de contrôle repérés et numérotés, produits placés à distance des denrées, passages planifiés et compte rendu écrit après chaque visite à conserver pour vos contrôles. Je respecte les normes HACCP et la loi EGalim, ainsi que l'utilisation de produits homologués.")

def _badges(items):
    return "<section class='sec'><div class='wrap'><ul class='badges'>%s</ul></div></section>" % "".join("<li>%s</li>" % b for b in items)

for _p, _d in P.items():
    if not _p.startswith(_PREF):
        continue
    der, bou = _est_derat(_p), _est_bouche(_p)
    badges = ["✓ Produits homologués, loi EGalim"]
    ajout = []
    if der:
        badges.append("✓ Méthodes chimique, mécanique et multicapture")
        ajout.append(_S_METH)
    if bou:
        badges.insert(0, "✓ Normes HACCP et loi EGalim")
        badges.pop(1)
        ajout.append(_S_HACCP)
    else:
        ajout.append(_S_EGALIM)
    _d["pre"] = _badges(badges) + _d.get("pre", "")
    _d["secs"] = list(_d["secs"]) + ajout

# --- Proofing (protection des bâtiments contre le retour des rongeurs), tournures variées selon le public ---
import zlib
_PROOF_TITRES = {
 "part": ["Le proofing : empêcher les rongeurs de revenir chez vous", "Après la dératisation, le proofing protège votre maison", "Proofing : boucher les accès pour ne plus revoir de rats ni de souris"],
 "pro": ["Le proofing : rendre vos locaux imperméables aux rongeurs", "Proofing : fermer les accès plutôt que seulement traiter", "Le proofing, complément du contrat de dératisation"],
 "syn": ["Le proofing : protéger durablement vos immeubles", "Proofing des parties communes : couper les accès aux rongeurs", "Le proofing, pour que le problème ne revienne pas dans la copropriété"],
}
_PROOF_TEXTES = {
 "part": [
  "Traiter ne suffit pas toujours : si les rongeurs peuvent rentrer, ils reviendront. Le proofing consiste à repérer puis à boucher leurs points d'entrée : passages de canalisations, trous dans un mur ou sous une porte, aérations non protégées, interstices sous la toiture. Une souris passe dans un trou de la taille d'un stylo, d'où l'intérêt d'un contrôle minutieux de la maison, du garage et des dépendances.",
  "Mon travail ne s'arrête pas à la pose de produits ou de pièges. Je fais aussi du proofing : je cherche par où les rongeurs entrent chez vous, puis je conseille ou je réalise les fermetures nécessaires (grille, laine d'acier, mortier, bavette sous porte). Moins il y a d'accès, moins il y a de risque de nouvelle infestation.",
  "Le proofing, c'est la prévention qui complète la dératisation. Je fais le tour de votre logement et de ses abords, je note chaque ouverture exploitable par les rats et les souris et je vous indique comment la condamner. Le résultat se voit dans la durée : un traitement plus court et moins de passages à prévoir.",
 ],
 "pro": [
  "Un traitement sans proofing laisse la porte ouverte. Je repère et je fais fermer les accès utilisés par les rongeurs : jonctions de murs, gaines techniques, bas de portes, trappes, évacuations. Pour un local professionnel, c'est la meilleure façon de réduire le nombre de passages et de sécuriser votre activité dans la durée.",
  "En complément des méthodes chimique, mécanique et multicapture, je propose le proofing : un diagnostic des points d'entrée du bâtiment, la liste des travaux d'étanchéité à prévoir et leur suivi dans mon compte rendu écrit. Vous gardez la preuve de ce qui a été fait, utile en cas de contrôle.",
  "Le proofing consiste à rendre votre établissement le moins accessible possible aux rongeurs. Je vérifie les ouvertures, les réseaux, les zones de stockage et les abords, puis je vous remets des préconisations claires. Avec un contrat de passages réguliers, c'est la combinaison qui protège le mieux vos locaux.",
 ],
 "syn": [
  "Dans un immeuble, les rongeurs circulent par les caves, les gaines, les locaux poubelles et les réseaux. Le proofing vise à fermer ces accès : je les repère lors de la visite, je les liste par bâtiment et je transmets des préconisations que le syndic peut faire exécuter. C'est ce qui évite de retraiter les mêmes lieux chaque année.",
  "Pour les copropriétés, les bailleurs et les collectivités, je fais du proofing en plus du traitement : repérage des points d'entrée, conseils d'étanchéité, priorités de travaux. Le compte rendu écrit sert de base pour décider des interventions, y compris en assemblée générale.",
  "Traiter les rongeurs sans condamner leurs passages revient à vider une baignoire sans fermer le robinet. Le proofing complète la dératisation de vos résidences et bâtiments : je signale les ouvertures à reboucher et je suis leur évolution lors des passages suivants.",
 ],
}

def _pub(p):
    if p in ("/particuliers/",) or (p.startswith("/deratisation-") and not any(("-%s-laval/" % m) in p for m in _MET)):
        return "part"
    if p in ("/agences-syndics/",):
        return "syn"
    if p in ("/professionnels/",) or _est_bouche(p) or p.startswith("/contrat-annuel-deratisation") or p.startswith("/contrats-metiers-de-bouche"):
        return "pro"
    if p == "/deratisation/":
        return "part"
    return None

for _p, _d in P.items():
    if _p.startswith(("/desinsectisation", "/blattes-cafards", "/fourmis")) or not (_p.startswith(("/deratisation", "/contrat-deratisation", "/contrat-annuel-deratisation", "/contrats-metiers-de-bouche")) or _p in ("/particuliers/", "/professionnels/", "/agences-syndics/")):
        continue
    _k = _pub(_p)
    if not _k:
        continue
    _i = zlib.crc32(_p.encode()) % 3
    _d["secs"] = list(_d["secs"]) + [(_PROOF_TITRES[_k][_i], _PROOF_TEXTES[_k][(_i + 1) % 3])]
    if _p.startswith(_PREF):
        _d["pre"] = _d["pre"].replace("</ul>", "<li>✓ Proofing : protection contre le retour des rongeurs</li></ul>", 1)

# Page /deratisation/ : la section sur les méthodes remonte en première position
_d = P["/deratisation/"]
_s = list(_d["secs"])
_m = [x for x in _s if x[0] == _S_METH[0]]
if _m:
    _s.remove(_m[0]); _d["secs"] = [_m[0]] + _s

# --- Frise : contrats de 1 à 12 passages par an ---
_FR = [("1", "1 passage", "Par an", "Contrôle annuel : un site peu exposé, avec un diagnostic complet et un compte rendu écrit."),
       ("2", "2 passages", "Semestriel", "Un passage à chaque saison clé, pour suivre un site à risque modéré."),
       ("4", "4 passages", "Trimestriel", "Le rythme courant pour un commerce, un restaurant ou un immeuble."),
       ("6", "6 passages", "Tous les 2 mois", "Pour les métiers de bouche et les sites où les rongeurs reviennent vite."),
       ("12", "12 passages", "Mensuel", "Sites très sensibles ou à forte pression : cuisine collective, agroalimentaire, bâtiments étendus.")]

def _frise_html():
    li = "".join("<li><span class='n'>%s</span><strong>%s</strong><em>%s</em><span class='t'>%s</span></li>" % x for x in _FR)
    return ("<section class='sec'><div class='wrap'><h2>Un contrat de 1 à 12 passages par an</h2>"
            "<p>Le nombre de passages se décide avec vous, selon le site et vos besoins. Voici les rythmes les plus courants :</p>"
            "<ol class='frise'>%s</ol>"
            "<p style='margin-top:28px'>Chaque passage donne lieu à un compte rendu écrit. Le rythme peut être ajusté en cours d'année selon les constats.</p></div></section>") % li

for _p, _d in P.items():
    if _p.startswith(("/contrat-deratisation", "/contrat-annuel-deratisation", "/contrats-metiers-de-bouche")):
        _d["pre"] = _d.get("pre", "") + _frise_html()

# --- Chenilles processionnaires : pièges sur les troncs et coupe des cocons ---
_c = P["/chenilles-processionnaires/"]
_c["secs"] = list(_c["secs"]) + [
 ("Pose de pièges sur les troncs",
  "Je pose des pièges autour du tronc des arbres concernés, notamment les pins. Au printemps, les chenilles descendent en file le long du tronc pour s'enfouir dans le sol : le piège les intercepte et les recueille dans un sac, sans qu'elles atteignent le sol, votre pelouse ou vos animaux. Je règle la pose pour que le dispositif soit bien étanche autour de l'écorce, puis je repasse le retirer une fois la période de descente terminée."),
 ("Coupe des cocons et des nids",
  "Quand les nids soyeux sont visibles dans la cime, je procède à leur coupe, appelée échenillage. Je porte une protection complète contre les poils urticants, je coupe le cocon avec la branche qui le porte, puis je le place dans un sac fermé pour l'évacuer et le détruire. Cette opération se fait en hiver, avant que les chenilles ne quittent leur nid. Ne montez pas sur une échelle pour le faire vous-même : les poils urticants se dispersent au moindre geste."),
 ("Chênes : retrait des cocons à l'aspirateur, sans insecticide",
  "Sur les chênes, j'interviens aussi sur les cocons de processionnaires. Je les retire avec un aspirateur, sans aucun insecticide. Cette méthode évite de répandre des produits dans le jardin, autour des enfants, des animaux ou près d'une aire de jeux. Je porte une protection complète contre les poils urticants et je récupère les cocons et les chenilles pour les détruire, au lieu de les laisser tomber au sol."),
 ("Quelle méthode selon votre arbre ?",
  "Pour un pin, je combine la coupe des nids et le piège sur le tronc. Pour un chêne, je retire les cocons à l'aspirateur. Lors de la visite, je regarde vos arbres, leur hauteur et leur accessibilité, puis je vous propose la solution adaptée dans un devis gratuit."),
]
_c["faq"] = list(_c["faq"]) + [
 ("À quoi sert un piège sur le tronc ?", "Il intercepte les chenilles processionnaires lorsqu'elles descendent en procession le long du tronc au printemps. Elles sont recueillies dans un sac et ne se dispersent pas dans le jardin."),
 ("Traitez-vous les chênes sans insecticide ?", "Oui. Je retire les cocons de processionnaires du chêne avec un aspirateur, sans insecticide, en portant une protection contre les poils urticants."),
 ("Faut-il couper les cocons ?", "Quand ils sont accessibles, la coupe des cocons en hiver supprime les chenilles avant leur sortie du nid. Elle doit être faite par un professionnel équipé, car les poils urticants sont dangereux."),
]

# --- Punaises de lit : traitement thermique ---
_u = P["/punaises-de-lit/"]
_u["secs"] = list(_u["secs"]) + [
 ("Une intervention thermique",
  "J'interviens de manière thermique : la chaleur élimine les punaises de lit à tous les stades, y compris les œufs, là où elles se cachent (matelas, sommier, plinthes, meubles). C'est une méthode qui s'applique directement dans le logement, qui ne laisse pas d'odeur de produit et qui permet de reprendre rapidement l'usage de la pièce. Je règle le traitement selon la taille et l'état du logement, et je contrôle le résultat après mon passage."),
 ("Ce que change le traitement thermique pour vous",
  "Pour une famille, une chambre d'hôtes, un gîte ou un logement loué, la chaleur est une méthode pratique : elle atteint les cachettes que l'on ne voit pas et permet de limiter le recours aux produits. Avant l'intervention, je vous indique ce qu'il faut ranger ou retirer des pièces concernées, puis je vous explique la suite lors du devis gratuit."),
]
_u["faq"] = list(_u["faq"]) + [
 ("Comment traitez-vous les punaises de lit ?", "J'interviens de manière thermique : la chaleur atteint les punaises et leurs œufs dans les cachettes (matelas, sommier, plinthes, meubles). Je vous précise la préparation avant le passage."),
]

# Punaises de lit : les sections sur le thermique remontent en tête de page
_s = list(_u["secs"])
_t = [x for x in _s if x[0] in ("Une intervention thermique", "Ce que change le traitement thermique pour vous")]
for _x in _t: _s.remove(_x)
_u["secs"] = _t + _s

# --- Page Devis et contact : formulaire ---
FORM_ENDPOINT = "https://formsubmit.co/ajax/" + MAIL
_FORM = """<section class='sec'><div class='wrap'><span class='label'>Formulaire</span><h2>Demandez votre devis gratuit</h2>
<p>Je vous réponds rapidement par téléphone ou par e-mail.</p>
<form class='cform' id='cform' method='post' action='%s' data-endpoint='%s' novalidate>
<label>Prénom<input type='text' name='Prénom' autocomplete='given-name' required></label>
<label>Nom<input type='text' name='Nom' autocomplete='family-name' required></label>
<label>E-mail<input type='email' name='E-mail' autocomplete='email' required></label>
<label>Téléphone<input type='tel' name='Téléphone' autocomplete='tel' required></label>
<label class='full'>Votre message<textarea name='Message' placeholder='Votre commune, le nuisible concerné, depuis quand, particulier ou professionnel…' required></textarea></label>
<input class='hp' type='text' name='_honey' tabindex='-1' autocomplete='off' aria-hidden='true'>
<input type='hidden' name='_subject' value='Demande de devis depuis le site Proxinuisibles'>
<input type='hidden' name='_template' value='table'>
<input type='hidden' name='_captcha' value='false'>
<p class='rgpd full'>Les informations saisies servent uniquement à répondre à votre demande. Elles ne sont ni revendues ni conservées sur ce site.</p>
<div class='full'><button class='btn' type='submit'>Envoyer ma demande</button></div>
<div class='cform-msg' id='cform-msg' hidden role='status'></div>
</form></div></section>""" % (FORM_ENDPOINT, FORM_ENDPOINT)
P["/contact/"]["pre"] = P["/contact/"].get("pre", "") + _FORM

# --- Photos de Gwendal sur la page Qui suis-je ---
_GAL = ("<section class='sec'><div class='wrap'><span class='label'>Sur le terrain</span><h2>Mon métier au quotidien</h2>"
        "<div class='gal'>"
        "<figure><img src='/media/gwendal-intervention.webp' alt=\"Gwendal, de Proxinuisibles, inspecte le bas d'un mur à la lampe torche lors d'un diagnostic\" width='1100' height='1466' loading='lazy'>"
        "<figcaption>Un diagnostic commence toujours par l'observation : je cherche les passages, les indices et les points d'entrée.</figcaption></figure>"
        "<figure><img src='/media/gwendal-salon.webp' alt=\"Le stand Proxinuisibles sur un salon, avec un nid de frelons, une combinaison de protection et des pièges\" width='1100' height='1466' loading='lazy'>"
        "<figcaption>Sur les salons et les marchés, je montre le matériel, les nids et les pièges, et je réponds aux questions.</figcaption></figure>"
        "</div></div></section>")
P["/qui-suis-je/"]["secs"] = list(P["/qui-suis-je/"]["secs"])
P["/qui-suis-je/"]["pre"] = P["/qui-suis-je/"].get("pre", "") + _GAL

# --- Encart badigeon sur la page Mouches ---
_BADIGEON = ("<section class='sec'><div class='wrap'><div class='band'>"
 "<span class='label'>Ma solution phare</span><h2>Le badigeon : une seule application pour toute la saison</h2>"

 "<p>C'est le traitement que je recommande en premier chez les particuliers, et c'est celui qui change vraiment la vie. "
 "Au lieu de pulvériser toutes les semaines, de suspendre des rubans collants et de racheter des bombes tout l'été, "
 "j'applique un badigeon une seule fois, à l'intérieur, sur les surfaces où les mouches viennent se poser. "
 "Elles s'y contaminent d'elles-mêmes, et le traitement reste actif de mai à décembre.</p>"
 "<p>Ce que cela change chez vous : plus de mouches dans la cuisine, la véranda ou la buanderie pendant toute la belle saison, "
 "sans odeur de bombe insecticide à chaque repas. Vous et vos animaux restez sur place : il n'y a ni évacuation du logement, "
 "ni vaisselle à ranger, ni bâche à poser. Le badigeon s'applique au pinceau, en bandes discrètes, en hauteur et sur les zones de repos des mouches, "
 "à l'écart des plans de travail, des aliments et des gamelles.</p>"
 "<p>Cela fonctionne aussi très bien dans une dépendance, un garage, un abri de jardin, un chenil ou un bâtiment d'élevage. "
 "Le mieux est d'intervenir au printemps, avant que la population ne monte : une visite suffit pour être tranquille jusqu'aux premiers froids.</p>"
 "<a class='btn' href='/contact/'>Demander un devis pour le badigeon \u2197</a>"
 "<p class='bio-avert'>Utilisez les biocides avec pr\u00e9caution. Lisez toujours l'\u00e9tiquette et les informations concernant le produit avant toute utilisation.</p>"
 "</div></div></section>")
P["/mouches/"]["pre"] = P["/mouches/"].get("pre", "") + _BADIGEON
