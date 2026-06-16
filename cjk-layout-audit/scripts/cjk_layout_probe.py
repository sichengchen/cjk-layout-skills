#!/usr/bin/env python3
"""Triage CJK layout signals in text, HTML/XHTML, CSS, and EPUB files."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import zipfile
from pathlib import Path
from typing import Iterable


CJK_RANGES = {
    "han": re.compile(r"[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]"),
    "hiragana": re.compile(r"[\u3040-\u309F]"),
    "katakana": re.compile(r"[\u30A0-\u30FF\u31F0-\u31FF]"),
    "hangul": re.compile(r"[\u1100-\u11FF\u3130-\u318F\uAC00-\uD7AF]"),
    "bopomofo": re.compile(r"[\u3100-\u312F\u31A0-\u31BF]"),
}

LINE_START_FORBIDDEN = set("，、。．！？；：」』）］｝〉》】〕〗〙〛ぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮ々ー")
LINE_END_FORBIDDEN = set("「『（［｛〈《【〔〖〘〚")
CSS_PROPS = [
    "writing-mode",
    "text-orientation",
    "line-break",
    "word-break",
    "overflow-wrap",
    "text-spacing",
    "text-autospace",
    "text-justify",
    "text-align",
    "letter-spacing",
    "font-family",
    "font-feature-settings",
    "ruby-position",
]


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def strip_markup(text: str) -> str:
    text = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    return html.unescape(text)


def iter_epub_items(path: Path) -> Iterable[tuple[str, str]]:
    with zipfile.ZipFile(path) as zf:
        for name in zf.namelist():
            lower = name.lower()
            if lower.endswith((".html", ".xhtml", ".htm", ".css", ".txt")):
                data = zf.read(name).decode("utf-8", errors="replace")
                yield name, data


def detect_scripts(text: str) -> dict[str, int]:
    return {name: len(pattern.findall(text)) for name, pattern in CJK_RANGES.items()}


def infer_languages(counts: dict[str, int]) -> list[str]:
    langs: list[str] = []
    if counts["hiragana"] or counts["katakana"]:
        langs.append("ja")
    if counts["hangul"]:
        langs.append("ko")
    if counts["han"] and not (counts["hiragana"] or counts["katakana"]):
        langs.append("zh-or-ja")
    if counts["bopomofo"]:
        langs.append("zh-Hant-bopomofo")
    return langs or ["none-detected"]


def css_signals(text: str) -> list[dict[str, str]]:
    signals = []
    for prop in CSS_PROPS:
        for match in re.finditer(rf"(?i)\b{re.escape(prop)}\s*:\s*([^;}}]+)", text):
            signals.append({"property": prop, "value": match.group(1).strip()})
    return signals


def markup_signals(text: str) -> dict[str, int]:
    return {
        "ruby_elements": len(re.findall(r"(?i)<ruby\b", text)),
        "rt_elements": len(re.findall(r"(?i)<rt\b", text)),
        "lang_attributes": len(re.findall(r"(?i)\b(?:xml:)?lang\s*=", text)),
        "vertical_classes": len(re.findall(r"(?i)(vertical|tate|縦|直排|세로)", text)),
    }


def line_boundary_risks(text: str, limit: int = 50) -> list[dict[str, str | int]]:
    risks = []
    for idx, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        first = stripped[0]
        last = stripped[-1]
        if first in LINE_START_FORBIDDEN:
            risks.append({"line": idx, "type": "forbidden_line_start_candidate", "char": first, "text": stripped[:80]})
        if last in LINE_END_FORBIDDEN:
            risks.append({"line": idx, "type": "forbidden_line_end_candidate", "char": last, "text": stripped[-80:]})
        if len(risks) >= limit:
            break
    return risks


def mixed_script_spacing(text: str, limit: int = 50) -> list[dict[str, str | int]]:
    risks = []
    pattern = re.compile(r"([\u3040-\u30FF\u3400-\u9FFF\uAC00-\uD7AF])([A-Za-z0-9])|([A-Za-z0-9])([\u3040-\u30FF\u3400-\u9FFF\uAC00-\uD7AF])")
    for match in pattern.finditer(text):
        start = max(0, match.start() - 20)
        end = min(len(text), match.end() + 20)
        risks.append({"offset": match.start(), "type": "adjacent_cjk_latin_or_digit", "context": text[start:end].replace("\n", " ")})
        if len(risks) >= limit:
            break
    return risks


def analyze_unit(path_label: str, raw: str) -> dict:
    plain = strip_markup(raw)
    counts = detect_scripts(plain)
    return {
        "path": path_label,
        "script_counts": counts,
        "inferred_languages": infer_languages(counts),
        "markup_signals": markup_signals(raw),
        "css_signals": css_signals(raw),
        "line_boundary_risks": line_boundary_risks(plain),
        "mixed_script_spacing_risks": mixed_script_spacing(plain),
    }


def analyze_path(path: Path) -> list[dict]:
    if path.suffix.lower() == ".epub":
        return [analyze_unit(f"{path}!/{name}", data) for name, data in iter_epub_items(path)]
    return [analyze_unit(str(path), read_file(path))]


def main() -> int:
    parser = argparse.ArgumentParser(description="Triage CJK layout signals in local files.")
    parser.add_argument("paths", nargs="+", help="Text, HTML/XHTML, CSS, or EPUB files to inspect")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a compact text summary")
    args = parser.parse_args()

    results = []
    for raw_path in args.paths:
        path = Path(raw_path)
        if not path.exists():
            results.append({"path": raw_path, "error": "not_found"})
            continue
        try:
            results.extend(analyze_path(path))
        except Exception as exc:  # noqa: BLE001 - CLI should report per-file failures.
            results.append({"path": raw_path, "error": str(exc)})

    if args.json:
        print(json.dumps({"results": results}, ensure_ascii=False, indent=2))
    else:
        for item in results:
            print(f"{item['path']}")
            if "error" in item:
                print(f"  error: {item['error']}")
                continue
            print(f"  languages: {', '.join(item['inferred_languages'])}")
            print(f"  scripts: {item['script_counts']}")
            print(f"  markup: {item['markup_signals']}")
            if item["css_signals"]:
                props = ", ".join(f"{s['property']}={s['value']}" for s in item["css_signals"][:8])
                print(f"  css: {props}")
            print(f"  line-boundary risks: {len(item['line_boundary_risks'])}")
            print(f"  mixed-script spacing risks: {len(item['mixed_script_spacing_risks'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
