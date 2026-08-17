---
id: m-tr01-capitolo-12-piano-completamento
type: chapter_plan
title: "Piano di completamento — Capitolo 12 Procurement ICT e gestione dei fornitori"
status: ready
domain: "concorsi pubblici italiani"
topics: ["procurement ICT", "capitolato tecnico", "SLA", "vendor management", "exit strategy"]
entities: ["ANAC", "AgID", "Consip", "RUP", "Direttore dell'esecuzione"]
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/codice-contratti-pubblici-d-lgs-36-2023-e-correttivo-209-2024", "sources/ciclo-contratti-pubblici-rup-stazione-appaltante-operatore-economico", "sources/digitalizzazione-contratti-pubblici-anac-bdncp-fvoe-pcp", "sources/mepa-consip-acquisti-in-rete-strumenti-acquisto-negoziazione"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "vol-08-ict-digitale-cybersecurity-dati", "il-metodo-bando", "m-tr02-appalti-pnrr-fondi-ue"]
confidence: 0.82
updated_at: 2026-07-30
created_at: 2026-07-30
review_required: true
canonical: false
tags: ["planning", "m-tr01", "chapter-12", "procurement-ict", "sla", "fornitori"]
chapter_ref: "chapters/12-procurement-ict-gestione-fornitori.md"
---

# Piano di completamento — Capitolo 12

## 1. Funzione del capitolo

Il capitolo deve insegnare al candidato ICT a tradurre un fabbisogno pubblico in una prestazione tecnica acquistabile, verificabile e governabile durante l'esecuzione. Non è un secondo capitolo generale sui contratti pubblici: parte dal ciclo contrattuale già trattato nel VOL-01 e sviluppa il delta specialistico di servizi cloud, software, dati, cybersecurity, assistenza e manutenzione.

Il filo conduttore è la continuità tra bisogno, requisiti, criteri di accettazione, livelli di servizio, controlli, evidenze, gestione delle modifiche e uscita dal contratto. Un capitolato efficace non accumula tecnologie o formule generiche; collega ogni requisito a un rischio, a una misura osservabile, a un responsabile e a una verifica.

Output centrali:

- checklist del capitolato tecnico ICT;
- matrice requisito-criterio di accettazione-evidenza;
- scheda SLA/SLI con soglie e regole di misurazione;
- registro dei rischi del fornitore e delle dipendenze;
- piano di monitoraggio dell'esecuzione;
- scheda di reversibilità, portabilità ed exit strategy.

## 2. Stato iniziale

Il capitolo contiene frontmatter, H1 e specifica della struttura madre. La matrice assegna «requisiti, SLA, fornitori», prevede checklist del capitolato e caso fornitore, ma classifica la copertura `parziale`.

Il wiki dispone di fonti consolidate sul ciclo dei contratti, sul RUP, sull'esecuzione, su Consip/MEPA e sulla digitalizzazione ANAC. Mancano tuttavia una source note specialistica unitaria sul procurement ICT e una topic page dedicata che colleghino requisiti tecnici, livelli di servizio, sicurezza, dati, continuità, audit, lock-in e uscita.

## 3. Nuclei assegnati

### 3.1 Dal fabbisogno alla strategia di acquisizione

- bisogno pubblico, risultato atteso e baseline;
- perimetro del servizio e confini di responsabilità;
- make, buy e reuse come valutazione organizzativa, non automatismo;
- vincoli, dipendenze, mercato e competenze interne;
- costo totale di possesso e di uscita, senza formule finanziarie avanzate;
- lotti, modularità e interoperabilità come presidi contro dipendenze eccessive;
- raccordo con programmazione e progettazione del contratto nel VOL-01.

### 3.2 Requisiti e capitolato tecnico

- requisiti funzionali e non funzionali;
- requisiti obbligatori, preferenziali e condizioni di esecuzione;
- formulazioni misurabili e verificabili;
- criteri di accettazione e tracciabilità requisito-test-evidenza;
- architettura, integrazioni, ambienti, dati, migrazione e documentazione;
- prestazioni, capacità, disponibilità, accessibilità, interoperabilità, manutenibilità e portabilità;
- specifiche tecniche neutrali e gestione motivata di equivalenze, standard e compatibilità;
- distinzione tra requisito, criterio di valutazione dell'offerta, obbligo contrattuale e SLA.

### 3.3 SLA, SLI e misurazione

- service level agreement come impegno contrattuale;
- service level indicator come misura osservata;
- obiettivo o soglia di servizio, con uso prudente della terminologia SLO;
- disponibilità, tempi di risposta, presa in carico, ripristino e risoluzione;
- finestra di servizio, periodo di misura, esclusioni e fonte del dato;
- severità e priorità degli incidenti;
- soglie, tolleranze, escalation, service credit o penali secondo il contratto;
- differenza tra SLA e KPI di governo;
- rischio di metriche facili da rispettare ma scollegate dall'esperienza del servizio.

### 3.4 Ruoli e governo dell'esecuzione

- stazione appaltante, RUP, direttore dell'esecuzione, referente tecnico e fornitore;
- owner del servizio, sicurezza, DPO e utenti interni per competenza;
- RACI o matrice equivalente come strumento organizzativo, non fonte normativa;
- avvio, presa in carico, riunioni operative e reporting;
- verifica di conformità, accettazione dei deliverable e gestione delle non conformità;
- registro decisioni, issue, rischi, dipendenze e azioni;
- escalation operativa, contrattuale e direzionale;
- distinzione tra governo del fornitore e trasferimento di responsabilità.

### 3.5 Sicurezza, dati e compliance nel contratto

- requisiti di sicurezza proporzionati a servizio, dati e rischio;
- IAM, segregazione, logging, vulnerabilità, patching, incidenti e continuità;
- localizzazione, accesso, restituzione e cancellazione dei dati;
- subfornitori e catena di fornitura;
- audit, evidenze, notifiche e cooperazione negli incidenti;
- privacy, ruoli e istruzioni da definire con DPO e giurista;
- software supply chain, componenti e SBOM quando pertinenti;
- raccordi ai capitoli 7-11 senza ripeterne la teoria.

### 3.6 Modifiche, rilascio e continuità

- change request e distinzione tra chiarimento, correzione, evoluzione e modifica contrattuale;
- versionamento di requisiti, configurazioni, deliverable e approvazioni;
- ambienti, test, cutover, rollback e criteri di go/no-go;
- capacità, backup, disaster recovery, RPO/RTO e continuità come obblighi verificabili;
- obsolescenza, end of support e dipendenze critiche;
- gestione delle modifiche del fornitore a piattaforme, prezzi, componenti o condizioni.

### 3.7 Lock-in, portabilità e uscita

- lock-in tecnico, contrattuale, economico, organizzativo e sui dati;
- formati, API, documentazione, codice, configurazioni e competenze;
- proprietà, licenze e diritti d'uso da verificare sul contratto;
- reversibilità e portabilità come attività pianificate fin dall'ingresso;
- exit plan con trigger, tempi, ruoli, dati, supporto alla transizione e prova di restituzione/cancellazione;
- continuità durante cambio fornitore, internalizzazione o dismissione;
- test periodico dell'uscita e aggiornamento dell'inventario delle dipendenze.

### 3.8 Strumenti di acquisto e ciclo digitale

- distinzione essenziale tra Consip, Acquisti in Rete e MEPA;
- convenzioni, accordi quadro, MEPA e SDAPA al solo livello necessario per orientare il candidato;
- piattaforme di approvvigionamento digitale, BDNCP, PCP e FVOE;
- tracciabilità e dati del ciclo contrattuale;
- rinvio al VOL-01 e al VOL-09 per procedure, soglie, affidamenti e disciplina avanzata.

## 4. Nuclei già completi

Nessun nucleo specialistico è completo nel file del capitolo. Sono disponibili prerequisiti consolidati:

- VOL-01, «Contratti pubblici essenziali»: principi, soggetti, ciclo, procedure, affidamento, stipula, esecuzione e controlli;
- capitolo 6: requisiti verificabili, test, tracciabilità, API e gestione delle modifiche;
- capitolo 7: cloud, responsabilità condivisa, migrazione, osservabilità, resilienza, RPO/RTO ed exit strategy;
- capitoli 8-9: risk assessment, controlli, supply chain, IAM, logging e incident response;
- capitolo 10: data governance, qualità, interoperabilità e responsabilizzazione;
- capitolo 11: sistemi AI acquistati, responsabilità del fornitore, versioni, evidenze e monitoraggio.

Questi contenuti vanno richiamati con destinazioni precise e applicati al contratto, non duplicati.

## 5. Nuclei da sviluppare

Tutti i nuclei del § 3 devono essere sviluppati. Priorità:

1. trasformare il fabbisogno in requisiti e criteri verificabili;
2. distinguere SLA, indicatori, soglie, KPI ed evidenze;
3. collegare governo tecnico e governo contrattuale dell'esecuzione;
4. integrare sicurezza, dati e continuità nelle clausole operative;
5. rendere verificabili change, accettazione, non conformità ed escalation;
6. trattare lock-in ed exit strategy come ciclo, non come clausola finale;
7. mantenere preciso il rinvio alla disciplina generale e avanzata degli appalti.

## 6. Sezioni da conservare

- frontmatter e identificativo `chapter-m-tr01-12`;
- H1 «Procurement ICT e gestione dei fornitori»;
- `outline_section: 12`;
- promessa della struttura madre su requisiti, capitolato tecnico, SLA, sicurezza e controllo del fornitore;
- rinvio agli appalti avanzati del VOL-09;
- `book_refs` verso M-TR01 e M-TR02, da mantenere e precisare.

## 7. Duplicazioni da evitare

- principi, soggetti, soglie, procedure, affidamento, esclusione, aggiudicazione e contenzioso del VOL-01/VOL-09;
- teoria generale dei requisiti, test e API del capitolo 6;
- modelli cloud, migrazione, DevOps, backup e continuità del capitolo 7;
- risk assessment, controlli e software supply chain del capitolo 8;
- IAM, crittografia, logging e incident response del capitolo 9;
- data governance, privacy e interoperabilità del capitolo 10;
- AI Act, metriche e model governance del capitolo 11;
- tutorial del portale MEPA o cataloghi di clausole non verificati;
- soglie, termini, percentuali e obblighi puntuali non ricontrollati sul testo vigente.

## 8. Caso guidato

### Servizio cloud comunale con gestione applicativa

Un comune deve acquisire hosting cloud, migrazione, manutenzione e assistenza per un servizio al cittadino. Il caso deve sviluppare:

1. bisogno, perimetro e baseline;
2. dati, utenti, integrazioni e dipendenze;
3. requisiti funzionali e non funzionali;
4. criteri di accettazione della migrazione;
5. disponibilità, presa in carico e ripristino per severità;
6. fonte delle misure e regole di calcolo;
7. sicurezza, accessi, log, vulnerabilità e incidenti;
8. subfornitori e responsabilità condivise;
9. reporting, riunioni, escalation e non conformità;
10. change request e rilascio;
11. portabilità, restituzione dei dati ed exit test;
12. chiusura o transizione verso un nuovo fornitore.

Il caso non deve scegliere una procedura di affidamento né fissare penali standard: questi elementi dipendono da importo, oggetto, atti di gara e disciplina vigente.

## 9. Output compilabili

### Matrice requisito-accettazione-evidenza

| ID | Requisito | Criterio di accettazione | Evidenza | Responsabile | Esito |
| --- | --- | --- | --- | --- | --- |
| R-01 | da compilare | misura o test | report/log/verbale | ruolo | aperto |

### Scheda SLA

Servizio, indicatore, definizione, soglia, finestra, periodo di misura, fonte dati, esclusioni, severità, escalation, conseguenza contrattuale e responsabile della verifica.

### Registro fornitore e dipendenze

Servizio, owner, fornitore, subfornitore, dati, integrazioni, componente critico, rischio, controllo, evidenza, scadenza e piano di uscita.

### Exit plan

Trigger, preavviso, inventario, formati, esportazione, documentazione, conoscenze, supporto alla transizione, cancellazione, verifiche, continuità e approvazione finale.

## 10. Domande ed esercizi

### Domanda da commissario

«Come imposteresti e controlleresti un contratto per un servizio cloud destinato ai cittadini?»

La risposta deve coprire bisogno, requisiti, accettazione, SLA, sicurezza, dati, ruoli, evidenze, modifiche, continuità, rischio fornitore ed exit strategy, con rinvio alla procedura contrattuale applicabile.

### Domande-trappola

- un requisito tecnico dettagliato è automaticamente verificabile?
- disponibilità del 99,9% basta senza finestra e fonte di misura?
- SLA e KPI sono sinonimi?
- la stipula conclude il lavoro del RUP e dell'ente?
- acquistare cloud trasferisce sicurezza e compliance al provider?
- una penale sostituisce il ripristino del servizio?
- il backup coincide con continuità e disaster recovery?
- l'exit strategy si prepara soltanto alla scadenza?
- MEPA è sinonimo di Consip?

### Esercizi

1. trasformare tre bisogni vaghi in requisiti verificabili;
2. individuare gli elementi mancanti in uno SLA;
3. classificare requisiti funzionali, non funzionali e condizioni di esecuzione;
4. costruire una matrice requisito-test-evidenza;
5. assegnare ruoli in un incidente del fornitore;
6. riconoscere cinque forme di lock-in;
7. compilare un exit plan essenziale;
8. rispondere oralmente al caso cloud con rubrica.

Ogni esercizio deve avere soluzione ragionata o criteri verificabili.

## 11. Fonti consolidate disponibili

- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]]: perimetro editoriale;
- [[sources/codice-contratti-pubblici-d-lgs-36-2023-e-correttivo-209-2024]]: principi e quadro del Codice;
- [[sources/ciclo-contratti-pubblici-rup-stazione-appaltante-operatore-economico]]: ciclo, RUP, DEC, esecuzione e verifica;
- [[sources/digitalizzazione-contratti-pubblici-anac-bdncp-fvoe-pcp]]: ciclo digitale e piattaforme;
- [[sources/mepa-consip-acquisti-in-rete-strumenti-acquisto-negoziazione]]: strumenti di acquisto e negoziazione;
- [[sources/trasparenza-anticorruzione-controlli-tracciabilita-contratti-pubblici]]: tracciabilità e controlli;
- [[sources/ingegneria-software-api-interoperabilita-fonti-tecniche]]: requisiti, accettazione e API;
- [[sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie]]: cloud, portabilità, resilienza e continuità;
- [[sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie]]: rischio fornitore e supply chain;
- [[sources/iam-crittografia-logging-incident-response-fonti-primarie]]: accessi, log e incidenti;
- [[sources/data-governance-open-data-interoperabilita-fonti-primarie]]: dati e interoperabilità.

## 12. Fonti da consolidare prima dello step 09

Creare una source note specialistica «procurement ICT, SLA e vendor management» che consolidi:

- testo vigente del D.Lgs. 36/2023 e allegati pertinenti a progettazione, esecuzione, DEC e verifica di conformità;
- indicazioni ufficiali ANAC, MIT, AgID e Consip applicabili agli acquisti ICT;
- fonti ufficiali su cloud PA, qualificazione e responsabilità applicabili, senza duplicare il capitolo 7;
- standard o guide primarie per SLA, service management, portabilità, reversibilità e continuità, distinguendo norme, standard volontari e buone pratiche;
- fonti istituzionali per sicurezza, supply chain e incidenti contrattuali;
- disciplina vigente su protezione dati, subfornitori e ruoli, da trattare con rinvio e review DPO;
- eventuali criteri ambientali o accessibilità soltanto se sostenuti da fonti ufficiali pertinenti al caso.

La nota deve registrare versione, data di consultazione, autorità, campo di applicazione, claim ammessi e limiti. Non introdurre clausole modello o soglie standard prive di fonte.

## 13. Topic, entity e quiz

Creare o aggiornare:

- `topics/procurement-ict-sla-gestione-fornitori.md`;
- collegamenti a [[topics/contratti-pubblici]] senza duplicarne il contenuto;
- entity esistenti per Codice dei contratti, ANAC, RUP, Consip e AgID;
- quiz specialistici su requisiti, SLA, ruoli, sicurezza, lock-in ed exit strategy.

## 14. Review umane richieste

- procurement specialist e giurista dei contratti pubblici;
- RUP e direttore dell'esecuzione con esperienza in servizi ICT;
- software/cloud architect per requisiti, integrazioni e portabilità;
- service manager per SLA, reporting, escalation e continuità;
- security architect e supply-chain specialist;
- DPO per dati, subfornitori, ruoli e cancellazione;
- specialista accessibilità e interoperabilità quando il caso lo richiede;
- revisore editoriale e impaginatore KDP.

## 15. Struttura H1/H2/H3

# Procurement ICT e gestione dei fornitori

## Obiettivo e confini

## Mappa BANDO dell'acquisto ICT

## Dal fabbisogno alla strategia di acquisizione
### Risultato, perimetro e baseline
### Make, buy, reuse e dipendenze
### Costo totale e rischio di uscita

## Requisiti e capitolato tecnico
### Funzionali e non funzionali
### Requisito, criterio, obbligo e SLA
### Accettazione, test ed evidenze

## SLA e misurazione del servizio
### Indicatori, soglie e fonti del dato
### Disponibilità, tempi e severità
### KPI, escalation e conseguenze

## Ruoli e governo dell'esecuzione
### RUP, DEC, referente tecnico e fornitore
### Avvio, reporting e verifiche
### Non conformità ed escalation

## Sicurezza, dati e supply chain
### Accessi, log, vulnerabilità e incidenti
### Dati, privacy e subfornitori
### Audit, evidenze e cooperazione

## Modifiche, rilasci e continuità
### Change request e versioni
### Test, cutover e rollback
### Backup, RPO/RTO e obsolescenza

## Lock-in, portabilità ed exit strategy
### Forme di dipendenza
### Reversibilità e transizione
### Exit test e chiusura

## Strumenti di acquisto e ciclo digitale
### Consip, Acquisti in Rete e MEPA
### BDNCP, PCP e FVOE
### Rinvio a VOL-01 e VOL-09

## Caso guidato: servizio cloud comunale

## Laboratorio: capitolato, SLA e registro fornitore

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
| fabbisogno e strategia | 400-550 |
| requisiti e capitolato | 650-850 |
| SLA e misurazione | 650-850 |
| ruoli e governo dell'esecuzione | 500-650 |
| sicurezza, dati e supply chain | 550-750 |
| modifiche, rilasci e continuità | 450-600 |
| lock-in, portabilità ed exit | 500-650 |
| strumenti e ciclo digitale | 300-450 |
| caso e laboratorio | 650-850 |
| orale, trappole, esercizi e checklist | 500-650 |
| riferimenti e note di review | 150-250 |
| **Totale** | **5.600-7.500** |

Le tabelle devono restare leggibili nel paperback KDP 6,69 × 9,61 in. La scheda SLA e la matrice requisito-evidenza vanno divise in due strumenti se la resa richiede corpo inferiore allo standard.

## 17. Criteri di accettazione dello step 09

- la teoria specialistica precede casi e checklist;
- il capitolo distingue requisito, criterio di accettazione, obbligo, SLA e KPI;
- ogni SLA contiene metrica, soglia, finestra, fonte, esclusioni e responsabilità;
- ruoli tecnici e contrattuali sono distinti senza attribuzioni normative inventate;
- sicurezza, dati, continuità e supply chain diventano requisiti ed evidenze;
- change, non conformità, escalation e accettazione sono governati;
- lock-in ed exit strategy coprono dati, tecnologia, contratto e organizzazione;
- il caso collega bisogno, requisito, misura, controllo e uscita;
- esercizi e strumenti hanno soluzioni o criteri verificabili;
- rinvii a VOL-01, VOL-09 e capitoli 6-11 sono precisi;
- soglie, termini e obblighi derivano da fonti vigenti consolidate;
- frontmatter, topic e source refs sono veritieri.

## 18. Esito del piano

Il piano è pronto. Lo step 09 può sviluppare la parte tecnica solo dopo aver creato la source note specialistica sul procurement ICT e aver verificato il quadro contrattuale vigente. La disciplina generale resta nel VOL-01; procedure e appalti avanzati restano nel VOL-09. Il capitolo 12 deve concentrarsi sulla progettazione tecnica della prestazione e sul governo verificabile del fornitore lungo tutto il ciclo di vita.

## Addendum retrofit Format 2 — 11 agosto 2026

Il retrofit conserva la lezione e gli strumenti già validi, ma li ricompone in sette nuclei con identificativi stabili: `N-TR01-12-01` fabbisogno e strategia; `02` requisiti e capitolato; `03` SLA, SLI e KPI; `04` governo dell'esecuzione; `05` sicurezza, dati e filiera; `06` modifiche, rilasci e continuità; `07` lock-in, portabilità, reversibilità ed uscita. Ogni nucleo sviluppa teoria, distinzione, conseguenza, applicazione e controllo; nessuno rinvia genericamente a VOL-01 o VOL-09.

Il blocco `▣ Verifica` segue il settimo nucleo e raccoglie sei quiz commentati, il caso del servizio cloud comunale e strumenti compilabili: matrice requisito-accettazione-evidenza, scheda SLA, registro delle dipendenze e traccia di exit plan. Il budget operativo è di almeno 600 parole per nucleo, sette nuclei, sei quiz e un caso ragionato. Il rinvio a VOL-01 resta circoscritto alla disciplina comune dei contratti; VOL-09/M-TR02 è soltanto un approfondimento avanzato, non una condizione per comprendere il governo tecnico del fornitore.

La fonte specialistica unitaria e la topic page previste dal piano sono presenti. Restano debiti mobili da verificare negli step 13-18: testo vigente del Codice e allegati, indicazioni ANAC/AgID/Consip, disciplina privacy del caso, subfornitura, qualificazione cloud e dati operativi. Il testo non fisserà soglie, penali, termini o clausole modello.
