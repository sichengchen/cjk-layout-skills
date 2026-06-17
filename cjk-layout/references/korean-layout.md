# Korean Layout

Use KLReq for Korean/Hangul layout decisions: `https://www.w3.org/TR/klreq/`.

## Load These KLReq Sections

- 3.1 Writing mode
- 4.1 Fonts & typeface styles
- 5.1 Characters & encoding
- 5.2 Grapheme/word segmentation & selection
- 6.1 Phrase & section boundaries
- 6.1.2 Hangul Punctuation Marks in Horizontal and Vertical Writing
- 7.1.1 Line Breaking Rules
- 7.1.2 Line Head Restrictions
- 7.1.3 Line End Restrictions
- 7.1.4 Word Break Restrictions
- 7.2.2 Restrictions on Inter-Character Width Adjustment when Adjusting Lines
- 7.3.1 Inter-Character Spacing for Hangul, Hanja, Kana, etc
- 7.3.2 Hangul and Latin Mixed Writing

## Priorities

- Respect Korean word spacing. Do not treat Korean like unspaced Chinese or Japanese prose.
- Use Korean font stacks and verify Hangul, Hanja, Latin, numbers, and punctuation in the same component.
- Handle line head restrictions, line end restrictions, word break restrictions, and Hangul-Latin mixed text.
- Account for punctuation forms and writing direction, including vertical behavior when the target medium requires it.
- Test IME composition, caret movement, selection, and form validation carefully.

## Line Breaking

KLReq 7.1.2 says lines cannot start with classes such as closing parentheses, hyphens, dividing punctuation, middle dots, periods/commas, iteration marks, or prolonged sound marks. KLReq 7.1.3 says opening parentheses cannot be placed at line end. KLReq 7.1.4 lists unbreakable sequences such as repeated dashes, ellipses, Arabic numerals, prefix/suffix symbols with numbers, base characters with superscript/subscript, and footnote number strings.

Implementation translation: for web UI, `word-break: keep-all` is a candidate for Korean text because it avoids arbitrary breaks inside Korean words:

```css
:lang(ko) {
  word-break: keep-all;
  overflow-wrap: normal;
}
```

Use emergency wrapping only in constrained components after testing. If a design cannot accommodate Korean words without destructive breaks, adjust the component width, line clamp, or content strategy before relaxing word breaking globally.

## Spacing And Justification

Preserve Korean source word spaces unless a Korean-specific style guide or text-processing requirement says otherwise. Evaluate justification against KLReq 7.2, especially 7.2.2 restrictions on expanding inter-character width. Avoid applying Japanese/Chinese inter-character spacing assumptions to Korean text.

## Mixed Hangul, Hanja, Latin, And Numbers

When Korean content contains Latin brands, product versions, dates, file names, or technical identifiers, keep Latin runs intact and readable. Verify baseline alignment, font fallback, and punctuation spacing against the target renderer.

## Punctuation

KLReq covers punctuation code ranges, horizontal and vertical punctuation, and changes by writing direction. Do not normalize Korean punctuation blindly to ASCII; preserve content conventions and product style rules.

## Vertical Korean

When the target requires vertical Korean, load KLReq 3.1 and 6.1.2, then use native vertical-writing properties and verify Hangul orientation, punctuation forms, Latin runs, and numbers in the target renderer.

## Interaction

For interactive Korean fields, test IME composition before adding validation or auto-formatting. Check:

- composing syllables in text inputs and contenteditable regions
- deleting and selecting jamo/syllable clusters
- validation while composition is active
- mixed Korean and Latin identifiers
- placeholder, label, and error text wrapping
