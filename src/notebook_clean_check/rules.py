from __future__ import annotations

from notebook_clean_check.models import Rule

PROJECT_NAME = 'notebook-clean-check'
DESCRIPTION = 'Audit notebook files for outputs, hidden state, and risky local paths.'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "service", "dataset", "route", "metric", "field", "path")
HIGH_SAMPLE = (
                  '"outputs": [{"text": "secret result"}], execution_count: 42, /Users/alic'
                  'e/private.csv'
              )
MEDIUM_SAMPLE = 'execution_count\\s*[:=]\\s*[1-9]'
CLEAN_SAMPLE = '"cells": [{"cell_type": "markdown", "source": "experiment notes"}]'

RULES = (
    Rule(
        code='committed-output',
        severity='high',
        pattern='\\"outputs\\"\\s*:\\s*\\[\\s*\\{',
        message='notebook output appears to be committed',
        recommendation='Clear outputs before review or store artifacts separately.',
    ),
    Rule(
        code='execution-state',
        severity='medium',
        pattern='execution_count\\s*[:=]\\s*[1-9]',
        message='execution count indicates hidden runtime state',
        recommendation='Restart and run all cells before sharing.',
    ),
    Rule(
        code='local-path',
        severity='low',
        pattern='(/Users/|C:\\\\\\\\Users\\\\\\\\|/home/).{1,80}',
        message='local machine path detected',
        recommendation='Replace local paths with project-relative paths or parameters.',
    ),
)
