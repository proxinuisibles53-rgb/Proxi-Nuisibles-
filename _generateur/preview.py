import os, re, json, base64
S = "/home/claude/site"
css = open(S + "/style.css", encoding="utf-8").read()
pages = {}
for root, _, files in os.walk(S):
    if "index.html" in files:
        path = "/" + os.path.relpath(root, S).replace(".", "") if root != S else "/"
        path = path if path == "/" else path.rstrip("/") + "/"
        html = open(os.path.join(root, "index.html"), encoding="utf-8").read()
        m = re.search(r"<body>(.*?)(?:<script src='/[^']+'></script>)+</body>", html, re.S)
        if not m:
            m = re.search(r"<body>(.*?)</body>", html, re.S)
        t = re.search(r"<title>(.*?)</title>", html).group(1)
        pages[path] = (t, m.group(1))
def uri(f, mime):
    return "data:%s;base64,%s" % (mime, base64.b64encode(open("/home/claude/assets/" + f, "rb").read()).decode())
IMG = {"/logo.webp": uri("logo.webp", "image/webp"), "/logo-petit.webp": uri("logo-petit.webp", "image/webp"), "/logo-texte.webp": uri("logo-texte.webp", "image/webp")}
MD = {"webp": "image/webp", "mp4": "video/mp4"}
MJ = dict(IMG)
for _f in sorted(os.listdir("/home/claude/assets/media")):
    MJ["/media/" + _f] = "data:%s;base64,%s" % (MD[_f.rsplit(".", 1)[1]], base64.b64encode(open("/home/claude/assets/media/" + _f, "rb").read()).decode())
blocks = "".join("<div class='pv-page' data-path='%s' hidden>%s</div>" % (p, b) for p, (t, b) in sorted(pages.items()))
titles = {p: t for p, (t, b) in pages.items()}
_sj = open("/home/claude/site/site.js", encoding="utf-8").read()
ASST = _sj[_sj.index("/* Assistant d'orientation"):].replace("</script>", "<\\/script>")
out = ("<!DOCTYPE html><html lang='fr'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>"
       "<title>Aperçu – Proxinuisibles</title><style>" + css +
       ".pv-bar{background:#000;color:#fff;font:14px/1.4 system-ui,sans-serif;text-align:center;padding:6px 10px}</style></head><body>"
       "<div class='pv-bar'>Aperçu du site : cliquez sur les liens pour passer d'une page à l'autre.</div>" + blocks +
       "<script>var M=" + json.dumps(MJ) + ";var T=" + json.dumps(titles, ensure_ascii=False) + ";"
       "document.addEventListener('click',function(e){var b=e.target.closest('.burger');if(b){var n=b.parentNode.querySelector('nav');var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);return;}document.querySelectorAll('.dd details').forEach(function(x){if(!x.contains(e.target)){x.removeAttribute('open');}});});"
       "document.querySelectorAll('[id=avis]').forEach(function(s){s.hidden=false;});document.querySelectorAll('[id=avis-fiche]').forEach(function(a){a.href='https://maps.app.goo.gl/BEtwDMWG5gN9sgXv7';a.hidden=false;a.target='_blank';});"
       "var AV=" + open("/home/claude/assets/avis.json", encoding="utf-8").read() + ";"
       "document.querySelectorAll('[id=avis-widget]').forEach(function(b){function el(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!==undefined)e.textContent=x;return e;}function st(n){return el('span','avis-etoiles','\\u2605\\u2605\\u2605\\u2605\\u2605'.slice(0,n)+'\\u2606\\u2606\\u2606\\u2606\\u2606'.slice(0,5-n));}var r=el('div','avis-resume');r.appendChild(el('strong','avis-note',String(AV.note_moyenne).replace('.',',')+' / 5'));r.appendChild(st(5));r.appendChild(el('span','avis-nb',AV.nombre_total+' avis Google'));b.appendChild(r);var g=el('div','avis-ban');var p=el('div','avis-piste');var L=AV.avis.slice(0,6);function ca(x,cp){var c=el('blockquote','avis-carte');if(cp)c.setAttribute('aria-hidden','true');c.appendChild(st(x.note));c.appendChild(el('p','avis-texte',x.texte));c.appendChild(el('footer','avis-auteur',x.auteur+' \\u00b7 '+x.date));return c;}L.forEach(function(x){p.appendChild(ca(x,false));});L.forEach(function(x){p.appendChild(ca(x,true));});p.style.setProperty('--dur',Math.max(40,L.length*14)+'s');g.appendChild(p);b.appendChild(g);});"
       "function show(p){var f=false;document.querySelectorAll('.pv-page').forEach(function(d){var on=d.dataset.path===p;d.hidden=!on;if(on)f=true;});"
       "if(!f){p='/';document.querySelector('.pv-page[data-path=\"/\"]').hidden=false;}document.querySelectorAll('.pv-page[data-path=\"'+p+'\"] [src^=\"/media/\"],.pv-page[data-path=\"'+p+'\"] [src^=\"/logo\"],.pv-page[data-path=\"'+p+'\"] [poster^=\"/media/\"]').forEach(function(e){[\"src\",\"poster\"].forEach(function(k){var v=e.getAttribute(k);if(v&&M[v])e.setAttribute(k,M[v]);});if(e.tagName===\"VIDEO\"){e.querySelectorAll(\"source\").forEach(function(o){var w=o.getAttribute(\"src\");if(w&&M[w])o.setAttribute(\"src\",M[w]);});e.load();var q=e.play();if(q&&q.catch)q.catch(function(){});}});window.scrollTo(0,0);location.hash=p;document.title='Aperçu – '+(T[p]||'');}"
       "document.addEventListener('click',function(e){var a=e.target.closest('a');if(!a)return;var h=a.getAttribute('href');"
       "if(h&&h.charAt(0)==='/'){e.preventDefault();show(h);}});"
       "show(decodeURIComponent(location.hash.slice(1))||'/');" + ASST + "</script></body></html>")
open("/mnt/user-data/outputs/apercu-proxinuisibles.html", "w", encoding="utf-8").write(out)
print(len(pages), len(out)//1024, "Ko", sorted(pages)[:4])
