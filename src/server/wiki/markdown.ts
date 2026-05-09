export function replaceHeadingSection(content: string, heading: string, nextBody: string) {
  const normalized = content.replace(/\r\n/g, "\n")
  const lines = normalized.split("\n")
  const target = heading.trim().toLowerCase()
  const start = lines.findIndex((line) => {
    const match = /^(#{1,6})\s+(.+?)\s*$/.exec(line)
    return Boolean(match && match[2].trim().toLowerCase() === target)
  })

  if (start === -1) {
    return `${normalized.trim()}\n\n## ${heading}\n${nextBody.trim()}\n`
  }

  const level = getHeadingLevel(lines[start])
  let end = lines.length

  for (let index = start + 1; index < lines.length; index += 1) {
    const nextLevel = getHeadingLevel(lines[index])

    if (nextLevel > 0 && nextLevel <= level) {
      end = index
      break
    }
  }

  const replacement = [
    lines[start],
    "",
    ...nextBody.trim().split("\n"),
    ""
  ]

  return [...lines.slice(0, start), ...replacement, ...lines.slice(end)].join("\n").replace(/\n{4,}/g, "\n\n\n")
}

export function appendToHeadingSection(content: string, heading: string, addition: string) {
  const normalized = content.replace(/\r\n/g, "\n")
  const lines = normalized.split("\n")
  const target = heading.trim().toLowerCase()
  const start = lines.findIndex((line) => {
    const match = /^(#{1,6})\s+(.+?)\s*$/.exec(line)
    return Boolean(match && match[2].trim().toLowerCase() === target)
  })

  if (start === -1) {
    return `${normalized.trim()}\n\n## ${heading}\n${addition.trim()}\n`
  }

  const level = getHeadingLevel(lines[start])
  let end = lines.length

  for (let index = start + 1; index < lines.length; index += 1) {
    const nextLevel = getHeadingLevel(lines[index])

    if (nextLevel > 0 && nextLevel <= level) {
      end = index
      break
    }
  }

  const nextLines = [...lines]
  let insertAt = end

  while (insertAt > start + 1 && nextLines[insertAt - 1]?.trim() === "") {
    insertAt -= 1
  }

  nextLines.splice(insertAt, 0, "", addition.trim(), "")

  return nextLines.join("\n").replace(/\n{4,}/g, "\n\n\n")
}

export function extractWikiLinks(content: string) {
  const links = new Set<string>()
  const pattern = /\[\[([^\]|]+)(?:\|[^\]]+)?\]\]/g
  let match = pattern.exec(content)

  while (match) {
    links.add(match[1])
    match = pattern.exec(content)
  }

  return Array.from(links)
}

function getHeadingLevel(line: string) {
  const match = /^(#{1,6})\s+/.exec(line)
  return match ? match[1].length : 0
}
