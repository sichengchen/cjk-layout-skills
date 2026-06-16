---
name: cjk-layout-audit
description: Audit Chinese, Japanese, or Korean text layout in frontend pages, web apps, rendered webpages, EPUB/ebook content, PDFs, screenshots, or source files against W3C JLReq, CLReq, and KLReq. Use when the user asks to inspect CJK typography, line breaking, punctuation placement, ruby/annotation layout, vertical writing, mixed Latin/CJK text, spacing, justification, page/book layout, ebook rendering, or locale-specific CJK text quality; also use for deep multi-agent layout audits that should run through the /goal loop.
---

# CJK Layout Audit

Audit visible Chinese, Japanese, and Korean text layout against W3C text layout requirements. Treat the W3C documents as requirements references, not as a generic typography checklist: connect each finding to a concrete rendered defect, affected language/script, and source requirement area.

## Required References

Load these files as needed:

- `references/audit-model.md`: W3C source map, language-specific audit areas, severity rules, and evidence standards.
- `references/artifact-contract.md`: `/goal` loop setup, scan artifact paths, subagent ownership, report schema, and completion gates.

Use `scripts/cjk_layout_probe.py` for deterministic triage of local text, HTML/XHTML, CSS, or EPUB files. The script surfaces CJK scripts, suspicious line-boundary punctuation, mixed-script spacing signals, and CSS properties relevant to writing mode, line breaking, spacing, and ruby.

## Workflow

1. Resolve the audit target.
   - For a live frontend/webpage, identify the URL, route list, viewport matrix, locale, and whether login/state is required.
   - For source files, identify rendered entry points and the build command when possible.
   - For EPUB/ebook/PDF/screenshots, identify the reading system, pages/chapters, writing direction, and target output format.
2. Create or adopt a `/goal` for any audit with multiple surfaces, multiple languages, multiple viewports/page renders, subagents, or a final artifact bundle. For a tiny one-surface inline check, a `/goal` is optional; still use the same coverage and closure rules in the final answer. In Codex, use goal tools when available. In Claude Code or another runtime without native goal tools, maintain the same closure contract with the runtime's task/todo mechanism and visible progress updates. Use an objective like:

   `Run the CJK Layout Audit for <target>; do not stop until every declared surface has either a completed layout review receipt or explicit deferred closure, and the final markdown report is written.`

3. Read `references/audit-model.md`, then build the audit plan:
   - classify language coverage as `ja`, `zh-Hans`, `zh-Hant`, `ko`, or mixed/unknown
   - classify surfaces by route/page/chapter/component/screenshot
   - choose the applicable W3C requirement families
   - define a viewport/page matrix that includes mobile, desktop, high zoom or large text when relevant, and vertical-writing states when present
4. Run source/content triage.
   - Use `scripts/cjk_layout_probe.py --json <paths...>` on local files when available.
   - Treat probe output as leads only. Confirm all findings through rendered output, DOM/CSS inspection, ebook extraction, or screenshot/PDF evidence.
5. Capture rendered evidence.
   - For webpages, use browser tools or Playwright to capture screenshots and inspect computed styles for affected text.
   - For ebooks/PDFs, extract representative text and render page/chapter images when layout matters.
   - Record viewport, page/chapter, locale, writing mode, font stack, and affected selector/file when discoverable.
   - If the user says not to edit files, do not modify the target or repository. Temporary evidence files such as screenshots, DOM dumps, extracted text, or probe JSON may still be written under `/tmp` or the agreed audit output directory; state those paths in the report.
6. Use subagents for non-trivial audits.
   - Split work by surface, language, viewport, or requirement family.
   - Give each subagent explicit ownership and a required receipt path from `references/artifact-contract.md`.
   - In Codex, use subagent/thread tools when the user has authorized delegation. In Claude Code, use Task agents when available.
   - Do not let subagents make final severity or dedupe decisions independently; parent owns reconciliation and final report.
7. Reconcile findings.
   - Deduplicate by user-visible defect and remediation, not by W3C section name.
   - Preserve separately affected scripts or independently broken surfaces when one fix would not resolve all of them.
   - Mark checked surfaces as `pass`, `finding`, `not_applicable`, or `deferred` with exact evidence.
8. Write the final report.
   - Include a concise executive summary, coverage matrix, findings ordered by severity, standards mapping, screenshots/artifacts, and deferred/not-applicable scope.
   - If no findings survive, still provide coverage evidence and residual risk.
9. Complete the `/goal` only after every declared surface has a receipt or explicit closure and the final report exists.

## Subagent Brief Pattern

Use a brief shaped like this for each worker:

```text
Use $cjk-layout-audit at <skill path> to audit only <owned surface/language/viewport>.

Do not edit product files. Produce a receipt at <receipt path> with:
- target and exact ownership
- language/script and writing mode observed
- rendered evidence inspected
- W3C requirement families checked
- findings with severity, affected selector/file/page, screenshot/artifact reference, and remediation
- pass/not_applicable/deferred closures for checked areas

Return only your receipt summary and paths.
```

## Hard Rules

- Do not report a CJK layout issue from source heuristics alone. Require rendered or extracted evidence.
- Do not apply Japanese, Chinese, and Korean rules interchangeably. Mixed-script content may require separate checks for each script.
- Do not treat browser defaults as acceptable without checking the visible result.
- Do not quote long W3C passages in reports; cite section names and links, then explain the defect in your own words.
- Do not collapse coverage to "looked at the page." Track each declared surface and applicable requirement family.
- Do not complete a `/goal` while any declared surface lacks a receipt or an explicit deferred/not-applicable closure.
