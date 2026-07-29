---
id: chapter-m-tr01-06
type: book_chapter
title: "Ingegneria software, API e interoperabilità PA"
status: developing
domain: "concorsi pubblici italiani"
topics: ["ingegneria software", "api", "interoperabilità", "PDND", "testing"]
entities: ["IEEE Computer Society", "IETF", "OpenAPI Initiative", "AgID", "PDND", "Unione europea"]
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/pa-digitale-cad-identita-documenti-servizi-dati", "sources/d-lgs-7-marzo-2005-n-82-amministrazione-digitale", "sources/agid-piano-triennale-informatica-pa-2024-2026-aggiornamento-2026", "sources/ingegneria-software-api-interoperabilita-fonti-tecniche"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "il-metodo-bando"]
confidence: 0.82
updated_at: 2026-07-29
created_at: 2026-07-28
review_required: true
canonical: true
tags: ["chapter", "m-tr01", "software-engineering", "api", "interoperabilita"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 6
draft_stage: content-draft
last_compiled_from: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/pa-digitale-cad-identita-documenti-servizi-dati", "sources/d-lgs-7-marzo-2005-n-82-amministrazione-digitale", "sources/agid-piano-triennale-informatica-pa-2024-2026-aggiornamento-2026", "sources/ingegneria-software-api-interoperabilita-fonti-tecniche", "topics/open-data-interoperabilita-cloud-pa", "topics/pa-digitale", "books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali", "books/moduli/m-tr01-ict-trasformazione-digitale/planning/08-capitolo-06-piano-completamento"]
---

# Ingegneria software, API e interoperabilità PA

All’origine di un servizio digitale c’è un bisogno. Il servizio coinvolge persone e amministrazioni, tratta dati, dipende da altri sistemi e deve funzionare anche quando requisiti e contesto cambiano. Il codice è solo una parte del lavoro: bisogna dimostrare che la soluzione risponde al bisogno, governarne l’evoluzione e permettere ad altri sistemi di usarla senza conoscerne l’implementazione interna.

L’ingegneria software disciplina questo percorso. Le API rendono espliciti i contratti fra sistemi; l’interoperabilità li collega a regole organizzative, semantiche e tecniche. Nella PA il risultato atteso è un servizio affidabile, comprensibile, autorizzato e governabile. L’endpoint ne costituisce soltanto l’interfaccia tecnica.

## Obiettivo e confine con il VOL-01

Il VOL-01, capitolo 10, § 16, introduce API, interoperabilità e PDND e chiarisce che scambio autorizzato e pubblicazione open data sono fenomeni diversi. Qui quei prerequisiti diventano strumenti di progettazione.

Dopo lo studio del capitolo dovrai saper:

- trasformare un bisogno in requisiti verificabili;
- confrontare modelli di ciclo di vita senza applicarli meccanicamente;
- leggere un’architettura per componenti, interfacce e dipendenze;
- distinguere verifica, validazione e livelli di test;
- spiegare controllo di versione e gestione delle modifiche;
- progettare il contratto essenziale di un’API;
- riconoscere compatibilità, idempotenza, errori e livelli di servizio;
- distinguere i livelli dell’interoperabilità;
- costruire un caso e-service con erogatore, fruitore, finalità ed evidenze.

Programmazione e strutture dati sono nel capitolo 3; basi dati nel capitolo 4; HTTP come protocollo e i servizi di rete nel capitolo 5. Cloud e CI/CD operativa sono nel capitolo 7; sicurezza, IAM e incident response nei capitoli 8-9; data governance e interoperabilità semantica nel capitolo 10; SLA contrattuali e fornitori nel capitolo 12.

## Mappa BANDO dal requisito all’e-service

| Passaggio | Domanda da porsi | Azione |
| --- | --- | --- |
| **B — Bando** | Sono richiesti metodologie, testing, API, standard o piattaforme specifiche? | Separare il nucleo trasferibile dai dettagli di prodotto. |
| **A — Aree** | La domanda riguarda bisogno, progetto, test, contratto API o interoperabilità? | Collocare il problema nella fase e nel livello corretti. |
| **N — Nuclei** | Quali elementi devono restare verificabili ed evolvibili? | Collegare requisito, interfaccia, test, versione ed evidenza. |
| **D — Diario** | Quale assunzione ha prodotto un errore o una modifica incompatibile? | Registrare decisione, impatto, prova e correzione. |
| **O — Output** | Serve una risposta orale, un caso, una specifica o una matrice? | Produrre l’artefatto richiesto, non una lista di acronimi. |

## Dal bisogno ai requisiti verificabili

Un **bisogno** descrive il risultato atteso da un soggetto. Un **requisito** traduce quel bisogno in una proprietà o capacità che il sistema deve possedere. Un **vincolo** limita le soluzioni ammissibili: può derivare da norme, standard, tecnologie già presenti, tempi, budget o organizzazione. Il **criterio di accettazione** indica invece una condizione osservabile con cui stabilire se il requisito è soddisfatto.

Esempio: «ridurre le richieste di certificati già disponibili» è un bisogno. «Il servizio deve verificare, previa autorizzazione, il possesso del requisito anagrafico presso il sistema erogatore» è un requisito funzionale. «La risposta deve essere disponibile entro il tempo concordato e ogni richiesta deve essere tracciabile» introduce requisiti non funzionali. «Dato valido → esito coerente; dato inesistente → errore classificato; fruitore non abilitato → richiesta rifiutata» fornisce criteri verificabili.

### Requisiti funzionali e non funzionali

I **requisiti funzionali** descrivono comportamenti, dati elaborati e risultati. I **requisiti non funzionali** qualificano il servizio: prestazioni, disponibilità, usabilità, accessibilità, sicurezza, manutenibilità, portabilità e osservabilità.

I requisiti non funzionali hanno effetti concreti. Un servizio può restituire il dato corretto e risultare comunque inadeguato perché non regge il carico, esclude parte degli utenti o rende impossibile ricostruire gli errori.

Per essere utilizzabile, un requisito deve rispondere a un bisogno riconoscibile, evitare ambiguità e restare coerente con gli altri. Deve inoltre risultare realizzabile, verificabile e collegabile a progetto, test e rilascio.

### Tracciabilità

La tracciabilità consente di seguire un requisito lungo il ciclo di vita.

| Requisito | Componente o API | Criterio | Test | Evidenza |
| --- | --- | --- | --- | --- |
| verificare un requisito anagrafico | servizio di verifica | esito coerente per tre classi di input | integrazione e accettazione | report di esecuzione |
| registrare l’uso | componente di audit | evento presente e correlabile | sistema | evento con identificativo |

Se una modifica interessa il requisito, la matrice aiuta a individuare contratto, test e documentazione da aggiornare. Se un test non è collegato a nessuna promessa, può essere ridondante; se una promessa non ha test, manca un’evidenza.

## Ciclo di vita e organizzazione dello sviluppo

Il **ciclo di vita del software** comprende attività di concezione, analisi, progettazione, realizzazione, verifica, rilascio, esercizio, manutenzione e dismissione. Le attività possono sovrapporsi e ripetersi: la sequenza dipende da rischio, stabilità dei requisiti, dimensione, vincoli e capacità dell’organizzazione.

Un modello **sequenziale** rende esplicite fasi e approvazioni ed è utile quando requisiti e vincoli sono abbastanza stabili. Il limite emerge quando il feedback arriva tardi. Un modello **iterativo** rivede più volte la soluzione; uno **incrementale** consegna parti utilizzabili in passi successivi. Gli approcci Agile privilegiano feedback frequente, collaborazione e adattamento, ma non eliminano architettura, documentazione, controllo e responsabilità.

La scelta del modello dipende dalla capacità di produrre evidenze in tempo utile, governare i rischi e rispettare i vincoli del servizio. L’etichetta «Agile» o «tradizionale», da sola, dice poco.

### Ruoli e responsabilità

Il committente definisce obiettivi e vincoli insieme agli utenti e agli altri portatori d’interesse. Gli analisti precisano i requisiti; progettisti e sviluppatori costruiscono la soluzione, mentre i tester raccolgono le evidenze e operations gestisce l’esercizio. Un responsabile del prodotto o del servizio ordina priorità e accettazione. Anche quando un fornitore riunisce più ruoli, responsabilità e criteri decisionali devono restare espliciti.

### Configurazione e controllo di versione

La **gestione della configurazione** identifica gli elementi controllati — codice, specifiche, schemi, configurazioni, test e documenti — e ne governa le modifiche. Il **controllo di versione** conserva la storia e permette di associare uno stato a una release.

Nel modello distribuito diffuso da Git, un repository conserva oggetti e riferimenti; un commit registra uno stato; un branch rappresenta una linea di sviluppo; un merge integra storie divergenti; un tag identifica un punto significativo. Il repository non garantisce qualità: servono regole su revisione, test, approvazione, tracciabilità e ripristino. L’integrazione continua automatizza controlli frequenti; deployment e infrastruttura della pipeline appartengono al capitolo 7.

## Architettura e qualità del software

L’**architettura software** descrive elementi significativi, responsabilità, relazioni e decisioni che condizionano l’evoluzione del sistema. Un **componente** racchiude una responsabilità; un’**interfaccia** espone modalità di interazione; una **dipendenza** indica che un elemento necessita di un altro.

Alta **coesione** significa che le responsabilità di un componente sono correlate. Basso **accoppiamento** riduce le conoscenze e le dipendenze necessarie fra componenti. Non sono valori assoluti: l’obiettivo è evitare legami inutili e rendere visibili quelli inevitabili.

### Forme architetturali

Un sistema **monolitico** distribuisce insieme più funzioni. Può essere semplice da avviare e operare, ma una crescita disordinata rende più difficili modifiche e rilasci. Un’architettura **a livelli** separa responsabilità. Il modello **client-server** distingue richiedente ed erogatore. Un’architettura **a servizi** scompone capacità dietro contratti, aumentando l’autonomia potenziale ma anche esigenze di rete, osservabilità e governo.

Scala, competenze, vincoli, frequenza delle modifiche e qualità richieste determinano quale forma architetturale sia più adatta al caso.

### Attributi di qualità e trade-off

Fra gli attributi di qualità rientrano affidabilità, prestazioni, usabilità, accessibilità, sicurezza e manutenibilità. Portabilità, interoperabilità e osservabilità diventano decisive quando il sistema deve integrarsi ed evolvere. Ogni scelta comporta un costo: molti servizi acquistano autonomia ma introducono comunicazioni remote e gestione distribuita; una cache riduce la latenza ma richiede una politica di coerenza. Il progetto deve dichiarare il compromesso adottato.

## Verifica, validazione e test

La **verifica** controlla che il prodotto sia costruito secondo specifiche e progetto. La **validazione** controlla che il prodotto risponda al bisogno d’uso.

| Livello | Oggetto | Esempio |
| --- | --- | --- |
| unitario | funzione o componente isolato | calcolo di una regola |
| integrazione | interazione fra elementi | chiamata fra servizio e database |
| sistema | comportamento complessivo | flusso end-to-end |
| accettazione | criteri concordati con stakeholder | esito del caso amministrativo |
| regressione | funzioni già valide dopo una modifica | suite rieseguita su nuova release |

Un **caso di test** specifica identificativo, obiettivo, precondizioni, dati di ingresso, passi, risultato atteso e risultato ottenuto. Un **difetto** è una carenza nel prodotto o in un artefatto; una **failure** è il comportamento osservato che non soddisfa il risultato atteso. Gravità e priorità non coincidono: la prima misura l’impatto, la seconda ordina l’intervento.

## API come contratto

Un’**API** definisce come un sistema può richiedere capacità o dati a un altro. Il contratto comprende operazioni, indirizzamento, parametri, rappresentazioni, precondizioni, risposte, errori e vincoli di utilizzo. L’implementazione interna può cambiare senza rompere i fruitori finché il comportamento promesso resta compatibile.

Un’interazione **sincrona** attende una risposta nel contesto della richiesta. In un’interazione **asincrona**, richiesta ed elaborazione o notifica possono essere separate nel tempo. Eventi e messaggi sono utili quando il produttore non deve attendere il completamento immediato, ma richiedono gestione di duplicati, ordine, errori e correlazione.

### REST, SOAP e rappresentazioni

REST è uno stile architetturale; nelle API HTTP orienta l’uso di risorse, identificatori, rappresentazioni e semantica del protocollo. SOAP è un protocollo di messaggistica basato su XML. Dire «REST usa JSON, SOAP usa XML» è incompleto: JSON è frequente nelle API REST, ma non definisce REST; SOAP possiede regole proprie oltre al formato XML.

In una API HTTP, l’URI identifica la risorsa o il punto di interazione; il metodo esprime la semantica; gli header trasportano metadati; il corpo contiene una rappresentazione quando prevista; il codice di stato descrive la classe di esito; lo schema definisce struttura e vincoli.

`GET` recupera una rappresentazione senza richiedere una modifica dello stato; `POST` invia dati per un’elaborazione; `PUT` sostituisce o crea lo stato della risorsa identificata secondo il contratto; `PATCH` applica una modifica parziale; `DELETE` richiede la rimozione.

L’**idempotenza** riguarda l’effetto intenzionale di più richieste uguali: ripeterle produce lo stesso effetto previsto sul server della singola richiesta. Non significa che ogni risposta debba essere identica né che l’operazione sia priva di effetti interni, come il logging.

### Errori e descrizione formale

La risposta di errore deve permettere al fruitore di capire la classe del problema, correlare l’evento e decidere se correggere la richiesta o riprovarla. Input non valido, risorsa assente, autorizzazione mancante, conflitto e indisponibilità non possono confluire tutti in un generico errore interno.

Una descrizione **OpenAPI** rappresenta in modo indipendente dal linguaggio la superficie di un’API HTTP: percorsi, operazioni, parametri, corpi, risposte, schemi e requisiti di sicurezza descritti. Può alimentare documentazione, test e strumenti, ma non implementa da sola il comportamento e non prova che il servizio rispetti il contratto.

## Evoluzione e gestione delle API

Una modifica è **compatibile** quando i fruitori conformi al contratto precedente possono continuare a funzionare. Aggiungere un campo opzionale può essere compatibile se i client ignorano elementi sconosciuti; rinominare un campo obbligatorio o cambiarne il tipo può rompere il contratto.

Il **versionamento** rende distinguibili contratti o comportamenti. La **deprecazione** annuncia che un elemento resta temporaneamente disponibile ma sarà sostituito; richiede documentazione, transizione e percorso di migrazione. Versione dell’API, versione dell’implementazione e versione della specifica OpenAPI sono concetti distinti.

### Requisiti operativi e API management

Un contratto utile specifica limiti di dimensione, paginazione e filtri; timeout e retry; throttling; disponibilità e latenza attese; identificativi di correlazione; metriche, log e canale per modifiche e incidenti.

Uno **SLO** esprime un obiettivo misurabile di servizio; uno **SLA** formalizza impegni e conseguenze nel rapporto fra parti. Il capitolo 12 affronta il profilo contrattuale.

L’API management comprende catalogazione, pubblicazione, controllo degli accessi, politiche di utilizzo, versioni, documentazione, misurazione e dismissione. Un gateway può applicare alcune politiche, ma non sostituisce governance, qualità del contratto o autorizzazione applicativa.

## Interoperabilità ed e-service nella PA

L’interoperabilità consente a organizzazioni e sistemi differenti di scambiare informazioni e usarle correttamente. Può essere letta sui livelli **giuridico**, **organizzativo**, **semantico** e **tecnico**.

Una API tecnicamente funzionante non risolve da sola gli altri livelli. Due enti possono scambiare un campo chiamato `stato` ma attribuirgli significati diversi; oppure condividere il significato ma non avere finalità e responsabilità definite.

### ModI, PDND ed e-service

Il Modello di interoperabilità della PA organizza tecnologie, pattern di interazione e sicurezza, profili e regole di governance. Le fonti AgID richiamano API documentate ed evolvibili, catalogazione, tracciabilità, limitazioni d’uso e livelli di servizio.

Nel contesto PDND, un **erogatore** rende disponibile una capacità; un **fruitore** ne richiede l’uso. L’**e-service** descrive il servizio disponibile nel catalogo e collega l’offerta alle API e alle condizioni di fruizione. La **finalità** esplicita lo scopo dell’accesso. Versioni, richieste di fruizione, attributi, accordi e meccanismi tecnici devono essere verificati sulla documentazione vigente prima di configurare un caso reale.

Il principio **once only** orienta a non chiedere nuovamente a cittadini e imprese informazioni già legittimamente disponibili. Non autorizza accessi indiscriminati: finalità, minimizzazione, responsabilità, autorizzazioni e tracciabilità restano requisiti del servizio.

Il Regolamento (UE) 2024/903 inquadra l’interoperabilità del settore pubblico a livello europeo. Per una prova generale conta cogliere la continuità fra dimensione tecnica, organizzativa, semantica e giuridica; obblighi e applicazioni puntuali richiedono verifica normativa aggiornata.

## Caso guidato: verifica di un requisito anagrafico

Un’amministrazione fruitrice deve verificare un requisito anagrafico durante l’istruttoria di una pratica. L’amministrazione erogatrice possiede il dato autorevole.

1. **Finalità:** usare il dato solo per l’istruttoria prevista.
2. **Dato minimo:** ottenere un esito, non l’intero profilo anagrafico.
3. **Requisito funzionale:** inviare l’identificativo previsto e ricevere esito, data e riferimento correlabile.
4. **Requisiti non funzionali:** tracciare la richiesta, rispettare il livello di servizio e classificare gli errori.
5. **Contratto:** definire input, output, errori, schema e versione.
6. **Autorizzazione:** consentire la fruizione secondo ruoli, finalità e condizioni applicabili.
7. **Test:** verificare esito positivo, requisito assente, input non valido, fruitore non abilitato e indisponibilità.
8. **Evidenza:** correlare richiesta, risposta, versione ed esito del test.

Restituire un esito invece dell’intero record riduce dati e accoppiamento. Se il significato dell’esito cambia, contratto, documentazione e test devono evolvere insieme.

## Laboratorio: disegno essenziale di un’API

| Campo | Decisione |
| --- | --- |
| bisogno | quale risultato amministrativo serve? |
| erogatore e fruitore | chi possiede la capacità e chi la usa? |
| finalità | perché lo scambio è necessario? |
| operazione | quale capacità viene richiesta? |
| input minimo | quali dati sono indispensabili? |
| output | quale esito è utile e comprensibile? |
| errori | quali condizioni deve distinguere il fruitore? |
| idempotenza | cosa accade in caso di retry? |
| versione | quali modifiche sarebbero incompatibili? |
| qualità | quali obiettivi e metriche servono? |
| evidenze | come si correlano richieste, test e anomalie? |

Un possibile contratto concettuale è `POST /verifiche-requisito`. La risposta non deve essere inventata a partire dalla tecnologia: va derivata dal bisogno, dallo schema condiviso e dalle condizioni di trattamento.

## Domanda da commissario

**Come passa da un requisito a un e-service interoperabile?**

Inizio dal bisogno e chiarisco stakeholder, finalità e vincoli. Traduco il requisito in criteri di accettazione, poi progetto componenti, contratto API, errori e requisiti di qualità. I test devono fornire evidenza per ogni promessa. Nel caso di un e-service individuo anche erogatore, fruitore, dati minimi, condizioni di fruizione e livelli di servizio; versione, documentazione e osservabilità ne accompagnano l’evoluzione.

## Domanda-trappola

**Un’API pubblicata è automaticamente accessibile a chiunque?**

No. Pubblicare o catalogare una descrizione rende conoscibile il contratto secondo le regole del contesto, ma non elimina autenticazione, autorizzazione, finalità, protezione dei dati o condizioni di fruizione. Interoperabilità e open data non sono sinonimi.

## Errore tipico

Disegnare subito endpoint e payload. La struttura tecnica finisce così per nascondere decisioni su finalità, significato, errori e qualità. Conviene partire dal bisogno e dal contratto osservabile; soltanto dopo si sceglie la rappresentazione.

## Mini-esercizi e quiz

### Esercizio 1 — Requisito e test

Trasforma «il servizio deve essere veloce» in un requisito verificabile.

**Soluzione:** definire operazione, carico, indicatore, valore obiettivo e finestra di misurazione. Senza questi elementi, «veloce» non produce un criterio di accettazione.

### Esercizio 2 — Compatibilità

Un campo obbligatorio `esito` viene rinominato `risultato`. La modifica è compatibile?

**Soluzione:** in generale no per i fruitori che cercano `esito`. Occorre mantenere il campo durante una transizione, introdurre una nuova versione o concordare una migrazione verificabile.

### Esercizio 3 — Caso e-service

Elenca cinque elementi da chiarire prima della fruizione.

**Soluzione:** erogatore, fruitore, finalità, dato o capacità minima, condizioni di accesso; vanno inoltre definiti contratto, errori, livelli di servizio ed evidenze.

### Quiz

Quale affermazione è corretta?

- A. Validazione e verifica sono sempre sinonimi.
- B. OpenAPI implementa automaticamente il servizio descritto.
- C. Un test di regressione controlla funzioni già valide dopo una modifica.
- D. Interoperabilità significa rendere ogni dato pubblico.

**Risposta corretta: C.** A confonde adeguatezza allo scopo e conformità; B attribuisce alla descrizione il comportamento dell’implementazione; D confonde scambio governato e open data.

## Checklist finale

| Competenza | Riconosco | Spiego | Applico |
| --- | --- | --- | --- |
| Distinguere bisogno, requisito, vincolo e criterio | ☐ | ☐ | ☐ |
| Collegare requisito, progetto, test ed evidenza | ☐ | ☐ | ☐ |
| Confrontare modelli di ciclo di vita | ☐ | ☐ | ☐ |
| Leggere componenti, interfacce e dipendenze | ☐ | ☐ | ☐ |
| Distinguere verifica, validazione e livelli di test | ☐ | ☐ | ☐ |
| Spiegare configurazione e controllo di versione | ☐ | ☐ | ☐ |
| Progettare il contratto essenziale di un’API | ☐ | ☐ | ☐ |
| Valutare compatibilità, errori e idempotenza | ☐ | ☐ | ☐ |
| Distinguere i livelli di interoperabilità | ☐ | ☐ | ☐ |
| Costruire un caso e-service | ☐ | ☐ | ☐ |

## Da sapere in 5 righe

- Il ciclo di vita collega bisogno, requisiti, progetto, test, rilascio ed evoluzione.
- Architettura e qualità si valutano attraverso trade-off espliciti.
- Un’API è un contratto: operazioni, dati, errori, vincoli e livelli di servizio.
- Interoperabilità tecnica, semantica, organizzativa e giuridica devono convergere.
- Un e-service richiede erogatore, fruitore, finalità, condizioni, evidenze e governo delle modifiche.

## Riferimenti consolidati

- [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali]], capitolo 10, § 16;
- [[topics/open-data-interoperabilita-cloud-pa]];
- [[topics/pa-digitale]];
- [[sources/ingegneria-software-api-interoperabilita-fonti-tecniche]];
- [[sources/pa-digitale-cad-identita-documenti-servizi-dati]];
- [[sources/d-lgs-7-marzo-2005-n-82-amministrazione-digitale]];
- [[sources/agid-piano-triennale-informatica-pa-2024-2026-aggiornamento-2026]];
- [[sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27]];
- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]].

## Note di review

- Verificare requisiti, architetture e attributi di qualità con un software architect.
- Verificare livelli di test, casi ed evidenze con un QA/test engineer.
- Validare esempi HTTP, compatibilità, idempotenza e OpenAPI con un API designer.
- Ricontrollare terminologia, ruoli e processo logico ModI/PDND sulle versioni vigenti prima del text freeze.
- Verificare finalità, minimizzazione e condizioni di fruizione con esperto privacy e diritto digitale.
- Validare su bandi ufficiali metodologie, standard, linguaggi, framework e piattaforme richiesti.
- Mantenere CI/CD operativa, cybersecurity, IAM, data governance e procurement nei capitoli dedicati.
- Verificare nel renderer KDP tabelle, stringhe tecniche e caselle della checklist.