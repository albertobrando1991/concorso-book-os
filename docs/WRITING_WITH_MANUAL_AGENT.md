# Scrivere capitoli con Manual Writer Agent

Manual Writer Agent e' l'agente specializzato nella scrittura dei capitoli del libro.

## Dove si usa

Dashboard:

```text
http://127.0.0.1:3000
```

Se la porta 3000 e' gia' occupata o mostra un vecchio server Next, usa:

```text
http://127.0.0.1:3001
```

Sezione:

```text
Manual Writer Agent / Scrittura automatica capitoli
```

Per la revisione visuale usa prima:

```text
Book Studio / Preview visuale e revisione del manuale
```

Da Book Studio puoi:

- vedere il capitolo gia' formattato come pagina di manuale;
- passare da vista capitolo a vista libro;
- selezionare un capitolo dall'indice;
- chiedere a Codex personalizzazioni, integrazioni o formattazione;
- aggiungere immagini al capitolo selezionato.

La dashboard mostra anche lo stato del provider di scrittura:

```text
Codex attivo
OpenAI attivo
Writer locale
```

Provider consigliato:

```text
WRITER_PROVIDER=codex
CODEX_WRITER_MODEL=gpt-5.5
CODEX_WRITER_REASONING_EFFORT=xhigh
```

In questa modalita' la dashboard usa `codex exec` locale con GPT-5.5 e reasoning xhigh, quindi sfrutta l'account Codex/Antigravity del PC invece di richiedere una `OPENAI_API_KEY`.
Se Codex CLI non e' autenticato o non parte, l'agente produce comunque una bozza strutturata locale e tracciabile.

Provider Hermes opzionale:

```text
WRITER_PROVIDER=hermes
HERMES_API_BASE=http://127.0.0.1:8642/v1
HERMES_API_KEY=chiave-hermes
HERMES_MODEL=hermes-agent
HERMES_WEBHOOK_SECRET=segreto-condiviso
```

In questa modalita' Manual Writer usa l'API server locale di Hermes. Hermes puo' essere collegato a Telegram tramite il suo gateway e puo' chiamare `POST /api/hermes/import-source` per importare una fonte ufficiale nel wiki, collegarla a un capitolo e, se richiesto, lanciare la generazione del capitolo.

Per attivare Codex CLI sul PC:

```powershell
codex login --device-auth
codex login status
```

Il launcher `AVVIA_CONCORSOBOOK.bat` segnala automaticamente se Codex CLI non e' autenticato.

## Come lavora

Per `Il Metodo BANDO`, la guida operativa canonica e':

```text
wiki/books/il-metodo-bando/struttura-madre.md
```

Ogni nota capitolo contiene anche una sezione `Specifica struttura madre`. Il Manual Writer deve partire da quella struttura, poi integrare la knowledge consolidata.

L'agente legge solo conoscenza consolidata:

```text
wiki/sources/
wiki/topics/
wiki/entities/
wiki/quizzes/
wiki/books/
```

Non usa mai direttamente:

```text
wiki/raw/
```

## Modalita'

- `Integra nel capitolo`: scrive o aggiorna la sezione `Testo editoriale`.
- `Sistema formattazione`: riorganizza il capitolo in stile manuale/workbook.
- `Migliora testo`: migliora chiarezza, progressione e utilita' didattica.
- `Espandi sezione`: aggiunge esempi, casi, domande e strumenti.
- `Solo bozza`: scrive nella sezione `Bozza agente`, senza toccare `Testo editoriale`.

## Formato editoriale

Ogni intervento deve seguire lo stile del Metodo BANDO:

- apertura editoriale;
- obiettivo;
- mappa BANDO;
- spiegazione strutturata;
- box "da sapere in 5 righe";
- caso guidato;
- domanda da commissario;
- domanda-trappola;
- mini-esercizio;
- errore tipico;
- riferimenti consolidati;
- note di review.

## Workflow consigliato

1. Aggiungi fonti in `wiki/raw/`.
2. Crea o aggiorna source notes e topic pages.
3. Apri la dashboard.
4. Vai in `Book Studio`.
5. Scegli il capitolo e controlla la preview formattata.
6. Scrivi una richiesta chiara nel pannello `Personalizzazione Codex`.
7. Usa `Applica al capitolo`.
8. Ricarica la preview e controlla `Testo editoriale`.
9. Aggiungi eventuali immagini dal pannello `Immagini e layout`.
10. Apri il capitolo in Obsidian se vuoi rifinire manualmente.
11. Consolida manualmente se il testo e' pronto.

## Esempi di richiesta

```text
Riscrivi il capitolo come unità operativa per candidati principianti, con caso guidato e domanda orale.
```

```text
Integra la nuova conoscenza su responsabilità dirigenziale, performance e governo del rischio senza rendere il testo enciclopedico.
```

```text
Trasforma questa sezione in formato workbook: mappa, box da sapere, errore tipico, mini-esercizio.
```
