from pathlib import Path
import json,hashlib
A=Path(__file__).parent;f=A/'M-TR02-freeze.json';d=json.loads(f.read_text(encoding='utf8'));delta=json.loads((A/'VOL-09-final-form-delta.json').read_text(encoding='utf8'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
changed=[]
for r in d['files']:
 current=sha(r['path'])
 if current!=r['sha256']:
  assert Path(r['path'])==Path(delta['path']) and r['sha256']==delta['beforeSha256'] and current==delta['afterSha256']
  changed.append(r['path']);r['sha256']=current
assert len(changed)==1
d['controlledLayoutCorrections'].append({'date':'2026-10-03','note':'P09-07: rimossi il segno più residuo e la fusione dei due campi; testo e fonti invariati salvo separazione dei paragrafi. Gate 14 e 15 superati senza warning.','files':[delta]})
f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
p=Path('wiki/reviews/pipeline/VOL-09/16-moduli-m-tr02-appalti-pnrr-fondi-ue.md');t=p.read_text(encoding='utf8');assert delta['beforeSha256'] in t;t=t.replace(delta['beforeSha256'],delta['afterSha256']);t+='\n\nDelta P09-07, 3 ottobre 2026: riletti i due campi della scheda; confronto byte per byte dei restanti file del manifest invariato. Audit 14 e 15 ripetuti via CLI, senza blocker o warning. Manifest precedente conservato in M-TR02-freeze-before-final-form.json. Il nuovo PDF richiede ancora verifica del delta.\n';p.write_text(t,encoding='utf8')
print(json.dumps({'filesVerified':len(d['files']),'changed':changed}))
