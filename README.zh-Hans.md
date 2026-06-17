# CJK 文字排版 Agent Skills

[English](README.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

本 repository 包含两个中文、日文与韩文文字排版 agent skill：

- `cjk-layout`：教 coding agent 如何按照 W3C JLReq、CLReq 与 KLReq 设计并实现 CJK 文字排版。
- `cjk-layout-audit`：审查网页、frontend app、电子书、PDF、截图，以及由源代码渲染出的可见 CJK 文字排版。

构建或修正排版行为时使用 `cjk-layout`。检查可见输出并产出证据型问题报告时使用 `cjk-layout-audit`。

## 对应标准

- [JLReq：日本語組版処理の要件](https://www.w3.org/TR/jlreq/)
- [CLReq：中文排版需求](https://www.w3.org/TR/clreq/)
- [KLReq：한국어 텍스트 레이아웃 및 타이포그래피를 위한 요구사항](https://www.w3.org/TR/klreq/)

## 涵盖项目

- 语言与 locale metadata
- 横排、竖排与书写方向混排
- 换行、行首禁则与行尾禁则处理
- 标点间距、悬挂标点与连续标点处理
- ruby、注音／旁注、强调标记与行内注
- CJK 与拉丁文字混排、数字、日期与符号
- 段落间距、对齐、孤行、孤字、标题与分页
- 电子书或 PDF 的页面版式、页眉、图、表与注释

## 使用方式

在支持这些 skills 的 agent runtime 中，输入以下 prompt：

```text
使用 $cjk-layout 按照 W3C 文字排版需求实现这个中文、日文或韩文版面。

使用 $cjk-layout-audit 审查这个 CJK 网页或电子书，检查是否符合 W3C 文字排版需求。
```

如果要实现排版，请指定目标语言、locale、UI surface、书写方向与渲染媒介。如果审查范围较大，请指定目标 URL、本地文件、截图、电子书或 PDF、预期语言，以及需要检查的设备或页面尺寸。

审查结果将返回具体问题、受影响范围、证据、对应的 W3C 需求、影响与修正建议。

## Codex Plugin

添加作者的 Codex Marketplace：

```bash
codex plugin marketplace add sichengchen/codex-plugins
```

然后安装 `cjk-text-layout` 插件。

---

本 README 以英文撰写，并由 LLM 翻译为简体中文。
