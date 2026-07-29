# VOL-03 Capitolo 2 - Bando Decoder specialistico Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Creare il secondo capitolo di VOL-03 come Bando Decoder specialistico condiviso tra M-FC02 e M-FC03, derivato dal wiki consolidato e completo di tre casi e scheda compilabile.

**Architecture:** Il nuovo capitolo sarà un file autonomo nella cartella `chapters/` del volume. Riutilizzerà selettivamente il Decoder fiscale esistente, integrandolo con le fonti consolidate previdenziali, ispettive ed EPNE; VOL-01 resterà il riferimento per il metodo generale e le materie comuni.

**Tech Stack:** Markdown Obsidian, frontmatter YAML, knowledge base ConcorsoBook OS, renderer A4 condiviso, controlli PowerShell/`rg`, test npm del repository.

## Global Constraints

- Non leggere o citare direttamente `wiki/raw/` nella redazione finale.
- Scrivere esclusivamente dentro `wiki/books/` per il prodotto editoriale.
- Conservare il precedente capitolo M-FC02 senza sovrascriverlo.
- Applicare il principio delta rispetto a VOL-01.
- Usare esempi dichiaratamente didattici senza attribuire dati inventati a bandi reali.
- Mantenere gerarchia H1/H2/H3 e tabelle compatibili con il master A4.
- Tracciare i claim importanti con link a source notes, topic ed entity pages consolidate.

---

### Task 1: Preparare il capitolo e la matrice delle fonti

**Files:**
- Create: `wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/chapters/02-bando-decoder-specialistico.md`
- Read: `wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/planning/02-indice-analitico-ricostruito-2026.md`
- Read: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/02-bando-decoder-fiscale.md`
- Read: `wiki/books/moduli/m-fc03-enti-non-economici/chapters/10-bando-decoder-epne.md`
- Read: `wiki/sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026.md`
- Read: `wiki/sources/m-fc03-bando-ripam-inail-308-funzionari-assistenti-sociali-2024.md`
- Read: `wiki/sources/m-fc03-inl-vigilanza-lavoro-previdenziale.md`
- Read: `wiki/sources/m-fc03-portali-bandi-concorsi-2023-2026.md`
- Read: `wiki/sources/vol-03-fonti-specialistiche-fisco-dogane-previdenza-ispettivo.md`
- Read: `wiki/sources/logica-volumi-copertura-concorsobook-v4.md`

**Interfaces:**
- Consumes: indice approvato, source notes e capitoli preesistenti.
- Produces: frontmatter valido e sezione `Specifica struttura madre` del nuovo capitolo.

- [ ] **Step 1: Verificare l'esistenza di tutte le fonti previste**

Run:

```powershell
$paths = @(
  'wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/02-bando-decoder-fiscale.md',
  'wiki/books/moduli/m-fc03-enti-non-economici/chapters/10-bando-decoder-epne.md',
  'wiki/sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026.md',
  'wiki/sources/m-fc03-bando-ripam-inail-308-funzionari-assistenti-sociali-2024.md',
  'wiki/sources/m-fc03-inl-vigilanza-lavoro-previdenziale.md',
  'wiki/sources/m-fc03-portali-bandi-concorsi-2023-2026.md'
)
$paths | ForEach-Object { "$(Test-Path $_) $_" }
```

Expected: ogni riga inizia con `True`.

- [ ] **Step 2: Creare frontmatter e specifica editoriale**

Il file deve iniziare con `id: chapter-vol-03-bando-decoder-specialistico`, `book_id: vol-03-fisco-dogane-previdenza-ispettivo`, `outline_section: 2`, `module_codes: ["M-FC02", "M-FC03"]`, `draft_stage: professional-draft`, `review_required: true` e riferimenti alle source notes elencate.

- [ ] **Step 3: Verificare i campi obbligatori**

Run:

```powershell
rg -n "^(id|type|title|status|source_refs|book_id|outline_section|draft_stage|module_codes|last_compiled_from):" 'wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/chapters/02-bando-decoder-specialistico.md'
```

Expected: tutti gli undici campi risultano presenti.

### Task 2: Redigere il nucleo metodologico e lo strumento compilabile

**Files:**
- Modify: `wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/chapters/02-bando-decoder-specialistico.md`

**Interfaces:**
- Consumes: frontmatter e riferimenti consolidati della Task 1.
- Produces: apertura, obiettivo, mappa BANDO, metodo di lettura e scheda `profilo-materie-output-fonti`.

- [ ] **Step 1: Scrivere apertura e raccordo con VOL-01**

Il testo deve chiarire che il Decoder generale individua vincoli e struttura del concorso, mentre questo capitolo misura il delta specialistico e converte il programma in profondità, priorità e output.

- [ ] **Step 2: Sviluppare i quattro livelli documentali**

Inserire sezioni distinte per avviso, allegati, codice profilo e comunicazioni successive, specificando quale decisione può essere presa e quale dato resta da verificare.

- [ ] **Step 3: Sviluppare verbi, profondità, frequenza e materie-soglia**

Includere una tabella leggibile A4 che distingua almeno `conoscere`, `applicare`, `analizzare/valutare` e `redigere/risolvere`, precisando che il verbo è un indizio da interpretare con profilo e prova.

- [ ] **Step 4: Collegare ogni prova a un output**

Mappare quiz, risposta sintetica, orale, caso teorico-pratico e quesito situazionale rispettivamente a esercizi a tempo, scalette, esposizioni 60/120/180 secondi, griglie fatto-norma-decisione e gerarchie comportamentali.

- [ ] **Step 5: Inserire la scheda compilabile**

La scheda deve contenere campi vuoti per `Profilo`, `Materie`, `Output`, `Fonti`, più le decisioni `studio subito`, `studio dopo`, `verifico sul bando`, `rinvio ad altro volume`.

- [ ] **Step 6: Verificare la copertura delle sezioni**

Run:

```powershell
rg -n "Avviso|Allegati|codice profilo|comunicazioni successive|Verbi del programma|materie-soglia|Scheda BANDO|studio subito|verifico sul bando" 'wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/chapters/02-bando-decoder-specialistico.md'
```

Expected: ogni nucleo compare almeno una volta come heading o campo operativo.

### Task 3: Redigere i tre casi e i blocchi di allenamento

**Files:**
- Modify: `wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/chapters/02-bando-decoder-specialistico.md`

**Interfaces:**
- Consumes: metodo e scheda della Task 2.
- Produces: tre applicazioni complete, domanda da commissario, domanda-trappola, errore, esercizio e checklist.

- [ ] **Step 1: Scrivere il caso tributario**

Usare un profilo didattico non attribuito a un bando reale; mostrare come diritto tributario, accertamento/compliance e formato della prova producano priorità e output specifici.

- [ ] **Step 2: Scrivere il caso ispettivo**

Mostrare il passaggio da vigilanza, poteri, acquisizione delle evidenze e verbalizzazione a un allenamento basato su sequenze procedimentali, casi e distinzione fatto-prova-norma.

- [ ] **Step 3: Scrivere il caso funzionario EPNE**

Mostrare come ordinamento dell'ente, procedimento/servizi, bilancio-controlli e materie comuni richiamate producano una preparazione diversa da quella tributaria e ispettiva.

- [ ] **Step 4: Inserire i box conclusivi**

Scrivere `Da sapere in 5 righe`, `Domanda da commissario`, `Domanda-trappola`, `Errore tipico`, `Mini-esercizio`, `Diario errori` e `Checklist operativa`.

- [ ] **Step 5: Verificare i tre casi e gli output**

Run:

```powershell
rg -n "Caso guidato.*tribut|Caso guidato.*ispett|Caso guidato.*EPNE|Domanda da commissario|Domanda-trappola|Errore tipico|Mini-esercizio|Checklist operativa" 'wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/chapters/02-bando-decoder-specialistico.md'
```

Expected: sono presenti i tre casi e tutti i blocchi workbook.

### Task 4: Revisionare tracciabilità, stile e coerenza di volume

**Files:**
- Modify: `wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/chapters/02-bando-decoder-specialistico.md`
- Modify: `wiki/log.md`
- Modify through service: `wiki/memory/agent/`

**Interfaces:**
- Consumes: capitolo completo della Task 3.
- Produces: professional draft verificato, evento di log e traccia sintetica LocalAgentMemory.

- [ ] **Step 1: Controllare placeholder, mojibake e spazi finali**

Run:

```powershell
rg -n "TBD|TODO|Aggiornamento generato|Istruzione ricevuta|Ã|Â|�" 'wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/chapters/02-bando-decoder-specialistico.md'
git diff --check -- 'wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/chapters/02-bando-decoder-specialistico.md'
```

Expected: nessuna corrispondenza e nessun errore dal diff check.

- [ ] **Step 2: Verificare riferimenti e principio delta**

Run:

```powershell
rg -n "\[\[(sources|topics|entities)/|VOL-01|delta specialistico" 'wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/chapters/02-bando-decoder-specialistico.md'
```

Expected: riferimenti consolidati presenti e rinvio esplicito a VOL-01.

- [ ] **Step 3: Eseguire i test disponibili**

Run:

```powershell
npm test
npm run typecheck
```

Expected: entrambi i comandi terminano con exit code `0`; eventuali fallimenti preesistenti devono essere distinti da regressioni del capitolo.

- [ ] **Step 4: Registrare l'evento editoriale**

Aggiungere a `wiki/log.md` una riga append-only con data, capitolo, modalità `professional_draft`, fonti consolidate, numero di righe e verifiche eseguite.

- [ ] **Step 5: Catturare la memoria locale**

Invocare `LocalAgentMemory.captureConversation` con scope `manual-writer`, route `codex/manual-writer/vol03-chapter02`, richiesta sintetica ed esito reale. Se il difetto storico del ranking impedisce l'invocazione, registrare il warning senza modificare il servizio fuori scope.

- [ ] **Step 6: Controllare esclusivamente il diff pertinente**

Run:

```powershell
git diff -- 'wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/chapters/02-bando-decoder-specialistico.md' 'wiki/log.md' 'wiki/memory/agent'
```

Expected: il capitolo, la riga append-only e la traccia di memoria sono le sole modifiche attribuibili a questo flusso.

