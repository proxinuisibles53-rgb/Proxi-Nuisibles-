var AVIS_DATA = {
  "nombre_total": 118,
  "note_moyenne": 5,
  "avis": [
    {
      "auteur": "Natacha P.",
      "note": 5,
      "date": "Septembre 2026",
      "texte": "Très bonne expérience, professionnel de qualité. J'avais un nid de frelons, je l'ai appelé lundi soir il était là le mardi. Efficace et vous expliquer tout parfaitement. Je recommande à 100%."
    },
    {
      "auteur": "Louis R.",
      "note": 5,
      "date": "Septembre 2026",
      "texte": "Nous avons fait appel à ce professionnel car un nuisible de type rongeur était dans notre cuisine. Il est intervenu en à peine deux heures à notre domicile, alors que d'autres annonçaient un délai de huit jours et ne souhaitait pas chasser l'animal, nous sommes vraiment reconnaissant de son professionnalisme, des conseils apportés, ainsi que son amabilité. Nous recommandons vivement ce professionnel dans le traitement des nuisibles, j'en fais d'ailleurs la même la promotion dès que j'en ai l'occasion."
    },
    {
      "auteur": "Beatrice F.",
      "note": 5,
      "date": "Septembre 2026",
      "texte": "Contacté pour un nid de guêpes. L'intervention a été efficace. Professionnel à l'écoute, prend le temps d'expliquer. Je n'hésiterais pas à faire à nouveau appel à ses services."
    },
    {
      "auteur": "Mathieu L.",
      "note": 5,
      "date": "Juillet 2026",
      "texte": "Très professionnel : des réponses aux questions, de l'outillage pro. Je dirais qu'il est là pour « chercher la petite bête » avec ironie ! Encore merci 👍"
    },
    {
      "auteur": "Céline G.",
      "note": 5,
      "date": "Juin 2026",
      "texte": "Professionnel à l'écoute et très réactif ! Contacté en fin de matinée pour un nid de guêpes en hauteur sur l'habitation. Intervention le jour même en début de soirée. Je n'hésiterai pas à refaire appel à lui si nécessaire. Vous pouvez lui faire confiance pour éradiquer votre problème de nuisibles ! Un grand merci !"
    }
  ]
};
/* AVIS GOOGLE
   1) La note et le nombre d'avis sont relus sur la fiche Google via /api/avis.
      Si cette lecture echoue, les valeurs de avis.json restent affichees.
   2) Les textes des avis viennent de avis.json. Aucun service externe, aucun cookie. */
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
  function el(tag, cls, txt) { var e = document.createElement(tag); if (cls) { e.className = cls; } if (txt !== undefined) { e.textContent = txt; } return e; }
  function etoiles(n) { n = Math.max(0, Math.min(5, Math.round(n))); var e = el("span", "avis-etoiles", "★★★★★".slice(0, n) + "☆☆☆☆☆".slice(0, 5 - n)); e.setAttribute("role", "img"); e.setAttribute("aria-label", n + " étoiles sur 5"); return e; }
  function resume(moy, total) {
    var r = el("div", "avis-resume");
    r.appendChild(el("strong", "avis-note", moy.toFixed(1).replace(".", ",") + " / 5"));
    r.appendChild(etoiles(moy));
    r.appendChild(el("span", "avis-nb", total + " avis Google"));
    var m = el("span", "avis-maj", "");
    m.hidden = true;
    r.appendChild(m);
    return r;
  }
  function rendre(data) {
    if (AVIS_HTML || !data || !data.avis || !data.avis.length) { return; }
    var liste = data.avis.filter(function (x) { return x && x.texte && x.note >= 1; });
    if (!liste.length) { return; }
    var moy = data.note_moyenne > 0 ? data.note_moyenne : liste.reduce(function (t, x) { return t + x.note; }, 0) / liste.length;
    var total = data.nombre_total > 0 ? data.nombre_total : liste.length;
    if (minibox) { minibox.appendChild(resume(moy, total)); }
    if (!box) { return; }
    box.appendChild(resume(moy, total));
    var g = el("div", "avis-ban");
    g.setAttribute("role", "region"); g.setAttribute("aria-label", "Avis de mes clients");
    var piste = el("div", "avis-piste");
    var cartes = liste.slice(0, AVIS_MAX);
    function carte(x, copie) {
      var c = el("blockquote", "avis-carte");
      if (copie) { c.setAttribute("aria-hidden", "true"); }
      c.appendChild(etoiles(x.note));
      c.appendChild(el("p", "avis-texte", x.texte));
      c.appendChild(el("footer", "avis-auteur", (x.auteur || "Client") + (x.date ? " · " + x.date : "")));
      return c;
    }
    cartes.forEach(function (x) { piste.appendChild(carte(x, false)); });
    cartes.forEach(function (x) { piste.appendChild(carte(x, true)); });
    piste.style.setProperty("--dur", Math.max(40, cartes.length * 14) + "s");
    g.appendChild(piste);
    box.appendChild(g);
  }
  var MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"];
  function dateFr(iso) {
    var p = String(iso || "").split("-");
    if (p.length !== 3) { return ""; }
    var j = parseInt(p[2], 10), m = parseInt(p[1], 10);
    if (!j || !m || !MOIS[m - 1]) { return ""; }
    return (j === 1 ? "1er" : j) + " " + MOIS[m - 1] + " " + p[0];
  }
  /* Compteur en direct : /api/avis relit la fiche Google (fonction Cloudflare).
     Si la reponse n'arrive pas, les valeurs de avis.json restent affichees. */
  function majDirect() {
    if (!window.fetch) { return; }
    fetch("/api/avis", { cache: "no-store" }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
      if (!d || !d.ok || !(d.note > 0)) { return; }
      Array.prototype.forEach.call(document.querySelectorAll(".avis-note"), function (n) { n.textContent = d.note.toFixed(1).replace(".", ",") + " / 5"; });
      Array.prototype.forEach.call(document.querySelectorAll(".avis-etoiles"), function (e) {
        if (e.parentNode && e.parentNode.className === "avis-resume") { e.parentNode.replaceChild(etoiles(d.note), e); }
      });
      if (d.total > 0) {
        Array.prototype.forEach.call(document.querySelectorAll(".avis-nb"), function (t) { t.textContent = d.total + " avis Google"; });
      }
      var jour = dateFr(d.maj);
      if (jour) {
        Array.prototype.forEach.call(document.querySelectorAll(".avis-maj"), function (m) { m.textContent = "mis à jour le " + jour; m.hidden = false; });
      }
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
