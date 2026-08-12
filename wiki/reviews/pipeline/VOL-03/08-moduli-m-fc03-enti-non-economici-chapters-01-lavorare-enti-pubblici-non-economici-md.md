---
volume: VOL-03
step: 08
module: M-FC03
chapter: 01
status: chapter_plan_ready
date: 2026-08-10
target: wiki/books/moduli/m-fc03-enti-non-economici/chapters/01-lavorare-enti-pubblici-non-economici.md
---

# Piano operativo — M-FC03, capitolo 01

## Diagnosi

Il capitolo è un `revised_draft` di circa 4.061 parole, già ricco di contenuti originali e strumenti workbook. Copre perimetro M-FC03, distinzione core/delta/profilo, enti guida, riconoscimento del bando, Decoder, checklist, caso, domande ed esercizio. L'intervento dello step 09 deve quindi essere conservativo: trasformare il testo nel formato 2, consolidare i confini e aggiungere la verifica mancante senza sostituire la voce dell'autore.

La matrice corrente `planning/01-matrice-copertura-materie.md` assegna al capitolo 01 l'ordinamento introduttivo e il perimetro EPNE, ma non usa ancora Nucleo ID stabili né il formato richiesto dal gate di copertura. Prima dello step 10 dovrà essere prodotta o riallineata la matrice canonica attesa in `planning/02-matrice-copertura-didattica.md`, mantenendo la matrice 01 come fonte storica e senza modificare manualmente il run-state.

## Nuclei assegnati e stato

| Nucleo ID | Nucleo assegnato | Stato attuale | Azione prevista |
| --- | --- | --- | --- |
| N-FC03-01-01 | Perimetro M-FC03 e criterio ente-profilo-materie | completo | Conservare apertura, obiettivi, tabella dentro/fuori e confini; organizzare il contenuto in un nucleo autonomo di almeno 600 parole. |
| N-FC03-01-02 | Core VOL-01, delta specialistico EPNE e profilo concreto | completo | Conservare il modello a tre strati; inserire soltanto rinvii VOL-01 precisi e verificati, senza duplicare la teoria base. |
| N-FC03-01-03 | Enti guida ed enti di orientamento | parziale | Conservare INPS/INAIL come enti guida; rendere esplicito che ACI, ENAC, ISTAT, ASI, ENEA, CONI e CRI richiedono verifica di natura, profilo e bando corrente. |
| N-FC03-01-04 | Riconoscere un bando M-FC03 | completo | Conservare le tre letture su fonte, profilo e prova; evitare di duplicare l'anatomia generale del bando e il Decoder completo del capitolo 10. |
| N-FC03-01-05 | Bando Decoder iniziale, rischi e checklist | completo | Conservare tabella Decoder, errori e checklist; distinguere dato stabile da informazione mobile e fonte/portale da ente che assume. |
| N-FC03-01-06 | Decisione operativa e verifica | parziale | Conservare caso, commissario, trappola, mini-esercizio e diario; aggiungere almeno sei quiz commentati e una verifica conclusiva coerente con il formato 2. |

## Nuclei già completi

- N-FC03-01-01: il testo spiega in modo operativo quando il modulo è pertinente e quando serve un altro percorso.
- N-FC03-01-02: il modello core/delta/profilo è già chiaro e coerente con la logica di copertura v4.
- N-FC03-01-04: le tre letture del bando producono decisioni concrete senza fissare prove o soglie mobili.
- N-FC03-01-05: Decoder, errori e checklist sono già utilizzabili come strumenti cartacei autonomi.

## Nuclei da sviluppare

1. Completare N-FC03-01-03 con una formula prudente sulla natura e sul perimetro corrente degli enti di orientamento, evitando classificazioni assolute fondate sul solo nome.
2. Completare N-FC03-01-06 con sei quiz commentati distribuiti su perimetro, core/delta, INPS-INAIL, enti di orientamento, fonte del bando e rinvio ad altro modulo.
3. Attribuire ai sei nuclei heading stabili e una checklist dimensionale nella matrice canonica.
4. Aggiungere `format_version: 2` e `dati_operativi: []` nel frontmatter, salvo che durante la scrittura emerga un vero dato operativo conforme alla policy.
5. Normalizzare il frontmatter: `source_refs` deve contenere soltanto source note; topic ed entity devono restare nei rispettivi campi.
6. Spostare `Riferimenti consolidati` e `Note di review` fuori dal corpo lettore, conservandone la tracciabilità nel frontmatter e nel report di pipeline.

## Sezioni da conservare

- Apertura editoriale, domanda guida e obiettivi.
- Istruzioni d'uso e Mappa BANDO.
- Tabella `Dentro o fuori`.
- Modello dei tre strati.
- Distinzione tra enti guida ed enti di orientamento.
- Tre letture del bando e Bando Decoder M-FC03.
- Checklist iniziale e finale.
- Caso guidato, domanda da commissario, domanda-trappola, errore tipico, mini-esercizio e diario errori.
- Formulazioni che ricordano di verificare bandi, portali, statuti e dati mobili sulle fonti ufficiali.

Le sezioni interne finali devono essere preservate come informazione editoriale ma rimosse dal corpo destinato allo studente.

## Duplicazioni da evitare

| Contenuto | Destinazione completa | Trattamento nel capitolo 01 |
| --- | --- | --- |
| Teoria generale del bando, requisiti, prove, punteggi e soglie | VOL-01, `anatomia-del-bando` | Solo applicazione ente-profilo-prova al perimetro EPNE. |
| Famiglie concorsuali e scelta del modulo | VOL-01, `famiglie-concorsi-pubblici` e `scegliere-moduli-integrativi` | Solo decisione M-FC03/altro modulo. |
| Ordinamento, governance, organi e controlli EPNE | Capitolo 02 M-FC03 | Solo mappa introduttiva e ragione del rinvio. |
| Previdenza e servizi INPS | Capitolo 03 e Appendice B | Solo funzione orientativa di INPS come ente guida. |
| Assicurazione, prevenzione e prestazioni INAIL | Capitolo 04 e Appendice B | Solo funzione orientativa di INAIL come ente guida. |
| Procedimenti, bilancio, PIAO, personale e contratti | Capitoli 05-09 | Solo elenco del delta specialistico. |
| Bando Decoder completo | Capitolo 10 | Nel capitolo 01 soltanto scheda iniziale di perimetro. |
| Casi, situazionali e piano 30/60/90 | Capitoli 11-13 | Un solo caso introduttivo e strumenti brevi. |
| Enti di orientamento e rinvii cross-family | Appendici C ed E | Solo criterio per decidere se restare nel modulo. |

## Esempi, casi, domande ed esercizi necessari

- Conservare il caso di un bando multi-profilo, richiedendo una decisione motivata tra M-FC03, M-IR03, M-TR01, M-TR02, M-FC02 e M-FC05.
- Conservare la domanda da commissario sulla differenza fra concorso EPNE e concorso amministrativo generico.
- Conservare la domanda-trappola: la pubblicazione su inPA o la gestione Formez non determinano da sole la famiglia.
- Rendere il mini-esercizio verificabile con cinque output: ente, profilo, prova dominante, delta specialistico e fonte ufficiale da monitorare.
- Aggiungere sei quiz commentati, ciascuno con risposta corretta e spiegazione dell'errore plausibile.
- Chiudere con una scheda compilabile che produca l'esito `M-FC03 principale / M-FC03 di contesto / altro modulo`.

## Fonti da usare

- `wiki/sources/m-fc03-dossier-redazionale-enti-pubblici-non-economici.md`: perimetro, confini, materie ad alta resa e regole di non duplicazione.
- `wiki/sources/m-fc03-fonti-ufficiali-enti-epne-2026.md`: canali istituzionali e uso prudente degli enti guida/orientamento.
- `wiki/sources/m-fc03-portali-bandi-concorsi-2023-2026.md`: distinzione fra campione redazionale, avviso ufficiale, allegati e comunicazioni successive.
- `wiki/topics/enti-pubblici-non-economici-concorsi.md` e `wiki/entities/inps-inail-epne.md`: sintesi di perimetro e rischi applicativi.
- Legge 20 marzo 1975, n. 70; D.Lgs. 30 giugno 1994, n. 479; legge 9 marzo 1989, n. 88; D.P.R. 30 giugno 1965, n. 1124; D.Lgs. 23 febbraio 2000, n. 38, esclusivamente attraverso source note consolidate e con verifica di vigenza nello step 15.
- VOL-01 con rinvii precisi a `famiglie-concorsi-pubblici#Famiglia 7 - Previdenza, lavoro e vigilanza`, `mappe-profilo-cosa-resta-comune-cosa-cambia#Mappa 7 - Previdenza, lavoro e vigilanza`, `scegliere-moduli-integrativi#Esempio A — Candidato INPS / INAIL` e `anatomia-del-bando#Il Bando Decoder`.

Non usare `wiki/raw/` per la scrittura finale e non trasformare il campione 2023-2026 in frequenze statistiche o regole universali.

## Audit specialistici richiesti

1. Verifica normativa della vigenza e dell'uso introduttivo delle fonti su EPNE, INPS e INAIL.
2. Verifica istituzionale della natura e del perimetro corrente di ACI, ENAC, ISTAT, ASI, ENEA, CONI e CRI prima di formule classificatorie.
3. Verifica bandi: ente, profilo, prove, materie, allegati e avvisi devono provenire dall'atto ufficiale corrente; nessun dato del campione va stabilizzato senza source note dedicata.
4. Verifica contrattuale ARAN per CCNL Funzioni Centrali, aree e profili, rinviando il dettaglio al capitolo 08.
5. Audit dei dati operativi: il capitolo non deve contenere posti, scadenze, punteggi, soglie o calendari senza fonte, ambito, versione e data.
6. Verifica dei rinvii VOL-01 e cross-family, tutti con file e heading esistenti.

## Struttura H1/H2/H3 proposta

1. `# Lavorare negli enti pubblici non economici`
2. `## Apertura editoriale`
3. `## Obiettivo e Mappa BANDO`
4. `## N-FC03-01-01 · Perimetro M-FC03 e confini`
   - `### Quando il modulo è principale`
   - `### Quando è solo contesto`
   - `### Quando serve un altro modulo`
5. `## N-FC03-01-02 · Core, delta EPNE e profilo concreto`
   - `### Core VOL-01`
   - `### Delta specialistico`
   - `### Profilo e prova dominante`
6. `## N-FC03-01-03 · Enti guida ed enti di orientamento`
   - `### INPS`
   - `### INAIL`
   - `### Altri enti: criterio prudente`
7. `## N-FC03-01-04 · Riconoscere un bando M-FC03`
   - `### Fonte ed ente che assume`
   - `### Profilo e area`
   - `### Prova che seleziona davvero`
8. `## N-FC03-01-05 · Decoder, rischi e checklist iniziale`
   - `### Bando Decoder M-FC03`
   - `### Errori di perimetro`
   - `### Checklist di attivazione`
9. `## N-FC03-01-06 · Dalla classificazione alla decisione operativa`
   - `### Caso guidato`
   - `### Domanda, trappola ed esercizio`
   - `### Diario e decisione finale`
10. `## ▣ Verifica - perimetro e attivazione del modulo`
    - `### Sei quiz commentati`
    - `### Caso ragionato conclusivo`
    - `### Checklist finale`

I sei nuclei formano un unico blocco di verifica, rispettando la soglia di 5-7 nuclei prevista dal formato 2.

## Budget parole, quiz e casi

La scheda pipeline non dichiara soglie personalizzate per il capitolo 01; valgono quindi i default del formato 2: almeno 3.000 parole, almeno cinque nuclei da 600 parole, almeno sei quiz e almeno un caso applicativo. Il testo corrente è già sopra la soglia complessiva, ma la densità deve essere verificata per singolo nucleo dopo il retrofit.

| Blocco | Budget parole | Quiz | Casi/esercizi |
| --- | ---: | ---: | ---: |
| Apertura, obiettivo e Mappa BANDO | 350-450 | 0 | 0 |
| N-FC03-01-01 | 650-750 | 1 | tabella perimetro |
| N-FC03-01-02 | 650-750 | 1 | mappa core/delta/profilo |
| N-FC03-01-03 | 650-750 | 1 | confronto INPS/INAIL/altro ente |
| N-FC03-01-04 | 650-750 | 1 | lettura guidata di bando anonimo |
| N-FC03-01-05 | 650-750 | 1 | Decoder e checklist |
| N-FC03-01-06 e verifica | 800-950 | 1 | un caso ragionato, domanda, trappola, mini-esercizio e diario |
| **Totale previsto** | **4.400-5.100** | **almeno 6** | **almeno 1 caso + 3 strumenti** |

## Criterio di completamento dello step 09

Il capitolo sarà completabile quando dichiarerà `format_version: 2`; i sei nuclei avranno ID stabili, almeno 600 parole e copertura nella matrice canonica; saranno presenti almeno sei quiz commentati e un caso ragionato; tutti i rinvii saranno precisi; il corpo non conterrà artefatti editoriali interni; i contenuti originali utili saranno preservati; nessun dato mobile sarà presentato come regola stabile.
