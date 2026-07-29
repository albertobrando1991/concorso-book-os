# Task 3 — Completamento IRPEF/IRES nel capitolo 6

## Contesto approvato

- Corpus e source note consolidati nel commit `0368e08`.
- Quadro sistematico del capitolo 4 approvato nel commit `ba1f58f`.
- Il capitolo 6 puo contenere modifiche preesistenti: devono essere preservate.

## Scope tassativo

Modificare esclusivamente:

`wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md`

Non modificare governance, memoria, source note o altri capitoli. Non eseguire commit.

## Fonti ammesse

Usare la source note consolidata `wiki/sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md` e, per coordinamento didattico, i capitoli 4 e 11. Non derivare il testo finale direttamente dal file raw.

## Requisiti editoriali

1. Rilevare e riportare stat/hash iniziali e diff finale del file, preservando le modifiche preesistenti.
2. Aggiornare coerentemente il frontmatter (fonti, data di compilazione e tracciabilita), senza innalzare automaticamente `status` o `confidence`.
3. Trattare a livello didattico 3 tutte le sei categorie reddituali dell'art. 6 TUIR:
   - redditi fondiari: fonte, categorie interne e logica catastale;
   - redditi di capitale: funzione, distinzione dai redditi diversi e criterio generale di determinazione;
   - redditi di lavoro dipendente: nozione funzionale e principio di onnicomprensivita, con formulazione prudente;
   - redditi di lavoro autonomo: abitualita, distinzione dall'impresa e logica selettiva di determinazione;
   - redditi d'impresa: soggetti, fonte e determinazione;
   - redditi diversi: residualita tipizzata e principali famiglie di interesse concorsuale.

   Per ciascuna categoria inserire, in misura adeguata: definizione, funzione, elementi, distinzioni, logica di determinazione, conseguenze operative, esempio, domanda/prospettiva concorsuale, errore tipico e criterio di verifica.
4. Spiegare soggetti e struttura dell'IRES.
5. Sviluppare i principi del reddito d'impresa: derivazione dal risultato civilistico, competenza, inerenza (con prudenza e distinguendo il dato testuale dalla costruzione interpretativa), imputazione, variazioni fiscali, principali componenti positivi e negativi. Rinviare con ancora precisa al capitolo 11 per la base contabile, senza duplicarla.
6. Inserire applicazioni autosufficienti:
   - caso IRPEF con piu componenti da classificare;
   - caso IRES dal risultato civilistico al reddito imponibile;
   - esercizio sulla distinzione deduzione/detrazione;
   - quiz, risposta modello alla commissione, trappole/errori e checklist operativa.
   Gli eventuali numeri devono essere dichiarati pedagogici e non presentati come parametri mobili vigenti.
7. Inserire rinvii precisi e verificabili ai capitoli 4 e 11.
8. Curare riferimenti, nota di revisione, collegamenti e autonomia didattica del capitolo.
9. Verificare frontmatter, link, codifica e diff finale.

## Anti-duplicazione

- Non replicare il quadro sistematico gia collocato nel capitolo 4.
- Non replicare la disciplina contabile gia collocata nel capitolo 11.
- Il capitolo 6 deve fornire la trattazione tributaria teorica e operativa completa necessaria al candidato.

## Report obbligatorio

Creare `.superpowers/sdd/redditi-task-3-report.md` con:

- baseline e file modificati;
- sintesi delle integrazioni;
- mappa requisiti/sezioni;
- controlli eseguiti e relativi esiti;
- diffstat finale;
- eventuali limiti residui.
