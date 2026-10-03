from pathlib import Path
import re,collections
for name in ['civile-codice-art822-urn','i7-art31-urn','ii14-art7-urn']:
 s=Path('wiki/raw/correzioni-vol10-2026-10-03/'+name+'.html').read_text(encoding='utf8')
 print(name,collections.Counter(re.findall(r'class="([^"]*art[^"]*)"',s)))
 print(re.findall(r'<title>(.*?)</title>',s,re.S))
 print('pre blocks',len(re.findall(r'<pre',s)))
 print(s[max(0,s.find('tredici')-150):s.find('tredici')+250])
for name in ['I.7','I.9','II.14']:
 s=Path('wiki/raw/correzioni-collana-2026-10-02/ii14-art28-20261003.html').read_text(encoding='utf8')
 i=s.find('>'+name+'</span>')
 if i<0:i=s.find('>Allegato '+name+'</span>')
 print(name,s[i:i+500])
