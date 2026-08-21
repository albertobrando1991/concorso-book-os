# VOL-04 — Pacchetto candidato per la pubblicazione

Versione candidata: `VOL-04-candidate-2026.08.21.2`

Questo pacchetto raccoglie i file e le istruzioni tecniche predisposti al termine dello step 23 della pipeline editoriale. Non costituisce approvazione alla pubblicazione: la revisione e il via libera umano restano nello step 24.

## File principali

- `vol-04-interior-kdp.pdf`: interno in bianco e nero, senza abbondanza, formato 6,69 × 9,61 pollici, 303 pagine fisiche;
- `vol-04-cover-kdp.pdf`: copertina completa con abbondanza, calcolata per 304 pagine KDP equivalenti e carta bianca;
- `METADATA-KDP.md`: metadati editoriali e campi ancora da confermare;
- `COVER-SPEC.md`: specifiche di calcolo e rigenerazione della copertina;
- `KDP-UPLOAD-CHECKLIST.md`: procedura controllata per caricamento, anteprima e prova di stampa;
- `REPORT-PUBBLICABILITA.md`: esito consolidato della revisione editoriale;
- `PREFLIGHT.md`: esito del controllo tecnico pre-pubblicazione;
- `VERSION.json`: identificazione riproducibile del candidato;
- `CHANGELOG.md`, `LIMITS.md`, `MAINTENANCE.md`: modifiche, limiti noti e piano di manutenzione;
- `MANIFEST.sha256`: impronte SHA-256 dei file consegnati.

## Sequenza operativa

1. Lo staff completa i campi contrassegnati **DA CONFERMARE** in `METADATA-KDP.md`.
2. Lo staff esegue lo step 24 della pipeline e registra l'esito della revisione umana.
3. Solo dopo l'approvazione umana, carica interno e copertina nella scheda KDP usando `KDP-UPLOAD-CHECKLIST.md`.
4. Avvia Print Previewer, risolve ogni errore bloccante e conserva le evidenze dell'anteprima.
5. Ordina una copia di prova cartacea prima della pubblicazione commerciale.

## Stato

- revisione editoriale automatizzata e tecnica: completata;
- pacchetto candidato: predisposto;
- revisione/approvazione umana: **non eseguita**;
- KDP Print Previewer: **non eseguito**;
- caricamento o pubblicazione su KDP: **non eseguiti**.

Il pacchetto va rigenerato se cambiano il PDF interno, il numero di pagine, il formato di taglio, il tipo di carta o un dato che compare in copertina.
