import { describe, expect, it } from "vitest"
import { backfillCandidateCount, keepGroupStart, moveTrailingHeadingToNextPage, paginateBlockGroups } from "@/src/book/pagination"

describe("Book Studio schema introductions", () => {
  const body = { type: "paragraph", text: "Testo precedente." }
  const heading = { type: "heading", text: "Schema 3.4" }
  const intro = { type: "paragraph", text: "Il metodo è ciclico: ogni errore può modificare il piano." }
  const table = { type: "table" }

  it("moves the heading and short introduction with their table", () => {
    const pages = [
      { chapter: { path: "a" }, blocks: [body, heading, intro] },
      { chapter: { path: "a" }, blocks: [table] }
    ]
    expect(moveTrailingHeadingToNextPage(pages)).toEqual([
      { chapter: { path: "a" }, blocks: [body] },
      { chapter: { path: "a" }, blocks: [heading, intro, table] }
    ])
  })

  it("never backfills an introduction without its table", () => {
    expect(backfillCandidateCount({ availableHeight: 190, candidates: [
      { ...intro, height: 35 }, { ...table, height: 190 }
    ] })).toBe(0)
  })

  it("backfills the complete title, two short introductions and list when they fit", () => {
    expect(backfillCandidateCount({ availableHeight: 290, candidates: [
      { ...heading, height: 30 }, { ...intro, height: 35 },
      { type: "paragraph", text: "Parti dalla condotta concreta e verifica ogni responsabilità.", height: 35 },
      { type: "list", height: 110 }
    ] })).toBe(4)
  })

  it("does not pull a schema across a chapter boundary", () => {
    const pages = [
      { chapter: { path: "a" }, blocks: [body, heading, intro] },
      { chapter: { path: "b" }, blocks: [table] }
    ]
    expect(moveTrailingHeadingToNextPage(pages)).toEqual(pages)
  })

  it("reserves the entire schema before a page break", () => {
    expect(paginateBlockGroups([body, heading, intro, table], [130, 30, 35, 120], 300, 20, 20))
      .toEqual([[body], [heading, intro, table]])
    expect(keepGroupStart([body, heading, intro, table], 3)).toBe(1)
  })

  it("keeps an example question and answer label with the following answer callout", () => {
    const question = { type: "paragraph", text: "Domanda: che cosa si intende per buon andamento?" }
    const label = { type: "paragraph", text: "Risposta ordinata:" }
    const answer = { type: "callout" }
    expect(paginateBlockGroups([body, heading, question, label, answer], [140, 30, 30, 20, 120], 300, 20, 20))
      .toEqual([[body], [heading, question, label, answer]])
  })

  it("allows an oversized chain to split without creating an empty page or overflowing a fitting block", () => {
    const blocks = [heading, intro, table]
    const heights = [30, 80, 240]
    const pages = paginateBlockGroups(blocks, heights, 300, 20, 20)
    expect(pages).toEqual([[heading, intro], [table]])
    expect(pages.flat()).toEqual(blocks)
    expect(moveTrailingHeadingToNextPage([
      { chapter: { path: "a" }, blocks: [body, heading, intro] },
      { chapter: { path: "a" }, blocks: [table] }
    ], () => false)[0].blocks).toEqual([body, heading, intro])
  })

  it("preserves continued fragments and index groups", () => {
    const continued = { type: "table", continued: true }
    expect(paginateBlockGroups([heading, intro, table, continued], [30, 30, 180, 80], 300, 20, 20))
      .toEqual([[heading, intro, table], [continued]])
    const part = { type: "index-part" }, chapter = { type: "index-chapter" }, row = { type: "index-row" }
    expect(paginateBlockGroups([body, part, chapter, row], [200, 30, 30, 30], 300, 20, 20))
      .toEqual([[body], [part, chapter, row]])
  })
})
