from pathlib import Path
import json,hashlib,shutil
A=Path(__file__).parent;R=A/'vol05-proof';D=Path('delivery/VOL-05/candidate-2026-10-03');W=Path('wiki/reviews/correzioni-collana-2026-10-02');P=Path('wiki/reviews/pipeline/VOL-05')
def load(p):return json.loads(p.read_text(encoding='utf8'))
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
v=load(R/'verification.json');vis=load(R/'visual-review.json');projection=load(R/'projection-manifest.json');freeze=load(A/'M-FC05-freeze.json')
assert vis['pdfSha256']==v['pdfSha256'] and vis['allFinalPagesVisuallyCovered']
assert v['domPdfPageCountMatch'] and not any(v[k] for k in ['indexMismatches','outsidePage','overflowPages','internalLeaks'])
assert all(f['embedded'] for f in v['fonts']) and len(v['nativeSchemes'])==75 and all(len(s['pages'])==1 for s in v['nativeSchemes'])
assert all(sha(Path(r['path']))==r['sha256'] for r in freeze['files'])
assert all(sha(Path(r['path']))==r['sha256'] for r in projection['sourceHashes'])
rows=[
('P05-01','75 schemi, capitoli 1–15','Didascalie','media','Doppie didascalie e titoli interposti nel PDF storico.','Un solo titolo Schema N.N con tabella nativa; didascalie duplicate eliminate.','Risolto e verificato'),
('P05-02','Tutti gli schemi; Decoder pp. 17–18','Leggibilità','media','Microtesto e giallo poco contrastato nelle figure raster.','75 schemi a caratteri nativi, tabelle 9,5 pt; Decoder verticale compilabile.','Risolto e verificato'),
('P05-03','Schemi 3.3 e 10.4 e serie collegata','Didattica visuale','media','Etichette generiche senza presupposti o conseguenze.','Reti, competenze e designazioni distinte con contenuti specifici.','Risolto e verificato'),
('P05-04','Capitolo 1, rinvii alla base','Rinvii','grave','Sequenza stampata «su , e ;», riscontro di V05-01.','Destinazioni e titoli ricostruiti; zero rinvii sorgente irrisolti e nessuna sequenza vuota.','Risolto e verificato'),
('P05-20','70 tavole originali dei capitoli 2–15','Didattica visuale','grave','Cinque modelli ripetuti con riempitivi.','70 schemi specifici; ulteriori cinque iniziali convertiti dopo prova di stampa.','Risolto e verificato'),
('P05-21','Quindici mappe BANDO','Metodo','grave','Lettere associate a concetti estranei al metodo.','Bando, Aree, Nuclei, Diario e Output applicati alla preparazione del tema.','Risolto e verificato'),
('P05-22','Mappe BANDO','Connettori','lieve','Ramo Output staccato dalla linea comune.','Relazioni espresse in tabelle; nessun connettore ambiguo residuo.','Risolto e verificato'),
('P05-23','Schemi 11.3 e 14.3, pp. 164 e 209','Sequenze e garanzie','media','Sanzione necessaria e protezione soltanto dopo l’istruttoria.','Esiti condizionati del controllo; riservatezza e protezione lungo il percorso.','Risolto e verificato'),
('P05-24','Bibliografie dei capitoli 1–14','Composizione','media','20 link esterni stampati con sintassi Markdown.','Titolo e dominio nella proiezione; URL completi nei master e manifest.','Risolto e verificato'),
('P05-25','Capitolo 2, pp. 35–39; capitolo 14, pp. 219–220','Riflusso','media','Grande vuoto prima del nucleo 2.4 e bibliografia isolata in chiusura ANAC.','Sottotitolo breve nel capoverso; bibliografia ANAC prima del caso. Tutte le parole conservate; bianchi finali di chiusura restano ammessi.','Risolto nel perimetro dichiarato'),
('C05-01','Front matter, pp. 1–4','Dipendenza comune','grave','Promessa di servizi digitali non verificata; colophon commerciale incompleto; descrizione «modulo premium per target ristretto».','Consolidare offerta e dati editoriali; sostituire la descrizione interna; proiettare i preliminari corretti e ricontrollare.','Aperto; coordinamento comune')]
table='| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |\n|---|---|---|---|---|---|---|\n'+'\n'.join('| '+' | '.join(r)+' |' for r in rows)
report=f'''# VOL-05 — Revisione del candidato impaginato, 3 ottobre 2026

## 1. Sintesi editoriale

Il candidato corrente ha **239 pagine**, 15 capitoli, 75 nuclei e 75 schemi nativi. Sono chiusi i 33 rilievi testuali e gli otto rilievi PDF/figure della baseline. L’ultima produzione corregge inoltre link visibili e riflusso. Restano aperte le dipendenze comuni del front matter: **nessun giudizio finale di pubblicabilità e nessuno step 24**.

SHA-256 PDF: `{v['pdfSha256']}`.

## 2. Punti di forza e checklist

Percorsi giuridico, economico-regolatorio e giuridico-economico distinti; teoria specialistica, applicazioni e output raccordati. Controllati struttura, copertura v4, autonomia, promesse, fonti, distinzioni, progressione, ripetizioni, stile, esempi, errori, quesiti, soluzioni, lingua, rinvii e impaginazione secondo la checklist a 30 punti. La lettura integrale dei 15 originali e il riesame delle integrazioni sono documentati nel checkpoint testuale; il controllo grafico non viene presentato come nuova rilettura integrale di ogni riga del PDF.

## 3. Registro degli interventi e residui

{table}

## 4. Macrostruttura e copertura

Tutti i 15 master sono presenti, nell’ordine previsto; 75 nuclei e 90 voci d’indice hanno destinazioni corrette nel PDF. Matrice analitica e 15 unità aggregate aggiornate. Nessun nucleo mancante o parziale nei gate; tutti i 15 controlli di capitolo passano senza blocker né warning. I rinvii al VOL-01 usano destinazioni esistenti; il volume sviluppa l’applicazione specialistica senza duplicare le materie comuni. Nessun sottoprofilo estraneo è stato introdotto per aumentare la copertura apparente.

## 5. Contenuto, norme e verifiche

I 90 quesiti aperti, 15 casi finali e 10 simulazioni sono stati riscritti e risolti nel ciclo testuale. I dossier contengono dati sufficienti e soluzioni motivate; calcoli, memo inglese e attribuzioni di competenza sono tracciati. Gli aggiornamenti comprendono TUF e OPA 2026, transitorio dei ricorsi, MAR, MiCAR, AAS, soglie AGCM, regolazione ARERA, DSA/DMA, GDPR e whistleblowing nei limiti delle note consolidate. I riscontri primari sono mirati alle disposizioni dichiarate, non all’intero contenuto di ogni testo unico. Alcuni atti UE sono verificati su estratti primari indicizzati: non si attribuisce lettura integrale ai PDF non acquisiti.

I 75 schemi restano coerenti con tali fonti. La verifica differenziale ricostruisce il corpo precedente isolando schemi, didascalie e confine del nucleo 8.3; quiz, casi e teoria esterna al delta sono preservati. La proiezione modifica 20 link, un breve sottotitolo e l’ordine/aggregazione di capoversi ANAC: confronto dei token e dei blocchi strutturati superato su 15 capitoli, senza perdita di contenuto.

## 6. Tipografia e geometria

Formato 6,69 × 9,61 pollici, 481,92 × 691,92 pt, senza bleed; colonna singola e margini speculari. Garamond 11 pt nel corpo, Arial 20/14/12 pt nella gerarchia, tabelle e indice a 9,5 pt. I quesiti aperti conservano il corpo Garamond con testata Verifica distinta. I corpi inferiori appartengono a marchi, indicatori BANDO e testatine; nessun contenuto didattico delle tavole dipende da microtesto. Font incorporati; zero overflow rispetto al piè di pagina, zero testo fuori pagina, zero immagini mancanti, zero HTML letterale. I 75 raster originali sono preservati nel repository; nel candidato sono sostituiti da schemi nativi.

## 7. Copertura visiva e seconda passata

Visionate tutte le 15 tavole contatto della prova da 239 pagine e 50 pagine ingrandite. Dopo l’ultimo riflusso, **232 pagine risultano pixel-identiche a 72 dpi**; tutte le **7 pagine modificate** sono state riesaminate a piena pagina. La copertura finale comprende così tutte le pagine e **53 pagine distinte di dettaglio**. I contatti finali sono rigenerati nel pacchetto; il registro distingue la visione della prova precedente dal controllo del delta, senza attribuire una rilettura separata a tavole non riaperte.

Controllati numerazione, tabelle e loro continuazioni, blocchi Verifica, campi compilabili, gerarchie, confini pagina, schemi, indice e bibliografie. Pagina 35 è riequilibrata. Le chiusure 39 e 220 mantengono spazio bianco dopo autovalutazione/riferimenti o conclusione del caso: non sono pagine vuote né contengono perdite. Le tavole panoramiche non sostituiscono la lettura del testo minuto o una prova fisica.

## 8. Giudizio di pubblicabilità

**Non pubblicabile allo stato attuale**, per C05-01. L’interno specialistico ha superato i controlli descritti, ma la promessa digitale e i dati commerciali comuni non sono verificati. Non sono attestati ISBN, copertina, accettazione KDP o prova fisica. Step 21 resta aperto; 22, 23 e 24 non vengono chiusi da questo lavoro. Il pacchetto è un candidato locale reviewabile, non una consegna autorizzata alla pubblicazione.

## 9. Artefatti e riproducibilità

Pacchetto: `delivery/VOL-05/candidate-2026-10-03/README.md`. Include PDF, payload congelato, manifest della proiezione, master e note fonte del freeze, registri testuali e visuali, immagini di controllo, hash e helper di riproduzione. I file storici `native` e `final` sono prove intermedie; il candidato corrente è `vol-05-candidate-20261003-proof.pdf`, copiato nel pacchetto come `vol-05-interior-kdp.pdf`.

Gate 14 e 15 rieseguiti dopo il delta e superati. Freeze manuale originario preservato; manifest corrente aggiornato con delta controllato. Step 18 e 19 non hanno gate automatico; step 20 accettato manualmente dopo `gate-not-implemented`, con evidenza pagina per pagina. Non viene simulata una verifica automatica inesistente.

## 10. Priorità residue e limiti

Risolvere C05-01 con i preliminari comuni consolidati; rigenerare la proiezione e ricontrollare pagine modificate, indice e conteggio. Completare poi i gate nell’ordine del CLI. Nessun upload, commit, push, pubblicazione o signoff umano finale è stato effettuato. La verifica normativa resta circoscritta alle fonti e agli ambiti dichiarati; la geometria non equivale a un collaudo di stampa.
'''
(W/'PDF-VOL-05.md').write_text(report,encoding='utf8');(P/'21-vol-05.md').write_text('---\nstatus: review\nreview_required: true\nupdated_at: 2026-10-03\n---\n\n'+report,encoding='utf8')
ledger=load(A/'VOL-05-ledger.json');ledger['production']={'pdfSha256':v['pdfSha256'],'pages':239,'report':str(W/'PDF-VOL-05.md'),'visualReview':str(R/'visual-review.json'),'nativeSchemes':75,'baselinePDFAndFigureIDsClosed':['P05-01','P05-02','P05-03','P05-04','P05-20','P05-21','P05-22','P05-23'],'findings':[dict(zip(['id','position','category','severity','description','correction','status'],r)) for r in rows],'finalSignoff':False};ledger['finalVerified']=False
for r in ledger['files']:r['sha256']=sha(Path(r['path']));r['pdfReview']='All-page visual coverage with 53 detailed pages; declared limits in PDF-VOL-05'
save(A/'VOL-05-ledger.json',ledger)
freeze['pdfChecked']={'sha256':v['pdfSha256'],'pages':239,'method':vis['method'],'finalSignoff':False};save(A/'M-FC05-freeze.json',freeze)
progress=load(A/'VOL-05-progress.json');progress['pending']=['C05-01: servizi digitali, dati editoriali e descrizione comune','Gate 21–24 dopo preliminari corretti'];progress['production'].update(pdfPages=239,pdfSha256=v['pdfSha256'],package=str(D),visualCoverage='239 pages; 53 details; final delta verified');save(A/'VOL-05-progress.json',progress)
p=W/'VOL-05.md';s=p.read_text(encoding='utf8');s+='\n## Esito della produzione\n\nCandidato di 239 pagine e 75 schemi nativi verificato; otto ID PDF/figure della baseline chiusi. Rapporto completo in [PDF-VOL-05.md](PDF-VOL-05.md), con copertura visiva e limiti. Restano aperte le dipendenze comuni C05-01; nessuno step 24.\n';p.write_text(s,encoding='utf8')
for sub in ['reports','masters','visual','reproduction']:(D/sub).mkdir(parents=True,exist_ok=True)
shutil.copy2(A/'vol-05-candidate-20261003-proof.pdf',D/'vol-05-interior-kdp.pdf')
for name in ['payload.json','source-payload.json','projection-manifest.json','projection-preservation.json','verification.json','visual-review.json','balance-comparison.json','page-review.json']:shutil.copy2(R/name,D/name)
shutil.copy2(A/'vol-05-candidate-20261003-proof-metrics.json',D/'proof-metrics.json')
for row in freeze['files']:
 src=Path(row['path']);dst=D/'masters'/src.relative_to('wiki');dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
for p in (R/'contacts').glob('contact-*.jpg'):shutil.copy2(p,D/'visual'/p.name)
for n in vis['fullResolutionPagesViewed']:shutil.copy2(R/'details'/f'page-{n:03}.png',D/'visual'/f'page-{n:03}.png')
for p in [W/'PDF-VOL-05.md',W/'VOL-05.md']+list(P.glob('1[45689]-*.md'))+[P/'20-vol-05.md',P/'21-vol-05.md']:shutil.copy2(p,D/'reports'/p.name)
for name in ['VOL-05-ledger.json','VOL-05-native-schemes.json','VOL-05-native-checkpoint.json','VOL-05-FC05-gates.json','VOL-05-FC05-links.json','VOL-05-simulations-verification.json','VOL-05-economia-calculations.json','VOL-05-external-reading-scope.json','M-FC05-freeze.json','M-FC05-freeze-before-graphics.json']:shutil.copy2(A/name,D/'reports'/name)
script=(A/'export-vol05-proof.mjs').read_text(encoding='utf8').replace("from '../../scripts/","from '../../../../scripts/").replace("import path from 'node:path'","import path from 'node:path'\nimport {fileURLToPath} from 'node:url'")
script=script.replace("const out=path.resolve('artifacts/correzioni-collana-2026-10-02')","const out=fileURLToPath(new URL('../reproduced/',import.meta.url));await fs.mkdir(out,{recursive:true})")
script=script.replace("fs.readFile('artifacts/correzioni-collana-2026-10-02/vol05-proof/payload.json','utf8')","fs.readFile(new URL('../payload.json',import.meta.url),'utf8')")
(D/'reproduction/export-vol05-proof.mjs').write_text(script,encoding='utf8')
for name in ['build-vol05-proof.py','verify-vol05-proof.py']:shutil.copy2(A/name,D/'reproduction'/name)
renderer=[Path('src/book/pagination.ts'),Path('src/server/book/book-preview.ts'),Path('scripts/book-studio-pdf-export-core.mjs'),Path('scripts/book-studio-layout-options.mjs')]+list(Path('app').rglob('*.css'))+list(Path('app').rglob('*book*.tsx'))
save(D/'renderer-source-hashes.json',[{'path':str(p),'sha256':sha(p)} for p in renderer if p.is_file()])
(D/'README.md').write_text(f'''# VOL-05 — candidato interno del 3 ottobre 2026

[PDF interno](vol-05-interior-kdp.pdf): **239 pagine**, 6,69 × 9,61 pollici. SHA-256 `{v['pdfSha256']}`.

15 capitoli, 75 nuclei, 90 quesiti aperti, 15 casi finali, 10 simulazioni e 75 schemi nativi. Trentatré rilievi testuali e otto rilievi storici PDF/figure corretti. Indice 90/90, zero overflow e font incorporati. Copertura visiva dichiarata: 15 contatti e 50 dettagli, poi sette pagine modificate riesaminate; le altre 232 sono pixel-identiche alla prova già vista. In totale 53 pagine distinte di dettaglio. Non è una nuova lettura integrale del testo minuto del PDF.

**Non pubblicabile allo stato attuale.** C05-01: servizi digitali, dati editoriali commerciali e descrizione comune devono essere consolidati. Nessun ISBN, copertina, upload KDP o prova fisica attestati. Step 21 aperto; nessuno step 24. Questo pacchetto rende verificabile il lavoro locale e non costituisce un via libera editoriale.

`masters` contiene i 36 file del freeze; `reports` conserva audit, fonti e registri; `visual` contiene contatti finali e dettagli correnti. `projection-manifest.json` documenta 20 link resi come nome e dominio, un sottotitolo incorporato e l’adattamento della chiusura ANAC. I master mantengono gli URL completi e la struttura originale. Nessun contenuto normativo, tabella, quesito o caso è eliminato dalla proiezione. I 75 raster originali rimangono nel repository, con hash nel ledger.

Riproduzione dal checkout con dipendenze installate e Book Studio su 127.0.0.1:3020: `node delivery/VOL-05/candidate-2026-10-03/reproduction/export-vol05-proof.mjs`. Usa il payload congelato e scrive in `reproduced`; renderer e font devono corrispondere agli hash. Gli altri helper sono copie di lavoro, da eseguire nella cartella artefatti originale dopo averne verificato i percorsi. Ogni rigenerazione richiede controlli nuovi.

Le prove storiche nelle altre cartelle delivery e quelle intermedie non sono questo candidato. Eventuali preliminari corretti dal coordinatore richiedono una nuova proiezione e un nuovo manifest.
''',encoding='utf8')
save(D/'package-manifest.json',{'volume':'VOL-05','date':'2026-10-03','pdfSha256':v['pdfSha256'],'files':[{'path':p.relative_to(D).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(D.rglob('*')) if p.is_file() and p.name!='package-manifest.json']})
print(json.dumps({'pages':239,'pdfSha256':v['pdfSha256'],'files':len(load(D/'package-manifest.json')['files']),'package':str(D)},ensure_ascii=False))
