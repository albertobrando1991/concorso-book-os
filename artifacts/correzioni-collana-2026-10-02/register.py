import json,sys,hashlib
from pathlib import Path

volume=sys.argv[1]
root=Path('artifacts/correzioni-collana-2026-10-02'); root.mkdir(parents=True,exist_ok=True)
target=root/(volume+'-changes.json')
audit=json.loads(Path('artifacts/review-integrale-2026-10-02',volume+'-ledger.json').read_text(encoding='utf8'))
findings=audit.get('findingsDetails',audit.get('findings',[]))
if not findings:
 for line in Path('wiki/reviews/audit-integrale-2026-10-02',volume+'.md').read_text(encoding='utf8').splitlines():
  if line.startswith('| V'+volume[-2:]+'-'):
   cells=[s.strip() for s in line.strip('|').split('|')]
   paths=[f['path'] for f in audit['files'] if cells[0] in f.get('findings',[])]
   findings.append({'id':cells[0],'path':paths[0] if paths else 'wiki/reviews/audit-integrale-2026-10-02/'+volume+'.md','proposal':cells[5]})
state=json.loads(target.read_text(encoding='utf8')) if target.exists() else {'volume':volume,'changes':{},'limitations':['Nuovi PDF e relativi controlli visivi ancora necessari. Nessuna dichiarazione di pubblicabilità.']}
if len(sys.argv)>2:
 update=json.loads(Path(sys.argv[2]).read_text(encoding='utf8'));state['changes'].update(update)
for fid,x in state['changes'].items():
 x['sha256']={p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in x.get('files',[]) if Path(p).exists()}
target.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
rows=[f'# {volume} — Registro delle correzioni autorizzate','', 'Mandato: applicare le correzioni e integrazioni dell’audit integrale del 2 ottobre 2026. Il rapporto storico resta immutato.','', 'Stati: **pendente**, **applicato** (modifica presente), **verificato** (riesame testuale e riscontro indicati conclusi). I gate e i controlli PDF sono dichiarati separatamente.','', '| ID | Modifica | File | Evidenza | Stato |','| --- | --- | --- | --- | --- |']
for f in findings:
 x=state['changes'].get(f['id'],{})
 files=x.get('files',[f['path']]); links=', '.join(f'[{Path(p).name}](../../../{p})' for p in files)
 fields=[f['id'],x.get('change',f.get('proposal','Intervento da eseguire')),links,x.get('evidence','Non ancora eseguita'),x.get('status','pendente')]
 rows.append('| '+' | '.join(s.replace('|','/').replace('\n',' ') for s in fields)+' |')
rows+=['','## Verifiche e limiti','']+['- '+s for s in state['limitations']]
report=Path('wiki/reviews/correzioni-collana-2026-10-02',volume+'.md');report.parent.mkdir(parents=True,exist_ok=True);report.write_text('\n'.join(rows)+'\n',encoding='utf8')
print(json.dumps({'volume':volume,'total':len(findings),'applied':len(state['changes']),'pending':len(findings)-len(state['changes'])}))
