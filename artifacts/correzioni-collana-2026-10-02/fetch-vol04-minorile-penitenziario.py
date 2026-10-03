from pathlib import Path
import requests,re,html,json,hashlib,concurrent.futures
from html.parser import HTMLParser
A=Path('artifacts/correzioni-collana-2026-10-02/norme-vol04');R=Path('wiki/raw/correzioni-vol04-2026-10-03')
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.on=0;self.buf=[]
 def handle_starttag(self,tag,attrs):
  if self.on:
   if tag not in ('br','hr','img','input','meta','link'):self.on+=1
   self.buf.append(' ')
  elif dict(attrs).get('class') in ('art-comma-div-akn','art-just-text-akn','attachment-just-text'):self.on=1;self.buf=[]
 def handle_data(self,t):
  if self.on:self.buf.append(t)
 def handle_endtag(self,tag):
  if self.on:
   self.on-=1
   if not self.on:self.parts.append(re.sub(r'\s+',' ',''.join(self.buf)).strip())
jobs=[('minori-testo','decreto.del.presidente.della.repubblica:1988-09-22;448',n) for n in [1,6,9,12,13,28,29]]+[('penitenziario-integrativo','legge:1975-07-26;354',n) for n in [18,20]]
def fetch(job):
 name,urn,n=job;p=R/f'{name}-art{n}.html';url=f'https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:{urn}~art{n}!vig='
 if not p.exists():
  sess=requests.Session();resp=sess.get(url,timeout=40);resp.raise_for_status();links=re.findall(r"showArticle\('([^']+)'[^>]*>([^<]+)</a>",resp.text)
  matches=[u for u,label in links if ('art.idArticolo='+str(n)+'&') in html.unescape(u) and ('art.flagTipoArticolo=1&' in html.unescape(u) if name=='minori-testo' else True)]
  if matches:resp=sess.get('https://www.normattiva.it'+html.unescape(matches[0]),timeout=40);resp.raise_for_status()
  p.write_bytes(resp.content)
 par=Parser();par.feed(p.read_text(encoding='utf8'));t='\n\n'.join(par.parts);(A/f'{name}-art{n}.txt').write_text(t,encoding='utf8')
 return {'path':p.as_posix(),'url':url,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'characters':len(t),'readComplete':False}
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for result in pool.map(fetch,jobs):rows.append(result);print(result['path'],result['characters'],flush=True)
for year,n in [(2019,99),(2019,253),(2024,10),(2019,263),(2025,203),(2026,110),(2022,174)]:
 p=R/f'corte-{year}-{n}.html';url=f'https://www.cortecostituzionale.it/scheda-pronuncia/{year}/{n}'
 if not p.exists():resp=requests.get(url,timeout=40);resp.raise_for_status();p.write_bytes(resp.content)
 raw=p.read_text(encoding='utf8');s=html.unescape(re.sub('<[^>]+>',' ',raw));s=re.sub(r'\s+',' ',s);(A/f'corte-{year}-{n}.txt').write_text(s,encoding='utf8');rows.append({'path':p.as_posix(),'url':url,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'characters':len(s),'readComplete':False});print(p,len(s),flush=True)
(A/'manifest-minorile-penitenziario.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
