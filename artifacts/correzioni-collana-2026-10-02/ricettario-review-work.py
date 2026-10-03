from pathlib import Path
import json,sys,hashlib,shutil
A=Path(__file__).parent;D=A/'ricettario-review';D.mkdir(exist_ok=True)
bundle=json.loads((A/'digital-publication/VOL-01/bundle.json').read_text('utf8'))
units=[u for u in bundle['volume']['chapters'] if u['scope']=='ricettario']
if sys.argv[1]=='inventory':
 rows=[]
 for n,u in enumerate(units,1):
  p=Path(u['sourcePath']);text=p.read_text('utf8');target=D/'before'/p.name;target.parent.mkdir(exist_ok=True)
  if not target.exists():shutil.copy2(p,target)
  rows.append({'module':f'R{n:02}','source':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'words':len(text.split()),'title':u['title'],'images':sum(b['type']=='image' for b in u['blocks'])})
 (D/'inventory.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n','utf8')
 print(json.dumps(rows,ensure_ascii=False))
elif sys.argv[1]=='read':
 for value in sys.argv[2:]:
  n=int(value);u=units[n-1];p=Path(u['sourcePath'])
  print(f'\n===== R{n:02} {p} =====\n'+p.read_text('utf8'))
