# CJK 文字排版 Agent Skills

[English](README.md) | [简体中文](README.zh-Hans.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

本 repository 包含兩個中文、日文與韓文文字排版 agent skill：

- `cjk-layout`：教導 coding agent 如何依照 W3C JLReq、CLReq 與 KLReq 設計並實作 CJK 文字排版。
- `cjk-layout-audit`：稽核網頁、frontend app、電子書、PDF、螢幕截圖，以及由原始碼渲染出的可見 CJK 文字排版。

建置或修正排版行為時使用 `cjk-layout`。檢查可見輸出並產出證據型問題報告時使用 `cjk-layout-audit`。

## 對應標準

- [JLReq：日本語組版処理の要件](https://www.w3.org/TR/jlreq/)
- [CLReq：中文排版需求](https://www.w3.org/TR/clreq/)
- [KLReq：한국어 텍스트 레이아웃 및 타이포그래피를 위한 요구사항](https://www.w3.org/TR/klreq/)

## 涵蓋項目

- 語言與 locale metadata
- 橫排、直排與書寫方向混排
- 換行、行首禁則與行尾禁則處理
- 標點間距、懸掛標點與連續標點處理
- ruby、註音／旁註、強調標記與行內註
- CJK 與拉丁文字混排、數字、日期與符號
- 段落間距、對齊、孤行、孤字、標題與分頁
- 電子書或 PDF 的頁面版式、頁眉、圖、表與註解

## 使用方式

在支援這些 skills 的 agent runtime 中，輸入下列 prompt：

```text
使用 $cjk-layout 依照 W3C 文字排版需求實作這個中文、日文或韓文版面。

使用 $cjk-layout-audit 稽核這個 CJK 網頁或電子書，檢查是否符合 W3C 文字排版需求。
```

若要實作排版，請指定目標語言、locale、UI surface、書寫方向與渲染媒介。若稽核範圍較大，請指定目標 URL、本機檔案、螢幕截圖、電子書或 PDF、預期語言，以及需要檢查的裝置或頁面尺寸。

稽核結果會回傳具體問題、受影響範圍、證據、對應的 W3C 需求、影響與修正建議。

## Codex Plugin

新增作者的 Codex Marketplace：

```bash
codex plugin marketplace add sichengchen/codex-plugins
```

然後安裝 `cjk-text-layout` 外掛。

---

本 README 以英文撰寫，並由 LLM 翻譯為繁體中文。
