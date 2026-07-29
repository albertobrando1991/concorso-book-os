# Piano di completamento — Capitolo 08

## Target

`chapters/08-cybersecurity-rischio-controlli-vulnerabilita.md`

## Impostazione proposta

Il capitolo segue il percorso con cui un’organizzazione passa dal contesto al trattamento del rischio:

1. obiettivi di sicurezza e patrimonio da proteggere;
2. minacce, vulnerabilità, eventi e impatti;
3. valutazione e trattamento del rischio;
4. controlli e difesa per livelli;
5. gestione delle vulnerabilità;
6. sviluppo sicuro e supply chain del software.

La progressione conduce agli output richiesti dalla matrice — risk matrix e analisi di rischio — senza duplicare la sicurezza di base del VOL-01 né assorbire IAM, crittografia, logging e incident response, assegnati al capitolo 9.

## Esito della ricognizione

Il capitolo contiene soltanto frontmatter, titolo e specifica della struttura madre. La riga «Cybersecurity» della matrice è `parziale`: rischio, controlli e vulnerabilità non dispongono ancora di testo specialistico destinato al lettore.

Il VOL-01, capitolo 10, § 6, sviluppa i prerequisiti operativi: obiettivi generali della sicurezza, password, MFA, phishing, social engineering, malware, antivirus, firewall, backup, aggiornamenti e inquadramento generale NIS2. Il capitolo 8 deve richiamare tali nozioni senza ripeterle e costruire il livello specialistico: asset, threat actor, minaccia, vulnerabilità, evento, probabilità, impatto, rischio inerente e residuo, trattamento, controlli, threat modeling, vulnerability management, secure SDLC, secure coding e supply chain.

Il confine con il capitolo 7 riguarda soprattutto continuità, backup e resilienza cloud. Il capitolo 9 sviluppa identità, autenticazione e autorizzazione, privilegi, cifratura, chiavi, log di sicurezza, rilevazione, triage, contenimento, eradicazione, ripristino e comunicazione dell’incidente. Il capitolo 12 tratta requisiti contrattuali, SLA e gestione dei fornitori.

## Collegamento riga per riga alla matrice

| Campo della matrice | Presa in carico nel piano |
| --- | --- |
| Famiglia/profilo: Cyber e ICT | Teoria, casi e verifiche calibrati su analisi e gestione operativa del rischio cyber nella PA. |
| Materia: Cybersecurity | Percorso unitario da obiettivi e asset a rischio, controlli, vulnerabilità, secure coding e supply chain. |
| Concetti: rischio, controlli, vulnerabilità | Tutti ricevono definizione, funzione, elementi, distinzioni, conseguenze ed esempi. |
| Frequenza/peso: da validare | Nessuna frequenza quantitativa; framework, standard e profondità dipendono dai bandi. |
| Fonte consolidata: dossier M-TR01 | Il dossier definisce il perimetro ma non basta per claim tecnici, regolatori e metodologici. |
| Collocazione: capitolo 08 | Rischio, controlli e prevenzione restano qui; IAM e risposta all’incidente ricevono rinvii precisi. |
| Copertura teorica: da sviluppare | Ogni nucleo avrà una spiegazione autonoma prima di casi, matrice ed esercizi. |
| Applicazione: risk matrix | Costruzione da asset, scenario di minaccia, vulnerabilità, probabilità, impatto e controllo. |
| Output: analisi rischio | Scheda motivata con rischio inerente, trattamento, responsabile, scadenza e rischio residuo. |
| Verifica: caso | Caso guidato, domanda-trappola, esercizi, quiz e checklist. |
| Stato: parziale | Potrà passare a `completo` soltanto dopo la verifica del testo reale allo step 10. |
| Review: ACN, NIST, OWASP | Necessari fonti ufficiali aggiornate e review risk, security architecture e application security. |

## Nuclei assegnati

1. Confine tra sicurezza introduttiva del VOL-01 e livello specialistico del VOL-08.
2. Sicurezza come protezione di dati, sistemi, servizi e capacità operative.
3. Riservatezza, integrità e disponibilità; autenticità, accountability e non ripudio come proprietà collegate da usare con precisione.
4. Asset informativi, tecnologici, fisici, umani, organizzativi e di servizio.
5. Valore, criticità, dipendenze e responsabile dell’asset.
6. Threat actor, minaccia, vettore, tecnica, evento e scenario di rischio.
7. Vulnerabilità come debolezza sfruttabile e distinzione da minaccia, esposizione ed exploit.
8. Superficie di attacco e condizioni che rendono praticabile uno scenario.
9. Probabilità o verosimiglianza, impatto e livello di rischio.
10. Impatti su servizio, dati, persone, finanze, conformità e reputazione istituzionale.
11. Rischio inerente e rischio residuo.
12. Criteri e scale qualitative o quantitative; necessità di definire scala, soglie e assunzioni.
13. Risk assessment: contesto, asset, scenari, controlli esistenti, stima, valutazione e priorità.
14. Risk register e risk matrix come strumenti di decisione, non misure oggettive assolute.
15. Trattamento del rischio: evitare, ridurre/mitigare, trasferire/condividere e accettare.
16. Risk owner, control owner, azione, scadenza, evidenza e monitoraggio.
17. Controlli amministrativi/organizzativi, tecnici e fisici.
18. Controlli preventivi, deterrenti, detective, correttivi, di recupero e compensativi, con tassonomia da consolidare.
19. Difesa in profondità e indipendenza dei livelli di controllo.
20. Minimo privilegio, separazione dei compiti, segmentazione, hardening, patching, protezione endpoint e backup come esempi, con rinvio ai capitoli specialistici.
21. NIST Cybersecurity Framework 2.0: Govern, Identify, Protect, Detect, Respond e Recover come mappa, senza sostituire l’analisi.
22. Governance del rischio, ruoli, politiche, eccezioni ed evidenze.
23. Concetto di Zero Trust a livello di principio, soltanto con fonte primaria e senza slogan.
24. Threat modeling: sistema, confini di fiducia, flussi, asset, minacce, mitigazioni e verifica.
25. STRIDE come possibile tassonomia didattica, solo dopo consolidamento della fonte e senza presentarlo come metodo obbligatorio.
26. Inventario degli asset e delle dipendenze come prerequisito della gestione delle vulnerabilità.
27. Scoperta tramite segnalazioni, scanning, test, intelligence e comunicazioni dei fornitori.
28. Validazione della vulnerabilità e distinzione fra vero positivo, falso positivo e accettazione del rischio.
29. Prioritizzazione basata su gravità, sfruttabilità, esposizione, criticità e controlli, non sul solo punteggio.
30. CVE, CWE e CVSS: ruoli distinti, versioni e limiti da verificare sulle fonti ufficiali.
31. Ciclo di remediation: assegnazione, patch, mitigazione temporanea, test, distribuzione, verifica e chiusura.
32. Gestione delle eccezioni e rischio residuo quando non si può correggere subito.
33. Responsible disclosure e coordinamento, a livello concettuale e senza istruzioni offensive.
34. Secure SDLC: requisiti, progettazione, implementazione, verifica, rilascio, esercizio e dismissione.
35. Security by design e by default, distinguendo il principio dalla sola scansione finale.
36. Secure coding: validazione degli input, codifica dell’output, query parametrizzate, gestione degli errori, secret, dipendenze e configurazione sicura.
37. OWASP Top 10 come strumento di consapevolezza, non checklist esaustiva né standard di conformità.
38. Code review, analisi statica e dinamica, test delle dipendenze e penetration test: funzioni, differenze e limiti.
39. Software supply chain: codice, dipendenze, toolchain, repository, pipeline, artefatti e canali di distribuzione.
40. SBOM, provenienza, firma o attestazione, dipendenze bloccate/versionate e verifica degli aggiornamenti, secondo fonti ufficiali.
41. Rischio di terze parti e fornitori, mantenendo requisiti contrattuali nel capitolo 12.
42. Caso PA, risk matrix, quiz, risposta orale e checklist.

## Nuclei già completi

Nessun nucleo specialistico è completo nel capitolo 8.

Nel VOL-01, capitolo 10, § 6, sono già completi i prerequisiti:

- finalità generale della sicurezza informatica;
- riservatezza, integrità e disponibilità a livello introduttivo;
- password, autenticazione e MFA;
- malware, virus, ransomware, phishing e social engineering;
- funzione generale di antivirus e firewall;
- backup e aggiornamenti come misure operative;
- comportamento sicuro sulla postazione;
- inquadramento generale della sicurezza nella PA e del recepimento NIS2.

Il rinvio non copre metodologia di risk assessment, rischio inerente e residuo, tassonomie dei controlli, threat modeling, vulnerability management, secure SDLC, secure coding o supply chain.

## Nuclei da sviluppare

- linguaggio comune di asset, minaccia, vulnerabilità, evento, probabilità, impatto e rischio;
- processo di valutazione e trattamento;
- costruzione e lettura di risk register e risk matrix;
- categorie, finalità e limiti dei controlli;
- governance e difesa in profondità;
- threat modeling e superficie di attacco;
- ciclo completo delle vulnerabilità;
- prioritizzazione contestuale e gestione delle eccezioni;
- secure SDLC e principi di secure coding;
- differenze fra review, SAST, DAST, test dipendenze e penetration test;
- rischi e controlli della software supply chain;
- caso guidato e analisi di rischio completa.

## Sezioni da conservare

- frontmatter e identificativi;
- H1 esistente;
- specifica della struttura madre come vincolo editoriale;
- collocazione nella Parte II del volume;
- output previsto: risk matrix;
- review ACN, NIST e OWASP.

## Duplicazioni da evitare

- password, MFA, phishing, malware, antivirus, firewall, backup e igiene digitale già trattati nel VOL-01;
- architettura di rete, segmentazione e troubleshooting generale del capitolo 5;
- requisiti, testing e ciclo di vita del software del capitolo 6, da richiamare solo per il delta security;
- resilienza, backup, RPO/RTO, disaster recovery e continuità del capitolo 7;
- identità, autorizzazione, privilegi, crittografia, chiavi, log, monitoraggio di sicurezza e incident response del capitolo 9;
- privacy, data breach e DPIA come disciplina specialistica, trattati nel volume base e nei capitoli pertinenti;
- clausole, SLA e gestione contrattuale dei fornitori del capitolo 12;
- tecniche offensive eseguibili, payload, exploit o procedure che non hanno funzione didattica difensiva.

Il testo non deve confondere minaccia e vulnerabilità, vulnerabilità e incidente, rischio e gravità tecnica, conformità e sicurezza, penetration test e vulnerability scan, CVE e CVSS, né presentare OWASP Top 10 come certificazione.

## Esempi, casi, domande ed esercizi necessari

- classificazione di esempi come asset, minaccia, vulnerabilità, evento, impatto o controllo;
- scenario di credenziali esposte su un portale e costruzione della catena causale;
- matrice 3×3 o 5×5 con scale dichiarate e limiti espliciti;
- confronto fra rischio inerente e residuo dopo uno o più controlli;
- scelta motivata fra evitare, mitigare, trasferire e accettare;
- classificazione di controlli per natura e funzione;
- mappa di minacce su un servizio di presentazione domande;
- prioritizzazione di due vulnerabilità con gravità tecnica diversa ma contesto differente;
- ciclo di remediation con patch non immediatamente applicabile e controllo compensativo;
- esempio di validazione input e query parametrizzata senza codice sfruttabile;
- confronto fra SAST, DAST, software composition analysis e penetration test;
- caso di dipendenza compromessa nella pipeline e misure di supply chain;
- domanda da commissario sul processo di risk assessment;
- domanda-trappola «la vulnerabilità con CVSS più alto va sempre corretta per prima?»;
- errore tipico: assegnare il rischio senza descrivere scenario, scala e controlli esistenti;
- quiz su rischio, controlli, vulnerabilità, secure coding e supply chain;
- checklist finale «contesto, asset, scenario, rischio, trattamento, evidenza, riesame».

## Fonti da usare

### Fonti e pagine già consolidate

- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]] — per perimetro editoriale;
- [[sources/sicurezza-informatica-privacy-nis2-pa]];
- [[sources/pa-digitale-cad-identita-documenti-servizi-dati]];
- [[sources/reti-sistemi-infrastrutture-fonti-tecniche]];
- [[sources/campione-bandi-ict-pa-vol-08-2024-2026]];
- [[sources/legge-28-giugno-2024-n-90-cybersicurezza-nazionale-e-reati-informatici]];
- [[topics/sicurezza-informatica]];
- [[topics/ict-digitale-cybersecurity-dati-concorsi-pa]];
- [[entities/agenzia-cybersicurezza-nazionale]];
- [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali]], capitolo 10, § 6;
- [[books/moduli/m-tr01-ict-trasformazione-digitale/planning/02-matrice-copertura-didattica]].

### Fonti tecniche e istituzionali da consolidare prima o durante lo step 09

- NIST Cybersecurity Framework 2.0 e profili ufficiali;
- NIST SP 800-30 per risk assessment;
- NIST SP 800-53 per famiglie e finalità dei controlli, usato come riferimento e non come obbligo generale per la PA italiana;
- NIST SP 800-218 Secure Software Development Framework;
- NIST National Vulnerability Database e documentazione ufficiale CVSS vigente;
- MITRE per CVE e CWE e per le rispettive funzioni;
- OWASP Top 10, ASVS, SAMM, Cheat Sheet Series e Software Component Verification Standard, selezionando soltanto i documenti pertinenti;
- documentazione ufficiale ACN su gestione del rischio, vulnerabilità e sviluppo sicuro;
- direttiva NIS2 e D.Lgs. 4 settembre 2024, n. 138, sulle fonti ufficiali vigenti;
- CISA e NTIA per SBOM e software supply chain, quando applicabili;
- SLSA e specifiche di attestazione/provenienza solo se sostenute da fonti primarie e utili ai bandi;
- bandi e tracce ufficiali del campione VOL-08 per validare framework, standard e profondità richiesti.

Le fonti consolidate attuali sostengono il perimetro introduttivo, ma non bastano per dichiarare completi risk assessment, vulnerability management, secure coding e supply chain. Le nuove fonti devono diventare una source note consolidata prima del congelamento del testo.

## Topic, entity e quiz collegati

- `topics/sicurezza-informatica.md` offre i prerequisiti ma resta orientato al livello generalista;
- `topics/ict-digitale-cybersecurity-dati-concorsi-pa.md` coordina il modulo;
- l’entity ACN richiede ancora fonti granulari su funzioni, procedure e misure;
- non risultano topic specialistici consolidati sufficienti su risk assessment, vulnerability management, application security e supply chain;
- non risultano quiz specialistici consolidati che coprano l’intero capitolo;
- esempi, risk matrix e quiz richiedono review tecnica e metodologica.

## Review umane richieste

- cyber risk manager: contesto, scale, stima, trattamento e rischio residuo;
- security architect: controlli, difesa in profondità, segmentazione e threat modeling;
- vulnerability manager: inventario, scanning, priorità, remediation, eccezioni e verifica;
- application security engineer: secure SDLC, secure coding, SAST/DAST e OWASP;
- software supply chain specialist: dipendenze, SBOM, provenienza, artefatti e toolchain;
- penetration tester: distinzione fra scanning, test e validazione, senza introdurre procedure offensive;
- esperto ACN/NIS2: terminologia, governance, misure e quadro vigente;
- DPO o privacy specialist: raccordi con dati personali e data breach senza duplicazioni;
- responsabile del campione bandi: profondità e framework effettivamente richiesti;
- responsabile editoriale: confini con VOL-01 e capitoli 5-7, 9 e 12;
- revisore didattico: coerenza fra teoria, risk matrix, caso, quiz e risposta orale;
- revisore fonti: vigenza e granularità dei riferimenti ACN, NIST, OWASP, MITRE e UE.

## Struttura proposta e budget KDP

# Cybersecurity operativa: rischio, controlli e vulnerabilità

## Obiettivo e confine con il VOL-01 — 170 parole

## Mappa BANDO dal contesto al trattamento — 190 parole

## Obiettivi di sicurezza e asset — 380 parole

### Riservatezza, integrità, disponibilità e proprietà collegate

### Asset, valore, dipendenze e responsabilità

## Minacce, vulnerabilità e scenari — 500 parole

### Threat actor, vettore, evento e impatto

### Vulnerabilità, exploit e superficie di attacco

## Valutare e trattare il rischio — 620 parole

### Probabilità, impatto, rischio inerente e residuo

### Risk matrix, risk register e opzioni di trattamento

## Controlli e difesa per livelli — 520 parole

### Natura, funzione e controlli compensativi

### Governance, NIST CSF e difesa in profondità

## Threat modeling e gestione delle vulnerabilità — 620 parole

### Confini, flussi, minacce e mitigazioni

### Scoperta, priorità, remediation, eccezioni e verifica

## Secure SDLC e secure coding — 560 parole

### Security by design lungo il ciclo di vita

### Input, output, query, errori, secret e dipendenze

## Software supply chain — 420 parole

### Repository, pipeline, artefatti e terze parti

### SBOM, provenienza e verifica

## Caso guidato: rischio su un servizio di presentazione domande — 320 parole

## Laboratorio: costruire una risk matrix — 320 parole

## Domanda da commissario e domanda-trappola — 170 parole

## Errore tipico — 80 parole

## Mini-esercizi e quiz — 320 parole

## Checklist finale — 160 parole più tabella

## Da sapere in cinque righe — 60 parole

## Riferimenti consolidati e note di review — 110 parole

Budget orientativo: 5.200-5.600 parole, tabelle, schemi, caso ed esercizi inclusi. Il budget non comprende tutorial offensivi, dettagli crittografici, playbook di incidente, disciplina privacy estesa o procurement.

## Criteri di approvabilità per lo step 09

- ogni elemento della specifica e della matrice riceve teoria e verifica;
- il rinvio al VOL-01 resta preciso e limitato ai prerequisiti;
- asset, minaccia, vulnerabilità, exploit, evento, impatto e rischio restano distinti;
- la risk matrix dichiara scale e limiti e non produce una falsa precisione;
- rischio inerente e residuo sono spiegati e applicati;
- trattamento, responsabile, scadenza ed evidenza accompagnano la valutazione;
- controlli sono classificati per natura e funzione senza tassonomie contraddittorie;
- NIST CSF è usato come mappa e non sostituisce il risk assessment;
- threat modeling parte da sistema, flussi e confini, non da un elenco astratto di attacchi;
- priorità delle vulnerabilità considera contesto e sfruttabilità, non il solo CVSS;
- CVE, CWE e CVSS sono definiti con ruoli distinti;
- secure coding è inserito nel ciclo di vita e non ridotto a scansione finale;
- OWASP Top 10 non è presentato come certificazione o lista esaustiva;
- supply chain comprende dipendenze, toolchain, pipeline, artefatti e distribuzione;
- IAM, crittografia, logging e incident response restano nel capitolo 9;
- esempi e casi applicano concetti già spiegati e non includono procedure offensive;
- fonti tecniche mancanti e review specialistiche restano aperte finché non eseguite.
