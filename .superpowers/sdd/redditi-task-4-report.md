# Task 4 - Governance della copertura IRPEF/IRES

## Baseline

Rilevata prima delle modifiche:

| File | Stato iniziale | Hash iniziale (`git hash-object`) | Ultimo commit sul file |
| --- | --- | --- | --- |
| `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md` | modificato, con variazione ACFI preesistente da preservare | `246081d789ee6c46110bb8f09c0e997f94cac0f3` | `f1ace22a9122627858b94d66e367e052dc2540d0` |
| `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md` | pulito | `4bbf21424366b72873f333428999a8e70fcd00dc` | `bc6f4b21e8737e71e9cf5c38bbd65ea983641a53` |
| `wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md` | pulito | `a8da77ff634cc7e5c1212771d0985e41b7cef702` | `bc6f4b21e8737e71e9cf5c38bbd65ea983641a53` |

La modifica ACFI gia presente nell'indice analitico e tutte le altre modifiche estranee del worktree sono state preservate.

## File realmente modificati

- `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md`: precisate le tre destinazioni didattiche dei redditi.
- `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md`: aggiornata esclusivamente la riga IRPEF/IRES e il riepilogo numerico.
- `wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md`: chiuso soltanto E06, allineate osservazioni e conteggi, rimossa soltanto la relativa voce dall'elenco dei parziali.
- `.superpowers/sdd/redditi-task-4-report.md`: presente report.

Nessun capitolo, source note, raw, memoria o altra governance e' stato modificato. Nessun commit e' stato eseguito.

## Evidenze per la chiusura di E06

- Capitolo 4, `IRPEF e IRES: il quadro sistematico`: definisce il criterio di ingresso per soggetto, distingue soggetti IRPEF e categorie di soggetti IRES, residenza, fonte e architettura di formazione del reddito; collega la source consolidata `[[sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18]]`.
- Capitolo 6, da `Imposte sui redditi: qualificare prima di calcolare` a `Trappole e checklist operativa sui redditi`: sviluppa le sei categorie dell'art. 6 TUIR, qualificazione, determinazione e imputazione, distinzioni ad alta frequenza, reddito d'impresa, soggetti e struttura IRES, ponte dal risultato civilistico al reddito imponibile, competenza/inerenza e componenti positivi/negativi. Contiene esempi per categoria, caso IRPEF multi-componente, caso IRES, esercizio, quiz dedicati, risposta modello orale, trappole e checklist.
- Capitolo 11, `14. Dal bilancio al reddito imponibile`: completa il raccordo civilistico-contabile spiegando variazioni in aumento/diminuzione e differenze permanenti/temporanee; il mini-esercizio include un costo fiscalmente indeducibile e la relativa variazione in aumento.

Le tre sedi, considerate insieme, soddisfano teoria, casi/esempi, output concorsuali, verifica e revisione. Lo stato `completo` attesta la completezza didattica locale, non la certificazione normativa: restano espresse la review TUIR vigente e la verifica articolo-specifica.

## Conteggi prima/dopo

| Stato | Prima | Dopo |
| --- | ---: | ---: |
| Nuclei totali | 80 | 80 |
| `completo` | 63 | 64 |
| `parziale` | 17 | 16 |
| `solo-nominato` | 0 | 0 |
| `rinviato` | 0 | 0 |
| `mancante` | 0 | 0 |
| Blocker editoriali | 17 | 16 |

## Controlli

- Coerenza matrice/review: 80 nuclei, 64 completi, 16 parziali e 16 blocker in entrambi i file.
- Perimetro: E06 risulta `Chiuso`; E07-E16 e gli ulteriori nuclei parziali non sono stati chiusi.
- Pubblicabilita: il giudizio resta esplicitamente `Non pubblicabile allo stato attuale`.
- Destinazioni: verificata l'esistenza esatta degli heading nei capitoli 4, 6 e 11.
- Source note: verificata l'esistenza di `wiki/sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md` e il suo collegamento nei capitoli 4 e 6.
- Link/anchor: le collocazioni riportano titoli di heading esistenti e verificabili.
- Codifica: file scritti in UTF-8 senza BOM; nessun errore di whitespace rilevato.
- `git diff --check`: superato sui file di governance e sul report.
- Memoria locale: `LocalAgentMemory` e' stato invocato, ma il runner `tsx` non e' disponibile/cacheato e Node puro non risolve gli import TypeScript extensionless; nessuna memoria parallela e' stata creata e la memoria non e' stata modificata, nel rispetto dello scope.

## Diffstat finale

- Governance tracciata: 3 file, 35 inserimenti e 36 eliminazioni (`git diff --stat`).
- Report nuovo: 62 righe prima dell'inserimento di questo diffstat.
- Totale file realmente modificati/creati dal task: 4.

## Blocker residui

Gli altri 16 blocker restano aperti. Il modulo M-FC02 resta non pubblicabile finche i 16 nuclei parziali non sono sviluppati e verificati; la chiusura di E06 non equivale alla completezza dell'intero modulo.