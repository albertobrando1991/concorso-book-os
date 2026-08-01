---
id: vol-07-step-07-audit-bandi-oss-m-sa02
type: review
title: "VOL-07 - Step 07 - Audit del cluster bandi OSS"
status: completed
domain: "concorsi pubblici italiani"
source_refs: ["sources/bandi-rappresentativi-oss-2025-2026", "sources/profilo-oss-dpcm-25-marzo-2025", "sources/profilo-oss-accordo-stato-regioni-22-febbraio-2001"]
book_refs: ["m-sa02-professioni-sanitarie", "vol-07-sanita-amministrativa-professioni-sanitarie"]
updated_at: 2026-07-28T23:55:00+02:00
created_at: 2026-07-28T22:40:00+02:00
review_required: true
canonical: true
tags: ["vol-07", "pipeline", "step-07", "oss", "bandi"]
---

# VOL-07 - Step 07 - Audit del cluster bandi OSS

## Esito

Acquisiti e verificati sei bandi OSS 2025-2026 da inPA. Tutti sono PDF validi e testualmente auditabili. Il campione copre Lombardia, Emilia-Romagna, Veneto e Piemonte; comprende due aziende del SSN e quattro enti/servizi alla persona.

Il blocker relativo alla sola esistenza del profilo nel perimetro concorsuale è risolto: l'OSS deve essere incluso in M-SA02 come sub-verticale distinto. La riga `SA02-01` resta `parziale` perché i bandi delimitano materie e prove, ma non sostengono l'insegnamento delle procedure.

## Verifiche

- 6 file presenti su 6;
- 6 firme `%PDF-`;
- 6 hash SHA-256 coerenti con il registro;
- 6 PDF con testo estraibile;
- 61 pagine e oltre 214.000 caratteri complessivi;
- programmi dettagliati in cinque bandi; un bando usa formule generali di profilo;
- prova pratica esplicita in tre bandi, con una simulazione su attrezzature/manichino.

## Decisione

- `OSS nel perimetro`: confermato.
- `Verticale autonomo`: obbligatorio.
- `Fonte profilo nazionale corrente`: DPCM 25 marzo 2025; l'Accordo del 22 febbraio 2001 è disapplicato e conservato come fonte storica.
- `Fonte delle procedure`: ancora mancante.
- `Gate step 07`: ancora bloccato.
