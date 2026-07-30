# Contratto didattico dello studente Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:subagent-driven-development` (recommended) or
> `superpowers:executing-plans` to implement this plan task-by-task. Steps use
> checkbox (`- [ ]`) syntax for tracking.

**Goal:** Impedire alla pipeline di approvare capitoli che dipendono dalla wiki
interna e risanare i due capitoli correnti di M-SA02 come testi autosufficienti
per candidati ai concorsi pubblici.

**Architecture:** Il contratto dello studente viene applicato dal gate
esistente dello step 09, senza aggiungere o rinumerare i 25 step. Il citation
guard distingue i rinvii didattici pubblicabili dai collegamenti interni di
conoscenza; prompt, skill e documentazione descrivono la stessa regola. I
capitoli conservano le fonti nel frontmatter e presentano nel corpo solo
spiegazioni e riferimenti leggibili.

**Tech Stack:** TypeScript, Vitest, Markdown, CLI editoriale ConcorsoBook OS.

## Global Constraints

- Non modificare manualmente `pipeline/VOL-07/run-state.json`.
- Non creare nuovi step né rinumerare il protocollo dei 25 prompt.
- Non rimuovere `source_refs` o `last_compiled_from` dal frontmatter.
- Non inventare norme, date, competenze o procedure.
- Non effettuare commit o push in questa sessione; la pubblicazione GitHub
  richiederà un passaggio esplicito successivo.
- Preservare tutte le modifiche non pertinenti già presenti nella worktree.

---

### Task 1: Gate del contratto didattico

**Files:**

- Modify: `tests/pipeline/gates.test.ts`
- Modify: `src/pipeline/gates/chapter-lint-gate.ts`

**Interfaces:**

- Consumes: `runChapterLintGate(ChapterLintInput): GateResult`.
- Produces: blocker `internal-knowledge-link`,
  `editorial-dependency` e `missing-didactic-section`.

- [ ] **Step 1: Scrivere test fallenti per link interni e dipendenze redazionali**

  Aggiungere casi che richiedono il blocco di `[[sources/...]]`,
  `[[topics/...]]`, `[[entities/...]]` e della formula “come spiegato nella
  source note consolidata”.

- [ ] **Step 2: Scrivere test fallenti per le evidenze didattiche**

  Il fixture valido deve contenere obiettivo, Mappa BANDO, spiegazione,
  applicazione/caso, errore e verifica/esercizio. Un test separato rimuove una
  famiglia alla volta e attende `missing-didactic-section`.

- [ ] **Step 3: Eseguire i test e osservare il fallimento atteso**

  Run: `npm test -- tests/pipeline/gates.test.ts`

  Expected: FAIL perché il gate non riconosce ancora il contratto.

- [ ] **Step 4: Implementare il controllo minimo**

  Analizzare esclusivamente il body restituito da `parseFrontmatter`;
  riconoscere i namespace interni con wikilink e le famiglie di heading con
  espressioni regolari esplicite.

- [ ] **Step 5: Eseguire i test mirati**

  Run: `npm test -- tests/pipeline/gates.test.ts`

  Expected: PASS.

### Task 2: Citation guard compatibile con il libro

**Files:**

- Modify: `tests/pipeline/gates.test.ts`
- Modify: `src/pipeline/gates/citation-guard.ts`

**Interfaces:**

- Consumes: `runCitationGuard(CitationGuardInput): GateResult`.
- Produces: protezione dei soli wikilink didattici e blocker
  `new-internal-knowledge-link`.

- [ ] **Step 1: Scrivere i test fallenti**

  Verificare che la rimozione di `[[sources/...]]` non generi
  `lost-wikilink`, che la rimozione di `[[books/...]]` continui a essere
  bloccata e che l'aggiunta di un link interno sia bloccata.

- [ ] **Step 2: Eseguire i test e osservare il fallimento atteso**

  Run: `npm test -- tests/pipeline/gates.test.ts`

  Expected: FAIL sui nuovi comportamenti.

- [ ] **Step 3: Separare link interni e link didattici**

  Introdurre un predicato condiviso nel file del guard e applicarlo
  all'analisi del body.

- [ ] **Step 4: Eseguire i test mirati**

  Run: `npm test -- tests/pipeline/gates.test.ts`

  Expected: PASS.

### Task 3: Contratto unico per agenti e staff

**Files:**

- Modify: `.agents/skills/concorso-book-professional-writer/SKILL.md`
- Modify: `.agents/skills/pipeline-volume/SKILL.md`
- Modify: `wiki/AGENTS.md`
- Modify: `wiki/templates/prompt-staff-revisione-completa-volumi.md`
- Modify: `src/pipeline/cli/commands.ts`
- Modify: `docs/PIPELINE.md`

**Interfaces:**

- Consumes: i codici e le regole dei gate delle Task 1-2.
- Produces: istruzioni concordanti negli step 09-12, nel prompt renderizzato e
  nella guida dello staff.

- [ ] **Step 1: Correggere la skill writer**

  Dichiarare le note interne come input editoriale, non come dipendenza del
  lettore; spostare i riferimenti interni nel frontmatter/report.

- [ ] **Step 2: Correggere i prompt 09-12**

  Inserire obiettivo canonico, divieti del corpo, gate di copertura e test
  dello studente; aggiornare lo step 11 affinché preservi fonti e norme senza
  preservare link interni.

- [ ] **Step 3: Aggiornare contratto CLI e documentazione**

  Descrivere esattamente ciò che il gate blocca e il comportamento del
  citation guard.

- [ ] **Step 4: Verificare coerenza lessicale**

  Run:
  `rg -n "autosufficiente|internal-knowledge-link|test dello studente|source_refs" .agents/skills/concorso-book-professional-writer/SKILL.md wiki/templates/prompt-staff-revisione-completa-volumi.md src/pipeline/cli/commands.ts docs/PIPELINE.md`

  Expected: le quattro superfici esprimono lo stesso contratto.

### Task 4: Risanamento dei capitoli M-SA02

**Files:**

- Modify:
  `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/01-mappa-profili-e-prove.md`
- Modify:
  `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md`

**Interfaces:**

- Consumes: frontmatter e contenuto consolidato esistente.
- Produces: due capitoli reader-facing che superano il contratto.

- [ ] **Step 1: Auditare i link e il lessico interno**

  Run:
  `rg -n "\[\[(sources|topics|entities)/|source note|fonte consolidata|fonti consolidate|corpus" <chapter-01> <chapter-03>`

  Expected: elenco completo delle dipendenze da rimuovere dal body.

- [ ] **Step 2: Correggere il capitolo 01**

  Preservare la teoria valida; sostituire il lessico editoriale e presentare i
  riferimenti finali in forma normativa/professionale leggibile.

- [ ] **Step 3: Correggere il capitolo 03**

  Integrare direttamente la conoscenza necessaria in ogni sezione, rimuovere
  i wikilink interni e sostituire la griglia “Fonte” con “Riferimento da
  ricordare”.

- [ ] **Step 4: Eseguire il nuovo gate sui due file**

  Run: script TypeScript che invoca `runChapterLintGate` sui due capitoli.

  Expected: entrambi `passed: true`.

### Task 5: Verifica e memoria

**Files:**

- Modify: `wiki/memory/agent/` esclusivamente tramite `LocalAgentMemory`.

**Interfaces:**

- Consumes: implementazione e capitoli corretti.
- Produces: verifiche verdi e traccia di continuità.

- [ ] **Step 1: Eseguire test pipeline e test completi**

  Run: `npm test -- tests/pipeline/gates.test.ts`

  Run: `npm test`

  Expected: tutti i test PASS.

- [ ] **Step 2: Eseguire il typecheck**

  Run: `npm run typecheck`

  Expected: exit code 0.

- [ ] **Step 3: Verificare il diff limitato**

  Run: `git diff -- <file del piano e della specifica, gate, test, prompt,
  skill, documentazione, capitoli>`

  Expected: nessuna modifica non pertinente.

- [ ] **Step 4: Registrare la decisione**

  Usare `LocalAgentMemory` con scope `VOL-07/M-SA02` per salvare obiettivo,
  modifica dei gate, capitoli risanati ed esito delle verifiche.
