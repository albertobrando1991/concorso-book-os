# Hermes Agent Telegram setup

Questa integrazione usa Telegram come interfaccia di Hermes, non come bot separato del sito.

## Architettura

```text
Telegram
  -> Hermes Gateway
  -> skill Hermes concorso-book-os
  -> API locale ConcorsoBook OS
  -> wiki/raw, wiki/sources, wiki/topics, wiki/entities, wiki/books
```

Il sito resta privato. Telegram parla con Hermes; Hermes chiama il sito via endpoint locale.

## 1. Prepara il sito

Nel `.env.local` del sito:

```text
HERMES_WEBHOOK_SECRET=una-chiave-condivisa-lunga
GLM_OCR_ENABLED=true
GLM_OCR_COMMAND=glmocr
```

Avvia la dashboard:

```powershell
npm run dev
```

Endpoint usato da Hermes:

```text
POST http://127.0.0.1:3000/api/hermes/import-source
```

## 2. Installa la skill per Hermes

Da questa repo:

```powershell
npm run hermes:install-skill
```

Se Hermes gira in WSL2, copia la cartella skill nel filesystem WSL:

```bash
mkdir -p ~/.hermes/skills/concorso-book-os
cp -r "/mnt/c/Users/alber/Desktop/LIBRO EDITORE CONCORSI PUBBLICI/hermes/skills/concorso-book-os/"* ~/.hermes/skills/concorso-book-os/
```

Verifica in Hermes:

```bash
hermes skills list
```

## 3. Configura Hermes per chiamare il sito

In `~/.hermes/.env`:

```bash
CONCORSOBOOK_BASE_URL=http://127.0.0.1:3000
CONCORSOBOOK_WEBHOOK_SECRET=una-chiave-condivisa-lunga
```

Usa la stessa chiave impostata nel sito come `HERMES_WEBHOOK_SECRET`.

Se Hermes gira in WSL e non raggiunge il server Windows su `127.0.0.1`, sostituisci `CONCORSOBOOK_BASE_URL` con l'IP host Windows o con un tunnel locale.

## 4. Configura Telegram in Hermes

Metodo consigliato:

```bash
hermes gateway setup
```

Seleziona Telegram, inserisci il token creato con BotFather e aggiungi il tuo Telegram user ID.

Configurazione manuale in `~/.hermes/.env`:

```bash
TELEGRAM_BOT_TOKEN=123456789:ABC...
TELEGRAM_ALLOWED_USERS=123456789
```

Il tuo user ID e' numerico. Puoi ottenerlo scrivendo a `@userinfobot` su Telegram.

Avvio:

```bash
hermes gateway
```

## 5. Uso da Telegram

Esempi:

```text
/concorso-book-os scarica questa legge e aggiungila alla conoscenza del capitolo diritto-amministrativo-per-candidati: https://example.gov/legge.pdf
```

```text
/concorso-book-os importa https://example.gov/decreto.pdf capitolo=books/il-metodo-bando/chapters/contratti-pubblici-essenziali.md titolo="Decreto correttivo" tipo=decree
```

```text
/concorso-book-os importa questa fonte e poi integra il capitolo: https://example.gov/legge.pdf capitolo=diritto-amministrativo-per-candidati
```

## 6. Silenzio intenzionale

Hermes deve poter non rispondere. La skill `concorso-book-os` resta silenziosa quando un messaggio di gruppo/canale non e' rivolto a Hermes, e' solo una conferma, e' duplicato, oppure non contiene una richiesta operativa per import, OCR, collegamento fonti o writer.

In chat privata Telegram, ogni messaggio dell'utente autorizzato va considerato rivolto a Hermes. Una lista di leggi o decreti con parole come `scarica`, `importa`, `aggiungi`, `cerca` o `integra` non deve mai generare silenzio: Hermes deve eseguire l'import oppure chiedere una sola chiarificazione se serve.

Quando un contesto API richiede comunque un testo, Hermes deve produrre solo:

```text
__HERMES_NO_REPLY__
```

L'endpoint `POST /api/hermes/chat`, se chiamato con `allowNoReply: true`, converte quel token in `204 No Content`.

## Note operative

- L'import salva il PDF in `wiki/raw/...`.
- Se GLM-OCR e' abilitato, il sito converte il PDF in Markdown prima di creare la source note.
- La conoscenza consolidata finisce in `wiki/sources/`, `wiki/topics/`, `wiki/entities/`.
- Il capitolo viene collegato via `source_refs`.
- Se chiedi anche di integrare il capitolo e `WRITER_PROVIDER=hermes`, il sito evita la ricorsione e non rilancia Hermes dentro Hermes.

## Fonti ufficiali Hermes

- Messaging Gateway: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/
- Telegram setup: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram
- Skills system: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
