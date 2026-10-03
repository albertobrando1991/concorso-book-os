"""Verify exact audited bytes are present in Git's index before staff sync."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
A = ROOT / 'artifacts/correzioni-collana-2026-10-02'
load = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
index = {}
for entry in subprocess.check_output(['git', 'ls-files', '--stage', '-z'], cwd=ROOT).decode().split('\0'):
    if entry:
        metadata, name = entry.split('\t', 1)
        index[name] = metadata.split()[1]

expected = set()
for bundle_path in (A / 'digital-publication').glob('VOL-*/bundle.json'):
    data = load(bundle_path)
    expected.add(bundle_path.relative_to(ROOT).as_posix())
    expected.update(unit['sourcePath'] for unit in data['volume']['chapters'])
    expected.update((bundle_path.parent / asset['bundlePath']).relative_to(ROOT).as_posix() for asset in data['assets'])
for n in range(1, 13):
    package = ROOT / 'delivery' / f'VOL-{n:02}' / ('candidate-tomi-2026-10-03' if n == 2 else 'candidate-2026-10-03')
    manifest = next(p for p in (package / 'package-manifest.json', package / 'manifest.json') if p.exists())
    expected.add(manifest.relative_to(ROOT).as_posix())
    expected.update((package / f['path']).relative_to(ROOT).as_posix() for f in load(manifest)['files'])
inventory = load(A / 'registro-evidence-inventory.json')
expected.update(e['path'] for e in inventory['sources'])
expected.update([inventory['baselinePath'], inventory['auditPath']])

errors = []
for name in sorted(expected):
    if Path(name).is_absolute():
        name = Path(name).relative_to(ROOT).as_posix()
    raw = (ROOT / name).read_bytes()
    blob = hashlib.sha1(f'blob {len(raw)}\0'.encode() + raw).hexdigest()
    if index.get(name) != blob:
        errors.append({'path': name, 'error': 'not-staged' if name not in index else 'indexed-bytes-differ'})

staged = list(filter(None, subprocess.check_output(['git', 'diff', '--cached', '--name-only', '-z'], cwd=ROOT).decode().split('\0')))
suspicious = []
pattern = re.compile(rb'(?<![A-Za-z0-9_])(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{50,}|AKIA[A-Z0-9]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|sk-(?:proj-)?[A-Za-z0-9_-]{35,})')
for name in staged:
    path = ROOT / name
    if path.suffix.lower() in {'.pdf', '.png', '.jpg', '.jpeg', '.gif', '.webp'}:
        continue
    if path.is_file() and pattern.search(path.read_bytes()):
        suspicious.append(name)
result = {'indexedAuditedFiles': len(expected), 'errors': errors, 'stagedFiles': len(staged), 'credentialPatternFindings': suspicious}
(A / 'staff-sync/index-verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
print(json.dumps(result, ensure_ascii=False))
raise SystemExit(1 if errors or suspicious else 0)
