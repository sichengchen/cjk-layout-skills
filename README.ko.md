# CJK 텍스트 레이아웃 Agent Skills

[English](README.md) | [繁體中文](README.zh-Hant.md) | [简体中文](README.zh-Hans.md) | [日本語](README.ja.md)

이 repository에는 중국어, 일본어, 한국어 텍스트 레이아웃을 위한 agent skill 두 개가 포함되어 있습니다.

- `cjk-layout`: W3C JLReq, CLReq, KLReq에 따라 CJK 텍스트 레이아웃을 설계하고 구현하는 방법을 coding agent에게 알려 줍니다.
- `cjk-layout-audit`: 웹페이지, frontend app, 전자책, PDF, 스크린샷, 소스에서 렌더링되는 CJK 텍스트 레이아웃을 감사합니다.

레이아웃을 만들거나 수정할 때는 `cjk-layout`을 사용합니다. 표시된 결과를 확인하고 증거 기반 지적 사항을 만들 때는 `cjk-layout-audit`를 사용합니다.

## 대응 표준

- [JLReq: 日本語組版処理の要件](https://www.w3.org/TR/jlreq/)
- [CLReq: 中文排版需求](https://www.w3.org/TR/clreq/)
- [KLReq: 한국어 텍스트 레이아웃 및 타이포그래피를 위한 요구사항](https://www.w3.org/TR/klreq/)

## 다루는 항목

- 언어 지정과 locale metadata
- 가로쓰기, 세로쓰기, 쓰기 방향 혼합
- 줄바꿈, 줄 시작 금칙, 줄 끝 금칙 처리
- 문장부호 간격, hanging punctuation, 연속 문장부호 처리
- ruby, 발음 주석, 강조 표시, 인라인 주
- CJK와 라틴 문자 혼합, 숫자, 날짜, 기호
- 문단 간격, 정렬, 고립 행, 고립 글자, 제목, 페이지 나눔
- 전자책 또는 PDF의 페이지 구성, 페이지 머리글, 그림, 표, 주석

## 사용 방법

이 skills를 지원하는 agent runtime에서 다음 prompt를 입력합니다.

```text
$cjk-layout를 사용해 이 중국어, 일본어 또는 한국어 레이아웃을 W3C 텍스트 레이아웃 요구사항에 맞게 구현해 주세요.

$cjk-layout-audit를 사용해 이 CJK 웹페이지 또는 전자책이 W3C 텍스트 레이아웃 요구사항에 맞는지 감사해 주세요.
```

구현 작업에서는 대상 언어, locale, UI surface, 쓰기 방향, 렌더링 매체를 지정합니다. 감사 범위가 큰 경우 대상 URL, 로컬 파일, 스크린샷, 전자책 또는 PDF, 예상 언어, 확인 대상 기기 또는 페이지 크기를 지정합니다.

감사 결과로 구체적인 문제, 영향 범위, 증거, 대응되는 W3C 요구사항, 영향, 수정 방법을 반환합니다.

## Codex Plugin

작성자의 Codex Marketplace를 추가합니다.

```bash
codex plugin marketplace add sichengchen/codex-plugins
```

이어서 `cjk-text-layout` 플러그인을 설치합니다.

---

이 README는 영어로 작성되었으며 LLM이 한국어로 번역한 문서입니다.
