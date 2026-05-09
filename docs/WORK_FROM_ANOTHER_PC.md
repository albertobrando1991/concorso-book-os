# Lavorare da un altro PC

Questa guida serve per aprire e continuare ConcorsoBook OS da un altro computer usando lo stesso account GitHub/Antigravity.

## Requisiti
- Accesso al tuo account GitHub.
- Node.js 24 o versione compatibile recente.
- Git.
- Antigravity, VS Code o altro editor.
- Opzionale: Obsidian se vuoi lavorare direttamente sul vault markdown.

## Repository

```text
https://github.com/albertobrando1991/concorso-book-os
```

## Setup rapido

```powershell
git clone https://github.com/albertobrando1991/concorso-book-os.git
cd concorso-book-os
npm install
npm run dev
```

Dashboard locale:

```text
http://127.0.0.1:3000
```

## Variabili locali

Copia `.env.example` in `.env.local` sul nuovo PC e compila solo le chiavi disponibili:

```text
OBSIDIAN_BASE_URL=https://127.0.0.1:27124
OBSIDIAN_API_KEY=
OPENAI_API_KEY=
WIKI_ROOT=wiki
DEFAULT_LLM_MODEL=gpt-4.1-mini
```

Non committare `.env.local`.

## Obsidian sul nuovo PC

Il vault e' la cartella:

```text
wiki/
```

In Obsidian:
1. Open folder as vault.
2. Seleziona `wiki/`.
3. Installa e abilita il plugin Local REST API solo se vuoi far usare all'app le patch chirurgiche via API locale.
4. Inserisci la API key in `.env.local`.

Nota: Obsidian Local REST API e' locale al PC. Ogni computer deve avere il proprio Obsidian/plugin/API key.

## Workflow consigliato

### Se lavori da solo

```powershell
git pull
npm install
npm run dev
```

Quando hai finito:

```powershell
npm run typecheck
npm test
npm run build
git status
git add -A
git commit -m "Describe the change"
git push
```

### Se lavori da due PC

Prima di iniziare su un PC:

```powershell
git pull
```

Dopo avere lavorato:

```powershell
git push
```

Evita di modificare lo stesso file wiki contemporaneamente su due PC. Se succede, risolvi il conflitto mantenendo `raw/` immutabile e preservando `log.md` come append-only.

## Cosa viene sincronizzato via GitHub
- Codice app.
- Dashboard.
- Agent services.
- Vault markdown `wiki/`.
- Artifacts.
- Test.

## Cosa non viene sincronizzato via GitHub
- `.env.local`.
- `node_modules/`.
- `.next/`.
- Config locali Obsidian.
- API key OpenAI e Obsidian.

## Verifica ambiente

```powershell
npm run typecheck
npm test
npm run build
npm run screenshot
```

Se questi comandi passano, il nuovo PC e' pronto.

