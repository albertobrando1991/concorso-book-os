---
id: design-system-editoriale-il-metodo-bando
type: book_design_system
title: "Design system editoriale - Il Metodo BANDO"
status: canonical
domain: "concorsi pubblici italiani"
topics: ["book design","typography","manual layout","workbook","metodo bando"]
entities: ["Metodo BANDO","Bando Decoder","Manual Writer Agent"]
source_refs: ["sources/book-layout-typography-standards.md","sources/struttura-madre-il-metodo-bando.md","sources/metodo-bando-progetto-editoriale.md","sources/vol-01-il-metodo-bando-struttura-2026-07-14.md"]
book_refs: ["il-metodo-bando"]
confidence: 0.92
updated_at: 2026-07-14T19:00:00+02:00
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

## Aggiornamento layout editoriale
Il riferimento operativo aggiornato e' il documento:

```text
G:\Il mio Drive\PROGETTO CAPITALE PERSONALE SITO\PROG_LIBRO_CAPITALE PERSONALE\proposta_layout_editoriale_metodo_bando.docx
```

Decisione applicata:
- impostare il libro come **manuale premium-workbook**;
- usare un master A4 verticale per scrittura, revisione e anteprima;
- derivare dal master il formato commerciale compatto 17 x 24 cm;
- mantenere il colore pagina gia' in uso nella preview;
- adottare Source Serif 4 per il corpo e Source Sans 3 per titoli, box e strumenti; Playfair Display resta limitato alle aperture di capitolo e agli elementi display;
- usare palette controllata Navy, Bordeaux, Muted Gold, Off-White e Rich Black;
- usare template ricorrenti riconoscibili: Ancora, Valore, Caso pratico, Diario, Profilo;
- conservare margini ottimizzati per legatura, leggibilita e workbook.

## Formato fisico consigliato
Formato editoriale operativo attuale per master e preview:

```text
A4 verticale
210 x 297 mm
```

Motivo:
- rende verificabili pagina, margini, tabelle, immagini e strumenti nella dashboard;
- sostiene un volume articolato con ritmo da manuale-workbook;
- lascia spazio a box, tabelle compilabili, griglie e pagine operative.

Formato commerciale compatto derivato:

```text
17 x 24 cm circa
KDP equivalente: 6.69 x 9.61 in
```

Motivo:
- conserva una proporzione editoriale professionale;
- viene generato solo dopo il controllo del master, con una nuova verifica di riflusso, tabelle, immagini, vedove e orfani.

Formato alternativo per edizione molto pratica/workbook:

```text
7 x 10 in
```

Usarlo solo se aumentano molto schede compilabili, griglie, tabelle e immagini e non si vuole mantenere A4.

## Margini e gabbia
Per il formato editoriale 16,8 x 24 / 17 x 24:

```text
interno/gutter: 18 mm
esterno: 16 mm
alto: 17 mm
basso: 20 mm
area testo: colonna singola
target riga: 58-64 caratteri medi
```

Per il formato A4 di revisione interna:

```text
interno/gutter: 20 mm
esterno: 18 mm
alto: 18 mm
basso: 22 mm
area testo: colonna singola
```

Per una variante 17 x 24 cm con dorso molto spesso, solo se la tipografia richiede piu sicurezza lato legatura:

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
- la preview dashboard deve essere paginata in singole pagine A4, con footer e numerazione;
- il testo corrente deve essere giustificato, con sillabazione italiana, vedove/orfani controllati e titoli non lasciati soli a fine pagina;
- tabelle larghe possono usare pagina piena o orientamento dedicato solo in appendice/PDF.

Bleed:
- default: no bleed per il corpo libro;
- usare bleed solo per pagine speciali con grafica a piena pagina;
- se anche una sola pagina interna richiede bleed, preparare l'intero file secondo le regole di bleed della piattaforma di stampa.

## Font
Scelta applicata:

```text
Corpo testo: Source Serif 4
Titoli, box, tabelle e workbook: Source Sans 3
Aperture capitolo e titoli display: Playfair Display, con uso limitato
Fallback corpo: Charter, Georgia, Times New Roman, serif
Fallback sans: Segoe UI, Arial, sans-serif
```

Motivo:
- Source Serif 4 garantisce una lettura lunga piu naturale;
- Source Sans 3 distingue istruzioni, dati, liste e procedure;
- Playfair Display costruisce autorevolezza nelle sole aperture;
- non introdurre altri font e non usare piu di tre pesi nella stessa pagina.

Alternative premium per impaginazione finale:
- Minion Pro per corpo;
- Myriad Pro o Source Sans 3 per titoli e box.

## Dimensioni tipografiche stampa
Corpo principale:

```text
Source Serif 4 Regular 10-10,5 pt
interlinea: 12,5-13,2 pt
spazio dopo paragrafo: 3-5 pt
allineamento: giustificato nella preview/PDF con sillabazione controllata
```

Titoli:

```text
H1 capitolo: 24-30 pt Playfair Display Semibold/Bold
H2 sezione: 15-17 pt Source Sans 3 Bold
H3 blocco operativo: 10-12 pt Source Sans 3 Semibold/Bold
Didascalie: 8-9 pt Source Sans 3
Note/fonti: 8-9 pt Source Sans 3
Tabelle/workbook: 7,5-8,5 pt Source Sans 3
```

Riga:

```text
target: 58-64 caratteri medi per riga
limite accettabile: 45-75 caratteri
```

## Dimensioni digitali/dashboard
Preview dashboard:

```text
formato pagina: A4 verticale
corpo: circa 13 px Source Serif 4
line-height: 1.45
larghezza testo: max 64ch
spaziatura paragrafo: 0.55-0.65rem
```

Il digitale deve restare accessibile: il layout non deve rompersi se il lettore aumenta interlinea o spaziatura.

## Gerarchia pagina capitolo
Ogni capitolo deve seguire questa architettura visiva:

1. Numero capitolo.
2. Titolo chiaro e orientato al bisogno.
3. Barra BANDO del capitolo.
4. Promessa/obiettivo del capitolo.
5. Mappa BANDO del capitolo.
6. Spiegazione principale in blocchi brevi.
7. Box operativi.
8. Caso guidato o esempio.
9. Domande e mini-esercizi.
10. Errori frequenti.
11. Riferimenti consolidati.
12. Note di review.

Numero capitolo:
- usare Muted Gold come micro-accento;
- non superare il 3-5% della pagina interna.

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
- Navy Dark `#0F172A`: aperture di parte, header, titoli istituzionali, dorso;
- Rich Black `#020617`: testi scuri e profondita;
- Aged Paper `#E7DDC4`: copertina, workbook, box concettuali, mai come unico colore pagina se la preview ha gia un colore stabilito;
- Bordeaux `#7A2430`: CTA, griglie BANDO, casi pratici, errori e azioni;
- Muted Gold `#D4AF37`: filetti, numeri, parole chiave, separatori;
- Off-White `#F8FAFC`: schemi, mappe, respiro e pagine dense.

Limiti:
- oro come micro-accento: 3-5% interno, massimo 10% copertina;
- bordeaux massimo 5-8% nella pagina;
- Navy dominante solo nelle pagine-segnale.

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

## Infografiche pre-epilogative
Nei capitoli densi o nei blocchi che chiudono un argomento principale, prevedere una **infografica pre-epilogativa** prima di `Da sapere in 5 righe`, `Caso guidato`, `Domanda da commissario` o `Mini-esercizio`.

Funzione:
- ricomporre i concetti studiati in una mappa unica;
- aiutare il candidato a vedere nessi, sequenze e differenze;
- preparare il passaggio dalla teoria all'output di prova;
- offrire una pagina o mezza pagina riutilizzabile nel ripasso.

Formato consigliato:
- titolo breve e didattico;
- massimo 5-7 nodi o passaggi;
- palette Navy/Bordeaux/Muted Gold con grigi leggibili anche in bianco e nero;
- didascalia che spieghi come usare lo schema;
- collegamento al capitolo e al blocco che sintetizza.

Non inserire infografiche pre-epilogative quando il blocco e' gia breve, quando ripetono una mappa iniziale senza aggiungere orientamento, o quando comprimono testo in modo illeggibile.

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
