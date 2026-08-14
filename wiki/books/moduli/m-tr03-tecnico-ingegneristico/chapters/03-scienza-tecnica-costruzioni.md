---
id: chapter-m-tr03-03-scienza-tecnica-costruzioni
type: book_chapter
title: "Scienza e tecnica delle costruzioni per concorsi"
status: draft
domain: "ingegneria strutturale"
topics: ["scienza delle costruzioni", "statica", "meccanica dei solidi", "resistenza dei materiali"]
entities: ["Sapienza Università di Roma", "Università di Napoli Federico II", "Politecnico di Milano", "Università di Bologna"]
source_refs: ["sources/scienza-tecnica-costruzioni-fonti-universitarie", "sources/campione-bandi-tecnici-pa-vol-10-2026", "sources/modulo-m-tr03-tecnico-ingegneristico-vol-10"]
book_refs: ["m-tr03-tecnico-ingegneristico", "vol-10-tecnico-ingegneristico-territorio-lavori-pubblici"]
confidence: 0.76
updated_at: 2026-07-29
created_at: 2026-07-29
review_required: false
canonical: true
tags: ["book-chapter", "m-tr03", "vol-10", "structural-mechanics"]
book_id: m-tr03-tecnico-ingegneristico
outline_section: 3
draft_stage: specialist-audited
module_code: M-TR03
module_family: trasversali
last_compiled_from: ["wiki/books/moduli/m-tr03-tecnico-ingegneristico/planning/08-capitolo-03-piano-completamento.md", "wiki/books/moduli/m-tr03-tecnico-ingegneristico/planning/02-matrice-copertura-didattica.md", "wiki/sources/scienza-tecnica-costruzioni-fonti-universitarie.md", "wiki/topics/scienza-tecnica-costruzioni.md"]
---

# Scienza e tecnica delle costruzioni per concorsi

Davanti a uno schema strutturale viene spontaneo cercare subito una formula. Conviene fermarsi un momento e chiarire il problema: qual è il sistema resistente? Come è vincolato? Quali azioni riceve? Quale comportamento sto assumendo? Che cosa devo determinare o verificare?

La scienza delle costruzioni fornisce i modelli con cui descrivere equilibrio, spostamenti, deformazioni, sollecitazioni e tensioni. La tecnica delle costruzioni usa questi strumenti per progettare e verificare opere ed elementi reali, nel quadro delle regole applicabili. Nei concorsi le due prospettive spesso convivono: occorre comprendere il principio e saperlo collegare alla decisione tecnica.

Questo capitolo costruisce il lessico e il ragionamento di base. Le prescrizioni delle Norme Tecniche per le Costruzioni, la sismica e la geotecnica sono trattate nel capitolo 4.

## Obiettivo

Al termine del capitolo saprai:

- passare da una struttura reale a uno schema ragionato;
- distinguere cinematica, statica e risposta del materiale;
- riconoscere azioni, vincoli, reazioni e sollecitazioni;
- spiegare il significato di tensione e deformazione;
- distinguere resistenza, rigidezza, stabilità, duttilità e durabilità;
- impostare una risposta orale senza nasconderti dietro formule isolate.

L'output è una checklist `ipotesi–modello–azione–risposta–verifica`, utilizzabile nei quiz, negli orali e nei casi qualitativi.

## La Mappa BANDO del problema strutturale

| Passaggio | Domanda | Risultato |
| --- | --- | --- |
| **B — Bando** | Il programma richiede statica, scienza o tecnica delle costruzioni? | profondità e tipo di prova |
| **A — Aree** | Il quesito riguarda modello, azioni, materiale o verifica? | perimetro del problema |
| **N — Nuclei** | Quali grandezze e distinzioni devo usare? | schema del ragionamento |
| **D — Diario** | Ho sbagliato ipotesi, vincoli, segni o significato fisico? | errore classificato |
| **O — Output** | Devo riconoscere, calcolare, tracciare o spiegare? | forma della risposta |

La stessa materia cambia volto nella prova. Un quiz può chiedere una distinzione; uno scritto può richiedere uno schema di calcolo; l'orale può valutare la capacità di spiegare perché un modello è adatto.

## Dalla struttura reale al modello

Una struttura reale ha geometria, materiali, collegamenti, difetti, storia costruttiva e condizioni d'uso. Il modello ne rappresenta gli aspetti rilevanti per il problema studiato. Non è una copia ridotta dell'opera: è una scelta tecnica.

Per costruirlo servono almeno:

- geometria e dimensioni significative;
- elementi resistenti;
- vincoli e collegamenti;
- azioni esterne;
- proprietà dei materiali;
- ipotesi sul comportamento;
- grandezze da determinare.

Un impalcato può essere rappresentato mediante travi, piastre o modelli più complessi. La scelta dipende dallo scopo, dai dati disponibili e dalla precisione necessaria. Aggiungere dettagli non migliora di per sé il modello: ciò che conta è la coerenza con il problema e la possibilità di controllarlo.

### Schema statico e struttura reale

Lo schema statico descrive elementi, vincoli e azioni in una forma adatta all'analisi. La struttura reale comprende dettagli e fenomeni che lo schema può idealizzare.

Nella risposta vanno dichiarate le ipotesi essenziali. Assumere piccoli spostamenti, comportamento elastico lineare o collegamenti ideali significa delimitare la validità del risultato.

### Vincoli e gradi di libertà

I gradi di libertà descrivono i movimenti possibili del sistema. I vincoli ne impediscono alcuni e generano reazioni. Un vincolo va letto per l'effetto cinematico che produce, non memorizzato soltanto come simbolo grafico.

Un sistema è labile se conserva movimenti incompatibili con la funzione resistente prevista. È isostatico quando equilibrio e vincoli consentono di determinare le reazioni con le sole equazioni statiche. È iperstatico quando servono anche compatibilità delle deformazioni e legami costitutivi.

## Azioni, reazioni ed equilibrio

Le azioni esterne comprendono forze, momenti e altri effetti che sollecitano il sistema. Possono derivare dal peso, dall'uso, dall'ambiente, da deformazioni imposte o da altri fenomeni. Il capitolo 4 tratterà la loro classificazione normativa.

Le reazioni sono le azioni esercitate dai vincoli sul sistema. Per determinarle occorre isolare correttamente il corpo o la parte di struttura e rappresentare tutte le azioni pertinenti.

L'equilibrio richiede che risultante delle forze e risultante dei momenti rispettino le condizioni statiche del modello. È una condizione necessaria, ma non sempre sufficiente per descrivere la risposta. Un sistema può essere in equilibrio e avere deformazioni eccessive; può soddisfare le equazioni statiche ma risultare instabile.

### Il diagramma di corpo libero

Il diagramma di corpo libero separa il sistema dall'ambiente e sostituisce i vincoli con le reazioni corrispondenti. È uno strumento di ragionamento: obbliga a dichiarare che cosa stai studiando e quali azioni gli attribuisci.

Gli errori più comuni sono tre:

- dimenticare un'azione o una reazione;
- rappresentare un vincolo con reazioni incompatibili;
- applicare l'equilibrio a un sistema isolato male.

## Sollecitazioni interne

Immagina di sezionare idealmente un elemento. Le azioni che una parte esercita sull'altra sono rappresentate dalle caratteristiche della sollecitazione.

### Sforzo normale

Lo sforzo normale agisce lungo l'asse dell'elemento. Può essere associato a trazione o compressione. Il segno dipende dalla convenzione adottata; il significato fisico non deve dipendere dalla memoria di un segno isolato.

### Taglio

Il taglio rappresenta l'azione interna trasversale rispetto all'asse dell'elemento. È collegato alla variazione del momento flettente lungo la trave e contribuisce allo stato tensionale.

### Momento flettente

Il momento flettente è associato alla curvatura dell'elemento e alla flessione. La distribuzione delle tensioni dipende, nelle ipotesi del modello, anche dalla geometria della sezione.

### Momento torcente

La torsione tende a far ruotare le sezioni intorno all'asse dell'elemento. Il comportamento dipende in modo sensibile dalla forma della sezione e dal modello adottato.

I diagrammi delle sollecitazioni mostrano come queste grandezze variano lungo l'elemento. Non sono disegni ornamentali: servono a individuare zone critiche, controllare la coerenza del risultato e preparare le verifiche.

## Tensione e deformazione

Sollecitazione e tensione non sono sinonimi. La sollecitazione è una grandezza risultante riferita alla sezione; la tensione descrive l'intensità locale delle azioni interne nel materiale.

La deformazione descrive il cambiamento locale di forma o dimensione. Lo spostamento riguarda il movimento di un punto; la deformazione riguarda la variazione relativa tra punti vicini. Un corpo può muoversi rigidamente senza deformarsi.

Il legame costitutivo collega tensione e deformazione secondo un modello del materiale. Nel comportamento elastico, rimuovendo l'azione il materiale tende a recuperare la deformazione prevista dal modello. La linearità aggiunge una relazione proporzionale entro il campo assunto. Elasticità e linearità, quindi, non sono la stessa cosa.

Queste distinzioni servono in prova perché impediscono risposte generiche. Dire "la trave è sollecitata" non chiarisce né la risultante interna né lo stato locale del materiale.

## Proprietà e comportamento dei materiali

Il comportamento strutturale dipende dal materiale e dal modo in cui è impiegato. Tra le proprietà ricorrenti:

- resistenza rispetto a specifiche modalità di crisi;
- rigidezza nel rapporto tra azione e deformazione;
- duttilità e capacità deformativa;
- tenacità, legata all'energia assorbibile prima della rottura;
- effetti del tempo, della temperatura e dell'ambiente;
- variabilità delle proprietà.

Un unico valore non descrive l'intero comportamento. Materiali diversi possono avere resistenza simile ma rigidezza, duttilità o durabilità differenti. Anche dire "materiale resistente" è incompleto se non si specificano tipo di azione, stato limite e condizioni.

## Cinque prestazioni da non confondere

### Resistenza

La resistenza riguarda la capacità di non raggiungere la crisi considerata. La verifica confronta domanda e capacità nel modello adottato. Non dice, da sola, se gli spostamenti sono accettabili.

### Rigidezza

La rigidezza esprime l'opposizione alla deformazione. Un elemento può essere resistente ma troppo deformabile per la funzione richiesta.

### Stabilità

La stabilità riguarda la conservazione dell'equilibrio rispetto a perturbazioni. Negli elementi compressi può diventare decisiva anche quando la resistenza del materiale, considerata isolatamente, sembrerebbe sufficiente.

### Duttilità

La duttilità è la capacità di sviluppare deformazioni significative oltre il campo elastico prima della crisi, secondo il materiale e il sistema. Non coincide con la deformabilità generica.

### Durabilità

La durabilità riguarda il mantenimento nel tempo delle prestazioni richieste. Ambiente, dettagli, protezione, manutenzione e uso influenzano il degrado. Una verifica iniziale non esaurisce il problema.

## Caso guidato: un elemento compresso

Un elemento snello riceve una forza di compressione. Una risposta superficiale controlla soltanto la tensione media. Una risposta strutturale completa procede diversamente.

Prima definisce geometria, vincoli e imperfezioni rilevanti. Poi distingue resistenza del materiale e stabilità dell'equilibrio. Considera la snellezza e il modo in cui i vincoli condizionano la deformata. Infine chiarisce quale verifica occorre svolgere secondo il quadro tecnico applicabile.

Il caso mostra perché non basta chiedere "quanto resiste il materiale?". La crisi può dipendere dal comportamento dell'intero elemento.

## Da sapere in 5 righe

Il modello è una scelta, non una copia della struttura.  
L'equilibrio è necessario ma non esaurisce la verifica.  
Sollecitazione, tensione e deformazione indicano grandezze diverse.  
Resistenza e rigidezza non sono sinonimi.  
Stabilità e durabilità richiedono controlli propri.

## Domanda da commissario

**Qual è il percorso logico per analizzare una struttura semplice?**

Si definiscono scopo e ipotesi, si costruisce lo schema con geometria e vincoli, si applicano le azioni, si determinano reazioni e sollecitazioni, si valuta la risposta in termini di tensioni e deformazioni e si eseguono le verifiche pertinenti. Il risultato va infine controllato sul piano fisico e dimensionale.

## Domanda-trappola

**Se un elemento soddisfa la verifica di resistenza, è certamente adeguato?**

No. Possono risultare decisive rigidezza, stabilità, deformazioni, durabilità e altre prestazioni richieste. L'adeguatezza dipende dall'insieme delle verifiche applicabili.

## Errore tipico

L'errore più comune è scrivere una formula senza dichiarare modello, ipotesi, grandezze e significato del risultato. Per evitarlo, segui questa sequenza: dati, schema, ipotesi, equazioni, risultato, controllo.

## Mini-esercizio

Per ciascun fenomeno indica la grandezza prevalente:

1. allungamento di una barra tesa;
2. rotazione di una trave inflessa;
3. perdita di equilibrio di un'asta compressa;
4. degrado progressivo in ambiente aggressivo;
5. azione interna trasversale in una sezione.

Le risposte attese sono: deformazione assiale; spostamento/rotazione legati alla rigidezza flessionale; stabilità; durabilità; taglio.

## Checklist di impostazione

- Ho definito il sistema e lo scopo?
- Ho dichiarato vincoli, azioni e ipotesi?
- Ho distinto reazioni e sollecitazioni?
- Ho distinto sollecitazioni, tensioni e deformazioni?
- Ho controllato resistenza, rigidezza e stabilità pertinenti?
- Il risultato è fisicamente plausibile?
- Ho indicato i limiti del modello?

## Riferimenti consolidati

- [[sources/scienza-tecnica-costruzioni-fonti-universitarie]]
- [[topics/scienza-tecnica-costruzioni]]
- [[sources/campione-bandi-tecnici-pa-vol-10-2026]]
- [[sources/modulo-m-tr03-tecnico-ingegneristico-vol-10]]

## Note di review

- Audit specialistico automatico chiuso l'11 agosto 2026: formule, convenzioni, unità ed esercizi presenti sono coerenti con il perimetro didattico consolidato e non costituiscono calcolo o verifica di un'opera reale.
- Il livello matematico va calibrato sul singolo bando; i programmi universitari definiscono il perimetro disciplinare, non la profondità di ogni concorso.
- Le prescrizioni NTC, le combinazioni delle azioni, la sismica e la geotecnica restano nel capitolo 4.
