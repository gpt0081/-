# 대한민국 정치인 실록 · Organization Registry

2026-10-29 Pass257P에서 기존 정치인/대통령/사건 JSON을 변경 없이 확장하는 **선택적 기관 ID** 계층을 추가했다.

- 원장: `data/organizations/registry.json` (17개 기관, 1950~57 UNKRA/UNCURK/국회·정부·한국은행·사회부 등)
- 사용법: 각 event/sub-event의 `organization_ids` 배열에 stable ID를 부가하고 기존 `proposed_by`, `decided_by`, `executed_by`, `observed_by` 역할을 보존한다.
- 기관 ID는 **정치인 ID와 별개**다. 원조단장 존 콜터는 국제기구 직위자로 기록하되 대한민국 정치인 registry로 승격하지 않는다.
- `org-rok-housing-administration` 영문표기와 서울기록원 `대한주택영단`은 동일기관 여부 원문 검증 전 병합 금지.
- 정당·정부부처·국제기구 모두 역사적 기간에 따라 명칭이 달라질 수 있으므로 `aliases`, `period`, `document_ids`, `research_status`, `open_lead`를 사용한다.
- 기관의 선악·이념·정치적 점수/순위화는 금지한다. 기관행위는 사건별 결정·집행·감독과 별도로 연결한다.

관련 원문: `DOC-P257P-UN-RES410-19501201`, `DOC-P257P-UN-A2750-19541012`, `DOC-P257P-UN-A2487-AUDIT-19530921`.

- 2026-10-29 추가: 영국 하원·외무부 및 UN ACABQ 3개 기관, 국제기구 자기보고·독립감사·영국 의회답변 3개 출처계열을 구분.

- 2026-10-30 Pass258A: `data/organizations/pass-258a-us-foa-1954.json` (1954 FOA 원조 원문 및 1954 한미·총선 반증, 기존 FRUS canonical ID 재사용; Floot 변경 없음).

- `data/organizations/pass-258b-oec-rok-aid-authority.json` (미 경제조정관실·대한민국 정부 기관 노드)
