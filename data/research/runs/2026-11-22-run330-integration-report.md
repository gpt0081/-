# Run330 · 누적 연구자료 중앙 통합 감사

- 날짜: 2026-11-22 (Asia/Seoul)
- Source snapshot: `e2d528b73bed55037ffbb525a623c11ffc98049b`
- Source tree: `58ea5d18e1b142a631127a25d7d59cf93e5750d8`
- Commits: `bb7275ac36901b888044c83b28d440ca86ab97e5`, `e2d528b73bed55037ffbb525a623c11ffc98049b`
- 상태: **FULL_INTEGRATION_INCOMPLETE**
- 중앙 동기화: **CENTRAL_SYNC_PARTIAL**
- Floot: 수정·빌드하지 않음.

## 전체 source inventory

현재 `data/integration/` 바깥의 데이터 파일 2,274개를 전수 목록화했다. 각 per-group inventory에는 Git blob SHA, SHA-256, bytes, target layer/registry, record counts, source conflict pointers, unintegrated reason을 보존했다. 최신 per-file authority는 `data/integration/generated/source-triage.json`이다. MASTER_INDEX와 11개 group inventory를 2026-11-22 snapshot으로 갱신했다.

| 그룹 | 파일 수 |
|---|---:|
| annals | 145 |
| claims | 154 |
| documents | 190 |
| events shards | 143 |
| evidence | 65 |
| organizations | 15 |
| politician shards | 109 |
| research / runs / leads / coverage / graphs | 1,450 |
| operational roots: events.json, politicians.json, presidents.json | 3 |
| **합계** | **2,274** |

Source triage:
- BLOCKED_ID_CONFLICT: 341
- INDEXED_NOT_CANONICAL_VERIFIED: 597
- NON_JSON_PRESERVED: 777
- UNMAPPED_AUXILIARY_OR_PARTIAL: 556
- OPERATIONAL_ROOT_PRESERVED: 2
- PRESIDENTIAL_BACKBONE_PRESERVED: 1

## Canonical registry audit

| Registry | Materialized | Source records | Unique IDs | Conflicted IDs |
|---|---:|---:|---:|---:|
| Documents | 4,585 | 4,828 | 4,694 | 109 |
| Claims | 2,115 | 2,165 | 2,137 | 22 |
| Events | 2,679 | 2,827 | 2,747 | 66 |
| Politicians | 855 | 2,336 | 1,241 | 385 |
| Organizations | 83 | 97 | 85 | 2 |

합계 584 conflicting IDs, exact duplicate IDs 11, auxiliary records 677, unintegrated sources 563, partial sources 11, parse errors 0. Conflict payload는 삭제하거나 임의 선택하지 않았다.

## Central operational roots

- `data/events.json`: 2,808 events; canonical rows merged 2,681; missing IDs 0; duplicate IDs 0; unresolved field variants 16.
- `data/politicians.json`: 975 politicians; canonical rows merged 764; missing IDs 0; duplicate IDs 0; unresolved field variants 110; policy exclusions 92.
- Operational links: 202 linked / 310 unlinked. Unlinked: annals 62, evidence 1, coverage 6, history-debt 16, lead queues 225.
- Relations: politician 446, event 514, document 923, claim 13, organization 1.
- Structural audit: integrity issues 0, reference issues 0, crosswalk gaps 0.

**CENTRAL_SYNC_PARTIAL**이다. Root ID 누락·중복은 0이지만 126 root field variants, 584 source conflict IDs, 563 unintegrated sources, 310 unlinked operational files가 남아 있다. 구조 검사 PASS를 역사적 검증 완료로 오해하지 않는다.

## PR #73/#74/#72 확인

- PR #73: changed paths 18/18 main에 존재.
- PR #74: changed paths 16/16 main에 존재.
- PR #72: changed paths 29/29 main에 존재하지만 PR 자체는 OPEN.
- 파일 경로 존재, PR merge state, semantic integration은 서로 다른 상태다. 73/74의 파일 존재를 전체 중앙 통합 완료로 계산하지 않는다.

## Pass329 김성수 central linking

기존 stable ID `pol-r164-kim-seong-su`와 기존 두 사건 ID를 재사용했다. 김성수 문서 6개와 주장 2개는 canonical documents/claims registry에서 확인된다. 이번 batch에서 event source shard와 politician additive link-update를 추가하고 documents/claims/events/politicians index를 갱신했다. Workflow 후 root의 `researchRefs`에 documents/event shard 및 annals/coverage/open-lead 참조가 반영된 것을 확인했다. 신규 정치인·event·claim ID는 생성하지 않았다.

## Workflow validation

[GitHub Actions Run 88](https://github.com/gpt0081/-/actions/runs/44950899243)은 통합 스크립트 compile, source consolidation, central-root sync, operational linking, audit, per-source triage, politician reference audit를 모두 성공적으로 수행했다. 마지막 completeness gate는 남은 conflict/unintegrated references 때문에 실패했다. 이는 예상된 **FULL_INTEGRATION_INCOMPLETE** 차단이며 성공으로 포장하지 않는다.

## 실행 지표

| 지표 | 실제값 |
|---|---:|
| 신규 독립 역사 연구선 | 0 |
| 일반 국정영역 신규 보강 | 0 |
| 신규/심화 비대통령 정치인 조사 | 0 (기존 김성수 node 링크 1건) |
| 신규 event ID | 0 (기존 event 2건 source shard 재연결) |
| 신규 claim ID | 0 (기존 claim 2건 canonical 확인) |
| 새로 직접 열어 확인한 역사 문서 | 0 |
| 공식·1차 원문 직접 열람 | 0 |
| adversarial searches | 0 |
| 독립 provenance 교차검증 묶음 | 0 |
| 기존 history-debt/open leads 실질 추적 | 0 |
| 새 구체적 integration leads | 33 |
| Floot 변경 | 0 |

기존 Run329 source shard의 문서·주장은 Run330 직접 열람 수치에 포함하지 않는다. 실제 1시간 실행을 주장하지 않는다.

## 역사부채 주간 전수조사

**역사부채 주간 전수조사 미실시.** 2026-11-22 전체 OPEN/NARROWED/BLOCKED/CONFLICTED/REOPENED 항목을 재조사하지 않았으며 `last_full_review`를 변경하지 않았다.

## 수정 파일

- `data/documents/INDEX.md`, `data/claims/INDEX.md`, `data/events/INDEX.md`, `data/politicians/INDEX.md`
- `data/events/run329-kim-seong-su-resignation.json`
- `data/politicians/run330-kim-seong-su-central-links.json`
- `data/research/ACTIVE_RESEARCH_HANDOFF.json`
- `data/research/runs/2026-11-22-run330-integration-report.md`
- `data/research/runs/2026-11-22-run330-integration-ledger.json`
- `data/research/lead-queues/run330-next-integration.json`
- `data/integration/PR_BACKLOG_73_74.json`
- `data/integration/MASTER_INDEX.json`, `data/integration/INTEGRATION_STATUS.md`, 11개 `data/integration/inventory/*.json`

## 다음 실행

33개 구체 lead는 `data/research/lead-queues/run330-next-integration.json`에 있다. 먼저 FRUS/국편/관보/국회 원문이 겹치는 document conflict 109건을 provenance 단위로 해소하고, 그 다음 정치인 status/identity variant와 event evidenceState/uncertainty variant를 correction history와 함께 중앙 root에 반영한다. 563 unintegrated sources와 310 unlinked operational files를 계속 줄인다.
