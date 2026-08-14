# VOL-08 Final Publication Package Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Completare il pacchetto di pubblicazione di VOL-08 con identità commerciale coerente nell'interno, copertina paperback KDP originale e verificata, metadati definitivi, manifest integro e soli controlli esterni KDP lasciati aperti.

**Architecture:** I metadati commerciali diventano proprietà opzionali del catalogo dei volumi e alimentano il frontespizio generato dal Book Studio. Una coppia di script focalizzati conserva geometria/copy della copertina e genera HTML vettoriale, PDF CMYK e anteprima PNG senza introdurre dipendenze npm. La documentazione di consegna registra in modo verificabile artefatti, limiti esterni, parametri KDP, audit e checksum.

**Tech Stack:** TypeScript 5.7, Node.js 20+, Vitest, Playwright/Chromium, HTML/CSS/SVG vettoriale, MuPDF `mutool`, Markdown, PowerShell, pipeline CLI ConcorsoBook OS.

## Global Constraints

- Titolo: `ICT, digitale, cybersecurity e dati`.
- Sottotitolo: `Manuale specialistico per concorsi pubblici — informatica, cloud, cybersecurity, dati e intelligenza artificiale`.
- Nome autoriale pubblico: `Capitale Personale`.
- Collana e numero: `ConcorsoBook OS`, `VOL-08`.
- ISBN: ISBN gratuito KDP; imprint `Independently published`; nessun ISBN o codice a barre incorporato nei file.
- Paperback: `6.69 × 9.61 in`, inchiostro nero su carta bianca, interno senza bleed, copertina opaca.
- Baseline interna: `231` pagine; se la rigenerazione produce un conteggio diverso, il dorso e la geometria della copertina devono essere ricalcolati prima della consegna.
- Dorso alla baseline: `231 × 0.002252 in = 0.520212 in`.
- Copertina alla baseline: `14.150212 × 9.86 in`, una pagina, ordine quarta-dorso-prima, bleed esterno `0.125 in`.
- Palette: `#F3EFE6`, `#173247`, `#8A3147`, `#2D7480`, `#25292C`, `#B59A63`.
- Grafica originale `Circuito Civico`; nessuna fotografia stock, figura umana, lucchetto, felpa con cappuccio o imitazione di copertine/artisti esistenti.
- Area codice a barre libera; KDP inserirà il codice automaticamente.
- PDF finale CMYK, font incorporati, trasparenze appiattite, nessun segno di taglio o template visibile; anteprima PNG a 300 DPI.
- Non modificare manualmente `pipeline/VOL-08/run-state.json`.
- Preservare tutte le modifiche estranee già presenti nel worktree; staging esclusivamente per percorsi VOL-08 esplicitamente verificati.
- Dichiarazione KDP trasparente: testo generato con sistemi di IA e sottoposto a revisione professionale; copertina costituita da grafica vettoriale originale generata programmaticamente, senza immagine generativa.

---

### Task 1: Identità commerciale nel catalogo e nel frontespizio

**Files:**
- Modify: `src/catalog/text-volumes.ts`
- Modify: `src/server/book/book-preview.ts`
- Modify: `tests/book-preview.test.ts`

**Interfaces:**
- Consumes: `TextVolume`, `buildBookStudioData(store, bookId)` e il flusso esistente di front matter generato.
- Produces: proprietà opzionali `subtitle?: string`, `author?: string`, `edition?: string`; frontespizio e copyright generati con i valori commerciali esatti di VOL-08.

- [ ] **Step 1: Aggiungere un test di regressione fallente per VOL-08**

  Integrare il test del volume composto o aggiungere un caso dedicato che costruisca `volumi/vol-08`, estragga i blocchi generati di `Frontespizio` e `Copyright e note editoriali` e verifichi:

  ```ts
  expect(titlePageText).toContain("Manuale specialistico per concorsi pubblici — informatica, cloud, cybersecurity, dati e intelligenza artificiale")
  expect(titlePageText).toContain("Capitale Personale")
  expect(copyrightText).toContain("© 2026 Capitale Personale. Tutti i diritti riservati.")
  expect(copyrightText).toContain("Prima edizione, 2026.")
  expect(`${titlePageText} ${copyrightText}`).not.toMatch(/ISBN\s*[:0-9]/i)
  ```

- [ ] **Step 2: Eseguire il test e confermare il rosso**

  Run: `npx vitest run tests/book-preview.test.ts`

  Expected: FAIL perché il sottotitolo commerciale, la riga di copyright e l'edizione non sono ancora prodotti.

- [ ] **Step 3: Estendere il tipo e il record VOL-08**

  In `TextVolume` aggiungere:

  ```ts
  subtitle?: string
  author?: string
  edition?: string
  ```

  Nel record `VOL-08` impostare:

  ```ts
  subtitle: "Manuale specialistico per concorsi pubblici — informatica, cloud, cybersecurity, dati e intelligenza artificiale",
  author: "Capitale Personale",
  edition: "Prima edizione, 2026",
  ```

- [ ] **Step 4: Rendere frontespizio e copyright metadata-driven**

  In `buildVolumeTitlePageMarkdown` usare `volume.subtitle || volume.promise`, `volume.author || "Capitale Personale"` e aggiungere l'edizione solo quando presente. In `buildVolumeCopyrightMarkdown` aggiungere, solo quando `author`/`edition` esistono, le righe:

  ```ts
  `© 2026 ${volume.author}. Tutti i diritti riservati.`,
  `${volume.edition}.`,
  ```

  Conservare intatte le note editoriali e normative già corrette e non introdurre un numero ISBN.

- [ ] **Step 5: Eseguire test mirato, typecheck e controllo diff**

  Run: `npx vitest run tests/book-preview.test.ts`

  Expected: PASS.

  Run: `npm run typecheck`

  Expected: exit code 0.

  Run: `git diff --check -- src/catalog/text-volumes.ts src/server/book/book-preview.ts tests/book-preview.test.ts`

  Expected: nessun output.

- [ ] **Step 6: Commit chirurgico**

  ```powershell
  git add -- src/catalog/text-volumes.ts src/server/book/book-preview.ts tests/book-preview.test.ts
  git diff --cached --name-only
  git commit -m "feat(vol-08): align interior commercial identity"
  ```

  Expected staged paths: soltanto i tre file elencati.

### Task 2: Motore riproducibile della copertina KDP

**Files:**
- Create: `scripts/vol08-kdp-cover-core.mjs`
- Create: `scripts/generate-vol08-kdp-cover.mjs`
- Create: `tests/vol08-kdp-cover.test.ts`

**Interfaces:**
- Consumes: Playwright disponibile in `@playwright/test`, MuPDF `mutool`, font Windows Arial/Garamond e specifica `docs/superpowers/specs/2026-08-14-vol-08-kdp-cover-design.md`.
- Produces: `VOL08_COVER_SPEC`, `calculateCoverGeometry(pageCount)`, `buildVol08CoverHtml(input)`, `resolveMutoolPath()`, generatore CLI di PDF/PNG.

- [ ] **Step 1: Scrivere i test fallenti della geometria e del contenuto**

  In `tests/vol08-kdp-cover.test.ts` importare il core `.mjs` e verificare almeno:

  ```ts
  const geometry = calculateCoverGeometry(231)
  expect(geometry.spineIn).toBeCloseTo(0.520212, 6)
  expect(geometry.widthIn).toBeCloseTo(14.150212, 6)
  expect(geometry.heightIn).toBeCloseTo(9.86, 6)

  const html = buildVol08CoverHtml({ pageCount: 231 })
  expect(html).toContain("ICT, digitale, cybersecurity e dati")
  expect(html).toContain("Manuale specialistico per concorsi pubblici — informatica, cloud, cybersecurity, dati e intelligenza artificiale")
  expect(html).toContain("Capitale Personale")
  expect(html).toContain("barcode-safe")
  expect(html).not.toMatch(/ISBN\s*[:0-9]/i)
  expect(html).not.toMatch(/crop-mark|template-overlay/i)
  ```

- [ ] **Step 2: Eseguire il test e confermare il rosso**

  Run: `npx vitest run tests/vol08-kdp-cover.test.ts`

  Expected: FAIL perché i moduli non esistono.

- [ ] **Step 3: Implementare costanti e geometria nel core**

  Esportare un oggetto immutabile con copy, palette e dimensioni approvate. Implementare:

  ```js
  export function calculateCoverGeometry(pageCount) {
    if (!Number.isInteger(pageCount) || pageCount < 24) throw new Error("pageCount must be an integer >= 24")
    const spineIn = pageCount * 0.002252
    return {
      pageCount,
      trimWidthIn: 6.69,
      trimHeightIn: 9.61,
      bleedIn: 0.125,
      spineIn,
      widthIn: 0.125 + 6.69 + spineIn + 6.69 + 0.125,
      heightIn: 0.125 + 9.61 + 0.125
    }
  }
  ```

- [ ] **Step 4: Implementare il canvas HTML vettoriale**

  `buildVol08CoverHtml({ pageCount })` deve produrre una pagina senza scroll con tre regioni geometriche esatte: `.back-cover`, `.spine`, `.front-cover`. Usare solo CSS/SVG originali: fondo avorio esteso al bleed, circuito a linee e nodi, campo navy sul dorso, ancoraggio tipografico su `cybersecurity`, quarta con il copy approvato e rettangolo `.barcode-safe` privo di testo essenziale.

  Le regole CSS devono includere font locali incorporabili:

  ```css
  @font-face { font-family: "CoverArial"; src: url("file:///C:/Windows/Fonts/arial.ttf"); }
  @font-face { font-family: "CoverArial"; src: url("file:///C:/Windows/Fonts/arialbd.ttf"); font-weight: 700; }
  @font-face { font-family: "CoverGaramond"; src: url("file:///C:/Windows/Fonts/GARA.TTF"); }
  ```

  I testi della quarta devono restare almeno a 9 pt; i testi di prima e quarta almeno `0.125 in` dentro il taglio; il dorso almeno `0.0625 in` dai bordi.

- [ ] **Step 5: Implementare il generatore CLI**

  Il CLI deve:

  1. leggere `--page-count` con default `231`;
  2. risolvere `mutool` da `MUTOOL_PATH`, dal `PATH` o da `C:\Program Files (x86)\bit4id\namirialsign\etc\sign_engine\mutool.exe`;
  3. creare una directory temporanea in `os.tmpdir()`;
  4. usare Chromium per stampare l'HTML in PDF della misura restituita da `calculateCoverGeometry`;
  5. convertire il PDF intermedio nel PDF finale con `mutool draw -F pdf -c cmyk`;
  6. renderizzare `vol-08-cover-kdp-preview.png` con `mutool draw -F png -c rgb -r 300`;
  7. fallire con messaggio esplicito se mancano Chromium, font o `mutool`;
  8. rimuovere soltanto la directory temporanea creata dal processo.

- [ ] **Step 6: Eseguire test e controlli statici**

  Run: `npx vitest run tests/vol08-kdp-cover.test.ts`

  Expected: PASS.

  Run: `node --check scripts/vol08-kdp-cover-core.mjs`

  Expected: exit code 0.

  Run: `node --check scripts/generate-vol08-kdp-cover.mjs`

  Expected: exit code 0.

- [ ] **Step 7: Commit chirurgico**

  ```powershell
  git add -- scripts/vol08-kdp-cover-core.mjs scripts/generate-vol08-kdp-cover.mjs tests/vol08-kdp-cover.test.ts
  git diff --cached --name-only
  git commit -m "feat(vol-08): add reproducible KDP cover generator"
  ```

  Expected staged paths: soltanto i tre file elencati.

### Task 3: Generazione, ispezione e riconciliazione geometrica

**Files:**
- Create: `delivery/VOL-08/candidate/vol-08-cover-kdp.pdf`
- Create: `delivery/VOL-08/candidate/vol-08-cover-kdp-preview.png`
- Modify: `delivery/VOL-08/candidate/vol-08-interior-kdp.pdf`
- Modify: `delivery/VOL-08/candidate/PREFLIGHT.md`

**Interfaces:**
- Consumes: generatore della Task 2, Book Studio e `scripts/export-book-studio-volume-pdf.mjs`.
- Produces: interno rigenerato, conteggio pagina definitivo, copertina coerente con quel conteggio e audit visivo/tecnico registrato.

- [ ] **Step 1: Rigenerare l'interno dal Book Studio isolato su VOL-08**

  Avviare l'app con `BOOK_STUDIO_BOOK_ID=volumi/vol-08`, usare una porta libera e lanciare l'export verso `delivery/VOL-08/candidate/vol-08-interior-kdp.pdf`. Non riusare un server privo della variabile di isolamento.

- [ ] **Step 2: Misurare il PDF interno appena generato**

  Validare che il PDF abbia una sola dimensione pagina `6.69 × 9.61 in`, nessuna pagina vuota anomala e conteggio atteso `231`. Se il conteggio differisce, passare il valore effettivo a tutti i passi successivi e aggiornare nella specifica i soli dati derivati di dorso/larghezza.

- [ ] **Step 3: Generare PDF e PNG di copertina**

  Run: `node scripts/generate-vol08-kdp-cover.mjs --page-count 231`

  Expected: creazione dei due artefatti nella candidate directory e riepilogo JSON con pagina, dorso, larghezza, altezza e percorsi.

- [ ] **Step 4: Verificare struttura e dimensioni del PDF**

  Controllare programmaticamente:

  ```text
  page count = 1
  MediaBox = 1018.815264 × 709.92 pt (tolleranza 0.02 pt)
  preview = circa 4245 × 2958 px
  ```

  Usare `mutool draw -s f` o ispezione equivalente per confermare uno spazio colore CMYK e assenza di errori di parsing.

- [ ] **Step 5: Ispezionare visivamente l'anteprima a risoluzione originale**

  Verificare prima, dorso e quarta: gerarchia, refusi, margini, contrasto, area barcode, continuità del reticolo, assenza di clipping, overlap e segni tecnici. Fare un secondo passaggio dedicato a allineamento, ritmo, microspaziatura, miniatura e scala di grigi; se un elemento non rafforza la composizione, semplificarlo e rigenerare.

- [ ] **Step 6: Registrare l'audit nel preflight**

  Aggiungere a `PREFLIGHT.md` conteggio pagina, MediaBox, dimensioni PNG, data del controllo, spazio colore, font, esito dell'ispezione a colori/scala di grigi/miniatura e nota che KDP Previewer e prova fisica restano esterni.

### Task 4: Metadati e documentazione di consegna KDP

**Files:**
- Modify: `delivery/VOL-08/candidate/KDP-METADATA.md`
- Modify: `delivery/VOL-08/candidate/KDP-UPLOAD-CHECKLIST.md`
- Modify: `delivery/VOL-08/candidate/LIMITS.md`
- Modify: `delivery/VOL-08/candidate/README.md`
- Modify: `delivery/VOL-08/candidate/CHANGELOG.md`
- Modify: `delivery/VOL-08/candidate/REPORT-PUBBLICABILITA.md`
- Modify: `delivery/VOL-08/candidate/VERSION.json`
- Modify: `delivery/VOL-08/candidate/MAINTENANCE.md`
- Modify: `delivery/VOL-08/candidate/MANIFEST.sha256`

**Interfaces:**
- Consumes: valori approvati, artefatti verificati delle Task 1-3 e pagine ufficiali KDP già consultate per ISBN, copertina, costi, royalty e contenuto generato con IA.
- Produces: scheda operativa pronta per l'inserimento in KDP e documentazione coerente con lo stato reale del pacchetto.

- [ ] **Step 1: Allineare la scheda metadati**

  Registrare senza varianti titolo, sottotitolo, autore, collana, volume, lingua, formato, carta, finitura, assenza bleed e scelta ISBN gratuito. Impostare `Independently published` come imprint atteso e spiegare che il numero ISBN sarà assegnato dalla piattaforma.

  Registrare proposta prezzo `€24,90`, costo stampa indicativo `€4,45` per 231 pagine e royalty indicativa `€10,49` con formula `60% × €24,90 − €4,45`; indicare che tasse, marketplace e calcolo visualizzato da KDP prevalgono.

  Registrare la dichiarazione IA da rendere in piattaforma: testo generato con IA = sì; immagine di copertina generata con IA = no, poiché la copertina è grafica vettoriale originale prodotta programmaticamente.

- [ ] **Step 2: Rendere la checklist operativa e veritiera**

  Marcare completati soltanto file, copy e controlli locali effettivamente conclusi. Lasciare aperti esclusivamente: assegnazione ISBN in KDP, upload, Print Previewer, controllo prezzo/royalty mostrati dalla piattaforma, ordinazione e approvazione della copia di prova, pubblicazione.

- [ ] **Step 3: Aggiornare limiti, README, changelog e manutenzione**

  Eliminare ogni affermazione secondo cui copertina o metadati mancano. Elencare i due PDF, la preview e i documenti operativi; descrivere in modo esplicito i controlli esterni residui e il comando di rigenerazione della copertina.

- [ ] **Step 4: Aggiornare giudizio e versione**

  Mantenere il giudizio editoriale coerente con il report finale già eseguito e distinguere la pubblicabilità editoriale dall'approvazione materiale KDP. Impostare una release candidate datata `2026-08-14`; registrare la conferma utente della specifica di copertina, senza dichiarare approvato l'artefatto renderizzato prima della sua consegna.

- [ ] **Step 5: Rigenerare il manifest per ultimo**

  Calcolare SHA-256 di tutti i file consegnabili nella directory, escluso `MANIFEST.sha256`, ordinarli per nome e scrivere righe nel formato:

  ```text
  <hash minuscolo>  <nome file>
  ```

  Ricalcolare il manifest ogni volta che un file della candidate directory cambia.

### Task 5: Verifica finale indipendente e tracciamento

**Files:**
- Modify: `delivery/VOL-08/candidate/PREFLIGHT.md`
- Modify: `delivery/VOL-08/candidate/MANIFEST.sha256`
- Modify: `wiki/log.md`
- Create: `wiki/memory/agent/l0/conv-<timestamp>-<hash>.md` tramite `LocalAgentMemory`
- Modify: `wiki/memory/agent/l0/conversations.jsonl` tramite `LocalAgentMemory`
- Modify: `wiki/memory/agent/l1/atoms.jsonl` tramite `LocalAgentMemory`
- Modify: `wiki/memory/agent/l2/scenarios.md` tramite `LocalAgentMemory`
- Modify: `wiki/memory/agent/l3/persona.md` tramite `LocalAgentMemory`

**Interfaces:**
- Consumes: pacchetto candidate completo e CLI pipeline.
- Produces: evidenza riproducibile dei controlli, memoria operativa VOL-08 e stato di consegna finale.

- [ ] **Step 1: Eseguire la suite completa**

  Run: `npm test`

  Expected: tutte le suite PASS.

  Run: `npm run typecheck`

  Expected: exit code 0.

  Run: `npm run build`

  Expected: exit code 0.

- [ ] **Step 2: Eseguire audit editoriale e pipeline in JSON**

  Run: `node scripts/audit-vol08-format2-nuclei.mjs`

  Expected: zero blocker, 13 capitoli, 82 nuclei e tutti i nuclei pubblicabili.

  Run: `npm run pipeline -- doctor --json`

  Expected: JSON valido senza impedimenti pertinenti a VOL-08.

  Run: `npm run pipeline -- status VOL-08 --json`

  Expected: stato concluso, nessuno step bloccato e nessun prossimo step. Non modificare il run-state.

- [ ] **Step 3: Eseguire il controllo “zero errori” indipendente**

  Cercare refusi, doppie parole, caratteri corrotti, riferimenti interni errati, mismatch di titolo/autore/sottotitolo, numeri pagina incoerenti, marcatori di conflitto e parole-sentinella nei file VOL-08 e di consegna. Confrontare hash reali e manifest; eseguire `git diff --check` sui soli percorsi modificati.

- [ ] **Step 4: Aggiornare preflight, manifest e log**

  Registrare comandi, orari, esiti e qualsiasi limite rimasto. Appendenre a `wiki/log.md` una sola voce sintetica per il completamento del pacchetto, senza correggere eventi precedenti.

- [ ] **Step 5: Catturare la memoria locale**

  Chiamare `LocalAgentMemory.fromConfig().captureConversation` con:

  ```ts
  {
    scope: "VOL-08",
    route: "codex/final-publication-package",
    messages: [{ role: "user", content: "Confermata la specifica finale VOL-08 e richiesta la preparazione del pacchetto pubblicabile." }],
    reply: "Pacchetto finale generato e verificato: interno, copertina Circuito Civico, metadati KDP, manifest e controlli tecnici; restano soltanto Previewer, ISBN e prova fisica in KDP.",
    metadata: { volume: "VOL-08", cover: true, pageCount: 231, publicationPackage: true }
  }
  ```

- [ ] **Step 6: Verificare lo staging e creare il commit finale**

  Prima dello staging, eseguire `git diff --cached --name-only` e rimuovere dall'indice qualunque percorso estraneo senza alterare il worktree. Aggiungere soltanto gli artefatti e la documentazione VOL-08 effettivamente prodotti da questo piano, poi rieseguire `git diff --cached --name-only`.

  Commit suggerito:

  ```powershell
  git commit -m "release(vol-08): complete KDP publication package"
  ```

  Non eseguire push senza richiesta esplicita dell'utente.

- [ ] **Step 7: Preparare la consegna**

  Restituire percorsi cliccabili per interno, copertina PDF, preview PNG, metadati, checklist e preflight. Dichiarare con precisione cosa è completo e quali operazioni devono essere eseguite nella piattaforma KDP; non usare la parola “perfetto” come sinonimo di controllo umano o fisico non ancora svolto.
