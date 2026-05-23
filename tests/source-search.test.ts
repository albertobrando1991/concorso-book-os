import { describe, expect, it } from "vitest"
import { buildSearchQueries, findPdfLinks, parseDuckDuckGoHtml, scoreCandidate } from "@/src/server/hermes/source-search"

describe("Hermes source search", () => {
  it("prioritizes official legal sources and PDFs", () => {
    const official = scoreCandidate({
      url: "https://www.gazzettaufficiale.it/eli/gu/1990/08/18/192/sg/pdf",
      title: "Legge 7 agosto 1990 n. 241",
      snippet: "",
      score: 0,
      source: "test"
    }, "legge 241 1990 procedimento amministrativo")
    const generic = scoreCandidate({
      url: "https://example.com/commento-legge-241",
      title: "Commento alla legge 241",
      snippet: "",
      score: 0,
      source: "test"
    }, "legge 241 1990 procedimento amministrativo")

    expect(official.score).toBeGreaterThan(generic.score)
  })

  it("extracts DuckDuckGo redirected result URLs", () => {
    const html = `
      <a class="result__a" href="//duckduckgo.com/l/?uddg=https%3A%2F%2Fnormattiva.it%2Furi-res%2FN2Ls%3Furn%3Dnir%3Astato%3Alegge%3A1990-08-07%3B241">Legge 241/1990</a>
    `

    expect(parseDuckDuckGoHtml(html, "duckduckgo")[0]).toMatchObject({
      url: "https://normattiva.it/uri-res/N2Ls?urn=nir:stato:legge:1990-08-07;241",
      title: "Legge 241/1990"
    })
  })

  it("finds PDF links on result pages", () => {
    const html = `<a href="/allegati/testo-vigente.pdf">Scarica PDF ufficiale</a>`
    const links = findPdfLinks(html, "https://www.gazzettaufficiale.it/eli/id/1990/08/18/090G0294/sg", "legge 241 1990")

    expect(links[0].url).toBe("https://www.gazzettaufficiale.it/allegati/testo-vigente.pdf")
  })

  it("builds official-site queries before generic queries", () => {
    const queries = buildSearchQueries("legge 241 1990", "law")

    expect(queries[0]).toContain("site:normattiva.it")
    expect(queries.at(-1)).toBe("legge 241 1990")
  })
})
