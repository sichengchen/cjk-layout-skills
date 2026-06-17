---
name: cjk-layout
description: Teach and guide implementation of Chinese, Japanese, and Korean text layout in code according to W3C CLReq, JLReq, and KLReq. Use when designing, building, fixing, or reviewing UI, HTML, CSS, EPUB, PDF, canvas, design-system, or frontend typography behavior for CJK text: writing modes, line breaking, punctuation, ruby or annotations, emphasis marks, mixed Latin/CJK content, fonts, spacing, justification, forms, and page or book layout. For evidence-driven defect reports or broad rendered audits, use cjk-layout-audit instead.
---

# CJK Layout

Build Chinese, Japanese, and Korean text layout deliberately instead of relying on Latin-default typography. Use W3C CLReq, JLReq, and KLReq as requirement sources, cite the exact requirement family or section name, and clearly separate standards requirements from practical CSS or renderer choices.

## Reference Loading

Load only the reference files needed for the task:

- `references/standards-map.md`: Always read first for W3C source selection, shared concepts, and cross-language boundaries.
- `references/implementation-patterns.md`: Read when writing or reviewing HTML/CSS, EPUB, PDF, canvas, or design-system code.
- `references/japanese-layout.md`: Read for Japanese, kana/kanji, vertical Japanese, ruby, emphasis dots, tate-chu-yoko, or JLReq-specific work.
- `references/chinese-layout.md`: Read for Simplified/Traditional Chinese, regional Chinese typography, Bopomofo or romanization annotations, Chinese punctuation, or CLReq-specific work.
- `references/korean-layout.md`: Read for Korean/Hangul, word spacing, Hangul-Latin mixed text, Korean punctuation, or KLReq-specific work.

Use `cjk-layout-audit` for independent rendered audits. Use this skill when the job is to design, implement, fix, or explain CJK layout techniques.

## Workflow

1. Classify the text context before coding.
   - Identify language tag and region: `ja`, `zh-Hans`, `zh-Hant`, `zh-CN`, `zh-TW`, `zh-HK`, `ko`, or mixed.
   - Identify medium: responsive web UI, long-form article, ebook, print/PDF, data table, form, canvas, or design-system component.
   - Identify writing direction: horizontal, vertical, mixed vertical/horizontal, or not applicable.
2. Read `references/standards-map.md`, then the relevant language and implementation reference.
3. Design the semantic text model first.
   - Preserve logical source order.
   - Use correct Unicode characters for language-specific punctuation and symbols.
   - Mark language changes with `lang`; do not expect one CJK font or rule set to cover all scripts.
4. Choose CSS and layout primitives intentionally.
   - Use browser-native text layout features before manual positioning.
   - Use vertical writing properties for vertical text rather than rotating containers.
   - Use ruby, emphasis, line-breaking, and spacing features with progressive fallback where support differs.
5. Verify with real rendered content.
   - Test representative strings, punctuation clusters, mixed Latin/CJK text, narrow widths, large text, and vertical writing when present.
   - Check at least one platform with native CJK fonts for the target language.
   - Treat source-level heuristics as insufficient when visible layout matters.
6. State uncertainty explicitly.
   - If a section is not loaded or the target renderer is unknown, say what still needs checking.
   - Do not present a locale convention as universal unless the relevant reference says so.

## Core Implementation Rules

- Apply Chinese, Japanese, and Korean requirements separately. Shared Han characters do not mean shared typography.
- Set accurate `lang` values on documents, components, and inline spans; many font, glyph, and line-break choices depend on language.
- Prefer locale-aware system font stacks or project-approved CJK fonts. Avoid Latin-only fallbacks that silently render CJK with inconsistent fallback glyphs.
- Avoid `word-break: break-all` as a generic overflow fix. It can damage Korean word spacing, Latin words, and punctuation behavior.
- Avoid using `letter-spacing` to simulate CJK justification or punctuation compression. Use layout features and tested fallbacks.
- Do not insert manual spaces around every CJK/Latin boundary unless the content style guide requires it. Use text-spacing support carefully and provide fallbacks.
- Do not rotate text or glyphs manually for vertical layout. Use `writing-mode`, `text-orientation`, and `text-combine-upright`.
- Do not flatten ruby, Bopomofo, or annotations into plain inline text when semantic markup or target-format annotation support is available.
- Do not assume browser defaults satisfy JLReq, CLReq, or KLReq. Defaults vary by engine, platform, font, and language metadata.
- Do not invent requirement details from memory. If a detail matters, load the relevant reference and cite the W3C section name.

## Output Expectations

When giving implementation guidance, include:

- target language, locale, medium, and writing mode assumptions
- relevant W3C requirement family or section names
- concrete markup/CSS or rendering changes
- browser or reading-system caveats when support is unknown or uneven
- a small set of representative test strings or scenarios

When editing code, keep changes scoped to the text layout surface and add verification notes in the final response.
