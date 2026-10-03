from pathlib import Path
import json,hashlib,shutil
A=Path(__file__).parent; R=A/'vol03-proof'; D=Path('delivery/VOL-03/candidate-2026-10-03'); W=Path('wiki/reviews/correzioni-collana-2026-10-02')
def load(p):return json.loads(p.read_text(encoding='utf8'))
def save(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
v=load(R/'verification.json');m=load(R/'manifest.json');vis=load(R/'visual-review.json')
assert vis['pdfSha256']==v['pdfSha256'] and vis['allContactSheetsViewed']
assert v['domPdfPageCountMatch'] and not v['indexMismatches'] and not v['pdfIndexMismatches'] and not v['overflowPages'] and not v['internalLeaks']
assert all(f['embedded'] for f in v['fonts']) and all(f['currentMatch'] for f in v['sourceHashes'])
assert len(v['nativeSchemes'])==70 and len(m['workbookChanges'])==4
rows=[
('P03-01','Indice, pp. 6–11','Tipografia','grave','Indice precedente a 6,75 pt.','Indice corrente a 9,5 pt; 194 destinazioni verificate direttamente nel PDF.','Corretto e verificato'),
('P03-02','Capitoli 13, 14 e 31; tre workbook','Usabilità','grave','Otto/dieci colonne spezzavano le parole e riducevano lo spazio di scrittura.','Tre schede verticali a due colonne; campi vuoti con due righe; contenuti originali conservati.','Corretto e verificato'),
('P03-03','Capitoli 30–31; mappe, appendici e rinvii','Layout e navigazione','medio','Riga Output isolata, schemi ridondanti illeggibili e slug visibili.','Mappa BANDO a due colonne; schemi nativi; etichette umane per 126 link e allineamento di 113 righe di rinvii.','Corretto e verificato'),
('P03-04','Sequenza capitoli fiscali 20–23','Struttura','grave','05a e 05b erano collocati dopo le appendici.','Ordine 05,05a,05b,06; indice globale 20,21,22,23 e riscontro dei titoli fisici.','Corretto e verificato'),
('P03-05','Schemi 30.1,31.1,31.2,31.5','Correttezza didattica','grave','Espansione BANDO e mappa delle appendici non corrispondevano al testo.','Bando/Aree/Nuclei/Diario/Output; appendici A–H corrispondenti ai contenuti effettivi.','Corretto e verificato'),
('P03-06','Schemi 20.2,23.3,24.3,25.4,29.3,30.3','Correttezza didattica','grave','Frecce trasformavano alternative, tempi diversi e contesti distinti in fasi obbligatorie.','Tabelle native distinguono esiti del controllo, dichiarazione/liquidazione/versamento, titoli della riscossione, AEO e casi per ente.','Corretto e verificato'),
('P03-07','Schemi 18.2 e 31.5','Correttezza istituzionale','grave','Profili come quarto ente; EORI confuso con AEO.','Profili come criterio di studio; enti e relazioni corretti; EORI identificazione, AEO status autorizzato.','Corretto e verificato'),
('P03-08','FC03 appendice E, §49.3','Rinvii errati','medio','Cybersecurity, Consip e authority indicavano altri volumi; capitoli locali ambigui.','Master corretto: VOL-08, VOL-09, VOL-05; ricerca e fisco rinviati al modulo e titolo effettivi. Gate 14/15/16 rieseguiti.','Corretto e verificato'),
]
table='| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |\n|---|---|---|---|---|---|---|\n'+'\n'.join('| '+' | '.join(row)+' |' for row in rows)
report=f'''# Revisione dell’impaginato corrente — VOL-03

## 1. Sintesi

Prova interna del 3 ottobre 2026: **{v['pages']} pagine**, 50 capitoli/appendici, 3 moduli, 144 nuclei e 194 voci d’indice. I 70 diagrammi testuali raster sono stati sostituiti da schemi nativi leggibili e corretti nel significato. Il PDF è un candidato tecnico revisionato: rimangono aperte le dipendenze comuni sui servizi digitali e sui dati editoriali. Nessun via libera step 24.

SHA-256 PDF: `{v['pdfSha256']}`.

## 2. Punti di forza

Progressione Ministeri, Agenzie fiscali, EPNE; casi e quiz preservati rispetto al freeze testuale. Le tabelle mantengono confronti e alternative senza false frecce di sequenza. I workbook più densi hanno spazio di compilazione verticale. Indice e rinvii usano la numerazione globale del volume.

## 3. Interventi verificati

{table}

## 4. Macrostruttura e completezza

Sono presenti tutti i 50 master previsti dal catalogo e tutti i 144 nuclei. Hash correnti confrontati con le sorgenti usate nell’export: zero difformità. La revisione testuale integrale del 2 ottobre e le correzioni testuali registrate il 3 ottobre restano documentate nei rispettivi audit; questo rapporto non dichiara una nuova rilettura integrale parola per parola. Il delta di produzione comprende 70 schemi, un passaggio IVA e cinque destinazioni della tabella EPNE, con confronto inverso e snapshot. I quiz e i casi non sono stati riscritti da questa lavorazione grafica.

## 5. Contenuto, fonti e rinvii

I 70 schemi originali sono stati esaminati e confrontati semanticamente con le nuove tavole. Fonti e limiti sono nella nota `wiki/sources/vol-03-schemi-fiscali-verifica-2026-10-03.md`; per EORI/AEO sono state ricontrollate le pagine ufficiali della Commissione. Le correzioni sostanziali precedenti conservano le loro source notes. Non viene attribuita alla verifica grafica una nuova certificazione di ogni norma. L’allineamento dei 113 riferimenti numerati e delle 126 etichette è registrato con prima/dopo nel manifest della proiezione. I rinvii esterni indicano moduli e titoli reali; quelli interni sono coerenti con l’indice.

## 6. Tipografia e geometria

Formato 6,69×9,61 pollici, {v['trimPt'][0]:.2f}×{v['trimPt'][1]:.2f} pt. Testo principale Garamond circa 11 pt; tabelle circa 9,5 pt; indice minimo 9,5 pt. Font incorporati, inclusi i glifi Type3 con CharProcs. Zero overflow DOM rispetto al piè di pagina, zero testo fuori pagina nella scansione geometrica. Nessuna figura raster residua nel PDF; i PNG originali restano archiviati nel repository. Il rispetto geometrico non equivale a una prova fisica di stampa.

## 7. Secondo controllo e copertura visiva

Visionate tutte le {len(vis['contactSheets'])} tavole contatto del candidato corrente ({v['pages']} pagine), più {len(vis['fullResolutionPagesViewed'])} pagine ingrandite, elencate nel registro visuale. Le tavole contatto consentono il controllo di struttura, ritmo, vuoti, salti e densità; non sono una lettura integrale del testo minuto a piena risoluzione. L’indice è stato verificato anche con estrazione diretta del PDF: 194/194 destinazioni corrette. La modalità stampa è stabilizzata e il DOM congelato prima dell’esportazione: conteggi DOM e PDF coincidenti. Sono ammesse continuazioni di tabelle con intestazione ripetuta; non sono state trovate perdite di righe.

## 8. Giudizio finale

**Non pubblicabile allo stato attuale per dipendenze editoriali comuni ancora aperte.** Il candidato interno ha superato le verifiche locali qui descritte. La promessa dei servizi digitali di pagina 1 non è stata verificata; dati editoriali commerciali, copertina, prova fisica e accettazione KDP non sono attestati. Step 21 resta in corso; 22, 23, 24 non chiusi da questo rapporto.

## 9. Produzione e artefatti

La [specifica KDP](https://kdp.amazon.com/it_IT/help/topic/GVBQ3CMEQW3W2VL6), verificata nel fascicolo di produzione VOL-02 il 3 ottobre, consente fino a 828 pagine per questo formato con nero e carta bianca. Il candidato di {v['pages']} pagine rientra in tale limite; supera invece 776 pagine e non è candidato alla carta crema. Non occorre comprimere il carattere né dividere questo interno. Margini, dorso, copertina e pagine eventualmente aggiunte dal servizio vanno verificati nel successivo passaggio reale di produzione.

Pacchetto: `delivery/VOL-03/candidate-2026-10-03/README.md`. Prova, manifest, registri di geometria e indice, tavole contatto, ingrandimenti mirati, payload congelato e snapshot dei 50 master sono inclusi. Le prove intermedie precedenti sono superate e non vanno consegnate.

## 10. Priorità residue

Confermare l’offerta digitale e i dati editoriali comuni; applicare gli eventuali delta di front matter; rigenerare e ricontrollare il PDF interessato; completare i gate nell’ordine del CLI; preparare copertina e prova fisica. Non sono stati effettuati upload, pubblicazione o signoff finale. Il lavoro locale non chiude automaticamente i rilievi comuni di collana.
'''
W.mkdir(parents=True,exist_ok=True);(W/'PDF-VOL-03.md').write_text(report,encoding='utf8')
canonical=Path('wiki/reviews/pipeline/VOL-03/21-vol-03.md');archive=A/'VOL-03-step 21-before-production.md'
if not archive.exists():shutil.copy2(canonical,archive)
canonical.write_text('---\nstatus: review\nreview_required: true\nupdated: 2026-10-03\n---\n\n'+report,encoding='utf8')
ledger=load(A/'VOL-03-ledger.json')
for r in ledger['files']:
 r['sha256']=sha(Path(r['path']));r['pdfTechnicalAndVisualReview']='contact sheets complete; targeted full resolution; see PDF-VOL-03';r['finalVerified']=False
for r in ledger['findings']:
 if 'PDF candidato da verificare' in r['status']:r['status']=r['status'].replace('PDF candidato da verificare','PDF verificato tecnicamente e con copertura visiva dichiarata; dipendenze comuni aperte')
ledger['production']={'pdfSha256':v['pdfSha256'],'pages':v['pages'],'findings':[dict(zip(['id','position','category','severity','diagnosis','correction','status'],r)) for r in rows],'report':str(W/'PDF-VOL-03.md'),'visualReview':str(R/'visual-review.json'),'finalSignoff':False}
save(A/'VOL-03-ledger.json',ledger)
cor=W/'VOL-03.md';t=cor.read_text(encoding='utf8');marker='\n## Delta di produzione del 3 ottobre 2026\n';t=t.split(marker)[0]+marker+'\nApplicati e verificati i rilievi P03-01–08, con 70 schemi nativi, tre workbook verticali, rinvii e sequenza corretti. Il rapporto [PDF-VOL-03](PDF-VOL-03.md) distingue la copertura visiva dai controlli del testo. La prova corrente ha '+str(v['pages'])+' pagine e indice 194/194; nessun signoff 24, dipendenze comuni aperte.\n';cor.write_text(t,encoding='utf8')
for mod in ['M-FC01','M-FC02','M-FC03']:
 f=A/f'{mod}-freeze.json';d=load(f)
 assert all(sha(Path(r['path']))==r['sha256'] for r in d['files'])
 d['pdfChecked']={'sha256':v['pdfSha256'],'method':'all-page contact sheets and selected full resolution; geometry/index all pages','finalSignoff':False};save(f,d)
D.mkdir(parents=True,exist_ok=True)
for sub in ['reports','masters','derived','reproduction','visual']: (D/sub).mkdir(exist_ok=True)
shutil.copy2(R/'vol-03-current-proof.pdf',D/'vol-03-interior-kdp.pdf')
for name in ['verification.json','manifest.json','visual-review.json','payload.json','source-payload.json','vol-03-current-proof-metrics.json']:shutil.copy2(R/name,D/name)
shutil.copy2(R/'vol-03-current-proof-audit/metrics.json',D/'pdf-geometry.json')
for p in (R/'vol-03-current-proof-audit').glob('contact-*.png'):
 if p.name in vis['contactSheets']:shutil.copy2(p,D/'visual'/p.name)
for n in vis['fullResolutionPagesViewed']:shutil.copy2(R/f'final-page-{n:03}.png',D/'visual'/f'page-{n:03}.png')
for row in m['sourceHashes']:
 src=Path(row['path']);dest=D/'masters'/src.relative_to('wiki');dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)
for p in R.glob('*.md'):shutil.copy2(p,D/'derived'/p.name)
for p in [W/'PDF-VOL-03.md',W/'VOL-03.md',Path('wiki/sources/vol-03-schemi-fiscali-verifica-2026-10-03.md')]:shutil.copy2(p,D/'reports'/p.name)
for name in ['VOL-03-ledger.json','VOL-03-native-schemes.json','VOL-03-native-checkpoint.json','VOL-03-original-figures-review.json','VOL-03-P03-08.json','M-FC01-freeze.json','M-FC02-freeze.json','M-FC03-freeze.json']:shutil.copy2(A/name,D/'reports'/name)
script=(A/'build-vol03-proof.ts').read_text(encoding='utf8').replace("from '../../src/","from '../../../../src/");(D/'reproduction/build-vol03-proof.ts').write_text(script,encoding='utf8')
script=(A/'export-vol03-proof.mjs').read_text(encoding='utf8').replace("from '../../scripts/","from '../../../../scripts/").replace("import path from 'node:path'","import path from 'node:path'\nimport {fileURLToPath} from 'node:url'")
script=script.replace("fs.readFile(`artifacts/correzioni-collana-2026-10-02/vol03-proof/payload.json`,'utf8')","fs.readFile(new URL('../payload.json',import.meta.url),'utf8')")
script=script.replace("const out=path.resolve('artifacts/correzioni-collana-2026-10-02/vol03-proof')","const out=fileURLToPath(new URL('../reproduced/',import.meta.url));await fs.mkdir(out,{recursive:true})")
(D/'reproduction/export-vol03-proof.mjs').write_text(script,encoding='utf8')
rendererFiles=[Path('src/book/pagination.ts'),Path('src/server/book/book-preview.ts'),Path('scripts/book-studio-pdf-export-core.mjs'),Path('scripts/book-studio-layout-options.mjs')]+list(Path('app').rglob('*.css'))+list(Path('app').rglob('*book*.tsx'))
save(D/'renderer-source-hashes.json',[{'path':str(p),'sha256':sha(p)} for p in rendererFiles if p.is_file()])
(D/'README.md').write_text(f'''# VOL-03 — candidato interno del 3 ottobre 2026

PDF: [vol-03-interior-kdp.pdf](vol-03-interior-kdp.pdf), **{v['pages']} pagine**, formato 6,69×9,61 pollici. SHA-256 `{v['pdfSha256']}`.

50 capitoli/appendici, 70 schemi nativi, 194 rimandi d’indice verificati, font incorporati e nessun overflow rilevato. Copertura visiva: tutte le 51 tavole contatto più gli ingrandimenti dichiarati in visual-review.json. Non è una nuova rilettura del testo minuto su ogni pagina.

**Candidato per nero su carta bianca; non per carta crema. Nessuna autorizzazione finale alla pubblicazione.** Servizi digitali e dati editoriali comuni restano da confermare; non sono verificati copertina, upload KDP o prova fisica. Step 21 aperto, nessuno step 24.

Il rapporto reports/PDF-VOL-03.md contiene gli otto rilievi di produzione e i limiti. masters conserva i 50 master, derived le proiezioni di stampa; manifest.json registra i 113 allineamenti numerati, 126 etichette di link e 4 trasformazioni di tabelle (tre workbook e una mappa).

Riproduzione dal checkout con dipendenze già installate e BookStudio attivo su 127.0.0.1:3020: `node delivery/VOL-03/candidate-2026-10-03/reproduction/export-vol03-proof.mjs`. Usa il payload congelato incluso e salva un nuovo risultato in reproduced. Renderer e font del sistema devono corrispondere alle versioni registrate; una rigenerazione va sempre ricontrollata. build-vol03-proof.ts serve invece a ricostruire la proiezione dai master correnti attraverso l’API e produce gli artefatti nella cartella di lavoro; non sostituisce la prova congelata.

I PDF storici nelle altre cartelle delivery non sono questa consegna. Questo pacchetto resta sottoposto alle dipendenze comuni e al percorso di gate successivo.
''',encoding='utf8')
save(D/'package-manifest.json',{'volume':'VOL-03','date':'2026-10-03','pdfSha256':v['pdfSha256'],'files':[{'path':str(p.relative_to(D)).replace('\\','/'),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(D.rglob('*')) if p.is_file() and p.name!='package-manifest.json']})
print(json.dumps({'pages':v['pages'],'pdfSha256':v['pdfSha256'],'packageFiles':len(load(D/'package-manifest.json')['files']),'package':str(D)},ensure_ascii=False))
