from pathlib import Path
import re,json,hashlib,shutil
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-tr01-ict-trasformazione-digitale');R=Path('wiki/reviews/pipeline/VOL-08')
files=sorted((B/'chapters').glob('*.md'));assert len(files)==13
for p in files:
 s=p.read_text(encoding='utf8');assert 'review_required: false' in s;s=re.sub(r'^draft_stage:.*$','draft_stage: text_frozen',s,flags=re.M);p.write_text(s,encoding='utf8')
p=B/'index.md';s=p.read_text(encoding='utf8').replace('revision-in-progress','text_frozen');s=re.sub(r'I tredici capitoli sono in revisione.*?(?=\n\n)','I tredici capitoli sono verificati e congelati al 3 ottobre 2026 dopo le correzioni dei 32 rilievi dell’audit integrale. I gate 14 e 15 sono superati e il freeze 16 è documentato con hash e controllo manuale previsto dal CLI. Restano da verificare figure, PDF aggiornato e gate finali di produzione: questo stato non è una dichiarazione di pubblicabilità.',s);p.write_text(s,encoding='utf8')
files+=[B/'index.md',B/'planning/02-matrice-copertura-didattica.md',B/'planning/10-manifest-nuclei-format-2.json']+sorted((B/'planning/verifiche').glob('*.md'))
checks=['13 capitoli presenti, 32 rilievi applicati e riesaminati.','82 nuclei coerenti tra manifest, capitoli, matrice e indice; evidenze staff fuori dal libro.','13 gate di densità e copertura passati senza warning; zero rinvii del corpo irrisolti.','47 test del controllo Format 2 e typecheck passati.','Fonti e casi pertinenti verificati al 3 ottobre 2026; soluzioni originali ricalcolate.','Gate 14 e 15 passati; gate text-freeze non implementato: verifica manuale documentata.']
manifest={'volume':'VOL-08','module':'M-TR01','date':'2026-10-03','verification':'manuale; gate-not-implemented','checks':checks,'files':[{'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'text-frozen'} for p in files],'limitations':['Figure e PDF candidato non congelati né approvati da questa attestazione.','Il precedente PDF visuale non rappresenta le integrazioni correnti; procedere ai controlli di produzione.']}
(A/'M-TR01-freeze.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
p=R/'16-moduli-m-tr01-ict-trasformazione-digitale.md'
if p.exists() and not (A/'before-text/VOL-08'/p.name).exists():shutil.copy2(p,A/'before-text/VOL-08'/p.name)
p.write_text('# M-TR01 — Congelamento del testo, 3 ottobre 2026\n\nIl CLI ha restituito `gate-not-implemented`; eseguita la verifica manuale prevista prima dell’accettazione motivata.\n\n'+'\n'.join('- '+x for x in checks)+'\n\n| File | Stato | SHA-256 |\n| --- | --- | --- |\n'+''.join('| '+x['path']+' | '+x['status']+' | '+x['sha256']+' |\n' for x in manifest['files'])+'\n## Limiti\n\n'+' '.join(manifest['limitations'])+' Ogni modifica sostanziale riapre il passaggio pertinente e richiede un nuovo manifest.\n',encoding='utf8')
lp=A/'VOL-08-ledger.json';d=json.loads(lp.read_text(encoding='utf8'))
for row in d['files']:row['sha256']=hashlib.sha256(Path(row['path']).read_bytes()).hexdigest()
for row in d['findings']:row['status']='Testo verificato e congelato; PDF da verificare'
d['freezeManifest']=(A/'M-TR01-freeze.json').as_posix();lp.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
p=Path('wiki/reviews/correzioni-collana-2026-10-02/VOL-08.md');s=p.read_text(encoding='utf8').replace('Applicato; riesame specialistico corrente','Testo verificato e congelato; PDF da verificare').replace('Audit specialistico e freeze tramite CLI;', 'Audit specialistico 15 concluso e freeze 16 manuale con hash documentato;').replace('Le correzioni note sono applicate e controllate nel testo.', 'Le 32 correzioni sono applicate, riesaminate e congelate nel testo; `textVerified: true`, `finalVerified: false`.');p.write_text(s,encoding='utf8')
print('Freeze manuale: 13 capitoli, indice, matrice, manifest e 13 mapping staff.')
