type PageBlock = { type: string; continued?: boolean }

type PageLike<TBlock extends PageBlock = PageBlock> = {
  chapter: { path: string }
  blocks: TBlock[]
}

export function normalizePageBoundaries<TPage extends PageLike>(pages: TPage[]): TPage[] {
  const normalized = pages.map((page) => ({ ...page, blocks: [...page.blocks] })) as TPage[]

  for (let index = 0; index < normalized.length - 1; index += 1) {
    const current = normalized[index]
    const next = normalized[index + 1]
    if (current.chapter.path !== next.chapter.path) continue

    const trailing = current.blocks.at(-1)
    if (trailing?.type === "heading") {
      current.blocks.pop()
      next.blocks.unshift(trailing)
    }
  }

  for (let index = normalized.length - 1; index > 0; index -= 1) {
    const current = normalized[index]
    const previous = normalized[index - 1]
    if (
      current.chapter.path === previous.chapter.path
      && current.blocks.length === 1
      && current.blocks[0]?.continued
    ) {
      const precedingFragment = previous.blocks.pop()
      if (precedingFragment) current.blocks.unshift(precedingFragment)
    }
  }

  return normalized.map((page, index) => ({ ...page, pageNumber: index + 1 })) as TPage[]
}