from pathlib import Path
p=Path('artifacts/correzioni-collana-2026-10-02/sa03-batch06.py')
s=p.read_text(encoding='utf-8')
prefix=s[:s.index("source('dirigenza-")]
tail=s[s.index('common='):]
tail=tail.replace("pos=s.index('\\n## ',s.index('## Mappa BANDO')+4)","pos=s.index('\\n## ',s.index('\\n# '))")
exec(compile(prefix+tail,'sa03-batch06-resume','exec'))
