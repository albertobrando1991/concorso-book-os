---
id: source-cloud-virtualizzazione-container-devops-continuita-fonti-primarie
type: source
title: "Cloud, container, DevOps, osservabilità e continuità — fonti primarie"
status: processed
domain: "informatica specialistica"
topics: ["cloud pa", "virtualizzazione", "container", "devops", "osservabilità", "business continuity"]
entities: ["Agenzia per la cybersicurezza nazionale", "NIST", "Kubernetes", "OpenTelemetry"]
source_refs: ["sources/pa-digitale-cad-identita-documenti-servizi-dati", "sources/sicurezza-informatica-privacy-nis2-pa"]
book_refs: ["m-tr01-ict-trasformazione-digitale"]
confidence: 0.9
updated_at: 2026-07-29
created_at: 2026-07-29
review_required: true
canonical: true
tags: ["source", "vol-08", "cloud", "container", "devops", "continuita"]
source_type: official_strategy_standards_and_documentation
source_url: "https://cloud.italia.it/strategia-cloud-pa/"
source_date: 2026-07-29
authority_level: alta
---

# Cloud, container, DevOps, osservabilità e continuità — fonti primarie

## Uso

Nota consolidata per il capitolo 7 di VOL-08. Sostiene le definizioni trasferibili di cloud computing, i principali concetti di container e orchestrazione, i segnali di osservabilità, la pianificazione della continuità e l’inquadramento del Cloud della PA. Non sostituisce la verifica specialistica di configurazioni, prodotti, requisiti contrattuali o misure di sicurezza.

## Fonti primarie

- **NIST SP 800-145 — The NIST Definition of Cloud Computing**, National Institute of Standards and Technology: <https://csrc.nist.gov/pubs/sp/800/145/final>. Definisce cinque caratteristiche essenziali, tre modelli di servizio e quattro modelli di distribuzione.
- **NIST SP 800-146 — Cloud Computing Synopsis and Recommendations**, National Institute of Standards and Technology: <https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-146.pdf>. Approfondisce benefici, rischi e considerazioni per l’adozione.
- **Strategia Cloud Italia**, Dipartimento per la trasformazione digitale e ACN: <https://cloud.italia.it/strategia-cloud-pa/>. Individua classificazione di dati e servizi, qualificazione dei servizi cloud e Polo Strategico Nazionale come pilastri della strategia.
- **Classificazione di dati e servizi**, Cloud Italia: <https://cloud.italia.it/strategia-cloud-pa/classificazione-di-dati-e-servizi/>. Distingue dati e servizi strategici, critici e ordinari in base all’impatto della compromissione.
- **Qualificazione dei servizi cloud per la PA**, Cloud Italia: <https://cloud.italia.it/qualificazione-servizi-cloud/>. Documenta la competenza ACN e il Regolamento unico adottato con decreto direttoriale n. 21007/24 del 27 giugno 2024, in vigore nel regime ordinario da agosto 2024.
- **Catalogo dei servizi cloud qualificati**, Cloud Italia: <https://cloud.italia.it/qualificazione-servizi-cloud/catalogo-servizi-cloud/>. Descrive il catalogo dei servizi IaaS, PaaS e SaaS qualificati e il rapporto con gli indicatori dei livelli di servizio.
- **Programma di abilitazione al cloud**, Cloud Italia: <https://cloud.italia.it/programma-abilitazione-cloud/>. Offre strumenti per inventario, prioritizzazione, assessment e scelta della strategia di migrazione.
- **Containers**, documentazione ufficiale Kubernetes: <https://kubernetes.io/docs/concepts/containers/>. Definisce immagini, container e runtime e chiarisce la natura ripetibile e tendenzialmente immutabile dei workload containerizzati.
- **Objects in Kubernetes**, documentazione ufficiale Kubernetes: <https://kubernetes.io/docs/concepts/overview/working-with-objects/>. Sostiene i concetti di stato desiderato, stato attuale e riconciliazione.
- **Pods**, documentazione ufficiale Kubernetes: <https://kubernetes.io/docs/concepts/workloads/pods/>. Definisce il Pod come minima unità distribuibile e come gruppo di uno o più container co-localizzati e co-schedulati.
- **Signals**, documentazione ufficiale OpenTelemetry: <https://opentelemetry.io/docs/concepts/signals/>. Distingue trace, metriche e log come segnali complementari.
- **NIST SP 800-34 Rev. 1 — Contingency Planning Guide for Federal Information Systems**, National Institute of Standards and Technology: <https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final>. Inquadra analisi d’impatto, requisiti e priorità di ripristino, piani, test ed esercitazioni.

## Decisioni editoriali

- Usare le cinque caratteristiche NIST per riconoscere il modello cloud senza far dipendere la spiegazione da un fornitore.
- Distinguere modello di servizio e modello di distribuzione.
- Presentare la responsabilità condivisa come ripartizione variabile per servizio e contratto, non come trasferimento totale al provider.
- Distinguere macchina virtuale e container per isolamento, dipendenze e gestione, evitando la formula «VM leggera».
- Trattare Kubernetes come esempio di orchestrazione, non come sinonimo universale di container.
- Presentare DevOps come collaborazione, feedback e automazione lungo il flusso; i prodotti restano esempi non canonici.
- Distinguere monitoraggio e osservabilità e usare insieme metriche, log e trace.
- Distinguere alta disponibilità, replica, snapshot, backup, disaster recovery e continuità operativa.
- Collegare RPO e RTO all’analisi d’impatto e verificare il ripristino mediante prove.
- Per la PA, partire dalla classificazione di dati e servizi e verificare la qualificazione corrente nel catalogo ACN.

## Limiti e review

- La disciplina Cloud PA è soggetta ad aggiornamento: ricontrollare regolamento, catalogo e documentazione ACN prima del text freeze.
- Le strategie di migrazione hanno denominazioni diffuse ma non perfettamente uniformi fra framework; nel capitolo sono usate come tassonomia operativa, non come classificazione normativa.
- Virtualizzazione, Infrastructure as Code, CI/CD, backup e FinOps richiedono review tecnica specialistica.
- NIST SP 800-34 è una guida statunitense: nel volume sostiene i concetti tecnici, non obblighi giuridici per le amministrazioni italiane.
- I dettagli di sicurezza sono rinviati ai capitoli 8 e 9; capitolati e SLA al capitolo 12.

## Collegamenti

- [[sources/pa-digitale-cad-identita-documenti-servizi-dati]]
- [[sources/sicurezza-informatica-privacy-nis2-pa]]
- [[topics/open-data-interoperabilita-cloud-pa]]
- [[books/moduli/m-tr01-ict-trasformazione-digitale/chapters/07-cloud-pa-virtualizzazione-container-devops]]
