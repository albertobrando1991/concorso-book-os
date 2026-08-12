# VOL-08 Atomic Q/C/E Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Consentire la chiusura fail-closed delle righe Format 2 quando i conteggi Q/C/E coincidono con il mapping atomico verificato.

**Architecture:** Il validatore deriva la categoria di ogni target dall'apparato reader-visible già analizzato e confronta il risultato con `parseVerificationCounts`. La matrice viene promossa solo dopo il passaggio del gate reale.

**Tech Stack:** Node.js ESM, TypeScript, Vitest, Markdown/JSON.

## Global Constraints

- Non modificare manualmente `pipeline/VOL-08/run-state.json`.
- Nessun conteggio Q/C/E è attendibile senza `verificationAttestations` valido.
- Conservare il comportamento fail-closed per mapping mancanti o discordanti.
- Non modificare i capitoli in questo intervento.

---

### Task 1: Gate Q/C/E atomico

**Files:**
- Modify: `tests/audit-vol08-format2-nuclei.test.ts`
- Modify: `scripts/audit-vol08-format2-nuclei.mjs`

**Interfaces:**
- Consumes: `manifest.verificationAttestations`, `chapter.apparatus.rows`, `parseVerificationCounts()`.
- Produces: confronto esatto tra conteggi dichiarati e conteggi derivati per nucleo.

- [ ] **Step 1: Scrivere il test rosso**

Aggiungere un test che sostituisce la verifica della prima riga con `Q:1 C:0 E:0`, mantenendo il mapping atomico corrispondente, e si aspetta exit code zero. Aggiungere un test separato con `Q:2 C:0 E:0` che si aspetta exit code non zero.

- [ ] **Step 2: Verificare RED**

Run: `npx vitest run tests/audit-vol08-format2-nuclei.test.ts -t "accepts Q/C/E counts derived from atomic verification mappings"`

Expected: FAIL perché il validatore respinge oggi ogni valore Q/C/E numerico.

- [ ] **Step 3: Implementare il confronto minimo**

In `scripts/audit-vol08-format2-nuclei.mjs`, sostituire il rifiuto indiscriminato con una funzione che:

1. legge `row.verificationCounts`;
2. trova le attestazioni valide del nucleo;
3. classifica il target reader-visible come quiz, caso o esercizio;
4. restituisce errore se i tre conteggi non coincidono esattamente.

- [ ] **Step 4: Verificare GREEN**

Run: `npx vitest run tests/audit-vol08-format2-nuclei.test.ts`

Expected: 43 test passati, inclusi accettazione coerente e rifiuto discordante.

- [ ] **Step 5: Commit**

```powershell
git add tests/audit-vol08-format2-nuclei.test.ts scripts/audit-vol08-format2-nuclei.mjs
git commit -m "fix(vol-08): validate atomic qce counts"
```

### Task 2: Promozione dimensionale della matrice

**Files:**
- Modify: `wiki/books/moduli/m-tr01-ict-trasformazione-digitale/planning/02-matrice-copertura-didattica.md`

**Interfaces:**
- Consumes: 82 attestazioni teoriche, 164 attestazioni didattiche e 82 attestazioni di verifica del manifest.
- Produces: 82 righe `completo` con checklist dimensionale chiusa.

- [ ] **Step 1: Riconciliare ogni riga**

Inserire nelle colonne applicazione e output le citazioni letterali attestate; dichiarare Q/C/E derivato; promuovere lo stato soltanto quando tutte le dimensioni risultano coperte.

- [ ] **Step 2: Chiudere la checklist dimensionale**

Per definizione, funzione, inquadramento, elementi, distinzioni, conseguenze, esempio/caso, uso prova, errore tipico, verifica e fonti registrare `✓ verified:` con evidenza o posizione verificabile già presente nel nucleo/manifest.

- [ ] **Step 3: Eseguire le verifiche**

Run: `node scripts/audit-vol08-format2-nuclei.mjs`

Run: `npx vitest run tests/audit-vol08-format2-nuclei.test.ts`

Run: `npm run typecheck`

Run: `git diff --check`

Expected: audit PASS con 82 righe complete, suite verde e typecheck verde.

- [ ] **Step 4: Commit**

```powershell
git add wiki/books/moduli/m-tr01-ict-trasformazione-digitale/planning/02-matrice-copertura-didattica.md
git commit -m "docs(vol-08): close dimensional coverage ledger"
```
