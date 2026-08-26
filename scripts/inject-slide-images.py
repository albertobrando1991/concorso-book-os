"""Insert unused chapter PNG figures into slide decks."""
from __future__ import annotations

import re
import sys
from pathlib import Path

SLIDES = Path(__file__).resolve().parents[1] / "slides"
VOLUMES = ["VOL-01", "VOL-02", "VOL-03", "VOL-04", "VOL-05"]


def title_from_name(name: str) -> str:
    stem = re.sub(r"-v\d+$", "", Path(name).stem)
    stem = re.sub(r"^\d+-", "", stem)
    return stem.replace("-", " ").strip().capitalize()


def figure_slide(filename: str, volume: str) -> str:
    title = title_from_name(filename)
    return f"""
            <section class="slide ivory">
                <div class="pad">
                    <p class="kicker reveal">Schema</p>
                    <h2 class="h-display section-title reveal d1">{title}</h2>
                    <div class="figure reveal d2">
                        <img src="images/{filename}" alt="{title}">
                    </div>
                </div>
                <div class="foot"><span>Capitale Personale · {volume}</span><span>Figura del capitolo</span></div>
            </section>
"""


def inject(folder: Path, volume: str) -> int:
    html_path = folder / "index.html"
    images = folder / "images"
    if not html_path.exists() or not images.exists():
        return 0
    pngs = sorted(p.name for p in images.glob("*.png"))
    if not pngs:
        return 0
    html = html_path.read_text(encoding="utf-8")
    unused = [name for name in pngs if f"images/{name}" not in html]
    if not unused:
        return 0
    # keep at most 3 extra figure slides to avoid flooding
    unused = unused[:3]
    block = "".join(figure_slide(name, volume) for name in unused)
    marker = "</section>"
    # insert after the cover (first section)
    idx = html.find(marker)
    if idx == -1:
        return 0
    idx = idx + len(marker)
    html = html[:idx] + "\n" + block + html[idx:]
    html_path.write_text(html, encoding="utf-8")
    return len(unused)


def main() -> None:
    volumes = sys.argv[1:] or VOLUMES
    total = 0
    for volume in volumes:
        root = SLIDES / volume
        if not root.exists():
            continue
        for folder in sorted(root.iterdir()):
            if not folder.is_dir():
                continue
            n = inject(folder, volume)
            if n:
                print(f"{volume}/{folder.name}: +{n} figure")
                total += n
    print(f"inserite {total} figure")


if __name__ == "__main__":
    main()
