---
id: template-modulo-specialistico
type: template
title: "Template modulo specialistico Metodo BANDO"
status: template
domain: "concorsi pubblici italiani"
topics: ["moduli specialistici","template editoriale"]
entities: ["Metodo BANDO"]
source_refs: []
book_refs: ["il-metodo-bando"]
confidence: 0.7
updated_at: 2026-06-28T12:38:57+02:00
created_at: 2026-06-27T19:56:28+02:00
review_required: false
canonical: false
tags: ["template","specialist-module"]
---

# Template modulo specialistico Metodo BANDO

## Frontmatter minimo
- type: specialist_module
- book_id: <slug-modulo>
- module_code: M-XXX
- module_family: <famiglia>
- companion_to: il-metodo-bando
- draft_stage: structure-ready

## Struttura minima
1. Prime pagine obbligatorie come libro autonomo: servizi digitali inclusi, frontespizio, copyright e note editoriali, sommario, premessa, indice.
2. Ruolo del modulo.
3. Perimetro.
4. Confine editoriale.
5. Capitoli di lavoro.
6. Fonti da consolidare.
7. Prossimo passo.

## Regola numerazione capitoli
- La numerazione vive solo in `outline_section`.
- Il campo `title` non deve contenere il numero del capitolo.
- L'H1 del file non deve contenere il numero del capitolo.
- Esempio corretto: `outline_section: 1`, `title: "Lavorare nei Ministeri"`, `# Lavorare nei Ministeri`.
- Esempio da evitare: `title: "1. Lavorare nei Ministeri"`, perche' in dashboard diventa una numerazione duplicata.

## Prime pagine standard
Creare sempre `front-matter/` con:
- `01-servizi-digitali.md` (`outline_section: FM1`)
- `02-frontespizio.md` (`outline_section: FM2`)
- `03-copyright-colophon.md` (`outline_section: FM3`)
- `04-sommario.md` (`outline_section: FM4`)
- `05-premessa.md` (`outline_section: FM5`)
- `06-indice.md` (`outline_section: FM6`, `front_matter_layout: analytical-index`, `index_detail: chapters-only`)

Il piano editoriale interno deve stare fuori da `chapters/`, ad esempio in `planning/00-piano-editoriale.md`, per non essere trattato come capitolo del libro.

L'indice dei moduli deve usare la stessa resa grafica del libro base: parti, righe capitolo, puntini guida e numero pagina. Nei moduli non deve generare sottorighe `1.1`, `2.1`, ecc.; quelle restano riservate al libro base quando serve un indice analitico dettagliato.
