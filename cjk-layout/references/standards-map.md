# Standards Map

Use W3C Internationalization layout requirements as the primary source family:

- JLReq: Requirements for Japanese Text Layout, latest TR `https://www.w3.org/TR/jlreq/`; current published TR is a W3C Working Group Note dated 11 August 2020, with a linked editor's draft.
- CLReq: Requirements for Chinese Text Layout, latest TR `https://www.w3.org/TR/clreq/`; current published TR is a W3C Group Note Draft dated 03 May 2026.
- KLReq: Requirements for Hangul Text Layout and Typography, latest TR `https://www.w3.org/TR/klreq/`; current published TR is a W3C Group Note Draft dated 21 March 2026.

Prefer the latest TR URL in code comments, docs, and reports unless the user requires a pinned version. For implementation decisions, treat editor's drafts as useful context but distinguish them from published TRs.

## Source Discipline

- Tie every non-obvious rule to a named section. Do not write "CJK requires..." without saying whether the source is JLReq, CLReq, KLReq, CSS, Unicode, or a product style guide.
- Distinguish "the requirement says the layout should behave this way" from "this CSS property is one implementation attempt."
- If a rule is a convention with documented exceptions, preserve the exception. Example: JLReq 3.1.7 describes strict Japanese line-start prohibition but also notes less strict practices for some classes.
- If the output target is a browser, EPUB reader, PDF generator, canvas renderer, or native app, verify actual support before claiming conformance.
- For user-facing reports or code comments, cite section names and URLs, not long copied passages.

## Requirement Families And Named Sections

Map tasks to these families before selecting details:

- Text direction: horizontal writing, vertical writing, line progression, page progression.
- Glyph shaping and positioning: font selection, locale-specific glyphs, punctuation forms, text orientation.
- Typographic units: character classes, grapheme/word segmentation, encoding, counters.
- Punctuation and inline features: brackets, commas, full stops, quotation marks, ellipses, emphasis marks, ruby/annotations, inline notes.
- Line and paragraph layout: line breaking, prohibition rules, unbreakable sequences, justification, indentation, last-line handling, line height, baselines.
- Mixed text: Latin, numbers, dates, units, symbols, and short horizontal runs inside vertical text.
- Page and book layout: page body, margins, headings, notes, figures, tables, running heads, widows, orphans.
- Forms and interaction: readable controls, input segmentation, caret/selection behavior, IME-friendly fields.

Use these named sections as navigation anchors:

| Topic | JLReq | CLReq | KLReq |
| --- | --- | --- | --- |
| Writing mode | 2.3 Vertical Writing Mode and Horizontal Writing Mode | 2.1 Writing mode | 3.1 Writing mode |
| Fonts and glyphs | 2.1 Characters and the Principles of Setting them | 3.1 Fonts & typeface styles | 4.1 Fonts & typeface styles |
| Line-start restrictions | 3.1.7 Characters Not Starting a Line | 6.1.1 Prohibition rules for line start and line end | 7.1.2 Line Head Restrictions |
| Line-end restrictions | 3.1.8 Characters Not Ending a Line | 6.1.1 Prohibition rules for line start and line end | 7.1.3 Line End Restrictions |
| Unbreakable sequences | 3.1.10 Unbreakable Character Sequences | 6.1.2 Prohibition rules for unbreakable marks | 7.1.4 Word Break Restrictions |
| Punctuation placement | 3.1 Line Composition Rules for Punctuation Marks | 5.1 Phrase & section boundaries and 6.3.2 Punctuation Width Adjustment | 6.1 Phrase & section boundaries |
| Mixed Latin/CJK | 3.2 Japanese and Western Mixed Text Composition | 6.1.4 and 6.3.3 mixed Western/Chinese text | 7.3.2 Hangul and Latin Mixed Writing |
| Ruby/annotations | 3.3 Ruby and Emphasis Dots | 5.5 Inline notes & annotations | 6.5 Inline notes & annotations |
| Line adjustment | 3.8 Line Adjustment | 6.2 Text alignment & justification | 7.2 Text alignment & justification |
| Page/book layout | 4. Positioning of Headings, Notes, Illustrations, Tables and Paragraphs | 7. Page & book layout | 8. Page & book layout |

## Cross-Language Boundaries

- Do not collapse all CJK into one rule set. Japanese, Chinese, and Korean differ in punctuation, word spacing, annotation traditions, vertical writing conventions, and preferred line-breaking behavior.
- Use `lang` as a layout primitive, not just accessibility metadata. It influences font fallback, glyph selection, line breaking, quotation marks, screen readers, and spell/IME behavior.
- Treat `zh-Hans` and `zh-Hant` as script distinctions, and use regional tags such as `zh-CN`, `zh-TW`, or `zh-HK` when typography or glyph standards are region-specific.
- For Korean text, consult KLReq 5.2 and 7.1 before changing word spaces or line breaks. Do not import Chinese or Japanese unspaced-line assumptions into Korean layout.
- Vertical writing is common in Japanese publishing and appears in Traditional Chinese contexts; it is less common for modern Korean interfaces but still covered by KLReq.

## Standards-To-Code Translation

- Standards describe expected layout behavior; code must be checked against the rendering engine actually used.
- CSS support is uneven for some CJK features. Prefer native properties when implemented, but provide fallback behavior for unsupported or partially supported features such as advanced ruby behavior, hanging punctuation, and vertical text edge cases.
- Use generated PDFs, canvas, or SVG text APIs only when they can preserve the needed CJK line breaking, font fallback, vertical forms, and annotations. Otherwise, pre-layout text with a library that understands the requirement family.
- For component libraries, expose locale and writing-mode variants instead of baking one global CJK style into every component.

## Test String Strategy

Build a small language-specific corpus for every implementation:

- punctuation at start and end of lines
- nested brackets and quotes
- CJK plus Latin words, versions, dates, times, units, and URLs
- long unspaced CJK runs and long Latin tokens
- ruby or annotation examples when supported
- vertical writing examples with two-digit numbers and punctuation
- form labels, placeholders, validation messages, and button text
