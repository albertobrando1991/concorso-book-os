# Integrazione 2 ottobre 2026 — controllo layout DOM mirato

## Esito effettivo

Verifiche browser concluse alle 22:38 circa; tutti i browser avviati dagli helper sono terminati. Server gestito dal main, non arrestato da questo audit. Nessun PDF creato, nessun codice canonico o manoscritto modificato dall'auditor, nessun gate/run-state modificato. Skill PDF e canvas-design usate per separare controllo DOM da PDF e privilegiare leggibilità delle tabelle senza riduzioni di corpo.

| Volume | Conteggio DOM assestato finale | Pagine dei capitoli verificate geometricamente | Esito geometrico nel perimetro |
| --- | ---: | ---: | --- |
| VOL-01 | 615 | 101: cap05 73–110; cap06 111–140; cap12 284–316 | Zero overflow >8px, collisioni fra blocchi adiacenti, tabelle fuori contenitore o celle con overflow orizzontale |
| VOL-07 | 414 | 59: cap04 8–39; cap09 79–105 | Medesimi controlli: zero anomalie rilevate |

Il primo verifier canonico `verify-book-studio-layout.mjs` aveva rilevato 615 / 412 pagine con scala tipografica/struttura conformi e nessun overflow/collisione. Il successivo riassetto delle tabelle sanitarie ha portato VOL-07 a **414**, confermato dopo la correzione dell'etichetta orfana. 412 non è il conteggio finale. I conteggi storici 592 / 394 non sono più utilizzabili per l'export aggiornato.

## Ispezione visiva reale

- Campione finale VOL-01: pagine **102, 138, 305**, rispettivamente tabella accessi separata, laboratorio situazioni/doveri e rischio/comportamento, nuovi quiz A1–B6. Tabelle e intestazioni leggibili, contenute, senza tagli; continuazioni con intestazioni presenti.
- Campione sanitario prima dell'ultima microcorrezione: pagine **21, 80, 89, 91, 98, 99, 102** a pagina intera, con tutte le nuove divisioni tabellari principali. Tabelle 2–3 colonne leggibili; laboratorio p102 conserva quattro griglie e campi di lavoro senza riduzione del font.
- Campione sanitario finale ripetuto: **98–99**. L'etichetta «Evidenze ed esiti», inizialmente rimasta sola al fondo di p98, è ora heading H4 insieme alla tabella a p99; anche «Azioni condizionate» precede correttamente la propria tabella. Rilievo risolto e ricontrollato.

Le prime screenshot con suffisso `-pNN.png` contenevano clipping dello scrollcontainer e parte dell'interfaccia: **non usarle come prova di pagina completa**. Le screenshot valide sono quelle con suffisso **`-full-pNN.png`**, ottenute da clone fuori UI, senza cambiare il master. Dimensioni original/clone verificate nel JSON: circa **642,234 × 922,547 CSS px**, differenza massima di arrotondamento 0,016px nel campione base; nessuna scalatura della pagina.

## Rilievi e limiti rimasti

1. **Minore preesistente:** VOL-01 p102 ripete la didascalia Figura 5.5 come figcaption e paragrafo. Confermato presente anche nel file a HEAD (`git show`). Da trattare nel controllo immagini/layout generale, non introdotto dalle divisioni tabellari; non corretto in questo audit.
2. Spazi: misurati, non tutti giudicati visivamente. Nel base i maggiori vuoti non terminali includono p312 (296px) e p313 (314px), tabelle soluzioni; nel sanitario p26 (253px) e p89 (243px). Non basta il numero per classificarli come difetti: vanno valutati allo step20 rispetto a titolo/blocco successivo indivisibile, continuità e spazio di lavoro. La diagnostica canonica esenta alcuni casi, ma l'esenzione non dimostra da sola buona impaginazione.
3. Dopo l'ultima patch sanitaria p98 ha 92px liberi, p99 182px, overflow zero. L'heading spostato ha risolto l'orfano senza forzare densità o font.
4. Le **160 pagine** sono copertura geometrica dei cinque capitoli, **non 160 pagine ispezionate visivamente**. L'intero volume finale non è certificato; nessun audit20 completo, nessun raster PDF/preflight eseguito.
5. Altri capitoli sanitari, le quattro tabelle preesistenti più larghe segnalate dal main e altri asset del volume restano fuori dal campione; lo step18 generale rimane in corso. Nessuna attestazione globale di assenza di difetti.

## Evidenze conservate

- `artifacts/20261002-integrazioni-layout-layout-report.json`: prima passata canonica 615/412, tipografia e struttura.
- `artifacts/20261002-targeted-vol01.json`: ultima geometria, campione 102/138/305 e dimensioni clone.
- `artifacts/20261002-targeted-vol07.json`: ultima geometria dopo H4, campione98/99 e dimensioni clone.
- `artifacts/20261002-targeted-vol01-full-p102.png`, `...-p138.png`, `...-p305.png`.
- `artifacts/20261002-targeted-vol07-full-p98.png`, `...-p99.png`; conservate anche le precedenti pagine p21/80/89/91/102.
- Helper diagnostico non canonico: `tmp/20261002-inspect-integration-layout.mjs`. Ultime esecuzioni:

```powershell
node tmp/20261002-inspect-integration-layout.mjs il-metodo-bando 102,138,305 only
node tmp/20261002-inspect-integration-layout.mjs volumi/vol-07 98,99 only
```

Gli helper aspettano font, immagini, 25 secondi di assestamento, sei letture uguali e conferma ritardata; verificano che il conteggio non cambi durante la raccolta geometrica. Questo non sostituisce il controllo completo della firma testuale della paginazione nello script canonico di audit20. Nessun artefatto storico è stato sovrascritto: tutti i nuovi file usano prefisso20261002. Le versioni intermedie con lo stesso prefisso sono state aggiornate durante la diagnostica; restano i relativi screenshot distinti.
