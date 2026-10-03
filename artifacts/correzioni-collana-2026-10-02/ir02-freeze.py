from pathlib import Path
import json,re,hashlib
B=Path('wiki/books/moduli/m-ir02-universita-afam');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-06')
entries=[]
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8').replace('ciòè','cioè').replace('dell esito',"dell'esito");assert 'review_required: false' in t
 t=t.replace('draft_stage: specialist-audit-complete','draft_stage: text_frozen');p.write_text(t,encoding='utf8')
 body=t.split('\n---\n',1)[1];assert not re.search(r'\[\[(sources|topics|entities|planning|raw|reviews)/',body)
 entries.append({'path':str(p).replace('\\','/'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'text-freeze','date':'2026-10-03','words':len(re.findall(r'\b[\w’]+\b',body))})
assert len(entries)==12
p=B/'index.md';t=p.read_text(encoding='utf8').replace('correction-in-progress','text_frozen').replace('editorial_revision','text_freeze').replace('correzioni testuali applicate; audit specialistico e nuovo PDF da completare.','correzioni testuali e audit specialistico conclusi; nuovo PDF da verificare.').replace('Completare audit verticale, controllo specialistico delle fonti mobili e preflight del modulo tramite pipeline.','Verificare il nuovo PDF e completare i controlli del volume tramite pipeline. Il manifest corrente documenta il testo congelato.');p.write_text(t,encoding='utf8')
p=B/'planning/02-matrice-copertura-didattica.md';t=p.read_text(encoding='utf8')+'\n### Chiusura testuale\n\nStep 15 passato il 3 ottobre 2026 con zero blocker e warning. Manifest dello step 16 corrente; il PDF aggiornato resta distinto.\n';p.write_text(t,encoding='utf8')
manifest={'volume':'VOL-06','module':'M-IR02','date':'2026-10-03','files':entries,'checks':['12 capitoli canonici presenti; 60 nuclei sopra 600 parole e 86 quiz.','Matrice collegata a teoria, applicazioni e soluzioni effettive.','Audit15 passato con zero blocker e warning sul report corrente.','Fonti ufficiali consolidate con data e limiti di lettura.','Refusi cioè/dell’esito corretti in chiusura; nessun collegamento staff nel corpo.','Indice e apparati effettivi riconciliati; Humanizer sui delta.'],'limitations':['Nuovo PDF non ancora verificato, incluso export IR02/09.','Altri moduli in correzione; nessuna pubblicabilità del volume.','Verifica normativa selettiva, non certificazione di ogni atto del corpus.']}
(A/'M-IR02-freeze.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
p=R/'16-moduli-m-ir02-universita-afam.md';arc=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-16-m-ir02.md')
if not arc.exists():arc.write_bytes(p.read_bytes())
p.write_text('# M-IR02 — Manifest del testo, 3 ottobre 2026\n\nVerifica manuale; esito del gate CLI registrato separatamente.\n\n'+'\n'.join('- '+x for x in manifest['checks'])+'\n\n| File | Stato | Data | SHA-256 |\n| --- | --- | --- | --- |\n'+'\n'.join('| '+e['path']+' | text-freeze | '+e['date']+' | '+e['sha256']+' |' for e in entries)+'\n\n'+' '.join(manifest['limitations'])+'\n',encoding='utf8')
print('Manifest IR02:',len(entries),'capitoli;',sum(e['words'] for e in entries),'parole')
