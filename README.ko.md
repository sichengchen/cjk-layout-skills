# CJK Layout Audit Skill

[English](README.md) | [繁體中文](README.zh-Hant.md) | [简体中文](README.zh-Hans.md) | [日本語](README.ja.md)

이 저장소에는 W3C 텍스트 레이아웃 요구사항을 기준으로 프런트엔드 화면, 렌더링된 웹페이지, EPUB/전자책, PDF, 스크린샷, 소스 파일의 중국어, 일본어, 한국어 텍스트 레이아웃을 감사하는 `cjk-layout-audit` Codex skill 이 포함되어 있습니다.

이 skill 은 다음 W3C 문서를 기반으로 합니다.

- [JLReq: Requirements for Japanese Text Layout](https://www.w3.org/TR/jlreq/)
- [CLReq: Requirements for Chinese Text Layout](https://www.w3.org/TR/clreq/)
- [KLReq: Requirements for Hangul Text Layout and Typography](https://www.w3.org/TR/klreq/)

## 구성

- `cjk-layout-audit/SKILL.md` - 주요 skill 지침과 워크플로.
- `cjk-layout-audit/references/audit-model.md` - W3C 요구사항 범주, 심각도 규칙, 증거 기준.
- `cjk-layout-audit/references/artifact-contract.md` - `/goal` 루프, subagent, 산출물, receipt, 보고서 계약.
- `cjk-layout-audit/scripts/cjk_layout_probe.py` - 로컬 텍스트, HTML/XHTML, CSS, EPUB 초기 조사를 위한 보조 스크립트.
- `cjk-layout-audit/agents/openai.yaml` - skill UI 메타데이터.

## 사용

Codex 에서 다음과 같이 skill 을 호출합니다.

```text
Use $cjk-layout-audit to audit this CJK webpage or ebook for W3C text layout issues.
```

단일 페이지 수준의 작은 확인을 넘어서는 감사에서는 이 skill 이 `/goal` 루프를 사용하고, 범위를 subagent 로 나누며, 각 surface 의 receipt 를 요구하고, 선언된 감사 범위가 닫힌 뒤에만 완료하도록 지시합니다.

## Probe Script

보조 스크립트를 로컬 파일에 실행하면 CJK 문자 포함 여부, 관련 CSS 속성, ruby 마크업, 의심스러운 줄 시작/끝 문장부호, CJK/라틴 혼합 텍스트 간격 단서를 확인할 수 있습니다.

```bash
python3 cjk-layout-audit/scripts/cjk_layout_probe.py --json path/to/file.html
```

probe 출력은 초기 조사 단서일 뿐입니다. 이 skill 은 레이아웃 finding 을 보고하기 전에 렌더링되었거나 추출된 증거를 요구합니다.

## 검증

생성 중 사용한 기본 로컬 검사:

```bash
python3 -B cjk-layout-audit/scripts/cjk_layout_probe.py --json path/to/file.html
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile cjk-layout-audit/scripts/cjk_layout_probe.py
```

Python 의존성이 준비되어 있으면 공식 skill validator 를 실행할 수 있습니다.

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py cjk-layout-audit
```
