# VOL-02 — Candidati in due tomi

Pacchetto locale per revisione e prova di stampa, 3 ottobre 2026. **Non autorizzato alla pubblicazione**: preliminari sui servizi digitali e dati editoriali comuni ancora da confermare. Step21 aperto; step22/23 non chiusi e nessun signoff24. Nessun caricamento KDP eseguito.

| Interno | Percorso | Pagine | PDF |
| --- | --- | --- | --- |
| Tomo I | Comuni, Regioni, area vasta, Camere di commercio | 700 | [Apri PDF](tomo-1/vol-02-tomo-1-proof.pdf) |
| Tomo II | Polizia locale | 268 | [Apri PDF](tomo-2/vol-02-tomo-2-proof.pdf) |

Formato 6,69 × 9,61 pollici; stampa prevista in nero su carta bianca, senza smarginatura. Corpo nominale11 pt, indice almeno9,5 pt. Ogni tomo ha indice e simulazione con soluzioni. La numerazione comune dei capitoli è spiegata nella guida iniziale. Copertine e dorsi non sono inclusi: dipendono dai metadati e dai conteggi definitivi dopo la risoluzione dei preliminari.

Il manifest principale contiene SHA-256 e dimensione dei file. Per ogni tomo sono inclusi payload impaginabile, sorgenti degli apparati adattati, manifest delle fonti, verifica degli indici, font incorporati e registro dei controlli visivi. [Rapporto PDF](PDF-VOL-02.md), [registro delle58 correzioni testuali](VOL-02.md) e [report editoriale21](21-vol-02.md) spiegano prove e limiti. Le tavole di contatto e gli ingrandimenti restano nel workspace in `artifacts/correzioni-collana-2026-10-02/vol02-tomi/`.

La riproduzione richiede questa repository, le sue dipendenze/font e Book Studio sulla porta3020. Gli script inclusi in `reproduction/` sono copie di evidenza: eseguirne gli originali dai percorsi seguenti, perché gli import sono relativi alla repository.

```powershell
.\node_modules\.bin\tsx.cmd artifacts/correzioni-collana-2026-10-02/build-vol02-tomi.ts
node artifacts/correzioni-collana-2026-10-02/export-vol02-tomo.mjs tomo-1
node artifacts/correzioni-collana-2026-10-02/export-vol02-tomo.mjs tomo-2
python artifacts/correzioni-collana-2026-10-02/verify-vol02-tomi.py
```

Il builder applica soltanto alla composizione i rinvii globali FL01, seleziona moduli interi e adatta gli apparati. L'export aumenta il croquis a9,5 pt; non riduce corpo o indice. Il renderer condiviso non è stato modificato da questo intervento. I due payload inclusi fissano i contenuti della prova; rigenerarli dal workspace dopo modifiche può produrre una prova diversa e richiede nuovi controlli.

La revisione visiva ha coperto tutte le pagine tramite61 tavole di contatto, oltre agli ingrandimenti indicati nei registri. Non è una rilettura a piena risoluzione di ogni parola delle968 pagine. Print Previewer e copia fisica restano da effettuare dopo la chiusura editoriale.

## Copertine disponibili

- [Copertina 02-I](covers/vol-02-i-cover.pdf) — 700 pagine per il dorso.
- [Copertina 02-II](covers/vol-02-ii-cover.pdf) — 268 pagine per il dorso.

Questa aggiunta supera le precedenti indicazioni di copertina assente. Restano da allineare i dati editoriali effettivi e la versione dopo la chiusura dei preliminari.
