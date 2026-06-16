# CJK Layout Audit Skill

This repository contains the `cjk-layout-audit` Codex skill for auditing Chinese, Japanese, and Korean text layout in frontend pages, rendered webpages, EPUB/ebook content, PDFs, screenshots, and source files.

The skill is based on W3C text layout requirements:

- [JLReq: Requirements for Japanese Text Layout](https://www.w3.org/TR/jlreq/)
- [CLReq: Requirements for Chinese Text Layout](https://www.w3.org/TR/clreq/)
- [KLReq: Requirements for Hangul Text Layout and Typography](https://www.w3.org/TR/klreq/)

## Contents

- `cjk-layout-audit/SKILL.md` - main skill instructions and workflow.
- `cjk-layout-audit/references/audit-model.md` - W3C requirement families, severity rules, and evidence standards.
- `cjk-layout-audit/references/artifact-contract.md` - `/goal` loop, subagent, artifact, receipt, and report contract.
- `cjk-layout-audit/scripts/cjk_layout_probe.py` - helper script for local text, HTML/XHTML, CSS, and EPUB triage.
- `cjk-layout-audit/agents/openai.yaml` - UI metadata for the skill.

## Use

Invoke the skill from Codex with:

```text
Use $cjk-layout-audit to audit this CJK webpage or ebook for W3C text layout issues.
```

For non-trivial audits, the skill instructs agents to use a `/goal` loop, split coverage across subagents, require surface-level receipts, and complete only after the declared audit scope is closed.

## Probe Script

Run the helper script on local files to identify CJK script coverage, relevant CSS properties, ruby markup, suspicious line-boundary punctuation, and mixed CJK/Latin spacing leads:

```bash
python3 cjk-layout-audit/scripts/cjk_layout_probe.py --json path/to/file.html
```

The probe output is triage only. The skill requires rendered or extracted evidence before reporting a layout finding.

## Validation

Basic local checks used during creation:

```bash
python3 -B cjk-layout-audit/scripts/cjk_layout_probe.py --json path/to/file.html
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile cjk-layout-audit/scripts/cjk_layout_probe.py
```

The official skill validator can be run when its Python dependencies are available:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py cjk-layout-audit
```
