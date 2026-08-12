# VOL-08 Source-Ready Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Acquisire il dossier M-TR01, strutturare integralmente l’indice source-ready di VOL-08 e avviare il protocollo editoriale tramite il CLI della pipeline.

**Architecture:** Il dossier esterno entra come raw immutabile e viene consolidato in source/topic/entity notes prima di alimentare l’outline. Il volume commerciale vive in `wiki/books/volumi/`, mentre il modulo operativo vive in `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/`; il CLI possiede stato, ordine e gate.

**Tech Stack:** Markdown/Obsidian wiki, TypeScript pipeline CLI (`tsx`), Vitest, LocalAgentMemory, Git.

## Global Constraints

- `cut_off_date` è `2026-07-28`.
- Responsabile normativo ed editoriale: `Alberto Brando`.
- Provider: `codex`.
- Il volume è monomodulo: `VOL-08` contiene soltanto `M-TR01`.
- Non modificare manualmente `pipeline/VOL-08/run-state.json`.
- Non produrre testo finale direttamente dalla fonte raw.
- Non chiudere gate non automatizzati senza una verifica manuale reale e una nota esplicita.
- Non modificare né includere in commit il lavoro preesistente non correlato.

---

### Task 1: Ingest del dossier M-TR01

**Files:**
- Create: `wiki/raw/business/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08.txt`
- Create: `wiki/sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08.md`
- Modify: `wiki/index.md`
- Modify: `wiki/log.md`

**Interfaces:**
- Consumes: dossier esterno `C:\Users\aless\OneDrive\Desktop\VOLUMI LIBRO PROG\Modulo M-TR01 – ICT, digitale, cybe.txt`.
- Produces: source note canonica `sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08`.

- [ ] **Step 1: Copiare la fonte raw senza modificarne il contenuto**

Usare `Copy-Item -LiteralPath` sul percorso risolto tramite il prefisso `Modulo M-TR01*`.

- [ ] **Step 2: Verificare identità e integrità**

Confrontare lunghezza e hash SHA-256 tra file esterno e copia raw con `Get-FileHash`.

- [ ] **Step 3: Creare la source note consolidata**

La nota deve contenere frontmatter completo, `authority_level: media`, `review_required: true`, `raw_path`, sintesi del perimetro, indice proposto, fonti indicate, limiti del campione bandi e tutti i `[DA VERIFICARE]`.

- [ ] **Step 4: Aggiornare catalogo e log**

Aggiungere la source note a `wiki/index.md` e appendere a `wiki/log.md` un evento datato `2026-07-28`.

- [ ] **Step 5: Verificare l’ingest**

Run:

```powershell
rg -n "modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08|VOL-08|M-TR01" wiki/sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08.md wiki/index.md wiki/log.md
```

Expected: fonte, indice e log contengono riferimenti coerenti.

### Task 2: Consolidamento dei nodi di conoscenza

**Files:**
- Create: `wiki/topics/ict-digitale-cybersecurity-dati-concorsi-pa.md`
- Create: `wiki/entities/agenzia-cybersicurezza-nazionale.md`
- Modify: `wiki/index.md`

**Interfaces:**
- Consumes: source note della Task 1 e fonti consolidate già presenti.
- Produces: nodo tematico e nodo istituzionale collegabili da outline e capitoli.

- [ ] **Step 1: Inventariare topic/entity già esistenti**

Run:

```powershell
rg -n "cybersecurity|interoperabilit|intelligenza artificiale|Agenzia.*cybersicurezza|ACN" wiki/topics wiki/entities wiki/sources
```

Expected: elenco dei nodi riutilizzabili, senza creare duplicati canonici.

- [ ] **Step 2: Creare o integrare il topic canonico**

Registrare perimetro, nuclei, rinvii a VOL-01/VOL-09/VOL-10/VOL-11/VOL-12, fonti e capitoli VOL-08.

- [ ] **Step 3: Creare o integrare l’entity ACN**

Limitarsi a ruolo istituzionale e rilevanza editoriale verificabile; non trasformare i riferimenti non acquisiti in claim certi.

- [ ] **Step 4: Aggiornare l’indice**

Inserire soltanto i nuovi nodi effettivamente creati.

- [ ] **Step 5: Verificare i link**

Run:

```powershell
rg -n "\[\[(sources/modulo-m-tr01|topics/ict-digitale|entities/agenzia-cybersicurezza)" wiki/sources wiki/topics wiki/entities
```

Expected: collegamenti bidirezionali essenziali presenti.

### Task 3: Struttura commerciale VOL-08

**Files:**
- Create: `wiki/books/volumi/vol-08-ict-digitale-cybersecurity-dati/index.md`
- Create: `wiki/books/volumi/vol-08-ict-digitale-cybersecurity-dati/planning/00-scheda-pipeline.md`
- Create: `wiki/books/volumi/vol-08-ict-digitale-cybersecurity-dati/planning/01-indice-completo.md`
- Create: `wiki/books/volumi/vol-08-ict-digitale-cybersecurity-dati/planning/02-matrice-copertura-didattica.md`

**Interfaces:**
- Consumes: specifica approvata e source/topic/entity notes.
- Produces: definizione commerciale del volume e input univoco del CLI.

- [ ] **Step 1: Creare la master note del volume**

Dichiarare titolo, modulo unico, target, promessa, pacchetto verticale, esclusioni e rinvii.

- [ ] **Step 2: Creare l’indice completo**

Usare le cinque parti, i 13 capitoli e le sei appendici approvate, indicando per ciascuno obiettivo, nuclei, output e riferimenti consolidati.

- [ ] **Step 3: Creare la matrice di volume**

Mappare tutte le materie a collocazione, teoria, applicazione, verifica, fonte e stato iniziale. Usare `parziale` o `mancante` quando la fonte ufficiale non è ancora consolidata.

- [ ] **Step 4: Creare la scheda pipeline**

Frontmatter:

```yaml
type: pipeline_spec
volume_code: VOL-08
volume_title: ICT, digitale, cybersecurity e dati
cut_off_date: 2026-07-28
responsabile_normativo: Alberto Brando
responsabile_editoriale: Alberto Brando
writer_provider: codex
phases: [A, B, C, D, E, F, G]
status: draft
updated_at: 2026-07-28
review_required: true
```

Dichiarare `M-TR01 | moduli/m-tr01-ict-trasformazione-digitale | 1 | A,B,C,D,E,F,G` e tutti i capitoli in ordine esplicito.

- [ ] **Step 5: Verificare struttura e riferimenti**

Run:

```powershell
rg -n "VOL-08|M-TR01|chapters/13-|appendices/F-" wiki/books/volumi/vol-08-ict-digitale-cybersecurity-dati
```

Expected: scheda, indice e matrice concordano.

### Task 4: Scaffold editoriale M-TR01

**Files:**
- Modify: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/index.md`
- Move: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/00-piano-editoriale.md` to `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/planning/01-piano-editoriale.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/planning/02-matrice-copertura-didattica.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/front-matter/FM1-servizi-digitali.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/front-matter/FM2-frontespizio.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/front-matter/FM3-copyright-note.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/front-matter/FM4-sommario.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/front-matter/FM5-premessa.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/front-matter/FM6-indice.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/01-lavorare-ict-pa-ruoli-enti-prove.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/02-informatica-specialistica-oltre-vol-01.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/03-programmazione-algoritmi-strutture-dati.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/04-basi-dati-sql-nosql-qualita-dato.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/05-reti-sistemi-operativi-infrastrutture.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/06-ingegneria-software-api-interoperabilita-pa.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/07-cloud-pa-virtualizzazione-container-devops.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/08-cybersecurity-rischio-controlli-vulnerabilita.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/09-iam-crittografia-logging-incident-response.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/10-data-governance-open-data-interoperabilita.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/11-ai-ml-pa-rischi-compliance.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/12-procurement-ict-gestione-fornitori.md`
- Create: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/13-laboratorio-prove-ict.md`
- Create: six files under `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/appendices/`.

**Interfaces:**
- Consumes: indice e matrici della Task 3.
- Produces: target reali che il CLI può derivare e lavorare.

- [ ] **Step 1: Spostare il piano fuori da `chapters/`**

Usare `Move-Item` soltanto sul file esatto, dopo verifica dei percorsi risolti.

- [ ] **Step 2: Creare front matter canonico**

Impostare `front_matter_layout: analytical-index` e `index_detail: chapters-only`; nessuna doppia numerazione nei titoli.

- [ ] **Step 3: Creare le 13 note capitolo**

Ogni nota deve includere frontmatter completo, `outline_section`, specifica, nuclei, output, fonti consolidate, rinvii e note di review. Non scrivere ancora il corpo finale.

- [ ] **Step 4: Creare le sei appendici**

Usare frontmatter coerente con il `book_id` del modulo e dichiarare i limiti delle fonti.

- [ ] **Step 5: Aggiornare index e matrice modulo**

Portare `module_status` e `draft_stage` a `source-ready`; collegare tutti i target.

- [ ] **Step 6: Verificare conteggio e naming**

Run:

```powershell
(Get-ChildItem wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters -File).Count
(Get-ChildItem wiki/books/moduli/m-tr01-ict-trasformazione-digitale/appendices -File).Count
```

Expected: `13` capitoli e `6` appendici.

### Task 5: Inizializzazione e primo ciclo pipeline

**Files:**
- Create via CLI: `pipeline/VOL-08/run-state.json`
- Create via CLI: `artifacts/pipeline/VOL-08/**`
- Create/modify according to prompt: target e report indicati dal CLI.

**Interfaces:**
- Consumes: scheda pipeline e scaffold.
- Produces: run-state governato, prompt materializzati ed esiti dei gate.

- [ ] **Step 1: Eseguire doctor strutturato**

Run:

```powershell
npm run pipeline -- doctor --json
```

Expected: registrare ogni check non verde; non confondere problemi Git ambientali con errori editoriali.

- [ ] **Step 2: Inizializzare VOL-08**

Run:

```powershell
npm run pipeline -- init VOL-08 --json
```

Expected: `ok: true` e creazione del run-state.

- [ ] **Step 3: Leggere lo stato**

Run:

```powershell
npm run pipeline -- status VOL-08 --json
```

Expected: primo step disponibile e target corretti.

- [ ] **Step 4: Materializzare il primo prompt**

Run:

```powershell
npm run pipeline -- next VOL-08 --json
```

Leggere integralmente il `prompt.md` indicato.

- [ ] **Step 5: Eseguire il lavoro e il gate**

Produrre esattamente file e report richiesti dal contratto, quindi usare il comando `complete` restituito dal prompt con `--json`.

- [ ] **Step 6: Ripetere fino al primo blocco reale**

Continuare `status → next → work → complete`. Per i gate manuali, verificare concretamente e usare `--accept --note`; per mancanze normative o review umane non eseguibili, lasciare lo step bloccato e documentare la causa.

### Task 6: Verifica finale e memoria

**Files:**
- Modify via LocalAgentMemory: `wiki/memory/agent/`
- Modify: `wiki/log.md`

**Interfaces:**
- Consumes: esiti delle Task 1–5.
- Produces: evidenza verificabile e continuità agentica.

- [ ] **Step 1: Eseguire verifiche statiche**

Run:

```powershell
npm run typecheck
npm test
```

Expected: entrambi terminano con codice `0`, oppure i fallimenti preesistenti/non correlati sono separati con evidenza.

- [ ] **Step 2: Verificare diff e whitespace**

Run:

```powershell
git diff --check
git status --short
```

Expected: nessun errore di whitespace nei file VOL-08; modifiche preesistenti chiaramente separate.

- [ ] **Step 3: Catturare la conversazione in LocalAgentMemory**

Usare scope `VOL-08` e route `codex-vol08-source-ready-pipeline`, registrando ingest, architettura, stato pipeline, gate superati e blocchi reali.

- [ ] **Step 4: Appendere l’esito al log**

Non correggere eventi precedenti; aggiungere un evento conclusivo con file creati e stato effettivo.

- [ ] **Step 5: Riportare l’esito**

Indicare indice creato, posizione della fonte consolidata, stato JSON della pipeline, verifiche eseguite e qualsiasi intervento umano ancora necessario.
