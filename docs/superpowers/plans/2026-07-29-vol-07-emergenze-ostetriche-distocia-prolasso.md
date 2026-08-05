# VOL-07 Emergenze ostetriche: distocia e prolasso Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ridurre il terzo blocker ad alta priorità di M-SA02 acquisendo campioni italiani auditabili su distocia di spalla e prolasso di funicolo, senza presentarli come linee guida nazionali correnti.

**Architecture:** Quattro PDF ufficiali entrano nel corpus raw con hash e metadati: una pratica regionale, due procedure aziendali e un piano formativo 2026. Una source note separata ne descrive copertura e limiti; matrice e audit restano `parziale` finché mancano verifica di attualità, protocollo del setting e review clinica indipendente.

**Tech Stack:** PowerShell, `curl.exe`, PyPDF, Markdown wiki, JSON, CLI pipeline npm, LocalAgentMemory.

## Global Constraints

- Non modificare manualmente `pipeline/VOL-07/run-state.json`.
- Conservare i PDF raw immutati dopo l'acquisizione.
- Registrare URL, byte e SHA-256 nel download log ostetrico.
- Non generalizzare procedure ASL VCO o Regione Toscana ad altri setting o all'intero territorio nazionale.
- Non trasformare algoritmi e manovre in istruzioni esecutive per il lettore.
- Non autocertificare attualità clinica, competenza professionale o prova su simulatore.
- Mantenere il gate chiuso finché esiste una riga `parziale`.

---

### Task 1: Acquisizione e verifica del lotto ufficiale

**Files:**
- Create: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-ostetrica/regione-toscana-pratica-distocia-spalla-v2-2-2018.pdf`
- Create: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-ostetrica/asl-vco-procedura-distocia-spalla-rev2020.pdf`
- Create: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-ostetrica/asl-vco-procedura-prolasso-funicolo.pdf`
- Create: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-ostetrica/asufc-piano-formazione-2026-distocia-stam-sten.pdf`
- Modify: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-ostetrica/download-log.json`

**Interfaces:**
- Consumes: PDF pubblicati da Regione Toscana, ASL VCO e Azienda Sanitaria Universitaria Friuli Centrale.
- Produces: record `OST-REG-13`, `OST-ASL-14`, `OST-ASL-15`, `OST-FOR-16` con integrità verificabile.

- [x] **Step 1: Scaricare i quattro PDF dagli URL ufficiali**

Run: `curl.exe -L` verso i quattro percorsi raw esatti.

Expected: quattro file con intestazione PDF e dimensione positiva.

- [x] **Step 2: Verificare pagine, cifratura, testo e revisione dichiarata**

Run: PyPDF sui quattro file e `Get-FileHash -Algorithm SHA256`.

Expected: PDF non cifrati e auditabili; le date/versioni sono riportate come dichiarate nei documenti, senza deduzioni.

- [x] **Step 3: Aggiornare il download log preservando i dodici record esistenti**

Run: patch JSON e parsing con `ConvertFrom-Json`.

Expected: sedici record, file/byte/hash coerenti e JSON valido.

### Task 2: Consolidamento e limiti d'uso

**Files:**
- Create: `wiki/sources/emergenze-ostetriche-distocia-spalla-prolasso-funicolo-protocolli-italiani.md`
- Modify: `wiki/sources/emergenze-ostetriche-eclampsia-sepsi-tromboembolia-itoss.md`

**Interfaces:**
- Consumes: quattro PDF verificati.
- Produces: source note canonica che distingue pratica regionale, procedura aziendale e formazione corrente.

- [x] **Step 1: Scrivere la source note con copertura e cautele**

Documentare riconoscimento, attivazione del team, comunicazione, registrazione, simulazione e confini professionali solo a livello descrittivo.

Expected: nessuna dose, manovra o sequenza presentata come istruzione autonoma; gap di attualità e setting espliciti.

- [x] **Step 2: Collegare il nuovo corpus alla nota ItOSS esistente**

Expected: il lotto completa due emergenze residue ma non sostituisce linee guida correnti, protocolli locali o review clinica.

### Task 3: Propagazione nella copertura M-SA02

**Files:**
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/02-matrice-copertura-didattica.md`
- Modify: `wiki/reviews/pipeline/VOL-07/07-audit-corpus-tecnici-m-sa02.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/index.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/00-piano-editoriale.md`
- Modify: `wiki/index.md`

**Interfaces:**
- Consumes: source note consolidata.
- Produces: matrice e audit aggiornati con stato ancora `parziale`.

- [x] **Step 1: Aggiornare le righe clinica, discipline specifiche e prova pratica**

Expected: distocia di spalla e prolasso di funicolo risultano documentati come campioni italiani; restano review, attualità e setting.

- [x] **Step 2: Aggiornare blocker, indici e conteggi audit effettivi**

Expected: 0 righe `completo`, 8 `parziale`; conteggi derivati dal corpus e non stimati.

### Task 4: Verifica, gate e memoria

**Files:**
- Modify: `wiki/log.md`
- Modify through `LocalAgentMemory`: `wiki/memory/agent/`

**Interfaces:**
- Consumes: lotto documentale consolidato.
- Produces: traccia append-only, memoria e gate riproducibile.

- [x] **Step 1: Verificare integrità del corpus e software**

Run: audit di tutti i download log M-SA02, `npm test`, `npm run typecheck`, `git diff --check`.

Expected: zero errori di integrità, 179 test verdi, typecheck e diff-check con exit 0.

- [x] **Step 2: Eseguire il gate CLI senza forzature**

Run: `npm run pipeline -- complete VOL-07 --step 07 --module M-SA02 --json`.

Expected: otto blocker `blocking-status`, nessun warning, step nuovamente `blocked`.

- [x] **Step 3: Registrare memoria, log e completamento del piano**

Expected: nuova conversazione LocalAgentMemory e log con documenti, pagine, conteggi, test e residui esterni.
