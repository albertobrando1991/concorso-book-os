---
id: pipeline-vol-12-00-presa-in-carico
type: pipeline_review
title: "VOL-12 — Step 00: presa in carico e regole operative"
volume_code: VOL-12
step: "00"
phase: A
scope: catalog
domain: "concorsi pubblici italiani"
updated_at: 2026-08-11T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "step-00"]
---

# VOL-12 — Step 00: presa in carico e regole operative

## Target identificato

**VOL-12 — Carriere speciali premium**, tier `premium`, terza ondata di lancio. Quattro moduli della famiglia Carriere Speciali, nell'ordine di priorità M-SP01, M-SP02, M-SP03, M-SP04.

Il target è identificato con certezza: il codice `VOL-12` compare in `src/catalog/text-volumes.ts`, nell'architettura canonica dei moduli e nella dashboard di copertura, con la stessa composizione di moduli in tutte e tre le sedi.

## File canonici coinvolti

**Volume aggregatore (creato in questo step-set):**

- `wiki/books/volumi/vol-12-carriere-speciali-premium/index.md`
- `wiki/books/volumi/vol-12-carriere-speciali-premium/planning/00-scheda-pipeline.md`

**Moduli:**

| Modulo | index | piano editoriale | capitoli |
| --- | --- | --- | ---: |
| M-SP01 | `wiki/books/moduli/m-sp01-forze-ordine/index.md` | `planning/00-piano-editoriale.md` | 0 |
| M-SP02 | `wiki/books/moduli/m-sp02-vigili-fuoco/index.md` | `planning/00-piano-editoriale.md` | 0 |
| M-SP03 | `wiki/books/moduli/m-sp03-magistratura-avvocatura-notariato/index.md` | `planning/00-piano-editoriale.md` | 0 |
| M-SP04 | `wiki/books/moduli/m-sp04-prefettizia-diplomatica/index.md` | `planning/00-piano-editoriale.md` | 0 |

**Riferimenti canonici:**

- `wiki/books/moduli/architettura-moduli-specialistici.md`
- `src/catalog/text-volumes.ts`
- `wiki/dashboards/copertura-didattica-globale.md`
- `wiki/templates/prompt-staff-revisione-completa-volumi.md`
- `docs/superpowers/specs/2026-08-10-vol-12-pipeline-completa-design.md`
- `docs/superpowers/plans/2026-08-10-vol-12-pipeline-completa.md`

## Memoria richiamata

LocalAgentMemory è presente e popolata: `wiki/memory/agent/l1/atoms.jsonl` conta 710 atomi, con `l2/scenarios.md` e `l3/persona.md` disponibili. Le occorrenze di VOL-12 in memoria si riferiscono alla progettazione della pipeline dell'agosto 2026, non a contenuti editoriali dei moduli M-SP.

Nessuna memoria operativa esiste per il contenuto di M-SP01/02/03/04: sono moduli mai scritti. La memoria non è una fonte normativa e non viene usata come tale.

## Stato Git

Branch `main`. Il worktree contiene un numero rilevante di modifiche preesistenti **non correlate a VOL-12**, riferite principalmente a VOL-01/Book Studio (`app/components/`, `src/book/pagination.ts`, `src/server/book/book-preview.ts`, `scripts/export-book-studio-volume-pdf.mjs`) e ai capitoli dei moduli M-FL01 e M-FL02.

Queste modifiche sono state preservate integralmente. Nessun reset, checkout distruttivo o cancellazione è stato eseguito.

Modifiche introdotte da questo intervento, tutte limitate al perimetro VOL-12:

- 8 file di scaffold dei quattro moduli M-SP (riscritti);
- `wiki/books/moduli/architettura-moduli-specialistici.md` (1 riga, titolo M-SP01);
- `src/catalog/text-volumes.ts` (2 righe, `audience` VOL-12 e `description` del pacchetto premium);
- 2 file nuovi del volume aggregatore;
- `pipeline/VOL-12/run-state.json` (generato dal CLI, mai modificato a mano).

## Rischi e collisioni

| # | Rischio | Gravità | Mitigazione adottata |
| --- | --- | --- | --- |
| 1 | Il volume non ha alcun capitolo: ~55-60 capitoli e ~280.000 parole da produrre | alta | la scheda dichiara le sole fasi A-B e nessun capitolo; i capitoli reali li determinano gli audit 05-07 |
| 2 | Zero fonti specialistiche consolidate: nessuna source note per la famiglia Carriere Speciali | alta | gate agli step 06; nessun claim normativo può entrare nei capitoli senza source note verificata |
| 3 | `src/catalog/text-volumes.ts` è toccato anche da lavoro preesistente sul worktree | media | modifica limitata a due stringhe della sola voce VOL-12 e della regola `premium` |
| 4 | Quattro moduli con scheletro identico produrrebbero capitoli sovrapponibili | media | scheletri differenziati per modulo, con nucleo comune esplicitato e orizzonti di studio distinti |
| 5 | M-SP03 aggrega tre selezioni eterogenee in un modulo solo | media | architettura a tre binari dichiarata nell'index e nel piano editoriale; vincolo riportato nella scheda di pipeline |
| 6 | Perimetro M-SP01 ambiguo tra forze di polizia e Forze armate | risolta | Forze armate escluse esplicitamente; titolo, copertura e architettura riallineati |
| 7 | `audience` di catalogo prometteva «alta dirigenza», non coperta da alcun modulo | risolta | rimossa dalla voce VOL-12 e dalla descrizione del pacchetto premium |

## Piano operativo

Strettamente limitato all'incarico, nell'ordine imposto dal CLI:

1. **Step 00** — presa in carico (questo documento).
2. **Step 01-03** — censimento del lavoro di staff, consolidamento dei contributi, riconciliazione del catalogo. Lavoro interno al repository, senza fonti esterne.
3. **Step 04** — impostazione di volume.
4. **Step 05-07 × 4 moduli** — audit dei bandi, audit delle fonti e matrici di copertura. **Richiedono ricerca su fonti primarie ufficiali** con cut-off 2026-08-10 e review umana: è il gate reale della fase B e non può essere superato con fonti dedotte.
5. Estensione della scheda a `phases: [A, B, C, D, E, F]` con i capitoli approvati, poi `sync`.
6. **Step 08-23** — produzione, revisione, impaginazione e preflight, capitolo per capitolo.
7. **Step 24** — unico sign-off umano. Non autoaccettabile.

## Vincoli confermati

- Non si usa `wiki/raw/` come fonte del testo editoriale finale.
- Non si inventano norme, articoli, date, dati o fonti.
- Non si dichiara completo un contenuto con nuclei parziali o solo nominati.
- `pipeline/VOL-12/run-state.json` non viene modificato a mano.
- Ogni gate non automatizzato richiede verifica manuale reale prima della chiusura.
