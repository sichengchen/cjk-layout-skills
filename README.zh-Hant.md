# CJK Layout Audit Skill

[English](README.md) | [简体中文](README.zh-Hans.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

本儲存庫包含 `cjk-layout-audit` Codex skill，用於依據 W3C 文字排版需求，稽核前端頁面、已渲染網頁、EPUB/電子書、PDF、螢幕截圖與原始碼中的中文、日文與韓文文字排版。

此 skill 依據以下 W3C 文件：

- [JLReq: Requirements for Japanese Text Layout](https://www.w3.org/TR/jlreq/)
- [CLReq: Requirements for Chinese Text Layout](https://www.w3.org/TR/clreq/)
- [KLReq: Requirements for Hangul Text Layout and Typography](https://www.w3.org/TR/klreq/)

## 內容

- `cjk-layout-audit/SKILL.md` - 主要 skill 指令與工作流程。
- `cjk-layout-audit/references/audit-model.md` - W3C 需求分類、嚴重程度規則與證據標準。
- `cjk-layout-audit/references/artifact-contract.md` - `/goal` 迴圈、subagent、產物、receipt 與報告契約。
- `cjk-layout-audit/scripts/cjk_layout_probe.py` - 用於本機文字、HTML/XHTML、CSS 與 EPUB 初步檢查的輔助腳本。
- `cjk-layout-audit/agents/openai.yaml` - skill 的 UI 中繼資料。

## 使用方式

在 Codex 中以下列方式呼叫 skill：

```text
Use $cjk-layout-audit to audit this CJK webpage or ebook for W3C text layout issues.
```

對於非單頁的小型稽核，skill 會要求 agent 使用 `/goal` 迴圈、將覆蓋範圍拆分給 subagent、要求每個 surface 產生 receipt，並且只在宣告的稽核範圍完成閉合後才結束。

## Probe Script

對本機檔案執行輔助腳本，可辨識 CJK 文字覆蓋、相關 CSS 屬性、ruby 標記、可疑的行首/行尾標點，以及 CJK/拉丁文字混排間距線索：

```bash
python3 cjk-layout-audit/scripts/cjk_layout_probe.py --json path/to/file.html
```

probe 輸出只作為初步線索。skill 要求必須有渲染後或抽取出的證據，才可回報排版 finding。

## 驗證

建立時使用的基本本機檢查：

```bash
python3 -B cjk-layout-audit/scripts/cjk_layout_probe.py --json path/to/file.html
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile cjk-layout-audit/scripts/cjk_layout_probe.py
```

當 Python 相依套件可用時，可執行官方 skill validator：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py cjk-layout-audit
```
