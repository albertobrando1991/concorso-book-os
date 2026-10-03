---
id: source-logica-volumi-copertura-concorsobook-v4
type: source
title: "Logica dei volumi e della copertura ConcorsoBook v4"
status: processed
domain: "concorsi pubblici italiani"
topics: ["catalogo editoriale", "copertura materie", "moduli specialistici", "pacchetti commerciali", "revisione editoriale"]
entities: ["ConcorsoBook", "Metodo BANDO", "Capitale Personale", "VOL-01"]
source_refs: ["sources/idea-business-vendita-libri-capitale-personale-2026-07-03.md", "sources/struttura-madre-il-metodo-bando.md"]
book_refs: ["il-metodo-bando", "moduli-specialistici"]
confidence: 0.92
updated_at: 2026-07-14T00:00:00+02:00
created_at: 2026-07-14T00:00:00+02:00
review_required: true
canonical: true
tags: ["source", "business-strategy", "catalogo-editoriale", "coverage-governance"]
source_type: business_strategy
source_url: ""
source_date: 2026-07-14
authority_level: alta
raw_path: "wiki/raw/business/logica-volumi-copertura-concorsobook-v4.md"
---

# Logica dei volumi e della copertura ConcorsoBook v4

## Stato della fonte
Questa nota consolida il documento operativo v4 ricevuto il 14 luglio 2026. E' la regola di partenza vincolante per progettare, sviluppare, vendere e revisionare i volumi ConcorsoBook. Integra la tassonomia canonica a 6 famiglie, 25 moduli e 12 volumi; non la sostituisce con una lista commerciale ridotta.

## Regola madre

- Materia comune a tutti i concorsi: solo `VOL-01`.
- Materia di famiglia: solo nel volume specialistico della famiglia corretta.
- Materia di sottoprofilo: appendice o verticale, soltanto quando la specializzazione e' reale.
- Materia di un'altra famiglia: rinvio esplicito al relativo specialistico, senza duplicazione.

Il sistema e' composto da tre livelli: `VOL-01` come base riusabile, Ricettario operativo digitale su Capitale Personale per allenamento e aggiornamenti, e specialistici per famiglia/profilo. Un bando non deve portare il candidato ad acquistare molti libri: la proposta standard e' base piu un solo specialistico pertinente.

## Perimetro inderogabile di VOL-01
`VOL-01 Manuale base PA` contiene il nucleo B-PA01/B-PA11: diritto costituzionale e pubblico; diritto amministrativo generale; pubblico impiego generale; reati contro la PA e responsabilita'; contabilita' pubblica essenziale; contratti pubblici essenziali; privacy, CAD e trasparenza digitale; inglese di base; informatica di base; logica, attitudinali e situazionali; redazione atti e casi pratici di base.

Gli specialistici applicano e contestualizzano questo nucleo: non lo riscrivono in forma generale. Il Ricettario digitale ospita quiz, simulazioni, casi, tracce, risposte, errori e aggiornamenti operativi; non sostituisce la preparazione autonoma fornita dal libro.

## Assegnazione obbligatoria di un bando
Prima di scrivere un volume, un capitolo specialistico, un'appendice, una proposta commerciale o una risposta al cliente, compilare la scheda di copertura:

| Campo | Decisione da registrare |
| --- | --- |
| Famiglia | Una delle 6 famiglie canoniche |
| Profilo | Profilo/area effettiva del bando |
| Nucleo comune | Voci B-PA gia' coperte da VOL-01 |
| Specialistico | Volume e modulo che coprono la materia di famiglia |
| Sottoprofilo | Appendice o verticale necessario, se realmente distintivo |
| Altra famiglia | Rinvio al volume corretto, senza duplicare il contenuto |
| Pacchetto | Standard, Verticale o Premium con motivazione |
| Esclusioni | Materiali che il candidato non deve acquistare |

Il flusso e': 1) identifica famiglia; 2) identifica profilo; 3) classifica ogni materia come comune, di famiglia, di sottoprofilo o di altra famiglia; 4) assegna il pacchetto minimo corretto; 5) dichiara esplicitamente cosa non serve acquistare.

## Catalogo, eccezioni e riconciliazione
La mappa commerciale resta quella di [[books/moduli/architettura-moduli-specialistici|Architettura moduli specialistici Metodo BANDO]]. In particolare, M-FL03 resta in `VOL-02` per coerenza con la famiglia locale; M-FC01 resta in `VOL-03`, ma puo' essere proposto solo con instradamento per profilo: amministrativo generale con il percorso Ministeri/PCM, tecnico verso `VOL-10`, ICT verso `VOL-08`, statistico-economico con base e approfondimento ministeriale mirato. Non e' un volume da proporre indiscriminatamente.

Le appendici chiudono lacune concrete; un verticale esiste solo se il bando richiede una specializzazione autonoma. I pacchetti sono: Standard = `VOL-01 + 1 specialistico`; Verticale = base + famiglia + appendice/verticale; Premium = base + percorso ad alta barriera. Non creare verticali per convenienza di catalogo.

## Gate per sviluppo e revisione
Ogni sviluppo e ogni revisione devono verificare e rendere tracciabile:

1. assenza di duplicazione del nucleo B-PA negli specialistici;
2. appartenenza della materia alla famiglia corretta;
3. copertura delle materie ricorrenti e pesate del bando/profilo;
4. rinvio cross-family quando serve, invece di una copia del contenuto;
5. necessarieta' effettiva di appendici, verticali e Premium;
6. coerenza del pacchetto e delle esclusioni dichiarate;
7. fonti consolidate e review umana per contenuti settoriali o normativi.

Le violazioni dei punti 1, 2 o 3 sono errori gravi di architettura editoriale e impediscono la pubblicazione fino alla correzione.

## Prossimi passi obbligatori

1. Creare o aggiornare la scheda di copertura per ogni modulo e per ogni proposta di volume.
2. Verificare i cluster prioritari su 5-6 bandi rappresentativi e registrare lacune, rinvii e aggiornamenti necessari.
3. Sviluppare capitoli solo dopo che fonti, topic/entity pages e scheda di copertura sono disponibili.
4. Eseguire due gate prima della pubblicazione: controllo di copertura/posizionamento e Revisore Editoriale Totale con checklist a 30 punti.
5. Portare la stessa logica nel decoder bando, nel catalogo/dashboard e nelle risposte di assistenza, per proporre il percorso minimo utile.

## Collegamenti
- [[books/moduli/architettura-moduli-specialistici|Architettura moduli specialistici Metodo BANDO]]
- [[sources/idea-business-vendita-libri-capitale-personale-2026-07-03|Aggiornamento catalogo 12 volumi]]
- [[sources/matrice-materie-profili-metodo-bando|Matrice materie e profili Metodo BANDO]]
- [[topics/logica-copertura-volumi-concorsobook|Logica di copertura dei volumi]]
