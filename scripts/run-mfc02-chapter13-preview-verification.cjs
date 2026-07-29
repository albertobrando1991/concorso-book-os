const next = require("next")
const { spawn } = require("node:child_process")

const port = Number(process.env.BOOK_STUDIO_VERIFY_PORT || 3023)
const hostname = "127.0.0.1"

async function main() {
  const app = next({
    dev: true,
    hostname,
    port,
    dir: process.cwd(),
    conf: {
      distDir: ".next-verify-mfc02-chapter13"
    }
  })
  const handler = app.getRequestHandler()
  await app.prepare()

  const server = await new Promise((resolve, reject) => {
    const candidate = require("node:http").createServer((req, res) => handler(req, res))
    candidate.once("error", reject)
    candidate.listen(port, hostname, () => resolve(candidate))
  })

  try {
    await runNode("scripts/verify-mfc02-chapter13-images.cjs", {
      ...process.env,
      BOOK_STUDIO_URL: `http://${hostname}:${port}`
    })
  } finally {
    await new Promise((resolve) => server.close(resolve))
  }
}

function runNode(script, env) {
  return new Promise((resolve, reject) => {
    const child = spawn(process.execPath, [script], {
      stdio: "inherit",
      env
    })

    child.on("error", reject)
    child.on("exit", (code) => {
      if (code === 0) {
        resolve()
        return
      }

      reject(new Error(`${script} exited with code ${code}`))
    })
  })
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error)
    process.exit(1)
  })
