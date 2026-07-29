# Task 4 brief — Governance IVA e adempimenti

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

### Task 4: Governance dei due nuclei

**Files:**
- Modify if necessary: `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md`
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md`
- Modify: `wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md`
- Create: `.superpowers/sdd/iva-task-4-report.md`

**Interfaces:**
- Consumes: capitoli 4 e 6 approvati e source note consolidate.
- Produces: stato canonico di copertura e conteggi verificabili.

- [ ] **Step 1: Verificare le prove prima dello stato**

Per ciascuno dei due nuclei compilare una mappa:

```text
teoria â†’ sede/heading
caso â†’ sede/heading
output concorsuale â†’ sede/heading
verifica â†’ sede/heading
source â†’ nota consolidata
review â†’ esito
```

Atteso: nessun passaggio a `completo` basato solo sulla lunghezza del testo.

- [ ] **Step 2: Aggiornare indice e matrice**

Usare heading canonici esatti. Portare a `completo` solo le righe IVA e adempimenti; registrare fonti, casi, output e verifiche. Non modificare gli altri 14 nuclei.

- [ ] **Step 3: Aggiornare il report M-FC02**

Chiudere esclusivamente i due blocker corrispondenti; impostare i conteggi a 80/66/14/0/0 e mantenere `Non pubblicabile allo stato attuale` con elenco dei 14 blocker residui.

- [ ] **Step 4: Eseguire conteggio e controllo reciproco**

Eseguire:

```powershell
rg -c "\| completo \|" wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md
rg -c "\| parziale \|" wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md
rg -n "Non pubblicabile|14 blocker|14 nuclei" wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
git diff --check -- wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
```

Atteso: `66`, `14`, stato non pubblicabile e diff-check pulito.

- [ ] **Step 5: Review indipendente e commit**

Ottenere i due PASS, applicare fix loop e committare solo i file governance realmente modificati:

```powershell
git add -- wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
git diff --cached --name-only
git commit -m "docs: close M-FC02 VAT and filing coverage gaps"
```

---

