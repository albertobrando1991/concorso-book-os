import { describe, expect, it } from "vitest"
import { TEXT_VOLUME_CATALOG } from "@/src/catalog/text-volumes"

describe("VOL-12 visible editorial copy", () => {
  it("uses reader-facing terminology in the catalog and title page", () => {
    const volume = TEXT_VOLUME_CATALOG.find((item) => item.code === "VOL-12")

    expect(volume?.audience).toContain("Avvocatura dello Stato")
    expect(volume?.audience).not.toContain("avvocatura erariale")
    expect(volume?.promise).toBe("Metodo e strategia per selezioni ad alta barriera.")
    expect(volume?.promise).not.toMatch(/pricing|pacchetto/i)
  })
})
