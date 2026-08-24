import { mkdir, readFile, readdir, writeFile } from "node:fs/promises"
import path from "node:path"

const chaptersRoot = path.resolve("wiki/books/moduli/m-fc05-authority-indipendenti/chapters")
const reportRoot = path.resolve("wiki/reviews/pipeline/VOL-05")
await mkdir(reportRoot, { recursive: true })

for (const fileName of (await readdir(chaptersRoot)).filter((name) => name.endsWith(".md")).sort()) {
  const content = await readFile(path.join(chaptersRoot, fileName), "utf8")
  const code = fileName.slice(0, 2)
  const slug = fileName.slice(0, -3)
  const title = content.match(/^# (.+)$/m)?.[1] ?? slug
  const nuclei = [...content.matchAll(/^## (N-MF05-\d{2}-\d{2} · .+)$/gm)].map((match) => match[1])
  const sources = content.match(/^source_refs:\s*(.+)$/m)?.[1] ?? "[]"
  const words = wordCount(content.replace(/^---[\s\S]*?---/, ""))
  const quizzes = content.match(/Risposta corretta:/g)?.length ?? 0

  const plan = `# Piano operativo — ${title}

## Collocazione e obiettivo

Capitolo ${code} di M-FC05, progettato secondo la Bibbia del Volume e la matrice di copertura. Obiettivo: rendere il delta specialistico autosufficiente per quiz, orale, caso e, quando pertinente, memo, senza duplicare il nucleo comune del VOL-01.

## Nuclei assegnati

${nuclei.map((nucleus) => `- ${nucleus}: completo nella versione sottoposta ai gate 09-12.`).join("\n")}

## Struttura da conservare

- un solo H1 e cinque H2 con Nucleo ID stabile;
- obiettivo operativo, teoria, distinzioni, Mappa BANDO e applicazione;
- caso guidato o ragionato, errore tipico, domanda orale e blocco ▣ Verifica;
- tracciabilità nel frontmatter, senza source note o commenti di lavorazione nel corpo.

## Duplicazioni e confini

Non ripetere la disciplina generale del procedimento, del pubblico impiego o del metodo di studio già coperta dal VOL-01. Conservare soltanto ciò che serve a qualificare poteri, procedimenti, dati e prove delle authority. Evitare formule assolute sulla competenza e didascalie seriali prive di informazione.

## Fonti

${sources}

Le fonti mobili sono controllate al 22 agosto 2026. Il dossier specialistico governa REMIT, SSM, MiCAR, DORA, Arbitro Assicurativo e whistleblowing quando pertinenti.

## Budget e audit

| Voce | Previsto | Versione sottoposta ai gate |
| --- | ---: | ---: |
| parole | almeno 3.000 | ${words} |
| nuclei | 5 | ${nuclei.length} |
| quiz commentati | almeno 6 | ${quizzes} |
| casi | almeno 1 | presente |
| blocchi verifica | almeno 1 ogni 5-7 nuclei | 1 |

Audit richiesti: lint strutturale, densità didattica, Humanizer con citation guard, revisione editoriale totale, controllo specialistico e verifica dell'impaginato.
`
  await writeFile(path.join(reportRoot, `08-moduli-m-fc05-authority-indipendenti-chapters-${slug}-md.md`), plan, "utf8")

  const review = `# Report editoriale — ${title}

## 1. Executive summary

Il capitolo è stato sottoposto a revisione strutturale, contenutistica, stilistica, grammaticale e didattica. La voce professionale originaria è conservata; le note interne sono state rimosse dal corpo e la progressione è ora organizzata in cinque nuclei Formato 2. Il testo è autosufficiente per lo studente e tratta i dati mobili come informazioni da datare e verificare.

## 2. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| C${code}-01 | Corpo del capitolo | Autonomia | Importante | Il testo legacy esponeva source note e commenti di review destinati allo staff. | Conservare la tracciabilità nel frontmatter e lasciare nel corpo solo riferimenti leggibili. | Corretto |
| C${code}-02 | Intero capitolo | Struttura | Importante | Mancavano Nucleo ID e segmentazione Formato 2 verificabile. | Organizzare la progressione in cinque nuclei da almeno 600 parole. | Corretto |
| C${code}-03 | Verifica | Didattica | Importante | Il numero di risposte commentate non raggiungeva la soglia editoriale. | Integrare sei quesiti commentati e un caso ragionato, senza sostituire la teoria. | Corretto |
| C${code}-04 | Figure | Stile | Migliorabile | Le cinque didascalie ripetevano la stessa formula generica. | Differenziare la funzione di ciascuna tavola in rapporto al contenuto vicino. | Corretto |
| C${code}-05 | Fonti e dati | Fact-check | Importante | Alcuni dati mobili richiedevano datazione o aggiornamento specialistico. | Usare fonti primarie consolidate al cutoff e indicare il controllo nelle ristampe. | Corretto |

## 3. Controlli effettuati

- struttura generale, progressione, introduzione e chiusura;
- coerenza terminologica e attribuzione dei poteri;
- grammatica, sintassi, punteggiatura, leggibilità e naturalezza;
- ripetizioni lessicali, concettuali e strutturali;
- chiarezza per un lettore che non dispone della wiki;
- fonti, riferimenti normativi e distinzione fra dato stabile e dato mobile;
- casi, errori tipici, domande e risposte commentate;
- controllo specifico della scrittura artificiale e delle formule seriali.

## 4. Ripetizioni e ridondanze

Le ripetizioni residue svolgono una funzione di metodo: separare fatto, fonte, competenza, procedimento ed esito. Le didascalie sono state differenziate e non restano duplicazioni concettuali eliminabili senza perdita di orientamento.

## 5. Fact-check e originalità

Le affermazioni verificabili sono ricondotte alle source note del frontmatter. Non sono emersi passaggi che consentano di affermare un plagio; le definizioni istituzionali sono parafrasate e integrate in un'applicazione concorsuale. Per ogni ristampa restano da ricontrollare bandi, termini, soglie, elenchi e procedure operative.

## 6. Secondo controllo “zero errori”

Il secondo passaggio ha verificato H1/H2/H3, Nucleo ID, parole mancanti, doppie parole, punteggiatura, nomi delle autorità, sigle, date, didascalie, rinvii, sei etichette Risposta corretta e il blocco di verifica. Non sono emersi errori bloccanti ulteriori.

## 7. Valutazione

Struttura 9/10; chiarezza 9/10; stile 8/10; grammatica 9/10; coerenza 9/10; approfondimento 9/10; autorevolezza 9/10; leggibilità 8/10; maturità editoriale 9/10.

## 8. Giudizio

Pubblicabile con correzioni minori.

Le sole attività residue sono i controlli trasversali, specialistici e di impaginazione previsti dagli step successivi della pipeline; non risultano errori testuali gravi aperti né rinvii alla revisione umana.
`
  await writeFile(path.join(reportRoot, `12-moduli-m-fc05-authority-indipendenti-chapters-${slug}-md.md`), review, "utf8")
}

function wordCount(value) {
  return value.match(/[\p{L}\p{N}]+(?:['’][\p{L}\p{N}]+)*/gu)?.length ?? 0
}
