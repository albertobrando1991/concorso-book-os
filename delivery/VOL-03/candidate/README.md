# VOL-03 — Candidato finale di consegna

Questo pacchetto contiene il candidato editoriale del **Volume 3 — Funzioni centrali, Fisco, Previdenza e Ispettivo** predisposto per la conferma umana dello step 24.

Il pacchetto non dichiara il volume approvato, pubblicato o caricato su KDP.

## Identità del candidato

- Versione editoriale: `VOL-03-candidate-2026.08.12.1`
- Data del candidato: 12 agosto 2026
- Cut-off normativo iniziale: 27 luglio 2026
- Verifiche specialistiche successive: fino al 12 agosto 2026, dove versionate
- Sorgente locale: branch `mfc02-didactic-coverage-20260727`, base `0f1cd8a` più modifiche selettive dello step 22-23
- Formato interno: paperback 6,69 × 9,61 pollici, bianco e nero, senza bleed
- Pagine: 819
- Stato: candidato di pubblicazione; conferma umana step 24 non eseguita

## Contenuto

- `vol-03-interior-kdp.pdf` — interno finale candidato.
- `REPORT-PUBBLICABILITA.md` — revisione editoriale totale e giudizio.
- `PREFLIGHT.md` — checklist tecnica con evidenze.
- `VERSION.json` — identità strutturata della versione.
- `CHANGELOG.md` — modifiche consolidate nel candidato.
- `LIMITS.md` — limiti dichiarati e controlli esterni residui.
- `MAINTENANCE.md` — ciclo futuro di aggiornamento.
- `MANIFEST.sha256` — hash SHA-256 dei file del pacchetto.

## Esito sintetico

- Giudizio editoriale: pubblicabile con correzioni minori, già applicate.
- Copertura aggregata: 67 righe, 0 blocker e 0 warning; 27/27 rinvii al VOL-01 risolti.
- Audit pagina per pagina: 819 pagine, 0 anomalie bloccanti e 14 note non bloccanti riesaminate.
- PDF: 9.517.620 byte; SHA-256 `357B144AE867BDED32195D75E47DC24A4898B180E6D91EC5AAD0C4EFB6234884`.
- Gate tecnici finali: test mirati, typecheck, build e controllo whitespace conformi.

## Stato remoto

Il 12 agosto 2026 è stato eseguito `git fetch origin`. Il branch locale è avanti rispetto al proprio remoto; rispetto a `origin/main` presenta storia divergente. Non è stato eseguito un merge nello step 23 per non contaminare la working tree condivisa. Il pacchetto usa staging selettivo e include esclusivamente file dichiarati nel manifest.

## Uso previsto

Prima di qualunque pubblicazione occorre eseguire lo step 24 e registrare gli eventuali messaggi del Previewer KDP durante l'upload. Qualunque errore emerso in quel passaggio deve riaprire il gate tecnico o editoriale pertinente.
