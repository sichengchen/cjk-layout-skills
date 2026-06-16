# CJK Layout Audit Artifact Contract

Use this contract for deep audits, `/goal` loops, and subagent fanout. For small one-page checks, use the same report fields inline without creating every artifact, and treat `/goal` creation as optional unless the user explicitly asked for it.

## Path Layout

Default base path:

```text
/tmp/cjk-layout-audits/<target-name>/<audit-id>/
  plan.md
  artifacts/
    01_context/
      target_inventory.md
      source_probe.json
    02_evidence/
      screenshots/
      rendered-pages/
      extracted-text/
    03_receipts/
      <surface-id>.md
    04_reconciliation/
      findings.jsonl
      coverage_matrix.md
  report.md
```

Use a user-provided output path when supplied. Keep screenshots and rendered page images alongside the final report or link to their stable paths.

When the user says not to edit files, interpret that as no modification to the audited target or repository. It is still acceptable to write temporary audit evidence under `/tmp` or the agreed audit output directory, including screenshots, DOM dumps, extracted text, and probe output. Mention these generated artifacts explicitly.

## Target Inventory

`target_inventory.md` must list:

- audit target and access method
- declared surfaces: routes, pages, chapters, components, screenshots, or files
- language/locale assumptions
- viewport or page-size matrix
- in-scope W3C sources: JLReq, CLReq, KLReq
- explicit exclusions and reason

## Receipt Schema

Each owned surface receipt must contain:

```markdown
# Receipt: <surface-id>

- Status: pass | finding | not_applicable | deferred
- Owner: parent | subagent:<id/name>
- Target: <URL/page/chapter/file/component>
- Language/script: <ja|zh-Hans|zh-Hant|ko|mixed|unknown>
- Writing mode: <horizontal|vertical|mixed|unknown>
- Evidence inspected: <screenshots, DOM, CSS, text extraction, rendered pages>
- Requirement families checked: <list>

## Findings

### <finding-id or title>
- Severity: critical | high | medium | low | info
- Confidence: high | medium | low
- W3C mapping: <JLReq/CLReq/KLReq section/family>
- Evidence: <artifact path and exact visual/text cue>
- Affected implementation: <selector/file/page/component or unknown>
- Remediation: <specific fix>

## Closures

- <family>: pass | not_applicable | deferred - <evidence/reason>
```

## Subagent Ownership

Use subagents when the audit has multiple routes/pages, multiple languages, multiple viewports, or both source and rendered artifacts. Assign disjoint ownership:

- route/page worker: one route group or ebook chapter range
- language worker: one locale/script across shared surfaces
- requirement worker: one family such as ruby/annotations, punctuation/line breaking, or page/book layout
- evidence worker: screenshot/render collection only, with no final severity decisions

Every subagent must write or return a receipt. The parent agent owns:

- target inventory
- `/goal` status
- subagent prompt construction
- artifact path assignment
- deduplication and final severity
- final report

## Goal Loop

Create or adopt a `/goal` for non-trivial audits. A non-trivial audit has more than one declared surface, more than one viewport/page render, more than one language/script, subagent fanout, or a requested report artifact. Do not mark it complete until:

- `target_inventory.md` exists or the final report includes an equivalent inventory
- every declared surface has a receipt or explicit closure
- every finding has rendered/extracted evidence and W3C mapping
- deferred scope is explicit and justified
- `report.md` exists or the final answer includes the complete report requested by the user

If a runtime lacks goal tools, state the same closure contract in the first audit update and follow it manually. In Claude Code, mirror the `/goal` loop with TodoWrite or the available task list and keep the same completion gates. In Codex, use goal tools when exposed and do not complete the goal before this contract is satisfied.

## Final Report Shape

Use this structure:

```markdown
# CJK Layout Audit Report

## Summary
- Target:
- Date:
- Overall result:
- Highest severity:

## Coverage
<matrix by surface, language, viewport/page, requirement families, status>

## Findings
### <severity> - <title>
- Affected surface:
- Language/script:
- W3C mapping:
- Evidence:
- Impact:
- Remediation:
- Confidence:

## Passes And Closures
<important checked areas with no finding>

## Deferred Or Out Of Scope
<explicit gaps and why>

## Artifacts
<screenshots, probe output, rendered page images>
```

Do not bury severe findings in prose. Keep remediation actionable enough for frontend, ebook, or document-generation engineers to implement.
