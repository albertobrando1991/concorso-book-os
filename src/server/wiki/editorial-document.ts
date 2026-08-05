export function isLegacyEditorialPlanPath(value: string) {
  return /\/chapters\/00-piano-editoriale\.md$/i.test(value.replace(/\\/g, "/"))
}

export function isStaffOnlyBookDocument(
  value: string,
  data: Record<string, unknown> = {}
) {
  const type = String(data.type ?? "").toLowerCase()
  const tags = Array.isArray(data.tags) ? data.tags.map((tag) => String(tag).toLowerCase()) : []
  const normalizedPath = value.replace(/\\/g, "/")

  return (
    normalizedPath.includes("/planning/") ||
    isLegacyEditorialPlanPath(normalizedPath) ||
    type === "editorial_plan" ||
    type === "module_plan" ||
    tags.includes("specialist-module-plan")
  )
}
