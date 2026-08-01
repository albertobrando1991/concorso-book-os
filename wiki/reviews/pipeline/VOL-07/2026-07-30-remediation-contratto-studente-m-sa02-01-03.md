---
id: review-vol-07-m-sa02-contratto-studente-2026-07-30
type: review
title: "M-SA02 capitoli 01 e 03 - Remediation contratto dello studente"
status: completed
domain: "concorsi pubblici italiani"
topics: ["M-SA02", "contratto dello studente", "autonomia didattica", "pipeline editoriale"]
source_refs: ["sources/bandi-rappresentativi-m-sa02-professioni-sanitarie-2025-2026", "sources/ordinamento-professioni-sanitarie-leggi-42-251-43-3", "sources/profili-professionali-infermiere-ostetrica-fisioterapista-tpall", "sources/profilo-oss-dpcm-25-marzo-2025"]
book_refs: ["m-sa02-professioni-sanitarie", "vol-07-sanita-amministrativa-professioni-sanitarie"]
confidence: 0.96
updated_at: 2026-07-30T10:00:26+02:00
created_at: 2026-07-30T10:00:26+02:00
review_required: true
canonical: false
tags: ["pipeline", "vol-07", "m-sa02", "reader-contract", "remediation"]
---

# Report editoriale — M-SA02, capitoli 01 e 03

## 1. Sintesi editoriale

- Genere editoriale: manuale professionale per concorsi pubblici sanitari.
- Pubblico target: candidati che studiano autonomamente e non hanno accesso alla knowledge base editoriale.
- Perimetro di questa revisione: contratto dello studente, autonomia didattica e linguaggio reader-facing dei capitoli 01 e 03.
- Stato generale in una frase: i due capitoli sono ora autosufficienti rispetto agli strumenti interni e superano il nuovo `chapter-lint`; restano vincolanti le review normative e professionali già assegnate allo step 15.

## 2. Punti applicati della checklist

Applicati i punti 1-26 e 28-30, con particolare attenzione a coerenza interna, progressione, completezza delle spiegazioni, definizioni, esempi, tabelle, riferimenti normativi, tono e stile didattico. Il punto 27, impaginazione, non è applicabile perché la revisione ha riguardato i sorgenti Markdown e non un PDF impaginato. Applicato anche il gate di copertura didattica integrale mediante confronto con i report degli step 10 già presenti.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | Capitoli 01 e 03, corpo e riferimenti | Autonomia didattica | Grave | Il testo esponeva collegamenti `sources/` non disponibili allo studente. | Conservare la tracciabilità nel frontmatter e presentare nel corpo riferimenti normativi e professionali leggibili. | applicato |
| E02 | Capitolo 03, sezioni dei profili | Tono editoriale | Grave | Formule come “source note consolidata”, “fonte consolidata” e “corpus dei bandi” trasformavano il processo editoriale nella lezione. | Insegnare direttamente il contenuto e descrivere i bandi come campione esaminato. | applicato |
| E03 | Capitoli 01 e 03, sezione finale | Struttura del capitolo | Media | Le note di review interne erano esposte nel capitolo. | Rimuoverle dal corpo, mantenendole nei report degli step 11, 12 e nel dossier delle review dello step 15. | applicato |
| E04 | Capitolo 03, griglia comparativa | Tabelle e schemi | Media | La rimozione dei link interni lasciava celle prive di un riferimento utile. | Sostituire la colonna “Fonte” con riferimenti normativi e professionali da ricordare. | applicato |
| E05 | Capitolo 03, apertura | Stile didattico | Media | Obiettivo e mappa erano fusi in una sola sezione e la Mappa BANDO non era esplicita. | Separare obiettivi di apprendimento, Mappa BANDO, tabella operativa e box “Da sapere in 5 righe”. | applicato |

## 4. Osservazioni per capitolo

### Capitolo 01 — Professioni sanitarie: profili, requisiti e prove

- Punti di forza: progressione dal profilo alla prova, distinzione fra requisiti strutturali e mobili, esercizi e checklist coerenti con il pubblico.
- Criticità: nessuna dipendenza editoriale residua; restano le verifiche giuridico-documentali V01-V04 già registrate nel report dello step 12.

### Capitolo 03 — Discipline professionali: autonomia, responsabilità e deontologia

- Punti di forza: quadro comune, cinque profili distinti, caso comparato, domanda da commissario, quiz, esercizio e riferimenti leggibili.
- Criticità: nessun link interno o linguaggio da staff residuo; restano le review `REV-LEG`, `REV-COD`, `REV-OSS`, `REV-OST`, `REV-FIS` e `REV-TPA` già assegnate.

## 5. Coerenza globale

- Terminologia: coerente; “fonte” indica ora il riferimento giuridico o professionale utilizzabile dal candidato, non una nota interna.
- Struttura vs indice: coerente con i due capitoli attualmente presenti nel modulo.
- Promesse dell'introduzione mantenute: sì per i nuclei assegnati ai capitoli 01 e 03; i nuclei dei capitoli successivi restano fuori da questo perimetro.

## 6. Contenuto da verificare

- Coordinamento tra D.P.R. 220/2001, disciplina concorsuale generale vigente e bando target.
- Titoli pregressi, equipollenze, equivalenze e riconoscimenti esteri.
- Vigenza e formulazione dei codici professionali al cut-off finale.
- Confini professionali, applicazioni regionali dell'OSS, attribuzioni del setting e correttezza dei casi.
- Assenza di conseguenze civilistiche, penali, cliniche o ispettive non validate.

Queste verifiche erano già aperte nei report canonici e non sono dichiarate concluse da questa remediation.

## 7. Suggerimenti facoltativi (non errori)

Nessuno. Ulteriori ampliamenti vanno valutati dopo le review professionali, per evitare di anticipare contenuti tecnici non validati.

## 8. Priorità degli interventi

1. Eseguire le review normative e professionali già assegnate allo step 15.
2. Rilanciare i gate 09-12 sui capitoli se le review producono modifiche sostanziali.
3. Ispezionare il PDF impaginato prima del congelamento del testo.

## 9. Giudizio di pubblicabilità

**Pubblicabile dopo intervento medio.**

Motivazione: la remediation reader-facing è completa e i due capitoli superano il contratto automatico senza blocker; la pubblicazione finale resta subordinata alle verifiche normative e professionali aperte, che non possono essere sostituite da questa revisione editoriale.

## 10. Limiti di questa revisione

La revisione ha controllato i sorgenti Markdown, il nuovo gate e i report di pipeline esistenti. Non ha svolto le review indipendenti dello step 15, non ha validato procedure cliniche o aziendali, non ha verificato un bando target scelto dal lettore e non ha ispezionato un PDF impaginato.
