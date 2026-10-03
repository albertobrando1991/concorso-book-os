from pathlib import Path
import subprocess, concurrent.futures, json, hashlib, re
from html.parser import HTMLParser
class Parser(HTMLParser):
 def __init__(self): super().__init__(); self.depth=0; self.parts=[]; self.buf=[]
 def handle_starttag(self,tag,attrs):
  if self.depth:
   if tag not in ('br','hr','img','input','meta','link'): self.depth+=1
   self.buf.append(' ')
  elif dict(attrs).get('class') in ('art-comma-div-akn','art-just-text-akn','attachment-just-text'): self.depth=1; self.buf=[]
 def handle_data(self,data):
  if self.depth:self.buf.append(data)
 def handle_endtag(self,tag):
  if self.depth:
   self.depth-=1
   if not self.depth:self.parts.append(re.sub(r'\s+',' ',''.join(self.buf)).strip())
A=Path('artifacts/correzioni-collana-2026-10-02/norme-vol04');A.mkdir(exist_ok=True)
R=Path('wiki/raw/correzioni-vol04-2026-10-03');R.mkdir(exist_ok=True)
groups=[
 ('feriale','legge:1969-10-07;742',[1,3]),
 ('ordinamento-allegato','regio.decreto:1941-01-30;12',[42,48,56,65,70,73]),
 ('ordinamento','regio.decreto:1941-01-30;12',[42,48,56,65,70,73]),
 ('assise','legge:1951-04-10;287',[3,4]),
 ('trib-minori','regio.decreto.legge:1934-07-20;1404',[2]),
 ('dl144','decreto.legge:2026-08-07;144',[7]),
 ('upp','decreto.legislativo:2022-10-10;151',[1,2,3,4,5,6,7,8,9]),
 ('dl100','decreto.legge:2026-06-12;100',[1,2,3,4,5,6,7,8,9,10,11,12]),
 ('dirigenza','decreto.legislativo:2006-07-25;240',[1,2,3,4]),
 ('spese','decreto.del.presidente.della.repubblica:2002-05-30;115',[9,10,11,13,14,16,71,76,77,78,79,82,83,99,106,112,113,115,124,126,131,136,168,170,227]),
 ('casellario','decreto.del.presidente.della.repubblica:2002-11-14;313',[3,5,24,'25bis',27,28,30,31,39,41]),
 ('cpc','regio.decreto:1940-10-28;1443',[132,133,134,135,139,140,143,155,'163bis',165,166,167,'171bis','171ter',183,'281decies','281undecies','281duodecies',325,326,327,409,414,415,416,474,475,480,481,482,'492bis',497,543,555]),
 ('disp-cpc','regio.decreto:1941-12-18;1368',[76,'196sexies']),
 ('cpp','decreto.del.presidente.della.repubblica:1988-09-22;447',[60,61,64,116,335,407,408,409,410,411,'415bis',416,431,438,440,442,444,445,449,453,459,460,'464bis','464quater','464septies',585,593]),
 ('minori','decreto.del.presidente.della.repubblica:1988-09-22;448',[9,28,29]),
 ('comunita','decreto.legislativo:2018-10-02;121',[2,3,4,5,6,7,8]),
 ('riparativa','decreto.legislativo:2022-10-10;150',[42,43,44,45,48,50,51,52,53,54,58]),
 ('penitenziario','legge:1975-07-26;354',['4bis',13,15,21,'30ter',35,'35bis','35ter',36,37,38,39,40,41,47,'47ter',48,50,54,59,60,61,69]),
 ('reg-penitenziario','decreto.del.presidente.della.repubblica:2000-06-30;230',[27,29,68]),
 ('cp','regio.decreto:1930-10-19;1398',[97,98,'168bis','168ter','168quater']),
]
def fetch(job):
 name,urn,art=job; p=R/f'{name}-art{art}.html'
 url=f'https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:{urn}~art{art}!vig='
 try:
  if name in ('cpc','cpp','disp-cpc','cp','ordinamento-allegato'):
   idx=A/f'{name}-art{art}-index.html';cookie=A/f'{name}-art{art}.cookie'
   if not idx.exists():subprocess.run(['curl.exe','-sS','-L','--retry','2','--max-time','50','-c',str(cookie),url,'-o',str(idx)],check=True)
   links=re.findall(r"showArticle\('([^']+)'[^>]*>([^<]+)</a>",idx.read_text('utf-8'))
   wanted=str(art).replace('-','')
   found=[u for u,label in links if label.replace('art.','').replace(' ','').replace('-','').strip()==wanted]
   if not found:raise ValueError('articolo non trovato nel sommario')
   url='https://www.normattiva.it'+found[0]
   if not p.exists():subprocess.run(['curl.exe','-sS','-L','--retry','2','--max-time','50','-b',str(cookie),url,'-o',str(p)],check=True)
  elif not p.exists():subprocess.run(['curl.exe','-sS','-L','--retry','2','--max-time','50',url,'-o',str(p)],check=True)
  parser=Parser();parser.feed(p.read_text('utf-8'));t='\n\n'.join(parser.parts)
  (A/f'{name}-art{art}.txt').write_text(t,'utf-8')
  return dict(name=name,article=art,url=url,path=p.as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),characters=len(t),readComplete=False,validExtraction=name not in ('ordinamento','assise'))
 except Exception as e:return dict(name=name,article=art,url=url,error=str(e),readComplete=False)
jobs=[(name,urn,n) for name,urn,arts in groups for n in arts]
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 for row in pool.map(fetch,jobs):
  rows.append(row)
  if len(rows)%10==0:print('Acquisiti',len(rows),'/',len(jobs),flush=True)
(A/'manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf-8')
print('Fine',len(rows),'vuoti/errori',[(r['name'],r['article'],r.get('error')) for r in rows if r.get('characters',0)<30])
