# 정치인 registry 확장 인덱스

- 기본 registry: `data/politicians.json` (기존 API 호환 유지)
- 2026-10-08 토지행정·제헌국회 독립 인물 12명: `data/politicians/run81-land-actors.json`
- 원문 기반 후보 상세: `data/research/candidates/run81-land-policy-actor-network.json`
- 안재홍 독립 실록: `data/annals/ahn-jae-hong.md`, 증거: `data/evidence/ahn-jae-hong.json`
- 신규 event/action: `data/events/run81-land-legal-actions.json`

조회 시 base와 overlay를 stable ID로 결합한다. 기존 ID를 삭제하거나 자동으로 덮어쓰지 않는다. `pol-lee-beom-seok-1900`과 `pol-lee-beom-seok`은 동일인 중복 의심이며 canonical은 후자로 제안하되 참조 전수조사 전 병합하지 않는다.


## 2026-10-08 · 제헌국회 식량법 의사절차 후보 10명 (run93)

`data/politicians/run93-grain-debate-candidates.json`: 공식 제헌국회 속기록 전사본의 실명·한자·의사행위에 근거한 독립 candidate ID 10명. 생몰·당적·지역구·동명이인 검증 전에는 정식 `data/politicians.json` 승격을 보류한다. 83:8은 철회안이 아니라 토론종결동의다.

## 2026-10-08 · 박상영 식량법 개정안 후보 (run95)
`data/politicians/run95-grain-actors.json`의 `pol-park-sang-yeong`은 1949-10-31·11-05 식량법 수정안 대표발의자 후보. 국사편찬위원회 헌정사 해제에 근거하며 국회 원속기록·생몰·한자·당선자원부 미대조. 후보 evidence/annals 별도 보존, 정식 승격 보류.

## 2026-10-08 · 교육법·계엄법 독립 후보 (run95 domain expansion)
`data/politicians/run95-domains-candidates.json`: 정광호(鄭光好)·김장열(金長烈)은 1949-10-25 제헌국회 제5회 제23차 계엄법 제2독회 원속기록의 서로 다른 수정안 발의자로 확인. 박희병(교육법 절충안)·안호상(문교부 초안)은 한국학중앙연구원 해제 단계의 후보로 등록. 네 명 모두 생몰·지역구·원면 보강 전 정식 registry 승격 보류.
