from pathlib import Path
import subprocess,json,hashlib,re,concurrent.futures
from html.parser import HTMLParser
header=Path('artifacts/correzioni-collana-2026-10-02/fetch-vol05.py').read_text(encoding='utf8').split("base=Path(")[0];exec(header)
D=Path('wiki/raw/correzioni-vol05-2026-10-03');O=Path('artifacts/correzioni-collana-2026-10-02/norme-vol05')
jobs=[('istruttoria','decreto.del.presidente.della.repubblica:1998-04-30;217',n) for n in [6,7,9,10,12,13,14]]
jobs += [('tuf-riforma','decreto.legislativo:2026-06-25;128',10)]
def run(job):
 slug,urn,n=job;u=f'https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:{urn}~art{n}!vig=';p=D/f'{slug}-art{n}.html'
 if not p.exists():subprocess.run(['curl.exe','-sS','-L','--max-time','60',u,'-o',str(p)],check=True)
 q=Parser();q.feed(p.read_text(encoding='utf8'));txt='\n\n'.join(q.parts);(O/f'{slug}-art{n}.txt').write_text(txt,encoding='utf8');return {'id':slug,'article':n,'url':u,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'characters':len(txt),'readComplete':False}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:rows=list(e.map(run,jobs))
f=O/'procedure-manifest.json';old=json.loads(f.read_text(encoding='utf8')) if f.exists() else [];scopes={(r['id'],r['article']):r.get('readComplete',False) for r in old}
for row in rows:row['readComplete']=scopes.get((row['id'],row['article']),False)
f.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print([(r['id'],r['article'],r['characters']) for r in rows])
idx=O/'cpa-index.html';cookies=O/'cpa-cookies.txt';indexurl='https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2010-07-02;104!vig='
if not idx.exists():subprocess.run(['curl.exe','-sS','-L','--max-time','60','-c',str(cookies),indexurl,'-o',str(idx)],check=True)
links=re.findall(r"showArticle\('([^']+)'[^>]*>([^<]+)</a>",idx.read_text(encoding='utf8'));cparows=[]
for n in [14,29,112,119,133,134,135]:
 candidates=[u for u,label in links if label.replace('art.','').replace(' ','').strip()==str(n) and 'flagTipoArticolo=2&' in u]
 assert candidates, n
 u='https://www.normattiva.it'+candidates[-1];p=D/f'cpa-art{n}.html'
 if not p.exists():subprocess.run(['curl.exe','-sS','-L','--max-time','60','-b',str(cookies),u,'-o',str(p)],check=True)
 q=Parser();q.feed(p.read_text(encoding='utf8'));txt='\n\n'.join(q.parts);(O/f'cpa-art{n}.txt').write_text(txt,encoding='utf8');cparows.append({'article':n,'url':u,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'characters':len(txt),'readComplete':False});print('CPA',n,len(txt),flush=True)
(O/'cpa-manifest.json').write_text(json.dumps(cparows,ensure_ascii=False,indent=2),encoding='utf8')
