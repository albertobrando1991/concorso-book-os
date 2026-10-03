from pathlib import Path
import json,hashlib,re
base=Path('artifacts/review-integrale-2026-10-02')
for p in sorted(base.glob('VOL-??-ledger.json')):
 d=json.loads(p.read_text(encoding='utf-8-sig')); rows=d.get('files',d.get('chapters',[]))
 bad=[]
 for r in rows:
  f=Path(r.get('path',r.get('file','')))
  if not f.exists() or hashlib.sha256(f.read_bytes()).hexdigest()!=r.get('sha256'):bad.append(str(f))
 print(p.name,'files',len(rows),'read',sum(r.get('readComplete')==True for r in rows),'changed',bad)
 print('keys',list(d.keys()))
for p in sorted(base.glob('VOL-??-current-export.json')):
 d=json.loads(p.read_text(encoding='utf-8-sig'))
 text=json.dumps([x for x in d if x['sectionType']!='chapter'],ensure_ascii=False)
 print(p.name,'appendici',[(x['title'],x['sectionType']) for x in d if 'appendic' in x['title'].lower()],'staff',[(s,text.lower().count(s)) for s in ['prima della pubblicazione','pubblicazione definitiva','verticale profondo']])
