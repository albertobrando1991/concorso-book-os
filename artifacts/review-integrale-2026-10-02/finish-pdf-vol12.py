import hashlib
import json
from pathlib import Path

root = Path('.')
pdf = 'delivery/VOL-12/candidate/vol-12-interior-kdp.pdf'
sha = hashlib.sha256(Path(pdf).read_bytes()).hexdigest()
inventory = next(x for x in json.loads(Path('artifacts/review-integrale-2026-10-02/pdf/inventory.json').read_text(encoding='utf-8-sig')) if x['volume'] == 'VOL-12')
assert sha == inventory['sha256']
base = Path('artifacts/review-integrale-2026-10-02/pdf/VOL-12/vol-12-interior-kdp')
contacts = sorted(p.as_posix() for p in base.glob('contact-*.jpg'))
assert len(contacts) == 20
details = [6, 11, 102, 120, 123, 124, 174, 285, 286, 349, 351, 459]
rows = [
 ('P12-01', 'pp. 6–9; dettaglio p. 6', 'Leggibilità', 'medio', 'L’indice completo è molto fitto: il corpo delle voci è di circa 6,75 punti e alcune etichette sono a 6,6 punti.', 'Aumentare il corpo e distribuire le voci su più pagine; verificare la leggibilità su una prova nelle dimensioni finali.'),
 ('P12-02', '30 pagine fra p. 100 e p. 174; dettagli pp. 102, 120, 123, 174', 'Residui di markup', 'grave', 'I tag HTML «<br>» sono stampati letteralmente dentro le celle, per esempio «compilare<br>Carabinieri». L’estrazione del PDF conta 299 occorrenze su 30 pagine; quattro pagine sono state confermate visivamente in dettaglio.', 'Correggere la gestione delle interruzioni nelle celle e rigenerare il PDF; controllare tutte le 30 pagine interessate prima di approvare il nuovo export.'),
 ('P12-03', 'pp. 120–123; sorgente M-SP01/07, righe 527–551', 'Apparati compilabili', 'grave', 'La «Scheda compilabile finale» concentra sei percorsi nelle due colonne «Dati essenziali» e «Verifica o azione». Le celle sono occupate dalle etichette dei percorsi e da «da compilare»; manca lo spazio per inserire i dati e le intestazioni non descrivono la suddivisione effettiva. La struttura è già presente nel Markdown.', 'Separare le schede per corpo e binario oppure fornire una scheda per singolo concorso, con campi vuoti ampi e intestazioni coerenti. L’eventuale versione digitale va indicata con un accesso concreto e verificato.'),
 ('P12-04', 'pp. 120, 174, 349 e 351', 'Usabilità su carta', 'medio', 'I campi vuoti per risposte, motivazioni, output trimestrali e controlli hanno spesso l’altezza di una sola riga tipografica. Lo spazio non è proporzionato alle informazioni richieste dalle istruzioni.', 'Aumentare l’altezza delle righe e riservare più spazio alle risposte aperte; provare la compilazione a mano nelle dimensioni finali.'),
 ('P12-05', 'p. 6, indice dei capitoli 1, 2, 4, 5 e 6; ricorrenze nel corpo', 'Navigazione', 'medio', 'L’indice ripete numeri di sezione per titoli diversi: per esempio 1.1 rimanda sia a p. 12 sia a p. 17, e 1.2 sia a p. 14 sia a p. 19. La duplicazione rispecchia la numerazione del testo e rende ambigui i rinvii.', 'Rinumerare le sezioni alla fonte e aggiornare indice e rinvii nello stesso export. Collegare questo rilievo al corrispondente rilievo testuale, senza contarne due volte la causa.'),
 ('P12-06', 'p. 11 e aperture successive', 'Gerarchia', 'lieve', 'Il titolo del capitolo viene ripetuto in nero e poi in rosso, separato dal nastro BANDO e dalla nota introduttiva, senza una diversa funzione dichiarata.', 'Conservare un solo titolo principale oppure distinguere chiaramente il secondo elemento come sottotitolo.'),
 ('P12-07', 'p. 124', 'Impaginazione', 'lieve', 'L’ultimo breve paragrafo dei riferimenti del capitolo 7 occupa da solo una pagina quasi vuota.', 'Valutare il recupero del paragrafo nella pagina precedente intervenendo sulla struttura delle schede, senza ridurre ulteriormente il corpo del testo.'),
 ('P12-08', 'p. 286, verifica del capitolo 19', 'Leggibilità dei quiz', 'medio', 'Le opzioni A, B, C e D sono impaginate nello stesso paragrafo continuo; la soluzione segue subito. La scansione delle alternative è faticosa rispetto alla struttura a righe separate utilizzata in altre verifiche del volume.', 'Mettere ciascuna alternativa su una riga distinta e separare visivamente domanda, opzioni e commento; uniformare il modello dei quiz nel volume.'),
]
findings = [dict(zip(['id','position','category','severity','description','proposal'], r), status='non applicato') for r in rows]
limitations = [
 'La copertura panoramica riguarda tutte le 459 pagine e consente il controllo di geometria e ritmo; non equivale alla lettura del testo minuto di ogni pagina rasterizzata.',
 'Il controllo grafico ingrandito e la lettura puntuale del PDF sono limitati alle dodici pagine elencate. La revisione integrale del testo originale è documentata separatamente dall’agente responsabile del volume.',
 'Nessuna prova cartacea, verifica cromatica, certificazione PDF/X o collaudo di tutti i collegamenti. Non controllate qui copertine e materiali commerciali esterni.',
 'Le metriche automatiche di supporto non segnalano oggetti testuali oltre il foglio, pagine bianche o caratteri sostitutivi; tali esiti non escludono difetti semantici, di leggibilità o di impaginazione.'
]
ledger = dict(volume='VOL-12', date='2026-10-02', pdf=pdf, sha256=sha, hashMatchesInventory=True, pages=459,
 contactSheetsViewed=contacts, contactCoverageComplete=True, detailPagesViewed=details, detailRenderScale=2,
 findings=findings, limitations=limitations,
 literalBrEvidence=dict(total=299,pages=[100,101,102,104,105,108,109,111,112,113,116,117,120,121,122,123,136,152,158,159,160,161,163,165,166,167,168,170,173,174],visuallyConfirmedPages=[102,120,123,174]))
Path('artifacts/review-integrale-2026-10-02/PDF-VOL-12-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines = [
 '# VOL-12 — Controllo visivo del PDF, 2 ottobre 2026', '',
 f'PDF: `{pdf}`. 459 pagine; SHA-256 `{sha}`. Hash coincidente con l’inventario: sì.', '',
 '## Copertura e metodo', '',
 'Scorse tutte le 459 pagine nelle 20 tavole panoramiche, 24 pagine per tavola salvo l’ultima. Non emergono tagli macroscopici, sovrapposizioni del corpo o pagine bianche alla scala osservata. Il volume termina a pagina 459 con il caso ragionato e la sintesi del capitolo 32.', '',
 'Ingrandite separatamente a scala 2 le pagine 6, 11, 102, 120, 123, 124, 174, 285, 286, 349, 351 e 459. I numeri riportati sono le pagine fisiche del PDF, coincidenti con la numerazione visibile. Applicata la skill PDF. Il conteggio dei tag stampati proviene dall’estrazione testuale del PDF ed è distinto dalla conferma visiva sui dettagli.', '',
 '## Rilievi', '',
 '| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |',
 '|---|---|---|---|---|---|---|'
]
for r in rows:
 lines.append('| '+' | '.join(s.replace('<br>', '`<br>`') for s in r)+' | Non applicato |')
lines += ['', '## Esito e limiti', '',
 'Richiesto un nuovo export dopo la correzione dei residui HTML e la revisione delle schede operative. I rilievi P12-03 e P12-05 documentano anche la resa in stampa di strutture presenti nel manoscritto: vanno collegati alla revisione testuale per evitare duplicazioni delle stesse cause. Nessun manoscritto o PDF è stato modificato.', '']
lines += ['- '+s for s in limitations]
lines += ['', 'Ledger di copertura: `artifacts/review-integrale-2026-10-02/PDF-VOL-12-ledger.json`. Le tavole esaminate sono in `artifacts/review-integrale-2026-10-02/pdf/VOL-12/vol-12-interior-kdp/`; i dettagli sono in `artifacts/review-integrale-2026-10-02/pdf/details-vol12/`.', '']
Path('wiki/reviews/audit-integrale-2026-10-02/PDF-VOL-12.md').write_text('\n'.join(lines),encoding='utf-8')
print(json.dumps(dict(pages=459,contacts=len(contacts),details=len(details),findings=len(findings),hashMatchesInventory=True)))
