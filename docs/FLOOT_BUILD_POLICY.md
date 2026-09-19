# Floot Build Policy

## 기본 원칙

> **GitHub First, Floot Batch Build.**

Floot는 매 조사 회차의 작업 공간으로 사용하지 않는다. 수동 조사와 증거 축적은 GitHub에서 계속 진행하고, 정보가 충분히 모였을 때만 Floot를 갱신한다.

## Floot 빌드 조건

다음 중 하나 이상을 만족할 때 빌드한다.

- 한 정치인의 기본 기록 축이 충분히 채워짐
- 10건 이상 새 검증 기록이 축적됨
- 3건 이상 의미 있는 comparison candidate가 축적됨
- DB 스키마 변경이 필요함
- 사용자 경험에 의미 있는 UI 변경이 필요함
- 사용자가 직접 Floot 반영을 요청함

숫자는 강제 규칙이 아니라 기본 batching 기준이다.

## 하지 않는 것

- 검색 한 번 할 때마다 Floot 수정
- 출처 하나 추가할 때마다 DB migration
- 미검증 research candidate를 바로 공개
- 단순 문서 변경 때문에 앱 재빌드

## 기준 저장소

GitHub가 조사 원장과 provenance의 기준점이다.

Floot DB는 공개/탐색용 파생 저장소로 취급한다. 두 저장소가 충돌하면 검증된 GitHub evidence ledger를 기준으로 Floot를 재생성/수정한다.
