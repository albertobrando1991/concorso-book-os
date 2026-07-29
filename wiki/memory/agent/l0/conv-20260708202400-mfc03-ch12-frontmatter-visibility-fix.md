# M-FC03 chapter 12 BOM/frontmatter fix

- timestamp: 2026-07-08T20:24:00+02:00
- route: codex/mfc03-ch12-frontmatter-visibility-fix
- request: rimuovere codici visibili prima del primo paragrafo del capitolo 12 e rispettare grammatica e punteggiatura italiana.
- result: Rimosso carattere BOM iniziale che impediva il riconoscimento del frontmatter. Il parser ora riconosce `---` come primo carattere e la parte pubblica inizia da `# Quesiti situazionali EPNE`.
- verification: controllo parser frontmatter OK; `npm test -- tests/frontmatter.test.ts tests/markdown.test.ts tests/book-preview.test.ts` passato fuori sandbox: 3 file, 12 test.
