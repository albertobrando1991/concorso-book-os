# Task 3 — Inventario globale volumi e moduli

Leggi `docs/superpowers/plans/2026-07-17-copertura-didattica-integrale.md`, Task 3; la specifica globale; `wiki/books/moduli/architettura-moduli-specialistici.md`; gli indici sotto `wiki/books/volumi/` e `wiki/books/moduli/`.

## Deliverable

Creare esclusivamente:

- `wiki/reviews/audit-copertura-didattica-inventario-globale-2026-07-17.md`
- `wiki/dashboards/copertura-didattica-globale.md`

## Contenuto obbligatorio

- censimento dei 12 volumi commerciali e dei 25 moduli canonici;
- per ogni elemento: id, titolo/famiglia, cartella/index presente, numero capitoli, distribuzione stati, conteggio indicativo parole, placeholder/source-ready, source refs, matrice disponibile;
- distinzione tra assenza filesystem, scaffold, source-ready, draft/revised, aggregatore commerciale e contenuto pubblicabile;
- nessuna equivalenza tra “file esistente” e “copertura completa”;
- totali globali e lista blocker/priorità;
- dichiarazione esplicita che è inventario strutturale, non audit semantico;
- segnalazione della working tree sporca: censire lo stato reale su disco senza modificare file utente;
- frontmatter standard per review/dashboard e link a source/topic di copertura integrale.

Un volume commerciale aggregatore senza capitoli propri non è automaticamente mancante se aggrega moduli identificati; deve però essere marcato come aggregatore e non come copertura verificata.

## Verifica

```powershell
rg -n "VOL-01|VOL-12|M-FC01|M-SP04|12 volumi|25 moduli|non.*audit semantico" wiki/reviews/audit-copertura-didattica-inventario-globale-2026-07-17.md wiki/dashboards/copertura-didattica-globale.md
git diff --check -- wiki/reviews/audit-copertura-didattica-inventario-globale-2026-07-17.md wiki/dashboards/copertura-didattica-globale.md
```

Controlla con script/PowerShell che le righe di catalogo contino realmente 12 e 25. Non leggere o usare raw per valutare contenuti.

Committare solo i due file con `docs: inventory didactic coverage catalog`.

Scrivere `.superpowers/sdd/task-3-report.md` con stato, metodo, conteggi, verifiche, commit e concerns.
