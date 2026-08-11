---
id: m-tr01-capitolo-11-piano-completamento
type: chapter_plan
title: "Piano di completamento — Capitolo 11 AI/ML nella PA: modelli, rischi e compliance"
status: retrofit-format-2-ready
domain: "concorsi pubblici italiani"
topics: ["intelligenza artificiale", "machine learning", "AI Act", "rischio algoritmico", "governance AI"]
entities: ["Unione europea", "AgID", "Agenzia per la cybersicurezza nazionale"]
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/legge-23-settembre-2025-n-132-intelligenza-artificiale"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "vol-08-ict-digitale-cybersecurity-dati", "il-metodo-bando"]
confidence: 0.78
updated_at: 2026-08-11
created_at: 2026-07-30
review_required: true
canonical: false
tags: ["planning", "m-tr01", "chapter-11", "ai", "machine-learning", "ai-act"]
chapter_ref: "chapters/11-ai-ml-pa-rischi-compliance.md"
---

# Piano di completamento — Capitolo 11

## 1. Funzione del capitolo

Il capitolo deve fornire al candidato ICT/Data una base tecnica e organizzativa sufficiente per descrivere un sistema di intelligenza artificiale, valutarne prestazioni e rischi e impostarne il governo nella pubblica amministrazione. Il lettore non deve diventare un data scientist, ma deve saper distinguere dati, modello, addestramento, inferenza, metriche, controlli e responsabilità.

Il filo conduttore è il ciclo di vita di un caso d'uso pubblico: problema amministrativo, dati, progettazione, valutazione, rilascio, uso umano, monitoraggio e dismissione. La compliance non va ridotta a un elenco di articoli; deve diventare un insieme di decisioni ed evidenze verificabili.

L'output centrale è composto da:

- scheda del caso d'uso AI;
- griglia di classificazione e rischio;
- scheda dati e modello;
- piano di controllo umano;
- registro di test, incidenti, drift e azioni correttive.

## 2. Stato iniziale

Il capitolo contiene soltanto frontmatter, H1 e specifica della struttura madre. La matrice assegna «modelli, rischi, controllo», con output «griglia rischio» e «caso algoritmo», ma classifica il nucleo `parziale`.

La source note generale di M-TR01 definisce il perimetro editoriale, non sostiene claim tecnici o normativi. La nota [[sources/legge-23-settembre-2025-n-132-intelligenza-artificiale]] deriva da una cattura automatica incompleta e non è utilizzabile, allo stato, per attribuire obblighi puntuali. Prima dello step 09 servono fonti primarie UE, italiane e tecniche consolidate.

## 3. Nuclei assegnati

### 3.1 Concetti fondamentali

- differenza tra automazione deterministica, algoritmo, sistema di IA e machine learning;
- modello, parametri, feature, label, dataset e pipeline;
- addestramento e inferenza;
- classificazione, regressione, clustering e generazione;
- sistemi predittivi, raccomandativi e generativi;
- limiti: correlazione non equivale a causalità; output plausibile non equivale a output corretto.

### 3.2 Paradigmi di apprendimento

- apprendimento supervisionato;
- apprendimento non supervisionato;
- apprendimento per rinforzo a livello concettuale;
- addestramento, validazione e test;
- generalizzazione;
- underfitting, overfitting e leakage;
- scelta del paradigma in rapporto al problema e ai dati disponibili.

### 3.3 Dati per l'AI

- rappresentatività, qualità, provenienza e liceità;
- raccolta, etichettatura e documentazione;
- sbilanciamento delle classi;
- dati mancanti, proxy e variabili sensibili;
- separazione dei dataset e prevenzione della contaminazione;
- raccordo con data governance, lineage, minimizzazione e sicurezza del capitolo 10.

### 3.4 Valutazione del modello

- baseline e confronto con il processo esistente;
- matrice di confusione;
- accuratezza, precision, recall e F1 per la classificazione;
- falsi positivi e falsi negativi come conseguenze amministrative;
- metriche di regressione a livello introduttivo;
- calibrazione, robustezza e test su sottogruppi;
- soglie decisionali motivate dal caso d'uso;
- distinzione tra prestazione tecnica, utilità operativa e impatto sui destinatari.

### 3.5 Bias, equità e spiegabilità

- bias nei dati, nel campionamento, nelle etichette, nel modello e nell'uso;
- differenza tra errore statistico, discriminazione e disparità di risultato;
- metriche di fairness come strumenti contestuali, non garanzia automatica;
- interpretabilità globale e spiegazione locale;
- trasparenza sul sistema e spiegazione del singolo output;
- limiti delle tecniche post-hoc;
- contestazione, riesame e comprensibilità per utenti e operatori.

### 3.6 Controllo umano

- human-in-the-loop, human-on-the-loop e human-in-command come modelli organizzativi;
- competenza, autorità e tempo effettivo per intervenire;
- rischio di automation bias e approvazione meramente formale;
- gestione delle eccezioni, escalation e override;
- tracciamento di input, output, decisione umana e motivazione;
- distinzione tra supporto alla decisione e decisione amministrativa.

### 3.7 Ciclo di vita e MLOps

- definizione del problema e criteri di successo;
- sperimentazione e validazione;
- versionamento di dati, codice e modello;
- rilascio controllato;
- monitoraggio delle prestazioni;
- data drift, concept drift e deterioramento;
- rollback, riaddestramento, sospensione e dismissione;
- registro delle modifiche e riproducibilità;
- raccordo con software lifecycle, DevOps e sicurezza dei capitoli 6-9.

### 3.8 Rischio e governance

- rischio per diritti, persone, servizi, organizzazione e sicurezza;
- probabilità, gravità, esposizione e reversibilità;
- uso previsto, uso improprio ragionevolmente prevedibile e dipendenze;
- ruoli del titolare del caso d'uso, funzione tecnica, fornitore, operatori e controllori;
- inventario dei sistemi AI;
- valutazione iniziale, controlli, accettazione del rischio ed evidenze;
- procurement, lock-in, dati del fornitore e responsabilità contrattuali, con rinvio al capitolo 12.

### 3.9 Quadro UE e italiano

Da sviluppare soltanto dopo consolidamento delle fonti:

- definizioni e campo del regolamento (UE) 2024/1689;
- pratiche vietate;
- sistemi ad alto rischio;
- obblighi di trasparenza pertinenti;
- modelli di IA per finalità generali, solo al livello necessario al profilo;
- ruoli lungo la catena del valore e distinzione tra provider e deployer;
- alfabetizzazione in materia di IA;
- sorveglianza umana, accuratezza, robustezza, cybersicurezza, registrazione e documentazione;
- calendario applicativo verificato alla data di cutoff;
- raccordo con GDPR, disciplina amministrativa, cybersecurity e legge italiana n. 132/2025;
- competenze e atti nazionali, senza anticipare interpretazioni o scadenze non consolidate.

## 4. Nuclei già completi

Nessun nucleo specialistico è completo nel file del capitolo.

Sono disponibili soltanto prerequisiti:

- capitolo 3: algoritmo, complessità e correttezza;
- capitolo 4: basi dati, vincoli e qualità tecnica;
- capitolo 6: ciclo di vita software, test, versionamento e API;
- capitoli 8-9: rischio, sicurezza, logging e incident response;
- capitolo 10: governance dei dati, lineage, qualità, privacy e responsabilizzazione;
- VOL-01: nozioni digitali comuni e uso prudente dell'AI come supporto, non teoria specialistica AI/ML.

Questi prerequisiti vanno richiamati con destinazioni precise, non duplicati.

## 5. Nuclei da sviluppare

Tutti i nuclei del § 3 devono essere sviluppati. Le priorità sono:

1. costruire una progressione tecnica autonoma da dati a modello e metriche;
2. collegare gli errori statistici alle conseguenze amministrative;
3. distinguere bias, fairness, spiegabilità e trasparenza;
4. rendere operativo il controllo umano;
5. applicare risk management e lifecycle a un caso PA;
6. trattare AI Act e legge italiana con fonti aggiornate e linguaggio non assertivo oltre il perimetro verificato.

## 6. Sezioni da conservare

- frontmatter e identificativo `chapter-m-tr01-11`;
- H1 «AI/ML nella PA: modelli, rischi e compliance»;
- `outline_section: 11`;
- promessa della struttura madre: apprendimento, dati, valutazione, bias, spiegabilità, controllo umano e rischio;
- output «griglia rischio» e «caso algoritmo»;
- richiesta di review AI Act e fonti ufficiali.

## 7. Duplicazioni da evitare

- algoritmi generali, pseudocodice, strutture dati e complessità del capitolo 3;
- teoria di database e SQL del capitolo 4;
- ciclo di sviluppo, testing e API del capitolo 6;
- DevOps generale del capitolo 7;
- risk assessment cyber, vulnerability management e secure SDLC del capitolo 8;
- IAM, logging e incident response del capitolo 9;
- data governance, metadati, qualità e open data del capitolo 10;
- disciplina generale di privacy, procedimento e trasparenza del VOL-01;
- procurement e SLA del capitolo 12;
- tutorial matematici, implementazioni Python o cataloghi di algoritmi non richiesti dalla promessa del volume.

Il capitolo deve usare questi contenuti come prerequisiti e concentrarsi sul loro adattamento al sistema AI.

## 8. Caso guidato

### Caso principale: priorità delle segnalazioni di manutenzione

Un comune valuta un sistema che assegna una priorità alle segnalazioni su strade ed edifici pubblici. Il modello non adotta il provvedimento finale: supporta la coda di lavoro degli operatori.

Il caso deve far emergere:

1. problema e baseline manuale;
2. stakeholder e persone potenzialmente interessate;
3. dati storici, etichette e possibili proxy territoriali;
4. separazione train-validation-test;
5. falsi positivi e falsi negativi;
6. soglia e criteri di escalation;
7. spiegazione utile all'operatore;
8. controllo umano sostanziale;
9. logging, versionamento e monitoraggio;
10. drift dopo cambiamenti di processo;
11. valutazione del rischio e classificazione normativa;
12. sospensione o rollback.

Il caso non deve presumere la classificazione AI Act: la griglia deve guidare la verifica sul testo vigente e sul caso concreto.

### Microcaso generativo

Uso di un modello generativo per predisporre una bozza di risposta al cittadino. Il microcaso serve a distinguere assistenza redazionale, verifica delle fonti, dati inseriti nel prompt, allucinazioni, autorizzazione alla pubblicazione e responsabilità umana.

## 9. Output compilabili

### Scheda del caso d'uso

Finalità, processo, destinatari, decisione supportata, output, dati, modello, owner, operatori, fornitore, base applicabile, rischi, controlli, evidenze e stato.

### Griglia di rischio

| Dimensione | Domanda | Evidenza | Livello | Controllo | Responsabile |
| --- | --- | --- | --- | --- | --- |
| diritti | chi può subire un effetto? | mappa stakeholder | da valutare | riesame | owner |
| dati | sono rappresentativi e documentati? | datasheet | da valutare | test sottogruppi | steward |
| modello | quali errori produce? | report metriche | da valutare | soglia/override | team tecnico |
| esercizio | il controllo umano è effettivo? | log decisioni | da valutare | escalation | process owner |

La griglia non assegna automaticamente la classe giuridica prevista dall'AI Act.

### Scheda dati e modello

- provenienza e versione dei dati;
- finalità e popolazione;
- etichettatura e qualità;
- partizioni di addestramento, validazione e test;
- algoritmo e versione;
- metriche complessive e per sottogruppi;
- limiti noti;
- condizioni d'uso e usi esclusi;
- monitoraggio e criteri di ritiro.

### Piano di controllo umano

Decisioni riservate alla persona, informazioni mostrate, spiegazione, soglie di escalation, potere di override, competenze, tempi, contestazione e tracciamento.

## 10. Domande ed esercizi

### Domanda da commissario

«Come valuteresti e governeresti un sistema di machine learning usato da un comune per dare priorità alle segnalazioni?»

La risposta modello deve coprire finalità, dati, baseline, metriche, errori, bias, controllo umano, sicurezza, monitoraggio, rischio, classificazione normativa ed evidenze.

### Domande-trappola

- accuratezza elevata significa sistema equo?
- un modello spiegabile è automaticamente corretto?
- controllo umano significa cliccare “approva”?
- usare dati storici elimina il bias?
- pseudonimizzare rende i dati anonimi?
- un output generativo plausibile è una fonte?
- un sistema non ad alto rischio è privo di obblighi?
- acquistare un servizio trasferisce al fornitore ogni responsabilità?

### Esercizi

1. distinguere automazione deterministica, ML e generative AI;
2. interpretare una matrice di confusione;
3. scegliere la metrica in base al costo dell'errore;
4. individuare leakage e proxy;
5. compilare la griglia di rischio;
6. progettare un controllo umano effettivo;
7. riconoscere un caso di drift;
8. formulare una risposta orale con rubriche di valutazione.

Tutti gli esercizi devono avere soluzione ragionata o criteri verificabili.

## 11. Fonti consolidate disponibili

- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]]: perimetro editoriale, non fonte tecnica o normativa;
- [[sources/legge-23-settembre-2025-n-132-intelligenza-artificiale]]: fonte istituzionale da riprocessare prima dell'uso;
- [[sources/programmazione-algoritmi-strutture-dati-fonti-tecniche]]: prerequisiti sugli algoritmi;
- [[sources/basi-dati-sql-nosql-qualita-fonti-tecniche]]: prerequisiti su dati e qualità;
- [[sources/ingegneria-software-api-interoperabilita-fonti-tecniche]]: prerequisiti su lifecycle e test;
- [[sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie]]: metodo di rischio e sicurezza;
- [[sources/data-governance-open-data-interoperabilita-fonti-primarie]]: governance e qualità dei dati.

## 12. Fonti da consolidare prima dello step 09

Creare una source note specialistica primaria che comprenda:

- regolamento (UE) 2024/1689 nel testo ufficiale vigente e relativo calendario applicativo;
- FAQ, linee guida e atti della Commissione europea o AI Office pertinenti;
- legge 23 settembre 2025, n. 132, riprocessata articolo per articolo dal testo vigente;
- Strategia italiana per l'intelligenza artificiale e documenti istituzionali pertinenti alla PA;
- eventuali linee guida AgID/ACN vigenti sull'adozione di AI nella PA;
- GDPR e fonti EDPB pertinenti a decisioni automatizzate e profilazione, con rinvio alla sede privacy;
- NIST AI Risk Management Framework 1.0 e relativo profilo generative AI, come riferimenti tecnici non normativi;
- documentazione tecnica primaria per metriche, model cards e datasheets, preferendo standard o pubblicazioni istituzionali.

La source note deve indicare autorità, versione, data di consultazione, claim sostenuti, campo di applicazione e limiti. Scadenze, categorie e obblighi non devono entrare nel capitolo prima di questa verifica.

## 13. Topic, entity e quiz

Creare o aggiornare:

- `topics/intelligenza-artificiale-machine-learning-governance-pa.md`;
- entity per regolamento (UE) 2024/1689 soltanto dopo source note primaria;
- collegamenti ad AgID, ACN, Commissione europea e AI Office quando sostenuti dalle fonti;
- quiz specialistici riutilizzabili su metriche, bias, controllo umano e classificazione del rischio.

La topic page generale ICT non è sufficiente per sostenere il capitolo.

## 14. Review umane richieste

- data scientist o ML engineer per paradigma, metriche, leakage e drift;
- MLOps engineer per versionamento, monitoraggio e rollback;
- esperto responsible AI per bias, fairness, spiegabilità e human oversight;
- giurista AI Act e diritto amministrativo;
- DPO per dati personali, profilazione e decisioni automatizzate;
- security architect per robustezza, attacchi e logging;
- responsabile di procedimento o dirigente PA per controllo umano e responsabilità;
- procurement specialist per ruoli del fornitore e clausole, in raccordo col capitolo 12;
- revisore editoriale e impaginatore KDP.

## 15. Struttura H1/H2/H3

# AI/ML nella PA: modelli, rischi e compliance

## Obiettivo e confini

## Mappa BANDO del sistema AI

## Dall'automazione al machine learning
### Algoritmo, sistema AI e modello
### Addestramento e inferenza
### Predittivo, raccomandativo e generativo

## Paradigmi di apprendimento
### Supervisionato e non supervisionato
### Apprendimento per rinforzo
### Train, validation e test

## Dati per l'AI
### Provenienza, qualità ed etichette
### Rappresentatività, classi e proxy
### Leakage, minimizzazione e sicurezza

## Valutare un modello
### Baseline e matrice di confusione
### Accuracy, precision, recall e F1
### Errori, soglie e conseguenze amministrative
### Robustezza, calibrazione e sottogruppi

## Bias, fairness e spiegabilità
### Dove nasce il bias
### Equità e limiti delle metriche
### Interpretabilità e spiegazione

## Controllo umano
### Human-in/on-the-loop e human-in-command
### Automation bias, override ed escalation
### Contestazione, riesame ed evidenze

## Ciclo di vita e MLOps
### Versioni, rilascio e riproducibilità
### Monitoraggio, drift e incidenti
### Riaddestramento, rollback e dismissione

## Rischio e governance nella PA
### Inventario, ruoli e responsabilità
### Valutazione e trattamento del rischio
### Fornitori e raccordo con il procurement

## Quadro UE e italiano
### Approccio basato sul rischio dell'AI Act
### Pratiche vietate, alto rischio e trasparenza
### Ruoli, documentazione e alfabetizzazione AI
### Raccordo italiano, privacy e sicurezza

## Caso guidato: priorità delle segnalazioni

## Microcaso: bozza generativa per il cittadino

## Laboratorio: griglia rischio e schede

## Domanda da commissario

## Domande-trappola

## Mini-esercizi e soluzioni

## Checklist finale

## Da sapere in 5 righe

## Riferimenti consolidati

## Note di review

## 16. Budget KDP

| Blocco | Parole orientative |
| --- | ---: |
| apertura, obiettivo e Mappa BANDO | 300-400 |
| concetti e paradigmi | 700-900 |
| dati per l'AI | 550-700 |
| valutazione e metriche | 750-950 |
| bias, fairness e spiegabilità | 650-850 |
| controllo umano | 450-600 |
| ciclo di vita e MLOps | 550-700 |
| rischio e governance PA | 550-700 |
| quadro UE e italiano | 700-900 |
| casi e laboratorio | 700-900 |
| orale, trappole, esercizi e checklist | 550-700 |
| riferimenti e note di review | 150-250 |
| **Totale** | **6.600-8.550** |

Le formule devono restare minime e leggibili. Tabelle di metriche e rischio vanno divise se superano la larghezza della pagina paperback KDP.

## 17. Criteri di accettazione dello step 09

- ogni nucleo ha teoria autonoma prima di casi e checklist;
- automazione, algoritmo, AI, ML e generative AI sono distinti;
- paradigma, dati, addestramento, inferenza e valutazione seguono una progressione;
- metriche ed errori sono collegati a conseguenze concrete;
- bias, fairness, spiegabilità e trasparenza non sono trattati come sinonimi;
- il controllo umano è sostanziale, non una firma formale;
- lifecycle, drift, incidenti e dismissione sono sviluppati;
- rischio tecnico, amministrativo e per i diritti sono integrati;
- AI Act e legge italiana derivano da fonti primarie consolidate e aggiornate;
- il caso non presume la classificazione normativa;
- output compilabili ed esercizi hanno soluzioni o criteri;
- rinvii a capitoli precedenti e VOL-01 sono precisi;
- frontmatter e source refs sono veritieri.

## 18. Esito del piano

Il piano è pronto. Lo step 09 non deve iniziare la scrittura normativa finché non siano state consolidate una source note specialistica sull'AI Act e una versione utilizzabile della legge italiana n. 132/2025. Il capitolo può essere progettato fin d'ora sul piano tecnico, ma date, classi, ruoli e obblighi devono essere verificati sul testo ufficiale vigente.

## 19. Retrofit Format 2 — piano esecutivo 2026-08-11

Il piano conserva la struttura utile già definita e la rende eseguibile nella pipeline aggiornata. I sette nuclei sono: `N-TR01-11-01` algoritmo, sistema AI, modello e inferenza; `N-TR01-11-02` paradigmi, partizioni e generalizzazione; `N-TR01-11-03` dati, provenienza, etichette e rappresentatività; `N-TR01-11-04` baseline, metriche e conseguenze degli errori; `N-TR01-11-05` bias, fairness, spiegabilità e controllo umano; `N-TR01-11-06` lifecycle, MLOps, rischio e governance; `N-TR01-11-07` quadro UE e italiano, ruoli e confini.

Ogni nucleo avrà almeno 600 parole, definizione, funzione, elementi, distinzioni, conseguenze, applicazione e verifica. Dopo il settimo nucleo sarà inserito un unico blocco `▣ Verifica` con sei quiz commentati, il caso della priorità alle segnalazioni, il microcaso generativo e una griglia di rischio compilabile. Restano da conservare apertura, Mappa BANDO, domanda da commissario, domande-trappola, esercizi e checklist; sono da evitare duplicazioni con i capitoli 03 (algoritmi), 04 e 10 (dati), 06 (lifecycle software), 08-09 (rischio e logging) e 12 (fornitore).

Le fonti consolidate sostengono i concetti tecnici, il regolamento (UE) 2024/1689, il raccordo prudente alla legge n. 132/2025, AgID e NIST. La copertura didattica può essere chiusa per il lettore; calendario AI Act, atti modificativi, linee guida definitive, applicazione della legge italiana e stato delle versioni NIST restano debiti mobili degli step 13-18. Nessuna classificazione giuridica o scadenza viene dedotta automaticamente dal caso.