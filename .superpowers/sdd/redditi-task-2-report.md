# Redditi Task 2 — Report capitolo 4

## Stato

DONE

## Baseline

- File: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md`
- Dimensione iniziale: 48.771 byte.
- Ultima modifica UTC rilevata prima dell'intervento: `2026-07-18T16:31:04.6820167Z`.
- SHA-256 iniziale: `ebab73348a19e9479394ce88d9924ae1c07e1a900237027abba75483b3ba495e`.

## Delta

- Dimensione finale: 57.138 byte; delta `+8.367` byte.
- SHA-256 finale: `3565db22ef3ff2a928ab4288d00ee4f99059f40cdfec9923e054280d4cde2555`.
- Diff Git del capitolo: 94 righe aggiunte e 4 righe rimosse; le rimozioni corrispondono alle sostituzioni chirurgiche del frontmatter.
- Modificato soltanto il capitolo 4, oltre al presente report richiesto; nessun commit.

## Sezioni integrate

- Frontmatter: aggiunti topic IRPEF/IRES, categorie reddituali, reddito complessivo e reddito d'impresa; aggiunta la source redditi; aggiornati `updated_at` e `last_compiled_from`. `companion_to` era gia presente. Stato, confidence e `review_required` sono rimasti invariati.
- Nuovo blocco `IRPEF e IRES: il quadro sistematico`, collocato tra la mappa d'uso del TUIR e il blocco IVA.
- Soggetti IRPEF e categorie di soggetti IRES, con criterio metodologico soggetto-residenza-natura.
- Sequenza IRPEF: redditi di categoria, reddito complessivo, deduzioni, imponibile, imposta lorda, detrazioni e altri scomputi.
- Sei categorie dell'art. 6 e distinzione tra fonte/provento, categoria e criterio di determinazione.
- Raccordo introduttivo tra risultato civilistico e reddito fiscale d'impresa, senza duplicare la meccanica contabile.
- Verifica risolta ed errore tipico specifici.
- Riferimenti consolidati e note di review su dati mobili e manutenzione normativa.

## Fonti e destinazioni

- Source principale: `[[sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18]]`, consolidata nel commit `0368e08`.
- Supporto: `[[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]]`, `[[topics/diritto-tributario-concorsi-agenzie-fiscali]]`, `[[entities/agenzia-delle-entrate]]`.
- Rinvio dichiarativo verificato: `[[books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni#Il ciclo dell'adempimento fiscale]]`.
- Rinvio contabile verificato: `[[books/moduli/m-fc02-agenzie-fiscali/chapters/11-contabilita-aziendale-economia-impresa-fisco#14. Dal bilancio al reddito imponibile]]`.
- Non e' stato letto alcun file in `wiki/raw/`.

## Controlli

- Anchor dei capitoli 6 e 11 trovati con corrispondenza esatta.
- Frontmatter ispezionato: delimitatori integri; `companion_to`, source/topic/entity e `last_compiled_from` presenti.
- UTF-8: nessun carattere di sostituzione, nessun pattern di mojibake rilevato, nessun BOM.
- `git diff --check` superato; solo avviso informativo CRLF/LF.
- Diff completo ispezionato per preservazione della baseline e assenza di sviluppi analitici delle singole categorie.

## Self-review

- Il capitolo 4 assume la responsabilita del quadro sistematico, non della determinazione analitica delle categorie.
- Il capitolo 6 resta responsabile di dichiarazione, liquidazione e versamento.
- Il capitolo 11 resta responsabile della meccanica contabile e degli esercizi sulle variazioni fiscali.
- Non sono stati introdotti aliquote, scaglioni, soglie, importi, percentuali o regimi mobili.
- La distinzione deduzione/detrazione, la funzione classificatoria dell'art. 6 e il ponte civilistico-fiscale sono espliciti e verificabili.

## Concerns

- Il tentativo di richiamo tramite `LocalAgentMemory` non ha completato il caricamento per la risoluzione degli import TypeScript senza estensione nell'esecuzione diretta Node. Si e' proseguito con il wiki consolidato; nessuna memoria e' stata usata come fonte normativa.
- Restano obbligatorie review normativa articolo per articolo e verifica delle fonti ufficiali vigenti prima della pubblicazione.
