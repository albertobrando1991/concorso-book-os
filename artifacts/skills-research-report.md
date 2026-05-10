# Skills research report

Date: 2026-05-10

## Sources checked

- OpenAI Agent Skills for Codex: https://developers.openai.com/codex/skills
- OpenAI skills catalog: https://github.com/openai/skills
- Agent Skills open standard: https://agentskills.io/home
- Agent Skills best practices: https://agentskills.io/skill-creation/best-practices
- GitHub `codex-skills` topic: https://github.com/topics/codex-skills

## Findings

- Skills are the right mechanism for repeatable project-specific behavior because they package instructions, workflows, scripts, references, and templates.
- Project-specific skill material should live in a repository-scoped skills directory so it can be versioned and shared with the project.
- Effective skills should stay focused, use progressive disclosure, include concrete output templates, and encode project-specific gotchas instead of generic advice.
- The official OpenAI skills catalog is useful for generic workflows such as skill creation, installation, CLI creation, GitHub workflows, and external tools.
- For ConcorsoBook OS, generic marketplace skills are less important than a custom professional writing skill tied to Metodo BANDO, the LLM Wiki rules, Obsidian traceability, and the Italian public competition domain.

## Recommended skill stack for ConcorsoBook OS

1. `concorso-book-professional-writer`
   - Status: implemented in `.agents/skills/concorso-book-professional-writer/SKILL.md`.
   - Purpose: professional chapter writing, rewriting, formatting, expansion, and review.
   - Reason: this is the highest-value custom skill because the product depends on editorial quality.

2. `skill-creator`
   - Status: available system skill.
   - Purpose: maintain and evolve project skills.
   - Reason: the project will need specialized skills for ingest, legal lint, book revision, and Obsidian workflows.

3. `modern-web-development`
   - Status: available local skill.
   - Purpose: Next.js dashboard, API routes, Supabase/Vercel evolution.
   - Reason: the dashboard is a core supervision surface.

4. `systematic-debugging`
   - Status: available local skill.
   - Purpose: debug server, Obsidian, Codex CLI, and test failures.
   - Reason: this project has multiple moving parts and long-running workflows.

5. `supabase-postgres-best-practices`
   - Status: available local skill.
   - Purpose: future multi-PC and staff collaboration layer.
   - Reason: use only when Supabase becomes canonical for shared app state; the markdown vault remains canonical knowledge.

6. `openai-docs`
   - Status: available system skill.
   - Purpose: current Codex/OpenAI docs, model/API decisions, official guidance.
   - Reason: use for provider/configuration decisions, but not as default writing provider when the user wants to use Codex subscription.

7. `cli-creator` from official catalog
   - Status: candidate, not installed.
   - Purpose: create durable CLIs for repeated vault operations if dashboard actions become too complex.
   - Reason: useful later for stable commands such as `ingest-source`, `compile-book`, `lint-vault`.

## Decision

The project should not install many third-party skills immediately. The strongest path is:

- create and version a focused project writing skill;
- inject that skill automatically into the Manual Writer Agent;
- keep generic skills as support tools for development and maintenance;
- add more project-specific skills only after real workflows expose recurring mistakes.

## Implemented outcome

- Added project skill: `.agents/skills/concorso-book-professional-writer/SKILL.md`.
- Manual Writer Agent now loads this skill and includes it in the `codex exec` writing prompt.
- Writer provider defaults to `WRITER_PROVIDER=codex`, using Codex CLI instead of requiring `OPENAI_API_KEY`.
