type PaginationBlock = { type: string }
type PaginationPage<TBlock extends PaginationBlock> = {
  chapter: { path: string }
  blocks: TBlock[]
}

type RenderedPageChapter = {
  bookScope?: string
  frontMatterLayout?: string
}

export function renderedPageGuard(chapter: RenderedPageChapter) {
  if (chapter.bookScope === "ricettario") return 30
  if (chapter.frontMatterLayout === "analytical-index") return 24

  return 10
}

export function canBackfillBlock(input: {
  availableHeight: number
  candidateHeight: number
  candidateType?: string
  followingBlockHeight?: number
}) {
  if (input.availableHeight < 180 || input.candidateHeight <= 0) return false
  if (input.candidateType === "heading") return false

  return input.candidateHeight + 12 <= input.availableHeight
}

export function backfillCandidateCount(input: {
  availableHeight: number
  candidates: Array<{
    type: string
    continued?: boolean
    height: number
  }>
}) {
  if (input.candidates.length === 0) return 0

  const mustMoveFinalPairTogether = input.candidates.length === 2
    && input.candidates.every((candidate) => candidate.continued)
  const moveCount = mustMoveFinalPairTogether ? 2 : 1
  const selected = input.candidates.slice(0, moveCount)
  const candidateHeight = selected.reduce((total, candidate) => total + candidate.height, 0)

  return canBackfillBlock({
    availableHeight: input.availableHeight,
    candidateHeight,
    candidateType: selected[0]?.type
  }) ? moveCount : 0
}

export function paginationIsEquivalent(
  left: Array<PaginationPage<PaginationBlock>>,
  right: Array<PaginationPage<PaginationBlock>>
) {
  if (left.length !== right.length) return false

  return left.every((page, pageIndex) => {
    const comparison = right[pageIndex]
    return page.chapter.path === comparison?.chapter.path
      && page.blocks.length === comparison.blocks.length
      && page.blocks.every((block, blockIndex) => block === comparison.blocks[blockIndex])
  })
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
