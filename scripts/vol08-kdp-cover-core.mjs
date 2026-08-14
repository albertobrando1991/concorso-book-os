import { deflateSync } from "node:zlib"

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

export function resolveCoverLayers() {
  return Object.freeze({ panels: 1, circuit: 2, content: 3, spine: 4, barcode: 5 })
}

export function resolveCircuitBand() {
  return Object.freeze({ topIn: 5.15, bottomIn: 6.8 })
}

export function parseCmykPam(input) {
  if (!Buffer.isBuffer(input)) throw new Error("PAM input must be a Buffer")
  const lfMarker = Buffer.from("ENDHDR\n", "ascii")
  const crlfMarker = Buffer.from("ENDHDR\r\n", "ascii")
  let headerEnd = input.indexOf(lfMarker)
  let markerLength = lfMarker.length

  if (headerEnd < 0) {
    headerEnd = input.indexOf(crlfMarker)
    markerLength = crlfMarker.length
  }
  if (headerEnd < 0) throw new Error("Invalid PAM: ENDHDR not found")

  const dataOffset = headerEnd + markerLength
  const header = input.subarray(0, headerEnd).toString("ascii")
  const fields = new Map(
    header.split(/\r?\n/)
      .slice(1)
      .map((line) => line.trim().split(/\s+/, 2))
      .filter(([key, value]) => key && value)
  )
  const widthPx = Number(fields.get("WIDTH"))
  const heightPx = Number(fields.get("HEIGHT"))
  const depth = Number(fields.get("DEPTH"))
  const maxValue = Number(fields.get("MAXVAL"))
  const tupleType = fields.get("TUPLTYPE")

  if (!header.startsWith("P7") || !Number.isInteger(widthPx) || widthPx < 1 || !Number.isInteger(heightPx) || heightPx < 1) {
    throw new Error("Invalid PAM geometry")
  }
  if (depth !== 4 || maxValue !== 255 || tupleType !== "CMYK") {
    throw new Error(`Expected 8-bit CMYK PAM, received depth=${depth} max=${maxValue} tuple=${tupleType || "missing"}`)
  }

  const pixels = input.subarray(dataOffset)
  const expectedBytes = widthPx * heightPx * depth
  if (pixels.length !== expectedBytes) {
    throw new Error(`Invalid PAM data length: expected ${expectedBytes}, received ${pixels.length}`)
  }

  return { widthPx, heightPx, pixels }
}

function pdfNumber(value) {
  return Number(value.toFixed(6)).toString()
}

export function buildCmykImagePdf({ widthPx, heightPx, widthIn, heightIn, pixels }) {
  if (!Number.isInteger(widthPx) || widthPx < 1 || !Number.isInteger(heightPx) || heightPx < 1) {
    throw new Error("PDF image dimensions must be positive integers")
  }
  if (!Number.isFinite(widthIn) || widthIn <= 0 || !Number.isFinite(heightIn) || heightIn <= 0) {
    throw new Error("PDF physical dimensions must be positive numbers")
  }
  if (!Buffer.isBuffer(pixels) || pixels.length !== widthPx * heightPx * 4) {
    throw new Error("PDF CMYK pixel buffer has an invalid length")
  }

  const pageWidthPt = pdfNumber(widthIn * 72)
  const pageHeightPt = pdfNumber(heightIn * 72)
  const compressedPixels = deflateSync(pixels, { level: 9 })
  const content = Buffer.from(`q\n${pageWidthPt} 0 0 ${pageHeightPt} 0 0 cm\n/Im0 Do\nQ\n`, "ascii")
  const chunks = [Buffer.from("%PDF-1.4\n%\xE2\xE3\xCF\xD3\n", "latin1")]
  const offsets = [0]
  let byteOffset = chunks[0].length

  const addObject = (number, parts) => {
    offsets[number] = byteOffset
    const objectChunks = [Buffer.from(`${number} 0 obj\n`, "ascii"), ...parts, Buffer.from("\nendobj\n", "ascii")]
    for (const chunk of objectChunks) {
      chunks.push(chunk)
      byteOffset += chunk.length
    }
  }

  addObject(1, [Buffer.from("<< /Type /Catalog /Pages 2 0 R >>", "ascii")])
  addObject(2, [Buffer.from("<< /Type /Pages /Kids [3 0 R] /Count 1 >>", "ascii")])
  addObject(3, [Buffer.from(
    `<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${pageWidthPt} ${pageHeightPt}] /Resources << /XObject << /Im0 4 0 R >> >> /Contents 5 0 R >>`,
    "ascii"
  )])
  addObject(4, [
    Buffer.from(
      `<< /Type /XObject /Subtype /Image /Width ${widthPx} /Height ${heightPx} /ColorSpace /DeviceCMYK /BitsPerComponent 8 /Interpolate false /Filter /FlateDecode /Length ${compressedPixels.length} >>\nstream\n`,
      "ascii"
    ),
    compressedPixels,
    Buffer.from("\nendstream", "ascii")
  ])
  addObject(5, [
    Buffer.from(`<< /Length ${content.length} >>\nstream\n`, "ascii"),
    content,
    Buffer.from("endstream", "ascii")
  ])

  const xrefOffset = byteOffset
  const xrefLines = offsets.slice(1).map((offset) => `${String(offset).padStart(10, "0")} 00000 n \n`).join("")
  chunks.push(Buffer.from(
    `xref\n0 6\n0000000000 65535 f \n${xrefLines}trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n${xrefOffset}\n%%EOF\n`,
    "ascii"
  ))

  return Buffer.concat(chunks)
}

function fontSource(data, localName) {
  return data ? `url("data:font/ttf;base64,${data}") format("truetype")` : `local("${localName}")`
}

export function buildVol08CoverHtml({ pageCount, fonts = {} }) {
  const geometry = calculateCoverGeometry(pageCount)
  const layers = resolveCoverLayers()
  const circuitBand = resolveCircuitBand()
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
    z-index: ${layers.panels};
  }
  .front-cover {
    left: ${frontLeftIn}in;
    width: ${backWidthIn}in;
    background: ${colors.ivory};
    z-index: ${layers.panels};
  }
  .spine {
    left: ${backWidthIn}in;
    width: ${geometry.spineIn}in;
    z-index: ${layers.spine};
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
    z-index: ${layers.circuit};
  }
  .back-content {
    position: absolute;
    left: 0.52in;
    top: 0.52in;
    width: 5.67in;
    height: 8.75in;
    z-index: ${layers.content};
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
    z-index: ${layers.barcode};
    background: ${colors.ivory};
  }
  .front-content {
    position: absolute;
    left: 0.55in;
    top: 0.52in;
    width: 5.65in;
    height: 8.82in;
    z-index: ${layers.content};
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
    <defs>
      <clipPath id="circuit-band">
        <rect x="0" y="${circuitBand.topIn}" width="${geometry.widthIn}" height="${circuitBand.bottomIn - circuitBand.topIn}"/>
      </clipPath>
    </defs>
    <g clip-path="url(#circuit-band)">
      <path d="M0.18 5.42 H1.34 V5.92 H2.55 V5.28 H3.72 V6.34 H5.08 V5.70 H6.38 V6.52 H6.95 V5.62 H7.58 V6.12 H8.76 V5.42 H9.96 V6.48 H11.18 V5.72 H12.42 V6.34 H13.97"
        fill="none" stroke="#C7D4D4" stroke-width="0.026"/>
      <path d="M0.35 6.63 H1.72 V6.10 H3.12 V6.68 H4.48 V5.98 H5.72 V6.44 H6.62 V5.30 H7.36 V6.68 H8.62 V6.02 H9.82 V6.57 H11.06 V5.33 H12.22 V6.05 H13.76 V5.56 H14.10"
        fill="none" stroke="#D9C7CA" stroke-width="0.021"/>
      <path d="M0.72 5.78 H1.86 V6.27 H3.36 V5.52 H4.72 V6.12 H5.95"
        fill="none" stroke="${colors.burgundy}" stroke-width="0.024"/>
      <path d="M8.08 6.55 H9.18 V5.76 H10.42 V6.25 H11.58 V5.55 H12.82 V6.52 H14.02"
        fill="none" stroke="${colors.teal}" stroke-width="0.027"/>
      <g fill="${colors.ivory}" stroke-width="0.026">
        <circle cx="1.34" cy="5.92" r="0.09" stroke="${colors.teal}"/>
        <circle cx="2.55" cy="5.28" r="0.065" stroke="${colors.gold}"/>
        <circle cx="3.72" cy="6.34" r="0.105" stroke="${colors.burgundy}"/>
        <circle cx="5.08" cy="5.70" r="0.075" stroke="${colors.teal}"/>
        <circle cx="6.38" cy="6.52" r="0.065" stroke="${colors.gold}"/>
        <circle cx="8.08" cy="6.55" r="0.095" stroke="${colors.burgundy}"/>
        <circle cx="9.18" cy="5.76" r="0.07" stroke="${colors.gold}"/>
        <circle cx="10.42" cy="6.25" r="0.115" stroke="${colors.teal}"/>
        <circle cx="11.58" cy="5.55" r="0.08" stroke="${colors.burgundy}"/>
        <circle cx="12.82" cy="6.52" r="0.07" stroke="${colors.gold}"/>
        <circle cx="13.76" cy="5.56" r="0.09" stroke="${colors.teal}"/>
      </g>
      <g fill="${colors.navy}">
        <rect x="0.44" y="6.16" width="0.08" height="0.08"/>
        <rect x="2.96" y="5.78" width="0.075" height="0.075"/>
        <rect x="5.52" y="6.15" width="0.085" height="0.085"/>
        <rect x="8.72" y="5.35" width="0.08" height="0.08"/>
        <rect x="11.18" y="6.26" width="0.09" height="0.09"/>
        <rect x="13.52" y="6.18" width="0.075" height="0.075"/>
      </g>
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
