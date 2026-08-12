# Pacchetto di review umana specialistica — M-TR01

## Identificazione

- Volume: VOL-08
- Modulo: M-TR01 — ICT e trasformazione digitale
- Revisore responsabile: Alberto Brando
- Data di preparazione: 2026-08-05
- Perimetro: premessa, indice, matrice e capitoli 01-13
- Stato: in attesa di review e firma umana

## Istruzioni per la firma

Per ogni riga compilare `Esito` con `Approvato`, `Correggere` o `Non applicabile`, aggiungendo nome e data. Se l'esito è `Correggere`, indicare in `Eventuale correzione` il testo o la decisione da applicare. Un'approvazione generale non sostituisce gli esiti sulle singole voci.

## Checklist specialistica

| ID | File e posizione | Affermazione | Fonte consolidata | Domanda al revisore | Esito | Eventuale correzione |
| --- | --- | --- | --- | --- | --- | --- |
| HR01 | Cap. 01, «Le famiglie di profilo» | I profili ICT sono distinti in generalista, infrastrutture/cloud, cyber, data/AI e alta professionalità; il campione non autorizza frequenze statistiche. | `sources/campione-bandi-ict-pa-vol-08-2024-2026` | Tassonomia e limiti inferenziali sono corretti per i bandi esaminati? |  |  |
| HR02 | Cap. 02, ciclo di istruzione e gerarchia di memoria | CPU, registri, cache, RAM e I/O sono descritti mediante un modello concettuale, senza attribuire dettagli microarchitetturali universali. | `sources/architettura-sistemi-rappresentazione-prestazioni-fonti-tecniche` | Definizioni, relazioni causa-effetto ed esercizi sono tecnicamente corretti? |  |  |
| HR03 | Cap. 03, algoritmi e complessità | Pseudocodice, strutture dati, ricerca, ordinamento e notazione di complessità sono presentati indipendentemente da uno specifico linguaggio. | `sources/programmazione-algoritmi-strutture-dati-fonti-tecniche` | Esempi, trace table, soluzioni e livello di astrazione sono corretti? |  |  |
| HR04 | Cap. 04, normalizzazione e SQL | Chiavi, vincoli, 1NF-3NF, join, aggregazioni, transazioni ACID, indici e famiglie NoSQL sono distinti per funzione. | `sources/basi-dati-sql-nosql-qualita-fonti-tecniche` | Schemi, query e soluzioni sono corretti e non dipendono indebitamente da un DBMS? |  |  |
| HR05 | Cap. 05, reti e sistemi | Modelli a livelli, Ethernet/VLAN, IPv4/IPv6, trasporto, servizi, processi, memoria e troubleshooting sono collegati per funzione ed evidenza. | `sources/reti-sistemi-infrastrutture-fonti-tecniche` | Subnetting, protocolli, casi e diagnosi sono corretti per una prova generalista ICT? |  |  |
| HR06 | Cap. 06, requisiti e test | Requisito, criterio di accettazione, verifica, validazione, livelli di test e tracciabilità sono concetti distinti. | `sources/ingegneria-software-api-interoperabilita-fonti-tecniche` | Le definizioni e la matrice requisito-test-evidenza sono corrette? |  |  |
| HR07 | Cap. 06, «ModI, PDND ed e-service» | Erogatore, fruitore, e-service, finalità e fruizione sono descritti con rinvio alla documentazione vigente. | `sources/pa-digitale-cad-identita-documenti-servizi-dati`; `sources/agid-piano-triennale-informatica-pa-2024-2026-aggiornamento-2026` | Terminologia, ruoli e sequenza logica ModI/PDND sono corretti al cut-off? |  |  |
| HR08 | Cap. 06 e 10, interoperabilità UE | Il Regolamento (UE) 2024/903 è richiamato senza estenderne automaticamente gli obblighi a ogni progetto locale. | fonti UE consolidate nei capitoli 06 e 10 | Campo, conseguenze didattiche e formulazione prudenziale sono corretti? |  |  |
| HR09 | Cap. 07, Cloud PA | Classificazione di dati/servizi, qualificazione cloud e catalogo sono ricondotti al quadro Cloud Italia/ACN e marcati mobili. | `sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie` | Regolamento, competenze, categorie e terminologia sono vigenti? |  |  |
| HR10 | Cap. 07, virtualizzazione e container | VM, immagini, snapshot, container, registry, runtime, orchestrazione e persistenza sono distinti per isolamento e ciclo di vita. | `sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie` | Distinzioni ed esercizi sono tecnicamente corretti e non vendor-specific? |  |  |
| HR11 | Cap. 07, continuità | Backup, replica, snapshot, alta disponibilità, RPO, RTO, DR e business continuity hanno funzioni diverse; RPO/RTO derivano dall'impatto. | fonte cloud/continuità consolidata | Definizioni, casi e soluzioni sono corretti? |  |  |
| HR12 | Cap. 08, rischio cyber | Asset, minaccia, vulnerabilità, scenario, probabilità, impatto, rischio inerente/residuo e trattamento sono distinti. | `sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie` | Matrice, caso, laboratorio e priorità di trattamento sono corretti? |  |  |
| HR13 | Cap. 08, CVE/CWE/CVSS e vulnerabilità | Il punteggio CVSS non sostituisce la priorità contestuale; inventario, esposizione, impatto e controlli modificano la decisione. | fonte cyber consolidata | Definizioni, versioni richiamate e esercizi sono accurati? |  |  |
| HR14 | Cap. 08, secure SDLC e supply chain | Secure design/coding, test, dipendenze, provenienza, attestazioni e SBOM sono controlli distinti e non garanzie assolute. | fonte cyber/supply-chain consolidata | Perimetro e terminologia sono corretti rispetto alle edizioni tecniche vigenti? |  |  |
| HR15 | Cap. 09, IAM e crittografia | Identità, account, autenticatore, autenticazione, autorizzazione, RBAC/ABAC/ACL, minimo privilegio e ciclo delle chiavi sono distinti. | `sources/iam-crittografia-logging-incident-response-fonti-primarie` | Definizioni, esempi e gestione del secret compromesso sono corretti? |  |  |
| HR16 | Cap. 09, logging e incident response | Evento, log, audit trail, alert e incidente sono distinti; preparazione, rilevazione, triage, contenimento e recupero formano un ciclo. | fonte IAM/IR consolidata; NIST CSF 2.0 | Sequenza, ruoli, timeline e playbook sono adeguati? |  |  |
| HR17 | Cap. 09, NIS2/CSIRT/privacy | Il d.lgs. 138/2024 recepisce NIS2; platea, significatività, procedure, canali e termini sono dichiarati mobili; incidente cyber e data breach non coincidono. | d.lgs. 138/2024 e atti ACN consolidati | Quadro, competenze e distinzione privacy sono corretti al cut-off? |  |  |
| HR18 | Cap. 10, open data | Pubblicazione web, trasparenza, accesso, open data e scambio interoperabile sono distinti; il riuso richiede condizioni, metadati e formati adeguati. | `sources/data-governance-open-data-interoperabilita-fonti-primarie` | Distinzioni, licenze, DCAT-AP_IT e caso sono corretti? |  |  |
| HR19 | Cap. 10, dataset di elevato valore | Direttiva (UE) 2019/1024 e Regolamento di esecuzione (UE) 2023/138 sono richiamati con categorie e cautele applicative. | fonte open data consolidata | Categorie, condizioni, API/download e limiti sono formulati correttamente? |  |  |
| HR20 | Cap. 11, metriche ML | Train/validation/test, leakage, overfitting, matrice di confusione, accuracy, precision, recall, F1, robustezza e sottogruppi sono distinti. | `sources/ai-ml-governance-rischi-compliance-fonti-primarie` | Definizioni, esempi numerici e soluzioni sono tecnicamente corretti? |  |  |
| HR21 | Cap. 11, AI Act | Il quadro è basato sul rischio; il capitolo evita scadenze puntuali e rinvia il calendario alla fonte ufficiale. | fonte AI/ML consolidata; Commissione europea | Classi, obblighi, calendario e quadro italiano sono corretti al cut-off? |  |  |
| HR22 | Cap. 11, controllo umano e caso | Human-in/on-the-loop e human-in-command richiedono competenza, informazione, autorità, escalation e override effettivi. | fonte AI/ML consolidata | Terminologia, rischio di automation bias e caso PA sono corretti? |  |  |
| HR23 | Cap. 12, requisiti, SLA e ruoli | Requisito, criterio, obbligo, SLA, SLI e KPI sono distinti; RUP, DEC, owner tecnico, sicurezza e DPO hanno funzioni non sovrapponibili. | `sources/procurement-ict-sla-vendor-management-fonti-consolidate` | Definizioni, ruoli e schede operative sono corretti? |  |  |
| HR24 | Cap. 12, quadro contratti | Il capitolo tratta il delta ICT e rinvia la disciplina generale al VOL-01; soglie, termini, penali e clausole mobili non sono fissati a memoria. | fonti consolidate sul d.lgs. 36/2023, correttivo, ANAC, MIT, AgID e Consip | Quadro vigente, competenze e formulazioni sono corretti al cut-off? |  |  |
| HR25 | Cap. 12, lock-in ed exit | Lock-in tecnico/contrattuale/economico/organizzativo, portabilità, reversibilità ed exit strategy sono distinti. | fonte procurement ICT consolidata | Caso cloud, checklist e criteri di accettazione sono corretti? |  |  |
| HR26 | Cap. 13, simulazione mista | Quiz, risposte brevi, elaborato, orale e casi applicano teoria dei capp. 02-12 e includono soluzioni/rubriche. | capp. 02-12; fonti Metodo BANDO sulle prove | Quesiti, chiavi, soluzioni, rubriche e livello di difficoltà sono corretti? |  |  |
| HR27 | Premessa, indice e matrice | La promessa è riusabile, aggiornabile e modulare; la matrice registra 14 nuclei completi e un rinvio puntuale al VOL-01. | matrice M-TR01; logica v4 | Promessa, confini, rinvii e giudizio di completezza sono approvabili? |  |  |

## Conflitti e incertezze emersi

- M-TR02 è ancora incompleto: ogni collegamento è instradamento di catalogo, non copertura sostitutiva.
- Fonti e capitoli evitano soglie e termini mobili non necessari; dove la mobilità è rilevante, la review deve confermare il cut-off.
- I gate individuali e trasversali non sostituiscono la validazione professionale di DBA, network/system engineer, software architect, esperto Cloud PA/ACN, cyber specialist, DPO, data/AI specialist e giurista dei contratti.
- Il PDF impaginato non rientra in questo sign-off e sarà verificato nel preflight.

## Esito complessivo e firma

- Esito complessivo: ______________________________________________
- Correzioni obbligatorie residue: _________________________________
- Limiti confermati dal revisore: __________________________________
- Nome e ruolo: Alberto Brando — responsabile normativo/editoriale
- Data: __________________
- Firma o approvazione esplicita tracciabile: ______________________
