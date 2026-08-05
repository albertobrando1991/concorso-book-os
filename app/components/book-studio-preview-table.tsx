import React from "react"
import type { MarkdownBlock } from "@/src/server/book/book-preview"
import { getPreviewBlockMetadata } from "@/src/server/book/book-preview-block-metadata"

export function BookStudioPreviewTable({ block }: { block: MarkdownBlock }) {
  const metadata = getPreviewBlockMetadata(block)

  return (
    <div
      className={`previewTableWrap${metadata.continued ? " continuedTable" : ""}`}
      data-block-continued={metadata.continued ? "true" : undefined}
      data-block-type={metadata.blockType}
    >
      <table className="previewTable">
        {metadata.showTableHeader ? (
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
