from pathlib import Path
from html.parser import HTMLParser
import sys
class Extract(HTMLParser):
 def __init__(self):super().__init__();self.level=0;self.text=[]
 def handle_starttag(self,tag,attrs):
  if tag in ['br','img','input','hr','meta','link']:return
  if self.level:self.level+=1
  elif any(k=='class' and any(c in v for c in ['bodyTesto','attachment-just-text','art_text_in_comma','ins-akn','pointedList']) for k,v in attrs):self.level=1
 def handle_endtag(self,tag):
  if self.level:self.level-=1
 def handle_data(self,data):
  if self.level:self.text.append(data)
for n in sys.argv[1:]:
 p=Path('wiki/raw/correzioni-collana-2026-10-02')/(n+'-20261003.html');e=Extract();e.feed(p.read_text(encoding='utf8'))
 print(n+'\n'+' '.join(' '.join(e.text).split())+'\n')
