---
id: chapter-m-tr01-08
type: book_chapter
title: "Cybersecurity operativa: rischio, controlli e vulnerabilità"
status: drafted
domain: "concorsi pubblici italiani"
topics: ["cybersecurity", "risk assessment", "vulnerabilità", "secure software", "software supply chain"]
entities: ["Agenzia per la cybersicurezza nazionale", "NIST", "OWASP", "CVE", "CWE", "FIRST", "CISA"]
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/sicurezza-informatica-privacy-nis2-pa", "sources/pa-digitale-cad-identita-documenti-servizi-dati", "sources/campione-bandi-ict-pa-vol-08-2024-2026", "sources/legge-28-giugno-2024-n-90-cybersicurezza-nazionale-e-reati-informatici", "sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "il-metodo-bando"]
confidence: 0.84
updated_at: 2026-07-29
created_at: 2026-07-28
review_required: true
canonical: true
tags: ["chapter", "m-tr01", "cybersecurity", "risk", "vulnerability"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 8
draft_stage: drafted
last_compiled_from: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/sicurezza-informatica-privacy-nis2-pa", "sources/pa-digitale-cad-identita-documenti-servizi-dati", "sources/campione-bandi-ict-pa-vol-08-2024-2026", "sources/legge-28-giugno-2024-n-90-cybersicurezza-nazionale-e-reati-informatici", "sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie", "books/moduli/m-tr01-ict-trasformazione-digitale/planning/08-capitolo-08-piano-completamento"]
---

# Cybersecurity operativa: rischio, controlli e vulnerabilità

Una vulnerabilità critica non coincide automaticamente con il rischio più urgente per un ente. La priorità dipende dal servizio interessato, dall’esposizione, dalla possibilità di sfruttamento, dagli impatti e dai controlli già presenti. La cybersecurity operativa comincia proprio qui: trasformare informazioni tecniche in decisioni motivate.

Questo capitolo costruisce il percorso completo. Parte dagli asset, descrive minacce e vulnerabilità, valuta il rischio, sceglie i controlli e segue le debolezze fino alla correzione. Chiude con sviluppo sicuro e software supply chain, perché molte vulnerabilità nascono prima del rilascio.

## Obiettivo e confine con il volume base

Il VOL-01, capitolo 10, § 6, tratta sicurezza di base, password, MFA, phishing, malware, antivirus, firewall, backup, aggiornamenti e inquadramento generale NIS2. Qui quei concetti sono prerequisiti.

Al termine saprai:

- distinguere asset, minaccia, vulnerabilità, evento, impatto e rischio;
- costruire una valutazione con scale dichiarate;
- distinguere rischio inerente e residuo;
- scegliere e classificare controlli;
- impostare threat modeling e vulnerability management;
- spiegare secure SDLC, secure coding e supply chain;
- produrre una risk matrix e una scheda di trattamento.

Continuità e backup sono nel capitolo 7. IAM, crittografia, logging e risposta all’incidente sono nel capitolo 9. Requisiti contrattuali e governo dei fornitori sono nel capitolo 12.

## Mappa BANDO: dal contesto al trattamento

| Formula nel bando | Nucleo | Output |
| --- | --- | --- |
| rischio cyber, risk assessment | scenario, probabilità, impatto | risk matrix |
| controlli, misure di sicurezza | natura, funzione, adeguatezza | piano di trattamento |
| vulnerability management | scoperta, priorità, remediation | registro vulnerabilità |
| threat modeling | asset, flussi, confini, minacce | modello di minaccia |
| secure coding, OWASP | debolezze e pratiche preventive | analisi applicativa |
| supply chain, SBOM | dipendenze, pipeline, artefatti | verifica di filiera |

In prova conviene seguire un ordine stabile: contesto, asset, scenario, rischio, trattamento, evidenza e riesame. Il nome di uno strumento conta meno della qualità del ragionamento.

## Obiettivi di sicurezza e asset

### Proprietà da proteggere

La triade CIA riassume tre proprietà:

- **riservatezza:** informazioni accessibili soltanto ai soggetti autorizzati;
- **integrità:** dati e sistemi non alterati in modo improprio e modifiche rilevabili;
- **disponibilità:** informazioni e servizi accessibili quando servono.

Si aggiungono, secondo il contesto, autenticità, tracciabilità e accountability. Il non ripudio riguarda la capacità di impedire che un soggetto neghi in modo plausibile una determinata azione, quando il sistema e il quadro applicabile lo consentono. Queste proprietà non sono intercambiabili: la cifratura può sostenere la riservatezza, ma non garantisce da sola disponibilità o correttezza del processo.

### Asset, valore e dipendenze

Un **asset** è qualcosa che ha valore per l’organizzazione e richiede protezione. Può essere:

- informativo, come un archivio;
- tecnologico, come server, applicazioni e reti;
- umano, come competenze e ruoli;
- fisico, come locali e apparati;
- organizzativo, come procedure e reputazione;
- di servizio, come la capacità di erogare una prestazione pubblica.

L’inventario registra responsabile, collocazione, dipendenze, criticità e ciclo di vita. Un asset isolato sulla carta può dipendere da identità, DNS, connettività, provider e personale reperibile. Senza tali relazioni, l’analisi sottostima i punti di guasto.

## Minacce, vulnerabilità e scenari

### Un linguaggio senza ambiguità

Una **minaccia** è una circostanza o causa potenziale capace di produrre un evento dannoso. Il **threat actor** è il soggetto che può agire intenzionalmente; non tutte le minacce, però, hanno un attore ostile: esistono errori, guasti ed eventi ambientali.

Una **vulnerabilità** è una debolezza che può essere sfruttata o contribuire al danno. Può trovarsi nel codice, nella configurazione, nel processo, nelle persone o nell’architettura. L’**exploit** è un mezzo o una tecnica che sfrutta una vulnerabilità. Il **vettore di attacco** è il percorso usato per raggiungere il bersaglio.

L’**evento** è ciò che accade; l’**impatto** è la conseguenza per l’organizzazione. Il **rischio** combina incertezza, probabilità o verosimiglianza e conseguenze rispetto agli obiettivi.

Esempio: il portale usa un componente vulnerabile (vulnerabilità); un attore invia una richiesta costruita per sfruttarlo (minaccia e vettore); il componente esegue un’operazione non prevista (evento); pratiche e servizio diventano indisponibili (impatto).

### Superficie di attacco e scenario

La **superficie di attacco** comprende punti attraverso i quali un sistema può essere raggiunto o influenzato: interfacce, API, account, dipendenze, dispositivi, persone e processi. Ridurla significa eliminare funzioni inutili, limitare esposizioni e controllare interazioni.

Uno scenario di rischio deve indicare:

1. asset e obiettivo compromesso;
2. fonte o attore della minaccia;
3. vulnerabilità e condizioni;
4. evento temuto;
5. conseguenze.

La frase «rischio ransomware alto» è troppo generica. Occorre precisare quale servizio, quale percorso, quale dipendenza e quale impatto.

## Valutare e trattare il rischio

### Probabilità e impatto

La probabilità stima quanto sia plausibile lo scenario, considerando capacità dell’attore, esposizione, frequenza, vulnerabilità e controlli. L’impatto considera conseguenze su servizi, dati, persone, finanze, conformità e fiducia istituzionale.

Una scala qualitativa può usare basso, medio e alto. Ogni livello deve avere criteri. «Impatto alto» potrebbe indicare interruzione di un servizio essenziale o compromissione significativa di dati; la definizione dipende dal contesto.

La matrice incrocia probabilità e impatto:

| Impatto \ Probabilità | Bassa | Media | Alta |
| --- | --- | --- | --- |
| Alto | Medio | Alto | Alto |
| Medio | Basso | Medio | Alto |
| Basso | Basso | Basso | Medio |

Questa matrice ordina le priorità, ma non produce una misura assoluta. Scale diverse possono dare risultati diversi; scenari con lo stesso livello possono richiedere decisioni differenti.

### Inerente e residuo

Il **rischio inerente** è valutato prima di considerare i controlli pertinenti secondo il metodo scelto. Il **rischio residuo** rimane dopo l’applicazione dei controlli. Dichiarare «residuo basso» richiede evidenze che i controlli siano presenti e funzionino.

Un controllo previsto ma non attuato non riduce il rischio. Un controllo installato ma mai verificato offre una garanzia debole.

### Processo di assessment

Un risk assessment comprende:

1. definizione di scopo, contesto, metodo e criteri;
2. identificazione di asset e dipendenze;
3. costruzione degli scenari;
4. analisi di probabilità e impatto;
5. valutazione rispetto a soglie e propensione al rischio;
6. priorità, trattamento e documentazione;
7. monitoraggio e aggiornamento.

Il **risk register** conserva scenario, asset, livello inerente, controlli, trattamento, responsabile, scadenza, evidenza e rischio residuo. Deve essere aggiornato quando cambiano architettura, minacce, vulnerabilità o impatti.

### Opzioni di trattamento

- **Evitare:** cessare l’attività che genera il rischio.
- **Ridurre o mitigare:** intervenire su probabilità o impatto.
- **Trasferire o condividere:** allocare parte delle conseguenze a un altro soggetto, senza cancellare la responsabilità dell’ente.
- **Accettare:** assumere consapevolmente il rischio residuo entro autorità e criteri definiti.

L’accettazione non equivale a ignorare. Richiede motivazione, titolare autorizzato, durata e riesame.

## Controlli e difesa per livelli

### Natura e funzione

Per natura, i controlli possono essere organizzativi, tecnici o fisici. Per funzione possono essere:

- **preventivi**, se riducono la probabilità;
- **detective**, se individuano eventi o anomalie;
- **correttivi**, se rimuovono o limitano una condizione;
- **di recupero**, se ripristinano capacità;
- **deterrenti**, se scoraggiano;
- **compensativi**, se offrono protezione alternativa quando il controllo previsto non è praticabile.

Le tassonomie variano. La classificazione serve a capire la funzione, non a moltiplicare etichette.

Esempi: formazione e policy sono organizzativi; segmentazione e protezione endpoint sono tecnici; controllo degli accessi ai locali è fisico. Un medesimo controllo può avere più effetti.

### Difesa in profondità

La difesa in profondità combina controlli diversi affinché il fallimento di uno non esponga direttamente l’asset. Inventario, hardening, patching, minimo privilegio, segmentazione, monitoraggio e backup agiscono su punti differenti.

I livelli devono essere sufficientemente indipendenti. Due strumenti che dipendono dalla stessa identità amministrativa possono fallire insieme se quell’identità è compromessa.

Il principio Zero Trust, quando applicato, evita di attribuire fiducia implicita soltanto per posizione di rete. Richiede verifica esplicita, minimo privilegio e valutazione continua del contesto; non è un prodotto.

### NIST CSF 2.0

Il NIST CSF 2.0 organizza outcome in sei funzioni:

- **Govern:** strategia, ruoli, politiche e supervisione;
- **Identify:** asset, contesto e rischi;
- **Protect:** salvaguardie;
- **Detect:** individuazione degli eventi;
- **Respond:** gestione della risposta;
- **Recover:** ripristino e miglioramento.

Le funzioni sono concorrenti e continue, non fasi rigide. Il CSF aiuta a comunicare outcome e lacune, ma non sostituisce l’assessment né prescrive un singolo insieme di tecnologie.

## Threat modeling

Il threat modeling anticipa domande di sicurezza durante progettazione ed evoluzione. Il gruppo:

1. descrive sistema, attori e obiettivi;
2. disegna componenti, flussi e confini di fiducia;
3. individua asset e scenari di minaccia;
4. seleziona mitigazioni;
5. verifica assunzioni e copertura.

STRIDE è una tassonomia possibile: spoofing, tampering, repudiation, information disclosure, denial of service ed elevation of privilege. Non è l’unico metodo e non deve diventare un elenco scollegato dal sistema.

Un diagramma dei flussi mostra dove i dati entrano, cambiano fiducia, vengono elaborati e conservati. Ogni confine suggerisce domande su validazione, identità, autorizzazione e protezione.

## Gestione delle vulnerabilità

### Scoperta e validazione

La gestione parte dall’inventario di asset, versioni e dipendenze. Le vulnerabilità emergono da scanning, test, segnalazioni, intelligence, advisory e comunicazioni dei fornitori.

Un risultato deve essere validato. Un **falso positivo** segnala una condizione inesistente o non applicabile; un **vero positivo** richiede trattamento. La validazione non autorizza prove invasive indiscriminate: scopo, permessi e sicurezza del test vanno definiti.

### CVE, CWE e CVSS

- **CVE** identifica una specifica vulnerabilità pubblicamente nota.
- **CWE** descrive una classe di debolezze che può generare vulnerabilità.
- **CVSS** comunica caratteristiche e gravità mediante un punteggio e un vettore.

CVSS 4.0 distingue metriche Base, Threat, Environmental e Supplemental. Il punteggio di base non conosce da solo criticità dell’asset, esposizione, exploit osservati o controlli locali. Perciò il CVSS più alto non è sempre la prima priorità.

### Priorità e remediation

La priorità considera:

- gravità tecnica;
- sfruttabilità e attività osservata;
- esposizione;
- criticità del servizio;
- presenza di dati sensibili;
- controlli compensativi;
- disponibilità e rischio della correzione.

La remediation assegna responsabile e scadenza, prova la patch, pianifica la distribuzione e verifica la chiusura. Se la patch non è applicabile subito, una mitigazione temporanea può ridurre esposizione o funzionalità. L’eccezione deve indicare rischio residuo, approvazione e data di riesame.

La responsible disclosure coordina segnalazione e correzione evitando diffusione prematura di dettagli. Nel lavoro pubblico vanno rispettati canali, autorizzazioni e procedure applicabili.

## Secure SDLC e secure coding

### Sicurezza lungo il ciclo di vita

Il NIST SSDF integra pratiche di sicurezza nel ciclo di sviluppo. La sicurezza entra in requisiti, progettazione, implementazione, verifica, rilascio, esercizio e dismissione.

**Security by design** significa considerare minacce e requisiti durante la progettazione. **Security by default** significa fornire configurazioni iniziali prudenti. Una scansione finale non recupera facilmente una scelta architetturale insicura.

Le attività comprendono requisiti verificabili, threat modeling, ambienti protetti, dipendenze governate, review, test, artefatti controllati, gestione delle vulnerabilità e apprendimento dalle cause.

### Pratiche di codice sicuro

- validare input rispetto a tipo, formato, lunghezza e dominio attesi;
- codificare l’output secondo il contesto;
- usare query parametrizzate invece di concatenare input;
- gestire errori senza esporre dettagli sensibili;
- non incorporare secret nel codice;
- applicare autorizzazioni sul server;
- mantenere dipendenze e configurazioni;
- fallire in modo sicuro quando una condizione non è gestibile.

La validazione client migliora l’esperienza, ma non sostituisce quella lato server. Una denylist di stringhe pericolose è spesso meno robusta della definizione positiva dei valori ammessi.

### Verifiche diverse

La **code review** esamina logica e modifiche. La **SAST** analizza codice o rappresentazioni senza eseguire l’applicazione. La **DAST** osserva il comportamento di un’applicazione in esecuzione. La **software composition analysis** esamina componenti e dipendenze. Il **penetration test** simula scenari entro uno scopo autorizzato.

Nessuna tecnica copre tutto. I risultati richiedono validazione e collegamento al rischio.

OWASP Top 10 è un documento di awareness sui rischi delle applicazioni web. L’edizione 2025 include categorie come controllo accessi, configurazione, supply chain, crittografia, injection e design insicuro. Non certifica la sicurezza e non sostituisce requisiti, threat modeling o test basati sul contesto.

## Software supply chain

La supply chain comprende codice proprio, librerie, componenti open source e commerciali, repository, tool di build, runner, pipeline, artefatti e canali di distribuzione. Un attacco può colpire un componente, una credenziale, il processo di build o l’aggiornamento.

I controlli includono:

- inventario di componenti e versioni;
- fonti e repository autorizzati;
- protezione di account e pipeline;
- review delle modifiche;
- isolamento e aggiornamento della toolchain;
- artefatti identificati e verificabili;
- provenienza e attestazioni;
- monitoraggio degli advisory;
- capacità di ricostruire e revocare una release.

Una **SBOM** è un record formale dei componenti e delle relazioni. Aiuta a rispondere «dove usiamo questa libreria?», ma non dimostra che il software sia sicuro, aggiornato o privo di componenti non dichiarati. Deve essere mantenuta, associata all’artefatto e usata nei processi di gestione.

Il rischio di terze parti resta dell’organizzazione anche quando alcune attività sono affidate fuori. Requisiti contrattuali e SLA sono trattati nel capitolo 12.

## Caso guidato: portale per le domande

Un ente gestisce un portale per presentare domande di contributo. L’applicazione usa una libreria con una vulnerabilità pubblica; il servizio è esposto e tratta documenti personali.

**Scenario.** Un attore remoto sfrutta la libreria tramite una funzione di caricamento e accede a documenti non autorizzati.

**Asset.** Documenti, profili utenti, applicazione e continuità del procedimento.

**Valutazione inerente.** Probabilità alta per esposizione e applicabilità; impatto alto per riservatezza e servizio. Nella matrice 3×3 il rischio è alto.

**Controlli esistenti.** Segmentazione, privilegi limitati e monitoraggio riducono propagazione e tempo di rilevazione, ma non eliminano la debolezza.

**Trattamento.** Il responsabile applica la patch dopo test; nel frattempo limita la funzione, rafforza le regole applicative e monitora gli indicatori pertinenti. Registra scadenza ed evidenze.

**Rischio residuo.** Viene rivalutato dopo verifica della versione e test funzionale. Non scende automaticamente: la decisione usa evidenze.

**Supply chain.** La SBOM consente di individuare altri servizi con la stessa libreria. La lezione viene riportata nei requisiti di aggiornamento e nella pipeline.

## Laboratorio: costruire una risk matrix

Compila una riga per ciascuno scenario.

| Campo | Domanda |
| --- | --- |
| Asset | che cosa ha valore e chi ne risponde? |
| Scenario | quale minaccia sfrutta quale vulnerabilità? |
| Evento | che cosa può accadere? |
| Impatto | quali conseguenze e con quale livello? |
| Probabilità | quali fattori la rendono plausibile? |
| Inerente | quale livello prima dei controlli? |
| Controlli | quali esistono e quali evidenze? |
| Trattamento | evitare, ridurre, trasferire o accettare? |
| Responsabile | chi attua e chi accetta? |
| Scadenza | entro quando? |
| Residuo | che cosa rimane dopo la verifica? |
| Riesame | quale evento o data riapre la valutazione? |

## Domanda da commissario

**«Come imposteresti un risk assessment cyber?»**

Definirei scopo, metodo e criteri; identificherei asset e dipendenze; costruirei scenari con minacce, vulnerabilità, eventi e impatti; stimerei probabilità e impatto; valuterei controlli e rischio inerente; sceglierei trattamento, responsabile, scadenza ed evidenza; infine valuterei il rischio residuo e fisserei il riesame.

## Domanda-trappola

**«La vulnerabilità con CVSS più alto va sempre corretta per prima?»**

No. CVSS comunica la gravità tecnica, ma la priorità dipende anche da esposizione, sfruttabilità, criticità dell’asset, impatto, controlli e rischio della modifica. Il punteggio è un input, non la decisione.

## Errore tipico

Assegnare «rischio alto» senza descrivere scenario e scale. Una valutazione verificabile esplicita asset, minaccia, vulnerabilità, impatto, probabilità, controlli e assunzioni.

## Mini-esercizi e quiz

1. Una configurazione predefinita con credenziali note è:
   - A. una minaccia
   - B. una vulnerabilità
   - C. un impatto
   - D. un rischio residuo

2. Il rischio dopo i controlli è:
   - A. inerente
   - B. residuo
   - C. assoluto
   - D. CVE

3. Quale identificatore riguarda una vulnerabilità specifica?
   - A. CWE
   - B. CVE
   - C. CVSS
   - D. CSF

4. Quale tecnica analizza un’applicazione in esecuzione?
   - A. DAST
   - B. SAST
   - C. SBOM
   - D. risk register

5. Una SBOM:
   - A. certifica che il software è sicuro
   - B. elenca componenti e relazioni della supply chain
   - C. sostituisce il penetration test
   - D. corregge le dipendenze

6. Costruisci uno scenario distinguendo minaccia, vulnerabilità, evento e impatto.

7. Indica un controllo preventivo, uno detective e uno compensativo per lo stesso scenario.

**Soluzioni:** 1-B; 2-B; 3-B; 4-A; 5-B. Nelle risposte aperte verifica che i termini non siano usati come sinonimi e che il controllo compensativo riduca realmente probabilità o impatto.

## Checklist finale

- ho definito scopo, metodo e scale;
- ho inventariato asset e dipendenze;
- ho distinto minaccia, vulnerabilità, evento e impatto;
- ho costruito scenari verificabili;
- ho valutato inerente e residuo;
- ho associato controlli a evidenze;
- ho assegnato responsabile e scadenza;
- ho prioritizzato vulnerabilità con il contesto;
- ho distinto CVE, CWE e CVSS;
- ho integrato sicurezza nel ciclo di sviluppo;
- ho considerato dipendenze, pipeline e artefatti;
- ho previsto riesame e chiusura.

## Da sapere in 5 righe

Il rischio nasce da uno scenario, non da un punteggio isolato. Minaccia, vulnerabilità, evento e impatto sono concetti distinti. I controlli riducono probabilità o conseguenze e devono produrre evidenze. CVE identifica, CWE classifica debolezze, CVSS comunica gravità. Sviluppo sicuro e supply chain portano la prevenzione prima del rilascio.

## Riferimenti consolidati

- [[sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie]]
- [[sources/sicurezza-informatica-privacy-nis2-pa]]
- [[sources/pa-digitale-cad-identita-documenti-servizi-dati]]
- [[sources/campione-bandi-ict-pa-vol-08-2024-2026]]
- [[sources/legge-28-giugno-2024-n-90-cybersicurezza-nazionale-e-reati-informatici]]
- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]]
- [[topics/sicurezza-informatica]]
- [[topics/ict-digitale-cybersecurity-dati-concorsi-pa]]
- [[entities/agenzia-cybersicurezza-nazionale]]
- [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali]], § 6.

## Note di review

- Verificare al text freeze quadro ACN, NIS2, procedure e terminologia vigenti.
- Sottoporre risk matrix e trattamento a cyber risk manager e security architect.
- Far validare vulnerability management, CVSS e remediation da uno specialista.
- Far revisionare secure coding, test e OWASP da un application security engineer.
- Verificare SBOM, provenienza e pipeline con uno specialista software supply chain.
- Mantenere nel capitolo 9 IAM, crittografia, logging e incident response di dettaglio.
