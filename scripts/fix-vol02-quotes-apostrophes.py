#!/usr/bin/env python3
"""Convert straight apostrophes/quotes to Italian typographic marks in VOL-02 chapters.

Only touches the markdown body (never YAML frontmatter), and never touches
fenced code blocks or inline code spans. Apostrophes (elision, e.g. "dell'ente")
become U+2019. Straight double-quote pairs become curly double quotes, matched
per line (verified beforehand: every body line has an even count of straight
double quotes, so per-line toggling is safe and cannot desynchronize).
"""

from __future__ import annotations

import glob
import re

CODE_FENCE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]*`")


def protect_code(body: str) -> tuple[str, list[str]]:
    placeholders: list[str] = []

    def stash(match: re.Match[str]) -> str:
        placeholders.append(match.group(0))
        return f"\x00CODE{len(placeholders) - 1}\x00"

    body = CODE_FENCE.sub(stash, body)
    body = INLINE_CODE.sub(stash, body)
    return body, placeholders


def restore_code(body: str, placeholders: list[str]) -> str:
    for i, original in enumerate(placeholders):
        body = body.replace(f"\x00CODE{i}\x00", original)
    return body


def convert_quotes_per_line(text: str) -> str:
    lines = text.split("\n")
    out = []
    for line in lines:
        if line.count('"') % 2 != 0:
            out.append(line)
            continue
        chars = list(line)
        opening = True
        for i, ch in enumerate(chars):
            if ch == '"':
                chars[i] = "“" if opening else "”"
                opening = not opening
        out.append("".join(chars))
    return "\n".join(out)


def fix_body(body: str) -> str:
    protected, placeholders = protect_code(body)
    protected = protected.replace("'", "’")
    protected = convert_quotes_per_line(protected)
    return restore_code(protected, placeholders)


def fix_file(path: str) -> bool:
    original = open(path, encoding="utf-8").read()
    if not original.startswith("---\n"):
        return False
    end = original.find("\n---\n", 4)
    if end == -1:
        return False
    frontmatter_end = end + len("\n---\n")
    frontmatter = original[:frontmatter_end]
    body = original[frontmatter_end:]
    new_body = fix_body(body)
    updated = frontmatter + new_body
    if updated != original:
        open(path, "w", encoding="utf-8", newline="\n").write(updated)
        return True
    return False


def main() -> None:
    files = sorted(glob.glob("wiki/books/moduli/m-fl0*/chapters/*.md"))
    changed = sum(fix_file(f) for f in files)
    print(f"changed {changed} of {len(files)} files")


if __name__ == "__main__":
    main()
