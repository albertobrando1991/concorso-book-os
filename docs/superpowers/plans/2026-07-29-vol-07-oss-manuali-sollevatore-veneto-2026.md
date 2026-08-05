# VOL-07 OSS Manuali sollevatore e laboratori Veneto 2026 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rafforzare in ordine il primo blocker M-SA02 con manuali modello-specifici per sollevatore e imbragatura e con il programma regionale Veneto 2026, lasciando esplicitamente aperte procedura aziendale, review e prova pratica.

**Architecture:** I documenti ufficiali sono acquisiti nel corpus raw e registrati con byte e SHA-256. Una source note separa standard formativo regionale e istruzioni del produttore; la checklist riceve riferimenti puntuali per i controlli sul dispositivo, senza trasformarli in una procedura generale.

**Tech Stack:** PowerShell, `curl.exe`, PyPDF, Markdown wiki, JSON, CLI pipeline npm.

## Global Constraints

- Non modificare manualmente `pipeline/VOL-07/run-state.json`.
- Usare il prompt renderizzato dal CLI e mantenere il gate chiuso finché esiste una riga `parziale`.
- Conservare i PDF raw immutati e verificare pagine, testo, byte e SHA-256.
- Trattare i manuali come modello-specifici e non generalizzabili ad altri sollevatori o imbragature.
- Non dichiarare acquisita una procedura aziendale corrente se non è pubblicamente verificabile.
- Non autocertificare review professionale o prova pratica.

---

### Task 1: Acquisizione del lotto ufficiale

**Files:**
- Create: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-assistenza-generale/regione-veneto-guida-laboratori-oss-2026.pdf`
- Create: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-assistenza-generale/invacare-birdie-evo-manuale-uso-60135843-b.pdf`
- Create: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-assistenza-generale/invacare-imbracature-universal-manuale-60124419-d.pdf`
- Modify: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-assistenza-generale/download-log.json`

**Interfaces:**
- Consumes: PDF ufficiale Regione Veneto e manuali pubblicati dal produttore Invacare/DHCare.
- Produces: tre PDF auditabili e record `ASSIST-GEN-VENETO-11`, `ASSIST-GEN-LIFT-12`, `ASSIST-GEN-SLING-13`.

- [x] **Step 1: Verificare raggiungibilità e scaricare i PDF**

Run: `curl.exe -L` sui tre URL ufficiali con destinazioni esatte.

Expected: tre file con intestazione PDF e dimensione positiva.

- [x] **Step 2: Verificare contenuto e metadati**

Run: PyPDF per pagine, cifratura, testo e titoli; `Get-FileHash -Algorithm SHA256` per l'integrità.

Expected: documenti non cifrati e testualmente auditabili; manuali coerenti con Birdie EVO e imbracature Universal.

- [x] **Step 3: Aggiornare il download log**

Usare `apply_patch`, preservando i dieci record esistenti.

Expected: JSON valido con tredici record e corrispondenza completa file/byte/hash.

### Task 2: Consolidamento documentale

**Files:**
- Create: `wiki/sources/ausili-trasferimento-oss-manuali-dispositivo-veneto-2026.md`
- Modify: `wiki/sources/assistenza-generale-oss-pasto-mobilizzazione-eliminazione.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/06-checklist-igiene-letto-trasferimenti-review.md`

**Interfaces:**
- Consumes: i tre PDF verificati.
- Produces: una source note canonica e riferimenti puntuali `VEN-2026`, `BIRDIE-EVO`, `SLING-UNI`.

- [x] **Step 1: Scrivere la source note con limiti**

Descrivere corpus, copertura, uso editoriale e limiti, distinguendo formazione regionale da istruzioni tecniche del produttore.

Expected: nessuna generalizzazione nazionale, nessuna tecnica manuale autonoma e gap della procedura aziendale ancora esplicito.

- [x] **Step 2: Aggiornare nota generale e checklist**

Collegare i nuovi documenti ai controlli T14, T15 e C09 e aggiornare la mappa delle evidenze.

Expected: la checklist diventa più pronta per il revisore, ma conserva caselle vuote e stato `ready_for_review`.

### Task 3: Propagazione nella matrice e nell'audit

**Files:**
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/02-matrice-copertura-didattica.md`
- Modify: `wiki/reviews/pipeline/VOL-07/07-audit-corpus-tecnici-m-sa02.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/index.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/00-piano-editoriale.md`
- Modify: `wiki/index.md`

**Interfaces:**
- Consumes: source note e checklist aggiornate.
- Produces: copertura documentale aggiornata con stato ancora `parziale`.

- [x] **Step 1: Aggiornare SA02-01 e PRV-03**

Registrare manuali modello-specifici e laboratorio Veneto 2026; mantenere i blocker su procedura aziendale, revisore e prova pratica.

Expected: 0 righe `completo`, 8 righe `parziale`.

- [x] **Step 2: Aggiornare indici e conteggi audit**

Inserire la nuova source note e i conteggi effettivi del corpus.

Expected: collegamenti coerenti e nessuna duplicazione della source note generale.

### Task 4: Traccia e verifiche

**Files:**
- Modify: `wiki/log.md`
- Modify through `LocalAgentMemory`: `wiki/memory/agent/`

**Interfaces:**
- Consumes: lotto documentale consolidato.
- Produces: traccia append-only, memoria e verifica riproducibile.

- [x] **Step 1: Verificare corpus e software**

Run: verifica di tutti i download log M-SA02, `npm test`, `npm run typecheck`, `git diff --check`.

Expected: zero errori di integrità, 179 test verdi, typecheck e diff-check con exit 0.

- [x] **Step 2: Ricontrollare il gate**

Run: `npm run pipeline -- complete VOL-07 --step 07 --module M-SA02 --json`.

Expected: otto blocker `blocking-status`, nessun warning e nessuna accettazione manuale.

- [x] **Step 3: Registrare memoria e log**

Usare `LocalAgentMemory.captureConversation` e appendere al log l'esito con ID memoria.

Expected: traccia coerente che identifica procedura aziendale, review e prova pratica come gap ancora esterni.
