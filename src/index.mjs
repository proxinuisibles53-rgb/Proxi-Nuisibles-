/* Worker Proxi Nuisibles
   - sert le site statique (dossier public/) : comportement inchange
   - expose /api/avis : note et nombre d'avis lus sur la fiche Google
   Voir src/avis.js pour la logique et les variables attendues. */

import { servirAvis } from "./avis.mjs";

export default {
  async fetch(request, env, ctx) {
    if (new URL(request.url).pathname === "/api/avis") {
      return servirAvis(request, env, ctx);
    }
    if (env.ASSETS) {
      return env.ASSETS.fetch(request);
    }
    return new Response("Not found", { status: 404 });
  },
};
