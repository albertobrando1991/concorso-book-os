interface PreviewBlockMetadataInput {
  type: string
  continued?: boolean
  headers?: string[]
}

export function getPreviewBlockMetadata(block: PreviewBlockMetadataInput) {
  const showTableHeader = block.type === "table" && (block.headers?.length || 0) > 0

  return {
    blockType: block.type,
    continued: Boolean(block.continued),
    showTableHeader,
    tableHeaderCost: showTableHeader ? 24 : 0
  }
}
