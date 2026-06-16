# CJK 文字排版审查 Agent Skill

[English](README.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

`cjk-layout-audit` 是用于审查中文、日文与韩文文字排版的 agent skill，适用于网页、前端应用、电子书、PDF、截图，以及可以渲染的源代码内容。

它可以帮助 agent 检查 CJK 文字是否易读、换行是否正确、标点与间距是否合理，并确认结果是否符合 W3C 文字排版需求。

## 依据标准

- [JLReq：日本語組版処理の要件](https://www.w3.org/TR/jlreq/)
- [CLReq：中文排版需求](https://www.w3.org/TR/clreq/)
- [KLReq：한국어 텍스트 레이아웃 및 타이포그래피를 위한 요구사항](https://www.w3.org/TR/klreq/)

## 可审查项目

- 语言与 locale metadata
- 横排、竖排与混合书写方向
- 换行、行首禁则与行尾禁则
- 标点间距、悬挂标点与连续标点处理
- ruby、注音／旁注、强调标记与行内注
- CJK 与拉丁文字混排、数字、日期与符号
- 段落间距、对齐、孤行、孤字、标题与分页
- 电子书或 PDF 的页面版式、页眉、图表、表格与注释

## 使用方式

在支持此 skill 的 agent runtime 中，可以使用以下 prompt：

```text
使用 $cjk-layout-audit 审查这个 CJK 网页或电子书，检查是否符合 W3C 文字排版需求。
```

如果审查范围较大，请提供目标 URL、本地文件、截图、电子书／PDF、预期语言，以及需要检查的设备或页面尺寸。

审查结果应包含具体问题、受影响范围、证据、对应的 W3C 需求、影响与修正建议。

## Codex Plugin

从 GitHub 安装：

```bash
codex plugin marketplace add sichengchen/cjk-layout-audit-skill
```

或从本地 checkout 安装：

```bash
codex plugin marketplace add /path/to/cjk-layout-audit-skill
```
