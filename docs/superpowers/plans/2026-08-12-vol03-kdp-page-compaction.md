# VOL-03 KDP Page Compaction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ridurre la composizione del VOL-03 da 832 a non più di 828 pagine senza eliminare contenuti o alterare lo standard KDP.

**Architecture:** Il renderer assegna una classe di layout solo quando il `bookId` è `volumi/vol-03`. La classe usa metriche verticali leggermente più compatte sia nella misurazione nascosta sia nelle pagine renderizzate; gli altri libri conservano le regole globali.

**Tech Stack:** React/TypeScript, CSS, Vitest, Playwright, Next.js, PDF Chromium.

## Global Constraints

- Formato pagina invariato: 6,69 × 9,61 pollici.
- Margini invariati: 23/13 mm e 18 mm sopra/sotto.
- Corpo Garamond 11 pt e titoli Arial 20/14/12 pt invariati.
- Interlinea consentita: 1,15–1,20; target VOL-03: 1,16.
- Nessuna eliminazione, abbreviazione o riordinamento del contenuto.
- Nessuna variazione di impaginazione per libri diversi da `volumi/vol-03`.

---

### Task 1: Selettore di layout specifico per VOL-03

**Files:**
- Create: `src/server/book/book-layout-profile.ts`
- Test: `tests/book-layout-profile.test.ts`
- Modify: `app/components/book-studio-panel.tsx`

**Interfaces:**
- Produces: `bookLayoutClass(bookId: string): string`, che restituisce `bookLayoutVol03Compact` solo per `volumi/vol-03`, altrimenti stringa vuota.
- Consumes: `data.bookId` già disponibile nel pannello.

- [ ] **Step 1: Scrivere il test fallente**

```ts
import { describe, expect, it } from "vitest"
import { bookLayoutClass } from "../src/server/book/book-layout-profile"

describe("bookLayoutClass", () => {
  it("compatta esclusivamente VOL-03", () => {
    expect(bookLayoutClass("volumi/vol-03")).toBe("bookLayoutVol03Compact")
    expect(bookLayoutClass("volumi/vol-07")).toBe("")
    expect(bookLayoutClass("il-metodo-bando")).toBe("")
  })
})
```

- [ ] **Step 2: Eseguire il test e osservare il fallimento**

Run: `npx vitest run tests/book-layout-profile.test.ts`

Expected: FAIL perché il modulo non esiste.

- [ ] **Step 3: Implementare la funzione minima**

```ts
export function bookLayoutClass(bookId: string) {
  return bookId === "volumi/vol-03" ? "bookLayoutVol03Compact" : ""
}
```

Importare la funzione nel pannello e applicare la classe sia a `.bookPages` sia a `.paginationMeasure` con composizione di stringhe, preservando le classi esistenti.

- [ ] **Step 4: Eseguire il test**

Run: `npx vitest run tests/book-layout-profile.test.ts`

Expected: PASS, 1 test superato.

- [ ] **Step 5: Commit atomico**

```powershell
git add -- src/server/book/book-layout-profile.ts tests/book-layout-profile.test.ts app/components/book-studio-panel.tsx
git commit -m "feat(book-studio): scope compact layout to VOL-03"
```

### Task 2: Metriche verticali compatte

**Files:**
- Modify: `app/globals.css`
- Test: `tests/book-layout-profile.test.ts`

**Interfaces:**
- Consumes: classe `bookLayoutVol03Compact` della Task 1.
- Produces: override CSS limitati ai discendenti `.previewBlocks` della classe.

- [ ] **Step 1: Estendere il test con il contratto CSS**

Leggere `app/globals.css` nel test e verificare la presenza del selettore `.bookLayoutVol03Compact .previewBlocks`, di `font-size: 11pt`, `line-height: 1.16` e l'assenza di override alle variabili dei margini pagina nel blocco compatto.

- [ ] **Step 2: Eseguire il test e osservare il fallimento**

Run: `npx vitest run tests/book-layout-profile.test.ts`

Expected: FAIL perché il selettore compatto non esiste.

- [ ] **Step 3: Aggiungere gli override minimi**

```css
.bookLayoutVol03Compact .previewBlocks {
  font-size: 11pt;
  line-height: 1.16;
}

.bookLayoutVol03Compact .previewBlocks p { margin-bottom: 3.5pt; }
.bookLayoutVol03Compact .previewBlocks h3 { margin: 9pt 0 3.5pt; }
.bookLayoutVol03Compact .previewBlocks h4 { margin: 6.5pt 0 2.5pt; }
.bookLayoutVol03Compact .previewBlocks h5 { margin: 5.5pt 0 2.5pt; }
.bookLayoutVol03Compact .previewBlocks ul,
.bookLayoutVol03Compact .previewBlocks ol { margin-bottom: 4.5pt; }
```

- [ ] **Step 4: Eseguire test e typecheck**

Run: `npx vitest run tests/book-layout-profile.test.ts && npm run typecheck`

Expected: tutti i test PASS e typecheck exit 0.

- [ ] **Step 5: Commit atomico**

```powershell
git add -- app/globals.css tests/book-layout-profile.test.ts
git commit -m "style(vol-03): compact vertical book rhythm"
```

### Task 3: Conteggio, audit DOM ed export PDF

**Files:**
- Modify: `wiki/reviews/pipeline/VOL-03/22-vol-03-preflight.md`
- Replace generated artifact: `delivery/VOL-03/candidate/vol-03-interior-kdp.pdf`

**Interfaces:**
- Consumes: Book Studio su `http://127.0.0.1:3010`, book ID `volumi/vol-03`.
- Produces: PDF aggiornato e checklist con evidenze fresche.

- [ ] **Step 1: Avviare Book Studio e misurare il conteggio stabile**

Avviare `npm run dev -- -p 3010` in background. Aprire `/?bookId=volumi%2Fvol-03&advanced=1#studio`, selezionare `Libro`, attendere font e immagini, quindi contare `.bookPages .bookPage`.

Expected: conteggio ≤ 828. Se è superiore, modificare soltanto gli spazi verticali del selettore VOL-03 entro i limiti della specifica e ripetere Task 2 dal test fallente aggiornato.

- [ ] **Step 2: Eseguire l'audit DOM completo**

Run con variabili PowerShell:

```powershell
$env:BOOK_STUDIO_BOOK_ID='volumi/vol-03'
$env:BOOK_STUDIO_EXPECTED_PAGE_COUNT='<conteggio misurato>'
$env:BOOK_STUDIO_ARTIFACT_PREFIX='vol-03-step-22'
node scripts/verify-book-studio-page-audit.mjs
```

Expected: 0 problemi bloccanti, 0 immagini mancanti, 0 overflow e registro completo.

- [ ] **Step 3: Esportare il PDF**

```powershell
$env:BOOK_STUDIO_BOOK_ID='volumi/vol-03'
$env:BOOK_STUDIO_EXPECTED_PAGES='<conteggio misurato>'
$env:BOOK_STUDIO_PDF_PATH='delivery/VOL-03/candidate/vol-03-interior-kdp.pdf'
npm run export:volume-pdf
```

Expected: JSON con `ok: true`, conteggio atteso e file non vuoto.

- [ ] **Step 4: Verificare PDF e progetto**

Eseguire test pertinenti, `npm run typecheck`, `npm run build` e `git diff --check`. Ispezionare MediaBox/CropBox, font incorporati, bleed, byte e SHA-256 con gli strumenti già usati nel report step 22.

- [ ] **Step 5: Aggiornare il report e chiudere il gate manuale**

Registrare conteggio, SHA-256, byte e ogni esito nel report. Poi eseguire:

```powershell
npm run pipeline -- complete VOL-03 --step 22 --accept --note "Preflight manuale completato: copertura verde, build e test superati, PDF entro 828 pagine, geometria KDP e font verificati."
```

Expected: JSON di completamento con step 22 `done` e step 23 disponibile.

- [ ] **Step 6: Registrare memoria e commit finale**

Usare `LocalAgentMemory.captureConversation` con scope `VOL-03`, quindi aggiungere esclusivamente file e artefatti del task e creare un commit descrittivo.
