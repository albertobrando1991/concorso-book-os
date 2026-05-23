#!/usr/bin/env python3
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path


def main() -> int:
    load_env_files()
    args = parse_args()

    if not args.url and not args.query:
        fail("Missing --url or --query")

    base_url = normalize_base_url(resolve_base_url())
    secret = os.environ.get("CONCORSOBOOK_WEBHOOK_SECRET") or os.environ.get("HERMES_WEBHOOK_SECRET") or ""
    payload = {
        "url": args.url,
        "query": args.query,
        "title": args.title,
        "sourceType": args.type or "law",
        "chapterPath": normalize_chapter_path(args.chapter),
        "runWriter": to_bool(args.writer),
        "writerMode": "integrate",
        "instruction": args.instruction,
    }

    if args.content_file:
        payload["content"] = Path(args.content_file).read_text(encoding="utf-8")

    payload = {key: value for key, value in payload.items() if value not in (None, "")}
    response = post_json(f"{base_url}/api/hermes/import-source", payload, secret)
    print(format_result(response))
    return 0


def parse_args():
    parser = argparse.ArgumentParser(description="Import a source into ConcorsoBook OS.")
    parser.add_argument("--url")
    parser.add_argument("--query")
    parser.add_argument("--title")
    parser.add_argument("--type", default="law")
    parser.add_argument("--chapter")
    parser.add_argument("--writer", default="false")
    parser.add_argument("--instruction")
    parser.add_argument("--content-file")
    return parser.parse_args()


def load_env_files():
    candidates = [
        os.environ.get("HERMES_ENV_FILE", ""),
        str(Path.home() / ".hermes" / ".env"),
        "/mnt/c/Users/alber/.hermes/.env",
    ]

    for candidate in candidates:
        if candidate:
            load_env_file(Path(candidate))


def load_env_file(path: Path):
    if not path.is_file():
        return

    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        clean = line.strip()
        if not clean or clean.startswith("#") or "=" not in clean:
            continue
        key, value = clean.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def resolve_base_url():
    configured = os.environ.get("CONCORSOBOOK_BASE_URL") or "http://127.0.0.1:3000"

    if is_wsl() and re.search(r"//(127\.0\.0\.1|localhost)(:|/|$)", configured):
        host_ip = wsl_default_gateway()
        if host_ip:
            return re.sub(r"//(127\.0\.0\.1|localhost)(?=:|/|$)", f"//{host_ip}", configured)

    return configured


def is_wsl():
    try:
        version = Path("/proc/version").read_text(encoding="utf-8", errors="ignore").lower()
        return "microsoft" in version or "wsl" in version
    except OSError:
        return False


def wsl_default_gateway():
    try:
        output = subprocess.check_output(["ip", "route"], text=True, stderr=subprocess.DEVNULL)
    except Exception:
        return ""

    for line in output.splitlines():
        parts = line.split()
        if parts[:1] == ["default"] and "via" in parts:
            return parts[parts.index("via") + 1]

    return ""


def post_json(url: str, payload: dict, secret: str):
    body = json.dumps(payload).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    if secret:
        headers["Authorization"] = f"Bearer {secret}"

    request = urllib.request.Request(url, data=body, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            text = response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        fail(f"Import failed {exc.code}: {detail}")
    except urllib.error.URLError as exc:
        fail(f"Import failed: {exc.reason}")

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"raw": text}


def format_result(data):
    changed_files = data.get("ingest", {}).get("changedFiles", [])
    warnings = data.get("warnings", [])
    lines = [
        f"Fonte importata: {data.get('sourceTitle') or 'senza titolo'}",
        f"URL: {data.get('sourceUrl') or ''}",
        f"Fonte wiki: {data.get('sourcePath') or 'non riportata'}",
        f"Markdown raw: {data.get('rawMarkdownPath') or 'non riportato'}",
        f"Capitolo collegato: {data.get('linkedChapterPath') or 'nessuno'}",
        f"Writer: {'eseguito' if data.get('writerResult') else 'non eseguito'}",
        "",
        "File aggiornati:",
    ]
    lines.extend(f"- {item}" for item in changed_files[:12])
    if not changed_files:
        lines.append("- nessun file riportato")
    if warnings:
        lines.extend(["", "Avvisi:"])
        lines.extend(f"- {item}" for item in warnings)
    search = data.get("search")
    if search:
        lines.extend(["", "Ricerca:"])
        lines.append(f"- Query: {search.get('query')}")
        selected = search.get("selected") or {}
        lines.append(f"- Selezionato: {selected.get('title')} ({selected.get('url')})")
    return "\n".join(lines)


def normalize_chapter_path(value):
    if not value:
        return None

    clean = value.strip().strip('"')
    if clean.startswith("books/") and clean.endswith(".md"):
        return clean

    slug = re.sub(r"[^a-z0-9]+", "-", clean.lower()).strip("-")
    return f"books/il-metodo-bando/chapters/{slug}.md"


def normalize_base_url(value):
    return value.rstrip("/")


def to_bool(value):
    return str(value or "").lower() in {"true", "1", "yes", "si", "sì"}


def fail(message):
    print(message, file=sys.stderr)
    raise SystemExit(1)


if __name__ == "__main__":
    raise SystemExit(main())
