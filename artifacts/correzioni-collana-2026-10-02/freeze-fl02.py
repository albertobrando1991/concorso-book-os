from pathlib import Path
import json,re,hashlib
mod=Path('wiki/books/moduli/m-fl02-regioni-province-citta-metropolitane');art=Path('artifacts/correzioni-collana-2026-10-02')
p=mod/'planning/02-matrice-copertura-didattica.md';t=p.read_text(encoding='utf-8')
archive=art/'M-FL02-matrice-prima-allineamento-nuclei.md'
if not archive.exists():
 archive.write_bytes(p.read_bytes())
 maps={'05':{3:2,4:3,5:4,6:5,7:6},'06':{3:2,4:3,6:4,7:5},'07':{3:2,5:3,6:4,7:5},'08':{3:2,5:3,6:4,7:5}}
 t=re.sub(r'N-FL02-(05|06|07|08)-(\d{2})',lambda m:f'N-FL02-{m[1]}-{maps[m[1]].get(int(m[2]),int(m[2])):02d}',t)
 t+='\n## Allineamento riferimenti al freeze del 3 ottobre 2026\n\nRiconciliati gli ID dei nuclei dei capitoli 05–08 con le intestazioni correnti. Le righe storiche di delta conservano gli stati prima/dopo; le parole «parziale» in tali righe non descrivono lo stato corrente. Il contenuto assegnato non cambia.\n'
 p.write_text(t,encoding='utf-8')
chapters=sorted((mod/'chapters').glob('*.md'));assert len(chapters)==12
missing=[]
for c in chapters:
 assigned=set(re.findall('N-FL02-'+c.name[:2]+r'-\d+',t))
 existing=set(re.findall(r'N-FL02-\d+-\d+',c.read_text(encoding='utf-8')))
 missing.extend(sorted(assigned-existing))
assert not missing,missing
p=mod/'index.md';t=p.read_text(encoding='utf-8').replace('M-FL02 - Regioni','M-FL02 — Regioni');t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,count=1,flags=re.M)
t=t[:t.index('## Note di review')]+'''## Note di review

I dodici capitoli hanno completato le correzioni e l’audit specialistico del 3 ottobre 2026. Il modulo mantiene il perimetro regionale e di area vasta; esempi e atti fittizi dichiarano i propri presupposti. Il manifest conserva gli hash del testo congelato. Per una Regione specifica, statuto, regolamenti, organizzazione e disciplina della singola misura restano dati da ricavare dal bando e dalle sue fonti: il modulo non attribuisce un regolamento locale a tutte le Regioni. Il nuovo PDF e la pubblicabilità complessiva del VOL-02 richiedono i successivi gate di produzione.
'''
p.write_text(t,encoding='utf-8')
records=[{'file':str(p).replace('\\','/'),'state':'text-freeze','date':'2026-10-03','sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in chapters]
(art/'M-FL02-freeze.json').write_text(json.dumps({'module':'M-FL02','cutoff':'2026-10-03','files':records,'pdfChecked':False},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manifest=mod/'planning/10-text-freeze-manifest.md';archive=art/'M-FL02-freeze-prima-correzioni.md'
if manifest.exists() and not archive.exists():archive.write_bytes(manifest.read_bytes())
lines=['---','id: m-fl02-text-freeze-manifest','type: text_freeze_manifest','title: "Text freeze — M-FL02"','status: frozen','module_code: M-FL02','freeze_date: 2026-10-03','updated_at: 2026-10-03','review_required: false','canonical: true','---','','# Text freeze — M-FL02','','Dodici capitoli presenti, indice coerente e matrice riconciliata con gli ID correnti dei nuclei. Gate 14 e 15 superati senza blocchi. Verifica manuale del freeze: il gate automatico non è implementato, non viene dichiarato test automatico. Gli 80 wikilink sono stati verificati; i riferimenti testuali dei nuclei sono stati riconciliati. Humanizer e microrevisione dei passaggi integrati completati. Cut-off normativo 3 ottobre 2026; fonti, casi e limiti nel report pipeline 15.','','La parte regionale di V02-20 è chiusa; simulazione finale e altri laboratori restano fuori dal presente perimetro. Il PDF precedente non rappresenta i testi corretti. Il pacchetto complessivo non è dichiarato pubblicabile.','','| File | Stato | Data | SHA-256 |','| --- | --- | --- | --- |']
for x in records:lines.append(f"| {Path(x['file']).name} | {x['state']} | {x['date']} | `{x['sha256']}` |")
lines+=['','Ogni modifica sostanziale richiede riapertura dei gate previsti dal protocollo. Nessun commit creato.']
manifest.write_text('\n'.join(lines)+'\n',encoding='utf-8')
statepath=art/'VOL-02-changes.json';state=json.loads(statepath.read_text(encoding='utf-8'))
for fid,x in state['changes'].items():
 if fid in [f'V02-{i:02d}' for i in range(21,35)]:x['status']='Applicato e riesaminato in M-FL02; gate 15 superato'
statepath.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'chapters':len(records),'missingNuclei':missing,'manifest':str(manifest)}))
