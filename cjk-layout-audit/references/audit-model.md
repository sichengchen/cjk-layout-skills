# CJK Layout Audit Model

Use this reference to decide what to inspect and how to classify findings. The canonical standards are:

- JLReq: https://www.w3.org/TR/jlreq/
- CLReq: https://www.w3.org/TR/clreq/
- KLReq: https://www.w3.org/TR/klreq/

## Source Map

The W3C documents describe requirements for layout realized with web and document technologies such as CSS, SVG, XSL-FO, and ebook standards. Use the latest published URL unless the user asks for a dated version.

- JLReq covers Japanese composition: page format, vertical/horizontal writing, line composition, punctuation placement, line-start/line-end restrictions, unbreakable sequences, mixed Japanese/Western text including tate-chu-yoko, ruby, emphasis dots, warichu, paragraph adjustment, headings, notes, tables, and page/book layout.
- CLReq covers Chinese layout: writing modes, mixed vertical text, glyph positioning, punctuation and inline features, quotations, emphasis marks, ellipsis/repetition, ruby and phonetic annotation including Bopomofo and romanization, line breaking, hanging punctuation, alignment/justification, spacing, baselines/line height, page/book layout, widows/orphans, headings, and forms/user interaction.
- KLReq covers Hangul/Korean layout: writing modes, bidirectional text, fonts and glyph positioning, kerning, segmentation, punctuation behavior across writing directions, emphasis/highlighting, annotations, line breaking, line-head/line-end restrictions, word-break restrictions, justification, paragraph adjustment, Hangul/Latin mixed writing, spacing, line height, lists, initials, and page/book layout.

## Language Identification

Classify the content before judging it:

- `ja`: kana present, Japanese punctuation, ruby/furigana, tate-chu-yoko, Japanese vertical layout conventions.
- `zh-Hans` or `zh-Hant`: simplified/traditional Han text, Chinese punctuation conventions, Bopomofo only for relevant Traditional Chinese contexts.
- `ko`: Hangul syllables/jamo, Korean punctuation and spacing expectations, Hangul/Latin mixed text.
- `mixed`: more than one CJK language or CJK plus substantial Latin/numeric content.
- `unknown`: CJK script is present but locale cannot be inferred; lower confidence and state the ambiguity.

Use document metadata (`lang`, `xml:lang`, EPUB package metadata, route locale), visible content, and user-provided locale together. If they conflict, record the conflict as an audit risk.

## Requirement Families

Apply only the families relevant to the detected language, writing mode, and surface.

| Family | What to inspect | Common evidence |
| --- | --- | --- |
| Language metadata | `lang`, `xml:lang`, page locale, font fallback, OpenType support | DOM, EPUB metadata, computed styles |
| Writing mode | horizontal vs vertical writing, block progression, sideways/rotated Latin, vertical punctuation glyphs | screenshots, `writing-mode`, `text-orientation`, computed styles |
| Punctuation | line-start/line-end restrictions, fullwidth punctuation spacing, consecutive punctuation, hanging punctuation, direction-dependent punctuation glyphs | line screenshots, extracted text around breaks, computed text metrics |
| Line breaking | forbidden breaks, unbreakable sequences, Korean word-break restrictions, awkward breaks in mixed text | screenshots at multiple widths, line boxes, text samples |
| Spacing and justification | ideographic spacing, inter-character expansion, mixed CJK/Latin spacing, punctuation width adjustment, grid alignment | computed CSS, before/after screenshots, viewport matrix |
| Ruby and annotations | ruby side, size, overhang, grouping, Bopomofo/romanized annotation, interlinear comments | DOM (`ruby`, `rt`, `rp`), screenshots at zoom/width changes |
| Emphasis and decoration | emphasis marks, underline/overline placement, Korean superscript/subscript, highlight collisions | CSS, screenshots, zoom states |
| Mixed text and numerals | tate-chu-yoko, Latin in vertical text, proportional Latin in CJK runs, dates/numbers/currency | screenshots, computed styles, text samples |
| Paragraphs | first-line indent, last-line alignment, widows/orphans, headings near page/column breaks | screenshots, page/chapter renders |
| Page/book layout | page progression, margins, running heads, page numbers, tables/figures/notes, columns | rendered pages, ebook/PDF page images |
| Interaction | input fields, text selection, copy/paste order, focus/hover states with CJK text | browser interaction, form screenshots |

## Common W3C Section Anchors

Prefer a concrete section name when it applies. Use the broader family only when the rendered issue is real but the exact section cannot be established quickly.

| Language | Issue area | Useful W3C anchor |
| --- | --- | --- |
| Japanese | punctuation layout, forbidden line start/end, unbreakable sequences | JLReq 3.1 Line Composition Rules for Punctuation Marks |
| Japanese | Japanese/Western mixed text, Latin in vertical text | JLReq 3.2 Japanese and Western Mixed Text Composition |
| Japanese | tate-chu-yoko | JLReq 3.2.5 Handling of Tate-chu-yoko |
| Japanese | ruby, overhang, emphasis dots | JLReq 3.3 Ruby and Emphasis Dots |
| Japanese | warichu | JLReq 3.4 Inline Cutting Note |
| Japanese | paragraph indents, alignment, widows | JLReq 3.5 Paragraph Adjustment Rules |
| Chinese | writing mode and vertical mixed text | CLReq 2 Text direction |
| Chinese | punctuation, quotations, emphasis, ellipsis, ruby, annotations | CLReq 5 Punctuation & inline features |
| Chinese | forbidden line starts/ends, unbreakable marks, hanging punctuation | CLReq 6.1 Line breaking & hyphenation |
| Chinese | alignment, justification, grid alignment, mixed Western text | CLReq 6.2 Text alignment & justification |
| Chinese | punctuation width, mixed-script spacing | CLReq 6.3 Text spacing |
| Chinese | page layout, widows/orphans, headings and page breaks | CLReq 7 Page & book layout |
| Korean | writing mode, vertical/horizontal mixed writing, bidi | KLReq 3 Text direction |
| Korean | punctuation marks and direction-dependent punctuation | KLReq 6 Punctuation & inline features |
| Korean | line breaking, line-head/end restrictions, word-break restrictions | KLReq 7.1 Line breaking & hyphenation |
| Korean | justification and paragraph adjustment | KLReq 7.2 Text alignment & justification |
| Korean | Hangul/Latin mixed text, inter-character spacing | KLReq 7.3 Text spacing |
| Korean | page body, tables, figures, object placement | KLReq 8 Page & book layout |

## Severity

Use severity to communicate user impact, not standards trivia.

- `critical`: CJK content is unreadable, important text is clipped/overlapped, wrong reading order causes material misunderstanding, or an ebook/page cannot be navigated/read.
- `high`: frequent visible violations affect core content or transaction-critical flows: broken line breaks, collapsed ruby, vertical text rendered in the wrong direction, missing locale metadata causing wrong shaping/fallback across major surfaces.
- `medium`: localized but user-visible typography defects reduce readability or professionalism: poor punctuation spacing, inconsistent mixed-script spacing, broken emphasis marks, widows/orphans in prominent content.
- `low`: minor polish issues with limited reach or uncertain locale impact.
- `info`: standards-relevant observation, coverage note, or risk requiring product/design confirmation.

## Evidence Standard

Every finding needs:

- target surface and exact state: URL/route/page/chapter/component, viewport/page size, locale, writing mode
- visible evidence: screenshot, rendered page image, copied text line, or DOM/CSS inspection tied to the affected text
- requirement family and W3C source: JLReq, CLReq, or KLReq with section name when available
- affected implementation: selector, file path, EPUB item, CSS rule, component, or "unknown from rendered artifact"
- remediation that fits the platform: CSS, markup, content, font, EPUB package, PDF generation, or design-system change
- confidence: `high`, `medium`, or `low`

## Non-Findings

Do not report:

- differences of aesthetic taste when the text is readable and the relevant W3C requirement is optional or context-dependent
- source-level CSS concerns that do not manifest in rendered output
- missing vertical writing support when the product intentionally supports only horizontal text and no vertical content is present
- locale-specific conventions when the locale is unknown and there is no user-visible defect

Record these as notes or deferred questions when they affect confidence.
