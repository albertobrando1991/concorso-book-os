# Conversation Summary - Capitolo 27 immagini

- created_at: 2026-06-10T16:09:31.8187103+02:00
- scope: il-metodo-bando
- route: codex/chapter27-editorial-images
- user_request: "procedi prossimo capitolo"

## Contesto

Il prossimo capitolo effettivo dopo il Capitolo 26 `Trasformare ogni concorso in capitale di studio` e' il Capitolo 27 `Gestire concorsi paralleli senza disperdersi`, file `wiki/books/il-metodo-bando/chapters/gestire-concorsi-paralleli-senza-dispersersi.md`.

## Azioni

- Identificate 7 figure editoriali coerenti con il capitolo: mappa BANDO dei concorsi paralleli, portafoglio concorsi, matrice di compatibilita, regola 70/20/10, calendario unico, diario/semaforo decisionale e caso Marta.
- Creato `scripts/generate-chapter27-assets.cjs`.
- Generati asset SVG master e PNG in `wiki/books/il-metodo-bando/assets/chapter-27/`.
- Inserite le immagini nel markdown con didascalie `Figura 27.1` - `Figura 27.7`.
- Creato `scripts/verify-chapter27-images.cjs`.

## Verifiche

- Preview Book Studio su porta 3027: 13 pagine, 7 immagini `chapter-27`, tutte caricate, 1600x900, aspect ratio conforme, nessuna sovrapposizione al footer.
- Audit SVG: 7 file, nessun testo fuori margine dopo correzione di contrasto e geometria sulla mappa/matrice.
- `npm test -- tests\book-preview.test.ts`: 3 test passati.
- `git diff --check`: solo warning CRLF preesistenti su file non coinvolti.

## Esito

Capitolo 27 illustrato e verificato con lo stesso standard dei capitoli precedenti.
