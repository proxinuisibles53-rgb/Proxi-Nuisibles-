/* Compteur d'avis Google — coeur partage
   ------------------------------------------------------------------
   Utilise par les deux modes de deploiement possibles :
     - Cloudflare Workers : src/index.mjs
     - Cloudflare Pages   : functions/api/avis.js
   Un seul des deux est actif selon le type de projet Cloudflare.

   Variables attendues (a creer dans Cloudflare, voir README) :
     GOOGLE_API_KEY  secret, obligatoire  -> cle Google Maps Platform
     PLACE_ID        variable, optionnel  -> identifiant de la fiche
     PLACE_QUERY     variable, optionnel  -> recherche si PLACE_ID absent

   Si la cle est absente ou si Google repond mal, la reponse est
   {"ok":false} : le site garde alors les valeurs de avis.json.
   ------------------------------------------------------------------ */

const CACHE_OK = 86400; /* 24 h : limite les appels factures a ~1 par jour */
const CACHE_KO = 60; /* 1 min en cas d'erreur, pour reessayer vite */
const RECHERCHE_DEFAUT = "Proxi Nuisibles Port-Brillet";
/* A incrementer pour repartir d'un cache vide apres un changement
   de configuration (ajout du secret, changement de fiche...). */
const VERSION = 11;

export async function servirAvis(request, env, ctx) {
  const origine = new URL(request.url).origin;
  /* Cle de cache fixe : toutes les visites partagent la meme entree,
     impossible de declencher des appels Google avec des parametres. */
  const cle = new Request(origine + "/__cache/avis-v" + VERSION, { method: "GET" });
  const cache = caches.default;

  const garde = await cache.match(cle);
  if (garde) {
    return marquer(garde, "HIT");
  }

  const data = await lireGoogle(env);
  data.v = VERSION; /* repere de version, pour diagnostic */
  const reponse = new Response(JSON.stringify(data), {
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "public, max-age=" + (data.ok ? CACHE_OK : CACHE_KO),
    },
  });
  if (ctx && ctx.waitUntil) {
    ctx.waitUntil(cache.put(cle, reponse.clone()));
  }
  return marquer(reponse, "MISS");
}

function marquer(reponse, etat) {
  const out = new Response(reponse.body, reponse);
  out.headers.set("x-avis-cache", etat);
  return out;
}

async function lireGoogle(env) {
  const cleApi = env.GOOGLE_API_KEY;
  if (!cleApi) {
    return { ok: false, raison: "cle_absente" };
  }
  try {
    let id = env.PLACE_ID;
    if (!id) {
      id = await trouverFiche(cleApi, env.PLACE_QUERY || RECHERCHE_DEFAUT);
    }
    if (!id) {
      return { ok: false, raison: "fiche_introuvable" };
    }
    const r = await fetch(
      "https://places.googleapis.com/v1/places/" + encodeURIComponent(id) + "?languageCode=fr",
      {
        headers: {
          "X-Goog-Api-Key": cleApi,
          /* id est facture au palier gratuit illimite ; la facturation
             retient de toute facon le champ le plus eleve demande. */
          "X-Goog-FieldMask": "id,rating,userRatingCount,reviews",
        },
      }
    );
    if (!r.ok) {
      return { ok: false, raison: "google_" + r.status };
    }
    const d = await r.json();
    if (typeof d.rating !== "number") {
      return { ok: false, raison: "sans_note" };
    }
    return {
      ok: true,
      note: Math.round(d.rating * 10) / 10,
      total: d.userRatingCount || 0,
      fiche: d.id || id,
      avis: lireAvis(d.reviews),
      maj: new Date().toISOString().slice(0, 10),
    };
  } catch (e) {
    return { ok: false, raison: "erreur_reseau" };
  }
}

/* Avis publies sur la fiche : Google en expose cinq au maximum et
   choisit lesquels. Ils sont repris tels quels, avec le nom de leur
   auteur et le lien vers l'avis, comme l'exigent les conditions
   d'utilisation de Google Maps Platform. */
function lireAvis(reviews) {
  if (!Array.isArray(reviews)) {
    return [];
  }
  return reviews
    .slice(0, 5)
    .map(function (r) {
      const t = (r.text && r.text.text) || (r.originalText && r.originalText.text) || "";
      const a = r.authorAttribution || {};
      const v = r.visitDate;
      return {
        note: r.rating || 0,
        texte: String(t).trim(),
        auteur: a.displayName || "Client",
        photo: a.photoUri || "",
        profil: a.uri || "",
        date: r.relativePublishTimeDescription || "",
        lien: r.googleMapsUri || a.uri || "",
        signalement: r.flagContentUri || "",
        /* Date de visite : obligatoire en France pour l'affichage
           d'avis en ligne (article L.111-7-2 du code de la consommation). */
        visite: v && v.year ? { an: v.year, mois: v.month || 0 } : null,
      };
    })
    .filter(function (x) {
      return x.texte && x.note >= 1;
    });
}

/* Recherche l'identifiant de la fiche. Champ demande : places.id
   seulement, ce qui releve du palier gratuit illimite de Google. */
async function trouverFiche(cleApi, requete) {
  const r = await fetch("https://places.googleapis.com/v1/places:searchText", {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "X-Goog-Api-Key": cleApi,
      "X-Goog-FieldMask": "places.id",
    },
    body: JSON.stringify({
      textQuery: requete,
      languageCode: "fr",
      regionCode: "FR",
      maxResultCount: 1,
    }),
  });
  if (!r.ok) {
    return null;
  }
  const d = await r.json();
  return d.places && d.places.length ? d.places[0].id : null;
}
