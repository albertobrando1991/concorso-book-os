---
id: review-vol-07-05-audit-bandi-m-sa02
type: review
title: "VOL-07 step 05 - Audit bandi M-SA02"
status: completed
domain: "concorsi pubblici italiani"
topics: ["professioni sanitarie", "bandi", "prove concorsuali"]
entities: ["inPA", "Azienda sanitaria"]
source_refs: ["sources/bandi-rappresentativi-m-sa02-professioni-sanitarie-2025-2026.md"]
book_refs: ["m-sa02-professioni-sanitarie", "vol-07-sanita-amministrativa-professioni-sanitarie"]
confidence: 0.93
updated_at: 2026-07-28T20:00:00+02:00
created_at: 2026-07-28T20:00:00+02:00
review_required: true
canonical: false
tags: ["pipeline", "vol-07", "step-05", "m-sa02", "audit"]
issue_type: source_audit
severity: high
affected_pages: ["books/moduli/m-sa02-professioni-sanitarie/index.md", "books/moduli/m-sa02-professioni-sanitarie/planning/00-piano-editoriale.md"]
---

# VOL-07 step 05 - Audit bandi M-SA02

## Esito sintetico

**GO per la progettazione delle fonti; STOP per la scrittura dei capitoli.**

Sono stati acquisiti 16 bandi ufficiali da inPA, con distribuzione `INF 5 + PRO 6 + PREV 5`. Quindici PDF consentono audit testuale integrale; il documento `PRO-02`, acquisito come scansione, è mantenuto come fonte supplementare ed escluso dai conteggi. Il corpus soddisfa la richiesta di 5-6 bandi per cluster prioritario e rende verificabili requisiti, prove, output e differenze di profilo.

Il corpus non soddisfa da solo il gate fonti: prima della scrittura servono norme vigenti, profili professionali, codici deontologici, linee guida e fonti tecnico-disciplinari.

## Metodo e campione

- Data di controllo: 28 luglio 2026.
- Fonte: pagine e allegati ufficiali inPA.
- Cluster: infermiere; ostetrica/fisioterapista; TPALL.
- Conservazione: `wiki/raw/m-sa02-professioni-sanitarie/bandi/` con registro URL, byte e SHA-256.
- Denominatori: 5 bandi per ciascun cluster; il sesto documento PRO è supplementare perché scansionato.
- Criteri: ente, profilo, requisiti, materie, prove, output, strumenti/competenze, elementi mobili.

## Quadro delle ricorrenze

| Cluster | Requisito professionale | Scritta | Orale | Pratica autonoma | Informatica/lingua |
| --- | ---: | ---: | ---: | ---: | ---: |
| Infermiere, n=5 | 5/5 | 5/5 | 4/5 | 3/5 | 5/5 |
| Ostetrica/fisioterapista, n=5 | 5/5 | 5/5 | 5/5 | 4/5 | 5/5 |
| TPALL, n=5 | 5/5 | 5/5 | 5/5 | 3/5 | 5/5 |

Le frequenze hanno valore interno al campione. Non sono stime dell'intero universo dei concorsi.

## Differenze che incidono sull'indice

### Infermiere

Servono nuclei separati su pianificazione assistenziale, tecniche generali e specialistiche, clinica, igiene/infezioni, rischio clinico, relazione e ricerca. La prova pratica richiede output autonomi e non può essere trattata come semplice ripasso della teoria.

### Ostetrica e fisioterapista

Il profilo ostetrico è troppo generico nello scaffold: occorre una mappa disciplinare sostenuta da fonti ufficiali proprie. Per fisioterapista vanno esplicitati organizzazione riabilitativa, valutazione funzionale e multidimensionale, rieducazione, fragilità, disabilità, cure palliative e casi.

### TPALL

Occorre distinguere la sottotraccia sanitaria/prevenzionale da quella ambientale ARPA. Ispezione, campionamento, verbalizzazione, atti, illeciti e sanzioni devono diventare output allenabili, sostenuti da norme settoriali.

## Lacune dell'indice attuale

1. Lo scaffold promette anche il profilo OSS, ma il campione non contiene bandi OSS. Prima della scrittura occorre acquisire un cluster dedicato oppure spostare/escludere esplicitamente il profilo dal perimetro M-SA02.
2. Il verticale infermiere non distingue ancora teoria assistenziale, tecniche, clinica, rischio/infezioni e prova pratica.
3. Fisioterapia richiede un percorso disciplinare e casi propri, non una voce generica “professioni sanitarie”.
4. Ostetricia richiede fonti e articolazione proprie: i bandi aggregati descrivono le prove, non il programma completo.
5. TPALL deve essere diviso tra prevenzione sanitaria/sicurezza e controllo ambientale.
6. L'architettura della prova pratica non è ancora rappresentata come asse editoriale autonomo.
7. Informatica e lingua possono rinviare al VOL-01 solo dopo verifica del contesto specifico delle prove sanitarie.
8. Norme regionali, procedure aziendali, calendario, posti, punteggi, piattaforme e requisiti locali devono essere marcati come mobili.

## Priorità per lo step 06

1. Profili professionali: D.M. 739/1994, D.M. 740/1994, D.M. 741/1994, D.M. 58/1997; quadro di lauree, albi e ordinamento professionale.
2. Ordinamento e responsabilità: leggi 251/2000, 43/2006, 3/2018, 24/2017, 219/2017 e disciplina concorsuale pertinente.
3. Fonti professionali: FNOPI, FNO TSRM e PSTRP e, per ostetricia, federazione/ordine nazionale competente.
4. Infermieristica: pianificazione, sicurezza, infezioni, rischio clinico, ricerca ed evidenze.
5. Fisioterapia e ostetricia: fonti tecnico-professionali ufficiali per i rispettivi verticali.
6. TPALL: sicurezza sul lavoro, igiene pubblica, ispezioni, sanzioni e corpus ambientale.
7. Cluster OSS: decisione di perimetro e, se confermato, raccolta di 5-6 bandi e relative fonti.

## Elementi mobili

Posti, scadenze, riserve, preferenze, contributi, modalità di domanda, piattaforme, calendario, punteggi, soglie, banca dati, sedi, contratto, requisito patente, normativa regionale, procedure aziendali, strumenti e protocolli locali. Devono essere controllati sul bando target e datati.

## Verdetto

Il gate manuale dello step 05 può essere accettato perché corpus, ricorrenze, differenze e lacune sono documentati e tracciati. I capitoli restano non scritti. Lo step 06 dovrà chiudere le lacune source-ready; lo step 07 potrà poi decidere il GO/STOP editoriale.
