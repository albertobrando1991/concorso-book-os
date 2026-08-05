import { createElement } from "react"
import { renderToStaticMarkup } from "react-dom/server"
import { describe, expect, it } from "vitest"
import { BookStudioPreviewTable } from "@/app/components/book-studio-preview-table"

describe("Book Studio preview table", () => {
  it("renders headers and continuation diagnostics on later fragments", () => {
    const html = renderToStaticMarkup(createElement(BookStudioPreviewTable, {
      block: {
        type: "table",
        continued: true,
        headers: ["Voce", "Regola"],
        rows: [["Accesso", "Verificare il titolo"]]
      }
    }))

    expect(html).toContain('data-block-type="table"')
    expect(html).toContain('data-block-continued="true"')
    expect(html).toContain("continuedTable")
    expect(html).toContain("<thead>")
    expect(html).toContain("<th>Voce</th>")
    expect(html).toContain("<th>Regola</th>")
  })
})
