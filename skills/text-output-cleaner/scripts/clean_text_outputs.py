#!/usr/bin/env python3
"""Clean text-file output formatting locally."""

from __future__ import annotations

import argparse
import fnmatch
import os
import re
import sys
import time
import unicodedata
from pathlib import Path
from typing import Optional


DEFAULT_PATTERNS = ("*.txt", "*.md", "*.csv", "*.tsv")
SKIP_DIRS = {".git", ".hg", ".svn", "__pycache__", "node_modules", ".venv", "venv"}

HIDDEN_CHARS = {
    "\u200b",
    "\u2060",
    "\ufeff",
    "\u00ad",
}

# These are format characters, but they are meaningful in scripts and emoji
# sequences (for example, an emoji sequence joined with U+200D). Never remove
# them as generic Cf characters.
PRESERVED_FORMAT_CHARS = {"\u200c", "\u200d"}

DASH_TRANSLATION = str.maketrans(
    {
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2015": "-",
        "\u2212": "-",
    }
)

QUOTE_TRANSLATION = str.maketrans(
    {
        "\u2018": "'",
        "\u2019": "'",
        "\u201a": "'",
        "\u201b": "'",
        "\u2032": "'",
        "\u2035": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u201e": '"',
        "\u201f": '"',
        "\u2033": '"',
        "\u2036": '"',
    }
)


def clean_text(
    text: str,
    *,
    remove_asterisks: bool = False,
    remove_markdown_headings: bool = False,
    delimited: bool = False,
) -> str:
    text = "".join(ch for ch in text if ch not in HIDDEN_CHARS)
    if not delimited:
        text = text.replace("\u00a0", " ").replace("\u202f", " ").replace("\u2007", " ")
        text = text.translate(DASH_TRANSLATION)
        text = text.translate(QUOTE_TRANSLATION)
        text = text.replace("\u2026", "...")

    kept_chars: list[str] = []
    for ch in text:
        category = unicodedata.category(ch)
        if category == "Cf" and ch not in PRESERVED_FORMAT_CHARS:
            continue
        if category == "Cc" and ch not in "\n\r\t":
            continue
        kept_chars.append(ch)
    text = "".join(kept_chars)

    if remove_asterisks:
        text = text.replace("*", "")

    lines = text.splitlines(keepends=True)
    if not lines:
        return text.rstrip()

    cleaned_lines = []
    in_code_fence = False
    for line in lines:
        newline = ""
        body = line
        if line.endswith("\r\n"):
            body = line[:-2]
            newline = "\r\n"
        elif line.endswith("\n") or line.endswith("\r"):
            body = line[:-1]
            newline = line[-1]

        if not delimited:
            body = body.rstrip()
        stripped = body.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_fence = not in_code_fence
        elif not in_code_fence and not delimited:
            body = collapse_repeated_spaces(body)
        if remove_markdown_headings and not delimited:
            body = remove_markdown_heading_prefix(body)
        cleaned_lines.append(body + newline)

    return "".join(cleaned_lines)


def collapse_repeated_spaces(line: str) -> str:
    leading = len(line) - len(line.lstrip(" "))
    return line[:leading] + re.sub(r" {2,}", " ", line[leading:])


def remove_markdown_heading_prefix(line: str) -> str:
    stripped = line.lstrip()
    indent = line[: len(line) - len(stripped)]
    if stripped.startswith("#"):
        hashes = len(stripped) - len(stripped.lstrip("#"))
        if 1 <= hashes <= 6 and stripped[hashes : hashes + 1] == " ":
            return indent + stripped[hashes + 1 :]
    return line


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    tmp = path.with_name(f".{path.name}.tmp")
    # Path.write_text(newline=...) is not available on Python 3.9.
    with tmp.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    tmp.replace(path)


def matches(path: Path, patterns: tuple[str, ...]) -> bool:
    return any(fnmatch.fnmatch(path.name.lower(), pattern.lower()) for pattern in patterns)


def iter_files(root: Path, patterns: tuple[str, ...]) -> list[Path]:
    if root.is_file():
        return [root] if matches(root, patterns) else []

    files: list[Path] = []
    for current_root, dirs, names in os.walk(root):
        dirs[:] = [name for name in dirs if name not in SKIP_DIRS]
        current = Path(current_root)
        for name in names:
            path = current / name
            if matches(path, patterns):
                files.append(path)
    return files


def destination_for(path: Path, base: Path, out_dir: Optional[Path]) -> Path:
    if out_dir is None:
        return path
    if base.is_file():
        return out_dir / path.name
    return out_dir / path.relative_to(base)


def clean_file(
    path: Path,
    *,
    base: Path,
    out_dir: Optional[Path],
    remove_asterisks: bool,
    remove_markdown_headings: bool,
    delimited: bool = False,
) -> bool:
    original = read_text(path)
    cleaned = clean_text(
        original,
        remove_asterisks=remove_asterisks,
        remove_markdown_headings=remove_markdown_headings,
        delimited=delimited,
    )
    if cleaned == original:
        return False

    dest = destination_for(path, base, out_dir)
    dest.parent.mkdir(parents=True, exist_ok=True)
    write_text(dest, cleaned)
    return True


def clean_once(args: argparse.Namespace) -> tuple[int, int]:
    root = args.path.resolve()
    out_dir = args.out_dir.resolve() if args.out_dir else None
    files = iter_files(root, args.patterns)
    changed = 0

    for path in files:
        delimited = path.suffix.lower() in {".csv", ".tsv"}
        if clean_file(
            path,
            base=root,
            out_dir=out_dir,
            remove_asterisks=args.remove_asterisks,
            remove_markdown_headings=args.remove_markdown_headings,
            delimited=delimited,
        ):
            changed += 1
            print(f"cleaned: {path}")

    return changed, len(files)


def watch(args: argparse.Namespace) -> None:
    seen: dict[Path, float] = {}
    print(f"watching {args.path.resolve()} for {', '.join(args.patterns)}", flush=True)
    while True:
        for path in iter_files(args.path.resolve(), args.patterns):
            try:
                mtime = path.stat().st_mtime
            except FileNotFoundError:
                continue
            if seen.get(path) == mtime:
                continue
            seen[path] = mtime
            changed = clean_file(
                path,
                base=args.path.resolve(),
                out_dir=args.out_dir.resolve() if args.out_dir else None,
                remove_asterisks=args.remove_asterisks,
                remove_markdown_headings=args.remove_markdown_headings,
                delimited=path.suffix.lower() in {".csv", ".tsv"},
            )
            if changed:
                print(f"cleaned: {path}", flush=True)
        time.sleep(args.interval)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Clean hidden characters and formatting quirks from text outputs."
    )
    parser.add_argument("path", nargs="?", default=".", type=Path)
    parser.add_argument(
        "--patterns",
        default=",".join(DEFAULT_PATTERNS),
        help="Comma-separated glob patterns. Default: *.txt,*.md,*.csv,*.tsv",
    )
    parser.add_argument("--out-dir", type=Path, help="Write cleaned copies here.")
    parser.add_argument("--watch", action="store_true", help="Keep cleaning changed files.")
    parser.add_argument(
        "--interval",
        type=float,
        default=1.0,
        help="Seconds between scans in watch mode. Default: 1.0",
    )
    parser.add_argument(
        "--remove-asterisks",
        action="store_true",
        help="Remove '*' characters. Off by default because it changes Markdown meaning.",
    )
    parser.add_argument(
        "--remove-markdown-headings",
        action="store_true",
        help="Strip leading Markdown heading markers. Off by default.",
    )
    args = parser.parse_args(argv)
    args.patterns = tuple(pattern.strip() for pattern in args.patterns.split(",") if pattern.strip())
    if not args.patterns:
        parser.error("--patterns must include at least one glob")
    return args


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if not args.path.exists():
        print(f"error: path does not exist: {args.path}", file=sys.stderr)
        return 2

    if args.watch:
        watch(args)
        return 0

    changed, total = clean_once(args)
    print(f"done: {changed}/{total} file(s) changed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
