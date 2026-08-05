# Standard globale — Indice studente e piano editoriale staff

## Stato e decisione approvata

La dashboard dei volumi deve distinguere in modo strutturale:

1. l'indice del libro destinato allo studente;
2. il piano editoriale e lo stato della pipeline destinati allo staff.

La regola nasce dal controllo del VOL-07, ma diventa uno standard valido per tutti i volumi e per tutti i moduli specialistici. Non è ammesso esporre nel libro commerciale note consolidate, piani, matrici, prompt, review o altri artefatti interni.

## Problema verificato nel VOL-07

La lista corrente contiene:

- sei sezioni di front matter generate;
- quattro aperture di modulo generate;
- tre capitoli editoriali reali;
- quattro file `00-piano-editoriale.md` classificati erroneamente come capitoli.

Sono inoltre presenti difetti nei dati visibili:

- `Sanita` al posto di `Sanità` nel catalogo e nei metadati dei moduli;
- assenza di `outline_section: 3` nel capitolo M-SA02/03;
- formati non uniformi per codice modulo, trattino, numero e titolo;
- capitoli pianificati e capitoli scritti non distinguibili nella dashboard.

## Contratto per il lettore

La lista principale della dashboard e l'anteprima commerciale mostrano esclusivamente:

- front matter pubblicabile o generato;
- apertura dei moduli inclusi nel volume;
- capitoli editoriali realmente esistenti;
- eventuali appendici esplicitamente destinate al lettore.

Non mostrano:

- piani editoriali;
- matrici di copertura;
- prompt e artefatti della pipeline;
- review, verbali, checklist di controllo interno;
- source note o riferimenti che presuppongano accesso al wiki dello staff;
- segnaposto per capitoli non ancora scritti.

L'indice del lettore resta quindi fedele al prodotto disponibile in quel momento e non promette contenuti ancora assenti.

## Contratto per lo staff

La dashboard espone una sezione separata, denominata `Piano editoriale staff`, non inclusa nell'anteprima del libro.

Per ogni modulo la sezione mostra:

- codice e titolo normalizzati;
- capitoli dichiarati dalla specifica della pipeline;
- stato `da pianificare`, `da scrivere`, `in lavorazione`, `scritto`, `in revisione` o `completato`;
- prossimo step e gate, quando disponibili;
- presenza o assenza del file editoriale;
- eventuale modulo preparato ma privo di capitoli formalmente dichiarati.

I capitoli non ancora dichiarati non vengono inventati. M-SA03 e M-SA04, nello stato attuale, saranno quindi presentati come moduli con copertura preparatoria disponibile e capitoli ancora da dichiarare.

La fonte dello stato deve essere il modello canonico della pipeline e il relativo run-state, mai una copia manuale dei prompt o un'interpretazione del testo formattato del CLI.

## Modello dei dati

`BookStudioData.chapters` continua a rappresentare soltanto le sezioni leggibili del libro.

La risposta del Book Studio aggiunge una struttura separata, indicativamente `editorialPlan`, composta da moduli e target editoriali. Questa struttura non viene convertita in `BookStudioChapter` e non partecipa a:

- conteggio delle pagine;
- indice analitico;
- sommario commerciale;
- selezione del capitolo attivo;
- anteprima PDF o stampa;
- conteggio dei capitoli scritti del libro.

La generazione del piano staff deve funzionare anche quando non esiste ancora un run-state: in quel caso mostra soltanto ciò che è formalmente dichiarato nella specifica editoriale.

## Classificazione e collocazione dei file

I piani editoriali appartengono a:

`wiki/books/moduli/<module-id>/planning/00-piano-editoriale.md`

Non appartengono a `chapters/`.

La migrazione riguarda tutti i moduli del repository che usano il vecchio percorso `chapters/00-piano-editoriale.md`, con aggiornamento atomico di wikilink, test e riferimenti interni.

Come protezione per repository non ancora migrati, il caricatore del Book Studio esclude dalla lista pubblica i documenti riconoscibili come piano tramite percorso, tipo o tag canonico. La compatibilità legacy è una rete di sicurezza, non il nuovo formato da continuare a usare.

## Standard dei titoli visibili

Per tutte le stringhe destinate al lettore o allo staff:

- gli accenti italiani sono obbligatori: `Sanità`, `priorità`, `qualità`, `responsabilità`, `contabilità`, `accessibilità`;
- codici e titoli sono separati con il trattino lungo: `M-SA01 — Sanità amministrativa`;
- i capitoli sono mostrati come `Capitolo 03 — Titolo`, mantenendo lo zero iniziale nella UI editoriale;
- il frontmatter `title` e l'H1 non contengono il numero del capitolo: la numerazione proviene soltanto da `outline_section`;
- ID, slug, nomi dei file, tag tecnici e chiavi macchina restano ASCII e non vengono rinominati per aggiungere accenti;
- non sono ammesse sequenze mojibake come `Ã`, `Â` o caratteri sostitutivi nelle stringhe visibili.

Il primo intervento editoriale applica questo standard a tutte le stringhe visibili del VOL-07. I test e le regole di caricamento lo rendono vincolante per gli altri volumi.

## VOL-07 dopo la correzione

L'indice studente mostra:

- le sei sezioni iniziali generate;
- l'apertura M-SA01 e il capitolo 04;
- l'apertura M-SA02 e i capitoli 01 e 03;
- le aperture M-SA03 e M-SA04 senza falsi capitoli interni.

Il piano staff mostra inoltre:

- M-SA01: capitoli 04, 05, 06, 09 e 10 con il rispettivo stato;
- M-SA02: capitoli 01 e 03 con il rispettivo stato;
- M-SA03 e M-SA04: moduli preparati, senza capitoli ancora dichiarati.

Il capitolo `03-discipline-professionali-autonomia-responsabilita.md` riceve `outline_section: 3`.

## Allineamento dello staff

La guida operativa dello staff deve chiarire che:

- `chapters/` contiene esclusivamente testo destinato al lettore;
- `planning/` contiene materiali di progettazione e controllo;
- un capitolo entra nel piano staff soltanto dopo la dichiarazione canonica nella pipeline;
- un capitolo entra nell'indice studente soltanto quando esiste come file editoriale;
- lo stato viene aggiornato tramite CLI e non modificando manualmente `run-state.json`;
- l'anteprima commerciale non è uno strumento di ispezione degli artefatti interni.

La stessa regola viene integrata nelle istruzioni agentiche e nella documentazione della pipeline, così agenti e persone seguono un unico contratto.

## Compatibilità e migrazione

La migrazione deve:

1. inventariare tutti i `chapters/00-piano-editoriale.md`;
2. spostarli nella corrispondente cartella `planning/`;
3. aggiornare ogni riferimento verificato;
4. mantenere invariati ID e contenuto, salvo correzioni di punteggiatura e accenti visibili;
5. non modificare manualmente alcun run-state;
6. non dichiarare nuovi capitoli o nuovi step;
7. produrre errori espliciti se due file collidono nella destinazione.

## Test e gate

La modifica richiede almeno:

- test del Book Studio: i piani non appaiono in `chapters`;
- test del volume commerciale: il piano staff resta separato dall'indice studente;
- test dello stato staff con target esistente, target assente e modulo senza target;
- test di ordinamento numerico dei capitoli;
- test del numero 03 di M-SA02;
- test delle stringhe visibili contro accenti mancanti noti e mojibake;
- test di migrazione o controllo repository che vieti nuovi `chapters/00-piano-editoriale.md`;
- test di regressione per volumi non specialistici e moduli aperti singolarmente;
- suite completa, typecheck e `git diff --check`;
- `pipeline doctor`, `status --json` e gate pertinenti sul VOL-07.

## Sequenza di rilascio

1. Introdurre i test del contratto globale.
2. Separare nel modello dati indice studente e piano staff.
3. Applicare filtro e compatibilità legacy.
4. Migrare i piani editoriali di tutti i moduli.
5. Correggere metadati, numerazione, accenti e punteggiatura del VOL-07.
6. Aggiornare dashboard e documentazione dello staff.
7. Verificare regressioni e stato pipeline.
8. Riprendere lo step 10 già aperto per M-SA01/04.

## Fuori perimetro

- Scrittura anticipata di capitoli non dichiarati.
- Creazione di titoli per M-SA03 o M-SA04 senza una decisione editoriale.
- Pubblicazione o congelamento di capitoli che non hanno superato i gate.
- Modifica manuale del run-state.
- Riscrittura indiscriminata dei testi dei capitoli: l'audit linguistico di questa attività riguarda titoli, etichette e liste visibili.
