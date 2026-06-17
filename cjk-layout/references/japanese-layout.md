# Japanese Layout

Use JLReq for Japanese layout decisions: `https://www.w3.org/TR/jlreq/`.

## Load These JLReq Sections

- 2.3 Vertical Writing Mode and Horizontal Writing Mode
- 3.1.2 Positioning of Punctuation Marks
- 3.1.4 Positioning of Consecutive Opening Brackets, Closing Brackets, Commas, Full Stops and Middle Dots
- 3.1.7 Characters Not Starting a Line
- 3.1.8 Characters Not Ending a Line
- 3.1.10 Unbreakable Character Sequences
- 3.2.5 Handling of Tate-chu-yoko
- 3.3.5 Positioning of Mono-ruby
- 3.3.6 Positioning of Group-ruby
- 3.3.7 Positioning of Jukugo-ruby
- 3.3.9 Composition of Emphasis Dots
- 3.8 Line Adjustment

## Priorities

- Preserve kanji, hiragana, and katakana rhythm with appropriate full-width punctuation and Japanese fonts.
- Support both horizontal and vertical writing when the product domain calls for it.
- Handle line-start and line-end prohibition rules, unbreakable sequences, punctuation compression, and line adjustment.
- Use ruby for readings and annotations instead of inline parenthetical hacks when the annotation is part of the text experience.
- Use emphasis dots and Japanese decoration conventions instead of Latin-only emphasis when appropriate.

## Writing Mode

For Japanese vertical writing, start from JLReq 2.3 and implement with `writing-mode: vertical-rl` when the target medium is CSS. Use `text-orientation: mixed` so CJK characters remain upright and Latin runs follow the renderer's vertical-text behavior. Use `text-combine-upright` for short numbers only when the design calls for tate-chu-yoko; check JLReq 3.2.5 for spacing around adjacent punctuation classes.

Do not rotate punctuation manually. Vertical forms, brackets, prolonged sound marks, and small kana need font and engine support.

## Line Composition

Plan from JLReq 3.1.7, 3.1.8, and 3.1.10:

- opening bracket classes covered by JLReq 3.1.8 line-end restrictions
- closing brackets, full stops, commas, small kana, prolonged sound marks, and other classes covered by JLReq 3.1.7 line-start restrictions
- unbreakable sequences for numbers, units, abbreviations, and some punctuation clusters
- punctuation compression before adding arbitrary inter-character space
- last-line and paragraph alignment behavior that preserves readability

Implementation translation: CSS `line-break: strict` is a candidate for stricter Japanese behavior, but verify the actual line breaks. Some UI surfaces may choose `normal` or `loose` for narrow mobile constraints; treat that as a product decision, not a JLReq default.

## Mixed Japanese And Latin

When Japanese content contains Latin product names, versions, dates, or acronyms, keep Latin runs as real Latin text with `lang` where substantial. Avoid breaking Latin words one letter at a time. In vertical text, decide whether short Latin/numeric runs should rotate, stay upright, or use tate-chu-yoko, then verify against JLReq 3.2.

## Ruby

Model ruby semantically and check JLReq 3.3.5 through 3.3.7. Do not assume all ruby is the same. Consider:

- mono-ruby for per-character readings
- group ruby for phrase-level readings
- jukugo ruby for compound words
- overhang and spacing when ruby is longer than the base
- placement side in horizontal and vertical text

Browser ruby behavior varies. Test dense ruby, long annotations, and vertical ruby before committing to a design.

## Editorial Layout

For long-form Japanese, account for kihon-hanmen-like grid thinking: line count, character count, line gap, page body, headings, notes, figures, tables, running heads, widows, and page breaks. Web implementations may not reproduce print grids exactly, but spacing should still be systematic and language-aware.
