---
id: vol-12-consegna-correzioni-m-sp02-fase-c
type: editorial_review
title: VOL-12 - Consegna correzioni M-SP02 fase C
status: awaiting-human-review
volume_code: VOL-12
module_code: M-SP02
domain: concorsi pubblici italiani
topics: []
entities: []
source_refs: [sources/bandi-e-ordinamento-corpo-nazionale-vigili-del-fuoco-m-sp02]
book_refs: [m-sp02-vigili-fuoco, vol-12-carriere-speciali-premium]
confidence: high
updated_at: 2026-08-13T00:00:00+02:00
created_at: 2026-08-13T00:00:00+02:00
review_required: true
canonical: false
tags: [vol-12, m-sp02, phase-c, corrections, handover]
---

# Consegna correzioni - M-SP02 Vigili del fuoco

## Esito

Le cinque correzioni del report 13 sono state applicate nell'ordine richiesto. I capitoli 01, 02, 03 e 04 non sono stati modificati. Gli interventi sul testo hanno riguardato soltanto i capitoli 05-08; la source note B2 è stata aggiornata perché il punto 1 lo richiedeva espressamente.

## Correzioni applicate

1. B2 e N-SP02-07-01 riportano quote 25/10/15/2, condizioni, eccezione di età per il 25%, condizione disciplinare per 25% e 10%, devoluzione e dichiarazione in domanda. Aggiornata anche la riga di matrice.
2. Le sezioni-fantoccio sono state rimosse da 05-08; teoria ed errori sono ora evidenze nei nuclei reali.
3. I cinque nuclei di ciascun capitolo 05-08 coprono decisioni e output distinti, quindi non richiedono accorpamenti. Rimossa dal 06 la frase duplicata. Nessuna prosa di riempimento aggiunta.
4. Il 05 contiene la tabella delle riserve; il 06 la matrice riuso-delta; il 07 il piano 30/60/90; l'08 la tabella errore-segnale-correzione-prova di ritorno.
5. La matrice usa i conteggi reali E 5/10/8/10/5/5/5/5. La checklist dimensionale non contiene `Stato`; il parser legge 40 nuclei, non 80.

## Esito dei gate per capitolo

| Capitolo | Parole | Parole per nucleo | Q/C/V | didactic-density | chapter-lint |
| --- | ---: | --- | --- | --- | --- |
| 01 | 3.769 | 607 / 604 / 643 / 613 / 632 | 6/1/1 | passed | passed |
| 02 | 5.697 | 689 / 1.068 / 770 / 654 / 738 | 6/1/2 | passed | passed |
| 03 | 5.278 | 610 / 709 / 685 / 694 / 824 | 6/1/2 | passed | passed |
| 04 | 5.543 | 690 / 666 / 844 / 804 / 620 | 6/1/2 | passed | passed |
| 05 | 3.927 | 911 / 605 / 629 / 624 / 635 | 6/1/1 | passed | passed |
| 06 | 3.832 | 617 / 882 / 612 / 600 / 612 | 6/1/1 | passed | passed |
| 07 | 3.756 | 603 / 600 / 613 / 622 / 611 | 6/1/1 | passed | passed |
| 08 | 3.808 | 623 / 601 / 612 / 607 / 632 | 6/1/1 | passed | passed |

`Q/C/V` indica quiz commentati, casi guidati o ragionati e blocchi di verifica. Entrambi i gate sono stati eseguiti con `format_version: 2`; non risultano blocker né warning.

## Matrice

- righe canoniche: 40;
- stato `completo`: 40;
- blocker: 0;
- warning: 0;
- righe complete secondo l'audit: 40.

Totali e dichiarazione finale sono coerenti con le righe.

## Incognite dichiarate ancora aperte

1. Il bando operativo non indica numero e durata dei quesiti, penalità per errore e disponibilità di una banca dati.
2. Il bando operativo non dichiara un livello autonomo di inglese.
3. L'eventuale preselezione direttiva dipende dagli avvisi della singola procedura.
4. Le specialità future non sono prevedibili e richiedono il relativo bando.
5. L'idoneità individuale resta competenza degli organi previsti.

## Stato della consegna

La consegna è pronta per la nuova review umana. Non sono stati eseguiti text freeze o avanzamenti di fase. `pipeline/VOL-12/run-state.json` non è stato modificato manualmente.
