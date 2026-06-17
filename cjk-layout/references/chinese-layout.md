# Chinese Layout

Use CLReq for Chinese layout decisions: `https://www.w3.org/TR/clreq/`.

## Load These CLReq Sections

- 1.2 Basic features of Chinese script
- 2.1 Writing mode
- 3.1 Fonts & typeface styles
- 5.1 Phrase & section boundaries
- 5.3.1 Emphasis marks
- 5.5 Inline notes & annotations
- 5.5.3 Positioning of Bopomofo ruby
- 6.1.1 Prohibition rules for line start and line end
- 6.1.2 Prohibition rules for unbreakable marks
- 6.1.3 Hanging punctuation at line end
- 6.2 Text alignment & justification
- 6.3.2 Punctuation Width Adjustment
- 6.3.3 Mixed text composition in horizontal writing mode
- 7.1.2 Handling of widows and orphans

## Priorities

- Choose script and region deliberately: Simplified, Traditional, Mainland China, Taiwan, Hong Kong, Macau, Singapore, Malaysia, or another locale.
- Use Chinese font stacks that match the selected script and region; glyph shapes can differ across locales.
- For horizontal Chinese UI, verify CLReq 6.1 through 6.3 line and spacing behavior. For vertical Chinese publishing or editorial contexts, verify CLReq 2.1 writing mode behavior before choosing layout primitives.
- Handle Chinese punctuation width, line-start and line-end prohibition, unbreakable punctuation sequences, hanging punctuation, and mixed Western text.
- Use annotations such as Bopomofo, romanization, bilingual notes, or interlinear comments only with tested rendering support.

## Language Tags

Prefer precise tags:

- `zh-Hans` for Simplified Chinese when region is unknown
- `zh-Hant` for Traditional Chinese when region is unknown
- `zh-CN`, `zh-SG`, `zh-TW`, `zh-HK`, `zh-MO` when regional glyphs or punctuation conventions matter

Do not use bare `zh` when the implementation needs script-specific fonts or region-specific glyph behavior.

## Punctuation And Line Breaking

Plan from CLReq 6.1 and 6.3:

- full-width Chinese punctuation in normal Chinese prose
- prohibition rules for line start and line end
- unbreakable marks and punctuation pairs
- line-end hanging punctuation when the target medium supports it
- different quotation mark preferences by region and product style guide
- ellipsis, dash, middle dot, book title marks, and interlinear punctuation conventions

Avoid replacing Chinese punctuation with ASCII punctuation unless the content style guide explicitly uses ASCII in technical UI copy.

Specific CLReq caveat: section 6.1.3 states that most Chinese publications do not use hanging punctuation at line end, but it also describes when hanging punctuation can be used and gives separate Traditional Chinese horizontal/vertical behavior. Do not claim hanging punctuation is always required for Chinese.

## Mixed Chinese And Western Text

Common cases include brand names, product versions, measurements, dates, file names, URLs, and code. Keep Latin runs readable and avoid breaking them destructively. Test spacing at CJK/Latin boundaries; if the platform lacks reliable automatic spacing, prefer component-level styling over mutating localized content with hard-coded spaces.

## Vertical Chinese

For vertical Chinese in CSS, use native vertical-writing primitives such as `writing-mode: vertical-rl` only after confirming the target writing mode from CLReq 2.1. Verify punctuation orientation, Latin/numeric runs, Bopomofo placement, headings, and page progression. Horizontal UI controls embedded in vertical editorial layouts need explicit product decisions.

## Annotations

For Bopomofo ruby, romanization, bilingual annotations, and interlinear comments, preserve source semantics and test target rendering. CLReq 5.5.3 describes Bopomofo placement, including right-side placement as preferred in both horizontal and vertical writing; do not replace that with generic Japanese ruby assumptions.

## Forms And UI

Chinese inputs may include IME composition, candidate windows, long addresses, names with rare characters, and mixed Latin codes. Verify caret movement, selection, placeholder layout, validation messages, and truncation. Never reject valid Han characters because they fall outside a narrow BMP-only regex.
