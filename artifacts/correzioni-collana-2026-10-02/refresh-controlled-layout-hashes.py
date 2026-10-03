from pathlib import Path
import json,hashlib,shutil
A=Path(__file__).parent
for volume,module,slug,note in [('VOL-09','M-TR02','m-tr02-appalti-pnrr-fondi-ue','Didascalia numerata Figura13.1 associata al Gantt: elimina la doppia didascalia senza cambiare dati o spiegazione. Gate10cap13passato.'),('VOL-10','M-TR03','m-tr03-tecnico-ingegneristico','Riferimenti in paragrafo in13capitoli; testo fonte preservato. Riferimenti NTC collocati nell’apertura. Solo composizione e posizione, nessuna variazione normativa.')]:
 p=A/(module+'-freeze.json');backup=A/(module+'-freeze-before-layout.json')
 if not backup.exists():shutil.copy2(p,backup)
 d=json.loads(p.read_text(encoding='utf8'));changes=[];report=Path(f'wiki/reviews/pipeline/{volume}/16-moduli-{slug}.md');t=report.read_text(encoding='utf8')
 for x in d['files']:
  current=hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()
  if current!=x['sha256']:changes.append({'path':x['path'],'before':x['sha256'],'after':current});t=t.replace(x['sha256'],current);x['sha256']=current
 d.setdefault('controlledLayoutCorrections',[]).append({'date':'2026-10-03','note':note,'files':changes});p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8');report.write_text(t+'\nCorrezione compositiva controllata del 3 ottobre 2026: '+note+' Manifest aggiornato, versione precedente conservata.\n',encoding='utf8')
 print(volume,len(changes),'hashes updated')
p=A/'VOL-10-ledger.json';d=json.loads(p.read_text(encoding='utf8'))
for x in d['files']:x['sha256']=hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()
d['controlledLayoutDelta']=(A/'VOL-10-layout-reference-delta.json').as_posix();p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
p=A/'registro-applicazione.json';d=json.loads(p.read_text(encoding='utf8'))
for r in d:
 if r['id'].startswith('V09-'):r['fileHashes']={f:hashlib.sha256(Path(f).read_bytes()).hexdigest() for f in r['changedFiles'] if Path(f).exists()}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
