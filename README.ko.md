# CJK 텍스트 레이아웃 감사 Agent Skill

[English](README.md) | [繁體中文](README.zh-Hant.md) | [简体中文](README.zh-Hans.md) | [日本語](README.ja.md)

`cjk-layout-audit`는 중국어, 일본어, 한국어 텍스트 레이아웃을 감사하기 위한 agent skill입니다. 웹페이지, 프런트엔드 앱, 전자책, PDF, 스크린샷, 렌더링 가능한 소스 기반 콘텐츠를 대상으로 사용할 수 있습니다.

이 skill은 CJK 텍스트가 읽기 쉬운지, 줄바꿈이 적절한지, 문장부호와 간격이 자연스러운지 확인하고, W3C 텍스트 레이아웃 요구사항에 맞춰 문제를 정리합니다.

## 기준 문서

- [JLReq: 日本語組版処理の要件](https://www.w3.org/TR/jlreq/)
- [CLReq: 中文排版需求](https://www.w3.org/TR/clreq/)
- [KLReq: 한국어 텍스트 레이아웃 및 타이포그래피를 위한 요구사항](https://www.w3.org/TR/klreq/)

## 확인 항목

- 언어 지정과 locale metadata
- 가로쓰기, 세로쓰기, 혼합 쓰기 방향
- 줄바꿈, 줄 시작 금칙, 줄 끝 금칙
- 문장부호 간격, 매달린 문장부호, 연속 문장부호 처리
- ruby, 주석, 강조 표시, 인라인 주
- CJK와 라틴 문자 혼합, 숫자, 날짜, 기호
- 문단 간격, 정렬, 고립 행, 고립 글자, 제목, 페이지 나눔
- 전자책 또는 PDF의 페이지 구성, 머리말, 그림, 표, 주석

## 사용 방법

이 skill을 사용할 수 있는 agent runtime에서 다음 prompt를 사용합니다.

```text
$cjk-layout-audit를 사용해 이 CJK 웹페이지 또는 전자책이 W3C 텍스트 레이아웃 요구사항에 맞는지 감사해 주세요.
```

감사 범위가 크다면 대상 URL, 로컬 파일, 스크린샷, 전자책/PDF, 예상 언어, 확인할 기기나 페이지 크기를 함께 제공하세요.

감사 결과에는 구체적인 문제, 영향을 받는 범위, 증거, 대응되는 W3C 요구사항, 영향, 수정 제안이 포함되어야 합니다.

## Codex Plugin

GitHub에서 설치:

```bash
codex plugin marketplace add sichengchen/cjk-layout-audit-skill
```

로컬 checkout에서 설치:

```bash
codex plugin marketplace add /path/to/cjk-layout-audit-skill
```
