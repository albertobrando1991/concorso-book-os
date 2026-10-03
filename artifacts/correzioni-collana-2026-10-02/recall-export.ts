import { LocalAgentMemory } from '../../src/server/memory/local-agent-memory'
async function main() {
  const result = await LocalAgentMemory.fromConfig().recall({query: 'correzioni export Book Studio PDF collana impaginazione KDP Garamond tabelle indice font preservare contenuti', maxResults: 10, maxTotalChars: 7000})
  console.log(result.context)
}
main()
