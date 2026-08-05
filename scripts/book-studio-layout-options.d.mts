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
