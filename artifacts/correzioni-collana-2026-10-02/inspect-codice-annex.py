from pathlib import Path
import re,json
t=Path('wiki/raw/correzioni-collana-2026-10-02/codice36-art63-20261003.html').read_text(encoding='utf8')
parts=re.split(r'<span>(Allegato [^<]+)</span>',t);out=[]
for i in range(1,len(parts)-1,2):
 if parts[i] not in ['Allegato I.2','Allegato I.5','Allegato II.4','Allegato II.14']:continue
 for x in re.findall(r"showArticle\('([^']+)",parts[i+1]):out.append({'annex':parts[i],'url':'https://www.normattiva.it'+x})
Path(__file__).with_name('codice-annex-links.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
