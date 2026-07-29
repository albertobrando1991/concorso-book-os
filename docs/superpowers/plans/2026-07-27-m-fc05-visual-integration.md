# M-FC05 Visual Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Dare ai quindici capitoli M-FC05 la stessa copertura di infografiche didattiche del Volume 2, senza modificare il perimetro contenutistico del modulo.

**Architecture:** Ogni capitolo mantiene il proprio Markdown e riceve una cartella `assets/chapter-XX/` con cinque master SVG e cinque PNG derivati. I riferimenti PNG sono dichiarati nel frontmatter `asset_refs` e collocati nel testo accanto al relativo blocco didattico. Gli SVG seguiranno il componente grafico riusabile e la palette dei generatori già in `scripts/generate-chapter*-assets.cjs`.

**Tech Stack:** Markdown, SVG nativo, Node.js, Playwright Chromium per rasterizzare e ispezionare, preview A4 esistente.

## Global Constraints

- Perimetro esclusivo: `wiki/books/moduli/m-fc05-authority-indipendenti/`, capitoli 1–15.
- Riferimenti vincolanti di stile: `wiki/books/il-metodo-bando/design-system-editoriale.md` e gli asset M-FC02.
- Cinque visual per capitolo, 1600 × 1000 px, SVG editabile + PNG di compatibilità.
- Nessuna fotografia, nessun visual decorativo, nessuna modifica sostanziale al testo esistente.
- Ogni asset ha titolo, descrizione accessibile, alt text e didascalia; palette e tipografia restano coerenti con M-FC02.
- L’esecuzione è sequenziale: un capitolo viene verificato prima di iniziare il successivo.
- Non modificare asset già validi: registrarne la revisione e passare oltre.

---

### Task 1: Stabilire il kit grafico e l’audit del Capitolo 1

**Files:**
- Create: `scripts/generate-mfc05-chapter01-assets.cjs`
- Create: `wiki/books/moduli/m-fc05-authority-indipendenti/assets/chapter-01/01-...svg` fino a `05-...svg`
- Create: versioni `.png` corrispondenti e `README.md`
- Modify: `wiki/books/moduli/m-fc05-authority-indipendenti/chapters/01-authority-viste-dal-candidato.md`

**Interfaces:**
- Consumes: `chapter-01` e il modello `scripts/generate-chapter11-assets.cjs`.
- Produces: cinque asset e cinque riferimenti Markdown del Capitolo 1.

- [x] Verificare se il capitolo contiene già infografiche e conservarle se conformi.
- [x] Derivare dal capitolo cinque soggetti non ridondanti.
- [x] Generare SVG con metadati accessibili e rasterizzarli in PNG.
- [x] Inserire `asset_refs`, immagini, alt text e didascalie dopo i blocchi pertinenti.
- [x] Ispezionare tutti i PNG e la preview A4, correggendo clipping, testo troppo piccolo o collisioni.

### Task 2: Integrare i Capitoli 2–7

**Files:**
- Create: `assets/chapter-02/` fino a `assets/chapter-07/`
- Modify: i sei Markdown dei capitoli 2–7
- Create: generatori dedicati se necessari, uno per capitolo

**Interfaces:**
- Consumes: kit grafico validato nel Task 1 e contenuti dei capitoli 2–7.
- Produces: 30 infografiche collegate e verificate.

- [x] Per ciascun capitolo, audire prima gli asset esistenti e non sostituire quelli conformi.
- [x] Per le lacune, creare cinque visual pertinenti alla mappa BANDO, architettura, procedura, confronto e sintesi.
- [x] Inserire immagini e didascalie in posizioni narrative coerenti.
- [x] Controllare dimensione, leggibilità e percorsi di tutti i file prodotti.
- [x] Eseguire una verifica A4 per capitolo prima di passare a quello successivo.

### Task 3: Integrare i Capitoli 8–14

**Files:**
- Create: `assets/chapter-08/` fino a `assets/chapter-14/`
- Modify: i sette Markdown dei capitoli 8–14
- Create: generatori dedicati se necessari, uno per capitolo

**Interfaces:**
- Consumes: kit grafico del Task 1, pattern di authority e contenuti dei capitoli 8–14.
- Produces: 35 infografiche collegate e verificate.

- [x] Rendere distinguibili mandato, destinatari, poteri, procedimenti e forme di tutela di ogni authority.
- [x] Impedire confronti impropri tra authority e ogni sovrapposizione di testo.
- [x] Inserire i cinque visual per capitolo secondo il flusso di lettura.
- [x] Ispezionare i PNG e controllare le immagini nella preview A4.

### Task 4: Integrare il Capitolo 15 e chiudere l’audit

**Files:**
- Create: `assets/chapter-15/`
- Modify: `chapters/15-laboratorio-prove-authority.md`
- Create: `wiki/reviews/m-fc05-audit-integrazione-visiva-2026-07-27.md`
- Modify: `wiki/log.md`

**Interfaces:**
- Consumes: i 14 capitoli già verificati e la struttura laboratoriale del Capitolo 15.
- Produces: cinque visual di performance, registro di audit e traccia di memoria del flusso.

- [x] Creare e inserire le cinque tavole operative del laboratorio.
- [x] Eseguire il controllo dell’intero modulo: 15 cartelle, 75 SVG, 75 PNG, 75 riferimenti nel frontmatter e nel corpo.
- [x] Registrare nel report le decisioni di creazione o mantenimento e gli esiti di layout.
- [ ] Catturare la memoria operativa finale tramite `LocalAgentMemory` (il servizio TypeScript non è invocabile dalla shell corrente per una risoluzione ESM preesistente); il log append-only è aggiornato.
- [x] Eseguire `npm.cmd run typecheck` e i controlli dei link/asset pertinenti.

## Self-review

- La sequenza mantiene la richiesta dell’utente: Capitolo 1 prima, poi avanzamento soltanto dopo la revisione.
- Ogni requisito della specifica ha una destinazione: formato e accessibilità nel Task 1, copertura nei Task 2–4, verifica e audit nel Task 4.
- Nessun passaggio introduce immagini decorative o modifica volumi diversi da M-FC05.
