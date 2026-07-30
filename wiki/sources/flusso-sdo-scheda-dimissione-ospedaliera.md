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
updated_at: 2026-07-30T14:40:00+02:00
created_at: 2026-07-30T14:10:00+02:00
review_required: true
canonical: true
tags: ["source", "m-sa01", "nsis", "sdo", "assistenza-ospedaliera"]
source_type: official_primary_and_operational
source_url: "https://www.gazzettaufficiale.it/eli/gu/2017/02/07/31/sg/pdf"
source_date: 2017-02-07
authority_level: primary_official
raw_path: "wiki/raw/m-sa01-sanita-amministrativa/fonti/dm-261-2016-sdo-gazzetta.pdf"
sha256: "A9FED7060A8D6447573646E52D47876E63A66A6778166BC6F52A2B7D8AA64D2B"
---

# Flusso SDO - Scheda di dimissione ospedaliera

## Fonti ufficiali verificate

La prova primaria locale è il fascicolo della *Gazzetta Ufficiale*, serie generale n. 31 del 7 febbraio 2017, che contiene il D.M. 7 dicembre 2016, n. 261 e il relativo disciplinare tecnico. Il PDF, acquisito il 30 luglio 2026, è valido, leggibile e registrato nel manifest M-SA01 con byte e SHA-256. Il decreto modifica il D.M. 27 ottobre 2000, n. 380 e documenta direttamente contenuti, unità di rilevazione, responsabilità di compilazione, alimentazione mensile da parte delle Regioni e Province autonome, trasmissione elettronica al NSIS, finalità e presidi tecnici del flusso.

Il precedente file `flusso-sdo-ministero.html` è conservato immutabile per audit, ma contiene soltanto una pagina di challenge Gcore: nel manifest è marcato come bloccato e non valido per il corpus. La pagina ministeriale corrente e le specifiche funzionali restano riferimenti da ricontrollare al cut-off editoriale, ma nessun claim di questa nota dipende dal file HTML fallito. Tracciati, campi, classificazioni e schemi tecnici sono elementi mobili: prima di una pubblicazione o applicazione operativa va verificata la versione corrente del decreto, delle specifiche e delle istruzioni regionali.

## Carta d'identità del flusso

### Finalità

La SDO raccoglie in modo sistematico informazioni sugli episodi di ricovero erogati dagli istituti pubblici e privati. È una sintesi fedele di informazioni contenute nella cartella clinica e sostiene finalità organizzativo-gestionali, programmazione sanitaria, monitoraggio dell'assistenza ospedaliera e dei LEA, analisi clinico-epidemiologiche, appropriatezza, qualità ed esiti. L'uso deve rispettare natura, limiti e qualità del dato.

### Soggetto alimentante e catena di trasmissione

La scheda è compilata dal medico che ha avuto in cura il paziente. Gli istituti di ricovero trasmettono le informazioni alle Regioni o Province autonome; queste effettuano controlli di qualità e inviano i dati al Ministero della Salute. Le responsabilità operative interne, i sistemi utilizzati e gli eventuali ulteriori controlli dipendono dalle regole regionali e aziendali vigenti.

### Unità di rilevazione

L'unità è l'episodio di ricovero relativo a un paziente dimesso da un istituto di ricovero pubblico o privato. Non è il bilancio dell'ospedale, né un aggregato economico. Le informazioni descrivono aspetti anagrafici, amministrativi, organizzativi e clinici dell'episodio secondo il tracciato vigente.

### Periodicità

Il D.M. 261/2016 sostituisce espressamente, nell'articolo 3 del D.M. 380/2000, la cadenza trimestrale con quella mensile e stabilisce la trasmissione elettronica al Ministero nell'ambito del NSIS. Questa indicazione descrive l'assetto nazionale documentato dal decreto, ma non autorizza a inventare il calendario operativo: scadenze, finestre di correzione, ritrasmissioni e specifiche vanno controllate nel disciplinare nazionale corrente e nelle istruzioni regionali applicabili.

### Controlli

La qualità va presidiata dalla compilazione alla trasmissione. Sono pertinenti controlli di completezza, coerenza logica, accuratezza rispetto alla cartella clinica, correttezza della codifica, validità dei valori e tracciabilità delle versioni. Il Ministero segnala espressamente possibili criticità di omogeneità, completezza e accuratezza e ricorda che i sistemi di classificazione cambiano nel tempo.

### Responsabilità

Il medico risponde della compilazione della scheda secondo la disciplina applicabile; l'istituto presidia produzione e invio; Regione o Provincia autonoma controlla la qualità e trasmette; il Ministero raccoglie, controlla, elabora e diffonde le informazioni nel proprio ambito. Validazione, correzione ed escalation interne devono essere ricostruite nelle fonti regionali e aziendali, senza attribuirle per analogia.

### Uso del dato

Il flusso alimenta conoscenza e valutazione dell'attività di ricovero, programmazione, monitoraggio dei LEA, analisi di appropriatezza e qualità, studi epidemiologici e valutazioni economico-gestionali. Un dato trasmesso non è automaticamente idoneo a ogni uso: occorre verificare periodo, perimetro, classificazione, completezza, versione ed eventuali anomalie.

## Parti mobili e review

Sono mobili: tracciati, campi, classificazioni, schemi XML, periodicità operativa, scadenze, finestre di correzione, controlli automatici e istruzioni regionali. La pagina ministeriale segnala inoltre un percorso di aggiornamento dei sistemi di classificazione: il capitolo non deve fissare dettagli tecnici destinati a cambiare. Review sanitaria e tecnico-informativa obbligatoria prima del congelamento.
