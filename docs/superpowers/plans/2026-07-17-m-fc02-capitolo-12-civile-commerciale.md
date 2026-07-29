# M-FC02 Capitolo 12 — Civile e commerciale Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redigere il capitolo 12 completo del modulo M-FC02 con taglio selettivo, applicativo e concorsuale.

**Architecture:** Un solo file canonico contiene il testo destinato al lettore. La redazione sostituisce la scheda source-ready con una progressione dal rapporto obbligatorio alla crisi d'impresa, mantenendo separati i raccordi con AE, ADM e AdER e chiudendo con strumenti di allenamento e review.

**Tech Stack:** Markdown Obsidian, frontmatter YAML, link interni wiki, renderer editoriale A4 ConcorsoBook OS.

## Global Constraints

- Usare esclusivamente fonti, topic, entity e capitoli consolidati; non usare `wiki/raw/`.
- Mantenere il perimetro civile e commerciale; escludere il diritto penale tributario.
- Non duplicare riscossione, dogane, catasto o contabilità aziendale già trattati nei capitoli 7, 8, 10 e 11.
- Evitare rinvii articolo per articolo, soglie e termini non sostenuti dalle fonti consolidate.
- Conservare gerarchia markdown e blocchi autonomi adatti al renderer A4.
- Contrassegnare le verifiche normative necessarie nelle note di review.

---

### Task 1: Redazione del nucleo teorico-applicativo

**Files:**
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/12-civile-commerciale-applicati-fisco-dogane-riscossione.md`

**Interfaces:**
- Consumes: specifica approvata, frontmatter e `Specifica struttura madre` esistenti, source note consolidate.
- Produces: capitolo canonico con frontmatter aggiornato e sezioni teoriche complete.

- [ ] **Step 1: Aggiornare lo stato editoriale**

Impostare `status: professional_draft`, `draft_stage: professional-draft`, `review_required: true`, aggiornare `updated_at` e ampliare `last_compiled_from` con le fonti e i capitoli di raccordo effettivamente usati.

- [ ] **Step 2: Scrivere apertura, obiettivi e Mappa BANDO**

Aprire con un'operazione economica letta come rete di soggetti, obblighi, contratti, garanzie e responsabilità. Inserire obiettivi verificabili e tabella BANDO/Aree/Nuclei/Diario/Output.

- [ ] **Step 3: Scrivere la progressione civilistica**

Sviluppare in paragrafi brevi: rapporto giuridico; obbligazioni; adempimento; inadempimento e mora; modificazioni ed estinzione; responsabilità; contratto; invalidità e scioglimento; contratti d'impresa; garanzie e conservazione patrimoniale.

- [ ] **Step 4: Scrivere la progressione commercialistica**

Sviluppare: imprenditore; azienda; scritture e rappresentanza; società di persone e di capitali in taglio comparativo; autonomia patrimoniale; bilancio come raccordo giuridico; responsabilità essenziale; box proporzionato sulla crisi d'impresa.

- [ ] **Step 5: Verificare il primo deliverable**

Run: `rg -n "^## |^### " wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/12-civile-commerciale-applicati-fisco-dogane-riscossione.md`

Expected: apertura, obiettivi, Mappa BANDO e una sequenza completa dal rapporto giuridico alla crisi d'impresa; nessun placeholder `Da sviluppare`.

### Task 2: Applicazioni e strumenti concorsuali

**Files:**
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/12-civile-commerciale-applicati-fisco-dogane-riscossione.md`

**Interfaces:**
- Consumes: nucleo teorico-applicativo prodotto dal Task 1.
- Produces: raccordi AE/ADM/AdER e apparato workbook completo.

- [ ] **Step 1: Aggiungere il raccordo con le Agenzie fiscali**

Distinguere l'uso degli istituti per AE, ADM e AdER senza riscrivere le rispettive procedure: qualificazione delle operazioni per AE, titolarità e garanzie nelle operazioni doganali per ADM, obbligazioni e garanzia patrimoniale per AdER.

- [ ] **Step 2: Scrivere un caso guidato unitario**

Usare un'impresa che acquista beni dall'estero, li rivende, concede una garanzia e attraversa una tensione finanziaria. Far classificare rapporto, contratto, obbligazione, responsabilità, garanzia, forma societaria e segnale di crisi.

- [ ] **Step 3: Costruire gli strumenti di prova**

Inserire `Da sapere in 5 righe`, domanda da commissario con traccia, domanda-trappola, errore tipico, mini-esercizio con soluzione ragionata e almeno quattro quiz a risposta multipla.

- [ ] **Step 4: Costruire gli strumenti di ripasso**

Inserire glossario operativo, diario degli errori e checklist finale compilabile.

- [ ] **Step 5: Verificare il secondo deliverable**

Run: `rg -n "Caso guidato|Da sapere in 5 righe|Domanda da commissario|Domanda-trappola|Errore tipico|Mini-esercizio|Quiz di verifica|Glossario operativo|Diario degli errori|Checklist finale" wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/12-civile-commerciale-applicati-fisco-dogane-riscossione.md`

Expected: tutte le dieci componenti presenti una sola volta e complete.

### Task 3: Tracciabilità e verifica editoriale

**Files:**
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/12-civile-commerciale-applicati-fisco-dogane-riscossione.md`
- Modify/Create: traccia canonica in `wiki/memory/agent/` tramite `LocalAgentMemory`, se il servizio è eseguibile.

**Interfaces:**
- Consumes: capitolo completo prodotto dai Task 1 e 2.
- Produces: capitolo verificato e traccia sintetica del flusso agentico.

- [ ] **Step 1: Aggiungere riferimenti e note di review**

Elencare solo i riferimenti consolidati effettivamente usati. Segnalare la necessità di controllo specialistico su contratti, garanzie, società e Codice della crisi prima della pubblicazione.

- [ ] **Step 2: Controllare frontmatter e placeholder**

Run: `rg -n "Da sviluppare|source-ready|Aggiornamento generato|Istruzione ricevuta|TBD|TODO" wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/12-civile-commerciale-applicati-fisco-dogane-riscossione.md`

Expected: nessuna corrispondenza.

- [ ] **Step 3: Controllare confini e tracciabilità**

Run: `rg -n "diritto penale|reat[oi] tributari|Riferimenti consolidati|Note di review|\[\[sources/" wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/12-civile-commerciale-applicati-fisco-dogane-riscossione.md`

Expected: nessuna trattazione penale sostanziale; sezioni finali e link alle source note presenti.

- [ ] **Step 4: Controllare il diff**

Run: `git diff --check -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/12-civile-commerciale-applicati-fisco-dogane-riscossione.md`

Expected: nessun errore di whitespace; modifica circoscritta al capitolo 12, salvo la traccia di memoria canonica.

- [ ] **Step 5: Registrare la memoria del flusso**

Invocare `LocalAgentMemory.captureConversation` con route `codex/manual-writer`, scope `global`, sintesi del perimetro approvato e metadati `module_code=M-FC02`, `chapter=12`. Se il runtime TypeScript non è disponibile, registrare il limite nel resoconto senza modificare manualmente gli archivi della memoria.
