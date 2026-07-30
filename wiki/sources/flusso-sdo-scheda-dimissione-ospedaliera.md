---
id: source-flusso-sdo-scheda-dimissione-ospedaliera
type: source
title: "Flusso SDO - Scheda di dimissione ospedaliera"
status: processed
domain: "concorsi pubblici italiani"
topics: ["NSIS", "SDO", "assistenza ospedaliera", "qualita del dato"]
entities: ["Ministero della Salute", "Regioni", "Azienda sanitaria"]
source_refs: ["sources/procurement-farmaci-dispositivi-flussi-nsis"]
book_refs: ["m-sa01-sanita-amministrativa", "vol-07-sanita-amministrativa-professioni-sanitarie"]
confidence: 0.96
updated_at: 2026-07-30T14:10:00+02:00
created_at: 2026-07-30T14:10:00+02:00
review_required: true
canonical: true
tags: ["source", "m-sa01", "nsis", "sdo", "assistenza-ospedaliera"]
source_type: official_primary_and_operational
source_url: "https://www.salute.gov.it/new/it/tema/assistenza-ospedaliera/il-flusso-informativo-sdo/"
source_date: 2026-07-30
authority_level: primary_official
raw_path: "wiki/raw/m-sa01-sanita-amministrativa/fonti/flusso-sdo-ministero.html"
sha256: "B2096D9573AF0A0CC70AF39C0521D25F5A82AA1B164E0BE2AB4A49E679F356C7"
---

# Flusso SDO - Scheda di dimissione ospedaliera

## Fonti ufficiali verificate

La pagina corrente del Ministero della Salute sul flusso informativo SDO è stata ricontrollata il 30 luglio 2026. La pagina ricostruisce la base normativa dal D.M. 28 dicembre 1991 al D.M. 27 ottobre 2000, n. 380 e alle successive modifiche, tra cui il D.M. 8 luglio 2010, n. 135, il D.M. 7 dicembre 2016, n. 261 e il D.M. 26 settembre 2023, n. 165. Il file ministeriale acquisito il 29 luglio 2026 è registrato nel manifest M-SA01 con byte e SHA-256.

Sono state verificate anche la pagina ministeriale "La scheda di dimissione ospedaliera" e le specifiche funzionali pubblicate dal Ministero. Tracciati, campi, classificazioni e schemi tecnici restano elementi mobili: prima di una pubblicazione o applicazione operativa va controllata la versione corrente del decreto, delle specifiche e delle istruzioni regionali.

## Carta d'identità del flusso

### Finalità

La SDO raccoglie in modo sistematico informazioni sugli episodi di ricovero erogati dagli istituti pubblici e privati. È una sintesi fedele di informazioni contenute nella cartella clinica e sostiene finalità organizzativo-gestionali, programmazione sanitaria, monitoraggio dell'assistenza ospedaliera e dei LEA, analisi clinico-epidemiologiche, appropriatezza, qualità ed esiti. L'uso deve rispettare natura, limiti e qualità del dato.

### Soggetto alimentante e catena di trasmissione

La scheda è compilata dal medico che ha avuto in cura il paziente. Gli istituti di ricovero trasmettono le informazioni alle Regioni o Province autonome; queste effettuano controlli di qualità e inviano i dati al Ministero della Salute. Le responsabilità operative interne, i sistemi utilizzati e gli eventuali ulteriori controlli dipendono dalle regole regionali e aziendali vigenti.

### Unità di rilevazione

L'unità è l'episodio di ricovero relativo a un paziente dimesso da un istituto di ricovero pubblico o privato. Non è il bilancio dell'ospedale, né un aggregato economico. Le informazioni descrivono aspetti anagrafici, amministrativi, organizzativi e clinici dell'episodio secondo il tracciato vigente.

### Periodicità

La pagina ministeriale corrente ricorda che il D.M. 135/2010 ha portato l'invio da semestrale a trimestrale per il 2010 e a mensile dal 2011. Questa indicazione descrive l'assetto nazionale riportato dal Ministero, ma non autorizza a inventare il calendario operativo: scadenze, finestre di correzione, ritrasmissioni e specifiche vanno controllate nel disciplinare nazionale corrente e nelle istruzioni regionali applicabili.

### Controlli

La qualità va presidiata dalla compilazione alla trasmissione. Sono pertinenti controlli di completezza, coerenza logica, accuratezza rispetto alla cartella clinica, correttezza della codifica, validità dei valori e tracciabilità delle versioni. Il Ministero segnala espressamente possibili criticità di omogeneità, completezza e accuratezza e ricorda che i sistemi di classificazione cambiano nel tempo.

### Responsabilità

Il medico risponde della compilazione della scheda secondo la disciplina applicabile; l'istituto presidia produzione e invio; Regione o Provincia autonoma controlla la qualità e trasmette; il Ministero raccoglie, controlla, elabora e diffonde le informazioni nel proprio ambito. Validazione, correzione ed escalation interne devono essere ricostruite nelle fonti regionali e aziendali, senza attribuirle per analogia.

### Uso del dato

Il flusso alimenta conoscenza e valutazione dell'attività di ricovero, programmazione, monitoraggio dei LEA, analisi di appropriatezza e qualità, studi epidemiologici e valutazioni economico-gestionali. Un dato trasmesso non è automaticamente idoneo a ogni uso: occorre verificare periodo, perimetro, classificazione, completezza, versione ed eventuali anomalie.

## Parti mobili e review

Sono mobili: tracciati, campi, classificazioni, schemi XML, periodicità operativa, scadenze, finestre di correzione, controlli automatici e istruzioni regionali. La pagina ministeriale segnala inoltre un percorso di aggiornamento dei sistemi di classificazione: il capitolo non deve fissare dettagli tecnici destinati a cambiare. Review sanitaria e tecnico-informativa obbligatoria prima del congelamento.
