# Template capitolo modulo specialistico

Usare questo schema dentro `chapters/` quando si aggiunge un capitolo a un modulo:

## Frontmatter capitolo
- `type: book_chapter`
- `book_id: <slug-modulo>`
- `outline_section: <numero-capitolo>`
- `title: <titolo senza numero>`
- `module_code: <codice-modulo>`
- `module_family: <famiglia>`

## Regola numerazione
Non inserire il numero dentro `title` o dentro l'H1. La dashboard aggiunge il numero usando `outline_section`.

Esempio corretto:

```yaml
title: "Lavorare nei Ministeri"
outline_section: 1
```

```markdown
# Lavorare nei Ministeri
```

## Schema contenuto
1. Specifica struttura modulo.
2. Obiettivo didattico.
3. Lettore.
4. Fonti da consolidare.
5. Testo editoriale.
6. Riferimenti e note di review.
