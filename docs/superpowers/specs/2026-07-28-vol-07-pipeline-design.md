# VOL-07 — Ingest delle fonti e avvio della pipeline editoriale

## Stato del disegno

- Approvato dall'utente il 28 luglio 2026.
- Approccio scelto: sviluppo progressivo completo.
- Responsabile normativo: Alberto Brando.
- Responsabile editoriale: Alberto Brando.
- Data di chiusura iniziale delle fonti: 2026-07-28.
- Ordine dei moduli: M-SA02, M-SA01, M-SA03, M-SA04.

## Obiettivo

Acquisire nel wiki il dossier:

`C:\Users\info\OneDrive\Desktop\# VOL-07 – Sanità amministrativa e.txt`

e usarlo come input canonico di pianificazione per costruire e avviare, tramite il CLI previsto da `AGENTS.md`, la pipeline editoriale di `VOL-07 — Sanità amministrativa e professioni sanitarie`.

Il dossier contiene il perimetro del volume, i quattro moduli, i profili, le materie richieste, la mappa delle fonti specialistiche, le decisioni di copertura, un indice di quindici capitoli, le appendici e i gap da risolvere. Non è però una fonte normativa primaria: orienta ingest, acquisizione e copertura, mentre ogni documento normativo o professionale deve essere verificato e consolidato separatamente.

## Input verificato

- File: `# VOL-07 – Sanità amministrativa e.txt`
- Dimensione: 43.588 byte.
- Righe: 631.
- Ultima modifica rilevata: 2026-07-28 00:17:17, fuso locale.
- SHA-256: `4045E18DE2B1AC2B0760047821D48683934321C98499E3A5446481769E0C2466`.
- Moduli coperti: M-SA01, M-SA02, M-SA03, M-SA04.

Il nome reale usa il trattino lungo `–`; le varianti del percorso con due spazi non identificano il file presente sul Desktop.

## Principi vincolanti

1. `VOL-07` è un solo libro commerciale articolato nei quattro moduli interni già censiti.
2. Il volume aggiunge il delta sanitario e non duplica le materie B-PA del VOL-01.
3. Il dossier viene conservato immutabile in `wiki/raw/` e sintetizzato in una source note.
4. Il testo finale può usare soltanto source notes, topic pages ed entity pages consolidate, mai direttamente il file raw.
5. Ogni materia promessa deve essere spiegata oppure rinviata a una destinazione precisa, completa e verificata.
6. Gli stati `mancante`, `solo-nominato` e `parziale` bloccano l'avanzamento editoriale.
7. Le norme sanitarie, le discipline professionali e le interpretazioni puntuali richiedono review umana.
8. Il run-state viene creato e aggiornato soltanto dal CLI; non va modificato manualmente.

## Architettura dei contenuti

### Dossier e fonte editoriale

Il file esterno viene copiato senza modifiche in:

`wiki/raw/business/vol-07-sanita-amministrativa-professioni-sanitarie-2026-07-28.txt`

La copia deve conservare l'impronta SHA-256 dell'originale. La source note del dossier viene creata in `wiki/sources/` con:

- natura di dossier editoriale e di copertura;
- autorevolezza distinta dalle fonti normative primarie;
- collegamenti a VOL-07 e a M-SA01–M-SA04;
- `review_required: true`;
- sintesi di perimetro, materie, fonti candidate, indice e gap;
- indicazione esplicita che le fonti elencate devono essere acquisite e verificate.

### Aggregatore di volume

Viene creato:

`wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/`

con almeno:

- `index.md`;
- `planning/00-scheda-pipeline.md`;
- `planning/01-dossier-source-ready.md`;
- `planning/02-matrice-copertura-didattica.md`.

L'aggregatore descrive il libro e compila i quattro moduli. I capitoli editoriali restano nei percorsi dei moduli già esistenti:

- `wiki/books/moduli/m-sa02-professioni-sanitarie/`;
- `wiki/books/moduli/m-sa01-sanita-amministrativa/`;
- `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/`;
- `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/`.

Le fasi A e B stabiliscono l'assegnazione univoca dei quindici capitoli proposti, evitando la duplicazione del nucleo sanitario comune e dei contenuti del VOL-01.

## Mappa delle fonti

La sezione `OUTPUT A` del dossier è integralmente acquisita come inventario di fonti candidate. Non viene ridotta ai tre collegamenti presenti nelle note finali.

L'inventario comprende:

- 11 righe di normativa primaria;
- 13 righe di normativa secondaria e regolamenti;
- 3 fonti di contrattazione collettiva;
- 10 famiglie di soft law e linee guida;
- 9 aree giurisprudenziali da censire;
- 14 portali o organismi operativi;
- 4 bandi già nominati e ulteriori cluster da acquisire;
- 10 categorie di manualistica e dottrina.

I conteggi descrivono le righe e le categorie del dossier, non un numero di documenti unici già consolidati. Duplicazioni, rinvii e discipline superate devono essere riconciliati durante l'audit.

Ogni voce riceve almeno:

| Campo | Funzione |
| --- | --- |
| ID | Identificatore stabile |
| Categoria | Normativa, contratto, soft law, giurisprudenza, bando, fonte operativa o dottrina |
| Estremi | Titolo, numero, data o descrizione disponibile |
| Autorità | Ente emanante o autore |
| URL ufficiale | Collegamento privo di parametri di tracking |
| Moduli | M-SA01–M-SA04 interessati |
| Materie | Nuclei didattici supportati |
| Stato | `da_acquisire`, `da_verificare`, `consolidata`, `superata` o `rinviata_VOL-01` |
| Review | Necessità e responsabile della verifica |

Le tre note URL finali del dossier sono soltanto punti di partenza espliciti per Legge 833/1978, Legge 24/2017 e CCNL Comparto Sanità 2019–2021. Tutte le altre voci restano incluse nell'inventario anche quando il dossier non fornisce un URL.

Le fonti generali già consolidate per il VOL-01 non vengono duplicate: la matrice deve registrare un rinvio puntuale alla source note esistente.

## Matrice delle materie

La matrice globale collega ogni materia richiesta mediante la catena:

`modulo → profilo → fonte → capitolo → teoria → applicazione → output → verifica → stato`

Deve coprire:

- nucleo sanitario comune;
- materie specifiche di M-SA01;
- materie specifiche di M-SA02;
- materie specifiche di M-SA03;
- materie specifiche di M-SA04;
- prove concorsuali per profilo;
- appendici e verticali;
- esclusioni e rinvii verso VOL-01, VOL-08, VOL-09, VOL-10 e VOL-11.

Ogni modulo mantiene anche una matrice autonoma coerente con quella globale.

## Strategia della pipeline

### Prima apertura: fasi A e B

La prima versione della scheda dichiara:

```yaml
volume_code: VOL-07
volume_title: Sanità amministrativa e professioni sanitarie
cut_off_date: 2026-07-28
responsabile_normativo: Alberto Brando
responsabile_editoriale: Alberto Brando
writer_provider: codex
phases: [A, B]
```

Ordine dei moduli:

1. M-SA02;
2. M-SA01;
3. M-SA03;
4. M-SA04.

Le fasi A e B producono il censimento, il perimetro, l'architettura, l'indice definitivo, l'assegnazione dei capitoli e le matrici. Gli step manuali vengono chiusi con `--accept --note` soltanto dopo una verifica documentata. Lo step 07 deve superare il gate di copertura.

### Seconda apertura: fasi C, D e F

Dopo la creazione dei capitoli e delle matrici, la scheda viene estesa a:

```yaml
phases: [A, B, C, D, F]
```

`npm run pipeline -- sync VOL-07` aggiunge gli step senza modificare manualmente il run-state.

Per ogni capitolo:

`08 piano → 09 scrittura → 10 copertura → 11 Humanizer → 12 revisione`

Per ogni modulo:

`13 revisione trasversale → 14 correzioni → 15 review umana → 16 text freeze`

Per il volume:

`21 revisione finale → 22 preflight → 23 consegna`

La fase E, dedicata a immagini e impaginazione, è esclusa dall'avvio iniziale e viene pianificata dopo il text freeze.

## Gestione dei blocchi

La pipeline si ferma quando:

- una fonte necessaria non è acquisita o verificata;
- una norma vigente non è stata riconciliata con una disciplina superata;
- una materia è `parziale`, `solo-nominato` o `mancante`;
- un rinvio non ha una destinazione precisa;
- un capitolo introduce claim non tracciati;
- manca la review umana richiesta;
- un gate automatico non passa;
- un gate manuale non ha evidenza sufficiente per l'accettazione.

Nessun blocker viene aggirato modificando il run-state o dichiarando verde un gate non eseguito.

## Verifiche

Prima dell'inizializzazione:

1. verificare che la copia raw abbia lo stesso SHA-256 dell'originale;
2. controllare frontmatter, percorsi e wikilink introdotti;
3. installare le dipendenze mancanti con `npm ci`;
4. eseguire `npm run pipeline -- doctor`;
5. eseguire i test della pipeline e il typecheck;
6. verificare il diff Git e preservare `.claude/settings.local.json`.

Avvio:

1. `npm run pipeline -- init VOL-07 --json`;
2. `npm run pipeline -- status VOL-07 --json`;
3. controllare che il run-state sia stato generato dal CLI;
4. `npm run pipeline -- next VOL-07 --json`;
5. leggere il prompt renderizzato e rispettarne il contratto.

## Criterio di pipeline avviata

La pipeline è avviata quando:

1. il dossier è conservato in raw e rappresentato da una source note;
2. l'intera mappa delle fonti e delle materie è registrata nell'inventario e nella matrice;
3. `doctor` non presenta blocker;
4. VOL-07 dispone di un run-state valido per le fasi A e B;
5. `next VOL-07 --json` ha preso in carico lo step 00;
6. il prompt canonico dello step 00 è stato generato ed è pronto per l'esecuzione.

Questo traguardo non implica che tutte le fonti siano già consolidate né che i capitoli siano scritti. Implica che gap, responsabilità, ordine e gate sono tracciati e che il primo step può essere eseguito senza bypass.

## Fuori perimetro iniziale

- Scrittura anticipata dei capitoli prima delle matrici e delle source notes.
- Duplicazione integrale delle materie generali del VOL-01.
- Manuali clinici completi o verticali professionali esterni al corpo comune.
- Calcolo di frequenze statistiche da un campione di bandi insufficiente.
- Immagini, impaginazione e preflight grafico prima del text freeze.
- Pubblicazione o dichiarazione di completezza con gap normativi o didattici aperti.
