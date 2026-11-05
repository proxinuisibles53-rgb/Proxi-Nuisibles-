# Contrats de dératisation - métiers de bouche - 7 communes autour de Vitré et Laval
# Clés : (slug ville, métier). Chaque page a ses propres textes, appuyés sur des faits locaux vérifiés.

VILLES = {
 "vitre": ("Vitré", "du château à la place du Marchix", ["chateaubourg", "argentre-du-plessis"], "/deratisation-vitre/"),
 "chateaubourg": ("Châteaubourg", "entre Vilaine et place de l'Hôtel de Ville", ["vitre", "cesson-sevigne"], "/deratisation-chateaubourg/"),
 "argentre-du-plessis": ("Argentré-du-Plessis", "autour de la place Notre-Dame", ["vitre", "saint-berthevin"], None),
 "saint-berthevin": ("Saint-Berthevin", "du plan d'eau de Coupeau à la place de l'Europe", ["argentre-du-plessis", "change"], "/deratisation-saint-berthevin/"),
 "change": ("Changé", "sur les bords de la Mayenne", ["saint-berthevin", "louverne"], None),
 "louverne": ("Louverné", "autour de la place de l'Église", ["change", "saint-berthevin"], None),
 "cesson-sevigne": ("Cesson-Sévigné", "des bords de la Vilaine à Rennes Atalante", ["chateaubourg", "vitre"], "/deratisation-cesson-sevigne/"),
}
METIERS = {
 "restaurant": ("Restaurant", "restaurants"),
 "boulangerie": ("Boulangerie", "boulangeries"),
 "boucherie": ("Boucherie", "boucheries et charcuteries"),
}
CONTRAT_LISTE = "- Diagnostic initial des locaux et des abords\n- Passages réguliers de contrôle\n- Intervention supplémentaire dès qu'un signe apparaît\n- Compte rendu écrit après chaque passage"

C = {}

# ---------------- VITRÉ ----------------
C[("vitre", "restaurant")] = dict(
 lead="Entre les remparts, la rue Baudrairie et la place du Marchix, les restaurants de Vitré travaillent souvent dans des murs de plusieurs siècles. Mon contrat de dératisation est pensé pour ces bâtiments.",
 secs=[("Un centre ancien qui offre des passages aux rongeurs", "Au pied du château, les maisons de pierre et à pans de bois laissent des vides dans les murs, les planchers et les caves. Mon premier passage consiste à inspecter ces points faibles, de la salle jusqu'à la réserve et aux locaux poubelles de la cour."),
       ("Le lundi, jour de marché", "Le marché se tient le lundi près de l'église Notre-Dame : le centre est plus fréquenté et les abords des restaurants reçoivent plus de cartons et de déchets. Je cale mes contrôles sur ce rythme pour surveiller les ruelles et les cours voisines."),
       ("Ce que comprend le contrat", "- Diagnostic initial des lieux\n- Passages réguliers, à des horaires qui ne gênent pas le service\n- Intervention supplémentaire dès qu'un signe apparaît\n- Compte rendu écrit à joindre à votre plan de maîtrise sanitaire")],
 faq=[("Mon restaurant est dans un bâtiment ancien : est-ce un problème ?", "Non. Je pose du matériel discret sans abîmer le bâti et je vous indique les ouvertures à faire reboucher par un artisan."),
      ("Les cafards et les mouches sont-ils inclus ?", "Ils peuvent être ajoutés au contrat. Dites-le-moi lors du devis et je l'adapte.")])
C[("vitre", "boulangerie")] = dict(
 lead="Du fournil des rues commerçantes du centre à celui des quartiers périphériques de Vitré, la farine attire les souris. Mon contrat protège vos stocks sans perturber la fournée du matin.",
 secs=[("Où les souris s'installent dans un fournil", "Sacs de farine, réserve de sucre, placards sous les laboratoires : je les contrôle un par un. Dans les bâtiments anciens, au pied du château, je regarde aussi les jonctions entre murs, plafonds et conduits."),
       ("Des passages calés sur vos horaires", "Une boulangerie travaille quand la ville dort. Je passe en fin d'après-midi ou après la dernière cuisson, jamais en pleine production, et je pose les postes loin des surfaces de travail."),
       ("Un contrat simple, sans surprise", CONTRAT_LISTE)],
 faq=[("Faut-il vider le fournil pour votre passage ?", "Non. Je travaille autour de votre activité et je vous préviens des gestes simples à prévoir, comme protéger les sacs ouverts."),
      ("Mon laboratoire est au sous-sol, est-il traité ?", "Oui, caves et sous-sols font partie du diagnostic car l'humidité y attire les rongeurs.")])
C[("vitre", "boucherie")] = dict(
 lead="À Vitré, la boucherie-charcuterie de centre-ville ou de quartier doit tenir ses chambres froides, son laboratoire et ses déchets à l'abri des rongeurs et des mouches. Mon contrat s'adapte à ce métier.",
 secs=[("Chambres froides, laboratoire, cour", "Les rongeurs cherchent chaleur et nourriture : je contrôle les groupes froids, les passages de canalisations, la zone de découpe et le local à déchets d'origine animale, souvent installé dans une petite cour à l'arrière du commerce."),
       ("Les mouches aussi", "En saison chaude, les mouches deviennent le premier souci. Le contrat peut inclure leur suivi, avec des conseils simples sur la gestion des déchets et la fermeture des ouvertures."),
       ("Le suivi de votre dossier sanitaire", "Chaque passage donne lieu à un compte rendu écrit que vous conservez pour vos contrôles. Vous savez quand je suis venu, ce que j'ai vu et ce que j'ai fait.")],
 faq=[("Intervenez-vous pendant les heures de vente ?", "Je choisis des créneaux qui ne croisent pas votre clientèle, par exemple en début ou en fin de journée."),
      ("Mon commerce est dans une rue étroite du centre, est-ce gênant ?", "Non, j'arrive avec un petit matériel et je m'organise pour ne bloquer ni la rue ni vos livraisons.")])

# ---------------- CHÂTEAUBOURG ----------------
C[("chateaubourg", "restaurant")] = dict(
 lead="Labellisée Village étape, Châteaubourg accueille de nombreux voyageurs entre Rennes et Vitré. Ses restaurants doivent rester irréprochables, et le contrat de dératisation en fait partie.",
 secs=[("Une commune de passage", "Le flux de voyageurs, les zones d'activités qui entourent le bourg et les repas du midi des salariés font tourner les cuisines. Une présence de rongeurs se remarque vite et se paie en réputation."),
       ("L'eau, les moulins et les étangs", "La vallée de la Vilaine, les anciens moulins comme celui du parc Bel Air et le plan d'eau de la forêt de la Corbière attirent les rats vers les berges et les fossés. Les restaurants proches de l'eau ou des espaces verts font l'objet d'un contrôle renforcé des abords."),
       ("Votre contrat de dératisation", "- Diagnostic initial de la salle, de la cuisine, des réserves et de la cour\n- Passages réguliers\n- Intervention dès qu'un signe apparaît\n- Compte rendu écrit après chaque visite")],
 faq=[("Mon restaurant est près de la Vilaine, dois-je m'inquiéter ?", "Pas forcément, mais les berges sont un passage naturel pour les rats : je surveille les abords et les évacuations d'eau."),
      ("Pouvez-vous passer entre deux services ?", "Oui, nous fixons ensemble un créneau creux, par exemple en début d'après-midi.")])
C[("chateaubourg", "boulangerie")] = dict(
 lead="Entre l'église Saint-Pierre, la place de l'Hôtel de Ville et les lotissements qui entourent le bourg, les boulangeries de Châteaubourg travaillent pour une clientèle d'habitués. Je protège leurs stocks de farine des souris.",
 secs=[("Le fournil et les réserves", "Je contrôle les zones de stockage de farine et de céréales, les arrière-boutiques et les points d'entrée dans le bâtiment : portes de livraison, bouches d'aération, gaines techniques."),
       ("Un commerce de bourg, des détails qui comptent", "Dans un centre-bourg, les commerces se touchent souvent par les murs et les caves. Un rongeur qui passe d'un bâtiment à l'autre est un vrai sujet : je regarde donc aussi les mitoyennetés et les cours communes."),
       ("Fréquence et suivi", "La fréquence des passages dépend de votre taille et de votre environnement. Je la fixe avec vous après le diagnostic, puis je vous remets un compte rendu écrit à chaque visite.")],
 faq=[("Les produits sont-ils sans danger pour le pain ?", "Je place le matériel loin des surfaces de travail et des denrées, et je vous explique l'organisation avant de commencer."),
      ("Mon commerce vient d'ouvrir, un contrat est-il utile ?", "Oui : un diagnostic dès l'ouverture permet de repérer les points faibles avant que les problèmes n'arrivent.")])
C[("chateaubourg", "boucherie")] = dict(
 lead="Les boucheries, charcuteries et traiteurs de Châteaubourg servent aussi bien les habitants du bourg que les salariés des zones d'activités voisines. Un contrat de dératisation protège leur laboratoire et leurs chambres froides.",
 secs=[("Les zones sensibles", "Chambres froides, laboratoire de découpe, stockage des emballages, zone de livraison et local à déchets : ce sont les premiers endroits où je cherche des traces."),
       ("Des livraisons toute la semaine", "Les camions apportent des cartons et des palettes dans lesquels les souris se glissent. Je vous conseille sur le stockage et je surveille les quais."),
       ("Ce que vous recevez", "- Diagnostic initial\n- Passages réguliers\n- Intervention hors passage prévu en cas d'alerte\n- Compte rendu écrit à conserver dans votre dossier sanitaire")],
 faq=[("Mon traiteur prépare aussi pour les entreprises du coin : cela change-t-il quelque chose ?", "Cela renforce l'intérêt d'un suivi écrit, car vos clients peuvent vous le demander. Je vous remets un compte rendu à chaque passage."),
      ("Et si je vois une souris entre deux passages ?", "Appelez-moi : le contrat prévoit une intervention supplémentaire sur demande.")])

# ---------------- ARGENTRÉ-DU-PLESSIS ----------------
C[("argentre-du-plessis", "restaurant")] = dict(
 lead="Sur l'axe qui relie Vitré à Laval, Argentré-du-Plessis accueille des restaurants qui servent habitants, salariés de ses zones d'activités et voyageurs. Un contrat de dératisation sécurise leurs cuisines.",
 secs=[("Autour de la place Notre-Dame", "Autour de l'église, dans le bourg, les commerces partagent des cours et des murs mitoyens. Je regarde les passages entre bâtiments, les locaux poubelles et les évacuations d'eau."),
       ("Les zones d'activités et les repas du midi", "Les zones de la Frotière, des Branchettes et de la Blinière font venir des salariés à l'heure du déjeuner. Les coups de feu de midi laissent peu de temps pour le nettoyage : j'en tiens compte dans mes horaires de passage."),
       ("Votre contrat", "- Diagnostic initial de la réception au stockage, de la cuisine à la salle et à la cour\n- Passages réguliers\n- Intervention supplémentaire sur appel\n- Compte rendu écrit")],
 faq=[("Intervenez-vous hors du bourg, près des zones d'activités ?", "Oui, j'interviens sur tout le territoire d'Argentré-du-Plessis et dans les communes voisines."),
      ("Je suis ouvert uniquement le midi, comment faire ?", "Je passe en fin d'après-midi, quand la cuisine est fermée et nettoyée.")])
C[("argentre-du-plessis", "boulangerie")] = dict(
 lead="Place Notre-Dame, dans le bourg ou en périphérie, les boulangeries d'Argentré-du-Plessis ouvrent tôt et fournissent autant les familles que les entreprises. Je veille à ce que souris et rats restent loin de la farine.",
 secs=[("Un commerce de proximité, des attentes élevées", "Dans une commune de cette taille, tout le monde se connaît : un problème de nuisibles se sait vite. Mon contrat vous aide à garder une longueur d'avance, avec des passages réguliers et un compte rendu clair."),
       ("Entre bourg et campagne", "La commune s'étend sur plus de 40 km² de campagne, avec le château du Plessis et son étang. Les rongeurs circulent facilement entre champs, bâtiments agricoles et bourg, et un fournil proche des champs mérite une vigilance particulière."),
       ("Programme type d'un passage", "- Contrôle des zones de stockage de farine\n- Inspection des abords : cour, poubelles, gouttières\n- Vérification des postes déjà installés\n- Conseils et compte rendu écrit")],
 faq=[("Je suis en pleine campagne, à quelques kilomètres du bourg : faut-il un contrat ?", "C'est même souvent plus utile : les bâtiments isolés sont les premiers visités par les rongeurs venus des champs."),
      ("Passez-vous avant l'ouverture ?", "Nous choisissons ensemble un créneau, souvent en fin de journée après la dernière fournée.")])
C[("argentre-du-plessis", "boucherie")] = dict(
 lead="Les boucheries et charcuteries d'Argentré-du-Plessis travaillent des produits frais et sensibles. Le contrat de dératisation s'ajoute à vos règles d'hygiène pour protéger laboratoire, chambres froides et déchets.",
 secs=[("Ce que je surveille", "Laboratoire de découpe, chambre froide, stockage des emballages, zone de livraison et abords extérieurs. Les rongeurs cherchent d'abord le chaud, l'humidité et les restes."),
       ("Une campagne toute proche", "Autour d'Argentré-du-Plessis, les champs et les bâtiments agricoles ne sont jamais loin. Les rats venus des fossés et des exploitations s'approchent des commerces de bouche : je surveille les cours, les gouttières et les regards d'évacuation."),
       ("Votre dossier sanitaire", "Après chaque passage, vous recevez un compte rendu écrit à conserver pour vos contrôles. Vous gardez une trace claire de mes constats et de mes actions.")],
 faq=[("Mon commerce est dans un petit bourg : un contrat annuel est-il proportionné ?", "Oui, je dimensionne la fréquence des passages à votre activité : un petit commerce n'a pas besoin du rythme d'une grosse structure."),
      ("Les mouches sont-elles couvertes ?", "Je peux les ajouter au contrat, c'est souvent utile en saison chaude.")])

# ---------------- SAINT-BERTHEVIN ----------------
C[("saint-berthevin", "restaurant")] = dict(
 lead="À Saint-Berthevin, les restaurants se partagent entre le bourg, la zone d'activité du Grand Ouest et les abords du plan d'eau de Coupeau. Chaque cuisine a ses risques, et mon contrat s'adapte à chacune.",
 secs=[("Près du plan d'eau de Coupeau", "Le plan d'eau, ses promenades et le cours du Vicoin voisin attirent promeneurs, pêcheurs et campeurs, mais aussi des rongeurs le long des berges. Les restaurants proches de l'eau ou de l'espace de loisirs font l'objet d'un contrôle renforcé des abords."),
       ("La zone d'activité et ses repas d'entreprise", "À l'ouest de Laval, la zone d'activité du Grand Ouest regroupe des entreprises dont les salariés déjeunent sur place. Les restaurants qui les reçoivent ont des volumes importants et des livraisons fréquentes : je les inclus dans le plan de passage."),
       ("Le contenu du contrat", "- Diagnostic des locaux et des abords\n- Passages réguliers\n- Intervention supplémentaire sur demande\n- Compte rendu écrit après chaque passage")],
 faq=[("Mon restaurant est près du plan d'eau : est-ce plus risqué ?", "Les abords de l'eau et des espaces verts attirent plus facilement les rats : je contrôle donc ces zones à chaque passage."),
      ("Intervenez-vous dans les petits bars-restaurants du bourg ?", "Oui, j'adapte le contrat à la taille et à l'activité de l'établissement.")])
C[("saint-berthevin", "boulangerie")] = dict(
 lead="Place de l'Europe, dans le centre ou le long des axes qui mènent à Laval, les boulangeries de Saint-Berthevin servent une commune d'environ 7 400 habitants. Je les aide à garder fournil et réserves hors de portée des souris.",
 secs=[("Un quartier, un contexte", "Commune résidentielle voisine de Laval, Saint-Berthevin compte de nombreux lotissements avec jardins et composteurs. Souris et rats passent d'un jardin à l'autre et s'approchent des commerces : je contrôle cours, gouttières et local à poubelles."),
       ("Dans le fournil", "Réserves de farine, pétrin, bacs de stockage, chambre de pousse : chaque zone a son point faible. J'installe des postes discrets et je vous montre comment éviter l'accès aux sacs ouverts."),
       ("Un suivi sur toute l'année", CONTRAT_LISTE)],
 faq=[("Je suis dans un petit centre commercial : est-ce possible ?", "Oui, je m'adapte aux contraintes d'un centre commercial et je coordonne le passage avec le gestionnaire si besoin."),
      ("Combien de passages par an ?", "Je le fixe avec vous après le diagnostic : cela dépend de votre taille et de votre environnement.")])
C[("saint-berthevin", "boucherie")] = dict(
 lead="Les boucheries, charcuteries et traiteurs de Saint-Berthevin ont affaire à des volumes variables, de la vente au détail aux repas livrés. Mon contrat de dératisation sécurise leurs laboratoires et leurs chambres froides.",
 secs=[("Les locaux concernés", "Chambre froide, laboratoire, local de découpe, zone de lavage, quai de livraison, stockage des emballages. Les rongeurs pénètrent par de petites ouvertures : je les repère et je vous dis comment les fermer."),
       ("Mouches et insectes en saison chaude", "À partir du printemps, les mouches sont un vrai souci dans les commerces de bouche. Je peux ajouter leur suivi au contrat, avec des conseils d'hygiène simples."),
       ("Une trace écrite de chaque visite", "Vous recevez un compte rendu après chaque passage, utile en cas de contrôle ou de question d'un client. Je vous explique ce que j'ai observé et ce que j'ai fait.")],
 faq=[("Je travaille aussi sur les marchés : est-ce pris en compte ?", "Le contrat porte sur vos locaux de production et de stockage. Je peux aussi vous conseiller sur le matériel transporté."),
      ("Quand dois-je vous appeler entre deux passages ?", "Dès que vous voyez une souris, des crottes ou des emballages rongés : j'interviens sans attendre le prochain passage.")])

# ---------------- CHANGÉ ----------------
C[("change", "restaurant")] = dict(
 lead="Au bord de la Mayenne, entre le château devenu mairie et le chemin de halage, Changé a des restaurants qui profitent des promeneurs. Un contrat de dératisation les protège toute l'année.",
 secs=[("Le bourg, la rivière et le chemin de halage", "Le bourg de Changé s'étire sur la rive droite de la Mayenne. Les berges, les haies et le chemin de halage sont des passages naturels pour les rats : je contrôle les abords des restaurants proches de la rivière à chaque passage."),
       ("Du parc des Ondines à la zone de la Biochère", "Près du parc des Ondines, en centre-bourg ou à proximité de la zone d'activités de la Biochère, les restaurants n'ont pas les mêmes besoins. Je ne propose pas le même programme à un snack de zone et à un restaurant de bord de rivière."),
       ("Votre contrat", "- Diagnostic initial\n- Passages réguliers\n- Intervention supplémentaire sur appel\n- Compte rendu écrit")],
 faq=[("Les fortes pluies changent-elles quelque chose ?", "Après de fortes pluies, les rongeurs cherchent des abris plus secs, parfois dans les bâtiments. Appelez-moi si vous remarquez un changement."),
      ("Mon restaurant n'ouvre qu'en saison : que faire ?", "Je cale les passages sur votre calendrier d'ouverture et je contrôle les locaux avant la réouverture.")])
C[("change", "boulangerie")] = dict(
 lead="Avec ses quartiers de Rive droite et de Rive gauche, Changé compte des commerces de proximité, dont des boulangeries qui ouvrent tôt. Je les aide à garder la farine hors de portée des rongeurs.",
 secs=[("Près de l'eau, des besoins particuliers", "La proximité de la rivière favorise la présence de rats et de souris dans les jardins voisins. Dans le fournil, je protège les sacs de farine et les zones de stockage ; à l'extérieur, je surveille les haies et les cours."),
       ("Le bâti ancien du bourg", "Les maisons du bourg, souvent en pierre, laissent des passages aux souris le long des murs et des canalisations. Je vérifie les jonctions et je vous signale les ouvertures à faire reboucher."),
       ("Passages et compte rendu", CONTRAT_LISTE)],
 faq=[("Le matin est-il le bon moment pour passer ?", "Non : je passe en dehors de votre production, souvent en fin de journée."),
      ("Faut-il fermer le commerce ?", "Non, je travaille sans interrompre votre activité.")])
C[("change", "boucherie")] = dict(
 lead="Boucherie-charcuterie, traiteur ou rôtisserie à Changé : les commerces de bouche ont besoin d'un suivi régulier pour garder leurs locaux hors de portée des nuisibles. Je leur propose un contrat de dératisation sur mesure.",
 secs=[("Des locaux à surveiller de près", "Les chambres froides, le laboratoire de découpe, les plonges et les locaux à déchets sont les zones où je commence mes contrôles. Je vérifie aussi les canalisations et les évacuations."),
       ("Une commune au bord de la Mayenne", "Le voisinage de la rivière, de ses berges et du parc des Ondines attire des rongeurs dans le secteur. Je tiens compte de cet environnement en renforçant le contrôle des cours et des gouttières."),
       ("Documents et traçabilité", "Après chaque passage, je vous remets un compte rendu écrit à conserver dans votre dossier. Vous gardez un historique clair de ce qui a été vu et fait.")],
 faq=[("Mon commerce est dans la zone de la Biochère : intervenez-vous là-bas ?", "Oui, j'interviens à Changé et dans toute l'agglomération lavalloise."),
      ("Les rats et les souris demandent-ils le même traitement ?", "Non : j'adapte les postes et les emplacements selon l'animal et le lieu.")])

# ---------------- LOUVERNÉ ----------------
C[("louverne", "restaurant")] = dict(
 lead="Entre la place de l'Église, la vallée de la Mayenne et les anciens fours à chaux, Louverné a un patrimoine particulier et des restaurants qui doivent rester irréprochables. Un contrat de dératisation les y aide.",
 secs=[("Un patrimoine industriel et des carrières", "Les anciennes carrières et les fours à chaux de la commune laissent des cavités et des zones de friche. Les rongeurs y trouvent facilement abri, puis s'approchent des habitations et des commerces. Je tiens compte de cet environnement dans mon diagnostic."),
       ("Promeneurs et visiteurs", "Randonneurs du circuit des fours et des carrières à chaux, visiteurs du parc Echologia : les restaurants de Louverné accueillent aussi une clientèle de passage. Un suivi régulier évite qu'un problème ne se voie."),
       ("Votre contrat", "- Diagnostic initial\n- Passages réguliers\n- Intervention supplémentaire sur appel\n- Compte rendu écrit")],
 faq=[("Mon restaurant est isolé en campagne : est-ce plus risqué ?", "Les bâtiments isolés sont souvent visités par les rongeurs venus des champs : je renforce le contrôle des abords."),
      ("Pouvez-vous intervenir en soirée ?", "Oui, j'adapte les créneaux à vos horaires d'ouverture.")])
C[("louverne", "boulangerie")] = dict(
 lead="À Louverné, la boulangerie du bourg, autour de la place de l'Église, fournit toute une commune proche de Laval. Je protège son fournil des souris grâce à un contrat régulier.",
 secs=[("Dans un bourg proche de Laval", "Louverné se situe aux portes de l'agglomération lavalloise. Lotissements, jardins et anciennes carrières offrent des refuges aux rongeurs, qui se rapprochent ensuite des commerces : le contrôle des abords en fait partie."),
       ("Les zones sensibles d'une boulangerie", "Sacs de farine, ingrédients, équipements de cuisson, arrière-boutique, local à poubelles. J'installe des postes discrets et je vérifie ceux déjà en place."),
       ("Ce que vous recevez", "- Diagnostic initial\n- Passages réguliers\n- Conseils d'hygiène adaptés\n- Compte rendu écrit après chaque visite")],
 faq=[("Ma boulangerie est aussi mon domicile : cela change-t-il quelque chose ?", "Je vous indique les précautions à prendre pour la partie habitation, notamment si vous avez des enfants ou des animaux."),
      ("Quelle est la fréquence des passages ?", "Elle dépend de votre activité et de votre environnement. Je la fixe avec vous après le diagnostic.")])
C[("louverne", "boucherie")] = dict(
 lead="Pour une boucherie, un traiteur ou un producteur-vendeur de Louverné, le contrat de dératisation s'ajoute aux règles d'hygiène. Je protège vos locaux de production et de stockage.",
 secs=[("Commerces de bouche et campagne", "Autour de Louverné, la campagne est proche et les commerces de bouche côtoient parfois des exploitations. J'adapte mon intervention à chaque type de lieu, du petit atelier à la boutique."),
       ("Les cavités de la commune", "Anciennes carrières, fours à chaux : les rongeurs peuvent s'y installer, puis rejoindre les bâtiments voisins. Un contrôle régulier de vos abords est donc essentiel."),
       ("Votre dossier de suivi", "Vous recevez un compte rendu écrit après chaque passage, pour vos contrôles et pour vos clients.")],
 faq=[("Je vends à la ferme : intervenez-vous dans ce type de lieu ?", "Oui, j'interviens aussi bien en commerce qu'en bâtiment agricole."),
      ("Les produits sont-ils sans danger pour mes denrées ?", "Je place le matériel loin des denrées et je vous explique l'organisation avant de commencer.")])

# ---------------- CESSON-SÉVIGNÉ ----------------
C[("cesson-sevigne", "restaurant")] = dict(
 lead="Entre les bords de la Vilaine, le technopôle Rennes Atalante et ViaSilva, Cesson-Sévigné compte de nombreux restaurants d'entreprise et de bureau. Mon contrat de dératisation répond à leurs exigences.",
 secs=[("Une clientèle d'entreprises", "Les restaurants proches de Rennes Atalante, de ViaSilva ou des pôles d'entreprises servent beaucoup de couverts en peu de temps. Une présence de nuisibles y a un impact immédiat : je prévois des passages réguliers et un compte rendu écrit."),
       ("Le centre-ville et le marché", "Autour du Mail de Bourgchevreuil, de la place du marché et du centre commercial Beausoleil, les commerces se côtoient et les rongeurs circulent entre cours et locaux poubelles. Je les inclus dans le contrôle."),
       ("La Vilaine et les étangs", "La Vilaine, ses étangs et les nombreux parcs de la commune offrent aux rats des abris tout près des restaurants. Les établissements riverains font l'objet d'un contrôle renforcé des abords."),
       ("Votre contrat", CONTRAT_LISTE)],
 faq=[("Mon restaurant est dans un parc d'entreprises : intervenez-vous là-bas ?", "Oui, j'interviens sur tout le territoire de Cesson-Sévigné et dans les communes de l'est rennais."),
      ("Pouvez-vous fournir un document pour mon audit ?", "Je remets un compte rendu écrit à chaque passage, que vous pouvez joindre à vos documents.")])
C[("cesson-sevigne", "boulangerie")] = dict(
 lead="À Cesson-Sévigné, ville de près de 18 000 habitants aux portes de Rennes, les boulangeries servent des quartiers très différents : centre, Bellevue, La Boulais, zones de bureaux. Mon contrat s'adapte à chaque implantation.",
 secs=[("Des quartiers pavillonnaires, des parcs et des jardins", "Les quartiers pavillonnaires sont reliés par un réseau d'espaces verts et de cheminements, avec des bords de Vilaine très plantés. Les rongeurs profitent de ces continuités et se rapprochent des commerces : je contrôle donc cours, haies et gouttières."),
       ("Dans le fournil", "Farines, levures, ingrédients de pâtisserie et emballages : je contrôle les réserves, les zones de livraison et les évacuations, et je vous donne des conseils pratiques pour le rangement."),
       ("Passages et traçabilité", CONTRAT_LISTE)],
 faq=[("Ma boulangerie est dans un centre commercial : comment faire ?", "Je m'organise avec le gestionnaire du centre pour accéder aux zones techniques et aux locaux poubelles."),
      ("Mon établissement est de grande taille : est-ce un problème ?", "Non, j'adapte le contrat à la taille de l'établissement, du petit commerce au grand ensemble.")])
C[("cesson-sevigne", "boucherie")] = dict(
 lead="Les boucheries, charcuteries et traiteurs de Cesson-Sévigné fournissent une clientèle exigeante, entre habitants et salariés des pôles d'entreprises. Un contrat de dératisation sécurise leurs locaux.",
 secs=[("Une ville qui se transforme", "Avec des projets d'urbanisation comme ViaSilva, les rongeurs sont dérangés dans leurs refuges et peuvent gagner les commerces voisins. Je surveille les abords et les locaux techniques."),
       ("Chambres froides et laboratoires", "Je contrôle les groupes froids, les gaines, les zones de découpe et le local à déchets. Chaque point d'entrée est noté et fait l'objet de conseils précis."),
       ("Un suivi par écrit", "Vous gardez une trace de chaque visite : dates, constats, actions. C'est utile en cas de contrôle ou de question d'un client.")],
 faq=[("Mon commerce est proche de la gare ou du métro : cela change-t-il le programme ?", "Les zones de passage dense génèrent plus de déchets : je renforce le contrôle des poubelles et des abords."),
      ("Pouvez-vous intervenir sur plusieurs boutiques d'un même groupe ?", "Oui, je peux proposer une organisation commune avec un compte rendu par établissement.")])
