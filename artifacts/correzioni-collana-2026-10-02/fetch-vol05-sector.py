from pathlib import Path
import json,subprocess,hashlib,concurrent.futures,sys
from html.parser import HTMLParser
import fitz
D=Path('wiki/raw/correzioni-vol05-2026-10-03');O=Path('artifacts/correzioni-collana-2026-10-02/norme-vol05')
class Plain(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,x):
  if not self.skip and x.strip():self.parts.append(x.strip())
name=sys.argv[1];jobs=json.loads((O/f'{name}-jobs.json').read_text(encoding='utf8'))
def run(j):
 slug,u=j;p=D/slug
 if not p.exists():subprocess.run(['curl.exe','-sS','-L','--max-time','60',u,'-o',str(p)],check=True)
 if p.suffix=='.pdf':
  try:
   doc=fitz.open(p);txt='\n'.join(f'\nPAGE {i+1}\n'+page.get_text() for i,page in enumerate(doc))
  except Exception as err:
   return {'id':slug,'url':u,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'characters':0,'readComplete':False,'valid':False,'error':str(err)}
 else:q=Plain();q.feed(p.read_text(encoding='utf8'));txt='\n\n'.join(q.parts)
 (O/(p.stem+'.txt')).write_text(txt,encoding='utf8');return {'id':slug,'url':u,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'characters':len(txt),'readComplete':False}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:rows=list(e.map(run,jobs))
f=O/f'{name}-manifest.json';old=json.loads(f.read_text(encoding='utf8')) if f.exists() else [];scopes={r['id']:r for r in old}
for r in rows:
 if r['id'] in scopes:r.update({k:v for k,v in scopes[r['id']].items() if k in ['readComplete','scope']})
f.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print([(r['id'],r['characters']) for r in rows])
