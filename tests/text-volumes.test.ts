import { describe, expect, it } from "vitest"
import {
  TEXT_VOLUME_CATALOG,
  bookIdsForTextVolumeBookId,
  isTextVolumeBookId,
  normalizeTextBookId,
  textVolumeBookId
} from "../src/catalog/text-volumes"

describe("commercial text volumes", () => {
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
