---
id: chapter-m-tr01-12
type: book_chapter
title: "Procurement ICT e gestione dei fornitori"
status: reviewed-draft
domain: "concorsi pubblici italiani"
topics: ["procurement ICT", "capitolato tecnico", "SLA", "vendor management", "exit strategy"]
entities: ["ANAC", "Consip", "RUP", "Direttore dell'esecuzione", "AgID"]
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/procurement-ict-sla-vendor-management-fonti-consolidate", "sources/codice-contratti-pubblici-d-lgs-36-2023-e-correttivo-209-2024", "sources/ciclo-contratti-pubblici-rup-stazione-appaltante-operatore-economico", "sources/digitalizzazione-contratti-pubblici-anac-bdncp-fvoe-pcp", "sources/mepa-consip-acquisti-in-rete-strumenti-acquisto-negoziazione", "sources/ingegneria-software-api-interoperabilita-fonti-tecniche", "sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie", "sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie", "sources/iam-crittografia-logging-incident-response-fonti-primarie", "sources/data-governance-open-data-interoperabilita-fonti-primarie"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "vol-08-ict-digitale-cybersecurity-dati", "il-metodo-bando", "m-tr02-appalti-pnrr-fondi-ue"]
confidence: 0.88
updated_at: 2026-08-05
created_at: 2026-07-28
review_required: false
canonical: true
tags: ["chapter", "m-tr01", "procurement-ict", "sla", "fornitori"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 12
draft_stage: cross-reviewed
last_compiled_from: ["sources/procurement-ict-sla-vendor-management-fonti-consolidate", "topics/procurement-ict-sla-gestione-fornitori", "planning/08-capitolo-12-piano-completamento"]
---

# Procurement ICT e gestione dei fornitori

Anche un servizio aggiudicato correttamente può fallire durante l'esecuzione. Accade se il bisogno resta vago, i requisiti non sono verificabili o gli SLA misurano ciò che è facile contare invece di ciò che serve agli utenti. In altri casi, l'ente scopre troppo tardi di non poter recuperare dati e configurazioni.

Nel procurement ICT la competenza tecnica non sostituisce quella amministrativa. Entrambe concorrono allo stesso risultato: tradurre il fabbisogno in una prestazione, precisarla con requisiti e verificarla attraverso evidenze utili al governo del contratto.

## Obiettivo e confini

Al termine del capitolo il candidato saprà:

- tradurre un fabbisogno in requisiti funzionali e non funzionali;
- distinguere requisito, criterio di accettazione, criterio di valutazione, obbligo e SLA;
- costruire un livello di servizio misurabile;
- collegare ruoli tecnici e contrattuali durante l'esecuzione;
- inserire sicurezza, dati, continuità e supply chain nel governo del fornitore;
- riconoscere lock-in e progettare portabilità, reversibilità ed uscita;
- orientarsi tra ciclo digitale e strumenti di acquisto senza confonderli.

La disciplina generale dei contratti pubblici è sviluppata in [[books/il-metodo-bando/chapters/contratti-pubblici-essenziali]]. Procedure, soglie e appalti avanzati rinviano a VOL-09/M-TR02. Qui interessa il delta tecnico-organizzativo dell'acquisto ICT.

## Mappa BANDO dell'acquisto ICT

- **B — Bisogno:** risultato pubblico, utenti, perimetro, baseline e vincoli.
- **A — Attori:** RUP, direttore dell'esecuzione, owner del servizio, referenti tecnici, sicurezza, DPO e fornitore.
- **N — Nodi:** requisiti vaghi, misure ambigue, dipendenze, incidenti, modifiche, subfornitori e lock-in.
- **D — Documenti:** capitolato, matrice dei requisiti, piano dei test, SLA, report, verbali, registro rischi ed exit plan.
- **O — Output:** servizio accettato e controllato, con evidenze, continuità e possibilità reale di uscita.

## Dal fabbisogno alla strategia di acquisizione

### Risultato, perimetro e baseline

Il fabbisogno parte dal problema pubblico da risolvere, non dal prodotto desiderato. «Acquistare una piattaforma cloud» indica già una soluzione; «garantire ai cittadini l'accesso continuativo al servizio, riducendo tempi di indisponibilità e oneri di gestione» esplicita invece il risultato.

La **baseline** fotografa la situazione iniziale: utenti, volumi, tempi, costi, incidenti, tecnologie, competenze e vincoli. Senza baseline non si può dimostrare se l'acquisto abbia migliorato il servizio.

Il perimetro chiarisce ciò che il fornitore deve consegnare e ciò che resta all'ente. Include ambienti, integrazioni, dati, migrazione, assistenza, manutenzione, formazione, documentazione e uscita. Se il confine resta incerto, alcune attività non trovano un responsabile e altri costi emergono soltanto durante l'esecuzione.

### Make, buy e reuse

L'ente può sviluppare internamente, acquistare, riusare soluzioni disponibili o combinare le opzioni. La scelta considera competenze, tempi, criticità, mercato, interoperabilità, manutenzione, sicurezza e sostenibilità nel ciclo di vita.

Anche dopo l'acquisto, l'ente deve conservare competenze interne. Se nessuno nell'ente sa verificare requisiti, dati, configurazioni e livelli di servizio, il fornitore finisce per controllare anche il significato delle misure con cui viene valutato.

### Costo e dipendenze

Il prezzo iniziale è solo una parte del costo. Contano migrazione, integrazioni, licenze, gestione, formazione, crescita dei volumi, assistenza, modifiche, transizione e dismissione. Il **costo totale di possesso** è una lente decisionale; il calcolo concreto dipende dagli atti e dai dati disponibili.

Una soluzione economica all'ingresso può diventare onerosa se richiede formati proprietari, competenze rare o costi elevati per esportare dati e configurazioni. Per questo il rischio di uscita si valuta prima dell'affidamento.

## Requisiti e capitolato tecnico

### Funzionali e non funzionali

Un **requisito funzionale** descrive ciò che il sistema deve fare. Esempio: «l'operatore può consultare lo stato della pratica e la cronologia delle modifiche».

Un **requisito non funzionale** riguarda qualità o vincoli. Può riferirsi a disponibilità, prestazioni, sicurezza, accessibilità, interoperabilità, manutenibilità, capacità o portabilità. Esempio: «la cronologia deve essere esportabile in un formato documentato e leggibile da strumenti indipendenti».

Questa distinzione orienta le verifiche, ma i due gruppi restano collegati: una funzione priva di requisiti di sicurezza e prestazione può risultare inutilizzabile.

### Scrivere requisiti verificabili

Per essere efficace, un requisito specifica:

1. soggetto o componente interessato;
2. comportamento o qualità richiesta;
3. condizioni operative;
4. risultato osservabile;
5. criterio di accettazione;
6. evidenza attesa.

«Il sistema deve essere veloce» non è verificabile. «Nelle condizioni di carico definite nel piano di test, il servizio risponde entro la soglia stabilita, misurata dal punto concordato e registrata nel report» indica almeno come completare la specifica. Il valore numerico va motivato e approvato, non inventato.

**Errore tipico:** descrivere una marca o una tecnologia senza collegarla al bisogno, ai vincoli e alla disciplina applicabile. Le specifiche devono consentire una valutazione tecnica trasparente e gestire correttamente standard, compatibilità ed equivalenze.

### Requisito, criterio, obbligo e SLA

Quattro elementi spesso confusi hanno funzioni diverse:

| Elemento | Domanda |
| --- | --- |
| requisito | che cosa deve fare o garantire la soluzione? |
| criterio di accettazione | come dimostriamo che il requisito è soddisfatto? |
| criterio di valutazione | come confrontiamo le offerte secondo gli atti? |
| SLA | quale livello deve essere mantenuto durante il servizio? |

Un requisito può essere verificato una volta al collaudo oppure monitorato nel tempo. Un criterio di valutazione opera nella scelta dell'offerta; non sostituisce l'obbligo di esecuzione. Lo SLA riguarda il servizio erogato e deve collegarsi a misure e conseguenze definite.

### Tracciabilità e accettazione

La matrice requisito-test-evidenza collega promessa e verifica:

| ID | Requisito | Verifica | Evidenza | Esito |
| --- | --- | --- | --- | --- |
| R-01 | esportazione dati | prova su campione | file e verbale | da compilare |
| R-02 | gestione accessi | test dei ruoli | log e report | da compilare |
| R-03 | ripristino | esercitazione | rapporto di prova | da compilare |

Accettare una prestazione non significa esprimere un assenso generico. Registra versione, ambiente, dati di prova, risultato, anomalie, riserve, responsabili e decisione. Se il requisito cambia, devono cambiare in modo controllato anche test ed evidenze.

## SLA e misurazione del servizio

### SLA, SLI e soglia

Lo **SLA** è l'impegno contrattuale sul livello di servizio. Lo **SLI** è l'indicatore osservato. La soglia o obiettivo indica il livello atteso. Il lessico può variare tra documenti; ciò che conta è rendere non ambigue definizione, misura e responsabilità.

Una scheda SLA completa specifica:

- servizio e popolazione osservata;
- formula o regola di misura;
- soglia;
- finestra e periodo di osservazione;
- fonte dei dati e punto di misura;
- esclusioni ammesse;
- severità o classe dell'evento;
- reporting e responsabile della verifica;
- escalation e conseguenze previste dagli atti.

### Disponibilità e tempi

La **disponibilità** indica la quota di tempo in cui il servizio è utilizzabile nel perimetro concordato. Senza finestra di servizio, periodo, componenti inclusi ed esclusioni, la percentuale è equivoca.

Il **tempo di presa in carico** misura quanto passa prima che il fornitore inizi a gestire una segnalazione. Il **tempo di ripristino** riguarda il ritorno a una condizione operativa; il **tempo di risoluzione** può richiedere la rimozione definitiva della causa. Un workaround può ripristinare il servizio senza chiudere il problema.

La severità dipende dall'impatto e dall'urgenza. Un malfunzionamento che blocca tutti gli utenti non è equivalente a un difetto cosmetico. Classi e regole devono essere definite prima dell'incidente.

### SLA e KPI

Un **KPI** sostiene il governo del servizio: volume ticket, tasso di riapertura, modifiche fallite, vulnerabilità scadute, soddisfazione o backlog. Può essere utile anche senza costituire uno SLA.

Una penale o un service credit non ripara da solo il servizio. L'ente deve ottenere ripristino, analisi della causa, azione correttiva e prevenzione della ricorrenza. Le conseguenze contrattuali concrete dipendono dagli atti e dal quadro vigente.

## Ruoli e governo dell'esecuzione

### Competenze diverse, un solo sistema di controllo

Il **RUP** presidia il progetto secondo la disciplina applicabile. Il **direttore dell'esecuzione**, quando previsto, controlla l'esecuzione. L'owner del servizio presidia risultato e utenti; il referente tecnico verifica architettura e deliverable; sicurezza e DPO intervengono per competenza. Il fornitore organizza le proprie responsabilità e produce le evidenze dovute.

Una matrice RACI può chiarire chi esegue, approva, consulta e riceve informazioni. È uno strumento organizzativo: non modifica competenze stabilite dalla normativa o dagli atti.

### Avvio, reporting e verifiche

Il kick-off traduce il contratto in un assetto operativo: contatti, canali, calendario, deliverable, ambienti, accessi, reporting, rischi ed escalation. Le decisioni vanno verbalizzate e collegate ai documenti applicabili.

Un report periodico serve a decidere e controllare, non a raccogliere numeri senza esito. Deve mostrare livelli raggiunti, scostamenti, incidenti, modifiche, rischi, azioni, responsabili e scadenze. L'ente conserva dati sufficienti per verificare la misura anche quando il calcolo è prodotto dal fornitore.

### Non conformità ed escalation

Una **non conformità** è uno scostamento rispetto a requisito, deliverable o obbligo verificabile. Va descritta con evidenza, impatto, causa nota o da analizzare, azione, termine, responsabile e verifica di chiusura.

L'escalation può essere tecnica, gestionale o contrattuale. Saltare subito al livello direzionale crea rumore; restare nel supporto operativo quando il servizio è critico ritarda la risposta. Trigger e canali devono essere stabiliti prima.

## Sicurezza, dati e supply chain

### Sicurezza come prestazione verificabile

La formula «il fornitore garantisce la sicurezza» non definisce una prestazione verificabile. I requisiti possono riguardare accessi privilegiati, segregazione, logging, patching, vulnerabilità, cifratura, incidenti, backup, test di ripristino e conservazione delle evidenze. Ogni controllo deve essere proporzionato al rischio e verificabile.

Il contratto chiarisce tempi e modalità di cooperazione negli incidenti, preservazione dei log, comunicazioni, contenimento e ripristino. Gli obblighi normativi dell'ente e del fornitore vanno verificati sul caso; lo SLA interno non sostituisce eventuali termini legali.

### Dati e subfornitori

Occorre conoscere quali dati sono trattati, dove transitano, chi vi accede, per quanto tempo sono conservati e come vengono restituiti o cancellati. Formati e procedure di esportazione vanno provati, non soltanto dichiarati.

I subfornitori possono introdurre dipendenze tecniche e geografiche. L'ente deve avere visibilità coerente con rischio e disciplina applicabile. Ruoli privacy, istruzioni, trasferimenti e misure richiedono validazione di giurista e DPO.

### Supply chain

Componenti software, librerie, servizi esterni e aggiornamenti appartengono alla supply chain. Quando pertinente, inventario, provenienza, vulnerabilità, supporto ed eventuale SBOM aiutano a governare il rischio. Il capitolo 8 sviluppa la teoria; qui questi elementi diventano requisiti, report o condizioni di gestione.

## Modifiche, rilasci e continuità

### Classificare le modifiche

Correzione di un difetto, manutenzione ordinaria, evoluzione funzionale, variazione del perimetro e modifica contrattuale non sono sinonimi. La classificazione determina analisi, approvazioni, costi, test e documentazione.

Una change request descrive motivo, impatto, dipendenze, rischio, piano di test, rilascio e rollback. Versioni di requisito, configurazione, codice, documentazione e approvazione devono essere riconciliabili.

### Cutover e rollback

Il **cutover** è il passaggio operativo alla nuova soluzione o versione. Richiede prerequisiti, sequenza, responsabili, comunicazioni e criteri di go/no-go. Il **rollback** riporta a una condizione precedente controllata se il rilascio non soddisfa i criteri.

### Continuità

Backup, replica, alta disponibilità e disaster recovery rispondono a scopi diversi. RPO e RTO, spiegati nel capitolo 7, diventano qui requisiti da provare. Finché non viene provato, il piano non dimostra la capacità di ripristino.

Il contratto deve considerare anche obsolescenza ed end of support. Un componente non più supportato può trasformare manutenzione e sicurezza in un rischio di continuità.

## Lock-in, portabilità ed exit strategy

### Forme di dipendenza

Il **lock-in** non riguarda soltanto la tecnologia. Può dipendere da:

- formati o API non trasferibili;
- licenze e condizioni contrattuali;
- costi di estrazione o migrazione;
- processi organizzativi costruiti sul fornitore;
- documentazione incompleta;
- competenze presenti solo nel gruppo esterno;
- dati, configurazioni o log non esportabili.

### Portabilità e reversibilità

La **portabilità** consente di trasferire dati, applicazioni o carichi in un altro ambiente. La **reversibilità** comprende il ritorno o il passaggio controllato del servizio, con conoscenze, configurazioni, documenti e assistenza alla transizione.

La consegna finale di un file, da sola, non garantisce la portabilità. Occorre verificare completezza, struttura, metadati, leggibilità, tempi e capacità del destinatario di riutilizzarlo.

### Exit plan

L'exit plan definisce:

1. eventi che lo attivano;
2. ruoli e governance della transizione;
3. inventario di dati, configurazioni, integrazioni e documenti;
4. formati e procedure di estrazione;
5. supporto al subentro;
6. continuità durante il passaggio;
7. verifica di restituzione e cancellazione;
8. criteri di chiusura e accettazione finale.

Preparare l'exit plan soltanto alla scadenza è tardivo: l'ente deve progettarlo all'ingresso e provarlo durante l'esecuzione.

## Strumenti di acquisto e ciclo digitale

Consip opera nell'ambito del programma di razionalizzazione degli acquisti. Acquisti in Rete è il canale attraverso cui amministrazioni e imprese accedono agli strumenti; il MEPA è uno di questi. Convenzioni, accordi quadro e sistemi dinamici hanno logiche diverse. Nessuno strumento elimina la necessità di definire fabbisogno, requisiti, copertura e controlli.

La digitalizzazione riguarda tutto il ciclo del contratto. La BDNCP è la banca dati nazionale gestita da ANAC; la PCP e il FVOE svolgono funzioni specifiche nell'ecosistema. Non vanno trattati come sinonimi. Dettagli operativi, procedure e soglie devono essere verificati sulle fonti vigenti e restano nella sede contrattuale generale.

## Caso guidato: servizio cloud comunale

Un comune acquisisce migrazione, hosting cloud, manutenzione e assistenza per un portale al cittadino.

1. **Bisogno:** garantire accesso e continuità; baseline con utenti, carichi e incidenti.
2. **Perimetro:** migrazione, ambienti, integrazioni, supporto, sicurezza, documentazione ed uscita.
3. **Requisiti:** funzioni del portale più disponibilità, accessibilità, capacità, logging e portabilità.
4. **Accettazione:** test funzionali, prestazionali, di accesso, migrazione e ripristino con verbale.
5. **SLA:** indicatori distinti per disponibilità, presa in carico e ripristino; fonte e finestra concordate.
6. **Sicurezza:** account privilegiati, log, vulnerabilità, incidenti e subfornitori tracciati.
7. **Esecuzione:** report mensile, registro rischi, non conformità e escalation.
8. **Change:** ogni rilascio ha impatto, test, go/no-go e rollback.
9. **Continuità:** backup e ripristino sono provati; RPO/RTO coerenti col servizio.
10. **Uscita:** esportazione di dati e configurazioni, documentazione, supporto al subentro e verifica di cancellazione.

Il caso non determina procedura, soglia o penale: tali elementi dipendono dagli atti e dalla disciplina vigente.

## Laboratorio operativo

### Checklist del capitolato

- [ ] bisogno, baseline, utenti e perimetro sono chiari;
- [ ] requisiti funzionali e non funzionali sono verificabili;
- [ ] ogni requisito critico ha criterio di accettazione ed evidenza;
- [ ] dati, integrazioni, ambienti e migrazione sono descritti;
- [ ] SLA indicano misura, soglia, finestra, fonte ed esclusioni;
- [ ] ruoli, reporting, non conformità ed escalation sono definiti;
- [ ] sicurezza, incidenti, continuità e subfornitori sono governati;
- [ ] change, versioni, cutover e rollback sono tracciati;
- [ ] portabilità, reversibilità ed exit plan sono provabili.

### Scheda SLA

| Campo | Compilazione |
| --- | --- |
| servizio e indicatore | che cosa misuriamo |
| soglia e periodo | livello e intervallo |
| fonte e punto di misura | da quali dati |
| esclusioni | casi ammessi e motivati |
| reporting | frequenza e responsabile |
| escalation | trigger e canale |

### Registro fornitore

| Elemento | Dipendenza | Rischio | Controllo | Evidenza |
| --- | --- | --- | --- | --- |
| servizio | da compilare | da valutare | da definire | report |
| dati | da compilare | da valutare | esportazione | prova |
| subfornitore | da compilare | da valutare | monitoraggio | registro |

## Domanda da commissario

**Come imposteresti e controlleresti un contratto per un servizio cloud destinato ai cittadini?**

Partirei dal risultato pubblico, dalla baseline e dal perimetro. Tradurrei il bisogno in requisiti funzionali e non funzionali, ciascuno collegato a criteri di accettazione ed evidenze. Definirei SLA misurabili con fonte, finestra, soglia ed esclusioni. Assegnerei ruoli a RUP, direzione dell'esecuzione, owner, tecnici, sicurezza, DPO e fornitore. Governerei report, non conformità, incidenti, modifiche, continuità e supply chain. Infine predisporrei fin dall'inizio portabilità, reversibilità ed exit plan. Procedura e clausole puntuali sarebbero verificate sugli atti e sul quadro vigente.

## Domande-trappola

- **Un requisito molto dettagliato è sempre verificabile?** No: servono condizione, risultato ed evidenza.
- **Disponibilità del 99,9% basta da sola?** No: mancano perimetro, finestra, fonte, periodo ed esclusioni.
- **SLA e KPI sono sinonimi?** No: un KPI può non essere un impegno contrattuale.
- **La stipula conclude il controllo dell'ente?** No: l'esecuzione richiede verifica e governo.
- **La penale risolve il disservizio?** No: servono ripristino e azione correttiva.
- **Il backup è disaster recovery?** No: è solo uno dei possibili presidi.
- **Il cloud trasferisce ogni responsabilità al provider?** No: i ruoli dipendono dal caso e dagli atti.
- **L'exit strategy si prepara alla scadenza?** No: si progetta all'ingresso.
- **MEPA è Consip?** No: MEPA è uno strumento; Consip è il soggetto che opera nel programma.

## Mini-esercizi e soluzioni

**1.** «Il portale deve essere intuitivo» è un requisito verificabile?

**Soluzione:** no. Occorre tradurlo in condizioni e verifiche osservabili, per esempio compiti, profili di utenti, criteri di completamento e test di accessibilità o usabilità appropriati.

**2.** Un report indica soltanto «disponibilità 99,5%». Che cosa manca?

**Soluzione:** almeno perimetro, finestra, periodo, fonte, regola di calcolo, esclusioni e soglia contrattuale di confronto.

**3.** Il fornitore propone una nuova versione il giorno prima del rilascio. Quali evidenze chiedere?

**Soluzione:** impatto, versione, dipendenze, test, approvazione, piano di cutover, criteri di go/no-go e rollback.

**4.** Alla scadenza l'ente riceve un file senza schema né metadati. È portabilità effettiva?

**Soluzione:** non ancora. Deve verificare completezza, struttura, documentazione, leggibilità e riuso nel sistema destinatario.

## Da sapere in 5 righe

Il fabbisogno deve diventare una prestazione verificabile.
Requisito, accettazione, criterio di valutazione e SLA non sono sinonimi.
Un livello di servizio vale solo se misura, finestra, fonte ed esclusioni sono chiare.
Acquistare non trasferisce all'esterno il governo del servizio.
Portabilità ed uscita si progettano prima della stipula e si verificano durante l'esecuzione.

## Riferimenti consolidati

- [[sources/procurement-ict-sla-vendor-management-fonti-consolidate]]
- [[topics/procurement-ict-sla-gestione-fornitori]]
- [[topics/contratti-pubblici]]
- [[entities/codice-dei-contratti-pubblici]]
- [[sources/ciclo-contratti-pubblici-rup-stazione-appaltante-operatore-economico]]
- [[sources/digitalizzazione-contratti-pubblici-anac-bdncp-fvoe-pcp]]
- [[sources/mepa-consip-acquisti-in-rete-strumenti-acquisto-negoziazione]]
- [[sources/ingegneria-software-api-interoperabilita-fonti-tecniche]]
- [[sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie]]
- [[sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie]]
- [[sources/iam-crittografia-logging-incident-response-fonti-primarie]]
- [[sources/data-governance-open-data-interoperabilita-fonti-primarie]]

## Note di review

Audit specialistico concluso: il D.Lgs. 36/2023 consolidato, gli allegati, le indicazioni ANAC/MIT/AgID/Consip e il caso applicativo sono verificati al cut-off. Procedure, soglie, termini, clausole e obblighi mobili richiedono controllo sul caso concreto; tabelle e checklist saranno provate nel PDF.