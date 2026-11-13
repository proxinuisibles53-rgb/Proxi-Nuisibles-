# -*- coding: utf-8 -*-
# Pages « prestation + commune » (longue traîne) pour : désinsectisation, chenilles processionnaires,
# taupier, dépigeonnage et piégeur agréé. Chaque page associe un paragraphe local propre à la commune,
# trois sections tirées d'un ensemble propre à la prestation (combinaison différente d'une page à l'autre),
# une section « Mon intervention » et trois questions fréquentes.
import itertools as _it

_SVV = {}   # service -> liste de (slug, nom, dep, (h2, texte local))

def _L(svc, slug, nom, dep, h2, txt):
    _SVV.setdefault(svc, []).append((slug, nom, dep, (h2, txt)))

# ======================= DÉSINSECTISATION =======================
_L("desinsectisation", "laval", "Laval", "53", "Les insectes dans les logements de Laval",
 "À Laval, une grande partie de mes interventions se passe dans les appartements du centre et des quartiers d'immeubles. Les cafards y circulent par les gaines techniques, les colonnes d'évacuation et les vide-ordures, d'un logement à l'autre. Les puces, elles, arrivent avec un animal ou restent après le départ d'un locataire.\nDans un immeuble, traiter un seul appartement ne suffit pas toujours : je vous dis si les logements voisins doivent être vus, et je fais un compte rendu utile au syndic ou au bailleur.")
_L("desinsectisation", "rennes", "Rennes", "35", "Copropriétés, commerces et restaurants à Rennes",
 "À Rennes, j'interviens surtout dans les copropriétés, les commerces et les cuisines professionnelles. Dans les immeubles collectifs, les blattes passent par les réseaux communs et un traitement isolé est vite rattrapé par les logements voisins.\nPour les restaurants et les commerces de bouche, j'organise le passage en dehors du service et je vous laisse un compte rendu écrit, utile lors d'un contrôle d'hygiène.")
_L("desinsectisation", "vitre", "Vitré", "35", "Maisons anciennes et entreprises à Vitré",
 "Le centre ancien de Vitré, avec ses maisons à pans de bois, ses caves et ses murs épais, offre beaucoup de cachettes aux insectes rampants : fissures, plinthes, dessous d'évier, conduits. Autour, les zones d'activité et les entreprises agroalimentaires demandent un suivi plus régulier.\nJe traite aussi bien un appartement du centre qu'un local professionnel, avec une méthode adaptée à ce que l'on stocke et à qui fréquente les lieux.")
_L("desinsectisation", "fougeres", "Fougères", "35", "Entre ville haute et ville basse",
 "Fougères mêle immeubles anciens, maisons de ville et commerces. Dans les bâtiments anciens, les fourmis et les blattes trouvent des passages dans les murs et sous les planchers, et reviennent d'une année sur l'autre si la source n'est pas atteinte.\nJe commence toujours par chercher par où arrivent les insectes, pour traiter là où ils vivent et pas seulement là où on les voit.")
_L("desinsectisation", "mayenne", "Mayenne", "53", "Le long de la rivière et dans le centre",
 "À Mayenne, les maisons du centre ancien et les immeubles proches de la rivière sont exposés à l'humidité, que recherchent beaucoup d'insectes rampants. Caves, buanderies et rez-de-chaussée sont les premières pièces touchées.\nJe vous conseille aussi sur ce qui entretient le problème : humidité, joints, nourriture accessible, passages autour des canalisations.")
_L("desinsectisation", "chateau-gontier", "Château-Gontier", "53", "Logements, commerces et collectivités",
 "À Château-Gontier-sur-Mayenne, j'interviens dans les logements, les commerces du centre et les bâtiments qui accueillent du public. Puces après le départ d'un animal, fourmis dans une cuisine, blattes dans un local de stockage : chaque cas demande son traitement.\nJe me déplace depuis Port-Brillet et je vous donne un tarif avant de venir, déplacement compris.")
_L("desinsectisation", "cesson-sevigne", "Cesson-Sévigné", "35", "Résidences et entreprises",
 "Cesson-Sévigné compte beaucoup de résidences récentes et de locaux d'entreprise. Les insectes y arrivent par les livraisons, les cartons, les déménagements ou les réseaux communs des bâtiments.\nPour une entreprise, je m'adapte à vos horaires et je vous indique les précautions à prendre pour le personnel avant et après le traitement.")
_L("desinsectisation", "saint-berthevin", "Saint-Berthevin", "53", "Tout près de ma base",
 "Saint-Berthevin est à une dizaine de kilomètres de Port-Brillet : c'est l'une des communes où je peux venir le plus vite. Entre lotissements, maisons avec jardin et zones d'activité, on m'appelle surtout pour des fourmis qui entrent par les terrasses et les seuils, et pour des puces chez les propriétaires d'animaux.\nJe traite l'intérieur et, si besoin, les abords de la maison, là où se trouve la colonie.")
_L("desinsectisation", "change", "Changé", "53", "Maisons récentes et jardins",
 "À Changé, beaucoup de maisons sont récentes, entourées de jardins et de haies. Les fourmis y nichent sous les dalles et les terrasses, puis entrent par les seuils, les plinthes et les passages de câbles.\nJe recherche le nid à l'extérieur quand c'est lui qui alimente l'invasion, plutôt que de traiter seulement les colonnes visibles dans la cuisine.")
_L("desinsectisation", "ernee", "Ernée", "53", "Bourg, fermes et dépendances",
 "Autour d'Ernée, maisons de bourg, fermes et dépendances se côtoient. Les mouches dans les bâtiments proches des élevages, les puces dans les maisons avec animaux et les fourmis dans les maisons anciennes sont les demandes les plus courantes.\nPour les mouches, je propose un badigeon appliqué à l'intérieur, qui protège toute la saison, de mai à décembre.")
_L("desinsectisation", "chateaubourg", "Châteaubourg", "35", "Entre Rennes et Vitré",
 "Châteaubourg mêle lotissements, maisons de bourg et zones d'activité le long de l'axe Rennes-Vitré. J'y traite des logements comme des locaux professionnels, avec des produits choisis selon les lieux et les personnes présentes.\nPour les professionnels, je propose un suivi avec compte rendu écrit après chaque passage.")
_L("desinsectisation", "la-guerche-de-bretagne", "La Guerche-de-Bretagne", "35", "Centre ancien et campagne",
 "À La Guerche-de-Bretagne, les maisons du centre ancien et les fermes des alentours n'ont pas les mêmes problèmes : blattes et fourmis dans les bâtiments anciens, mouches autour des élevages.\nJe me déplace depuis Port-Brillet, avec un tarif annoncé avant de venir, déplacement compris.")

# ======================= CHENILLES PROCESSIONNAIRES =======================
_L("chenilles-processionnaires", "laval", "Laval", "53", "Pins et chênes des jardins lavallois",
 "À Laval, les chenilles processionnaires touchent surtout les pins des jardins privés, des résidences et des espaces verts, ainsi que certains chênes. Un cocon repéré dans un jardin de quartier concerne vite les voisins, car les chenilles descendent et se déplacent au sol.\nJe vous conseille sur le moment d'intervenir selon l'arbre et la saison, et j'interviens avec une protection complète.")
_L("chenilles-processionnaires", "rennes", "Rennes", "35", "Résidences, écoles et espaces verts",
 "À Rennes, les demandes viennent souvent des copropriétés, des écoles et des gestionnaires d'espaces verts, là où passent des enfants et des chiens. Un pin dans une cour de résidence suffit pour exposer de nombreux habitants aux poils urticants.\nJe propose des pièges sur les troncs, la coupe des cocons en hiver et, sur les chênes, le retrait à l'aspirateur sans insecticide.")
_L("chenilles-processionnaires", "vitre", "Vitré", "35", "Jardins et propriétés autour de Vitré",
 "Autour de Vitré, les pins et les chênes des propriétés, des haies et des bords de chemins peuvent héberger des cocons. Les chenilles sont visibles au moment de leur descente, mais le cocon, lui, se repère souvent dès l'hiver dans la cime.\nPlus on agit tôt, plus l'intervention est simple : appelez-moi dès que vous voyez un cocon blanc et soyeux.")
_L("chenilles-processionnaires", "cesson-sevigne", "Cesson-Sévigné", "35", "Espaces verts et sites d'entreprise",
 "À Cesson-Sévigné, de nombreux sites d'entreprise et de résidences sont plantés d'arbres d'ornement. Une procession sur un cheminement ou près d'une aire de pause expose le personnel et les visiteurs.\nJ'interviens pour les gestionnaires de sites comme pour les particuliers, avec une méthode sans insecticide sur les chênes.")
_L("chenilles-processionnaires", "saint-berthevin", "Saint-Berthevin", "53", "Lotissements et jardins arborés",
 "Saint-Berthevin compte de nombreux jardins plantés de pins et de conifères. C'est souvent en promenant le chien ou en tondant qu'on découvre une procession au pied d'un arbre.\nJe suis installé à une dizaine de kilomètres : je peux venir poser des pièges ou couper les cocons rapidement.")
_L("chenilles-processionnaires", "change", "Changé", "53", "Bords de Mayenne et jardins",
 "À Changé, les jardins arborés et les espaces verts proches de la Mayenne sont fréquentés par les familles et les promeneurs avec leur chien. Un cocon dans un pin de jardin peut gêner tout un quartier au moment des processions.\nJe vous indique ce qu'il faut faire en attendant mon passage : tenir les enfants et les animaux à distance et ne pas toucher au cocon.")
_L("chenilles-processionnaires", "l-huisserie", "L'Huisserie", "53", "Coteaux boisés et jardins",
 "L'Huisserie est bordée par la vallée de la Mayenne et des coteaux boisés. Les chênes et les pins des jardins et des lisières peuvent accueillir des cocons, parfois haut dans l'arbre.\nSur les chênes, je retire les cocons à l'aspirateur, sans aucun insecticide, et je les évacue dans un sac fermé.")
_L("chenilles-processionnaires", "chateaubourg", "Châteaubourg", "35", "Jardins et lotissements",
 "À Châteaubourg, les pins plantés en haie ou en isolé dans les jardins des lotissements sont les arbres les plus souvent touchés. Le cocon se voit l'hiver : une boule blanche et soyeuse au bout des branches.\nC'est le bon moment pour le couper, avant que les chenilles n'en sortent.")
_L("chenilles-processionnaires", "mayenne", "Mayenne", "53", "Jardins de ville et campagne",
 "À Mayenne et autour, les cocons se trouvent dans les pins des jardins, des parcs et des bords de route, et dans les chênes des haies bocagères. Les chiens qui fouillent le sol au printemps sont particulièrement exposés.\nJe pose des pièges sur les troncs pour intercepter les chenilles lors de leur descente.")
_L("chenilles-processionnaires", "port-brillet", "Port-Brillet", "53", "Chez moi, à Port-Brillet",
 "Port-Brillet est la commune où je suis installé. Les pins des jardins et les chênes des bois et des haies alentour sont concernés chaque année.\nJe peux passer rapidement pour un diagnostic, poser des pièges sur les troncs ou couper les cocons en hiver.")

# ======================= TAUPIER =======================
_L("taupier", "laval", "Laval", "53", "Pelouses et jardins à Laval",
 "À Laval, on m'appelle surtout pour des pelouses de maisons individuelles, des jardins familiaux et des espaces verts. Quelques taupinières suffisent à abîmer une pelouse et à gêner la tonte.\nJe repère les galeries actives et je pose des pièges, puis je repasse jusqu'à ce que la taupe soit prise.")
_L("taupier", "vitre", "Vitré", "35", "Jardins, prairies et terrains autour de Vitré",
 "Autour de Vitré, les taupes touchent aussi bien les jardins des lotissements que les prairies des exploitations. Dans un pré de fauche, la terre des taupinières se retrouve dans le fourrage.\nJ'adapte le nombre de pièges et la fréquence des passages à la surface à traiter.")
_L("taupier", "saint-berthevin", "Saint-Berthevin", "53", "Lotissements et grands jardins",
 "Saint-Berthevin compte de nombreux jardins engazonnés, souvent bordés de haies et de champs. Les taupes y entrent depuis les parcelles voisines.\nJe suis installé à une dizaine de kilomètres, ce qui me permet de revenir relever les pièges souvent, sans frais de déplacement en plus.")
_L("taupier", "change", "Changé", "53", "Pelouses et terrains de sport",
 "À Changé, les jardins des maisons et les espaces engazonnés sont les terrains les plus touchés. Sur un terrain de sport ou une aire de jeux, les taupinières posent aussi un problème de sécurité.\nJ'interviens pour les particuliers comme pour les gestionnaires de terrains.")
_L("taupier", "ernee", "Ernée", "53", "Prairies et exploitations",
 "Autour d'Ernée, les demandes viennent surtout des exploitations agricoles et des grandes propriétés. Les taupinières gênent la fauche et salissent le fourrage.\nSur une prairie, je travaille par zones, en commençant par les galeries les plus actives.")
_L("taupier", "loiron-ruille", "Loiron-Ruillé", "53", "Jardins de bourg et parcelles",
 "À Loiron-Ruillé, à quelques kilomètres de Port-Brillet, j'interviens dans les jardins du bourg comme sur les parcelles agricoles. Les taupes passent facilement des champs vers les jardins.\nJe peux venir vite et repasser souvent pour relever les pièges.")
_L("taupier", "le-genest-saint-isle", "Le Genest-Saint-Isle", "53", "Entre bourg et campagne",
 "Au Genest-Saint-Isle, les maisons avec jardin côtoient les prés et les champs. Une taupe installée dans un pré voisin finit souvent par gagner la pelouse.\nJe pose des pièges sur les galeries actives et je vous explique comment repérer une nouvelle arrivée.")
_L("taupier", "chateaubourg", "Châteaubourg", "35", "Pelouses des lotissements",
 "À Châteaubourg, les lotissements récents sont souvent construits en bordure de champs, d'où arrivent les taupes. Une pelouse neuve, à la terre meuble, est particulièrement exposée.\nJe traite le terrain et je vous indique où surveiller les nouvelles taupinières.")
_L("taupier", "argentre-du-plessis", "Argentré-du-Plessis", "35", "Jardins et prairies",
 "À Argentré-du-Plessis, j'interviens dans les jardins du bourg et sur les prairies des exploitations. Plus on intervient tôt, moins le réseau de galeries est étendu.\nJe vous donne un tarif avant de venir, déplacement compris.")
_L("taupier", "port-brillet", "Port-Brillet", "53", "Chez moi, à Port-Brillet",
 "Port-Brillet est la commune où je suis installé : je peux passer très vite et relever les pièges aussi souvent que nécessaire.\nJardins, pelouses, prairies : j'adapte la pose au terrain.")

# ======================= DÉPIGEONNAGE =======================
_L("depigeonnage", "laval", "Laval", "53", "Façades et toitures du centre de Laval",
 "Dans le centre de Laval, les pigeons se posent sur les corniches, les rebords de fenêtres, les toitures et les balcons des immeubles. Les fientes salissent les façades et les trottoirs et bouchent les gouttières.\nJe propose des pics, des filets ou des câbles selon le bâtiment, et un piégeage en cage quand une colonie est déjà bien installée.")
_L("depigeonnage", "rennes", "Rennes", "35", "Immeubles, balcons et commerces",
 "À Rennes, les demandes viennent surtout des copropriétés et des commerces : balcons envahis, enseignes souillées, cours intérieures où les pigeons nichent. Sur un immeuble, la solution doit être discrète et durable.\nJe fournis un devis détaillé, utile au syndic pour faire décider les travaux.")
_L("depigeonnage", "vitre", "Vitré", "35", "Bâti ancien et toitures",
 "Le bâti ancien de Vitré, avec ses toitures, ses lucarnes et ses corniches, offre beaucoup de points de pose et de nidification aux pigeons. Les protections doivent respecter l'aspect des façades.\nJe choisis des dispositifs discrets et adaptés au support.")
_L("depigeonnage", "fougeres", "Fougères", "35", "Ville haute et bâtiments anciens",
 "À Fougères, les toitures et les façades anciennes du centre attirent les pigeons, qui s'installent sous les avancées de toit et dans les ouvertures. Les fientes abîment la pierre et le zinc.\nJe protège les points de pose et je ferme les accès aux combles et aux greniers.")
_L("depigeonnage", "mayenne", "Mayenne", "53", "Quais, centre ancien et bâtiments publics",
 "À Mayenne, les pigeons se regroupent dans le centre ancien et près de la rivière, sur les toitures, les rebords et les bâtiments publics. Une fois installés, ils reviennent chaque jour au même endroit.\nJe combine protections et, si nécessaire, piégeage en cage pour réduire la colonie.")
_L("depigeonnage", "chateau-gontier", "Château-Gontier", "53", "Centre ancien et entrepôts",
 "À Château-Gontier-sur-Mayenne, j'interviens sur les façades du centre comme sur les entrepôts et les bâtiments d'activité, où les pigeons nichent dans les charpentes.\nDans un bâtiment de stockage, les fientes posent aussi un problème d'hygiène pour les marchandises.")
_L("depigeonnage", "ernee", "Ernée", "53", "Hangars et bâtiments agricoles",
 "Autour d'Ernée, les pigeons s'installent souvent dans les hangars, les stabulations et les silos, attirés par le grain. Les fientes souillent le matériel et les stocks.\nJe pose des filets sous les charpentes et je peux mettre en place un piégeage en cage pour réduire une colonie installée.")
_L("depigeonnage", "craon", "Craon", "53", "Bourg et bâtiments d'activité",
 "À Craon, les pigeons se posent sur les toitures du bourg et s'installent dans les bâtiments d'activité et les dépendances. Plus la colonie est ancienne, plus elle est difficile à déloger.\nJe me déplace depuis Port-Brillet et je vous donne un tarif avant de venir.")

# ======================= PIÉGEUR AGRÉÉ =======================
_L("piegeur-agree", "laval", "Laval", "53", "Fouines dans les combles à Laval",
 "À Laval, l'essentiel de mes interventions de piégeage concerne des fouines installées dans les combles des maisons et des immeubles. Bruits de course la nuit, isolation tassée, odeur : les signes ne trompent pas longtemps.\nPrès de la Mayenne et des plans d'eau, on m'appelle aussi pour des ragondins qui creusent les berges.")
_L("piegeur-agree", "vitre", "Vitré", "35", "Maisons anciennes et étangs",
 "Autour de Vitré, les maisons anciennes, les granges et les dépendances sont des abris de choix pour les fouines. Les étangs et les cours d'eau du secteur attirent ragondins et rats musqués.\nJe repère les passages avant de poser le moindre piège, et je vous indique les accès à fermer.")
_L("piegeur-agree", "ernee", "Ernée", "53", "Fermes, poulaillers et plans d'eau",
 "Autour d'Ernée, les demandes viennent des fermes et des maisons de campagne : fouines dans les granges et les poulaillers, ragondins dans les mares et les fossés.\nJe vous conseille aussi sur la protection des volailles, pour éviter qu'un autre animal ne reprenne la place.")
_L("piegeur-agree", "port-brillet", "Port-Brillet", "53", "Chez moi, à Port-Brillet",
 "Port-Brillet est ma commune. Étangs, bois et maisons anciennes : le secteur réunit tout ce qu'aiment les fouines et les ragondins.\nJe peux venir vite et relever les pièges dans le respect de la réglementation.")
_L("piegeur-agree", "loiron-ruille", "Loiron-Ruillé", "53", "Bourg, fermes et dépendances",
 "À Loiron-Ruillé, j'interviens pour des fouines dans les combles et les dépendances, et pour des ragondins près des mares et des fossés. La commune est à quelques kilomètres de Port-Brillet.\nJe peux relever les pièges souvent, sans frais de déplacement en plus.")
_L("piegeur-agree", "saint-pierre-la-cour", "Saint-Pierre-la-Cour", "53", "Maisons et bâtiments ruraux",
 "À Saint-Pierre-la-Cour, voisine de Port-Brillet, les fouines s'installent dans les greniers, les garages et les granges. Sur les voitures garées dehors, elles peuvent ronger durites et câbles.\nJe confirme d'abord l'animal en cause, puis je choisis le piège adapté.")
_L("piegeur-agree", "chateau-gontier", "Château-Gontier", "53", "Bords de Mayenne et maisons de ville",
 "À Château-Gontier-sur-Mayenne, les berges de la rivière et les plans d'eau attirent les ragondins, et les combles des maisons de ville abritent souvent des fouines.\nJ'interviens pour les particuliers, les copropriétés et les collectivités.")
_L("piegeur-agree", "mayenne", "Mayenne", "53", "Rivière, berges et combles",
 "À Mayenne, la rivière et ses berges sont un milieu favorable aux ragondins et aux rats musqués, qui creusent et fragilisent les rives. En ville, les fouines profitent des combles des maisons anciennes.\nJe pose et relève les pièges dans le respect des arrêtés en vigueur en Mayenne.")
_L("piegeur-agree", "argentre-du-plessis", "Argentré-du-Plessis", "35", "Maisons, fermes et étangs",
 "À Argentré-du-Plessis, j'interviens pour des fouines dans les combles et les bâtiments agricoles, et pour des ragondins autour des étangs et des fossés.\nJe m'appuie sur les arrêtés en vigueur en Ille-et-Vilaine pour les espèces et les périodes.")
_L("piegeur-agree", "cosse-le-vivien", "Cossé-le-Vivien", "53", "Campagne et plans d'eau",
 "Autour de Cossé-le-Vivien, les fermes, les granges et les plans d'eau réunissent fouines et ragondins. Les poulaillers sont souvent la première cible.\nJe vous explique comment protéger vos volailles et fermer les accès après le piégeage.")


# ======================= CONTENU PAR PRESTATION =======================
_SVC_DEF = {
 "desinsectisation": dict(
  court="Désinsectisation", stype="Désinsectisation",
  h1="Désinsectisation à %(nom)s (%(dep)s) : cafards, fourmis, puces et mouches",
  titres=["Désinsectisation %(nom)s (%(dep)s) | Proxinuisibles", "Désinsectisation %(nom)s | Proxinuisibles", "Désinsectisation %(nom)s"],
  metas=["Désinsectisation à %(nom)s (%(dep)s) : cafards, blattes, fourmis, puces et mouches. Traitement ciblé, devis gratuit, déplacement compris.",
         "Désinsectisation à %(nom)s (%(dep)s) : cafards, fourmis, puces, mouches. Devis gratuit."],
  leads=["Cafards dans la cuisine, fourmis qui reviennent, puces après le départ d'un animal : à %(nom)s, j'identifie l'insecte avant de traiter, puis je vous explique comment éviter son retour.",
         "À %(nom)s, je traite les insectes rampants et volants chez les particuliers et les professionnels : blattes, fourmis, puces et mouches. Devis gratuit, déplacement compris."],
  pool=[("Identifier l'insecte avant de traiter", "Chaque insecte a ses habitudes et sa méthode de traitement. Une blatte germanique ne se traite pas comme une blatte orientale, et une fourmi qui niche dans un mur ne se traite pas comme une fourmi qui vient du jardin.\nJe commence donc par identifier l'espèce et par chercher où elle vit et par où elle passe. C'est ce qui permet un traitement ciblé, avec moins de produit et un meilleur résultat."),
        ("Cafards et blattes", "Les blattes se cachent le jour derrière les appareils électroménagers, sous les éviers, dans les gaines et les colonnes techniques. Elles sortent la nuit et se multiplient vite.\nJe traite le plus souvent avec un gel appâtant, posé en petits points dans les cachettes : les blattes le consomment et le ramènent dans leur abri. Voir aussi ma page <a href='/blattes-cafards/'>blattes et cafards</a>."),
        ("Fourmis : remonter jusqu'à la colonie", "Les fourmis que l'on voit dans la cuisine ne sont qu'une petite partie de la colonie. Si on se contente de les tuer, d'autres prennent la relève.\nJe suis leur trajet jusqu'au point d'entrée et, quand c'est possible, jusqu'au nid. J'utilise des appâts que les ouvrières rapportent à la colonie. Voir aussi ma page <a href='/fourmis/'>fourmis</a>."),
        ("Puces : traiter le logement et l'animal", "Les puces adultes ne sont qu'une partie du problème : les œufs et les larves se cachent dans les tapis, les canapés, les plinthes et le panier de l'animal.\nJe traite le logement pendant que vous faites traiter l'animal par votre vétérinaire. Je vous explique comment préparer les pièces avant mon passage. Voir aussi ma page <a href='/puces/'>puces</a>."),
        ("Mouches : le badigeon pour toute la saison", "Dans une maison, une dépendance ou un bâtiment proche d'un élevage, je propose un badigeon appliqué à l'intérieur, sur les surfaces où les mouches se posent. Il protège toute la saison, de mai à décembre.\nC'est plus simple que des pulvérisations répétées. Voir aussi ma page <a href='/mouches/'>mouches</a>."),
        ("Logement, commerce ou local professionnel", "Dans un logement, je vous dis à l'avance s'il faut quitter les lieux et pendant combien de temps. Dans un commerce ou un restaurant, je m'organise pour intervenir en dehors des heures d'ouverture.\nPour les professionnels, je laisse un compte rendu écrit après chaque passage.")],
  fin=["Appelez-moi et décrivez ce que vous voyez : un insecte, des traces, l'endroit où vous les trouvez. Une photo m'aide à identifier l'espèce.\nJe vous donne un tarif avant de venir, déplacement compris, et j'interviens à %(nom)s en général sous 24 à 48 heures. Je suis joignable de 8h à 21h en semaine et de 9h à 18h le week-end.",
       "À %(nom)s, l'intervention commence par un échange au téléphone : je vous pose quelques questions pour savoir de quel insecte il s'agit et quelle surface traiter.\nVous recevez un prix clair, déplacement compris. Sur place, je traite, je vous explique les précautions à prendre et je vous dis si un second passage est utile.",
       "Je me déplace à %(nom)s depuis Port-Brillet. Sur place, j'identifie l'insecte, je repère les cachettes et j'applique le traitement adapté.\nJe suis titulaire du Certibiocide et je vous laisse des conseils simples pour éviter le retour des insectes. Je prends la carte bancaire, les espèces, les chèques et les virements."],
  faq=[("Dois-je quitter mon logement pendant le traitement ?", "Cela dépend du traitement. Avec un gel appâtant, ce n'est généralement pas nécessaire ; avec une pulvérisation, il faut parfois quitter les lieux quelques heures. Je vous le précise avant l'intervention."),
       ("Combien de passages faut-il ?", "Souvent un seul, parfois deux pour atteindre les insectes qui éclosent après le premier traitement. Je vous le dis dès le devis."),
       ("Le traitement est-il compatible avec mes animaux ?", "Je vous indique les précautions à prendre selon le produit utilisé : éloigner l'animal, couvrir l'aquarium, attendre avant de rouvrir une pièce."),
       ("Pourquoi les fourmis reviennent-elles ?", "Parce que la colonie n'a pas été atteinte. Je cherche le nid ou j'utilise des appâts que les ouvrières y rapportent."),
       ("Intervenez-vous pour les professionnels ?", "Oui : restaurants, commerces, locaux d'entreprise et bâtiments agricoles, avec un compte rendu écrit après chaque passage.")]),

 "chenilles-processionnaires": dict(
  court="Chenilles processionnaires", stype="Traitement des chenilles processionnaires",
  h1="Chenilles processionnaires à %(nom)s (%(dep)s) : pièges et retrait des cocons",
  titres=["Chenilles Processionnaires %(nom)s (%(dep)s)", "Chenilles Processionnaires %(nom)s", "Processionnaires %(nom)s | Proxinuisibles"],
  metas=["Chenilles processionnaires à %(nom)s (%(dep)s) : pièges sur les troncs, coupe des cocons, aspiration sans insecticide sur les chênes. Devis gratuit.",
         "Chenilles processionnaires à %(nom)s (%(dep)s) : pièges, coupe des cocons, devis gratuit."],
  leads=["Un cocon blanc dans un pin, une file de chenilles au pied d'un arbre : à %(nom)s, je pose des pièges sur les troncs, je coupe les cocons et, sur les chênes, je les retire à l'aspirateur, sans insecticide.",
         "À %(nom)s, je traite les chenilles processionnaires du pin et du chêne chez les particuliers, dans les résidences, les écoles et les espaces verts. Ne touchez pas aux cocons : appelez-moi."],
  pool=[("Processionnaire du pin ou du chêne ?", "La processionnaire du pin tisse en hiver des cocons blancs et soyeux au bout des branches. Les chenilles en descendent à la fin de l'hiver ou au printemps, en file, pour s'enfouir dans le sol.\nLa processionnaire du chêne vit en colonies sur le tronc et les branches des chênes, plus tard dans la saison. Les deux portent des poils urticants. Je vous dis de quelle espèce il s'agit et quand intervenir."),
        ("Les pièges posés sur le tronc", "Je pose autour du tronc un piège qui intercepte les chenilles au moment de leur descente. Elles sont recueillies dans un sac, sans atteindre le sol, la pelouse ou vos animaux.\nJe règle la pose pour qu'elle soit bien étanche autour de l'écorce, puis je reviens retirer le dispositif à la fin de la période de descente."),
        ("La coupe des cocons en hiver", "Quand les cocons sont visibles et accessibles, je les coupe en hiver, avant que les chenilles n'en sortent. Je coupe le cocon avec la branche qui le porte et je le place dans un sac fermé pour le détruire.\nJe porte une protection complète : les poils urticants se dispersent au moindre geste."),
        ("Sur les chênes, l'aspirateur sans insecticide", "Sur les chênes, je retire les cocons et les chenilles avec un aspirateur, sans aucun insecticide. Rien n'est répandu dans le jardin, près des enfants, des animaux ou d'une aire de jeux.\nLes cocons et les chenilles sont récupérés pour être détruits, au lieu de tomber au sol."),
        ("Un vrai danger pour les enfants et les chiens", "Les poils des chenilles provoquent des démangeaisons, des irritations des yeux et parfois des gênes respiratoires. Ils restent urticants longtemps, même dans un cocon abandonné.\nLes chiens sont particulièrement exposés, car ils flairent et lèchent les chenilles. Si votre chien a été en contact, appelez sans attendre un vétérinaire."),
        ("Particuliers, écoles et collectivités", "J'interviens dans les jardins des particuliers, les résidences, les écoles, les campings, les aires de jeux et les espaces verts communaux.\nPour un site qui accueille du public, je vous aide à organiser les interventions d'une année sur l'autre, car un arbre touché l'est souvent à nouveau.")],
  fin=["Envoyez-moi une photo du cocon ou des chenilles, prise à distance : je vous dis de quelle espèce il s'agit et quelle solution convient.\nJe vous donne un tarif avant de venir, déplacement compris, et j'interviens à %(nom)s avec une protection complète. Je suis joignable de 8h à 21h en semaine et de 9h à 18h le week-end.",
       "À %(nom)s, je viens voir l'arbre et je vous propose la méthode adaptée : pièges, coupe des cocons ou aspiration.\nLe devis est gratuit et le déplacement compris. En attendant mon passage, gardez enfants et animaux à distance et ne touchez à rien.",
       "Je me déplace à %(nom)s depuis Port-Brillet. Je vous annonce le prix avant de venir, puis j'interviens et j'évacue les cocons dans des sacs fermés.\nJe vous indique aussi quand repasser l'année suivante, car un arbre touché l'est souvent de nouveau."],
  faq=[("Mon chien a touché une chenille, que faire ?", "Appelez sans attendre un vétérinaire : c'est une urgence."),
       ("Puis-je couper le cocon moi-même ?", "Non : les poils se dispersent et provoquent de fortes irritations. Faites appel à un professionnel équipé."),
       ("À quelle période faut-il intervenir ?", "La coupe des cocons de la processionnaire du pin se fait en hiver ; les pièges se posent avant la descente des chenilles. Je vous précise le bon moment lors du devis."),
       ("Utilisez-vous des insecticides ?", "Mes méthodes sont mécaniques : pièges, coupe des cocons et aspiration. Sur les chênes, je n'utilise aucun insecticide."),
       ("Les chenilles reviennent-elles chaque année ?", "Souvent, oui : un arbre touché attire de nouveau les papillons. Un suivi d'une année sur l'autre permet de garder la situation sous contrôle.")]),

 "taupier": dict(
  court="Taupier", stype="Piégeage des taupes",
  h1="Taupier à %(nom)s (%(dep)s) : piégeage des taupes",
  titres=["Taupier %(nom)s (%(dep)s) | Proxinuisibles", "Taupier %(nom)s | Proxinuisibles", "Taupier %(nom)s"],
  metas=["Taupier à %(nom)s (%(dep)s) : piégeage des taupes dans les jardins, pelouses, terrains de sport et prairies. Devis gratuit, déplacement compris.",
         "Taupier à %(nom)s (%(dep)s) : piégeage des taupes, devis gratuit."],
  leads=["Des taupinières dans la pelouse, le potager ou la prairie ? À %(nom)s, je piège les taupes : c'est la méthode la plus fiable pour retrouver un terrain propre.",
         "À %(nom)s, je débarrasse jardins, pelouses, terrains de sport et prairies des taupes par piégeage. Devis gratuit, déplacement compris."],
  pool=[("Repérer les galeries actives", "Toutes les taupinières ne se valent pas : certaines sont anciennes, d'autres montrent une galerie encore utilisée. Je repère les galeries actives et les axes de passage avant de poser le moindre piège.\nC'est ce travail de repérage qui fait la différence entre un piégeage rapide et des semaines d'essais."),
        ("Le piégeage, la méthode la plus fiable", "Je pose des pièges dans les galeries actives, puis je repasse les relever. Je poursuis jusqu'à ce que les taupes soient prises et que de nouvelles taupinières n'apparaissent plus.\nLe nombre de passages dépend de la surface et du nombre d'animaux. Je vous le précise dès le devis."),
        ("Pourquoi les répulsifs ne suffisent pas", "Les répulsifs, les vibrations ou les produits versés dans les galeries déplacent souvent la taupe de quelques mètres, ou chez le voisin, sans régler le problème.\nLe piégeage, lui, retire l'animal du terrain."),
        ("Jardins, pelouses et potagers", "Dans un jardin, quelques taupes suffisent à bouleverser une pelouse, à soulever des semis et à gêner la tonte.\nJe pose les pièges de façon à abîmer le moins possible le terrain, et je vous explique comment repérer une nouvelle arrivée."),
        ("Prairies et parcelles agricoles", "Sur une prairie, les taupinières gênent la fauche, usent le matériel et mélangent de la terre au fourrage.\nJe travaille par zones, en commençant par les plus touchées, et j'adapte la fréquence des passages à la surface."),
        ("Terrains de sport et espaces publics", "Sur un terrain de sport, un golf ou une aire de jeux, les taupinières abîment la surface et peuvent provoquer des chutes.\nJ'interviens pour les communes, les clubs et les gestionnaires de terrains, avec un calendrier de passages.")],
  fin=["Appelez-moi et décrivez votre terrain : surface, nombre de taupinières, depuis quand elles apparaissent. Une photo m'aide à préparer l'intervention.\nJe vous donne un tarif avant de venir, déplacement compris, et j'interviens à %(nom)s en général sous 24 à 48 heures.",
       "À %(nom)s, je viens voir le terrain, je repère les galeries actives et je pose les pièges. Je repasse ensuite les relever.\nLe devis est gratuit et le déplacement compris. Je suis joignable de 8h à 21h en semaine et de 9h à 18h le week-end.",
       "Je me déplace à %(nom)s depuis Port-Brillet. Je vous annonce le prix avant de venir et le nombre de passages prévus.\nJe prends la carte bancaire, les espèces, les chèques et les virements."],
  faq=[("Combien de temps dure le traitement ?", "Quelques passages, étalés selon la surface et le nombre de taupes."),
       ("Pourquoi ne pas utiliser des répulsifs ?", "Ils déplacent souvent le problème chez le voisin sans l'éliminer."),
       ("Intervenez-vous en hiver ?", "Oui : la taupe ne dort pas l'hiver et reste active toute l'année."),
       ("Les taupes peuvent-elles revenir ?", "Oui, d'autres taupes peuvent arriver des terrains voisins. Je vous explique comment repérer une nouvelle arrivée pour intervenir tôt."),
       ("Est-ce forcément une taupe ?", "Pas toujours : d'autres petits animaux creusent aussi des galeries. Je vérifie sur place avant de poser les pièges.")]),

 "depigeonnage": dict(
  court="Dépigeonnage", stype="Dépigeonnage",
  h1="Dépigeonnage à %(nom)s (%(dep)s) : protections et piégeage",
  titres=["Dépigeonnage %(nom)s (%(dep)s) | Proxinuisibles", "Dépigeonnage %(nom)s | Proxinuisibles", "Dépigeonnage %(nom)s"],
  metas=["Dépigeonnage à %(nom)s (%(dep)s) : pics, filets, câbles et piégeage en cage pour façades, toitures et bâtiments. Devis gratuit.",
         "Dépigeonnage à %(nom)s (%(dep)s) : pics, filets, câbles, piégeage. Devis gratuit."],
  leads=["Pigeons sur le toit, le balcon ou dans le hangar : à %(nom)s, je pose pics, filets et câbles et, si une colonie est installée, je mets en place un piégeage en cage.",
         "À %(nom)s, je protège façades, toitures, balcons et bâtiments contre les pigeons, pour les particuliers, les copropriétés, les commerces et les exploitations."],
  pool=[("Pics, filets et câbles", "- Pics sur les rebords, les corniches et les enseignes\n- Filets sur les ouvertures, les balcons et sous les charpentes\n- Câbles tendus sur les poutres, les acrotères et les garde-corps\nJe choisis la solution selon le bâtiment et l'endroit où les pigeons se posent."),
        ("Le piégeage en cage", "Quand une colonie est déjà bien installée, les protections seules ne suffisent pas toujours. Je pose des cages de capture : l'oiseau entre attiré par la nourriture et ne peut plus ressortir.\nLe piégeage vise les pigeons domestiques et les pigeons de ville. Il ne concerne pas le pigeon ramier, dont le piégeage est interdit. Voir aussi ma page <a href='/depigeonnage/'>dépigeonnage</a>."),
        ("Les dégâts des fientes", "Les fientes salissent les façades, les balcons et les trottoirs, abîment la pierre et le zinc et bouchent les gouttières. Dans un bâtiment de stockage, elles souillent le matériel et les marchandises.\nPlus une colonie reste longtemps, plus les dégâts s'accumulent."),
        ("Copropriétés et syndics", "Sur un immeuble, la décision revient souvent au syndic ou à la copropriété. Je fournis un devis détaillé avec les zones à protéger et les solutions proposées.\nC'est le document qui permet de faire voter les travaux."),
        ("Commerces, entrepôts et bâtiments agricoles", "Dans un hangar, une stabulation ou un entrepôt, les pigeons nichent dans les charpentes, attirés par le grain et l'abri. Je pose des filets sous les charpentes et je ferme les accès.\nDans un commerce, je protège l'enseigne, la façade et la vitrine de façon discrète."),
        ("Supprimer ce qui attire les pigeons", "Les pigeons reviennent tant qu'ils trouvent de quoi manger et s'abriter. Nourrissage, grain accessible, ouvertures dans les combles : je vous indique ce qu'il faut changer.\nC'est ce qui rend le résultat durable.")],
  fin=["Envoyez-moi une photo de l'endroit où se posent les pigeons : je vous dis quelle solution convient.\nJe vous donne un tarif avant de venir, déplacement compris, et je me déplace à %(nom)s pour un diagnostic sur place.",
       "À %(nom)s, je viens voir le bâtiment, je repère les points de pose et de nidification, puis je vous propose la solution adaptée.\nLe devis est gratuit et le déplacement compris. Je suis joignable de 8h à 21h en semaine et de 9h à 18h le week-end.",
       "Je me déplace à %(nom)s depuis Port-Brillet. Je vous annonce le prix avant de venir et je vous explique la durée de l'intervention.\nJe prends la carte bancaire, les espèces, les chèques et les virements."],
  faq=[("Les pics font-ils du mal aux pigeons ?", "Non, ils empêchent seulement l'oiseau de se poser."),
       ("Peut-on piéger tous les pigeons ?", "Non. Le piégeage concerne les pigeons domestiques et les pigeons de ville. Il est interdit pour le pigeon ramier, aussi appelé palombe."),
       ("Le dispositif tient-il longtemps ?", "Un dispositif bien posé et entretenu dure longtemps."),
       ("Le piégeage suffit-il à régler le problème ?", "Rarement à lui seul : d'autres pigeons reviennent si le site reste accessible. Je l'associe à des protections."),
       ("Intervenez-vous pour les copropriétés ?", "Oui, avec un devis détaillé pour le syndic et la copropriété.")]),

 "piegeur-agree": dict(
  court="Piégeur agréé", stype="Piégeage de nuisibles",
  h1="Piégeur agréé à %(nom)s (%(dep)s) : fouines, ragondins, rats musqués",
  titres=["Piégeur Agréé %(nom)s (%(dep)s) | Proxinuisibles", "Piégeur Agréé %(nom)s | Proxinuisibles", "Piégeur Agréé %(nom)s"],
  metas=["Piégeur agréé à %(nom)s (%(dep)s) : fouines dans les combles, ragondins, rats musqués. Piégeage encadré par la loi, devis gratuit.",
         "Piégeur agréé à %(nom)s (%(dep)s) : fouines, ragondins. Devis gratuit."],
  leads=["Fouine dans les combles, ragondin au bord de l'étang : à %(nom)s, je réalise le piégeage en tant que piégeur agréé, dans le respect de la réglementation.",
         "À %(nom)s, j'interviens comme piégeur agréé pour les fouines, les ragondins et les rats musqués, chez les particuliers, les agriculteurs et les collectivités."],
  pool=[("Un piégeage encadré par la loi", "Le piégeage des espèces classées susceptibles d'occasionner des dégâts demande une formation spécifique et un agrément délivré par le préfet. La liste des espèces et les modalités varient selon le département.\nJe m'appuie sur les arrêtés en vigueur en Mayenne et en Ille-et-Vilaine. Voir aussi ma page <a href='/piegeur-agree/'>piégeur agréé</a>."),
        ("La fouine dans les combles", "La fouine se trahit par des bruits de course et de griffes la nuit, une odeur forte, des déjections et une isolation tassée ou arrachée. Elle ronge aussi les câbles et, sur les voitures garées à proximité, les durites.\nJe confirme d'abord qu'il s'agit bien d'une fouine : rat, loir, lérot ou oiseau ne laissent pas les mêmes traces."),
        ("Ragondins et rats musqués", "Les ragondins et les rats musqués creusent les berges des étangs, des mares et des fossés, et fragilisent les rives et les digues. Ils s'attaquent aussi aux cultures proches de l'eau.\nJe repère les terriers et les coulées avant de poser les pièges."),
        ("Comment je travaille", "Je repère les passages et les dégâts, je choisis le piège adapté et je le pose dans le respect de la réglementation. Je relève les pièges régulièrement.\nJe vous explique ensuite comment éviter le retour de l'animal : fermeture des accès, protection des volailles et des cultures."),
        ("Fermer les accès après le piégeage", "Une fois l'animal retiré, il faut fermer les accès : tuiles déplacées, rives de toiture, chatières, branches qui touchent le toit. Une fouine passe par une ouverture de la taille d'un poing.\nSans cette étape, une autre fouine reprend la place. Je vous remets la liste des points à reboucher."),
        ("Particuliers, agriculteurs et agences", "J'interviens chez les particuliers, sur les exploitations agricoles, autour des plans d'eau et pour les communes. Je travaille aussi avec les agences immobilières, les syndics et les bailleurs, avec un compte rendu écrit après chaque passage.")],
  fin=["Appelez-moi et décrivez ce que vous entendez ou voyez : bruits, traces, dégâts. Je vous dis de quel animal il s'agit probablement et comment je peux intervenir.\nJe vous donne un tarif avant de venir, déplacement compris. Je suis joignable de 8h à 21h en semaine et de 9h à 18h le week-end.",
       "À %(nom)s, je viens d'abord identifier l'animal et ses passages. Je vous propose ensuite le piégeage adapté, dans le respect de la réglementation.\nLe devis est gratuit et le déplacement compris.",
       "Je me déplace à %(nom)s depuis Port-Brillet. Je pose les pièges, je les relève régulièrement, puis je vous indique les accès à fermer.\nJe prends la carte bancaire, les espèces, les chèques et les virements."],
  faq=[("Pourquoi faire appel à un piégeur agréé ?", "Parce que le piégeage de certaines espèces est réservé aux personnes formées et agréées, avec des règles précises sur les pièges et les périodes."),
       ("J'entends des bruits dans mes combles la nuit, est-ce une fouine ?", "C'est possible. La fouine fait un bruit de course et de griffes, souvent en début de nuit et au petit matin. Je me déplace pour identifier l'animal avant de proposer une solution."),
       ("Une fouine peut-elle abîmer ma voiture ?", "Oui. Elle s'attaque aux durites et aux câbles du compartiment moteur des véhicules garés près de son territoire."),
       ("Que faire après le retrait de l'animal ?", "Fermer les accès, sinon une autre fouine reprend la place. Je vous remets la liste des points à reboucher."),
       ("Intervenez-vous pour les ragondins ?", "Oui, autour des étangs, des mares, des fossés et des cours d'eau, chez les particuliers, les agriculteurs et les collectivités.")]),
}

_COMB3 = list(_it.combinations(range(6), 3))
_FCOMB3 = list(_it.combinations(range(5), 3))

def _premier(cands, maxi, v):
    for c in cands:
        t = c % v
        if len(t) <= maxi:
            return t
    return cands[-1] % v

_AUTRES = [("Dératisation", "deratisation"), ("Frelons et guêpes", "frelons-guepes"), ("Punaises de lit", "punaises-de-lit"),
           ("Désinsectisation", "desinsectisation"), ("Chenilles processionnaires", "chenilles-processionnaires"),
           ("Taupier", "taupier"), ("Dépigeonnage", "depigeonnage"), ("Piégeur agréé", "piegeur-agree"), ("Débarras", "debarras")]

# 1) enregistrer toutes les pages (pour que les liens croisés se voient entre services)
_SV_PAGES = {}
for _svc, _villes in _SVV.items():
    for _slug, _nom, _dep, _loc in _villes:
        _SV_PAGES["/%s-%s/" % (_svc, _slug)] = (_svc, _slug, _nom, _dep, _loc)

for _svc, _villes in _SVV.items():
    D = _SVC_DEF[_svc]
    for _i, (_slug, _nom, _dep, _loc) in enumerate(_villes):
        path = "/%s-%s/" % (_svc, _slug)
        if path in P:
            continue
        v = {"nom": _nom, "dep": _dep}
        _k = (_i * 7 + len(_svc)) % len(_COMB3)
        secs = [_loc] + [D["pool"][j] for j in _COMB3[_k]]
        secs.append(("Mon intervention à %s" % _nom, D["fin"][_i % len(D["fin"])] % v))
        faq = [D["faq"][j] for j in _FCOMB3[(_i * 3 + len(_svc)) % len(_FCOMB3)]]
        autres = [("%s à %s" % (lab, _nom), "/%s-%s/" % (s, _slug)) for lab, s in _AUTRES
                  if s != _svc and (("/%s-%s/" % (s, _slug)) in P or ("/%s-%s/" % (s, _slug)) in _SV_PAGES)]
        autres.append(("%s : la prestation" % D["court"], "/%s/" % _svc))
        voisins = [(n, "/%s-%s/" % (_svc, s)) for s, n, *_ in _villes[max(0, _i - 2):_i] + _villes[_i + 1:_i + 3]]
        links = [("Autres services à %s" % _nom, autres)]
        if voisins:
            links.append(("Autres communes", [("%s à %s" % (D["court"], n), u) for n, u in voisins]))
        links.append(("Voir aussi", [("Zones d'intervention", "/zones-intervention/"), ("Particuliers", "/particuliers/"),
                                     ("Agriculteurs", "/agriculteurs/"), ("Devis et contact", "/contact/")]))
        add(path, h1=D["h1"] % v, title=_premier(D["titres"], 60, v), meta=_premier(D["metas"], 155, v),
            lead=D["leads"][_i % 2] % v, secs=secs, faq=faq, links=links, kind="ville",
            parent=(D["court"], "/%s/" % _svc), stype=D["stype"])

# 2) liens depuis les pages prestations et la page zones
for _svc, _villes in _SVV.items():
    D = _SVC_DEF[_svc]
    _l = [("%s à %s" % (D["court"], n), "/%s-%s/" % (_svc, s)) for s, n, *_ in _villes]
    P["/%s/" % _svc]["links"] = list(P["/%s/" % _svc].get("links") or []) + [("%s, commune par commune" % D["court"], _l)]
    P["/zones-intervention/"]["links"].append(("%s, commune par commune" % D["court"], _l))
