# CJK Layout Audit Agent Skill

[English](README.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

本仓库包含 `cjk-layout-audit` agent skill，用于依据 W3C 文字排版需求，审查前端页面、已渲染网页、EPUB/电子书、PDF、截图和源文件中的中文、日文与韩文文字排版。

此 skill 基于以下 W3C 文档：

- [JLReq: Requirements for Japanese Text Layout](https://www.w3.org/TR/jlreq/)
- [CLReq: Requirements for Chinese Text Layout](https://www.w3.org/TR/clreq/)
- [KLReq: Requirements for Hangul Text Layout and Typography](https://www.w3.org/TR/klreq/)

## 内容

- `cjk-layout-audit/SKILL.md` - 主要 skill 指令与工作流。
- `cjk-layout-audit/references/audit-model.md` - W3C 需求分类、严重程度规则和证据标准。
- `cjk-layout-audit/references/artifact-contract.md` - `/goal` 循环、subagent、产物、receipt 和报告契约。
- `cjk-layout-audit/scripts/cjk_layout_probe.py` - 用于本地文本、HTML/XHTML、CSS 和 EPUB 初步检查的辅助脚本。
- `cjk-layout-audit/agents/openai.yaml` - skill 的 UI 元数据。

## 使用方式

在 Codex 等 agent runtime 中，可以用以下方式调用 skill：

```text
Use $cjk-layout-audit to audit this CJK webpage or ebook for W3C text layout issues.
```

对于非单页的小型审查，skill 会要求 agent 使用 `/goal` 循环、将覆盖范围拆分给 subagent、要求每个 surface 生成 receipt，并且只在声明的审查范围完成闭合后才结束。

## Probe Script

对本地文件运行辅助脚本，可以识别 CJK 文字覆盖、相关 CSS 属性、ruby 标记、可疑的行首/行尾标点，以及 CJK/拉丁文字混排间距线索：

```bash
python3 cjk-layout-audit/scripts/cjk_layout_probe.py --json path/to/file.html
```

probe 输出只作为初步线索。skill 要求必须有渲染后或抽取出的证据，才可以报告排版 finding。

## 验证

创建时使用的基本本地检查：

```bash
python3 -B cjk-layout-audit/scripts/cjk_layout_probe.py --json path/to/file.html
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile cjk-layout-audit/scripts/cjk_layout_probe.py
```

当 Python 依赖可用时，可以运行 Codex-compatible skill validator：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py cjk-layout-audit
```
