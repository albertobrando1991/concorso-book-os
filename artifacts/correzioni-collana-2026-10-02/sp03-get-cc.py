from pathlib import Path
import re,subprocess,html,requests
B=Path('wiki/raw/correzioni-collana-2026-10-02')
t=(B/'cc-art1337-20261003.html').read_text(encoding='utf8')
session=requests.Session()
session.get('https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262',timeout=30)
for n in [1337,1338,1022,588,536,602,603]:
 matches=re.findall(r"showArticle\('([^']+)'",t)
 u=next(u for u in matches if f'art.idArticolo={n}&' in u and 'art.idSottoArticolo=1&' in u)
 url='https://www.normattiva.it'+html.unescape(u)
 p=B/f'cc-art{n}-testo-20261003.html'
 response=session.get(url,timeout=30);response.raise_for_status();p.write_bytes(response.content)
 s=p.read_text(encoding='utf8');clean=html.unescape(re.sub('<[^>]+>',' ',s));clean=re.sub(r'\s+',' ',clean)
 print(n,clean[-10000:])
