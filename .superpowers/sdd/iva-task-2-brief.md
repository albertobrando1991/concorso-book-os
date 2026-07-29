# Task 2 brief — M-FC02 architettura IVA

Plan: `docs/superpowers/plans/2026-07-20-m-fc02-iva-adempimenti.md`

## Global constraints

## Global Constraints

- Seguire `wiki/AGENTS.md` e usare `LocalAgentMemory`; se il runner non Ã¨ disponibile, documentare l'errore senza creare memorie parallele.
- Applicare `concorso-book-professional-writer` e l'Integral Didactic Coverage Gate.
- Il testo editoriale deriva soltanto da `wiki/sources/`, `wiki/topics/`, `wiki/entities/` e conoscenza consolidata; non scrivere dai raw.
- Preservare tutte le modifiche preesistenti del worktree e usare `apply_patch` per le modifiche; se il wrapper Windows lo impedisce, registrare il fallimento prima di un fallback chirurgico sul solo file autorizzato.
- Usare struttura normativa stabile; aliquote, soglie, termini, modelli, codici e regole telematiche soltanto se ufficialmente verificati, datati e didatticamente necessari.
- Non presentare l'IVA come neutrale in modo assoluto; non confondere non imponibilitÃ , esenzione ed esclusione; non descrivere detrazione o compensazione come incondizionate.
- Non duplicare nei capitoli 4 e 6 la disciplina responsabile dei capitoli 5, 5A, 5B e 7.
- Ogni task richiede implementazione, SPEC COMPLIANCE review, QUALITY review, fix loop e commit isolato.
- Governance attesa dopo approvazione: 80 nuclei, 66 `completo`, 14 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`, 14 blocker; giudizio globale ancora `Non pubblicabile allo stato attuale`.

### Task 2: Architettura IVA nel capitolo 4

**Files:**
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md`
- Create: `.superpowers/sdd/iva-task-2-report.md`

**Interfaces:**
- Consumes: le due source note approvate nel Task 1 e la source UE giÃ  consolidata.
- Produces: sede teorica responsabile dell'architettura IVA e anchor precisi per il capitolo 6.

- [ ] **Step 1: Registrare baseline e mappare le promesse**

Eseguire stat, SHA-256 e diff del capitolo. Elencare le affermazioni giÃ  presenti sotto `## IVA: operazioni, soggetti, detrazione e adempimenti` e verificare ciÃ² che Ã¨ soltanto nominato.

- [ ] **Step 2: Integrare il quadro teorico**

Sviluppare nel blocco IVA:

```text
IVA come imposta armonizzata sui consumi
neutralitÃ  come meccanismo, con limiti
tre presupposti
soggetto passivo / debitore / consumatore finale
catena rivalsa â†’ detrazione â†’ liquidazione
quattro classi di operazioni e loro conseguenza essenziale
rinvio esatto al capitolo 6
```

Per ciascun concetto includere definizione, funzione, distinzione, conseguenza, mini-esempio, errore tipico e verifica, senza duplicare la casistica applicativa del capitolo 6.

- [ ] **Step 3: Aggiornare tracciabilitÃ  e frontmatter**

Aggiungere le source note approvate e la data di compilazione/review pertinente. Non aumentare automaticamente `status` o `confidence`.

- [ ] **Step 4: Eseguire il gate del capitolo 4**

Verificare presenza dei nuclei, assenza di aliquote/soglie mobili non datate, anchor del capitolo 6, UTF-8 e:

```powershell
git diff --check -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
```

Atteso: diff pulito e nessuna regressione del blocco IRPEF/IRES.

- [ ] **Step 5: Review indipendente e commit**

Ottenere `SPEC COMPLIANCE: PASS` e `QUALITY: PASS`, applicare il fix loop e committare:

```powershell
git add -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
git commit -m "docs: strengthen M-FC02 VAT framework"
```

---

