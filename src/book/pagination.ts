type PaginationBlock = { type: string }
type PaginationPage<TBlock extends PaginationBlock> = {
  chapter: { path: string }
  blocks: TBlock[]
}

export function moveTrailingHeadingToNextPage<
  TBlock extends PaginationBlock,
  TPage extends PaginationPage<TBlock>
>(pages: TPage[]): TPage[] {
  const nextPages = pages.map((page) => ({
    ...page,
    blocks: [...page.blocks]
  })) as TPage[]

  for (let index = 0; index < nextPages.length - 1; index += 1) {
    const page = nextPages[index]
    const nextPage = nextPages[index + 1]
    const trailingBlock = page.blocks.at(-1)

    if (
      page.blocks.length > 1
      && trailingBlock?.type === "heading"
      && nextPage.chapter.path === page.chapter.path
    ) {
      page.blocks.pop()
      nextPage.blocks.unshift(trailingBlock)
    }
  }

  return nextPages
}
