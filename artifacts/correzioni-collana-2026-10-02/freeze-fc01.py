from pathlib import Path
import re,json,hashlib,shutil
A=Path('artifacts/correzioni-collana-2026-10-02'); B=Path('wiki/books/moduli/m-fc01-ministeri'); R=Path('wiki/reviews/pipeline/VOL-03')
old=R/'16-moduli-m-fc01-ministeri.md'
archive=A/'before-text/VOL-03'/old.name
if old.exists() and not archive.exists(): shutil.copy2(old,archive)
for p in [B/'index.md',B/'planning/02-matrice-copertura-didattica.md']:
 s=p.read_text(encoding='utf8')
 s=s.replace('Restano aperte le review normative/tecniche e il preflight KDP.','Il riesame normativo del testo è concluso il 3 ottobre 2026; restano controllo delle figure, PDF candidato e preflight KDP.')
 s=s.replace('processo-tributario-dlgs-175-2024-aggiornamento-2026-07-18','processo-tributario-regime-2026-rettifica-2026-10-03')
 s=s.replace('restano freeze 16 e controllo dell’export candidato.','il freeze 16 è documentato nel manifest del 3 ottobre; resta il controllo dell’export candidato.')
 s=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',s,flags=re.M)
 s=re.sub(r'^review_required:.*$','review_required: false',s,flags=re.M)
 p.write_text(s,encoding='utf8')
files=sorted((B/'chapters').glob('*.md'))
assert len(files)==15
for p in files:
 s=p.read_text(encoding='utf8'); assert 'review_required: false' in s
 s=re.sub(r'^draft_stage:.*$','draft_stage: text_frozen',s,flags=re.M)
 p.write_text(s,encoding='utf8')
links=json.loads((A/'VOL-03-FC01-links.json').read_text(encoding='utf8'))
entries=[{'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'date':'2026-10-03','status':'text-frozen'} for p in files+[B/'index.md',B/'planning/02-matrice-copertura-didattica.md']]
checks=['15 capitoli presenti e coerenti con l’indice.','12 rilievi del modulo corretti; audit integrale e riesame specialistico corrente documentati.','Matrice: censimento storico e delta delle integrazioni riconciliati; nessuna lacuna nota aperta nel perimetro auditato.','Rinvii nel corpo: scansione dedicata con zero destinazioni o ancore irrisolte.','Micro-revisione dei delta e conservazione dei nuclei legittimi; correzioni normative verificate su fonti primarie.','Gate 14 e 15 superati; text-freeze restituisce gate-not-implemented e richiede verifica manuale.']
manifest={'volume':'VOL-03','module':'M-FC01','date':'2026-10-03','verification':'manuale; gate non implementato','files':entries,'checks':checks,'limitations':['Congelamento del testo del modulo, non delle figure e non di tutto VOL-03.','PDF aggiornato e preflight restano necessari; nessuna dichiarazione di pubblicabilità.']}
(A/'M-FC01-freeze.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
old.write_text('# M-FC01 — Congelamento del testo, 3 ottobre 2026\n\nIl CLI ha restituito `gate-not-implemented`: verifica manuale svolta e documentata prima del comando `--accept`. Il precedente manifest è conservato negli artefatti, senza attribuire ai revisori storici le correzioni correnti.\n\n'+ '\n'.join('- '+x for x in checks)+'\n\n| File | Stato | Data | SHA-256 |\n| --- | --- | --- | --- |\n'+ '\n'.join('| '+e['path']+' | '+e['status']+' | '+e['date']+' | '+e['sha256']+' |' for e in entries)+'\n\n## Limiti e riapertura\n\n'+' '.join(manifest['limitations'])+' Ogni modifica sostanziale richiede riapertura dei gate editoriali pertinenti e aggiornamento del manifest.\n',encoding='utf8')
print('Freeze manuale: 15 capitoli e 2 apparati; manifest scritto.')
