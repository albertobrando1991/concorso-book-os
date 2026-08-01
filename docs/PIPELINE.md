# Pipeline editoriale — guida operativa

Esegue il protocollo dei 25 prompt su un volume, capitolo per capitolo, senza incollare un prompt alla volta. Il CLI possiede stato, ordine e gate; l'agente (Codex CLI, Claude Code, Hermes o una persona) esegue il lavoro editoriale.

I prompt non sono duplicati in codice: il CLI li legge da `wiki/templates/prompt-staff-revisione-completa-volumi.md`. Modificare il wiki cambia ciò che la pipeline esegue.

## Primo avvio dopo il clone

```
git clone <repo> && cd "LIBRO EDITORE CONCORSI PUBBLICI"
npm ci
cp .env.example .env.local        # su Windows: copy .env.example .env.local
npm run pipeline -- doctor
```

`doctor` verifica versione di Node, dipendenze, browser Playwright, `.env.local`, provider di scrittura, repository git e presenza del protocollo. Ogni riga fallita porta con sé il comando esatto per rimediare. Esce con codice 1 finché qualcosa manca.

Se manca il browser: `npx playwright install chromium`.

## Scheda del volume

Unico input richiesto allo staff. Modello: `wiki/templates/scheda-pipeline-volume-template.md`. Va copiato in `wiki/books/<percorso-volume>/planning/00-scheda-pipeline.md` e compilato.

Servono obbligatoriamente `volume_code`, `volume_title`, `cut_off_date`, `responsabile_normativo`, `phases` e la tabella `## Moduli`. Quando il piano dei capitoli è approvato, dichiarare nella scheda numero, titolo, file, matrice e stato atteso. Se la tabella è omessa, la pipeline deriva soltanto i file editoriali già esistenti in `<module id>/chapters/`: non inventa target pianificati.

Esempio già compilato: `wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/planning/00-scheda-pipeline.md`.

## Indice studente e piano editoriale staff

- `chapters/` contiene esclusivamente testo destinato al lettore: capitoli reali e appendici pubblicabili.
- `planning/` contiene gli artefatti editoriali interni: piani, matrici, checklist e pacchetti di review.
- Un capitolo entra nel piano staff quando è dichiarato nella scheda della pipeline; titolo e numero devono essere canonici.
- Un capitolo entra nell'indice studente soltanto quando il relativo file editoriale esiste in `chapters/`.
- La sezione `Piano editoriale staff` usa specifica e run-state della pipeline; non è parte del libro e non genera pagine.
- L'anteprima commerciale non è uno strumento di ispezione degli artefatti interni.
- Non modificare manualmente `pipeline/<VOL>/run-state.json`: usare sempre i comandi CLI.

I piani di modulo usano il percorso `books/moduli/<module-id>/planning/00-piano-editoriale.md`, il tipo `editorial_plan` e il tag `specialist-module-plan`. Non creare o ripristinare `chapters/00-piano-editoriale.md`.

## Comandi

```
npm run pipeline -- init VOL-03                    valida la scheda e crea il run-state
npm run pipeline -- status VOL-03                  avanzamento, blocchi, proprietari
npm run pipeline -- next VOL-03                    step successivo e prompt renderizzato
npm run pipeline -- gate VOL-03 --step 10 --module M-FC02 --chapter 01
npm run pipeline -- complete VOL-03 --step 09 --module M-FC02 --chapter 01
npm run pipeline -- sync VOL-03                    riallinea il run-state alla scheda
```

Opzioni: `--json` (output strutturato per gli agenti), `--phase C`, `--from 10`, `--force` (subentro), `--accept --note "..."` (chiusura manuale di un gate non ancora automatizzato).

## Come lavorano in più persone

Il run-state vive in `pipeline/<VOL>/run-state.json` ed è **versionato in git**: l'avanzamento è visibile a tutti e passa dalla review del commit. I prompt renderizzati e i report intermedi finiscono in `artifacts/pipeline/`, che è ignorato da git.

Ogni step registra `owner` e `agent`. `next` rifiuta uno step già in carico ad altri; `--force` serve a subentrare dopo essersi accordati. Dopo un `git pull`, `sync` riallinea il piano alla scheda e segnala gli step spariti che non erano in stato `pending`.

## Fasi e gate

| Fase | Step | Stato |
| --- | --- | --- |
| A | 00-03 catalogo | manuale |
| B | 04-07 volume e moduli | manuale (gate copertura disponibile) |
| C | 08-12 capitolo | automatizzata |
| D | 13-16 modulo | automatizzata |
| E | 17-20 immagini e impaginazione | manuale |
| F | 21-23 revisione finale, preflight, consegna | automatizzata |
| G | 24 manutenzione | manuale |

### Gate implementati

| Gate | Step | Cosa verifica |
| --- | --- | --- |
| `human-review-assignment` | 04 | ogni review umana richiesta dal perimetro ha un revisore nominativo assegnato nella scheda pipeline |
| `coverage` | 07 e dentro il gate composito 10 | righe della matrice: nessuno stato `parziale`, `solo-nominato`, `mancante`; rinvii precisi, verifica strutturata e checklist dimensionale complete. Riusa `src/server/editorial/didactic-coverage.ts`, lo stesso motore di `npm run audit:coverage` |
| `chapter-lint` | 09 | contratto studente autosufficiente: un solo H1, gerarchia senza salti, obiettivo, Mappa BANDO, teoria, applicazione, errore e verifica; nessuna dipendenza nel corpo da source note, wiki, dashboard o report interni; frontmatter veritiero con `source_refs`, `draft_stage` e `format_version: 2` |
| `didactic-density` | 10 | gate composito: copertura per `Nucleo ID`, checklist dimensionale, almeno 5 nuclei da 600 parole, 3.000 parole, 6 quiz, 1 caso e verifiche ogni 5-7 nuclei; i capitoli legacy ricevono solo `retrofit-dovuto`; verifica anche i rinvii a VOL-01 fino all'heading |
| `citation-guard` | 11 | `source_refs`, riferimenti normativi e rinvii didattici pubblicabili invariati rispetto allo snapshot pre-Humanizer; consente la rimozione dei link interni di conoscenza, blocca quelli rimasti o introdotti e segnala le norme *introdotte* dall'Humanizer |
| `review-report` | 12, 13, 14, 21 | presenza della tabella errori del template fisso, zero errori gravi aperti; sullo step 21 anche il giudizio "Pubblicabile con correzioni minori" |

Gli altri gate (`chapter-plan`, `human-signoff`, `text-freeze`, `page-fill`, `preflight`, `delivery`) rispondono `gate-not-implemented` e **bloccano**: vanno verificati a mano e chiusi con `--accept --note`. Nessun gate dichiara verde ciò che non ha verificato.

### Contratto di esecuzione

`next` antepone al prompt canonico un blocco che dichiara target, gate, comando di chiusura e — quando serve — il percorso in cui scrivere il report: `wiki/reviews/pipeline/<VOL>/<step>-<slug>.md`. Il corpo del prompt resta quello del wiki, invariato.

Sullo step 11 `next` salva anche lo snapshot pre-Humanizer in `artifacts/pipeline/<VOL>/11/<slug>/before.md`: senza quello snapshot il `citation-guard` blocca, perché non avrebbe un termine di paragone.

### Contratto dello studente

Il capitolo pubblicabile deve funzionare senza wiki, dashboard, source note, planning o report. Le fonti consolidate alimentano la scrittura e restano tracciate in `source_refs` e `last_compiled_from`; il corpo insegna direttamente la materia e presenta norme e documenti professionali con denominazioni leggibili. Lo step 12 applica il test dello studente: se togliendo frontmatter e strumenti interni manca una conoscenza assegnata dalla matrice, il capitolo non è pubblicabile.

Sullo step 15 `next` estrae automaticamente ogni box `Dato operativo` dai capitoli del modulo e aggiunge al pacchetto una riga obbligatoria con ID, file e linea, revisore, fonte, versione e data di verifica. La riga resta da compilare con un esito attribuibile al revisore umano.

Le soglie ordinarie sono dichiarate nel contratto degli step 09-10 e possono essere aumentate per capitolo con le colonne `Min parole` e `Min quiz` della scheda. La matrice di modulo è autoritativa; quella di volume si genera con `node scripts/aggregate-coverage-matrices.mjs`.

Strumenti retrofit: `scripts/retrofit/audit-debito.mjs`, `pulisci-contratto.mjs`, `proponi-nuclei.mjs` ed `estrai-item.mjs`. L'audit campiona anche la checklist dimensionale; la proposta nuclei incrocia gli heading con la matrice. Solo `pulisci-contratto.mjs --write` modifica i capitoli.

## Regola dei blocchi

Stop al primo blocker: se un gate non passa, nessuno step a valle parte. Si corregge e si ripete lo stesso step. È la traduzione in codice del protocollo, non una scelta di comodità.
