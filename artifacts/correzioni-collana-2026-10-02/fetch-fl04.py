from pathlib import Path
import subprocess,concurrent.futures,json,hashlib,re
from html.parser import HTMLParser
class Extractor(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.depth=0;self.buf=[]
 def handle_starttag(self,tag,attrs):
  if self.depth:
   if tag not in ('br','hr','img','input','meta','link'):self.depth+=1
   self.buf.append(' ')
  elif dict(attrs).get('class') in ('art-comma-div-akn','art-just-text-akn','attachment-just-text'):self.depth=1;self.buf=[]
 def handle_data(self,data):
  if self.depth:self.buf.append(data)
 def handle_endtag(self,tag):
  if not self.depth:return
  self.depth-=1
  if not self.depth:self.parts.append(re.sub(r'\s+',' ',''.join(self.buf)).strip())
base=Path('artifacts/correzioni-collana-2026-10-02/normattiva-fl04');base.mkdir(exist_ok=True)
groups=[('l65','stato:legge:1986-03-07;65',[3,4,5,9]),('cds','stato:decreto.legislativo:1992-04-30;285',[38,43,80,116,141,142,145,146,148,172,173,180,186,187,189,193,196,200,201,202,203,'204bis']),('l689','stato:legge:1981-11-24;689',[2,3,6,28]),('d150','stato:decreto.legislativo:2011-09-01;150',[6,7]),('d286','stato:decreto.legislativo:1998-07-25;286',[5,6]),('dl14','stato:decreto.legge:2017-02-20;14',[9,10]),('d59','stato:decreto.legislativo:2010-03-26;59',[71]),('dpr380','stato:decreto.del.presidente.della.repubblica:2001-06-06;380',[27,31,44]),('d152','stato:decreto.legislativo:2006-04-03;152',[192,255,'255bis','255ter','232bis','232ter']),('allegato-cpp','stato:decreto.del.presidente.della.repubblica:1988-09-22;447',[55,57,347,349,350,351,354,355,356]),('allegato-tulps','stato:regio.decreto:1931-06-18;773',[1,8,9,10,11,68,69,80,100]),('allegato-cp','stato:regio.decreto:1930-10-19;1398',['589bis','590bis'])]
groups += [('cds','stato:decreto.legislativo:1992-04-30;285',['186bis','218ter']),('disp-cpp','stato:decreto.legislativo:1989-07-28;271',[113,114]),('l241','stato:legge:1990-08-07;241',['19bis',20]),('d114','stato:decreto.legislativo:1998-03-31;114',[4]),('dl201','stato:decreto.legge:2024-12-27;201',[7]),('dpr616','stato:decreto.del.presidente.della.repubblica:1977-07-24;616',[19]),('l182','stato:legge:2025-12-02;182',[34]),('allegato-cpp','stato:decreto.del.presidente.della.repubblica:1988-09-22;447',[63,64])]
items=[(f'{name}-art{n}',f'{urn}~art{n}') for name,urn,arts in groups for n in arts]
def fetch(item):
 name,urn=item;p=base/f'{name}.html';url='https://www.normattiva.it/uri-res/N2Ls?urn:nir:'+urn+'!vig='
 if name.startswith('allegato-'):
  cookie=base/(name+'.cookies');index=base/(name+'-index.html')
  if not index.exists():subprocess.run(['curl.exe','-sS','-L','--retry','2','--max-time','60','-c',str(cookie),url,'-o',str(index)],check=True)
  wanted=name.split('-art')[1]
  links=re.findall(r"showArticle\('([^']+)'[^>]*>([^<]+)</a>",index.read_text(encoding='utf-8'))
  candidates=[u for u,label in links if label.replace('art.','').replace(' ','').replace('-','').strip()==wanted]
  if not candidates:raise ValueError((name,'no article link'))
  url='https://www.normattiva.it'+candidates[0]
  if not p.exists():subprocess.run(['curl.exe','-sS','-L','--retry','2','--max-time','60','-b',str(cookie),url,'-o',str(p)],check=True)
 elif not p.exists():subprocess.run(['curl.exe','-sS','-L','--retry','2','--max-time','60',url,'-o',str(p)],check=True)
 parser=Extractor();parser.feed(p.read_text(encoding='utf-8'));text='\n\n'.join(parser.parts)
 (base/f'{name}.txt').write_text(text,encoding='utf-8')
 return {'name':name,'url':url,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'parts':len(parser.parts),'characters':len(text),'readComplete':False}
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for future in [ex.submit(fetch,item) for item in items]:
  try:rows.append(future.result())
  except Exception as e:print(str(e),flush=True)
(base/'manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{k:v for k,v in x.items() if k in ['name','characters','parts']} for x in rows]))
