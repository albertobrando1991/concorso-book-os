# VOL-12 — Avvio progressivo della pipeline editoriale completa

**Data:** 2026-08-10

**Volume:** VOL-12 — Carriere speciali premium

**Cut-off delle fonti:** 2026-08-10

**Stato:** approvato per la pianificazione esecutiva

## Obiettivo

Portare VOL-12 attraverso l'intero protocollo editoriale di 25 step, dal censimento iniziale alla preparazione del pacchetto di pubblicazione, rispettando l'ordine e i gate del CLI. L'esecuzione termina allo step 24, che resta l'unico passaggio di conferma umana.

## Stato iniziale verificato

- `npm run pipeline -- doctor --json` restituisce `ok: true`.
- Non esiste ancora `pipeline/VOL-12/run-state.json`.
- Non esiste una scheda con `volume_code: VOL-12`.
- VOL-12 è definito dall'architettura canonica come volume premium composto da M-SP01, M-SP02, M-SP03 e M-SP04.
- I quattro moduli hanno `index.md` e `planning/00-piano-editoriale.md`, ma sono ancora scaffold.
- Non risultano capitoli pubblicabili né matrici di copertura specifiche per questi moduli.

## Decisione

La pipeline viene configurata ed eseguita in due aperture consecutive dello stesso run-state.

### Apertura 1 — Fondazioni, fasi A e B

Creare il volume aggregatore in `wiki/books/volumi/vol-12-carriere-speciali-premium/` e la prima versione di `planning/00-scheda-pipeline.md` con:

- `volume_code: VOL-12`;
- `volume_title: Carriere speciali premium`;
- `cut_off_date: 2026-08-10`;
- `writer_provider: codex`;
- `phases: [A, B]`;
- moduli, nell'ordine canonico: M-SP01, M-SP02, M-SP03, M-SP04;
- nessuna assegnazione nominativa di revisori;
- nessun capitolo inventato o derivato da cartelle vuote.

Eseguire gli step 00-07 tramite `next` e `complete`. I gate non automatizzati devono essere verificati manualmente e chiusi con `--accept --note` soltanto quando la verifica richiesta dal prompt è stata realmente svolta. Lo step 07 deve produrre matrici di copertura senza stati bloccanti.

### Apertura 2 — Produzione e pubblicazione, fasi C-F

Al termine della fase B, consolidare nella scheda:

- i capitoli approvati per ciascun modulo;
- titolo editoriale, file, matrice, stato atteso, soglia minima di parole e quiz;
- `phases: [A, B, C, D, E, F]`;
- le stesse priorità dei moduli, salvo una diversa decisione documentata emersa dagli audit dei bandi.

Eseguire `npm run pipeline -- sync VOL-12 --json` per aggiungere i target al run-state senza modificarlo a mano. Proseguire quindi con gli step 08-23, capitolo per capitolo e modulo per modulo. Lo step 24 resta in attesa della conferma umana finale.

## Ordine dei moduli

1. M-SP01 — Polizia, Carabinieri e Guardia di Finanza.
2. M-SP02 — Vigili del Fuoco.
3. M-SP03 — Magistratura, Avvocatura e Notariato.
4. M-SP04 — Prefettizia e diplomatica.

L'ordine segue l'architettura canonica. Può cambiare soltanto se gli step 05-07 producono evidenza editoriale sufficiente e la decisione viene registrata nella scheda e nella memoria operativa.

## Flusso di esecuzione

Per ogni target:

1. richiamare `LocalAgentMemory` con scope VOL-12 e del modulo pertinente;
2. interrogare il CLI con `status --json` e `next --json`;
3. leggere integralmente il prompt renderizzato dal CLI;
4. eseguire il lavoro richiesto usando la skill prescritta per lo step;
5. eseguire `complete --json`;
6. se il gate blocca, correggere lo stesso target e ripetere senza avanzare;
7. registrare una traccia sintetica in `LocalAgentMemory` dopo ogni flusso importante.

Le skill obbligatorie restano:

- step 09: `concorso-book-professional-writer`;
- step 11: `humanizer`;
- step 12, 13, 15 e 21: `revisore-editoriale-totale`;
- step 17 e 18: `canvas-design`.

## Gestione dei gate e degli errori

- Il run-state non viene mai modificato a mano.
- Un esito `gate-not-implemented` non equivale a un gate verde: richiede verifica manuale documentata e `--accept --note`.
- Gli stati `mancante`, `solo-nominato` e `parziale` nella copertura impediscono l'avanzamento.
- I capitoli della fase C devono essere in formato 2 e superare le soglie dichiarate nel contratto prodotto da `next`.
- Per le carriere speciali, fonti settoriali, bandi rappresentativi e audit specialistico sono prerequisiti del text freeze.
- Dati normativi, ordinamenti, requisiti, prove fisiche o procedure non possono essere inventati né ricavati dalla memoria agentica.
- Lo step 24 non viene autoaccettato e non viene dichiarato concluso senza conferma umana.

## Artefatti previsti

- volume aggregatore e scheda pipeline VOL-12;
- run-state generato dal CLI;
- report degli step 00-07;
- dossier dei bandi e fonti consolidate;
- matrici di copertura di volume e modulo;
- piani e capitoli pubblicabili in formato 2;
- report di revisione, audit specialistici e text freeze;
- filosofia visiva, asset, impaginato e audit pagina per pagina;
- revisione finale, preflight e pacchetto di consegna;
- stato finale `awaiting-human-signoff` allo step 24.

## Verifica

Ogni transizione viene valutata sul JSON restituito dal CLI. Prima di dichiarare completata una fase si verificano almeno:

- `npm run pipeline -- status VOL-12 --json`;
- gate pertinenti dello step;
- test e typecheck quando il lavoro modifica codice o strumenti;
- assenza di errori in `git diff --check`;
- tracciabilità degli artefatti e memoria operativa aggiornata.

## Criterio di successo

VOL-12 raggiunge lo step 24 con tutti gli step 00-23 completati, nessun blocker aperto, testi e fonti congelati, impaginato verificato, preflight verde e pacchetto di consegna pronto. La pubblicazione resta subordinata alla conferma umana finale.
