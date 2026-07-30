---
id: source-flussi-economici-nsis-modelli-ce-sp
type: source
title: "Flussi economici NSIS - modelli CE e SP"
status: processed
domain: "concorsi pubblici italiani"
topics: ["NSIS", "contabilita sanitaria", "modello CE", "modello SP", "monitoraggio economico"]
entities: ["Ministero della Salute", "Ragioneria generale dello Stato", "Regioni", "Azienda sanitaria"]
source_refs: ["sources/contabilita-budget-aziende-sanitarie", "sources/armonizzazione-contabile-enti-territoriali-d-lgs-118-2011"]
book_refs: ["m-sa01-sanita-amministrativa", "vol-07-sanita-amministrativa-professioni-sanitarie"]
confidence: 0.95
updated_at: 2026-07-30T14:10:00+02:00
created_at: 2026-07-30T14:10:00+02:00
review_required: true
canonical: true
tags: ["source", "m-sa01", "nsis", "ce", "sp", "contabilita-sanitaria"]
source_type: official_primary_and_operational_corpus
source_url: "https://www.salute.gov.it/new/it/tema/programmazione-e-finanziamento-del-ssn/dati-economico-finanziari-regionali/"
source_date: 2026-07-30
authority_level: primary_official
raw_path: "wiki/raw/m-sa01-sanita-amministrativa/fonti/openbdap-spesa-sanitaria-ce-sp.html"
sha256: "38C9E580D86F02FF9D7B56FB6346D944DE161553FDDAA520DFCE037E9CCC78B6"
---

# Flussi economici NSIS - modelli CE e SP

## Fonti ufficiali verificate

Il 30 luglio 2026 sono state ricontrollate:

- la pagina del Ministero della Salute sui dati economico-finanziari regionali;
- la scheda ministeriale "Flussi economici", aggiornata l'8 gennaio 2026;
- la pagina OpenBDAP della Ragioneria generale dello Stato sulla spesa sanitaria;
- il Vademecum RGS per il controllo e la vigilanza negli enti del SSN;
- il decreto del Ministro della salute, di concerto con il Ministro dell'economia e delle finanze, 24 maggio 2019, pubblicato nella Gazzetta Ufficiale n. 147 del 25 giugno 2019, che adotta i modelli CE e SP.

Il corpus locale contiene il file ministeriale sui dati economico-finanziari, lo snapshot OpenBDAP e il Vademecum RGS, tutti registrati nel manifest M-SA01. Il decreto del 2019 aggiorna i modelli; per questo le scadenze e le istruzioni di compilazione non vanno dedotte da documenti precedenti senza verifica corrente.

## Scheda CE

### Finalità

Il modello Conto economico (CE) rileva costi e ricavi degli enti del Servizio sanitario regionale e sostiene monitoraggio della spesa, consolidamento, comparazioni, proiezioni e verifica degli equilibri economici. È un modello standardizzato di comunicazione economico-finanziaria e non sostituisce il bilancio o la contabilità dell'ente.

### Soggetto alimentante

OpenBDAP indica che il CE è trasmesso al NSIS da ciascun ente del Servizio sanitario regionale e dalla Regione dopo le necessarie operazioni di consolidamento. Il Ministero include, nel perimetro descritto, aziende sanitarie locali, aziende ospedaliere, IRCCS pubblici e aziende ospedaliero-universitarie secondo la disciplina applicabile.

### Unità di rilevazione

L'unità è l'ente o l'aggregato regionale identificato nel modello per un determinato periodo contabile. Le voci rappresentano componenti economiche, in particolare costi e ricavi, secondo lo schema vigente. Non sono episodi assistenziali individuali.

### Periodicità

OpenBDAP descrive trasmissioni CE a preventivo, trimestrali e a consuntivo annuale. La banca dati pubblica ministeriale espone dati annuali a consuntivo. Scadenze, versioni, rettifiche e calendari regionali sono mobili e devono essere verificati nelle istruzioni ministeriali e regionali vigenti per l'esercizio considerato.

### Controlli, responsabilità e uso

I controlli devono collegare il modello alla contabilità dell'ente, verificare completezza e quadratura delle voci, coerenza temporale, corretto perimetro e consolidamento regionale. L'ente alimenta e valida secondo il proprio assetto; la Regione consolida e trasmette nel quadro previsto; Ministero e tavoli di monitoraggio utilizzano i dati nelle rispettive funzioni. Ruoli interni, firme, rettifiche ed escalation dipendono dalle procedure vigenti. Il CE è usato per monitoraggio infrannuale e annuale, proiezioni del risultato, comparazioni e controllo degli equilibri.

## Scheda SP

### Finalità

Il modello Stato patrimoniale (SP) rileva attività e passività e completa la lettura della gestione con la dimensione patrimoniale. È distinto dal CE: il primo rappresenta consistenze patrimoniali, il secondo componenti economiche del periodo.

### Soggetto alimentante

OpenBDAP indica che lo SP è inviato al NSIS da ogni ente del Servizio sanitario regionale e da ogni Regione. Il perimetro soggettivo va controllato con la disciplina e il modello applicabili all'esercizio.

### Unità di rilevazione

L'unità è l'ente o l'aggregato regionale per l'esercizio e la data di riferimento del modello. Le voci rappresentano consistenze patrimoniali secondo lo schema vigente. Non è un inventario informale e non descrive singoli ricoveri.

### Periodicità

Il Vademecum RGS descrive lo SP come rendicontazione annuale a consuntivo; la banca dati ministeriale pubblica dati SP annuali. La periodicità applicativa, la data di riferimento, le scadenze e le finestre di rettifica devono comunque essere controllate nelle istruzioni correnti, poiché modelli e regole sono stati aggiornati nel tempo.

### Controlli, responsabilità e uso

I controlli riguardano completezza e quadratura del modello, corrispondenza con la fonte contabile, coerenza tra saldi iniziali e finali e raccordi pertinenti con variazioni economiche. L'ente alimenta e valida secondo il proprio assetto; la Regione consolida e trasmette; il livello nazionale usa il flusso per monitoraggio e comparazione. Il modello consente di analizzare struttura patrimoniale, attività, passività e variazioni, insieme ma non in sostituzione del CE e del bilancio.

## Distinzioni e parti mobili

CE e SP non sono sinonimi, né versioni dello stesso prospetto: oggetto, struttura e periodicità differiscono. Restano mobili schemi, voci, codici, istruzioni, controlli automatici, scadenze, modalità di trasmissione, responsabilità interne e calendari regionali. La review amministrativo-contabile deve verificare il decreto e le istruzioni applicabili al cut-off editoriale.
