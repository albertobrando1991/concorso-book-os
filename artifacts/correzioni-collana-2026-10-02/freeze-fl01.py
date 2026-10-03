from pathlib import Path
import json,hashlib,re
base=Path('wiki/books/moduli/m-fl01-comuni-unioni');art=Path('artifacts/correzioni-collana-2026-10-02')
matrix=base/'planning/02-matrice-copertura-didattica.md'
t=matrix.read_text(encoding='utf8')
replacements={
'books/il-metodo-bando/index#Il nucleo comune':'books/il-metodo-bando/chapters/diritto-amministrativo-per-candidati#15. Enti territoriali e autonomie locali',
'books/il-metodo-bando/index#Procedimento amministrativo':'books/il-metodo-bando/chapters/diritto-amministrativo-per-candidati#3. Procedimento amministrativo',
'books/il-metodo-bando/index#PA digitale':'books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali#10. CAD e amministrazione digitale',
"#7. Schema dal fabbisogno all'esecuzione":'#7. Schema dal fabbisogno all’esecuzione'}
for old,new in replacements.items():t=t.replace(old,new)
matrix.write_text(t,encoding='utf8')
index=base/'index.md';t=index.read_text(encoding='utf8').replace('M-FL01 - Comuni e Unioni','M-FL01 — Comuni e Unioni').replace('review_required: true','review_required: false',1)
t=re.sub(r'^updated_at:.*$', 'updated_at: 2026-10-03',t,count=1,flags=re.M)
t=t.replace('I capitoli 01-14 hanno completato la revisione individuale e trasversale. La copertura v4 è completa; restano l\'audit specialistico automatico, il text freeze, gli apparati e il preflight previsti dalla pipeline prima della conferma umana finale.','I capitoli 01–14 hanno completato il riesame correttivo e l’audit specialistico del 3 ottobre 2026. Il manifest di text freeze riporta gli hash correnti. La chiusura del modulo non certifica il restante volume né il nuovo PDF: restano gli apparati e il preflight del pacchetto complessivo prima della conferma finale.')
index.write_text(t,encoding='utf8')
chapters=sorted((base/'chapters').glob('*.md'));assert len(chapters)==14
records=[{'file':str(p).replace('\\','/'),'state':'text-freeze','date':'2026-10-03','sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in chapters]
(art/'M-FL01-freeze.json').write_text(json.dumps({'module':'M-FL01','cutoff':'2026-10-03','files':records,'pdfChecked':False},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
manifest=base/'planning/10-text-freeze-manifest.md';archive=art/'M-FL01-freeze-prima-correzioni.md'
if manifest.exists() and not archive.exists():archive.write_bytes(manifest.read_bytes())
lines=['---','id: m-fl01-text-freeze-manifest','type: text_freeze_manifest','title: "Text freeze — M-FL01 Comuni e Unioni"','status: frozen','book_id: m-fl01-comuni-unioni','module_code: M-FL01','freeze_date: 2026-10-03','updated_at: 2026-10-03','review_required: false','canonical: true','---','','# Text freeze — M-FL01 Comuni e Unioni','','Congelamento correttivo del 3 ottobre 2026. Presente l’intera sequenza dei 14 capitoli, coerente con indice e matrice. Audit specialistico step 15 superato via CLI senza blocker. Humanizer e verifica didattica ripetuti nei passaggi modificati. Gli ID V02-17/V02-20 sono chiusi solo nella parte M-FL01; le parti esterne non appartengono a questo freeze.','','Il gate automatico text-freeze non è implementato: verifica manuale dichiarata, senza presentarla come test automatico. Controllati 227 collegamenti wiki in capitoli, indice e matrice; sei anchor interni della matrice sono stati corretti. Nessuna modifica sostanziale successiva all’audit; il nuovo PDF non è ancora verificato.','','Cut-off normativo: 3 ottobre 2026. Fonti e limiti nel report `wiki/reviews/pipeline/VOL-02/15-moduli-m-fl01-comuni-unioni.md`. Hash SHA-256 dei byte dei file correnti; nessun commit creato. Lo storico precedente è conservato negli artifact.','','| File | Stato | Data | SHA-256 |','| --- | --- | --- | --- |']
for x in records:lines.append(f"| {Path(x['file']).name} | {x['state']} | {x['date']} | `{x['sha256']}` |")
lines+=['','Ogni modifica sostanziale richiede riapertura dei gate previsti dal protocollo. Il congelamento non è approvazione per pubblicazione del volume.']
manifest.write_text('\n'.join(lines)+'\n',encoding='utf8')
statepath=art/'VOL-02-changes.json';state=json.loads(statepath.read_text(encoding='utf8'))
for fid,x in state['changes'].items():
 if fid not in ('V02-17','V02-20'):x['status']='Applicato e riesaminato in M-FL01; gate 15 superato'
statepath.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'chapterCount':len(records),'manifest':str(manifest)}))
