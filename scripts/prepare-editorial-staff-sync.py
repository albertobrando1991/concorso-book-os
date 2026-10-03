"""Inventory the editorial checkpoint without staging unrelated local work."""
from pathlib import Path
import collections
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'artifacts/correzioni-collana-2026-10-02/staff-sync'
OUT.mkdir(exist_ok=True)

def git_paths(*args):
    return set(filter(None, subprocess.check_output(['git', *args, '-z'], cwd=ROOT, stderr=subprocess.DEVNULL).decode('utf-8').split('\0')))

changed = git_paths('diff', '--name-only') | git_paths('diff', '--cached', '--name-only') | git_paths('ls-files', '--others', '--exclude-standard')
explicit = {
    '.gitattributes',
    'app/components/book-studio-panel.tsx', 'app/components/book-studio-preview-table.tsx',
    'app/globals.css', 'docs/PIPELINE.md', 'next.config.ts',
    'src/book/pagination.ts', 'src/catalog/text-volumes.ts',
    'src/pipeline/review/operational-data.ts', 'src/pipeline/state/run-state.ts',
    'src/server/book/book-preview.ts', 'src/server/wiki/markdown-table.ts',
    'scripts/audit-vol08-format2-nuclei.mjs', 'scripts/prepare-editorial-staff-sync.py',
    'scripts/verify-editorial-staff-sync.py', 'scripts/export-libreria-12-volumi.mjs',
    'tests/audit-vol08-format2-nuclei.test.ts', 'tests/book-studio-pagination-backfill.test.ts',
    'tests/book-studio-preview-table.test.ts', 'tests/book-preview-export-regressions.test.ts',
    'tests/book-studio-pagination-chains.test.ts', 'tests/pipeline/operational-data.test.ts',
    'tests/pipeline/reopen-command.test.ts', 'tests/pipeline/run-state.test.ts',
    'tests/pipeline/vol-07-hybrid-pilot.test.ts', 'tests/pipeline/vol-07-spec.test.ts',
    'tests/vol-07-visible-copy.test.ts', 'wiki/AGENTS.md', 'wiki/index.md', 'wiki/log.md',
    'docs/ALLINEAMENTO-STAFF-2026-10-03.md',
}
roots = ('wiki/books/', 'wiki/reviews/', 'wiki/sources/', 'wiki/topics/', 'wiki/entities/', 'pipeline/', 'delivery/')
artifact_roots = ('artifacts/correzioni-collana-2026-10-02/', 'artifacts/review-integrale-2026-10-02/', 'artifacts/review-collana-2026-10-02/')
text_suffixes = {'.md', '.json', '.csv', '.ts', '.mjs', '.cjs', '.py'}

def include(p):
    if p.startswith('artifacts/correzioni-collana-2026-10-02/staff-sync/'):
        return False
    if p in explicit or p.startswith(roots):
        return True
    if p.startswith(('wiki/raw/correzioni-', 'wiki/raw/integrazioni-nazionali-2026-10-02/')):
        return Path(p).suffix in {'.html', '.pdf', '.txt', '.json'}
    if p.startswith('artifacts/correzioni-collana-2026-10-02/digital-publication/'):
        return True
    return p.startswith(artifact_roots) and Path(p).suffix in text_suffixes and '__pycache__' not in p

selected = sorted(p for p in changed if include(p))
files = [{'path': p, 'bytes': (ROOT / p).stat().st_size if (ROOT / p).is_file() else 0} for p in selected]
report = {'files': files, 'count': len(files), 'bytes': sum(f['bytes'] for f in files),
          'groups': dict(collections.Counter(p.split('/')[0] for p in selected)),
          'excludedCount': len(changed - set(selected)),
          'policy': 'Editorial sources, official source captures, reports, current delivery and digital candidates; no study-plan feature, credentials, cookies, local caches or transient visual proof copies.'}
(OUT / 'selection.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(OUT / 'paths.nul').write_bytes(b'\0'.join(p.encode('utf-8') for p in selected) + b'\0')
print(json.dumps({k: v for k, v in report.items() if k != 'files'}, ensure_ascii=False))
print('Largest:', sorted(files, key=lambda f: f['bytes'], reverse=True)[:3])
