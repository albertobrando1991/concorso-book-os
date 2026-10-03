from pathlib import Path
import re,json,hashlib
art=Path('artifacts/correzioni-collana-2026-10-02');mod=Path('wiki/books/moduli/m-fl03-camere-commercio')
p=Path('wiki/reviews/pipeline/VOL-02/15-moduli-m-fl03-camere-commercio.md');archive=art/'VOL-02-step15-M-FL03-prima-correzioni.md'
if p.exists() and not archive.exists():archive.write_bytes(p.read_bytes())
t=Path('wiki/reviews/pipeline/VOL-02/14-moduli-m-fl03-camere-commercio.md').read_text(encoding='utf-8')
t=t.replace('# Correzioni autorizzate — M-FL03','# Audit specialistico correttivo — M-FL03')
t=t.replace('Applicato nel modulo; audit 15 successivo','Chiuso nel modulo')
t=t.replace('Eseguire audit 15 prima del freeze.','Riesaminati tutti i nuclei integrati, nessuna criticità normativa grave o media residua nel perimetro camerale. Nessun box Dato operativo rilevato dal CLI. Il gate 14 è passato senza blocchi.')
t=t.replace('Gate 14, audit 15 e freeze CLI; poi produzione e verifica del nuovo PDF.','Registrare gate 15 e freeze CLI; produzione e verifica del nuovo PDF restano passaggi distinti.')
t=t.replace('Testo corretto nel perimetro dei rilievi camerali; nessuna dichiarazione di pubblicabilità del VOL-02.','Testo camerale idoneo al freeze nel perimetro riesaminato. Nessuna dichiarazione di pubblicabilità del VOL-02: mancano correzioni di altri moduli e nuova produzione.')
t=t.replace('## 5. Coerenza globale\n','''## 5. Coerenza globale

Verificati 62 wikilink: nessun file o heading mancante. Risolti nuovamente i quiz nuovi: cap. 02, 7B/8C; cap. 03, 7B/8A; cap. 04, 7D/8B. Il caso dell'art. 2193 non deduce conoscenza effettiva da una comunicazione mai recapitata. I rimedi distinguono rifiuto su domanda (otto giorni) e determinazioni d'ufficio ex art. 40 (quindici dalla comunicazione). Il pagamento della cambiale a otto mesi soddisfa il requisito temporale, quello a quattordici no; la cancellazione richiede istanza e documenti. Per la bilancia, il controllo a richiesta non sostituisce la verifica periodica. Le tre vicende lavorative distinguono differenziale, incarico EQ e progressione tra aree. La visura del concorrente è pubblica; gli allegati della pratica di contributo seguono il regime di accesso pertinente.

La rilettura ha eliminato l'equivoco fra limite certificativo della visura e opponibilità dei fatti iscritti. Il capitolo 03 include la possibilità vigente di riabilitazione con atto notarile e l'eccezione camerale nella verificazione metrologica; le vecchie pagine istituzionali non aggiornate non sono state usate per negarle. La fonte del CCNL distingue rinnovo firmato nel 2026 e disposizioni 2022 ancora richiamate.
''')
p.write_text(t,encoding='utf-8')
statepath=art/'VOL-02-changes.json';s=json.loads(statepath.read_text(encoding='utf-8'))
for fid in ['V02-35','V02-36','V02-37']:s['changes'][fid]['status']='Applicato e riesaminato in M-FL03; gate 15 da registrare'
statepath.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(p)
