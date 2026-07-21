---
id: review-vol-01-intervento-p1-superficie-struttura-2026-07-21
type: review
title: "VOL-01 - Verifica editoriale P1 su superficie e coerenza strutturale"
status: completed
domain: "concorsi pubblici italiani"
topics: ["revisione editoriale", "superficie di pubblicazione", "appendice E", "uniformita grafica"]
entities: ["VOL-01", "Metodo BANDO"]
source_refs: ["sources/schema-universale-risposta-orale-metodo-bando.md", "sources/struttura-madre-il-metodo-bando.md", "sources/prove-concorsuali-quiz-scritto-orale-dpr-487-1994.md"]
book_refs: ["il-metodo-bando"]
confidence: 0.95
updated_at: 2026-07-21T00:00:00+02:00
created_at: 2026-07-21T00:00:00+02:00
review_required: false
canonical: true
issue_type: editorial_review
severity: high
affected_pages: ["intero volume", "appendice E", "capitoli 19-20"]
tags: ["revisore-editoriale-totale", "vol-01", "follow-up", "book-studio"]
---

# Report editoriale - Il Metodo BANDO (intervento P1)

## 1. Sintesi editoriale

- Genere editoriale: manuale-workbook per concorsi pubblici italiani.
- Pubblico target: candidati generalisti e amministrativi che studiano e si allenano anche senza strumenti digitali.
- Perimetro di questa revisione: E08, E09 ed E13 del report generale, con controllo della superficie pubblica, dell'Appendice E e delle heading dei capitoli 19-20.
- Stato generale in una frase: E08 ed E13 sono risolti; E09 è stato rettificato come falso positivo sulla base della fonte consolidata e reso esplicito nel testo, senza duplicare i capitoli sulle prove.

## 2. Punti applicati della checklist

Sono stati applicati tutti i 30 punti al perimetro modificato: coerenza fra struttura, indice e contenuto; gerarchia delle heading; progressione; completezza; terminologia; accuratezza concettuale; esempi, tabelle e note; apparato delle fonti; sintassi, chiarezza, tono e stile didattico; ripetizioni e contraddizioni; grammatica, ortografia, punteggiatura, refusi, uniformità grafica, layout Markdown, leggibilità e qualità complessiva.

Il punto 27 è limitato alla preview generata da Book Studio: non è stato ispezionato un PDF finale. Il gate di copertura integrale è stato applicato verificando la matrice aggiornata, senza promuovere nuclei che conservano `review_required: true`.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| E08 | Book Studio, intero VOL-01 | Superficie di pubblicazione | Grave | Le sezioni `Note di review` non erano comprese fra le heading riservate allo staff e potevano entrare nella preview. | Aggiunta la heading al filtro canonico e introdotto un test di regressione che ne verifica l'assenza dai blocchi pubblici. | Risolto |
| E09 | Appendice E | Coerenza struttura-fonte | Grave | Il report precedente interpretava i “tre formati” come quiz, scritto e orale. La fonte consolidata li definisce invece come tre durate della risposta orale. | Rettificato il rilievo; esplicitate nel testo le durate 30 secondi, 2 minuti e 5 minuti e il rinvio ai capitoli 14-15 per quiz e scritto. | Rettificato e risolto |
| E13 | Capitoli 19-20 | Uniformità grafica | Lieve | `sanità amministrativa` iniziava con minuscola in due heading parallele. | Uniformata la forma `Sanità amministrativa` in entrambi i capitoli. | Risolto |

## 4. Osservazioni per capitolo

### Capitoli 1-24 e appendici A-F - Superficie pubblica

- Punti di forza: le note interne restano nei file sorgente per il workflow editoriale, ma non vengono più proiettate nella preview destinata al lettore.
- Criticità: il filtro riguarda la generazione Book Studio; l'eventuale pipeline futura di export diretto Markdown dovrà riusare la stessa regola.

### Appendice E - Schema universale di risposta orale

- Punti di forza: fonte, titolo, indice e contenuto sono coerenti; le tre durate sono tutte sviluppate con template e griglie.
- Criticità: resta necessaria la review editoriale finale dell'appendice e della resa grafica delle schede.

### Capitoli 19-20 - Famiglie e mappe profilo

- Punti di forza: la denominazione `Sanità amministrativa` è ora uniforme fra atlante e mappa.
- Criticità: esempi e catalogo restano mobili e richiedono il riallineamento già registrato nella matrice.

## 5. Coerenza globale

- Terminologia: coerente nel perimetro; `Note di review` resta una denominazione interna, mentre `Sanità amministrativa` è uniforme nel corpo pubblico.
- Struttura vs indice: Appendice E resta correttamente dedicata alla risposta orale; quiz e scritto rimangono nei capitoli 14 e 15.
- Promesse dell'introduzione mantenute: la promessa dei tre formati dell'Appendice E è soddisfatta come 30 secondi, 2 minuti e 5 minuti, secondo la fonte consolidata.
- Matrice: V01-PROVE, V01-PROFILI e V01-APP descrivono ora lo stato effettivo senza alterare il conteggio complessivo dei gate.

## 6. Contenuto da verificare

- Resa delle griglie dell'Appendice E nel PDF finale A4.
- Riutilizzo del filtro staff-only in ogni futura pipeline di export diversa da Book Studio.
- Allineamento di esempi e denominazioni dei capitoli 19-20 al catalogo e ai bandi correnti.

## 7. Suggerimenti facoltativi (non errori)

- Rendere la lista delle heading staff-only una costante condivisa se verrà introdotto un secondo esportatore.
- Inserire nell'Appendice E una pagina duplicabile per ciascuna delle tre durate durante l'impaginazione finale.

## 8. Priorità degli interventi

1. Riconsolidare e revisionare le fonti normative mobili, con priorità al capitolo 9.
2. Correggere il perimetro anti-duplicazione dei capitoli 8 e 10.
3. Uniformare l'apparato delle fonti e gli stati editoriali residui.
4. Eseguire preview e controllo PDF finale dopo gli interventi contenutistici.

## 9. Giudizio di pubblicabilità

**Non pubblicabile allo stato attuale.**

Motivazione: E08, E09 ed E13 non sono più blocker, ma la matrice conserva 15 nuclei `parziale` per review normative, perimetro, apparato e workflow. Questo intervento migliora la superficie editoriale senza certificare il resto del volume.

## 10. Limiti di questa revisione

- Il controllo è circoscritto ai tre rilievi indicati e non ripete l'audit integrale dei 31 file.
- Non è stato ispezionato un PDF finale né verificato un esportatore diverso da Book Studio.
- Non sono state aggiornate norme o fonti mobili in questo intervento.
- La rettifica E09 deriva dal confronto fra source note consolidata, indice e contenuto effettivo dell'appendice.
