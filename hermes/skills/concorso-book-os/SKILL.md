---
name: concorso-book-os
description: Use when Telegram or chat asks Hermes to import Italian legal/public-competition sources into ConcorsoBook OS, download PDFs, run OCR through the site's pipeline, connect a source to a chapter, or trigger chapter integration through the local dashboard API.
version: 1.0.0
metadata:
  hermes:
    tags: [telegram, concorsobook, legal-sources, obsidian, ocr]
    category: productivity
    requires_toolsets: [terminal]
---

# ConcorsoBook OS

## When To Use

Use this skill when the user asks from Telegram, CLI, or any Hermes surface to:

- import, download, or add a law, decree, manual, article, website, or PDF to ConcorsoBook OS;
- connect a source to a book chapter;
- add knowledge before generating or revising a chapter;
- run the ConcorsoBook import/OCR pipeline;
- use Obsidian/wiki knowledge for `Il Metodo BANDO`.

Typical Telegram wording:

```text
Scarica questa legge in PDF e aggiungila alla conoscenza del capitolo diritto-amministrativo-per-candidati: https://...
```

When the user does not provide a URL, search from the document request:

```text
Cerca il testo ufficiale della legge 241/1990, scaricalo, convertilo in markdown e aggiungilo al capitolo procedimento-amministrativo.
```

## Silence Policy

Hermes is allowed to send no message.

Do not reply when:

- a group/channel message is clearly not addressed to Hermes;
- the message is only an acknowledgement, thanks, duplicate, or noise;
- there is no actionable ConcorsoBook import, OCR, source-linking, or writer request;
- the request is outside this skill and no useful routing/action is available.

In private Telegram chat, treat every message from an allowed user as addressed to Hermes, even if it does not mention the bot name.

Never stay silent when the message contains:

- verbs like `scarica`, `importa`, `aggiungi`, `cerca`, `integra`;
- a list of laws, decrees, PDFs, official sources, or public-competition documents;
- legal references such as `D.Lgs.`, `DPR`, `Legge`, `n.`, dates, or topic labels.

If a relevant request is missing a required detail, ask one short clarification instead of staying silent.

In API contexts that require a text body for silence, output exactly:

```text
__HERMES_NO_REPLY__
```

## Required Local Setup

The ConcorsoBook dashboard must be running locally:

```bash
npm run dev
```

Hermes needs these environment variables in `~/.hermes/.env`:

```bash
CONCORSOBOOK_BASE_URL=http://127.0.0.1:3000
CONCORSOBOOK_WEBHOOK_SECRET=<same value as HERMES_WEBHOOK_SECRET in the site .env.local>
```

If Hermes runs in WSL and the dashboard runs on Windows, `127.0.0.1` may not resolve to the Windows process. In that case use the Windows host IP or a tunnel URL as `CONCORSOBOOK_BASE_URL`.

## Procedure

1. Extract the source URL from the user's message. If there is no URL, extract a precise `query` from the requested document title, law/decree number, year, authority, and topic.
2. Identify whether the user supplied one source or multiple sources.
   - If the user supplied a list, process each source separately and sequentially.
   - Build one `query` and one clear `title` for each listed item.
   - Use `--writer false` unless the user explicitly asks to integrate or rewrite a chapter.
3. Identify the target chapter.
   - If the user gives a full path, use it.
   - If the user gives a slug, normalize it to `books/il-metodo-bando/chapters/<slug>.md`.
   - If the chapter is missing and the user only asked to download/import sources, omit `--chapter` and import into the wiki without linking a chapter.
   - Ask for clarification only when the user explicitly asks to link/integrate/update a chapter but does not say which one.
4. Infer `sourceType`:
   - `law` for legge, normativa, regolamento unless a more specific type is clear;
   - `decree` for decreto, d.lgs., DPR, DM;
   - `manual`, `article`, `website`, or `transcript` when explicit.
5. Decide whether to run the writer:
   - default `runWriter=false`;
   - set `runWriter=true` only if the user explicitly asks to integrare, generare, scrivere, or aggiornare the chapter text.
6. Call the helper script.

   Preferred command on this Windows/WSL setup when the user did not provide a URL:

```bash
python3 /mnt/c/Users/alber/.hermes/skills/concorso-book-os/scripts/import-source.py \
  --query "legge 7 agosto 1990 n. 241 testo vigente PDF" \
  --chapter "books/il-metodo-bando/chapters/procedimento-amministrativo.md" \
  --title "Legge 241/1990 - procedimento amministrativo" \
  --type law \
  --writer false
```

   Preferred command when the user provided a URL:

```bash
python3 /mnt/c/Users/alber/.hermes/skills/concorso-book-os/scripts/import-source.py \
  --url "https://example.gov/legge.pdf" \
  --chapter "books/il-metodo-bando/chapters/diritto-amministrativo-per-candidati.md" \
  --title "Titolo fonte" \
  --type law \
  --writer false
```

   Native Node fallback, only when the terminal is not WSL or Node is installed in the terminal environment:

```bash
node ~/.hermes/skills/concorso-book-os/scripts/import-source.mjs \
  --url "https://example.gov/legge.pdf" \
  --chapter "books/il-metodo-bando/chapters/diritto-amministrativo-per-candidati.md" \
  --title "Titolo fonte" \
  --type law \
  --writer false
```

   Bulk example when the user sends a plain list without URLs or chapters:

```bash
python3 /mnt/c/Users/alber/.hermes/skills/concorso-book-os/scripts/import-source.py \
  --query "D.Lgs. 30 marzo 2001 n. 165 pubblico impiego testo vigente PDF" \
  --title "D.Lgs. 30 marzo 2001, n. 165 - pubblico impiego" \
  --type decree \
  --writer false
```

   Repeat one helper call per listed source. After the batch, report a compact summary with imported titles, source paths, and warnings.

7. Report the result concisely:
   - source title;
   - linked chapter;
   - changed files;
   - warnings, especially OCR or review warnings.

## API Contract

The helper calls:

```http
POST /api/hermes/import-source
Authorization: Bearer <CONCORSOBOOK_WEBHOOK_SECRET>
Content-Type: application/json
```

Payload:

```json
{
  "url": "https://example.gov/legge.pdf",
  "title": "Titolo fonte",
  "sourceType": "law",
  "chapterPath": "books/il-metodo-bando/chapters/diritto-amministrativo-per-candidati.md",
  "runWriter": false
}
```

Search payload when no URL is supplied:

```json
{
  "query": "legge 7 agosto 1990 n. 241 testo vigente PDF",
  "title": "Legge 241/1990 - procedimento amministrativo",
  "sourceType": "law",
  "chapterPath": "books/il-metodo-bando/chapters/procedimento-amministrativo.md",
  "runWriter": false
}
```

If you already extracted reliable text from the source, include:

```json
{
  "content": "Markdown or text extracted from the official source..."
}
```

If `content` is omitted and the selected URL is a PDF, ConcorsoBook OS will save the PDF and, when enabled, run GLM-OCR before creating the source note. The converted Markdown is written under `wiki/raw/<source-section>/...md`; the source note is written under `wiki/sources/...md`; topic/entity/chapter references are updated by the site pipeline.

## Editorial Rules

- The final chapter must derive from consolidated wiki knowledge, not directly from `wiki/raw/`.
- PDF originals are evidence in `wiki/raw/`; generated chapter text must cite source notes, topic pages, and entity pages.
- Do not invent legal dates, article numbers, thresholds, or amendments.
- Prefer official sources for laws and public administration material.
- If OCR fails or the source is incomplete, report a review note instead of claiming full consolidation.

## Safety

- Never delete or move wiki files from Telegram.
- Do not run arbitrary shell commands from a user message.
- Use only the documented helper script or explicit `curl`/HTTP call to the ConcorsoBook local endpoint.
- If the endpoint returns an error, show the error and stop; do not try unrelated fixes.
