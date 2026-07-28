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

Servono obbligatoriamente `volume_code`, `volume_title`, `cut_off_date`, `responsabile_normativo`, `phases` e la tabella `## Moduli`. I capitoli si possono omettere: la pipeline li deriva da `<module id>/chapters/`.

Esempio già compilato: `wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/planning/00-scheda-pipeline.md`.

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

### Se due persone lavorano sullo stesso volume

Il primo argine è la scelta stessa dei target: ogni step è identificato da `id:capitolo` (es. `09:moduli/m-fc02-agenzie-fiscali/chapters/01-perimetro.md`). Due persone su **capitoli diversi** dello stesso volume non si scontrano mai: sono chiavi diverse nel run-state.

Il secondo argine è il lock applicativo: `next` rifiuta di assegnare uno step già `in-progress` a un altro owner (vedi sopra). Ma questo lock vale solo finché entrambi lavorano sullo stesso file locale — se due persone fanno `next` su macchine diverse **prima** di essersi allineate via `git pull`, possono entrambe reclamare lo stesso capitolo in locale senza saperlo. È esattamente il caso che il terzo argine copre.

Il terzo argine è un **merge driver Git dedicato** su `pipeline/*/run-state.json` (dichiarato in `.gitattributes`, registrato automaticamente da `pipeline doctor` la prima volta che lo esegui). Quando fai `git pull`/`git merge` e quel file è cambiato su entrambi i lati, Git non usa il merge testuale grezzo (che produrrebbe marcatori `<<<<<<<` in mezzo a un oggetto JSON, illeggibili e rischiosi): usa la logica di `runMergeDriver`, che ragiona per singolo step, confrontando anche la base comune:

- **Step diversi cambiati da persone diverse** → uniti automaticamente, nessun conflitto, nessun avanzamento perso.
- **Stesso step, ma una delle due parti non lo ha mai toccato** (è rimasto identico alla base comune) → si prende senza conflitto la versione di chi lo ha effettivamente lavorato.
- **Stesso step, cambiato in modo diverso da entrambi** (es. alice lo ha preso in carico, bruno lo ha completato e bloccato) → **conflitto esplicito**: il file resta con marcatori `<<<<<<< HEAD` / `=======` / `>>>>>>> incoming` attorno alle due versioni JSON complete, e Git stampa in chiaro quale step, quali owner, quali esiti. Va risolto a mano: decidi quale versione tenere (o accordati con l'altra persona), rimuovi i marcatori, `git add pipeline/<VOL>/run-state.json`, poi continua il merge (`git commit`).

Questo meccanismo non tocca i **file dei capitoli** (`wiki/books/.../chapters/*.md`): se due persone scrivono davvero lo stesso capitolo in prosa senza rispettare il lock del `next`, quello resta un normale conflitto di testo Git, da risolvere come qualunque conflitto di contenuto — motivo in più per non bypassare mai `next`/`--force` senza essersi prima accordati.

### Allinearsi al lavoro degli altri, a ogni sessione

Più persone (e agenti) commettono direttamente su `main`. Prima di iniziare a lavorare:

```
git pull
npm ci                              # solo se package.json/package-lock.json sono cambiati
npm run pipeline -- doctor          # se qualcosa nell'ambiente è cambiato
npm run pipeline -- sync VOL-03     # se lavori su un volume: riallinea il run-state alla scheda
npm run pipeline -- status VOL-03   # vedi chi ha in carico cosa
```

**Se `git pull` va in conflitto**, quasi sempre è sui file append-only condivisi da tutti — `wiki/log.md` e i tre file in `wiki/memory/agent/` (`l0/conversations.jsonl`, `l1/atoms.jsonl`, `l2/scenarios.md`) — perché due sessioni hanno scritto in coda nello stesso punto nello stesso momento. Non è un vero conflitto di contenuto: è un doppio append. La regola di risoluzione è sempre la stessa:

1. **Tieni entrambe le appendici.** Mai cancellare o riscrivere una riga esistente, mai scegliere "la mia versione" scartando l'altra.
2. Per i `.jsonl`, verifica che ogni riga resti JSON valido dopo la risoluzione (una virgola o una parentesi di troppo rompe silenziosamente `LocalAgentMemory`).
3. Prima di chiudere il merge:
   ```
   git diff --cached --check
   npm test
   npm run typecheck
   ```
4. Solo dopo, `git commit` (senza `--no-edit` se vuoi rivedere il messaggio) e `git push`.

Se il conflitto coinvolge `pipeline/<VOL>/run-state.json`, non lo vedrai quasi mai come marker JSON grezzi in mezzo a un oggetto: il merge driver dedicato (sezione successiva) lo risolve da solo quando le persone hanno lavorato su step diversi, e lo segnala in modo leggibile — step, owner, esiti — solo quando è un vero conflitto sullo stesso step. Dopo aver risolto (o quando il merge è passato pulito), esegui comunque `npm run pipeline -- sync VOL-03`: non serve a fondere conflitti, ma riallinea l'elenco degli step alla scheda se nel frattempo qualcuno ha aggiunto o tolto moduli/capitoli.

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
| `coverage` | 07, 10 | righe della matrice collocate nel capitolo: nessuno stato `parziale`, `solo-nominato`, `mancante`; rinvii con destinazione precisa. Riusa `src/server/editorial/didactic-coverage.ts`, lo stesso motore di `npm run audit:coverage` |
| `chapter-lint` | 09 | un solo H1, gerarchia senza salti, nessun segnaposto (`TODO`, `lorem ipsum`, `[da completare]`), nessun meta-commento da agente, frontmatter con `source_refs` e `draft_stage` |
| `citation-guard` | 11 | wikilink, `source_refs` e riferimenti normativi invariati rispetto allo snapshot pre-Humanizer; segnala anche le norme *introdotte* dall'Humanizer |
| `review-report` | 12, 13, 14, 21 | presenza della tabella errori del template fisso, zero errori gravi aperti; sullo step 21 anche il giudizio "Pubblicabile con correzioni minori" |

Gli altri gate (`chapter-plan`, `human-signoff`, `text-freeze`, `page-fill`, `preflight`, `delivery`) rispondono `gate-not-implemented` e **bloccano**: vanno verificati a mano e chiusi con `--accept --note`. Nessun gate dichiara verde ciò che non ha verificato.

### Contratto di esecuzione

`next` antepone al prompt canonico un blocco che dichiara target, gate, comando di chiusura e — quando serve — il percorso in cui scrivere il report: `wiki/reviews/pipeline/<VOL>/<step>-<slug>.md`. Il corpo del prompt resta quello del wiki, invariato.

Sullo step 11 `next` salva anche lo snapshot pre-Humanizer in `artifacts/pipeline/<VOL>/11/<slug>/before.md`: senza quello snapshot il `citation-guard` blocca, perché non avrebbe un termine di paragone.

## Regola dei blocchi

Stop al primo blocker: se un gate non passa, nessuno step a valle parte. Si corregge e si ripete lo stesso step. È la traduzione in codice del protocollo, non una scelta di comodità.
