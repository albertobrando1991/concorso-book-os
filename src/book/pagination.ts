type PaginationBlock = { type: string; text?: string; continued?: boolean }
type PaginationPage<TBlock extends PaginationBlock> = {
  chapter: { path: string }
  blocks: TBlock[]
}

type RenderedPageChapter = {
  bookScope?: string
  frontMatterLayout?: string
}

// Only short, contiguous introductions to a structured block form a chain.
// Continued table/list fragments remain independently pageable.
export function keepGroupEnd(blocks: PaginationBlock[], start: number): number {
  const first = blocks[start]
  if (!first) return start
  const next = blocks[start + 1]
  if (first.type === "index-part" && next?.type === "index-chapter") {
    return blocks[start + 2]?.type === "index-row" ? start + 3 : start + 2
  }
  if (first.type === "index-chapter" && next?.type === "index-row") return start + 2
  let cursor = start + (first.type === "heading" ? 1 : 0)
  let words = 0
  let paragraphs = 0
  while (blocks[cursor]?.type === "paragraph" && paragraphs < 3) {
    const text = blocks[cursor].text?.trim()
    const count = text ? text.split(/\s+/).length : 0
    if (!count || count > 48 || words + count > 72) break
    words += count
    paragraphs += 1
    cursor += 1
  }
  if ((paragraphs > 0 || first.type === "heading")
    && ["table", "list", "code", "image", "callout"].includes(blocks[cursor]?.type)
    && !blocks[cursor]?.continued) return cursor + 1
  return first.type === "heading" && next && next.type !== "heading" ? start + 2 : start + 1
}

export function keepGroupStart(blocks: PaginationBlock[], splitIndex: number): number {
  for (let start = 0; start < splitIndex;) {
    const end = keepGroupEnd(blocks, start)
    if (end > splitIndex) return start
    start = end
  }
  return splitIndex
}

export function paginateBlockGroups<T extends PaginationBlock>(
  blocks: T[], heights: number[], budget: number, firstHeader: number, runningHeader: number
): T[][] {
  const pages: T[][] = []
  let page: T[] = []
  let used = firstHeader
  for (let index = 0; index < blocks.length;) {
    let end = keepGroupEnd(blocks, index)
    let height = heights.slice(index, end).reduce((sum, value) => sum + value, 0)
    // An over-height group may split; keeping it together must not create overflow.
    if (height > budget - runningHeader) {
      end = index + 1
      height = heights[index]
    }
    if (page.length && used + height > budget) {
      pages.push(page)
      page = []
      used = runningHeader
    }
    page.push(...blocks.slice(index, end))
    used += height
    index = end
  }
  if (page.length || !pages.length) pages.push(page)
  return pages
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
    text?: string
    continued?: boolean
    height: number
  }>
}) {
  if (input.candidates.length === 0) return 0

  const chainEnd = keepGroupEnd(input.candidates, 0)
  if (chainEnd > 1) {
    const chain = input.candidates.slice(0, chainEnd)
    if (chain.some((candidate) => candidate.height <= 0)) return 0
    return canBackfillBlock({
      availableHeight: input.availableHeight,
      candidateHeight: chain.reduce((sum, candidate) => sum + candidate.height, 0)
    }) ? chainEnd : 0
  }

  // A lone closing paragraph needs only its measured height and the guard,
  // not the large-gap threshold used for ordinary page rebalancing.
  if (input.candidates.length === 1 && input.candidates[0].type === "paragraph") {
    const height = input.candidates[0].height
    return height > 0 && height + 12 <= input.availableHeight ? 1 : 0
  }

  // A closing reference section may fit in the previous page as one unit.
  // Never pull its heading alone or change the keep-with-next rule elsewhere.
  if (input.candidates.length === 2
    && input.candidates[0].type === "heading"
    && input.candidates[1].type === "paragraph") {
    return canBackfillBlock({
      availableHeight: input.availableHeight,
      candidateHeight: input.candidates[0].height + input.candidates[1].height
    }) ? 2 : 0
  }

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
>(pages: TPage[], canMoveChain: (pageIndex: number, start: number, end: number) => boolean = () => true): TPage[] {
  const nextPages = pages.map((page) => ({
    ...page,
    blocks: [...page.blocks]
  })) as TPage[]

  for (let index = 0; index < nextPages.length - 1; index += 1) {
    const page = nextPages[index]
    const nextPage = nextPages[index + 1]
    if (nextPage.chapter.path !== page.chapter.path) continue
    const combined = [...page.blocks, ...nextPage.blocks]
    const start = keepGroupStart(combined, page.blocks.length)
    const end = keepGroupEnd(combined, start)
    if (start > 0 && start < page.blocks.length && canMoveChain(index, start, end)) {
      nextPage.blocks.unshift(...page.blocks.splice(start))
    }
  }

  return nextPages
}
