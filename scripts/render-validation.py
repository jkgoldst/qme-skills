#!/usr/bin/env python3
"""Render the validation record's small Markdown subset with no dependencies."""
from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent


def inline(value):
    value = escape(value)
    value = re.sub(r"\[([^]]+)\]\((https://[^)]+)\)", r'<a href="\2">\1</a>', value)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    return re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)


def render(text):
    parts = []
    lines = iter(text.splitlines())
    for line in lines:
        if not line.strip():
            continue
        if line.startswith("```"):
            code = []
            for content in lines:
                if content.startswith("```"):
                    break
                code.append(escape(content))
            parts.append("<pre><code>" + "\n".join(code) + "</code></pre>")
        elif line.startswith("|"):
            headers = line.strip("|").split("|")
            separator = next(lines, "")
            if not re.fullmatch(r"\|(?:\s*:?-+:?\s*\|)+", separator):
                raise ValueError("Expected Markdown table separator")
            table = ['<div class="table-scroll"><table><thead><tr>']
            table.extend("<th>" + inline(value.strip()) + "</th>" for value in headers)
            table.append("</tr></thead><tbody>")
            for row in lines:
                if not row.startswith("|"):
                    if row.strip():
                        raise ValueError("Separate the table from its next block with a blank line")
                    break
                table.append("<tr>")
                table.extend("<td>" + inline(value.strip()) + "</td>" for value in row.strip("|").split("|"))
                table.append("</tr>")
            table.append("</tbody></table></div>")
            parts.append("".join(table))
        elif match := re.match(r"^(#{1,3}) (.*)", line):
            level = len(match[1])
            parts.append(f"<h{level}>" + inline(match[2]) + f"</h{level}>")
        elif line.startswith("- ") or re.match(r"^\d+\. ", line):
            ordered = not line.startswith("- ")
            tag = "ol" if ordered else "ul"
            pattern = r"^\d+\. " if ordered else r"^- "
            items = ["<li>" + inline(re.sub(pattern, "", line)) + "</li>"]
            for item in lines:
                if not re.match(pattern, item):
                    if item.strip():
                        raise ValueError("Separate lists from their next block with a blank line")
                    break
                items.append("<li>" + inline(re.sub(pattern, "", item)) + "</li>")
            parts.append(f"<{tag}>" + "".join(items) + f"</{tag}>")
        else:
            parts.append("<p>" + inline(line) + "</p>")
    return "\n".join(parts)


page = '''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Validation status | QME AI Hero</title><link rel="stylesheet" href="style.css"></head><body><main class="report"><a href="index.html">← Back to the review</a>
<!-- Generated from validation.md by scripts/render-validation.py. -->
''' + render((ROOT / "docs/validation.md").read_text()) + '<p><a href="validation.md">Source validation record</a></p></main></body></html>\n'
(ROOT / "docs/validation.html").write_text(page)
print("Rendered docs/validation.html")
