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
base=Path('artifacts/correzioni-collana-2026-10-02/normattiva-fl03');base.mkdir(exist_ok=True)
items=[(f'l580-art{n}',f'stato:legge:1993-12-29;580~art{n}') for n in [8,9,10,11,12,14,15,16,17,20]]
items += [(f'cc-art{n}',f'stato:regio.decreto:1942-03-16;262~art{n}') for n in [2188,2189,2190,2191,2192,2193,2331]]
items += [('d228-art2','stato:decreto.legislativo:2001-05-18;228~art2'),('dl7-art9','stato:decreto.legge:2007-01-31;7~art9'),('l77-art4','stato:legge:1955-02-12;77~art4'),('l108-art17','stato:legge:1996-03-07;108~art17'),('d28-art12','stato:decreto.legislativo:2010-03-04;28~art12'),('cpc-art824bis','stato:regio.decreto:1940-10-28;1443~art824bis')]
items += [(f'codice-civile-art{n}',f'stato:codice.civile:1942-03-16;262~art{n}') for n in [2188,2189,2190,2191,2192,2193,2331]]
items += [('codice-procedura-civile-art824bis','stato:codice.procedura.civile:1940-10-28;1443~art824bis')]
items += [(f'allegato-civile-art{n}',f'stato:regio.decreto:1942-03-16;262~art{n}') for n in [2188,2189,2190,2191,2192,2193,2331]]
items += [('allegato-procedura-art824bis','stato:regio.decreto:1940-10-28;1443~art824bis')]
items += [(f'dm93-art{n}',f'ministero.sviluppo.economico:decreto:2017-04-21;93~art{n}') for n in [3,4,5,8,9,10,13,14]]
items += [('d150-art12','stato:decreto.legislativo:2011-09-01;150~art12'),('dl76-art40','stato:decreto.legge:2020-07-16;76~art40')]
def fetch(item):
 name,urn=item;p=base/f'{name}.html';url='https://www.normattiva.it/uri-res/N2Ls?urn:nir:'+urn+'!vig='
 if not p.exists():
  if name.startswith('allegato-'):
   cookie=base/(name+'.cookies');index=base/(name+'-index.html')
   subprocess.run(['curl.exe','-sS','-L','--retry','2','--max-time','50','-c',str(cookie),url,'-o',str(index)],check=True)
   wanted=name.split('-art')[1]
   links=re.findall(r"showArticle\('([^']+)'[^>]*>([^<]+)</a>",index.read_text(encoding='utf-8'))
   candidates=[u for u,label in links if label.replace('art.','').replace(' ','').replace('-','').strip()==wanted]
   if not candidates:raise ValueError((name,'no article link'))
   url='https://www.normattiva.it'+candidates[0]
   subprocess.run(['curl.exe','-sS','-L','--retry','2','--max-time','50','-b',str(cookie),url,'-o',str(p)],check=True)
  else:subprocess.run(['curl.exe','-sS','-L','--retry','2','--max-time','50',url,'-o',str(p)],check=True)
 if name.startswith('allegato-'):
  wanted=name.split('-art')[1]
  links=re.findall(r"showArticle\('([^']+)'[^>]*>([^<]+)</a>",(base/(name+'-index.html')).read_text(encoding='utf-8'))
  url='https://www.normattiva.it'+next(u for u,label in links if label.replace('art.','').replace(' ','').replace('-','').strip()==wanted)
 parser=Extractor();parser.feed(p.read_text(encoding='utf-8'));text='\n\n'.join(parser.parts)
 (base/f'{name}.txt').write_text(text,encoding='utf-8')
 invalid=name.startswith(('cc-','cpc-','codice-'))
 return {'name':name,'url':url,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'parts':len(parser.parts),'characters':len(text),'readComplete':False,'valid':not invalid,'limitation':'URN ha restituito articolo 1 del decreto di approvazione: escluso dalla prova' if invalid else ''}
old=json.loads((base/'manifest.json').read_text(encoding='utf-8')) if (base/'manifest.json').exists() else []
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(fetch,items))
for x in rows:
 if any(y['name']==x['name'] and y['sha256']==x['sha256'] and y.get('readComplete') for y in old):x['readComplete']=True
(base/'manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{k:v for k,v in x.items() if k in ['name','characters','parts']} for x in rows]))
