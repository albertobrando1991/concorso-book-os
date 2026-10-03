from pathlib import Path
import re, shutil, hashlib, json
root=Path.cwd()
base=root/'wiki/books/moduli/m-fc02-agenzie-fiscali/chapters'
p=base/'05b-tutela-processo-tributario.md'
backup=root/'artifacts/correzioni-collana-2026-10-02/before-text/VOL-03'
backup.mkdir(parents=True,exist_ok=True)
if not (backup/p.name).exists(): shutil.copy2(p,backup/p.name)
s=p.read_text(encoding='utf-8')
s=s.replace('status: final','status: revised_draft').replace('draft_stage: text_frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true').replace('updated_at: 2026-08-22T14:30:00+02:00','updated_at: 2026-10-03')
s=s.replace('source_refs: [','source_refs: ["sources/processo-tributario-regime-2026-rettifica-2026-10-03", ',1).replace('last_compiled_from: [','last_compiled_from: ["wiki/sources/processo-tributario-regime-2026-rettifica-2026-10-03.md", ',1)
old="Il capitolo usa il Testo unico della giustizia tributaria approvato con D.Lgs. 175/2024, applicabile dal 1 gennaio 2026 e coordinato con gli interventi ufficiali acquisiti fino all'audit del 18 luglio 2026. Non riproduce termini numerici o regole telematiche mobili: insegna la sequenza e segnala dove la versione vigente deve essere aperta."
new="Nel 2026 il riferimento è il D.Lgs. 546/1992 per il processo, insieme al D.Lgs. 545/1992 per l'ordinamento degli organi, entrambi con le successive modifiche. Il Testo unico della giustizia tributaria, D.Lgs. 175/2024, si applicherà dal **1° gennaio 2027**: il rinvio è disposto dall'art. 4 del D.L. 200/2025, convertito dalla legge 26/2026. Le regole qui illustrate sono verificate al 3 ottobre 2026; per una controversia concreta si controllano anche le disposizioni transitorie."
assert old in s;s=s.replace(old,new)
s=re.sub(r'Questa sequenza segue la mappa del TU 175:.*?singolo articolo nella versione aggiornata\.',"Il riferimento del 2026 è il D.Lgs. 546/1992: artt. 1–17 per la disciplina generale; 18–24 per introduzione e costituzione; 30–38 per trattazione e decisione; 39–46 per le vicende del processo; 47–48-ter per cautela e conciliazione; 49–67 per impugnazioni; 67-bis–70 per esecuzione e ottemperanza. L'ordinamento delle Corti è disciplinato dal D.Lgs. 545/1992.",s)
s=s.replace("Il TU 175 distingue ordinamento degli organi e disciplina del processo.","I D.Lgs. 545 e 546 del 1992 distinguono ordinamento degli organi e disciplina del processo.")
s=s.replace("Il criterio territoriale di competenza va ricavato dalla disposizione vigente collegando parte resistente, sede/ufficio o altro elemento normativamente rilevante. Non si sceglie la corte dal domicilio del ricorrente per intuizione e non si trasferiscono alla competenza tributaria criteri di altri processi.","L'art. 4 del D.Lgs. 546/1992 collega ordinariamente la competenza territoriale alla sede dell'ente impositore o dell'agente della riscossione resistente. Per articolazioni dell'Agenzia delle entrate con competenza sovraterritoriale conta la sede dell'ufficio cui spettano le attribuzioni sul rapporto controverso. Per i concessionari della fiscalità locale va considerata la sede dell'ente locale impositore, secondo la sentenza della Corte costituzionale 44/2016. L'appello appartiene alla Corte di secondo grado nella cui circoscrizione ha sede quella che ha pronunciato. Il domicilio del contribuente non è un criterio generale alternativo.")
needle="Litisconsorzio e intervento servono"
insert="La difesa tecnica è la regola per il contribuente. L'art. 12 consente di stare in giudizio personalmente nelle controversie di valore **fino a 3.000 euro**, compreso il valore esatto di 3.000. Il valore è il tributo contestato, senza interessi e sanzioni accessorie; se si impugnano soltanto sanzioni, si considera la loro somma. Un atto con 2.800 euro di tributo, 700 di sanzioni e 100 di interessi ha quindi valore 2.800, non 3.600. La possibilità di difesa personale non elimina termini, motivi e onere probatorio.\n\n"
s=s.replace(needle,insert+needle)
s=re.sub(r'La tabella traduce il blocco del TU 175.*?testo coordinato applicabile\.',"L'art. 19 del D.Lgs. 546/1992 elenca gli atti impugnabili. Le famiglie seguenti aiutano a riconoscerli; per i dinieghi di autotutela occorre distinguere l'obbligatoria dalla facoltativa: il rifiuto espresso o tacito della prima è previsto dalla lettera g-bis), mentre per la seconda la lettera g-ter) riguarda il rifiuto espresso.",s)
needle='### Checklist PTT'
insert="""### Termini essenziali e calcolo guidato

| Adempimento | Termine ordinario | Da quale evento |
| --- | --- | --- |
| Proporre il ricorso, art. 21 | 60 giorni | Notificazione dell'atto impugnato. |
| Costituirsi come ricorrente, art. 22 | 30 giorni | Proposizione del ricorso. |
| Costituirsi come resistente, art. 23 | 60 giorni | Ricevimento del ricorso. |

Il primo termine riguarda la notificazione del ricorso alla controparte; il secondo il deposito per instaurare il fascicolo davanti alla Corte. Confonderli può rendere inammissibile il ricorso. Per il rifiuto tacito di rimborso opera una regola diversa: il ricorso è proponibile dopo il novantesimo giorno dalla domanda e fino alla prescrizione del diritto, ferme le condizioni della domanda originaria. Non si applicano automaticamente i 60 giorni di un atto notificato.

Nel computo si esclude il giorno iniziale e si include quello finale; se la scadenza processuale cade in giorno festivo o di sabato opera il rinvio previsto dall'art. 155 c.p.c. La sospensione feriale va dal 1° al 31 agosto (legge 742/1969), salve le esclusioni. Adesione e altre fattispecie possono introdurre sospensioni proprie: l'istanza di autotutela, invece, non sospende da sola il termine.

**Caso con calendario dichiarato.** Un avviso è notificato a Omega il 2 marzo 2026; non ricorrono adesione, sospensioni o proroghe speciali. I 60 giorni decorrono dal 3 marzo: la scadenza aritmetica è il 1° maggio, festivo; seguono sabato 2 e domenica 3, perciò il termine slitta a lunedì 4 maggio. Omega notifica il ricorso il 20 aprile: i 30 giorni per costituirsi scadono il 20 maggio. Un'istanza di autotutela depositata il 10 marzo non cambia queste date. **Verifica:** se Omega si costituisce il 25 maggio, il ricorso è tempestivamente notificato ma il deposito è tardivo: i due controlli restano distinti.

"""
s=s.replace(needle,insert+needle)
s=s.replace("La regola va applicata alla singola domanda, senza slogan come “prova sempre l'ufficio” o “prova sempre il contribuente”. Il numero e il testo dell'articolo devono essere controllati sul TU 175 coordinato: il capitolo non cristallizza una numerazione non validata dalla source, ma rende esplicito il contenuto normativo consolidato.","L'art. 7, comma 5-bis, impone all'amministrazione di provare in giudizio le violazioni contestate; il giudice annulla l'atto quando la prova manca, è contraddittoria o insufficiente rispetto alla pretesa. Il contribuente prova le ragioni della richiesta di rimborso, salvo il rimborso conseguente al pagamento di somme oggetto di accertamenti impugnati. La regola si applica alla specifica domanda e va coordinata con le presunzioni legali: non significa che una delle parti debba provare indistintamente ogni fatto.")
s=s.replace('secondo la formula e i presupposti del TU vigente','ai sensi dell’art. 47 del D.Lgs. 546/1992')
s=s.replace('TU 175/2024','D.Lgs. 546/1992').replace('secondo TU e processo telematico','secondo il D.Lgs. 546/1992 e le regole del processo telematico').replace('il TU vigente','il D.Lgs. 546/1992 vigente').replace('dal TU','dal D.Lgs. 546/1992').replace('del TU','del D.Lgs. 546/1992').replace('il TU','il D.Lgs. 546/1992')
s=s.replace("**Domanda rapida:** quale mezzo useresti", "Il termine ordinario per impugnare la sentenza è di **60 giorni dalla notificazione a istanza di parte** (art. 51). Se la sentenza non è notificata, il termine lungo è di **sei mesi dalla pubblicazione**, attraverso il rinvio all'art. 327 c.p.c., fatte salve le eccezioni legali. Comunicazione della segreteria e notificazione a istanza di parte non sono equivalenti.\n\n**Domanda rapida:** quale mezzo useresti")
s=s.replace("La mappa completa è tracciata nella source [[sources/autotutela-adesione-deflativi-aggiornamento-2026-07-29#Mappa didattica]].", "Il riferimento per l'autotutela è negli artt. 10-quater e 10-quinquies della legge 212/2000; per adesione e acquiescenza nel D.Lgs. 218/1997.")
s=s.replace("La distinzione rispetto ad autotutela, adesione e acquiescenza è consolidata in [[sources/autotutela-adesione-deflativi-aggiornamento-2026-07-29]].", "Gli artt. 48, 48-bis e 48-ter del D.Lgs. 546/1992 regolano conciliazione fuori udienza, in udienza e relative conseguenze.")
s=s.split('## Riferimenti consolidati')[0].rstrip()+"\n\n## Riferimenti normativi essenziali\n\n- D.Lgs. 545/1992 e D.Lgs. 546/1992, nelle versioni applicabili nel 2026.\n- D.L. 200/2025, art. 4, convertito dalla legge 26/2026: applicazione del D.Lgs. 175/2024 dal 1° gennaio 2027.\n- Legge 212/2000, artt. 10-quater e 10-quinquies; D.Lgs. 218/1997.\n- Legge 742/1969; codice di procedura civile, artt. 155 e 327; disciplina del processo tributario telematico.\n"
p.write_text(s,encoding='utf-8')
oldsource=root/'wiki/sources/processo-tributario-dlgs-175-2024-aggiornamento-2026-07-18.md'
s=oldsource.read_text(encoding='utf-8')
if '## Rettifica del 3 ottobre 2026' not in s:
 pos=s.index('\n## Fonte applicabile')
 s=s[:pos]+"\n## Rettifica del 3 ottobre 2026\n\n**Le conclusioni originarie sul calendario e sulla sostituzione del D.Lgs. 546/1992 sono errate e superate.** Il TU 175 si applica dal 1° gennaio 2027, per effetto del D.L. 200/2025 convertito dalla legge 26/2026. Per il 2026 usare D.Lgs. 545 e 546 del 1992 e la nuova nota [[sources/processo-tributario-regime-2026-rettifica-2026-10-03]]. Il testo sottostante documenta lo stato precedente e non è una fonte valida per la decorrenza.\n"+s[pos:]
 s=s.replace('status: consolidated','status: superseded').replace('canonical: true','canonical: false')
 oldsource.write_text(s,encoding='utf-8')
print('Updated 05b and superseded source; original saved in',backup)
