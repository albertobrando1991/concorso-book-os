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
base=Path('wiki/raw/correzioni-vol05-2026-10-03');base.mkdir(exist_ok=True);out=Path('artifacts/correzioni-collana-2026-10-02/norme-vol05');out.mkdir(exist_ok=True)
groups=[('agcm', 'legge:1990-10-10;287', [10, 11, 14, '14bis', '14ter', '14quater', 15, 16]), ('arera', 'legge:1995-11-14;481', [2]), ('agcom', 'legge:1997-07-31;249', [1]), ('collegi', 'decreto.legge:2011-12-06;201', [23]), ('consob', 'decreto.legge:1974-04-08;95', [1]), ('risparmio', 'legge:2005-12-28;262', [19]), ('ivass', 'decreto.legge:2012-07-06;95', [13]), ('privacy', 'decreto.legislativo:2003-06-30;196', [153, 155, 156, 157, 158, 166]), ('anac', 'decreto.legge:2014-06-24;90', [19]), ('civit', 'decreto.legislativo:2009-10-27;150', [13]), ('tuf', 'decreto.legislativo:1998-02-24;58', [5, 21, 94, 106, '187septies', 195]), ('tub', 'decreto.legislativo:1993-09-01;385', [5, 53, 67, 80, 145]), ('processo', 'decreto.legislativo:2011-09-01;150', [10]), ('consumo', 'decreto.legislativo:2005-09-06;206', [20, 21, 22, 23, 24, 25, 26, 27, '37bis']), ('whistle', 'decreto.legislativo:2023-03-10;24', [1, 2, 3, 4, 5, 6, 8, 12, 16, 17, 19]), ('contratti', 'decreto.legislativo:2023-03-31;36', [220, 222])]
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
