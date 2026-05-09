import { spawn } from "node:child_process"
import fs from "node:fs/promises"
import { chromium } from "@playwright/test"

const port = process.env.PORT || "3000"
const url = `http://127.0.0.1:${port}`
const screenshotPath = "artifacts/dashboard-screenshot.png"
const notePath = "artifacts/screenshot-ui.md"

await fs.mkdir("artifacts", { recursive: true })

const server = spawn(process.execPath, ["node_modules/next/dist/bin/next", "dev", "-p", port], {
  stdio: "ignore",
  env: {
    ...process.env,
    NEXT_TELEMETRY_DISABLED: "1"
  }
})

try {
  await waitFor(url)
  const browser = await launchBrowser()
  const page = await browser.newPage({ viewport: { width: 1440, height: 980 } })
  await page.goto(url, { waitUntil: "networkidle" })
  await page.screenshot({ path: screenshotPath, fullPage: true })
  await browser.close()
  await fs.writeFile(
    notePath,
    `# UI screenshot

- File: \`${screenshotPath}\`
- URL: \`${url}\`
- Captured: ${new Date().toISOString()}
`,
    "utf8"
  )
} catch (error) {
  await fs.writeFile(
    notePath,
    `# UI screenshot

Screenshot capture failed.

- URL: \`${url}\`
- Captured: ${new Date().toISOString()}
- Error: ${error instanceof Error ? error.message : String(error)}
`,
    "utf8"
  )
  process.exitCode = 1
} finally {
  server.kill()
}

async function waitFor(targetUrl) {
  const started = Date.now()

  while (Date.now() - started < 30000) {
    try {
      const response = await fetch(targetUrl)

      if (response.ok) return
    } catch {
      await new Promise((resolve) => setTimeout(resolve, 750))
    }
  }

  throw new Error(`Timed out waiting for ${targetUrl}`)
}

async function launchBrowser() {
  try {
    return await chromium.launch({ channel: "msedge" })
  } catch {
    try {
      return await chromium.launch({ channel: "chrome" })
    } catch {
      return chromium.launch()
    }
  }
}
