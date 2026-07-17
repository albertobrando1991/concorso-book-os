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

## Architettura editoriale Metodo BANDO
La linea prodotto canonica e' a tre livelli:

1. Libro principale `books/il-metodo-bando/`: volume autonomo con metodo, materie comuni, prove, adattamento ai profili e kit finale.
2. Ricettario operativo digitale `books/il-metodo-bando/ricettario-digitale.md`: capitoli 25-47 riclassificati come protocolli, schede, casi, checklist e laboratori.
3. Moduli specialistici `books/moduli/`: percorsi separati per famiglia concorsuale, lavorabili dalla dashboard come libri autonomi.

Regole per i moduli specialistici:
- La tassonomia canonica e' `books/moduli/architettura-moduli-specialistici.md`.
- Ogni modulo deve stare in `books/moduli/<module-id>/` con `index.md` e capitoli in `chapters/`.
- Il `book_id` dei capitoli deve coincidere con lo slug della cartella modulo.
- Ogni modulo deve dichiarare `module_code`, `module_family`, `companion_to: il-metodo-bando` e `draft_stage`.
- I moduli non duplicano il nucleo comune del libro principale: applicano il Metodo BANDO a profili, prove, materie specialistiche e rischi della famiglia.
- La logica vincolante di copertura e sviluppo e' [[sources/logica-volumi-copertura-concorsobook-v4]]: comune solo in VOL-01, famiglia nel relativo specialistico, sottoprofilo in appendice/verticale necessario, altra famiglia tramite rinvio senza duplicazioni. Per il catalogo e le riconciliazioni dei 25 moduli usare anche [[books/moduli/architettura-moduli-specialistici]].
- Prima della scrittura finale servono source notes consolidate, topic/entity pages collegate e review umana per norme settoriali, sanita e carriere speciali.
- La promessa pubblica corretta e': riusabile, aggiornabile, modulare. Evitare formule come copertura totale garantita o aggiornamento automatico.

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

## Memoria agentica locale
La memoria locale del progetto deve restare sempre attiva nel contesto ConcorsoBook OS, salvo disattivazione tecnica esplicita per debug.

Regole:
- Prima di generare output AI, richiamare le memorie pertinenti da `wiki/memory/agent/l1/atoms.jsonl` tramite il servizio `LocalAgentMemory`.
- Dopo chat Hermes, import fonti, writer o altri flussi agentici, catturare una traccia sintetica della conversazione in memoria.
- La memoria conserva preferenze, istruzioni operative, workflow ricorrenti, decisioni e risultati utili a migliorare gli output successivi.
- La memoria e' condivisa da tutti gli agenti/provider usati nel progetto: Codex/GPT, Claude, Kimi, OpenAI API, Hermes e writer locale.
- Ogni nuovo agente deve riusare `LocalAgentMemory` e lo store `wiki/memory/agent/`; non deve creare memorie parallele scollegate.
- La memoria non sostituisce il wiki consolidato: per norme, date, fonti e claim editoriali restano vincolanti `sources/`, `topics/` ed `entities/`.
- Ogni memoria richiamata deve essere considerata suggerimento operativo contestuale, non fonte normativa.
- La preferenza utente stabile e': ricordare sempre cio' che e' stato detto nel contesto ConcorsoBook OS e usare la memoria per migliorare progressivamente gli output.

## Manual Writer Agent
Il Manual Writer Agent e' l'agente specializzato nella scrittura effettiva dei capitoli. Deve comportarsi come elaboratore editoriale, non come semplice generatore di testo.

Regole:
- Deve usare `books/il-metodo-bando/struttura-madre.md` come guida operativa canonica per ogni sviluppo del manuale.
- Deve applicare `books/il-metodo-bando/design-system-editoriale.md` per formato, gerarchia, box, font, layout e logica workbook.
- Deve leggere la nota capitolo selezionata e rispettare la sezione `Specifica struttura madre` prima di generare o integrare testo.
- Per ogni capitolo di volume o modulo deve applicare la scheda di copertura v4: famiglia, profilo, B-PA gia' nel base, specialistico, eventuale sottoprofilo, rinvio cross-family, pacchetto minimo ed esclusioni. La stessa verifica vale per integrazioni e revisioni: non duplicare il B-PA, non collocare materie nella famiglia sbagliata e non creare verticali non necessari.
- Legge solo `sources/`, `topics/`, `entities/`, `quizzes/` e capitoli esistenti.
- Il cervello wiki e' la base obbligatoria della conoscenza: source notes, topic pages, entity pages, struttura madre, design system, capitoli e quiz vengono sempre prima.
- Non legge mai direttamente `raw/` per produrre testo editoriale finale.
- Deve scrivere capitoli effettivi destinati al lettore, non riepiloghi del sistema, non note tecniche, non descrizioni del lavoro svolto.
- Quando servono dati aggiornati o verifica normativa corrente, deve usare ricerca web come supporto di aggiornamento, non come scorciatoia: le fonti web rilevanti vanno trasformate in source notes consolidate e collegate al wiki prima di diventare conoscenza stabile del capitolo.
- Scrive solo dentro `books/`.
- In modalita `draft` aggiorna la sezione `Bozza agente`.
- In modalita `integrate`, `format`, `improve`, `expand` aggiorna la sezione `Testo editoriale`.
- Deve preservare tracciabilita: ogni blocco deve indicare riferimenti consolidati usati.
- Deve mantenere stile workbook Metodo BANDO: apertura editoriale, obiettivo, mappa BANDO, spiegazione, box "da sapere in 5 righe", caso guidato, domanda da commissario, domanda-trappola, mini-esercizio, errore tipico, riferimenti, note di review.
- Deve scrivere in modo impaginabile: paragrafi brevi, titoli non orfani, tabelle leggibili in pagina A4, box autonomi e note layout solo quando servono alla revisione visiva.
- Deve rispettare la gerarchia tipografica canonica di collana: H1 Arial Bold 18-20 pt, H2 Arial Bold 14 pt, H3 Arial Bold 12 pt, corpo Garamond Regular 11 pt con interlinea 1,15-1,20, tabelle/quiz/schemi/box Arial 9,5-10 pt. La regola vale per tutti i volumi, moduli, integrazioni e revisioni.
- Non deve mai produrre formule come "Aggiornamento generato", "Istruzione ricevuta" o riepiloghi delle fonti al posto del capitolo.
- Deve integrare nuova conoscenza senza cancellare il lavoro umano preesistente fuori dalle sezioni gestite.
- Provider consigliato: `WRITER_PROVIDER=codex`, che usa `codex exec` locale e la skill di progetto `.agents/skills/concorso-book-professional-writer/SKILL.md`.
- Provider supportati con memoria condivisa: `codex`, `claude`, `kimi`, `openai`, `hermes`, `local`.
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
- Il formato operativo canonico per dashboard, revisione ed export di lavoro di `Il Metodo BANDO` e' A4 verticale, testo giustificato, pagine singole numerate, corpo Garamond 11 pt, titoli Arial Bold 20/14/12 pt, tabelle/quiz/schemi/box Arial 9,5-10 pt, colonna singola, box operativi ricorrenti e strumenti compilabili. Il 17 x 24 cm resta solo eventuale formato commerciale compatto finale.
- Separare note canoniche da note di lavoro.
- Richiedere review umana per interpretazioni normative puntuali.
- Per il libro `Il Metodo BANDO`, l'outline base e' Parte I Orientarsi, Parte II Materie comuni, Parte III Allenamento, Parte IV Sistema adattabile, Appendici/tool.
- Ogni strumento cartaceo deve essere completo anche senza sito; QR code e digitale devono aggiungere velocita, tracking o aggiornamenti.

## Revisore Editoriale Totale
Il Revisore Editoriale Totale e' la skill globale per la revisione finale pre-pubblicazione di libri, moduli e manuali.

Regole:
- La skill e' in `.agents/skills/revisore-editoriale-totale/SKILL.md` con riferimenti in `references/`.
- E' globale e condivisa da tutti i provider: `codex`, `claude`, `kimi`, `openai`, `hermes`, `local`.
- Si attiva quando un modulo o libro e' completato e deve essere revisionato prima della pubblicazione.
- Copre 30 controlli su 4 livelli: struttura (macro), capitolo (meso), frase/paragrafo (micro), superficie.
- Usa la checklist `references/checklist-30-punti.md` come criterio oggettivo.
- Usa il template `references/template-report.md` come formato fisso del report.
- L'agent server e' `src/server/agents/editorial-reviewer-agent.ts`.
- L'endpoint API e' `POST /api/editorial-reviewer/run`.
- Il pannello dashboard e' `app/components/editorial-reviewer-panel.tsx`.
- Il risultato include: sintesi editoriale, tabella errori per gravita, osservazioni per capitolo, giudizio di pubblicabilita motivato, contenuto da verificare, suggerimenti facoltativi, priorita degli interventi e limiti della revisione.
- Il revisore non riscrive il testo: segnala, spiega il motivo, propone una correzione concreta. L'autore decide.
- Per ogni volume o modulo il revisore applica anche [[sources/logica-volumi-copertura-concorsobook-v4]] prima della checklist a 30 punti: segnala come errore grave duplicazioni B-PA, materia nella famiglia errata o lacune su materie ricorrenti/pesate; verifica rinvii cross-family, necessita' di verticali e congruenza del pacchetto minimo.
- I report di revisione sono salvati in `wiki/reviews/` e loggati in `log.md`.

## Gate globale di copertura didattica integrale

La regola canonica e' [[sources/principio-copertura-didattica-integrale-2026-07-17]]. Il Metodo BANDO organizza la teoria richiesta e la trasforma in performance concorsuale, ma non la sostituisce.

Regole non negoziabili:
- ogni concetto promesso deve essere spiegato oppure rinviato con destinazione precisa, completa e verificata;
- progressione logica, completezza, accuratezza delle definizioni, autonomia didattica, coerenza promessa-contenuto, esempi, casi e verifiche sono requisiti globali;
- ogni volume/modulo mantiene una matrice con materia, concetti, fonti, collocazione, teoria, applicazione, output, verifica, stato e review normativa;
- per ogni nucleo si coprono, quando applicabili, definizione, funzione, inquadramento, elementi, distinzioni, conseguenze, esempio/caso, modalita d'esame, errore tipico, verifica e fonti;
- `solo-nominato` e `mancante` sono bloccanti; `parziale` non e' pubblicabile; `rinviato` richiede destinazione precisa e completa;
- la formula "il candidato deve sapere/riconoscere/distinguere" crea una promessa formativa verificabile;
- la guida operativa non sostituisce la copertura teorica e la lunghezza non dimostra completezza;
- il Revisore Editoriale Totale classifica i nuclei e tratta promessa non mantenuta, rinvio generico e autonomia insufficiente come errori gravi.
