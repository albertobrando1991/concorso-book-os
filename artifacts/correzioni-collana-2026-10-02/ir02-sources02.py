from pathlib import Path
import shutil,hashlib,re
A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/raw/correzioni-collana-2026-10-02')
groups={
'contabilita-economico-patrimoniale-universita-enti-pubblici':(['dlgs18-art1-current.html','mur-di34-2025.pdf'],'''## Aggiornamento universitario verificato il 3 ottobre 2026

Letto D.Lgs. 18/2012, art. 1, testo vigente, e D.I. MUR-MEF 34 del 15 gennaio 2025, pagine PDF 1–4, 7, 10, 12–13 e 17. Verifica selettiva del decreto di 33 pagine, non certificazione dell'intero manuale tecnico. Fonti: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2012-01-27;18~art1!vig= ; https://www.mur.gov.it/sites/default/files/2025-01/DI%20n.%2034%20del%2015-01-2025.pdf .

Il bilancio unico annuale di previsione autorizzatorio comprende budget economico e degli investimenti; il triennale conserva queste componenti. Il bilancio di esercizio comprende stato patrimoniale, conto economico, rendiconto finanziario e nota integrativa, con relazione sulla gestione. Per le università comprese nelle amministrazioni pubbliche si aggiungono preventivo finanziario non autorizzatorio e rendiconto finanziario ai fini del consolidamento pubblico. Il consolidato del gruppo è distinto dal bilancio unico.

Il D.I. 34/2025 reca principi e schemi aggiornati: l'art. 10 abroga i precedenti D.I. 19/2014, 394/2017 e 925/2015, da non presentare come disciplina vigente autonoma. Competenza economica distinta dalla cassa; ratei e risconti richiedono quote temporali comuni a più esercizi. Rateo passivo: costo maturato con manifestazione monetaria futura; risconto attivo: costo pagato anticipatamente di competenza futura. Ammortamento ripartisce il costo del bene a utilità pluriennale; i beni culturali non sono assoggettati all'ammortamento ordinario (p. 10). Nei progetti, principi di commessa completata o percentuale di completamento nei casi previsti; gli assestamenti confrontano proventi registrati, non semplicemente anticipi incassati, con costi maturati (p. 13). Non universalizzare lo schema dei contributi privati.

Esercizi originali autorizzati per la didattica: attrezzatura ordinaria di 60.000 euro disponibile dal 1° gennaio, vita cinque anni, valore residuo nullo, quota costante di 12.000; canone di 12.000 per dodici mesi dal 1° ottobre, costo corrente di 3.000 e risconto attivo di 9.000; interesse semestrale ottobre-marzo di 1.200, quota corrente di 600 e rateo passivo di 600. Sono ipotesi didattiche espresse, senza IVA, contributi in conto capitale o altre operazioni. Collegamenti: [[topics/m-ir02-universita-afam-fonti-e-profili]], [[entities/ministero-universita-ricerca]], [[books/moduli/m-ir02-universita-afam/chapters/06-bilancio-ateneo]].
'''),
'grant-management-horizon-pnrr-2026-08-23':(['eu-aga-2025.pdf'],'''## Forme di finanziamento e verifica del 3 ottobre 2026

Commissione europea, AGA Annotated Grant Agreement, versione 2.0 del 1° aprile 2025, https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/common/guidance/aga_en.pdf : lettura selettiva artt. 5–6, pagine PDF 34–45; documento di 431 pagine, non letto integralmente. La REA conferma il ruolo vincolante del grant e la procedura di amendment: https://rea.ec.europa.eu/horizon-europe-grants-reporting_en .

Costi effettivi: importi realmente sostenuti, pertinenti, verificabili e ammissibili. Costi unitari: unità effettive documentate per importo unitario applicabile. Tasso forfettario: percentuale sulla base ammissibile definita, con esclusioni specifiche. Somma forfettaria: attività e risultati contrattuali realizzati, senza ricalcolare il contributo sul costo effettivo; permangono obblighi non finanziari. Finanziamento non collegato ai costi distinto dalla mera rendicontazione semplificata. La forma applicabile è indicata nel grant, non scelta liberamente dal beneficiario. Le variazioni del budget possono essere ammesse senza amendment entro le condizioni dell'art. 5.5, ma modifiche sostanziali dell'azione e particolari categorie richiedono amendment o approvazione pertinente. La semplificazione non aumenta il massimo del contributo e non autorizza doppio finanziamento.

Gli esempi nei capitoli usano valori ipotetici dichiarati, diversi dagli esempi AGA: non forniscono aliquote permanenti né sostituiscono call, allegati e contratto. Milestone è un traguardo qualitativo, target un obiettivo quantitativo; la spesa non dimostra da sola il raggiungimento. DNSH è obbligatorio per le misure RRF; evidenze e verifiche variano per misura e intervento. Collegamenti: [[topics/m-ir02-universita-afam-fonti-e-profili]], [[entities/ministero-universita-ricerca]], [[books/moduli/m-ir02-universita-afam/chapters/07-ricerca-grant-management]], [[books/moduli/m-ir02-universita-afam/chapters/08-prin-horizon-pnrr-audit]].
''')}
for slug,(names,delta) in groups.items():
 p=Path('wiki/sources')/(slug+'.md');t=p.read_text(encoding='utf8')+'\n'+delta+'\n### Evidenze acquisite\n\n'
 for name in names:
  if not (R/name).exists():shutil.copyfile(A/name,R/name)
  t+=f'- `raw/correzioni-collana-2026-10-02/{name}` — SHA256 {hashlib.sha256((R/name).read_bytes()).hexdigest()}.\n'
 t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf8')
print('IR02 fonti contabili e grant consolidate')
