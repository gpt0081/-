# Architecture

## Product boundary

이 프로젝트는 대한민국 정치인을 평가하거나 선거 선택을 추천하는 시스템이 아니다. 장기 목표는 **대한민국 역대 정치인 전체의 검증 가능한 디지털 실록**을 구축하는 것이다. 공개 기록을 구조화하고 인물·사건·기관·정당·정책·법률 사이 관계를 연결해 사용자가 원문과 맥락을 직접 검토하게 하는 evidence ledger다.

대통령 임기순 탐색은 초기 수집 backbone이며 데이터 모델의 계층이 아니다. 대통령, 총리, 장관, 국회의원, 정당 지도부, 지방자치단체장, 정부수립기·독립운동기 주요 정치인은 모두 동일한 `politician` 노드다.

## Core entities

- `politicians`: stable ID, 이명/한자/영문명, 생몰, 시기별 직책·정당/정파, 조사상태, evidence/annals/history-debt 연결
- `roles`: 익명·가명·집단 행위자 슬롯. `candidateRoleId`·`candidateGroupId`를 별도 stable role ID로 보존하며, 실명·동일인 근거가 확보되기 전에는 정치인 노드로 승격하지 않음
- `events`: stable ID를 가진 사건. 관련 정치인·기관·정당·법률·정책·결정·집행·반대·결과·후대판단 연결
- `records`: 날짜가 있는 발언·공약·표결·정책·행동·해명
- `sources`: 각 record/event의 근거, 원문 위치, provenance와 접근일
- `institutions`: 정부기관·국회·정당·법원·군·경찰 등 행위 주체
- `relationships`: 정치인↔사건↔기관↔정당↔정책 사이의 역할 기반 edge
- `principles`: 반복해서 적용되는 규범적 기준을 정규화한 객체
- `comparisons`: 두 record를 나란히 검토할 수 있도록 연결한 후보 관계
- `history_debt`: 아직 확인되지 않은 명령계통·책임선·원문·상충 증언·접근불가 기록

comparison은 판정이 아니라 검토 객체다.

## Migration strategy

기존 `data/presidents.json`과 `president-*` ID는 즉시 폐기하지 않는다. `data/politicians.json`의 stable ID와 `legacyIds`를 통해 점진적으로 일반화한다. 기존 evidence/annals 파일도 깨뜨리지 않고 registry에서 연결한다. 이름이 가려진 직책 보유자, 미확인 서명자 집단, 익명 위원회 구성원은 `roles`에 보존하고, 신원 확인 전 정치인 ID를 부여하지 않는다. 대통령 중심 UI 역시 향후 정치인·사건 중심 탐색을 추가할 수 있게 별도 view로 취급한다.

## Event graph

사건은 특정 대통령 실록의 하위 문단이 아니라 독립 객체다. 동일 사건에서 다음 역할을 분리한다.

1. 제안자
2. 공식 결정권자
3. 명령 발신자
4. 집행자
5. 반대·견제자
6. 보고 수신자
7. 사후 조사·판단 기관

재임 중 발생했다는 사실과 직접 명령은 같은 edge가 아니다. 각 관계는 가능한 경우 원문 source를 가진다.

## Two-stage architecture

### Stage A — GitHub evidence ledger

GitHub를 조사 원장과 변경 이력의 기준점으로 사용한다. 원자료 URL, 날짜, 발언/행동, 사건 관계, 당시 문맥, 반론·반증, 비교 후보, 미해결 단서, 역사부채, 데이터 변경 이력을 축적한다.

### Stage B — Floot application

충분한 조사 batch가 형성되고 사용자가 별도로 요청했을 때만 GitHub 데이터를 Floot DB/UI에 반영한다. Floot는 검색/필터, 정치인 탐색, 대통령 backbone view, 사건 graph view, 과거/이후 기록 병렬 보기, 원문 링크, 검토 상태를 제공하는 배포·인터랙션 계층이다.

## Publication pipeline

1. 출처/사건 발견
2. 기존 정치인·사건 stable ID 확인 또는 후보 생성
3. GitHub evidence ledger 기록
4. 사실 중심 record와 관계 edge 후보 생성
5. 반증·상반 자료 검색
6. 원문·문맥·달라진 조건·당사자 설명 확인
7. unresolved는 history debt/open lead로 유지
8. 충분한 batch 형성
9. Floot 반영은 별도 요청 시 수행
10. 사람의 검토
11. published 상태로 승격

자동 위선 점수, 선악 판정, 정당 순위, 후보 추천은 만들지 않는다.
