# ACFI Task 3 — Governance report

## Stato

DONE

## Modifiche eseguite

- Indice analitico verificato ma non modificato durante Task 3: all'avvio del fallback la voce 9 ACFI era gia presente come modifica non committata nel worktree. La baseline `HEAD` e il commit `f1ace22` contengono invece la precedente voce `Interpello, compliance e adempimento collaborativo.`; il diff dell'indice non e' quindi attribuito a Task 3. La struttura corrente resta di 16 unita.
- Matrice aggiornata esclusivamente nella riga `M-FC02/ACFI | Fiscalita internazionale`: fonte consolidata, collocazione precisa nel capitolo 5, teoria, caso, output e verifiche reali; stato portato a `completo`. La colonna review distingue la review didattica ACFI superata il 2026-07-18 dalla manutenzione normativa e dalla verifica delle fonti vigenti, ancora obbligatorie; la destinazione rinvio resta `-`.
- Totali matrice aggiornati a 80 nuclei: 63 `completo`, 17 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`; 17 blocker.
- Review aggiornata in sintesi, E05, osservazione sul capitolo 5, coerenza, priorita e giudizio di pubblicabilita. Chiuso solo E05; conservati i 17 nuclei parziali e il giudizio `Non pubblicabile`.
- Piano non modificato: indice e matrice rendono gia precisa la destinazione ACFI.

## Verifiche

- Conteggio reale delle 80 righe della matrice: `completo=63`, `parziale=17`; nessun altro stato presente.
- Fonte `sources/fiscalita-internazionale-acfi-aggiornamento-2026-07-18` presente e collegata.
- Intestazioni del capitolo 5 verificate: `Profili ACFI e fiscalita internazionale`, `Fonti e metodo operativo`, `Commissario, trappole, esercizio e quiz`.
- Nessuna frase obsoleta trovata: `62 completo`, `18 blocker`, `1 solo-nominato`, `unico nucleo ancora solo nominato`.
- UTF-8 verificato sui tre file di governance: nessun carattere di sostituzione e nessun BOM.
- `git diff --check` sui file autorizzati: superato; soli warning informativi CRLF/LF.
- Diff ispezionato: modifiche eseguite dal fallback Task 3 limitate alla riga/totali della matrice e alle sezioni pertinenti della review. Il diff dell'indice era gia presente nel worktree all'avvio e non e' stato prodotto da Task 3. Nessun commit eseguito.

## Esito editoriale

Il perimetro ACFI e' completo solo per residenza, stabile organizzazione, convenzioni e doppia imposizione, transfer pricing, documentazione e operazioni infragruppo, rischio fiscale e Tax Control Framework. Non viene promessa la copertura integrale della fiscalita internazionale.
