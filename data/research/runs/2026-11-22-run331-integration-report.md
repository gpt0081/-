# 대한민국 정치인 실록 · Run331 중앙 통합 보고 (2026-11-22)

## 실행 범위

이번 회차는 새 사료 발굴보다 누적 연구자료의 중앙 통합, PR #73/#74 후속 검토, 인물·사건 attribution correction, 역사부채 주간검토 상태 정합성 복구를 우선했다. 1시간 실행을 주장하지 않는다. 이 보고는 새 역사 원문 조사 성과가 아니라 실제 저장소 감사와 데이터 수정 내역이다.

## 실제로 반영한 수정

- `claim-r225-cabinet-unanimous-dissolution`: FRUS d163을 지지 근거에서 제거하고 반대 근거로 유지했다. 해당 문서는 장택상의 간접 보고에서 내각 다수의 반대를 전하므로 '만장일치 지지'를 지지하지 않는다. 전체 claim 상태는 OPEN/adversarial 상태로 유지했다.
- `evt-r225-july-arrest-report`: 1952-07-07 보도에서 확인되지 않는 `pol-r164-seo-min-ho`를 사건 행위자 목록에서 제거했다. 서민호의 별도 국무회의/지휘계통 기록은 `evt-r225-cabinet-command-chain`에 남겼다.
- 2026-10-04 주간 전수조사 보고서가 존재하고 `history-debt-review-state.json`도 해당 날짜를 가리키므로 마지막 완료일을 2026-10-04로 정합화했다. 2026-11-22 시도는 INCOMPLETE로 유지하고 같은 날 재시도하지 않았다.

## 중앙 통합 감사 수치

| 계층 | 현재 감사값 |
|---|---:|
| 원본 data 파일 | 5184 |
| 비JSON 원본 보존 | 1315 |
| 충돌 검토 필요 파일 | 513 |
| 보조 JSON 인덱싱 | 1584 |
| 정식 canonical materialization | 1754 |
| 부분 canonical materialization | 15 |
| 고유 충돌 ID | 915 |
| 미통합 소스 | 1599 |
| 보조 레코드 | 2244 |
| 부분 소스 | 15 |
| 파싱 오류 | 0 |

Canonical materialized: documents 11683, claims 4983, events 6205, politicians 1569, organizations 263, roles 65.

Root sync: events 6334/6205 (missing 0, duplicates 0, unresolved field conflicts 11); politicians 1807/1321 (missing 0, duplicates 0, unresolved field conflicts 35).

Operational sidecars: 1405 files, 518 explicitly linked and 887 without explicit identity. Unlinked breakdown: {"annals":426,"coverage":72,"evidence":192,"history_debt":164,"lead_queue":551}. Structural audit: 300 integrity issues, 292 reference issues, 0 crosswalk gaps.

## PR #73/#74 reconciliation

- PR #73: 18 changed paths present; 11 identical and 7 shared-path variants.
- PR #74: 16 changed paths present; 12 identical and 4 shared-root variants.
- PR #74 snapshot: 453/453 branch politician IDs are present in the 1,807-record main root; 0 branch-only, 1,354 main-only. All 453 shared records still have field differences. ID coverage is complete; semantic field reconciliation is not.
- PR #72 remains open and diverged. No whole-branch merge was attempted.

## 상태와 한계

**FULL_INTEGRATION_INCOMPLETE / CENTRAL_SYNC_PARTIAL**

Canonical registry가 존재하고 root에 missing ID가 0개라는 사실은 전체 통합 완료를 뜻하지 않는다. 915개 충돌 ID, 1,599개 미통합 소스, 887개 identity-unlinked operational sidecar, 11개 event root 및 35개 politician root field conflict, 300개 structural integrity issue와 292개 reference issue가 남아 있다. 원본을 삭제하거나 임의의 canonical winner를 선택하지 않았다.

- 역사부채 주간 전수조사: **미실시**. 2026-11-22 첫 시도가 이미 INCOMPLETE로 기록되어 있어 같은 날짜에 반복하지 않았다. 마지막 완료일은 2026-10-04, 다음 예정일은 2026-11-29.
- 새 역사 원문 직접 확인: 0건. 이 회차는 integration-first이며 연구량 하한을 달성했다고 주장하지 않는다.
- Floot: 수정하지 않았고 빌드하지 않았다.

## 다음 통합 우선순위

구체적인 33개 충돌·운영 계층 표적은 `data/integration/next-integration-leads-2026-11-22.json`에 저장했다. 첫 우선순위는 FRUS/국회/관보 문서 ID 충돌, 1952~54 사건의 책임·표결 관계, 이범석·장택상·백두진·장면·정일권 등 비대통령 인물의 날짜별 직책/사건 연결, 그리고 인물 실록·증거·coverage sidecar의 명시적 ID 연결이다.

이번 회차의 source inventory는 5184개를 감사했다. 본 보고서와 ledger 2개가 추가되어 다음 workflow가 5186개 source file 기준으로 per-file inventory를 다시 생성해야 한다.
