# Architecture

## Product boundary

눈가리고아웅판별기는 정치인을 평가하거나 선거 선택을 추천하는 시스템이 아니다. 공개 기록을 구조화하고, 서로 비교할 가치가 있는 기록을 연결해 사용자가 원문과 맥락을 직접 검토하게 하는 evidence ledger다.

## Core entities

- politicians: 추적 대상 인물의 식별 정보
- records: 날짜가 있는 발언·공약·표결·정책·행동·해명
- sources: 각 record의 근거 출처
- principles: 반복해서 적용되는 규범적 기준을 정규화한 객체
- comparisons: 두 record를 나란히 검토할 수 있도록 연결한 후보 관계

comparison은 판정이 아니라 검토 객체다.

## Two-stage architecture

### Stage A — GitHub evidence ledger

수동 GPT 조사 루프는 GitHub를 기준 저장소로 사용한다.

- 원자료 URL
- 날짜
- 발언 또는 행동
- 당시 문맥
- 반론/예외 사유
- 비교 후보
- 미해결 단서
- 데이터 변경 이력

을 축적한다.

이 단계에서는 조사량을 우선하고, Floot build action을 소비하지 않는다.

### Stage B — Floot application

충분한 묶음이 만들어졌을 때만 GitHub 데이터를 Floot DB/UI에 반영한다.

Floot의 역할:

- 구조화된 DB
- 검색/필터
- 대통령 임기순 탐색
- 과거/이후 기록 병렬 보기
- 출처 원문 링크
- 검토 상태 표시
- 공개 웹앱

## Publication pipeline

1. 출처 발견
2. GitHub evidence ledger 기록
3. 사실 중심 record 후보 생성
4. 주제와 가능한 principle 추출
5. 같은 주제의 다른 시점 기록 검색
6. comparison candidate 생성
7. 원문·문맥·달라진 조건·당사자 설명 확인
8. 충분한 batch 형성
9. Floot DB/UI 반영
10. 사람의 검토
11. published 상태로 승격

자동 위선 점수, 정당 순위, 후보 추천은 만들지 않는다.

자세한 수집 정책은 docs/RESEARCH_LOOP.md, Floot 반영 정책은 docs/FLOOT_BUILD_POLICY.md를 참고한다.
