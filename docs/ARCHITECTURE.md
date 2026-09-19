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

## Publication pipeline

1. 출처 발견
2. 사실 중심 record 후보 생성
3. 주제와 가능한 principle 추출
4. 같은 주제의 다른 시점 기록 검색
5. comparison candidate 생성
6. 원문·문맥·달라진 조건·당사자 설명 확인
7. 사람의 검토
8. published 상태로 승격

자동 위선 점수, 정당 순위, 후보 추천은 만들지 않는다.

## Floot implementation

Floot 버전은 Postgres 기반으로 동작한다. 공개 홈은 published comparison만 읽는다. 연구 루프가 수집한 후보는 research_candidates의 pending 상태에만 저장되고 공개 데이터로 자동 승격되지 않는다.

자세한 수집 정책은 docs/RESEARCH_LOOP.md를 참고한다.
