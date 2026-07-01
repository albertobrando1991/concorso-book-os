export function ricettarioModuleLabel(outlineSection: string) {
  const number = Number.parseInt(outlineSection, 10)

  if (!Number.isFinite(number) || number < 25) return ""

  return `R${number - 24}`
}