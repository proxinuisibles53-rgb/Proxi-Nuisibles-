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
const CACHE_KO = 600; /* 10 min en cas d'erreur, pour reessayer vite */
const RECHERCHE_DEFAUT = "Proxi Nuisibles Port-Brillet";

export async function servirAvis(request, env, ctx) {
  const origine = new URL(request.url).origin;
  /* Cle de cache fixe : toutes les visites partagent la meme entree,
     impossible de declencher des appels Google avec des parametres. */
  const cle = new Request(origine + "/__cache/avis", { method: "GET" });
  const cache = caches.default;

  const garde = await cache.match(cle);
  if (garde) {
    return marquer(garde, "HIT");
  }

  const data = await lireGoogle(env);
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
          "X-Goog-FieldMask": "rating,userRatingCount",
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
      maj: new Date().toISOString().slice(0, 10),
    };
  } catch (e) {
    return { ok: false, raison: "erreur_reseau" };
  }
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
