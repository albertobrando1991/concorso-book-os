from pathlib import Path
import json,hashlib,shutil
A=Path(__file__).parent;B=Path('wiki/books/moduli/m-tr04-ambiente-protezione-civile/chapters');sha=lambda b:hashlib.sha256(b).hexdigest()
freeze=A/'M-TR04-freeze.json';f=json.loads(freeze.read_text(encoding='utf8'))
assert all(sha(Path(r['path']).read_bytes())==r['sha256'] for r in f['files'])
shutil.copy2(freeze,A/'M-TR04-freeze-before-production.json')
specs=[('10-sistema-protezione-civile-pianificazione.md','P11-01','Responsabile/funzione','Responsabile / funzione'),('11-rischi-allertamento-it-alert-emergenze.md','P11-02','- **ID:** DO-TR04-11-IT-ALERT-2026-08-17.',''),('12-clima-energia-rinnovabili-cer.md','P11-02','- **ID:** DO-TR04-12-CLIMA-2026-08-18.',''),('14-laboratorio-casi-quesiti-sintetici.md','P11-06','30.000 × 0,25 = 7,5 t/anno','30.000 kWh × 0,25 kg/kWh ÷ 1.000 = 7,5 t/anno')]
meta={11:{'id':'DO-TR04-11-IT-ALERT-2026-08-17','title':'IT-alert al 3 ottobre 2026','heading':'Dato operativo · IT-alert al 3 ottobre 2026','auditArea':'protezione civile e comunicazione del rischio','source':'Portale IT-alert e direttiva 12 febbraio 2026, G.U. n. 100 del 2 maggio 2026','version':'stato nazionale al 3 ottobre 2026','verifiedAt':'2026-10-03'},12:{'id':'DO-TR04-12-CLIMA-2026-08-18','title':'Quadro climatico UE','heading':'Dato operativo · Quadro climatico UE — aggiornamento del 3 ottobre 2026','auditArea':'clima ed energia','source':'Regolamento (UE) 2021/1119, consolidato al 7 aprile 2026, e regolamento (UE) 2026/667','version':'consolidato al 7 aprile 2026; verifica 3 ottobre 2026','verifiedAt':'2026-10-03'}}
rows=[]
for name,id,before,after in specs:
 p=B/name;old=p.read_bytes();t=old.decode('utf8');nl='\r\n' if '\r\n' in t else '\n';assert t.count(before)==1
 (A/f'VOL-11-{name[:2]}-before-production.md').write_bytes(old)
 if not after:t=t.replace(before+nl,'')
 else:t=t.replace(before,after)
 n=int(name[:2])
 if n in meta:
  assert 'dati_operativi_audit:' not in t
  marker=next(x for x in t.splitlines() if x.startswith('dati_operativi:'))
  t=t.replace(marker+nl,marker+nl+'dati_operativi_audit: '+json.dumps([meta[n]],ensure_ascii=False)+nl)
 new=t.encode('utf8');p.write_bytes(new);rows.append({'id':id,'path':p.as_posix(),'beforeSha256':sha(old),'afterSha256':sha(new),'before':before,'after':after,'auditMetadata':meta.get(n)})
(A/'VOL-11-production-delta.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
for step in ['14','15']:
 p=Path(f'wiki/reviews/pipeline/VOL-11/{step}-moduli-m-tr04-ambiente-protezione-civile.md')
 with p.open('a',encoding='utf8') as out:out.write('\n\n### Delta di produzione del 3 ottobre 2026\n\nP11-01: spaziata la barra nell’intestazione Responsabile / funzione per evitare una parola troncata. P11-02: rimossi i due ID dal corpo dei capitoli 11 e 12; mantenuti in dati_operativi e associati a fonte, versione, data e posizione in dati_operativi_audit. Fonti e affermazioni normative immutate. P11-06: corretta dimensionalmente la formula illustrativa dell’appendice B: 30.000 kWh × 0,25 kg/kWh = 7.500 kg = 7,5 t; esplicitato il divisore 1.000. Copie precedenti e delta esatto in artifacts/correzioni-collana-2026-10-02/VOL-11-production-delta.json. Nuova prova PDF da verificare.\n')
print(json.dumps({'changedFiles':len(rows),'ids':[r['id'] for r in rows]}))
