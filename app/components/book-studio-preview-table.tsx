import React from "react"
import type { MarkdownBlock } from "@/src/server/book/book-preview"
import { getPreviewBlockMetadata } from "@/src/server/book/book-preview-block-metadata"

export function BookStudioPreviewTable({
  block,
  isFirstOnPage = true
}: {
  block: MarkdownBlock
  isFirstOnPage?: boolean
}) {
  const metadata = getPreviewBlockMetadata(block)
  // A fragment that continues the same table onto a new page repeats the header
  // so the reader can still identify the columns. A fragment that continues on
  // the SAME page, right below the previous fragment, must not repeat it: the
  // table is unbroken there and a second header only looks like a formatting bug.
  const showTableHeader = metadata.showTableHeader && (!metadata.continued || isFirstOnPage)

  return (
    <div
      className={`previewTableWrap${metadata.continued ? " continuedTable" : ""}`}
      data-block-continued={metadata.continued ? "true" : undefined}
      data-block-type={metadata.blockType}
    >
      <table className="previewTable">
        {showTableHeader ? (
          <thead>
            <tr>
              {(block.headers || []).map((header, index) => (
                <th key={`${header}-${index}`}>{header}</th>
              ))}
            </tr>
          </thead>
        ) : null}
        <tbody>
          {(block.rows || []).map((row, rowIndex) => (
            <tr key={`${row.join("-")}-${rowIndex}`}>
              {row.map((cell, cellIndex) => (
                <td key={`${cell}-${cellIndex}`}>{cell}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
