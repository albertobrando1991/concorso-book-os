from pathlib import Path
import subprocess,concurrent.futures,json,hashlib,re
from html.parser import HTMLParser
class Extractor(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.depth=0;self.buf=[]
 def handle_starttag(self,tag,attrs):
  if self.depth:
   if tag not in ('br','hr','img','input','meta','link'):self.depth+=1
   self.buf.append(' ')
  elif dict(attrs).get('class')=='art-comma-div-akn':self.depth=1;self.buf=[]
 def handle_data(self,data):
  if self.depth:self.buf.append(data)
 def handle_endtag(self,tag):
  if not self.depth:return
  self.depth-=1
  if not self.depth:self.parts.append(re.sub(r'\s+',' ',''.join(self.buf)).strip())
base=Path('artifacts/correzioni-collana-2026-10-02/normattiva-fl02');base.mkdir(exist_ok=True)
items=[('l131-art8','stato:legge:2003-06-05;131~art8'),('d281-art8','stato:decreto.legislativo:1997-08-28;281~art8'),('d281-art9','stato:decreto.legislativo:1997-08-28;281~art9'),('d118-art36','stato:decreto.legislativo:2011-06-23;118~art36'),('d118-art39','stato:decreto.legislativo:2011-06-23;118~art39'),('d118-art50','stato:decreto.legislativo:2011-06-23;118~art50'),('d118-art63','stato:decreto.legislativo:2011-06-23;118~art63'),('d118-art68','stato:decreto.legislativo:2011-06-23;118~art68'),('l56-art1','stato:legge:2014-04-07;56~art1')]
def fetch(item):
 name,urn=item;p=base/f'{name}.html';url='https://www.normattiva.it/uri-res/N2Ls?urn:nir:'+urn+'!vig='
 if not p.exists():subprocess.run(['curl.exe','-sS','-L','--max-time','50',url,'-o',str(p)],check=True)
 parser=Extractor();parser.feed(p.read_text(encoding='utf8'));text='\n\n'.join(parser.parts)
 (base/f'{name}.txt').write_text(text,encoding='utf8')
 return {'name':name,'url':url,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'parts':len(parser.parts),'characters':len(text),'readComplete':False}
items += [('d118-art18','stato:decreto.legislativo:2011-06-23;118~art18'),('d118-art57','stato:decreto.legislativo:2011-06-23;118~art57'),('d118-art58','stato:decreto.legislativo:2011-06-23;118~art58')]
items += [('l23-art3','stato:legge:1996-01-11;23~art3')]
items += [(f'd201-art{n}',f'stato:decreto.legislativo:2022-12-23;201~art{n}') for n in [2,4,14,17,27,30,32]]
items += [(f'd175-art{n}',f'stato:decreto.legislativo:2016-08-19;175~art{n}') for n in [2,16,20]]
items += [('d36-art177','stato:decreto.legislativo:2023-03-31;36~art177')]
items += [(f'd327-art{n}',f'stato:decreto.del.presidente.della.repubblica:2001-06-08;327~art{n}') for n in [8,9,12,13,23,24]]
old=json.loads((base/'manifest.json').read_text(encoding='utf8')) if (base/'manifest.json').exists() else []
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(fetch,items))
for x in rows:
 if any(y['name']==x['name'] and y['sha256']==x['sha256'] and y.get('readComplete') for y in old):x['readComplete']=True
(base/'manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(rows,ensure_ascii=False))
