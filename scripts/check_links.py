#!/usr/bin/env python3
"""Check local Markdown links for missing files and anchors."""

from __future__ import annotations

import re
import sys
import unicodedata
from functools import lru_cache
from pathlib import Path
from urllib.parse import urldefrag

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
MARKDOWN_FILES = [*sorted(ROOT.glob("*.md")), *sorted(DOCS_DIR.rglob("*.md"))]

MARKDOWN_LINK_RE = re.compile(r'!?\[[^\]]*]\(([^)]+)\)')
HTML_HREF_RE = re.compile(r'href="([^"]+)"')
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:")


def clean_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split(" ", 1)[0]
    return target


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9 _-]", "", text)
    text = re.sub(r"[\s_]+", "-", text).strip("-")
    return text


@lru_cache(maxsize=None)
def anchors_for(path: Path) -> set[str]:
    if not path.exists() or path.suffix.lower() != ".md":
        return set()

    anchors = {"top"}
    text = path.read_text(encoding="utf-8")
    for match in HEADING_RE.finditer(text):
        anchor = slugify(match.group(2))
        if anchor:
            anchors.add(anchor)
    return anchors


def iter_targets(text: str) -> list[str]:
    targets: list[str] = []
    for regex in (MARKDOWN_LINK_RE, HTML_HREF_RE):
        for match in regex.finditer(text):
            targets.append(clean_target(match.group(1)))
    return targets


def resolve_path(source: Path, target_path: str) -> Path:
    if target_path.startswith("/"):
        return (ROOT / target_path.lstrip("/")).resolve()
    return (source.parent / target_path).resolve()


def validate_link(source: Path, target: str) -> list[str]:
    if not target or target.startswith(SKIP_PREFIXES):
        return []

    path_part, anchor = urldefrag(target)
    if not path_part and not anchor:
        return []

    if not path_part and anchor:
        resolved = source
    else:
        resolved = resolve_path(source, path_part)

    errors: list[str] = []

    if not resolved.exists():
        errors.append(f"{source.relative_to(ROOT)} -> {target}: missing target")
        return errors

    if anchor:
        anchors = anchors_for(resolved)
        if anchors and anchor not in anchors:
            errors.append(f"{source.relative_to(ROOT)} -> {target}: missing anchor '#{anchor}'")

    return errors


def main() -> int:
    missing: list[str] = []

    for path in MARKDOWN_FILES:
        if not path.exists():
            missing.append(f"{path.relative_to(ROOT)}: file missing")
            continue

        text = path.read_text(encoding="utf-8")
        for target in iter_targets(text):
            if target.startswith("#"):
                missing.extend(validate_link(path, target))
                continue
            missing.extend(validate_link(path, target))

    if missing:
        print("Broken local links found:")
        for error in sorted(set(missing)):
            print(f"  - {error}")
        return 1

    print(f"Checked {len(MARKDOWN_FILES)} Markdown files. No broken local links found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
