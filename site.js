document.addEventListener("click",function(e){var b=e.target.closest(".burger");if(b){var n=b.parentNode.querySelector("nav");var o=n.classList.toggle("open");b.setAttribute("aria-expanded",o);return;}document.querySelectorAll(".dd details").forEach(function(x){if(!x.contains(e.target)){x.removeAttribute("open");}});});
/* Assistant d'orientation : aucun serveur, aucun cookie. Il propose la bonne page du site selon les mots saisis. */
(function () {
  if (window.__asst) { return; }
  window.__asst = true;
  var COM = {"laval": ["Laval", "/deratisation-laval/"], "saint berthevin": ["Saint-Berthevin", "/deratisation-saint-berthevin/"], "vitre": ["Vitré", "/deratisation-vitre/"], "ernee": ["Ernée", "/deratisation-ernee/"], "mayenne": ["Mayenne", "/deratisation-mayenne/"], "fougeres": ["Fougères", "/deratisation-fougeres/"], "chateaubourg": ["Châteaubourg", "/deratisation-chateaubourg/"], "cesson sevigne": ["Cesson-Sévigné", "/deratisation-cesson-sevigne/"], "rennes": ["Rennes", "/deratisation-rennes/"], "olivet": ["Olivet", "/deratisation-olivet/"], "la brulatte": ["La Brûlatte", "/deratisation-la-brulatte/"], "launay villiers": ["Launay-Villiers", "/deratisation-launay-villiers/"], "saint pierre la cour": ["Saint-Pierre-la-Cour", "/deratisation-saint-pierre-la-cour/"], "le bourgneuf la foret": ["Le Bourgneuf-la-Forêt", "/deratisation-le-bourgneuf-la-foret/"], "le genest saint isle": ["Le Genest-Saint-Isle", "/deratisation-le-genest-saint-isle/"], "saint ouen des toits": ["Saint-Ouën-des-Toits", "/deratisation-saint-ouen-des-toits/"], "la gravelle": ["La Gravelle", "/deratisation-la-gravelle/"], "loiron ruille": ["Loiron-Ruillé", "/deratisation-loiron-ruille/"], "bourgon": ["Bourgon", "/deratisation-bourgon/"], "la baconniere": ["La Baconnière", "/deratisation-la-baconniere/"], "saint cyr le gravelais": ["Saint-Cyr-le-Gravelais", "/deratisation-saint-cyr-le-gravelais/"], "breal sous vitre": ["Bréal-sous-Vitré", "/deratisation-breal-sous-vitre/"], "la chapelle erbree": ["La Chapelle-Erbrée", "/deratisation-la-chapelle-erbree/"], "mondevert": ["Mondevert", "/deratisation-mondevert/"], "la croixille": ["La Croixille", "/deratisation-la-croixille/"], "saint germain le fouilloux": ["Saint-Germain-le-Fouilloux", "/deratisation-saint-germain-le-fouilloux/"], "erbree": ["Erbrée", "/deratisation-erbree/"], "saint hilaire du maine": ["Saint-Hilaire-du-Maine", "/deratisation-saint-hilaire-du-maine/"], "le pertre": ["Le Pertre", "/deratisation-le-pertre/"], "saint m herve": ["Saint-M'Hervé", "/deratisation-saint-m-herve/"], "montjean": ["Montjean", "/deratisation-montjean/"], "ahuille": ["Ahuillé", "/deratisation-ahuille/"], "juvigne": ["Juvigné", "/deratisation-juvigne/"], "saint germain le guillaume": ["Saint-Germain-le-Guillaume", "/deratisation-saint-germain-le-guillaume/"], "andouille": ["Andouillé", "/deratisation-andouille/"], "change": ["Changé", "/deratisation-change/"], "louverne": ["Louverné", "/deratisation-louverne/"], "argentre du plessis": ["Argentré-du-Plessis", "/deratisation-argentre-du-plessis/"], "chailland": ["Chailland", "/deratisation-chailland/"], "cosse le vivien": ["Cossé-le-Vivien", "/deratisation-cosse-le-vivien/"], "beaulieu sur oudon": ["Beaulieu-sur-Oudon", "/deratisation-beaulieu-sur-oudon/"], "l huisserie": ["L'Huisserie", "/deratisation-l-huisserie/"], "etrelles": ["Étrelles", "/deratisation-etrelles/"], "meral": ["Méral", "/deratisation-meral/"], "astille": ["Astillé", "/deratisation-astille/"], "saint pierre des landes": ["Saint-Pierre-des-Landes", "/deratisation-saint-pierre-des-landes/"], "chatillon en vendelais": ["Châtillon-en-Vendelais", "/deratisation-chatillon-en-vendelais/"], "gennes sur seiche": ["Gennes-sur-Seiche", "/deratisation-gennes-sur-seiche/"], "montautour": ["Montautour", "/deratisation-montautour/"], "brielles": ["Brielles", "/deratisation-brielles/"], "saint jean sur mayenne": ["Saint-Jean-sur-Mayenne", "/deratisation-saint-jean-sur-mayenne/"], "courbeveille": ["Courbeveille", "/deratisation-courbeveille/"], "montigne le brillant": ["Montigné-le-Brillant", "/deratisation-montigne-le-brillant/"], "prince": ["Princé", "/deratisation-prince/"], "la bigottiere": ["La Bigottière", "/deratisation-la-bigottiere/"], "balaze": ["Balazé", "/deratisation-balaze/"], "saint poix": ["Saint-Poix", "/deratisation-saint-poix/"], "montenay": ["Montenay", "/deratisation-montenay/"], "montflours": ["Montflours", "/deratisation-montflours/"]};
  var SUJETS = [
    [/frelon asiatique|velutina|pattes jaunes/, "Frelon asiatique", "/frelon-asiatique/"],
    [/frelon|gu[eê]pe|vespa|\bnid/, "Nid de frelons ou de guêpes", "/frelons-guepes/"],
    [/\brats?\b|souris|rongeur|mulot|d[eé]ratis|surmulot|loir/, "Rats, souris et rongeurs", "/deratisation/"],
    [/punaise|piq[uû]re/, "Punaises de lit", "/punaises-de-lit/"],
    [/chenille|processionnaire/, "Chenilles processionnaires", "/chenilles-processionnaires/"],
    [/taupe|taupini/, "Taupes", "/taupier/"],
    [/pigeon|fiente|goeland|go[eé]land/, "Pigeons et oiseaux", "/depigeonnage/"],
    [/fouine|martre|ragondin|musqu|corbeau|corvid|pi[eè]ge/, "Fouines, ragondins, corvidés", "/piegeur-agree/"],
    [/cafard|blatte|cancrelat/, "Cafards et blattes", "/blattes-cafards/"],
    [/fourmi/, "Fourmis", "/fourmis/"],
    [/mouche|mouches|drosophile|moucheron/, "Mouches", "/mouches/"],
    [/puce|puces/, "Puces", "/puces/"],
    [/insecte|moustique|mite|d[eé]sinsect/, "Autres insectes", "/desinsectisation/"],
    [/restaurant|boulang|boucher|charcut|traiteur|cuisine|p[aâ]tiss|m[eé]tiers? de bouche/, "Contrats métiers de bouche", "/contrats-metiers-de-bouche/"],
    [/syndic|agence|copropri|immobili|bailleur|locatif/, "Agences immobilières et syndics", "/agences-syndics/"],
    [/agricul|[eé]leveur|ferme|exploitation|[eé]table|hangar|silo|[eé]levage/, "Agriculteurs et éleveurs", "/agriculteurs/"],
    [/mairie|[eé]cole|collectivit|entreprise|professionnel|entrep[oô]t|commerce|magasin|bureau/, "Professionnels et collectivités", "/professionnels/"],
    [/contrat|annuel|suivi/, "Contrat annuel avec compte rendu", "/contrat-annuel-deratisation/"],
    [/particulier|maison|jardin|logement|appartement/, "Particuliers", "/particuliers/"],
    [/devis|prix|tarif|co[uû]t|combien|rendez|contact|urgence|appel/, "Demander un devis gratuit", "/contact/"],
    [/zone|secteur|intervenez|r[eé]gion|commune|ville/, "Mes zones d'intervention", "/zones-intervention/"]
  ];
  function norm(s) { return String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/['’\-]/g, " ").replace(/\s+/g, " ").trim(); }
  function el(tag, cls, txt) { var e = document.createElement(tag); if (cls) { e.className = cls; } if (txt !== undefined) { e.textContent = txt; } return e; }
  function chercher(q) {
    var n = norm(q), res = [], vus = {};
    function add(l, u) { if (!vus[u] && res.length < 4) { vus[u] = 1; res.push([l, u]); } }
    Object.keys(COM).forEach(function (k) { if (n.indexOf(k) > -1) { add("Dératisation à " + COM[k][0], COM[k][1]); } });
    SUJETS.forEach(function (s) { if (s[0].test(q.toLowerCase()) || s[0].test(n)) { add(s[1], s[2]); } });
    return res;
  }
  function fermer(box) {
    var p = box.querySelector(".asst-panel"), b = box.querySelector(".asst-btn");
    p.hidden = true; b.setAttribute("aria-expanded", "false");
  }
  document.addEventListener("click", function (e) {
    var b = e.target.closest(".asst-btn");
    if (b) {
      var box = b.closest(".asst"), p = box.querySelector(".asst-panel"), ouvert = p.hidden;
      p.hidden = !ouvert; b.setAttribute("aria-expanded", ouvert ? "true" : "false");
      if (ouvert) { var i = p.querySelector(".asst-q"); if (i) { try { i.focus(); } catch (x) {} } }
      return;
    }
    var c = e.target.closest(".asst-close");
    if (c) { fermer(c.closest(".asst")); return; }
    var a = e.target.closest(".asst a");
    if (a) { fermer(a.closest(".asst")); return; }
    document.querySelectorAll(".asst").forEach(function (bx) { if (!bx.contains(e.target)) { fermer(bx); } });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { document.querySelectorAll(".asst").forEach(fermer); }
  });
  document.addEventListener("submit", function (e) {
    var f = e.target.closest(".asst-form");
    if (!f) { return; }
    e.preventDefault();
    var q = f.querySelector(".asst-q").value.trim(), out = f.parentNode.querySelector(".asst-out");
    while (out.firstChild) { out.removeChild(out.firstChild); }
    if (!q) { out.appendChild(el("p", "asst-msg", "Écrivez par exemple : nid de guêpes, rats à Laval, punaises de lit...")); return; }
    var res = chercher(q);
    if (!res.length) {
      out.appendChild(el("p", "asst-msg", "Je n'ai pas trouvé de page précise pour cette demande. Le plus simple est de m'appeler ou de demander un devis gratuit."));
    } else {
      out.appendChild(el("p", "asst-msg", res.length > 1 ? "Voici les pages qui correspondent :" : "Voici la page qui correspond :"));
      var ul = el("ul", "asst-res");
      res.forEach(function (r) { var li = el("li"), a = el("a", "", r[0] + " →"); a.href = r[1]; li.appendChild(a); ul.appendChild(li); });
      out.appendChild(ul);
    }
  });
})();

document.addEventListener('submit',function(e){var f=e.target;if(!f||f.id!=='cform')return;e.preventDefault();
var m=document.getElementById('cform-msg'),b=f.querySelector('button[type=submit]');
function show(t,ok){m.hidden=false;m.className='cform-msg '+(ok?'ok':'ko');m.textContent=t;}
var req=f.querySelectorAll('[required]');for(var i=0;i<req.length;i++){if(!req[i].value.trim()){show('Merci de remplir tous les champs.',false);req[i].focus();return;}}
var em=f.querySelector('[type=email]');if(em.value.indexOf('@')<1){show('Merci de saisir une adresse e-mail valide.',false);em.focus();return;}
if(f.querySelector('[name=_honey]').value){return;}
b.disabled=true;b.textContent='Envoi en cours...';
var d=new FormData(f);
fetch(f.dataset.endpoint,{method:'POST',body:d,headers:{'Accept':'application/json'}}).then(function(r){return r.json().catch(function(){return {};}).then(function(j){if(r.ok&&j.success!=='false'){f.reset();show('Merci, votre demande est bien envoyée. Je vous réponds rapidement.',true);}else{throw new Error('x');}});}).catch(function(){show('Envoi impossible pour le moment. Appelez-moi au 06 64 57 66 55 ou écrivez à proxinuisibles53@gmail.com.',false);}).then(function(){b.disabled=false;b.textContent='Envoyer ma demande';});
});
