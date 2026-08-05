---
id: m-tr01-capitolo-09-piano-completamento
type: chapter_plan
title: "Piano di completamento — Capitolo 09 IAM, crittografia, logging e incident response"
status: ready
domain: "concorsi pubblici italiani"
topics: ["iam", "crittografia", "logging", "incident response", "nis2"]
entities: ["Agenzia per la cybersicurezza nazionale", "CSIRT Italia", "NIST"]
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/sicurezza-informatica-privacy-nis2-pa", "sources/pa-digitale-cad-identita-documenti-servizi-dati"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "vol-08-ict-digitale-cybersecurity-dati", "il-metodo-bando"]
confidence: 0.82
updated_at: 2026-07-30
created_at: 2026-07-30
review_required: true
canonical: false
tags: ["planning", "m-tr01", "chapter-09", "iam", "incident-response"]
chapter_ref: "chapters/09-iam-crittografia-logging-incident-response.md"
---

# Piano di completamento — Capitolo 09

File destinatario: `chapters/09-iam-crittografia-logging-incident-response.md`.

Il capitolo deve portare il lettore dall’identità digitale all’azione durante un incidente. La progressione prevista è: identità e account, autenticazione, autorizzazione e privilegi, protezione crittografica, logging e rilevazione, qualificazione dell’evento, risposta, recupero e apprendimento. L’output centrale è un playbook con timeline, ruoli, decisioni ed evidenze.

## 1. Funzione del capitolo nel volume

Il capitolo 8 insegna a descrivere scenari, valutare rischio e controlli e gestire vulnerabilità. Il capitolo 9 applica quei concetti a quattro capacità operative collegate:

1. stabilire chi o che cosa accede a una risorsa;
2. limitare ciò che l’identità può fare;
3. proteggere dati e chiavi;
4. rilevare, contenere e gestire un incidente lasciando evidenze utilizzabili.

Il capitolo 10 passa alla governance del dato, ai metadati, alla qualità, agli open data e all’interoperabilità. Il capitolo 9 non deve anticiparne il perimetro, salvo spiegare che classificazione e responsabilità del dato condizionano autorizzazioni, cifratura, log e risposta.

## 2. Stato iniziale

Il file contiene frontmatter, titolo e specifica della struttura madre. Non esiste ancora testo reader-facing. La riga «IAM e incident response» della matrice M-TR01 è `parziale` e indica come nuclei identità, crittografia, log e risposta, con output `playbook`, `timeline incidente` e `caso`.

### Nuclei già completi

Nessun nucleo specialistico è completo nel capitolo 9.

Sono disponibili soltanto prerequisiti esterni:

- VOL-01, capitolo 10, § 6: autenticazione, autorizzazione, password, MFA, crittografia, certificati, sicurezza PA e quadro NIS2 introduttivo;
- capitolo 7 di M-TR01: continuità, backup, RPO/RTO, disaster recovery, osservabilità tecnica;
- capitolo 8 di M-TR01: CIA, asset, rischio, controlli, vulnerabilità, NIST CSF 2.0 e trattamento;
- source note generale su sicurezza, privacy e NIS2.

Questi contenuti sono prerequisiti o raccordi. Non sostituiscono IAM specialistico, ciclo delle chiavi, log di sicurezza e incident response.

## 3. Nuclei assegnati

### 3.1 IAM e ciclo di vita delle identità

- identità umane, tecniche, di servizio e workload;
- account, credenziale, autenticatore, sessione e attributo;
- identity proofing, provisioning, modifica, sospensione, revoca e deprovisioning;
- joiner, mover, leaver;
- account nominativi, condivisi, privilegiati e di emergenza;
- separazione dei compiti e riesame periodico degli accessi;
- federazione e single sign-on, senza trasformare il capitolo in un manuale di prodotto.

### 3.2 Autenticazione, autorizzazione e privilegi

- distinzione fra identificazione, autenticazione, autorizzazione e accounting;
- fattori di autenticazione e MFA;
- rischio di phishing, replay, credential stuffing e session hijacking come esempi, senza duplicare il capitolo 8;
- modelli RBAC e ABAC, con cenno motivato alle ACL;
- minimo privilegio, need to know, just-in-time e just-enough administration;
- privileged access management e controllo degli account amministrativi;
- autorizzazione negata per default e verifica lato servizio.

### 3.3 Crittografia e gestione delle chiavi

- obiettivi: riservatezza, integrità, autenticità e, dove applicabile, non ripudio;
- cifratura simmetrica e asimmetrica;
- hash, MAC, firma digitale e certificato: funzioni diverse;
- dati in transito, a riposo e in uso, con cautela sul terzo caso;
- ciclo della chiave: generazione, distribuzione, conservazione, uso, rotazione, revoca, archiviazione e distruzione;
- chiavi, secret e certificati: inventario, responsabilità, scadenza e compromissione;
- HSM e servizi di gestione delle chiavi come categorie, non come prodotti obbligatori;
- distinzione fra cifratura e pseudonimizzazione; rinvio al capitolo 10 e alle fonti privacy per la governance del dato.

### 3.4 Logging, monitoraggio e rilevazione

- evento, log, audit trail, alert, incidente e indicatore;
- sorgenti: identità, sistemi, reti, applicazioni, cloud e dispositivi;
- campi minimi: timestamp, soggetto, azione, risorsa, esito, origine e correlazione;
- sincronizzazione temporale, integrità, accesso, conservazione e minimizzazione;
- centralizzazione, correlazione e casi d’uso;
- SIEM come capacità di raccolta, normalizzazione, correlazione e analisi, non come sinonimo di sicurezza;
- falsi positivi, falsi negativi, soglie, baseline e triage;
- rapporto tra logging, privacy e accesso autorizzato ai log;
- evidenze e catena di custodia solo al livello trasferibile supportato dalle fonti.

### 3.5 Incident response

- distinzione fra evento, alert, incidente cyber, data breach e crisi;
- preparazione, rilevazione, analisi, contenimento, eradicazione, recupero e miglioramento, dichiarando che i modelli possono variare;
- classificazione e severità basate su servizio, impatto, diffusione, dati e urgenza;
- ruoli: incident manager, team tecnico, responsabile del servizio, sicurezza, comunicazione, legale/privacy, vertice e soggetti esterni;
- escalation tecnica, organizzativa, privacy e istituzionale;
- comunicazione interna ed esterna, registro decisionale e aggiornamenti di situazione;
- acquisizione e preservazione delle evidenze senza improvvisare attività forensi;
- contenimento a breve e lungo termine;
- recupero controllato, monitoraggio rafforzato, chiusura e lesson learned;
- raccordo con business continuity e disaster recovery del capitolo 7.

### 3.6 Quadro PA, NIS2 e notifiche

- ruolo di ACN e CSIRT Italia nel perimetro pertinente;
- governance e responsabilità organizzative;
- obblighi e procedure da presentare soltanto dopo consolidamento delle fonti ufficiali vigenti;
- distinzione fra notifica di incidente cyber e notifica di violazione dei dati personali;
- divieto di inventare termini, soglie, moduli, canali o platee;
- rinvio alla review umana ACN/NIS2 e privacy prima del text freeze.

## 4. Nuclei da sviluppare e criteri di completezza

| Nucleo | Definizione e funzione | Elementi e distinzioni | Conseguenze e applicazione | Verifica richiesta |
| --- | --- | --- | --- | --- |
| IAM | identità, account, credenziale, autenticatore e ciclo di vita | umano/tecnico; authn/authz; provisioning/revoca | accessi coerenti con ruolo e cessazione tempestiva | caso joiner-mover-leaver e matrice accessi |
| Privilegi | minimo privilegio e separazione dei compiti | RBAC/ABAC; standard/privilegiato/emergenza | riduzione dell’abuso e tracciabilità | esercizio di autorizzazione e domanda-trappola |
| Crittografia | cifratura, hash, MAC, firma e certificati | simmetrica/asimmetrica; dato in transito/a riposo | scelta della proprietà da proteggere e gestione del compromesso | tabella funzione-meccanismo e caso chiave compromessa |
| Key management | governo del materiale crittografico | generazione, uso, rotazione, revoca, distruzione | perdita o compromissione della chiave può annullare la protezione | checklist del ciclo di vita |
| Logging | registrazione verificabile degli eventi | log/audit/alert; sorgenti, campi, tempo, integrità | rilevazione, ricostruzione e accountability | scheda evento-log-evidenza |
| Rilevazione e triage | trasformazione di segnali in priorità | indicatore, regola, correlazione, falso positivo/negativo | escalation proporzionata e riduzione del rumore | esercizio di classificazione alert |
| Incident response | governo coordinato di un incidente | evento/incidente/data breach/crisi; ruoli e fasi | contenimento, recupero, comunicazione e apprendimento | playbook, timeline e caso guidato |
| PA/NIS2/privacy | collocazione istituzionale e obblighi | ACN/CSIRT, notifica cyber/data breach | responsabilità, termini e canali solo se verificati | review ufficiale e domanda orale |

Nessun caso, quiz o playbook può sostituire la teoria indicata nella tabella.

## 5. Sezioni da conservare

- frontmatter e identificativi canonici;
- titolo H1 «IAM, crittografia, logging e incident response»;
- collocazione `outline_section: 9`;
- promessa della specifica struttura madre: identità, autorizzazione, privilegi, cifratura, chiavi, log, rilevazione e risposta;
- output `playbook incidente`;
- review ACN e NIS2.

Al momento della scrittura, la sezione «Specifica struttura madre» va trasformata in testo editoriale effettivo oppure mantenuta solo come nota gestita, secondo il formato adottato nei capitoli 2-8. Non deve restare come unico corpo del capitolo.

## 6. Duplicazioni da evitare

- password, phishing, malware, antivirus, firewall e backup di base già spiegati nel VOL-01, capitolo 10, § 6;
- triade CIA, asset, rischio, tassonomie generali dei controlli, vulnerabilità, CVE/CWE/CVSS, secure coding e supply chain del capitolo 8;
- backup, RPO/RTO, disaster recovery e business continuity del capitolo 7;
- firma digitale e documento informatico come disciplina amministrativa generale, già nel VOL-01;
- data governance, qualità, cataloghi, open data e interoperabilità del capitolo 10;
- procurement, SLA e obblighi contrattuali del capitolo 12;
- dettagli di prodotto su directory, PAM, SIEM, HSM, cloud KMS o strumenti forensi;
- procedure operative ACN, termini e soglie non ancora consolidati in source note ufficiali.

## 7. Casi, domande ed esercizi necessari

### Caso guidato principale

Compromissione di un account privilegiato usato per amministrare un servizio pubblico. Il caso deve mostrare:

1. segnale iniziale e log disponibili;
2. identità, account, privilegi e sessione coinvolti;
3. triage e classificazione;
4. contenimento dell’account e delle credenziali;
5. verifica di accessi, chiavi, token e azioni eseguite;
6. escalation tecnica, privacy e istituzionale secondo perimetro verificato;
7. recupero e monitoraggio rafforzato;
8. revisione di privilegi, regole e playbook.

### Output compilabile

- matrice ruolo-risorsa-permesso-evidenza;
- scheda del ciclo di vita di account e privilegi;
- checklist del ciclo di vita delle chiavi;
- matrice sorgente-evento-campo-alert-responsabile;
- playbook incidente con trigger, severità, ruoli, azioni, comunicazioni, evidenze, criteri di recupero e chiusura;
- timeline dell’incidente con fatto, fonte, decisione, responsabile e timestamp.

### Domanda da commissario

«Come imposteresti la risposta alla compromissione di un account privilegiato in un ente pubblico?»

La risposta modello deve partire dalla qualificazione del segnale, preservare evidenze, contenere l’account, valutare impatto e propagazione, attivare ruoli ed escalation, recuperare in modo controllato e chiudere con lesson learned.

### Domande-trappola

- autenticazione riuscita significa autorizzazione corretta?
- la cifratura elimina la necessità del controllo degli accessi?
- un log presente è automaticamente completo, integro e utilizzabile?
- ogni alert è un incidente?
- isolamento immediato è sempre la prima azione corretta, anche se distrugge evidenze o interrompe un servizio essenziale?
- notifica NIS2 e data breach GDPR coincidono?

### Esercizi e quiz

1. classificare esempi come identificazione, autenticazione, autorizzazione o accounting;
2. scegliere RBAC o ABAC motivando il criterio;
3. distinguere cifratura, hash, MAC e firma in quattro scenari;
4. ordinare le fasi del ciclo di vita di una chiave;
5. progettare i campi minimi di un log di accesso privilegiato;
6. distinguere evento, alert, incidente e data breach;
7. costruire una timeline da evidenze sparse;
8. completare un playbook per account compromesso;
9. quiz con soluzione ragionata su MFA, minimo privilegio, log, SIEM e incident response.

## 8. Fonti consolidate da usare

- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]] — perimetro editoriale e campione di materie;
- [[sources/sicurezza-informatica-privacy-nis2-pa]] — sicurezza PA, MFA, log, incidenti, NIS2 e raccordo privacy;
- [[sources/pa-digitale-cad-identita-documenti-servizi-dati]] — identità e servizi digitali della PA;
- [[sources/campione-bandi-ict-pa-vol-08-2024-2026]] — profondità e output richiesti dai bandi;
- [[sources/legge-28-giugno-2024-n-90-cybersicurezza-nazionale-e-reati-informatici]] — quadro nazionale pertinente, da usare nei limiti della source note;
- [[topics/sicurezza-informatica]];
- [[topics/ict-digitale-cybersecurity-dati-concorsi-pa]];
- [[entities/agenzia-cybersicurezza-nazionale]].

## 9. Fonti primarie da consolidare prima dello step 09

Creare una source note specialistica unica o un piccolo gruppo di note collegate. Non scrivere il capitolo definitivo basandosi direttamente sulle pagine web.

- NIST SP 800-63 rev. 4, Digital Identity Guidelines, con parti A/B/C per identity proofing, autenticazione e federazione. La rev. 4 ha sostituito la rev. 3 nel 2025.
- NIST SP 800-57 Part 1 rev. 5 e Part 2 rev. 1 per ciclo di vita, protezione, ruoli e policy di key management; verificare al text freeze eventuale esito della revisione successiva.
- NIST SP 800-92, Guide to Computer Security Log Management, tenendo conto che SP 800-92 rev. 1 risulta draft e non va presentata come finale finché tale stato non cambia.
- NIST SP 800-61 rev. 3, finale da aprile 2025, per integrare incident response e CSF 2.0; non riutilizzare meccanicamente il ciclo della rev. 2 come se fosse ancora la struttura corrente.
- NIST CSF 2.0 per il raccordo Govern/Identify/Protect/Detect/Respond/Recover.
- Fonti ufficiali ACN e CSIRT Italia vigenti per ruoli, registrazione, segnalazione/notifica, canali, soglie e termini NIS2.
- D.Lgs. 4 settembre 2024, n. 138 e atti ACN applicabili, verificati nel testo vigente.
- GDPR, Codice privacy e fonti del Garante per distinguere incidente cyber e violazione dei dati personali.

Ogni fonte deve indicare versione, data di consultazione, autorità, limiti di trasferibilità al contesto italiano e claim sostenuti.

## 10. Topic, entity e quiz

### Topic

Il topic [[topics/sicurezza-informatica]] offre il raccordo generale. Prima della scrittura valutare una pagina specialistica canonica `topics/iam-crittografia-logging-incident-response.md` che colleghi fonti, capitoli 8-10, ACN/CSIRT e output concorsuali.

### Entity

Aggiornare [[entities/agenzia-cybersicurezza-nazionale]] soltanto dopo consolidamento delle fonti ufficiali. Separare chiaramente ACN, CSIRT Italia, soggetti NIS2, titolare/responsabile privacy e team interno di risposta.

### Quiz

Non risultano quiz specialistici canonici dedicati al capitolo. Lo step 09 dovrà integrare quiz ed esercizi nel capitolo; l’eventuale banca quiz separata dovrà riusare gli stessi termini e conservare la tracciabilità alle source note.

## 11. Review umane richieste

- IAM architect: ciclo identità, federazione, RBAC/ABAC, account di servizio e privilegi;
- PAM specialist: accessi amministrativi, emergenza, sessioni e riesami;
- specialista crittografia/key management: proprietà, algoritmi a livello concettuale, ciclo delle chiavi, compromissione e recupero;
- SOC/SIEM engineer: sorgenti, campi, correlazione, soglie, falsi positivi/negativi e conservazione;
- incident response lead o CSIRT: triage, severità, contenimento, evidenze, recupero e lesson learned;
- esperto ACN/NIS2: platea, governance, procedure, canali, soglie e termini vigenti;
- DPO/privacy counsel: distinzione fra incidente cyber e data breach, minimizzazione e accesso ai log;
- responsabile continuità operativa: raccordo con capitolo 7 e criteri di ripristino;
- revisore editoriale: autonomia didattica, coerenza terminologica e resa del playbook nel formato KDP.

## 12. Struttura H1/H2/H3 proposta

# IAM, crittografia, logging e incident response

## Obiettivo e confine con il volume base

## Mappa BANDO: dall’identità alla risposta

## Identità, account e ciclo di vita
### Identità umane e tecniche
### Provisioning, modifica, revoca e deprovisioning
### Account privilegiati, di servizio e di emergenza

## Autenticazione, autorizzazione e privilegi
### Identificazione, autenticazione, autorizzazione e accounting
### Fattori, MFA, sessioni e federazione
### RBAC, ABAC e separazione dei compiti
### Minimo privilegio e privileged access management

## Crittografia applicata
### Cifrare, produrre integrità, autenticare e firmare
### Simmetrica, asimmetrica, hash e MAC
### Dati in transito e a riposo
### Certificati, secret e identità delle macchine

## Gestione delle chiavi
### Ciclo di vita del materiale crittografico
### Inventario, responsabilità, rotazione e revoca
### Compromissione, recupero e distruzione

## Logging e audit trail
### Eventi, log, audit, alert e incidenti
### Sorgenti e campi minimi
### Tempo, integrità, accesso e conservazione
### Centralizzazione, correlazione e SIEM

## Rilevazione e triage
### Indicatori, regole, baseline e anomalie
### Falsi positivi e falsi negativi
### Severità, priorità ed escalation

## Incident response
### Preparazione e ruoli
### Analisi e qualificazione
### Contenimento ed eradicazione
### Recupero, monitoraggio e chiusura
### Comunicazione, evidenze e lesson learned

## PA, NIS2, CSIRT e privacy
### Governance ed escalation istituzionale
### Incidente cyber e data breach
### Notifiche: usare soltanto procedure verificate

## Caso guidato: account privilegiato compromesso

## Laboratorio: costruire playbook e timeline

## Domanda da commissario

## Domande-trappola

## Mini-esercizi e quiz

## Checklist finale

## Da sapere in 5 righe

## Riferimenti consolidati

## Note di review

## 13. Budget orientativo KDP

| Sezione | Parole orientative |
| --- | ---: |
| Apertura, obiettivo e Mappa BANDO | 280-340 |
| Identità, account e ciclo di vita | 430-500 |
| Autenticazione, autorizzazione e privilegi | 550-650 |
| Crittografia applicata | 500-600 |
| Gestione delle chiavi | 380-460 |
| Logging e audit trail | 520-620 |
| Rilevazione e triage | 330-400 |
| Incident response | 650-760 |
| PA, NIS2, CSIRT e privacy | 300-380 |
| Caso guidato | 350-430 |
| Laboratorio, domande, esercizi e checklist | 650-780 |
| Riferimenti e note di review | 120-180 |
| Totale orientativo | 5.070-6.100 |

Il budget comprende tabelle e strumenti. Nel formato KDP 6,69 × 9,61 in privilegiare paragrafi brevi, tabelle con non più di quattro colonne quando possibile e playbook suddiviso in blocchi. Se la timeline supera la larghezza utile, usare righe verticali per evento invece di comprimere il corpo.

## 14. Criteri di accettazione dello step 09

- il capitolo è reader-facing e non contiene note di sistema al posto della teoria;
- ogni nucleo della matrice riceve definizione, funzione, inquadramento, elementi, distinzioni, conseguenze, caso, uso nella prova, errore tipico, verifica e fonti;
- autenticazione, autorizzazione e accounting restano distinti;
- cifratura, hash, MAC, firma e certificato non sono presentati come sinonimi;
- il ciclo delle chiavi include responsabilità, rotazione, revoca e compromissione;
- logging non equivale automaticamente a monitoraggio o rilevazione;
- evento, alert, incidente, data breach e crisi restano distinti;
- il modello di incident response è coerente con NIST SP 800-61 rev. 3 e non copia senza avvertenza la rev. 2;
- termini, soglie e canali ACN/NIS2 sono presenti solo se verificati e datati;
- il playbook assegna trigger, ruoli, decisioni, azioni, comunicazioni, evidenze e criteri di chiusura;
- casi e quiz applicano teoria già spiegata;
- il rinvio al VOL-01 è preciso e limitato ai prerequisiti;
- il capitolo non duplica rischio, vulnerabilità, continuità, data governance o procurement;
- source note, topic, entity, matrice e frontmatter sono aggiornati e coerenti;
- review umane e punti ancora da verificare sono esplicitati.

## 15. Esito del piano

Il capitolo è pianificato ma non ancora pronto per la scrittura definitiva. Prima dello step 09 vanno consolidate fonti primarie dedicate su identità digitale, key management, log management e incident response, oltre al quadro ufficiale ACN/NIS2. Una volta chiuso questo gap, la struttura proposta consente di sviluppare il capitolo senza duplicare VOL-01 o i capitoli 7-8 e mantenendo l’output concorsuale promesso: playbook e timeline di incidente.