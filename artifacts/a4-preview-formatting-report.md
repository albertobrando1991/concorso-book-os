# A4 Preview Formatting Report

## Task List
- Fix Book Studio preview so the manual is shown as separate A4 pages.
- Justify body text in the chapter preview.
- Prevent headings from being left alone at the bottom of a page.
- Keep footer and page number visible without content overlap.
- Persist the formatting rule in project knowledge and writer conventions.

## Implementation
- `app/components/book-studio-panel.tsx`: added page pagination logic for markdown blocks, running headers, footers and page numbers.
- `app/globals.css`: added A4 page sizing, justified text, Italian hyphenation, widows/orphans rules, anti-break styling and A4 print CSS.
- `wiki/books/il-metodo-bando/design-system-editoriale.md`: made A4 the canonical dashboard/revision/export format.
- `wiki/AGENTS.md` and `.agents/skills/concorso-book-professional-writer/SKILL.md`: added page-aware writer rules.

## Verification
- `npm run typecheck`: passed.
- `npm test`: passed, 4 files and 7 tests.
- `npm run build`: passed.
- `$env:PORT='3011'; npm run screenshot`: passed and updated `artifacts/dashboard-screenshot.png`.

## Final State
Book Studio now presents the selected chapter as a real A4 review preview: one page per sheet, justified text, running headers on continuation pages, footer/page number, readable tables and no orphan heading at the bottom of the checked chapter preview.

## Follow-Up Optimization
- Added browser-side measured pagination: the preview measures the real rendered height of each block inside an invisible A4 sheet before creating page breaks.
- Tightened table spacing for workbook/manual pages.
- Added heading pull-forward logic so a heading is not stranded when the next block moves to the following page.
- Added keep-with-next logic for short exercise instructions before tables, images or code blocks.
