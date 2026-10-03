from pathlib import Path
import json,re,hashlib

root=Path('.')
dest=Path('artifacts/correzioni-collana-2026-10-02/VOL-02-changes.json')
state=json.loads(dest.read_text(encoding='utf8')) if dest.exists() else {'volume':'VOL-02','changes':{},'limitations':['Gate editoriali e normativi aperti; PDF da rigenerare e verificare.']}
audit=Path('wiki/reviews/audit-integrale-2026-10-02/VOL-02.md').read_text(encoding='utf8')
findings=[]
for line in audit.splitlines():
 if not line.startswith('| V02-'):continue
 cells=[x.strip() for x in line.strip('|').split('|')]
 findings.append({'id':cells[0],'files':[p.replace('../../../','',1) for p in re.findall(r'\]\(([^)]+)\)',cells[1])],'proposal':cells[5]})
state['findings']=findings
for fid,x in state['changes'].items():
 x['sha256']={p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in x.get('files',[]) if Path(p).exists()}
dest.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
lines=['# VOL-02 — Correzioni e integrazioni autorizzate','', 'Audit storico preservato. Il registro distingue intervento scritto, riesame testuale e chiusura dei gate. Nessuna attestazione di pubblicabilità finché restano rilievi aperti e produzione da verificare.','', '| ID | File | Intervento | Evidenza | Stato |','| --- | --- | --- | --- | --- |']
for f in sorted(findings,key=lambda x:x['id']):
 x=state['changes'].get(f['id'],{})
 vals=[f['id'],', '.join(f'[{Path(p).name}](../../../{p})' for p in x.get('files',f['files'])),x.get('change',f['proposal']),x.get('evidence','Da eseguire'),x.get('status','pendente')]
 lines.append('| '+' | '.join(v.replace('|','/').replace('\n',' ') for v in vals)+' |')
lines+=['','## Gate e limiti','']+['- '+x for x in state['limitations']]
p=Path('wiki/reviews/correzioni-collana-2026-10-02/VOL-02.md');p.parent.mkdir(parents=True,exist_ok=True);p.write_text('\n'.join(lines)+'\n',encoding='utf8')
print(json.dumps({'findings':len(findings),'withChanges':len(state['changes'])}))
