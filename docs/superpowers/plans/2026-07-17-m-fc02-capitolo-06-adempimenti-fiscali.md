# M-FC02 Chapter 6 Editorial Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redigere il capitolo completo M-FC02.6 sugli adempimenti fiscali, sostituendo il placeholder nel file canonico con un testo operativo-concorsuale tracciabile.

**Architecture:** Un solo file editoriale viene modificato nella sezione `## Testo editoriale`; frontmatter, specifica e scheda di lavoro restano preservati. Il capitolo segue il flusso `fattispecie -> qualificazione -> dichiarazione -> liquidazione -> versamento -> eventuale controllo` e rinvia ai capitoli contigui per teoria generale, accertamento e riscossione.

**Tech Stack:** Markdown, Obsidian wikilinks, ConcorsoBook OS LLM Wiki, renderer editoriale A4 condiviso.

## Global Constraints

- Usare soltanto fonti consolidate in `wiki/sources/`, `wiki/topics/`, `wiki/entities/`, `wiki/quizzes/` e capitoli esistenti; non usare `wiki/raw/`.
- Scrivere esclusivamente in `wiki/books/` per il contenuto editoriale finale.
- Conservare `book_id: m-fc02-agenzie-fiscali`, `module_code: M-FC02` e `module_family: funzioni-centrali`.
- Non duplicare teoria generale dell'imposta, accertamento sostanziale o riscossione.
- Non cristallizzare scadenze, soglie, percentuali, modelli o codici soggetti a variazione senza fonte consolidata aggiornata.
- Preservare la gerarchia Markdown compatibile con Arial Bold 20/14/12 pt e corpo Garamond 11 pt nel renderer A4.

---

### Task 1: Costruire il testo editoriale completo

**Files:**
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md`

**Interfaces:**
- Consumes: `[[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]]`, `[[sources/adempimenti-contabilita-civile-commerciale-m-fc02]]`, `[[topics/diritto-tributario-concorsi-agenzie-fiscali]]` e capitoli M-FC02 4-5.
- Produces: capitolo Markdown completo nella sezione `## Testo editoriale`.

- [ ] **Step 1: Fotografare struttura e stato iniziale**

Run:

```powershell
rg -n "^## |^### |Da sviluppare con Manual Writer Agent" wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
```

Expected: presenza del placeholder e delle sezioni canoniche iniziali.

- [ ] **Step 2: Sostituire soltanto il placeholder con il capitolo**

Il testo deve contenere, nell'ordine:

```markdown
## Testo editoriale

## Perché gli adempimenti sono una sequenza
## Obiettivo del capitolo
## Mappa BANDO
## Il ciclo dell'adempimento fiscale
## Imposte sui redditi: la mappa essenziale
### Dalla categoria al reddito imponibile
### IRPEF e IRES: distinzione funzionale
## IVA: la mappa essenziale
### Presupposti e operazioni
### Rivalsa, detrazione e neutralità
## Dichiarazione, liquidazione e versamento
### Dichiarazione e documentazione
### Liquidazione e versamento
### Compensazione e correzione degli errori
## Servizi fiscali e rapporto con il contribuente
## Da sapere in 5 righe
## Caso guidato
## Domanda da commissario
## Domanda-trappola
## Errore tipico
## Mini-esercizio
## Quiz ragionati
## Diario degli errori
## Checklist finale
## Riferimenti consolidati
## Note di review
```

Ogni sezione deve contenere testo effettivo per il lettore. Il caso deve distinguere qualificazione, dichiarazione, liquidazione, versamento e possibile controllo; la domanda-trappola deve impedire di trattare dichiarazione e pagamento come sinonimi.

- [ ] **Step 3: Aggiornare lo stato editoriale nel frontmatter**

Applicare queste modifiche puntuali:

```yaml
status: draft
draft_stage: professional-draft
last_compiled_from:
  - wiki/sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md
  - wiki/sources/adempimenti-contabilita-civile-commerciale-m-fc02.md
  - wiki/topics/diritto-tributario-concorsi-agenzie-fiscali.md
```

Aggiornare `updated_at` alla data e ora di esecuzione in formato ISO 8601 con offset Europe/Rome. Conservare `review_required: true`.

- [ ] **Step 4: Verificare struttura e placeholder**

Run:

```powershell
rg -n "Da sviluppare con Manual Writer Agent|Aggiornamento generato|Istruzione ricevuta|^## |^### " wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
```

Expected: nessun placeholder o formula vietata; tutte le sezioni previste risultano presenti.

### Task 2: Eseguire il gate editoriale e di tracciabilità

**Files:**
- Verify: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md`

**Interfaces:**
- Consumes: capitolo prodotto dalla Task 1.
- Produces: evidenza di conformità strutturale, tracciabilità e pulizia della patch.

- [ ] **Step 1: Controllare i riferimenti consolidati**

Run:

```powershell
rg -n "\[\[(sources|topics|books)/" wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
```

Expected: collegamenti alle due source note obbligatorie, al topic tributario e ai capitoli contigui pertinenti.

- [ ] **Step 2: Controllare i nuclei didattici obbligatori**

Run:

```powershell
rg -ni "redditi|IRPEF|IRES|IVA|dichiarazione|liquidazione|versamento|compensazione|contribuente|caso guidato|domanda-trappola|errore tipico|mini-esercizio" wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
```

Expected: ogni nucleo compare in una sezione sostanziale, non soltanto nel frontmatter.

- [ ] **Step 3: Controllare frontmatter e patch**

Run:

```powershell
git diff --check -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
git diff -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
```

Expected: nessun errore di whitespace; diff limitato al frontmatter previsto e alla sezione `Testo editoriale`.

- [ ] **Step 4: Eseguire una lettura finale orientata all'esame**

Verificare manualmente che il capitolo consenta al candidato di rispondere senza confondere:

```text
imposta != dichiarazione != liquidazione != versamento != controllo != riscossione
```

Expected: le distinzioni sono esplicite nella spiegazione, nel caso, nella domanda-trappola e nel diario degli errori.

- [ ] **Step 5: Registrare la memoria del flusso**

Usare `LocalAgentMemory.captureConversation` con scope `manual-writer`, route `codex/manual-writer/mfc02-chapter06` e un esito sintetico che descriva capitolo, fonti e gate eseguiti.

- [ ] **Step 6: Preparare il commit isolato, solo se richiesto**

```powershell
git add -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
git commit -m "docs(m-fc02): write chapter 6 fiscal compliance"
```

Expected: il commit contiene esclusivamente il capitolo 6; le modifiche preesistenti dell'utente restano escluse.
