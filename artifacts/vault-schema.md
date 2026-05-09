# Vault schema

```text
wiki/
  AGENTS.md
  index.md
  log.md
  raw/
    articles/
    laws/
    decrees/
    manuals/
    websites/
    transcripts/
    assets/
  sources/
  topics/
  entities/
  books/
  quizzes/
  reviews/
  templates/
  dashboards/
  logs/
```

## Frontmatter
Base fields: `id`, `type`, `title`, `status`, `domain`, `topics`, `entities`, `source_refs`, `book_refs`, `confidence`, `updated_at`, `created_at`, `review_required`, `canonical`, `tags`.

Type-specific fields:
- Source: `source_type`, `source_url`, `source_date`, `authority_level`
- Topic: `parent_topics`, `child_topics`, `chapter_refs`
- Chapter: `book_id`, `outline_section`, `draft_stage`, `last_compiled_from`
- Review: `issue_type`, `severity`, `affected_pages`

