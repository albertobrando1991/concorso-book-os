from pathlib import Path
import urllib.request,hashlib,json,fitz,time
D=Path('wiki/raw/correzioni-vol05-2026-10-03');O=Path('artifacts/correzioni-collana-2026-10-02/norme-vol05');rows=[]
for slug,celex in []:
 url=f'https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:{celex}'
 p=D/(slug+'.pdf')
 try:
  if not p.exists():
   req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
   b=urllib.request.urlopen(req,timeout=60).read()
   if not b.startswith(b'%PDF'): raise ValueError('Not PDF '+str(b[:80]))
   p.write_bytes(b)
  with fitz.open(p) as doc:
   txt='\n'.join('PAGE '+str(i+1)+'\n'+pg.get_text() for i,pg in enumerate(doc)); n=len(doc)
  (O/(slug+'.txt')).write_text(txt,encoding='utf8');rows.append({'id':slug,'url':url,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'pages':n,'readComplete':False});print(slug,n,len(txt),flush=True)
 except Exception as e:rows.append({'id':slug,'url':url,'error':str(e)});print(slug,str(e),flush=True)
for slug,url in [
 ('ep-fonti','https://www.europarl.europa.eu/ftu/pdf/it/FTU_1.2.1.pdf'),
 ('ecn-page','https://competition-policy.ec.europa.eu/antitrust-and-cartels/european-competition-network_en'),
 ('eba-compliance','https://www.eba.europa.eu/about-us/legal-and-policy-framework/compliance-eba-regulatory-products'),
 ('eiopa-convergence','https://www.eiopa.europa.eu/browse/supervisory-convergence/supervisory-convergence-tools_en'),
 ('acer-investigations','https://acer.europa.eu/remit/remit-investigations'),
 ('berec-regulation','https://eur-lex.europa.eu/legal-content/en/ALL/?uri=CELEX%3A32018R1971')]:
 p=D/(slug+('.pdf' if '.pdf' in url else '.html'))
 try:
  if not p.exists():
   b=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read()
   if len(b)<500:raise ValueError('Empty/short response')
   p.write_bytes(b)
  rows.append({'id':slug,'url':url,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'readScope':'pending'});print(slug,len(p.read_bytes()),flush=True)
 except Exception as e:rows.append({'id':slug,'url':url,'error':str(e)});print(slug,str(e),flush=True)
(O/'eu-institutional-manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
