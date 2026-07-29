# Task 3 report — M-FC02 capitolo 6 IVA e adempimenti

## Status

DONE

## Baseline, perimetro e hash

- File editoriale: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md`.
- SHA-256 baseline: `7ADEA78E0C1E4EEF241A006E3595A25F9917224F870AC8BC2DC3F727E498F810`.
- SHA-256 dopo fix loop: `F03B8D680914136CE2B37D3EC61D0795C1C4E5209099B81D309C42A8A1101EA3`.
- Hash IRPEF/IRES HEAD: `F08C429FE23837D4760C8677E3F39909D0D35B758C83DEE6C170A03EA2F7C92A`.
- Hash IRPEF/IRES finale: `F08C429FE23837D4760C8677E3F39909D0D35B758C83DEE6C170A03EA2F7C92A`: preservazione confermata.
- `updated_at` preservato a `2026-07-20T00:00:00+02:00`.
- Il diff finale comprende anche una modifica di integrazione di una riga nel capitolo 4, necessaria a ripristinare il link/anchor verso il capitolo 6; è uno scope coordinato e giustificato dal collegamento rotto. Nessun commit.

## Fix reviewer

| ID | Correzione | Evidenza | Esito |
| --- | --- | --- | --- |
| C1 | Soggettività e territorialità L3 | beni/servizi, mappa B2B/B2C, eccezioni come gate, esempio ed errore | PASS |
| C2 | Catena documentale | fattura, registri vendite/acquisti, debito/detrazione, liquidazione ed errore risolto | PASS |
| I2 | Credito IVA | riporto, compensazione, rimborso e percorso prudente | PASS |
| I3 | Caso IVA determinato | Alfa/Beta/Gamma, luoghi, data, documenti, base `4.200 × t`, rivalsa, detrazione e saldo | PASS |
| I4 | Dichiarazioni | originaria, correttiva legata alle istruzioni, tardiva valida, omessa, integrative a favore/sfavore e quattro casi | PASS |
| M1 | Compensazione | sei gate: esistenza, spettanza, disponibilità, perimetro, ostacoli, controlli; due scenari | PASS |
| M2 | Dato temporale | vigenza D.Lgs. 241/1997 artt. 17-20 e disposizioni pertinenti al 20/07/2026; art. 24 transitorio/non fondativo di F24; futuro D.Lgs. 33/2025 dal 01/01/2027 | PASS |
| Refusi | Citazione «tutte senza IVA» e definizione della detrazione nel quiz | testo corretto | PASS |

## Test specifici e output

- `rg -c '^## Operazioni IVA e ciclo degli adempimenti$' <capitolo>` → `1`.
- `rg -c '^\*\*Scenario risolto [AB]' <capitolo>` → `2`.
- Ricerca mirata B2B/B2C, registri, casi dichiarativi, sei gate, riporto/compensazione/rimborso e frase datata → tutte le evidenze presenti.
- Ricerca `?tutte` → 0 occorrenze.
- `updated_at` → `2026-07-20T00:00:00+02:00`.
- Sequenza “Da sapere in 5 righe” → fattispecie/qualificazione, documentazione, registrazione, liquidazione, dichiarazione, versamento/compensazione, controllo, correzione nello stesso ordine — PASS.
- Caso Alfa/Beta/Gamma → la fattura del 12 marzo anticipa l’effettuazione per l’importo fatturato; la sola ultimazione non basta nella regola generale della prestazione ordinaria nazionale — PASS.
- Fonte F24 → artt. 17-20 e disposizioni pertinenti; art. 24 qualificato come transitorio e non fondativo — PASS.
- Hash IRPEF/IRES HEAD/finale identici → PASS.
- `git diff --check -- <capitolo>` → output vuoto, PASS.
- SPEC COMPLIANCE: PASS.
- QUALITY: PASS.

## Diffstat

Diff coordinato dei capitoli 4 e 6: `2 files changed, 132 insertions(+), 43 deletions(-)`. Dettaglio: capitolo 4 `1+/1-` (una riga di integrazione per il link/anchor); capitolo 6 `131+/42-`. Il report è un file nuovo. Nessun commit eseguito.

## Note tecniche pregresse

`apply_patch` era stato bloccato dal wrapper Windows; il fallback è rimasto chirurgico e circoscritto agli heading IVA/adempimenti. Il richiamo `LocalAgentMemory` era stato bloccato dall'assenza del runner `tsx` (`ENOTCACHED`); non è stata creata memoria parallela.
