# VOL-07 Emergenze ostetriche ItOSS Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ridurre il gap documentale M-SA02 sulle emergenze ostetriche con tre fonti ufficiali ItOSS, mantenendo chiuso il gate finché restano review e protocolli applicativi mancanti.

**Architecture:** I PDF ufficiali sono acquisiti nel corpus raw immutabile e registrati nel relativo `download-log.json`. Una source note separa contenuto documentato, impiego editoriale e limiti; matrice, audit e indici ricevono soltanto rinvii e stato aggiornato, senza produrre istruzioni cliniche esecutive.

**Tech Stack:** PowerShell, `curl.exe`, PDF.js/Node già presenti nel repository, Markdown wiki, JSON, CLI pipeline npm.

## Global Constraints

- Eseguire il protocollo tramite CLI; non modificare mai `pipeline/VOL-07/run-state.json`.
- Usare solo fonti ufficiali ISS/ItOSS con URL e metadati verificati.
- Conservare i PDF raw senza trasformazioni e registrare byte e SHA-256.
- Non autocertificare review cliniche o professionali e non trasformare i dossier in protocolli locali.
- Lasciare tutte le righe non complete come `parziale` e non avviare capitoli.

---

### Task 1: Acquisizione e integrità del corpus ItOSS

**Files:**
- Create: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-ostetrica/itoss-eclampsia-fact-sheet-2021.pdf`
- Create: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-ostetrica/itoss-sepsi-ostetricia-dossier-2018.pdf`
- Create: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-ostetrica/itoss-patologia-cardiaca-tromboembolica-gravidanza-puerperio.pdf`
- Modify: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-ostetrica/download-log.json`

**Interfaces:**
- Consumes: URL ufficiali EpiCentro/ItOSS già verificati.
- Produces: tre PDF integri e tre record `OST-ITOSS-10..12` con byte, SHA-256, autorità, URL e data di controllo.

- [x] **Step 1: Scaricare i tre PDF dagli URL ufficiali**

Run: tre invocazioni `curl.exe -L <url> -o <percorso-esatto>`.

Expected: tre file con dimensione maggiore di zero e intestazione `%PDF`.

- [x] **Step 2: Verificare pagine, cifratura e testo**

Run: parser PDF.js locale sugli esatti tre percorsi.

Expected: 1, 40 e 24 pagine; nessun errore di parsing; testo estraibile.

- [x] **Step 3: Calcolare metadati di integrità**

Run: `Get-Item` e `Get-FileHash -Algorithm SHA256` sui tre PDF.

Expected: byte positivi e tre digest SHA-256 distinti.

- [x] **Step 4: Registrare il delta nel download log**

Modificare `download-log.json` con `apply_patch`, preservando le nove voci esistenti.

Expected: JSON valido con 12 voci e corrispondenza completa file/byte/hash.

### Task 2: Source note clinico-editoriale

**Files:**
- Create: `wiki/sources/emergenze-ostetriche-eclampsia-sepsi-tromboembolia-itoss.md`

**Interfaces:**
- Consumes: i tre PDF verificati della Task 1 e le source note ostetriche già consolidate.
- Produces: una scheda canonica con corpus, copertura, uso editoriale, limiti e `review_required: true`.

- [x] **Step 1: Estrarre titoli, date, sezioni e messaggi pertinenti**

Run: estrazione testuale mirata dai PDF e ricerca di `eclampsia`, `sepsi`, `tromboembol`, `puerper`, `raccomand`.

Expected: evidenza sufficiente a distinguere fact sheet, dossier evidence-based e documento cardiaco/tromboembolico.

- [x] **Step 2: Scrivere la source note**

Usare `apply_patch` con frontmatter completo e sezioni `Corpus acquisito`, `Copertura utile`, `Uso editoriale`, `Limiti e cautele`, `Stato revisione`.

Expected: nessuna dose, sequenza o checklist clinica presentata come esecutiva; espliciti contesto storico, verifica di attualità e necessità di review professionale.

### Task 3: Propagazione controllata nella wiki

**Files:**
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/02-matrice-copertura-didattica.md`
- Modify: `wiki/reviews/pipeline/VOL-07/07-audit-corpus-tecnici-m-sa02.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/index.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/00-piano-editoriale.md`
- Modify: `wiki/index.md`

**Interfaces:**
- Consumes: source note canonica della Task 2.
- Produces: rinvii coerenti e conteggi aggiornati senza variazione del gate.

- [x] **Step 1: Aggiornare matrice e audit**

Inserire la source note nelle `source_refs`; aggiornare SA02-02/SA02-04/PRV-03 e i conteggi del corpus, mantenendo `parziale`.

Expected: il testo riconosce eclampsia, sepsi ostetrica e rischio tromboembolico, ma conserva i blocker su protocolli locali, attualità e review.

- [x] **Step 2: Aggiornare indici e piano editoriale**

Inserire il collegamento nella lista delle fonti e aggiornare il prossimo passo, senza avviare testo editoriale.

Expected: il nuovo nodo è raggiungibile da `wiki/index.md`, indice modulo e piano editoriale.

### Task 4: Traccia e verifica

**Files:**
- Modify: `wiki/log.md`
- Modify through `LocalAgentMemory`: `wiki/memory/agent/`

**Interfaces:**
- Consumes: delta documentale completo.
- Produces: traccia append-only, memoria locale e prova che la pipeline resta coerentemente bloccata.

- [x] **Step 1: Registrare il flusso**

Appendere a `wiki/log.md` un evento `knowledge_ingest` con numero documenti, pagine, fonti, conteggi e limiti; richiamare e poi registrare la memoria tramite `LocalAgentMemory`.

Expected: log append-only e identificativo della conversazione in memoria.

- [x] **Step 2: Verificare integrità editoriale e software**

Run: controllo di tutti i `download-log.json`, `npm test`, `npm run typecheck`, `git diff --check`.

Expected: nessun file mancante, byte/hash coerenti, test e typecheck verdi, nessun errore whitespace.

- [x] **Step 3: Ricontrollare il gate via CLI JSON**

Run: `npm run pipeline -- status VOL-07 --json` e `npm run pipeline -- complete VOL-07 --step 07 --module M-SA02 --json`.

Expected: otto righe ancora `parziale` e blocco `blocking-status`; nessuna accettazione manuale e nessuna modifica diretta del run-state.
