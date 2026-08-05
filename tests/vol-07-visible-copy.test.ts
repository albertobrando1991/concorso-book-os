import { readFile } from "node:fs/promises"
import path from "node:path"
import { describe, expect, it } from "vitest"
import { TEXT_VOLUME_CATALOG } from "@/src/catalog/text-volumes"
import { buildBookStudioData } from "@/src/server/book/book-preview"
import { FileWikiStore } from "@/src/server/wiki/file-store"
import { parseFrontmatter } from "@/src/server/wiki/frontmatter"

const wikiRoot = path.resolve(process.cwd(), "wiki")
const moduleIds = [
  "m-sa01-sanita-amministrativa",
  "m-sa02-professioni-sanitarie",
  "m-sa03-dirigenza-medica-sanitaria",
  "m-sa04-tecnici-sanitari-prevenzione"
]

describe("VOL-07 visible editorial copy", () => {
  it("uses the canonical accented volume and module labels", async () => {
    const volume = TEXT_VOLUME_CATALOG.find((item) => item.code === "VOL-07")

    expect(volume?.title).toBe("Sanità amministrativa e professioni sanitarie")
    expect(volume?.shortTitle).toBe("Sanità")

    for (const moduleId of moduleIds) {
      for (const relativePath of ["index.md", "planning/00-piano-editoriale.md"]) {
        const content = await readFile(path.join(wikiRoot, "books", "moduli", moduleId, relativePath), "utf8")
        const parsed = parseFrontmatter(content)
        const visibleBody = parsed.body
          .replace(/\[\[([^|\]]+)\|([^\]]+)\]\]/g, "$2")
          .replace(/\[\[[^\]]+\]\]/g, "")
        const visibleLabels = [
          parsed.data.title,
          parsed.data.module_family_title,
          ...visibleBody.split("\n").filter((line) => /^(#|[-*] Famiglia:)/.test(line))
        ].filter(Boolean).join("\n")

        expect(visibleLabels, `${moduleId}/${relativePath}`).not.toMatch(/\bSanita\b/)
        expect(visibleLabels, `${moduleId}/${relativePath}`).not.toMatch(/Ã|Â|�/)
        expect(visibleBody, `${moduleId}/${relativePath}`).not.toMatch(
          /\b(?:priorita|qualita|responsabilita|contabilita|accessibilita|gia)\b/i
        )
      }
    }
  })

  it("renders only canonical reader chapters with consistent numbering", async () => {
    const chapter03Path = path.join(
      wikiRoot,
      "books/moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md"
    )
    const chapter03 = parseFrontmatter(await readFile(chapter03Path, "utf8"))

    expect(chapter03.data.outline_section).toBe(3)
    expect(chapter03.data.title).toBe("Discipline professionali: autonomia, responsabilità e deontologia")

    const preview = await buildBookStudioData(
      new FileWikiStore(wikiRoot),
      "volumi/vol-07"
    )
    const readerChapters = preview.chapters.filter((chapter) => !chapter.isGenerated)

    expect(preview.title).toBe("VOL-07 — Sanità amministrativa e professioni sanitarie")
    expect(readerChapters.map((chapter) => [chapter.outlineSection, chapter.title])).toEqual([
      ["1", "Atti, procedimenti e flussi informativi nelle aziende sanitarie"],
      ["2", "Documentazione sanitaria, accesso, privacy e conservazione"],
      ["3", "Front-office e comunicazione con l'utenza sanitaria"],
      ["4", "Contabilità, budget e controllo di gestione nelle aziende sanitarie"],
      ["5", "Procurement sanitario, farmaci, dispositivi e magazzino"],
      ["6", "Professioni sanitarie: profili, requisiti e prove"],
      ["7", "Discipline professionali: autonomia, responsabilità e deontologia"],
      ["8", "Assistenza infermieristica, tecniche assistenziali e supporto OSS"],
      ["9", "Valutazione clinica, triage, urgenza ed emergenza"],
      ["10", "Prevenzione, continuità assistenziale e presa in carico"],
      ["11", "Evidenze scientifiche, PICO, GRADE e applicabilità"],
      ["12", "Igiene pubblica, epidemiologia, sorveglianza e screening"],
      ["13", "Controlli TPALL, verbalizzazione, campionamento e sanzioni"],
      ["14", "Prova pratica e casi professionali"],
      ["15", "Profili, requisiti e prove della dirigenza sanitaria"],
      ["16", "Programmazione sanitaria e organizzazione dei servizi"],
      ["17", "Linee guida, appropriatezza e decisioni cliniche"],
      ["18", "Governo clinico, HTA, qualità, accreditamento e rischio"],
      ["19", "Epidemiologia e sanità pubblica per la dirigenza"],
      ["20", "Dirigenza medica: discipline e casi"],
      ["21", "Dirigenza sanitaria non medica: discipline e casi"],
      ["22", "TSLB e TSRM: profili, requisiti, prove e responsabilità"],
      ["23", "TSLB: processo di laboratorio, qualità e biosicurezza"],
      ["24", "TSRM: imaging, dosimetria e radioprotezione"],
      ["25", "Tecnologie, dispositivi, apparecchiature e rischio tecnologico"]
    ])
    expect(readerChapters).toHaveLength(25)
    expect(readerChapters.map((chapter) => chapter.outlineSection)).toEqual(
      Array.from({ length: 25 }, (_, index) => String(index + 1))
    )
    expect(readerChapters.map((chapter) => chapter.moduleOutlineSection)).toEqual([
      "4", "5", "6", "9", "10",
      "1", "3", "4", "5", "6", "7", "8", "9", "10",
      "1", "2", "3", "4", "5", "6", "7",
      "1", "2", "3", "4"
    ])
    expect(new Set(readerChapters.map((chapter) => chapter.path)).size).toBe(25)
    expect(readerChapters.every((chapter) => chapter.blocks.length > 0)).toBe(true)
    expect(readerChapters.some((chapter) => /piano editoriale/i.test(chapter.title))).toBe(false)

    const visibleCopy = readerChapters.flatMap((chapter) => [
      chapter.title,
      ...chapter.blocks.map((block) => JSON.stringify(block))
    ]).join("\n")

    expect(visibleCopy).not.toMatch(
      /\b(?:fonti consolidate|source notes?|corpus interno|dashboard|prompt|report di revisione|pacchetto interno)\b/i
    )
    expect(visibleCopy).not.toMatch(/Ãƒ|Ã‚|ï¿½/)
  })
})
