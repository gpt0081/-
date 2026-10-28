# 기존 실록의 군정·사법 명령선 event ID 보수 (pass236C)

2026-10-28 데이터 무결성 점검에서 정치인 registry가 참조하지만 data/events.json에 없던 사건 ID 세 개를 발견했다. 새 사료 발견이 아니라 기존 `data/evidence/rhee-syngman.json` 연표·출처를 event graph로 연결한 보수다.

- `evt-1950-han-river-bridge`: 1950-06-28 국군 공병대 한강인도교 폭파, 후대 최창식 무죄. 채병덕·이승만의 구체적 명령 발신·승인 시각은 미확인. 기존 evidence IDs S1950-HAN·S1964-CHOI-FINAL.
- `evt-1951-national-defense-corps`: 1951-01-04 이승만의 국민방위군 부정 조사·처벌 지시 원문과 후속 군법회의를 분리. 신성모 연관은 기존 registry에서 계승했으며 대통령의 사전인지·신성모 직접집행은 별도 검증 필요. S1951-NDC-DIRECTIVE.
- `evt-1951-geochang`: 1951-04-30 이승만의 사후 징계 지시·후속 군법회의. 최덕신 및 대통령의 사건 전 명령선은 여전히 OPEN. S1951-GEOCHANG-DIRECTIVE.

이 세 사건은 새로운 1차자료 열람으로 집계하지 않는다. 역사부채 주간 전수조사 미실시.
