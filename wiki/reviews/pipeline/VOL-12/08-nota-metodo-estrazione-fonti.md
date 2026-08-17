---
id: pipeline-vol-12-08-nota-metodo-estrazione
type: pipeline_review
title: "VOL-12 — Nota di metodo: estrazione delle fonti e correzioni conseguenti"
volume_code: VOL-12
phase: B
scope: volume
domain: "concorsi pubblici italiani"
updated_at: 2026-08-12T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "metodo", "correzioni"]
---

# VOL-12 — Nota di metodo: estrazione delle fonti e correzioni conseguenti

## Il difetto

Tutte le fonti PDF del volume sono state estratte con `pdftotext` senza l'opzione `-layout`. Su documenti discorsivi il risultato è corretto. **Su tabelle e allegati tabellari il testo viene scomposto in colonne slegate**, e il contenuto risulta illeggibile o, peggio, leggibile in modo sbagliato.

Il difetto è stato scoperto scrivendo il capitolo pilota di M-SP02: l'allegato B del bando 400 sembrava contenere solo un elenco di categorie di patente, mentre conteneva anche i punteggi.

## Le tre correzioni che ne sono derivate

### 1. I valori dei parametri fisici sono nel regolamento, non nelle direttive tecniche

La source note [[sources/parametri-fisici-concorsi-dpr-207-2015-vol-12]] affermava che i valori numerici dei tre parametri fossero fissati solo da direttive tecniche e non andassero scritti in capitolo.

**Sbagliato.** Il d.P.R. 207/2015 ha un **Allegato A, «di cui all'articolo 3, comma 1»**, che li fissa:

| Parametro | Maschi | Femmine |
| --- | --- | --- |
| forza muscolare (handgrip, kg) | 40 | 20 |
| composizione corporea (% massa grassa) | fra 7 e 22 | fra 12 e 30 |
| massa metabolicamente attiva (% massa magra teorica) | 40 | 28 |

Le direttive tecniche governano le **modalità di accertamento**, non i valori. Conseguenza editoriale: i valori possono e devono essere dati al lettore, perché sono **verificabili in anticipo** con un dinamometro e una bioimpedenziometria. È un'informazione azionabile mesi prima della domanda.

### 2. La logica di valutazione delle prove fisiche dell'Arma

La source note [[sources/prove-efficienza-fisica-accertamenti-forze-di-polizia-m-sp01]] sosteneva che nella Polizia di Stato «conta superare» e nell'Arma «conta anche quanto si supera», sulla base di tabelle lette male.

**Sbagliato.** Entrambi i corpi adottano un impianto di idoneità con bonus contenuto, non un sistema a punteggi graduati. La differenza reale è un'altra: **l'Arma prevede una prova facoltativa** — salto in alto a 130 o 140 cm, fino a 1 punto — che la Polizia di Stato non ha. È l'unico margine discrezionale del sistema, a costo zero perché la rinuncia non è penalizzata.

### 3. I punteggi dei titoli nel concorso dei vigili del fuoco

L'allegato B del bando 400 assegna da 1 a 5 punti in funzione della patente posseduta, con punteggi **non cumulabili**. Senza il layout, la corrispondenza patente-punti era invisibile e la sezione del capitolo pilota si era fermata all'elenco delle categorie.

## Regola operativa

**Ogni PDF con contenuto tabellare va estratto con `pdftotext -layout`.** L'estrazione senza layout è ammessa solo per verificare la presenza di un documento o per cercare stringhe, mai per leggerne il contenuto ai fini editoriali.

Quando la corrispondenza fra colonne resta ambigua anche con il layout, il dato va classificato **DA VERIFICARE** e non ricostruito per allineamento presunto.

## Ripasso sistematico — esito

Tutte le sette fonti sono state riestratte con `-layout`. Due hanno prodotto risultati sostanziali.

### Carriera prefettizia — la struttura reale delle prove scritte

L'audit precedente riportava genericamente «cinque prove scritte». L'articolato dice molto di più:

| | Prova | Durata |
| --- | --- | --- |
| a) | tre elaborati: amministrativo e/o costituzionale · civile · storia contemporanea e della PA | 8 ore ciascuno |
| b) | risoluzione di un **caso** giuridico-amministrativo o gestionale-organizzativo | 7 ore |
| c) | **traduzione con vocabolario**, inglese o francese | 4 ore |

**Trentacinque ore complessive di prove scritte**, svolte in modalità digitale, contro le ventiquattro della magistratura ordinaria. È la prova di scrittura più pesante dell'intero volume.

Due elementi che il modulo trattava male: la prova b) **non è un tema** ma una simulazione di problem solving dirigenziale, e la prova c) **non è una prova di lingua orale** ma una traduzione scritta con vocabolario. Entrambe richiedono allenamenti propri.

L'orale aggiunge sociologia e scienza dell'organizzazione, scienza delle finanze, diritto penale limitato a parti determinate del codice, legislazione speciale del Ministero dell'Interno, contabilità di Stato, e una **verifica applicativa di informatica**.

Riferimento regolamentare individuato: d.i. 4 giugno 2002, n. 144, modificato nel 2007 e nel 2017.

### d.m. 166/2019 — l'Allegato A è verificato ma non pubblicabile

L'Allegato A, richiamato dall'articolo 1, contiene le **cause di non idoneità** per i ruoli operativi del Corpo. È un elenco clinico analitico: malattie infettive con indicazione di singole positività sierologiche, patologie respiratorie e allergiche in relazione all'uso dei dispositivi di protezione, e via elencando.

**Fonte verificata, contenuto da non riprodurre.** Un elenco diagnostico in un manuale di preparazione concorsuale è inutile al lettore e potenzialmente dannoso: induce autodiagnosi e autoesclusioni su un giudizio che spetta alla commissione medica dell'amministrazione.

Il trattamento editoriale corretto è dire al lettore che l'allegato esiste, che cosa disciplina e dove si trova, e invitare chi ha una condizione nota a verificarla con il proprio medico prima di presentare domanda. **Il capitolo non elenca patologie.**

È un caso istruttivo: una fonte può essere pienamente verificata e non appartenere comunque al libro. La verifica riguarda l'attendibilità, non l'opportunità.

### Le altre cinque

`cc-bando-3081`, `cc-ist16-898` e relativo decreto di modifica, `gdf-bando-983`, `maeci-35`, `vvf-bando-400` sono stati riestratti e restano disponibili in versione leggibile per la fase C. Non hanno prodotto correzioni a quanto già scritto, ma le rispettive tabelle di riserve, contingenti e titoli sono ora leggibili e andranno usate al momento della scrittura dei capitoli corrispondenti.

## Rilievo generale

Il difetto non ha prodotto contenuto inventato: le affermazioni sbagliate erano interpretazioni prudenti di dati incompleti, ed erano dichiarate come tali. Ha però prodotto **due conclusioni editoriali errate su tre**, entrambe in aree che sarebbero finite in capitolo.

È la conferma pratica del principio già scritto nella Bibbia del Volume: la qualità di un capitolo dipende meno dalla scrittura che dalla completezza della lettura della fonte.
