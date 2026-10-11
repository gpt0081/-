# Run172 사건 그래프 통합 인덱스

1952년 국회 감독·사법절차·농정·재정·노동·경찰·인사·지방복지·통신·산업의 사건/하위사건 **20개**를 `data/events.json`에 기존 구조를 유지한 채 추가했다.

원자료 계층: `data/events/run172-accountability-four.json`, `run172-rice-cabinet.json`, `run172-agriculture-two.json`, `run172-labor-assembly-two.json`, `run172-local-two.json`, `run172-policy-three.json`, `run172-diplomacy-election-two.json`, `run172-veterans.json`, `run172-party-convention.json`, `run172-police-appointment-two.json`.

각 사건은 가능한 범위에서 `proposed_by`, `decided_by`, `executed_by`, `opposed_by`, `legal_authority`, `observed_by`를 구분한다. 중앙 registry의 `politicians`은 정식 인물 ID만, `candidatePoliticians`은 미승격 후보 ID만 포함한다.

관련 주장/반증: `data/claims/run172-*.json`의 13개. 문서 registry: `data/documents/run172-*.json`의 서로 다른 원문 위치 47건. 신문 전사·공식 관보 원문·FRUS 외교문서·후대 해설을 구별한다.

**검증 유보:** 10/30 불신임 103/105표, 12/4 입도선매 통계, 11/8 미곡자금 집행, 전화 6000/5000대 발표, 영장 집행, 대통령 개인의 직접지시.
