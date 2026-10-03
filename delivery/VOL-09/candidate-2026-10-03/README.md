# VOL-09 — candidato interno del 3 ottobre 2026

**267 pagine; nessuna autorizzazione alla pubblicazione.** Servizi digitali e dati editoriali comuni restano aperti. Step 21 in corso; 22–24 non chiusi. Destinazione prevista: nero su carta bianca,6,69×9,61 pollici.

PDF: `vol-09-interior-kdp.pdf`
SHA-256: `8dd41fc17e9e2cf638e8b1e3279a1f679b68243fb624853fa620ac9b99cb9097`.

Controlli: 87 destinazioni d’indice corrette, DOM=PDF, font incorporati, zero overflow e testo fuori pagina. Copertura: tutte le pagine in tavole contatto; ingrandimenti mirati e confronto raster dei delta. Il controllo delle miniature non è lettura di ogni parola a piena risoluzione. Metodo e limiti in `reports/PDF-VOL-09.md` e `visual-review.json`.

Il pacchetto contiene PDF, payload congelato, snapshot di master/fonti/asset, hash, rapporti, contatti e zoom. Le sorgenti normative raw complete restano nel repository: le note fonte incluse ne documentano provenienza e limiti. Non sono inclusi copertina, prova fisica o collaudo della piattaforma digitale.

Riproduzione nell’attuale repository: server Book Studio su 3020, dipendenze installate e renderer corrispondente a `renderer-source-hashes.json`; poi `node delivery/VOL-09/candidate-2026-10-03/reproduction/export-frozen.mjs`. L’helper intercetta il payload API con quello congelato e scrive una cartella `reproduced`, preservando il candidato. Gli asset devono corrispondere agli hash e agli snapshot. Dipende dal repository e dai font installati: non è un export autonomo e l’identità binaria del PDF non è garantita. Qualunque nuova prova richiede verifica visiva e geometrica.

## Candidato aggiornato per la pubblicabilità

[Interno corrente](vol-09-interior-kdp.pdf), 267 pagine, SHA-256 `8dd41fc17e9e2cf638e8b1e3279a1f679b68243fb624853fa620ac9b99cb9097`. Il Gantt di p. 240 è stato renderizzato a 1950 × 1410 pixel dall’originale PDF vettoriale, senza interpolazione del vecchio raster. La risoluzione effettiva supera 370 ppi. Le altre 266 pagine sono identiche nel rendering; dati, calcolo e testo conservati.

Per riprodurre la nuova proiezione usare dalla radice della repository `node artifacts/correzioni-collana-2026-10-02/export-publication-refinements.mjs 09`, con Book Studio sulla porta 3021 e il payload congelato. Le copie in `publication-refinements/` sono evidenze; gli import degli helper originali dipendono dal checkout. I precedenti comandi di export non includono necessariamente questo delta.

## Copertine disponibili

- [Copertina 09](covers/vol-09-cover.pdf) — 268 pagine per il dorso.

Questa aggiunta supera le precedenti indicazioni di copertina assente. Restano da allineare i dati editoriali effettivi e la versione dopo la chiusura dei preliminari.
