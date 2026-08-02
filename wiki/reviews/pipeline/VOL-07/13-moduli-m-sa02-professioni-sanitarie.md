# Report editoriale — M-SA02 Professioni sanitarie

## 1. Sintesi editoriale

- Genere editoriale: modulo specialistico e workbook per concorsi pubblici sanitari.
- Pubblico target: candidati ai profili di infermiere, OSS, ostetrica, fisioterapista e TPALL.
- Perimetro di questa revisione: indice, piano, matrice e nove capitoli dichiarati, 01 e 03-10.
- Stato generale in una frase: fase C completa e architettura didattica coerente; la correzione di metadati passa allo step 14 e cinque aree specialistiche passano all'audit automatico dello step 15.

## 2. Punti applicati della checklist

Applicati i punti 1-26 e 28-30 ai file Markdown: indice, struttura, progressione, titoli, coerenza interna e tra capitoli, terminologia, completezza, definizioni, contenuti, casi, tabelle, apparato normativo, sintassi, chiarezza, tono, stile didattico, ripetizioni, contraddizioni, grammatica, ortografia, punteggiatura, refusi, uniformità grafica e leggibilità. Applicato il gate di copertura didattica integrale confrontando i nove nuclei della matrice con il testo reale. Il punto 27 non è applicabile perché non è disponibile un PDF impaginato del modulo.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | Capitolo 01, frontmatter | Coerenza metadati | Media | Il capitolo 01 usava `type: book_chapter`, `status: editorial_draft` e `draft_stage: editorial-draft`; gli altri otto capitoli e la Bibbia adottano `chapter`, `draft` e `written`. | Uniformare il capitolo 01 allo standard del modulo senza cambiare il testo. | applicato |

Non risultano errori gravi, nuclei parziali, capitoli orfani o rinvii generici nel testo destinato allo studente.

## 4. Osservazioni per capitolo

### Capitolo 01 — Professioni sanitarie: profili, requisiti e prove

- Punti di forza: apre il percorso, distingue profili, requisiti stabili e mobili e forme di prova.
- Criticità: sola incoerenza E01 nel frontmatter.

### Capitolo 03 — Discipline professionali: autonomia, responsabilità e deontologia

- Punti di forza: definisce i confini dei cinque percorsi e fornisce il lessico comune del modulo.
- Criticità: nessuna certa; fonti professionali da confermare allo step 15.

### Capitolo 04 — Assistenza infermieristica, tecniche assistenziali e supporto OSS

- Punti di forza: teoria del processo assistenziale prima delle attività di base; ruoli e sicurezza restano distinti.
- Criticità: procedure, ausili e attribuzioni rientrano nell'area assistenziale dell'audit automatico.

### Capitolo 05 — Valutazione clinica, triage, urgenza ed emergenza

- Punti di forza: priorità, deterioramento ed escalation precedono i casi; scenari non esecutivi.
- Criticità: triage, supporto vitale ed emergenze ostetriche richiedono validazione specialistica.

### Capitolo 06 — Prevenzione, continuità assistenziale e presa in carico

- Punti di forza: collega prevenzione, cronicità, territorio, piano e transizioni senza ridurli a elenco di servizi.
- Criticità: modelli territoriali e applicazioni di profilo devono essere controllati nel setting.

### Capitolo 07 — Evidenze scientifiche, PICO, GRADE e applicabilità

- Punti di forza: distingue prova, certezza, raccomandazione e applicabilità; esercizi successivi alla teoria.
- Criticità: appraisal e versionamento rientrano nell'area metodologica dell'audit automatico.

### Capitolo 08 — Igiene pubblica, epidemiologia, sorveglianza e screening

- Punti di forza: progressione da misure a screening, sorveglianza e risposta al segnale.
- Criticità: calcoli, definizioni di caso, PREMAL e ICA rientrano nell'area epidemiologica dell'audit automatico.

### Capitolo 09 — Controlli TPALL, verbalizzazione, campionamento e sanzioni

- Punti di forza: separa competenza, evidenza, metodo, atto e conseguenza.
- Criticità: metodi, qualifica, atti e conseguenze rientrano nell'area TPALL dell'audit automatico.

### Capitolo 10 — Prova pratica e casi professionali

- Punti di forza: integra il percorso con LEAD-S, cinque laboratori distinti e autoverifica.
- Criticità: i laboratori restano non esecutivi fino alle cinque validazioni professionali.

## 5. Coerenza globale

- Terminologia: coerente nei concetti centrali; la Bibbia del Modulo fissa forme preferite per SSN, OSS, ostetrica, TPALL, équipe, handover ed escalation.
- Struttura vs indice: nove file, nove link e nove nuclei completi; l'assenza del capitolo 02 è intenzionale e spiegata.
- Promesse dell'introduzione mantenute: sì. Profili, prove, assistenza, emergenza, continuità, evidenze, epidemiologia, TPALL e prova pratica sono sviluppati in capitoli autonomi.
- Ripetizioni: sicurezza, competenza, documentazione e rivalutazione ricorrono con funzioni diverse; non risultano paragrafi lunghi duplicati.
- Rinvii: i rinvii al VOL-01 sono precisi e limitati al metodo generale; non sostituiscono il delta sanitario.

## 6. Contenuto da verificare

- Area assistenziale: attività attribuite, assistenza di base, ausili, compatibilità e procedure del setting.
- Area ostetrico-neonatale: puerperio, neonato, eclampsia, sepsi, tromboembolismo, distocia e prolasso.
- Area riabilitativa: valutazione funzionale, scale, controindicazioni e percorsi.
- Area epidemiologica e metodologica: calcoli, GRADE, screening, PASSI, PREMAL, focolaio e ICA.
- Area TPALL: competenze, metodi, campionamento, atti, PG e conseguenze.

Sono aree obbligatorie dell'audit automatico dello step 15, non incarichi assegnati a persone.

## 7. Suggerimenti facoltativi (non errori)

In impaginazione si può assegnare un segno grafico costante ai cinque profili, purché resti leggibile in bianco e nero e non sostituisca il nome del profilo.

## 8. Priorità degli interventi

1. Eseguire e registrare le cinque aree dell'audit automatico dello step 15.
2. Riaprire i capitoli interessati se l'audit produce correzioni sostanziali.
3. Eseguire il controllo visivo sul PDF prima del congelamento.

## 9. Giudizio di pubblicabilità

**Pubblicabile con correzioni minori.** La struttura, la copertura e l'autonomia didattica non presentano blocker testuali. E01 passa allo step 14; l'audit automatico specialistico precede comunque il congelamento.

## 10. Limiti di questa revisione

La revisione riguarda i file Markdown, la matrice e gli apparati interni. Procedure aziendali concrete e dispositivi reali restano fuori dal perimetro editoriale del manuale; il PDF impaginato sarà controllato nel preflight dedicato.
