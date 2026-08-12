---
id: m-tr01-capitolo-10-piano-completamento
type: chapter_plan
title: "Piano di completamento — Capitolo 10 Data governance, open data, interoperabilità e qualità"
status: ready
domain: "concorsi pubblici italiani"
topics: ["data governance", "data quality", "metadati", "open data", "interoperabilità"]
entities: ["AgID", "PDND", "Unione europea"]
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/pa-digitale-cad-identita-documenti-servizi-dati", "sources/agid-piano-triennale-informatica-pa-2024-2026-aggiornamento-2026", "sources/ingegneria-software-api-interoperabilita-fonti-tecniche"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "vol-08-ict-digitale-cybersecurity-dati", "il-metodo-bando"]
confidence: 0.82
updated_at: 2026-07-30
created_at: 2026-07-30
review_required: true
canonical: false
tags: ["planning", "m-tr01", "chapter-10", "data-governance", "open-data"]
chapter_ref: "chapters/10-data-governance-open-data-interoperabilita.md"
---

# Piano di completamento — Capitolo 10

## 1. Funzione del capitolo

Il capitolo deve mostrare come un ente governa il dato dal momento in cui lo acquisisce fino all'uso, allo scambio, alla pubblicazione e alla dismissione. Il filo conduttore è operativo: responsabilità, inventario, metadati, qualità, catalogo, accesso, riuso e interoperabilità.

Il capitolo 4 tratta modelli di basi dati, SQL, NoSQL, vincoli e qualità a livello tecnico. Il capitolo 6 tratta API, ModI, PDND ed e-service. Il capitolo 9 governa accessi, log e incidenti. Il capitolo 10 collega questi prerequisiti alla responsabilità organizzativa sul patrimonio informativo, senza ripeterne la teoria tecnica.

L'output centrale è una coppia di strumenti:

- inventario dei dati, con responsabilità, finalità, fonte, qualità e dipendenze;
- scheda dataset, con metadati, classificazione, accesso, riuso, aggiornamento e controlli.

## 2. Stato iniziale

Il file contiene soltanto frontmatter, H1 e specifica della struttura madre. La riga «Data governance» della matrice è `parziale` e indica qualità, open data e interoperabilità, con output inventario dati, scheda dataset ed esercizio.

Nessun nucleo specialistico è completo nel capitolo. Sono disponibili prerequisiti:

- VOL-01, capitolo 10, § 16: definizioni introduttive di interoperabilità, PDND, API e open data;
- M-TR01, capitolo 4: modellazione, vincoli e qualità del dato nella base dati;
- M-TR01, capitolo 6: contratti API, interoperabilità tecnica, ModI, PDND ed e-service;
- M-TR01, capitolo 9: autorizzazione, logging, protezione e risposta;
- source note PA digitale e Piano Triennale 2024-2026, Aggiornamento 2026.

Questi contenuti sono prerequisiti o raccordi. Non sostituiscono governance, ruoli, ciclo di vita, metadati, cataloghi e riuso.

## 3. Nuclei assegnati

### 3.1 Data governance

- dato come asset informativo e non semplice contenuto di una tabella;
- obiettivi: disponibilità controllata, qualità, comprensibilità, sicurezza, conformità e riuso;
- principi, policy, standard, responsabilità, decisioni ed evidenze;
- rapporto fra governance, gestione operativa e architettura dei dati;
- ambito, domini e priorità proporzionati al contesto dell'ente.

### 3.2 Ruoli e responsabilità

- organo o funzione di governo;
- data owner come responsabile delle decisioni sul dominio;
- data steward come presidio di definizioni, qualità e metadati;
- data custodian o funzione tecnica di conservazione e protezione;
- produttore, fruitore e responsabile del servizio;
- raccordo con RTD, sicurezza, privacy, trasparenza e responsabili dei processi;
- matrice RACI come strumento possibile, non come modello obbligatorio.

### 3.3 Ciclo di vita del dato

- pianificazione e definizione della finalità;
- acquisizione o creazione;
- validazione, trasformazione e integrazione;
- conservazione, uso e condivisione;
- pubblicazione o riuso quando consentiti;
- aggiornamento, archiviazione e dismissione;
- tracciabilità di origine, trasformazioni, responsabilità e decisioni.

### 3.4 Inventario, catalogo e metadati

- differenza tra inventario dei dati e catalogo;
- dataset, elemento informativo, dominio e fonte;
- metadati descrittivi, strutturali, amministrativi, tecnici e di qualità;
- glossario aziendale e definizioni condivise;
- data lineage a livello concettuale;
- identificativi, versioni, frequenza di aggiornamento, titolare, licenza e condizioni d'uso;
- catalogo come capacità di scoperta e governo, non come semplice elenco di file.

### 3.5 Qualità del dato

- accuratezza, completezza, coerenza, tempestività, validità e unicità;
- regola di qualità, misura, soglia, controllo, anomalia e remediation;
- qualità intrinseca e adeguatezza all'uso;
- profiling, validazione, riconciliazione e monitoraggio;
- responsabilità sulla correzione e gestione delle eccezioni;
- conseguenze amministrative di dati non affidabili.

### 3.6 Open data e riuso

- dato aperto, formato aperto, leggibilità da macchina, licenza e riutilizzabilità;
- differenza fra pubblicazione web, trasparenza, accesso, condivisione e open data;
- dataset, distribuzione, catalogo e metadati;
- qualità, aggiornamento, documentazione e versionamento;
- limiti derivanti da dati personali, segreti, sicurezza, diritti di terzi e altri vincoli;
- high-value datasets soltanto dopo consolidamento delle fonti UE vigenti.

### 3.7 Interoperabilità semantica e organizzativa

- livelli giuridico, organizzativo, semantico e tecnico;
- significato condiviso, vocabolari, schemi e identificatori;
- accordi, ruoli e responsabilità tra amministrazioni;
- once only come obiettivo, non come accesso indiscriminato;
- raccordo con API, ModI, PDND ed e-service del capitolo 6;
- distinzione netta tra interoperabilità autorizzata e open data.

### 3.8 Governance, privacy e sicurezza

- finalità, base giuridica e minimizzazione come vincoli al trattamento e allo scambio;
- classificazione, accessi, logging, conservazione e dismissione;
- responsabilizzazione ed evidenze;
- privacy by design e security by design come raccordi, non duplicazioni;
- valutazione separata di comunicazione, diffusione, pubblicazione e riuso.

## 4. Criteri di completezza

| Nucleo | Teoria necessaria | Applicazione | Verifica |
| --- | --- | --- | --- |
| Governance | definizione, obiettivi, componenti e decisioni | modello di governo di un dominio | domanda orale |
| Ruoli | funzione, confini e responsabilità | RACI o matrice ruolo-decisione-evidenza | caso di conflitto |
| Ciclo di vita | fasi, passaggi e conseguenze | percorso di un dataset | ordinamento guidato |
| Metadati/catalogo | tipi, funzione e distinzioni | scheda dataset | completamento campi |
| Qualità | dimensioni, regole, metriche e remediation | cruscotto qualità | diagnosi di anomalie |
| Open data | requisiti, licenza, formati e limiti | valutazione di pubblicabilità | domanda-trappola |
| Interoperabilità | livelli e distinzione da open data | scambio tra enti | caso PDND con rinvio preciso |
| Privacy/sicurezza | finalità, accesso, protezione ed evidenze | classificazione e decisione | checklist |

Nessun inventario o esercizio può sostituire la spiegazione teorica.

## 5. Sezioni da conservare

- frontmatter e identificativi canonici;
- H1 «Data governance, open data, interoperabilità e qualità»;
- `outline_section: 10`;
- promessa della struttura madre: ruoli, ciclo di vita, metadati, qualità, cataloghi, riuso e interoperabilità;
- output inventario e scheda dataset;
- richiesta di review UE e AgID.

## 6. Duplicazioni da evitare

- modello relazionale, SQL, NoSQL, vincoli e indici del capitolo 4;
- spiegazione tecnica approfondita delle dimensioni di qualità già introdotte nel capitolo 4: qui vanno governate e misurate;
- progettazione API, HTTP, OpenAPI, ModI, PDND ed e-service del capitolo 6;
- IAM, crittografia, logging e incident response del capitolo 9;
- disciplina generale di privacy, trasparenza e accesso del VOL-01;
- AI training data, bias e model governance del capitolo 11;
- dettagli di prodotti commerciali di catalogazione, MDM, data lake o data mesh;
- obblighi, scadenze, formati e dataset UE/AgID non consolidati.

## 7. Casi, domande ed esercizi

### Caso guidato principale

Un comune deve governare il dataset delle autorizzazioni per occupazione di suolo pubblico, usato dall'ufficio competente, condiviso con altri servizi e candidato alla pubblicazione in forma aperta.

Il caso deve far emergere:

1. finalità e processi;
2. owner, steward, custode e fruitori;
3. sorgenti e lineage;
4. metadati e frequenza di aggiornamento;
5. regole di qualità e anomalie;
6. classificazione, accessi e privacy;
7. decisione separata su interoperabilità e open data;
8. versione, pubblicazione, monitoraggio e dismissione.

### Output compilabili

- inventario dati: dominio, dataset, finalità, fonte, owner, steward, custode, sistemi, classificazione e stato;
- scheda dataset: descrizione, struttura, metadati, qualità, frequenza, licenza, accesso, riuso e contatti;
- matrice regola-metrica-soglia-evidenza-responsabile;
- decision tree «interno, condiviso, interoperabile o open»;
- glossario minimo del dominio;
- registro delle anomalie e delle remediation.

### Domanda da commissario

«Come imposteresti la governance di un dataset pubblico destinato sia allo scambio tra enti sia al possibile riuso come open data?»

La risposta deve distinguere finalità, responsabilità, qualità, metadati, interoperabilità autorizzata, pubblicazione aperta, privacy, licenza, aggiornamento ed evidenze.

### Domande-trappola

- un dato presente in una banca dati è automaticamente di qualità?
- catalogare un dataset significa pubblicarlo?
- interoperabilità significa accesso libero?
- un PDF online è sempre open data?
- completezza significa raccogliere il maggior numero possibile di dati?
- il data owner coincide sempre con l'amministratore del database?
- anonimizzazione, pseudonimizzazione e aggregazione sono equivalenti?

### Esercizi

1. assegnare ruoli a uno scenario;
2. ordinare le fasi del ciclo di vita;
3. completare una scheda dataset;
4. trasformare un problema in regola e metrica di qualità;
5. distinguere catalogo, interoperabilità e open data;
6. valutare la pubblicabilità di un dataset;
7. costruire un mini-glossario;
8. quiz con soluzioni ragionate.

## 8. Fonti consolidate da usare

- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]];
- [[sources/pa-digitale-cad-identita-documenti-servizi-dati]];
- [[sources/agid-piano-triennale-informatica-pa-2024-2026-aggiornamento-2026]];
- [[sources/ingegneria-software-api-interoperabilita-fonti-tecniche]];
- [[sources/d-lgs-7-marzo-2005-n-82-amministrazione-digitale]];
- [[sources/basi-dati-sql-nosql-qualita-fonti-tecniche]];
- [[topics/open-data-interoperabilita-cloud-pa]];
- [[topics/ict-digitale-cybersecurity-dati-concorsi-pa]].

## 9. Fonti da consolidare prima dello step 09

Preparare una source note specialistica con fonti ufficiali vigenti su:

- linee guida nazionali open data e cataloghi AgID;
- profilo nazionale dei metadati e cataloghi dati.gov.it;
- direttiva open data, disciplina italiana di recepimento e regolamento sui dataset di elevato valore;
- Data Governance Act e, se pertinente al perimetro, Data Act, senza sovrapporre la disciplina generale al caso PA;
- Interoperable Europe Act ed European Interoperability Framework;
- vocabolari e strumenti semantici nazionali pertinenti;
- standard o riferimenti tecnici trasferibili per qualità e metadati, evitando certificazioni improprie.

Ogni nota deve indicare versione, data di consultazione, autorità, claim sostenuti e limiti. Prima del text freeze verificare linee guida, cataloghi, licenze, dataset e terminologia vigenti.

## 10. Topic, entity e quiz

Aggiornare [[topics/open-data-interoperabilita-cloud-pa]] o creare una pagina specialistica `topics/data-governance-qualita-metadati-open-data.md`, collegando il capitolo 10 e separando il cloud già sviluppato nel capitolo 7.

Le entity da verificare sono AgID, PDND, dati.gov.it e Unione europea. Non creare entity normative senza una source note primaria adeguata.

Non risultano quiz specialistici canonici dedicati. Lo step 09 deve inserire esercizi e soluzioni nel capitolo; una futura banca quiz dovrà riusare definizioni e fonti.

## 11. Review umane richieste

- chief data officer o responsabile data governance;
- data steward/data quality manager;
- data architect o data engineer per lineage e catalogo;
- esperto open data e metadati AgID;
- esperto interoperabilità/PDND;
- giurista del dato pubblico, trasparenza e riuso;
- DPO per pubblicazione, comunicazione e dati personali;
- security architect per classificazione e accessi;
- revisore editoriale per autonomia didattica e resa KDP.

## 12. Struttura H1/H2/H3

# Data governance, open data, interoperabilità e qualità

## Obiettivo e confine con il volume base

## Mappa BANDO: governare il dato

## Il dato come patrimonio informativo
### Dato, informazione, dataset e dominio
### Governance, gestione e architettura

## Ruoli e responsabilità
### Owner, steward e custodian
### Produttori, fruitori e responsabili del processo
### Decisioni, RACI ed evidenze

## Ciclo di vita del dato
### Creazione e acquisizione
### Validazione, uso e condivisione
### Archiviazione e dismissione

## Inventario, catalogo e glossario
### Inventario e catalogo
### Glossario e definizioni condivise
### Lineage, versioni e dipendenze

## Metadati
### Descrittivi, strutturali, amministrativi e tecnici
### Metadati di qualità e aggiornamento
### Scheda dataset

## Qualità del dato
### Dimensioni e adeguatezza all'uso
### Regole, metriche, soglie e controlli
### Anomalie, remediation e monitoraggio

## Open data e riuso
### Formato, macchina, licenza e accessibilità
### Dataset, distribuzioni e cataloghi
### Limiti alla pubblicazione

## Interoperabilità
### Giuridica, organizzativa, semantica e tecnica
### Vocabolari, schemi e identificatori
### Raccordo con ModI, PDND ed e-service

## Privacy, sicurezza e responsabilizzazione

## Caso guidato: dataset delle occupazioni di suolo pubblico

## Laboratorio: inventario e scheda dataset

## Domanda da commissario

## Domande-trappola

## Mini-esercizi e quiz

## Checklist finale

## Da sapere in 5 righe

## Riferimenti consolidati

## Note di review

## 13. Budget KDP

| Blocco | Parole orientative |
| --- | ---: |
| apertura, obiettivo e Mappa BANDO | 350-450 |
| patrimonio informativo e governance | 500-650 |
| ruoli e responsabilità | 500-650 |
| ciclo di vita | 450-600 |
| inventario, catalogo, glossario e lineage | 600-750 |
| metadati e scheda dataset | 550-700 |
| qualità del dato | 650-800 |
| open data e riuso | 650-800 |
| interoperabilità e raccordi | 500-650 |
| privacy, sicurezza e accountability | 350-450 |
| caso e laboratorio | 650-850 |
| orale, trappole, esercizi, checklist e sintesi | 500-650 |
| riferimenti e note di review | 150-250 |
| **Totale** | **6.350-7.800** |

Le tabelle devono restare leggibili nel formato KDP. Dividere l'inventario e la scheda dataset se una tabella unica richiede troppe colonne.

## 14. Criteri di accettazione dello step 09

- ogni nucleo ha teoria autonoma prima degli strumenti;
- ruoli e ciclo di vita sono spiegati con conseguenze;
- metadati, inventario, catalogo, glossario e lineage sono distinti;
- qualità è collegata a regole, metriche e remediation;
- open data è distinto da trasparenza, accesso e interoperabilità;
- il rinvio al capitolo 6 è preciso e non sostituisce la governance;
- privacy e sicurezza sono integrate senza duplicare VOL-01 e capitolo 9;
- caso, inventario e scheda dataset sono completi e compilabili;
- esercizi hanno soluzioni o criteri;
- fonti UE/AgID sono consolidate e tracciate;
- ogni dettaglio mobile resta in review;
- frontmatter e riferimenti sono veritieri.

## 15. Esito del piano

Il piano è pronto per la scrittura, ma lo step 09 deve prima consolidare le fonti primarie specialistiche su data governance, metadati, qualità, open data e interoperabilità europea. Il capitolo non va dichiarato completo basandosi soltanto sulle fonti generali già disponibili.

## Addendum retrofit formato 2 — 11 agosto 2026

Il piano resta conservativo: il testo legacy valido viene redistribuito nei sette nuclei sotto indicati e ampliato soltanto dove serve a rendere esplicita la copertura richiesta. Non si ripetono la modellazione e i vincoli di base del capitolo 04, i contratti API e l'operatività di ModI/PDND del capitolo 06, né IAM, logging e risposta agli incidenti del capitolo 09. La governance di dati per AI rimane un raccordo verso il capitolo 11.

| Nucleo ID | Titolo e contenuto | Stato di partenza | Intervento e verifica |
| --- | --- | --- | --- |
| `N-TR01-10-01` | Il dato come asset informativo e il confine tra governance, gestione e architettura | parziale | Rendere autonome definizioni, decisioni, evidenze ed effetto sul procedimento; quiz 1. |
| `N-TR01-10-02` | Ruoli, decisioni, RACI ed evidenze | parziale | Distinguere owner, steward, custodian e funzioni di processo senza attribuire qualifiche legali; quiz 2 e matrice ruolo-decisione-evidenza. |
| `N-TR01-10-03` | Ciclo di vita, classificazione e lineage | parziale | Collegare finalità, acquisizione, validazione, uso, condivisione, conservazione e dismissione; quiz 3. |
| `N-TR01-10-04` | Inventario, catalogo, glossario e metadati | parziale | Separare chiaramente gli artefatti e rendere compilabile una scheda dataset; quiz 4 e laboratorio. |
| `N-TR01-10-05` | Qualità del dato: regole, metriche, anomalie e rimedio | parziale | Passare dalle dimensioni alle regole misurabili e alla responsabilità di chiusura; quiz 5. |
| `N-TR01-10-06` | Open data, riuso, distribuzioni e limiti | parziale | Distinguere pubblicazione web, trasparenza, accesso, condivisione e riuso; quiz 6. |
| `N-TR01-10-07` | Interoperabilità, privacy, sicurezza e responsabilizzazione | parziale | Trattare i quattro livelli e la decisione organizzativa; rinvio preciso al capitolo 06 per ModI, PDND ed e-service; caso guidato. |

### Struttura e budget del retrofit

- H1 invariato; apertura, obiettivo e Mappa BANDO sono mantenuti prima dei nuclei.
- Sette heading H2 nel formato `N-TR01-10-NN · titolo`; ogni nucleo ha almeno 600 parole, con definizione, funzione, elementi, distinzioni, conseguenze, uso d'esame, errore ed evidenza quando pertinenti.
- Dopo il settimo nucleo compare un solo blocco `▣ Verifica`, con sei quiz commentati e il caso delle occupazioni di suolo pubblico. Il laboratorio conserva inventario, scheda dataset e albero decisionale come strumenti stampabili.
- Budget: almeno 4.200 parole nei nuclei, oltre ad apertura, caso, laboratorio, domanda orale e verifica; obiettivo editoriale 5.200-6.200 parole complessive.

### Fonti, rinvii e audit

Usare esclusivamente le source note consolidate elencate nella sezione 8, in particolare `data-governance-open-data-interoperabilita-fonti-primarie` e il Piano Triennale AgID. Nel corpo, il rinvio a ModI, PDND ed e-service è: capitolo 06, sezione "N-TR01-06-06 · Interoperabilità PA ed e-service"; il rinvio serve soltanto ai dettagli di contratto e piattaforma, non alla teoria organizzativa qui sviluppata. Prima del text freeze gli step 13-18 devono ricontrollare al cut-off fonti mobili, profilo DCAT-AP_IT, linee guida AgID, licenze e campo di applicazione dei dataset di elevato valore. Il capitolo non dichiara conclusi tali debiti specialistici o normativi.
