from pathlib import Path
import json,re,shutil
A=Path(__file__).parent;R=Path('wiki/reviews/correzioni-collana-2026-10-02')
cfg={
'06':('vol-06-release-20261003',617,50,36,'IR01: schede a due colonne e campi reali. IR02: i nuclei del capitolo biblioteche sono presenti (da pagina 212), bibliografia normale a 227; IR03: titoli leggibili e rinvii descrittivi. IR04: mappa MiC all’inizio del modulo, pagina 430; ordine numerico dei 13 capitoli e titoli senza numero locale duplicato.'),
'07':('vol-07-release-20261003',456,32,41,'SA01: matrici contabili e casi riorganizzati; SA02: NEWS2 alle pagine 201–202 e triage a 204 in tabelle native; SA03: rimozione delle istruzioni interne. SA04: serie QC a 404, movimento a 423, rumore/contrasto a 424; tutti e tre gli apparati letti a piena risoluzione nel contesto.'),
'12':('vol-12-final-20261003',492,194,66,'SP01: scheda personale su tre tabelle native a pagine 127–129, tutti i 16 campi conservati; piano con spazi corretti a 142. SP02: tabelle delle prove e soglie conservate. SP03: numerazione univoca e quiz con opzioni distinte. SP04: punteggio prefettizio a 416, laboratorio inglese a 449–450, settimane da 12 e 20 ore a 474–475 leggibili.')}
findings={
'06':[
('P06-01','Schede IR01, dettagli 20–67','Workbook','grave','Griglie strette dell’audit storico sostituite con campi a due colonne; nessuna parola spezzata in lettere isolate nei dettagli.','Correzione applicata e resa controllata.','verificato'),
('P06-02','IR02/09–10; dettaglio 227','Gerarchia','media','Bibliografie ora separate dal titolo e rese come corpo.','Separazione heading/lista applicata.','verificato'),
('P06-03','IR04, capitoli 38–50 da p. 430','Ordine','grave','Ordine canonico ripristinato; MiC precede gli approfondimenti.','Titoli e rinvii uniformati.','verificato'),
('P06-04','Indice e IR03/04','Titoli','media','Titolo editoriale sostituisce il nome file spurio.','Metadati corretti e indice verificato sul PDF.','verificato'),
('EXP-01','IR02/09, p. 212 e seguenti','Export','grave','I cinque nuclei prima esclusi sono presenti nella proiezione corretta.','Correzione comune del renderer; evidenza nel PDF.','verificato')],
'07':[
('P07-01','pp. 201–202','Tabella clinica','grave','Parametri NEWS2 resi in celle reali; scala 2 e limiti leggibili.','Tabella nativa con fonte e ambito; dettagli riletti.','verificato'),
('P07-02','SA01/04 e SA02/02, pp. 103–108 e 167–168','Workbook','grave','Matrici da otto/sei colonne ridotte e articolate in tabelle distinte.','Tipografia conservata, campi e intestazioni leggibili.','verificato'),
('P07-03','Aperture dei capitoli','Gerarchia','media','Titolo principale non duplicato sotto BANDO.','Proiezione dei titoli corretta.','verificato'),
('P07-04','Indice pp. 6–7','Leggibilità','media','Voci interne a 9,5 pt nominali; 32 destinazioni controllate.','Indice distribuito e verificato.','verificato'),
('P07-05','pp. 201–204, conclusione volume','Residui interni','grave','Nessun ID DO, Humanizer, gate o step nel corpo esportato.','Audit nel frontmatter, fonti e limiti nel corpo.','verificato'),
('V07-35/V07-39','pp. 404, 423–424','Apparati','grave','Tre figure originali inserite e controllate in dettaglio con didascalie, domande e soluzioni.','Grafici didattici presenti, leggibili e coerenti con i dati.','verificato')],
'12':[
('P12-01','Indice pp. 6–11','Leggibilità','media','Indice a 9,5 pt nominali; 194 voci con destinazioni fisiche corrette.','Aumentato spazio e corpo delle voci.','verificato'),
('P12-02','Intero PDF','Markup','grave','Nessun tag br stampato: controllo testuale totale e panoramica delle pagine.','Gestione dei ritorni di cella corretta.','verificato'),
('P12-03','pp. 127–129','Workbook','grave','Scheda per un concorso con 16 campi vuoti, suddivisa in tre tabelle.','Griglia precedente sostituita senza perdere i campi.','verificato'),
('P12-04','Schede SP01 e SP03','Compilabilità','media','Campi vuoti ampliati e leggibili sul PDF; non eseguita compilazione fisica a penna.','Miglioramento applicato; prova d’uso cartacea da includere nella prova fisica.','parzialmente verificato'),
('P12-05','Indice e numerazione del corpo','Navigazione','media','Nuclei rinumerati senza duplicazioni; rinvii interni descrittivi.','Indice rigenerato e verificato.','verificato'),
('P12-06','Aperture dei capitoli','Gerarchia','lieve','Titolo principale unico.','Eliminata duplicazione nella proiezione.','verificato'),
('P12-07','p. 129','Spazio bianco','lieve','La pagina contiene ancora l’ultima riga della scheda e i riferimenti, con ampio bianco residuo.','Miglioramento facoltativo ancora valutabile senza ridurre il corpo.','pendente non bloccante'),
('P12-08','Cap. 19, pp. 300–302','Quiz','media','Alternative A–D su righe distinte e commenti separati.','Formato delle verifiche uniformato.','verificato')]}
checknames=['Indice','Struttura generale','Progressione','Titoli','Completezza per pubblicazione','Coerenza interna','Coerenza tra capitoli','Terminologia','Spiegazioni','Definizioni','Concetti','Normativa','Esempi','Apparati','Fonti','Sintassi','Chiarezza','Tono','Didattica','Ripetizioni','Contraddizioni','Grammatica','Ortografia','Punteggiatura','Refusi','Coerenza grafica','Paginazione','Layout','Leggibilità','Qualità complessiva']
for v,(label,pages,entries,nfind,moduletext) in cfg.items():
 ledger=json.loads((A/f'VOL-{v}-production-visual-checkpoint.json').read_text(encoding='utf8'))
 rows=findings[v]+[(f'FM{v}-01','p. 1','Promessa editoriale','grave','La proiezione generata afferma che sono inclusi servizi digitali non verificati per questa edizione.','Confermare condizioni e accesso reali oppure proiettare un testo autonomo senza promessa.','pendente'),(f'FM{v}-02','p. 3','Dati editoriali','media','Pagina editoriale generica; dati definitivi di edizione e titolarità non attestati in questa revisione.','Completare i dati effettivi prima della pubblicazione.','pendente')]
 checklist=[]
 for i,name in enumerate(checknames,1):
  state='Riesame testuale e audit specialistico precedenti; limiti delle fonti nel registro delle correzioni'
  if i in [1,4,14,26,27,28,29]:state='Verificato nella proiezione, con metodo e copertura indicati sotto'
  if i in [5,30]:state='Non concluso per le dipendenze editoriali FM indicate'
  if i==12:state='Verifica normativa selettiva documentata; nessuna certificazione generale'
  checklist.append(f'| {i} | {name} | {state} |')
 text=f'''# VOL-{v} — Verifica della prova di produzione, 3 ottobre 2026

## 1. Sintesi editoriale

La prova `{label}-proof.pdf` contiene {pages} pagine. Gli interventi testuali sono documentati nel [registro delle correzioni](VOL-{v}.md); questo rapporto chiude il controllo locale della loro proiezione e distingue le dipendenze ancora aperte. SHA-256: `{ledger['sha256']}`. Nessuna pubblicazione o conferma finale eseguita.

## 2. Checklist dei 30 controlli

La lettura integrale del manoscritto e il riesame dei delta precedono questa prova. La presente passata approfondisce composizione, apparati, indice e leggibilità; non riattesta ogni norma né rilegge a piena risoluzione tutte le pagine.

| Punto | Controllo | Esito e perimetro |
| --- | --- | --- |
'''+ '\n'.join(checklist)+f'''

## 3. Registro dei rilievi e degli interventi

Le pagine dell’audit storico restano nelle relative relazioni immutate. Qui sono indicate le posizioni nella prova corrente.

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''+ '\n'.join('| '+' | '.join(row)+' |' for row in rows)+f'''

## 4. Osservazioni per capitolo e modulo

{moduletext}

## 5. Coerenza e verifiche tecniche

Conteggio DOM e PDF coincidenti: {pages}. Controllate {entries} voci di indice contro i titoli e le pagine effettive del PDF: nessuna divergenza. Formato 481,92 × 691,92 pt; corpo Garamond nominale 11 pt, tabelle e indice nominali 9,5 pt. Font incorporati; nessun testo fuori pagina, glifo sostitutivo, immagine mancante o overflow nei controlli locali. I rinvii di modulo ambigui sono stati sostituiti con titoli descrittivi verificabili. Non è un’attestazione di accettazione del file da parte di un servizio di stampa.

## 6. Contenuti da verificare esternamente

Fonti e limiti dei riscontri normativi sono quelli dei rapporti specialistici dello step 15 e del registro delle correzioni. Questa passata verifica la proiezione dei contenuti già riesaminati. Restano da attestare i servizi digitali promessi e i dati editoriali effettivi. Copertina, anteprima esterna e prova fisica appartengono alla preparazione della consegna e non costituiscono, da soli, nuovi errori del manoscritto.

## 7. Miglioramenti facoltativi

Alcune chiusure di capitolo conservano bianco ampio; alcune continuazioni di tabella hanno poche righe. Non comprimere il corpo per recuperare pagine. Gli eventuali ritocchi richiedono una nuova prova e il controllo delle pagine modificate.

## 8. Priorità operative

Risolvere FM{v}-01 e FM{v}-02 prima di chiudere la revisione finale. Conservare il pacchetto preparatorio e gli hash di questa prova; aggiornare soltanto le evidenze realmente invalidate da eventuali correzioni successive. Poi eseguire nell’ordine preflight, preparazione della consegna e conferma umana, senza saltare i gate.

## 9. Giudizio di pubblicabilità

Interno revisionabile e documentato, ma pubblicabilità complessiva non dichiarata: restano le due dipendenze editoriali sopra indicate. Nessun gate 24 eseguito. I controlli locali sono evidenza preparatoria per gli step successivi, non equivalgono alla loro chiusura.

## 10. Copertura e limiti

Panoramica coperta su {pages}/{pages} pagine: {len(ledger['directPanoramaPages'])} viste direttamente nella prova corrente e {len(ledger['pixelMatchedPreviouslyReviewedPages'])} corrispondenti pixel per pixel a pagine già viste. La corrispondenza esclude i 40 pt inferiori del piè di pagina; numeri e indice sono controllati separatamente. Dettagli correnti ingranditi: {', '.join(map(str,ledger['closeupsSeenCurrentProof'])) or 'nessun nuovo dettaglio; si vedano i dettagli della prova precedente e il confronto pixel'}. Dettagli nella prova precedente: {', '.join(map(str,ledger['closeupsSeenPreviousProof']))}.

Evidenze: `artifacts/correzioni-collana-2026-10-02/VOL-{v}-production-visual-checkpoint.json`, `{label}-verification.json`, `{label}-proof-audit/metrics.json` e confronto di rendering. Panoramica e riscontri mirati non equivalgono alla correzione di bozze a piena risoluzione di ogni pagina; nessuna prova fisica eseguita.
'''
 (R/f'PDF-VOL-{v}.md').write_text(text,encoding='utf8')
 save={'volume':'VOL-'+v,'pdf':label+'-proof.pdf','sha256':ledger['sha256'],'findings':[{'id':r[0],'position':r[1],'status':r[-1],'evidence':r[4]+' '+r[5]} for r in rows]}
 (A/f'VOL-{v}-production-findings.json').write_text(json.dumps(save,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 for step in ['19','20']:
  # Step 20 is written only after reading its canonical prompt separately.
  if step=='20':continue
  p=Path(f'wiki/reviews/pipeline/VOL-{v}/{step}-vol-{v}.md')
  if p.exists():shutil.copy2(p,A/f'VOL-{v}-step{step}-before-production.md')
  p.write_text(f'''# VOL-{v} — Impaginazione di produzione

Master applicato alla prova `{label}-proof.pdf`, {pages} pagine. Formato 6,69 × 9,61 in senza bleed; colonna singola, margini speculari del master, Garamond 11 pt, titoli Arial 20/14/12 pt e apparati 9,5 pt nominali. Nessun testo o immagine eliminato per ridurre il conteggio.

Riflusso, divisioni delle tabelle e numerazione sono verificati nel [rapporto PDF](../../correzioni-collana-2026-10-02/PDF-VOL-{v}.md). I dati del front matter generato restano una dipendenza editoriale da risolvere nella revisione finale; l’impaginazione non ne attesta la correttezza commerciale. Indice: {entries} voci confrontate con la destinazione effettiva. Nessun overflow locale, font incorporati.

Lo step non dispone di gate automatico; verifica manuale documentata. Nessuna accettazione KDP o prova fisica dichiarata.
''',encoding='utf8')
 print(v,len(rows),pages)
