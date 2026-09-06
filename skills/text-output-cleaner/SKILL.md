---
name: text-output-cleaner
description: Clean hidden formatting characters from local text output without corrupting Markdown, CSV, TSV, code, or emoji. Use when text files contain zero-width artifacts, BOMs, control characters, inconsistent punctuation, trailing spaces, or noisy generated output.
---

# Text Output Cleaner

Use the bundled local script to clean text files conservatively. It is a formatting utility, not a content editor or data normalizer.

## Command

```bash
python3 ~/.codex/skills/text-output-cleaner/scripts/clean_text_outputs.py <path>
```

Useful options:

```bash
--out-dir <directory>       # write cleaned copies; do not overwrite source files
--patterns '*.md,*.txt'     # override the default file globs
--watch                     # clean newly changed matching files
--interval 1.0              # watch scan interval in seconds
--remove-asterisks          # explicit Markdown-destructive option
--remove-markdown-headings  # explicit Markdown-destructive option
```

Default patterns are `*.txt,*.md,*.csv,*.tsv`. The script skips VCS directories, virtual environments, caches, and `node_modules`.

## Safety behavior

- Preserves emoji and script joiners (`U+200D` ZWJ and `U+200C` ZWNJ), including family/profession emoji sequences.
- Removes only known unsafe hidden formatting characters and non-line control characters by default.
- For Markdown/plain text, normalizes selected spaces, dash/quote variants, ellipses, trailing whitespace, and repeated spaces outside fenced code.
- For CSV/TSV, performs only the hidden/control-character cleanup. It does **not** collapse spaces, trim fields, normalize punctuation, strip headings, or rewrite delimiters/quotes. This avoids changing meaningful cell values.
- `--remove-asterisks` and `--remove-markdown-headings` are opt-in because they can change document meaning.
- Writes through a same-directory temporary file and replacement, using a Python 3.9-compatible file-writing path.

## Workflow

1. Inspect the target path and file types before running.
2. Prefer `--out-dir` when the source is important or uncommitted.
3. Run the cleaner once, inspect the changed-file count, and review representative output.
4. For CSV/TSV, spot-check row/column structure and values; for Markdown, spot-check fenced code, headings, links, tables, and emoji.
5. Do not run `--watch` on a directory that contains its own output directory or generated files unless the scope is intentional.

Never use this skill to remove secrets, redact regulated data, or make semantic edits. Those require a source-specific workflow and explicit review.
