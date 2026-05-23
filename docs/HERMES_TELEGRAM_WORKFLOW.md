# Hermes Agent + Telegram workflow

Telegram deve parlare con Hermes Gateway. Il sito non espone un bot Telegram separato: resta backend operativo privato chiamato da Hermes.

## Obiettivo

Da Telegram puoi chiedere a Hermes di importare una fonte normativa e collegarla a un capitolo:

```text
Importa questa legge per il capitolo books/il-metodo-bando/chapters/diritto-amministrativo-per-candidati.md:
https://example.gov/legge.pdf
Scarica la fonte, aggiungila al wiki e poi integra il capitolo.
```

Puoi anche chiedere un documento senza fornire URL:

```text
Cerca il testo ufficiale della legge 241/1990, scaricalo, convertilo in Markdown e aggiungilo alla conoscenza del capitolo procedimento-amministrativo.
```

## Endpoint del sito

La skill Hermes `concorso-book-os` deve chiamare:

```http
POST http://127.0.0.1:3000/api/hermes/import-source
Authorization: Bearer <HERMES_WEBHOOK_SECRET>
Content-Type: application/json
```

Installa la skill:

```powershell
npm run hermes:install-skill
```

Setup completo: [HERMES_AGENT_TELEGRAM_SETUP.md](HERMES_AGENT_TELEGRAM_SETUP.md).

Payload minimo:

```json
{
  "url": "https://example.gov/legge.pdf",
  "title": "Titolo della fonte",
  "sourceType": "law",
  "chapterPath": "books/il-metodo-bando/chapters/diritto-amministrativo-per-candidati.md",
  "runWriter": true
}
```

Payload di ricerca quando l'utente non fornisce un URL:

```json
{
  "query": "legge 7 agosto 1990 n. 241 testo vigente PDF",
  "title": "Legge 241/1990 - procedimento amministrativo",
  "sourceType": "law",
  "chapterPath": "books/il-metodo-bando/chapters/procedimento-amministrativo.md",
  "runWriter": false
}
```

Il sito cerca candidati ufficiali, preferisce domini istituzionali e PDF, poi passa il documento selezionato allo stesso pipeline di download, GLM-OCR e ingest. Se il risultato scelto e' una pagina HTML con link PDF, il sito segue il PDF prima di creare la conoscenza.

Payload consigliato quando Hermes riesce a estrarre il testo dal PDF:

```json
{
  "url": "https://example.gov/legge.pdf",
  "title": "Titolo della fonte",
  "sourceType": "law",
  "content": "Testo ufficiale estratto dal PDF...",
  "chapterPath": "books/il-metodo-bando/chapters/diritto-amministrativo-per-candidati.md",
  "runWriter": true,
  "writerMode": "integrate",
  "instruction": "Integra questa fonte nel capitolo senza usare raw sources direttamente. Aggiungi note di review sui punti normativi da verificare."
}
```

## Cosa viene creato

- `wiki/raw/laws/<slug>.pdf` se l'URL restituisce un PDF.
- `wiki/raw/laws/<slug>.md` come Markdown estratto dal PDF con GLM-OCR, raw source testuale o nota di estrazione da completare.
- `wiki/sources/<slug>.md` come source note consolidata.
- aggiornamenti a `wiki/topics/` e `wiki/entities/`.
- collegamento del capitolo via `source_refs`.
- riga operativa in `wiki/log.md`.

Se `runWriter` e' `true`, viene eseguito anche Manual Writer sul capitolo indicato. Se pero' `WRITER_PROVIDER=hermes`, l'endpoint non rilancia automaticamente il writer per evitare una chiamata ricorsiva allo stesso agente Hermes che sta orchestrando l'import. Per l'automazione completa da Telegram usa `WRITER_PROVIDER=codex`, `openai` o `local`, oppure importa la fonte e poi lancia il writer dalla dashboard.

## Regola editoriale

La generazione del capitolo deve usare source notes, topic pages ed entity pages. Il PDF originale resta prova grezza in `wiki/raw/`, non fonte finale per il testo editoriale.

## GLM-OCR

Per convertire automaticamente i PDF in Markdown prima dell'ingest:

```text
GLM_OCR_ENABLED=true
GLM_OCR_COMMAND=glmocr
GLM_OCR_TIMEOUT_MS=600000
```

Installazione SDK:

```powershell
pip install glmocr
```

GLM-OCR puo' usare il servizio cloud MaaS o un backend self-hosted. Il sito invoca solo la CLI:

```powershell
glmocr parse <file.pdf> --output <cartella-temporanea>
```

Se GLM-OCR non produce Markdown o non e' configurato, l'import non si blocca: salva comunque il PDF e crea una nota di review che chiede l'estrazione del testo.
