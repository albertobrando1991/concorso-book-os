export function slugify(input: string) {
  return input
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
}

export function createId(prefix: string, title: string) {
  const slug = slugify(title)
  return `${prefix}-${slug}`
}

export function wikiLink(title: string, label = title) {
  const slug = slugify(title)
  return `[[${slug}|${label}]]`
}

