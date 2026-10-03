---
id: source-procurement-farmaci-dispositivi-flussi-nsis
type: source
title: "Procurement sanitario, farmaci, dispositivi e flussi informativi NSIS"
status: processed
domain: "concorsi pubblici italiani"
topics: ["procurement sanitario", "farmaci", "dispositivi medici", "NSIS", "SDO"]
entities: ["Ministero della Salute", "AIFA", "ANAC"]
source_refs: ["sources/codice-contratti-pubblici-d-lgs-36-2023-e-correttivo-209-2024", "sources/ciclo-contratti-pubblici-rup-stazione-appaltante-operatore-economico", "sources/procedure-affidamento-gare-appalti-concessioni-soglie", "sources/digitalizzazione-contratti-pubblici-anac-bdncp-fvoe-pcp", "sources/flusso-sdo-scheda-dimissione-ospedaliera", "sources/flussi-economici-nsis-modelli-ce-sp"]
book_refs: ["vol-07-sanita-amministrativa-professioni-sanitarie", "m-sa01-sanita-amministrativa"]
confidence: 0.9
updated_at: 2026-10-02
created_at: 2026-07-29T16:48:00+02:00
review_required: true
canonical: true
tags: ["source", "m-sa01", "procurement", "farmaci", "dispositivi", "nsis", "sdo"]
source_type: official_operational_corpus
source_url: "https://www.aifa.gov.it/osservatorio-impiego-medicinali-osmed"
source_date: 2026-07-29
authority_level: official_operational
raw_path: "wiki/raw/m-sa01-sanita-amministrativa/fonti/osmed-aifa.html"
sha256: "8128A589094E4BBD674B03B85146EA34AB2973CD870C49DB9A259F32681F9D9A"
---

# Procurement sanitario, farmaci, dispositivi e flussi NSIS

## Confine con il nucleo comune

Programmazione, progettazione, affidamento, esecuzione, RUP, piattaforme, BDNCP e tracciabilità sono rinviati alle source note del VOL-01 sul D.Lgs. 36/2023 e sul correttivo. Nel corpus verificato M-SA01 aggiunge il fabbisogno clinico-organizzativo e la continuità della fornitura per i farmaci, oltre ai flussi specifici SDO, CE e SP. Per definizione e regime dei dispositivi si usa il raccordo MDR/IVDR aggiornato sotto; i claim sui relativi flussi NSIS restano esclusi finché non sostenuti da una fonte valida.

## Fonti locali verificate e capture escluse

Il perimetro attivo usa lo snapshot AIFA dell'OsMed per farmaci e spesa farmaceutica, il D.M. 7 dicembre 2016, n. 261 in Gazzetta per la SDO, il D.M. 24 maggio 2019 in Gazzetta e lo snapshot OpenBDAP per CE e SP, oltre alle source note verificate sui contratti pubblici. Le capture `patrimonio-informativo-nsis-ministero.html` e `monitoraggio-consumi-dispositivi-ministero.html` contengono soltanto una challenge Gcore: il manifest le marca `blocked` e `valid_corpus: false`. Restano conservate per audit ma sono escluse dal corpus attivo; nessun claim di questa nota dipende da quei file.

## Farmaci e dispositivi

### Integrazione verificata il 2 ottobre 2026

L'AIC autorizza l'immissione in commercio dopo valutazione di qualità, sicurezza ed efficacia; la decisione sul rimborso è distinta. La procedura centralizzata comprende valutazione EMA e autorizzazione della Commissione europea, mentre AIFA interviene nel procedimento nazionale e nella classificazione italiana. Le classi A e H individuano medicinali a carico del SSN secondo condizioni e ambiti ammessi; la C individua in via ordinaria medicinali a carico del cittadino. La classe non coincide con regime di fornitura, obbligo di ricetta o scelta terapeutica. Fonti: [AIFA, procedura centralizzata](https://www.aifa.gov.it/en/procedura-di-autorizzazione-centralizzata), [classi](https://www.aifa.gov.it/en/-/elenco-dei-farmaci-autorizzati), [elenchi correnti A e H](https://www.aifa.gov.it/liste-farmaci-a-h). La C(nn) distingue medicinali non ancora valutati ai fini del rimborso; non viene usata per inferire inefficacia.

La centralizzazione degli acquisti sanitari collega art. 9 D.L. 66/2014 e art. 1, commi 548–550, L. 208/2015: per le categorie e condizioni previste occorre utilizzare centrali regionali/Consip e, nei casi disciplinati, altri soggetti aggregatori. Il capitolo insegna la verifica preventiva dell'obbligo, senza pubblicare soglie non consolidate. [ANAC, vademecum](https://www.anticorruzione.it/-/soggetti-aggregatori-il-vademecum-di-anac-1). Il Nodo di smistamento degli ordini veicola documenti elettronici di ordinazione fra enti SSN e fornitori; non sostituisce gara, contratto o fattura. Fonte [RGS, Linee guida NSO 1.5, §3.1](https://www.rgs.mef.gov.it/_Documenti/VERSIONE-I/e-GOVERNME1/apir/NSO-Linee-guida-IT.pdf).

Rotazione FEFO, separazione delle scorte non disponibili e conservazione secondo le condizioni del prodotto sono principi delle [GDP europee del 5 novembre 2013](https://eur-lex.europa.eu/legal-content/IT/ALL/?uri=uriserv%3AOJ.C_.2013.343.01.0001.01.ITA), §§5.5, 6 e 9; il loro ambito regolatorio è la distribuzione dei medicinali. L'esempio di magazzino li impiega come principi logistici, senza assimilare ogni deposito ospedaliero a un grossista né fissare temperature universali. La catena del freddo richiede mantenimento e documentazione delle condizioni autorizzate, con gestione delle escursioni. Il punto di riordino consumo durante il tempo di approvvigionamento più scorta di sicurezza è un modello didattico, subordinato a variabilità, ordini aperti e utilizzabilità.

Per definizione, classificazione e vigilanza dei dispositivi il raccordo attivo è [[sources/dispositivi-medici-ivd-vigilanza-rischio-tecnologico-2026]] e il capitolo M-SA04/04; ciò non sana la capture ministeriale sui flussi NSIS, che resta esclusa.

Lo snapshot verificato AIFA documenta che l'Osservatorio nazionale sull'impiego dei medicinali monitora consumi e spesa dei medicinali erogati a carico del SSN e integra più fonti informative. Sostiene il lessico e la logica del controllo farmaceutico, non una procedura aziendale universale di magazzino.

Per i dispositivi medici il corpus locale non contiene, allo stato, una pagina ministeriale valida alternativa alla capture Gcore. La nota non consolida quindi quantità, campi, contratti o caratteristiche di un flusso nazionale sui consumi dei dispositivi. Gli esempi su acquisto, ricevimento, tracciabilità e magazzino restano limitati alla logica generale di procurement e controllo interno già sostenuta dalle source note sui contratti; i claim specifici sui dispositivi richiedono una nuova fonte ufficiale valida prima della pubblicazione.

Per i casi concorsuali il ciclo minimo è: rilevazione del fabbisogno, programmazione/acquisto, ordine, ricevimento e controllo, carico e tracciabilità, distribuzione o impiego, fattura, liquidazione e pagamento, riconciliazione e monitoraggio. Segregazione delle funzioni, controlli e gestione delle anomalie devono essere visibili.

## NSIS e SDO

La capture bloccata non consente di sostenere un inventario generale del patrimonio informativo NSIS. Questa nota consolida soltanto due famiglie documentate da fonti primarie valide: la SDO per gli episodi di ricovero, tramite il D.M. 261/2016, e i flussi economici CE e SP, tramite il D.M. 24 maggio 2019 e OpenBDAP. Il capitolo deve distinguere finalità, soggetto alimentante, periodicità, unità di rilevazione, qualità del dato e uso di questi flussi, evitando di estendere per analogia l'elenco ad altre famiglie non verificate.

## Parti mobili e review

- Soglie e procedure di affidamento: rinvio alla fonte generale vigente e controllo alla data.
- Banche dati e classificazioni dei farmaci: rischio alto di aggiornamento; per i dispositivi il nucleo specifico resta sospeso finché non è acquisita una fonte ufficiale valida.
- Specifiche tecniche dei flussi NSIS e SDO: usare decreti e disciplinari correnti prima di inserire tracciati, campi o scadenze.
- Logistica, scorte e controlli sono organizzati anche da procedure regionali e aziendali; ogni caso locale va qualificato come esempio.

## Destinazioni

Capitolo 10 per procurement, farmaci, magazzino e ciclo passivo; il segmento dispositivi è limitato ai passaggi generali e resta da consolidare con fonte ufficiale valida. Capitolo 4 per SDO, CE e SP come flussi verificati; appendice operativa per checklist e casi. Fonte pronta con review procurement e sanitaria obbligatoria, ma non autorizza claim specifici sul flusso nazionale dei dispositivi o sull'intero catalogo NSIS.
