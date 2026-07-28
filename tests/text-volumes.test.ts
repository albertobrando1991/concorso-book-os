import { describe, expect, it } from "vitest"
import {
  TEXT_CATALOG_MODULE_COUNT,
  TEXT_VOLUME_CATALOG,
  bookIdsForTextVolumeBookId,
  isTextVolumeBookId,
  normalizeTextBookId,
  textVolumeBookId
} from "../src/catalog/text-volumes"

describe("commercial text volumes", () => {
  it("keeps VOL-03 aligned with the canonical central-functions architecture", () => {
    const volume = TEXT_VOLUME_CATALOG.find((item) => item.code === "VOL-03")

    expect(volume?.title).toBe("Funzioni centrali, Fisco, Previdenza e Ispettivo")
    expect(volume?.shortTitle).toBe("Funzioni centrali e fisco")
    expect(volume?.modules).toEqual(["M-FC01", "M-FC02", "M-FC03"])
    expect(volume?.bookIds).toEqual([
      "moduli/m-fc01-ministeri",
      "moduli/m-fc02-agenzie-fiscali",
      "moduli/m-fc03-enti-non-economici"
    ])
  })

  it("keeps the commercial catalog at 12 volumes and 25 unique specialist modules", () => {
    const modules = TEXT_VOLUME_CATALOG.flatMap((volume) => volume.modules)
    const bookIds = TEXT_VOLUME_CATALOG.flatMap((volume) => volume.bookIds)

    expect(TEXT_VOLUME_CATALOG).toHaveLength(12)
    expect(TEXT_CATALOG_MODULE_COUNT).toBe(25)
    expect(new Set(modules).size).toBe(25)
    expect(new Set(bookIds).size).toBe(bookIds.length)
    expect(
      TEXT_VOLUME_CATALOG.every(
        (volume) => volume.modules.length === 0 || volume.modules.length === volume.bookIds.length
      )
    ).toBe(true)
  })

  it("keeps the base manual outside the specialist volume aggregator", () => {
    const baseVolume = TEXT_VOLUME_CATALOG.find((volume) => volume.code === "VOL-01")
    const specialistVolume = TEXT_VOLUME_CATALOG.find((volume) => volume.code === "VOL-02")

    expect(baseVolume).toBeDefined()
    expect(specialistVolume).toBeDefined()
    expect(normalizeTextBookId("vol-01")).toBe("il-metodo-bando")
    expect(normalizeTextBookId("volumi/vol-01")).toBe("il-metodo-bando")
    expect(isTextVolumeBookId("volumi/vol-01")).toBe(false)
    expect(textVolumeBookId(baseVolume!)).toBe("il-metodo-bando")
    expect(bookIdsForTextVolumeBookId("volumi/vol-01")).toEqual([])
    expect(normalizeTextBookId("vol-02")).toBe("volumi/vol-02")
    expect(isTextVolumeBookId("volumi/vol-02")).toBe(true)
    expect(textVolumeBookId(specialistVolume!)).toBe("volumi/vol-02")
  })
})
