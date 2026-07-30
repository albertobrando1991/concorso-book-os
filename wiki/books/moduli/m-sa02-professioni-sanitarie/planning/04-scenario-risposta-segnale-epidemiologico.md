---
id: m-sa02-scenario-risposta-segnale-epidemiologico
type: planning
title: "M-SA02 - Scenario completo di risposta a un segnale epidemiologico"
status: draft
domain: "concorsi pubblici italiani"
source_refs:
  - "sources/premal-definizioni-caso-risposta-segnale-epidemiologico"
  - "sources/epidemiologia-base-iss"
book_refs: ["m-sa02-professioni-sanitarie", "vol-07-sanita-amministrativa-professioni-sanitarie"]
updated_at: 2026-07-29T18:00:00+02:00
created_at: 2026-07-29T18:00:00+02:00
review_required: true
canonical: false
tags: ["m-sa02", "scenario", "epidemiologia", "focolaio", "premal", "prova-pratica", "pipeline-step-07"]
---

# Scenario completo di risposta a un segnale epidemiologico

## Regole d'uso

Questa è una risorsa di pianificazione per una prova teorico-pratica, non un protocollo clinico o aziendale. Evento, date e conteggi sono sintetici. La soluzione espone il metodo di sanità pubblica, mantiene separate ipotesi e conclusioni e rinvia alle procedure territoriali per responsabilità, modulistica, campionamento e provvedimenti.

## Traccia

Il 16 ottobre il Servizio di igiene riceve, attraverso i canali previsti, segnalazioni relative a più persone con sintomi gastrointestinali dopo un pranzo consumato il 15 ottobre nella stessa mensa aziendale. Alcune persone si sono rivolte a medici diversi; il laboratorio comunica che sono in corso accertamenti microbiologici. Non è ancora identificato un agente eziologico.

Alla mensa risultano 120 presenti. Sono contattabili 112 persone; 96 completano l'intervista iniziale. Ventiquattro soddisfano la definizione operativa adottata. La scheda alimentare produce questi dati didattici:

| Esposizione | Malati | Non malati | Totale | Tasso d'attacco |
| --- | ---: | ---: | ---: | ---: |
| Pietanza A: esposti | 22 | 22 | 44 | 50,0% |
| Pietanza A: non esposti | 2 | 50 | 52 | 3,85% |
| Pietanza B: esposti | 17 | 51 | 68 | 25,0% |
| Pietanza B: non esposti | 7 | 21 | 28 | 25,0% |

Il candidato deve descrivere la risposta dal segnale al rapporto finale, formulare una definizione di caso, calcolare gli indicatori essenziali, proporre le azioni e indicare i limiti.

## Soluzione guidata

### 1. Verificare il segnale

La prima domanda non è quale alimento abbia causato l'evento, ma se esista un incremento coerente di casi collegati nel tempo, nel luogo e nella popolazione. Occorre:

- verificare identità, duplicati, data e ora di esordio;
- confermare criteri clinici minimi e comune occasione di esposizione;
- controllare eventuali variazioni di accesso, diagnosi o segnalazione;
- confrontare, se disponibili, dati attesi e segnalazioni di laboratorio;
- attivare il coordinamento previsto senza attendere una conferma eziologica quando il rischio richiede misure tempestive.

Output: nota iniziale con fonte del segnale, numero provvisorio di persone, setting, incertezze, azioni già intraprese e responsabile del coordinamento.

### 2. Attivare segnalazione e coordinamento

Il medico segnala il caso accertato o sospetto alla struttura competente dell'Azienda sanitaria secondo il D.M. 7 marzo 2022. L'Azienda sanitaria alimenta PREMAL, svolge l'indagine epidemiologica, completa e valida la segnalazione e la trasmette al livello regionale secondo il flusso applicabile.

Nel caso concreto vanno individuati, secondo l'organizzazione locale, almeno coordinamento medico di sanità pubblica, assistente sanitario o infermiere, tecnico della prevenzione, laboratorio e referenti clinici. La composizione non attribuisce automaticamente poteri o atti: competenze e firme devono seguire normativa e procedure locali.

### 3. Formulare la definizione operativa

Definizione iniziale per la ricerca dei casi:

> Persona presente al pranzo della mensa aziendale del 15 ottobre che abbia sviluppato diarrea, definita come almeno tre scariche liquide in 24 ore, entro le 72 ore successive al pasto.

La soglia e la finestra riprendono la struttura di un esempio ECDC e servono solo per questo esercizio. La definizione contiene persona, luogo/esposizione, tempo e criterio clinico. Deve essere applicata anche a chi non ha consultato un medico.

Classi di lavoro:

- `caso operativo`: soddisfa integralmente la definizione;
- `persona da approfondire`: presenta sintomi o tempi non pienamente compatibili;
- `caso con conferma di laboratorio collegabile al focolaio`: categoria utilizzabile solo dopo che agente, metodo e collegamento siano definiti.

Queste classi non sostituiscono `possibile`, `probabile` e `confermato` della definizione ufficiale della specifica malattia, ancora ignota.

### 4. Ricercare e descrivere i casi

Costruire una line list con identificativo pseudonimizzato, contatti consentiti, età o classe di età, ruolo, presenza al pasto, alimenti consumati, data e ora di esordio, sintomi, durata, assistenza ricevuta, ricovero, esami e risultati. Registrare anche non esposti e non malati necessari all'analisi.

Calcoli iniziali:

- tasso di risposta: `96 / 112 = 85,7%`;
- tasso d'attacco complessivo fra gli intervistati: `24 / 96 = 25,0%`.

Produrre curva epidemica per ora di esordio, distribuzione per area o gruppo e tabella dei sintomi. Un andamento compatibile con fonte comune genera un'ipotesi, non prova la causa.

### 5. Generare e testare le ipotesi

Per la pietanza A:

- tasso d'attacco esposti: `22 / 44 = 50,0%`;
- tasso d'attacco non esposti: `2 / 52 = 3,85%`;
- rischio relativo didattico: `0,50 / 0,03846 = 13,0`.

Per la pietanza B:

- esposti: `17 / 68 = 25,0%`;
- non esposti: `7 / 28 = 25,0%`;
- rischio relativo: `1,0`.

La pietanza A è l'ipotesi prioritaria perché presenta una forte associazione nel dataset sintetico; la pietanza B non discrimina i casi. Prima di concludere occorre valutare precisione, confondimento, esposizioni correlate, errori di ricordo, non risposta, contaminazione crociata e plausibilità temporale e microbiologica.

### 6. Integrare epidemiologia, laboratorio e ambiente

Le attività devono essere guidate dalle ipotesi:

- concordare campioni clinici e ricerche appropriate con il laboratorio;
- acquisire menu, processi, tempi, temperature, forniture e tracciabilità;
- verificare disponibilità di avanzi o materie prime pertinenti;
- documentare metodi, tempi e catena di custodia secondo le procedure applicabili;
- confrontare eventuali risultati umani, alimentari e ambientali senza considerarli intercambiabili.

Un risultato negativo non esclude da solo l'ipotesi se campione, tempo o metodo erano inadeguati; un risultato positivo richiede interpretazione epidemiologica e tecnica.

### 7. Adottare misure proporzionate

Le misure immediate dipendono dal rischio e dalle competenze dell'autorità: assistenza ai malati, indicazioni ai soggetti esposti, conservazione delle evidenze, correzione di condizioni igieniche critiche, gestione prudenziale degli alimenti sospetti e comunicazione ai livelli competenti. Vanno registrati motivazione, responsabile, ora, destinatari e criterio di revoca.

Non si attende necessariamente la diagnosi definitiva se esiste un rischio controllabile; non si attribuiscono però responsabilità o causalità prima dell'analisi.

### 8. Aggiornare definizione e valutazione

Ad ogni nuovo dato:

- riesaminare la definizione operativa;
- distinguere inclusioni, esclusioni e casi dubbi;
- aggiornare line list, curva e denominatori;
- confrontare ipotesi epidemiologica, risultati di laboratorio e indagine ambientale;
- documentare perché un'ipotesi sia mantenuta, modificata o respinta.

### 9. Comunicare

Prevedere tre prodotti:

1. aggiornamento operativo breve per il team e le autorità;
2. comunicazione coerente ai soggetti interessati, rispettosa di privacy e incertezze;
3. rapporto finale con problema, obiettivi, metodi, definizione di caso, ricerca dei casi, risultati descrittivi e analitici, laboratorio, ambiente, limiti, azioni e raccomandazioni.

Numeratore, denominatore, casi esclusi, dati mancanti e data di estrazione devono essere sempre visibili.

### 10. Chiudere e apprendere

La chiusura richiede verifica dell'andamento dei casi, esito delle misure, risultati pendenti, tracciabilità delle decisioni e follow-up. La revisione finale deve separare:

- fatti osservati;
- calcoli;
- interpretazioni;
- ipotesi non confermate;
- decisioni adottate;
- miglioramenti del sistema.

## Griglia di valutazione

| Criterio | Punti | Evidenza attesa |
| --- | ---: | --- |
| Verifica del segnale | 2 | Duplicati, baseline, distorsioni, incertezze |
| Flusso di notifica | 2 | Medico, Azienda sanitaria, PREMAL, Regione |
| Definizione operativa | 3 | Tempo, luogo, persona, clinica; distinzione dalla definizione ufficiale |
| Ricerca e descrizione | 3 | Line list, curva, tempo-luogo-persona, denominatori |
| Calcoli | 4 | Risposta 85,7%; attacco 25%; RR A 13,0; RR B 1,0 |
| Indagine integrata | 3 | Epidemiologia, laboratorio, ambiente, tracciabilità |
| Misure e comunicazione | 3 | Proporzionalità, ruoli, privacy, report |
| Limiti e revisione | 2 | Bias, dati mancanti, ipotesi non causalità |
| **Totale** | **22** |  |

## Errori da penalizzare

- chiamare `confermato` un caso senza applicare la definizione specifica;
- confondere caso `potenziale/conclamato` di PREMAL con `possibile/probabile/confermato`;
- dichiarare causalità dalla sola associazione;
- calcolare percentuali senza denominatore;
- campionare senza ipotesi, metodo e tracciabilità;
- attendere sempre la diagnosi prima di ogni misura;
- inventare competenze, tempi o moduli locali;
- omettere non risposta, privacy, limiti e risultati pendenti.

## Review richiesta

I quattro calcoli e la checklist specialistica sono inclusi nel [[books/moduli/m-sa02-professioni-sanitarie/planning/05-pacchetto-review-epidemiologica-indipendente|pacchetto di review epidemiologica indipendente]]. Il verbale resta da compilare da parte di un revisore esterno.

Prima dell'uso editoriale servono:

1. controllo indipendente dei quattro calcoli;
2. review epidemiologica della definizione e dell'interpretazione;
3. review professionale dei ruoli multiprofessionali;
4. verifica della versione corrente del flusso PREMAL e della definizione di sorveglianza applicabile;
5. adattamento alle procedure territoriali solo dopo acquisizione della relativa fonte.
