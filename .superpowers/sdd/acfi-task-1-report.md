# Task 1 ACFI - Report di implementazione

## Stato

DONE_WITH_CONCERNS

## File creati

- `wiki/sources/fiscalita-internazionale-acfi-aggiornamento-2026-07-18.md`
- `wiki/raw/m-fc02-agenzie-fiscali/ae-bando-350-funzionari-acfi-2025.pdf`
- `wiki/raw/m-fc02-agenzie-fiscali/gazzetta-dm-14-maggio-2018-transfer-pricing.html` - landing/indice ufficiale dell'atto
- `wiki/raw/m-fc02-agenzie-fiscali/gazzetta-serie-generale-118-2018-transfer-pricing.pdf` - fascicolo ufficiale con testo integrale
- `wiki/raw/m-fc02-agenzie-fiscali/oecd-model-tax-convention-update-2025.pdf`
- `wiki/raw/m-fc02-agenzie-fiscali/oecd-transfer-pricing-guidelines-2022.pdf`
- `wiki/raw/m-fc02-agenzie-fiscali/oecd-co-operative-tax-compliance-tcf-2016.pdf`

## File fornito dall'utente

- `wiki/raw/m-fc02-agenzie-fiscali/ae-provvedimento-360494-2020-documentazione-transfer-pricing.pdf` - copia ufficiale fornita dall'utente, verificata ma non modificata.

Raw ufficiali preesistenti riusati senza modifiche:

- `wiki/raw/m-fc02-agenzie-fiscali/ae-avviso-350-funzionari-acfi-2025.html`
- `wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-917-1986-tuir.html`
- `wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-128-2015-adempimento-collaborativo.html`

## URL ufficiali e versioni

| Documento | URL ufficiale | Versione/data | Audit |
| --- | --- | --- | --- |
| Pagina e bando AE 350 ACFI | https://www.agenziaentrate.gov.it/portale/avviso-del-18-aprile-2025 | Bando prot. 187311/2025; pagina aggiornata 6 febbraio 2026 | 18 luglio 2026 |
| Provvedimento documentazione TP | Copia ufficiale fornita dall'utente | Prot. AGE.AGEDC001.REGISTRO UFFICIALE.0360494.23-11-2020-U; PDF 1.4, 14 pagine; SHA-256 CA6CFC50E77DFA83C3B647E6E31C169FDA49E9FCEA442972FA6E042F3405C80E | Identita verificata localmente |
| TUIR | https://www.normattiva.it/eli/id/1986/12/31/086U0917 | ELI ufficiale generico; raw dell'espressione vigente al 1 luglio 2026; ultimo aggiornamento dell'atto segnalato 22 maggio 2026 | Consultazione 18 luglio 2026 |
| Decreto MEF transfer pricing | https://www.gazzettaufficiale.it/eli/id/2018/05/23/18A03544/sg e https://www.gazzettaufficiale.it/eli/gu/2018/05/23/118/sg/pdf | HTML landing/indice dell'atto; fascicolo PDF ufficiale con testo integrale del decreto 14 maggio 2018 | 18 luglio 2026 |
| D.Lgs. 128/2015 | https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=15G00146 | Testo vigente; aggiornamenti acquisiti nel raw locale | 18 luglio 2026 |
| Aggiornamento Modello OCSE | https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/11/the-2025-update-to-the-oecd-model-tax-convention_c7031e1b/5798080f-en.pdf | Update 2025, approvato dal Consiglio OCSE il 18 novembre 2025 | 18 luglio 2026 |
| Linee guida OCSE transfer pricing | https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/01/oecd-transfer-pricing-guidelines-for-multinational-enterprises-and-tax-administrations-2022_57104b3a/0e655865-en.pdf | Edizione gennaio 2022 | 18 luglio 2026 |
| OCSE Tax Control Framework | https://www.oecd.org/content/dam/oecd/en/publications/reports/2016/05/co-operative-tax-compliance_g1g66744/9789264253384-en.pdf | Edizione 13 maggio 2016 | 18 luglio 2026 |

## Perimetro estratto dal bando

Il PDF ufficiale e' stato estratto localmente. Il profilo:

- cura ammissione e requisiti dell'adempimento collaborativo;
- analizza e monitora il TCF;
- definisce in contraddittorio la mappa dei rischi e la verifica periodicamente;
- coordina la risk analysis delle posizioni fiscali;
- gestisce interlocuzione preventiva, compliance e controllo preventivo del rischio;
- indirizza i controlli dichiarativi dei soggetti ammessi;
- segue ICAP e transfer pricing con le multinazionali;
- cura il dialogo con imprese estere nella cooperazione e collaborazione rafforzata.

La prova comprende tributario/teoria dell'imposta, civile-commerciale, amministrativo, contabilita aziendale, penale tributario e casi fiscali in inglese. La source note mantiene il perimetro selettivo del brief: residenza, stabile organizzazione, convenzioni/doppia imposizione, transfer pricing, infragruppo, rischio e TCF.

## Controlli eseguiti

- esistenza e dimensione non nulla di ogni raw creato;
- firma `%PDF-` per i PDF;
- presenza di stringhe identificative nei raw HTML;
- frontmatter della source note: campi canonici, source URL, source date, authority level, raw refs;
- risoluzione di tutti i raw refs;
- risoluzione dei wikilink della source note;
- scansione UTF-8/mojibake;
- `git diff --check` sui soli file del task;
- controllo del perimetro con `git status --short` filtrato ai file autorizzati;
- nessun commit.

## Self-review

La nota distingue norme interne, convenzioni, Modello/Linee guida OCSE e prassi. Non contiene aliquote, soglie o termini mobili. Residenza, stabile organizzazione, transfer pricing e TCF sono presentati come metodi di qualificazione, non come automatismi. Il caso integra i nuclei senza anticipare testo editoriale di capitolo. Lo stato resta `consolidated` e `review_required: true`; non viene dichiarata copertura `completo`.

## Limiti e preoccupazioni

Il blocco S1 e' risolto dalla copia ufficiale fornita dall'utente. L'identita del provvedimento e' confermata da oggetto, protocollo, data, struttura in otto punti, motivazioni, riferimenti normativi, firma PDF e hash corrispondente. La source e' riportata a status consolidated.

Resta una concern: l'acquisizione prova il contenuto del provvedimento 2020, ma non certifica da sola che nessuna modifica o prassi successiva incida su termini e modalita operative al 18 luglio 2026. La source evita pertanto valori mobili e richiede verifica ufficiale puntuale prima dell'applicazione a una fattispecie.


## Fix review S1/Q1/Q2

- S1: risolto tramite copia ufficiale fornita dall'utente, verificata localmente; source riportata a consolidated.
- Q1: aggiunto il fascicolo PDF integrale GU n. 118/2018; HTML qualificato come landing/indice.
- Q2: URL TUIR riconciliato con ELI generico; separate consultazione 18 luglio 2026, espressione vigente 1 luglio 2026 e ultimo aggiornamento atto 22 maggio 2026.
## Controlli sulla copia fornita

- firma file: PDF 1.4;
- pagine estratte: 14;
- protocollo: AGE.AGEDC001.REGISTRO UFFICIALE.0360494.23-11-2020-U;
- oggetto coerente con documentazione idonea e decreto MEF 14 maggio 2018;
- struttura verificata: definizioni, Masterfile, Documentazione Nazionale, stabili organizzazioni, PMI, forma ed efficacia, comunicazione, servizi a basso valore aggiunto e decorrenza;
- SHA-256 calcolato: CA6CFC50E77DFA83C3B647E6E31C169FDA49E9FCEA442972FA6E042F3405C80E, corrispondente al valore fornito.