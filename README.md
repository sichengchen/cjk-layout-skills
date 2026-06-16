# CJK Layout Audit Agent Skill

[繁體中文](README.zh-Hant.md) | [简体中文](README.zh-Hans.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

`cjk-layout-audit` is an agent skill for auditing Chinese, Japanese, and Korean text layout in webpages, frontend apps, ebooks, PDFs, screenshots, and source-backed rendered content.

It helps an agent check whether visible CJK text is readable, properly wrapped, correctly spaced, and aligned with W3C text layout requirements.

## Standards

- [JLReq: Requirements for Japanese Text Layout / 日本語組版処理の要件](https://www.w3.org/TR/jlreq/)
- [CLReq: Requirements for Chinese Text Layout / 中文排版需求](https://www.w3.org/TR/clreq/)
- [KLReq: Requirements for Hangul Text Layout and Typography / 한국어 텍스트 레이아웃 및 타이포그래피를 위한 요구사항](https://www.w3.org/TR/klreq/)

## What It Checks

- language and locale metadata
- horizontal and vertical writing modes
- line breaking and forbidden line-start or line-end punctuation
- punctuation spacing and hanging punctuation
- ruby, phonetic annotations, emphasis marks, and inline notes
- CJK and Latin mixed text, numbers, dates, and symbols
- paragraph spacing, justification, widows, orphans, headings, and page breaks
- ebook or PDF page layout, running heads, figures, tables, and notes

## How To Use

Use this prompt in an agent runtime that supports this skill:

```text
Use $cjk-layout-audit to audit this CJK webpage or ebook against W3C text layout requirements.
```

For larger audits, provide the target URL, local files, screenshots, ebook/PDF, expected language, and the devices or page sizes you care about.

The audit should return concrete findings with affected content, evidence, W3C mapping, impact, and remediation.

## Codex Plugin

Install from GitHub:

```bash
codex plugin marketplace add sichengchen/cjk-layout-audit-skill
```

Or install from a local checkout:

```bash
codex plugin marketplace add /path/to/cjk-layout-audit-skill
```
