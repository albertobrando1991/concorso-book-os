# Preflight tecnico ed editoriale — VOL-06

## Esito

Preflight locale superato senza blocker. Il PDF candidato contiene 530 pagine, usa il trim paperback 6,69 × 9,61 pollici senza bleed e incorpora i font rilevati. Le evidenze dettagliate sono registrate nel report di pipeline `wiki/reviews/pipeline/VOL-06/22-vol-06-preflight.md`.

| Controllo | Esito | Evidenza |
| --- | --- | --- |
| Copertura didattica | PASS | 4 matrici, 50 righe complete, 0 blocker e 0 warning. |
| Stato editoriale | PASS | Quattro moduli chiusi con audit, report e text freeze. |
| Typecheck | PASS | `npm run typecheck` concluso senza errori. |
| Build | PASS | `npm run build` concluso con compilazione e pagine statiche generate. |
| Test | PASS | `npm test`: 65 file e 554 test superati. |
| PDF | PASS | Book Studio `volumi/vol-06`: 530 pagine, file generato nel presente pacchetto. |
| Formato | PASS | `pdfinfo`: 481,92 × 691,92 pt, equivalenti a 6,69 × 9,61 pollici; rotazione 0. |
| Bleed | PASS | MediaBox e CropBox coincidenti; interno no-bleed. |
| Font | PASS | Arial Bold, Arial, Garamond e CambriaMath incorporati e subset. |
| Conteggio pagine | PASS | PDF e Book Studio: 530 pagine. |
| `git diff --check` | WARN non bloccante | Hard break Markdown intenzionali M-IR02 e un CRLF VOL-11 fuori perimetro. |
| KDP Previewer | NON ESEGUITO | Non disponibile nell'ambiente; controllo riservato allo step 24. |

## Identità del PDF

- File: `delivery/VOL-06/candidate/vol-06-interior-kdp.pdf`
- Dimensione: 3.487.971 byte
- SHA-256: `E262D329A64D7D7B1867FC85FE88DA46CD433F0917CCEAA06886ABF35CDB5838`
- Stato: candidato verificato localmente, non approvato né pubblicato.
