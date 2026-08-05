import React from "react"
import type {
  BookStudioEditorialPlan,
  EditorialTargetState
} from "@/src/server/book/editorial-plan"

export function EditorialPlanPanel({ plan }: { plan: BookStudioEditorialPlan }) {
  return (
    <section className="editorialPlanPanel" aria-label="Piano editoriale staff">
      <div className="editorialPlanHeading">
        <span>Piano editoriale staff</span>
        <small>Non incluso nell'anteprima del libro</small>
      </div>
      {plan.modules.map((module) => (
        <details className="editorialPlanModule" key={module.code} open>
          <summary>{formatCodedTitle(module.code, module.title)}</summary>
          {module.targets.length ? (
            module.targets.map((target) => (
              <div className={`editorialPlanTarget state-${target.state}`} key={target.path}>
                <span>{formatChapterLabel(target.number, target.title)}</span>
                <small>
                  {editorialTargetStateLabel(target.state)}
                  {target.nextStep ? ` · prossimo step ${target.nextStep}` : ""}
                </small>
              </div>
            ))
          ) : (
            <p>Capitoli non ancora dichiarati nella pipeline.</p>
          )}
        </details>
      ))}
    </section>
  )
}

export function formatChapterLabel(number: string, title: string) {
  const parsed = Number.parseInt(number, 10)
  const label = Number.isFinite(parsed) ? String(parsed).padStart(2, "0") : number.trim()

  return `Capitolo ${label} — ${title}`
}

export function formatCodedTitle(code: string, title: string) {
  const cleanTitle = title.replace(/^M-[A-Z]{2}\d{2}\s*[-–—]?\s*/i, "").trim()

  return `${code} — ${cleanTitle || code}`
}

export function editorialTargetStateLabel(state: EditorialTargetState) {
  if (state === "to-plan") return "Da pianificare"
  if (state === "to-write") return "Da scrivere"
  if (state === "in-progress") return "In lavorazione"
  if (state === "written") return "Scritto"
  if (state === "in-review") return "In revisione"
  if (state === "complete") return "Completato"

  return "Bloccato"
}
