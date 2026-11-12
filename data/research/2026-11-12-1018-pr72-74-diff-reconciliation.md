# 2026-11-12 10:18 KST | PR #72–74 실제 diff 기반 중복 통합 게이트

## 검토 범위
GitHub main README, 운영지침, 역사부채, presidents/politicians, 기존 09:12 identity ledger와 05:20 research overlay, 최근 커밋, 열린 PR 메타데이터를 읽고 PR #72, #73, #74의 **실제 unified diff**를 각각 열어 변경 파일과 주요 actor/claim ID를 대조했다. PR 본문의 정량 성과는 이번 회차 직접 원문 열람으로 재계산하지 않았다.

## 확인된 브랜치 의존성과 파일 충돌
- #72: base `research/run222-febmar1952-frus-policy-actor-crosscheck`, head `research/run223-apr1952-pow-elections-governance`; 변경 파일 14개.
- #73: base `research/run223-apr1952-pow-elections-governance`, head `research/run224-may1952-constitutional-pow-economy`; 변경 파일 18개.
- #74: base `research/run224-may1952-constitutional-pow-economy`, head `research/run225-june1952-cabinet-unc-pow`; 변경 파일 16개.
- 세 PR 모두 `data/politicians.json`을 변경한다. #73과 #74는 `data/research/HISTORY_DEBT.md`, `data/research/rhee-syngman-coverage.json`, `data/research/rhee-syngman-open-leads.json`도 겹친다. **독립 PR 3개를 main에 순서 없이 합치는 것은 위험**하다. #72의 base가 main도 아니므로 선행 #71/#70 계보까지 먼저 확인해야 한다.
- #74 diff에는 `1952-06-03 이범석의 전 국회의원 체포 제안은 이승만의 실행된 직접 체포명령이다`라는 claim 문구가 있다. 이 문구의 존재 자체는 그 주장의 승인/입증을 뜻하지 않는다. claim의 polarity, supporting/contradicting evidence를 실제 JSON 문맥에서 검증해야 한다.
- #74 diff의 1952-06-03 행위/인물 기록은 `pol-lee-beom-seok`을 사용한다. main의 05:20 overlay는 `candidate-1952-yi-pom-sok`을 사용한다. 이들은 **동일 사건 중복 가능성이 있는 crosswalk 후보**이지 자동 동등성 확정이 아니다.
- #73과 #74의 diff에 `pol-pyun-yong-tae`가 등장한다. main 05:20 overlay의 `candidate-1954-pyun-yung-tai`와 연결 후보지만, 해당 PR들의 1952년 사건을 1954년 제네바 사건과 같은 사건으로 합치면 안 된다.
- main registry의 `pol-lee-beom-seok` / `pol-lee-beom-seok-1900` 신원 충돌은 계속 보존한다. PR #74가 전자를 쓴다는 이유만으로 후자를 삭제하거나 두 인물을 병합하지 않는다.

## 다음 단계 (구체적 실행 순서)
1. #71 → #72 → #73 → #74의 base/head SHA 및 변경 파일 해시를 대조하여 누적 브랜치 계보를 확정한다.
2. #74 `data/claims/run225-june1952-adversarial.json`의 위 6월 3일 명제 전체 객체를 읽어 **반증 가설인지 채택된 사실인지** 구별한다.
3. #74 `data/events/run225-june1952-actor-decision-graph.json`의 6월 3일 행위 ID와 main overlay의 3개 1952년 action ID를 날짜·행위·문서 ID로 매칭한다.
4. #73 `data/research/corrections/run224-identity-guardrail.json`을 읽어 동명이인 방지규칙과 기존 possibleSameAs 관계를 보존한다.
5. 이범석 두 중앙 ID의 각 inbound reference 및 1948/1952 관보 임명원문을 확인한 뒤에만 canonical ID migration을 검토한다.
6. 1952-06-03 한국 국무회의 원회의록·출석부 및 국회 개헌안 접수대장으로 장면/이범석 관련 미국측 간접전언을 반증 검토한다.
7. 1954년 변영태 제네바 한국측 훈령·초안과 6월 15일 선언 원본을 확인해 1952년 외교·내각 actor와 분리한다.

## 판정
**DIFF_INSPECTED_NOT_MERGED**. 실제 PR diff 3개를 확인했고 누적 브랜치 관계와 중복 가능성을 구체화했다. 원본 한국 사료·FRUS 신규 열람은 0건, 새로운 정치인 승격 0명, 신규 event 0건, 독립 출처 교차확증 0묶음, 새 history-debt 해결 0건이다. 위 7개는 기존 문제를 구체화한 next actions이며 새로운 역사적 사실 7건이 아니다. 본 문서만 추가하는 감사 커밋은 중앙 데이터 동기화 완료를 의미하지 않는다. 1시간 실행 주장 없음. 역사부채 주간 전수조사 미실시 (목요일). Floot 수정·빌드 없음.
