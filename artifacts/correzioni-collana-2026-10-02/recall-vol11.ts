import { LocalAgentMemory } from '../../src/server/memory/local-agent-memory'
async function main() {
 const result = await LocalAgentMemory.fromConfig().recall({query: 'VOL-11 ambiente protezione civile sostenibilità energia rifiuti VIA AIA AUA acque CAM DNSH correzione editoriale copertura fonti pipeline', maxResults: 10, maxTotalChars: 7000})
 console.log(result.context)
}
main()
