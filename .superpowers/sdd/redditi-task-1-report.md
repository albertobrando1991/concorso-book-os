# Redditi Task 1 — report

## Stato

DONE_WITH_REVIEW_NOTES

## Obiettivo ed esito

Creata la source note articolo-specifica per IRPEF, IRES, categorie reddituali e reddito d'impresa, senza modificare capitoli, matrici, index, log o memoria. Il nucleo resta dichiarato parziale e non pubblicabile fino a integrazione e review.

## Fonti e versioni

Fonte primaria: D.P.R. 22 dicembre 1986, n. 917, portale ufficiale Normattiva.

Riferimenti temporali separati:

- data richiesta e riferimento della richiesta di export: 1 luglio 2026;
- identificatore AKN della FRBRExpression acquisita: ita@2026-05-23;
- data di consultazione e acquisizione: 18 luglio 2026;
- ultimo aggiornamento dell'atto indicato dal portale: 22 maggio 2026.

Fonti wiki di raccordo:

- [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]]
- [[sources/contabilita-aziendale-bilancio-reddito-impresa-aggiornamento-2026-07-18]]

Il raw HTML preesistente conteneva i metadati ufficiali e il solo art. 1, poiche' Normattiva carica dinamicamente gli altri articoli. Il primo tentativo di download diretto e' fallito per DNS; un secondo tentativo sul collegamento Akoma Ntoso senza sessione ha restituito una pagina di errore e non e' stato conservato. Mediante sessione ufficiale Normattiva e referer dell'atto e' stato infine acquisito l'export integrale.

## Raw ufficiali

- wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-917-1986-tuir.html — raw preesistente, metadati e art. 1.
- wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-917-1986-tuir-akn-vigente-2026-07-01.xml — nuovo export ufficiale integrale Akoma Ntoso.

Controlli sull'XML:

- dimensione: 1.998.905 byte;
- elementi articolo: 236;
- SHA-256: 4C0FF42461D791C50D75878A42BD778D5548F7F2AFD74DDD189768663ADDE8DA;
- XML parsabile con namespace Akoma Ntoso ufficiale.

## Mappa articolo-istituto verificata

IRPEF e categorie:

- artt. 1-3: presupposto, soggetti, base imponibile;
- art. 6: classificazione delle sei categorie;
- artt. 7-8: periodo e reddito complessivo;
- artt. 10-12 e seguenti: deduzioni, determinazione dell'imposta, detrazioni;
- artt. 23 e 25 e seguenti: non residenti e redditi fondiari;
- art. 44 e seguenti: capitale;
- artt. 49 e 51: lavoro dipendente e determinazione;
- artt. 53-54: lavoro autonomo e determinazione;
- artt. 55-56: impresa e determinazione;
- artt. 67-68 e disposizioni collegate: redditi diversi e regole delle fattispecie.

IRES e reddito d'impresa:

- artt. 72-73: presupposto e soggetti;
- artt. 75-76: base imponibile e periodo;
- artt. 81 e 83: reddito complessivo e determinazione;
- artt. 85-89: ricavi, plusvalenze, sopravvenienze, dividendi e interessi;
- art. 92: variazioni delle rimanenze dei beni disciplinati dalla disposizione;
- art. 93: opere, forniture e servizi di durata ultrannuale, con disciplina distinta;
- artt. 95-96, 99, 101-102, 107-109: lavoro, interessi, oneri fiscali, perdite, ammortamenti, accantonamenti, spese pluriennali e norme generali.

Rubriche e presenza di tutti gli articoli sopra sono state lette direttamente nell'XML ufficiale.

## File creati

- wiki/sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md
- wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-917-1986-tuir-akn-vigente-2026-07-01.xml
- .superpowers/sdd/redditi-task-1-report.md

Nessun altro file e' stato modificato da questo task. Nessun commit.

## Contenuto consolidato

La source note contiene:

- frontmatter canonico;
- esito audit e distinzione delle date;
- perimetro e divisione funzionale tra capitoli 4, 6 e 11;
- mappe IRPEF e IRES;
- funzione, criteri, fonte/provento, determinazione selettiva, distinzioni e raccordo col reddito complessivo per le sei categorie;
- sequenza deduzioni–imponibile–imposta–detrazioni;
- reddito d'impresa: risultato civilistico, derivazione, competenza, imputazione, raccordo ex art. 109, comma 5, e variazioni;
- componenti positivi e negativi essenziali;
- raccordo contabile e metodo dei casi;
- limiti, review, raw refs e link consolidati.

## Correzioni S1/Q1/Q2

- S1: separate data richiesta/riferimento 1 luglio 2026, FRBRExpression ita@2026-05-23, consultazione 18 luglio 2026 e aggiornamento dell'atto 22 maggio 2026; aggiornati frontmatter e provenienza.
- Q1: limitato il claim normativo al perimetro dell'art. 109, comma 5; la formula qualitativa sull'inerenza e' esplicitamente una sintesi elaborativa soggetta a verifica specialistica.
- Q2: separati art. 92, variazioni delle rimanenze, e art. 93, opere, forniture e servizi ultrannuali, con descrizioni prudenti.
- Il raw ufficiale e' rimasto immutato; hash riconfermato.

## Controlli ed esiti

- frontmatter: campi canonici e source-specific presenti;
- stato: consolidated per la source note; nessuna marcatura completo del nucleo;
- raw refs: entrambi i file esistenti e tracciati;
- XML: parsabile, 236 articoli, hash registrato e immutato; FRBRExpression verificata come ita@2026-05-23;
- wikilink: target esistenti;
- encoding: UTF-8 senza BOM per note e report;
- mojibake e sequenze spurie: assenti;
- valori mobili: nessuna aliquota, scaglione, soglia, importo, percentuale o termine operativo;
- git diff --check: eseguito sui file di task;
- scope: nessun capitolo, matrice, index, log o memoria modificati;
- commit: non eseguito.

## Self-review

La mappa e' selettiva e non enciclopedica. Le categorie non sono semplicemente elencate: per ciascuna sono indicati funzione classificatoria, criteri, regola di determinazione a livello stabile, categorie contigue e confluenza nel reddito complessivo. Per il reddito d'impresa e' preservata la distinzione tra contabilita e fiscalita e tra esistenza, imputazione, riferibilita ex art. 109, comma 5, e deducibilita. La nozione qualitativa di inerenza e' marcata come sintesi elaborativa da verificare, non come formula testuale attribuita al TUIR.

La nota evita di cristallizzare dati mobili e non trasforma la source note in testo di capitolo. La divisione 4/6/11 e' esplicita.

## Concerns e review residue

- Prima della pubblicazione occorre verificare il testo vigente dei singoli commi, non soltanto presenza e rubrica degli articoli.
- La derivazione rafforzata richiede review specialistica per soggetto, principi contabili ed eccezioni.
- Art. 68 non esaurisce tutte le regole di determinazione dei redditi diversi: ogni fattispecie va collegata alla disposizione pertinente.
- Regimi sostitutivi, tassazione separata, trasparenza, consolidato, enti non commerciali, non residenti e discipline agevolative restano fuori dal nucleo salvo fonte dedicata.