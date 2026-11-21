# Run330 · 누적 연구자료 중앙 통합 감사

- 날짜: 2026-11-22 (Asia/Seoul)
- 기준 main commit: `90e3bbea6b082e075d8c3cb6e57b6faf4fab5d56`
- 실행 유형: 통합·무결성 우선. 신규 역사 원문 채굴 회차가 아님.
- 상태: **FULL_INTEGRATION_INCOMPLETE**
- 중앙 동기화: **CENTRAL_SYNC_PARTIAL**
- Floot: 수정·빌드하지 않음.

## 핵심 결과

기준 main snapshot에서 `data/integration/` 바깥의 데이터 파일 2,269개를 전수 목록 기준으로 대조했다. 최신 per-source triage는 각 파일에 SHA-256, 바이트 수, 대상 layer/registry, record counts, 충돌 ID, 미통합 사유를 붙인다. 기존 per-group inventory와 MASTER_INDEX는 2026-11-13 tree snapshot(2,239 files)을 가리켜 현재 파일 범위보다 오래되었다. 따라서 현재 기준은 `data/integration/generated/source-triage.json`과 `sources.json`으로 두고, 오래된 inventory shard는 historical snapshot으로 취급한다.

| 항목 | 확인값 |
|---|---:|
| source files | 2,269 |
| BLOCKED_ID_CONFLICT | 341 |
| INDEXED_NOT_CANONICAL_VERIFIED | 595 |
| NON_JSON_PRESERVED | 776 |
| UNMAPPED_AUXILIARY_OR_PARTIAL | 554 |
| OPERATIONAL_ROOT_PRESERVED | 2 |
| PRESIDENTIAL_BACKBONE_PRESERVED | 1 |
| source-level conflicting IDs | 584 |
| exact duplicate IDs | 11 |
| auxiliary records | 675 |
| unintegrated sources | 561 |
| partial sources | 11 |
| parse errors | 0 |

## Canonical registry materialization

| Registry | Canonical materialized records | Source records | Unique IDs | Conflicted IDs |
|---|---:|---:|---:|---:|
| Documents | 4,585 | 4,828 | 4,694 | 109 |
| Claims | 2,115 | 2,165 | 2,137 | 22 |
| Events | 2,679 | 2,825 | 2,745 | 66 |
| Politicians | 855 | 2,335 | 1,240 | 385 |
| Organizations | 83 | 97 | 85 | 2 |

합계 584 conflict IDs는 문서·주장·사건·정치인·기관 사이에서 각각 보존해야 한다. 같은 ID라고 무조건 한 payload를 선택하지 않는다. exact duplicate ID 11건도 단순 삭제하지 않고 provenance와 payload equality를 확인해야 한다.

## Operational roots and cross-links

- `data/events.json`: 2,808 root events, 2,679 canonical materialized IDs merged, missing canonical IDs 0, duplicate root IDs 0, scalar field variants 16.
- `data/politicians.json`: 975 root politicians, 763 canonical materialized IDs merged, missing canonical IDs 0, scalar field variants 110, policy-excluded external/organization/placeholder records 92.
- Operational layer scan: linked 201 / unlinked 310. Unlinked breakdown: annals 62, evidence 1, coverage 6, history-debt 16, lead queues 225.
- Relation counts: politician 438, event 507, document 908, claim 12, organization 1.
- Structural integrity audit: integrityIssues 0, referenceIssueCount 0, crosswalkGaps 0. 이는 구조 검사 결과이며 역사적 사실의 진실성이나 provenance 독립성 검증을 뜻하지 않는다.

**CENTRAL_SYNC_PARTIAL** 판정 이유: root ID 누락·중복은 0이지만 root scalar field variants 126건, source conflict IDs 584건, unintegrated sources 561건, operational unlinked 310건이 남아 있다. 따라서 PASS로 승격하지 않는다.

## PR #73/#74 및 연관 PR #72

- PR #73 changed paths: 18/18 현재 main tree에 존재, missing 0.
- PR #74 changed paths: 16/16 현재 main tree에 존재, missing 0.
- PR #72 changed paths: 29/29 현재 main tree에 존재하지만 PR #72 자체는 open 상태.
- 경로 존재와 PR merge state, semantic integration은 별도 상태다. #73/#74의 merge 상태를 근거로 cross-registry 통합 완료라고 보지 않는다.
- 남은 shared conflicts: `data/politicians.json`, `data/research/HISTORY_DEBT.md`, `data/research/rhee-syngman-coverage.json`, `data/research/rhee-syngman-open-leads.json`.

## Pass329 김성수 데이터 중앙 연결

김성수 stable ID `pol-r164-kim-seong-su`는 기존 root의 VERIFIED node를 재사용했다. 사표 제출 1952-05-29와 국회 수리 가결 1952-06-28의 두 event ID를 그대로 재사용하며 신규 event ID를 만들지 않았다. 6개 document object와 2개 claim은 canonical documents/claims에서 확인됐다. 본 run은 해당 source shard를 event index에 연결하고 politician node에 document/event shard references를 additive update한다. 원사표·제86차 국회 원속기록은 여전히 OPEN이며, 이 회차에서 새 역사 원문을 직접 열어 보지는 않았다.

## 정량 실행기록

| 지표 | Run330 실제값 |
|---|---:|
| 신규 독립 역사 연구선 | 0 |
| 일반 국정영역 신규 보강 | 0 |
| 신규/심화 비대통령 정치인 조사 | 0 (기존 김성수 노드의 링크 동기화 1건) |
| 신규 event ID | 0 (기존 event 2건 source shard 재연결) |
| 신규 claim ID | 0 (기존 claim 2건 canonical 존재 확인) |
| 새로 직접 열어 확인한 역사 문서 | 0 |
| 공식·1차 원문 직접 열람 | 0 |
| adversarial searches | 0 |
| 독립 provenance 교차검증 묶음 | 0 |
| 기존 history-debt/open leads 실질 추적 | 0 |
| 새 구체적 integration lead | 33 |
| Floot 변경 | 0 |

기존 Run329 source shard의 6개 문서와 2개 주장은 이전 조사 결과이며 Run330의 직접 열람 수치에 포함하지 않는다. 실제 1시간 실행을 주장하지 않는다.

## 역사부채 주간 전수조사

**역사부채 주간 전수조사 미실시.** 현재 우선순위는 누적 연구자료의 중앙 통합과 root conflict audit이다. `last_full_review`를 변경하지 않았다. 302 OPEN, 319 NARROWED, 15 BLOCKED, 176 CONFLICTED, 2 REOPENED 상태 mention을 전수 재조사한 것으로 간주하지 않는다.

## 수정 대상

- `data/documents/INDEX.md`
- `data/claims/INDEX.md`
- `data/events/INDEX.md`
- `data/politicians/INDEX.md`
- `data/events/run329-kim-seong-su-resignation.json`
- `data/politicians/run330-kim-seong-su-central-links.json`
- `data/research/ACTIVE_RESEARCH_HANDOFF.json`
- `data/research/runs/2026-11-22-run330-integration-report.md`
- `data/research/runs/2026-11-22-run330-integration-ledger.json`
- `data/research/lead-queues/run330-next-integration.json`
- `data/integration/PR_BACKLOG_73_74.json`

## 다음 실행

`data/research/lead-queues/run330-next-integration.json`의 33개 표적을 우선순위대로 처리한다. 먼저 문서 ID conflict 109건 중 FRUS/국편/관보/국회 원문을 직접 대조할 수 있는 항목부터 해결하고, 그 결과를 canonical document/claim/event registry 및 operational roots에 같은 batch로 반영한다. source-triage의 341 conflict-marked files와 554 auxiliary/partial sources, operational-links의 310 unlinked paths를 계속 줄인다.
