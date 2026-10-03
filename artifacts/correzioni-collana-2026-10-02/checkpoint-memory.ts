import { LocalAgentMemory } from '../../src/server/memory/local-agent-memory'
async function main() {
 const result = await LocalAgentMemory.fromConfig().captureConversation({
  scope:'global',route:'codex/applicazione-correzioni-collana',
  messages:[{role:'user',content:'Ora procedi a tutte le modifiche e integrazioni portando i volumi a pubblicabili.'}],
  reply:'Autorizzata e avviata applicazione integrale dei 582 rilievi sui 12 volumi. Snapshot iniziale di 326 manoscritti conservato. Registri in wiki/reviews/correzioni-collana-2026-10-02 e artifacts/correzioni-collana-2026-10-02. Pipeline step14 riaperto con cascade via CLI nei volumi lavorati; nessuno stato scritto a mano. Root VOL01/09/10/11 e coordinamento; review_vol02 VOL02/04/05; review_vol03 renderer poi VOL03/08; review_vol06 VOL07/06/12. Correzioni in corso, non ancora verificate come pubblicabili. Preservare precedenti INT e lavoro non pertinente. Autorizzate tutte correzioni locali, integrazioni e rigenerazioni, non pubblicazione esterna. Conferma umana solo step24 sul pacchetto finito. Domanda pendente su effettiva operatività del mese digitale gratuito prima di confermare la promessa stampata.',
  metadata:{publicationReady:false,correctionsInProgress:true,register:'artifacts/correzioni-collana-2026-10-02/registro-applicazione.json'}
 });console.log(JSON.stringify({conversationId:result.conversationId,atoms:result.atoms.length}))
}
main().catch(e=>{console.error(e);process.exitCode=1})
