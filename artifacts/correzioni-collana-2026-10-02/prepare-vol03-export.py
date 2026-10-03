from pathlib import Path
p=Path('artifacts/correzioni-collana-2026-10-02')
s=(p/'export-vol02-tomo.mjs').read_text(encoding='utf8')
s=s.replace("const bookId='volumi/vol-02'","const bookId='volumi/vol-03'")
s=s.replace("const tomo=process.argv[2]||'tomo-1'","const tomo='current'")
s=s.replace('vol02-tomi/${tomo}-payload.json','vol03-proof/payload.json')
s=s.replace('vol-02-${tomo}','vol-03-${tomo}')
s=s.replace("2026-10-02/vol02-tomi'","2026-10-02/vol03-proof'")
(p/'export-vol03-proof.mjs').write_text(s,encoding='utf8')
