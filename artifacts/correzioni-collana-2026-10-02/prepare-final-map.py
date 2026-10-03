from pathlib import Path
A=Path(__file__).parent
s=(A/'vol01-native-pdf-map.py').read_text(encoding='utf8')
s=s.replace("vol-01-native-20261003-proof.pdf", "vol-01-native-final-20261003-proof.pdf").replace("out=D/'pdf-pages'", "out=D/'final-pdf-pages'").replace("VOL-01-native-pdf-map.json", "VOL-01-native-final-pdf-map.json")
(A/'vol01-native-final-pdf-map.py').write_text(s,encoding='utf8')
s=(A/'vol01-native-contact.py').read_text(encoding='utf8')
s=s.replace('VOL-01-native-pdf-map.json','VOL-01-native-final-pdf-map.json').replace("'pdf-sheets'","'final-pdf-sheets'").replace("'pdf-pages'","'final-pdf-pages'").replace('VOL-01-native-pdf-visual-ledger.json','VOL-01-native-final-pdf-visual-ledger.json')
(A/'vol01-native-final-contact.py').write_text(s,encoding='utf8')
