# CJK Layout Agent Skills

[繁體中文](README.zh-Hant.md) | [简体中文](README.zh-Hans.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

This repository contains agent skills for Chinese, Japanese, and Korean text layout:

- `cjk-layout`: teaches coding agents how to design and implement CJK text layout according to W3C JLReq, CLReq, and KLReq.
- `cjk-layout-audit`: audits rendered CJK text layout in webpages, frontend apps, ebooks, PDFs, screenshots, and source-backed rendered content.

Use `cjk-layout` when building or fixing layout behavior. Use `cjk-layout-audit` when checking visible output and producing evidence-backed findings.

## Standards

- [JLReq: Requirements for Japanese Text Layout / 日本語組版処理の要件](https://www.w3.org/TR/jlreq/)
- [CLReq: Requirements for Chinese Text Layout / 中文排版需求](https://www.w3.org/TR/clreq/)
- [KLReq: Requirements for Hangul Text Layout and Typography / 한국어 텍스트 레이아웃 및 타이포그래피를 위한 요구사항](https://www.w3.org/TR/klreq/)

## What They Cover

- language and locale metadata
- horizontal and vertical writing modes
- line breaking and forbidden line-start or line-end punctuation
- punctuation spacing and hanging punctuation
- ruby, phonetic annotations, emphasis marks, and inline notes
- CJK and Latin mixed text, numbers, dates, and symbols
- paragraph spacing, justification, widows, orphans, headings, and page breaks
- ebook or PDF page layout, running heads, figures, tables, and notes

## How To Use

Use one of these prompts in an agent runtime that supports these skills:

```text
Use $cjk-layout to implement this Chinese, Japanese, or Korean text layout according to W3C layout requirements.

Use $cjk-layout-audit to audit this CJK webpage or ebook against W3C text layout requirements.
```

For implementation work, provide the target language, locale, UI surface, writing mode, and rendering medium. For larger audits, provide the target URL, local files, screenshots, ebook/PDF, expected language, and the devices or page sizes you care about.

The audit should return concrete findings with affected content, evidence, W3C mapping, impact, and remediation.

## Codex Plugin

Install the Codex plugin from my Codex Marketplace:

```bash
codex plugin marketplace add sichengchen/codex-plugins
```

Then install the `cjk-text-layout` plugin.
