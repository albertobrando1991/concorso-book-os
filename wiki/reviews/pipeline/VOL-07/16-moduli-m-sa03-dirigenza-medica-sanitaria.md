# M-SA03 — Manifest di congelamento del testo, 3 ottobre 2026

Verifica manuale eseguita perché il CLI restituisce `gate-not-implemented` per `text-freeze`. Non è dichiarato un gate automatico implementato. Il successivo comando `--accept` documenta questa verifica sostanziale.

- Capitoli canonici presenti; assenza SA02/02 intenzionale.
- Delta audit integrale applicati e riesaminati; nessun errore testuale noto aperto nel modulo.
- Rinvii per profilo precisi; nessun rinvio a wiki nel corpo pubblico.
- Humanizer e micro-revisione sui delta; audit15 passed zero warning.
- SA02/05 densità e copertura passed; 2 DO coerenti.
- Fonti, cut-off, esempi e soluzioni distinti; norme verificate selettivamente.

| File | Stato | Data | SHA-256 |
| --- | --- | --- | --- |
| wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/01-profili-requisiti-prove-dirigenza-sanitaria.md | text-freeze | 2026-10-03 | 267ac1029736886e150d80520b2bb764115ee2f436f59f51d08d375f6898fc6c |
| wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/02-programmazione-sanitaria-organizzazione-servizi.md | text-freeze | 2026-10-03 | 7458867db28196c8ec4ecada5441551f7f2bcebc7ca6ddc29ffc49856dfb7a77 |
| wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/03-linee-guida-appropriatezza-decisioni-cliniche.md | text-freeze | 2026-10-03 | b869bf7ef33ce1db556e512b4ca3aa68f2d29b25206eeb448bdde29ea99a7b93 |
| wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/04-governo-clinico-hta-qualita-accreditamento-rischio.md | text-freeze | 2026-10-03 | 76fabdc1482d953c6c49dc2c21a602e2f0aa8c63e3c51e3c9e5ba8f16111ecb1 |
| wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/05-epidemiologia-sanita-pubblica-dirigenza.md | text-freeze | 2026-10-03 | b02a94829e8ac3c4bc52349005b120e816b214cde925e50b9efd7c44d388a7cb |
| wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/06-dirigenza-medica-discipline-casi.md | text-freeze | 2026-10-03 | 0e3ae40f05a5409fd8e5611e60bc436065cd12baf1e4d73196bbb445a7ae5892 |
| wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/07-dirigenza-sanitaria-non-medica-discipline-casi.md | text-freeze | 2026-10-03 | 4a0a07b4c3407b471d3c375556b64a814656d23883d40272bc6d2b74a8416fd4 |

Limiti: Non è freeze di VOL-07 nel suo complesso: SA01/SA04 e apparati hanno stato separato. PDF nuovi e controllo visivo ancora necessari.

Manifest JSON: `artifacts/correzioni-collana-2026-10-02/M-SA03-freeze.json`. Una modifica sostanziale richiede riapertura dei gate; non modificare il run-state a mano.
