from pathlib import Path
p=Path('app/components/book-studio-panel.tsx');s=p.read_text(encoding='utf8')
start=s.index('  const pages: Array<Omit<PreviewPage, "pageNumber">> = []',s.index('function paginateBlocksByHeight('))
end=s.index('\nfunction paginateBlocks(chapter:',start)
s=s[:start]+'''  return paginateBlockGroups(
    chapter.blocks,
    chapter.blocks.map((block, index) => blockHeights[index] || estimateBlockCost(block)),
    pageBudget, firstHeaderHeight, runningHeaderHeight
  ).map((blocks, index) => ({ chapter, blocks, chapterPageNumber: index + 1, isFirstPage: index === 0 }))
}
''' +s[end:]
start=s.index('  const pages: Array<Omit<PreviewPage, "pageNumber">> = []',s.index('function paginateBlocks(chapter:'))
end=s.index('\nfunction isSinglePageFrontMatter(',start)
s=s[:start]+'''  const frontMatter = chapter.sectionType === "front_matter"
  return paginateBlockGroups(
    chapter.blocks,
    chapter.blocks.map((block) => estimateBlockCost(block) + layoutSafetyCost(block)),
    frontMatter ? FRONT_MATTER_PAGE_BUDGET : MAIN_PAGE_FALLBACK_BUDGET,
    frontMatter ? FRONT_MATTER_FIRST_PAGE_COST : FIRST_PAGE_HEADER_COST,
    frontMatter ? FRONT_MATTER_RUNNING_PAGE_COST : RUNNING_HEADER_COST
  ).map((blocks, index) => ({ chapter, blocks, chapterPageNumber: index + 1, isFirstPage: index === 0 }))
}
''' +s[end:]
start=s.index('function shouldKeepWithNext(');end=s.index('function estimateBlockCost(',start)
s=s[:start]+s[end:];p.write_text(s,encoding='utf8')
