# Task 2: Quadro sistematico IRPEF/IRES nel capitolo 4

## Contesto

La source `[[sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18]]` è consolidata nel commit `0368e08`. Il capitolo 4 deve assumere la responsabilità del sistema, non della determinazione analitica delle categorie.

## Vincoli

- Modificare soltanto `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md`.
- Usare source/topic/entity/capitoli consolidati; non leggere raw per scrittura.
- Non duplicare il capitolo 6 né gli esercizi contabili del capitolo 11.
- Nessun dato mobile non verificato.
- Preservare il contenuto esistente; nessun nuovo capitolo.
- Non modificare matrice/report/index/log/memoria; non commit.

## Requisiti

1. Registrare baseline stat/hash del capitolo prima dell'intervento.
2. Aggiornare frontmatter con source/topic/entity, `companion_to` se assente, updated_at e `last_compiled_from`; non alzare confidence/stato senza review.
3. Inserire nel punto logicamente corretto un quadro sistematico che spieghi:
   - soggetti IRPEF e soggetti IRES;
   - reddito complessivo, oneri deducibili, imponibile, imposta lorda e detrazioni;
   - sei categorie dell'art. 6 e funzione della classificazione;
   - distinzione tra fonte/provento, categoria e criterio di determinazione;
   - rapporto introduttivo tra risultato civilistico e reddito fiscale d'impresa.
4. Non sviluppare nel dettaglio la determinazione delle singole categorie.
5. Aggiungere rinvii con anchor reali al blocco responsabile del capitolo 6 e alla sezione contabile pertinente del capitolo 11.
6. Aggiungere almeno una verifica risolta e un errore tipico specifici del quadro sistematico.
7. Aggiornare riferimenti consolidati e note di review sui dati mobili/manutenzione normativa.
8. Verificare link/anchor, frontmatter, UTF-8, mojibake, baseline/delta e `git diff --check`.

## Report

Scrivere `.superpowers/sdd/redditi-task-2-report.md` con baseline, delta, sezioni, fonti, controlli, self-review e concerns. In chat restituire stato breve.
