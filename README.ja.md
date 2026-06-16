# CJK Layout Audit Agent Skill

[English](README.md) | [繁體中文](README.zh-Hant.md) | [简体中文](README.zh-Hans.md) | [한국어](README.ko.md)

このリポジトリには、W3C の文字組版要件に基づいて、フロントエンド画面、レンダリング済み Web ページ、EPUB/電子書籍、PDF、スクリーンショット、ソースファイル内の中国語・日本語・韓国語の文字レイアウトを監査する `cjk-layout-audit` agent skill が含まれています。

この skill は以下の W3C 文書に基づいています。

- [JLReq: Requirements for Japanese Text Layout](https://www.w3.org/TR/jlreq/)
- [CLReq: Requirements for Chinese Text Layout](https://www.w3.org/TR/clreq/)
- [KLReq: Requirements for Hangul Text Layout and Typography](https://www.w3.org/TR/klreq/)

## 内容

- `cjk-layout-audit/SKILL.md` - メインの skill 指示とワークフロー。
- `cjk-layout-audit/references/audit-model.md` - W3C 要件カテゴリ、重大度ルール、証拠基準。
- `cjk-layout-audit/references/artifact-contract.md` - `/goal` ループ、subagent、成果物、receipt、レポート契約。
- `cjk-layout-audit/scripts/cjk_layout_probe.py` - ローカルのテキスト、HTML/XHTML、CSS、EPUB を初期調査する補助スクリプト。
- `cjk-layout-audit/agents/openai.yaml` - skill の UI メタデータ。

## 使い方

Codex などの agent runtime では次のように skill を呼び出します。

```text
Use $cjk-layout-audit to audit this CJK webpage or ebook for W3C text layout issues.
```

単一ページの小さな確認を超える監査では、この skill は `/goal` ループを使い、対象範囲を subagent に分割し、surface ごとの receipt を要求し、宣言された監査範囲が閉じられてから完了するよう指示します。

## Probe Script

補助スクリプトをローカルファイルに対して実行すると、CJK 文字の含有状況、関連 CSS プロパティ、ruby マークアップ、不審な行頭・行末句読点、CJK/ラテン混在テキストのスペーシング手がかりを検出できます。

```bash
python3 cjk-layout-audit/scripts/cjk_layout_probe.py --json path/to/file.html
```

probe の出力は初期調査用の手がかりです。skill では、レイアウト finding を報告する前に、レンダリング済みまたは抽出済みの証拠を要求します。

## 検証

作成時に使用した基本的なローカルチェック:

```bash
python3 -B cjk-layout-audit/scripts/cjk_layout_probe.py --json path/to/file.html
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile cjk-layout-audit/scripts/cjk_layout_probe.py
```

Python 依存関係が利用できる場合は、Codex-compatible skill validator を実行できます。

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py cjk-layout-audit
```
