# Task 2: Integrazione didattica ACFI nel capitolo 5

## Contesto

La source `[[sources/fiscalita-internazionale-acfi-aggiornamento-2026-07-18]]` è consolidata e approvata. Il capitolo 5 contiene già revisioni non committate da preservare; il richiamo nominale `Profili ACFI e fiscalita internazionale` deve diventare un blocco autonomo Livello 3, senza creare un capitolo 5C.

## Vincoli globali

- Perimetro selettivo: residenza, stabile organizzazione, convenzioni, doppia imposizione, transfer pricing, operazioni infragruppo, rischio e tax control framework.
- Usare solo source/topic/entity/capitoli consolidati; non leggere raw per scrivere.
- Nessuna aliquota, soglia, termine, elenco di Stati o modalità mobile non verificata.
- Preservare tutte le modifiche preesistenti nel capitolo.
- Non duplicare impropriamente i capitoli 4, 6 e 11: usare rinvii precisi.
- Non marcare autonomamente la matrice come completa: governance nel Task 3.

## File

- Modificare soltanto `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/05-accertamento-controlli-compliance-fiscale.md`.
- Leggere `wiki/sources/fiscalita-internazionale-acfi-aggiornamento-2026-07-18.md`.
- Leggere per raccordo i capitoli 4, 6 e 11.

## Requisiti

1. Fotografare e descrivere nel report il diff preesistente del capitolo prima dell'intervento.
2. Aggiornare frontmatter con source/topic/entity pertinenti, `companion_to: il-metodo-bando`, data e `last_compiled_from`, senza alzare arbitrariamente confidence o stato complessivo.
3. Sostituire il richiamo nominale dopo l'adempimento collaborativo con una progressione completa: mappa e valore delle fonti; criteri di collegamento e residenza di persone fisiche/società; stabile organizzazione materiale/personale ed esclusione di automatismi; convenzioni e doppia imposizione; transfer pricing e libera concorrenza; operazioni infragruppo, Masterfile/Documentazione Nazionale, comparabilità e rischio; raccordo con TCF e attività dell'ufficio.
4. Per ogni nucleo coprire definizione, funzione, elementi, distinzioni, conseguenze, esempio, uso in prova, errore e verifica.
5. Inserire caso completo società residente–impresa collegata–presenza estera con sequenza fatti → qualificazione → fonti → rischio → istruttoria → output.
6. Aggiungere risposta da commissario, domande-trappola, mini-esercizio risolto, quiz ragionati, errori e checklist.
7. Rinvii precisi ai capitoli 4, 6 e 11; riferimenti consolidati e note di review sulle prassi successive e sui dettagli mobili.
8. Verificare link/anchor, frontmatter, encoding, assenza di artefatti e `git diff --check`.
9. Non modificare altri file e non committare.

## Report

Scrivere `.superpowers/sdd/acfi-task-2-report.md` con: baseline/diff preesistente, sezioni integrate, fonti usate, controlli con esiti, self-review e concerns. In chat restituire solo stato, una riga di verifiche e concerns.
