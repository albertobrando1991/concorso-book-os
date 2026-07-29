# Task 3: Governance della copertura ACFI

## Contesto

La source ACFI è consolidata nel commit `9b2f5ce` e il capitolo 5 è stato approvato nel commit `d4c3a5c`. La governance deve ora riflettere esclusivamente la copertura realmente raggiunta, senza chiudere altri gap.

## Vincoli globali

- Perimetro selettivo ACFI: residenza, stabile organizzazione, convenzioni/doppia imposizione, transfer pricing, documentazione, operazioni infragruppo, rischio e TCF.
- Non promettere l'intera fiscalità internazionale.
- Preservare tutte le modifiche preesistenti nel worktree.
- Non modificare capitoli, source, raw, `wiki/index.md`, `wiki/log.md` o memoria.
- Il modulo resta non pubblicabile per i nuclei parziali residui.

## File autorizzati

- `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md`
- `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md`
- `wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md`
- `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/00-piano-editoriale.md` soltanto se necessario per rendere precisa la destinazione ACFI.

## Requisiti

1. Nell'indice analitico collegare ACFI al capitolo 5 e nominare gli istituti coperti, senza cambiare la struttura delle 16 unità.
2. Nella matrice aggiornare soltanto la riga `M-FC02/ACFI | Fiscalita internazionale`: fonte ACFI consolidata, collocazione precisa nel cap. 5, teoria, caso, output, verifica e review reali; stato da `solo-nominato` a `completo` soltanto perché il capitolo ha superato review.
3. Ricalcolare i totali: 80 nuclei = 63 `completo` + 17 `parziale`; 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`; 17 blocker.
4. Nel report chiudere E05, aggiornare sintesi/coerenza/priorità/giudizio e osservazione cap. 5; eliminare fiscalità internazionale dall'elenco dei blocker. Mantenere esplicitamente non pubblicabile e non alterare gli altri 17 parziali.
5. Aggiornare il piano editoriale solo se la destinazione ACFI non è già precisa; se modificato, dichiarare perché nel report.
6. Controllare link/anchor, conteggi matematici, riferimenti stale (`solo-nominato`, 18 blocker, 62 completi), UTF-8 e `git diff --check`.
7. Non committare.

## Report

Scrivere `.superpowers/sdd/acfi-task-3-report.md` con file modificati, cambiamenti, conteggi verificati, controlli ed esiti, self-review e concerns. Restituire in chat stato breve.
