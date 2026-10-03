from pathlib import Path
import json,hashlib
A=Path(__file__).parent;p=A/'registro-applicazione.json';rows=json.loads(p.read_text(encoding='utf8'))
for r in rows:
 if r['id'] in ['V01-50','V01-51']:
  f='wiki/books/il-metodo-bando/front-matter/'+('05-premessa.md' if r['id']=='V01-50' else '03-copyright-colophon.md')
  r['status']='parzialmente-applicato';r['changedFiles']=list(dict.fromkeys(r.get('changedFiles',[])+[f]));r['fileHashes']={f:hashlib.sha256(Path(f).read_bytes()).hexdigest()}
  r['verification']=['Premessa coordinata alla pagina servizi; nessuna condizione commerciale inventata. Restano procedura reale, decorrenza mese e collaudo autorizzato.' if r['id']=='V01-50' else 'Edizione2026 e aggiornamento3ottobre2026 inseriti. Restano canale errata effettivo e identificativi assegnati dall’editore; nessun ISBN inventato.']
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
p=Path('wiki/reviews/correzioni-collana-2026-10-02/README.md');t=p.read_text(encoding='utf8').replace('VOL-03/08/10 e codice comune di esportazione; coordinatore per VOL-01/09/11','VOL-03/08/10/11; coordinatore per VOL-01/09 e codice comune di esportazione');p.write_text(t,encoding='utf8')
p=Path('wiki/reviews/correzioni-collana-2026-10-02/PRELIMINARI.md');p.write_text('''# Preliminari — stato verificato, 3 ottobre 2026

V01-50: la premessa rimanda ora alla pagina dei servizi, evitando la contraddizione fra inclusione certa e disponibilità eventuale. La promessa del mese incluso resta quella del progetto autorizzato. Il sito risponde, ma questo non prova registrazione, abilitazione dei materiali o decorrenza del mese. La domanda operativa all’editore resta senza risposta; non è sostituita da un’assunzione.

V01-51: inseriti edizione2026 e cut-off3ottobre2026; precisate date degli esempi ed efficacia futura. Recapito per errata e identificativi dell’edizione devono essere quelli effettivi dell’editore. Non si inventano indirizzi, ISBN o una pagina web pubblicata. La clausola di riproduzione è conservata: l’audit stesso qualifica la menzione esplicita degli usi consentiti come miglioramento facoltativo, non difetto giuridico certo.

Le correzioni sono parziali e non autorizzano il rilascio del prodotto. Proseguono integralmente i lavori indipendenti su contenuti, impaginazione e pacchetto di consegna.
''',encoding='utf8')
print('Preliminaries partial status recorded; business facts remain unverified.')
