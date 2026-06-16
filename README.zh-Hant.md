# CJK 文字排版稽核 Agent Skill

[English](README.md) | [简体中文](README.zh-Hans.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

`cjk-layout-audit` 是用於稽核中文、日文與韓文文字排版的 agent skill。適用對象包括網頁、frontend app、電子書、PDF、螢幕截圖，以及由原始碼渲染出的內容。

此 skill 用於檢查可見 CJK 文字的可讀性、換行、間距，以及與 W3C 文字排版需求的一致性。

## 對應標準

- [JLReq：日本語組版処理の要件](https://www.w3.org/TR/jlreq/)
- [CLReq：中文排版需求](https://www.w3.org/TR/clreq/)
- [KLReq：한국어 텍스트 레이아웃 및 타이포그래피를 위한 요구사항](https://www.w3.org/TR/klreq/)

## 稽核項目

- 語言與 locale metadata
- 橫排、直排與書寫方向混排
- 換行、行首禁則與行尾禁則處理
- 標點間距、懸掛標點與連續標點處理
- ruby、註音／旁註、強調標記與行內註
- CJK 與拉丁文字混排、數字、日期與符號
- 段落間距、對齊、孤行、孤字、標題與分頁
- 電子書或 PDF 的頁面版式、頁眉、圖、表與註解

## 使用方式

在支援此 skill 的 agent runtime 中，輸入下列 prompt：

```text
使用 $cjk-layout-audit 稽核這個 CJK 網頁或電子書，檢查是否符合 W3C 文字排版需求。
```

若稽核範圍較大，請指定目標 URL、本機檔案、螢幕截圖、電子書或 PDF、預期語言，以及需要檢查的裝置或頁面尺寸。

稽核結果會回傳具體問題、受影響範圍、證據、對應的 W3C 需求、影響與修正建議。

## Codex Plugin

新增作者的 Codex Marketplace：

```bash
codex plugin marketplace add sichengchen/codex-plugins
```

然後安裝 `cjk-text-layout` 外掛。

---

本 README 以英文撰寫，並由 LLM 翻譯為繁體中文。
