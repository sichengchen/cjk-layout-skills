# CJK テキストレイアウト Agent Skills

[English](README.md) | [繁體中文](README.zh-Hant.md) | [简体中文](README.zh-Hans.md) | [한국어](README.ko.md)

この repository には、中国語・日本語・韓国語のテキストレイアウト向け agent skill が 2 つ含まれます。

- `cjk-layout`: W3C JLReq、CLReq、KLReq に沿って CJK テキストレイアウトを設計・実装するための知識を coding agent に与えます。
- `cjk-layout-audit`: Web ページ、frontend app、電子書籍、PDF、スクリーンショット、ソースからレンダリングされる可視 CJK テキストレイアウトを監査します。

レイアウトを構築または修正する場合は `cjk-layout` を使用します。可視出力を確認し、証拠に基づく指摘を作成する場合は `cjk-layout-audit` を使用します。

## 対応標準

- [JLReq：日本語組版処理の要件](https://www.w3.org/TR/jlreq/)
- [CLReq：中文排版需求](https://www.w3.org/TR/clreq/)
- [KLReq：한국어 텍스트 레이아웃 및 타이포그래피를 위한 요구사항](https://www.w3.org/TR/klreq/)

## 対象項目

- 言語指定と locale metadata
- 横組み、縦組み、書字方向の混在
- 改行、行頭禁則、行末禁則処理
- 約物の間隔、ぶら下げ、連続する約物の処理
- ルビ、ふりがな／注釈、強調表記、行内注
- CJK とラテン文字の混在、数字、日付、記号
- 段落間隔、行揃え、孤立行、孤立字、見出し、改ページ
- 電子書籍および PDF のページ構成、柱、図版、表、注

## 使用方法

これらの skills に対応した agent runtime で、次の prompt を入力します。

```text
$cjk-layout を使って、この中国語・日本語・韓国語レイアウトを W3C の文字組版要件に沿って実装してください。

$cjk-layout-audit を使って、この CJK Web ページまたは電子書籍を W3C の文字組版要件に照らして監査してください。
```

実装作業では、対象言語、locale、UI surface、書字方向、レンダリング媒体を指定してください。監査範囲が大きい場合は、対象 URL、ローカルファイル、スクリーンショット、電子書籍または PDF、想定言語、確認対象のデバイスまたはページサイズを指定します。

監査結果として、具体的な指摘、対象箇所、証拠、W3C 要件との対応、影響、修正方法を返します。

## Codex Plugin

作者の Codex Marketplace を追加します。

```bash
codex plugin marketplace add sichengchen/codex-plugins
```

続いて、`cjk-text-layout` プラグインをインストールします。

---

この README は英語で作成され、LLM によって日本語に翻訳されたものです。
