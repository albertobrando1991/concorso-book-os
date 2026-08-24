import fs from "node:fs/promises"
import path from "node:path"
import sharp from "sharp"

const source = path.resolve("wiki/books/moduli/m-fc05-authority-indipendenti/assets")
const output = path.resolve("artifacts/VOL-05/image-audit")
const groups = [[1, 5], [6, 10], [11, 15]]
const cellWidth = 320
const cellHeight = 230
const thumbWidth = 288
const thumbHeight = 180

await fs.mkdir(output, { recursive: true })

for (const [start, end] of groups) {
  const composites = []
  let index = 0
  for (let chapter = start; chapter <= end; chapter += 1) {
    const code = String(chapter).padStart(2, "0")
    const directory = path.join(source, `chapter-${code}`)
    const files = (await fs.readdir(directory)).filter((file) => file.endsWith(".png")).sort()
    for (const file of files) {
      const column = index % 5
      const row = Math.floor(index / 5)
      const image = await sharp(path.join(directory, file)).resize(thumbWidth, thumbHeight).png().toBuffer()
      composites.push({ input: image, left: column * cellWidth + 16, top: row * cellHeight + 34 })
      const label = `C${code} · ${file.slice(0, 2)}`
      composites.push({
        input: Buffer.from(`<svg width="${cellWidth}" height="30"><rect width="100%" height="100%" fill="#10233F"/><text x="16" y="21" font-family="Arial" font-size="16" font-weight="700" fill="#FFFFFF">${label}</text></svg>`),
        left: column * cellWidth,
        top: row * cellHeight
      })
      index += 1
    }
  }
  const name = `contact-sheet-${String(start).padStart(2, "0")}-${String(end).padStart(2, "0")}.png`
  await sharp({ create: { width: 1600, height: 1150, channels: 3, background: "#E2E8F0" } })
    .composite(composites)
    .png()
    .toFile(path.join(output, name))
  console.log(path.join(output, name))
}
