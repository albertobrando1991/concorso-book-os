# VOL-06 — Pacchetto preparatorio dell’interno

PDF: `artifacts/correzioni-collana-2026-10-02/vol-06-release-20261003-proof.pdf` (617 pagine). Hash e inventario in `manifest.json`. Per leggere gli esiti aprire `wiki/reviews/correzioni-collana-2026-10-02/PDF-VOL-06.md` e il registro delle correzioni accanto.

Stato: **interno revisionabile, front matter comune da completare**. Servizi digitali e dati editoriali non attestati; step 21 aperto, nessuna chiusura 22/23/24. Non è un pacchetto pronto da caricare su KDP: copertina finale, preflight esterno e prova fisica non inclusi.

Sono inclusi manoscritti, matrici pertinenti, source/topic/entity notes raggiungibili, asset modificati, freeze e controlli del PDF. Le raw immutabili restano nell’archivio del progetto; l’inclusione di una source note non significa che ogni sua affermazione sia stata ricertificata. Eventuali riferimenti bibliografici interni irrisolti sono elencati nel manifest.

Riproduzione: i quattro helper sotto `artifacts/correzioni-collana-2026-10-02` vanno eseguiti dalla radice della repo completa con ambiente già configurato; non sono un’applicazione autonoma. Conservare questa prova e usare un prefisso nuovo per un export successivo. Il manifest include gli hash, non promette identità binaria di PDF rigenerati.

## Candidato aggiornato per la pubblicabilità

[Interno corrente](vol-06-interior-kdp.pdf), 617 pagine, SHA-256 `34b57193a490375dcab8c48f858de6fb360d3d05af1c183b29d114b32380ab94`. Corretto Universita in Università nel catalogo e nelle sette occorrenze generate (pp. 2, 3, 5, 8, 122, 273, 429). Le altre 610 pagine sono identiche nel rendering; nessun cambiamento del contenuto disciplinare.

Per riprodurre la nuova proiezione usare dalla radice della repository `node artifacts/correzioni-collana-2026-10-02/export-publication-refinements.mjs 06`, con Book Studio sulla porta 3021 e il payload congelato. Le copie in `publication-refinements/` sono evidenze; gli import degli helper originali dipendono dal checkout. I precedenti comandi di export non includono necessariamente questo delta.

## Copertine disponibili

- [Copertina 06](covers/vol-06-cover.pdf) — 618 pagine per il dorso.

Questa aggiunta supera le precedenti indicazioni di copertina assente. Restano da allineare i dati editoriali effettivi e la versione dopo la chiusura dei preliminari.
