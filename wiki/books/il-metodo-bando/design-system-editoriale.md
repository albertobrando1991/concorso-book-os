---
id: design-system-editoriale-il-metodo-bando
type: book_design_system
title: "Design system editoriale - Il Metodo BANDO"
status: canonical
domain: "concorsi pubblici italiani"
topics: ["book design","typography","manual layout","workbook","metodo bando"]
entities: ["Metodo BANDO","Bando Decoder","Manual Writer Agent"]
source_refs: ["sources/book-layout-typography-standards.md","sources/struttura-madre-il-metodo-bando.md","sources/metodo-bando-progetto-editoriale.md"]
book_refs: ["il-metodo-bando"]
confidence: 0.92
updated_at: 2026-05-10T12:59:21+02:00
created_at: 2026-05-10T12:59:21+02:00
review_required: false
canonical: true
tags: ["editorial-design","manual","workbook","layout"]
---

# Design system editoriale - Il Metodo BANDO

## Principio
`Il Metodo BANDO` deve apparire come un manuale-workbook professionale: leggibile, operativo, modulare, adatto a studio autonomo, prove concorsuali, ripasso e compilazione.

Non deve sembrare:
- un romanzo;
- un compendio universitario fitto;
- una raccolta generica di quiz;
- una dispensa scolastica improvvisata.

## Formato fisico consigliato
Formato principale:

```text
17 x 24 cm circa
KDP equivalente: 6.69 x 9.61 in
```

Motivo:
- abbastanza ampio per tabelle, box, mappe e pagine compilabili;
- piu professionale di un 6 x 9 per un manuale operativo;
- meno ingombrante di un A4 o 8.5 x 11;
- coerente con manuali, guide tecniche e workbook europei.

Formato alternativo per edizione molto pratica/workbook:

```text
7 x 10 in
```

Usarlo solo se aumentano molto schede compilabili, griglie, tabelle e immagini.

## Margini e gabbia
Per un libro previsto tra 300 e 500 pagine:

```text
interno/gutter: 19 mm
esterno: 15 mm
alto: 18 mm
basso: 22 mm
area testo: colonna singola
```

Regola:
- niente testo troppo vicino alla legatura;
- no layout a due colonne per la spiegazione principale;
- box e strumenti devono entrare nella colonna senza comprimere il testo;
- tabelle larghe possono usare pagina piena o orientamento dedicato solo in appendice/PDF.

Bleed:
- default: no bleed per il corpo libro;
- usare bleed solo per pagine speciali con grafica a piena pagina;
- se anche una sola pagina interna richiede bleed, preparare l'intero file secondo le regole di bleed della piattaforma di stampa.

## Font
Scelta consigliata:

```text
Testo principale: Source Serif 4
Titoli, box, didascalie, tabelle: Source Sans 3
Fallback testo: Charter, Georgia, serif
Fallback sans: Segoe UI, Arial, sans-serif
```

Motivo:
- Source Serif 4 e' adatto alla lettura lunga e ha optical sizes;
- Source Sans 3 mantiene chiarezza operativa in titoli, box e tabelle;
- entrambe le famiglie sono disponibili con licenza open source/commerciale tramite Adobe Fonts.

Alternative premium per impaginazione finale:
- Minion Pro per corpo;
- Myriad Pro o Source Sans 3 per titoli e box.

## Dimensioni tipografiche stampa
Corpo principale:

```text
10.8-11 pt
interlinea: 14.2-14.8 pt
spazio dopo paragrafo: 4-6 pt
allineamento: preferibilmente bandiera sinistra per bozza e digitale; giustificato solo in PDF finale con sillabazione controllata
```

Titoli:

```text
H1 capitolo: 24-28 pt Source Sans 3 Bold
H2 sezione: 15-17 pt Source Sans 3 Semibold
H3 blocco operativo: 11.5-13 pt Source Sans 3 Semibold
Didascalie: 8.5-9 pt Source Sans 3
Note/fonti: 8.5-9 pt Source Sans 3
```

Riga:

```text
target: 60-75 caratteri medi per riga
limite accettabile: 45-90 caratteri
```

## Dimensioni digitali/dashboard
Preview dashboard:

```text
corpo: 17 px
line-height: 1.56
larghezza testo: max 68ch
spaziatura paragrafo: 0.75rem
```

Il digitale deve restare accessibile: il layout non deve rompersi se il lettore aumenta interlinea o spaziatura.

## Gerarchia pagina capitolo
Ogni capitolo deve seguire questa architettura visiva:

1. Numero capitolo.
2. Titolo chiaro e orientato al bisogno.
3. Promessa/obiettivo del capitolo.
4. Mappa BANDO del capitolo.
5. Spiegazione principale in blocchi brevi.
6. Box operativi.
7. Caso guidato o esempio.
8. Domande e mini-esercizi.
9. Errori frequenti.
10. Riferimenti consolidati.
11. Note di review.

## Tassonomia box
Usare box ricorrenti, con nomi stabili:

```text
BANDO in pratica
Da sapere in 5 righe
Come lo chiede la commissione
Domanda-trappola
Errore tipico
Caso guidato
Risposta modello
Mini-esercizio
Checklist operativa
Bando Decoder
Diario errori
Fonti consolidate
Da verificare
```

Colori:
- blu istituzionale: metodo, mappe, definizioni;
- verde: checklist, conferme, output;
- ambra: errori, trappole, attenzione;
- rosso solo per blocchi critici o review;
- grigio neutro per fonti, note, metadati.

I box non devono diventare decorazione: ogni box deve produrre utilita didattica.

## Tabelle e schemi
Tabelle:
- intestazioni sans serif;
- righe leggere;
- zebra striping molto tenue;
- evitare tabelle fitte dentro il testo principale;
- se una tabella supera la leggibilita, spostarla in appendice o renderla strumento compilabile.

Linee e grafici:
- linee minimo 0.75 pt per stampa;
- grigi non troppo chiari;
- se stampato in bianco e nero, i riempimenti devono restare visibili.

## Immagini
Usare immagini solo se migliorano apprendimento o uso pratico:
- mappe concettuali;
- flowchart del procedimento;
- schemi Metodo BANDO;
- esempi di griglie compilate;
- screenshot annotati solo quando necessari;
- icone funzionali in tabelle e checklist.

Ogni immagine deve avere:
- titolo o didascalia;
- funzione didattica;
- eventuale fonte o nota di produzione;
- collegamento al capitolo.

Evitare:
- immagini stock generiche;
- foto decorative;
- grafiche a effetto senza funzione;
- immagini scure o poco leggibili.

## Logica didattica
Ogni doppia pagina deve idealmente rispondere a una domanda:

```text
Che cosa devo capire?
Perche mi serve nel concorso?
Come lo uso in prova?
Quale errore devo evitare?
Che output devo produrre?
```

Il testo deve alternare:
- spiegazione;
- selezione dei nuclei;
- esempio;
- esercizio;
- controllo errore.

## Regole per Manual Writer Agent
Quando il writer riceve `format`, `improve`, `integrate` o `expand`, deve applicare questo design system:
- non produrre blocchi lunghi senza sottotitoli;
- usare box ricorrenti quando aggiungono funzione;
- mantenere paragrafi brevi;
- trasformare teoria in strumenti;
- proporre immagini solo se hanno funzione didattica;
- indicare se un contenuto e' pronto per stampa, pronto per revisione o solo bozza.

## Stato
Questo file e' canonico per l'impaginazione e deve essere aggiornato se cambiano formato stampa, font o canale editoriale.
