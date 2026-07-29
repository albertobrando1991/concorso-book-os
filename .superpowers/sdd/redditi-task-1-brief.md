# Task 1: Corpus TUIR articolo-specifico

## Contesto

M-FC02 ha un nucleo `parziale` su IRPEF/IRES, categorie reddituali e reddito d'impresa. Questo task deve creare la fonte consolidata utilizzabile dai writer; non modifica ancora i capitoli.

## Vincoli

- Divisione funzionale tra capitoli 4, 6 e 11; nessun nuovo capitolo.
- Nessun claim editoriale deriva direttamente dai raw.
- Nessuna aliquota, scaglione, soglia, importo o regime mobile non verificato.
- Preservare tutte le modifiche preesistenti.
- Non marcare il nucleo `completo`.

## File

- Leggere `wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-917-1986-tuir.html`.
- Leggere `wiki/sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md`.
- Leggere `wiki/sources/contabilita-aziendale-bilancio-reddito-impresa-aggiornamento-2026-07-18.md`.
- Creare `wiki/sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md`.
- Creare nuovi raw ufficiali solo se necessari a integrare/sostituire la versione TUIR già acquisita.

## Requisiti

1. Verificare su fonte ufficiale la versione TUIR al 18 luglio 2026, separando consultazione, espressione vigente e ultimo aggiornamento.
2. Costruire una mappa articolo-istituto verificata: soggetti/passività IRPEF e IRES; art. 6 e categorie; reddito complessivo e sequenza deduzioni–imponibile–imposta–detrazioni; fondiari; capitale; dipendente; autonomo; impresa; diversi; principi e componenti essenziali del reddito d'impresa.
3. Trattare con precisione almeno: funzione della categoria, criteri soggettivi, fonte/provento, regola selettiva di determinazione, distinzione dalle categorie contigue, raccordo col reddito complessivo.
4. Per reddito d'impresa consolidare: rapporto risultato civilistico–imponibile, derivazione, competenza, inerenza, imputazione, variazioni fiscali, componenti positivi/negativi essenziali, senza enciclopedismo.
5. Inserire frontmatter canonico, esito audit, perimetro, mappa normativa, definizioni/distinzioni, raccordo contabile, metodo dei casi, limiti/review, raw refs e link consolidati.
6. Non modificare capitoli, matrici, report, index/log/memoria. Non commit.
7. Verificare frontmatter, raw refs, wikilink, UTF-8, mojibake e `git diff --check`.

## Report

Scrivere `.superpowers/sdd/redditi-task-1-report.md` con fonti/versioni, mappa articoli, file creati, controlli ed esiti, self-review e concerns. In chat restituire stato breve.
