# Piano di completamento — Capitolo 07

## Target

`chapters/07-cloud-pa-virtualizzazione-container-devops.md`

## Impostazione proposta

Il capitolo segue il percorso operativo di un servizio pubblico che passa dall’analisi alla migrazione e poi all’esercizio:

1. modelli cloud e responsabilità;
2. virtualizzazione, container e orchestrazione;
3. migrazione al cloud nella PA;
4. DevOps, CI/CD e Infrastructure as Code;
5. osservabilità, resilienza, backup, disaster recovery e continuità operativa.

Questa progressione porta agli output richiesti dalla matrice — checklist di migrazione e caso cloud — senza trasformare il capitolo in un catalogo di prodotti o in una duplicazione dei capitoli su reti, cybersecurity, IAM e procurement.

## Esito della ricognizione

Il capitolo contiene soltanto frontmatter, titolo e specifica della struttura madre. La riga «Cloud e DevOps» della matrice è `parziale`: cloud, container, backup e business continuity non dispongono ancora di testo destinato al lettore.

Il VOL-01, capitolo 10, § 17, introduce cloud computing, IaaS, PaaS e SaaS e richiama classificazione dei dati e dei servizi, sicurezza, continuità, qualificazione del fornitore, localizzazione, reversibilità e lock-in. Il capitolo 7 deve assumerli come prerequisiti e sviluppare il livello specialistico: caratteristiche e modelli del cloud, responsabilità condivisa, macchine virtuali e container, orchestrazione, strategie di migrazione, DevOps, pipeline CI/CD, Infrastructure as Code, osservabilità, resilienza, backup, RPO, RTO, disaster recovery e continuità operativa.

I confini sono netti: il capitolo 5 tratta infrastrutture, disponibilità e troubleshooting; il capitolo 6 ciclo di vita, test, API e versionamento; il capitolo 8 minacce, vulnerabilità, controlli e secure coding; il capitolo 9 IAM, crittografia, logging di sicurezza e incident response; il capitolo 10 data governance; il capitolo 12 procurement, SLA e fornitori.

## Collegamento riga per riga alla matrice

| Campo della matrice | Presa in carico nel piano |
| --- | --- |
| Famiglia/profilo: ICT e Cloud | Teoria e casi calibrati sulla migrazione e sull’esercizio di servizi digitali pubblici. |
| Materia: Cloud e DevOps | Trattazione coordinata di modelli cloud, virtualizzazione, container, delivery e operazioni. |
| Concetti: cloud, container, backup, BC | Tutti ricevono definizioni, distinzioni, relazioni ed esempi; BC è sviluppata come business continuity. |
| Frequenza/peso: da validare | Nessuna frequenza quantitativa; piattaforme e profondità dipendono dai bandi del campione. |
| Fonte consolidata: dossier M-TR01 | Il dossier definisce il perimetro, ma non basta per i claim tecnici e regolatori. |
| Collocazione: capitolo 07 | Migrazione ed esercizio cloud restano qui; sicurezza, IAM, dati e procurement ricevono rinvii. |
| Copertura teorica: da sviluppare | Ogni nucleo avrà definizione, funzione, elementi, trade-off, conseguenze ed esempio. |
| Applicazione: checklist migrazione | Dall’assessment iniziale a dati, dipendenze, strategia, test, cutover, rollback, osservabilità e uscita. |
| Output: caso cloud | Caso motivato di migrazione di un servizio pubblico con vincoli, architettura, RPO/RTO e responsabilità. |
| Verifica: caso | Caso guidato, laboratorio, domanda-trappola, quiz e checklist. |
| Stato: parziale | Potrà passare a `completo` solo dopo la verifica del testo reale allo step 10. |
| Review: ACN | Necessari controllo della disciplina vigente, review cloud architecture, operations e continuità operativa. |

## Nuclei assegnati

1. Confine tra introduzione del VOL-01 e livello specialistico del VOL-08.
2. Cloud computing: servizio on demand, accesso in rete, condivisione delle risorse, elasticità e misurazione.
3. Modelli IaaS, PaaS e SaaS e ripartizione delle responsabilità.
4. Modelli di distribuzione pubblico, privato, ibrido e community, senza confondere public cloud e settore pubblico.
5. Regioni, zone, tenancy e collocazione dei dati a livello concettuale.
6. Responsabilità condivisa fra amministrazione, provider e altri fornitori.
7. Virtualizzazione: host, hypervisor, macchina virtuale, guest, immagine, template e snapshot.
8. Hypervisor di tipo 1 e 2; isolamento, allocazione e sovra-allocazione delle risorse.
9. Container: immagine, registry, container, runtime, livelli e persistenza.
10. Differenze fra macchina virtuale e container, evitando l’equivalenza «container = VM leggera».
11. Orchestrazione: stato desiderato, scheduling, replica, service discovery, scaling, configurazione e secret.
12. Assessment di migrazione: applicazioni, dati, dipendenze, prestazioni, compliance e vincoli.
13. Strategie di migrazione: rehost, replatform, refactor, repurchase, retain e retire, con terminologia da consolidare.
14. Portabilità, interoperabilità, reversibilità, lock-in ed exit strategy.
15. Classificazione dei dati e dei servizi della PA e conseguenze sulla destinazione cloud.
16. Strategia Cloud Italia, qualificazione dei servizi e quadro ACN vigente, da verificare prima del testo finale.
17. DevOps come cultura e modello operativo di collaborazione, feedback e automazione, non come ruolo o singolo strumento.
18. CI/CD: source, build, test, analisi, artefatto, release, deploy e verifica.
19. Differenza fra continuous integration, continuous delivery e continuous deployment.
20. Artefatti versionati, repository e promozione coerente fra ambienti.
21. Infrastructure as Code, configurazione dichiarativa, ripetibilità, versionamento e controllo delle modifiche.
22. Deployment progressivo, rollback e separazione fra rilascio tecnico e attivazione funzionale.
23. Monitoraggio e osservabilità; metriche, log, trace ed eventi.
24. Indicatori, soglie, dashboard e alert orientati a sintomi e impatto.
25. Capacità, autoscaling, consumo misurato e responsabilizzazione sui costi, con FinOps solo a livello concettuale.
26. Resilienza: ridondanza, bilanciamento, distribuzione su zone e degradazione controllata.
27. Backup completo, incrementale e differenziale a livello concettuale; retention, cifratura, immutabilità e test di ripristino.
28. Distinzione fra snapshot, replica e backup.
29. RPO e RTO come obiettivi diversi, collegati all’analisi d’impatto.
30. Disaster recovery: strategie, failover, failback, runbook ed esercitazioni.
31. Distinzione e relazione fra alta disponibilità, backup, disaster recovery e business continuity.
32. Cutover, rollback, comunicazione ed evidenze di una migrazione.
33. Caso cloud, checklist di migrazione, quiz, risposta orale e autovalutazione.

## Nuclei già completi

Nessun nucleo specialistico è completo nel capitolo 7.

Nel VOL-01, capitolo 10, § 17, sono già completi i prerequisiti:

- definizione introduttiva del cloud;
- distinzione essenziale fra IaaS, PaaS e SaaS;
- richiamo a classificazione dei dati e dei servizi;
- sicurezza e continuità come criteri di valutazione;
- qualificazione del fornitore, protezione e localizzazione dei dati;
- reversibilità e rischio di lock-in.

Il rinvio non copre virtualizzazione, container, orchestrazione, strategie di migrazione, responsabilità condivisa, DevOps, pipeline CI/CD, Infrastructure as Code, osservabilità, RPO/RTO, disaster recovery o progettazione della continuità.

## Nuclei da sviluppare

- caratteristiche, modelli e responsabilità del cloud;
- funzionamento concettuale di hypervisor, VM, immagini e snapshot;
- immagini, registry, runtime, container e orchestrazione;
- assessment e strategie di migrazione;
- classificazione e disciplina Cloud PA vigente;
- portabilità, reversibilità ed exit strategy;
- principi DevOps e flusso CI/CD;
- artefatti, ambienti, IaC, deployment e rollback;
- monitoraggio e osservabilità;
- capacità, elasticità e governo del consumo;
- resilienza, backup e ripristino;
- RPO, RTO, disaster recovery e business continuity;
- checklist di migrazione e caso cloud completo.

## Sezioni da conservare

- frontmatter e identificativi;
- H1 esistente;
- specifica della struttura madre come vincolo editoriale;
- collocazione nella Parte II del volume;
- output previsto: checklist di migrazione;
- review ACN.

## Duplicazioni da evitare

- introduzione generale al cloud e ai modelli di servizio già completa nel VOL-01;
- disponibilità, RAID, componenti di rete e troubleshooting generale del capitolo 5;
- ciclo di vita, test, API, versionamento del software e SLO introdotti nel capitolo 6;
- threat modeling, vulnerabilità, hardening, secure coding e supply chain del capitolo 8;
- IAM, crittografia, logging di sicurezza e incident response del capitolo 9;
- qualità e governance dei dati del capitolo 10;
- capitolati, clausole, SLA contrattuali e gestione dei fornitori del capitolo 12;
- tutorial su prodotti, comandi, manifest o servizi commerciali non richiesti dai bandi.

Il testo non deve affermare che il cloud sia sempre più economico o più sicuro, che uno snapshot equivalga a un backup, che la replica sostituisca il backup, che il backup coincida con la continuità o che i container siano macchine virtuali leggere.

## Esempi, casi, domande ed esercizi necessari

- classificazione di responsabilità in scenari IaaS, PaaS e SaaS;
- confronto motivato fra VM e container per un servizio applicativo;
- lettura concettuale di immagine, registry, runtime e orchestratore;
- scelta ragionata fra rehost, replatform e refactor;
- mappa di applicazioni, dati, dipendenze, vincoli e destinatari;
- pipeline CI/CD dal commit alla verifica in esercizio;
- esempio di modifica IaC sottoposta a review e applicata in modo ripetibile;
- distinzione fra metrica, log e trace durante un degrado;
- calcolo guidato dell’effetto di un RPO e di un RTO sul caso;
- confronto fra snapshot, replica, backup e disaster recovery;
- caso di migrazione di un servizio comunale con dati, dipendenze, cutover e rollback;
- domanda da commissario sulla responsabilità condivisa;
- domanda-trappola «se il servizio è replicato, il backup non serve?»;
- errore tipico: scegliere tecnologia e provider prima di classificare servizio, dati e vincoli;
- quiz su modelli cloud, container, CI/CD, osservabilità, backup e continuità;
- checklist finale «valuto, classifico, progetto, migro, verifico, osservo, ripristino, riesamino».

## Fonti da usare

### Fonti e pagine già consolidate

- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]] — per perimetro editoriale;
- [[sources/pa-digitale-cad-identita-documenti-servizi-dati]];
- [[sources/sicurezza-informatica-privacy-nis2-pa]];
- [[sources/reti-sistemi-infrastrutture-fonti-tecniche]];
- [[sources/campione-bandi-ict-pa-vol-08-2024-2026]];
- [[topics/open-data-interoperabilita-cloud-pa]];
- [[topics/ict-digitale-cybersecurity-dati-concorsi-pa]];
- [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali]], capitolo 10, § 17;
- [[books/moduli/m-tr01-ict-trasformazione-digitale/planning/02-matrice-copertura-didattica]].

### Fonti tecniche e istituzionali da consolidare prima o durante lo step 09

- NIST SP 800-145 per definizione, caratteristiche e modelli del cloud;
- specifiche e documentazione ufficiale OCI per immagini e runtime dei container;
- documentazione ufficiale Kubernetes per i concetti essenziali di orchestrazione;
- documentazione OpenTelemetry per metriche, log e trace;
- fonti primarie o standard accessibili per virtualizzazione, CI/CD, Infrastructure as Code, backup, RPO, RTO e continuità;
- Strategia Cloud Italia e documenti ufficiali vigenti;
- regolamento, determinazioni, cataloghi e documentazione ACN vigenti sulla classificazione e qualificazione cloud;
- Piano Triennale per l’informatica nella PA e aggiornamento vigente;
- bandi ufficiali del campione VOL-08 per validare piattaforme, certificazioni e tecnologie effettivamente richieste.

Le fonti consolidate attuali consentono il perimetro introduttivo e il raccordo PA, ma non bastano a sostenere tutti i claim specialistici. Le nuove fonti devono diventare source note consolidate prima del congelamento del testo. Terminologia, decorrenze e regime ACN richiedono verifica sulla versione vigente; non si inseriranno soglie o date ricordate a memoria.

## Topic, entity e quiz collegati

- `topics/open-data-interoperabilita-cloud-pa.md` offre il raccordo introduttivo con Cloud PA;
- `topics/ict-digitale-cybersecurity-dati-concorsi-pa.md` offre il quadro concorsuale del modulo;
- l’entity ACN è già associata al capitolo, ma richiede fonti granulari e aggiornate;
- non risultano topic specialistici consolidati sufficienti su virtualizzazione, container, CI/CD, osservabilità e continuità;
- non risultano quiz specialistici consolidati che coprano l’intero capitolo;
- esempi, quiz e caso devono essere verificati tecnicamente e contro i bandi del campione.

## Review umane richieste

- cloud architect: modelli, responsabilità, migrazione, resilienza e trade-off;
- platform engineer: virtualizzazione, container e orchestrazione;
- DevOps/SRE engineer: CI/CD, IaC, osservabilità, deployment e rollback;
- specialista backup e disaster recovery: copie, replica, ripristino, RPO e RTO;
- responsabile business continuity: analisi d’impatto, piani, esercitazioni e raccordo organizzativo;
- esperto ACN/Cloud PA: classificazione, qualificazione e terminologia vigente;
- DPO o privacy specialist: collocazione, trattamento, conservazione e trasferimento dei dati;
- esperto cybersecurity: responsabilità condivisa, secret e controlli, senza assorbire i capitoli 8-9;
- responsabile del campione bandi: profondità, tecnologie e certificazioni effettivamente richieste;
- responsabile editoriale: confini con VOL-01 e capitoli 5-6 e 8-12;
- revisore didattico: coerenza fra teoria, caso, checklist, quiz e risposta orale;
- revisore fonti: vigenza e granularità dei riferimenti ACN, AgID, NIST e standard tecnici.

## Struttura proposta e budget KDP

# Cloud PA, virtualizzazione, container e DevOps

## Obiettivo e confine con il VOL-01 — 170 parole

## Mappa BANDO dalla classificazione all’esercizio — 190 parole

## Modelli cloud e responsabilità — 500 parole

### Caratteristiche, modelli di servizio e distribuzione

### Responsabilità condivisa, regioni, zone e tenancy

## Virtualizzazione, container e orchestrazione — 540 parole

### Hypervisor, macchine virtuali, immagini e snapshot

### Immagini, registry, container e stato desiderato

## Cloud PA e percorso di migrazione — 620 parole

### Classificazione, qualificazione e vincoli

### Assessment, strategie, reversibilità ed exit strategy

## DevOps, CI/CD e Infrastructure as Code — 540 parole

### Cultura, feedback, artefatti e pipeline

### Ambienti, IaC, deployment progressivo e rollback

## Operabilità e osservabilità — 420 parole

### Metriche, log, trace, dashboard e alert

### Capacità, elasticità e governo del consumo

## Resilienza, backup e continuità operativa — 640 parole

### Ridondanza, backup, replica e ripristino

### RPO, RTO, disaster recovery e business continuity

## Caso guidato: migrazione di un servizio comunale — 310 parole

## Laboratorio: checklist di migrazione — 300 parole

## Domanda da commissario e domanda-trappola — 160 parole

## Errore tipico — 80 parole

## Mini-esercizi e quiz — 300 parole

## Checklist finale — 160 parole più tabella

## Da sapere in cinque righe — 60 parole

## Riferimenti consolidati e note di review — 100 parole

Budget orientativo: 4.500-4.900 parole, tabelle, schemi, caso ed esercizi inclusi. Il budget non comprende tutorial di prodotto, configurazioni eseguibili, controlli cyber di dettaglio, IAM specialistico, data governance o procurement.

## Criteri di approvabilità per lo step 09

- ogni elemento della specifica e della matrice riceve teoria e verifica;
- il rinvio al VOL-01 resta preciso e limitato ai prerequisiti;
- modelli di servizio, distribuzione e responsabilità non sono confusi;
- VM, container, immagini, snapshot, replica e backup restano distinti;
- orchestrazione e Kubernetes sono spiegati per concetti trasferibili, non come tutorial;
- strategie di migrazione sono presentate come scelte basate su vincoli e trade-off;
- disciplina e terminologia Cloud PA sono verificate su fonti ACN e istituzionali vigenti;
- DevOps non è ridotto a strumento, ruolo o sinonimo di automazione;
- continuous delivery e continuous deployment restano distinti;
- osservabilità non è ridotta alla sola raccolta di log;
- backup, disaster recovery, alta disponibilità e continuità operativa non sono usati come sinonimi;
- RPO e RTO sono definiti, applicati e collegati all’impatto;
- il caso dichiara servizio, dati, dipendenze, responsabilità, strategia, test, cutover, rollback e ripristino;
- cybersecurity, IAM, dati e procurement restano nei capitoli dedicati;
- esempi e casi applicano concetti già spiegati;
- fonti tecniche mancanti e review specialistiche restano aperte finché non eseguite.

## Addendum retrofit Format 2 — 2026-08-10

Questo addendum sostituisce, per il nuovo ciclo degli step 08-12, le valutazioni legacy sullo stato del capitolo. Il testo destinato al lettore esiste già: contiene circa 3.545 parole e costituisce la base da conservare. Lo step 09 dovrà riorganizzarlo nel Format 2 e colmare i delta misurabili, non riscriverlo da zero.

### Stato reale e criterio di intervento

- Il capitolo sviluppa già modelli cloud e responsabilità, virtualizzazione e container, migrazione Cloud PA, DevOps e CI/CD, osservabilità, backup, RPO/RTO, disaster recovery e continuità operativa.
- Sono presenti Mappa BANDO, confronto IaaS/PaaS/SaaS, tabella VM-container, caso comunale, laboratorio di migrazione, domanda da commissario, domanda-trappola, errore tipico, sette esercizi/quiz e checklist.
- La source note `sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie` consolida riferimenti NIST, OCI, Kubernetes, OpenTelemetry, ACN e continuità; disciplina, catalogo e terminologia Cloud PA restano da ricontrollare al text freeze.
- Il retrofit deve introdurre sei Nucleo ID stabili, almeno 600 parole per nucleo, una verifica dopo 5-7 nuclei e almeno sei quiz commentati.
- La riga `Cloud e DevOps` della matrice resta `completo` sul piano aggregato, ma lo step 10 dovrà dimostrare la copertura atomica dei sei nuclei Format 2.

### Nuclei Format 2 assegnati

| Nucleo ID | Titolo operativo | Stato attuale | Sviluppo previsto allo step 09 | Confini principali |
| --- | --- | --- | --- | --- |
| `N-TR01-07-01` | Modelli cloud e responsabilità condivisa | parziale-avanzato | Consolidare caratteristiche NIST, scalabilità/elasticità, IaaS/PaaS/SaaS, serverless, modelli di distribuzione, regioni, zone, tenancy e matrice delle responsabilità. | Reti e disponibilità infrastrutturale al cap. 5; SLA contrattuali al cap. 12. |
| `N-TR01-07-02` | Virtualizzazione, container e orchestrazione | parziale-avanzato | Collegare hypervisor, VM, immagini, snapshot, container, registry, runtime, persistenza, stato desiderato e riconciliazione a criteri di scelta e domini di guasto. | Sistemi operativi al cap. 2; hardening e supply chain al cap. 8. |
| `N-TR01-07-03` | Cloud PA e percorso di migrazione | parziale-avanzato | Integrare classificazione, qualificazione, PSN, assessment, strategie di migrazione, portabilità, reversibilità, exit strategy, cutover e rollback in una procedura verificabile. | Data governance al cap. 10; procurement e lock-in contrattuale al cap. 12. |
| `N-TR01-07-04` | DevOps, CI/CD e Infrastructure as Code | parziale | Sviluppare cultura DevOps, pipeline, artefatti, continuous integration/delivery/deployment, IaC, promozione, tecniche di distribuzione, rollback ed evidenze. | Ciclo di vita e test al cap. 6; Secure SDLC e controlli di filiera al cap. 8. |
| `N-TR01-07-05` | Operabilità, osservabilità e governo del consumo | parziale | Ampliare monitoraggio/osservabilità, metriche, log, trace, eventi, alert azionabili, SLI/SLO operativi, capacità, autoscaling e FinOps concettuale con un caso diagnostico. | Logging di sicurezza e incident response al cap. 9; SLA al cap. 12. |
| `N-TR01-07-06` | Resilienza, backup e continuità operativa | parziale-avanzato | Coordinare alta disponibilità, domini di guasto, degradazione, snapshot/replica/backup, ripristino, RPO/RTO, DR e business continuity; assorbire caso, laboratorio e output concorsuali. | Disponibilità di base al cap. 5; rischio cyber al cap. 8; continuità contrattuale al cap. 12. |

I sei nuclei devono superare autonomamente il test dello studente: definizione, funzione, inquadramento, elementi, distinzioni, conseguenze, esempio e verifica. Nessun nucleo è dichiarato completo in Format 2 prima del controllo dello step 10.

### Struttura H1/H2/H3 prevista

# Cloud PA, virtualizzazione, container e DevOps

## Obiettivo, confine con il VOL-01 e Mappa BANDO

## N-TR01-07-01 · Modelli cloud e responsabilità condivisa

### Caratteristiche, modelli di servizio e distribuzione

### Responsabilità, regioni, zone e tenancy

## N-TR01-07-02 · Virtualizzazione, container e orchestrazione

### Hypervisor, VM, immagini e snapshot

### Container, persistenza, stato desiderato e riconciliazione

## N-TR01-07-03 · Cloud PA e percorso di migrazione

### Classificazione, qualificazione e assessment

### Strategie, reversibilità, cutover e rollback

## N-TR01-07-04 · DevOps, CI/CD e Infrastructure as Code

### Cultura, pipeline, artefatti e ambienti

### IaC, distribuzione progressiva e rollback

## N-TR01-07-05 · Operabilità, osservabilità e governo del consumo

### Metriche, log, trace, eventi e alert

### Capacità, autoscaling, SLI/SLO e costi

## N-TR01-07-06 · Resilienza, backup e continuità operativa

### Disponibilità, domini di guasto, copie e ripristino

### RPO, RTO, disaster recovery e business continuity

### Caso guidato, laboratorio e output concorsuali

### Domanda da commissario, domanda-trappola ed errore tipico

## ▣ Verifica

### Tre o più esercizi applicativi

### Sei o più quiz commentati

## Checklist finale

## Da sapere in 5 righe

## Riferimenti professionali essenziali

### Budget e prove previste

- Corpo complessivo: **4.700-5.700 parole**, escluso frontmatter.
- Densità: **600-900 parole per ciascun Nucleo ID**; eventuali scostamenti richiedono motivazione didattica.
- Verifiche: **un unico blocco dopo i sei nuclei**, entro il limite di 5-7 nuclei consecutivi.
- Quiz: **almeno sei**, con risposta corretta e commento sui distrattori o sull’errore tipico.
- Esercizi: **almeno tre** — responsabilità cloud, strategia di migrazione e continuità/ripristino.
- Casi: **almeno uno completo**, con servizio, dati, dipendenze, responsabilità, strategia, test, cutover, rollback e ripristino.
- Output: confronto dei modelli, matrice VM-container, piano/checklist di migrazione, scenario di continuità e risposta orale motivata.

### Fonti, topic, entity e rinvii da preservare

- Conservare tutti i `source_refs` e i `last_compiled_from` attuali, inclusa la source note primaria su cloud, container, DevOps e continuità.
- Usare `topics/open-data-interoperabilita-cloud-pa` e `topics/ict-digitale-cybersecurity-dati-concorsi-pa` come raccordi, non come sostituti delle fonti specialistiche.
- Conservare le entity ACN, NIST, Kubernetes e OpenTelemetry soltanto nei punti sostenuti dalle fonti dichiarate.
- Mantenere il rinvio preciso al VOL-01, capitolo 10, § 17, limitato ai prerequisiti su cloud e modelli di servizio.
- Conservare i confini con i capp. 5-6, 8-10 e 12 fissati dal piano e dalla Bibbia del modulo.

### Audit specialistici richiesti

1. `chapter-lint` e controllo di densità didattica Format 2.
2. Audit cloud architecture su modelli, responsabilità, migrazione, resilienza e trade-off.
3. Audit platform engineering su virtualizzazione, container, orchestrazione, persistenza e domini di guasto.
4. Audit DevOps/SRE su CI/CD, IaC, distribuzione, rollback, osservabilità, capacità e SLI/SLO.
5. Audit backup/DR/BC su copie, replica, ripristino, RPO/RTO, failover, failback ed esercitazioni.
6. Audit ACN/Cloud PA su classificazione, qualificazione, catalogo, PSN e terminologia vigente.
7. Controllo dei confini con VOL-01 e con i capitoli 5-6 e 8-12.
8. Citation guard su `source_refs`, `last_compiled_from`, riferimenti istituzionali e professionali.
9. Revisione editoriale a 30 punti, test dello studente e controllo KDP su tabelle e stringhe tecniche.

### Criterio di uscita aggiornato

Lo step 09 è approvabile quando i sei Nucleo ID compaiono nel capitolo, ogni nucleo supera la soglia e il test dello studente, la verifica contiene almeno sei quiz commentati e tre esercizi, il caso cloud collega classificazione, dipendenze, responsabilità, migrazione, esercizio e ripristino e il corpo non dipende da materiali interni. Lo step 10 dovrà dimostrare la copertura reale nella matrice; gli step 11-12 completeranno Humanizer e revisione editoriale senza anticipare la conferma umana dello step 24.
