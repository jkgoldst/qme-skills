#!/usr/bin/env python3
"""Check skill bundle parity and local documentation links, without executing a model.

Run after build-skill-zip.sh. These checks establish packaging consistency only.
"""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent.parent


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.duplicates = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if identifier := values.get("id"):
            if identifier in self.ids:
                self.duplicates.append(identifier)
            self.ids.add(identifier)
        for key in ("href", "src", "aria-controls", "aria-labelledby"):
            if value := values.get(key):
                self.links.append((key, value))


def check():
    errors = []
    source = ROOT / "skills/qme-env-audit"
    with ZipFile(ROOT / "docs/qme-env-audit.zip") as bundle:
        expected = {"qme-env-audit/" + str(p.relative_to(source)) for p in source.rglob("*") if p.is_file()}
        actual = {entry.filename for entry in bundle.infolist() if not entry.is_dir()}
        if actual != expected:
            errors.append("ZIP file inventory differs from skill source")
        for name in actual & expected:
            if bundle.read(name) != (ROOT / "skills" / name).read_bytes():
                errors.append("Stale ZIP entry: " + name)

    pages = {}
    for path in (ROOT / "docs").glob("*.html"):
        page = Page()
        page.feed(path.read_text())
        pages[path] = page
        errors.extend(f"{path.name}: duplicate ID {value}" for value in page.duplicates)
    for path, page in pages.items():
        for key, value in page.links:
            if key.startswith("aria-"):
                for identifier in value.split():
                    if identifier not in page.ids:
                        errors.append(f"{path.name}: missing ARIA target {identifier}")
                continue
            url = urlsplit(value)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.exists():
                errors.append(f"{path.name}: missing local resource {value}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f"{path.name}: missing fragment {value}")

    for path in [ROOT / "README.md", *source.rglob("*.md")]:
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            url = urlsplit(target)
            if not url.scheme and not url.netloc and url.path:
                if not (path.parent / unquote(url.path)).resolve().exists():
                    errors.append(f"{path.relative_to(ROOT)}: missing reference {target}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"ZIP/source parity and local links passed ({len(pages)} HTML pages).")
    return 0


if __name__ == "__main__":
    sys.exit(check())
