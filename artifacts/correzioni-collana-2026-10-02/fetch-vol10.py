from pathlib import Path
import subprocess,concurrent.futures,json,hashlib,re
from html.parser import HTMLParser
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.active=False;self.depth=0;self.buf=[];self.parts=[]
 def handle_starttag(self,tag,attrs):
  if self.active:
   if tag not in ('br','hr','img','input','meta','link'):self.depth+=1
   self.buf.append(' ')
  elif dict(attrs).get('class') in ('art-comma-div-akn','art-just-text-akn','attachment-just-text'):self.active=True;self.depth=1;self.buf=[]
 def handle_data(self,data):
  if self.active:self.buf.append(data)
 def handle_endtag(self,tag):
  if self.active:
   self.depth-=1
   if self.depth==0:self.parts.append(re.sub(r'\s+',' ',''.join(self.buf)).strip());self.active=False
base=Path('wiki/raw/correzioni-vol10-2026-10-03'); out=Path('artifacts/correzioni-collana-2026-10-02/norme-vol10');out.mkdir(exist_ok=True)
groups=[('codice','decreto.legislativo:2023-03-31;36',[17,41,43,50,108]),('sicurezza','decreto.legislativo:2008-04-09;81',[90,92]),('espropri','decreto.del.presidente.della.repubblica:2001-06-08;327',[9,39]),('edilizia','decreto.del.presidente.della.repubblica:2001-06-06;380',[3,'6-bis',20,22,23,'34-bis',36,'36-bis']),('civile','regio.decreto:1942-03-16;262',[822,823,826,828]),('strade','decreto.legislativo:1992-04-30;285',[2]),('semplificazione','legge:2025-12-02;182',[40]),('procedimento','legge:1990-08-07;241',[14,19])]
jobs=[(name,urn,n) for name,urn,nums in groups for n in nums]
jobs += [('edilizia','decreto.del.presidente.della.repubblica:2001-06-06;380',n) for n in ['6bis','34bis','36bis']]
def fetch(job):
 name,urn,n=job;url=f'https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:{urn}~art{n}!vig='
 p=base/f'{name}-art{n}.html'
 if not p.exists():subprocess.run(['curl.exe','-sS','-L','--max-time','50',url,'-o',str(p)],check=True)
 parser=Parser();parser.feed(p.read_text(encoding='utf8'));text='\n\n'.join(parser.parts);(out/f'{name}-art{n}.txt').write_text(text,encoding='utf8')
 return dict(name=name,article=n,url=url,path=p.as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),characters=len(text),readComplete=False)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(fetch,jobs))
(out/'manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps([{'name':r['name'],'article':r['article'],'characters':r['characters']} for r in rows]))
linkjobs=[]
for n in [822,823,826,828]:
 s=(base/'civile-art822.html').read_text(encoding='utf8')
 links=re.findall(r"showArticle\('([^']+)'",s)
 link=next(x for x in links if f'art.idArticolo={n}&' in x)
 linkjobs.append((f'civile-codice-art{n}',link))
s=(base/'codice-art43.html').read_text(encoding='utf8')
for annex,nums in [('I.7',[5,27,31]),('I.9',[1]),('II.14',[7,12,28])]:
 # Read the current article URL from the act's own table of contents.
 hit=re.search(r'(?:Allegato|ALLEGATO)\s+'+re.escape(annex)+r'\s*</',s)
 if not hit:raise RuntimeError('Annex not found '+annex)
 section=s[hit.start():];section=section[:section.find('box_allegati_small',100)]
 links=re.findall(r"showArticle\('([^']+)'",section)
 for n in nums:linkjobs.append((f'{annex.lower().replace(".","")}-art{n}',next(x for x in links if f'art.idArticolo={n}&' in x)))
def fetchlink(job):
 name,link=job
 flag=re.search(r'art.flagTipoArticolo=(\d+)',link)[1];n=re.search(r'art.idArticolo=(\d+)',link)[1]
 urn='1942;262' if name.startswith('civile') else '2023;36'
 url=f'https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:{urn}:{flag}~art{n}!vig='
 p=base/f'{name}-urn.html';kind='civile' if name.startswith('civile') else 'codice'
 if name=='civile-codice-art826':p=base/f'{name}-urn-complete.html'
 if not p.exists():subprocess.run(['curl.exe','-sS','-L','-b',str(out/f'{kind}-session.txt'),'--max-time','50',url,'-o',str(p)],check=True)
 parser=Parser();parser.feed(p.read_text(encoding='utf8'));text='\n\n'.join(parser.parts);(out/f'{name}.txt').write_text(text,encoding='utf8')
 return dict(name=name,url=url,path=p.as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),characters=len(text),readComplete=False)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:extras=list(pool.map(fetchlink,linkjobs))
(out/'manifest-extra.json').write_text(json.dumps(extras,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps([{'name':r['name'],'characters':r['characters']} for r in extras]))
