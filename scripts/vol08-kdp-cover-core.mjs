export const VOL08_COVER_SPEC = Object.freeze({
  code: "VOL-08",
  title: "ICT, digitale, cybersecurity e dati",
  subtitle: "Manuale specialistico per concorsi pubblici — informatica, cloud, cybersecurity, dati e intelligenza artificiale",
  author: "Capitale Personale",
  series: "CONCORSOBOOK OS · METODO BANDO",
  summary: "13 capitoli · 82 nuclei · casi applicativi · quiz commentati · laboratorio prove",
  website: "www.capitalepersonale.it",
  palette: Object.freeze({
    ivory: "#F3EFE6",
    navy: "#173247",
    burgundy: "#8A3147",
    teal: "#2D7480",
    charcoal: "#25292C",
    gold: "#B59A63"
  })
})

export function calculateCoverGeometry(pageCount) {
  if (!Number.isInteger(pageCount) || pageCount < 24) {
    throw new Error("pageCount must be an integer >= 24")
  }

  const trimWidthIn = 6.69
  const trimHeightIn = 9.61
  const bleedIn = 0.125
  const spineIn = pageCount * 0.002252

  return {
    pageCount,
    trimWidthIn,
    trimHeightIn,
    bleedIn,
    spineIn,
    widthIn: bleedIn + trimWidthIn + spineIn + trimWidthIn + bleedIn,
    heightIn: bleedIn + trimHeightIn + bleedIn
  }
}

function fontSource(data, localName) {
  return data ? `url("data:font/ttf;base64,${data}") format("truetype")` : `local("${localName}")`
}

export function buildVol08CoverHtml({ pageCount, fonts = {} }) {
  const geometry = calculateCoverGeometry(pageCount)
  const backWidthIn = geometry.bleedIn + geometry.trimWidthIn
  const frontLeftIn = backWidthIn + geometry.spineIn
  const colors = VOL08_COVER_SPEC.palette

  return `<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${VOL08_COVER_SPEC.code} Cover</title>
<style>
  @page { size: ${geometry.widthIn}in ${geometry.heightIn}in; margin: 0; }
  @font-face {
    font-family: "CoverArial";
    src: ${fontSource(fonts.arial, "Arial")};
    font-style: normal;
    font-weight: 400;
  }
  @font-face {
    font-family: "CoverArial";
    src: ${fontSource(fonts.arialBold, "Arial Bold")};
    font-style: normal;
    font-weight: 700;
  }
  @font-face {
    font-family: "CoverGaramond";
    src: ${fontSource(fonts.garamond, "Garamond")};
    font-style: normal;
    font-weight: 400;
  }
  * { box-sizing: border-box; }
  html, body {
    width: ${geometry.widthIn}in;
    height: ${geometry.heightIn}in;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background: ${colors.ivory};
  }
  body { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
  .cover {
    position: relative;
    width: ${geometry.widthIn}in;
    height: ${geometry.heightIn}in;
    overflow: hidden;
    color: ${colors.charcoal};
    background: ${colors.ivory};
  }
  .back-cover,
  .front-cover,
  .spine {
    position: absolute;
    top: 0;
    height: ${geometry.heightIn}in;
  }
  .back-cover {
    left: 0;
    width: ${backWidthIn}in;
    background: ${colors.ivory};
    z-index: 2;
  }
  .front-cover {
    left: ${frontLeftIn}in;
    width: ${backWidthIn}in;
    background: ${colors.ivory};
    z-index: 2;
  }
  .spine {
    left: ${backWidthIn}in;
    width: ${geometry.spineIn}in;
    z-index: 5;
    background: linear-gradient(90deg, #254255 0%, ${colors.navy} 17%, ${colors.navy} 83%, #254255 100%);
    color: ${colors.ivory};
  }
  .spine::before,
  .spine::after {
    content: "";
    position: absolute;
    top: 0;
    width: 0.065in;
    height: 100%;
    background: #D5DBD7;
    z-index: -1;
  }
  .spine::before { left: -0.065in; }
  .spine::after { right: -0.065in; }
  .circuit-field {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
  }
  .back-content {
    position: absolute;
    left: 0.52in;
    top: 0.52in;
    width: 5.67in;
    height: 8.75in;
    z-index: 3;
  }
  .back-kicker,
  .eyebrow,
  .volume-tag,
  .back-summary,
  .back-signature,
  .author,
  .spine-label {
    font-family: "CoverArial", Arial, sans-serif;
  }
  .back-kicker {
    color: ${colors.teal};
    font-size: 8.8pt;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
  }
  .back-title {
    width: 5.05in;
    margin: 0.18in 0 0.22in;
    color: ${colors.navy};
    font-family: "CoverArial", Arial, sans-serif;
    font-size: 21pt;
    line-height: 1.03;
    font-weight: 700;
    letter-spacing: -0.025em;
  }
  .back-rule {
    width: 0.92in;
    height: 0.045in;
    margin-bottom: 0.24in;
    background: ${colors.burgundy};
  }
  .back-copy {
    width: 5.35in;
    margin: 0;
    color: ${colors.charcoal};
    font-family: "CoverGaramond", Garamond, serif;
    font-size: 10.4pt;
    line-height: 1.34;
    letter-spacing: 0.002em;
  }
  .back-copy p { margin: 0 0 0.15in; }
  .back-summary {
    position: absolute;
    left: 0;
    top: 6.5in;
    width: 5.55in;
    padding: 0.16in 0.2in 0.14in;
    border-top: 0.018in solid ${colors.navy};
    border-bottom: 0.018in solid ${colors.navy};
    color: ${colors.navy};
    background: #E9E5DB;
    font-size: 8.15pt;
    line-height: 1.3;
    font-weight: 700;
    letter-spacing: 0.035em;
    text-transform: uppercase;
  }
  .back-signature {
    position: absolute;
    left: 0;
    top: 7.93in;
    width: 3.45in;
    color: ${colors.navy};
    font-size: 8.4pt;
    line-height: 1.45;
    font-weight: 700;
    letter-spacing: 0.045em;
  }
  .barcode-safe {
    position: absolute;
    left: 4.37in;
    top: 8.08in;
    width: 2in;
    height: 1.2in;
    z-index: 8;
    background: ${colors.ivory};
  }
  .front-content {
    position: absolute;
    left: 0.55in;
    top: 0.52in;
    width: 5.65in;
    height: 8.82in;
    z-index: 3;
  }
  .eyebrow {
    color: ${colors.teal};
    font-size: 8.7pt;
    line-height: 1;
    font-weight: 700;
    letter-spacing: 0.17em;
    text-transform: uppercase;
  }
  .volume-tag {
    display: inline-block;
    margin-top: 0.33in;
    padding: 0.075in 0.14in 0.065in;
    color: ${colors.ivory};
    background: ${colors.burgundy};
    font-size: 9.2pt;
    font-weight: 700;
    letter-spacing: 0.12em;
  }
  .title {
    width: 5.62in;
    margin: 0.44in 0 0;
    color: ${colors.navy};
    font-family: "CoverArial", Arial, sans-serif;
    font-size: 37pt;
    line-height: 0.98;
    font-weight: 700;
    letter-spacing: -0.038em;
  }
  .title .anchor {
    display: block;
    margin: 0.07in 0 0.03in;
    color: ${colors.burgundy};
    font-size: 43pt;
    line-height: 0.96;
    letter-spacing: -0.052em;
  }
  .subtitle {
    width: 4.95in;
    margin-top: 0.38in;
    padding-left: 0.19in;
    border-left: 0.055in solid ${colors.teal};
    color: ${colors.charcoal};
    font-family: "CoverGaramond", Garamond, serif;
    font-size: 13.1pt;
    line-height: 1.28;
  }
  .front-marker {
    position: absolute;
    left: 0;
    bottom: 1.12in;
    display: flex;
    align-items: center;
    gap: 0.14in;
  }
  .front-marker .node {
    width: 0.17in;
    height: 0.17in;
    border: 0.035in solid ${colors.gold};
    border-radius: 50%;
    background: ${colors.ivory};
  }
  .front-marker .line {
    width: 1.18in;
    height: 0.025in;
    background: ${colors.teal};
  }
  .front-marker span:last-child {
    color: ${colors.teal};
    font-family: "CoverArial", Arial, sans-serif;
    font-size: 7.8pt;
    font-weight: 700;
    letter-spacing: 0.13em;
    text-transform: uppercase;
  }
  .author {
    position: absolute;
    left: 0;
    bottom: 0.15in;
    color: ${colors.navy};
    font-size: 12.5pt;
    font-weight: 700;
    letter-spacing: 0.09em;
    text-transform: uppercase;
  }
  .spine-label {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 8.72in;
    transform: translate(-50%, -50%) rotate(90deg);
    color: ${colors.ivory};
    font-size: 7.3pt;
    line-height: 1;
    font-weight: 700;
    letter-spacing: 0.075em;
    text-align: center;
    text-transform: uppercase;
    white-space: nowrap;
  }
</style>
</head>
<body>
<main class="cover" data-page-count="${geometry.pageCount}" aria-label="Copertina completa VOL-08">
  <svg class="circuit-field" viewBox="0 0 ${geometry.widthIn} ${geometry.heightIn}" preserveAspectRatio="none" aria-hidden="true">
    <path d="M0.2 8.22 H2.05 V7.48 H3.52 V8.93 H5.02 V7.95 H6.58 V6.72 H7.08 V5.84 H8.08 V7.42 H9.25 V6.36 H10.54 V7.84 H12.04 V6.72 H13.92"
      fill="none" stroke="#C7D4D4" stroke-width="0.028"/>
    <path d="M0.36 1.72 H1.84 V2.32 H3.18 V1.36 H4.62 V2.72 H6.13 V3.44 H6.92 V4.22 H7.82 V3.12 H9.04 V4.48 H10.18 V3.72 H11.58 V4.82 H13.78"
      fill="none" stroke="#D9C7CA" stroke-width="0.021"/>
    <path d="M1.16 5.54 H2.52 V4.72 H4.08 V5.68 H5.38 V4.92 H6.71 V5.26 H7.44 V6.18 H8.63 V5.44 H9.74 V6.12 H11.11 V5.22 H12.36 V5.78 H14.08"
      fill="none" stroke="#D8D2BF" stroke-width="0.018"/>
    <path d="M8.52 8.82 V7.65 H9.62 V8.21 H10.72 V7.18 H11.84 V8.54 H12.96 V7.82 H13.74"
      fill="none" stroke="${colors.teal}" stroke-width="0.027"/>
    <path d="M9.1 5.55 V4.92 H10.12 V5.62 H11.27 V4.78 H12.42 V5.26 H13.6"
      fill="none" stroke="${colors.burgundy}" stroke-width="0.022"/>
    <g fill="${colors.ivory}" stroke-width="0.026">
      <circle cx="2.05" cy="8.22" r="0.105" stroke="${colors.teal}"/>
      <circle cx="3.52" cy="8.93" r="0.075" stroke="${colors.gold}"/>
      <circle cx="5.02" cy="7.95" r="0.115" stroke="${colors.burgundy}"/>
      <circle cx="6.58" cy="6.72" r="0.08" stroke="${colors.teal}"/>
      <circle cx="8.08" cy="7.42" r="0.105" stroke="${colors.burgundy}"/>
      <circle cx="9.25" cy="6.36" r="0.075" stroke="${colors.gold}"/>
      <circle cx="10.54" cy="7.84" r="0.125" stroke="${colors.teal}"/>
      <circle cx="12.04" cy="6.72" r="0.09" stroke="${colors.burgundy}"/>
      <circle cx="13.92" cy="6.72" r="0.07" stroke="${colors.gold}"/>
      <circle cx="1.84" cy="2.32" r="0.065" stroke="${colors.gold}"/>
      <circle cx="4.62" cy="2.72" r="0.08" stroke="${colors.teal}"/>
      <circle cx="6.92" cy="4.22" r="0.075" stroke="${colors.burgundy}"/>
      <circle cx="10.18" cy="3.72" r="0.09" stroke="${colors.teal}"/>
      <circle cx="12.42" cy="5.26" r="0.075" stroke="${colors.gold}"/>
    </g>
    <g fill="${colors.navy}">
      <rect x="0.68" y="7.18" width="0.09" height="0.09"/>
      <rect x="3.05" y="4.26" width="0.075" height="0.075"/>
      <rect x="5.72" y="2.86" width="0.085" height="0.085"/>
      <rect x="8.95" y="8.78" width="0.085" height="0.085"/>
      <rect x="11.78" y="3.05" width="0.09" height="0.09"/>
      <rect x="13.42" y="8.42" width="0.075" height="0.075"/>
    </g>
  </svg>

  <section class="back-cover" aria-label="Quarta di copertina">
    <div class="back-content">
      <div class="back-kicker">Metodo BANDO · Percorso specialistico</div>
      <h2 class="back-title">La competenza tecnica diventa una risposta da concorso.</h2>
      <div class="back-rule"></div>
      <div class="back-copy">
        <p>Prepararsi a un concorso ICT nella pubblica amministrazione non significa ripassare informatica in modo generico. Significa collegare fondamenti tecnici, sicurezza, dati, organizzazione pubblica e capacità di trasformare la teoria in risposte efficaci.</p>
        <p>Questo volume organizza il percorso in 13 capitoli e 82 nuclei didattici: programmazione, basi di dati, reti e sistemi, software e API, cloud e DevOps, cybersecurity, identità e risposta agli incidenti, data governance, intelligenza artificiale, procurement ICT e prove concorsuali.</p>
        <p>Ogni nucleo unisce spiegazioni autonome, distinzioni ad alta resa, errori frequenti, casi applicativi, quiz commentati e strumenti di allenamento. Un manuale-workbook per studiare, verificare e correggere il proprio metodo prima della prova.</p>
      </div>
      <div class="back-summary">${VOL08_COVER_SPEC.summary}</div>
      <div class="back-signature">Capitale Personale · Metodo BANDO<br>${VOL08_COVER_SPEC.website}</div>
    </div>
    <div class="barcode-safe" aria-hidden="true"></div>
  </section>

  <section class="spine" aria-label="Dorso">
    <div class="spine-label">VOL-08 · ICT, DIGITALE, CYBERSECURITY E DATI · CAPITALE PERSONALE</div>
  </section>

  <section class="front-cover" aria-label="Prima di copertina">
    <div class="front-content">
      <div class="eyebrow">${VOL08_COVER_SPEC.series}</div>
      <div class="volume-tag">${VOL08_COVER_SPEC.code}</div>
      <h1 class="title">ICT, digitale,<span class="anchor">cybersecurity</span>e dati</h1>
      <div class="subtitle">${VOL08_COVER_SPEC.subtitle}</div>
      <div class="front-marker"><span class="node"></span><span class="line"></span><span>teoria · casi · verifica</span></div>
      <div class="author">${VOL08_COVER_SPEC.author}</div>
    </div>
  </section>
</main>
</body>
</html>`
}
