from pathlib import Path
import re,json,hashlib
BASE=Path('wiki/books/il-metodo-bando/chapters')
REF='sources/vol-01-esempi-logica-inglese-metodo-2026-10-02.md'
changes={}
def save(slug,text,ids,ref=REF):
 p=BASE/(slug+'.md')
 text=re.sub(r'^updated_at:.*$', 'updated_at: 2026-10-03',text,flags=re.M)
 text=re.sub(r'^review_required:.*$', 'review_required: true',text,flags=re.M)
 text=re.sub(r'^draft_stage:.*$', 'draft_stage: editorial-review',text,flags=re.M)
 for key in ['source_refs','last_compiled_from']:
  line=next((l for l in text.splitlines() if l.startswith(key+':')),None)
  if line and ref not in line:text=text.replace(line,line[:-1]+', "'+ref+'"]',1)
 p.write_text(text,encoding='utf8')
 for id in ids:changes.setdefault(id,[]).append(p.as_posix())
def read(slug):return (BASE/(slug+'.md')).read_text(encoding='utf8')
def replace(text,old,new):
 if old not in text:raise ValueError('Missing anchor '+old[:90])
 return text.replace(old,new)
def record():
 p=Path('artifacts/correzioni-collana-2026-10-02/registro-applicazione.json')
 rows=json.loads(p.read_text(encoding='utf8'))
 for r in rows:
  if r['id'] in changes:
   r['status']='applicato-da-verificare';r['changedFiles']=list(dict.fromkeys(r.get('changedFiles',[])+changes[r['id']]+['wiki/'+REF]))
   r['verification']=['Delta applicato ai manoscritti; verifica indipendente, matrici e PDF/figure ancora da completare']
   r['fileHashes']={f:hashlib.sha256(Path(f).read_bytes()).hexdigest() for f in changes[r['id']]}
 p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
 print(json.dumps(changes,ensure_ascii=False))
