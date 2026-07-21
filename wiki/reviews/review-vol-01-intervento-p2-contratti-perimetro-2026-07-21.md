---
id: review-vol-01-intervento-p2-contratti-perimetro-2026-07-21
type: review
title: "VOL-01 - Verifica P2 su contratti pubblici e perimetro specialistico"
status: completed
domain: "concorsi pubblici italiani"
topics: ["revisione normativa", "contratti pubblici", "anti-duplicazione", "copertura didattica"]
entities: ["VOL-01", "D.Lgs. 36/2023", "D.Lgs. 209/2024", "M-TR01", "M-TR02"]
source_refs: ["sources/codice-contratti-pubblici-d-lgs-36-2023-e-correttivo-209-2024.md", "sources/capitolo-9-corpus-fonti-ufficiali-contratti-pubblici-2026-05-26.md", "sources/logica-volumi-copertura-concorsobook-v4.md"]
book_refs: ["il-metodo-bando", "m-tr01-ict-trasformazione-digitale", "m-tr02-appalti-pnrr-fondi-ue"]
confidence: 0.95
updated_at: 2026-07-21T14:20:00+02:00
created_at: 2026-07-21T14:20:00+02:00
review_required: false
canonical: true
issue_type: editorial_review
severity: high
affected_pages: ["capitolo 8", "capitolo 9", "capitolo 10"]
tags: ["revisore-editoriale-totale", "vol-01", "follow-up", "normativa", "perimetro"]
---

# Report editoriale - Il Metodo BANDO (intervento P2)

## 1. Sintesi editoriale

- Genere editoriale: manuale-workbook per concorsi pubblici italiani.
- Pubblico target: candidati generalisti e amministrativi che devono acquisire il nucleo comune senza confonderlo con la preparazione specialistica.
- Perimetro: E05, E06 ed E07 del report professionale, con intervento diretto sul Capitolo 9 e audit delle destinazioni specialistiche dei Capitoli 8 e 10.
- Esito: E07 e' risolto come disallineamento della fonte e del lessico; E05 ed E06 restano aperti perche' M-TR01 e M-TR02 sono scaffold e non possono ricevere rinvii che promettano contenuto inesistente.
- Gate: il conteggio resta 2 nuclei `completo` e 15 `parziale`.

## 2. Punti applicati della checklist

Sono stati applicati tutti i 30 punti della checklist al perimetro esaminato: struttura reale, completezza, progressione, gerarchia, pubblicabilita, coerenza interna e fra capitoli, terminologia, spiegazioni, definizioni, accuratezza concettuale e normativa, esempi, tabelle, apparato delle fonti, sintassi, chiarezza, tono, stile didattico, ripetizioni, contraddizioni, grammatica, ortografia, punteggiatura, refusi, uniformita grafica, resa Markdown, layout, leggibilita e qualita complessiva.

Il punto 27 resta limitato al sorgente editoriale: non e' stato esaminato un PDF finale. Il gate didattico e' stato applicato anche ai rinvii: una destinazione soltanto pianificata non vale come contenuto esistente.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravita | Evidenza e intervento | Stato |
|---|---|---|---|---|---|
| E05 | Capitolo 8 | Perimetro | Grave | Le sezioni locali, universitarie, economico-patrimoniali e PNRR superano il nucleo essenziale. Le destinazioni locali e M-TR02 contengono soltanto piani editoriali; un taglio ora produrrebbe una promessa non mantenuta. | Aperto; trasferimento subordinato alla scrittura delle destinazioni |
| E06 | Capitolo 10 | Perimetro | Grave | Reti, SQL, programmazione e cybersicurezza avanzata appartengono al delta ICT, ma M-TR01 e' ancora `scaffold` con il solo capitolo `00-piano-editoriale`. | Aperto; separazione subordinata alla scrittura di M-TR01 |
| E07 | Capitolo 9 | Accuratezza normativa | Grave | La source note canonica e il capitolo sono stati riallineati al D.Lgs. 36/2023 nel testo vigente al 30 giugno 2026. Il D.Lgs. 209/2024 e' ora qualificato come correttivo rilevante, non come ultimo aggiornamento disponibile. | Risolto per fonte e lessico |
| E07-A | Capitolo 9 | Claim mobili | Media | L'inventario non rileva valori numerici di soglie o termini fissati nel testo; il capitolo prescrive la verifica alla data del concorso. Il flusso BDNCP-FVOE-PCP e' coerente con la pagina ufficiale ANAC aggiornata il 29 settembre 2025. | Verificato nel perimetro generale |
| E07-B | Capitolo 9 | Gate normativo | Grave | Non e' stata svolta una certificazione giuridica articolo per articolo di ogni istituto, allegato e disciplina transitoria. `review_required` e' stato attivato sul capitolo e sul corpus. | Aperto e bloccante per la pubblicazione |

## 4. Osservazioni per capitolo

### Capitolo 8 - Contabilita pubblica essenziale

- Punti di forza: il nucleo comune su bilancio, entrate, spese, residui, controlli e responsabilita e' autonomo e didatticamente applicato.
- Criticita: la parte avanzata e' gia scritta nel base, mentre le destinazioni specialistiche non lo sono. La migrazione deve conservare il testo e avvenire solo dopo la creazione di capitoli effettivi nei volumi o moduli riceventi.
- Correzione collaterale: il richiamo al Codice dei contratti e' stato aggiornato alla formula `D.Lgs. 36/2023 nel testo vigente`.

### Capitolo 9 - Contratti pubblici essenziali

- Punti di forza: ciclo, soggetti, procedure, esecuzione, strumenti digitali e verifiche sono completi per il livello base.
- Intervento: aggiornata la fonte canonica, datata la verifica, corretti obiettivo, sezione fonti, sintesi e glossario; mantenuta la prudenza sulle soglie mobili.
- Criticita residua: prima della pubblicazione serve una review giuridica puntuale e datata.

### Capitolo 10 - Informatica, PA digitale e competenze digitali

- Punti di forza: il lettore dispone gia di definizioni, distinzioni, esempi e verifiche.
- Criticita: il livello base e quello ICT avanzato sono mescolati. Non e' stato introdotto un rinvio a M-TR01 come sostituto, perche' il modulo non contiene ancora il testo promesso.

## 5. Coerenza globale

- Terminologia normativa: `testo vigente` e `correttivo di particolare rilievo` sostituiscono la formula fuorviante che fermava l'aggiornamento al 2024.
- Coerenza fra fonti e capitolo: source note, corpus, Capitolo 9 e richiamo contabile usano ora la stessa regola.
- Anti-duplicazione: la decisione preserva il contenuto esistente e impedisce rinvii vuoti. Il trasferimento futuro dovra essere atomico: destinazione completa, verifica, sostituzione nel base e matrice aggiornata.
- Promesse formative: nessuna promessa e' stata dichiarata chiusa sulla sola esistenza di uno scaffold.

## 6. Contenuto da verificare

- Soglie, termini, deroghe, allegati e regole transitorie del D.Lgs. 36/2023 alla data del bando e prima della pubblicazione.
- Effetti puntuali degli atti successivi al D.Lgs. 209/2024 sui singoli istituti trattati.
- Scrittura effettiva dei capitoli riceventi per contabilita locale/settoriale, PNRR, reti, SQL, programmazione e cybersicurezza.
- Corrispondenza dei futuri rinvii a heading stabili e contenuti completi.

## 7. Suggerimenti facoltativi (non errori)

- Aggiungere alla pipeline editoriale un campo `normative_checked_at` distinto da `updated_at`.
- Generare un report automatico dei riferimenti normativi con anno e data dell'ultima verifica.
- Conservare nei moduli specialistici un box iniziale che elenchi esplicitamente il core riusato dal VOL-01.

## 8. Priorita degli interventi

1. Eseguire la review giuridica articolo per articolo del Capitolo 9.
2. Scrivere prima le destinazioni specialistiche M-TR01 e M-TR02, quindi migrare gli approfondimenti senza perdita di contenuto.
3. Definire le destinazioni complete della contabilita locale e settoriale nei volumi pertinenti.
4. Rieseguire matrice, test, preview e controllo PDF dopo ogni migrazione.

## 9. Giudizio di pubblicabilita

**Non pubblicabile allo stato attuale.**

E07 e' chiuso come difetto di fonte e formulazione, ma il Capitolo 9 conserva un gate giuridico esplicito. E05 ed E06 restano bloccanti: il volume contiene approfondimenti fuori perimetro e le destinazioni specialistiche non sono ancora pronte. La matrice resta quindi a 2 nuclei `completo` e 15 `parziale`.

## 10. Limiti di questa revisione

- Il controllo normativo certifica fonte, data di vigenza, lessico generale e claim mobili inventariati; non costituisce parere legale ne' certificazione articolo per articolo.
- La pagina ANAC e' stata usata per la struttura dell'ecosistema digitale, non per sostituire il testo normativo.
- Non sono stati spostati o cancellati approfondimenti dai Capitoli 8 e 10 perche' le destinazioni non contengono ancora testo completo.
- Non e' stato esaminato un PDF finale.
