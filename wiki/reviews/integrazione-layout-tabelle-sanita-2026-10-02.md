# Layout tabelle sanità — 2 ottobre 2026

## Filosofia visiva: Continuità leggibile

La gabbia resta quella del paperback editoriale: una colonna, margini esistenti e spazio sufficiente per leggere e compilare. La divisione delle tabelle restituisce spazio alle celle senza ridurre il corpo tipografico. La cura del lavoro riguarda soprattutto la conservazione esatta dei rapporti tra intestazioni, righe e contenuti.

Colore, materiali e font restano invariati: nessun nuovo accento grafico, nessuna riduzione di Garamond o Arial. La soluzione lavora sulla forma delle tabelle Markdown e si affida al renderer condiviso. L'attenzione artigianale è rivolta alla precisione del raccordo, non alla decorazione.

Il ritmo procede per blocchi brevi di due o tre colonne. La prima colonna ripete la stessa chiave, così il lettore ritrova senza ambiguità la medesima voce nella griglia seguente. Le denominazioni non vengono abbreviate; dati e risposte non vengono condensati.

La gerarchia visiva separa confronto, calcolo e interpretazione, conservando l'ordine dei contenuti originari. Le didascalie di blocco restano brevi e non introducono nuovi nuclei o norme. Il controllo finale deve unire confronto meticoloso delle celle e verifica visiva del PDF: la sola riduzione del numero di colonne non prova la riuscita dell'impaginazione.

## Perimetro

Ownership: soltanto capitoli M-SA01 04 e 09; nessun cambiamento a norme, casi, soluzioni, font, rinvii o heading esistenti. Il coordinatore aggiorna gli hash del freeze dopo i controlli. Il collega audit_pipeline verifica la preview DOM; non è prevista la produzione di un PDF in questo turno e il controllo PDF resta pendente.

## Interventi effettuati

| Capitolo e tabella | Prima | Dopo |
| --- | --- | --- |
| 04 — Livello / Funzione prevalente / Esempio di fonte / Limite da ricordare | 4 colonne, 3 righe | Funzioni e fonti: 3 colonne; Limiti per livello: 2 colonne |
| 09 — Mappa BANDO | 4 colonne, 5 righe | Domande e parole chiave: 3; Output da prova: 2 |
| 09 — Strumenti contabili | 5 colonne, 5 righe | Oggetto e funzione: 3; Destinatari e limiti: 3 |
| 09 — Sigla o documento | 4 colonne, 5 righe | Oggetto e momento: 3; Domande utili: 2 |
| 09 — Indicatori del caso guidato | 5 colonne, 3 righe | Valori di confronto: 3; Scostamenti: 3 |
| 09 — Ipotesi, evidenze, esiti e azioni | 4 colonne, 5 righe | Evidenze ed esiti: 3; Azioni condizionate: 2 |
| 09 — Laboratorio da foglio di calcolo | 8 colonne, 4 righe | Dati: 3; Calcoli: 3; Cause e controlli: 3; Azioni possibili: 2 |

Ogni blocco ripete integralmente la chiave della riga. Le nuove etichette sono didascalie in grassetto, non heading: nessun ancoraggio esistente cambia. Le colonne numeriche conservano l'allineamento a destra. Il laboratorio mantiene tutti i campi vuoti compilabili e tutte le istruzioni e soluzioni originali.

## Verifiche di conservazione

Confronto automatico tra snapshot in memoria acquisito immediatamente prima della patch e testo successivo. Per ogni tabella originaria sono state costruite le tuple `(chiave di riga, intestazione, contenuto della cella)`, confrontate con le tuple delle tabelle suddivise. Ogni intestazione e ogni contenuto, incluse celle vuote, numeri, segni, percentuali e denominazioni, rimane associato alla stessa chiave.

- Capitolo 04: 9/9 tuple identiche.
- Capitolo 09: 105/105 tuple identiche (15 Mappa, 20 strumenti, 15 modelli, 12 indicatori, 15 ipotesi, 28 laboratorio).
- Totale: 114/114 tuple conservate, nessuna perdita o associazione modificata.
- La ricostruzione attesa dal testo precedente mediante le sole sette sostituzioni tabellari coincide esattamente col testo successivo.
- Frontmatter byte-identico, heading e loro ordine identici. Nessun testo fuori dalle tabelle modificato. Aggiunte soltanto le didascalie, oltre alla ripetizione delle chiavi e delle intestazioni necessaria alla divisione.
- Zero righe tabellari oltre tre colonne in entrambi i capitoli.

La lettura e la seconda passata sulle griglie non hanno richiesto interventi sostanziali. Stato text_frozen, review_required e fonte di compilazione sono rimasti invariati come richiesto. Nessun nuovo audit normativo dedotto dal lavoro tipografico.

## Lint, rinvii e test

Eseguite direttamente le funzioni pure di controllo, senza CLI e senza scrivere report condivisi:

- `runChapterLintGate`, legacy (`requireFormatVersion2:false`): passed=true, zero blocker e warning per entrambi.
- `runVerifiedReferralGate`: passed=true, zero blocker e warning per entrambi. Il controllo automatico riguarda i wikilink riconosciuti; i rinvii in prosa e gli heading sono rimasti identici, non si attribuisce al gate una verifica ulteriore del loro contenuto.
- `npm test -- tests/pipeline/vol-07-m-sa01-corpus.test.ts -t "resolves every declared chapter matrix"`: 1 test passato, 3 non selezionati.
- `git diff --check` sui due capitoli: nessuna anomalia.

## Identificazione e passaggio al renderer

| File | SHA-256 precedente nel manifest16 | SHA-256 dopo la suddivisione |
| --- | --- | --- |
| Capitolo 04 | `1b54fe0bf0bfb3c1dea69c628987d66883dd5f60f1858c85b752b0ad36320215` | `d60498e040922b51ee29eb29dcea2cc5138f29ec484d3359e5e4b47a7e60a94f` |
| Capitolo 09 | `628883f2c2b67ca00abb66eb3a9bd74d7e9ce663e913fc9cbaee7416a4074a5d` | `ef6c8325b44eb325af173e07786e2f524e7a69f4e93e6f858aed8a8f0232a2e5` |

Avvisato audit_pipeline sia prima delle modifiche sia al rilascio dei file per il nuovo controllo della preview DOM. La prova visiva su PDF, compresi spazi bianchi, salti, margini e leggibilità delle nuove griglie, resta pendente e non è svolta in questo turno. Non si dichiara il PDF pronto sulla base dei controlli testuali o della preview DOM. Il coordinatore aggiorna il manifest; questo agente non modifica pipeline, matrice, indice, report condivisi o memoria.

## Addendum del coordinatore — etichetta orfana

La successiva ispezione della preview ha rilevato «Evidenze ed esiti» in fondo a pagina98, separata dalla tabella in99. Convertite soltanto questa etichetta e «Azioni condizionate» in sottotitoli Markdown H4, sotto l'H3 «Cause da verificare e controlli», affinché il renderer applichi la protezione del titolo. Il testo delle etichette e tutte le celle restano identici; i precedenti heading non cambiano, si aggiungono questi due sottotitoli. Il controllo di conservazione sopra documentato resta riferito alla prima divisione.

Nuovi lint e rinvii: passed, zero blocker/warning. Hash definitivo cap09 dopo questa seconda correzione tipografica: `acbb8642654bc16160e9759bceb46d79be98380959df4a79dab584a2b5486fa8`. Richiesta nuova verifica della preview; non si attesta una verifica PDF.

Riesecuzione conclusa: sulle nuove pagine98–99 i due sottotitoli sono uniti alle rispettive tabelle, senza etichette orfane. Evidenze e limiti in [[reviews/integrazione-layout-verifica-preview-2026-10-02]].
