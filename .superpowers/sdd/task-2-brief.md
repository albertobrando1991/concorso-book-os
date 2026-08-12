# Task 2 — Template e validatore della matrice

Leggi `docs/superpowers/plans/2026-07-17-copertura-didattica-integrale.md`, Task 2, e `docs/superpowers/specs/2026-07-17-copertura-didattica-integrale-design.md`.

## Files

Creare:

- `wiki/templates/didactic-coverage-matrix-template.md`
- `src/server/editorial/didactic-coverage.ts`
- `scripts/audit-didactic-coverage.mjs`
- `tests/didactic-coverage.test.ts`

Modificare solo `package.json` oltre ai file creati.

## API

- `parseCoverageMatrix(markdown: string): CoverageRow[]`
- `auditCoverageRows(rows: CoverageRow[]): { blockers: CoverageIssue[]; warnings: CoverageIssue[]; complete: number }`
- Stati validi: `completo | parziale | solo-nominato | rinviato | mancante`.

La riga deve rappresentare almeno: famiglia/profilo, materia, concetto/sotto-concetti, frequenza/peso, fonti, collocazione, copertura teorica, applicazione, output concorsuale, verifica, stato, review normativa, destinazione rinvio.

## Regole

- `solo-nominato`, `mancante`, `parziale` => blocker.
- `rinviato` senza destinazione precisa => blocker.
- fonte consolidata mancante => warning.
- stato non valido => blocker.
- `completo` con campi teorici/applicativi/verifica vuoti => blocker.
- parser/audit non modificano file.

## TDD

1. Scrivere test per: riga completa; solo-nominato; rinvio senza destinazione; fonte mancante; stato invalido; completo con copertura vuota.
2. Eseguire test e registrare il fallimento iniziale.
3. Implementare il minimo necessario.
4. Creare template Markdown con tutte le colonne.
5. Creare CLI che scansiona ricorsivamente `*-matrice-copertura-didattica.md`, stampa riepilogo e termina 1 con blocker.
6. Aggiungere a package.json: `"audit:coverage": "node scripts/audit-didactic-coverage.mjs"`.

Nota: Node non importa TypeScript direttamente. La CLI può contenere una piccola implementazione JS equivalente oppure leggere un modulo JS condiviso, ma i test devono coprire l'API TypeScript. Evita dipendenze nuove.

## Verification

```powershell
npx vitest run tests/didactic-coverage.test.ts
npm test
npm run typecheck
npm run audit:coverage
git diff --check -- wiki/templates/didactic-coverage-matrix-template.md src/server/editorial/didactic-coverage.ts scripts/audit-didactic-coverage.mjs tests/didactic-coverage.test.ts package.json
```

L'audit senza matrici deve uscire 0 con messaggio esplicito; quando le matrici esisteranno, blocker editoriali devono produrre exit 1 senza crash.

Committare soltanto i cinque file con messaggio `feat: add didactic coverage audit`.

Scrivere `.superpowers/sdd/task-2-report.md` con stato ammesso, red/green evidence, test, commit e concerns.
