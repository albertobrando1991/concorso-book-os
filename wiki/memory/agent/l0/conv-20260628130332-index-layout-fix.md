# Indice analitico e sovrapposizioni front matter

Data: 2026-06-28T13:03:32+02:00

Richiesta: adattare l'indice M-FC01 alla struttura grafica dell'indice del libro base e correggere anche il libro base dove alcune pagine front matter sovrapponevano testi.

Esito:
- M-FC01 usa `front_matter_layout: analytical-index` con `index_detail: chapters-only`;
- l'indice M-FC01 ha parti, righe capitolo, puntini guida e numeri pagina come il libro base, ma senza sottorighe `1.1`, `2.1`, ecc.;
- l'indice base resta analitico dettagliato;
- la preview front matter lunga viene paginata invece di essere forzata in una sola pagina;
- lo stile delle righe indice passa a griglia per evitare collisioni tra titolo, puntini guida e numero pagina;
- aggiunto script `scripts/verify-book-studio-layout.mjs` per screenshot e controllo overflow/sovrapposizioni.

Verifiche: `npm test`, `npm run typecheck`, `node scripts/verify-book-studio-layout.mjs`.
