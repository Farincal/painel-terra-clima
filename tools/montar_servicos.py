# Monta servicos.html a partir do corpo, com cabeçalhos de segurança (CSP com hash dos scripts).
# Uso: python3 tools/montar_servicos.py servicos-corpo.html servicos.html
import re,hashlib,base64,sys
body=open(sys.argv[1]).read()
scripts=re.findall(r'<script>(.*?)</script>',body,re.S)
hs=" ".join("'sha256-"+base64.b64encode(hashlib.sha256(s.encode()).digest()).decode()+"'" for s in scripts)
csp=("default-src 'none'; script-src "+hs+"; style-src 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data:; connect-src 'none'; base-uri 'none'; form-action 'none'; object-src 'none'")
head=('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
 '<meta http-equiv="Content-Security-Policy" content="'+csp+'">\n<meta name="referrer" content="strict-origin-when-cross-origin">\n'
 '<meta name="description" content="Painéis de clima e riscos sob medida para prefeituras, agro e empresas, com atualização automática. Paneles a medida para ayuntamientos y empresas.">\n'
 '<link rel="canonical" href="https://farincal.github.io/painel-terra-clima/servicos.html">\n<link rel="icon" href="favicon.svg" type="image/svg+xml">\n<meta name="theme-color" content="#07121B">\n'
 '<meta property="og:type" content="website">\n<meta property="og:title" content="Painéis de clima sob medida · FarincalTec">\n<meta property="og:description" content="Seu painel de clima e riscos, atualizado sozinho. Para prefeituras, agro e empresas.">\n<meta property="og:image" content="https://farincal.github.io/painel-terra-clima/og.png">\n<meta name="twitter:card" content="summary_large_image">\n')
i=body.index('<div class="wrap">')
doc=head+body[:i]+'</head>\n<body>\n'+body[i:]+'\n</body>\n</html>\n'
doc=doc.replace('body{background:var(--bg)','body{margin:0;background:var(--bg)',1)
open(sys.argv[2],'w').write(doc)
