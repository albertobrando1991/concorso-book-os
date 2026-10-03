from pathlib import Path
import json,hashlib,shutil
A=Path(__file__).parent;W=Path('wiki/reviews/correzioni-collana-2026-10-02');label='vol-04-reader-final-20261003'
load=lambda p:json.loads(p.read_text('utf8'))
v=load(A/(label+'-verification.json'));assert not v['indexMismatches'] and not v['overflowPages'] and v['allFontsEmbedded']
ledger=load(A/'VOL-04-ledger.json');assert len(ledger['findings'])==29
old=W/'VOL-04.md';backup=A/'VOL-04-progress-report-before-final.md'
if not backup.exists():shutil.copy2(old,backup)
table='| ID | Stato | Intervento verificato |\n|---|---|---|\n'+'\n'.join('| '+r['id']+' | Corretto e verificato | '+r['evidence'].replace('|',' / ')+' |' for r in ledger['findings'])
text=f'''# VOL-04 — Correzioni e integrazioni completate sul testo

## 1. Sintesi editoriale

Revisionati tutti i 17 capitoli e apparati di Giustizia e UPP; i 29 rilievi testuali iniziali hanno una correzione documentata. Il programma specialistico comprende 14 capitoli disciplinari, appendici operative, conclusione e fonti. Prova finale: {v['pages']} pagine, SHA-256 `{v['sha256']}`.

## 2. Punti di forza

84 quiz con quattro alternative e commento, chiavi A/B/C/D distribuite 21 volte ciascuna. Sei simulazioni complete con dossier, consegne, soluzione ragionata e griglia su 30 punti: UPP civile, penale, cancelleria, UNEP, minorile e penitenziario. Distinti i compiti di supporto dalle decisioni riservate alle autorità competenti.

## 3. Tabella delle correzioni

{table}

## 4. Macrostruttura e copertura

La matrice puntuale collega nuclei, fonti, casi e quiz; non considera il numero dei quiz una prova sufficiente di esaustività. Il nucleo comune resta nel volume base; il delta specialistico riguarda uffici, ordinamento, procedimenti e servizi della Giustizia. I 17 capitoli sono legacy: non vengono dichiarati retroattivamente formato 2. Il perimetro esclude la preparazione completa alla magistratura e alle altre carriere premium. Il candidato deve sempre rapportare il percorso al proprio bando.

## 5. Fonti e correttezza

Nove source notes consolidate al 3 ottobre 2026 coprono organizzazione, civile, penale, cancelleria, spese, casellario, UNEP, digitale, minorile e penitenziario. Acquisizioni grezze errate o incomplete sono state escluse, non usate come prova. Corrette la conversione del DL 100/2026 e la distinzione fra approvazione parlamentare del DL 144 il 30 settembre e successiva pubblicazione della legge. Il PCT distingue la prima ricevuta di accettazione nel regime delle specifiche vigenti, condizionata all'accettazione del deposito, dalla seconda PEC storica. Le decorrenze penali future restano future. Termini, soglie, casi e chiavi sono riscontrati nei report 13–15, con i rispettivi limiti.

## 6. Lingua, terminologia e didattica

Precisati soggetti, funzioni, termini, effetti e limiti. Riscritte domande generiche e distrattori deboli; eliminate formulazioni assolute non sostenibili. Uniformati acronimi, denominazioni attuali e storiche, notificazione/comunicazione, UPP/uffici di procura, DGMC/DAP/UEPE. Le ultime correzioni di superficie riguardano spaziature nelle rubriche e due richiami ripetitivi al diario; norme, punteggi e soluzioni restano invariati.

## 7. Secondo controllo

Gate 13, 14 e 15 superati; freeze 16 chiuso manualmente perché il gate non è automatizzato. I delta successivi sono registrati nel manifest M-FC04-freeze.json con prima/dopo. Il rapporto [PDF-VOL-04](PDF-VOL-04.md) documenta indice, pagine, font, tabelle, preliminari e copertura visiva. Il controllo del PDF integra la lettura integrale iniziale e il riesame delle modifiche; non equivale a una nuova certificazione astratta di ogni proposizione.

## 8. Giudizio editoriale

**Pubblicabile con correzioni minori di confezione finale.** Nessun rilievo testuale iniziale resta irrisolto nel perimetro dichiarato. La prima pagina e il colophon del candidato locale derivano dai master corretti, senza la promessa standard dei servizi digitali generata dall'API. Restano il preflight del pacchetto, la copertina coerente con pagine e carta, gli identificativi del canale scelto e la conferma finale. Questa valutazione non è un upload né una prova fisica di stampa.

## 9. Artefatti

Pacchetto: `delivery/VOL-04/candidate-2026-10-03/README.md`. Ledger dei 29 rilievi, 9 note fonti, matrice, report canonici 13–16, delta tipografici, payload di stampa e PDF sono conservati con hash. Le prove precedenti sono superate; non consegnare il candidato originario di 303 pagine.

## 10. Priorità residue

Terminare i gate di preflight e consegna nell'ordine del CLI. Il front matter corretto è applicato nella proiezione locale riproducibile inclusa: l'esportazione generica dell'API non è equivalente a questo candidato e può reintrodurre testi standard. Copertina, identificativi editoriali e prova fisica devono riferirsi al candidato definitivo, senza riusare il dorso del vecchio PDF. Nessun signoff umano 24 è stato eseguito.
'''
old.write_text(text,'utf8')
rows=[('P04-01','Quiz, già p. 65','Didattica','Grave','La soluzione precedeva le alternative.','Domanda, quattro alternative, poi risposta e commento; ordine riscontrato nei PDF.','Corretto e verificato'),('P04-02','Tabella spesa/evento, già p. 152','Layout','Media','Parole e acronimi interrotti nelle celle.','Etichette con separatori spaziati e quattro colonne; tavola controllata a piena leggibilità.','Corretto e verificato'),('P04-03','Aperture dei 17 capitoli','Gerarchia','Lieve','Titoli consecutivi duplicati.','Rimosso il solo H1 ridondante; titolo metadata conservato e generato una volta.','Corretto e verificato'),('P04-04','Finali di capitolo','Paginazione','Media','Code molto brevi e pagine quasi vuote.','Riflusso senza riduzione di font; due richiami al diario condensati riassorbiti alle pp.38 e136. Conservate le chiusure autonome con contenuto.','Corretto e verificato')]
pt='| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |\n|---|---|---|---|---|---|---|\n'+'\n'.join('| '+' | '.join(r)+' |' for r in rows)
report=f'''# VOL-04 — Revisione dell'impaginato corrente

## 1. Sintesi editoriale

PDF di {v['pages']} pagine, SHA-256 `{v['sha256']}`. Tutti i 17 capitoli e apparati previsti, 84 quiz e sei simulazioni. I quattro rilievi PDF originari sono corretti; i 29 rilievi testuali sono documentati separatamente in VOL-04.md.

## 2. Punti di forza

Tabelle native, nessun diagramma raster minuto, schede compilabili, casi completi e bibliografia leggibile. Gli URL lunghi sono sostituiti a stampa da titoli identificabili e domini ufficiali; i 23 collegamenti integrali sono preservati nel registro bibliografico e nelle fonti.

## 3. Tabella degli interventi

{pt}

## 4. Struttura e completezza

Indice di 17 capitoli verificato contro titoli e pagine fisiche. La struttura legacy non contiene un indice di nuclei numerati; non viene dichiarato un controllo di nuclei inesistenti. Nessun contenuto staff, asset mancante o glifo sostitutivo trovato nei controlli del candidato.

## 5. Contenuto e fonti

Audit normativo e didattico del 3 ottobre: nove source notes, rapporti 13–15 e manifest 16. Il delta di produzione elimina duplicazioni di titolo, migliora separatori e rubriche, rende leggibili le citazioni e riduce due chiusure ridondanti. Non cambia le regole, i punteggi o le chiavi dei quiz. FM1 e FM3 sono proiettati dai master effettivi, ignorati dall'export generico: ora non promettono un servizio commerciale non confermato.

## 6. Tipografia e geometria

Formato 6,69 × 9,61 pollici; Garamond circa 11 pt, tabelle e indice almeno circa 9,5 pt. Font incorporati; zero overflow e testo fuori pagina. Nessuna immagine raster. Testatine e numeri pagina hanno corpi distinti dal testo didattico. DOM e PDF hanno lo stesso conteggio finale; il conteggio intermedio del browser non identifica l'export.

## 7. Copertura visiva

Il coordinatore ha esaminato tutte le 24 tavole della precedente prova di 369 pagine, con ingrandimenti di 6,8,71,183,257,262,354,358,367,368,369. La revisione finale e il confronto con il candidato corrente sono registrati in vol04-proof/visual-review.json. La proiezione finale viene confezionata solo dopo tale riscontro. La vista panoramica copre struttura e composizione; non è lettura di ogni riga in miniatura. Le immagini di controllo e il rapporto del delta restano nel pacchetto.

## 8. Giudizio

**Pubblicabile con correzioni minori di confezione finale.** L'interno revisionato soddisfa i controlli locali qui descritti. Identificativi del canale, copertina, prova fisica e accettazione KDP non sono attestati. Nessuna conferma finale 24.

## 9. Consegna riproducibile

`delivery/VOL-04/candidate-2026-10-03/README.md`: PDF, sorgenti, payload congelato, fonti, hash, report e riproduzione. L'export generico non è equivalente alla proiezione locale FM1/FM3: usare il candidato identificato dall'hash, non i PDF storici.

## 10. Passaggi successivi

Preflight, dati del canale e copertina sul numero definitivo di pagine, quindi revisione della confezione e conferma umana conclusiva. Un cambiamento successivo di testi o preliminari richiede rigenerazione e controllo dei rimandi interessati.
'''
(W/'PDF-VOL-04.md').write_text(report,'utf8')
p=Path('wiki/reviews/pipeline/VOL-04/21-vol-04.md')
if p.exists() and not (A/'VOL-04-step21-before-final.md').exists():shutil.copy2(p,A/'VOL-04-step21-before-final.md')
p.write_text('---\nstatus: review\nreview_required: false\nupdated: 2026-10-03\n---\n\n'+text+'\n\n'+report,'utf8')
ledger['production']=dict(pdfSha256=v['sha256'],pages=v['pages'],findings=[dict(zip(['id','position','category','severity','diagnosis','correction','status'],r)) for r in rows],finalSignoff=False)
(A/'VOL-04-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),'utf8')
print('VOL04 final reports and 33 original findings documented')
