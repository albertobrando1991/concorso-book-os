# M-SA02 — Manifest di congelamento del testo, 3 ottobre 2026

Verifica manuale eseguita perché il CLI restituisce `gate-not-implemented` per `text-freeze`. Non è dichiarato un gate automatico implementato. Il successivo comando `--accept` documenta questa verifica sostanziale.

- Capitoli canonici presenti; assenza SA02/02 intenzionale.
- Delta audit integrale applicati e riesaminati; nessun errore testuale noto aperto nel modulo.
- Rinvii per profilo precisi; nessun rinvio a wiki nel corpo pubblico.
- Humanizer e micro-revisione sui delta; audit15 passed zero warning.
- SA02/05 densità e copertura passed; 2 DO coerenti.
- Fonti, cut-off, esempi e soluzioni distinti; norme verificate selettivamente.

| File | Stato | Data | SHA-256 |
| --- | --- | --- | --- |
| wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/01-mappa-profili-e-prove.md | text-freeze | 2026-10-03 | 31304f56950b7fb03f7ba67df4d9d8b9cd921b208c403ccc4729cc030e618c91 |
| wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md | text-freeze | 2026-10-03 | c500422c47ddf8b96e5fb1d82c16da3dbdb2cf4cd4c1f4d75c549d86be64158d |
| wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/04-assistenza-infermieristica-tecniche-assistenziali-oss.md | text-freeze | 2026-10-03 | b4dca5c60b8af6e2e8008928c40e27c2c4aa93affb8ac53ba2e0daab20e96d3c |
| wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/05-valutazione-clinica-triage-urgenza-emergenza.md | text-freeze | 2026-10-03 | 667b6719e2e9246653879a71f22db6d5794010787fb466ee1d82ce4950d73014 |
| wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/06-prevenzione-continuita-presa-in-carico.md | text-freeze | 2026-10-03 | 15e6f3c1a83354054d6ea590881f637c76a0f5033e6299331317f72f299aaf33 |
| wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/07-evidenze-pico-grade-applicabilita.md | text-freeze | 2026-10-03 | 20c7110483bfa93a1875f69086225fd249ed21ea5ea8dc3534f479cebdb83e89 |
| wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/08-igiene-pubblica-epidemiologia-screening.md | text-freeze | 2026-10-03 | a4f6dfde6e8db1d8120b31db8c113ad2ba42e320b447bc8e67aae405eae6016a |
| wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/09-controlli-tpall-verbalizzazione-campionamento-sanzioni.md | text-freeze | 2026-10-03 | 9743fdae14da9db81058a1ed8ac27bd09c93c68fe3ad4d0587b9beaec3f1c07e |
| wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/10-prova-pratica-casi-professionali.md | text-freeze | 2026-10-03 | 0b7c9345476f789cc917bd36992e61ab757f42d93cb883189376e346420f4373 |

Limiti: Non è freeze di VOL-07 nel suo complesso: SA01/SA04 e apparati hanno stato separato. PDF nuovi e controllo visivo ancora necessari.

Manifest JSON: `artifacts/correzioni-collana-2026-10-02/M-SA02-freeze.json`. Una modifica sostanziale richiede riapertura dei gate; non modificare il run-state a mano.
