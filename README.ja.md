# CJK 文字レイアウト監査 Agent Skill

[English](README.md) | [繁體中文](README.zh-Hant.md) | [简体中文](README.zh-Hans.md) | [한국어](README.ko.md)

`cjk-layout-audit` は、中国語・日本語・韓国語の文字レイアウトを監査するための agent skill です。Web ページ、フロントエンドアプリ、電子書籍、PDF、スクリーンショット、レンダリング可能なソース由来のコンテンツを対象にできます。

この skill は、CJK テキストが読みやすいか、改行が適切か、約物や間隔が自然かを確認し、W3C の文字組版要件に照らして問題を整理します。

## 準拠する要件

- [JLReq：日本語組版処理の要件](https://www.w3.org/TR/jlreq/)
- [CLReq：中文排版需求](https://www.w3.org/TR/clreq/)
- [KLReq：한국어 텍스트 레이아웃 및 타이포그래피를 위한 요구사항](https://www.w3.org/TR/klreq/)

## 確認できる項目

- 言語指定と locale metadata
- 横組み、縦組み、混在する書字方向
- 改行、行頭禁則、行末禁則
- 約物の間隔、ぶら下げ、連続する約物の処理
- ruby、ふりがな／注釈、強調標記、行内注
- CJK とラテン文字の混在、数字、日付、記号
- 段落間隔、揃え、孤立行、孤立字、見出し、改ページ
- 電子書籍や PDF のページ構成、柱、図版、表、注

## 使い方

この skill を利用できる agent runtime で、次の prompt を使います。

```text
$cjk-layout-audit を使って、この CJK の Web ページまたは電子書籍を W3C の文字組版要件に照らして監査してください。
```

監査範囲が大きい場合は、対象 URL、ローカルファイル、スクリーンショット、電子書籍／PDF、想定言語、確認したいデバイスやページサイズを指定してください。

監査結果には、具体的な問題、影響範囲、証拠、対応する W3C 要件、影響、修正案が含まれるべきです。

## Codex Plugin

GitHub からインストール：

```bash
codex plugin marketplace add sichengchen/cjk-layout-audit-skill
```

ローカル checkout からインストール：

```bash
codex plugin marketplace add /path/to/cjk-layout-audit-skill
```
