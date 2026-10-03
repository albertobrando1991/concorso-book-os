import { readFile } from 'node:fs/promises'
import { LocalAgentMemory } from '../../src/server/memory/local-agent-memory'

async function main() {
  const result = JSON.parse(await readFile('artifacts/review-integrale-2026-10-02/final-verification.json', 'utf8'))
  if (!result.textReviewComplete || result.chapters !== 326 || result.problems.length) {
    throw new Error('Revisione non ancora consolidata: nessuna memoria di completamento registrata')
  }
  const visual = JSON.parse(await readFile('artifacts/review-integrale-2026-10-02/visual-verification.json', 'utf8'))
  if (!visual.complete) throw new Error('Verifica visuale non consolidata')
  const captured = await LocalAgentMemory.fromConfig().captureConversation({
    scope: 'global',
    route: 'codex/revisione-integrale-collana',
    messages: [{role: 'user', content: 'Completa la revisione integrale dei volumi della collana. Individua errori e integrazioni necessari per correttezza ed esaustivita rispetto ai concorsisti; le correzioni si applicano successivamente.'}],
    reply: `Completata la revisione diagnostica dei 12 volumi cartacei: lettura integrale di 326 capitoli e appendici, quiz e casi; ${result.actions} voci di intervento (${result.contentActions} testuali, ${result.pdfAndExportActions} PDF/figure/export). Panorama di tutte le 4861 pagine dei 12 PDF selezionati con dettagli mirati; 308 immagini originali esaminate. Riscontro esterno normativo e fattuale selettivo, non certificazione di ogni claim. Dossier in wiki/reviews/audit-integrale-2026-10-02/README.md e registro-interventi.md/.csv. Tutti i volumi richiedono correzioni prima della pubblicazione. Nessuna correzione applicata da questo audit ai libri, PDF o pipeline. Il dossier supera lo stato parziale del precedente audit, conservato come storico. Ricettario digitale separato escluso. Preservate integrazioni di altri incarichi e relative esclusioni.`,
    metadata: {
      report: 'wiki/reviews/audit-integrale-2026-10-02/README.md',
      chapters: 326,
      actions: result.actions,
      fullTextReviewComplete: true,
      publicationReady: false,
      correctionsApplied: false,
      externalClaimCertification: false
    }
  })
  console.log(JSON.stringify({conversationId: captured.conversationId, atoms: captured.atoms.length}))
}
main().catch(error => { console.error(error); process.exitCode = 1 })
