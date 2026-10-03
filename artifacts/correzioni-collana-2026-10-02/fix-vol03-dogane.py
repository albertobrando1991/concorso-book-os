from pathlib import Path
import re,shutil
root=Path.cwd();base=root/'wiki/books/moduli/m-fc02-agenzie-fiscali/chapters'
backup=root/'artifacts/correzioni-collana-2026-10-02/before-text/VOL-03';backup.mkdir(parents=True,exist_ok=True)
def load(n):
 p=next(base.glob(n+'-*.md'))
 if not (backup/p.name).exists():shutil.copy2(p,backup/p.name)
 return p,p.read_text(encoding='utf-8')
def save(p,s):
 s=s.replace('status: final','status: revised_draft').replace('draft_stage: text_frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true')
 s=re.sub(r'updated_at: [^\n]+','updated_at: 2026-10-03',s,count=1)
 ref='sources/dogane-accise-rettifiche-2026-10-03'
 if ref not in s:s=s.replace('source_refs: [',f'source_refs: ["{ref}", ',1).replace('last_compiled_from: [',f'last_compiled_from: ["wiki/{ref}.md", ',1)
 p.write_text(s,encoding='utf-8')
p,s=load('08')
s=s.replace('Il D.P.R. 43/1973 conserva rilievo storico e per le disposizioni non superate, ma non può più essere trattato come unica architrave del sistema.',"Il D.P.R. 43/1973 (vecchio testo unico doganale) è stato abrogato dal D.Lgs. 141/2024. Può servire per ricostruire vicende anteriori secondo le regole temporali, ma non è il complemento ordinariamente vigente del CDU.")
s=s.replace('Le merci non unionali restano sotto vigilanza doganale finche non acquistano lo status unionale, vengono vincolate a un altro regime o escono dal territorio.',"Le merci non unionali restano sotto vigilanza doganale fino a quando acquistano lo status unionale, sono portate fuori dal territorio doganale o sono distrutte, secondo l'art. 134 CDU. Il vincolo a un altro regime, per esempio dal transito al deposito doganale, non fa cessare da solo la vigilanza: cambia il regime, non lo status della merce.")
s=s.replace("Prima dello svincolo, la dichiarazione può essere rettificata nei casi e nei limiti del CDU.","Dopo l'accettazione la dichiarazione può essere modificata nei limiti dell'art. 173 CDU; la modifica ordinaria non è autorizzata quando la dogana ha annunciato la visita, accertato l'inesattezza o già svincolato le merci. Esiste però una distinta possibilità **dopo lo svincolo**: su richiesta del dichiarante entro tre anni dalla data di accettazione, la modifica può essere autorizzata per consentire l'adempimento degli obblighi relativi al regime. Non è una modifica automatica e non consente di dichiarare merci diverse.")
s=s.replace("**3. Origine.** Spedizione dalla Turchia e origine non coincidono. Va verificata la lavorazione effettuata e la prova invocata; la produzione cinese può escludere l'origine preferenziale se non ricorrono le regole dell'accordo.","**3. Origine e libera pratica.** Per componenti industriali coperti dall'unione doganale UE–Turchia, il trattamento daziario si collega alla libera pratica, comprovata dall'A.TR, non a una generica dichiarazione di origine preferenziale turca. La produzione cinese non esclude da sola il beneficio se la merce è stata regolarmente immessa in libera pratica in Turchia e ricorrono le altre condizioni. L'origine non preferenziale resta da accertare, per esempio per misure antidumping. L'ufficio controlla quindi classificazione, ambito dell'unione doganale e A.TR; non confonde il certificato di circolazione con una prova di origine. Prodotti agricoli e carbo-siderurgici esclusi dall'unione doganale richiedono un distinto esame del regime applicabile.")
s=s.replace('## Da sapere in 5 righe',"**Verifica aggiuntiva.** Merci cinesi passano dal transito al deposito doganale: cessa la vigilanza? No, restano non unionali. Il dichiarante scopre dopo sei mesi dallo svincolo un dato errato: la modifica è impossibile? No, può chiedere l'autorizzazione nei presupposti dell'art. 173, par. 3; i tre anni decorrono dall'accettazione.\n\n## Da sapere in 5 righe")
save(p,s)
p,s=load('09')
s=s.replace("Il destinatario registrato può ricevere, alle condizioni dell'autorizzazione, prodotti provenienti da un altro Stato membro in sospensione, ma non per questo può fabbricarli o detenerli indefinitamente in sospensione come un depositario.","Il destinatario registrato può ricevere, alle condizioni dell'autorizzazione, prodotti provenienti da un altro Stato membro in sospensione. La ricezione conclude quel movimento e rende esigibile l'accisa secondo la disciplina applicabile. Questa qualifica non consente di fabbricare, trasformare, detenere, immagazzinare o spedire prodotti in sospensione: il divieto non dipende dalla durata della detenzione. È quindi diverso dal depositario autorizzato.")
needle='## 5.'
pos=s.index(needle)
s=s[:pos]+"""### Prodotti già immessi in consumo: il secondo circuito EMCS

Dal 13 febbraio 2023 EMCS segue anche i prodotti già immessi in consumo in uno Stato membro e trasferiti in un altro per consegna a fini commerciali. Qui operano **speditore certificato** e **destinatario certificato**, con il documento amministrativo elettronico semplificato, detto **e-DAS unionale**. Nel circuito sospensivo il documento è invece l'e-AD. L'aggettivo «certificato» non è un modo alternativo per dire «registrato»: identifica un ruolo diverso.

**Confronto risolto.** Alcol parte da un deposito fiscale francese verso un destinatario registrato italiano: movimento in sospensione con e-AD, poi esigibilità al ricevimento. Alcol già immesso in consumo in Francia è trasferito commercialmente in Italia: circuito a imposta assolta con e-DAS unionale e soggetti certificati, applicando il regime dell'accisa nello Stato di destinazione e il rimborso nello Stato di partenza alle condizioni previste. Il nome del sistema informatico è lo stesso; presupposti, qualifiche e documento cambiano.

"""+s[pos:]
save(p,s)
p,s=load('14')
s=s.replace('Sistema di controllo della circolazione in sospensione.','Sistema di controllo dei movimenti in sospensione e dei trasferimenti commerciali intra-UE di prodotti già immessi in consumo.').replace('Soggetto che presenta la dichiarazione in proprio nome o per conto altrui.','Persona che presenta la dichiarazione in nome proprio o persona nel cui nome la dichiarazione è presentata.')
save(p,s)
p,s=load('05')
s=s.replace('pregiudizio grave o irreparabile','pregiudizio grave e irreparabile').replace('e alla source note processuale consolidata','(D.Lgs. 546/1992, art. 47)')
s=s.replace('source_refs: [','source_refs: ["sources/processo-tributario-regime-2026-rettifica-2026-10-03", ',1)
save(p,s)
topic=root/'wiki/topics/dogane-accise-monopoli-adm.md'
t=topic.read_text(encoding='utf-8')
if '## Rettifiche del 3 ottobre 2026' not in t:t+='\n## Rettifiche del 3 ottobre 2026\n\nLa nuova [[sources/dogane-accise-rettifiche-2026-10-03]] precisa vigilanza delle merci non unionali, modifica dopo svincolo entro tre anni, abrogazione del TULD, A.TR distinto da origine, qualifica del destinatario registrato ed estensione EMCS ai trasferimenti commerciali a imposta assolta. Le correzioni sono applicate ai capitoli 08, 09 e 14 di M-FC02.\n'
topic.write_text(t,encoding='utf-8')
print('Updated FC02 05/08/09/14 and topic')
