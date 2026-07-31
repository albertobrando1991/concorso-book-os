---
id: source-premal-definizioni-caso-risposta-segnale-epidemiologico
type: source
title: "PREMAL, definizioni di caso e risposta a un segnale epidemiologico"
status: processed
domain: "concorsi pubblici italiani"
topics: ["epidemiologia", "malattie infettive", "PREMAL", "definizione di caso", "indagine di focolaio"]
entities: ["Ministero della Salute", "Istituto Superiore di Sanità", "Centro europeo per la prevenzione e il controllo delle malattie"]
source_refs:
  - "sources/epidemiologia-base-iss"
  - "sources/sicurezza-cure-ica-sorveglianza-epidemiologica-prevenzione"
book_refs: ["m-sa02-professioni-sanitarie", "m-sa03-dirigenza-medica-sanitaria", "vol-07-sanita-amministrativa-professioni-sanitarie"]
confidence: 0.96
updated_at: 2026-07-31T18:30:00+02:00
created_at: 2026-07-29T18:00:00+02:00
review_required: true
canonical: true
tags: ["source", "epidemiologia", "premal", "notifica", "focolaio", "iss", "ecdc", "m-sa02"]
source_type: official_legal_and_public_health_corpus
source_url: "https://www.salute.gov.it/new/it/tema/malattie-infettive/modalita-di-segnalazione-delle-malattie-infettive/"
source_date: "2013-2026"
authority_level: official_legal_and_scientific
raw_path: "wiki/raw/m-sa02-professioni-sanitarie/epidemiologia/"
---

# PREMAL, definizioni di caso e risposta a un segnale epidemiologico

## Corpus acquisito

Il corpus locale contiene quattro PDF ufficiali, per complessive 190 pagine:

- fascicolo della Gazzetta Ufficiale n. 82 del 7 aprile 2022, con il D.M. 7 marzo 2022 sulla revisione del sistema PREMAL e i relativi allegati, 96 pagine;
- guida EpiCentro-ISS per la gestione delle malattie veicolate da alimenti, versione PDF creata nel 2022, 77 pagine;
- guida ECDC alla redazione dei rapporti di indagine su focolai, 11 pagine;
- strumento ECDC per costruire definizioni di caso nelle indagini su focolai veicolati da alimenti e acqua, 6 pagine.

Byte e SHA-256 sono registrati in `epidemiologia/download-log.json`. Le pagine correnti del Ministero sulla segnalazione delle malattie infettive e sul sistema PREMAL sono state controllate il 29 luglio 2026. Il CDN ministeriale ha restituito a `curl` una pagina tecnica Gcore anziché il contenuto: tali risposte non sono state conservate come false fonti raw. I localizzatori ufficiali rimangono:

- `https://www.salute.gov.it/new/it/tema/malattie-infettive/modalita-di-segnalazione-delle-malattie-infettive/`;
- `https://www.salute.gov.it/new/it/sistema-informativo/sorveglianza-delle-malattie-infettive-premal/`.

## Quadro normativo e flusso di segnalazione

Il D.M. 7 marzo 2022 disciplina organizzazione e funzionamento di PREMAL, modalità di segnalazione, raccolta, elaborazione e uso dei dati sulle malattie infettive. Il medico che, nell'esercizio delle proprie funzioni, venga a conoscenza di un caso di malattia infettiva e diffusiva o sospetta di esserlo effettua la segnalazione alla struttura sanitaria competente dell'Azienda sanitaria. La struttura aziendale:

1. alimenta PREMAL secondo tempi e modalità applicabili;
2. svolge l'indagine epidemiologica;
3. adotta i provvedimenti di sanità pubblica di competenza;
4. completa i dati non disponibili all'inizio;
5. valida e trasmette la segnalazione alla struttura regionale o provinciale autonoma competente.

La pagina ministeriale corrente distingue nel sistema un caso `potenziale`, ancora privo di dati sufficienti, da un caso `conclamato`, che soddisfa la definizione applicabile. L'indagine può riclassificare il caso. Questa terminologia di sistema non va confusa con le classi epidemiologiche `possibile`, `probabile` e `confermato` previste dalle definizioni di sorveglianza per specifiche malattie.

## Definizione di caso: due livelli da non confondere

### Definizione di sorveglianza

È la definizione ufficiale applicabile a una determinata malattia. Può combinare criteri clinici, di laboratorio ed epidemiologici e classificare i casi. La guida ISS descrive:

- `possibile`: soddisfa i criteri clinici, senza evidenza epidemiologica o di laboratorio richiesta;
- `probabile`: soddisfa i criteri clinici e presenta una correlazione epidemiologica;
- `confermato`: soddisfa i criteri di laboratorio previsti dalla definizione applicabile.

La versione corrente della definizione specifica deve essere verificata al momento dell'uso; non è corretto trasferire una classificazione da una malattia a un'altra.

### Definizione operativa di caso nell'indagine di focolaio

Serve a trovare e classificare in modo coerente le persone collegate all'evento sotto indagine. Non è la definizione del focolaio, ma la regola con cui si decide chi includere fra i casi dell'indagine. Le guide ISS ed ECDC richiedono almeno:

- tempo;
- luogo;
- persona o popolazione;
- criteri clinici;
- criteri di laboratorio, quando disponibili;
- eventuale legame epidemiologico.

È una definizione di lavoro: deve essere esplicita, applicata uniformemente e aggiornata se emergono nuove informazioni. Non sostituisce la definizione nazionale di sorveglianza e non dimostra da sola la causa del focolaio. Il focolaio riguarda invece un'aggregazione di casi collegati epidemiologicamente o un numero di casi superiore all'atteso in tempo, luogo e popolazione definiti, secondo i criteri applicabili alla malattia e al sistema di sorveglianza. Per eventi rari o ad alto impatto anche un singolo caso può attivare un'allerta, senza diventare per questo una definizione universale di focolaio.

## Sequenza di risposta al segnale

La guida EpiCentro-ISS organizza l'indagine in dieci passaggi:

1. identificare un possibile episodio e confermarlo;
2. formulare una definizione di caso;
3. ricercare i casi;
4. intervistare i casi;
5. descrivere tempo, luogo e persona e formulare una prima ipotesi;
6. effettuare studi di epidemiologia analitica;
7. svolgere accertamenti sul patogeno, sull'alimento e sui luoghi di esposizione o contaminazione;
8. comunicare i risultati preliminari e adottare o proporre misure di controllo;
9. verificare l'ipotesi;
10. comunicare i risultati e redigere un rapporto.

La verifica iniziale deve considerare distorsioni informative, variazioni diagnostiche, stagionalità e concentrazioni casuali. La guida precisa anche che non occorre attendere la diagnosi eziologica per adottare misure di contenimento proporzionate quando il rischio lo richiede.

## Uso editoriale

- `SA02-06`: distinguere segnale, caso potenziale, definizione ufficiale e definizione operativa;
- `SA02-06`: descrivere il flusso medico-Azienda sanitaria-Regione-PREMAL;
- `SA02-06`: costruire line list, curva epidemica, tasso d'attacco e confronto fra esposti e non esposti;
- `PRV-03`: svolgere uno scenario completo senza anticipare causalità o competenze locali non documentate;
- cap. 08 e laboratorio prove, solo dopo apertura del gate.

Lo scenario applicativo è in [[books/moduli/m-sa02-professioni-sanitarie/planning/04-scenario-risposta-segnale-epidemiologico]].
Il controllo esterno è predisposto nel [[books/moduli/m-sa02-professioni-sanitarie/planning/05-pacchetto-review-epidemiologica-indipendente|pacchetto di review epidemiologica indipendente]] e nel [[reviews/pipeline/VOL-07/07-verbale-review-epidemiologica-indipendente-m-sa02|verbale ancora da compilare]].

## Limiti e cautele

- La guida ISS sulle malattie veicolate da alimenti contiene una procedura regionale di dettaglio: la sequenza epidemiologica generale è riusabile, mentre ruoli, modulistica e tempi locali vanno verificati nel territorio competente.
- Gli strumenti ECDC sulle definizioni di caso sono anteriori al 2022; restano utili per la struttura metodologica, non per sostituire le definizioni vigenti.
- La pagina ministeriale corrente e le specifiche PREMAL sono fonti mobili; data e versione devono essere ricontrollate alla pubblicazione.
- Lo scenario didattico non autorizza diagnosi, campionamenti o provvedimenti reali e richiede review epidemiologica e professionale.

## Stato revisione

Il vuoto documentale su notifica, definizioni di caso e sequenza completa di risposta è risolto. Il pacchetto di review è pronto, ma non ancora eseguito: il nucleo `SA02-06` resta `parziale` finché la batteria quantitativa e lo scenario non ricevono una review epidemiologica indipendente e non viene effettuato il controllo di versione prepubblicazione.
