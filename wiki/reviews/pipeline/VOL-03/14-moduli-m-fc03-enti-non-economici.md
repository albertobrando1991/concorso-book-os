# Report editoriale — Correzioni M-FC03 Enti pubblici non economici

## 1. Sintesi editoriale

- Genere editoriale: manuale-workbook specialistico per concorsi negli enti pubblici non economici.
- Pubblico target: candidati INPS, INAIL e altri EPNE per profili amministrativi, giuridici, economico-contabili, di servizio e di vigilanza non tecnica.
- Perimetro di questa revisione: applicazione delle correzioni M01-M06 del report trasversale dello step 13.
- Stato generale in una frase: tutti i rilievi obbligatori sono stati corretti; audit specialistico, text freeze e preflight restano correttamente aperti.

Le correzioni hanno riguardato stato e workflow del modulo, front matter, piano editoriale, matrice didattica, metadati dei 19 contenuti e normalizzazione ortografica. Teoria, casi, quiz, fonti e perimetro didattico non sono stati riscritti.

## 2. Punti applicati della checklist

Applicati i controlli pertinenti dei punti 1-26 e 28-30: struttura, indice, progressione, gerarchia, coerenza tra apparati e contenuti, completezza, terminologia, sintassi, ortografia, uniformità grafica, layout Markdown, leggibilità e qualità complessiva. Ripetuti il controllo di copertura integrale, la verifica dei 114 Nuclei ID, il test dei metadati e il controllo dei rinvii interni al corpo.

Il punto 27 non è applicabile perché non è disponibile un PDF impaginato. Non sono state anticipate le verifiche normative e fattuali dello step 15. Le integrazioni al sommario e alla premessa sono limitate a una frase di raccordo ciascuna; la micro-revisione conferma che non introducono nuove promesse formative né modificano la voce autoriale.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| M01 | `index.md` | Struttura, stato editoriale e workflow | Media | Stato, fase e prossimo passo erano obsoleti; la review umana era anticipata impropriamente. | Allineare il modulo allo step 14, indicare audit automatico step 15 e conferma umana step 24. | Corretto |
| M02 | `front-matter/01-05` | Coerenza degli apparati e metadati | Media | Cinque apparati risultavano ancora `source_ready`; sommario e premessa non riflettevano le sei appendici. | Aggiornare gli stati e integrare il raccordo all'Appendice F. | Corretto |
| M03 | `planning/00-piano-editoriale.md` | Corrispondenza piano-contenuto | Media | Il piano ometteva l'Appendice F e conservava istruzioni antecedenti alla scrittura. | Inserire l'Appendice F e trasformare le note in controlli per audit e freeze. | Corretto |
| M04 | `planning/02-matrice-copertura-didattica.md` | Gerarchia, matrice e tracciabilità | Media | Stato `working`, checklist 02 sotto il capitolo 01 e intestazione 02 vuota. | Riordinare i blocchi, aggiungere l'esito 01 e portare la matrice a completa/canonica. | Corretto |
| M05 | Frontmatter dei 19 contenuti | Coerenza dei metadati | Media | Stato e `draft_stage` erano disomogenei; l'Appendice F risultava ancora draft. | Uniformare a `revised_draft` e `step-14-corrected` senza anticipare il text freeze. | Corretto |
| M06 | Capitoli 01-11 e front matter | Ortografia e uniformità grafica | Media | Erano presenti 1.150 grafie ASCII al posto degli accenti italiani. | Normalizzare i token verificati nel solo corpo, preservando frontmatter tecnico, slug, URL e apostrofi corretti. | Corretto |

### Registro delle correzioni applicate

| ID | File modificato | Correzione | Fonte/evidenza | Stato finale |
| --- | --- | --- | --- | --- |
| M01 | `index.md` | Aggiornati status, tag, fase, perimetro e prossimo passo; distinto audit automatico step 15 dalla conferma umana step 24. | Run-state VOL-03, protocollo pipeline e report step 13. | Corretto |
| M02 | `front-matter/01-05` | Allineati status e draft stage; sommario e premessa ora citano 13 capitoli e 6 appendici, inclusa F. | Indice studente e 19 file reali. | Corretto |
| M03 | `planning/00-piano-editoriale.md` | Aggiunta Appendice F; note di pre-scrittura convertite in controlli step 15/text freeze. | Scheda pipeline, indice e capitolo Appendice F. | Corretto |
| M04 | `planning/02-matrice-copertura-didattica.md` | Riordinati capitoli 01-02 in overlay, checklist, delta ed esito; stato completo e canonico. | 114 ID unici attesi e presenti; ordine dei blocchi verificato. | Corretto |
| M05 | 19 file in `chapters/` | Uniformati status e draft stage, mantenendo `format_version: 2`, `book_id` e `companion_to`. | Controllo automatico frontmatter: 19 su 19 coerenti. | Corretto |
| M06 | 11 capitoli e 4 file front matter | Normalizzate 1.150 grafie ASCII nel corpo; mantenuti quattro `po'` corretti. | Confronto HEAD/worktree e ricerca token residui. | Corretto |

## 4. Osservazioni per capitolo

### Capitoli 1-4
- Punti di forza: ortografia normalizzata; percorso da perimetro e governance a INPS e INAIL invariato.
- Criticità: fonti e assetti vigenti restano da audit specialistico.

### Capitoli 5-9
- Punti di forza: uniformità grafica ripristinata senza modificare procedimento, bilancio, PIAO, personale o contratti.
- Criticità: atti annuali, CCNL e disciplina dei contratti restano da verificare allo step 15.

### Capitoli 10-13
- Punti di forza: Decoder, casi, situazionali e piano mantengono rinvii, esercizi e verifiche; metadati allineati.
- Criticità: dati mobili dei bandi devono essere controllati al cut-off.

### Appendici A-F
- Punti di forza: metadati uniformi, Appendice F inserita nel piano e negli apparati di orientamento.
- Criticità: vigilanza, enti di orientamento e materie integrative richiedono gli audit specialistici già pianificati.

## 5. Coerenza globale

- Terminologia: accenti italiani uniformati; `po'` preservato come apostrofo corretto.
- Struttura vs indice: 13 capitoli e 6 appendici corrispondono ai 19 file reali e al piano aggiornato.
- Promesse dell'introduzione mantenute: sì; sommario e premessa descrivono ora anche l'Appendice F senza ampliare indebitamente il perimetro.
- Matrice: completa e canonica, con 114 Nuclei ID unici e sequenza iniziale corretta.
- Metadati: 19 contenuti su 19 sono `revised_draft`, `step-14-corrected`, Format 2 e collegati al modulo corretto.
- Contenuto autoriale: preservato; le modifiche ai capitoli sono limitate a metadati e accenti.

## 6. Contenuto da verificare

- Ordinamento, statuti, regolamenti, organi e poteri di vigilanza degli enti.
- Disciplina vigente INPS e INAIL su contribuzione, assicurazione, eventi, prestazioni, servizi e canali.
- Sicurezza sul lavoro, bilancio e controlli, PIAO, performance e CCNL Funzioni Centrali.
- Codice dei contratti, soglie, piattaforme e procedure correnti.
- Bandi, allegati, rettifiche, calendari e programmi usati come casi.
- Assetti di ACI, ENAC, ISTAT, ENEA, ASI, CONI e CRI.
- Fonti UE, civili, lavoristiche, processuali, penali e professionali dell'Appendice F.

## 7. Suggerimenti facoltativi (non errori)

- Valutare nel preflight una tavola iniziale profilo-capitoli-appendici-rinvii.
- Uniformare “libro base” in “Il Metodo BANDO” alla prima occorrenza solo se compatibile con la voce autoriale.
- Mantenere uniti in pagina casi, griglie e rubriche correlate.

## 8. Priorità degli interventi

1. Eseguire l'audit specialistico automatico dello step 15 sulle voci della sezione 6.
2. Chiudere ogni eventuale rilievo dell'audit prima del text freeze.
3. Eseguire successivamente preflight e revisione sull'impaginato.

## 9. Giudizio di pubblicabilità

**Pubblicabile con correzioni minori.**

Motivazione: M01-M06 sono chiusi, la copertura resta completa e non risultano errori gravi o medi residui nel perimetro dello step 14. Il giudizio non anticipa l'audit specialistico né la verifica dell'impaginato.

## 10. Limiti di questa revisione

La revisione ha verificato sorgenti Markdown, frontmatter, matrice, apparati, token ortografici, integrità del diff e permanenza dei nuclei. Non ha verificato la vigenza delle fonti esterne e non ha ispezionato un PDF impaginato. Le correzioni meccaniche sono state controllate sui token effettivamente presenti; non costituiscono una nuova revisione stilistica integrale.
