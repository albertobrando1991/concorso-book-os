# Conversation Summary - Capitolo 25 immagini

- created_at: 2026-06-09T19:22:06.0253752+02:00
- scope: il-metodo-bando
- route: codex/chapter25-editorial-images
- user_request: "PROSSIMO CAPITOLO"

## Contesto

Il prossimo capitolo effettivo dopo il Capitolo 24 `Checklist operative` e' il Capitolo 25 `Aggiornare il metodo dopo il libro`, file `wiki/books/il-metodo-bando/chapters/aggiornare-il-metodo-dopo-il-libro.md`.

## Azioni

- Identificate 7 figure editoriali coerenti con il capitolo: mappa BANDO dell'aggiornamento, gerarchia fonti, fonti da controllare, protocollo dei 20 minuti, scheda aggiornamento, decisione sul cambio piano e caso Davide.
- Creato `scripts/generate-chapter25-assets.cjs`.
- Generati asset SVG master e PNG in `wiki/books/il-metodo-bando/assets/chapter-25/`.
- Inserite le immagini nel markdown con didascalie `Figura 25.1` - `Figura 25.7`.
- Creato `scripts/verify-chapter25-images.cjs`.

## Verifiche

- Preview Book Studio su porta 3025: 15 pagine, 7 immagini `chapter-25`, tutte caricate, 1600x900, aspect ratio conforme, nessuna sovrapposizione al footer.
- Audit SVG: 7 file, nessun testo fuori margine.
- `npm test -- tests\book-preview.test.ts`: 3 test passati.
- `git diff --check`: solo warning CRLF preesistenti su file non coinvolti.

## Esito

Capitolo 25 illustrato e verificato con lo stesso standard dei capitoli precedenti.
