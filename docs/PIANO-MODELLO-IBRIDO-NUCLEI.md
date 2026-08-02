# Piano — Modello editoriale ibrido ConcorsoBook: nuclei, verifiche e gate misurabili

> Documento di handoff per agenti implementatori. Autosufficiente: non presuppone contesto di conversazione precedente. Riferisce sempre percorsi file assoluti rispetto alla root del repo.
>
> Stato: architettura implementata e integrata in `main`; pilot M-SA02/05 e retrofit M-FC02/04 eseguiti nel worktree dedicato, audit automatico M-SA02 chiuso allo step 15. Decisione sulla conferma umana finale recepita il 2026-08-01.

## Context

L'analisi di VOL-07 (modulo sanità, `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/`, lavoro reale nel worktree `.worktrees/vol-07-pipeline-start`) ha mostrato tre difetti misurabili: apparato di allenamento quasi assente, densità fuori controllo (957 → 7.309 parole nello stesso volume), e una matrice di copertura non verificabile a macchina (colonna `Verifica apprendimento` in prosa libera). Il gate di copertura esistente misura la *presenza* del nucleo, non la sua *sufficienza didattica*.

La misurazione del corpus esistente in `main` mostra che il problema è sistemico, non solo di VOL-07:

| Metrica sui 189 capitoli esistenti (`wiki/books/**/chapters/*.md`) | Valore |
|---|---|
| Parole totali | 577.916 |
| **Capitoli senza un solo quiz** | **149 su 189 (79%)** |
| Quiz nell'intero corpus (`Risposta corretta:`) | 71 |
| Mediana parole/capitolo | 2.989 |
| Capitoli sotto le 3.000 parole | 96 |

Questa è la baseline storica precedente all'integrazione di VOL-07. La misura riproducibile corrente, generata il 2026-08-01 da `node scripts/retrofit/audit-debito.mjs`, è:

| Metrica corrente | Valore |
|---|---|
| Capitoli | 191 |
| Parole totali | 640.553 |
| Capitoli senza quiz | 162 |
| Capitoli sotto le 3.000 parole | 86 |

Casi peggiori: `wiki/books/moduli/m-fc05-authority-indipendenti/` — 16 capitoli, 44.100 parole, **0 quiz**; `wiki/books/il-metodo-bando/` — 54 capitoli, 190.696 parole, **48 senza quiz**; `wiki/books/moduli/m-fl04-polizia-locale/` — mediana 2.073 parole. Caso migliore: `wiki/books/moduli/m-fc02-agenzie-fiscali/` — 37 quiz, solo 4 capitoli scoperti su 16.

L'analisi di 9 manuali ufficiali di mercato per concorsi pubblici italiani (Edises/Simone/frg press: RIPAM, CNR, MIC, Aziende Sanitarie, Infermiere) fornisce i riferimenti mancanti:

| Riferimento | Dato rilevato | Conseguenza per noi |
|---|---|---|
| Manuale MIC AFAV (epub, 1.500 assistenti vigilanza/custodia) | 1.651 micro-unità con tassonomia `Materia \| Macro-area \| Micro-argomento`, **200 blocchi di verifica** (1 ogni ~7 unità), 4 sezioni fisse per unità | l'atomizzazione con ID è ciò che rende la copertura misurabile; **ma è interamente immagini (345 JPG, zero testo estraibile)** — architettura da copiare, esecuzione no |
| Il Manuale dei Concorsi per Infermiere (Edises) | 30 capitoli, **Test di verifica in coda a ogni capitolo**; scale operative pubblicate (Conley, Stratify, Tinetti); Parte IV di **procedure numerate** (27.1–27.18+) | il concorrente pubblica esattamente i valori operativi che il modulo M-SA02 oggi omette per policy |
| Concorsi per Collaboratore e Assistente amministrativo Aziende Sanitarie (Edises) | 1.246 pp, di cui **~860 pp di solo sanitario** + Appendice di **23 formule di atti** (92 pp) | è il livello di profondità specialistica da eguagliare, avendo scelto di non duplicare il generico |
| Concorso CNR 110 Funzionari / MIC 1800 assistenti / RIPAM 2133 Funzionari | ogni volume è autosufficiente e ripete il nucleo comune costituzionale/amministrativo (31–100% del testo) | scelta confermata dall'utente: **non duplichiamo** — quindi tutta la profondità va sul delta specialistico |

**Decisioni prese dall'utente (2026-08-01):**
1. **Nucleo comune**: si mantiene la regola v4 stretta di `wiki/books/moduli/architettura-moduli-specialistici.md` (nucleo solo in VOL-01), **alzando il livello del volume specialistico** perché regga da solo il confronto a scaffale con i concorrenti.
2. **Contenuto operativo clinico/tecnico**: si pubblica (scale, soglie, codici, procedure) **quando esiste fonte ufficiale citabile**, sempre con versione, data e ambito.
3. **Granularità**: il capitolo resta l'unità editoriale, ma diventa una sequenza di **nuclei identificati**, con blocchi di verifica intercalati.
4. **Conferma umana**: nessun revisore viene assegnato durante apertura, scrittura o audit. I testi devono essere già perfetti e completi; l'unico passaggio umano è lo step 24, ultimo del protocollo, che conferma o respinge la validità finale.
5. **I miglioramenti valgono per i prossimi volumi, per quelli in lavorazione E per quelli già scritti.** Il retrofit del corpus esistente è parte del lavoro, non un'eventualità (§9).
6. **La verifica di un nucleo non può essere solo quantitativa.** Contare parole e quiz non garantisce che l'argomento richiesto sia coperto in modo congruo ed efficace. Serve un controllo esplicito, per ogni nucleo, sulla profondità reale della copertura — non solo sulla sua lunghezza (§3-bis).
7. **L'impaginazione va rivista prendendo spunto dai manuali ufficiali analizzati**, non solo la struttura dei contenuti (§6-bis). Sul punto di maggiore impatto commerciale — stampa interna a colori vs bianco e nero — l'utente ha deciso di **restare in bianco e nero per ora** (§6-bis.1): nessun impatto sui margini di stampa; la differenziazione visiva si ottiene con tabelle/schemi ben disegnati in scala di grigi, riservando la palette colore a copertina e canale digitale.

**Esito atteso**: un formato di capitolo che il gate della pipeline può verificare a macchina, un apparato di allenamento presente ovunque, una profondità specialistica allineata al mercato, e i quiz estraibili come banca item senza rifare l'impaginato.

---

## 1. Formato del capitolo: nuclei con ID + verifiche intercalate

Il capitolo passa da monolite a sequenza di **nuclei**. Un nucleo = una riga della matrice di copertura, resa in testo.

```markdown
# Valutazione clinica, triage, urgenza ed emergenza

## Obiettivo del capitolo
## Mappa BANDO

## N-SA02-05-01 · Valutazione iniziale e priorità
<teoria essenziale> → <schema o tabella> → <applicazione al profilo>

## N-SA02-05-02 · Urgenza, emergenza e rischio evolutivo
## N-SA02-05-03 · Rivalutazione

## ▣ Verifica 05.A
<6 quiz con risposta commentata + 1 caso ragionato>

## N-SA02-05-04 · NEWS2: funzione, soglie e limiti
## N-SA02-05-05 · Comunicazione strutturata ed escalation
## N-SA02-05-06 · Sospetta infezione e percorso sepsi

## ▣ Verifica 05.B
## Errori e trappole ricorrenti
## Checklist finale
## Riferimenti normativi e professionali
```

**Regole del formato**

- ID nucleo: `N-<MODULO>-<CAP>-<nn>` (es. `N-SA02-05-01`). Stabile, non cambia con la rinumerazione editoriale.
- Ogni nucleo sviluppa nell'ordine: **teoria essenziale → schema/tabella → applicazione al profilo**.
- Un blocco `▣ Verifica <cap>.<lettera>` ogni **5-7 nuclei**, minimo uno per capitolo.
- Ogni blocco di verifica: **≥6 quiz** a risposta multipla con spiegazione del corretto e almeno un distrattore commentato, **+1 caso ragionato**.
- Si conservano i box già canonici (`Da sapere in 5 righe`, `Errore tipico`, `Domanda da commissario`, `Domanda-trappola`, `Caso guidato`, `Mini-esercizio`, `Checklist`): sono già presenti in ~140 capitoli su 189 e non vanno toccati.

**Target quantitativi** (sostituiscono il giudizio discrezionale «conciso ma completo»):

| Metrica | Minimo | Stato attuale del corpus |
|---|---|---|
| Nuclei per capitolo | 5 | non tracciato oggi |
| Parole per nucleo | 600 | — |
| Parole per capitolo | 3.000 | **86 capitoli su 191 sotto soglia** |
| Quiz per capitolo | 6 | **162 capitoli su 191 a zero** |
| Casi ragionati per capitolo | 1 | ~142 capitoli hanno già `Caso guidato` |
| Copertura righe matrice | 100% delle righe assegnate ha un nucleo con ID | non verificabile oggi |

---

## 2. La matrice di copertura diventa verificabile a macchina

Oggi `wiki/templates/didactic-coverage-matrix-template.md` ha 13 colonne e quelle didattiche (`Output concorsuale`, `Verifica apprendimento`) contengono prosa libera (es. `"casi e checklist"`, `"domande, micro-traccia, esercizio"`). Il gate non può contarle.

- Nuova colonna **`Nucleo ID`** — il `N-XXnn-cc-nn` che realizza la riga nel testo. Vuota = riga non ancora scritta.
- La colonna **`Verifica apprendimento`** passa a formato strutturato: `Q:6 C:1 E:1` (quiz / casi / esercizi). Prosa ammessa dopo il codice, dietro `—`.
- La colonna **`Collocazione`** passa da `Cap. 5` a `Cap. 05 § N-SA02-05-04`, così `coverage-gate` risolve l'ancora esatta invece del pattern matching sul numero di capitolo (`chapterPattern`, regex `\bcap(itolo)?\.?\s*0*N\b` in `src/pipeline/gates/coverage-gate.ts`).

**Una sola fonte di verità.** La matrice di modulo (es. `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/02-matrice-copertura-didattica.md`) è autoritativa; quella di volume (es. `wiki/books/volumi/vol-07-.../planning/02-matrice-copertura-didattica.md`) viene **generata** da uno script di aggregazione, non mantenuta a mano. Elimina la contraddizione attuale di VOL-07 (`index.md`: «25 capitoli completi»; matrice di volume: «43 righe mancante»).

⚠️ **Attenzione**: la logica di parsing della matrice è oggi **duplicata** in `src/server/editorial/didactic-coverage.ts` (usata dal gate, funzioni `parseCoverageMatrix`, `auditCoverageRows`) e in `scripts/audit-didactic-coverage.mjs` (usata da `npm run audit:coverage`, comando standalone). Vanno **unificate prima** di aggiungere colonne, altrimenti divergono silenziosamente. Le 8 matrici esistenti già divergono dal template (11 vs 13 colonne).

---

## 3. Nuovo gate `didactic-density`, con modalità legacy

`src/pipeline/gates/chapter-lint-gate.ts` ha oggi 7 blocker: `heading-h1` (un solo H1), `heading-jump` (nessun salto di livello), `placeholder` (TODO/TBD/FIXME/lorem ipsum), `agent-meta` (meta-commenti da assistente AI), `missing-source-refs`, `missing-draft-stage`, `empty-chapter`. **Nessuno è quantitativo.**

Si aggiunge un gate **separato**, non si gonfia `chapter-lint` — così le due responsabilità (igiene del file / sufficienza didattica) restano distinte e testabili.

### 3.1 Nuovo file

`src/pipeline/gates/didactic-density-gate.ts`, export `runDidacticDensityGate(input: {content: string; chapterPath: string; formatVersion?: number}): GateResult`. Funzione pura come le esistenti (nessun I/O). Riusa `headingsOf()` di `chapter-lint-gate.ts` (già salta i code fence via `isInsideFence`) per estrarre e contare heading nucleo e blocchi di verifica.

### 3.2 Blocker (solo quando `format_version: 2`, vedi §3.3)

| Codice | Condizione |
|---|---|
| `nuclei-insufficienti` | meno di 5 heading che matchano `^N-[A-Z]{2}\d{2}-\d{2}-\d{2} · .+` |
| `nucleo-id-malformato` | heading che inizia con `N-` ma non rispetta il pattern completo |
| `nucleo-troppo-breve` | un nucleo (testo tra il suo heading e il successivo) < 600 parole |
| `verifica-assente` | nessun blocco heading `▣ Verifica` nel capitolo |
| `verifica-troppo-distante` | più di 7 heading nucleo consecutivi senza un blocco `▣ Verifica` frapposto |
| `quiz-insufficienti` | meno di 6 occorrenze di `Risposta corretta:` |
| `caso-assente` | nessuna occorrenza di `Caso ragionato` o `Caso guidato` |
| `capitolo-troppo-breve` | corpo (esclusa frontmatter) < 3.000 parole |
| `rinvio-non-risolto` | wikilink verso `books/il-metodo-bando/...` il cui file o `#heading` non esiste (vedi §5) |

Warning (mai bloccanti): `nucleo-molto-lungo` (> 1.800 parole, candidato a split), `squilibrio-nuclei` (nucleo più lungo > 3x il più corto del capitolo).

### 3.3 Modalità legacy — perché serve ed è obbligatoria

Accendere questo gate su tutto il corpus esistente renderebbe **istantaneamente `blocked`** ogni volume in pipeline: 149 capitoli fallirebbero su `quiz-insufficienti`, 96 su `capitolo-troppo-breve`. Il meccanismo:

- Nuovo campo frontmatter **`format_version: 1 | 2`**. Assente o `1` = legacy.
- Su `format_version: 1` (o assente) il gate **non emette blocker**, solo un warning `retrofit-dovuto` col delta mancante (quante parole/quiz/nuclei mancano rispetto alla soglia).
- Su `format_version: 2` il gate applica i blocker della tabella §3.2 normalmente.
- Regola non negoziabile: **ogni capitolo che passa dal ciclo degli step 08-12 deve uscire con `format_version: 2`**. Non è ammesso riscrivere un capitolo (farlo passare per lo step 09) e lasciarlo dichiarato legacy.
- Al termine del retrofit (§9, Fase 5) si rimuove la modalità legacy e il gate blocca ovunque incondizionatamente.

### 3.4 Wiring nella pipeline (4 modifiche coordinate)

⚠️ Se si aggiunge l'id gate al registry senza il dispatch in `gates/index.ts`, `notImplemented()` fa hard-block dello step con `gate-not-implemented`. Le 4 modifiche vanno fatte insieme:

1. **`src/pipeline/gates/index.ts`** — in `runGate(gateId, context)`, aggiungere un branch `if (gateId === "didactic-density") return didacticDensity(context)`. Serve anche una funzione loader (accanto a `chapterLint()`) che risolve il file con `chapterFileOf(context.wikiRoot, context.step.target)` e restituisce `blocker("missing-chapter", ...)` su ENOENT, esattamente come fa oggi `chapterLint()`.
2. **`src/pipeline/steps/registry.ts`** — il gate va assegnato allo step **10** (oggi porta `coverage` — `definition("10", "C", "Controllo di copertura del capitolo", "chapter", "llm", "automated", "coverage")`). Valutare in fase di implementazione se comporre i due gate (coverage + densità nello stesso step) o spostare `coverage` sullo step **08** (oggi porta `chapter-plan`, che **non è implementato** e quindi oggi fa hard-block incondizionato — `notImplemented()` in `gates/index.ts`).
3. **`src/pipeline/cli/commands.ts`** — in `deliveryContract()` (~riga 441) aggiungere una riga con le soglie quantitative, così il prompt renderizzato dichiara i minimi all'agente scrittore **prima** che scriva, non dopo.
4. **`tests/pipeline/gates.test.ts`** — riusare la fixture `chapter(body, frontmatter)` e l'helper `codes(result)` già presenti nel file per i nuovi casi di test (§11).

⚠️ **`tests/pipeline/steps.test.ts`** contiene un'asserzione che **ogni step automatico delle fasi C/D/F abbia un gate assegnato**: va aggiornato se si rimescolano gli id gate tra gli step 08/10.

### 3.5 Soglie configurabili per capitolo (opzionale, valutare in implementazione)

`GateContext` (definito in `src/pipeline/gates/index.ts`, tipo `{wikiRoot, projectRoot, spec, step, module?, chapterNumber?}`) trasporta già `spec`, `module`, `chapterNumber`, ma la funzione `chapterLint()` in `gates/index.ts` li scarta passando solo `{content, chapterPath}` al gate vero e proprio. Per soglie differenziate (es. un capitolo-laboratorio ha più quiz e meno teoria dei nuclei ordinari) servirebbero colonne opzionali `min_parole` / `min_quiz` nella tabella capitoli della scheda pipeline — modifica in `src/pipeline/spec/parse-volume-spec.ts` (tipo `VolumeSpecChapter`), `src/pipeline/spec/validate-volume-spec.ts` (funzione `validateChapter`) e nel template `wiki/templates/scheda-pipeline-volume-template.md`.

---

## 3-bis. Copertura qualitativa per nucleo: il numero non basta

### 3-bis.1 Il problema che il gate quantitativo non risolve

Il gate `didactic-density` (§3) verifica volume: un nucleo con 600+ parole, incluso in un blocco con 6 quiz, **passa il gate anche se è didatticamente vuoto** — spiega solo la definizione e non le distinzioni, non ha un errore tipico, non chiarisce come si presenta in prova. Un capitolo può essere quantitativamente conforme e restare superficiale su metà degli argomenti richiesti. Il rischio non è ipotetico: è esattamente il meccanismo con cui, oggi, un capitolo da 957 parole viene classificato "conciso ma completo" — la stessa formula generica si applicherebbe domani a un nucleo verboso ma vuoto.

**Questo controllo esiste già come dottrina, ma non come artefatto strutturato.** `wiki/AGENTS.md`, sezione "Gate globale di copertura didattica integrale" (fonte canonica: `wiki/sources/principio-copertura-didattica-integrale-2026-07-17`), richiede già che ogni nucleo copra, quando applicabili: **definizione, funzione, inquadramento, elementi, distinzioni, conseguenze, esempio/caso, modalità d'esame, errore tipico, verifica, fonti**. E dichiara: *"la guida operativa non sostituisce la copertura teorica e la lunghezza non dimostra completezza"* — è già scritto, oggi semplicemente non è verificato in modo sistematico. Il Prompt 10 del protocollo (`wiki/templates/prompt-staff-revisione-completa-volumi.md`) chiede a un agente di verificarlo "nel testo reale", ma il risultato è un giudizio olistico in prosa libera per l'intero capitolo, non una checklist esplicita per ciascun nucleo.

### 3-bis.2 La correzione: checklist dimensionale per Nucleo ID

Ogni riga della matrice di copertura (già dotata di `Nucleo ID`, §2) acquisisce una seconda tabella compagna — o colonne aggiuntive nella stessa matrice — con una cella per ciascuna delle 10 dimensioni della dottrina esistente:

| Nucleo ID | Definizione | Funzione | Inquadramento | Elementi | Distinzioni | Conseguenze | Esempio/caso | Errore tipico | Verifica | Fonti |
|---|---|---|---|---|---|---|---|---|---|---|
| N-SA02-05-04 | ✓ §NEWS2 p.1 | ✓ | ✓ | ✓ | ✓ vs score simili | n/a | ✓ Caso 1 | ✓ box | ✓ Quiz 05.B-3 | ✓ |
| N-SA02-05-05 | ✓ | ✓ | ✗ **manca** | ✓ | n/a | ✓ | ✗ **manca** | ✓ | ✓ | ✓ |

Regole:
- Ogni cella è **✓ con evidenza** (riferimento a heading/citazione), **✗ con motivo** (mancante), o **n/a** (dimensione non applicabile a quel tipo di nucleo — va giustificato, non lasciato ambiguo).
- Compilarla resta un compito di giudizio (non è regex-contabile come i quiz): la esegue l'agente automatico nello step 10 del protocollo, **ma il deliverable cambia da prosa libera a tabella esplicita per dimensione**. Questo rende il controllo auditabile e permette alla conferma umana finale dello step 24 di vedere immediatamente quali dimensioni sono state verificate per ciascun nucleo, senza introdurre blocchi anticipati.
- Nuovo blocker nel gate `coverage` esistente (`src/pipeline/gates/coverage-gate.ts`, che già consuma `parseCoverageMatrix`/`auditCoverageRows` da `src/server/editorial/didactic-coverage.ts`): `dimensione-mancante` quando un nucleo ha una o più dimensioni applicabili marcate ✗. Si allinea alla logica già esistente per cui `solo-nominato` e `mancante` bloccano a livello di riga — qui si applica alla singola dimensione dentro la riga, non solo allo stato complessivo della riga.
- Un nucleo non può essere dichiarato coperto (stato `completo` nella matrice) se ha dimensioni ✗ non giustificate come `n/a`.

### 3-bis.3 Conseguenza sul retrofit (§9): il Livello A si divide in due esiti

Nel piano originale, il Livello A del retrofit (assegnare Nucleo ID e aggiungere quiz al testo già scritto) era classificato come puramente meccanico — nessuna nuova fonte, nessun nuovo audit normativo. **Questo resta vero per l'aggiunta dei quiz**, ma l'esecuzione del Livello A deve includere anche la compilazione della checklist dimensionale su ogni nucleo esistente. Due esiti possibili per ciascun nucleo legacy:

- **Checklist compilabile con evidenza già presente nel testo** → il nucleo resta Livello A (solo formalizzazione: ID, raggruppamento in blocco di verifica, quiz derivati dal testo esistente).
- **Checklist rivela una dimensione mancante non derivabile dal testo esistente** (es. il nucleo ha definizione ed esempio ma nessuna distinzione né errore tipico) → il nucleo **scala a Livello B**, perché completarlo richiede scrittura nuova, non solo riorganizzazione. Questo va rifatto **prima** di assegnare `format_version: 2` al capitolo — il gate quantitativo da solo non lo avrebbe intercettato, dato che il nucleo può già superare le 600 parole.

Questo significa che la stima di costo del retrofit fatta nel §9.1/§9.3 sui soli conteggi di parole/quiz è un limite inferiore: `audit-debito.mjs` (§9.4.1) deve incorporare anche un campionamento della checklist dimensionale, non solo i conteggi quantitativi, per dare una stima realistica del Livello A vs B per modulo.

### 3-bis.4 File da toccare (aggiunta alla tabella dell'§8)

| File | Modifica |
|---|---|
| `wiki/templates/didactic-coverage-matrix-template.md` | aggiungere le 10 colonne dimensionali (o tabella compagna) accanto a `Nucleo ID` |
| `src/server/editorial/didactic-coverage.ts` | estendere `parseCoverageMatrix`/`auditCoverageRows` per leggere le colonne dimensionali e produrre il blocker `dimensione-mancante` |
| `src/pipeline/gates/coverage-gate.ts` | propagare il nuovo blocker nel `GateResult` |
| `wiki/templates/prompt-staff-revisione-completa-volumi.md` | Prompt 10: sostituire l'istruzione di giudizio libero con l'istruzione di compilare la checklist dimensionale per ogni Nucleo ID, con evidenza citata |
| `scripts/retrofit/audit-debito.mjs` | includere il campionamento dimensionale nella stima del debito, non solo i conteggi quantitativi |

---

## 4. Policy sul contenuto operativo clinico e tecnico

Decisione utente: si pubblica **con versione e fonte**. Nuovo box canonico, da aggiungere alla Bibbia del Volume (es. `wiki/books/volumi/vol-07-.../planning/04-bibbia-del-volume.md`) e al Prompt 09 del protocollo (`wiki/templates/prompt-staff-revisione-completa-volumi.md`):

```markdown
> **Dato operativo — Scala di Conley**
> Ambito: prevenzione cadute, adulto ospedalizzato · Livello: nazionale
> Fonte: <estremi> · Versione: <n> · Verificata al: 2026-08-01
> <contenuto: item, punteggi, soglie>
> Audit automatico: clinico-assistenziale
```

Regole:
- Ammesso solo con fonte ufficiale acquisita e source note (la catena `raw → source note → fonte ufficiale verificata → topic/entity page → capitolo`, già canonica in `wiki/AGENTS.md`, resta invariata).
- **Ogni box `Dato operativo` genera automaticamente una riga obbligatoria** nell'audit specialistico automatico dello step 15, con il tag della competenza richiesta già indicato nel box. Fonte, ambito, versione e data devono essere verificati e corretti prima del text freeze.
- Nuovo campo frontmatter `dati_operativi: [<id>, …]`, per rendere il capitolo interrogabile negli audit automatici e nella manutenzione post-pubblicazione. Lo step 24 resta esclusivamente la conferma umana finale del pacchetto.
- Restano esclusi: dosi e posologie, energie di defibrillazione, sequenze di manovra eseguibili, protocolli locali presentati come regola nazionale. Questi si citano per *esistenza e funzione*, mai per contenuto esecutivo.
- La premessa al lettore (`front-matter/05-premessa.md` di ciascun volume) dichiara esplicitamente il perimetro: cosa il volume pubblica e cosa rinvia a corsi certificati e protocolli di struttura.

**Conseguenza operativa**: aumenta il carico dell'audit specialistico automatico, che deve verificare e correggere ogni dato operativo prima del text freeze. I quattro vecchi stati `awaiting-human` osservati su VOL-07 sono stati migrati tramite CLI: M-SA02 è chiuso dal nuovo step 15 automatico; M-SA01, M-SA03 e M-SA04 sono tornati `pending` automatici. Nessun modulo resta in attesa di una persona prima dello step 24.

---

## 5. Regola v4 stretta: rinvii verificati, non generici

Avendo confermato la regola v4 (nucleo comune solo in VOL-01, nessuna duplicazione), un rinvio a una destinazione inesistente o vaga in un volume specialistico lascia un buco che il lettore paga direttamente.

- Formato obbligatorio per ogni rinvio a VOL-01: `[[books/il-metodo-bando/chapters/<file>#<heading>]]` — capitolo **e** sezione, mai il solo volume o il solo capitolo.
- Nuovo blocker `rinvio-non-risolto` (§3.2) se il file target o l'heading indicato non esistono. Riusa `extractWikiLinks()` di `src/server/wiki/markdown.ts`.
- La Bibbia del Volume dichiara già: «Finché tale destinazione non è disponibile, la riga resta aperta e non può essere considerata coperta» — oggi è una regola scritta ma non verificata meccanicamente; con questo gate diventa un blocker automatico.

⚠️ **Dipendenza critica per la sequenza di implementazione**: questo blocker non può essere attivato finché VOL-01 (`wiki/books/il-metodo-bando/`, 54 capitoli) non ha una struttura di heading stabile e indicizzata — altrimenti ogni rinvio esistente nei volumi specialistici risulterebbe `non-risolto` per motivi indipendenti dalla loro qualità. Da qui l'ordine di priorità del retrofit in §9.5 (Fase 1 = VOL-01 prima di tutto).

---

## 6. Alzare il livello del volume specialistico

Benchmark di riferimento: il libro *Concorsi per Collaboratore e Assistente amministrativo nelle Aziende Sanitarie* ha **~860 pagine di solo contenuto sanitario** (Libri III-VII, esclusi i Libri I-II generici). Applicando i minimi quantitativi del §1 ai 25 capitoli di VOL-07 si arriva a una fascia di 75.000–180.000 parole di **solo specialistico**, che è l'ordine di grandezza giusto.

Tre interventi mutuati dai libri di riferimento analizzati:

1. **Appendice di atti e formule** (moduli amministrativi, a partire da M-SA01). Il libro Aziende Sanitarie chiude con 23 formule (ratifica di concorso, convenzioni, bandi di gara, nomine di direttore, adozione di bilancio, designazione RPD, istanza di accesso agli atti…) su 92 pagine: è il contenuto a più alto valore percepito del libro e il più facile da produrre con fonti verificate (sono modelli di atti amministrativi standard). Nuova cartella `appendix/` nel modulo, es. `wiki/books/moduli/m-sa01-sanita-amministrativa/appendix/`.
2. **Appendice di procedure** (moduli clinico-tecnici: M-SA02, M-SA04), sul modello delle procedure numerate del manuale Infermiere (`Procedura 27.12 Pulsossimetria`, `27.16 Sicurezza nella deambulazione`, ecc.), restando sul piano descrittivo-professionale coerente con la policy §4.
3. **Front matter metodologico**. Il compendio MIC AFAV apre con «Come sono organizzate le materie nel volume» + tre percorsi di studio (sequenziale / strategico per peso / diagnostico via test iniziale) + soglie di autovalutazione 70-85% con recupero mirato. Costo di produzione bassissimo, valore percepito alto, e per ConcorsoBook è onesto farlo: i percorsi si derivano dal campione di bandi reale con SHA-256 verificato, cosa che il concorrente non ha. Va in `front-matter/05-premessa.md` (esistente) e in un nuovo `front-matter/07-come-studiare-questo-volume.md`.

---

## 6-bis. Impaginazione: confronto con i manuali ufficiali e revisione del design system

Il design system editoriale esistente (`wiki/books/il-metodo-bando/design-system-editoriale.md`, canonico per tutta la collana) è già maturo: paperback KDP 6,69×9,61", Garamond 11pt corpo / Arial Bold per titoli e strumenti, colonna singola, tassonomia di 12 box ricorrenti, palette Navy/Bordeaux/Muted Gold/Off-White, gerarchia di pagina in 12 punti, regole esplicite su tabelle, immagini e "infografiche pre-epilogative". Il confronto con i 9 manuali ufficiali analizzati non richiede di rifarlo da zero — richiede quattro correzioni puntuali.

### 6-bis.1 Colore di stampa — decisione dell'utente

Il manuale Infermiere di riferimento è **interamente a colori** ("il volume, interamente a colori" — dichiarato nella premessa dell'editore); il design system ConcorsoBook impone oggi **bianco e nero senza bleed** su tutti i volumi (Prompt 19 del protocollo). La stampa interna a colori su KDP ha una struttura di costo per pagina sensibilmente più alta e riduce il margine per copia.

**Decisione presa dall'utente (2026-08-01): si resta in bianco e nero.** Nessuna modifica al design system su questo punto. La differenziazione visiva tra tipi di contenuto (box, tabelle, schemi) si ottiene con contrasto, tratteggio e struttura in scala di grigi — già previsto dal design system esistente ("se stampato in bianco e nero, i riempimenti devono restare visibili"). La palette colore resta riservata a copertina e canale digitale/dashboard, come oggi.

### 6-bis.2 Numerazione decimale visibile in pagina

I manuali Edises (RIPAM, CNR, MIC, Aziende Sanitarie) usano una numerazione decimale visibile e profonda (`1.1`, `1.1.1`, `1.1.2`…) che diventa l'indice analitico del libro — il lettore trova un argomento specifico dall'indice, non solo il capitolo che lo contiene. Oggi ConcorsoBook numera solo il capitolo; le sotto-sezioni non hanno un numero visibile in pagina.

Il sistema di `Nucleo ID` introdotto dal §1 (`N-SA02-05-04`) risolve già la tracciabilità interna, ma è un identificatore tecnico, non pensato per il lettore. Proposta: derivare da ogni `Nucleo ID` un **numero decimale visibile** nel titolo stampato del nucleo — es. l'heading interno `## N-SA02-05-04 · NEWS2: funzione, soglie e limiti` si rende in pagina come **"5.4 NEWS2: funzione, soglie e limiti"** (capitolo.progressivo-nucleo), mentre l'ID tecnico resta nel markdown per la matrice e i gate.

Implicazioni:
- Aggiornare la gerarchia di pagina del design system (punto 6 della lista dei 12) per registrare la numerazione decimale come elemento visivo stabile.
- Il front matter `06-indice.md` di ciascun volume deve includere le voci decimali, non solo i titoli di capitolo — cambia la generazione dell'indice (oggi verosimilmente chapters-only, come indicato dal Prompt 19: *"indice dei moduli chapters-only"*).
- Regola di derivazione numero-da-ID da definire e documentare nel design system, così resta stabile anche se un nucleo viene spostato.

### 6-bis.3 Il blocco `▣ Verifica` è un box nuovo, non ancora nella tassonomia

La tassonomia box esistente (12 nomi: *BANDO in pratica, Da sapere in 5 righe, Come lo chiede la commissione, Domanda-trappola, Errore tipico, Caso guidato, Risposta modello, Mini-esercizio, Checklist operativa, Bando Decoder, Diario errori, Fonti consolidate, Da verificare*) non ha un box dedicato a un **blocco di verifica strutturato che chiude un gruppo di nuclei** (6+ quiz e un caso, introdotto dal §1) — oggi "Mini-esercizio" è un box puntuale, non un raggruppamento ricorrente a cadenza fissa.

Il manuale Infermiere conferma il valore di questa scelta: chiude **ogni singolo capitolo** con un "Test di verifica" a posizione fissa — è esattamente ciò che i blocchi `▣ Verifica` del §1 fanno, con la differenza che ConcorsoBook li intercala anche a metà capitolo, non solo in chiusura. Aggiungere `▣ Verifica` come tredicesimo box canonico, con trattamento tipografico proprio (probabilmente un filetto Muted Gold di apertura/chiusura per segnalare visivamente il cambio di modalità lettura→autoverifica, coerente con la palette esistente).

### 6-bis.4 Tabelle e schemi comparativi: da eccezione a strumento di memorizzazione

Il design system attuale tratta le tabelle con cautela ("evitare tabelle fitte dentro il testo principale", "se una tabella supera la leggibilità, spostarla in appendice"). Il manuale Infermiere fa la scelta opposta e la dichiara esplicitamente in premessa: *"L'impostazione integrata e l'ampio ricorso a tabelle e schematizzazioni consentono di stabilire connessioni tra le discipline e facilitano la ripetizione e la memorizzazione delle nozioni"*.

Non è un conflitto da risolvere eliminando la cautela esistente — le regole di sicurezza tipografica del Prompt 18 (*"non usare più di tre colonne compatte negli esercizi; dividi le griglie dense invece di ridurre il carattere"*) restano valide e vincolanti per il formato KDP a colonna singola. È un cambio di **enfasi**: per i nuclei che si prestano al confronto (distinzioni tra profili, differenze normative, sequenze procedurali — esattamente la dimensione "Distinzioni" del §3-bis) va **preferita** una tabella comparativa a 2-3 colonne rispetto alla prosa continua, non trattata come ultima risorsa. Aggiornare la sezione "Tabelle e schemi" del design system per registrare questa preferenza, mantenendo il limite di 3 colonne compatte già in vigore.

### 6-bis.5 Cosa NON si prende dal manuale MIC AFAV

Il compendio AFAV struttura ogni micro-unità in 4 sezioni fisse (contenuti essenziali / infografiche e schemi / approfondimenti applicativi / espansioni digitali) — un pattern interessante, ma la sua esecuzione reale è un segnale di allarme, non un modello: il file è **interamente immagini** (345 JPG, zero testo estraibile), il che indica un compendio assemblato e impaginato senza controllo tipografico reale, incompatibile con la tracciabilità delle fonti che è il vantaggio competitivo di ConcorsoBook. **Non si adotta la struttura fissa a 4 sezioni per nucleo** — appesantirebbe la produzione senza beneficio dimostrato. Si adotta solo il principio già presente nel §1: ogni nucleo separa teoria essenziale da applicazione al profilo, che è la stessa idea senza il costo di 4 sotto-box rigidi.

### 6-bis.6 File da toccare (aggiunta alla tabella dell'§8)

| File | Modifica |
|---|---|
| `wiki/books/il-metodo-bando/design-system-editoriale.md` | aggiungere `▣ Verifica` alla tassonomia box (§6-bis.3); registrare la numerazione decimale visibile nella gerarchia di pagina (§6-bis.2); aggiornare la sezione tabelle con la preferenza per schemi comparativi sui nuclei a dimensione "Distinzioni" (§6-bis.4) |
| Generazione front matter (`front-matter/06-indice.md` per volume) | includere le voci decimali dei nuclei, non solo i titoli di capitolo (§6-bis.2) — individuare in fase di implementazione quale componente genera oggi questo file |
| `wiki/templates/prompt-staff-revisione-completa-volumi.md` | Prompt 19 (impaginazione KDP): aggiungere la resa del blocco `▣ Verifica` e della numerazione decimale alle regole del master editoriale |

---

## 7. Audit specialistico automatico e conferma umana finale

La policy §4 (pubblicare dati operativi con fonte) aumenta il rigore degli audit, non introduce dipendenze da revisori assegnati durante la produzione.

- Lo step 04 apre il volume senza nomi, costi o tempi di revisori e senza gate `review-non-assegnata`.
- Lo step 15 è un audit specialistico automatico del modulo. Verifica claim normativi e tecnici, procedure, soglie, dati mobili, casi, quiz e box `Dato operativo`; applica le correzioni e chiude ogni rilievo prima del text freeze.
- Nessuna criticità può essere marcata `pending` o rinviata a una persona per far avanzare il flusso. Se le fonti non consentono una formulazione affidabile, il testo va corretto, circoscritto o rimosso.
- Lo step 23 prepara soltanto il candidato di consegna. Lo step 24 è l'unico passaggio umano: conferma la validità del pacchetto già completo oppure lo respinge indicando i gate automatici da riaprire.
- La scheda pipeline non contiene una tabella di assegnazione nominativa dei revisori.

---

## 8. Elenco completo dei file da modificare

Le tabelle §3-bis.4 (copertura qualitativa) e §6-bis.6 (impaginazione) contengono le rispettive liste dedicate e non sono ripetute qui.

### Tooling (`src/`, `scripts/`, `tests/`)

| File | Modifica |
|---|---|
| `src/pipeline/gates/didactic-density-gate.ts` | **nuovo** — funzione pura sul modello di `chapter-lint-gate.ts` (§3.1-3.2) |
| `src/pipeline/gates/index.ts` | dispatch del nuovo gate + loader (§3.4 punto 1) |
| `src/pipeline/steps/registry.ts` | assegnazione gate agli step 08/10 (§3.4 punto 2) |
| `src/pipeline/cli/commands.ts` | riga soglie in `deliveryContract()` (§3.4 punto 3) |
| `src/server/editorial/didactic-coverage.ts` | nuove colonne matrice (§2); blocker `dimensione-mancante` (§3-bis.2); **unificare con** `scripts/audit-didactic-coverage.mjs` |
| `scripts/audit-didactic-coverage.mjs` | unificare la logica di parsing con `didactic-coverage.ts` invece di duplicarla (§2) |
| `src/pipeline/gates/coverage-gate.ts` | risoluzione per `Nucleo ID` invece che per numero di capitolo (§2); propagazione blocker `dimensione-mancante` (§3-bis.4) |
| `src/pipeline/spec/parse-volume-spec.ts` | tipo `VolumeSpecChapter`: soglie opzionali per capitolo (§3.5) |
| `src/pipeline/spec/validate-volume-spec.ts` | `validateChapter`: validazione delle soglie opzionali (§3.5) |
| `scripts/retrofit/audit-debito.mjs` | **nuovo** — audit del debito didattico, incluso campionamento dimensionale (§9.4.1, §3-bis.3) |
| `scripts/retrofit/pulisci-contratto.mjs` | **nuovo** — pulizia livello A0 (§9.4.2) |
| `scripts/retrofit/proponi-nuclei.mjs` | **nuovo** — proposta mappatura heading→Nucleo ID (§9.4.3) |
| `scripts/retrofit/estrai-item.mjs` | **nuovo** — estrazione banca item dai 71 quiz esistenti (§9.4.4) |
| `scripts/` | **nuovo script** aggregatore matrici di modulo → matrice di volume (§2) |
| `tests/pipeline/gates.test.ts` | nuovi casi per `didactic-density-gate` (§11) |
| `tests/pipeline/steps.test.ts` | aggiornare l'asserzione "ogni step automatico ha un gate" se si spostano gli id (§3.4) |
| `tests/didactic-coverage.test.ts` | test sulle nuove colonne, sul blocker dimensionale e sulla deduplicazione (§2, §3-bis.2) |

### Template e dottrina (`wiki/`)

| File | Modifica |
|---|---|
| `wiki/templates/didactic-coverage-matrix-template.md` | colonne `Nucleo ID`, `Verifica` strutturata (§2); colonne/tabella dimensionale (§3-bis.2) |
| `wiki/templates/prompt-staff-revisione-completa-volumi.md` | Prompt 08 (piano per nuclei), Prompt 09 (formato nuclei + box `Dato operativo` + soglie), Prompt 10 (verifica per ID **e checklist dimensionale**, §3-bis.4), Prompt 19 (blocco `▣ Verifica` e numerazione decimale in impaginazione, §6-bis.6); **nuovo Prompt 09-R** dedicato al retrofit (§9) |
| `wiki/templates/scheda-pipeline-volume-template.md` | soglie per capitolo; nessuna assegnazione nominativa di revisori (§3.5, §7) |
| `wiki/books/moduli/_template-modulo/chapter-template.md` | scheletro a nuclei (oggi prescrive solo 6 punti generici, non un formato) |
| `wiki/AGENTS.md` | gate di copertura, policy dato operativo, formato rinvii, campo `format_version` |
| `wiki/books/moduli/architettura-moduli-specialistici.md` | regola v4: rinvii verificati + livello del volume specialistico (§5, §6) |
| `wiki/books/il-metodo-bando/design-system-editoriale.md` | box `▣ Verifica`, numerazione decimale, enfasi tabelle comparative (§6-bis.6) |
| `docs/PIPELINE.md` | documentare il nuovo gate nella tabella "Gate implementati" |
| `.claude/skills/pipeline-volume/SKILL.md` | aggiornare la descrizione del loop per l'agente che guida la pipeline |

---

## 9. Retrofit del corpus già scritto

I miglioramenti valgono su tre fronti, come richiesto esplicitamente dall'utente: **volumi nuovi** (nascono direttamente in `format_version: 2`), **volumi in lavorazione** (VOL-02, VOL-07 — migrano nel ciclo 08-12 già in corso), **volumi già scritti e considerati completi** (retrofit dedicato, descritto in questa sezione).

### 9.1 Perimetro reale del debito

Dei 191 capitoli correnti in `wiki/books/**/chapters/*.md`, una quota è costituita da scaffold da scrivere direttamente in formato 2. Il report `wiki/reviews/retrofit/00-debito-didattico.md` è la fonte autoritativa per conteggi e priorità; la tabella seguente conserva la fotografia modulare usata per definire l'ordine iniziale:

| Modulo (percorso sotto `wiki/books/`) | Cap. | Parole | Senza quiz | Sotto 3.000 parole | Priorità e motivo |
|---|---:|---:|---:|---:|---|
| `il-metodo-bando/` (VOL-01) | 54 | 190.696 | 48 | 27 | **1 — prerequisito del blocker `rinvio-non-risolto` (§5)** |
| `moduli/m-fc02-agenzie-fiscali/` | 16 | 80.503 | 4 | 0 | 2 — il più vicino al traguardo, buon capitolo pilota |
| `moduli/m-fl01-comuni-unioni/` | 15 | 69.451 | 9 | 1 | 3 — VOL-02, in lavorazione |
| `moduli/m-fc04-giustizia/` | 15 | 71.256 | 10 | 1 | 4 — VOL-04 |
| `moduli/m-fl02-regioni-province-citta-metropolitane/` | 13 | 53.349 | 8 | 1 | 5 — VOL-02 |
| `moduli/m-fc05-authority-indipendenti/` | 16 | 44.100 | **16** | 10 | 6 — VOL-05, caso peggiore per copertura quiz |
| `moduli/m-fl04-polizia-locale/` | 16 | 33.729 | 13 | 15 | 7 — VOL-02, mediana 2.073 parole |
| `moduli/m-fl03-camere-commercio/` | 6 | 16.093 | 6 | 5 | 8 — VOL-02 |
| `moduli/m-sa01…04-*/` (VOL-07, nel worktree) | 25 | ~120.000 | 22 | 3 | in lavorazione, vedi §10 (pilota) |

### 9.2 La struttura legacy è già compatibile — non è una riscrittura da zero

Ispezione di un capitolo reale (`wiki/books/moduli/m-fc05-authority-indipendenti/chapters/02-indipendenza-governance-accountability-personale.md`, 2.684 parole):

```
## Scheda di lavoro                     ← contenuto interno di processo, NON deve stare nel libro
## Testo editoriale
   ### Apertura editoriale
   ### Obiettivo operativo del capitolo
   ### Indipendenza: una garanzia, non un privilegio      ┐
   ### Governance: chi decide e chi istruisce             │ questi SONO
   ### Accountability: autonomia controllabile            │ i nuclei
   ### Personale: perché non esiste una scorciatoia unica ┘
   ### Mappa BANDO
   ### Caso guidato: …          ┐
   ### Domanda da commissario   │ questo È l'embrione
   ### Domanda-trappola         │ del blocco di verifica
   ### Errore tipico            │
   ### Mini-esercizio           ┘
   ### Riferimenti consolidati
   ### Note di review editoriale         ← contenuto interno di processo, NON deve stare nel libro
```

**Il formato a nuclei non è una rottura del corpus esistente: è la sua formalizzazione.** Le sezioni sostanziali sono già lì, l'apparato didattico è già lì. Mancano gli ID, i quiz e la pulizia del confine tra "testo per il lettore" e "artefatti di processo editoriale".

Rilievo quantitativo corpus-wide, sui 155 capitoli sostanziali (>400 parole, esclusi gli scaffold):

| Rilievo | Capitoli coinvolti |
|---|---:|
| Con `### Note di review editoriale` **esposta nel corpo del capitolo** | **141 su 155** |
| Con `## Scheda di lavoro` (contenuto puramente interno di processo) nel corpo | **77 su 155** |
| Con apparato didattico già presente (`Domanda da commissario` + `Mini-esercizio`) | **143 su 155** |

Il primo rilievo è lo stesso difetto già trovato e corretto su VOL-07, modulo M-SA02, capitoli 01 e 03, e classificato **Grave** in `wiki/reviews/pipeline/VOL-07/2026-07-30-remediation-contratto-studente-m-sa02-01-03.md`: gergo interno e artefatti di processo esposti allo studente che ha pagato il libro (esempio citato nel report: link a `sources/` non disponibili al lettore, formule come «source note consolidata»). Su VOL-07 è stato risolto su 2 capitoli; **nel resto del corpus è aperto su 141**.

### 9.3 Tre livelli di intervento, costi molto diversi

**Livello A0 — contratto dello studente (puramente meccanico, nessuna decisione editoriale).**
Rimuovere dal corpo del capitolo `## Scheda di lavoro` e `### Note di review editoriale`, archiviandoli in `wiki/reviews/`. Appiattire il contenitore `## Testo editoriale` (i suoi `###` salgono a `##`). Precedente già applicato e verbalizzato su VOL-07 (vedi il report citato sopra). **Scriptabile quasi al 100%**: un audit automatico del diff e i test del contratto studente devono dimostrare che nessun contenuto didattico è stato rimosso; la conferma umana resta allo step 24.

**Livello A — apparato didattico (meccanico, nessuna nuova fonte richiesta).**
Assegnare i `Nucleo ID` alle sezioni sostanziali già esistenti (già identificate nell'ispezione §9.2) e raggruppare l'apparato già presente (`Caso guidato`, `Domanda da commissario`, `Domanda-trappola`, `Mini-esercizio`) in un blocco `▣ Verifica`, **completandolo con i quiz mancanti derivati dal testo già scritto e già passato per l'audit editoriale**. Punto chiave: questi quiz non introducono claim normativi o fattuali nuovi — sono derivati dal contenuto già verificato — quindi **non aprono un nuovo ciclo di audit normativo**; il gate deve dimostrare automaticamente che ogni item è derivabile dal testo esistente. Copre il difetto più grave del corpus (162 capitoli correnti a zero quiz) al costo più basso, partendo dall'apparato già presente dove disponibile.

**Livello B — densità (sostanziale, richiede fonti nuove e audit specialistico completo).**
Portare a soglia gli 86 capitoli correnti sotto le 3.000 parole. Qui servono fonti nuove, scrittura e audit automatici completi: è lavoro di pipeline vera, da svolgere modulo per modulo attraverso tutti i gate previsti, senza dipendenze umane prima dello step 24.

Il mix di livelli necessari cambia molto per modulo — esempi dalla tabella §9.1:
- `m-fc02-agenzie-fiscali`: 0 capitoli sotto soglia parole → serve solo **A** (quiz) su 4 capitoli.
- `m-fc05-authority-indipendenti`: 16 capitoli senza quiz e 10 sotto soglia → serve **A0+A su tutti i 16, più B sui 10** sotto soglia.
- `m-fl04-polizia-locale`: il caso più costoso, 15 capitoli su 16 sotto soglia **e** 13 senza quiz → **A0+A+B quasi ovunque**.

### 9.4 Strumenti di supporto al retrofit

Quattro script nuovi in `scripts/retrofit/`, tutti in sola lettura tranne dove indicato:

1. **`audit-debito.mjs`** — gira su tutti i capitoli del corpus e produce `wiki/reviews/retrofit/00-debito-didattico.md`: per ogni capitolo, parole / nuclei / quiz / casi attuali, delta rispetto alle soglie del §1, livello di intervento richiesto (A0, A, B, o combinazione), stima. **Deve condividere il codice di conteggio con `didactic-density-gate.ts`** (§3.1), non duplicarlo — è esattamente l'errore già commesso col parsing delle matrici (§2), da non ripetere.
2. **`pulisci-contratto.mjs`** — implementa il livello A0. Rimuove `## Scheda di lavoro` e `### Note di review editoriale` dal corpo, archiviandoli in `wiki/reviews/retrofit/<modulo>/<capitolo>.md`, e appiattisce `## Testo editoriale`. **È l'unico dei quattro script che scrive nei file**; va eseguito su un branch dedicato, con il diff rivisto capitolo per capitolo prima del merge.
3. **`proponi-nuclei.mjs`** — legge gli heading `##`/`###` esistenti di un capitolo e **propone** (non scrive) una mappatura heading → `Nucleo ID`, incrociandola con le righe della matrice di copertura del modulo corrispondente. Produce un piano testuale che l'agente valida contro matrice, unicità degli ID e gate prima di applicarlo; la conferma umana resta allo step 24.
4. **`estrai-item.mjs`** — estrae i 71 quiz già presenti nel corpus (identificati dal pattern `Risposta corretta:`) in una banca item strutturata con ID e tag di nucleo di provenienza. Oggi questi item sono inline nei capitoli, senza ID, senza tag, non estraibili; la cartella `wiki/quizzes/` contiene un solo file demo generato programmaticamente e non collegato a nessun capitolo reale del corpus.

### 9.5 Sequenza del retrofit

- **Fase 0 — misura.** Unificare il parsing della matrice (§2), implementare `didactic-density-gate` con la modalità legacy (§3.3), far girare `audit-debito.mjs`. Output: il backlog completo del debito con le stime per modulo. **Nessun capitolo viene modificato in questa fase.**
- **Fase 1 — ancore di VOL-01.** Stabilizzare la struttura di heading di `wiki/books/il-metodo-bando/` e assegnarne i `Nucleo ID`. Questo sblocca il blocker `rinvio-non-risolto` per tutti gli altri volumi (§5): è un **prerequisito**, non un'opzione posticipabile, perché nessun rinvio negli altri moduli può risolversi finché VOL-01 non ha ancore stabili.
- **Fase 2 — livello A0 su tutto il corpus, in un colpo solo.** È scriptabile e non richiede decisioni editoriali caso per caso: 141 capitoli smettono di esporre note di review interne al lettore, 77 smettono di contenere la scheda di lavoro interna. Un branch, un diff complessivo e un audit automatico. **È l'intervento con il miglior rapporto valore/costo di tutto il piano.**
- **Fase 3 — livello A, modulo per modulo**, nell'ordine di priorità della tabella §9.1. Ogni capitolo trattato esce con `format_version: 2` nel frontmatter.
- **Fase 4 — livello B per priorità commerciale**, con il ciclo completo degli step 08-12 sui capitoli sotto soglia, iniziando dai volumi più vicini alla pubblicazione.
- **Fase 5 — rimozione della modalità legacy.** Una volta che il backlog di Fase 3-4 è esaurito, il gate blocca ovunque incondizionatamente. Da questo momento in poi nessun capitolo può regredire sotto le soglie.

Il retrofit non si esegue in un blocco unico isolato: procede **in parallelo** alla produzione dei volumi nuovi. La modalità legacy tiene il sistema "verde" (nessun volume in lavorazione si blocca inaspettatamente) nel frattempo, e il backlog prodotto dalla Fase 0 rende il debito visibile e quantificato invece che implicito come è oggi.

---

## 10. Pilota

**Pilota del formato: modulo M-SA02 di VOL-07** — ha il campione di bandi rappresentativi più solido del progetto (16 bandi ufficiali inPA, conservati con URL/byte/SHA-256 in `wiki/raw/m-sa02-professioni-sanitarie/bandi/`, denominatori dichiarati per cluster) ed è il modulo con il mercato potenziale più ampio (infermieri, principale professione sanitaria per numero di concorsi).

Sequenza del pilota:
1. Fase 0 del §9.5 (tooling di base + audit del debito), applicata almeno al perimetro di VOL-07 e VOL-01.
2. Riscrivere la matrice di copertura di M-SA02 (`wiki/books/moduli/m-sa02-professioni-sanitarie/planning/02-matrice-copertura-didattica.md`) nel nuovo formato del §2, assegnando i `Nucleo ID`.
3. Rilanciare gli step 08-12 del protocollo sul **capitolo 05** (`wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/05-valutazione-clinica-triage-urgenza-emergenza.md`, triage/emergenza): è il capitolo dove convergono tutti i pezzi nuovi — formato a nuclei, box `Dato operativo` per NEWS2/scale cliniche, blocchi di verifica.
4. In parallelo, provare il **livello A** del retrofit (§9.3) su un capitolo di `m-fc02-agenzie-fiscali` (il modulo più sano del corpus legacy) per calibrare il costo reale dell'intervento meccanico su un caso favorevole.
5. Misurare entrambi i binari: parole prodotte, nuclei creati, quiz prodotti, righe di matrice risolte, ore di lavoro effettive, esiti del gate.
6. Solo se entrambi reggono la misurazione: estendere il formato agli altri 8 capitoli di M-SA02 e avviare formalmente la Fase 1 del retrofit (VOL-01) su tutto `il-metodo-bando`.

**Risultati misurati il 2026-08-01**

| Binario | Parole | Nuclei | Quiz | Casi | Matrice | Gate |
|---|---:|---:|---:|---:|---|---|
| M-SA02/05 | 6.634 | 7 (613–854 parole) | 7 | 3 | 7 righe v2 con checklist | densità, copertura, lint, citazioni e audit step 15 verdi |
| M-FC02/04, livello A | 8.388 | 6 (860–1.251 parole) | 6 | 1 | overlay di 6 righe v2; storico legacy preservato | densità e copertura verdi senza warning |

Il campione M-FC02 mostra che la proposta automatica grezza non è sufficiente: aveva prodotto 22 candidati da heading. Il costo reale del livello A include il raggruppamento editoriale degli H2 in nuclei sostanziali. Sul caso favorevole non sono servite nuove fonti né nuova teoria: sono bastati ristrutturazione degli heading, un quiz derivato dal testo e la checklist dimensionale.

**Precondizione soddisfatta il 2026-08-01**: il worktree `.worktrees/vol-07-pipeline-start` è stato integrato in `main` con il modello ibrido e la nuova sequenza automatica. Il pilota può quindi partire da un worktree isolato basato sul commit di integrazione.

**Vincolo di rilascio aggiornato**: il pilota deve superare l'audit specialistico automatico dello step 15 e tutti i gate successivi senza dipendere da persone. La sola conferma umana resta allo step 24, quando testi e pacchetto sono già completi. L'obiettivo resta portare **un solo modulo** fino al candidato di pubblicazione e ritarare le soglie quantitative sui risultati reali, prima di aprire la scrittura del terzo volume del catalogo a 12 volumi.

---

## 11. Verifica end-to-end

Checklist per l'agente implementatore, da eseguire in quest'ordine:

1. `npm test` — devono passare i nuovi test di `didactic-density-gate`: capitolo conforme (nessun blocker); nuclei insufficienti; ID nucleo malformato; nucleo troppo breve; verifica assente; verifica troppo distante da nuclei precedenti; quiz insufficienti; capitolo troppo breve; heading dentro un code fence correttamente ignorati (riuso di `headingsOf`); **`format_version: 1` produce solo warning, mai blocker**; `format_version: 2` applica i blocker normalmente. Più la regressione sui gate esistenti: `chapter-lint`, `coverage`, `citation-guard`, e su `steps.test.ts`.
2. `npm run typecheck` — nessun errore introdotto.
3. `npm run audit:coverage` — deve girare senza errori di parsing sulle matrici migrate al nuovo formato e produrre lo stesso esito del gate `coverage` sullo stesso input (prova diretta che la deduplicazione della logica del §2 è riuscita: se i due comandi divergono su uno stesso file, la deduplicazione non è completa).
4. `node scripts/retrofit/audit-debito.mjs` (sull'intero `wiki/books/`) — i totali prodotti devono riprodurre la misura corrente (191 capitoli, 162 senza quiz, 86 sotto soglia parole); se divergono, il conteggio del gate e quello dello script di audit non condividono davvero lo stesso codice (violazione del vincolo del §9.4 punto 1).
5. `npm run pipeline -- gate VOL-07 --step 10 --chapter <target del cap. 05 M-SA02>` — comando in sola lettura: la versione legacy deve passare con il solo warning `retrofit-dovuto`; una versione dichiarata `format_version: 2` ma incompleta deve fallire; la versione v2 finale deve passare senza blocker.
6. `npm run pipeline -- status VOL-02` e `npm run pipeline -- status VOL-03` — devono restare **verdi** (nessuno step che va in `blocked`) subito dopo l'accensione del nuovo gate nel registry, grazie alla modalità legacy. Se uno dei due passa a `blocked`, la modalità legacy non sta funzionando come previsto e va corretta prima di procedere oltre.
7. **Copertura qualitativa (§3-bis)**: sul capitolo 05 pilota, verificare che la checklist dimensionale sia compilata per ciascun `Nucleo ID` con evidenza citata (non solo ✓/✗ senza riferimento) e che il blocker `dimensione-mancante` si attivi davvero rimuovendo manualmente una dimensione da un nucleo di test (es. cancellare la frase che marca una distinzione) e verificando che il gate `coverage` lo segnali.
8. **Impaginazione (§6-bis)**: sul PDF impaginato del capitolo 05 pilota (fase KDP, step 19-20 del protocollo) verificare che il blocco `▣ Verifica` sia visivamente distinto e non si spezzi male tra una pagina e l'altra; che la numerazione decimale visibile (es. "5.4") compaia nel titolo stampato del nucleo e nell'indice del volume; che le tabelle dei box `Dato operativo` e degli schemi comparativi restino entro le tre colonne compatte previste dal design system (`wiki/books/il-metodo-bando/design-system-editoriale.md`); che il volume resti in bianco e nero come da decisione §6-bis.1.

---

## Riferimenti rapidi per chi implementa

- Protocollo dei 25 prompt (dottrina editoriale): `wiki/templates/prompt-staff-revisione-completa-volumi.md`
- Regole vincolanti del progetto: `wiki/AGENTS.md` (root) e `AGENTS.md` (root repo)
- Dottrina di copertura qualitativa già esistente (fonte del §3-bis): `wiki/AGENTS.md` sezione "Gate globale di copertura didattica integrale" + `wiki/sources/principio-copertura-didattica-integrale-2026-07-17`
- Design system editoriale della collana (fonte e target del §6-bis): `wiki/books/il-metodo-bando/design-system-editoriale.md`
- Architettura moduli/volumi: `wiki/books/moduli/architettura-moduli-specialistici.md`
- Documentazione tecnica esistente della pipeline: `docs/PIPELINE.md`
- Skill che guida l'esecuzione della pipeline per un volume: `.claude/skills/pipeline-volume/SKILL.md`
- Esempio di remediation "contratto dello studente" già eseguita (precedente diretto del livello A0): `wiki/reviews/pipeline/VOL-07/2026-07-30-remediation-contratto-studente-m-sa02-01-03.md`
- Bibbia del Volume VOL-07 (fonte della policy sui dati operativi e sugli audit specialistici): `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/04-bibbia-del-volume.md`
