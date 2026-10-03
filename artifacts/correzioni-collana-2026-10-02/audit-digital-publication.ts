import { mkdir, writeFile } from 'node:fs/promises'
import { execFileSync } from 'node:child_process'
import path from 'node:path'
import { buildBookIntegrationBundle, writeBookIntegrationBundle } from '../../src/server/book/book-integration-bundle'

async function main() {
  const root = process.cwd()
  const output = path.join(root, 'artifacts/correzioni-collana-2026-10-02/digital-publication')
  await mkdir(output, { recursive: true })
  const commit = execFileSync('git', ['rev-parse', 'HEAD'], { encoding: 'utf8' }).trim()
  const dirty = Boolean(execFileSync('git', ['status', '--porcelain', '--untracked-files=no'], { encoding: 'utf8' }).trim())
  const results = []
  for (let n = 1; n <= 12; n++) {
    const volumeCode = `VOL-${String(n).padStart(2, '0')}`
    try {
      const bundle = await buildBookIntegrationBundle({ projectRoot: root, volumeCode, channel: 'candidate', sourceSha: commit })
      await writeBookIntegrationBundle(root, path.join(output, volumeCode), bundle)
      const units = [...bundle.volume.frontMatter, ...bundle.volume.chapters]
      const result = {
        volume: volumeCode, contentDigest: bundle.contentDigest,
        counts: bundle.volume.counts, assets: bundle.assets.length,
        gate: bundle.gate,
        units: units.map(u => ({ id: u.id, sourcePath: u.sourcePath, sourceHash: u.sourceHash, contentHash: u.contentHash, scope: u.scope, sectionType: u.sectionType, reviewRequired: u.reviewRequired, contentState: u.contentState, status: u.status, draftStage: u.draftStage })),
        serviceClaims: units.filter(u => /servizi digitali inclusi|mese gratuito|un mese gratis/i.test(JSON.stringify(u.blocks))).map(u => ({id:u.id, sourcePath:u.sourcePath, title:u.title}))
      }
      results.push(result)
      console.log(JSON.stringify({ volume: volumeCode, counts: result.counts, assets: result.assets, blockers: bundle.gate.blockers.map(b=>({code:b.code,count:b.count})), serviceClaims: result.serviceClaims }))
    } catch (error) {
      const result = { volume: volumeCode, error: error instanceof Error ? error.message : String(error) }
      results.push(result); console.log(JSON.stringify(result))
    }
  }
  await writeFile(path.join(output, 'audit.json'), JSON.stringify({ checkedAt:new Date().toISOString(), sourceCommit:commit, workingTreeDirty:dirty, provenance:'Local working-tree candidates, not a clean commit or approved release. Per-unit source/content hashes identify actual input.', results },null,2)+'\n')
}
main().catch(e=>{console.error(e);process.exitCode=1})
