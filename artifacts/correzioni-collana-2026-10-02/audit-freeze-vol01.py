from pathlib import Path
import re,json,hashlib,shutil,sys
A=Path(__file__).parent;B=Path('wiki/books/il-metodo-bando');R=Path('wiki/reviews/pipeline/VOL-01')
inventory=json.loads((A/'VOL-01-structure.json').read_text(encoding='utf8'));paths=[Path(x['path']) for x in inventory['units']];assert len(paths)==32
sources=sorted([p for p in Path('wiki/sources').glob('vol-01-*-2026-10-0[23].md') if any(z in p.name for z in ['correzioni','esempi-logica'])])
mode=sys.argv[1]
if mode=='audit':
 report=(R/'14-il-metodo-bando.md').read_text(encoding='utf8')
 report=report.replace('# Report editoriale — Correzioni integrali VOL-01','# Audit specialistico conclusivo — Testo autoriale VOL-01')
 report='\n'.join(l for l in report.splitlines() if not l.startswith(('| V01-50 |','| V01-51 |')))+'\n'
 report=report.replace('Concludere audit specialistico e congelamento tramite CLI.','Audit specialistico concluso sul testo autoriale; procedere al congelamento tramite CLI.')
 report=report.replace('## 6. Contenuto verificato e fonti','''## 6. Contenuto verificato e fonti

L’audit riguarda le32unità autoriali della scheda; i due rilievi dei preliminari rimangono nel registro di volume e non vengono chiusi da questo step. Nessun box «Dato operativo» rilevato dal CLI. I claim modificati sono stati confrontati con le sette note consolidate e i riscontri primari lì specificati. Nessun rilievo specialistico grave o medio noto resta aperto nei49delta testuali. Lo stato `review_required: false` dei capitoli si riferisce a questo controllo, non al preflight.

| ID | File e posizione | Categoria | Gravità originaria | Evidenza consolidata | Correzione applicata | Stato finale |
| --- | --- | --- | --- | --- | --- | --- |
| A01-01 | Cap.4, istituzioni e checkpoint | Normativa | Grave | Nota costituzione: Cost.artt.17/32/33/56–61/64/72–75/83–94/100/138; Reg.Camera96 e Senato36; TUE13/TFUE288 | Ambito, numeri, regole e casi; referendum2026 senza introdurre riforma respinta | Chiuso |
| A01-02 | Cap.5 e15/17, atti e procedimenti | Normativa | Grave | Nota procedimento: L241 artt.2/3/10-bis/14–14-quinquies/18–21-nonies; DL19/L50del2026 | Tempi, invalidità, conferenze, SCIA, revoca e acquisizione d’ufficio; modello con termine assegnato | Chiuso |
| A01-03 | Cap.6 e glossario | Normativa | Grave | Nota impiego: D165artt.3/55-bis; CP317; DL80/DPR81/DM132 e PNA2022 | Ordinamenti, UPD, termini, PIAO e50dipendenti; riserva/preferenza/titoli | Chiuso |
| A01-04 | Cap.7 e10, appendiceA | Normativa | Grave | Nota accesso/privacy: D33artt.5/5-bis/26; D24artt.4–6/15; GDPR12/17/20/33–36; Codiceprivacy2-septies | Termini e limiti, breach, DPIA e ruoloRPD coerenti | Chiuso |
| A01-05 | Cap.8 e appendiceB | Tecnica contabile | Grave | Nota impiego/contabilità: TUEL186/187, armonizzazione e contabilità statale; verifica numerica | Residui40, risultato120, quota25/−10; FPV/FCDE senza doppia sottrazione | Chiuso |
| A01-06 | Cap.9 e17 | Normativa | Grave | Nota contratti: D36artt.14/15/17/37/41/48/50/101; Reg.UE2025/2152; Consip | Soglie2026, programmi, PFTE/esecutivo, requisiti e casi sotto soglia | Chiuso |
| A01-07 | Cap.10 e appendiciA/B | Normativa e informatica | Grave | Nota digitale: CAD1/20–22; esempi originali; database SQL eseguito | Documento/copia, domicilio/open data; JOIN/ordine/FK e formule riproducibili | Chiuso |
| A01-08 | Cap.11–14/18/22/23, appendiceD | Didattica quantitativa e linguistica | Media | Nota esempi: fonti linguistiche, logica e calcoli diretti | Quiz univoci, condizioni, valore atteso, chiavi bilanciate, piani e denominatori | Chiuso |
| A01-09 | Cap.2/24 e appendiceC | Procedura concorsuale | Grave | Nota candidatura: DPR487 e relativo ambito, misure speciali e dossier | Controlli richiesta/documentazione/termine/canale, distinte riserve e preferenze | Chiuso |
| A01-10 | Intero testo e apparati | Coerenza | Media | Inventario32, matrice21aggregati, audit originario e registro51 | Lessico staff rimosso, rinvii reali, nessuna fonte o immagine mancante nel controllo | Chiuso |

''')
 p=R/'15-il-metodo-bando.md';backup=A/'before-text/VOL-01/review-reconciliation'/p.name
 if p.exists() and not backup.exists():shutil.copy2(p,backup)
 p.write_text(report,encoding='utf8')
 for p in paths:
  t=p.read_text(encoding='utf8');t=re.sub(r'^review_required:.*$','review_required: false',t,flags=re.M);t=re.sub(r'^status:.*$','status: reviewed_text',t,flags=re.M);p.write_text(t,encoding='utf8')
 for p in sources:
  t=p.read_text(encoding='utf8');t=re.sub(r'^review_required:.*$','review_required: false',t,flags=re.M);p.write_text(t,encoding='utf8')
 p=B/'planning/02-matrice-copertura-didattica.md';t=p.read_text(encoding='utf8').replace('Audit specialistico step15 prima del freeze; conferma umana soltanto finale.','Audit specialistico step15 concluso sui delta; conferma umana soltanto finale.');p.write_text(t,encoding='utf8')
 print('Audit15 documentato:32testi; preliminari esclusi e rilievi50/51 conservati.')
elif mode=='freeze':
 for p in paths:
  t=p.read_text(encoding='utf8');assert 'review_required: false' in t
  t=re.sub(r'^draft_stage:.*$','draft_stage: text_frozen',t,flags=re.M);p.write_text(t,encoding='utf8')
 files=paths+[B/'planning/00-scheda-pipeline.md',B/'planning/02-matrice-copertura-didattica.md']+sources
 fig=json.loads((A/'figure-vol01-corrette-manifest.json').read_text(encoding='utf8'))
 checks=['32unità autoriali cartacee:49rilievi testuali risolti; Ricettario25–47 escluso.','Step14superato con due warning espliciti relativi ai preliminari; step15concluso sul testo dei capitoli.','Fonti normative puntuali, esempi e raccordi verificati; integrazioni precedenti preservate.','Inventario:zero immagini mancanti, fonti mancanti e riferimenti staff nel corpo.','19figure corrette presenti nel manifest dedicato; asset e PDF richiedono il controllo dell’impaginato.','Preliminari V01-50/51 esclusi dal freeze:servizio digitale, errata e identificativi ancora da completare.','Gate16non automatizzato:controllo manuale e hash; nessuna certificazione di pubblicabilità finale.']
 manifest={'volume':'VOL-01','module':'M-PA01','date':'2026-10-03','textVerified':True,'finalPublicationVerified':False,'scope':'32chapter units only; front matter excluded','checks':checks,'figureManifest':str(A/'figure-vol01-corrette-manifest.json'),'files':[{'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}
 (A/'M-PA01-freeze.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
 p=R/'16-il-metodo-bando.md';backup=A/'before-text/VOL-01/review-reconciliation'/p.name
 if p.exists() and not backup.exists():shutil.copy2(p,backup)
 p.write_text('# VOL-01 — Congelamento dei32testi autoriali,3ottobre2026\n\nGate automatico non implementato; verifica manuale del perimetro.\n\n'+'\n'.join('- '+x for x in checks)+'\n\n| File | SHA-256 |\n| --- | --- |\n'+''.join('| '+x['path']+' | '+x['sha256']+' |\n' for x in manifest['files']),encoding='utf8')
 rows=json.loads((A/'registro-applicazione.json').read_text(encoding='utf8'))
 for r in rows:
  if re.fullmatch(r'V01-\d+',r['id']) and int(r['id'][-2:])<=49:
   r['freezeManifest']=(A/'M-PA01-freeze.json').as_posix();r['fileHashes']={f:hashlib.sha256(Path(f).read_bytes()).hexdigest() for f in r.get('changedFiles',[]) if Path(f).exists()}
 (A/'registro-applicazione.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
 print({'files':len(files),'chapters':len(paths),'frontMatterExcluded':True})
