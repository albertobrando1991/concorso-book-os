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
updated_at: 2026-07-30T15:58:00+02:00
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

Programmazione, progettazione, affidamento, esecuzione, RUP, piattaforme, BDNCP e tracciabilità sono rinviati alle source note del VOL-01 sul D.Lgs. 36/2023 e sul correttivo. Nel corpus verificato M-SA01 aggiunge il fabbisogno clinico-organizzativo e la continuità della fornitura per i farmaci, oltre ai flussi specifici SDO, CE e SP. Per i dispositivi restano utilizzabili soltanto i passaggi generali di procurement e controllo interno; il delta settoriale richiede una fonte ufficiale valida ulteriore.

## Fonti locali verificate e capture escluse

Il perimetro attivo usa lo snapshot AIFA dell'OsMed per farmaci e spesa farmaceutica, il D.M. 7 dicembre 2016, n. 261 in Gazzetta per la SDO, il D.M. 24 maggio 2019 in Gazzetta e lo snapshot OpenBDAP per CE e SP, oltre alle source note verificate sui contratti pubblici. Le capture `patrimonio-informativo-nsis-ministero.html` e `monitoraggio-consumi-dispositivi-ministero.html` contengono soltanto una challenge Gcore: il manifest le marca `blocked` e `valid_corpus: false`. Restano conservate per audit ma sono escluse dal corpus attivo; nessun claim di questa nota dipende da quei file.

## Farmaci e dispositivi

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
