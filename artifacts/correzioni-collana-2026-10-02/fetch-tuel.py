from pathlib import Path
import subprocess,concurrent.futures,hashlib,json,re
from html.parser import HTMLParser
class Extractor(HTMLParser):
 def __init__(self):
  super().__init__();self.parts=[];self.active=None;self.depth=0;self.buf=[];self.label='';self.vig=''
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if self.active:
   if tag not in ('br','hr','img','input','meta','link'):self.depth+=1
   self.buf.append(' ')
  elif a.get('class')=='art-comma-div-akn' or a.get('id')=='artInizio':
   self.active=a.get('class') if a.get('id')!='artInizio' else 'vig';self.depth=1;self.buf=[]
 def handle_data(self,data):
  if self.active:self.buf.append(data)
 def handle_endtag(self,tag):
  if not self.active:return
  self.depth-=1
  if self.depth==0:
   value=re.sub(r'\s+',' ',''.join(self.buf)).strip()
   if self.active=='vig':self.vig=value
   else:self.parts.append(value)
   self.active=None
base=Path('artifacts/correzioni-collana-2026-10-02/normattiva-tuel');base.mkdir(exist_ok=True)
articles=[6,32,39,42,48,49,50,54,97,107,124,134,147,151,163,169,170,175,183,184,186,187,188,191,192,193,194,223,227,234,235,239,244]
def fetch(n):
 url=f'https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2000-08-18;267~art{n}!vig='
 p=base/f'art{n}.html'
 if not p.exists():
  r=subprocess.run(['curl.exe','-sS','-L','--max-time','40',url,'-o',str(p)],capture_output=True,text=True)
  if r.returncode:return {'article':n,'error':r.stderr}
 soup=Extractor();soup.feed(p.read_text(encoding='utf8'));parts=soup.parts;text='\n\n'.join(parts)
 if not parts:return {'article':n,'error':'No full comma text found','bytes':p.stat().st_size}
 (base/f'art{n}.txt').write_text(text,encoding='utf8')
 return {'article':n,'url':url,'html':str(p).replace('\\','/'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'versionFrom':soup.vig,'commasExtracted':len(parts),'characters':len(text),'readComplete':False,'numbering':'official comma labels from HTML'}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(fetch,articles))
(base/'manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'downloaded':sum('error' not in x for x in rows),'errors':[x for x in rows if 'error'in x]}))
extra=[('imu-commi','stato:legge:2019-12-27;160~art1-com740',list(range(740,750))),('tari-commi','stato:legge:2013-12-27;147~art1-com641',list(range(641,650))+[668]),('accertamento-commi','stato:legge:2006-12-27;296~art1-com161',[161,163]),('tuel-revisori','stato:decreto.legge:2011-08-13;138~art16',[25])]
for name,urn,commas in extra:
 p=base/f'{name}.html';url='https://www.normattiva.it/uri-res/N2Ls?urn:nir:'+urn+'!vig='
 cookie=base/f'{name}-session.txt'
 subprocess.run(['curl.exe','-sS','-L','-c',str(cookie),'--max-time','50',url,'-o',str(p)],check=True)
 parser=Extractor();parser.feed(p.read_text(encoding='utf8'))
 selected=[s for s in parser.parts if re.match(r'^(\d+)\.',s) and int(re.match(r'^(\d+)\.',s)[1]) in commas]
 if not selected:
  links=re.findall(r"showArticle\('([^']+)'\)",p.read_text(encoding='utf8'))
  if links:
   target=1+(min(commas)-1)//100
   url='https://www.normattiva.it'+re.sub(r'art.progressivo=\d+',f'art.progressivo={target}',links[-1]).replace(' ','%20').replace('&amp;','&')
   block=base/f'{name}-block.html'
   subprocess.run(['curl.exe','-sS','-L','-b',str(cookie),'--max-time','50',url,'-o',str(block)],check=True)
   parser=Extractor();parser.feed(block.read_text(encoding='utf8'));p=block
   selected=[s for s in parser.parts if re.match(r'^(\d+)\.',s) and int(re.match(r'^(\d+)\.',s)[1]) in commas]
 (base/f'{name}.txt').write_text('\n\n'.join(selected),encoding='utf8')
 print(json.dumps({'name':name,'url':url,'selected':len(selected),'characters':sum(map(len,selected)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
