---
id: source-programmi-screening-oncologici-dati-passi-iss
type: source
title: "Programmi di screening oncologico e dati PASSI - corpus ISS"
status: processed
domain: "concorsi pubblici italiani"
topics: ["epidemiologia", "screening oncologici", "PASSI", "indicatori", "sorveglianza"]
entities: ["Istituto Superiore di Sanità"]
source_refs:
  - "sources/epidemiologia-base-iss"
  - "sources/sorveglianza-passi-protocollo-operativo-iss"
book_refs: ["m-sa02-professioni-sanitarie", "m-sa03-dirigenza-medica-sanitaria", "vol-07-sanita-amministrativa-professioni-sanitarie"]
confidence: 0.96
updated_at: 2026-10-03
created_at: 2026-07-29T17:30:00+02:00
review_required: false
canonical: true
tags: ["source", "iss", "passi", "epidemiologia", "screening", "dataset", "m-sa02"]
source_type: official_surveillance_results
source_url: "https://www.epicentro.iss.it/passi/dati/ScreeningColorettale"
source_date: "2021-2025"
authority_level: official_scientific
raw_path: "wiki/raw/m-sa02-professioni-sanitarie/epidemiologia/"
---

# Programmi di screening oncologico e dati PASSI

## Corpus acquisito

Sono conservati quattro documenti ufficiali EpiCentro-ISS:

- scheda PASSI Molise-Italia sullo screening mammografico 2021-2022, 2 pagine;
- scheda PASSI Molise-Italia sullo screening cervicale 2021-2022, 2 pagine;
- tabella riassuntiva dei sistemi di sorveglianza di popolazione, dicembre 2025, 23 pagine, con stime e intervalli di confidenza al 95% per USL Umbria 1, Regione Umbria e pool nazionale;
- pagina nazionale PASSI sullo screening colorettale 2023-2024, conservata come HTML testualmente auditabile con definizioni operative, popolazione, numeratori e denominatori.

I file sono registrati nel `download-log.json` con URL, byte e SHA-256.

## Copertura utile

Il corpus documenta i tre programmi oncologici principali e consente di distinguere copertura totale, organizzata e spontanea. Per lo screening colorettale, la pagina nazionale definisce la popolazione target 50-69 anni e i tempi di riferimento: ricerca del sangue occulto nelle feci negli ultimi due anni oppure colonscopia/rettosigmoidoscopia negli ultimi cinque anni. Nel biennio 2023-2024 riporta una copertura nazionale totale del 47%, con 62% al Nord, 55% al Centro e 30% al Sud.

La tabella 2025 fornisce valori numerici riusabili in esercizi controllati. Per il pool nazionale riporta, tra gli altri:

- cervicale: totale 77,7%, organizzato 46,8%, spontaneo 30,7%;
- mammografico: totale 74,9%, organizzato 54,8%, spontaneo 19,8%;
- colorettale: totale 47,4%, organizzato 39,3%, spontaneo 7,7%;
- sangue occulto fecale negli ultimi due anni: 41,3%;
- colonscopia/rettosigmoidoscopia negli ultimi cinque anni: 15,2%.

## Uso editoriale

- `SA02-06`: definire popolazione, numeratore, denominatore, indicatore e intervallo di confidenza;
- `SA02-06`: confrontare copertura totale, organizzata e spontanea senza confondere percentuali con conteggi;
- `SA02-06`: leggere differenze geografiche e temporali con cautele appropriate;
- `PRV-03`: costruire calcoli su punti percentuali, rapporti, frequenze attese e lettura degli intervalli di confidenza;
- cap. 08, solo dopo apertura del gate: collegare protocollo PASSI, risultati e limiti inferenziali.

## Limiti e cautele

PASSI è una sorveglianza campionaria basata su interviste: le stime non sono conteggi amministrativi degli inviti o degli esami. Le schede mammografica e cervicale sono profili regionali che includono confronti nazionali; non vanno presentate come rapporti nazionali completi. Nel PDF 2025, pagina stampata 20, i valori sono trascritti correttamente ma le componenti pubblicate non sommano al totale: scarti di 0,2 punti per cervicale, 0,3 per mammografico e 0,4 per colorettale. Il solo arrotondamento di tre valori al decimo non basta a spiegare scarti superiori a 0,15 punti; pesi comuni non eliminano l'additività. Il prospetto non consente di stabilire qui la causa: servono denominatori effettivi, trattamento dei dati mancanti e regole di classificazione. Non attribuire lo scarto alla pesatura senza prova, né modificare i valori ufficiali. I confronti fra territori richiedono attenzione a campionamento, pesi e intervalli di confidenza; non dimostrano da soli causalità o efficacia.

## Quadro dei programmi, verificato il 3 ottobre 2026

[ISS EpiCentro, screening oncologici](https://www.epicentro.iss.it/screening/) e [archivio informativo](https://www.epicentro.iss.it/screening/2016-2023) sostengono lo schema didattico ordinario: mammografia biennale 50–69 anni; cervice, Pap test triennale 25–29 e HPV primario quinquennale 30–64; colorettale, ricerca del sangue occulto fecale biennale 50–69. Estensioni regionali, storia clinica e percorsi per coorti vaccinate richiedono verifica del programma effettivo: lo schema non è prescrizione individuale. I tempi degli indicatori PASSI sulle endoscopie non diventano automaticamente intervalli universali di offerta del programma.

## Verifica quantitativa

La batteria [[books/moduli/m-sa02-professioni-sanitarie/planning/03-batteria-esercizi-epidemiologia-screening]] espone dati, formule, risultati e cautele. I calcoli sono riproducibili e separano sempre il dato ufficiale dalla trasformazione didattica derivata.

## Stato revisione

Il vuoto su programmi di screening, risultati PASSI recenti e dataset tabellare ufficiale è risolto. La componente quantitativa dispone di una prima batteria verificata; [[sources/premal-definizioni-caso-risposta-segnale-epidemiologico]] e lo scenario collegato risolvono i gap documentali su definizioni di caso, notifica e risposta a un segnale. Il precedente vincolo di review è superato dal riesame automatico del 3 ottobre 2026: calcoli, limiti inferenziali e definizioni sono verificati nel report 15 M-SA02 corrente.

## Esito editoriale corrente

Riesame automatico dei claim recepiti nei capitoli concluso il 3 ottobre 2026 nei report 15 M-SA02/M-SA03 pertinenti. Questa attestazione aggiorna i rinvii storici a future review; non amplia il perimetro a procedure locali o a tutti gli articoli del corpus. Le fonti mobili mantengono versione e ambito dichiarati.
