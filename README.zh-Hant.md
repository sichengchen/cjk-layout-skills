# CJK 文字排版稽核 Agent Skill

[English](README.md) | [简体中文](README.zh-Hans.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

`cjk-layout-audit` 是用於稽核中文、日文與韓文文字排版的 agent skill，適用於網頁、前端應用程式、電子書、PDF、螢幕截圖，以及可渲染的原始碼內容。

它可以協助 agent 檢查 CJK 文字是否易讀、換行是否正確、標點與間距是否合理，並確認結果是否符合 W3C 文字排版需求。

## 依據標準

- [JLReq：日本語組版処理の要件](https://www.w3.org/TR/jlreq/)
- [CLReq：中文排版需求](https://www.w3.org/TR/clreq/)
- [KLReq：한국어 텍스트 레이아웃 및 타이포그래피를 위한 요구사항](https://www.w3.org/TR/klreq/)

## 可稽核項目

- 語言與 locale metadata
- 橫排、直排與混合書寫方向
- 換行、行首禁則與行尾禁則
- 標點間距、懸掛標點與連續標點處理
- ruby、註音／旁註、強調標記與行內註
- CJK 與拉丁文字混排、數字、日期與符號
- 段落間距、對齊、孤行、孤字、標題與分頁
- 電子書或 PDF 的頁面版式、頁眉、圖表、表格與註解

## 使用方式

在支援此 skill 的 agent runtime 中，可使用下列 prompt：

```text
使用 $cjk-layout-audit 稽核這個 CJK 網頁或電子書，檢查是否符合 W3C 文字排版需求。
```

若稽核範圍較大，請提供目標 URL、本機檔案、螢幕截圖、電子書／PDF、預期語言，以及需要檢查的裝置或頁面尺寸。

稽核結果應包含具體問題、受影響範圍、證據、對應的 W3C 需求、影響與修正建議。

## Codex Plugin

從 GitHub 安裝：

```bash
codex plugin marketplace add sichengchen/cjk-layout-audit-skill
```

或從本機 checkout 安裝：

```bash
codex plugin marketplace add /path/to/cjk-layout-audit-skill
```
