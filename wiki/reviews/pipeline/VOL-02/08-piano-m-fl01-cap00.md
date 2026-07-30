---
id: review-pipeline-vol-02-step-08-m-fl01-cap00
type: pipeline_step_evidence
title: "Piano operativo step 08 - M-FL01 capitolo 00"
status: completed_for_manual_gate
volume_code: VOL-02
module_code: M-FL01
chapter: "00"
step: "08"
gate: chapter-plan
review_required: true
canonical: false
updated_at: 2026-07-30
---

# Piano operativo step 08 — M-FL01 capitolo 00

## Perimetro e funzione

Il target è `wiki/books/moduli/m-fl01-comuni-unioni/chapters/00-piano-editoriale.md`, la scheda editoriale del modulo M-FL01. Non è un capitolo didattico da riscrivere: definisce obiettivo, lettore, struttura, collegamenti, fonti e stato dei quattordici capitoli specialistici.

Nella pipeline VOL-02 il file va conservato come scheda di controllo del modulo. La scrittura e i gate didattici si applicano ai capitoli 01-14 di M-FL01, non al capitolo 00 come prosa destinata al lettore.

## Nuclei assegnati

- Identità del modulo: Funzioni Locali, Comuni e Unioni di Comuni.
- Trasferimento del Metodo BANDO dal VOL-01 al delta specialistico locale.
- Profili, prove e output: amministrativo, contabile, tecnico-amministrativo di interfaccia e servizi locali.
- Sequenza didattica dei capitoli 01-14.
- Collegamenti obbligatori a VOL-01, Struttura madre, Ricettario e architettura moduli.
- Pacchetto fonti: TUEL, finanza locale, entrate, servizi demografici/sociali, CAD/ANPR, SPL, SUAP, edilizia, contratti, MEPA e bandi VOL-02.

## Nuclei già completi

- Obiettivo, lettore e struttura prevista sono esplicitati.
- Il sommario operativo collega ciascun capitolo a funzione didattica e output prevalente.
- I capitoli 01-14 sono presenti e dichiarati in bozza professionale.
- I rinvii di perimetro a VOL-01, VOL-09 e VOL-10 sono già indicati.
- Il frontmatter dichiara `draft_stage: professional-draft-complete` e `review_required: true`, coerentemente con la matrice VOL-02.

## Nuclei da verificare o sviluppare

- Verificare che ogni capitolo 01-14 mantenga la promessa di teoria, applicazione, output e verifica della matrice.
- Controllare i rinvii a VOL-01: devono puntare a contenuti completi e non sostituire la teoria specialistica locale.
- Controllare i rinvii a VOL-09/VOL-10 per evitare duplicazioni o lacune su procurement avanzato, edilizia e lavori.
- Allineare gli output dei laboratori ai bandi target e ai relativi allegati.
- Eseguire review normativa umana su TUEL, contabilità locale, CAD/ANPR, servizi sociali, contratti, soglie e fonti regionali/locali.

## Sezioni da conservare

- Frontmatter e metadati di tracciabilità.
- Sezioni `Specifica struttura modulo`, `Collegamenti obbligatori`, `Fonti da consolidare`, `Testo editoriale`, `Sommario operativo`, `Capitoli di lavoro` e `Note di review`.
- Titoli, ordine e link dei capitoli 01-14, salvo correzioni chirurgiche documentate.
- Distinzione tra nucleo comune VOL-01 e delta locale specialistico.

## Duplicazioni da evitare

- Non replicare diritto costituzionale/amministrativo generale, pubblico impiego, trasparenza, privacy, CAD generale, inglese, informatica, logica e prove già coperte dal VOL-01.
- Non trasformare il capitolo 00 in un nuovo capitolo didattico.
- Non duplicare procurement avanzato, PNRR e lavori tecnici destinati a VOL-09/VOL-10.
- Non collocare materia regionale o di Polizia locale nel perimetro M-FL01.

## Esempi, casi, domande ed esercizi necessari

Il capitolo 00 non richiede casi propri. Deve però verificare che il piano dei capitoli 01-14 includa:

- tabella organo-competenza-atto e caso locale;
- caso su statuto/regolamento e laboratorio di atto;
- check-list procedimento/accesso e caso di istanza digitale;
- casi demografici, welfare e presa in carico;
- tavola obiettivo-risorsa-responsabile e caso contabile;
- caso entrata locale e check-list affidamento;
- simulazioni finali per i quattro profili comunali;
- domande da commissario, domanda-trappola, mini-esercizio e diario errori in ogni capitolo applicabile.

## Fonti da usare

- `sources/metodo-bando-progetto-editoriale.md`
- `sources/struttura-madre-il-metodo-bando.md`
- `sources/d-lgs-18-agosto-2000-n-267-enti-locali.md`
- `sources/ordinamento-finanziario-enti-locali-tuel-dup-peg-rendiconto-revisione.md`
- `sources/entrate-tributi-locali-patrimonio-riscossione-comunale.md`
- `sources/servizi-demografici-elettorali-anagrafe-stato-civile.md`
- `sources/servizi-sociali-educativi-enti-locali.md`
- `sources/ministero-interno-dait-anpr-finanza-locale.md`
- `sources/pa-digitale-cad-identita-documenti-servizi.md`
- `sources/codice-contratti-pubblici-d-lgs-36-2023-e-correttivo-209-2024.md`
- `sources/digitalizzazione-contratti-pubblici-anac-bdncp-fvoe-pcp.md`
- `sources/mepa-consip-acquisti-in-rete-strumenti-acquisto-negoziazione.md`
- `sources/bandi-inpa-vol-02-campione-2026.md`

## Struttura H1/H2/H3 e budget KDP

Il capitolo 00 conserva una struttura tecnica breve, non una nuova unità didattica:

- H1: Piano editoriale — M-FL01 Comuni e Unioni.
- H2: Specifica struttura modulo; Testo editoriale; Note di review.
- H3: Obiettivo; Lettore; Struttura prevista; Collegamenti obbligatori; Fonti da consolidare; Sommario operativo; Capitoli di lavoro.

Budget indicativo: 1.000-1.500 parole per la scheda, con tabelle compatte e leggibili in paperback KDP. Il budget didattico è invece assegnato ai capitoli 01-14, non al capitolo 00.

## Review umane richieste

- Responsabile normativo: verifica del testo vigente e delle fonti locali/regionali richiamate dai capitoli.
- Responsabile editoriale: verifica di perimetro, ordine, rinvii, output e coerenza con il Metodo BANDO.
- Verifica finale su bandi PDF, allegati, prove e profili target prima di promuovere gli stati `parziale` a `completo`.

## Esito operativo

Il piano è pronto per il gate manuale. Il gate CLI `chapter-plan` non è implementato: non va dichiarato automaticamente superato. La chiusura richiede `complete VOL-02 --step 08 --module M-FL01 --chapter 00 --accept --note ...` solo dopo la verifica umana di questa evidenza.
