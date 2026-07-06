<p align="center">
  <img src="assets/readme-cover.svg" alt="Notebook Clean Check cover" width="100%" />
</p>

# Notebook Clean Check

![stack](https://img.shields.io/badge/stack-Python-2563eb?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-16a34a?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-dc2626?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-7c3aed?style=flat-square)

Audit notebook files for outputs, hidden state, and risky local paths.

## Why it exists

Small review tasks are easy to skip when the signal lives in notes, spreadsheets, or loosely formatted exports. `notebook-clean-check` turns those checks into a repeatable command with plain findings and CI-friendly exit codes.

## Quick run

```bash
python -m pip install -e ".[dev]"
notebook-clean-check examples/sample.txt
notebook-clean-check examples/sample.txt --json --fail-on medium
```

## Rule set

| Rule | Severity | What it catches |
| --- | --- | --- |
| `committed-output` | high | notebook output appears to be committed |
| `execution-state` | medium | execution count indicates hidden runtime state |
| `local-path` | low | local machine path detected |

## Input

The reader accepts plain text, JSON, JSONL, and CSV. That keeps it useful for hand-written notes, review exports, and small automation jobs.

## Sample risky input

```text
examples/sample.txt
```

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m notebook_clean_check --help
```

`cli.py` handles arguments, `core.py` reads and evaluates records, and `rules.py` keeps the Notebook Clean Check policy easy to review.
