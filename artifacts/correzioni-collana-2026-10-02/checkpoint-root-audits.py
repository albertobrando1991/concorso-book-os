from pathlib import Path
import json,hashlib
A=Path(__file__).parent;R=Path('wiki/reviews/correzioni-collana-2026-10-02')
p=Path('wiki/books/moduli/m-tr03-tecnico-ingegneristico/chapters/04-ntc-sismica-geotecnica-sicurezza-strutturale.md')
t=p.read_text(encoding='utf8');old='Il quadro è stato ricontrollato sulle fonti ufficiali il 21 agosto 2026';new='Il quadro è stato ricontrollato sulle fonti ufficiali il 3 ottobre 2026';assert old in t
before=hashlib.sha256(p.read_bytes()).hexdigest();p.write_text(t.replace(old,new),encoding='utf8');after=hashlib.sha256(p.read_bytes()).hexdigest()
note='Data del riscontro NTC allineata al3ottobre2026, confermata dal revisore dei capitoli2e8NTC. Nessuna modifica della disciplina. Il PDF125p precede questa sola rettifica e sarà rigenerato nel pacchetto finale.'
q=A/'M-TR03-freeze.json';d=json.loads(q.read_text(encoding='utf8'))
for f in d['files']:
 if Path(f['path'])==p:assert f['sha256']==before;f['sha256']=after
d.setdefault('controlledTextCorrections',[]).append({'date':'2026-10-03','note':note,'path':p.as_posix(),'before':before,'after':after});q.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
q=Path('wiki/reviews/pipeline/VOL-10/16-moduli-m-tr03-tecnico-ingegneristico.md');q.write_text(q.read_text(encoding='utf8').replace(before,after)+'\n'+note+'\n',encoding='utf8')
q=A/'VOL-10-ledger.json';d=json.loads(q.read_text(encoding='utf8'))
for f in d['files']:
 if Path(f['path'])==p:f['sha256']=after
q.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
q=R/'PDF-VOL-10.md';q.write_text(q.read_text(encoding='utf8')+'\nUlteriore verifica: pagina78 della prova125p esaminata; tabella leggibile e prosecuzione coerente. '+note+'\n',encoding='utf8')
q=R/'EXPORT-COLLANA.md'
with q.open('a',encoding='utf8') as f:f.write('''

## Aggiornamento prove e approvazioni — 3 ottobre 2026

VOL-01: nuova prova di666pagine, indice minimo9,5pt, zero br letterali, immagini mancanti e overflow DOM; controllo visivo in corso. VOL-09: prova corrente265pagine, Gantt a pagina238 visto a dimensione piena, con unica didascalia e calcoli leggibili. VOL-10: prova125pagine, esaminata anche pagina78 della tabella DL; successiva rettifica della sola data NTC richiede rigenerazione finale.

La riapertura a cascata della pipeline ora invalida anche lo step24, senza concedere una nuova approvazione:38test di stato e CLI superati, typecheck superato. Le vecchie conferme di VOL-02 e VOL-08 sono state invalidate tramite reopen23--cascade; per VOL-09 sync ha aggiunto lo step24 che mancava. Nessun run-state modificato a mano e nessun signoff simulato.
''')
q=R/'README.md';t=q.read_text(encoding='utf8').replace('VOL-02/04/05; VOL-06/07/12; VOL-03/08/10/11; coordinatore per VOL-01/09','VOL-02; VOL-06/07/12; VOL-03/08/10/11/05; coordinatore per VOL-01/04/09');q.write_text(t,encoding='utf8')
with Path('wiki/log.md').open('a',encoding='utf8') as f:f.write('\n\n## 2026-10-03 — Testi base e affidabilità del signoff\n\nVOL-01:49rilievi dei capitoli verificati,32unità congelate con41hash; due preliminari ancora aperti. Step14passato conwarning dichiarati,15passato,16manuale,17filosofia aggiornata,18in corso. Nuova prova666p. Corretto cascadeCLI per invalidare24 dopo modifiche;38test e typecheck passati. Riassegnati VOL04al coordinatore eVOL05al revisore03dopo11. Nessuna pubblicazione finale.\n')
print('Checkpoint scritto; data NTC aggiornata e freeze allineato.')
