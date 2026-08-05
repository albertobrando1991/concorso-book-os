export type AuditSeverity = "bloccante" | "media" | "lieve" | "nessuna"
export type AuditOutcome = "aperto" | "conforme" | "risolto - ricontrollato"

export interface PageAuditOptions {
  baseUrl: string
  bookId: string
  artifactPrefix: string
  reportPath: string
  expectedPageCount: number
  contactSheetSize: number
  reportMode: "write" | "verify"
  explicitScreenshotPages: number[]
}

export interface ContactSheetRange {
  index: number
  start: number
  end: number
  pages: number[]
}

export interface PageBlockDiagnostic {
  type: string
  continued: boolean
  lines: number
}

export interface TableDiagnostic {
  label: string
  continued: boolean
  hasHeader: boolean
  contained: boolean
}

export interface ImageDiagnostic {
  label: string
  loaded: boolean
  contained: boolean
  hasCaption: boolean
}

export interface PageDiagnostic {
  page: number
  domIndex: number
  printedNumber: number
  title: string
  chapterPath: string
  sectionType: string
  frontMatterLayout: string
  side: "recto" | "verso"
  width: number
  height: number
  paddingTop: number
  paddingRight: number
  paddingBottom: number
  paddingLeft: number
  freeSpace: number
  fillRatio: number
  overflow: number
  collisions: string[]
  firstBlock?: PageBlockDiagnostic
  lastBlock?: PageBlockDiagnostic
  tables: TableDiagnostic[]
  images: ImageDiagnostic[]
  rawMarkdown: string[]
  typographyFailures: string[]
  headingFailures: string[]
  unjustifiedProse: string[]
  consecutiveImages: boolean
  detachedBlocks: string[]
  isSectionTerminal: boolean
}

export interface PageAuditContext {
  pageCount: number
  medianFreeSpace: number
  expectedWidth: number
  expectedHeight: number
}

export interface PageAuditIssue {
  page: number
  problemType: string
  element: string
  severity: AuditSeverity
  correction: string
  outcome: AuditOutcome
}

export interface PageRegistryRow extends PageAuditIssue {}

export interface PageAuditReportInput {
  generatedAt: string
  bookId: string
  diagnostics: PageDiagnostic[]
  issues: PageAuditIssue[]
}

export function resolvePageAuditOptions(env?: Record<string, string | undefined>): PageAuditOptions
export function buildContactSheetRanges(pageCount: number, sheetSize?: number): ContactSheetRange[]
export function flaggedPageNumbers(
  issues: Array<{ page: number }>,
  explicitPages?: number[]
): number[]
export function classifyPageDiagnostic(
  page: PageDiagnostic,
  context: PageAuditContext
): PageAuditIssue[]
export function buildPageRegistryRows(
  diagnostics: PageDiagnostic[],
  issues: PageAuditIssue[]
): PageRegistryRow[]
export function renderPageAuditMarkdown(input: PageAuditReportInput): string
export function validatePageAuditMarkdown(markdown: string, expectedPageCount: number): string[]
