# Manual Writer correction report

## Date
2026-05-10

## Problem
The writer generated a technical fallback block instead of actual chapter prose. It included meta text such as:

- `Aggiornamento generato da Manual Writer Agent`
- `Istruzione ricevuta`
- summaries of source notes as the chapter body

## Correction
- Manual Writer Agent now rejects meta-like outputs and falls back to a chapter-specific editorial draft.
- Prompts now explicitly require real reader-facing chapter text.
- Dashboard default instructions now say to use the wiki brain first.
- The professional writer skill and `AGENTS.md` now define the hierarchy:

```text
struttura madre -> selected chapter note -> source notes -> topic pages -> entity pages -> quizzes/reviews -> web research only when needed
```

## Chapter Fixes
- Rewrote `wiki/books/il-metodo-bando/chapters/introduzione.md`.
- Rewrote `wiki/books/il-metodo-bando/chapters/il-nuovo-candidato-pubblico.md`.

Both now contain real editorial text for the book, with:
- opening prose;
- BANDO map;
- explanation;
- operational boxes;
- cases;
- exercises;
- review notes;
- consolidated references.

## Preview Fix
Book Studio now renders markdown tables as tables, not as raw pipe text.

## Verification
- `npm run typecheck`: passed.
- `npm test`: passed.
- `npm run build`: passed.
- `PORT=3011 npm run screenshot`: passed.
- Meta-text grep on the two corrected chapters: passed.
