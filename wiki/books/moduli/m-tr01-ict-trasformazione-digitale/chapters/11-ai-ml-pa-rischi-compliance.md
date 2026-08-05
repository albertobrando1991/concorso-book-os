---
id: chapter-m-tr01-11
type: book_chapter
title: "AI/ML nella PA: modelli, rischi e compliance"
status: reviewed-draft
domain: "concorsi pubblici italiani"
topics: ["intelligenza artificiale", "machine learning", "governance AI", "rischio algoritmico", "AI Act"]
entities: ["Unione europea", "Commissione europea", "AI Office", "AgID", "NIST"]
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/ai-ml-governance-rischi-compliance-fonti-primarie", "sources/legge-23-settembre-2025-n-132-intelligenza-artificiale", "sources/basi-dati-sql-nosql-qualita-fonti-tecniche", "sources/ingegneria-software-api-interoperabilita-fonti-tecniche", "sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie", "sources/data-governance-open-data-interoperabilita-fonti-primarie"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "vol-08-ict-digitale-cybersecurity-dati"]
confidence: 0.88
updated_at: 2026-08-05
created_at: 2026-07-28
review_required: true
canonical: true
tags: ["chapter", "m-tr01", "ai", "machine-learning", "ai-act"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 11
draft_stage: cross-reviewed
last_compiled_from: ["sources/ai-ml-governance-rischi-compliance-fonti-primarie", "topics/intelligenza-artificiale-machine-learning-governance-pa", "planning/08-capitolo-11-piano-completamento"]
---

# AI/ML nella PA: modelli, rischi e compliance

Assegnare automaticamente una priorità alle segnalazioni dei cittadini può accorciare i tempi di lavorazione. Lo stesso sistema, però, può riprodurre errori storici, penalizzare alcune zone o spingere l'operatore a fidarsi di un punteggio che non comprende. La domanda corretta non è soltanto «quanto è accurato il modello?», ma «per quale decisione viene usato, con quali dati, rischi, controlli e responsabilità?».

Nella PA, l'intelligenza artificiale va considerata come un sistema sociotecnico: il risultato dipende dal modello e dai dati, ma anche dal software, dalle persone, dal procedimento e dall'organizzazione. Il suo governo richiede quindi competenze tecniche e amministrative.

## Obiettivo e confini

Il capitolo permette di:

- distinguere automazione, algoritmo, AI, machine learning e generative AI;
- comprendere addestramento, inferenza, dati e principali metriche;
- riconoscere overfitting, leakage, bias e drift;
- distinguere accuratezza, equità, spiegabilità e trasparenza;
- progettare un controllo umano effettivo;
- impostare ciclo di vita, griglia di rischio ed evidenze;
- orientarsi nel quadro UE e italiano senza confondere classificazione giuridica e rischio tecnico.

Algoritmi generali e complessità sono nel capitolo 3; dati e qualità nel capitolo 4; sviluppo e test nel capitolo 6; rischio e sicurezza nei capitoli 8-9; data governance nel capitolo 10. Qui quei concetti sono applicati ai sistemi AI.

## Mappa BANDO del sistema AI

- **B — Bisogno:** problema, finalità, destinatari e baseline.
- **A — Attori:** owner del caso d'uso, tecnici, operatori, controllori e fornitore.
- **N — Nodi:** dati, errori, bias, sicurezza, diritti, drift e uso improprio.
- **D — Documenti:** scheda del caso, datasheet, model card, test, log e valutazioni.
- **O — Output:** previsione, raccomandazione o contenuto, sempre inseriti in un processo governato.

## Dall'automazione al machine learning

### Algoritmo, sistema AI e modello

Un'**automazione deterministica** applica regole esplicite: a parità di input e regole produce lo stesso risultato. Un **algoritmo** è una procedura finita per risolvere un problema. Nel **machine learning**, invece, un modello apprende relazioni dai dati anziché ricevere tutte le regole già formulate.

Il modello non coincide con l'intero sistema AI. Il sistema comprende interfacce, dati, infrastruttura, persone, istruzioni, controlli e processo nel quale l'output viene usato.

### Addestramento e inferenza

Durante l'**addestramento** il sistema modifica i parametri del modello per ridurre un errore rispetto agli esempi. Durante l'**inferenza** applica il modello appreso a nuovi input. Una buona prestazione sui dati di addestramento non basta a dimostrare che il modello funzioni su casi nuovi.

Le **feature** sono caratteristiche usate come input; la **label** è il valore-obiettivo nei problemi supervisionati. Un parametro viene appreso dal modello; un iperparametro è scelto nel processo di configurazione.

### Predittivo, raccomandativo e generativo

Un sistema predittivo stima una classe o un valore. Un raccomandatore ordina opzioni. Un sistema generativo produce testo, immagini, audio o altro contenuto. L'output generativo può essere plausibile e tuttavia falso: non è, per ciò solo, una fonte.

## Paradigmi di apprendimento

### Supervisionato e non supervisionato

Nell'**apprendimento supervisionato** gli esempi contengono input e risultato atteso. La classificazione assegna una categoria; la regressione stima un valore. Nell'**apprendimento non supervisionato** mancano label-obiettivo e il metodo cerca strutture, per esempio gruppi di osservazioni simili.

L'**apprendimento per rinforzo** usa ricompense e penalità per apprendere una strategia di azione. Nel manuale basta riconoscerne la logica: non è una variante della classificazione supervisionata.

### Train, validation e test

Il dataset di **training** serve ad apprendere i parametri. Quello di **validation** sostiene scelte e regolazioni. Il **test set** fornisce una stima finale su dati non usati nelle scelte precedenti. Se lo si usa più volte per migliorare il modello, il test set finisce per diventare un altro validation set.

L'**overfitting** si verifica quando il modello aderisce troppo ai dati di training e generalizza male. L'**underfitting** indica un modello troppo semplice o non adeguatamente addestrato. Il **data leakage** porta nel processo informazioni che non sarebbero disponibili al momento reale della previsione o contamina le partizioni.

## Dati per l'AI

### Provenienza, qualità ed etichette

Un dataset utile deve avere provenienza, finalità, periodo, popolazione e trasformazioni documentati. Le etichette possono contenere errori o giudizi storici: se «urgenza» deriva dalla priorità assegnata in passato, il modello può apprendere prassi incoerenti.

L'assenza di valori mancanti, da sola, non garantisce la qualità. Bisogna valutare anche rappresentatività, tempestività, copertura dei casi rari, coerenza e adeguatezza all'uso.

### Classi, proxy e minimizzazione

Una classe minoritaria può essere quasi ignorata da un modello che ottiene comunque un'accuracy elevata. Una variabile apparentemente neutra può agire da **proxy** di una caratteristica sensibile. Eliminare il campo sensibile, quindi, non elimina automaticamente il rischio di disparità.

Si raccolgono i dati necessari alla finalità e si applicano classificazione, accessi, conservazione e sicurezza. Per inventario, lineage e regole di qualità si rinvia al capitolo 10.

## Valutare un modello

### Baseline e matrice di confusione

Prima di valutare il modello bisogna fissare una **baseline**: può essere una regola semplice, il processo attuale o una prestazione minima da superare. Senza questo confronto, un numero isolato non chiarisce se la soluzione apporti valore.

Per una classificazione binaria:

| Esito | Significato |
| --- | --- |
| vero positivo | caso positivo riconosciuto |
| falso positivo | caso negativo classificato positivo |
| falso negativo | caso positivo non riconosciuto |
| vero negativo | caso negativo riconosciuto |

Le conseguenze dipendono dal processo. Una segnalazione urgente classificata non urgente produce un falso negativo; una segnalazione ordinaria classificata urgente produce un falso positivo.

### Accuracy, precision, recall e F1

- **accuracy:** quota complessiva di classificazioni corrette;
- **precision:** tra i casi indicati come positivi, quota realmente positiva;
- **recall:** tra i casi realmente positivi, quota riconosciuta;
- **F1:** media armonica di precision e recall.

La metrica si sceglie in base al costo dell'errore. Se perdere un caso urgente è molto grave, il recall diventa centrale; aumentarlo può però far crescere i falsi positivi. La soglia decisionale è quindi una scelta di processo, non un dettaglio puramente matematico.

### Oltre la media

Il controllo delle prestazioni deve distinguere anche periodi, territori e gruppi pertinenti. La **calibrazione** riguarda la corrispondenza tra probabilità stimate e frequenze osservate. La robustezza misura la tenuta a variazioni e perturbazioni. Nessuna singola metrica dimostra utilità, equità o conformità.

## Bias, fairness e spiegabilità

### Dove nasce il bias

Il bias può derivare dal campionamento, dalle etichette, dalle feature, dall'obiettivo ottimizzato o dal modo in cui l'output entra nel processo. Correggere il modello non basta se il problema è nella procedura o nell'accesso al servizio.

Una disparità osservata richiede analisi tecnica e giuridica. Le metriche di fairness possono essere incompatibili tra loro e dipendono dal contesto: non esiste un indicatore universale che certifichi l'equità.

### Interpretazione e spiegazione

L'**interpretabilità globale** aiuta a capire il comportamento generale; una **spiegazione locale** riguarda un singolo output. La trasparenza comprende anche finalità, dati, limiti, ruolo del sistema e canali di contestazione.

Una spiegazione post-hoc può essere utile ma non prova che il modello sia corretto. **Errore tipico:** confondere una spiegazione convincente con una giustificazione valida della decisione.

## Controllo umano

Human-in-the-loop indica un intervento umano nel flusso; human-on-the-loop una supervisione; human-in-command il governo complessivo del sistema. Queste etichette descrivono il modello di supervisione, ma contano soprattutto le condizioni in cui l'operatore lavora.

Il controllo è effettivo se la persona:

- comprende scopo e limiti;
- riceve informazioni utili;
- dispone di tempo e competenza;
- può discostarsi dall'output;
- può sospendere o segnalare anomalie;
- motiva e traccia la decisione quando necessario.

L'**automation bias** porta a privilegiare la raccomandazione automatica anche contro altri elementi. Un pulsante «approva» non crea controllo umano se l'operatore non ha strumenti o autorità per contestare.

## Ciclo di vita e MLOps

MLOps porta nel ciclo del modello le pratiche dell'ingegneria e delle operations. Il gruppo di lavoro deve versionare dati, codice, configurazioni e modello, documentare test e approvazioni, controllare il rilascio e predisporre il rollback.

Il **data drift** è un cambiamento nella distribuzione degli input. Il **concept drift** riguarda il mutamento della relazione fra input e risultato. Anche senza drift, le prestazioni possono deteriorarsi per cambiamenti organizzativi.

Il monitoraggio include qualità degli input, metriche, sottogruppi, override umani, reclami, incidenti e usi fuori perimetro. Quando emerge un problema, l'ente può analizzarne le cause, correggere i dati, ripetere la validazione, riaddestrare il modello o modificare la soglia. Nei casi più seri può sospendere il sistema, eseguire il rollback o dismetterlo.

## Rischio e governance nella PA

### Inventario, ruoli ed evidenze

L'ente censisce casi d'uso e sistemi, inclusi servizi acquistati. L'owner del caso definisce finalità e accettazione; le funzioni tecniche curano modello e piattaforma; data steward, sicurezza, DPO, responsabile del procedimento e procurement intervengono per competenza.

Le evidenze comprendono scheda del caso, provenienza dei dati, test, valutazione del rischio, istruzioni, log, incidenti, versioni e riesami.

### Valutazione del rischio

La valutazione considera gli effetti su persone e diritti, oltre alle conseguenze per servizio, finanze, sicurezza e reputazione. Per ogni scenario si descrivono causa, evento, conseguenza, probabilità, gravità, controlli e rischio residuo. Vanno considerati uso previsto, uso improprio prevedibile, dipendenze e reversibilità.

La classificazione giuridica prevista dall'AI Act non coincide con una generica matrice probabilità-impatto: entrambe sono necessarie, ma rispondono a domande diverse.

### Fornitori

L'acquisto di un servizio non libera l'ente dalle proprie responsabilità. Contratto e SLA devono disciplinare dati, versioni, prestazioni, sicurezza, audit, incidenti, subfornitori, modifiche, uscita e restituzione delle evidenze. Il capitolo 12 sviluppa procurement e gestione del fornitore.

## Quadro UE e italiano

Il regolamento (UE) 2024/1689 adotta un approccio basato sul rischio e distingue pratiche vietate, sistemi ad alto rischio, obblighi di trasparenza e modelli per finalità generali. La categoria non dipende dal fatto che il prodotto «usi AI», ma da definizioni, uso previsto, contesto e ruolo dell'operatore.

Per i sistemi ad alto rischio, il quadro comprende gestione del rischio, governance dei dati, documentazione, registrazione, informazioni al deployer, sorveglianza umana, accuratezza, robustezza e cybersicurezza. Specifici sistemi hanno obblighi di trasparenza. Provider e deployer hanno funzioni diverse.

Il calendario applicativo è progressivo ed è stato interessato da modifiche recenti. Prima di indicare una scadenza, quindi, occorre controllare il testo consolidato e gli atti modificativi, senza affidarsi alla memoria.

La legge 23 settembre 2025, n. 132 reca principi e deleghe nazionali e si interpreta in conformità all'AI Act. La Strategia italiana 2024-2026 organizza azioni su ricerca, PA, imprese e formazione, ma non crea da sola obblighi. GDPR, procedimento, trasparenza e cybersecurity continuano ad applicarsi secondo i rispettivi presupposti.

Il NIST AI RMF 1.0 organizza il lavoro in Govern, Map, Measure e Manage. È un riferimento volontario, non una norma UE.

## Caso guidato: priorità delle segnalazioni

Un comune valuta un modello che assegna priorità alle segnalazioni di manutenzione.

1. **Bisogno:** ridurre i tempi sui casi urgenti; baseline: processo attuale.
2. **Dati:** storico delle segnalazioni, esiti e tempi; si documentano provenienza, periodo, etichette e zone poco rappresentate.
3. **Errore:** un falso negativo ritarda un'urgenza; un falso positivo occupa risorse.
4. **Valutazione:** recall degli urgenti, precision, test temporale e per territorio; soglia motivata.
5. **Controllo umano:** l'operatore vede motivi e dati, può cambiare priorità e segnala anomalie.
6. **Rischio:** si valutano effetti, proxy territoriali, sicurezza, contestazione e uso improprio.
7. **Esercizio:** modello e dati hanno versioni; input, output, override e motivi sono tracciati.
8. **Monitoraggio:** si controllano drift, errori, reclami e carico; sono previsti rollback e sospensione.

La classificazione AI Act deve essere verificata sul caso e sul testo vigente: la griglia non la produce automaticamente.

## Microcaso generativo

Un ufficio usa un modello generativo per preparare una bozza di risposta. L'operatore non inserisce dati non autorizzati, verifica fatti e fonti, corregge il testo e approva l'invio. Prompt, strumenti, accessi e conservazione sono governati. Solo la validazione prevista dal processo autorizzato può trasformare l'output in un atto dell'ente.

## Laboratorio: griglia di rischio

| Dimensione | Domanda | Evidenza | Controllo |
| --- | --- | --- | --- |
| finalità | quale decisione supporta? | scheda caso | limite d'uso |
| dati | sono adeguati e documentati? | datasheet | test qualità |
| prestazioni | quali errori produce? | report metriche | soglia e baseline |
| persone | chi può subire effetti? | mappa stakeholder | riesame |
| controllo | l'operatore può intervenire? | log override | escalation |
| esercizio | come rileviamo degrado? | dashboard | rollback |

Una model card essenziale riporta versione, uso previsto, usi esclusi, dati, metriche, limiti, controllo umano, monitoraggio e responsabili.

## Domanda da commissario

**Come governeresti un modello usato per dare priorità alle segnalazioni comunali?**

Partirei da finalità e baseline, documenterei dati ed etichette, separerei training, validation e test, sceglierei metriche in base al costo degli errori e verificherei sottogruppi e robustezza. Progetterei controllo umano, logging, versioni, monitoraggio e rollback. Valuterei rischi e classificazione AI Act sul caso concreto, coinvolgendo competenze tecniche, amministrative, privacy, sicurezza e procurement.

## Domande-trappola

- **Accuracy elevata significa equità?** No: può nascondere errori su classi o gruppi.
- **Un modello spiegabile è corretto?** No: la spiegazione non prova accuratezza o liceità.
- **Controllo umano significa approvare l'output?** No: servono comprensione e potere d'intervento.
- **Dati storici eliminano il bias?** No: possono incorporare errori e disparità pregresse.
- **Un output plausibile è una fonte?** No: fatti e riferimenti vanno verificati.
- **Il fornitore assume ogni responsabilità?** No: ruoli e obblighi dipendono dal caso e dal contratto.

## Mini-esercizi e soluzioni

**1.** Un modello riconosce 90 pratiche urgenti su 100. Qual è il recall?
**Soluzione:** 90%; servono altri dati per calcolare precision e accuracy.

**2.** La data di chiusura della pratica è usata per prevedere, all'apertura, se sarà chiusa in ritardo. Qual è il problema?
**Soluzione:** leakage, perché l'informazione non è disponibile al momento reale della previsione.

**3.** Dopo una nuova procedura cambiano tempi ed etichette. Che cosa controllare?
**Soluzione:** data e concept drift, prestazioni, soglia e validità del modello.

**4.** Un operatore non può modificare il punteggio. È controllo umano?
**Soluzione:** non effettivo; mancano autorità e possibilità di override o escalation.

## Checklist finale

- [ ] Problema, finalità, baseline e usi esclusi sono definiti.
- [ ] Dati, etichette, provenienza e partizioni sono documentati.
- [ ] Metriche e soglie riflettono le conseguenze degli errori.
- [ ] Bias, sottogruppi, robustezza e sicurezza sono verificati.
- [ ] Il controllo umano è competente, informato e dotato di autorità.
- [ ] Dati, codice, modello e decisioni sono versionati e tracciati.
- [ ] Drift, incidenti, reclami, rollback e dismissione sono governati.
- [ ] Classificazione normativa e ruolo dell'ente sono verificati.
- [ ] Fornitori e dipendenze sono inclusi nella governance.

## Da sapere in 5 righe

Il modello è solo una parte del sistema AI.
La prestazione si valuta su dati separati e con metriche legate al costo dell'errore.
Accuratezza, fairness, spiegabilità e conformità non sono sinonimi.
Il controllo umano richiede competenza, informazioni e potere d'intervento.
Rischio, versioni, drift e obblighi si governano per tutto il ciclo di vita.

## Riferimenti consolidati

- [[sources/ai-ml-governance-rischi-compliance-fonti-primarie]]
- [[sources/legge-23-settembre-2025-n-132-intelligenza-artificiale]]
- [[sources/basi-dati-sql-nosql-qualita-fonti-tecniche]]
- [[sources/ingegneria-software-api-interoperabilita-fonti-tecniche]]
- [[sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie]]
- [[sources/data-governance-open-data-interoperabilita-fonti-primarie]]
- [[topics/intelligenza-artificiale-machine-learning-governance-pa]]

## Note di review

Prima del text freeze verificare il testo consolidato dell'AI Act, gli atti modificativi, il calendario applicativo e le linee guida definitive. La legge n. 132/2025 richiede review articolo per articolo prima di aggiungere obblighi nazionali puntuali. Data scientist, responsible AI specialist, giurista, DPO, security architect e responsabile PA devono validare metriche, bias, controllo umano, caso e griglia. Le tabelle vanno provate nel formato KDP.
