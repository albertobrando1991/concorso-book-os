---
id: review-vol-08-retrofit-formato-2-baseline
type: review
title: "VOL-08 â€” Baseline retrofit formato 2"
status: complete
domain: "concorsi pubblici italiani"
topics: ["formato 2", "nuclei didattici", "Book Studio"]
entities: ["ConcorsoBook OS", "Metodo BANDO"]
source_refs: []
book_refs: ["vol-08-ict-digitale-cybersecurity-dati", "m-tr01-ict-trasformazione-digitale"]
confidence: 1
updated_at: 2026-08-09
created_at: 2026-08-09
review_required: false
canonical: false
tags: ["review", "pipeline", "vol-08", "retrofit", "format-2", "baseline"]
issue_type: didactic_format
severity: high
affected_pages: ["wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/"]
---

# VOL-08 â€” Baseline retrofit formato 2

## Esito sintetico

La baseline fotografa i 13 capitoli dichiarati di M-TR01 prima di qualsiasi modifica editoriale del retrofit. Il contenuto Ã¨ ancora in formato legacy: i capitoli totalizzano 34.167 parole e 454 heading, ma non espongono Nucleo ID nÃ© heading `â–£ Verifica` riconoscibili dal gate del formato 2.

Il comando `pipeline reopen VOL-08 --step 08 --module M-TR01 --cascade` ha riaperto gli step 08-12 dei 13 capitoli e gli step dipendenti 13-23. Gli step 00-07 sono rimasti conclusi; lo step 24 di conferma umana Ã¨ rimasto pendente e non Ã¨ stato alterato.

## Metodo di misurazione

- Parole, Nucleo ID, verifiche, quiz e casi sono misurati con `analyzeDidacticDensity`, cioÃ¨ con le stesse regole del gate di densitÃ  didattica.
- Gli heading comprendono tutti i titoli Markdown del corpo, escluso il frontmatter.
- Un quiz Ã¨ conteggiato quando contiene l'etichetta `Risposta corretta:`; un caso quando contiene `Caso ragionato` o `Caso guidato`.
- Le righe matrice sono quelle della tabella canonica iniziale in `planning/02-matrice-copertura-didattica.md`, escluse le tabelle delta e la riga trasversale rinviata a VOL-01.
- I source ref sono letti dal frontmatter di ciascun capitolo.

## Baseline quantitativa per capitolo

| Cap. | Parole | Heading | Nuclei | `â–£ Verifica` | Quiz | Casi | Source ref | Righe matrice |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 01 | 1.559 | 30 | 0 | 0 | 0 | 1 | 4 | 2 |
| 02 | 2.345 | 27 | 0 | 0 | 1 | 1 | 4 | 1 |
| 03 | 2.469 | 30 | 0 | 0 | 1 | 1 | 4 | 1 |
| 04 | 2.937 | 36 | 0 | 0 | 1 | 1 | 4 | 1 |
| 05 | 2.698 | 31 | 0 | 0 | 1 | 1 | 5 | 1 |
| 06 | 2.988 | 34 | 0 | 0 | 1 | 1 | 5 | 1 |
| 07 | 3.325 | 41 | 0 | 0 | 0 | 1 | 6 | 1 |
| 08 | 2.842 | 38 | 0 | 0 | 0 | 1 | 6 | 1 |
| 09 | 1.852 | 16 | 0 | 0 | 0 | 1 | 5 | 1 |
| 10 | 2.410 | 40 | 0 | 0 | 0 | 1 | 6 | 1 |
| 11 | 2.449 | 37 | 0 | 0 | 0 | 1 | 7 | 1 |
| 12 | 2.868 | 44 | 0 | 0 | 0 | 1 | 11 | 1 |
| 13 | 3.425 | 50 | 0 | 0 | 0 | 1 | 8 | 1 |
| **Totale** | **34.167** | **454** | **0** | **0** | **5** | **13** | **75** | **14** |

## Source ref dichiarati

### Capitoli 01-04

- **01:** `sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08`; `sources/campione-bandi-ict-pa-vol-08-2024-2026`; `sources/audit-bandi-rappresentativi-m-tr01-2026-07-28`; `sources/logica-volumi-copertura-concorsobook-v4`.
- **02:** `sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08`; `sources/informatica-operativa-office-sistemi-hardware`; `sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27`; `sources/architettura-sistemi-rappresentazione-prestazioni-fonti-tecniche`.
- **03:** `sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08`; `sources/database-programmazione-formati-concorsi`; `sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27`; `sources/programmazione-algoritmi-strutture-dati-fonti-tecniche`.
- **04:** `sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08`; `sources/database-programmazione-formati-concorsi`; `sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27`; `sources/basi-dati-sql-nosql-qualita-fonti-tecniche`.

### Capitoli 05-09

- **05:** `sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08`; `sources/reti-web-protocolli-concorsi`; `sources/informatica-operativa-office-sistemi-hardware`; `sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27`; `sources/reti-sistemi-infrastrutture-fonti-tecniche`.
- **06:** `sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08`; `sources/pa-digitale-cad-identita-documenti-servizi-dati`; `sources/d-lgs-7-marzo-2005-n-82-amministrazione-digitale`; `sources/agid-piano-triennale-informatica-pa-2024-2026-aggiornamento-2026`; `sources/ingegneria-software-api-interoperabilita-fonti-tecniche`.
- **07:** `sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08`; `sources/pa-digitale-cad-identita-documenti-servizi-dati`; `sources/sicurezza-informatica-privacy-nis2-pa`; `sources/reti-sistemi-infrastrutture-fonti-tecniche`; `sources/campione-bandi-ict-pa-vol-08-2024-2026`; `sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie`.
- **08:** `sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08`; `sources/sicurezza-informatica-privacy-nis2-pa`; `sources/pa-digitale-cad-identita-documenti-servizi-dati`; `sources/campione-bandi-ict-pa-vol-08-2024-2026`; `sources/legge-28-giugno-2024-n-90-cybersicurezza-nazionale-e-reati-informatici`; `sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie`.
- **09:** `sources/iam-crittografia-logging-incident-response-fonti-primarie`; `sources/sicurezza-informatica-privacy-nis2-pa`; `sources/pa-digitale-cad-identita-documenti-servizi-dati`; `sources/campione-bandi-ict-pa-vol-08-2024-2026`; `sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08`.

### Capitoli 10-13

- **10:** `sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08`; `sources/data-governance-open-data-interoperabilita-fonti-primarie`; `sources/pa-digitale-cad-identita-documenti-servizi-dati`; `sources/agid-piano-triennale-informatica-pa-2024-2026-aggiornamento-2026`; `sources/ingegneria-software-api-interoperabilita-fonti-tecniche`; `sources/basi-dati-sql-nosql-qualita-fonti-tecniche`.
- **11:** `sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08`; `sources/ai-ml-governance-rischi-compliance-fonti-primarie`; `sources/legge-23-settembre-2025-n-132-intelligenza-artificiale`; `sources/basi-dati-sql-nosql-qualita-fonti-tecniche`; `sources/ingegneria-software-api-interoperabilita-fonti-tecniche`; `sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie`; `sources/data-governance-open-data-interoperabilita-fonti-primarie`.
- **12:** `sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08`; `sources/procurement-ict-sla-vendor-management-fonti-consolidate`; `sources/codice-contratti-pubblici-d-lgs-36-2023-e-correttivo-209-2024`; `sources/ciclo-contratti-pubblici-rup-stazione-appaltante-operatore-economico`; `sources/digitalizzazione-contratti-pubblici-anac-bdncp-fvoe-pcp`; `sources/mepa-consip-acquisti-in-rete-strumenti-acquisto-negoziazione`; `sources/ingegneria-software-api-interoperabilita-fonti-tecniche`; `sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie`; `sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie`; `sources/iam-crittografia-logging-incident-response-fonti-primarie`; `sources/data-governance-open-data-interoperabilita-fonti-primarie`.
- **13:** `sources/campione-bandi-ict-pa-vol-08-2024-2026`; `sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08`; `sources/simulazioni-concorsuali-metodo-bando`; `sources/risposta-sintetica-domande-aperte-metodo-bando`; `sources/strategia-punteggio-prova-concorsuale-metodo-bando`; `sources/revisione-finale-risposta-concorsuale-metodo-bando`; `sources/prove-concorsuali-quiz-scritto-orale-dpr-487-1994`; `sources/schema-universale-risposta-orale-metodo-bando`.

## Baseline Book Studio

La verifica registrata nello step 19 attesta:

| Controllo | Baseline |
| --- | ---: |
| Pagine | 139 |
| Overflow | 0 |
| Collisioni | 0 |
| Nuclei nel testo | 0 |
| Nuclei nell'indice analitico | 0 |
| Heading `â–£ Verifica` | 0 |

Il master KDP Ã¨ quindi stabile sul contenimento fisico, ma il volume non soddisfa ancora il contratto strutturale del formato 2. Questa baseline non attribuisce completezza didattica sulla base della lunghezza: serve soltanto a misurare il delta dei successivi step 08-23.
