const http = require("node:http")
const { spawn } = require("node:child_process")
const next = require("next")

const HOST = "127.0.0.1"
const PORT = Number(process.env.BOOK_STUDIO_VERIFY_PORT || 3012)
const DIST_DIR = ".next-verify-mfc02"

async function main() {
  const app = next({
    dev: true,
    dir: process.cwd(),
    hostname: HOST,
    port: PORT,
    conf: {
      distDir: DIST_DIR
    }
  })
  const handle = app.getRequestHandler()

  await app.prepare()

  const server = http.createServer((request, response) => handle(request, response))

  await new Promise((resolve, reject) => {
    server.once("error", reject)
    server.listen(PORT, HOST, resolve)
  })

  try {
    await runVerifier()
  } finally {
    await new Promise((resolve) => server.close(resolve))
  }
}

function runVerifier() {
  return new Promise((resolve, reject) => {
    const child = spawn(
      process.execPath,
      ["scripts/verify-mfc02-chapter02-images.cjs"],
      {
        cwd: process.cwd(),
        env: {
          ...process.env,
          BOOK_STUDIO_URL: `http://${HOST}:${PORT}`
        },
        stdio: "inherit"
      }
    )

    child.on("error", reject)
    child.on("exit", (code) => {
      if (code === 0) {
        resolve()
      } else {
        reject(new Error(`Verifier terminato con codice ${code}`))
      }
    })
  })
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error)
    process.exit(1)
  })
