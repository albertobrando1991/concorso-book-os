# M-FC02 capitolo 1 - correzione layout immagini e paginazione

Data: 2026-07-02T19:35:15+02:00
Scope: dashboard/editorial-layout

Richiesta: correggere errori di impaginazione nel capitolo 1 M-FC02, con testo sovrapposto/tagliato a fondo pagina e collisioni interne nelle immagini.

Diagnosi:
- la pagina visibile della preview si restringeva in base al contenitore, mentre il paginatore misurava una pagina a 168mm pieni;
- su viewport dashboard la pagina reale risultava piu stretta e piu bassa, con testo che andava a capo diversamente e poteva arrivare sul footer;
- alcune tabelle/figure avevano bisogno di costo di sicurezza aggiuntivo;
- nella figura 1.4 i cerchi `+` erano troppo vicini ai riquadri e davano effetto di sovrapposizione.

Interventi:
- fissata la pagina `.bookPage` a `--book-page-width` e `--book-page-height`, con scroll orizzontale del contenitore quando necessario;
- aggiunto safety cost nel paginatore per immagini, tabelle, paragrafi, liste, callout e code block;
- aggiunto pass di rifinitura DOM: se un blocco supera la zona sicura sopra il footer, viene spostato alla pagina successiva;
- aggiornato lo script `scripts/generate-mfc02-chapter01-assets.cjs`;
- rigenerate le immagini PNG/SVG del capitolo 1;
- corretti i `+` della figura 1.4 spostandoli negli spazi tra le card e riducendo il raggio.

Verifica:
- `npm.cmd test`: 23/23 passed;
- `npm.cmd run typecheck`: passed;
- `npm.cmd run build`: passed con `BUILD_ID` e `pages-manifest.json` presenti;
- Playwright production: 28 pagine, page size 635x907 px, `badPages=0`, `uniqueFigureCount=5`, `allFiguresOk=true`;
- screenshot/report: `output/playwright/mfc02-chapter01-layout-production-final.png` e `.json`.
