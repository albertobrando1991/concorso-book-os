# ConcorsoBook OS Agent Schema

## Obiettivo del sistema
ConcorsoBook OS mantiene una knowledge base persistente in stile LLM Wiki per scrivere e aggiornare progressivamente libri per concorsi pubblici italiani. Il libro e' una proiezione editoriale del wiki consolidato, non un file separato dalla conoscenza.

## North star prodotto
Il riferimento prodotto canonico e' [[sources/metodo-bando-progetto-editoriale]]. Ogni scelta editoriale deve partire dal Metodo BANDO: libro-workbook autonomo, sistema pratico per preparare concorsi diversi, digitale come ottimizzatore opzionale e non come sostituto.

Regole non negoziabili:
- Il libro non e' l'ennesimo manuale materia + quiz.
- Il libro insegna a leggere un bando, costruire un piano, studiare materie comuni e allenarsi su output reali.
- La promessa e': preparare molti concorsi senza ricominciare da zero ogni volta.
- Ogni capitolo deve contenere metodo, mappa, esercizio, errore tipico o tool compilabile quando possibile.
- Le materie sono funzionali alla prova e al metodo, non enciclopedia.

## Struttura cartelle
- `raw/`: sorgenti immutabili. Nessun agente deve modificarle dopo ingest.
- `sources/`: una source summary note per ogni fonte.
- `topics/`: pagine cumulative per argomento.
- `entities/`: enti, normative, procedure, istituti, autori.
- `books/`: master note, outline, capitoli, appendici, revisioni.
- `quizzes/`: quiz, recall, errori frequenti.
- `reviews/`: lint, conflict reports, gap analysis.
- `templates/`: modelli frontmatter e contenuto.
- `dashboards/`: export markdown dello stato sistema.
- `logs/`: log tecnici granulari.
- `index.md`: catalogo navigabile del wiki.
- `log.md`: log cronologico append-only.

## Naming conventions
- Usare slug kebab-case ASCII per file e ID.
- Usare `source-*`, `topic-*`, `entity-*`, `chapter-*`, `review-*` come prefissi ID.
- Una pagina canonica per concetto. Le note di lavoro devono avere `canonical: false`.
- Le raw sources conservano il nome slug della fonte e restano nel sottofolder di tipo.

## Frontmatter standard
Campi minimi:

```yaml
id:
type:
title:
status:
domain:
topics: []
entities: []
source_refs: []
book_refs: []
confidence:
updated_at:
created_at:
review_required:
canonical:
tags: []
```

Campi specifici:
- Source notes: `source_type`, `source_url`, `source_date`, `authority_level`.
- Topic notes: `parent_topics`, `child_topics`, `chapter_refs`.
- Book chapters: `book_id`, `outline_section`, `draft_stage`, `last_compiled_from`.
- Review notes: `issue_type`, `severity`, `affected_pages`.

## Policy di ingest
1. Salvare la fonte in `raw/` e non modificarla piu'.
2. Creare una source summary in `sources/`.
3. Estrarre metadata, topic, entita e livello di autorevolezza.
4. Creare o aggiornare topic/entity pages.
5. Aggiornare `index.md`.
6. Appendenre evento a `log.md`.
7. Identificare libri e capitoli impattati.
8. Marcare i capitoli come `review_required` o `to_expand`.
9. Produrre artifact di verifica.

## Policy di aggiornamento
- Preferire patch chirurgiche su heading e frontmatter.
- Aggiornare solo sezioni interessate: `Sintesi`, `Fonti`, `Capitoli collegati`, `Stato revisione`, `Note editoriali`.
- Non cancellare lavoro editoriale precedente senza registrare una revisione.
- Quando una nuova fonte migliora un topic, appendere il delta e aggiornare i riferimenti.

## Policy di linking interno
- Ogni source note deve linkare topic ed entita rilevate.
- Ogni topic deve linkare source notes, entita e capitoli collegati.
- Ogni capitolo deve linkare topic e source notes consolidate.
- Ogni claim importante deve essere tracciabile a una o piu' source notes.

## Policy per index.md e log.md
- `index.md` deve essere rigenerabile e contenere cataloghi per sources, topics, entities e books.
- `log.md` e' append-only. Non correggere eventi passati; aggiungere un evento di rettifica.

## Workflow di query
- Rispondere partendo da topic pages, entity pages e source summaries.
- Usare raw sources solo per audit o verifica, mai come output finale.
- Segnalare esplicitamente bassa confidenza o revisione umana richiesta.

## Manual Writer Agent
Il Manual Writer Agent e' l'agente specializzato nella scrittura effettiva dei capitoli. Deve comportarsi come elaboratore editoriale, non come semplice generatore di testo.

Regole:
- Legge solo `sources/`, `topics/`, `entities/`, `quizzes/` e capitoli esistenti.
- Non legge mai direttamente `raw/` per produrre testo editoriale finale.
- Scrive solo dentro `books/`.
- In modalita `draft` aggiorna la sezione `Bozza agente`.
- In modalita `integrate`, `format`, `improve`, `expand` aggiorna la sezione `Testo editoriale`.
- Deve preservare tracciabilita: ogni blocco deve indicare riferimenti consolidati usati.
- Deve mantenere stile workbook Metodo BANDO: apertura editoriale, obiettivo, mappa BANDO, spiegazione, box "da sapere in 5 righe", caso guidato, domanda da commissario, domanda-trappola, mini-esercizio, errore tipico, riferimenti, note di review.
- Deve integrare nuova conoscenza senza cancellare il lavoro umano preesistente fuori dalle sezioni gestite.
- Provider consigliato: `WRITER_PROVIDER=codex`, che usa `codex exec` locale e la skill di progetto `.agents/skills/concorso-book-professional-writer/SKILL.md`.
- Modello obbligatorio per scrittura: `CODEX_WRITER_MODEL=gpt-5.5` con `CODEX_WRITER_REASONING_EFFORT=xhigh`.
- Se Codex CLI non e' autenticato, il writer deve usare fallback locale tracciabile e segnalare l'avviso.

## Workflow di lint
- Trovare pagine senza inbound link.
- Trovare topic citati ma mancanti.
- Trovare capitoli con fonti insufficienti.
- Trovare fonti a bassa affidabilita.
- Segnalare claim potenzialmente obsoleti o conflittuali.

## Regole editoriali
- Un capitolo finale non deve mai derivare solo da una raw source.
- Ogni capitolo deve includere obiettivo didattico, spiegazione, punti chiave, riferimenti, esempi, errori frequenti e quiz collegati.
- La scrittura e' incrementale: integrare, chiarire e migliorare senza distruggere lavoro precedente.
- Separare note canoniche da note di lavoro.
- Richiedere review umana per interpretazioni normative puntuali.
- Per il libro `Il Metodo BANDO`, l'outline base e' Parte I Orientarsi, Parte II Materie comuni, Parte III Allenamento, Parte IV Sistema adattabile, Appendici/tool.
- Ogni strumento cartaceo deve essere completo anche senza sito; QR code e digitale devono aggiungere velocita, tracking o aggiornamenti.
