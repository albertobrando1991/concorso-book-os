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
base=Path('wiki/raw/correzioni-vol11-2026-10-03');base.mkdir(exist_ok=True);out=Path('artifacts/correzioni-collana-2026-10-02/norme-vol11');out.mkdir(exist_ok=True)
groups=[('ambiente','decreto.legislativo:2006-04-03;152',['3bis','3ter','3quater','3quinquies','3sexies',6,'7bis',12,13,14,15,19,23,24,25,27,'27bis','29quater','29sexies','29octies','29nonies',64,76,103,104,117,121,124,133,137,'184bis','184ter',188,'188bis',190,193,208,212,214,216,240,242,250,255,256,258,269,272,279,'298bis',300,303,'318bis','318ter','318quater','318quinquies','318sexies','318septies']),('aua','decreto.del.presidente.della.repubblica:2013-03-13;59',[1,2,3,4,5,6]),('snpa','legge:2016-06-28;132',[1,3,6,9,10]),('natura','decreto.del.presidente.della.repubblica:1997-09-08;357',[5]),('informazione','decreto.legislativo:2005-08-19;195',[2,3,5]),('pc','decreto.legislativo:2018-01-02;1',[7,9,12,18,39,40]),('fer','decreto.legislativo:2024-11-25;190',[6,7,8,9]),('cer','decreto.legislativo:2021-11-08;199',[31,32]),('efficienza','decreto.legislativo:2014-07-04;102',[5,8]),('edifici','decreto.legislativo:2005-08-19;192',[3,6]),('seveso','decreto.legislativo:2015-06-26;105',[13,15,20,21])]
groups.append(('sanzioni','legge:1981-11-24;689',[14,16,18]))
groups.append(('danno','legge:2013-08-06;97',[25]))
jobs=[(name,urn,n) for name,urn,nums in groups for n in nums]
def fetch(job):
 name,urn,n=job;url=f'https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:{urn}~art{n}!vig=';p=base/f'{name}-art{n}.html'
 try:
  if not p.exists():subprocess.run(['curl.exe','-sS','-L','--max-time','60',url,'-o',str(p)],check=True)
  parser=Parser();parser.feed(p.read_text(encoding='utf8'));text='\n\n'.join(parser.parts);(out/f'{name}-art{n}.txt').write_text(text,encoding='utf8')
  return dict(name=name,article=n,url=url,path=p.as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),characters=len(text),readComplete=False)
 except Exception as e:return dict(name=name,article=n,url=url,error=str(e),readComplete=False)
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for row in pool.map(fetch,jobs):
  rows.append(row)
  if len(rows)%10==0:print('Fetched',len(rows),'of',len(jobs),flush=True)
(out/'manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print('Complete',len(rows),'empty/errors:',[(r['name'],r['article']) for r in rows if r.get('characters',0)<20])
