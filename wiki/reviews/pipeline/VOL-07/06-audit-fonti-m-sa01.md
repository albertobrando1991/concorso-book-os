---
id: vol-07-step-06-audit-fonti-m-sa01
type: review
title: "VOL-07 step 06 - Audit fonti M-SA01"
status: complete
domain: "concorsi pubblici italiani"
source_refs:
  - "sources/ssn-organizzazione-aziende-standard-lea"
  - "sources/ccnl-comparto-sanita-2022-2024"
  - "sources/documentazione-sanitaria-accesso-fse-dossier-privacy"
  - "sources/contabilita-budget-aziende-sanitarie"
  - "sources/procurement-farmaci-dispositivi-flussi-nsis"
  - "sources/bandi-rappresentativi-m-sa01-sanita-amministrativa-2025-2026"
book_refs: ["m-sa01-sanita-amministrativa", "vol-07-sanita-amministrativa-professioni-sanitarie"]
updated_at: 2026-07-29T16:55:00+02:00
created_at: 2026-07-29T16:55:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-07", "step-06", "m-sa01", "source-audit"]
---

# VOL-07 step 06 - Audit fonti M-SA01

## Esito

I nuclei indispensabili per progettare M-SA01 dispongono ora di fonti ufficiali consolidate, source note, rinvii puntuali al nucleo comune e parti mobili esplicite. Sono stati acquisiti 15 snapshot ufficiali da Normattiva, Gazzetta Ufficiale, ARAN, Garante privacy, Ministero della Salute e AIFA. Il manifest immutabile contiene URL, dimensione e SHA-256 per ogni file.

Il CCNL Comparto Sanità 2019-2021 indicato dal dossier è stato sostituito come fonte corrente dal CCNL 2022-2024, sottoscritto definitivamente il 27 ottobre 2025. Il testo precedente è utilizzabile solo per disposizioni mantenute vigenti o richiamate.

## Matrice richiesta

| Nucleo | Fonte consolidata | Autorità | Ultimo controllo | Rischio aggiornamento | Capitolo impattato | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| SA01-01 Atti e procedimenti delle aziende sanitarie | [[sources/ssn-organizzazione-aziende-standard-lea]]; fonti VOL-01 su procedimento, atti e trasparenza; corpus bandi M-SA01 | Normattiva; Gazzetta Ufficiale; inPA | 2026-07-29 | medio-alto per modifiche al D.Lgs. 502/1992, norme regionali e atti aziendali | cap. 4 | consolidata |
| SA01-02 Documentazione, accesso e conservazione | [[sources/documentazione-sanitaria-accesso-fse-dossier-privacy]]; note Garante e AgID già consolidate | Garante privacy; AgID; Normattiva | 2026-07-29 | alto per FSE, decreti attuativi e discipline regionali | cap. 5 | consolidata |
| SA01-03 Front-office e comunicazione con l'utenza | Legge 150/2000 acquisita; [[sources/documentazione-sanitaria-accesso-fse-dossier-privacy]]; corpus bandi, verticale URP | Normattiva; Garante privacy; inPA | 2026-07-29 | medio per canali, organizzazione locale e servizi digitali | cap. 6 | consolidata |
| SA01-04 Contabilità economico-patrimoniale sanitaria | [[sources/contabilita-budget-aziende-sanitarie]]; D.Lgs. 118/2011 Titolo II; dati economico-finanziari SSN | Normattiva; Ministero della Salute | 2026-07-29 | medio-alto per schemi e istruzioni tecniche | cap. 9 | consolidata |
| SA01-05 Budget e programmazione aziendale | [[sources/contabilita-budget-aziende-sanitarie]]; [[sources/ssn-organizzazione-aziende-standard-lea]]; bando CAP controllo di gestione | Normattiva; Ministero della Salute; inPA | 2026-07-29 | medio-alto per disciplina regionale e sistemi aziendali | cap. 9 | consolidata |
| SA01-06 Procurement sanitario | [[sources/procurement-farmaci-dispositivi-flussi-nsis]]; rinvii puntuali alle note VOL-01 sul D.Lgs. 36/2023, correttivo, ciclo, procedure e digitalizzazione | Normattiva; ANAC; Ministero della Salute | 2026-07-29 | alto per soglie, piattaforme e disciplina tecnica | cap. 10 | consolidata |
| SA01-07 Farmaci, dispositivi, magazzino e ciclo passivo | [[sources/procurement-farmaci-dispositivi-flussi-nsis]]; corpus bandi acquisti | AIFA; Ministero della Salute; inPA | 2026-07-29 | alto per banche dati, classificazioni, vigilanza e procedure locali | cap. 10 | consolidata |
| SA01-08 Flussi informativi sanitari applicati | [[sources/procurement-farmaci-dispositivi-flussi-nsis]]; pagina patrimonio NSIS; pagina SDO; dati CE/SP | Ministero della Salute | 2026-07-29 | alto per tracciati, periodicità e nuove rilevazioni | cap. 4 | consolidata |

## Integrità del corpus

- 15 file acquisiti, 15 esiti `ok`, 0 errori di download.
- PDF ARAN con firma `%PDF` e dimensione coerente; pagine HTML conservate come snapshot della fonte ufficiale.
- Manifest: `wiki/raw/m-sa01-sanita-amministrativa/fonti/download-log.json`.
- Le pagine ministeriali con rendering dinamico sono mantenute come prova di acquisizione; per claim di dettaglio la scrittura deve usare la pagina ufficiale corrente o il decreto tecnico citato.

## Conflitti e parti mobili

1. Il D.Lgs. 502/1992 va sempre usato nel testo consolidato; D.Lgs. 517/1993 e 229/1999 sono fonti di modifica, non ordinamenti autonomi da sommare.
2. FSE, dossier sanitario e cartella clinica restano concetti distinti; le linee guida del Garante del 2009 non esauriscono il quadro 2026.
3. Contabilità sanitaria e contabilità finanziaria generale non sono intercambiabili; per gli enti del SSN rileva il Titolo II del D.Lgs. 118/2011.
4. Il procurement generale resta nel VOL-01; M-SA01 copre il delta sanitario e i processi applicati.
5. Modelli, tracciati, soglie, CCNL, disciplina regionale e procedure aziendali richiedono controllo al cut-off editoriale.

## Gate editoriale

Nessuna fonte indispensabile manca per passare alla progettazione della matrice M-SA01. Restano obbligatorie review normativa, contabile, privacy e procurement allo step 15 prima del congelamento; non bloccano la scrittura non esecutiva degli step 08-14.
