import { LocalAgentMemory } from '../../src/server/memory/local-agent-memory'
async function main() {
  const result = await LocalAgentMemory.fromConfig().recall({query: 'revisione collana correttezza esaustivita concorsisti pubblicazione solo segnalazioni contenuti volumi', maxResults: 12, maxTotalChars: 8500})
  console.log(result.context)
}
main()
