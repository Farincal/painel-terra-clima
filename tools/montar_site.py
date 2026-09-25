# Monta o index.html do site a partir do corpo publicado no Claude.
# Uso: python3 tools/montar_site.py corpo.html index.html
import re,hashlib,base64,sys,os
body=open(sys.argv[1]).read(); out=sys.argv[2]
extra_p=os.path.join(os.path.dirname(os.path.abspath(out)),'head-extra.html')
extra=open(extra_p).read().strip()+'\n' if os.path.exists(extra_p) else ''
scripts=re.findall(r'<script>(.*?)</script>',body,re.S)
hs=" ".join("'sha256-"+base64.b64encode(hashlib.sha256(s.encode()).digest()).decode()+"'" for s in scripts)
csp=("default-src 'none'; script-src "+hs+"; style-src 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data:; connect-src https://earthquake.usgs.gov; base-uri 'none'; form-action 'none'; object-src 'none'")
head=('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
 '<meta http-equiv="Content-Security-Policy" content="'+csp+'">\n<meta name="referrer" content="strict-origin-when-cross-origin">\n'
 '<meta name="description" content="Plantão de fenômenos naturais e monitoramento do El Niño 2026–27, em português.">\n'+extra)
i=body.index('<div class="top">')
doc=head+body[:i]+'</head>\n<body>\n'+body[i:]+'\n</body>\n</html>\n'
doc=doc.replace('body{background:var(--bg)','body{margin:0;background:var(--bg)',1)
open(out,'w').write(doc)
