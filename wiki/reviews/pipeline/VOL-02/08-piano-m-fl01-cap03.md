---
type: pipeline_step_evidence
volume: VOL-02
module: M-FL01
chapter: 03
step: 08
status: completed_for_manual_gate
updated_at: 2026-07-30
---

# Piano capitolo 03 — Organizzazione comunale: uffici, servizi e gestioni associate

## Perimetro e funzione

Secondo capitolo operativo del modulo (volume_chapter 6). Funzione: far capire come il Comune funziona dentro — uffici, servizi, responsabili, gestioni associate — con occhio da utente della pratica e da candidato. Il capitolo arriva dopo perimetro/ordinamento (cap. 01) e statuto/regolamenti (cap. 02); precede gli atti (cap. 04).

Confini da presidiare:
- organi e indirizzo-gestione → cap. 01;
- statuto/regolamenti/programmazione → cap. 02;
- atti (deliberazioni/determinazioni) in sé → cap. 04;
- procedimento, protocollo, albo, URP → cap. 05 (il capitolo stesso vi rinvia);
- servizi pubblici locali avanzati e affidamenti → cap. 12 / VOL-09 (solo confine);
- CCNL, incarichi, dettagli di dirigenza → solo rinvio fonte (già in Note di review).

## Nuclei di modulo assegnati

| Nucleo (matrice `Organizzazione`) | Dove vive |
|---|---|
| Segretario | Sez. 3 + tabella + caso guidato (Fase 1) |
| Direttore/dirigenza | Sez. 3 + tabella |
| Uffici e servizi | Sez. 4 + tabella servizi/output |
| Gestioni associate | Sez. 5 + tabella piano/soggetto + caso guidato (Unione tributi) |
| Responsabile del procedimento | Sez. 6 + tabella D (flusso pratica) + mappa ufficio→procedimento→atto |

Output atteso della riga: "mappa ufficio → procedimento → atto, caso organizzativo, esercizio" → tutti presenti (mappa a 6 colonne + esempio, caso guidato in 4 fasi, mini-esercizio con soluzione).

## Sezioni da conservare (già buone)

Struttura completa e conforme: spec (6 nuclei + Note sui confini), Scheda di lavoro, sezioni H3 canoniche con 6 tabelle operative (etichette organizzative, piano/soggetto gestioni associate, servizi/output, flusso pratica, mappa ufficio→procedimento→atto + esempio), caso guidato su Unione/tributi, mini-esercizio con soluzione, diario errori, checklist, Note di review corrette, collegamento capitolo 2 nel formato canonico.

## Duplicazioni da evitare

- Non trasformare la sezione gestioni associate in trattazione dei servizi pubblici locali (è cap. 12/VOL-09): restare sul piano delle forme associative.
- Non anticipare gli atti: la mappa arriva fino a "atto" come etichetta, senza spiegare deliberazione/determinazione (cap. 04).
- Mantenere i rinvii espliciti a capp. 01 e 05 invece di rispiegare.

## Esempi, casi, dimostrazioni

- Caso guidato: pratica tributaria gestita in Unione (4 fasi con attori e errori da evitare) — da conservare; verifica che il collegamento al cap. 02 (statuto Unione) resti solo funzionale.
- Tabella mappa + esempio riga-per-riga (pratica edilizia): il "modo operativo" richiesto dalla spec.
- Mini-esercizio con soluzione: verificare la soluzione solo per coerenza interna.

## Fonti da usare

Già in `source_refs` (8): `ordinamenti/tuel-testo-unico-enti-locali`, `ordinamenti/dlgs-165-2001-pubblico-impiego`, `ordinamenti/dlgs-201-2022-riordino-enti-locali`, `ordinamenti/statuto-regolamenti-programmazione-fonti`, `dossier_vol02_da_leggere`, `campione_bandi_enti_locali`, `glossario_unificato`, `mappa_nuclei_trasversali`. Uso corrente corretto; nessuna nuova fonte necessaria.

## Struttura H1/H2/H3 e budget

- H1 unico + H2 canoni + H3 numerati: conforme.
- `volume_chapter` e `outline_section` già allineati.
- Frontmatter completo; aggiornare solo `updated_at`.
- Budget KDP: peso da verificare con conteggio parole (stima ~4.300, dentro il range 4.000–4.700); se superiore, valutare micro-sfrondature.

## Interventi previsti (step 09–11)

1. Refuso: "Il capitolo successivo entera" → "entrerà" (linea ~85).
2. Riga finale "Riferimenti consolidati: Cfr. VOL-01..." → convertire in wikilink (come fatto su cap. 01/02).
3. Domanda-trappola in formato `**Domanda:** / **Trappola:**` → uniformare al formato piano nel pass humanizer (step 11).
4. Verifica copertura didattica (step 10) e report revisione (step 12).

## Review umane richieste

- Il refuso "entera" va corretto (non una scelta stilistica: è un errore).
- L'uniformazione del formato domande segue la decisione già presa sul cap. 01/02.

## Esito operativo

Capitolo in buono stato: interventi leggeri (refuso, wikilink, formato domande), nessuna riscrittura strutturale. Il piano step 08 si chiude con accept manuale (gate non implementato) dopo verifica che il capitolo non è stato toccato in questo step.
