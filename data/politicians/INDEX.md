# 비대통령 정치인 후보 인덱스

정식 정치인 registry: `data/politicians.json`. 아래 overlay는 기존 ID를 파괴하지 않고 별도 후보와 증거를 추가한다.

- `data/politicians/run110-1950-administrative-actors.json`: 기존 4명 심화, 1950-06-12 경제안정위원회 관료 후보 6명.
- `data/politicians/run110e-1950-political-actors.json`: 1950-05~06 정당·관료·지방행정·지주대표 후보 17명. 생몰·임면 원문과 동명이인 미검증.
- `data/politicians/run109-people-index.md`: 기존 1950 인물망.

성숙도는 DISCOVERED → IDENTIFIED → VERIFIED → ANNALS_ACTIVE → MATURE로만 관리하며 정치적 평가점수는 사용하지 않는다. 기존 노드와 중복 여부 확인 전 candidate ID를 stable registry로 승격하지 않는다.
