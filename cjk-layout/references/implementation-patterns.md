# Implementation Patterns

Use these patterns when turning JLReq, CLReq, and KLReq requirements into code. These are implementation candidates, not quotations from the W3C layout requirement documents. Always pair them with the relevant requirement section from the language reference.

## HTML And Language Metadata

Use precise language tags:

```html
<html lang="ja">
<p lang="zh-Hant-TW">...</p>
<span lang="ko">...</span>
```

Mark inline language changes instead of forcing one font and one line-breaking policy on mixed text:

```html
<p lang="ja">次の版は <span lang="en">Version 2.1</span> です。</p>
```

## Font Stacks

Prefer project-approved fonts that cover the target script. When using system stacks, order by language and platform:

```css
:lang(ja) {
  font-family: "Hiragino Sans", "Yu Gothic", "Meiryo", system-ui, sans-serif;
}

:lang(zh-Hans),
:lang(zh-CN) {
  font-family: "PingFang SC", "Microsoft YaHei", "Noto Sans CJK SC", system-ui, sans-serif;
}

:lang(zh-Hant),
:lang(zh-TW),
:lang(zh-HK) {
  font-family: "PingFang TC", "Microsoft JhengHei", "Noto Sans CJK TC", system-ui, sans-serif;
}

:lang(ko) {
  font-family: "Apple SD Gothic Neo", "Malgun Gothic", "Noto Sans CJK KR", system-ui, sans-serif;
}
```

Confirm the exact stack against product requirements. For editorial text, define serif/mincho/song/myungjo stacks separately from sans-serif UI stacks.

## Line Breaking And Overflow

Start conservatively:

```css
.cjk-copy {
  line-break: strict;
  overflow-wrap: normal;
  word-break: normal;
}

:lang(ko) .cjk-copy {
  word-break: keep-all;
}
```

Use `overflow-wrap: anywhere` only for narrow emergency surfaces such as chips, table cells, or cards where overflow is worse than imperfect breaking. Avoid making it the default for long-form CJK copy unless the product accepts the standards tradeoff.

For truncation, prefer tested clamping and full-text affordances. Ellipsis can hide important disambiguating characters in CJK names, addresses, and legal text.

## Vertical Writing

Use native vertical writing:

```css
.vertical-ja {
  writing-mode: vertical-rl;
  text-orientation: mixed;
  line-height: 1.8;
}

.vertical-ja .digits-2 {
  text-combine-upright: digits 2;
}
```

Keep DOM order logical. Do not rotate whole paragraphs with `transform`; that breaks selection, hit testing, accessibility, punctuation orientation, and line progression.

## Ruby And Annotations

Use semantic ruby markup when the target supports it:

```html
<ruby>漢<rp>(</rp><rt>かん</rt><rp>)</rp>字<rp>(</rp><rt>じ</rt><rp>)</rp></ruby>
```

For Bopomofo or complex annotation placement, test in the target browser or reading system. If support is insufficient, use a component with explicit fallback and preserve the source text semantically.

## Emphasis And Decoration

Use native emphasis marks where appropriate:

```css
.emphasis {
  text-emphasis-style: sesame;
  text-emphasis-position: over right;
}
```

Avoid underlines that collide with ideographic glyphs, ruby, or vertical text. Test links and focus rings in both horizontal and vertical modes.

## Spacing And Justification

Use `text-align: justify` only after checking the target language and browser behavior. CJK justification should be evaluated against the relevant line-adjustment sections: JLReq 3.8, CLReq 6.2, or KLReq 7.2.

Treat `text-spacing` and related emerging CSS as progressive enhancement:

```css
@supports (text-spacing: auto) {
  .cjk-copy {
    text-spacing: auto;
  }
}
```

Do not replace standards-aware spacing with blanket inserted spaces; content mutation harms search, copy/paste, speech, and localization.

## Components And Design Systems

Expose these as component variants or tokens:

- `lang` and locale
- writing mode
- line-height by script and density
- font family by script and region
- ruby/annotation support
- compact overflow policy
- form control sizing for IME and long CJK labels

Avoid setting a single global `.cjk` class. Prefer language selectors and component props so mixed-language products can compose correct behavior.

## Verification

Check:

- Chrome, Safari, and Firefox when web layout matters
- native CJK fonts on macOS/Windows when system font fallback is used
- mobile widths, zoom, dynamic type, and high-density table/card layouts
- copy/paste, selection, caret movement, IME composition, and screen reader order for interactive text
- generated PDF/EPUB output in the actual reader or renderer
