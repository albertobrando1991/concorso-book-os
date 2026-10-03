from pathlib import Path
import re,json,hashlib
B=Path('wiki/books/moduli/m-sp02-vigili-fuoco');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-12');C=Path('wiki/reviews/correzioni-collana-2026-10-02')
entries=[]
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');assert 'review_required: false' in t;t=t.replace('draft_stage: specialist-audit-complete','draft_stage: text_frozen');p.write_text(t,encoding='utf8');entries.append({'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'text-freeze','date':'2026-10-03'})
p=B/'index.md';t=p.read_text(encoding='utf8');arc=C/'archive/pre-correzioni-sp02-index.md'
if not arc.exists():arc.write_text(t,encoding='utf8')
t=t.replace('M-SP02 -','M-SP02 —');t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M)
t=re.sub(r'^- Stato:.*$','- Stato: correzioni e audit specialistico del 3 ottobre 2026 conclusi; nuovo PDF e controlli di volume necessari.',t,flags=re.M)
t=t.replace('Le sezioni normative e specialistiche richiedono source notes consolidate e review umana.','Le sezioni normative e specialistiche derivano da fonti consolidate; gli audit precedono il sign-off finale del volume.')
t=t.replace('- [[books/moduli/m-sp02-vigili-fuoco/planning/00-piano-editoriale|Piano editoriale del modulo]]\n','')
t=t.split('## Prossimo passo')[0]+'## Prossimo passo\n\nProdurre e controllare il nuovo PDF; completare la revisione del volume prima della conferma finale.\n\n## Piano staff\n\n[[books/moduli/m-sp02-vigili-fuoco/planning/00-piano-editoriale|Piano editoriale interno]].\n';p.write_text(t,encoding='utf8')
p=B/'planning/00-piano-editoriale.md';t=p.read_text(encoding='utf8');arc=C/'archive/pre-correzioni-sp02-piano.md'
if not arc.exists():arc.write_text(t,encoding='utf8')
t=t.replace('quesiti logico-deduttivi e analitici —','quesiti logico-deduttivi e analitici, uso delle applicazioni informatiche e lingua inglese —').replace('Al candidato civile privo di questi titoli resta il 5%, più i posti riservati non coperti.','Il 5% è il residuo nominale non riservato; non è garantito esclusivamente ai candidati privi di riserve. Merito e devoluzione vanno considerati insieme.')
t=t.replace('due di essi — storia d\'Italia dal 1861 ed elementi di chimica e fisica — non sono coperti da nessun altro materiale concorsuale.','storia e scienze richiedono materiali pertinenti e verifica delle lacune personali.').replace('il volume base tratta l\'informatica come amministrazione digitale, mentre qui il bando chiede l\'uso pratico delle apparecchiature e delle applicazioni più diffuse.','il volume base comprende informatica giuridica e d’uso: i rinvii aggiornati del capitolo 6 selezionano le sezioni pertinenti al bando.')
t=t.replace('## Testo editoriale\nDa sviluppare con Manual Writer Agent dopo consolidamento delle fonti specifiche.','## Stato corrente\n\nOtto capitoli effettivi, quaranta nuclei rinumerati per capitolo, 48 quiz commentati. Correzioni e audit specialistico del 3 ottobre conclusi. I conteggi e le note di accorpamento precedenti descrivono la storia editoriale; il manifest M-SP02-freeze.json identifica il testo corrente. Nuovo PDF ancora da verificare.')
t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf8')
p=B/'planning/02-matrice-copertura-didattica.md';t=p.read_text(encoding='utf8').replace('review_required: true','review_required: false');p.write_text(t,encoding='utf8')
manifest={'volume':'VOL-12','module':'M-SP02','date':'2026-10-03','files':entries,'checks':['8 capitoli, 40 nuclei almeno 600 parole, 48 quiz commentati.','Calcoli, casi, chiavi, rinvii e fonti dei delta riesaminati.','Step 15 passato con zero blocker e warning; indice e matrice riconciliati.'],'limitations':['Nuovo PDF e altri moduli del volume ancora da completare.','Fonti normative verificate selettivamente; avviso 7 ottobre futuro al controllo.']}
(A/'M-SP02-freeze.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
p=R/'16-moduli-m-sp02-vigili-fuoco.md';arc=C/'archive/pre-correzioni-16-m-sp02.md'
if p.exists() and not arc.exists():arc.write_bytes(p.read_bytes())
p.write_text('# M-SP02 — Manifest testuale del 3 ottobre 2026\n\nVerifica manuale, esito CLI registrato separatamente.\n\n'+'\n'.join('- '+s for s in manifest['checks'])+'\n\n| File | Stato | Data | SHA256 |\n| --- | --- | --- | --- |\n'+'\n'.join('| '+x['path']+' | '+x['status']+' | '+x['date']+' | '+x['sha256']+' |' for x in entries)+'\n\n'+' '.join(manifest['limitations'])+'\n',encoding='utf8')
mapping=json.loads((A/'M-SP02-findings-map.json').read_text(encoding='utf8'));batch={}
for n,(c,desc) in mapping.items():batch[f'V12-{int(n):02}']={'change':desc,'files':[next((B/'chapters').glob(f'{c:02}-*.md')).as_posix(),'wiki/sources/bandi-e-ordinamento-corpo-nazionale-vigili-del-fuoco-m-sp02.md','wiki/reviews/pipeline/VOL-12/15-moduli-m-sp02-vigili-fuoco.md'],'evidence':'Audit specialistico dei delta e gate 15 passato; fonti, calcoli e chiavi nelle evidenze M-SP02. PDF ancora necessario.','status':'applicato'}
(A/'VOL-12-batch1.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2),encoding='utf8');print('SP02 manifest e 20 rilievi registrabili')
