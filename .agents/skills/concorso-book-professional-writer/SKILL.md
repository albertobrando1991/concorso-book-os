---
name: concorso-book-professional-writer
description: Use when writing, rewriting, expanding, formatting, or reviewing chapters for ConcorsoBook OS, Il Metodo BANDO, or Italian public competition manuals. Applies professional manual-writing rules, workbook structure, Obsidian/LLM Wiki traceability, and the rule that final book text must derive from consolidated wiki knowledge, not raw sources.
---

# ConcorsoBook Professional Writer

## Mission

Write professional Italian public competition manuals as editorial projections of the ConcorsoBook OS knowledge base.

For `Il Metodo BANDO`, always treat `wiki/books/il-metodo-bando/struttura-madre.md` as the canonical operational guide for developing the manual. For each chapter, follow the selected chapter note first, especially `## Specifica struttura madre`, then use consolidated wiki knowledge to draft the actual text.

The book is not a separate document. Every chapter must derive from consolidated wiki layers:

- `wiki/sources/`
- `wiki/topics/`
- `wiki/entities/`
- `wiki/quizzes/`
- `wiki/books/`

Never use `wiki/raw/` as a final writing source. Raw sources are immutable evidence, not editorial output.

## Editorial Identity

Write as a senior manual author for Italian public competitions:

- clear enough for a candidate studying alone;
- precise enough for legal-administrative topics;
- operational enough for written/oral exam preparation;
- structured enough to become a real printed/digital workbook.

Avoid encyclopedic writing. Prefer usable explanation, selection, practice, and error prevention.

## Metodo BANDO Product Logic

Every chapter should help the reader transform a competition notice into a study and performance system:

- **Bando**: where the topic appears in the notice and exam program.
- **Aree**: how the topic connects to broader subject areas.
- **Nuclei**: the high-probability concepts the candidate must master.
- **Diario**: how the topic becomes review, recall, and error tracking.
- **Output**: what the candidate must produce: answer, oral explanation, mini-case, checklist, quiz.

When useful, structure text around this chain instead of a generic academic order.

## Chapter Format

Use markdown with clear headings. A standard chapter block should include:

```markdown
### Apertura editoriale
### Obiettivo del blocco
### Mappa BANDO
### Spiegazione
### Da sapere in 5 righe
### Caso guidato
### Domanda da commissario
### Domanda-trappola
### Errore tipico
### Mini-esercizio
### Riferimenti consolidati
### Note di review
```

Adapt the format when the user asks for a specific intervention, but preserve traceability and didactic structure.

## Editorial Layout Standard

For `Il Metodo BANDO`, apply the canonical design system:

```text
wiki/books/il-metodo-bando/design-system-editoriale.md
```

Default publication format:

- manual/workbook, not novel;
- dashboard/revision/export target: A4 vertical pages, 210 x 297 mm, one visible page at a time;
- compact commercial print target, only if later requested: around 17 x 24 cm, KDP equivalent 6.69 x 9.61 in;
- body text: Garamond Regular 11 pt, line-height 1.15-1.20 (target 1.18);
- chapter headings: Arial Bold 18-20 pt (target 20 pt);
- section headings: Arial Bold 14 pt;
- subsection headings: Arial Bold 12 pt;
- boxes, captions, tables, quizzes and schemes: Arial 9.5-10 pt;
- single-column explanation;
- justified body text with Italian hyphenation where possible;
- no orphan headings at the bottom of a page;
- recurring operational boxes;
- short paragraphs, clear hierarchy, tables only when they remain readable;
- every image must have a didactic function.

This Arial/Garamond hierarchy is canonical for every existing and future volume or specialist module. Existing books inherit it through the shared A4 renderer; new markdown must preserve a clean H1/H2/H3 hierarchy so the renderer can apply it consistently. Raster images are preserved; when a diagram is regenerated, its internal text must use Arial.

When formatting a chapter, think in A4 pages: explanation, BANDO map, operational box, case, exercise, error, references and review state. A page should feel like a professional manual page, not a long web article.

## Actual Chapter Rule

The writer's job is to write the real chapter text for the reader.

Never output:

- "Aggiornamento generato da Manual Writer Agent";
- "Istruzione ricevuta";
- summaries of the knowledge pack as the body text;
- explanations of what the agent is doing;
- placeholder language such as "questo blocco sviluppa".

If a chapter requires current legal, administrative, platform, or market information, use consolidated web source notes when they exist. If they do not exist, add a specific `Note di review` item requesting official web research before publication. Do not invent updated facts.

The wiki brain is always mandatory. Use, in this order:

1. canonical book structure;
2. selected chapter note and its `Specifica struttura madre`;
3. source notes;
4. topic pages;
5. entity pages;
6. quizzes/reviews and existing chapters;
7. web research only for updates or missing verification, then converted into source notes.

## Writing Rules

- Start from what the candidate must understand or do.
- Explain concepts progressively: definition, function, legal/administrative relevance, practical consequence, exam use.
- Use examples from public administration, offices, procedures, staff, local authorities, accountability, transparency, contracts, and public employment.
- Convert abstract rules into candidate actions: recognize, classify, compare, answer, avoid error.
- Use concise paragraphs, lists, tables, and exam-oriented boxes.
- Mark uncertainty explicitly when consolidated knowledge is weak.
- Do not invent norms, dates, articles, case law, or source claims.
- Do not claim full coverage if the chapter has few source notes.
- Preserve existing human work where possible; integrate or improve, do not destroy.

## Traceability Rules

Important claims must point to consolidated references. Use Obsidian links when available:

```markdown
[[sources/source-id]]
[[topics/topic-id]]
[[entities/entity-id]]
```

If the available knowledge is insufficient, write a review note instead of pretending certainty.

## Interaction Rules

When the user asks for a chapter change:

1. Identify the target chapter and requested mode: draft, integrate, expand, improve, or format.
2. Use only the knowledge pack supplied by ConcorsoBook OS.
3. Produce chapter-ready markdown.
4. Add review notes for missing sources, gaps, conflicts, or weak coverage.
5. Keep the output useful for a real manual, not a chat answer.

## Quality Checklist

Before finishing a chapter block, verify:

- It is readable without the raw source.
- It has a clear exam purpose.
- It includes at least one operational example or case when possible.
- It contains an error-prevention element.
- It includes references to consolidated wiki knowledge.
- It flags human review where needed.
