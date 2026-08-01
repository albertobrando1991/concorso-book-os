import type { VolumeSpecHumanReview } from "../spec/parse-volume-spec"
import type { GateResult } from "../state/types"

export interface HumanReviewAssignmentGateInput {
  reviews: VolumeSpecHumanReview[]
  specPath: string
}

export function runHumanReviewAssignmentGate(input: HumanReviewAssignmentGateInput): GateResult {
  const blockers = input.reviews
    .filter((review) => review.required && !review.reviewer.trim())
    .map((review) => ({
      code: "review-non-assegnata",
      message: `La review ${review.code || review.scope} è richiesta ma non ha un nome assegnato.`,
      location: `${input.specPath}:${review.line}`
    }))

  if (!input.reviews.length) {
    blockers.push({
      code: "review-non-assegnata",
      message: "La scheda non contiene la tabella Review umane — nomi, costi, tempi.",
      location: input.specPath
    })
  }

  return { passed: blockers.length === 0, blockers, warnings: [] }
}
