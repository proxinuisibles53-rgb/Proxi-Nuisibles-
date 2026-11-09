/* Variante Cloudflare Pages de /api/avis.
   Ignoree si le projet Cloudflare est un Worker (c'est alors
   src/index.js qui repond). Voir src/avis.js. */

import { servirAvis } from "../../src/avis.mjs";

export function onRequestGet({ request, env, waitUntil }) {
  return servirAvis(request, env, { waitUntil: waitUntil });
}
