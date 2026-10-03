from pathlib import Path
import subprocess,json,hashlib,concurrent.futures
from html.parser import HTMLParser
header=Path('artifacts/correzioni-collana-2026-10-02/fetch-vol05.py').read_text(encoding='utf8').split("base=Path(")[0];exec(header)
D=Path('wiki/raw/correzioni-vol05-2026-10-03');O=Path('artifacts/correzioni-collana-2026-10-02/norme-vol05')
class Plain(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,x):
  if not self.skip and x.strip():self.parts.append(x.strip())
jobs=[(f'agcm-art{n}',f'https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1990-10-10;287~art{n}!vig=',True) for n in ['2','3','6','15bis']]
jobs += [('consumer-green-art3','https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-02-20;30~art3!vig=',True)]
jobs += [(f'conflitto-art{n}',f'https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2004-07-20;215~art{n}!vig=',True) for n in [1,2,3,6]]
jobs += [('rating-faq','https://www.agcm.it/competenze/rating-di-legalita/FAQ-Regolamento-Rating-2026',False),('agcm-thresholds','https://www.agcm.it/per-le-imprese/Concorrenza/concentrazioni/soglie-di-fatturato',False),('consumer-procedure','https://agcm.it/per-le-imprese/imprese-e-consumatori/regolamento-agcm-sulle-procedure-istruttorie-in-materia-di-tutela-del-consumatore',False),('agcm-conflict','https://www.agcm.it/competenze/conflitto-di-interessi/',False),('agcm-clemenza','https://www.agcm.it/competenze/tutela-della-concorrenza/intese-e-abusi/programma-di-clemenza',False)]
def run(j):
 slug,u,norm=j;p=D/f'{slug}.html'
 if not p.exists():subprocess.run(['curl.exe','-sS','-L','--max-time','60',u,'-o',str(p)],check=True)
 q=Parser() if norm else Plain();q.feed(p.read_text(encoding='utf8'));txt='\n\n'.join(q.parts);(O/f'{slug}.txt').write_text(txt,encoding='utf8');return {'id':slug,'url':u,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'characters':len(txt),'readComplete':False}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:rows=list(e.map(run,jobs))
f=O/'agcm-specific-manifest.json';old=json.loads(f.read_text(encoding='utf8')) if f.exists() else [];scopes={r['id']:r.get('readComplete',False) for r in old}
for r in rows:r['readComplete']=scopes.get(r['id'],False)
f.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print([(r['id'],r['characters']) for r in rows])
