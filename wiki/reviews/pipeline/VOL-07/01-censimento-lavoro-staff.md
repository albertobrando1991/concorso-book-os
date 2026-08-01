---
id: review-vol-07-pipeline-01-censimento-lavoro-staff
type: review
title: "VOL-07 - Censimento sicuro del lavoro dello staff"
status: complete
domain: "concorsi pubblici italiani"
topics: ["pipeline editoriale", "catalogo volumi", "moduli specialistici"]
entities: ["Metodo BANDO", "ConcorsoBook OS"]
source_refs: ["sources/logica-volumi-copertura-concorsobook-v4.md", "sources/vol-07-dossier-fonti-materie-sanita-2026-07-28.md"]
book_refs: ["vol-07-sanita-amministrativa-professioni-sanitarie"]
confidence: 0.93
updated_at: 2026-07-28T14:45:00+02:00
created_at: 2026-07-28T14:45:00+02:00
review_required: false
canonical: false
tags: ["review", "pipeline", "vol-07", "staff-census"]
issue_type: staff_work_inventory
severity: medium
affected_pages: []
---

# VOL-07 - Censimento sicuro del lavoro dello staff

## Perimetro e metodo

Audit read-only eseguito per lo step 01 della pipeline VOL-07. Sono stati controllati catalogo applicativo, architettura a 12 volumi e 25 moduli, filesystem editoriale, frontmatter, planning, matrici, fonti, immagini, branch, worktree e differenze rispetto a `main`.

Non sono stati sovrascritti o integrati contributi. I README tecnici degli asset M-FC02 sono gli unici file Markdown nei moduli senza frontmatter: non sono pagine canoniche e non costituiscono un errore editoriale.

## Stato Git e provenienza

- Worktree principale: branch `main`, commit `ec50c19`, tre commit avanti a `origin/main`.
- Worktree pipeline: branch `vol-07-pipeline-start`, sette commit editoriali/tecnici avanti a `main` prima dello step 01.
- Modifica nel worktree pipeline: soltanto `pipeline/VOL-07/run-state.json`, prodotta dal CLI per gli step 00 e 01.
- File locale non tracciato in `main`: `.claude/settings.local.json`; appartiene all'utente, resta escluso da qualsiasi integrazione.
- Nessun altro worktree o branch locale concorrente rilevato.
- Nessuna versione concorrente dello stesso file rilevata fra worktree attivi.

## Tabella del lavoro disponibile

| Volume | Modulo | File | Autore/branch se rilevabile | Stato contenuto | Stato fonti | Stato immagini | Possibile collisione | Azione proposta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VOL-01 | Base PA | `books/il-metodo-bando/` | staff storico / `main` | utilizzabile, con review in corso | consolidate ma soggette a cut-off | patrimonio grafico presente | nessuna nel worktree VOL-07 | riusare con rinvii puntuali, non duplicare |
| VOL-02 | M-FL01 | `moduli/m-fl01-comuni-unioni/` (1 capitolo) | staff storico / `main` | da verificare: index `drafting`, filesystem ancora minimo | molte source note dichiarate | assenti nel modulo | log storico indica capitoli non presenti nel filesystem corrente | ricostruire provenienza prima di dichiarare il modulo scritto |
| VOL-02 | M-FL02 | `moduli/m-fl02-regioni-province-citta-metropolitane/` (1 capitolo) | staff storico / `main` | da verificare: index `drafting`, filesystem ancora minimo | corpus ampio dichiarato | assenti | stessa incoerenza fra log e filesystem | audit storico dedicato |
| VOL-02 | M-FL03 | `moduli/m-fl03-camere-commercio/` (1 capitolo) | staff storico / `main` | da completare | source note settoriali presenti | assenti | nessuna versione concorrente | sviluppare dopo matrice |
| VOL-02 | M-FL04 | `moduli/m-fl04-polizia-locale/` (1 capitolo) | staff storico / `main` | da completare | source note settoriali presenti | assenti | nessuna versione concorrente | sviluppare dopo matrice |
| VOL-03 | M-FC01 | `moduli/m-fc01-ministeri/` (15 capitoli, 6 front matter) | staff storico / `main` | utilizzabile, `source_ready` | source-ready; review puntuale necessaria | assenti | nessuna | consolidare e revisionare prima della pubblicazione |
| VOL-03 | M-FC02 | `moduli/m-fc02-agenzie-fiscali/` (16 capitoli, 3 planning, 6 front matter) | staff storico / `main` | da completare, `revised_draft` | matrice: 66 completi e 14 parziali | 15 PNG + 15 SVG | nessuna | chiudere i 14 blocker e audit visivo |
| VOL-03 | M-FC03 | `moduli/m-fc03-enti-non-economici/` (1 capitolo, 1 planning) | staff storico / `main` | da completare, benché `source_ready` | fonti dichiarate disponibili | assenti | stato più avanzato del contenuto effettivo | allineare status e sviluppare capitoli |
| VOL-04 | M-FC04 | `moduli/m-fc04-giustizia/` (1 capitolo) | staff storico / `main` | conflitto: index `drafting`, ma resta solo il piano | log storico cita capitoli non presenti | assenti | possibile lavoro non confluito o rimosso | ricostruire commit/provenienza prima di scrivere |
| VOL-05 | M-FC05 | `moduli/m-fc05-authority-indipendenti/` | scaffold / `main` | scaffold | sole fonti di architettura | assenti | nessuna | acquisire fonti e bandi |
| VOL-06 | M-IR01 | `moduli/m-ir01-scuola/` | scaffold / `main` | scaffold | sole fonti di architettura | assenti | nessuna | acquisire fonti e bandi |
| VOL-06 | M-IR02 | `moduli/m-ir02-universita-afam/` | scaffold / `main` | scaffold | sole fonti di architettura | assenti | nessuna | acquisire fonti e bandi |
| VOL-06 | M-IR03 | `moduli/m-ir03-enti-ricerca/` | scaffold / `main` | scaffold | sole fonti di architettura | assenti | nessuna | acquisire fonti e bandi |
| VOL-06 | M-IR04 | `moduli/m-ir04-cultura-beni-culturali/` | scaffold / `main` | scaffold | sole fonti di architettura | assenti | nessuna | acquisire fonti e bandi |
| VOL-07 | M-SA02 | `moduli/m-sa02-professioni-sanitarie/` | `vol-07-pipeline-start` | scaffold prioritario | dossier censito; fonti ufficiali non consolidate | assenti | nessuna | audit bandi e fonti, poi matrice del modulo |
| VOL-07 | M-SA01 | `moduli/m-sa01-sanita-amministrativa/` | `vol-07-pipeline-start` | scaffold prioritario 2 | dossier censito; fonti ufficiali non consolidate | assenti | nessuna | audit bandi e fonti, poi matrice del modulo |
| VOL-07 | M-SA03 | `moduli/m-sa03-dirigenza-medica-sanitaria/` | `vol-07-pipeline-start` | scaffold prioritario 3 | dossier censito; fonti ufficiali non consolidate | assenti | nessuna | audit bandi e fonti, poi matrice del modulo |
| VOL-07 | M-SA04 | `moduli/m-sa04-tecnici-sanitari-prevenzione/` | `vol-07-pipeline-start` | scaffold prioritario 4 | dossier censito; fonti ufficiali non consolidate | assenti | nessuna | audit bandi e fonti, poi matrice del modulo |
| VOL-08 | M-TR01 | `moduli/m-tr01-ict-trasformazione-digitale/` | scaffold / `main` | scaffold | sole fonti di architettura | assenti | nessuna | acquisire fonti e bandi |
| VOL-09 | M-TR02 | `moduli/m-tr02-appalti-pnrr-fondi-ue/` | scaffold / `main` | scaffold | sole fonti di architettura | assenti | nessuna | riconciliare con capitoli procurement presenti altrove |
| VOL-10 | M-TR03 | `moduli/m-tr03-tecnico-ingegneristico/` | scaffold / `main` | scaffold | sole fonti di architettura | assenti | nessuna | acquisire fonti e bandi |
| VOL-11 | M-TR04 | `moduli/m-tr04-ambiente-protezione-civile/` | scaffold / `main` | scaffold | sole fonti di architettura | assenti | nessuna | acquisire fonti e bandi |
| VOL-12 | M-SP01 | `moduli/m-sp01-forze-ordine/` | scaffold / `main` | scaffold | sole fonti di architettura | assenti | nessuna | acquisire fonti e bandi |
| VOL-12 | M-SP02 | `moduli/m-sp02-vigili-fuoco/` | scaffold / `main` | scaffold | sole fonti di architettura | assenti | nessuna | acquisire fonti e bandi |
| VOL-12 | M-SP03 | `moduli/m-sp03-magistratura-avvocatura-notariato/` | scaffold / `main` | scaffold | sole fonti di architettura | assenti | nessuna | acquisire fonti e bandi |
| VOL-12 | M-SP04 | `moduli/m-sp04-prefettizia-diplomatica/` | scaffold / `main` | scaffold | sole fonti di architettura | assenti | nessuna | acquisire fonti e bandi |

## Materiali VOL-07 non ancora presenti in `main`

Il branch `vol-07-pipeline-start` contiene, rispetto a `main`:

- raw immutabile e source note del dossier;
- volume aggregator e quattro documenti di planning;
- aggiornamenti agli otto scaffold di M-SA01/M-SA02/M-SA03/M-SA04;
- topic sanitario e cinque entity page istituzionali;
- scheda e run-state della pipeline;
- due correzioni all'orchestratore con test di regressione;
- traccia LocalAgentMemory, indice e log aggiornati.

Questi file formano un unico pacchetto coerente. Non devono essere copiati selettivamente senza conservare source note, matrice, run-state e test.

## Gap e decisioni

1. VOL-07 non contiene ancora capitoli specialistici: i quattro `00-piano-editoriale.md` sono scaffold.
2. Le 74 voci dell'inventario non equivalgono a 74 fonti consolidate.
3. Le 48 righe specialistiche della matrice sono tutte `mancante`; nessuna è pubblicabile.
4. Non esistono immagini, quiz o report specialistici VOL-07 da preservare.
5. Il file locale `.claude/settings.local.json` non deve essere aggiunto, spostato o sovrascritto.
6. Le incoerenze storiche di M-FL01/M-FL02/M-FC04 sono fuori dal perimetro di modifica VOL-07 e vengono soltanto segnalate.

## Esito del gate manuale

Ogni contributo rilevato ha una destinazione o una decisione esplicita. Non risultano collisioni irrisolte sul perimetro VOL-07. Il lavoro può passare al consolidamento controllato dello step 02 senza integrare contributi esterni inesistenti.
