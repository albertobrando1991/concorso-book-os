# Scrivere capitoli con Manual Writer Agent

Manual Writer Agent e' l'agente specializzato nella scrittura dei capitoli del libro.

## Dove si usa

Dashboard:

```text
http://127.0.0.1:3000
```

Sezione:

```text
Manual Writer Agent / Scrittura automatica capitoli
```

La dashboard mostra anche lo stato del provider di scrittura:

```text
Codex attivo
OpenAI attivo
Writer locale
```

Provider consigliato:

```text
WRITER_PROVIDER=codex
```

In questa modalita' la dashboard usa `codex exec` locale, quindi sfrutta l'account Codex/Antigravity del PC invece di richiedere una `OPENAI_API_KEY`.
Se Codex CLI non e' autenticato o non parte, l'agente produce comunque una bozza strutturata locale e tracciabile.

Per attivare Codex CLI sul PC:

```powershell
codex login --device-auth
codex login status
```

Il launcher `AVVIA_CONCORSOBOOK.bat` segnala automaticamente se Codex CLI non e' autenticato.

## Come lavora

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
4. Scegli il capitolo.
5. Scrivi una richiesta chiara.
6. Usa `Integra nel capitolo`.
7. Apri il capitolo in Obsidian.
8. Rivedi `Testo editoriale`.
9. Consolida manualmente se il testo e' pronto.

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
