from pathlib import Path
import re
p=Path('wiki/books/moduli/m-sp01-forze-ordine/chapters/08-piano-30-60-90-doppio-binario.md'); t=p.read_text(encoding='utf-8').replace('sp 01','sp01')
t=re.sub(r'https://[^)\n]+',lambda m:m.group(0).replace(' ',''),t)
p.write_text(t,encoding='utf-8')
