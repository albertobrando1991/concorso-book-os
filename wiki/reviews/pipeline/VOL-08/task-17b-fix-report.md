# Task 17b — Fix report

## Esito

PASS. Una attestazione `verified` richiede ora un reviewer identificabile: una stringa con contenuto non vuoto dopo `trim()`.

## Correzione

`validAttestation()` rifiuta sia valori non stringa (incluso `true`) sia stringhe vuote o composte da whitespace. Non è stato introdotto un formato più restrittivo, per non escludere identificativi validi già usati nei flussi editoriali.

## Regressioni

- reviewer `"   "`: FAIL atteso.
- reviewer `true`: FAIL atteso.
- reviewer `"revisore-specialistico"`: PASS atteso.

## Verifiche

- Test mirati: 21/21 PASS.
- Audit Format 2: PASS, 13 capitoli e 82/82/82 nuclei.
- Pipeline: 302/302 PASS.
- Typecheck e `git diff --check`: PASS.

## Scope

Nessuna modifica a capitoli, indice, run-state, step 24 o memoria.