---
id: source-vol-09-consip-strumenti-obblighi-2026-10-03
type: source
title: "Consip: strumenti, obblighi e categorie aggiornate nel 2026"
status: consolidated
domain: contratti pubblici
topics: ["Consip", "MEPA", "centrali di committenza"]
entities: ["Consip", "D.Lgs. 36/2023", "ANAC"]
source_refs: ["sources/mepa-consip-acquisti-in-rete-strumenti-acquisto-negoziazione", "sources/vol-09-governance-contratti-verifica-2026-10-03"]
book_refs: ["m-tr02-appalti-pnrr-fondi-ue", "m-sa01-sanita-amministrativa"]
confidence: 0.96
updated_at: 2026-10-03
created_at: 2026-10-03
review_required: false
canonical: true
tags: ["correzioni-collana"]
source_type: official-guidance-and-law
source_url: https://www.consip.it/amministrazioni/negoziazioni
source_date: 2026-10-03
authority_level: primary
---

# Fonti e acquisizioni

- Consip, Negoziazioni: https://www.consip.it/amministrazioni/negoziazioni — raw `wiki/raw/correzioni-collana-2026-10-02/consip-negoziazioni-20261003.html`. MePA beni,servizi,lavori sottoUE; SDAPA anche sopraUE; ASP piattaforma gratuita con supporto Consip per gare proprie anche concessioni servizi. Correggere vecchia limitazione MePA ai soli lavori manutentivi.
- Codice36 artt32 e59: raw `codice36-art32-20261003.html` e `codice36-art59-20261003.html` nella stessa cartella; letti integralmente.
- Tabella Consip Obblighi–Facoltà,31/07/2026,13pp: https://www.acquistinretepa.it/opencms/export/sites/acquistinrete/documenti/airpa/TABELLA_OBBLIGO_facoltx.pdf — lettura web; estratto `consip-tabella-web-extract-20261003.txt`. **La copia scaricata con curl col nome consip-tabella-obblighi-20260731.pdf è in realtà l'avviso manutenzione2–4ottobre,6pp: NON fonte normativa.** Anche pagina obblighi acquisita direttamente va controllata per manutenzione. La tabella web guida i collegamenti normativi, non si presume che una richiesta HTTP200 abbia acquisito la fonte desiderata.
- DPCM11febbraio2026, GU88del16aprile2026, codice26A01854: https://www.gazzettaufficiale.it/eli/id/2026/04/16/26A01854/SG ; originale completo `gu-20260416-88.pdf`, PDF10–15,stampate6–11, letto. Obblighi decorrenti dalla pubblicazione, sostituiscono DPCM11luglio2018.

## Regole verificate

Art59: AQ ordinari massimo4anni salvoeccezionimotivate; stazioniidentificate/operatoriselezionati; singoloOEentrocondizioni; multiOE senza confronto se tutti termini e condizionioggettive, conconfronto se terminiincompleti, misto se previsto ecriterioggettivi. Appaltoattuativo nonmodificasostanzialmentel'AQ. C5consultazionescritta operatoriidonei,termineadeguato,offertesegretefinoascadenza,criteripredefiniti. C5bispossibilenonstipula/risoluzioneseequilibrio nonripristinabile secondo norma.

Art32: corrente/disponibilemercato, tuttoelettronico, apertointeravalidità atuttigliidonei, nessunlimitenumerico; proceduraristretta; domandeiniziali30giorni, offerte10giornifattosalvo72c5; valutazionedomande10lavorativi,15incasimotivati; tuttiammessicategoriainvitati; DGUEaggiornamento5lavorativi; nessuncontributoamministrativo; duratadichiarata, nonmutuare4anniAQ.

Obblighi da leggere congiuntamente: L296/2006art1c449(convenzioni)ec450(mercatoelettronico da5000sottoUE,ambitidifferenziati); L160/2019art1c583(AQ/SDAPA statali,scuole/università,enti nazionaliprevidenza/assistenza,agenziefiscali,fermiregimi449/450); DL95/2012art15c13d(sanitàtelematico da1000) eart1c7(categorieenergetiche/telefonia/altriambiti normativi); L208/2015c512ICT, c510derogainidoneitàconvenzione/autorizzazionevertice/Corteconti,c516derogaICT/autorizzazionevertice/comunicazioneANAC-AGID. Non rendere una facoltà generale valida per ogni soggetto.

DPCM2026art1: categorie40.000euro includonofarmaci,vaccini,ausiliincontinenza,medicazionigenerali/speciali,aghi/siringhe,gestioneapparecchiatureelettromedicali,pulizia/ristorazione/lavanderiaSSN,rifiutisanitari,vigilanza,guardiania,guanti,suture,trasportoscolastico,arredi. CategorielegateasogliaUEsubcentrale(216.000nel2026–27):stent,protesianca/ginocchio,defibrillatori,pacemaker,facilitymanagement,puliziaimmobili,manutenzioneimmobiliimpianti,ossigenoterapia,diabetologiaterritoriale,manutenzionestradeservizi/forniture,suturatrici,verde. C2importomassimoannuo per categoria, **pluriennalesuinteroperiodo**. C3bloccoCIG dallaattivazionecontrattoaggregatore. SoggettisecondoDL66art9c3; esclusiscuole/università daquestospecificoregime, non daogniobbligoConsip.

## Collegamenti

[[topics/vol-09-appalti-pnrr-procurement]], [[entities/anac]], [[entities/codice-dei-contratti-pubblici]]. Il casoICTdelComuneAlfa deve esplicitareusoSDAPA/altrostrumentoidoneo aggregatore oppure deroga516: solaassenza diconvenzione nonlibera da512.

## Completamento acquisizione diretta — 3 ottobre 2026

Letti integralmente su Normattiva i commi 449 e 450 della legge 296/2006 e 510, 512 e 516 della legge 208/2015. Raw validi: `l296-obblighi-block-20261003.html`, `l208-obblighi-block-20261003.html`, nel folder raw comune. Manifest con URL e SHA256: `artifacts/correzioni-collana-2026-10-02/obblighi-commi-manifest.json`. La paginazione caricaArticolo, con sessione originata dall’URN e progressivo5/6, ha risolto la precedente acquisizione del solo inizio dell’articolo1. I vecchi file con c449/c512 nel nome non provano la presenza del relativo comma.

Il comma449 comprende scuole e università fra i soggetti obbligati alle convenzioni. Il comma450 le esclude dalla prima frase relativa alle amministrazioni statali e mantiene ambiti differenziati: non ricavarne esonero generale dall’acquisto digitale. Per le altre PA e authority, da5.000 sottoUE, MePA, altri mercati elettronici o sistema telematico regionale. Deroga510 per inidoneità della convenzione dovuta a mancanza di caratteristiche essenziali: autorizzazione del vertice e trasmissione alla Corte dei conti. ICT512/516: strumenti Consip/aggregatori per beni disponibili, deroga per indisponibilità/inidoneità o necessità e urgenza per continuità; autorizzazione motivata e comunicazione ANAC/AgID.

Caso laboratorio90.000 di arredi assegnato a università, non Comune: evita di ignorare il nuovo obbligo merceologico del DPCM2026 per enti locali oltre40.000. L’esclusione universitaria dall’art.9c3 non elimina il comma449 o gli altri strumenti obbligatori: l’ipotesi rende esplicita la verifica di indisponibilità.
