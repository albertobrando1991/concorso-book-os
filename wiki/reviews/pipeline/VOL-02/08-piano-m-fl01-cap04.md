---
type: pipeline_step_evidence
volume: VOL-02
module: M-FL01
chapter: 04
step: 08
status: completed_for_manual_gate
updated_at: 2026-07-31
---

# Piano capitolo 04 — Deliberazioni, determinazioni, decreti, ordinanze e pareri

## Perimetro e funzione

Capitolo-ponte tra ordinamento e prova teorico-pratica (volume_chapter 7). Funzione: dare una grammatica pratica degli atti locali — non un formulario — per scegliere e motivare l'atto corretto collegandolo a competenza, funzione e procedimento.

Confini da presidiare:
- organi e competenze generali → cap. 01; fonti interne → cap. 02; organizzazione/uffici → cap. 03 (richiamato, non rispiegato);
- procedimento, protocollo, albo, URP, accesso → cap. 05 (il capitolo vi rinvia esplicitamente);
- bilancio, impegni, visti, controlli in esteso → capp. 09-10 (Nota di review);
- ordinanze di sicurezza urbana, igiene, viabilità, polizia locale → M-FL04 (Nota di review);
- modelli completi di deliberazione/determinazione/ordinanza → esclusi per scelta (Scheda di lavoro): solo riconoscere forma, soggetto, iter;
- teoria generale del provvedimento (motivazione, elementi, vizi) → VOL-01 (rinvio finale).

## Nuclei di modulo assegnati

| Nucleo (matrice `Atti`) | Dove vive |
|---|---|
| Deliberazioni consiliare e di Giunta | Sezioni dedicate + tabella atto-organo-funzione + caso guidato |
| Determinazione | Sezione dedicata (competenza, istruttoria, effetto) |
| Decreto sindacale e ordinanza | Sezioni dedicate (tre piani dell'ordinanza) |
| Pareri e visto di copertura | Sezioni dedicate + tabella presidi |
| Catena istruttoria | Sezione con tabella a 7 fasi |
| Errore di competenza | Domanda-trappola + Errore tipico + diario errori |

Output atteso della riga: "laboratorio atto locale" (sezione "Come scegliere l'atto corretto" + tabella applicazione rapida), "atto guidato" (caso guidato contributi culturali), "domanda-trappola/checklist" → tutti presenti.

## Sezioni da conservare (già buone)

Struttura completa e conforme: spec (6 nuclei), Scheda di lavoro, sezioni H3 canoniche, 6 tabelle operative (atto-organo-funzione, presidi, catena istruttoria, applicazione rapida, mini-esercizio + soluzione, diario errori), caso guidato con separazione dei piani, "Come rispondere all'orale" in 5 passaggi, Note di review corrette.

## Duplicazioni da evitare

- Non trasformare la sezione pareri/visto in trattazione di contabilità (capp. 09-10): restare sulla grammatica minima.
- Non anticipare il procedimento (cap. 05): la catena arriva a pubblicazione/esecuzione come fasi, senza disciplina di dettaglio.
- Mantenere il rinvio al cap. 03 per organizzazione/uffici invece di rispiegare responsabili e servizi.

## Esempi, casi, domande ed esercizi

- Caso guidato: contributi ad associazioni culturali (5 piani: regolamento → indirizzo → gestione → presidi contabili → pubblicazione) — da conservare.
- Tabella applicazione rapida traccia → atto: il "laboratorio" richiesto dalla spec.
- Mini-esercizio con soluzione (6 situazioni): verificare coerenza interna con le sezioni teoriche.

## Fonti da usare

Già in `source_refs` (6): TUEL, L. 241/1990, D.Lgs. 165/2001, ordinamento finanziario enti locali, dossier VOL-02, campione bandi. Uso corrente corretto; nessuna nuova fonte necessaria. Spec cita anche `[[topics/enti-locali]]`: verificare la coerenza tra riferimenti della spec e riferimenti finali (la lista finale usa la forma completa con dossier e campione: da allineare solo se necessario, senza perdere wikilink).

## Struttura H1/H2/H3 e budget

- H1 unico + H2 canoni + H3 numerati: conforme.
- `volume_chapter: 7` e `outline_section: 4` già allineati.
- Frontmatter completo; aggiornare solo `updated_at` e aggiungere la matrice a `last_compiled_from`.
- Budget KDP: 4.247 parole lorde, dentro il range orientativo 4.000–4.700; nessuna sfrondatura prevista.

## Interventi previsti (step 09–11)

1. Refusi di accento (step 09): "solidita" → "solidità"; "Se si," → "Se sì,"; "temporaneita" → "temporaneità"; "sviluppera" → "svilupperà"; "esecutivita" → "esecutività"; "trattera" → "tratterà".
2. Riga finale "Cfr. VOL-01 per..." → convertire in wikilink (step 09), come su capp. 01-03.
3. Domanda da commissario/trappola in formato `**Domanda:** / **Risposta:**` → uniformare al formato piano (step 11).
4. Aperture meccaniche "Il primo è / Il secondo è / Il terzo è" (determinazione, ordinanza, due estremi) → variare in pass humanizer (step 11).
5. Verifica copertura didattica riga `Atti` (step 10) e report revisione (step 12).

## Review umane richieste

- I refusi di accento sono correzioni oggettive, non scelte stilistiche.
- Review normativa (step 15): citazioni puntuali TUEL su pareri, visto, competenze degli organi, funzioni dirigenziali, decreti e ordinanze — il capitolo evita deliberatamente formule testuali non verificate.

## Esito operativo

Capitolo in buono stato: interventi leggeri (refusi, wikilink, formato domande, aperture elenchi), nessuna riscrittura strutturale. Il piano step 08 si chiude con accept manuale (gate non implementato) dopo verifica che il capitolo non è stato toccato in questo step.
