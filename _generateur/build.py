import os, json, shutil, zipfile

BASE = "https://www.proxinuisibles.fr"
FICHE = "https://maps.app.goo.gl/BEtwDMWG5gN9sgXv7"
CERT_URL = "https://certibiocide.din.developpement-durable.gouv.fr/verifCertificat"
CERT_NUM = "059860"
TEL_D, TEL, MAIL = "06 64 57 66 55", "+33664576655", "proxinuisibles53@gmail.com"
OUT = "/home/claude/site"

import re
import unicodedata

def T(s):
    return re.sub(r"'(?![^<>]*>)", "\u2019", s)

P = {}
def add(path, **kw):
    P[path] = kw

# ---------- SERVICES ----------
SV = [
 ("deratisation", "Dératisation", "Dératisation en Mayenne et Ille-et-Vilaine : rats et souris",
  "Dératisation Mayenne et Ille-et-Vilaine | Proxinuisibles",
  "Dératisation de rats et souris en Mayenne et Ille-et-Vilaine : maisons, fermes, commerces. Diagnostic et devis gratuits.",
  "Des bruits dans les combles, des crottes dans un placard, des câbles rongés : je cherche d'où viennent les rongeurs, je les élimine et je ferme les accès pour qu'ils ne reviennent pas.",
  [("Comment se passe une dératisation", "Je commence par un diagnostic : repérage des passages, des traces et des points d'eau ou de nourriture. Je choisis ensuite le traitement adapté (postes sécurisés, pièges) et je repasse vérifier que l'infestation est terminée."),
   ("Rats ou souris : ce qui change", "Le rat creuse des galeries, ronge les canalisations et s'installe près des égouts, des berges et des bâtiments d'élevage. La souris se glisse par de très petits trous et s'installe dans les cuisines, les placards et les combles. Le traitement n'est pas le même."),
   ("Où j'interviens", "- Maisons et appartements\n- Fermes et bâtiments agricoles\n- Commerces, restaurants et entrepôts\n- Logements gérés par une agence ou un syndic")],
  [("Comment savoir si j'ai des rats ou des souris ?", "Bruits la nuit dans les murs ou le plafond, crottes, traces de gras le long des murs, câbles ou emballages rongés. Une photo de ce que vous voyez m'aide à identifier l'animal."),
   ("Les produits sont-ils dangereux pour mes animaux ?", "J'utilise du matériel sécurisé placé hors de portée, et je vous explique les précautions à prendre avant mon passage.")]),
 ("frelons-guepes", "Frelons et guêpes", "Destruction de nids de frelons et de guêpes en Mayenne et Ille-et-Vilaine",
  "Destruction Nid de Frelons et Guêpes | Proxinuisibles",
  "Destruction de nids de frelons asiatiques, frelons européens et guêpes en Mayenne et Ille-et-Vilaine. Intervention sécurisée, devis gratuit.",
  "Un nid de frelons ou de guêpes dans une haie, sous le toit, dans un mur ou sous une terrasse : n'y touchez pas, appelez-moi. J'interviens avec une tenue de protection et le matériel adapté, y compris en hauteur.",
  [("Frelon asiatique, frelon européen ou guêpes ?", "Le frelon asiatique construit de gros nids ronds, souvent en haut des arbres ou sur les façades. Le frelon européen s'installe plutôt dans les cavités (volets, murs, arbres creux) et joue un rôle utile dans la nature : je vous conseille au cas par cas, parfois il vaut mieux le laisser en place. Les guêpes font des nids de papier gris, au sol, dans un mur ou sous un toit."),
   ("Pourquoi ne pas le faire soi-même", "Les piqûres de frelons peuvent être graves, surtout en cas d'allergie, et un nid dérangé devient très agressif. Mieux vaut appeler un professionnel équipé."),
   ("Quand agir", "Du printemps à l'automne, les nids grossissent vite : plus vous attendez, plus le nid est gros et difficile à atteindre.")],
  [("Combien coûte la destruction d'un nid ?", "Le prix dépend de la hauteur, de l'accessibilité et du type de nid. Envoyez-moi une photo, je vous donne un devis gratuit."),
   ("Dois-je rester chez moi pendant l'intervention ?", "Je vous indique où vous placer, en général à l'intérieur, fenêtres fermées, à distance du nid.")]),
 ("desinsectisation", "Désinsectisation", "Désinsectisation : cafards, fourmis, puces et mouches",
  "Désinsectisation : Cafards, Fourmis, Puces | Proxinuisibles",
  "Désinsectisation en Mayenne et Ille-et-Vilaine : cafards, fourmis, puces, mouches. Traitement ciblé pour particuliers et professionnels.",
  "Un insecte dans la maison, le commerce ou l'atelier : je l'identifie avant de traiter, car chaque espèce demande sa propre méthode. Cafards, punaises de lit, puces, fourmis et mouches ont chacun leur page sur ce site.",
  [("Les insectes que je traite", "- <a href='/blattes-cafards/'>Cafards et blattes</a>\n- <a href='/punaises-de-lit/'>Punaises de lit</a>\n- <a href='/puces/'>Puces</a>\n- <a href='/fourmis/'>Fourmis</a>\n- <a href='/mouches/'>Mouches</a>\n- Moustiques, mites, guêpes et autres insectes : je traite au cas par cas, après identification"),
   ("Une méthode en trois temps", "J'identifie l'insecte et son point d'entrée, je réalise un traitement ciblé (gel, pulvérisation ou pièges selon le cas), puis je vous donne des conseils de prévention et je repasse si nécessaire."),
   ("Particuliers et professionnels", "Logement, restaurant, commerce, local d'entreprise : j'adapte le traitement aux lieux où l'on mange, dort ou travaille.")],
  [("Dois-je quitter mon logement ?", "Selon le traitement, vous devrez parfois quitter les lieux quelques heures. Je vous le précise avant l'intervention."),
   ("Pourquoi les fourmis reviennent-elles après mon passage ?", "Une colonie compte souvent plusieurs nids. Un second passage ou un traitement par appâts permet d'atteindre la source.")]),
 ("blattes-cafards", "Blattes et cafards", "Blattes et cafards en Mayenne et Ille-et-Vilaine : traitement ciblé",
  "Cafards et Blattes Mayenne | Proxinuisibles",
  "Traitement des cafards et blattes en Mayenne et Ille-et-Vilaine : diagnostic, gel, suivi. Particuliers et professionnels. Devis gratuit.",
  "Les cafards se cachent le jour et sortent la nuit : quand on en voit un, il y en a souvent beaucoup d'autres. Je repère les foyers, je traite et je contrôle le résultat.",
  [("Reconnaître une infestation de cafards", "Cafards aperçus la nuit, petites crottes noires comme du poivre moulu, odeur tenace, mues et oothèques (petites capsules brunes contenant les œufs) derrière les meubles. Ils se cachent dans les cuisines, les salles de bain, derrière les plinthes, autour des appareils électriques et dans les gaines techniques."),
   ("Pourquoi ils s'installent", "Les cafards cherchent trois choses : de la chaleur, de l'humidité et de la nourriture. Une miette sous un meuble, une fuite sous l'évier ou un carton de livraison suffit à les attirer. Ils arrivent souvent par les colis, les cartons, les gaines communes et les logements voisins."),
   ("Mon traitement, étape par étape", "Je commence par un diagnostic : je repère les foyers, j'identifie l'espèce et je cherche d'où ils viennent. Je traite ensuite avec la méthode adaptée au lieu (gel appât, pulvérisation ciblée ou pièges), en protégeant les denrées, les enfants et les animaux. Selon l'ampleur de l'infestation, je repasse pour contrôler le résultat."),
   ("Ce que vous pouvez faire avant et après", "Videz et nettoyez les zones à traiter, rangez les aliments dans des boîtes fermées, évitez de laver les plinthes juste après le traitement et réparez les fuites. Ne déplacez pas les meubles dans d'autres pièces : vous disperseriez les cafards."),
   ("Cuisines, restaurants et locaux alimentaires", "Dans un commerce ou un restaurant, la présence de cafards est un risque sanitaire et réglementaire. J'intègre le traitement à votre démarche HACCP : points de contrôle repérés, passages planifiés et compte rendu écrit à conserver pour vos contrôles. Un contrat de passages réguliers permet de détecter le problème avant qu'il ne s'installe."),
   ("Immeubles, copropriétés et locations", "Les cafards circulent d'un logement à l'autre par les gaines et les canalisations. Pour un immeuble, je traite les parties communes et les logements concernés, en coordination avec le syndic ou le bailleur, pour ne pas laisser de foyer résiduel.")],
  [("Les cafards reviennent-ils après le traitement ?", "Ils peuvent revenir si l'origine n'est pas traitée : humidité, nourriture accessible ou voisinage infesté. Je vous donne des conseils précis pour éviter une nouvelle infestation et je repasse au besoin."),
   ("Combien de passages faut-il ?", "Cela dépend de l'ampleur et du lieu. Un petit foyer peut se régler en un passage, une infestation installée demande en général un second passage de contrôle."),
   ("Dois-je quitter mon logement ?", "Selon le traitement, vous devrez parfois sortir quelques heures. Je vous le précise avant l'intervention."),
   ("Intervenez-vous dans les restaurants ?", "Oui. J'interviens dans les restaurants, boulangeries, boucheries et cuisines collectives, avec un compte rendu écrit après chaque passage.")]),
 ("fourmis", "Fourmis", "Fourmis dans la maison ou le jardin : traitement en Mayenne",
  "Fourmis Mayenne et Ille-et-Vilaine | Proxinuisibles",
  "Traitement des fourmis en Mayenne et Ille-et-Vilaine : fourmis dans la maison, le jardin ou les murs. Diagnostic, appâts, suivi. Devis gratuit.",
  "Une colonne de fourmis dans la cuisine, des fourmis qui sortent d'un mur ou d'une terrasse : je cherche le nid, pas seulement les fourmis que vous voyez.",
  [("Quelle fourmi avez-vous ?", "Toutes les fourmis ne se traitent pas de la même façon. Les fourmis noires des jardins entrent pour chercher du sucre. Les fourmis charpentières creusent le bois humide ou abîmé. Les fourmis pharaon, minuscules et jaunes, s'installent dans les bâtiments chauffés. J'identifie l'espèce avant de choisir le traitement."),
   ("Pourquoi elles entrent chez vous", "Les fourmis suivent les pistes laissées par leurs éclaireuses jusqu'à la nourriture : sucre, miettes, nourriture pour animaux, fruits. Elles passent par la moindre fissure, un seuil de porte, une gaine ou un câble. Une colonie compte souvent plusieurs nids et une ou plusieurs reines, ce qui explique que les fourmis reviennent après un simple coup de spray."),
   ("Mon traitement, étape par étape", "Je repère le trajet des fourmis, la source de nourriture et l'entrée. Je traite ensuite à l'endroit le plus efficace, en général avec des appâts que les ouvrières rapportent au nid pour atteindre la colonie, complétés par un traitement ciblé des passages. Je vous indique les points à surveiller et je repasse si nécessaire."),
   ("Fourmis dans les murs, le bois ou le jardin", "Quand les fourmis sortent d'un mur, d'une poutre ou d'une terrasse, le nid est souvent à l'intérieur de la structure ou dans le sol. Je cherche l'origine de l'humidité qui attire les fourmis charpentières et je traite le nid, pas seulement le point de sortie."),
   ("Ce que vous pouvez faire", "Rangez les aliments sucrés dans des boîtes fermées, nettoyez les miettes, ne lavez pas la piste avec du vinaigre juste avant mon passage (cela efface les repères que j'utilise) et bouchez les fissures visibles. Évitez les sprays du commerce sur les pistes : ils dispersent la colonie."),
   ("Restaurants, boulangeries et locaux professionnels", "Les fourmis dans un local alimentaire posent un problème d'hygiène. Je traite avec des méthodes adaptées aux lieux où l'on manipule des denrées, avec un compte rendu écrit après chaque visite, utile pour votre démarche HACCP.")],
  [("Pourquoi les fourmis reviennent-elles après un spray ?", "Le spray tue les fourmis visibles mais pas la colonie. Les ouvrières que vous voyez ne sont qu'une petite partie du nid, et les autres continuent de chercher de la nourriture."),
   ("Les appâts sont-ils dangereux pour mes animaux ?", "Je les place hors de portée des enfants et des animaux, dans des endroits peu accessibles, et je vous explique où ils se trouvent."),
   ("Combien de temps pour voir le résultat ?", "Avec des appâts, il faut compter quelques jours à quelques semaines : la colonie doit les rapporter au nid. Je repasse si nécessaire."),
   ("Traitez-vous les fourmis charpentières ?", "Oui. Je cherche l'origine de l'humidité dans le bois et je traite le nid ; une réparation du support peut aussi être nécessaire.")]),
 ("frelon-asiatique", "Frelon asiatique", "Frelon asiatique : reconnaître le nid et le faire détruire",
  "Frelon Asiatique Mayenne et Ille-et-Vilaine | Proxinuisibles",
  "Destruction de nids de frelons asiatiques en Mayenne et Ille-et-Vilaine : reconnaître l'espèce, le nid, que faire. Devis gratuit.",
  "Un nid de frelon asiatique peut abriter plusieurs milliers d'individus et se défend violemment : ne tentez jamais de le détruire vous-même. J'interviens avec le matériel et la protection adaptés, du nid primaire au printemps au gros nid d'automne.",
  [("Reconnaître le frelon asiatique", "Le frelon asiatique (Vespa velutina, variété nigrithorax) mesure de 17 à 32 mm. Il a la tête orange avec le dessus noir, le thorax entièrement noir, l'abdomen sombre barré de fines bandes jaunes et orange, et surtout l'extrémité des pattes jaune, ce qui lui vaut le nom de frelon à pattes jaunes.\nÀ ne pas confondre avec le frelon européen (Vespa crabro), notre espèce locale : celui-ci est plus clair, avec des marques rousses et un abdomen largement jaune. Le frelon européen n'est pas une espèce envahissante et son nid ne se détruit pas systématiquement."),
   ("Reconnaître le nid", "Le nid est en carton gris ou brun, nettement strié. Un nid mature mesure le plus souvent 40 à 60 cm de diamètre ; les plus gros atteignent 1 m de haut et 80 cm de large. Son ouverture est petite et placée sur le côté, alors que celle des guêpes communes se trouve en bas.\nAu printemps, la fondatrice construit d'abord un nid primaire, petit et abrité : sous un abri de jardin, dans un carport, sous une avancée de toit, dans un cabanon. Quand la colonie grandit, elle déménage souvent dans un nid secondaire, plus haut, en général dans un arbre. C'est celui qu'on découvre à l'automne, à la chute des feuilles."),
   ("Le cycle annuel, et pourquoi la saison compte", "La fondatrice démarre sa colonie entre février et avril. La colonie grossit tout l'été. Les premiers mâles apparaissent vers la mi-septembre, les futures fondatrices début octobre, et le nombre d'individus culmine début novembre. Un nid mature produit en moyenne environ 6 000 individus sur la saison, et plus de 15 000 pour les plus grosses colonies.\nEn fin d'automne, la reine et les ouvrières meurent. Seules les futures fondatrices passent l'hiver, cachées dans le sol, un tas de bois ou une anfractuosité. Un nid vide n'est jamais réutilisé l'année suivante : inutile de le détruire en hiver, sauf s'il gêne."),
   ("Le danger pour vous et vos proches", "Le frelon asiatique n'attaque pas spontanément quand on passe à distance. En revanche, il défend son nid avec vigueur : s'approcher à quelques mètres, tondre ou tailler à côté, ou faire vibrer le support suffit à déclencher une attaque groupée, avec des piqûres multiples.\nLes données des centres antipoison ne montrent pas que ses piqûres soient plus dangereuses que celles des autres hyménoptères. Le risque reste sérieux en cas de piqûres multiples, de piqûre à la gorge ou au visage, et chez les personnes allergiques. En cas de gêne respiratoire, de malaise ou de gonflement qui s'étend, appelez le 15 sans attendre."),
   ("Le danger pour les abeilles", "Le frelon asiatique chasse devant les ruches. Les abeilles domestiques représentent environ 37 % de ses proies, avec les guêpes et les mouches. Une pression continue devant une ruche arrête le butinage et peut affaiblir la colonie au point de la faire mourir de faim pendant l'hiver.\nIl est classé danger sanitaire de deuxième catégorie pour l'abeille domestique. Si vous avez des ruches, ou un rucher voisin, signalez-le-moi : cela change l'urgence de l'intervention."),
   ("Mon intervention sur un nid", "Je repère le nid et j'observe le trajet des ouvrières, j'évalue la hauteur et l'accès, puis j'interviens avec une combinaison de protection intégrale et une perche télescopique quand le nid est haut. Je sécurise la zone avant de commencer et je vous indique où vous placer, en général à l'intérieur, fenêtres fermées.\nJe retire le nid quand c'est possible, sinon je le neutralise sur place. Le délai habituel est de 24 à 48 heures, et je traite les urgences plus vite : nid à hauteur d'homme, près d'une entrée, d'une école ou d'une personne allergique."),
   ("Ce qu'il ne faut surtout pas faire", "- Ne jetez rien sur le nid, ne l'arrosez pas au jet d'eau et n'y mettez pas le feu : vous déclencheriez une attaque et risqueriez l'incendie\n- N'utilisez pas de bombe insecticide du commerce : la portée est insuffisante et le produit retombe sur vous\n- Ne montez pas sur une échelle pour atteindre un nid : les piqûres provoquent une chute\n- Ne bouchez pas l'entrée d'un nid logé dans un mur ou un coffre de volet : les frelons ressortent par l'intérieur du bâtiment"),
   ("Le piégeage de printemps : ce qu'il faut savoir", "Beaucoup de pièges à fondatrices sont vendus au printemps. Les études disponibles montrent que leur efficacité fait débat : les captures de fondatrices sont faibles (1 à 6 par piège et par semaine) et représentent moins de 2 % de ce qui est attrapé. Le reste, soit 48 à 92 % des captures, est constitué de mouches, de papillons, de coléoptères, d'abeilles et de frelons européens, des espèces utiles et parfois en déclin.\nSi vous piégez malgré tout, par exemple pour protéger un rucher, utilisez un piège sélectif (type nasse), piégez d'avril à début mai et arrêtez ensuite. La destruction des nids reste la méthode la plus efficace."),
   ("Ce que dit la loi, et qui paie", "Le frelon asiatique figure sur la liste des espèces exotiques envahissantes fixée par l'arrêté du 14 février 2018. Le code de l'environnement interdit de détenir, transporter ou vendre des spécimens vivants, et le préfet peut ordonner la destruction de nids, y compris sur une propriété privée.\nL'État ne finance pas la destruction : elle reste à la charge du propriétaire. Certaines communes ou communautés de communes participent cependant aux frais. Appelez votre mairie avant l'intervention : si une aide existe, je vous fournis la facture nécessaire.")],
  [("Comment savoir si c'est un frelon asiatique ou européen ?", "Regardez les pattes : le frelon asiatique a l'extrémité des pattes jaune et le thorax entièrement noir. Le frelon européen est plus clair, avec des marques rousses et un abdomen largement jaune. En cas de doute, envoyez-moi une photo."),
   ("Faut-il détruire un nid de frelons européens ?", "Pas systématiquement. Le frelon européen est une espèce locale utile, peu agressive loin de son nid. Je ne détruis son nid que s'il présente un vrai risque : près d'une entrée, d'un lieu de passage ou d'une personne allergique."),
   ("Que faire si je trouve un nid en hiver ?", "Un nid vide n'est jamais réutilisé l'année suivante. Si les frelons n'y entrent plus et qu'il ne gêne pas, vous pouvez le laisser. S'il est mal placé ou qu'il risque de tomber, je peux le retirer."),
   ("Ma mairie prend-elle en charge la destruction ?", "Cela dépend de votre commune : il n'y a pas d'aide nationale. Appelez votre mairie avant mon passage, et je vous remets la facture dont vous aurez besoin."),
   ("J'ai un nid dans un volet roulant ou un mur, est-ce possible ?", "Oui, surtout pour un nid primaire au printemps. Ne bouchez pas l'ouverture : les frelons chercheraient une autre sortie, souvent vers l'intérieur. Appelez-moi, je traite depuis l'extérieur."),
   ("Combien coûte la destruction d'un nid ?", "Le tarif dépend de la hauteur, de l'accessibilité et de la situation. Envoyez-moi une photo prise à distance : je vous donne un devis gratuit, déplacement compris.")]),
 ("mouches", "Mouches", "Invasion de mouches : traitement en Mayenne et Ille-et-Vilaine",
  "Invasion de Mouches Mayenne | Proxinuisibles",
  "Traitement contre les mouches en Mayenne et Ille-et-Vilaine : maison, dépendance, élevage, local pro. Badigeon longue durée. Devis gratuit.",
  "Des dizaines de mouches dans une pièce, une véranda ou un bâtiment : j'interviens pour faire tomber la population et la tenir basse pendant toute la saison.",
  [("Quelle mouche avez-vous ?", "- La mouche domestique : la plus courante dans les maisons et les bâtiments, très présente dès qu'il fait chaud\n- La petite mouche des fruits (drosophile) : minuscule, autour des fruits, des bouteilles et des bacs à déchets\n- La mouche des terreaux : autour des plantes d'intérieur\n- La mouche bleue ou verte : grosse et bruyante, souvent le signe d'un animal mort dans un comble ou une cloison\n- La mouche des étables : piqueuse, fréquente autour des bâtiments d'élevage\nL'espèce change le traitement et les surfaces à traiter : je l'identifie avant d'intervenir."),
   ("Mon traitement, étape par étape", "Je regarde d'abord où les mouches se posent et se rassemblent : plafonds, encadrements de fenêtres, suspensions, charpente, zones chaudes et éclairées. Ce sont ces surfaces de repos qui portent le traitement.\nJ'applique ensuite le traitement adapté au lieu : badigeon longue durée dans une pièce ou une dépendance, traitement des surfaces de repos dans un bâtiment, appâts ou pièges lumineux dans un local professionnel. L'effet sur les mouches présentes est rapide, et le traitement continue d'agir sur celles qui arrivent ensuite.\nJe repasse pour contrôler le résultat si l'infestation était importante."),
   ("Le badigeon, ma solution longue durée", "C'est le traitement que je propose en premier chez les particuliers : une seule application, posée au pinceau sur les surfaces de repos, et une saison entière tranquille, de mai à décembre. Il évite les pulvérisations répétées et les bombes insecticides rachetées tout l'été. Voir le détail plus haut sur cette page."),
   ("Maisons, vérandas et dépendances", "Une cuisine, une véranda, une buanderie, un garage, un abri de jardin ou un chenil : ce sont les pièces où les mouches se concentrent dès les beaux jours. J'applique le traitement en hauteur, sur les zones où elles se posent, à l'écart des plans de travail, des aliments et des gamelles. Vous et vos animaux restez sur place."),
   ("Élevages et bâtiments agricoles", "Dans une étable, une stabulation ou un poulailler, les mouches pèsent sur le calme et le bien-être des animaux. Je traite les surfaces de repos du bâtiment, avec des produits et des modes d'application adaptés à la présence des animaux et aux règles sanitaires de votre exploitation."),
   ("Restaurants, boulangeries et commerces alimentaires", "Une mouche dans une salle ou un laboratoire, c'est un risque sanitaire et une mauvaise image immédiate auprès de vos clients. J'interviens avec des méthodes adaptées aux locaux alimentaires, et je remets un compte rendu écrit après chaque passage, à conserver pour vos contrôles dans le cadre de votre démarche HACCP."),
   ("Quand me faire intervenir", "Le mieux est d'intervenir au printemps, dès les premières mouches, avant que la population ne monte : le traitement tient alors toute la belle saison. En plein été, j'interviens aussi bien, mais le résultat est plus visible si l'on n'a pas laissé la situation s'installer pendant des semaines.")],
  [("Combien de temps avant de voir un résultat ?", "La population d'adultes chute en général dans les heures qui suivent l'intervention. Le badigeon, lui, continue d'agir ensuite pendant toute la saison."),
   ("Combien de temps dure le traitement ?", "Le badigeon reste actif de mai à décembre. Pour les autres traitements, la durée dépend du produit et du lieu ; je vous le précise lors du devis."),
   ("D'où viennent ces grosses mouches bleues dans mon grenier ?", "Le plus souvent d'un animal mort : rongeur, oiseau ou fouine, dans un comble ou une cloison. Je le cherche, je le retire quand c'est possible et je traite la zone."),
   ("Peut-on traiter avec des animaux dans le bâtiment ?", "Oui, avec des produits et des modes d'application adaptés. Je vous indique les précautions à prendre avant mon passage."),
   ("Dois-je quitter la pièce pendant le traitement ?", "Avec le badigeon, non : vous et vos animaux restez sur place. Pour les autres traitements, je vous précise avant mon passage s'il faut sortir quelques heures.")]),
 ("puces", "Puces", "Puces dans la maison : traitement en Mayenne et Ille-et-Vilaine",
  "Traitement Puces Mayenne | Proxinuisibles",
  "Traitement des puces en Mayenne et Ille-et-Vilaine : maison, chat, chien, logement vide. Diagnostic, traitement, suivi. Devis gratuit.",
  "Des piqûres sur les chevilles, un animal qui se gratte, de petites bêtes qui sautent : les puces se logent dans les textiles et les planchers, pas seulement sur l'animal. Je traite le logement et vous accompagnez le traitement de l'animal.",
  [("Reconnaître une infestation de puces", "Les signes les plus fréquents sont des piqûres groupées sur les chevilles et le bas des jambes, souvent plusieurs à la suite, un animal qui se gratte ou se mordille, de petits grains noirs dans son pelage ou son panier (les déjections, qui rougissent sur un papier humide) et de petites bêtes brunes qui sautent quand on écarte un tapis.\nLes puces se cachent dans les tapis, les moquettes, les fentes des planchers, les plinthes, les paniers et les canapés. On ne les voit pas toujours : les adultes visibles ne représentent qu'une petite partie de la population."),
   ("Pourquoi un simple traitement de l'animal ne suffit pas", "Les puces adultes vivent sur l'animal, mais les œufs tombent au sol : dans le panier, les tapis, les interstices du parquet. S'y ajoutent les larves et les cocons, qui résistent longtemps et peuvent attendre plusieurs semaines, parfois plusieurs mois, avant d'éclore. Ils réagissent à la chaleur et aux vibrations, c'est-à-dire à votre passage.\nTraiter seulement l'animal laisse donc intacte la majeure partie de l'infestation. Il faut traiter le logement en même temps."),
   ("Mon traitement, étape par étape", "Je repère les zones de couchage et de passage de l'animal, puis je traite les sols, les plinthes, les textiles et les interstices avec un produit adapté aux lieux et à la présence d'enfants ou d'animaux. Selon l'ampleur, un second passage est nécessaire pour atteindre les puces écloses après le premier traitement. Je vous explique avant mon passage ce qu'il faut préparer, et après, ce qu'il faut faire ou éviter."),
   ("Ce que vous devez faire de votre côté", "Faites traiter l'animal par votre vétérinaire : c'est indispensable, et c'est son rôle, pas le mien. Lavez les paniers et les couvertures à 60 °C si le textile le permet. Passez l'aspirateur partout avant mon passage, insistez sur les plinthes et les interstices, puis jetez le sac dehors. Après le traitement, ne lavez pas les sols pendant la durée que je vous indique : vous retireriez le produit. Continuez d'aspirer régulièrement, car les vibrations font éclore les cocons et exposent les puces au traitement."),
   ("Logement vide, vente ou location", "Un logement inoccupé après le départ d'un animal reste infesté : les cocons attendent. Les nouveaux arrivants se font piquer dès les premiers jours. Si vous êtes propriétaire, bailleur ou agence, faites traiter avant la remise des clés. J'interviens dans les logements vides, les gîtes et les locations saisonnières."),
   ("Piqûres et santé", "Les piqûres de puces provoquent des démangeaisons et de petits boutons groupés, surtout aux chevilles. Le grattage peut entraîner une surinfection. Chez l'animal, une allergie à la salive de puce est fréquente et demande un suivi vétérinaire. Pour toute question médicale, adressez-vous à votre médecin ou à votre vétérinaire.")],
  [("Dois-je traiter mon animal en même temps ?", "Oui, c'est indispensable : sans cela, l'animal réensemence le logement. Le traitement de l'animal relève de votre vétérinaire, celui du logement de mon intervention."),
   ("Pourquoi vois-je encore des puces après le traitement ?", "Parce que les cocons éclosent progressivement. Les puces qui émergent entrent en contact avec le produit et meurent. Un second passage est parfois nécessaire ; je vous le dis dès le diagnostic."),
   ("Puis-je rester chez moi ?", "Selon le traitement, vous devrez parfois quitter les lieux quelques heures. Je vous le précise avant l'intervention."),
   ("J'ai des puces alors que je n'ai pas d'animal, est-ce possible ?", "Oui. Elles peuvent venir d'un logement voisin, d'un ancien occupant, d'un animal de passage, ou de rongeurs, de fouines ou d'oiseaux installés dans les combles. Je cherche l'origine.")]),
 ("chenilles-processionnaires", "Chenilles processionnaires", "Traitement des chenilles processionnaires en Mayenne et Ille-et-Vilaine",
  "Chenilles Processionnaires Mayenne | Proxinuisibles",
  "Traitement des chenilles processionnaires du pin et du chêne en Mayenne et Ille-et-Vilaine. Intervention sécurisée, devis gratuit.",
  "Les poils urticants des chenilles processionnaires provoquent des irritations de la peau, des yeux et des voies respiratoires, et sont dangereux pour les chiens. Ne touchez pas aux cocons.",
  [("Pins et chênes", "La processionnaire du pin forme des cocons blancs et soyeux dans les pins en hiver. La processionnaire du chêne descend en colonnes le long du tronc au printemps."),
   ("Quand traiter", "Le bon moment dépend de l'espèce et de la saison. Je vous le précise lors du devis."),
   ("Où j'interviens", "Jardins de particuliers, écoles, campings, aires de jeux et espaces verts.")],
  [("Mon chien a touché une chenille, que faire ?", "Appelez sans attendre un vétérinaire : c'est une urgence."),
   ("Puis-je couper le cocon moi-même ?", "Non : les poils se dispersent et peuvent provoquer de graves irritations. Faites appel à un professionnel équipé.")]),
 ("punaises-de-lit", "Punaises de lit", "Traitement des punaises de lit en Mayenne et Ille-et-Vilaine",
  "Traitement Punaises de Lit Mayenne | Proxinuisibles",
  "Traitement des punaises de lit en Mayenne et Ille-et-Vilaine : diagnostic, traitement discret et suivi. Particuliers, locations et gîtes.",
  "Piqûres au réveil, petites taches noires sur le matelas ou le sommier : les punaises de lit se cachent bien et ne partent pas seules. Je traite discrètement, chez les particuliers comme dans les locations et les hébergements.",
  [("Reconnaître une infestation", "Piqûres alignées, taches de sang ou points noirs sur la literie, odeur douceâtre. Les punaises se logent dans le matelas, le sommier, les plinthes et les meubles."),
   ("Un traitement discret", "Après un diagnostic, je traite les zones touchées puis je contrôle le résultat. Selon l'ampleur, un ou plusieurs passages sont nécessaires."),
   ("Avant mon passage", "Lavez le linge à 60 °C si possible et ne déplacez pas les meubles dans d'autres pièces, pour ne pas disséminer les punaises."),
   ("Locations, gîtes et agences", "Je peux intervenir rapidement dans un logement loué pour que les occupants suivants ne soient pas touchés.")],
  [("Puis-je les éliminer avec des produits de grande surface ?", "Ils suffisent rarement pour une infestation installée : les œufs et les cachettes résistent. Un traitement professionnel est plus fiable."),
   ("Combien de passages faut-il ?", "Cela dépend de l'ampleur. Je vous l'indique dès le diagnostic.")]),
 ("taupier", "Taupier", "Taupier : piégeage des taupes en Mayenne et Ille-et-Vilaine",
  "Taupier en Mayenne et Ille-et-Vilaine | Proxinuisibles",
  "Piégeage de taupes en Mayenne et Ille-et-Vilaine : jardins, terrains de sport, prairies. Intervention rapide, devis gratuit.",
  "Des taupinières dans la pelouse, le potager ou la prairie ? Le piégeage est la méthode la plus fiable pour retrouver un terrain propre.",
  [("Le piégeage", "Je repère les galeries actives et je pose des pièges adaptés. Je repasse les relever et je poursuis jusqu'à la disparition des taupes."),
   ("Où j'interviens", "- Jardins et potagers\n- Terrains de sport et golfs\n- Prairies et parcelles agricoles")],
  [("Pourquoi ne pas utiliser des répulsifs ?", "Ils déplacent souvent le problème chez le voisin sans l'éliminer."),
   ("Combien de temps dure le traitement ?", "Quelques passages, étalés selon la surface et le nombre de taupes.")]),
 ("depigeonnage", "Dépigeonnage", "Dépigeonnage : protéger façades, toitures et bâtiments",
  "Dépigeonnage Mayenne et Ille-et-Vilaine | Proxinuisibles",
  "Dépigeonnage en Mayenne et Ille-et-Vilaine : pics, filets, câbles et piégeage en cage pour façades, toitures et bâtiments. Devis gratuit.",
  "Les fientes salissent les façades, abîment les matériaux et présentent un risque sanitaire : je pose pics, filets et câbles pour éloigner les pigeons. Quand une colonie est déjà bien installée, je complète par un piégeage en cage.",
  [("Les solutions", "- Pics anti-pigeons sur les rebords et corniches\n- Filets sur les ouvertures, balcons et charpentes\n- Câbles tendus sur les poutres et enseignes\n- Piégeage en cage pour réduire une colonie installée\nJe choisis la solution selon le bâtiment."),
   ("Le piégeage des pigeons", "Quand des dizaines d'oiseaux occupent un hangar, un clocher ou une toiture, les protections seules ne suffisent pas toujours. Je pose alors des cages de capture : l'oiseau entre attiré par la nourriture et ne peut plus ressortir. Pendant quelques jours, je les habitue au point de nourrissage, puis je lance la capture et je contrôle les cages régulièrement."),
   ("Un piégeage qui a ses règles", "- Il vise les pigeons domestiques et les pigeons de ville, pas le pigeon ramier (la palombe), dont le piégeage est interdit\n- Sur un site privé, il se fait avec l'accord du propriétaire ou du gestionnaire\n- Dans un bourg ou sur le domaine public, la régulation relève du maire : j'interviens avec son accord\nJe commence donc par identifier l'espèce et le cadre de l'intervention."),
   ("Piéger et protéger : les deux vont ensemble", "Une colonie capturée se reforme vite si le lieu reste accueillant. Après le piégeage, je ferme les accès, je pose les protections adaptées et je vous indique les sources de nourriture à supprimer. C'est ce qui rend le résultat durable. Pour les autres animaux, voir aussi mon activité de <a href='/piegeur-agree/'>piégeur agréé</a>."),
   ("Pour qui", "Copropriétés, commerces, entrepôts, exploitations agricoles, collectivités et particuliers.")],
  [("Les pics font-ils du mal aux pigeons ?", "Non, ils empêchent seulement l'oiseau de se poser."),
   ("Le dispositif tient-il longtemps ?", "Un dispositif bien posé et entretenu dure longtemps."),
   ("Peut-on piéger tous les pigeons ?", "Non. Le piégeage concerne les pigeons domestiques et les pigeons de ville. Il est interdit pour le pigeon ramier, aussi appelé palombe."),
   ("Le piégeage suffit-il à régler le problème ?", "Rarement à lui seul : d'autres pigeons reviennent si le site reste accessible. Je l'associe à des protections et à la suppression des sources de nourriture.")]),
 ("piegeur-agree", "Piégeur agréé", "Piégeur agréé en Mayenne et Ille-et-Vilaine : ragondins, fouines, corvidés",
  "Piégeur Agréé Mayenne et Ille-et-Vilaine | Proxinuisibles",
  "Piégeur agréé en Mayenne et Ille-et-Vilaine : fouines dans les combles, ragondins, corvidés. Piégeage encadré par la loi, devis gratuit.",
  "Fouine dans les combles, ragondin au bord de l'étang : le piégeage de ces animaux est encadré par la loi, et je le réalise en tant que piégeur agréé. La fouine est le cas le plus fréquent : bruits la nuit, isolation arrachée, câbles rongés.",
  [("Un piégeage encadré par la loi", "Le piégeage des espèces classées susceptibles d'occasionner des dégâts demande une formation spécifique et un agrément délivré par le préfet. La liste des espèces et les modalités varient selon le département : je m'appuie sur les arrêtés en vigueur en Mayenne et en Ille-et-Vilaine."),
   ("Les situations que je traite", "- Ragondins et rats musqués près des berges, étangs et fossés\n- Fouines et martres dans les combles, les garages et les véhicules\n- Corvidés (corneilles, corbeaux freux) dans les cultures\n- D'autres animaux classés, selon le département et la période"),
   ("Comment je travaille", "Je repère les passages et les dégâts, je choisis le piège adapté et je le pose dans le respect de la réglementation. Je relève les pièges régulièrement et je vous explique comment éviter le retour de l'animal : fermeture des accès, protection des volailles et des cultures."),
   ("La fouine : le cas le plus fréquent", "La fouine est de loin l'animal pour lequel on m'appelle le plus. Elle s'installe dans les combles, les faux plafonds, les garages, les granges et les greniers, et se trahit par des bruits nocturnes de course et de griffes au-dessus du plafond, une odeur forte, des déjections et des restes de proies.\nLes dégâts sont réels : laine de verre arrachée et tassée, câbles et gaines rongés, planchers et plafonds souillés par l'urine, et isolation à remplacer. Sur les véhicules garés à proximité, elle s'attaque aux durites et aux câbles du compartiment moteur, ce qui peut coûter cher à réparer."),
   ("Comment je traite une fouine dans les combles", "Je commence par confirmer qu'il s'agit bien d'une fouine : rat, loir, lérot ou oiseau ne laissent ni les mêmes traces ni les mêmes bruits. Je cherche ensuite les accès : tuiles déplacées, rives de toiture, chatières, passages de gouttières ou arbres qui touchent le toit. Une fouine passe par une ouverture de la taille d'un poing.\nLe piégeage se fait avec des pièges adaptés, posés et relevés dans le respect de la réglementation. Une fois l'animal retiré, je vous indique les accès à fermer : sans cette étape, une autre fouine reprend la place, car l'emplacement reste attractif."),
   ("Copropriétés, bailleurs et agences immobilières", "Les fouines dans les combles d'un immeuble ou d'une maison en gestion posent un problème concret : nuisances sonores pour les occupants, dégradation de l'isolation, et parfois conflit entre locataire et propriétaire sur l'origine des bruits.\nJe travaille avec des agences immobilières, des syndics et des bailleurs du secteur. J'interviens sur un logement comme sur un ensemble, je remets un compte rendu écrit après chaque passage, et je fournis la liste des accès à reboucher pour que le problème ne revienne pas. C'est le document qui permet de décider des travaux, y compris en assemblée générale."),
   ("Particuliers, agriculteurs et collectivités", "J'interviens chez les particuliers, sur les exploitations agricoles, autour des étangs et des plans d'eau, et pour les communes qui ont un problème de nuisibles. Pour les professionnels de l'immobilier, voir aussi ma page dédiée aux agences et aux syndics.")],
  [("Pourquoi faire appel à un piégeur agréé ?", "Parce que le piégeage de certaines espèces est réservé aux personnes formées et agréées, avec des règles précises sur les pièges et les périodes."),
   ("J'entends des bruits dans mes combles la nuit, est-ce une fouine ?", "C'est possible. La fouine fait un bruit de course et de griffes, souvent en début de nuit et au petit matin. Un rat, un loir ou un lérot ne laissent pas les mêmes traces : je me déplace pour identifier l'animal avant de proposer une solution."),
   ("Une fouine peut-elle abîmer ma voiture ?", "Oui. Elle s'attaque aux durites et aux câbles du compartiment moteur des véhicules garés près de son territoire. C'est un motif fréquent d'intervention."),
   ("Que faire après le retrait de l'animal ?", "Il faut fermer les accès, sinon une autre fouine reprend la place. Je vous remets la liste des points à reboucher après mon intervention."),
   ("Travaillez-vous avec les agences et les syndics ?", "Oui, régulièrement. J'interviens sur un logement comme sur un ensemble, avec un compte rendu écrit après chaque passage."),
   ("Intervenez-vous aussi pour les rats, les souris et les taupes ?", "Oui, ce sont d'autres prestations de mon activité. Voir les pages dératisation et taupier.")]),
]
_ORDRE = ["deratisation", "frelons-guepes", "frelon-asiatique", "punaises-de-lit", "blattes-cafards",
          "puces", "fourmis", "mouches", "desinsectisation", "chenilles-processionnaires",
          "taupier", "depigeonnage", "piegeur-agree"]
SV.sort(key=lambda x: _ORDRE.index(x[0]) if x[0] in _ORDRE else 99)
for slug, nav, h1, title, meta, lead, secs, faq in SV:
    add("/%s/" % slug, nav=nav, h1=h1, title=title, meta=meta, lead=lead, secs=secs, faq=faq, kind="service")

# ---------- CIBLES ----------
add("/particuliers/", h1="Anti-nuisibles pour particuliers en Mayenne et Ille-et-Vilaine",
    title="Anti-Nuisibles Particuliers Mayenne | Proxinuisibles",
    meta="Rats, souris, frelons, punaises de lit, chenilles : intervention chez les particuliers en Mayenne et Ille-et-Vilaine. Devis gratuit.",
    lead="Un nuisible chez vous est stressant. Je viens, j'identifie le problème, je vous explique ce qui se passe et je règle la situation.",
    secs=[("Les problèmes que je règle", "- Rats et souris dans la maison, le garage ou le jardin\n- Nids de frelons et de guêpes\n- Punaises de lit, puces, cafards, fourmis\n- Chenilles processionnaires et taupes"),
          ("Comment ça se passe", "Vous m'appelez ou m'envoyez une photo, je vous donne un devis gratuit, puis nous fixons un créneau. Je vous explique chaque étape et les précautions à prendre.")],
    faq=[("Le devis est-il gratuit ?", "Oui, le diagnostic et le devis sont gratuits.")], kind="cible")
add("/agriculteurs/", h1="Dératisation et nuisibles pour agriculteurs et éleveurs",
    title="Dératisation Agriculteurs et Éleveurs | Proxinuisibles",
    meta="Dératisation de bâtiments d'élevage, hangars et exploitations en Mayenne et Ille-et-Vilaine. Taupes, rats, souris. Devis gratuit.",
    lead="Les rongeurs abîment les stocks, les câbles et l'isolation, et peuvent contaminer l'alimentation des animaux. J'interviens sur les exploitations avec une méthode adaptée aux bâtiments agricoles.",
    secs=[("Bâtiments concernés", "- Bâtiments d'élevage et étables\n- Hangars et silos\n- Locaux de stockage de céréales et d'aliments"),
          ("Rats, souris et taupes", "Je traite les rongeurs dans les bâtiments et je piège les taupes dans les prairies et les parcelles. Je vous conseille sur les points d'entrée à fermer et la gestion des déchets et des stocks. Pour les ragondins, les fouines ou les corvidés, j'interviens aussi en tant que piégeur agréé.")],
    faq=[("Intervenez-vous en pleine campagne ?", "Oui, je me déplace sur tout le secteur Mayenne et Ille-et-Vilaine.")], kind="cible")
add("/professionnels/", h1="Anti-nuisibles pour professionnels et collectivités : restaurants, commerces, mairies",
    title="Anti-Nuisibles Professionnels Laval | Proxinuisibles",
    meta="Dératisation et désinsectisation pour restaurants, boulangeries, traiteurs, entreprises, communes et collectivités. Contrat annuel et suivi.",
    lead="Pour un professionnel, un nuisible est un risque sanitaire, un risque de contrôle et un risque d'image. Je propose des interventions ponctuelles et des contrats de suivi.",
    secs=[("Métiers de bouche", "Chaque métier a ses points sensibles. Choisissez le vôtre pour voir ce que je traite."),
          ("Entreprises, entrepôts et collectivités", "Locaux d'entreprise, entrepôts, écoles, mairies : je réalise un diagnostic puis un traitement adapté, avec un suivi régulier si besoin.")],
    faq=[("Proposez-vous un contrat annuel ?", "Oui, avec des passages réguliers et un suivi de votre site. Voir la page contrat annuel.")],
    links=[("Par métier", [("Restaurant", "/deratisation-restaurant-laval/"), ("Boulangerie", "/deratisation-boulangerie-laval/"), ("Boucherie", "/deratisation-boucherie-laval/"), ("Traiteur", "/deratisation-traiteur-laval/"), ("Cuisine collective", "/deratisation-cuisine-collective-laval/"), ("Contrat annuel", "/contrat-annuel-deratisation/"), ("Contrats métiers de bouche autour de Laval et Vitré", "/contrats-metiers-de-bouche/"), ("Agences et syndics", "/agences-syndics/")])],
    kind="cible")
add("/agences-syndics/", h1="Anti-nuisibles pour agences immobilières et syndics",
    title="Anti-Nuisibles Agences et Syndics | Proxinuisibles",
    meta="Rongeurs, punaises de lit, fouines dans les combles : j'interviens pour les agences immobilières, syndics et bailleurs en Mayenne et Ille-et-Vilaine.",
    lead="Locataires gênés, parties communes touchées, logement à remettre en état : j'interviens vite pour limiter les dégâts et les litiges.",
    secs=[("Pour la gestion locative et les copropriétés", "- Rats et souris dans les caves et locaux poubelles\n- Punaises de lit, cafards et puces dans les logements\n- Nids de frelons et pigeons sur les parties communes\n- <a href='/piegeur-agree/'>Fouines dans les combles et les faux plafonds</a>"),
          ("Les fouines dans les combles : un motif d'appel fréquent", "C'est l'un des problèmes qui remontent le plus souvent en gestion locative, et l'un des plus mal traités. Un locataire signale des bruits de course au-dessus du plafond, parfois une odeur : il s'agit très souvent d'une fouine installée dans les combles ou un faux plafond.\nLes conséquences sont concrètes : laine de verre arrachée et tassée, câbles et gaines rongés, plafonds souillés, isolation à remplacer, et des véhicules endommagés sur le parking quand l'animal s'attaque aux durites. Plus l'intervention tarde, plus les travaux de remise en état coûtent cher."),
          ("Ce que je vous apporte sur ce sujet", "J'identifie d'abord l'animal, car un rat, un loir ou un oiseau ne se traitent pas de la même façon. Je réalise ensuite le piégeage en tant que piégeur agréé, dans le respect de la réglementation.\nSurtout, je vous remets la liste des accès à reboucher : sans cette étape, une autre fouine reprend la place. C'est ce document qui vous permet de chiffrer les travaux et de les faire voter, en conseil syndical comme en assemblée générale. Voir la page <a href='/piegeur-agree/'>piégeur agréé</a> pour le détail."),
          ("Un interlocuteur unique", "C'est moi qui réponds, qui viens et qui interviens : pas de plateforme, pas de sous-traitance. Je vous remets un devis clair avant chaque intervention et un compte rendu écrit après, et je peux assurer un suivi par résidence. Je suis joignable de 8h à 21h en semaine et de 9h à 18h le week-end.")],
    faq=[("Pouvez-vous intervenir en urgence dans un logement ?", "Appelez-moi, nous fixons un créneau le plus tôt possible selon la situation."),
         ("Un locataire entend des bruits dans les combles, que faire ?", "Faites-moi intervenir pour identifier l'animal avant d'engager des travaux : fouine, rat, loir et oiseau demandent des réponses différentes."),
         ("Fournissez-vous un document pour l'assemblée générale ?", "Oui. Après mon passage, je remets un compte rendu écrit avec les constats et la liste des accès à reboucher, utilisable pour chiffrer et faire voter les travaux."),
         ("Intervenez-vous sur plusieurs logements d'un même immeuble ?", "Oui, et dans la même journée quand c'est possible, ce qui évite qu'une infestation reparte d'un logement non traité.")], kind="cible")

# ---------- METIERS (Laval) ----------
METIERS = [
 ("restaurant", "restaurant", "Dératisation Restaurant à Laval (53) | Proxinuisibles",
  "Dératisation et désinsectisation pour restaurants à Laval : intervention discrète, contrat annuel, devis gratuit.",
  "Un rongeur en cuisine, c'est un risque sanitaire et une menace pour votre réputation. J'interviens discrètement, en dehors des heures de service si besoin.",
  [("Les points sensibles d'un restaurant", "Réserves, caves, locaux poubelles, arrière-cuisine et passages de canalisations sont les premiers endroits où s'installent rongeurs et cafards."),
   ("Un suivi pour rester serein", "Avec un contrat annuel, je passe régulièrement et je vous remets un compte rendu à conserver pour vos contrôles d'hygiène."),
   ("Insectes aussi", "Cafards, mouches et fourmis sont traités avec des produits adaptés aux locaux alimentaires.")],
  [("Intervenez-vous en dehors des horaires d'ouverture ?", "Oui, nous fixons ensemble un créneau pour ne pas gêner le service.")]),
 ("boulangerie", "boulangerie", "Dératisation Boulangerie à Laval (53) | Proxinuisibles",
  "Dératisation et désinsectisation pour boulangeries à Laval : farines, fournil, réserves. Contrat annuel, devis gratuit.",
  "Farine, grains et sucre attirent souris, rats et insectes. Je protège votre fournil et vos réserves sans perturber la production.",
  [("Les zones à surveiller", "Réserve de farine, fournil, quai de livraison, locaux de stockage et abords de la boulangerie."),
   ("Prévention", "Je vous conseille sur le stockage, la fermeture des accès et la gestion des déchets pour limiter les risques."),
   ("Un contrat sur mesure", "Des passages réguliers calés sur votre activité, avec un compte rendu écrit.")],
  [("Mes produits de boulangerie risquent-ils d'être touchés ?", "Je place le matériel loin des denrées et je vous explique l'organisation avant chaque traitement.")]),
 ("boucherie", "boucherie", "Dératisation Boucherie à Laval (53) | Proxinuisibles",
  "Dératisation et désinsectisation pour boucheries et charcuteries à Laval : chambres froides, labo, déchets. Devis gratuit.",
  "Chambres froides, laboratoire de découpe et déchets d'origine animale attirent rongeurs et mouches. Je sécurise vos locaux avec un traitement adapté à l'alimentaire.",
  [("Points d'attention", "Chambres froides, labo de découpe, local à déchets, cour et quais de livraison."),
   ("Mouches et insectes", "Les mouches sont un vrai sujet en boucherie : je traite et je vous donne des conseils d'hygiène simples."),
   ("Suivi", "Passages réguliers et compte rendu écrit pour vos contrôles.")],
  [("Intervenez-vous pendant les horaires de vente ?", "Je m'adapte à vos horaires pour ne pas gêner les clients.")]),
 ("traiteur", "traiteur", "Dératisation Traiteur à Laval (53) | Proxinuisibles",
  "Dératisation et désinsectisation pour traiteurs à Laval : laboratoires, stockage, livraisons. Contrat annuel, devis gratuit.",
  "Laboratoire, stockage de matières premières, livraisons : un traiteur est exposé aux rongeurs et aux insectes. Je mets en place une protection discrète et durable.",
  [("Les zones à contrôler", "Laboratoire, réserves, chambres froides, locaux de stockage du matériel et abords."),
   ("Traiteurs et événements", "J'adapte les passages à votre activité, y compris en période de forte saison."),
   ("Suivi", "Contrat annuel ou interventions ponctuelles, avec compte rendu écrit.")],
  [("Puis-je commencer par une seule intervention ?", "Oui, vous pouvez passer ensuite à un contrat de suivi si vous le souhaitez.")]),
 ("cuisine-collective", "cuisine collective", "Dératisation Cuisine Collective à Laval | Proxinuisibles",
  "Dératisation et désinsectisation pour cantines, restaurants d'entreprise et cuisines collectives à Laval. Suivi et devis gratuit.",
  "Cantines, restaurants d'entreprise, établissements de santé : les volumes sont importants et les règles d'hygiène strictes. Je mets en place un suivi régulier et documenté.",
  [("Un suivi régulier", "Plan de passages, points de contrôle et compte rendu écrit pour vos audits et contrôles."),
   ("Zones sensibles", "Réserves, plonge, locaux poubelles, quais de livraison et abords extérieurs."),
   ("Rongeurs et insectes", "Je traite rongeurs, cafards, mouches et fourmis avec des produits adaptés aux locaux alimentaires.")],
  [("Pouvez-vous intervenir sur plusieurs sites ?", "Oui, contactez-moi pour étudier votre organisation et vos sites.")]),
]
for slug, nom, title, meta, lead, secs, faq in METIERS:
    add("/deratisation-%s-laval/" % slug, h1="Dératisation %s à Laval" % nom, title=title, meta=meta, lead=lead, secs=secs, faq=faq,
        links=[("Voir aussi", [("Professionnels", "/professionnels/"), ("Contrat annuel", "/contrat-annuel-deratisation/"), ("Désinsectisation", "/desinsectisation/"), ("Dératisation à Laval", "/deratisation-laval/")])], kind="metier")
add("/contrat-annuel-deratisation/", h1="Contrat annuel de dératisation pour professionnels",
    title="Contrat Annuel Dératisation Pro | Proxinuisibles",
    meta="Contrat annuel de dératisation pour restaurants, commerces et entreprises en Mayenne et Ille-et-Vilaine. Passages réguliers et suivi.",
    lead="Un contrat annuel vous évite les mauvaises surprises : je passe régulièrement, je surveille les points sensibles et j'interviens dès qu'un signe apparaît.",
    secs=[("Ce que comprend le contrat", "- Diagnostic initial du site\n- Passages réguliers de contrôle\n- Intervention en cas de constat de nuisibles\n- Compte rendu écrit à conserver"),
          ("Pour qui", "Restaurants, boulangeries, traiteurs, cuisines collectives, commerces, entrepôts et entreprises."),
          ("Comment démarrer", "Appelez-moi ou écrivez-moi : je visite votre site et je vous propose un devis adapté au nombre de passages dont vous avez besoin.")],
    faq=[("Puis-je résilier le contrat ?", "Les conditions sont précisées dans le contrat remis avec le devis.")],
    links=[("Voir aussi", [("Professionnels", "/professionnels/"), ("Restaurant", "/deratisation-restaurant-laval/"), ("Boulangerie", "/deratisation-boulangerie-laval/")])], kind="cible")

# ---------- VILLES ----------
CITIES = [
 ("laval", "Laval", "53", "Laval, avec son centre ancien et ses quartiers le long de la Mayenne, offre aux rongeurs de nombreux abris : caves, vides sanitaires, berges et réseaux souterrains.",
  "Rats près des berges, souris dans les appartements anciens, rongeurs dans les commerces du centre.", ["saint-berthevin", "mayenne", "ernee", "vitre"]),
 ("saint-berthevin", "Saint-Berthevin", "53", "Commune résidentielle voisine de Laval, Saint-Berthevin mêle lotissements, jardins et zones d'activités. Les rongeurs profitent des composteurs, des abris de jardin et des bâtiments commerciaux.",
  "Rats attirés par les composteurs et les poulaillers, souris dans les garages et les combles, rongeurs dans les zones d'activités.", ["laval", "vitre", "mayenne"]),
 ("vitre", "Vitré", "35", "Vitré réunit un centre historique, des commerces, des entreprises agroalimentaires et une campagne d'élevage toute proche. Rongeurs et insectes y trouvent de quoi se nourrir toute l'année.",
  "Souris dans les maisons anciennes du centre, rats autour des bâtiments d'élevage, nuisibles dans les commerces de bouche et les locaux d'entreprise.", ["saint-berthevin", "chateaubourg", "fougeres", "laval"]),
 ("ernee", "Ernée", "53", "Ernée est une petite ville entourée de campagne, entre Laval et Fougères. Fermes, hangars et granges y côtoient les maisons du bourg, et les rongeurs passent facilement de l'un à l'autre.",
  "Rats dans les bâtiments agricoles, souris dans les granges et les maisons de campagne, rongeurs dans les commerces du bourg.", ["laval", "mayenne", "fougeres"]),
 ("mayenne", "Mayenne", "53", "Traversée par la rivière qui lui donne son nom, Mayenne compte de nombreuses berges, des quais et un centre ancien en pente. Ce sont des terrains favorables aux rats.",
  "Rats près de l'eau et des quais, souris dans les vieux immeubles, rongeurs dans les caves des commerces.", ["ernee", "laval", "fougeres"]),
 ("fougeres", "Fougères", "35", "Fougères mêle quartiers anciens, centre commerçant et campagne alentour. Les rongeurs s'installent dans les caves et les murs des vieux bâtiments comme dans les fermes du Pays de Fougères.",
  "Souris dans les maisons anciennes, rats dans les exploitations agricoles, rongeurs dans les restaurants et les commerces du centre.", ["ernee", "vitre", "mayenne"]),
 ("chateaubourg", "Châteaubourg", "35", "Située entre Vitré et Rennes, Châteaubourg se développe avec des lotissements, des zones d'activités et des entreprises. Les travaux et terrassements dérangent souvent les rongeurs, qui se réfugient alors dans les habitations.",
  "Rongeurs délogés par des travaux, souris dans les pavillons récents, nuisibles dans les entrepôts et locaux d'entreprise.", ["vitre", "cesson-sevigne", "rennes"]),
 ("cesson-sevigne", "Cesson-Sévigné", "35", "Aux portes de Rennes, Cesson-Sévigné réunit quartiers résidentiels, pôles d'entreprises et commerces. Les entreprises et les restaurants y ont besoin d'un suivi régulier pour rester conformes aux règles d'hygiène.",
  "Rongeurs dans les locaux d'entreprise, souris dans les restaurants, nuisibles dans les résidences gérées par un syndic.", ["chateaubourg", "rennes", "vitre"]),
 ("rennes", "Rennes", "35", "À Rennes, la densité des immeubles, des restaurants et des caves favorise les rats et les souris, mais aussi les cafards et les punaises de lit.",
  "Rats dans les cours et les locaux poubelles, souris dans les restaurants, punaises de lit en logement et en location, nuisibles dans les copropriétés.", ["cesson-sevigne", "chateaubourg", "vitre"]),
]
CN = {c[0]: c[1] for c in CITIES}
for slug, nom, dep, local, cas, voisins in CITIES:
    add("/deratisation-%s/" % slug,
        h1="Dératisation à %s (%s) : rats et souris" % (nom, dep),
        title="Dératisation à %s (%s) | Proxinuisibles" % (nom, dep),
        meta="Dératisation à %s et alentours : rats, souris, rongeurs. Particuliers, agriculteurs et professionnels. Diagnostic et devis gratuits." % nom,
        lead="Rats, souris ou autres rongeurs à %s ? J'interviens chez les particuliers, les agriculteurs et les professionnels, avec un diagnostic et un devis gratuits." % nom,
        secs=[("Pourquoi des rongeurs à %s" % nom, local),
              ("Les cas classiques à %s" % nom, cas),
              ("Mon intervention", "Je repère d'où viennent les rongeurs, je traite avec un matériel sécurisé, je ferme les accès quand c'est possible et je repasse vérifier que tout est réglé.")],
        faq=[("Intervenez-vous rapidement à %s ?" % nom, "Oui, j'interviens à %s et dans les communes voisines. Appelez-moi au %s, nous fixons un créneau." % (nom, TEL_D)),
             ("Combien coûte une dératisation à %s ?" % nom, "Le prix dépend de l'ampleur de l'infestation et des lieux. Le diagnostic et le devis sont gratuits.")],
        links=[("Autres services à %s" % nom, [("Frelons et guêpes", "/frelons-guepes/"), ("Frelon asiatique", "/frelon-asiatique/"), ("Désinsectisation", "/desinsectisation/"), ("Blattes et cafards", "/blattes-cafards/"), ("Fourmis", "/fourmis/"), ("Mouches", "/mouches/"), ("Puces", "/puces/"), ("Punaises de lit", "/punaises-de-lit/"), ("Chenilles processionnaires", "/chenilles-processionnaires/"), ("Taupier", "/taupier/"), ("Dépigeonnage", "/depigeonnage/"), ("Piégeur agréé", "/piegeur-agree/")]),
               ("Communes voisines", [("Dératisation à %s" % CN[v], "/deratisation-%s/" % v) for v in voisins])],
        kind="ville")

# ---------- ACCUEIL ----------
home_pre = ("<section class='sec'><div class='wrap'><h2>Ce que je traite</h2><div class='grid'>" +
            "".join("<a class='card' href='/%s/'><h3>%s</h3><p>%s</p></a>" % (s[0], s[1], T(s[5].split(".")[0] + ".")) for s in SV) +
            "</div></div></section>" +
            "<section class='sec alt'><div class='wrap'><h2>Où j'interviens</h2><p>De Laval à Rennes, en passant par Vitré et Fougères. Choisissez votre commune.</p><ul class='chips'>" +
            "".join("<li><a href='/deratisation-%s/'>%s</a></li>" % (c[0], c[1]) for c in CITIES) + "</ul></div></section>")
add("/", h1="Dératisation, désinsectisation et nids de frelons à Laval, Vitré, et dans toute la Mayenne et l'Ille-et-Vilaine",
    title="Dératisation, Désinsectisation, Frelons | Proxinuisibles",
    meta="Anti-nuisibles en Mayenne et Ille-et-Vilaine : rats, insectes, frelons, guêpes, punaises de lit. Intervention rapide, devis gratuit. Appelez-nous.",
    lead="Rats, souris, insectes, frelons, guêpes, punaises de lit : j'interviens chez les particuliers, les agriculteurs et les professionnels en Mayenne et en Ille-et-Vilaine. Devis gratuit.",
    pre=home_pre,
    secs=[("Particuliers, agriculteurs et professionnels", "Une infestation ne prévient pas. Je propose des interventions ponctuelles et des contrats de suivi annuels pour les restaurants, boulangeries, traiteurs, cuisines collectives, agences immobilières et syndics."),
          ],
    links=[("Pour qui", [("Particuliers", "/particuliers/"), ("Agriculteurs", "/agriculteurs/"), ("Professionnels", "/professionnels/"), ("Agences et syndics", "/agences-syndics/"), ("Contrat annuel", "/contrat-annuel-deratisation/")])],
    faq=[("Combien coûte la destruction d'un nid de frelons ?", "Le prix dépend de la hauteur et de l'accessibilité du nid. Appelez ou envoyez une photo, je vous donne un devis gratuit."),
         ("Quelles communes couvrez-vous ?", "Toute la Mayenne et l'Ille-et-Vilaine, de Laval à Rennes. Si votre commune n'est pas listée, appelez-moi."),
         ("Intervenez-vous en urgence ?", "Appelez-moi et nous convenons d'un créneau le plus tôt possible selon la situation.")], kind="home")

# ---------- CONTACT / MENTIONS ----------
add("/contact/", h1="Devis et contact", title="Devis et Contact Anti-Nuisibles Laval | Proxinuisibles",
    meta="Demandez votre devis gratuit : rats, frelons, punaises, pigeons. Réponse rapide en Mayenne et en Ille-et-Vilaine, de Laval à Rennes.",
    lead="Remplissez le formulaire, appelez-moi ou écrivez-moi : plus vous me donnez de détails, plus mon devis gratuit est précis.",
    secs=[("Mes horaires", "- Du lundi au vendredi : 8h - 21h\n- Samedi et dimanche : 9h - 18h\nJe réponds moi-même au téléphone. Si je suis en intervention, laissez un message : je vous rappelle."),
          ("Mon délai d'intervention", "Je m'organise pour intervenir sous 24 à 48 heures. Pour les urgences, j'essaie de venir plus vite : nid de frelons à hauteur d'homme, près d'une entrée, d'une école ou d'une personne allergique, rongeurs dans un local alimentaire. Dites-le-moi dès votre appel."),
          ("Tarifs, déplacement et paiement", "Le devis est gratuit et le déplacement est compris dans le tarif : vous ne payez pas de frais de déplacement en plus.\nChaque situation étant différente, j'établis le tarif au cas par cas, après avoir vu le lieu ou la photo que vous m'envoyez. Vous connaissez le prix avant que je commence.\nJe prends tous les moyens de paiement : carte bancaire, espèces, chèque et virement."),
          ("Me joindre", "- Téléphone : <a href='tel:%s'>%s</a>\n- E-mail : <a href='mailto:%s'>%s</a>\n- Zone : Mayenne et Ille-et-Vilaine, de Laval à Rennes" % (TEL, TEL_D, MAIL, MAIL)),
          ("Ce qui m'aide pour votre devis", "- Votre commune\n- Le nuisible concerné (rats, frelons, punaises...)\n- Une photo si possible\n- Particulier, agriculteur ou professionnel"),
          ("Écrire directement", "<a class='btn' href='mailto:%s?subject=Demande%%20de%%20devis&body=Commune%%20%%3A%%0ANuisible%%20%%3A%%0ADescription%%20%%3A' >Préparer mon e-mail de devis</a>" % MAIL)],
    faq=[], kind="contact")
add("/mentions-legales/", h1="Mentions légales", title="Mentions légales | Proxinuisibles", meta="Mentions légales du site Proxinuisibles.", lead="Informations légales du site.",
    secs=[("Éditeur du site", "Proxinuisibles\nSIRET : 98424277600016\nResponsable de publication : Gwendal Renault\nAdresse : 7 rue des Lavandières, 53410 Port-Brillet\nTéléphone : %s\nE-mail : %s" % (TEL_D, MAIL)),
          ("Hébergeur", "[À compléter : nom, adresse et site de l'hébergeur choisi]"),
          ("Assurance professionnelle", "[À compléter : nom de l'assureur et zone de couverture]"),
          ("Données personnelles", "Les informations transmises par e-mail ou par téléphone servent uniquement à répondre à votre demande de devis. Elles ne sont pas revendues. Pour exercer vos droits d'accès ou de suppression, écrivez à %s." % MAIL)],
    faq=[], kind="legal")


add("/qui-suis-je/", h1="Qui suis-je ? Gwendal, spécialiste anti-nuisibles en Mayenne",
    title="Qui suis-je ? | Anti-Nuisibles Mayenne | Proxinuisibles",
    meta="Gwendal, à la tête de Proxinuisibles : dératisation, nids de frelons et désinsectisation en Mayenne et Ille-et-Vilaine.",
    lead="Je dirige Proxinuisibles depuis la Mayenne et j'interviens chez les particuliers, les agriculteurs et les professionnels.",
    secs=[("Moi, c'est Gwendal", "Je viens moi-même comprendre votre problème de nuisibles, vous expliquer mon intervention et assurer le suivi. Vous avez un interlocuteur unique, du premier appel à la fin de la prestation."),
          ("Ma façon de travailler", "- J'observe : je cherche les indices et les zones d'activité\n- Je traite : je choisis le protocole adapté aux lieux\n- Je contrôle : je vérifie le résultat et je précise les conditions de suivi"),
          ("Mes qualifications", "[À compléter : vos certifications et formations, par exemple Certibiocide si vous l'avez]")],
    faq=[], kind="info")
add("/zones-intervention/", h1="Zones d'intervention en Mayenne et Ille-et-Vilaine",
    title="Zones d'intervention Mayenne et 35 | Proxinuisibles",
    meta="Proxinuisibles intervient de Laval à Rennes : Vitré, Fougères, Ernée, Mayenne, Saint-Berthevin, Châteaubourg, Cesson-Sévigné.",
    lead="J'interviens dans toute la Mayenne et en Ille-et-Vilaine, de Laval à Rennes.",
    secs=[("Choisissez votre commune", "Chaque commune a sa page dédiée avec les cas les plus fréquents du secteur."),
          ("Votre commune n'est pas dans la liste ?", "Appelez-moi : je me déplace aussi dans les communes voisines selon mes disponibilités.")],
    links=[("Les communes", [("Dératisation " + c[1], "/deratisation-%s/" % c[0]) for c in CITIES])],
    faq=[], kind="info")
# Carte de la zone d'intervention (Leaflet + OpenStreetMap, fichiers servis par le site)
P["/zones-intervention/"]["pre"] = ("<section class='sec carte-sec'><div class='wrap'><span class='label'>Ma zone d'intervention</span>"
    "<h2>J'interviens dans toute la zone colorée</h2>"
    "<p>Toute la Mayenne et toute l'Ille-et-Vilaine, de Laval à Rennes, au départ de Port-Brillet. "
    "Votre commune n'a pas de page sur le site ? Je viens quand même : appelez-moi.</p>"
    "<div id='carte' class='carte' role='img' aria-label=\"Carte de la zone d'intervention : la Mayenne et l'Ille-et-Vilaine en entier\"></div>"
    "<p class='carte-note'>Fond de carte © <a href='https://www.openstreetmap.org/copyright' target='_blank' rel='noopener'>contributeurs OpenStreetMap</a>.</p>"
    "</div></section>")
P["/zones-intervention/"]["head"] = "<link rel='stylesheet' href='/leaflet/leaflet.css'>"
P["/zones-intervention/"]["js"] = "<script src='/leaflet/leaflet.js'></script><script src='/carte.js'></script>"

def clink(label):
    return "<a href='" + CERT_URL + "' target='_blank' rel='noopener'>" + label + "</a>"

add("/qui-suis-je/", h1="Qui suis-je ? Gwendal, spécialiste anti-nuisibles en Mayenne",
    title="Qui suis-je ? | Anti-Nuisibles Mayenne | Proxinuisibles",
    meta="Gwendal, à la tête de Proxinuisibles : dératisation, nids de frelons et désinsectisation en Mayenne et Ille-et-Vilaine. Certibiocide.",
    lead="Je dirige Proxinuisibles depuis la Mayenne et j'interviens chez les particuliers, les agriculteurs et les professionnels.",
    secs=[("Moi, c'est Gwendal", "J'exerce dans la lutte contre les nuisibles depuis 2016 et je suis installé à mon compte depuis 2024, basé à Port-Brillet, entre Vitré et Laval. Je travaille seul, sans intermédiaire : de votre premier appel jusqu'à l'intervention chez vous, c'est toujours moi que vous avez au bout du fil et sur le terrain.\nCette relation directe me permet de comprendre rapidement votre situation et de proposer une solution efficace, durable et adaptée à votre environnement. J'interviens sur le bassin lavallois, sur Vitré et sur le bassin rennais, pour les particuliers comme pour les professionnels."),
          ("Ma façon de travailler", "- J'observe : je cherche les indices et les zones d'activité\n- Je traite : je choisis le protocole adapté aux lieux\n- Je contrôle : je vérifie le résultat et je précise les conditions de suivi"),
          ("Mon certificat Certibiocide", "Mon certificat individuel Certibiocide porte le numéro " + CERT_NUM + ", au nom de Renault. Ce certificat est obligatoire depuis le 1er juillet 2015.\nVous pouvez en vérifier la validité sur le site officiel, en saisissant le numéro " + CERT_NUM + " et le nom Renault : " + clink("Vérifier mon certificat") + ".")],
    faq=[], kind="info")

MEL = "proxinuisibles53@gmail.com"
add("/mentions-legales/", h1="Mentions légales", title="Mentions légales | Proxinuisibles",
    meta="Mentions légales, médiateur de la consommation et données personnelles du site Proxinuisibles, entreprise de désinsectisation et dératisation.",
    lead="Entreprise de désinsectisation et dératisation en Mayenne et Ille-et-Vilaine. Dernière mise à jour : 4 novembre 2026.",
    secs=[("Éditeur et propriétaire du site", "Gwendal Renault, entreprise individuelle, exerçant sous le nom commercial Proxi Nuisibles\n7 rue des Lavandières, 53410 Port-Brillet\nTéléphone : 06 64 57 66 55\nE-mail : " + MEL + "\nSIRET : 984 242 776 00016\nAssurance multirisque professionnelle : MAAF Assurances, contrat n° 153027432 N 001, garantie France métropolitaine\nCertificat Certibiocide n° " + CERT_NUM + " (nom : Renault) - " + clink("vérifier la validité du certificat") + "\nResponsable de publication et webmaster : Gwendal Renault"),
          ("Hébergeur", "Le site est hébergé par Cloudflare, Inc., 101 Townsend Street, San Francisco, CA 94107, États-Unis (<a href='https://www.cloudflare.com' target='_blank' rel='noopener'>cloudflare.com</a>).\nLe nom de domaine est enregistré auprès de OVH SAS, 2 rue Kellermann, 59100 Roubaix, France."),
          ("Médiateur de la consommation", "Depuis le 1er janvier 2016, en tant que professionnel, je dois permettre à tout consommateur l'accès à un dispositif de médiation de la consommation en vue de la résolution amiable de tout éventuel litige (article L.612-1 du code de la consommation).\nJ'ai choisi un médiateur inscrit sur la liste prévue à l'article L.615-1 du code de la consommation : Société de la Médiation Professionnelle - Médiateur de la consommation (<a href='https://mediateurconsommationsmp.fr' target='_blank' rel='noopener'>mediateurconsommationsmp.fr</a>), 24 rue Albert de Mun, 33000 Bordeaux."),
          ("1. Conditions générales d'utilisation du site", "Le site constitue une œuvre de l'esprit protégée par le code de la propriété intellectuelle et les réglementations internationales applicables. Le client ne peut en aucune manière réutiliser, céder ou exploiter pour son propre compte tout ou partie des éléments ou travaux du site.\nL'utilisation du site www.proxinuisibles.fr implique l'acceptation pleine et entière des présentes conditions générales d'utilisation. Elles peuvent être modifiées ou complétées à tout moment : les utilisateurs sont invités à les consulter régulièrement.\nLe site est normalement accessible à tout moment. Une interruption pour maintenance technique peut être décidée par Gwendal Renault, qui s'efforcera d'en informer préalablement les utilisateurs. Les mentions légales peuvent également être modifiées à tout moment et s'imposent à l'utilisateur."),
          ("2. Description des services fournis", "Le site a pour objet de fournir une information sur l'ensemble des activités de l'entreprise. Gwendal Renault s'efforce de fournir des informations aussi précises que possible, mais ne peut être tenu responsable des oublis, des inexactitudes et des carences de mise à jour, qu'elles soient de son fait ou du fait de tiers partenaires.\nToutes les informations sont données à titre indicatif, ne sont pas exhaustives et sont susceptibles d'évoluer."),
          ("3. Limitations contractuelles sur les données techniques", "Le site utilise la technologie JavaScript. Il ne pourra être tenu responsable de dommages matériels liés à son utilisation. L'utilisateur s'engage à y accéder avec un matériel récent, exempt de virus, et un navigateur à jour."),
          ("4. Propriété intellectuelle et contrefaçons", "Gwendal Renault est propriétaire des droits de propriété intellectuelle et détient les droits d'usage sur tous les éléments du site : textes, images, graphismes, logos, icônes. Toute reproduction, représentation, modification, publication ou adaptation de tout ou partie de ces éléments, quel que soit le moyen ou le procédé, est interdite sans autorisation écrite préalable de Gwendal Renault.\nToute exploitation non autorisée du site ou de l'un de ses éléments sera considérée comme une contrefaçon et poursuivie conformément aux articles L.335-2 et suivants du code de la propriété intellectuelle."),
          ("5. Limitations de responsabilité", "Proxinuisibles agit en tant qu'éditeur du site et est responsable de la qualité et de la véracité du contenu qu'il publie.\nGwendal Renault ne pourra être tenu responsable des dommages directs et indirects causés au matériel de l'utilisateur lors de l'accès au site (matériel non conforme, bug ou incompatibilité), ni des dommages indirects, tels qu'une perte de marché ou une perte d'une chance, consécutifs à l'utilisation du site."),
          ("6. Gestion des données personnelles", "Le client est informé des réglementations relatives à la communication marketing, de la loi du 21 juin 2004 pour la confiance dans l'économie numérique, de la loi Informatique et Libertés du 6 janvier 1978 modifiée et du règlement général sur la protection des données (RGPD, règlement (UE) 2016/679).\nResponsable du traitement des données personnelles : Gwendal Renault, Proxi Nuisibles, 7 rue des Lavandières, 53410 Port-Brillet, " + MEL + ".\nDonnées collectées par le formulaire de contact : prénom, nom, adresse e-mail, numéro de téléphone et contenu du message. Elles servent uniquement à répondre à votre demande de devis ou de renseignement. La base légale est votre demande (mesures précontractuelles) et, à défaut, mon intérêt légitime à répondre aux sollicitations.\nDurée de conservation : le temps nécessaire au traitement de votre demande, puis au maximum 3 ans à compter du dernier contact si aucune prestation n'est conclue. En cas de prestation, les données de facturation sont conservées selon les durées légales.\nDestinataires : moi-même et le prestataire technique chargé de transmettre le formulaire par e-mail (Web3Forms). La carte de la page « Zones d'intervention » affiche des fonds de carte OpenStreetMap : votre navigateur les télécharge depuis les serveurs d'OpenStreetMap, qui reçoivent à cette occasion votre adresse IP. Aucun cookie n'est déposé par cette carte. Les données ne sont ni vendues ni cédées à des tiers à des fins commerciales.\nComme tout site web, l'hébergeur enregistre dans ses journaux techniques des données de connexion (adresse IP, date et heure, navigateur) à des fins de sécurité et de bon fonctionnement."),
          ("7. Vos droits sur vos données", "Conformément à la réglementation européenne, vous disposez des droits suivants :\n- accès (article 15 du RGPD) et rectification (article 16)\n- effacement (article 17), lorsque les données sont inexactes, incomplètes, équivoques ou périmées, ou que leur collecte, utilisation, communication ou conservation est interdite\n- retrait de votre consentement à tout moment (article 7.3)\n- limitation du traitement (article 18)\n- opposition au traitement (article 21)\n- portabilité des données que vous avez fournies (article 20)\n- définition du sort de vos données après votre décès\nPour exercer ces droits, écrivez à Proxi Nuisibles, 7 rue des Lavandières, 53410 Port-Brillet, ou à " + MEL + ", en indiquant les données concernées et en joignant une copie de pièce d'identité. Les demandes de suppression restent soumises aux obligations légales de conservation et d'archivage.\nVous pouvez également déposer une réclamation auprès de la CNIL (<a href='https://www.cnil.fr/fr/plaintes' target='_blank' rel='noopener'>cnil.fr/fr/plaintes</a>)."),
          ("8. Transferts et sécurité des données", "Certains prestataires techniques (hébergeur, service d'envoi du formulaire) peuvent traiter des données en dehors de l'Union européenne, notamment aux États-Unis. Ces transferts sont encadrés par les garanties prévues par le RGPD (par exemple les clauses contractuelles types de la Commission européenne ou le cadre de protection des données UE-États-Unis).\nJe prends les précautions nécessaires pour préserver la sécurité des informations et les protéger contre toute communication à des personnes non autorisées. En cas d'incident touchant leur intégrité ou leur confidentialité, vous serez informé dans les meilleurs délais des mesures prises. Aucune donnée sensible n'est collectée par ce site."),
          ("9. Liens hypertextes et cookies", "Le site contient des liens vers d'autres sites (par exemple ma fiche Google). Je ne peux pas vérifier leur contenu et n'assume aucune responsabilité à ce titre.\nUn cookie est un petit fichier enregistré dans votre terminal (ordinateur, smartphone) lors de la visite d'un site : il contient par exemple le fournisseur d'accès, le système d'exploitation, la date et l'heure d'accès. Ce site n'utilise aucun cookie de suivi, de mesure d'audience ou de publicité, et ne dépose aucun cookie sur votre terminal. Si vous cliquez sur un lien vers un site tiers (fiche Google, site du groupement Experts Guêpes et Frelons), celui-ci peut déposer ses propres cookies, selon sa propre politique.\nVous pouvez configurer votre navigateur pour accepter ou refuser les cookies, ou pour être prévenu avant l'enregistrement d'un cookie ; la procédure est décrite dans le menu d'aide de chaque navigateur. Un refus peut limiter certaines fonctionnalités du site."),
          ("10. Droit applicable et juridiction", "Tout litige relatif à l'utilisation du site est soumis au droit français. En dehors des cas où la loi ne le permet pas, les tribunaux compétents de Laval ont compétence exclusive.")],
    faq=[], kind="legal")

_seen, _faq = set(), []
for _p in list(P):
    for q, a in P[_p]["faq"]:
        if q not in _seen and _p not in ("/contact/", "/mentions-legales/") and "à " + "" not in q[:0]:
            _seen.add(q); _faq.append((q, a))
_faq = [f for f in _faq if not any(c[1] in f[0] for c in CITIES)]
add("/questions-frequentes/", h1="Questions fréquentes sur les nuisibles",
    title="Questions Fréquentes Nuisibles | Proxinuisibles",
    meta="Rats, frelons, punaises de lit, chenilles, taupes, pigeons : les réponses aux questions les plus fréquentes. Devis gratuit.",
    lead="Les questions que l'on me pose le plus souvent. Une autre question ? Appelez-moi.",
    secs=[], faq=_faq, kind="info")

exec(open("/home/claude/communes_data.py", encoding="utf-8").read())
exec(open("/home/claude/communes20km.py", encoding="utf-8").read())
exec(open("/home/claude/communes40_bouche.py", encoding="utf-8").read())
exec(open("/home/claude/extras600.py", encoding="utf-8").read())
exec(open("/home/claude/debarras.py", encoding="utf-8").read())
exec(open("/home/claude/punaises_villes.py", encoding="utf-8").read())
exec(open("/home/claude/frelons_villes.py", encoding="utf-8").read())
exec(open("/home/claude/services_villes.py", encoding="utf-8").read())
exec(open("/home/claude/mentions.py", encoding="utf-8").read())
exec(open("/home/claude/seo_deratiseur.py", encoding="utf-8").read())
exec(open("/home/claude/laval.py", encoding="utf-8").read())
exec(open("/home/claude/chenilles.py", encoding="utf-8").read())

# ---------- RENDU ----------
NAV = [("Dératisation", "/deratisation/"), ("Frelons et guêpes", "/frelons-guepes/"), ("Désinsectisation", "/desinsectisation/"), ("Professionnels", "/professionnels/"), ("Devis et contact", "/contact/")]

def body(txt):
    out, ul = [], []
    for line in T(txt).split("\n"):
        if line.startswith("- "):
            ul.append("<li>%s</li>" % line[2:])
        else:
            if ul:
                out.append("<ul>%s</ul>" % "".join(ul)); ul = []
            out.append("<p>%s</p>" % line)
    if ul:
        out.append("<ul>%s</ul>" % "".join(ul))
    return "".join(out)

def foot_col(title, items):
    return "<div><h3>%s</h3><ul>%s</ul></div>" % (title, "".join("<li><a href='%s'>%s</a></li>" % (u, l) for l, u in items))

FOOT = ("<footer class='foot'><div class='wrap'><div class='fgrid'>" +
        foot_col("Services", [(s[1], "/%s/" % s[0]) for s in SV] + [("Débarras", "/debarras/")]) +
        foot_col("Zones", [("Dératisation " + c[1], "/deratisation-%s/" % c[0]) for c in CITIES] + [("Dératisation " + f[1], "/deratisation-%s/" % f[0]) for f in FICHES if f[0] in ("saint-pierre-la-cour", "loiron-ruille", "le-genest-saint-isle", "cosse-le-vivien", "etrelles", "olivet")] + [("Toutes les communes", "/zones-intervention/")]) +
        foot_col("Professionnels", [("Restaurant", "/deratisation-restaurant-laval/"), ("Boulangerie", "/deratisation-boulangerie-laval/"), ("Boucherie", "/deratisation-boucherie-laval/"), ("Traiteur", "/deratisation-traiteur-laval/"), ("Cuisine collective", "/deratisation-cuisine-collective-laval/"), ("Contrat annuel", "/contrat-annuel-deratisation/"), ("Contrats métiers de bouche", "/contrats-metiers-de-bouche/"), ("Agences et syndics", "/agences-syndics/")]) +
        foot_col("Proxinuisibles", [("Zones d'intervention", "/zones-intervention/"), ("Avis clients", "/avis/"), ("Questions fréquentes", "/questions-frequentes/"), ("Particuliers", "/particuliers/"), ("Agriculteurs", "/agriculteurs/"), ("Devis gratuit", "/contact/"), ("Qui suis-je ?", "/qui-suis-je/"), ("Mentions légales", "/mentions-legales/")]) +
        "</div><p class='small'>© 2026 Proxinuisibles - SIRET 98424277600016 - Port-Brillet, Mayenne - <a href='tel:%s'>%s</a> - Certibiocide n° 059860 (<a href='https://certibiocide.din.developpement-durable.gouv.fr/verifCertificat' target='_blank' rel='noopener'>vérifier</a>)</p></div></footer>" % (TEL, TEL_D))

ASST_HTML = ("<div class='asst'><button type='button' class='asst-btn' aria-expanded='false' aria-label='Poser une question ou me contacter'>"
             "<span class='asst-bulle'>Une question ?<br><b>Je vous oriente !</b></span><img src='/logo-petit.webp' alt='' width='95' height='160'></button>"
             "<div class='asst-panel' role='dialog' aria-label='Poser une question' hidden>"
             "<div class='asst-head'><strong>Une question ? Je vous oriente.</strong><button type='button' class='asst-close' aria-label='Fermer'>\u00d7</button></div>"
             "<p class='asst-msg'>Dites-moi ce qui se passe : je vous envoie vers la bonne page du site.</p>"
             "<form class='asst-form'><input class='asst-q' type='text' maxlength='120' placeholder='Ex. : nid de guêpes, rats à Laval...' aria-label='Votre demande'><button class='btn' type='submit'>Trouver</button></form>"
             "<div class='asst-out' aria-live='polite'></div>"
             "<p class='asst-sub'>Je suis :</p><ul class='asst-quick'><li><a href='/particuliers/'>Particulier</a></li><li><a href='/agriculteurs/'>Agriculteur ou éleveur</a></li>"
             "<li><a href='/contrats-metiers-de-bouche/'>Commerce de bouche</a></li><li><a href='/professionnels/'>Syndic, professionnel ou collectivité</a></li></ul>"
             "<div class='asst-act'><a class='btn' href='tel:%s'>\u260e Appeler</a><a class='btn btn-ghost' href='/contact/'>Devis et contact</a></div></div></div>" % TEL)
TOP_HTML = ("<button type='button' class='toplink' id='toplink' aria-label='Revenir en haut de la page' title='Revenir en haut' hidden>"
            "<svg class='tl-ring' viewBox='0 0 44 44' aria-hidden='true'>"
            "<circle class='tl-bg' cx='22' cy='22' r='20'/><circle class='tl-pg' cx='22' cy='22' r='20'/></svg>"
            "<svg class='tl-arrow' viewBox='0 0 24 24' aria-hidden='true'><path d='M12 6.5l6.5 7.2h-4.1v5.8h-4.8v-5.8H5.5z'/></svg>"
            "</button>")
FOOT = FOOT + ASST_HTML + TOP_HTML
AVIS_MINI = ("<section class='sec alt' id='avis-mini' hidden><div class='wrap'><span class='label'>La parole à mes clients</span>"
             "<h2>Ce que disent mes clients sur Google</h2><div id='avis-widget-mini'></div>"
             "<p><a class='btn' href='/avis/'>Lire les avis de mes clients \u2197</a></p></div></section>")
AVIS = ("<section class='sec alt' id='avis' hidden><div class='wrap'><span class='label'>En direct de ma fiche</span><h2>Ma note aujourd'hui</h2><div id='avis-widget'></div><p><a id='avis-fiche' class='btn' href='#' hidden>Voir tous mes avis sur Google</a></p>"
        "<p><a id='avis-lien' class='btn btn-ghost' href='#' hidden>Laisser un avis sur Google</a></p></div></section>")

add("/avis/", h1="Les avis de mes clients sur Google",
    title="Avis clients | Proxinuisibles",
    meta="Les avis laissés par mes clients sur ma fiche Google, affichés tels quels : note, nombre d'avis et commentaires. Mayenne et Ille-et-Vilaine.",
    lead="Mes clients laissent leurs avis sur ma fiche Google. Ils sont repris ici tels quels, sans tri de ma part.",
    pre=AVIS,
    secs=[("Pourquoi mes avis sont sur Google et pas ailleurs",
           "Un avis déposé sur Google est rattaché à un compte Google, visible publiquement, et je ne peux ni le supprimer ni le modifier. C'est ce qui lui donne sa valeur.\nLa note, le nombre d'avis et les commentaires affichés en haut de cette page sont lus directement sur ma fiche, une fois par jour. Je ne les saisis pas à la main : ce que vous voyez est ce que dit Google au moment où vous lisez.\nGoogle n'en laisse passer que cinq à la fois, et c'est lui qui choisit lesquels. Pour les lire tous, le bouton ci-dessus ouvre ma fiche."),
          ("Laisser un avis après une intervention",
           "Si je suis intervenu chez vous, un avis m'aide bien plus que n'importe quelle publicité : c'est souvent la première chose que regarde la personne qui hésite à appeler.\nQuelques mots suffisent. Dire ce pour quoi je suis venu, si le problème est réglé et comment ça s'est passé est plus utile qu'un long texte.\nEt si quelque chose ne va pas, appelez-moi avant d'écrire : je préfère régler le problème que lire qu'il existait."),
          ("Ce que je ne fais pas",
           "- Je n'achète pas d'avis et je n'en fais pas rédiger\n- Je ne propose aucune remise en échange d'un avis\n- Je ne masque pas les avis qui me déplaisent, je n'en ai pas le pouvoir\n- Je ne reprends ici aucun avis qui ne viendrait pas de ma fiche Google")],
    faq=[("Les avis affichés sur ce site sont-ils vérifiés ?",
          "Ils proviennent de ma fiche Google Business Profile, où chaque avis est rattaché à un compte Google. La note et le nombre affichés sont relus automatiquement sur cette fiche une fois par jour."),
         ("Puis-je laisser un avis si vous êtes intervenu il y a longtemps ?",
          "Oui, Google n'impose aucun délai. Un avis déposé plusieurs mois après l'intervention compte autant qu'un autre."),
         ("Je ne suis pas satisfait, que faire ?",
          "Appelez-moi au " + TEL_D + ". Si une intervention n'a pas donné le résultat attendu, je préfère revenir voir sur place plutôt que de laisser la situation en l'état.")],
    kind="info")

ICON_SVG = {
 "frelon-asiatique": '<ellipse cx="24" cy="30" rx="7" ry="11"/><path d="M24 22v18" stroke-width="0"/><circle cx="24" cy="15" r="4.5"/><path class="a" d="M20 11l-4-6M28 11l4-6"/><path d="M17 20C9 14 4 18 5 24c1 5 7 5 12 2M31 20c8-6 13-2 12 4-1 5-7 5-12 2"/><path d="M17 36l-6 5M31 36l6 5"/>',
 "mouches": '<ellipse cx="24" cy="29" rx="6" ry="9"/><circle cx="24" cy="16" r="5"/><circle class="a" cx="21" cy="15" r="1.6"/><circle class="a" cx="27" cy="15" r="1.6"/><path d="M18 22C10 18 4 22 6 28c2 5 9 3 12 0M30 22c8-4 14 0 12 6-2 5-9 3-12 0"/><path d="M20 37l-4 5M28 37l4 5"/>',
 "puces": '<ellipse cx="26" cy="24" rx="9" ry="7" transform="rotate(-20 26 24)"/><circle cx="16" cy="18" r="4"/><path class="a" d="M13 13l-3-5M18 12l1-6"/><path d="M20 30l-6 9M26 32l-3 10M32 30l6 9M33 24l8-3"/>',
 "blattes-cafards": '<ellipse cx="24" cy="28" rx="9" ry="13"/><path d="M24 15v26"/><circle cx="24" cy="12" r="3.5"/><path class="a" d="M21 9c-3-5-7-6-10-6M27 9c3-5 7-6 10-6"/><path d="M15 22l-8-3M15 29l-9 1M16 36l-7 5M33 22l8-3M33 29l9 1M32 36l7 5"/>',
 "fourmis": '<circle cx="10" cy="27" r="5"/><circle cx="23" cy="27" r="4"/><circle class="a" cx="35" cy="26" r="6"/><path d="M8 32l-3 8M22 31l-1 9M26 31l3 9M33 32l2 8M38 20l5-6M33 20l-2-7"/>',
 "deratisation": '<circle class="a" cx="12" cy="24" r="2"/><ellipse cx="26" cy="29" rx="14" ry="9"/><circle cx="31" cy="19" r="5"/><path d="M40 31c6 0 6 8 0 10"/><path d="M10 26l-5-2M10 30l-5 1"/>',
 "frelons-guepes": '<ellipse cx="24" cy="31" rx="6" ry="9"/><path class="a" d="M18 29h12M18 34h12"/><circle cx="24" cy="19" r="4"/><circle cx="24" cy="12" r="3"/><ellipse cx="13" cy="16" rx="8" ry="4" transform="rotate(-30 13 16)"/><ellipse cx="35" cy="16" rx="8" ry="4" transform="rotate(30 35 16)"/><path d="M22 10l-3-4M26 10l3-4M24 40v5"/>',
 "desinsectisation": '<ellipse cx="24" cy="28" rx="8" ry="12"/><circle cx="24" cy="13" r="4"/><path d="M22 10c-4-5-8-4-10-6M26 10c4-5 8-4 10-6"/><path class="a" d="M24 18v20"/><path d="M16 22l-8-4M16 28H7M17 34l-8 6M32 22l8-4M32 28h9M31 34l8 6"/>',
 "chenilles-processionnaires": '<circle cx="7" cy="34" r="5"/><circle cx="14" cy="30" r="5"/><circle cx="21" cy="29" r="5"/><circle cx="28" cy="30" r="5"/><circle cx="34" cy="32" r="5"/><circle class="a" cx="41" cy="29" r="5.5"/><path d="M40 23l-2-6M44 25l3-5"/><path d="M7 39v4M14 35v4M21 34v4M28 35v4M34 37v4"/>',
 "punaises-de-lit": '<path d="M5 12v28"/><path d="M5 31h38v9"/><rect x="9" y="23" width="10" height="6" rx="3"/><path d="M22 31v-6h17a4 4 0 0 1 4 4v2"/><ellipse class="a" cx="33" cy="12" rx="4.5" ry="3.5"/><path class="a" d="M29 10l-3-2M29 14l-3 2M37 10l3-2M37 14l3 2"/>',
 "taupier": '<path d="M4 41c4-12 14-16 20-16s16 4 20 16z"/><circle cx="24" cy="17" r="7"/><circle class="a" cx="24" cy="9" r="2.2"/><circle cx="21" cy="16" r=".8"/><circle cx="27" cy="16" r=".8"/><path d="M14 31l-3-3M34 31l3-3"/>',
 "depigeonnage": '<circle cx="34" cy="14" r="5"/><path class="a" d="M39 14l6 2-6 3"/><path d="M12 30c0-8 10-10 18-9 6 1 8 7 4 12-6 5-18 5-22-3z"/><path d="M12 30l-8 4 4-7"/><path d="M16 30c6-4 12-2 14 2"/><path d="M22 37v7M28 37v7"/><circle cx="35" cy="13" r=".8"/>',
 "piegeur-agree": '<rect x="4" y="18" width="34" height="22" rx="3"/><path d="M12 18v22M20 18v22M28 18v22"/><path d="M4 29h34"/><path d="M8 40v4M34 40v4"/><circle class="a" cx="39" cy="13" r="7"/><path class="a" d="M35.5 13l2.5 2.5 5-5"/>',
}
def ico(path):
    k = path.strip("/")
    if k not in ICON_SVG:
        return ""
    return "<span class='ico' aria-hidden='true'><svg viewBox='0 0 48 48' xmlns='http://www.w3.org/2000/svg'>%s</svg></span>" % ICON_SVG[k]

TAGS = {"deratisation": "Rongeurs", "frelons-guepes": "Insectes volants", "desinsectisation": "Autres insectes", "frelon-asiatique": "Espèce envahissante", "mouches": "Insectes volants", "puces": "Animaux et habitat", "blattes-cafards": "Insectes rampants", "fourmis": "Insectes rampants", "chenilles-processionnaires": "Arbres", "punaises-de-lit": "Habitat", "taupier": "Jardins et terrains", "depigeonnage": "Bâtiments", "piegeur-agree": "Faune sauvage"}
# Ordre du menu déroulant « Mes services » (indépendant de l'ordre de SV, utilisé par l'accueil et le pied de page).
MENU_SERVICES = ["deratisation", "desinsectisation", "frelons-guepes", "frelon-asiatique", "punaises-de-lit", "blattes-cafards",
                 "puces", "fourmis", "mouches", "chenilles-processionnaires", "taupier", "contrat-annuel-deratisation",
                 "depigeonnage", "piegeur-agree"]
# Catégories principales, mises en avant dans le menu comme Débarras (orange + chevron).
MENU_PRINCIPAUX = {"deratisation", "desinsectisation", "piegeur-agree"}
_NOMS_MENU = dict([(s[0], s[1]) for s in SV] + [("contrat-annuel-deratisation", "Contrat annuel pro")])
assert set(_NOMS_MENU) == set(MENU_SERVICES), "un service manque dans MENU_SERVICES"
SVG_FB = "<svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><path d='M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0 0 22 12z'/></svg>"
SVG_IG = "<svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><rect x='2.5' y='2.5' width='19' height='19' rx='5.5' fill='none' stroke='currentColor' stroke-width='2'/><circle cx='12' cy='12' r='4.2' fill='none' stroke='currentColor' stroke-width='2'/><circle cx='17.4' cy='6.6' r='1.4'/></svg>"
SVG_MSG = "<svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><path d='M12 3C6.9 3 2.8 6.5 2.8 10.9c0 2.3 1.1 4.3 2.9 5.8-.1 1-.6 2.4-1.4 3.4 0 0 2.5-.4 4.3-1.7 1 .3 2.1.4 3.4.4 5.1 0 9.2-3.5 9.2-7.9S17.1 3 12 3z'/></svg>"
from urllib.parse import quote as _url_q
WA_LIEN = "https://wa.me/33664576655?text=" + _url_q("Bonjour, je vous contacte depuis votre site.")
LIEN_FB = "https://www.facebook.com/profile.php?id=61557433013899"
LIEN_IG = "https://www.instagram.com/proxinuisibles/"
UTIL = ("<div class='util'><div class='wrap'>"
  "<a class='util-ico' href='" + LIEN_FB + "' target='_blank' rel='noopener' aria-label='Proxinuisibles sur Facebook' title='Facebook'>" + SVG_FB + "</a>"
  "<a class='util-ico' href='" + LIEN_IG + "' target='_blank' rel='noopener' aria-label='Proxinuisibles sur Instagram' title='Instagram'>" + SVG_IG + "</a>"
  "<a class='util-wa' href='" + WA_LIEN + "' target='_blank' rel='noopener'>" + SVG_MSG + "<span>WhatsApp</span></a>"
  "</div></div>")

# Bandeau de saison : visible sur l'accueil et les pages chenilles, uniquement
# pendant la saison du pin. Le masquage hors saison est fait par le navigateur
# (voir SAISON_JS) pour qu'il disparaisse seul si le site n'est pas regenere.
SAISON = ("<aside class='saison' hidden>"
          "<div class='wrap'><span class='saison-tag'>En ce moment</span>"
          "<p>Les cocons d’hiver de chenilles processionnaires du pin sont visibles dans les arbres. "
          "L’échenillage se pratique tout l’hiver ; les écopièges, eux, doivent être posés "
          "<strong>avant la descente des chenilles</strong>, qui démarre en février.</p>"
          "<a class='btn btn-light' href='/chenilles-processionnaires/'>Traitement des chenilles \u2197</a></div>"
          "<svg width='0' height='0' aria-hidden='true' style='position:absolute'><symbol id='ch' viewBox='0 0 62 22'><g stroke='#e8a86c' stroke-width='1.1' stroke-linecap='round'><path d='M9 9.5 7 5M13 9 13 4.3M17 9 19 4.6M22 9 22 4.2M26 9.2 28 4.8M31 9 31 4.4M35 9.2 37 5M40 9 40 4.6'/></g><g stroke='#7a4420' stroke-width='1.6' stroke-linecap='round'><path d='M11 17 10 20.5M17 17.2 18 20.5M24 17 23 20.5M30 17.2 31 20.5M37 17 36 20.5M43 17.2 44 20.5'/></g><g fill='#c87a38'><circle cx='11' cy='13' r='5.4'/><circle cx='18' cy='13.2' r='5.7'/><circle cx='25' cy='13' r='5.9'/><circle cx='32' cy='13.2' r='5.8'/><circle cx='39' cy='13' r='5.6'/></g><circle cx='47' cy='12.8' r='6.2' fill='#8a4a1e'/><g stroke='#8a4a1e' stroke-width='1.2' stroke-linecap='round'><path d='M48 7 50 3M51.5 8.5 55 5.5'/></g><circle cx='49.6' cy='11.6' r='1.25' fill='#2a1a10'/></symbol></svg><div class='chenilles-piste piste-bas' aria-hidden='true'><div class='file'><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg></div></div><div class='chenilles-piste piste-haut' aria-hidden='true'><div class='file'><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg><svg class='chenille' viewBox='0 0 62 22'><use href='#ch'/></svg></div></div></aside>")

SAISON_JS = ("(function(){var b=document.querySelector('.saison');if(!b){return;}"
             "var d=new Date(),m=d.getMonth()+1,j=d.getDate();"
             # du 15 octobre au 15 mars
             "var ouvert=(m===10&&j>=15)||m===11||m===12||m===1||m===2||(m===3&&j<=15);"
             "if(!ouvert){return;}b.hidden=false;"
                          "})();")

HEADER = ("<header class='top'>" + UTIL + "<div class='wrap bar'><a class='logo' href='/'><img src='/logo-petit.webp' alt='' width='95' height='160'><img class='logo-txt' src='/logo-texte.webp' alt='Proxinuisibles, accueil' width='92' height='62'></a>"
  "<button class='burger' type='button' aria-label='Menu' aria-expanded='false'>\u2630</button>"
  "<nav id='nav'><ul><li><a href='/'>Accueil</a></li>"
  "<li class='dd'><details><summary>Mes services</summary><ul>" + "".join("<li><a%s href='/%s/'>%s</a></li>" % (" class='nav-deb'" if s in MENU_PRINCIPAUX else "", s, _NOMS_MENU[s]) for s in MENU_SERVICES) +
  "<li><a class='nav-deb' href='/debarras/'>Débarras</a></li></ul></details></li>"
  "<li><a href='/contact/'>Devis et contact</a></li><li><a href='/avis/'>Avis</a></li><li><a href='/questions-frequentes/'>Questions fréquentes</a></li><li><a href='/qui-suis-je/'>Qui suis-je ?</a></li></ul></nav>"
  "<a class='btn' href='tel:%s'>\u260e %s</a></div></header>" % (TEL, TEL_D))
CTA = ("<section class='cta'><div class='wrap'><h2>Décrivez-moi ce que vous voyez. Je vous dirai comment avancer.</h2>"
       "<p>Un nid, des traces, des bruits dans les combles ? Appelez-moi directement.</p>"
       "<div class='actions'><a class='btn' href='tel:%s'>Appeler le %s</a><a class='btn btn-wa' href='%s' target='_blank' rel='noopener'>Écrire sur WhatsApp</a><a class='btn btn-light' href='mailto:%s'>Écrire par e-mail</a></div></div></section>" % (TEL, TEL_D, WA_LIEN, MAIL))

def faq_html(d):
    return "<section class='sec alt'><div class='wrap'><h2>Questions fréquentes</h2>%s</div></section>" % "".join(
        "<details><summary>%s</summary><p>%s</p></details>" % (T(q), T(a)) for q, a in d["faq"])

PROFILS = [
 ("particuliers", "Vous êtes particulier", "Un nuisible chez vous, dans le jardin ou dans la maison.",
  [("frelons-guepes", "Nid de frelons ou de guêpes"), ("deratisation", "Rats et souris à la maison"), ("punaises-de-lit", "Punaises de lit"), ("desinsectisation", "Cafards, fourmis, puces"), ("chenilles-processionnaires", "Chenilles processionnaires"), ("taupier", "Taupes au jardin"), ("piegeur-agree", "Fouines dans les combles")]),
 ("agriculteurs", "Vous êtes agriculteur ou éleveur", "Bâtiments d'élevage, hangars, silos et parcelles.",
  [("deratisation", "Rongeurs dans les bâtiments et les stocks"), ("taupier", "Taupes dans les prairies"), ("piegeur-agree", "Ragondins, fouines, corvidés"), ("depigeonnage", "Pigeons dans les hangars")]),
 ("professionnels", "Vous êtes professionnel", "Restaurant, boulangerie, commerce, entreprise ou collectivité.",
  [("deratisation", "Dératisation de vos locaux"), ("desinsectisation", "Cafards et insectes rampants"), ("frelons-guepes", "Nids autour de l'établissement"), ("depigeonnage", "Pigeons sur le bâtiment"), ("contrat-annuel-deratisation", "Contrat annuel avec compte rendu"), ("contrats-metiers-de-bouche", "Contrats métiers de bouche")]),
 ("agences-syndics", "Vous êtes agence ou syndic", "Copropriétés, logements locatifs et parties communes.",
  [("deratisation", "Rats et souris en caves et locaux poubelles"), ("punaises-de-lit", "Punaises de lit dans les logements"), ("desinsectisation", "Cafards et puces"), ("frelons-guepes", "Nids sur les parties communes"), ("depigeonnage", "Pigeons sur la résidence")]),
]

_CHOIX = [
 ("particuliers", "Je suis particulier", "Maison, jardin, logement",
  [("frelons-guepes", "Nid de frelons ou de guêpes"), ("deratisation", "Rats et souris à la maison"), ("punaises-de-lit", "Punaises de lit"), ("desinsectisation", "Cafards, fourmis, puces"), ("chenilles-processionnaires", "Chenilles processionnaires"), ("taupier", "Taupes au jardin"), ("piegeur-agree", "Fouines dans les combles")]),
 ("agriculteurs", "Je suis agriculteur ou éleveur", "Bâtiments, stocks et parcelles",
  [("deratisation", "Rongeurs dans les bâtiments et les stocks"), ("taupier", "Taupes dans les prairies"), ("piegeur-agree", "Ragondins, fouines, corvidés"), ("depigeonnage", "Pigeons dans les hangars")]),
 ("contrats-metiers-de-bouche", "Je tiens un commerce de bouche", "Restaurant, boulangerie, boucherie, traiteur",
  [("deratisation-restaurant-laval", "Restaurant"), ("deratisation-boulangerie-laval", "Boulangerie-pâtisserie"), ("deratisation-boucherie-laval", "Boucherie-charcuterie"), ("deratisation-traiteur-laval", "Traiteur"), ("deratisation-cuisine-collective-laval", "Cuisine collective"), ("contrat-annuel-deratisation", "Contrat annuel avec compte rendu"), ("contrats-metiers-de-bouche", "Mon contrat dans ma commune")]),
 ("professionnels", "Je suis syndic, professionnel ou collectivité", "Commerce, entreprise, copropriété, commune",
  [("deratisation", "Dératisation de vos locaux ou de vos caves"), ("desinsectisation", "Cafards et insectes rampants"), ("punaises-de-lit", "Punaises de lit dans les logements"), ("frelons-guepes", "Nids autour de l'établissement ou de la résidence"), ("depigeonnage", "Pigeons sur le bâtiment"), ("professionnels", "Écoles, mairies et bâtiments publics"), ("contrat-annuel-deratisation", "Contrat annuel avec compte rendu")]),
]

def profils_html():
    cards = "".join("<div class='choix'><span class='choix-tag'>%s</span><h3><a href='/%s/'>%s</a></h3><ul>%s</ul><a class='more' href='/%s/'>%s \u2197</a></div>" %
                    (T(sous), slug, T(titre), "".join("<li><a href='/%s/'>%s</a></li>" % (u, T(l)) for u, l in lis), slug, T("Voir toutes mes prestations")) for slug, titre, sous, lis in _CHOIX)
    return ("<section class='sec' id='services'><div class='wrap'><span class='label'>%s</span><h2>%s</h2><p>%s</p><div class='choixgrid'>%s</div>"
            "<p class='choix-agence'>%s <a href='/agences-syndics/'>%s</a></p></div></section>" %
            (T("Je clique sur mon profil"), T("Qui êtes-vous ?"), T("Choisissez votre situation : vous arrivez sur une page qui regroupe toutes les prestations qui vous concernent."),
             cards, T("Agence immobilière ou syndic de copropriété ?"), T("Accès direct à votre page")))

_PP = {
 "particuliers": [("Particuliers", [
    ("frelons-guepes", "Nids de frelons et de guêpes", "Repérage et destruction du nid, dans les toitures, les arbres, les murs et les abris de jardin."),
    ("deratisation", "Rats et souris", "Diagnostic, fermeture des accès et traitement dans la maison, le garage et le jardin."),
    ("punaises-de-lit", "Punaises de lit", "Traitement discret du logement, avec contrôle du résultat."),
    ("desinsectisation", "Cafards, fourmis, puces et mouches", "Traitement adapté à l'insecte et aux lieux."),
    ("chenilles-processionnaires", "Chenilles processionnaires", "Traitement des pins et des chênes, et prévention."),
    ("taupier", "Taupes au jardin", "Piégeage des taupes dans la pelouse et le potager."),
    ("depigeonnage", "Pigeons", "Pics, filets et câbles pour protéger toiture, balcon et façade."),
    ("piegeur-agree", "Fouines, ragondins et autres", "Piégeage encadré par la loi, par un piégeur agréé.")])],
 "agriculteurs": [("Agriculteurs et éleveurs", [
    ("deratisation", "Rongeurs dans les bâtiments et les stocks", "Étables, hangars, silos et locaux de stockage : diagnostic puis traitement adapté."),
    ("taupier", "Taupes dans les prairies et parcelles", "Piégeage pour retrouver des terrains propres."),
    ("piegeur-agree", "Ragondins, fouines et corvidés", "Piégeage encadré par la loi autour des étangs, fossés et bâtiments."),
    ("depigeonnage", "Pigeons dans les hangars", "Protection des bâtiments et des stocks contre les fientes."),
    ("frelons-guepes", "Nids de frelons et de guêpes", "Destruction des nids dans les bâtiments, les haies et les arbres."),
    ("desinsectisation", "Insectes dans les locaux", "Mouches et autres insectes dans les bâtiments et les annexes.")])],
 "professionnels": [("Professionnels", [
    ("deratisation", "Dératisation de vos locaux", "Diagnostic, points de contrôle et traitement pour commerces, entreprises et collectivités."),
    ("desinsectisation", "Cafards et insectes rampants", "Traitement adapté aux locaux alimentaires et aux locaux d'activité."),
    ("frelons-guepes", "Nids autour de l'établissement", "Destruction des nids sur les bâtiments, les terrasses et les abords."),
    ("depigeonnage", "Pigeons sur le bâtiment", "Pics, filets et câbles pour façades, toitures et entrepôts."),
    ("punaises-de-lit", "Punaises de lit : gîtes, hôtels et locations", "Intervention rapide pour limiter l'impact sur vos occupants."),
    ("contrat-annuel-deratisation", "Contrat annuel avec compte rendu", "Passages réguliers et suivi écrit à conserver."),
    ("contrats-metiers-de-bouche", "Contrats métiers de bouche", "Restaurants, boulangeries, boucheries, traiteurs : une page par commune.")]),
   ("Collectivités et communes", [
    ("deratisation", "Écoles, mairies et bâtiments publics", "Diagnostic puis traitement des locaux, avec un suivi régulier si besoin."),
    ("taupier", "Terrains de sport et espaces verts", "Piégeage des taupes sur les pelouses et les terrains de sport."),
    ("piegeur-agree", "Berges, étangs et plans d'eau", "Ragondins et rats musqués : piégeage encadré par la loi."),
    ("depigeonnage", "Pigeons sur les bâtiments communaux", "Pics, filets et câbles pour églises, mairies, halles et salles."),
    ("frelons-guepes", "Nids sur les bâtiments et les espaces publics", "Destruction des nids de frelons et de guêpes."),
    ("contrat-annuel-deratisation", "Contrat annuel avec compte rendu", "Passages réguliers et suivi écrit pour chaque site.")]),
   ("Agences immobilières et syndics", [
    ("deratisation", "Rats et souris en caves et locaux poubelles", "Traitement des parties communes et suivi par résidence."),
    ("punaises-de-lit", "Punaises de lit dans les logements", "Intervention rapide entre deux locataires."),
    ("desinsectisation", "Cafards et puces", "Traitement des logements et des parties communes."),
    ("frelons-guepes", "Nids sur les parties communes", "Destruction des nids sur les façades, les toitures et les espaces verts."),
    ("depigeonnage", "Pigeons sur la résidence", "Protection des balcons, des toitures et des façades."),
    ("taupier", "Taupes dans les espaces verts", "Piégeage dans les pelouses et les jardins de la résidence."),
    ("chenilles-processionnaires", "Chenilles processionnaires", "Traitement des pins et des chênes de la copropriété.")])],
 "agences-syndics": [("Agences immobilières et syndics", [
    ("deratisation", "Rats et souris en caves et locaux poubelles", "Traitement des parties communes et suivi par résidence."),
    ("punaises-de-lit", "Punaises de lit dans les logements", "Intervention rapide entre deux locataires."),
    ("desinsectisation", "Cafards et puces", "Traitement des logements et des parties communes."),
    ("frelons-guepes", "Nids sur les parties communes", "Destruction des nids sur les façades, les toitures et les espaces verts."),
    ("depigeonnage", "Pigeons sur la résidence", "Protection des balcons, des toitures et des façades."),
    ("taupier", "Taupes dans les espaces verts", "Piégeage dans les pelouses et les jardins de la résidence."),
    ("chenilles-processionnaires", "Chenilles processionnaires", "Traitement des pins et des chênes de la copropriété."),
    ("contrat-annuel-deratisation", "Contrat annuel avec compte rendu", "Passages réguliers et suivi écrit par résidence.")])],
}
_SWITCH = [("particuliers", "Particulier"), ("agriculteurs", "Agriculteur ou éleveur"), ("contrats-metiers-de-bouche", "Métiers de bouche"), ("professionnels", "Syndic, professionnel ou collectivité")]

def _pre_profil(slug):
    sw = "<ul class='switch' aria-label='Choisir mon profil'>%s</ul>" % "".join(
        "<li><a href='/%s/'%s>%s</a></li>" % (u, " aria-current='page'" if (u == slug or (slug == "agences-syndics" and u == "professionnels")) else "", T(l)) for u, l in _SWITCH)
    out = ["<section class='sec'><div class='wrap'>", sw]
    for titre, items in _PP[slug]:
        out.append("<h2>%s</h2><div class='pgrid'>%s</div>" % (T("Toutes mes prestations : " + titre.lower() if False else "Mes prestations pour " + titre.lower()),
                   "".join("<a class='pcard' href='/%s/'><h3>%s</h3><p>%s</p><span class='more'>%s \u2197</span></a>" % (u, T(t), T(dsc), T("Voir la prestation")) for u, t, dsc in items)))
    out.append("</div></section>")
    return "".join(out)

for _s in _PP:
    P["/%s/" % _s]["pre"] = _pre_profil(_s)

def home_page(path, d, title, meta, scripts):
    cards = "".join("<a class='scard' href='/%s/'>%s<span class='num'>%02d / %s</span><h3>%s</h3><p>%s</p><span class='more'>Découvrir \u2197</span></a>" %
                    (s[0], ico("/%s/" % s[0]), i + 1, T(TAGS[s[0]]), T(s[1]), T(s[5].split(".")[0] + ".")) for i, s in enumerate(SV))
    chips = "".join("<li><a href='/deratisation-%s/'>%s</a></li>" % (c[0], c[1]) for c in CITIES)
    h = ["<!DOCTYPE html><html lang='fr'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>"
         "<title>%s</title><meta name='description' content=\"%s\"><link rel='canonical' href='%s%s'><link rel='stylesheet' href='/style.css'><link rel='icon' href='/favicon.ico' sizes='any'><link rel='icon' type='image/png' href='/favicon.png' sizes='64x64'><link rel='apple-touch-icon' href='/apple-touch-icon.png'><meta name='theme-color' content='#24261a'><meta property='og:site_name' content='Proxinuisibles'><meta property='og:locale' content='fr_FR'>%s</head><body>" %
         (title, meta.replace('"', ''), BASE, path, "".join(scripts)), HEADER, SAISON]
    h.append("<section class='hero'><div class='wrap'><div><span class='label'>%s</span><h1>%s</h1><p>%s</p>"
             "<div class='actions'><a class='btn' href='tel:%s'>Appeler le %s</a><a class='btn btn-light' href='#services'>Découvrir mes services</a></div>"
             "<p class='facts'>%s</p></div></div></section>" %
             (T("Dératiseur et désinsectisation · Mayenne et Ille-et-Vilaine"), T(d["h1"]), T(d["lead"]), TEL, TEL_D, T("Mayenne et Ille-et-Vilaine · Particuliers, agriculteurs et professionnels · Diagnostic et devis gratuits")))
    h.append(profils_html())
    h.append("<section class='sec' id='toutes-prestations'><div class='wrap'><span class='label'>Toutes mes prestations</span><h2>Une réponse précise à chaque nuisible</h2><p>Vous savez déjà ce que vous cherchez ? Choisissez directement la prestation.</p><div class='grid'>%s</div></div></section>" % cards.replace("d'i", "d\u2019i"))
    h.append("<section class='sec alt'><div class='wrap'><span class='label'>Pourquoi me choisir</span><h2>Un interlocuteur, une méthode, un suivi</h2><div class='why'>"
             + "".join("<div><span class='num'>%s</span><h3>%s</h3><p>%s</p></div>" % (n, T(t), T(p)) for n, t, p in [
                 ("01", "Un interlocuteur unique", "Je prends moi-même en charge votre problème, du premier appel au suivi, avec des explications claires à chaque étape."),
                 ("02", "Une méthode adaptée", "J'identifie le nuisible et les zones d'activité avant de choisir le traitement adapté aux lieux."),
                 ("03", "Un secteur que je connais", "J'interviens en Mayenne et en Ille-et-Vilaine, de Laval à Rennes, en ville comme à la campagne, pour des petites ou des plus grosses bêtes.")])
             + "</div></div></section>")
    h.append("<section class='sec'><div class='wrap'><div class='cert'><span class='label'>Certification</span><h2>Certibiocide n° " + CERT_NUM + "</h2><p>Ce certificat est obligatoire depuis le 1er juillet 2015. Vous pouvez vérifier sa validité sur le site officiel : il suffit de saisir mon numéro de certificat, " + CERT_NUM + ", et mon nom, Renault.</p><a class='btn btn-ghost' href='" + CERT_URL + "' target='_blank' rel='noopener'>Vérifier mon certificat \u2197</a></div></div></section>")
    h.append("<section class='sec'><div class='wrap'><div class='band'><span class='label'>Nouveau</span><h2>Débarras : je vide, et je traite ce qui s'y cachait</h2>"
             "<p>%s</p><a class='btn' href='/debarras/'>Découvrir le débarras \u2197</a></div></div></section>" %
             T("Maison, cave, grenier, garage ou logement à reprendre : je vide, je trie et j'évacue. Et comme un logement encombré abrite presque toujours des rongeurs, des cafards ou des punaises, je m'en occupe dans le même passage. Une intervention au lieu de deux."))
    h.append("<section class='sec alt'><div class='wrap'><div class='band'><div class='exp'><a href='https://www.experts-guepes-frelons.fr/' target='_blank' rel='noopener' aria-label='Site des Experts Guêpes et Frelons' style='flex:none'><img src='/media/experts-guepes-frelons-logo.webp' alt='Logo du groupement Experts Guêpes et Frelons' width='160' height='160' loading='lazy'></a><div><span class='label'>Mon réseau</span><h2>Membre du groupement Experts Guêpes et Frelons</h2>"
             "<p>%s</p><p>%s</p><a class='btn' href='https://www.experts-guepes-frelons.fr/' target='_blank' rel='noopener'>Découvrir le groupement \u2197</a> <a href='https://www.experts-guepes-frelons.fr/' target='_blank' rel='noopener' style='color:#fff;margin-left:14px;text-decoration:underline'>www.experts-guepes-frelons.fr</a></div></div></div></div></section>" %
             (T("Je fais partie des Experts Guêpes et Frelons, un groupement d'indépendants pour une lutte raisonnée et durable. Son objectif : appliquer les méthodes les plus sûres connues à ce jour pour les nids de frelons et les chenilles processionnaires, en limitant l'impact sur la santé, l'environnement, la biodiversité et la sécurité des intervenants."),
              T("Chaque membre est indépendant, titulaire d'un Certibiocide valable et assuré en responsabilité civile professionnelle. Nous échangeons entre nous lors des interventions délicates, pour vous garantir une intervention sûre.")))
    h.append("<section class='sec'><div class='wrap'><span class='label'>En bref</span><h2>Un artisan, un suivi direct</h2><ul class='faits'>"
             "<li><strong>Depuis 2016</strong><span>dans la lutte contre les nuisibles</span></li>"
             "<li><strong>Ind\u00e9pendant depuis 2024</strong><span>un seul interlocuteur, du devis au suivi</span></li>"
             "<li><strong>Mayenne et Ille-et-Vilaine</strong><span>de Laval \u00e0 Rennes, particuliers et professionnels</span></li>"
             "<li><strong>Certibiocide n\u00b0 " + CERT_NUM + "</strong><span>produits homologu\u00e9s, loi EGalim</span></li>"
             "<li><strong>8h - 21h en semaine</strong><span>9h - 18h le samedi et le dimanche</span></li>"
             "<li><strong>En g\u00e9n\u00e9ral sous 24 \u00e0 48 h</strong><span>urgences r\u00e9elles en priorit\u00e9</span></li>"
             "<li><strong>Devis gratuit, d\u00e9placement compris</strong><span>CB, esp\u00e8ces, ch\u00e8que et virement</span></li>"
             "</ul></div></section>")
    h.append("<section class='sec alt'><div class='wrap'><span class='label'>Me suivre</span><h2>Mes interventions au quotidien</h2>"
             "<div class='socgrid'>"
             "<a class='soc' href='https://www.facebook.com/profile.php?id=61557433013899' target='_blank' rel='noopener'>"
             "<span class='soc-ico' aria-hidden='true'><svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><path d='M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0 0 22 12z'/></svg></span>"
             "<span class='soc-txt'><strong>Facebook</strong><span>Mes interventions, mes conseils et l'actualit\u00e9 des nuisibles dans le secteur.</span><span class='more'>Voir ma page \u2197</span></span></a>"
             "<a class='soc' href='https://www.instagram.com/proxinuisibles/' target='_blank' rel='noopener'>"
             "<span class='soc-ico' aria-hidden='true'><svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><rect x='2.5' y='2.5' width='19' height='19' rx='5.5' fill='none' stroke='currentColor' stroke-width='2'/><circle cx='12' cy='12' r='4.2' fill='none' stroke='currentColor' stroke-width='2'/><circle cx='17.4' cy='6.6' r='1.4'/></svg></span>"
             "<span class='soc-txt'><strong>Instagram</strong><span>Photos et vid\u00e9os de nids, de pi\u00e8ges et de chantiers, prises sur le terrain.</span><span class='more'>Voir mon compte \u2197</span></span></a>"
             "</div></div></section>")
    h.append(AVIS_MINI)
    h.append("<section class='sec'><div class='wrap'><div class='band'><span class='label'>Pour les professionnels</span><h2>Qui surveille votre établissement entre deux infestations ?</h2>"
             "<p>%s</p><a class='btn' href='/contrat-annuel-deratisation/'>Découvrir le contrat annuel \u2197</a></div></div></section>" %
             T("Restaurant, boulangerie, commerce, entrepôt ou bâtiment public : je mets en place un contrat annuel adapté à votre site, avec des passages réguliers et un compte rendu écrit."))
    h.append("<section class='sec'><div class='wrap'><span class='label'>Ma méthode</span><h2>Observer. Traiter. Contrôler.</h2><p>%s</p>"
             "<div class='steps'><div><span class='num'>01</span>Échange et diagnostic</div><div><span class='num'>02</span>Protocole adapté aux lieux</div><div><span class='num'>03</span>Intervention et suivi</div></div>"
             "<a class='btn' href='/contact/'>Parlons de votre situation \u2197</a></div></section>" %
             T("Chaque lieu est différent. Je commence par comprendre où les nuisibles circulent et pourquoi ils sont présents. J'explique ensuite le traitement proposé et les étapes de suivi."))
    h.append("<section class='sec'><div class='wrap'><span class='label'>Proxinuisibles</span><h2>%s</h2><p>%s</p><p>%s</p><ul class='chips'>%s</ul></div></section>" %
             (T("Dératisation et destruction de nids depuis Port-Brillet"),
              T("Je suis Gwendal, à la tête de Proxinuisibles. J'interviens chez les particuliers, les agriculteurs, les professionnels et les agences en Mayenne et en Ille-et-Vilaine."),
              T("Je cherche les indices, je vous explique ce que je vais faire et je précise comment se passe le suivi. Chaque prestation a sa page détaillée."),
              "<li><a href='/qui-suis-je/'>Mon parcours</a></li><li><a href='/zones-intervention/'>Mes zones d'intervention</a></li><li><a href='/questions-frequentes/'>Questions fréquentes</a></li><li><a href='/contact/'>Devis gratuit</a></li>".replace("d'i", "d\u2019i")))
    h.append("<section class='sec alt'><div class='wrap'><span class='label'>Où j'intervient</span><h2>De Laval à Rennes</h2><ul class='chips'>%s</ul></div></section>".replace("Où j'intervient", T("Où j'interviens")) % chips)
    h.append("<section class='sec'><div class='wrap'><span class='label'>Autour de Port-Brillet</span><h2>Communes où j\u2019interviens à moins de 20 km</h2><p>Une page dédiée par commune, avec les nuisibles du secteur, les conseils utiles et mes coordonnées.</p><ul class='chips'>%s</ul><p><a class='btn btn-ghost' href='/zones-intervention/'>Voir toutes les zones d\u2019intervention \u2197</a></p></div></section>" %
             "".join("<li><a href='/deratisation-%s/'>%s</a></li>" % (f[0], f[1]) for f in sorted(FICHES, key=lambda x: x[3]) if "/deratisation-%s/" % f[0] in P))
    h.append("<section class='sec'><div class='wrap'><span class='label'>Qui suis-je ?</span><h2>Moi, c'est Gwendal.</h2><p>%s</p><a class='btn btn-ghost' href='/qui-suis-je/'>Découvrir mon parcours \u2197</a></div></section>".replace("c'est", "c\u2019est") %
             T("Depuis le premier appel jusqu'au suivi, je viens moi-même comprendre votre problème de nuisibles et vous expliquer mon intervention."))
    h.append(faq_html(d))
    h.append(CTA)
    h.append(FOOT + "<script src='/site.js'></script><script src='/avis.js'></script></body></html>")
    return "".join(h)

MEDIA = {
 "/mouches/": ("image", "badigeon-mouches", "Application au pinceau d'un badigeon anti-mouches sur le dormant d'une fenêtre", "Le badigeon s'applique au pinceau, sur les surfaces où les mouches se posent."),
 "/frelons-guepes/": ("video", "frelons-nid-primaire", "Une guêpe et son nid primaire, placés dans un bocal après une intervention", "Un nid primaire et sa fondatrice, récupérés lors d'une intervention au printemps."),
 "/deratisation/": ("video", "deratisation-rats", "Des rats surmulots qui mangent de la nourriture laissée à l'extérieur", "Rats surmulots attirés par de la nourriture accessible : c'est ainsi qu'une infestation commence."),
 "/piegeur-agree/": ("video", "piegeage-ragondin", "Un ragondin au bord de l'eau, dans les roseaux", "Un ragondin au bord de l'eau : son piégeage est encadré par la loi."),
 "/desinsectisation/": ("video", "desinsectisation-fourmis", "Des fourmis autour de l'entrée de leur nid", "Des fourmis à l'entrée de leur nid : repérer le passage est la première étape du traitement."),
 "/chenilles-processionnaires/": ("image", "chenilles-nid-pin", "Un cocon de chenilles processionnaires dans la cime d'un pin", "Un nid de chenilles processionnaires, visible en haut d'un pin."),
 "/depigeonnage/": ("video", "depigeonnage-pigeons-toit", "Des pigeons posés sur un toit, près d'une ventilation", "Des pigeons sur une toiture : ils s'installent vite sur les rebords et les ventilations.", 500),
 "/punaises-de-lit/": ("video", "punaises-lit-reelle", "Punaises de lit vivantes, œufs et taches noires dans la couture d'un matelas, filmés lors d'une intervention", "Images prises lors d'une de mes interventions : punaises vivantes, œufs et traces noires le long d'une couture.", 360),
 "/qui-suis-je/": ("image", "gwendal-portrait", "Portrait illustré de Gwendal, fondateur de Proxinuisibles, en tee-shirt noir à l'effigie de la marque", "Gwendal, fondateur de Proxinuisibles, basé à Port-Brillet.", 420),
 "/taupier/": ("image", "taupinieres-prairie", "Des taupinières alignées dans une prairie", "Des taupinières dans une prairie : signe d'une taupe en activité."),
}

MEDIA.update(globals().get("MEDIA_EXTRA", {}))

# Média de fond du hero : vidéo sur les pages nuisibles, image sinon
# Hero : la vidéo remplace le bloc de couleur, uniquement sur les pages qui ont une vidéo
HERO_SKIP = ("/qui-suis-je/",)

def has_hero_video(path):
    m = MEDIA.get(path)
    return bool(m) and path not in HERO_SKIP

def hero_media(path):
    """Renvoie (classe, html de fond) pour le hero : vidéo ou image à la place du bloc de couleur."""
    if not has_hero_video(path):
        return "", ""
    kind, name = MEDIA[path][0], MEDIA[path][1]
    if kind == "video":
        el = ("<video autoplay muted loop playsinline preload='metadata' poster='/media/%s-poster.webp' aria-hidden='true' tabindex='-1'>"
              "<source src='/media/%s.mp4' type='video/mp4'></video>" % (name, name))
    else:
        el = "<img src='/media/%s.webp' alt='' aria-hidden='true'>" % name
    return " hero-media", "<div class='hero-bg' aria-hidden='true'>%s</div>" % el

def media_html(path):
    m = MEDIA.get(path)
    if not m or has_hero_video(path):
        return ""
    kind, name, alt, cap = m[:4]
    mw = (' style="max-width:%dpx"' % m[4]) if len(m) > 4 else ''
    if kind == "video":
        el = ("<video autoplay muted loop playsinline preload='metadata' poster='/media/%s-poster.webp' aria-label=\"%s\"><source src='/media/%s.mp4' type='video/mp4'></video>" % (name, T(alt).replace('"', ''), name))
    else:
        el = "<img src='/media/%s.webp' alt=\"%s\" loading='lazy'>" % (name, T(alt).replace('"', ''))
    return "<section class='sec media-sec'><div class='wrap'><figure class='media'%s>%s<figcaption>%s</figcaption></figure></div></section>" % (mw, el, T(cap))

import datetime as _dt
_TODAY = _dt.date.today().isoformat()
_SVC = {"frelons-guepes": "Destruction de nids de frelons et de guêpes", "desinsectisation": "Désinsectisation", "frelon-asiatique": "Destruction de nids de frelons asiatiques", "mouches": "Traitement contre les mouches", "puces": "Traitement contre les puces", "blattes-cafards": "Traitement des blattes et cafards", "fourmis": "Traitement des fourmis", "punaises-de-lit": "Traitement contre les punaises de lit",
        "chenilles-processionnaires": "Traitement des chenilles processionnaires", "taupier": "Taupier", "depigeonnage": "Dépigeonnage", "piegeur-agree": "Piégeage de nuisibles", "deratisation": "Dératisation"}

def _lieu(d):
    m = re.search(r" à (.+?)(?: \(|:|,|$)", d["h1"])
    return m.group(1).strip() if m else None

import re as _re_crumb
# « ... à <Commune> (53) » : on s'arrête au premier séparateur pour ne pas avaler la phrase
_RE_COMMUNE = _re_crumb.compile(r"à ([^à,:()]+?)\s*\(\d{2}\)")
_RE_COMMUNE_FIN = _re_crumb.compile(r"à ([^à,:()]+?)\s*$")
_METIERS = ("boulangerie-pâtisserie", "boucherie-charcuterie", "restauration collective",
            "restauration d’entreprise", "restauration d'entreprise", "cuisine collective",
            "cuisine centrale", "boulangerie", "boucherie", "restaurant", "traiteur")

_CRUMB_FAM = (
 ("/punaises-de-lit-", "Punaises de lit", "/punaises-de-lit/"),
 ("/frelons-guepes-", "Frelons et guêpes", "/frelons-guepes/"),
 ("/debarras-", "Débarras", "/debarras/"),
 ("/contrats-metiers-de-bouche", None, None),
 ("/contrat-deratisation-", "Contrats métiers de bouche", "/contrats-metiers-de-bouche/"),
 ("/deratisation-", "Zones d'intervention", "/zones-intervention/"),
)
_CRUMB_NOM = {
 "/contact/": "Devis et contact", "/zones-intervention/": "Zones d'intervention",
 "/questions-frequentes/": "Questions fréquentes", "/qui-suis-je/": "Qui suis-je ?",
 "/avis/": "Avis clients",
 "/mentions-legales/": "Mentions légales", "/debarras/": "Débarras",
 "/particuliers/": "Particuliers", "/professionnels/": "Professionnels",
 "/agriculteurs/": "Agriculteurs et éleveurs", "/agences-syndics/": "Agences et syndics",
 "/metiers-de-bouche/": "Métiers de bouche", "/contrats-metiers-de-bouche/": "Contrats métiers de bouche",
 "/contrat-annuel-deratisation/": "Contrat annuel", "/piegeur-agree/": "Piégeur agréé",
}

def _crumb_commune(h1):
    m = _RE_COMMUNE.findall(h1) or _RE_COMMUNE_FIN.findall(h1)
    return m[-1].strip() if m else None

def _crumb_metier(h1):
    bas = h1.lower()
    for mot in _METIERS:
        if mot in bas:
            return mot[0].upper() + mot[1:]
    return None

def _crumb_dernier(path, d, title):
    """Libellé court du dernier maillon : jamais le titre SEO."""
    if path in _CRUMB_NOM:
        return _CRUMB_NOM[path]
    if d.get("crumb"):
        return d["crumb"]
    if d.get("nav"):
        return d["nav"]
    h1 = d.get("h1", "")
    com = _crumb_commune(h1)
    if com:
        if path.startswith("/contrat-deratisation-"):
            met = _crumb_metier(h1)
            return "%s à %s" % (met, com) if met else com
        if path.startswith("/deratisation-") and path.endswith("-laval/"):
            met = _crumb_metier(h1)
            if met:
                return met
        return com
    return title.split(" | ")[0]

def crumbs(path, d, title):
    c = [("Accueil", "/")]
    if path != "/":
        if d.get("parent"):
            c.append(d["parent"])
        elif path.startswith("/deratisation-") and path.endswith("-laval/") and path != "/deratisation-laval/":
            c.append(("Dératisation à Laval", "/deratisation-laval/"))
        else:
            for pref, lib, url in _CRUMB_FAM:
                if path.startswith(pref) and path != url:
                    if lib:
                        c.append((lib, url))
                    break
    c.append((_crumb_dernier(path, d, title), path))
    return c

def crumbs_html(cs):
    li = "".join("<li><a href='%s'>%s</a></li>" % (u, l) if i < len(cs) - 1 else "<li aria-current='page'>%s</li>" % l for i, (l, u) in enumerate(cs))
    return "<nav class='crumbs' aria-label=\"Fil d'Ariane\"><ol>%s</ol></nav>" % li

def crumbs_ld(cs):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": l, "item": BASE + u} for i, (l, u) in enumerate(cs)]}

def service_ld(path, d):
    if d["kind"] not in ("service", "ville", "metier"):
        return None
    if d["kind"] == "service":
        stype = _SVC.get(path.strip("/"), d["h1"])
        area = None
    else:
        stype = d.get("stype") or ("Contrat de dératisation" if path.startswith("/contrat-deratisation-") else "Dératisation")
        area = _lieu(d)
    ld = {"@context": "https://schema.org", "@type": "Service", "name": d["h1"], "serviceType": stype, "url": BASE + path,
          "provider": {"@type": "LocalBusiness", "name": "Proxinuisibles", "url": BASE + "/", "telephone": TEL}}
    if area:
        ld["areaServed"] = {"@type": "City", "name": area}
    return ld

def render(path, d):
    title, meta = T(d["title"]), T(d["meta"])
    ld = {"@context": "https://schema.org", "@type": "LocalBusiness", "name": "Proxinuisibles", "url": BASE + "/",
          "telephone": TEL, "email": MAIL,
          "description": "Dératiseur : dératisation, destruction de nids de frelons et guêpes, désinsectisation en Mayenne et Ille-et-Vilaine.",
          "areaServed": [c[1] for c in CITIES], "hasMap": FICHE,
          "address": {"@type": "PostalAddress", "streetAddress": "7 rue des Lavandières", "postalCode": "53410", "addressLocality": "Port-Brillet", "addressCountry": "FR"},
          "openingHoursSpecification": [
              {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "21:00"},
              {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Saturday", "Sunday"], "opens": "09:00", "closes": "18:00"}],
          "paymentAccepted": "Carte bancaire, espèces, chèque, virement", "priceRange": "$$"}
    scripts = ['<script type="application/ld+json">%s</script>' % json.dumps(ld, ensure_ascii=False)]
    if d["kind"] == "home":
        site_ld = {"@context": "https://schema.org", "@type": "WebSite", "name": "Proxinuisibles",
                   "alternateName": ["Proxi Nuisibles", "Proxinuisibles 53"], "url": BASE + "/",
                   "publisher": {"@type": "LocalBusiness", "name": "Proxinuisibles", "url": BASE + "/"}}
        scripts.append('<script type="application/ld+json">%s</script>' % json.dumps(site_ld, ensure_ascii=False))
    if d["faq"]:
        fq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": T(q), "acceptedAnswer": {"@type": "Answer", "text": T(a)}} for q, a in d["faq"]]}
        scripts.append('<script type="application/ld+json">%s</script>' % json.dumps(fq, ensure_ascii=False))
    _cs = crumbs(path, d, title) if d["kind"] != "home" else None
    if _cs:
        scripts.append('<script type="application/ld+json">%s</script>' % json.dumps(crumbs_ld(_cs), ensure_ascii=False))
    _sv = service_ld(path, d)
    if _sv:
        scripts.append('<script type="application/ld+json">%s</script>' % json.dumps(_sv, ensure_ascii=False))
    if d["kind"] == "home":
        return home_page(path, d, title, meta, scripts)
    h = ["<!DOCTYPE html><html lang='fr'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>",
         "<title>%s</title><meta name='description' content=\"%s\"><link rel='canonical' href='%s%s'><link rel='stylesheet' href='/style.css'><link rel='icon' href='/favicon.ico' sizes='any'><link rel='icon' type='image/png' href='/favicon.png' sizes='64x64'><link rel='apple-touch-icon' href='/apple-touch-icon.png'><meta name='theme-color' content='#24261a'><meta property='og:site_name' content='Proxinuisibles'><meta property='og:locale' content='fr_FR'>" % (title, meta.replace('"', ''), BASE, path) + d.get("head", ""),
         "".join(scripts), "</head><body>",
         HEADER,
         SAISON if path.startswith("/chenilles-processionnaires") else "",
         "<section class='hero%s'>%s<div class='wrap'>%s%s<h1>%s</h1><p>%s</p>" % (hero_media(path) + (crumbs_html(_cs), ico(path), T(d["h1"]), T(d["lead"])))]
    if d["kind"] != "legal":
        h.append("<div class='actions'><a class='btn' href='tel:%s'>Appeler le %s</a><a class='btn btn-light' href='/contact/'>Demander un devis</a>%s</div>" % (TEL, TEL_D, ("<a class='btn btn-light' href='/deratisation/'>Voir la prestation de dératisation</a>" if path.startswith(("/deratisation-", "/contrat-deratisation-", "/contrats-metiers-de-bouche")) else "")))
    h.append("</div></section>")
    h.append(d.get("pre", ""))
    h.append(media_html(path))
    for i, (t, p) in enumerate(d["secs"]):
        h.append("<section class='sec%s'><div class='wrap'><h2>%s</h2>%s</div></section>" % (" alt" if i % 2 == (0 if d.get("pre") else 1) else "", T(t), body(p)))
    for t, items in d.get("links", []):
        h.append("<section class='sec'><div class='wrap'><h2>%s</h2><ul class='chips'>%s</ul></div></section>" % (T(t), "".join("<li><a href='%s'>%s</a></li>" % (u, T(l)) for l, u in items)))
    if d["faq"]:
        h.append("<section class='sec alt'><div class='wrap'><h2>Questions fréquentes</h2>%s</div></section>" % "".join("<details><summary>%s</summary><p>%s</p></details>" % (T(q), T(a)) for q, a in d["faq"]))
    if d.get("avis"):
        h.append(AVIS)
    if d["kind"] != "legal":
        h.append(CTA)
    h.append(FOOT + "<script src='/site.js'></script><script src='/avis.js'></script>" + d.get("js", "") + "</body></html>")
    return "".join(h)

CSS = """
:root{--orange:rgb(255,133,27);--olive:rgb(106,112,76);--dark:rgb(36,38,26);--soft:rgb(245,244,236)}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font:17px/1.65 "Segoe UI",system-ui,-apple-system,Arial,sans-serif;color:#000;background:#fff}
[hidden]{display:none!important}
a{color:#000}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
h1,h2,h3{line-height:1.2;margin:0 0 .6em}
h1{color:var(--orange);font-size:clamp(2rem,5vw,3.1rem)}
h2{color:var(--olive);font-size:clamp(1.5rem,3.4vw,2.05rem)}
h3{color:#000;font-size:1.1rem}
p,ul{max-width:70ch;margin:0 0 1em}
.top{background:#fff;border-bottom:3px solid var(--orange);position:sticky;top:0;z-index:10}
.bar{display:flex;align-items:center;gap:12px;flex-wrap:wrap;padding-top:12px;padding-bottom:12px}
.logo{font-weight:800;font-size:1.35rem;color:var(--olive);text-decoration:none}
.top nav{flex:1;display:flex;justify-content:center}.util{background:var(--dark)}.util .wrap{display:flex;align-items:center;justify-content:flex-end;gap:12px;padding-top:6px;padding-bottom:6px}.util-ico{display:flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:9px;color:#fff;text-decoration:none}.util-ico svg{width:23px;height:23px;fill:currentColor}.util-ico:hover{background:rgba(255,255,255,.15)}.util-wa{display:inline-flex;align-items:center;gap:8px;padding:6px 15px;border-radius:999px;background:#25d366;color:#07321a;font-weight:700;font-size:.92rem;text-decoration:none;line-height:1.5}.util-wa svg{width:19px;height:19px;fill:currentColor}.util-wa:hover{filter:brightness(1.08)}.saison{background:var(--dark);color:#fff;border-bottom:3px solid var(--orange);position:relative;overflow:hidden}.chenilles-piste{position:absolute;left:0;right:0;height:22px;pointer-events:none;overflow:hidden}.piste-bas{bottom:3px}.piste-haut{top:3px}.file{position:absolute;top:0;left:-2100px;display:flex;gap:8px;width:max-content;will-change:transform;animation:defile 35s linear infinite}.piste-haut .file{animation-delay:-17.5s}.chenille{width:62px;height:22px;flex:none;opacity:.95;display:block;animation:ondule .55s ease-in-out infinite alternate}.chenille:nth-child(3n+2){animation-delay:-.18s}.chenille:nth-child(3n+3){animation-delay:-.36s}.file .chenille:nth-child(5n){margin-right:342px}/* ecart fixe par decalage horizontal : la file garde la meme forme quelle que soit la largeur de l'ecran */@keyframes defile{from{transform:translateX(0)}to{transform:translateX(2100px)}}@keyframes ondule{from{transform:translateY(0) scaleX(1)}to{transform:translateY(-1.5px) scaleX(.95)}}@media(prefers-reduced-motion:reduce){.chenilles-piste{display:none}}.saison .wrap{display:flex;align-items:center;gap:14px 20px;flex-wrap:wrap;padding-top:30px;padding-bottom:30px;position:relative;z-index:1}.saison-tag{background:var(--orange);color:var(--dark);font-weight:800;font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;padding:4px 10px;border-radius:999px;white-space:nowrap}.saison p{margin:0;flex:1;min-width:260px;font-size:.95rem;line-height:1.55}.saison strong{color:var(--orange)}.saison .btn{white-space:nowrap}@media(max-width:700px){.saison .wrap{gap:10px}.saison p{font-size:.9rem}.saison .btn{width:100%;text-align:center}}.btn-wa{background:#25d366;border-color:#25d366;color:#07321a}
.top nav ul{list-style:none;display:flex;flex-wrap:nowrap;gap:6px 11px;margin:0;padding:0;max-width:none}.top nav>ul>li{display:flex;align-items:center}
.top nav a,.top nav summary{text-decoration:none;font-weight:600;font-size:.9rem;white-space:nowrap}.top nav>ul>li>a,.dd summary{display:inline-flex;align-items:center;line-height:1.3}
.top nav a:hover{color:var(--olive);text-decoration:underline}
.btn{display:inline-block;padding:12px 24px;border-radius:8px;background:var(--orange);color:#000;font-weight:700;text-decoration:none;border:2px solid var(--orange)}
.btn:hover{filter:brightness(.95)}
.btn-ghost{background:transparent;border-color:var(--olive)}
.avis-resume{display:flex;flex-wrap:wrap;align-items:center;gap:6px 14px;margin:18px 0}.avis-note{font-size:1.6rem}.avis-etoiles{color:var(--orange);letter-spacing:2px;font-size:1.15rem}.avis-nb{opacity:.8}.avis-maj{font-size:.85rem;opacity:.7;font-style:italic;flex-basis:100%}.avis-ban{overflow:hidden;margin:0 0 22px;-webkit-mask-image:linear-gradient(90deg,transparent,#000 4%,#000 96%,transparent);mask-image:linear-gradient(90deg,transparent,#000 4%,#000 96%,transparent)}.avis-piste{display:flex;gap:16px;width:max-content;animation:avis-defile var(--dur,70s) linear infinite}.avis-ban:hover .avis-piste,.avis-ban:focus-within .avis-piste{animation-play-state:paused}.avis-ban .avis-carte{flex:none;width:340px;white-space:normal}@keyframes avis-defile{from{transform:translateX(0)}to{transform:translateX(-50%)}}@media(prefers-reduced-motion:reduce){.avis-ban{overflow-x:auto;-webkit-mask-image:none;mask-image:none}.avis-piste{animation:none}.avis-piste [aria-hidden=true]{display:none}}@media(hover:none),(pointer:coarse){.avis-ban{overflow-x:auto;overflow-y:hidden;-webkit-overflow-scrolling:touch;scroll-snap-type:x proximity;-webkit-mask-image:none;mask-image:none;padding-bottom:6px}.avis-piste{animation:none;width:auto;padding-right:16px}.avis-piste [aria-hidden=true]{display:none}.avis-ban .avis-carte{scroll-snap-align:start}}.avis-aide{font-size:.85rem;opacity:.7;margin:-12px 0 18px}@media(hover:hover) and (pointer:fine){.avis-aide{display:none}}@media(max-width:700px){.avis-ban .avis-carte{width:280px}}.avis-carte{background:#fff;border:1px solid rgba(0,0,0,.12);border-radius:10px;padding:16px 18px;margin:0}.avis-carte p{margin:8px 0}.avis-tete{display:flex;align-items:center;gap:10px;margin-bottom:8px;font-weight:700}.avis-photo{width:34px;height:34px;border-radius:50%;flex:none;background:var(--soft)}.avis-tete a{color:inherit;text-decoration:none}.avis-tete a:hover{text-decoration:underline}.avis-source{font-size:.85rem;margin:10px 0 0;display:flex;align-items:center;flex-wrap:wrap}.avis-logo{height:18px;width:auto;display:block;margin:10px 10px 5px 0}.avis-source-txt{opacity:.75}.avis-auteur{font-size:.82rem;opacity:.7;line-height:1.5}.avis-auteur a{color:inherit;text-decoration:underline}.avis-auteur a:hover{color:var(--olive)}\n.choixgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(225px,1fr));gap:16px;margin:22px 0 14px}.choix{display:flex;flex-direction:column;gap:6px;padding:26px 24px;border-radius:14px;background:var(--dark);color:#fff;text-decoration:none;border:2px solid var(--dark);transition:transform .15s,border-color .15s}.choix:hover,.choix:focus-visible{transform:translateY(-3px);border-color:var(--orange)}.choix h3{margin:0;color:var(--orange);font-size:1.45rem}.choix p{margin:0;opacity:.92}.choix h3 a{color:var(--orange);text-decoration:none}.choix ul{list-style:none;margin:6px 0 4px;padding:0}.choix li{padding:7px 0;border-top:1px solid rgba(255,255,255,.16)}.choix li:first-child{border-top:0}.choix li a{color:#fff;text-decoration:none}.choix li a:hover,.choix li a:focus-visible{color:var(--orange);text-decoration:underline}.choix .more{color:var(--orange)}\n.choix-tag{font-size:.85rem;letter-spacing:.04em;text-transform:uppercase;opacity:.75}.choix .more{margin-top:auto;padding-top:10px;font-weight:700}.choix-agence{margin:6px 0 0}\n.pgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin:16px 0 8px}.pcard{display:block;padding:18px 20px;border-radius:12px;background:#fff;border:1px solid rgba(0,0,0,.14);color:inherit;text-decoration:none}.pcard:hover{border-color:var(--orange)}.pcard h3{margin:0 0 6px;font-size:1.1rem;color:var(--olive)}.pcard p{margin:0 0 8px;font-size:.95rem}.pcard .more{font-weight:700}.switch{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 18px;padding:0;list-style:none}.switch a{display:inline-block;padding:8px 16px;border-radius:99px;border:2px solid var(--olive);text-decoration:none;color:inherit;font-weight:600}.switch a[aria-current]{background:var(--olive);color:#fff}\n.asst{position:fixed;right:16px;bottom:16px;z-index:50;font:inherit}.asst-btn{display:flex;align-items:flex-end;gap:2px;padding:0;border:0;background:transparent;color:var(--dark);cursor:pointer}.asst-btn img{width:100px;height:auto;display:block;filter:drop-shadow(0 4px 8px rgba(0,0,0,.35));transition:transform .2s}.asst-bulle{position:relative;max-width:190px;margin-bottom:72px;padding:11px 15px;background:#fff;color:var(--dark);border:2px solid var(--dark);border-radius:18px;text-align:left;font-size:1rem;line-height:1.3;box-shadow:0 4px 14px rgba(0,0,0,.25);animation:asst-pop 2.6s ease-in-out infinite}.asst-bulle b{color:var(--orange);-webkit-text-stroke:.3px var(--dark)}.asst-bulle::after{content:'';position:absolute;right:-9px;bottom:14px;width:14px;height:14px;background:#fff;border-right:2px solid var(--dark);border-top:2px solid var(--dark);transform:rotate(45deg)}.asst-btn:hover img,.asst-btn:focus-visible img{transform:scale(1.05)}.asst-btn:focus-visible{outline:3px solid var(--orange);outline-offset:4px;border-radius:12px}@keyframes asst-pop{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}@media(prefers-reduced-motion:reduce){.asst-bulle{animation:none}}.asst-btn[aria-expanded=true] .asst-bulle{display:none}.asst-panel{position:absolute;right:0;bottom:calc(100% + 10px);width:min(360px,calc(100vw - 32px));max-height:min(78vh,620px);overflow:auto;background:#fff;color:var(--dark);border:2px solid var(--dark);border-radius:14px;padding:16px;box-shadow:0 8px 28px rgba(0,0,0,.35)}.asst-head{display:flex;justify-content:space-between;align-items:center;gap:8px}.asst-close{border:0;background:transparent;font-size:1.6rem;line-height:1;cursor:pointer;color:inherit}.asst-msg{margin:10px 0}.asst-form{display:flex;gap:8px;margin:8px 0}.asst-q{flex:1;min-width:0;padding:10px;border:2px solid var(--olive);border-radius:8px;font:inherit}.asst-form .btn{width:auto;padding:10px 14px}.asst-res,.asst-quick{list-style:none;margin:6px 0;padding:0}.asst-res li,.asst-quick li{margin:4px 0}.asst-res a{display:block;padding:9px 12px;border-radius:8px;background:var(--soft);color:inherit;font-weight:700;text-decoration:none}.asst-res a:hover{outline:2px solid var(--orange)}.asst-sub{margin:12px 0 4px;font-weight:700}.asst-quick{display:flex;flex-wrap:wrap;gap:6px}.asst-quick a{display:inline-block;padding:6px 12px;border-radius:99px;border:2px solid var(--olive);color:inherit;text-decoration:none;font-size:.92rem}.asst-quick a:hover{background:var(--olive);color:#fff}.asst-act{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}.asst-act .btn{width:auto;flex:1;text-align:center;padding:10px 12px}@media(max-width:700px){.asst{right:8px;bottom:8px}.asst-btn img{width:68px}.asst-bulle{max-width:140px;margin-bottom:46px;padding:8px 11px;font-size:.85rem}.asst-act .btn,.asst-form .btn{width:auto}}
.badges{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:8px}.badges li{padding:7px 14px;border-radius:99px;background:var(--soft);border:2px solid var(--olive);font-weight:700;font-size:.95rem}\n.frise{list-style:none;margin:28px 0 0;padding:0;display:grid;grid-template-columns:repeat(5,1fr);gap:0;position:relative;counter-reset:f}.frise::before{content:'';position:absolute;left:10%;right:10%;top:27px;height:4px;background:var(--olive);opacity:.35}.frise li{position:relative;text-align:center;padding:0 10px}.frise .n{display:flex;align-items:center;justify-content:center;width:56px;height:56px;margin:0 auto 12px;border-radius:50%;background:var(--orange,#ff8a1f);color:#fff;font-weight:800;font-size:1.25rem;border:4px solid #fff;box-shadow:0 0 0 3px var(--olive);position:relative}.frise strong{display:block;font-size:1.05rem;margin-bottom:4px}.frise em{display:block;font-style:normal;font-size:.8rem;font-weight:700;text-transform:uppercase;letter-spacing:.04em;opacity:.7;margin-bottom:6px}.frise span.t{display:block;font-size:.92rem;line-height:1.45}
@media(max-width:800px){.frise{grid-template-columns:1fr;gap:20px}.frise::before{left:27px;right:auto;top:0;bottom:0;width:4px;height:auto}.frise li{text-align:left;padding:0 0 0 76px;min-height:56px}.frise .n{position:absolute;left:0;top:0;margin:0}}\n.exp{display:flex;gap:32px;align-items:center}.exp img{width:160px;height:160px;border-radius:50%;flex:none;border:3px solid #fff}@media(max-width:700px){.exp{flex-direction:column;align-items:flex-start}.exp img{width:120px;height:120px}}\n.cform{display:grid;grid-template-columns:1fr 1fr;gap:16px;max-width:760px}.cform label{display:flex;flex-direction:column;gap:6px;font-weight:700;font-size:.95rem}.cform .full{grid-column:1/-1}.cform input,.cform textarea{font:inherit;font-weight:400;padding:12px 14px;border:2px solid var(--olive);border-radius:10px;background:#fff;color:inherit}.cform input:focus,.cform textarea:focus{outline:3px solid var(--orange);outline-offset:1px}.cform textarea{min-height:150px;resize:vertical}.cform .rgpd{font-size:.85rem;font-weight:400;opacity:.8}.cform .hp{position:absolute;left:-9999px;opacity:0}.cform-msg{grid-column:1/-1;padding:14px 16px;border-radius:10px;font-weight:700}.cform-msg.ok{background:#e8f3e1;border:2px solid #5b8a3c}.cform-msg.ko{background:#fdeaea;border:2px solid #b94a48}@media(max-width:700px){.cform{grid-template-columns:1fr}}\n.faits{list-style:none;margin:22px 0 0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:18px}.faits li{border-left:4px solid var(--orange);padding:4px 0 4px 16px}.faits strong{display:block;font-size:1.25rem;color:var(--olive)}.faits span{display:block;font-size:.92rem;opacity:.85;margin-top:3px}\n.socgrid{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:22px}.soc{display:flex;gap:16px;align-items:flex-start;padding:22px;border-radius:14px;background:#fff;border:2px solid rgba(0,0,0,.12);text-decoration:none;color:inherit;transition:transform .15s,border-color .15s}.soc:hover,.soc:focus-visible{transform:translateY(-3px);border-color:var(--orange)}.soc-ico{flex:none;width:46px;height:46px;border-radius:12px;background:var(--dark);color:#fff;display:flex;align-items:center;justify-content:center}.soc-ico svg{width:26px;height:26px;fill:currentColor}.soc-txt strong{display:block;font-size:1.1rem;margin-bottom:4px}.soc-txt span{display:block;font-size:.93rem;line-height:1.45}.soc .more{margin-top:8px;font-weight:700;color:var(--olive)}@media(max-width:700px){.socgrid{grid-template-columns:1fr}}\n.gal{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin:22px 0 0}.gal figure{margin:0}.gal img{width:100%;height:auto;display:block;border-radius:14px;border:3px solid var(--orange)}.gal figcaption{font-size:.9rem;opacity:.8;margin-top:8px}@media(max-width:700px){.gal{grid-template-columns:1fr}}\n.bio-avert{font-size:.82rem;opacity:.75;margin-top:18px;font-style:italic}\n.band .mini{float:right;width:190px;margin:0 0 16px 26px}.band .mini img{width:100%;height:auto;display:block;border-radius:12px;border:3px solid var(--orange)}.band .mini figcaption{font-size:.8rem;opacity:.8;margin-top:8px;line-height:1.4}@media(max-width:700px){.band .mini{float:none;width:100%;max-width:260px;margin:0 0 18px}}\n.top nav .nav-deb{color:var(--orange);font-weight:800}.top nav .nav-deb::before{content:'\u25B8 ';opacity:.8}.top nav .nav-deb:hover,.top nav .nav-deb:focus-visible{color:var(--orange);text-decoration:underline}\n.foot .nav-deb{color:var(--orange);font-weight:800}\n.toplink{position:fixed;right:22px;bottom:192px;z-index:50;width:50px;height:50px;padding:0;border:0;border-radius:50%;background:rgba(255,255,255,.92);backdrop-filter:blur(6px);cursor:pointer;display:grid;place-items:center;box-shadow:0 4px 16px rgba(0,0,0,.22);opacity:0;transform:translateY(12px) scale(.9);transition:opacity .22s,transform .22s,background .15s,box-shadow .15s}.toplink.on{opacity:1;transform:none}.toplink>*{grid-area:1/1}.tl-ring{width:50px;height:50px;transform:rotate(-90deg)}.tl-ring circle{fill:none;stroke-width:3}.tl-bg{stroke:rgba(0,0,0,.1)}.tl-pg{stroke:var(--orange);stroke-linecap:round;stroke-dasharray:125.6;stroke-dashoffset:125.6;transition:stroke-dashoffset .1s linear}.tl-arrow{width:21px;height:21px;fill:var(--dark);transition:fill .15s,transform .15s}.toplink:hover,.toplink:focus-visible{background:var(--orange);box-shadow:0 6px 20px rgba(0,0,0,.3)}.toplink:hover .tl-arrow,.toplink:focus-visible .tl-arrow{fill:#fff;transform:translateY(-2px)}.toplink:hover .tl-bg,.toplink:focus-visible .tl-bg{stroke:rgba(255,255,255,.35)}.toplink:hover .tl-pg,.toplink:focus-visible .tl-pg{stroke:#fff}@media(max-width:700px){.toplink{right:14px;bottom:152px;width:44px;height:44px}.tl-ring{width:44px;height:44px}.tl-arrow{width:18px;height:18px}}@media(prefers-reduced-motion:reduce){.toplink,.tl-pg,.tl-arrow{transition:none}}\n.crumbs{margin:0 0 14px;font-size:.9rem}.crumbs ol{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:4px 0}.crumbs li+li::before{content:'\\203A';margin:0 8px;opacity:.7}.crumbs a{color:#fff;text-decoration:underline}.crumbs li[aria-current]{opacity:.85}\n.btn-light{background:transparent;border-color:#fff;color:#fff}\n.carte{height:520px;margin-top:20px;border-radius:14px;border:3px solid var(--olive);background:#e9ecdf;z-index:0}.carte-note{font-size:.8rem;opacity:.75;margin-top:8px}.carte .leaflet-popup-content{font:inherit;font-size:.95rem}.carte .leaflet-popup-content a{color:var(--olive);font-weight:700}@media(max-width:700px){.carte{height:380px}}
.btn:focus-visible,summary:focus-visible,a:focus-visible{outline:3px solid var(--orange);outline-offset:3px}
.hero{position:relative;isolation:isolate;overflow:hidden;color:#fff;padding:72px 0 64px;background:radial-gradient(120% 140% at 85% 0%,rgba(255,133,27,.22) 0%,rgba(255,133,27,0) 55%),linear-gradient(160deg,#2e3122 0%,var(--dark) 45%,#1b1d14 100%)}\n.hero::before{content:'';position:absolute;inset:0;z-index:-1;pointer-events:none;background:repeating-linear-gradient(135deg,rgba(255,255,255,.035) 0 2px,transparent 2px 9px)}\n.hero-bg{position:absolute;inset:0;z-index:-3;overflow:hidden}.hero-bg video,.hero-bg img{width:100%;height:100%;object-fit:cover;display:block}\n.hero-media::after{content:'';position:absolute;inset:0;z-index:-2;pointer-events:none;background:linear-gradient(100deg,rgba(20,22,15,.78) 0%,rgba(20,22,15,.6) 38%,rgba(20,22,15,.3) 68%,rgba(20,22,15,.15) 100%)}\n.hero-media h1,.hero-media p,.hero-media .label,.hero-media .crumbs,.hero-media .facts{text-shadow:0 2px 10px rgba(0,0,0,.75),0 1px 3px rgba(0,0,0,.6)}\n.hero-media::before{background:none}\n.hero>.wrap{position:relative}\n@media(max-width:860px){.hero-media::after{background:linear-gradient(180deg,rgba(20,22,15,.45) 0%,rgba(20,22,15,.62) 45%,rgba(20,22,15,.78) 100%)}.hero-media h1,.hero-media p,.hero-media .label,.hero-media .crumbs,.hero-media .facts{text-shadow:0 2px 12px rgba(0,0,0,.9),0 1px 4px rgba(0,0,0,.8)}}\n@media(prefers-reduced-motion:reduce){.hero-bg video{display:none}}
.hero p{font-size:1.15rem}
.actions{display:flex;flex-wrap:wrap;gap:14px;margin-top:26px}
.sec{padding:56px 0}
.alt{background:var(--soft)}
.grid{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));margin-top:24px}
.card{display:block;background:#fff;border-left:5px solid var(--orange);padding:18px 22px;border-radius:4px;text-decoration:none;box-shadow:0 1px 3px rgba(0,0,0,.12)}
.card p{margin:0;font-size:.96rem}
.card:hover{border-left-color:var(--olive)}
.chips{display:flex;flex-wrap:wrap;gap:10px;list-style:none;padding:0;margin:20px 0 0;max-width:none}
.chips a{display:block;padding:8px 16px;border-radius:999px;border:1px solid var(--olive);background:#fff;text-decoration:none;font-weight:600}
.chips a:hover{background:var(--olive);color:#fff}
details{border-bottom:1px solid rgba(0,0,0,.18);padding:14px 0;max-width:760px}
summary{cursor:pointer;font-weight:700}
details p{margin:10px 0 0}
.cta{background:var(--dark);color:#fff;text-align:center;padding:56px 0}
.cta h2{color:var(--orange)}
.cta p{margin-left:auto;margin-right:auto}
.cta .actions{justify-content:center}
.foot{background:var(--dark);color:#fff;padding:44px 0 28px;font-size:.95rem;border-top:1px solid rgba(255,255,255,.2)}
.foot a{color:#fff}
.foot h3{color:var(--orange)}
.fgrid{display:grid;gap:28px;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}
.foot ul{list-style:none;padding:0;margin:0}
.foot li{margin:0 0 6px}
.small{margin-top:28px;font-size:.88rem}
@media(max-width:700px){.btn{width:100%;text-align:center}.top .btn{width:auto}.sec{padding:40px 0}.hero{padding:48px 0 40px}.top{position:static}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
"""

CSS += """
.label{display:inline-block;font-size:.95rem;font-weight:600;color:var(--olive);margin:0 0 .8em;padding-left:14px;border-left:4px solid var(--orange)}
.hero .label{color:#fff}
.herogrid{display:grid;gap:36px;grid-template-columns:1.4fr 1fr;align-items:center}
.panel{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.25);border-radius:12px;padding:24px 26px}
.panel ul{list-style:none;padding:0;margin:0}
.panel li{padding:12px 0;border-bottom:1px solid rgba(255,255,255,.18)}
.panel li:last-child{border-bottom:0}
.panel strong{color:var(--orange)}
.by{font-size:.95rem;opacity:.9;margin-top:20px}
.why{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));margin-top:24px}
.why>div{background:#fff;border-radius:10px;padding:22px;box-shadow:0 1px 3px rgba(0,0,0,.12)}
.num{display:block;font-weight:800;color:var(--olive);margin-bottom:6px}
.scard{display:flex;flex-direction:column;background:#fff;border-radius:10px;padding:22px;text-decoration:none;box-shadow:0 1px 3px rgba(0,0,0,.12);border-top:5px solid var(--orange)}
.scard p{margin:0 0 12px;font-size:.96rem}
.scard .more{margin-top:auto;font-weight:700;color:var(--olive)}
.scard:hover{border-top-color:var(--olive)}
.media{margin:0;max-width:760px}
.media video,.media img{display:block;width:100%;height:auto;border-radius:10px;background:var(--soft);border:3px solid var(--orange)}
.media figcaption{font-size:.92rem;color:#333;padding-top:8px}
.media-sec{padding-bottom:0}

.profils{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));margin-top:24px}
.profil{display:flex;flex-direction:column;background:var(--soft);border-radius:10px;padding:22px;border-top:5px solid var(--olive)}
.profil h3{color:var(--olive);font-size:1.2rem}
.profil p{margin:0 0 10px;font-size:.96rem}
.profil ul{list-style:none;padding:0;margin:0 0 14px}
.profil li{padding:7px 0;border-bottom:1px solid rgba(0,0,0,.1)}
.profil li a{font-weight:600;text-decoration:none}
.profil li a:hover{color:var(--olive);text-decoration:underline}
.profil .more{margin-top:auto;font-weight:700;color:var(--olive);text-decoration:none}

.band{background:var(--dark);color:#fff;border-radius:14px;padding:36px}
.band h2{color:var(--orange)}
.band .label{color:#fff}
.band .btn{margin-top:6px}
.steps{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin:24px 0}
.steps div{border-left:4px solid var(--orange);padding:6px 0 6px 16px;font-weight:700}
.burger{display:none;background:#fff;border:2px solid var(--olive);border-radius:8px;font-size:1.3rem;padding:4px 12px;cursor:pointer}
.dd{position:relative}
.dd summary{cursor:pointer;font-weight:600;list-style:none;display:inline-flex;align-items:center;gap:7px}
.dd summary::-webkit-details-marker{display:none}
.dd summary::after{content:"";width:7px;height:7px;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:translateY(-2px) rotate(45deg)}
.dd details{border:0;padding:0;max-width:none;display:flex;align-items:center}
.dd details ul{position:absolute;top:100%;left:0;z-index:20;background:#fff;border:1px solid rgba(0,0,0,.15);border-radius:8px;box-shadow:0 6px 18px rgba(0,0,0,.15);padding:6px 0;margin:6px 0 0;min-width:232px;display:block;gap:0}
.dd details li a{display:block;padding:4px 16px;line-height:1.35;font-size:.88rem}
@media(max-width:1050px){.herogrid{grid-template-columns:1fr}.burger{display:block;margin-left:auto}.top nav{display:none;flex-basis:100%;order:3}.top nav.open{display:block}.top nav>ul{flex-direction:column;flex-wrap:wrap;gap:4px}.dd details{display:block}.dd details ul{position:static;box-shadow:none;border:0;padding:4px 0 4px 12px}}
"""

CSS += """
.logo{display:flex;align-items:center;gap:10px}
.logo img{height:48px;width:auto}.logo .logo-txt{height:62px}
.mascot{margin:0;background:var(--soft);border-radius:18px;padding:18px;text-align:center}
.mascot img{max-height:400px;width:auto;max-width:100%;height:auto}
.facts{font-weight:600}
@media(max-width:860px){.mascot img{max-height:260px}}
"""

CSS += """
.ico{display:inline-flex;align-items:center;justify-content:center;width:58px;height:58px;border-radius:50%;background:rgba(106,112,76,.14);margin-bottom:12px}
.ico svg{width:36px;height:36px;fill:none;stroke:var(--olive);stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.ico .a{stroke:var(--orange)}
.hero .ico{background:rgba(255,255,255,.12)}
.hero .ico svg{stroke:#fff}
"""

CSS += """
.cert{background:var(--soft);border-left:6px solid var(--orange);border-radius:10px;padding:26px 28px}
.cert .btn{margin-top:6px}
"""

AVIS_JS = """/* AVIS GOOGLE
   La note, le nombre d'avis et jusqu'a cinq avis sont relus sur la fiche
   Google via /api/avis. Si cette lecture echoue, le contenu de avis.json
   reste affiche. Aucun service externe, aucun cookie. */
var AVIS_SCRIPT_SRC = "";
var AVIS_HTML = "";
var AVIS_LIEN_FICHE = "https://maps.app.goo.gl/BEtwDMWG5gN9sgXv7"; /* votre fiche Google */
var AVIS_LIEN_GOOGLE = ""; /* lien « Laisser un avis » ; sinon construit depuis /api/avis */
var AVIS_JSON = "/avis.json";
var AVIS_MAX = 6;
(function () {
  var section = document.getElementById("avis");
  var mini = document.getElementById("avis-mini");
  if (!section && !mini) { return; }
  var box = document.getElementById("avis-widget");
  var minibox = document.getElementById("avis-widget-mini");
  if (section) { section.hidden = false; }
  if (mini) { mini.hidden = false; }
  if (box && AVIS_HTML) { box.innerHTML = AVIS_HTML; }
  if (AVIS_SCRIPT_SRC) { var sc = document.createElement("script"); sc.src = AVIS_SCRIPT_SRC; sc.async = true; document.body.appendChild(sc); }
  var f = document.getElementById("avis-fiche");
  if (f && AVIS_LIEN_FICHE) { f.href = AVIS_LIEN_FICHE; f.hidden = false; f.target = "_blank"; f.rel = "noopener"; }
  var a = document.getElementById("avis-lien");
  if (a && AVIS_LIEN_GOOGLE) { a.href = AVIS_LIEN_GOOGLE; a.hidden = false; a.target = "_blank"; a.rel = "noopener"; }
  var listeLocale = [];
  function el(tag, cls, txt) { var e = document.createElement(tag); if (cls) { e.className = cls; } if (txt !== undefined) { e.textContent = txt; } return e; }
  function etoiles(n) { n = Math.max(0, Math.min(5, Math.round(n))); var e = el("span", "avis-etoiles", "\u2605\u2605\u2605\u2605\u2605".slice(0, n) + "\u2606\u2606\u2606\u2606\u2606".slice(0, 5 - n)); e.setAttribute("role", "img"); e.setAttribute("aria-label", n + " \u00e9toiles sur 5"); return e; }
  var MOIS = ["janvier", "f\u00e9vrier", "mars", "avril", "mai", "juin", "juillet", "ao\u00fbt", "septembre", "octobre", "novembre", "d\u00e9cembre"];
  function dateFr(iso) {
    var p = String(iso || "").split("-");
    if (p.length !== 3) { return ""; }
    var j = parseInt(p[2], 10), m = parseInt(p[1], 10);
    if (!j || !m || !MOIS[m - 1]) { return ""; }
    return (j === 1 ? "1er" : j) + " " + MOIS[m - 1] + " " + p[0];
  }
  function resume(moy, total, maj) {
    var r = el("div", "avis-resume");
    r.appendChild(el("strong", "avis-note", moy.toFixed(1).replace(".", ",") + " / 5"));
    r.appendChild(etoiles(moy));
    r.appendChild(el("span", "avis-nb", total + " avis Google"));
    var jour = dateFr(maj);
    if (jour) { r.appendChild(el("span", "avis-maj", "mis \u00e0 jour le " + jour)); }
    return r;
  }
  function lien(txt, url, copie) {
    var l = el("a", null, txt);
    l.href = url; l.target = "_blank"; l.rel = "noopener nofollow";
    if (copie) { l.tabIndex = -1; }
    return l;
  }
  function carte(x, copie) {
    var c = el("blockquote", "avis-carte");
    if (copie) { c.setAttribute("aria-hidden", "true"); }
    var tete = el("div", "avis-tete");
    if (x.photo) {
      var img = document.createElement("img");
      img.className = "avis-photo"; img.src = x.photo; img.alt = "";
      img.width = 34; img.height = 34; img.loading = "lazy"; img.referrerPolicy = "no-referrer";
      tete.appendChild(img);
    }
    var nom = x.auteur || "Client";
    tete.appendChild(x.profil ? lien(nom, x.profil, copie) : el("span", null, nom));
    c.appendChild(tete);
    c.appendChild(etoiles(x.note));
    c.appendChild(el("p", "avis-texte", x.texte));
    var pied = el("footer", "avis-auteur");
    var bouts = [];
    if (x.date) { bouts.push(el("span", null, x.date)); }
    if (x.visite && x.visite.an) {
      bouts.push(el("span", null, "visite en " + (MOIS[x.visite.mois - 1] ? MOIS[x.visite.mois - 1] + " " : "") + x.visite.an));
    }
    if (x.lien) { bouts.push(lien("voir sur Google Maps", x.lien, copie)); }
    if (x.signalement) { bouts.push(lien("signaler", x.signalement, copie)); }
    bouts.forEach(function (e, i) {
      if (i) { pied.appendChild(document.createTextNode(" \u00b7 ")); }
      pied.appendChild(e);
    });
    c.appendChild(pied);
    return c;
  }
  function dessiner(moy, total, liste, maj) {
    if (AVIS_HTML) { return; }
    if (minibox) { minibox.innerHTML = ""; minibox.appendChild(resume(moy, total, maj)); }
    if (!box) { return; }
    box.innerHTML = "";
    box.appendChild(resume(moy, total, maj));
    if (!liste.length) { return; }
    var g = el("div", "avis-ban");
    g.setAttribute("role", "region"); g.setAttribute("aria-label", "Avis de mes clients");
    var piste = el("div", "avis-piste");
    var cartes = liste.slice(0, AVIS_MAX);
    cartes.forEach(function (x) { piste.appendChild(carte(x, false)); });
    cartes.forEach(function (x) { piste.appendChild(carte(x, true)); });
    piste.style.setProperty("--dur", Math.max(40, cartes.length * 14) + "s");
    g.appendChild(piste);
    box.appendChild(g);
    box.appendChild(el("p", "avis-aide", "Faites glisser les avis du doigt pour les parcourir."));
    var att = el("p", "avis-source");
    /* Logo officiel Google Maps, non modifie, hauteur 18 px, zone de
       degagement assuree en CSS : exige par les regles d'attribution. */
    var marque = document.createElement("img");
    marque.className = "avis-logo"; marque.src = "/google-maps.svg";
    marque.alt = "Google Maps"; marque.width = 98; marque.height = 18; marque.loading = "lazy";
    var enveloppe = document.createElement("a");
    enveloppe.href = AVIS_LIEN_FICHE; enveloppe.target = "_blank"; enveloppe.rel = "noopener";
    enveloppe.appendChild(marque);
    att.appendChild(enveloppe);
    att.appendChild(el("span", "avis-source-txt", "Avis class\u00e9s par pertinence, tels que Google les transmet. Google ne v\u00e9rifie pas les avis."));
    box.appendChild(att);
  }
  function rendre(data) {
    if (AVIS_HTML || !data || !data.avis || !data.avis.length) { return; }
    listeLocale = data.avis.filter(function (x) { return x && x.texte && x.note >= 1; });
    if (!listeLocale.length) { return; }
    var moy = data.note_moyenne > 0 ? data.note_moyenne : listeLocale.reduce(function (t, x) { return t + x.note; }, 0) / listeLocale.length;
    var total = data.nombre_total > 0 ? data.nombre_total : listeLocale.length;
    dessiner(moy, total, listeLocale, "");
  }
  /* Lecture en direct de la fiche Google (fonction Cloudflare).
     Si elle echoue, ce qui vient de avis.json reste affiche. */
  function majDirect() {
    if (!window.fetch) { return; }
    fetch("/api/avis", { cache: "no-store" }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
      if (!d || !d.ok || !(d.note > 0)) { return; }
      var liste = (d.avis && d.avis.length) ? d.avis : listeLocale;
      dessiner(d.note, d.total > 0 ? d.total : liste.length, liste, d.maj);
      if (a && !AVIS_LIEN_GOOGLE && d.fiche) {
        a.href = "https://search.google.com/local/writereview?placeid=" + encodeURIComponent(d.fiche);
        a.hidden = false; a.target = "_blank"; a.rel = "noopener";
      }
    }).catch(function () {});
  }
  if (!AVIS_HTML && typeof AVIS_DATA !== "undefined") { rendre(AVIS_DATA); majDirect(); }
  else if (!AVIS_HTML && AVIS_JSON && window.fetch) {
    fetch(AVIS_JSON, { cache: "no-store" }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) { rendre(d); majDirect(); }).catch(function () {});
  }
})();
"""

SITE_JS = """document.addEventListener("click",function(e){var b=e.target.closest(".burger");if(b){var n=b.parentNode.querySelector("nav");var o=n.classList.toggle("open");b.setAttribute("aria-expanded",o);return;}document.querySelectorAll(".dd details").forEach(function(x){if(!x.contains(e.target)){x.removeAttribute("open");}});});"""

if os.path.exists(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)
for path, d in P.items():
    folder = OUT + path
    os.makedirs(folder, exist_ok=True)
    open(os.path.join(folder, "index.html"), "w", encoding="utf-8").write(render(path, d))
open(OUT + "/style.css", "w", encoding="utf-8").write(CSS)
open(OUT + "/avis.js", "w", encoding="utf-8").write("var AVIS_DATA = " + open("/home/claude/assets/avis.json", encoding="utf-8").read() + ";\n" + AVIS_JS)
for _f in ("avis.json", "avis.exemple.json"):
    shutil.copy("/home/claude/assets/" + _f, OUT + "/" + _f)
_COM = {}
for _p in P:
    _m = re.match(r"^/deratisation-([a-z0-9-]+)/$", _p)
    if _m and P[_p].get("kind") == "ville":
        _nm = re.search(r" à (.+?)(?: \(|:|,|$)", P[_p]["h1"])
        if _nm:
            _COM[re.sub(r"\s+", " ", re.sub(r"['\-]", " ", unicodedata.normalize("NFD", _nm.group(1).lower())).encode("ascii", "ignore").decode()).strip()] = [_nm.group(1), _p]
ASST_JS = open("/home/claude/assets/assistant.js", encoding="utf-8").read().replace("/*COM*/{}", json.dumps(_COM, ensure_ascii=False))
SITE_JS = SITE_JS + ASST_JS

FORM_JS = """
document.addEventListener('submit',function(e){var f=e.target;if(!f||f.id!=='cform')return;e.preventDefault();
var m=document.getElementById('cform-msg'),b=f.querySelector('button[type=submit]');
function show(t,ok){m.hidden=false;m.className='cform-msg '+(ok?'ok':'ko');m.textContent=t;}
var req=f.querySelectorAll('[required]');for(var i=0;i<req.length;i++){if(!req[i].value.trim()){show('Merci de remplir tous les champs.',false);req[i].focus();return;}}
var em=f.querySelector('[type=email]');if(em.value.indexOf('@')<1){show('Merci de saisir une adresse e-mail valide.',false);em.focus();return;}
var hp=f.querySelector('[name=botcheck]');if(hp&&hp.checked){return;}
b.disabled=true;b.textContent='Envoi en cours...';
var d=new FormData(f);
fetch(f.dataset.endpoint,{method:'POST',body:d,headers:{'Accept':'application/json'}}).then(function(r){return r.json().catch(function(){return {};}).then(function(j){if(r.ok&&j.success===true){f.reset();show('Merci, votre demande est bien envoyée. Je vous réponds rapidement.',true);}else{throw new Error('x');}});}).catch(function(){show('Envoi impossible pour le moment. Appelez-moi au 06 64 57 66 55 ou écrivez à proxinuisibles53@gmail.com.',false);}).then(function(){b.disabled=false;b.textContent='Envoyer ma demande';});
});
"""
TOP_JS = """
(function(){var L=document.querySelectorAll('.toplink');if(!L.length)return;
var C=125.6,seuil=400,visible=false,tick=false;
function maj(){
  var doc=document.documentElement;
  var y=window.pageYOffset||doc.scrollTop;
  var max=(doc.scrollHeight-window.innerHeight)||1;
  var r=Math.min(1,Math.max(0,y/max));
  for(var i=0;i<L.length;i++){
    var p=L[i].querySelector('.tl-pg');
    if(p)p.style.strokeDashoffset=(C*(1-r)).toFixed(1);
  }
  var v=y>seuil;
  if(v!==visible){visible=v;
    for(var j=0;j<L.length;j++){(function(b){
      if(v){b.hidden=false;requestAnimationFrame(function(){b.classList.add('on');});}
      else{b.classList.remove('on');setTimeout(function(){if(!visible)b.hidden=true;},250);}
    })(L[j]);}}
  tick=false;}
window.addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(maj);}},{passive:true});
window.addEventListener('resize',function(){maj();},{passive:true});
for(var i=0;i<L.length;i++){L[i].addEventListener('click',function(){
  var doux=!window.matchMedia||!window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(doux){window.scrollTo({top:0,behavior:'smooth'});}else{window.scrollTo(0,0);}
});}
maj();})();
"""
SITE_JS = SITE_JS + FORM_JS + TOP_JS + SAISON_JS
CARTE_JS = """
(function(){var el=document.getElementById('carte');if(!el||typeof L==='undefined')return;
var tactile=window.matchMedia&&window.matchMedia('(pointer: coarse)').matches;
var m=L.map(el,{scrollWheelZoom:false,dragging:!tactile,tap:false,zoomSnap:0.25});
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:15,minZoom:7,attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'}).addTo(m);
var z=L.geoJSON(ZONE,{style:{color:'#6a704c',weight:3,fillColor:'#ff851b',fillOpacity:.28},
  onEachFeature:function(f,l){l.bindPopup('<strong>'+f.properties.nom+'</strong><br>J\u2019interviens dans toutes les communes.<br><a href="tel:+33664576655">06 64 57 66 55</a>');}}).addTo(m);
m.attributionControl.setPrefix('<a href="https://leafletjs.com">Leaflet</a>');m.fitBounds(z.getBounds(),{padding:[12,12]});
L.circleMarker([48.1136,-0.9703],{radius:9,color:'#fff',weight:3,fillColor:'#6a704c',fillOpacity:1}).addTo(m)
 .bindTooltip('Port-Brillet : mon point de départ',{direction:'top',offset:[0,-8]});
if(tactile){m.on('click',function(){m.dragging.enable();});}
})();
"""
open(OUT + "/site.js", "w", encoding="utf-8").write(SITE_JS)
for _f in ("logo.webp", "logo-petit.webp", "logo-texte.webp", "favicon.png", "favicon.ico", "apple-touch-icon.png", "icon-192.png", "icon-512.png", "google-maps.svg"):
    shutil.copy("/home/claude/assets/" + _f, OUT + "/" + _f)
os.makedirs(OUT + "/leaflet", exist_ok=True)
for _f in ("leaflet.js", "leaflet.css", "LICENSE.txt"):
    shutil.copy("/home/claude/assets/leaflet/" + _f, OUT + "/leaflet/" + _f)
open(OUT + "/carte.js", "w", encoding="utf-8").write("var ZONE = " + open("/home/claude/assets/zone.geojson", encoding="utf-8").read() + ";\n" + CARTE_JS)
os.makedirs(OUT + "/media", exist_ok=True)
for _f in os.listdir("/home/claude/assets/media"):
    shutil.copy("/home/claude/assets/media/" + _f, OUT + "/media/" + _f)
open(OUT + "/wrangler.jsonc", "w", encoding="utf-8").write('{\n  "name": "proxinuisibles",\n  "compatibility_date": "2026-11-02",\n  "assets": { "directory": "./" }\n}\n')
open(OUT + "/.assetsignore", "w", encoding="utf-8").write("wrangler.jsonc\n.assetsignore\n.git\nnode_modules\n")
open(OUT + "/robots.txt", "w").write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % BASE)
open(OUT + "/sitemap.xml", "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' +
    "".join("<url><loc>%s%s</loc><lastmod>%s</lastmod></url>" % (BASE, p, _TODAY) for p in P if p != "/mentions-legales/") + "</urlset>")

# empreinte de version sur les fichiers css/js : le navigateur recharge
# la nouvelle version des qu'un de ces fichiers change
import hashlib as _hl
_emp = {}
for _f in ("style.css", "site.js", "avis.js"):
    _emp[_f] = _hl.sha1(open(OUT + "/" + _f, "rb").read()).hexdigest()[:8]
for _path in P:
    _fp = OUT + _path + "index.html"
    _h = open(_fp, encoding="utf-8").read()
    for _f, _v in _emp.items():
        _h = _h.replace("'/%s'" % _f, "'/%s?v=%s'" % (_f, _v))
    open(_fp, "w", encoding="utf-8").write(_h)
print("empreintes:", _emp)

# vérification des liens internes
import re
bad = []
for path in P:
    html_ = open(OUT + path + "index.html", encoding="utf-8").read()
    for m in re.findall(r"href='(/[^']*)'", html_):
        if m in P:
            continue
        cible = m.split("#")[0].split("?")[0]
        if "." in cible.rsplit("/", 1)[-1]:   # fichier (css, ico, png, xml...) : on vérifie sur le disque
            if not os.path.exists(OUT + cible):
                bad.append((path, m))
            continue
        bad.append((path, m))
print("pages:", len(P), "liens cassés:", sorted(set(bad)))

os.makedirs("/mnt/user-data/outputs", exist_ok=True)
z = "/mnt/user-data/outputs/proxinuisibles-site.zip"
with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, _, files in os.walk(OUT):
        for f in files:
            full = os.path.join(root, f)
            zf.write(full, os.path.relpath(full, OUT))
print("zip ok")
