import { LocalAgentMemory } from '../../src/server/memory/local-agent-memory'

async function main() {
  const result = await LocalAgentMemory.fromConfig().captureConversation({
    scope: 'global', route: 'codex/editorial-staff-sync',
    messages: [{ role: 'user', content: 'Fai commit e push delle integrazioni e delle modifiche effettuate per allineare allo staff.' }],
    reply: 'Autorizzati commit e push delle modifiche editoriali già effettuate. Preparato branch codex/revisione-collana-2026-10-03 con testi, fonti ufficiali, rapporti, dodici pacchetti correnti, candidati digitali e correzioni agli strumenti editoriali. Attività study-plan separata ed esclusa. Nota staff docs/ALLINEAMENTO-STAFF-2026-10-03.md. Verifiche ripetute: typecheck,123 test mirati,2580 file dei dodici pacchetti,integrità348unità/251asset digitali,registro582rilievi con577verificati. La revisione digitale prosegue: letti R1–R11, osservazioni non ancora applicate salvo le tre correzioni R4/R11/R20 del controllo precedente; R12–R23 e verifica immagini/lettore ancora aperti. Note complete in artifacts/correzioni-collana-2026-10-02/ricettario-review/working-notes.md. Nessuna certificazione di pubblicabilità, promozione massiva degli stati o signoff24. Al momento di questa cattura commit e push sono in preparazione: verificarne esito effettivo sul remoto prima di dichiararli conclusi.',
    metadata: { branch: 'codex/revisione-collana-2026-10-03', publicationReady: false, testsPassed: 123, ricettarioTextRead: 11, commitPushAuthorized: true }
  })
  console.log(result.conversationId)
}
main().catch(error => { console.error(error); process.exitCode = 1 })
