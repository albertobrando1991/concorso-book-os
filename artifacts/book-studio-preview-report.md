# Book Studio preview report

## Date
2026-05-10

## Scope
Added a visual Book Studio to the dashboard so the user can review the manual as a formatted book, navigate chapters, request Codex edits, and attach images to selected chapters.

## Implemented
- Dashboard section: `Book Studio / Preview visuale e revisione del manuale`.
- Chapter and full-book preview modes.
- Outline navigation using `outline_section` ordering.
- Formatted preview page with headings, paragraphs, lists, code blocks and Obsidian image embeds.
- Right-side revision panel for selected chapter metadata, Codex personalization request and image upload.
- API route `GET /api/book-studio` for live preview data from the vault.
- API route `POST /api/book-studio/assets` for image upload into `wiki/raw/assets/books/<book_id>/`.
- API route `GET /api/book-studio/assets/file` for serving vault images in the browser preview.

## Verification
- `npm run typecheck`: passed.
- `npm test`: passed, 4 test files and 7 tests.
- `npm run build`: passed.
- `PORT=3011 npm run screenshot`: passed.
- Local dashboard verified on `http://127.0.0.1:3000` and `http://127.0.0.1:3001`.
- `GET /api/book-studio`: returned HTTP 200.

## Screenshot
- `artifacts/dashboard-screenshot.png`

## Notes
- The Book Studio uses the vault as source of truth.
- Codex edits still go through Manual Writer Agent and patch chapter headings.
- Images are stored as vault assets and appended to the selected chapter under `## Immagini e layout`.
