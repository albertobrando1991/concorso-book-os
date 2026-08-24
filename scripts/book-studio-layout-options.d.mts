export interface BookStudioLayoutCase {
  id: string
  label: string
}

export interface BookStudioLayoutOptions {
  cases: BookStudioLayoutCase[]
  artifactPrefix: string
  expectedCounts: Record<string, number> | null
}

export function resolveBookStudioLayoutOptions(
  env?: Record<string, string | undefined>
): BookStudioLayoutOptions

export interface BookPageCountReader {
  locator(selector: string): {
    count(): Promise<number>
  }
  waitForTimeout(milliseconds: number): Promise<void>
}

export interface StableBookPageCountOptions {
  selector?: string
  stableReadings?: number
  intervalMs?: number
  confirmationDelayMs?: number
  maxReadings?: number
}

export function waitForStableBookPageCount(
  page: BookPageCountReader,
  options?: StableBookPageCountOptions
): Promise<number>
