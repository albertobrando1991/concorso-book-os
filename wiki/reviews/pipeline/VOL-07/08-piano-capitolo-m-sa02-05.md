---
id: vol-07-step-08-piano-m-sa02-cap-05
type: review
title: "VOL-07 step 08 - Piano M-SA02 capitolo 05"
status: complete
domain: "concorsi pubblici italiani"
source_refs:
  - "sources/sicurezza-cure-responsabilita-consenso-leggi-24-219"
  - "sources/metodo-evidenze-sistema-nazionale-linee-guida-iss"
  - "sources/sicurezza-terapia-triage-assistenza-infermieristica-ministero"
  - "sources/deterioramento-clinico-news2-sepsi-regioni"
  - "sources/arresto-cardiaco-bls-iss-snlg-2026"
  - "sources/als-adulto-erc-irc-2025"
  - "sources/sicurezza-travaglio-parto-morte-materna-ministero"
  - "sources/emorragia-post-partum-allattamento-iss-ministero"
  - "sources/puerperio-neonato-supporto-vitale-oms-irc-iss"
  - "sources/emergenze-ostetriche-eclampsia-sepsi-tromboembolia-itoss"
  - "sources/emergenze-ostetriche-distocia-spalla-prolasso-funicolo-protocolli-italiani"
book_refs: ["m-sa02-professioni-sanitarie", "vol-07-sanita-amministrativa-professioni-sanitarie"]
updated_at: 2026-08-01T23:30:00+02:00
created_at: 2026-07-31T18:45:00+02:00
review_required: false
automatic_audit_required: true
canonical: true
tags: ["pipeline", "vol-07", "step-08", "m-sa02", "chapter-05", "chapter-plan", "format-v2"]
---

# Piano operativo — M-SA02, capitolo 05

Target: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/05-valutazione-clinica-triage-urgenza-emergenza.md`.

## Obiettivo e standard di completezza

Il capitolo deve arrivare agli audit automatici già completo, autosufficiente e didatticamente sufficiente. La conferma umana non interviene nella produzione, non colma lacune e non limita il contenuto: è soltanto l'ultimo passaggio dello step 24, dopo il superamento di tutti i gate automatici.

Budget: **6.400–7.600 parole**, con **sette nuclei stabili**, **sette quiz a risposta multipla**, **tre casi ragionati** e una verifica intermedia. Ogni nucleo contiene teoria, applicazione professionale, errore tipico e verifica.

## Nuclei assegnati

| ID stabile | Nucleo | Applicazione | Verifica minima |
| --- | --- | --- | --- |
| `N-SA02-05-01` | valutazione iniziale e priorità | riconoscere dati significativi, rischio evolutivo e necessità di rivalutazione | quiz + caso |
| `N-SA02-05-02` | deterioramento, NEWS2 e sepsi | usare lo score come supporto, integrare giudizio clinico ed escalation | quiz + verifica 05.A |
| `N-SA02-05-03` | triage | distinguere finalità, priorità, rivalutazione e responsabilità organizzative | quiz + caso |
| `N-SA02-05-04` | équipe, comunicazione e sicurezza | attivazione, handover, documentazione, competenze e debriefing | quiz |
| `N-SA02-05-05` | arresto cardiaco adulto: BLS e ALS | riconoscimento, allerta, livelli di risposta e continuità post-evento | quiz + caso |
| `N-SA02-05-06` | supporto vitale neonatale | preparazione, valutazione, termoregolazione, team e trasferimento | quiz |
| `N-SA02-05-07` | allarmi ostetrici | riconoscere EPP, eclampsia, sepsi, tromboembolia, distocia e prolasso | quiz + caso |

## Architettura didattica

1. obiettivi e mappa `sicurezza → riconoscimento → priorità → allerta → équipe → rivalutazione`;
2. sette sezioni H2, una per nucleo stabile;
3. box operativi versionati quando un dato è necessario per rispondere correttamente;
4. verifica 05.A dopo il blocco deterioramento/triage;
5. tre casi ragionati distribuiti tra adulto, neonato e ostetricia;
6. batteria finale di sette quiz, ciascuno con spiegazione della risposta corretta e dei distrattori;
7. checklist finale e riferimenti istituzionali.

## Dati operativi e rinvii

Il NEWS2 non viene ridotto a un rinvio generico: il capitolo riporta parametri, classi di punteggio, ossigeno supplementare e soglia di allerta globale, con fonte, versione, ambito e limiti. Il box è identificato come `DO-SA02-05-NEWS2-ER-2024`.

Algoritmi BLS/ALS/NLS, dosi, energie, manovre e protocolli locali sono trattati al livello necessario per la prova concorsuale. Le informazioni mobili sono accompagnate dal rinvio verificabile alla fonte corrente; il testo non simula addestramento pratico né inventa sequenze universali.

## Confini editoriali

- Il capitolo 03 conserva il quadro generale di autonomia e responsabilità.
- Il capitolo 04 conserva processo assistenziale, terapia, ICA e rapporto infermiere–OSS.
- Il capitolo 06 conserva prevenzione, cronicità e continuità territoriale.
- Il capitolo 10 conserva il metodo generale della prova pratica.
- Questo capitolo resta autosufficiente per riconoscimento, priorità, escalation, sicurezza e verifica concorsuale.

## Gate misurabili

- frontmatter `format_version: 2`;
- sette ID nucleo univoci e allineati alla matrice;
- almeno 400 parole per nucleo;
- nessun nucleo privo delle quattro dimensioni richieste;
- almeno una verifica ogni tre nuclei;
- sette quiz completi di spiegazioni;
- almeno tre casi ragionati;
- dati operativi dichiarati e fonti verificabili;
- nessun blocco del gate `didactic-density`;
- nessun blocco del gate `coverage`.

## Audit e conferma finale

Lo step 15 esegue automaticamente l'audit specialistico su coerenza clinica, fonti, versione dei dati operativi, triage, BLS/ALS, supporto neonatale, allarmi ostetrici, sicurezza e qualità dei quiz. Ogni rilievo deve essere risolto prima del text freeze.

Non sono previsti revisori nominati né approvazioni umane intermedie. Soltanto allo step 24 una persona conferma in via conclusiva la validità dei testi già completi e già verificati.

## Esito del piano

Il piano è completo e implementabile: definisce contenuti, sufficienza didattica, verifiche, dati operativi, fonti, confini e gate senza delegare lacune alla conferma finale.
