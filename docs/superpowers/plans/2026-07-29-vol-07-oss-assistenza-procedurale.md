# VOL-07 OSS Assistenza Procedurale Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ridurre il blocker M-SA02 su bagno completo a letto e trasferimenti acquisendo fonti istituzionali italiane, consolidandole nel wiki e predisponendo checklist di pianificazione da sottoporre a review professionale.

**Architecture:** Il ciclo conserva i documenti immutabili nel corpus raw, registra URL, byte e SHA-256 nel log di acquisizione, consolida solo quanto effettivamente documentato nella source note esistente e mantiene la procedura in un artefatto di planning non canonico. Matrice e gate restano aderenti all'evidenza: nessuna checklist è dichiarata validata senza revisore professionale.

**Tech Stack:** Markdown/YAML del wiki, JSON per il registro raw, PowerShell/curl per acquisizione, Poppler `pdfinfo`/`pdftotext` per audit, CLI pipeline TypeScript, Vitest.

## Global Constraints

- Rispettare `wiki/AGENTS.md` e usare `LocalAgentMemory` prima e dopo il ciclo.
- Usare esclusivamente fonti istituzionali italiane o documenti ufficiali di enti sanitari pubblici.
- Non modificare documenti già presenti in `wiki/raw/`.
- Non trasformare una procedura aziendale o regionale in protocollo nazionale.
- Non dichiarare completa la riga Infermiere/OSS senza review professionale indipendente.
- Non avviare capitoli mentre lo step 07 è bloccato.

---

### Task 1: Selezione delle fonti procedurali

**Files:**
- Read: `wiki/sources/assistenza-generale-oss-pasto-mobilizzazione-eliminazione.md`
- Read: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-assistenza-generale/download-log.json`
- Read: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/02-matrice-copertura-didattica.md`

**Interfaces:**
- Consumes: gap documentali “bagno completo a letto” e “sequenze di trasferimento”.
- Produces: elenco di PDF istituzionali con URL diretto, ente, data e copertura verificata.

- [x] **Step 1:** Cercare sui domini di Regioni, ASL, AO, IRCCS pubblici, università sanitarie pubbliche e INAIL documenti che descrivano sequenze operative di igiene completa a letto o trasferimento letto-carrozzina.
- [x] **Step 2:** Aprire i risultati e scartare dispense private, aggregatori, copie senza provenienza e documenti che citano soltanto il titolo della procedura.
- [x] **Step 3:** Preferire documenti datati o versionati, con ente emittente identificabile e contenuto testuale auditabile.
- [x] **Step 4:** Registrare per ogni candidato la copertura effettiva: preparazione, valutazione della persona, ausili, ergonomia, sequenza, sicurezza, privacy, osservazione e riordino.

### Task 2: Acquisizione e audit del corpus

**Files:**
- Create: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-assistenza-generale/<slug-fonte>.pdf`
- Modify: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-assistenza-generale/download-log.json`

**Interfaces:**
- Consumes: URL diretti selezionati nella Task 1.
- Produces: PDF locali immutabili e record JSON con `id`, `file`, `bytes`, `sha256`, `authority`, `url`, `checked_at`.

- [x] **Step 1:** Scaricare ogni PDF selezionato con `curl.exe -L` nella cartella raw esistente.
- [x] **Step 2:** Verificare firma PDF, numero di pagine e presenza di testo con `pdfinfo` e `pdftotext`.
- [x] **Step 3:** Calcolare byte e SHA-256 con gli strumenti nativi di PowerShell.
- [x] **Step 4:** Aggiungere al `download-log.json` soltanto record relativi a file effettivamente verificati.
- [x] **Step 5:** Rileggere il JSON completo e verificare che ogni file registrato esista e corrisponda a byte e hash.

### Task 3: Consolidamento della conoscenza

**Files:**
- Modify: `wiki/sources/assistenza-generale-oss-pasto-mobilizzazione-eliminazione.md`
- Create: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/06-checklist-igiene-letto-trasferimenti-review.md`

**Interfaces:**
- Consumes: documenti raw verificati e limiti di generalizzabilità.
- Produces: source note consolidata e checklist di planning tracciabile.

- [x] **Step 1:** Aggiornare la sezione documenti acquisiti con ente, titolo, data e pagine dei nuovi PDF.
- [x] **Step 2:** Descrivere nella source note solo elementi rintracciabili nei documenti, distinguendo indicazioni comuni e specificità locali.
- [x] **Step 3:** Creare una checklist non canonica separata per igiene completa a letto e trasferimento letto-carrozzina.
- [x] **Step 4:** Per ogni passaggio indicare fonte, prerequisiti, rischi, limite professionale e campo vuoto per l'esito del revisore.
- [x] **Step 5:** Marcare esplicitamente la checklist come non esecutiva e non pubblicabile finché manca review professionale.

### Task 4: Collegamenti e stato del gate

**Files:**
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/02-matrice-copertura-didattica.md`
- Modify: `wiki/reviews/pipeline/VOL-07/07-audit-corpus-tecnici-m-sa02.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/index.md`
- Modify: `wiki/index.md`
- Modify: `wiki/log.md`
- Modify: `wiki/memory/agent/` tramite `LocalAgentMemory`

**Interfaces:**
- Consumes: source note e checklist della Task 3.
- Produces: tracciabilità completa senza chiusura impropria della riga.

- [x] **Step 1:** Collegare la nuova checklist da source note, indice del modulo e indice generale.
- [x] **Step 2:** Aggiornare la riga Infermiere/OSS descrivendo il delta reale e mantenendo `parziale` se la review non è svolta.
- [x] **Step 3:** Aggiornare l'audit con conteggi documentali ricalcolati e limiti residui.
- [x] **Step 4:** Appendere un evento a `wiki/log.md` senza modificare gli eventi precedenti.
- [x] **Step 5:** Catturare risultato e decisione nello store `LocalAgentMemory` con scope `VOL-07/M-SA02`.

### Task 5: Verifica conclusiva

**Files:**
- Test: `tests/**/*.test.ts`
- Verify: `pipeline/VOL-07/run-state.json` esclusivamente tramite CLI.

**Interfaces:**
- Consumes: tutti gli artefatti delle Task 1-4.
- Produces: evidenza riproducibile di integrità e stato reale.

- [x] **Step 1:** Eseguire `npm test` e richiedere 179 test superati o il nuovo totale completo senza fallimenti.
- [x] **Step 2:** Eseguire `npm run typecheck` e richiedere exit code 0.
- [x] **Step 3:** Eseguire `git diff --check` e controllare link locali, frontmatter e JSON.
- [x] **Step 4:** Eseguire `npm run pipeline -- status VOL-07 --json` e registrare il numero reale di blocker.
- [x] **Step 5:** Confrontare i risultati con questo piano e dichiarare separatamente ciò che è consolidato e ciò che resta soggetto a review.
