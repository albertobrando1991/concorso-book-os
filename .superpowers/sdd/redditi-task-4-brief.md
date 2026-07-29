# Task 4 — Governance della copertura IRPEF/IRES

## Contesto approvato

- Source note consolidata: commit `0368e08`.
- Quadro sistematico nel capitolo 4: commit `ba1f58f`.
- Trattazione teorico-operativa nel capitolo 6: commit `9fc4dcc`.
- Il raccordo contabile resta nel capitolo 11.

## Scope autorizzato

Modificare soltanto i file effettivamente necessari tra:

- `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md` — solo se servono destinazioni piu precise;
- `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md`;
- `wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md`.

Non modificare capitoli, source note, raw, memoria o altra governance. Non eseguire commit.

## Requisiti

1. Rilevare baseline, hash e stato di ciascun file prima di modificarlo; preservare variazioni preesistenti.
2. Aggiornare esclusivamente il nucleo/riga IRPEF-IRES-categorie reddituali-reddito d'impresa, portandolo a `completa` solo se la verifica puntuale dei capitoli 4, 6 e 11 lo giustifica.
3. Registrare la nuova source note e collocazioni precise e verificabili:
   - capitolo 4 per il quadro sistematico IRPEF/IRES;
   - capitolo 6 per categorie, determinazione, IRES e applicazioni;
   - capitolo 11 per il raccordo civilistico-contabile e le variazioni fiscali.
4. Rendere espliciti teoria, casi/esempi, output concorsuali, verifica e revisione.
5. Chiudere soltanto il blocker `E06` relativo a IRPEF/IRES; non alterare gli altri blocker.
6. Ricalcolare coerentemente i totali M-FC02 attesi: 80 nuclei, 64 completi, 16 parziali, 0 solo-citati, 0 mancanti, 16 blocker residui.
7. Il report deve restare non pubblicabile finche persistono i 16 nuclei parziali/blocker; non suggerire che l'intero modulo sia completo.
8. Aggiornare l'indice analitico soltanto se gli attuali rinvii non consentono di individuare con precisione le nuove sedi didattiche.
9. Verificare coerenza reciproca dei file, link/anchor, codifica e `git diff --check`.

## Report obbligatorio

Creare `.superpowers/sdd/redditi-task-4-report.md` con:

- baseline e file realmente modificati;
- evidenze che giustificano la chiusura di E06;
- conteggi prima/dopo;
- controlli e relativi esiti;
- diffstat finale;
- conferma che gli altri 16 blocker restano aperti.
