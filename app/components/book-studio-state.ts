interface ChapterPathItem {
  path: string
}

interface InitialChapterItem extends ChapterPathItem {
  isGenerated?: boolean
  status?: string
}

interface BookStudioPayloadLike {
  chapters: ReadonlyArray<ChapterPathItem>
}

interface BookStudioPayloadState<Data extends BookStudioPayloadLike> {
  data: Data
  selectedPath: string
}

interface BookStudioRefreshRequest {
  preferredPath?: string
}

export function getInitialBookStudioChapterPath(
  chapters: ReadonlyArray<InitialChapterItem>,
  requestedPath?: string
) {
  if (requestedPath && chapters.some((chapter) => chapter.path === requestedPath)) return requestedPath

  return (
    chapters.find((chapter) => !chapter.isGenerated && chapter.status !== "structure")?.path ||
    chapters.find((chapter) => !chapter.isGenerated)?.path ||
    chapters[0]?.path ||
    ""
  )
}

export function reconcileSelectedChapterPath(
  chapters: ReadonlyArray<ChapterPathItem>,
  currentPath: string,
  requestedPath?: string
) {
  if (requestedPath && chapters.some((chapter) => chapter.path === requestedPath)) return requestedPath
  if (chapters.some((chapter) => chapter.path === currentPath)) return currentPath

  return chapters[0]?.path || ""
}

export function reconcileBookStudioPayloadState<Data extends BookStudioPayloadLike>(
  currentState: BookStudioPayloadState<Data>,
  nextData: Data,
  requestedPath?: string
): BookStudioPayloadState<Data> {
  return {
    data: nextData,
    selectedPath: reconcileSelectedChapterPath(nextData.chapters, currentState.selectedPath, requestedPath)
  }
}

export function reconcileBookStudioRefreshPayloadState<Data extends BookStudioPayloadLike>(
  currentState: BookStudioPayloadState<Data>,
  nextData: Data,
  request: BookStudioRefreshRequest = {}
): BookStudioPayloadState<Data> {
  return reconcileBookStudioPayloadState(currentState, nextData, request.preferredPath)
}
