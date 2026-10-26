# Rhee Pass 100 — Peace Line precursor source-access audit

Date: 2026-09-23
Focus: Pass 99의 최우선 lead인 1951-09-04/06 외정 제958호, 총의 제174호, 5~8월 선행문서의 개별 원문 접근 재검증.

## Material result
동북아역사재단 한일회담외교문서의 상위 문서철 색인을 다시 직접 확인했다. 색인은 다음 개별 기록의 날짜·문서번호·순서를 공식적으로 노출한다.

- 1951-05-10 `아국연해어업보호정책에 관한 품의 건`, 한일대 제1949호
- 1951-05-16 `아국연해어업보호정책에 관한 건`, 외정 제402호
- 1951-06-18 `아국연안어업보호정책에 관한 건`, 상수 제368호
- 1951-08-25 `대일어업문제에 관한 회의록`
- 1951-08-25 `대일어업협정에 관한 합석회의의 개략과 결의록`
- 1951-09-04 `어업보호구역 선포에 관한 건`, 외정 제958호
- 1951-09-06 `어업보호구역선포에 관한 건` 2건
- 1951-09-08 `국무회의제출안건 처리 상황통지의 건`, 총의 제174호
- 1951-09-08 `어업보호수역 선포에 관한 건`, 외정 제958호

상위 색인에서 개별 record IDs도 회수했다. 특히 9/4는 `kj.d_0007_0010_0550`, 9/6 두 건은 `_0560`, `_0570`, 총의 제174호는 `_0580`이다.

## Access failure is now a documented blocker
이번 회차에 `_0550`, `_0560`, `_0570`, `_0580`을 각각 직접 열었으나 모두 HTTP 502 Bad Gateway로 실패했다. 같은 방식으로 5/10 `_0420`, 5/16 `_0430`, 6/18 `_0450`, 8/25 회의록 `_0500`, 8/25 결의록 `_0522`도 502가 재현되었다. 반면 1951-05-04 보고서 `_0421`은 검색 인덱스에서 날짜·문서종류(보고서)·형태(필사, 국한문)와 문두 `別紙報吿書 / 檀紀四二八四二年五月四日 / 題目「我國領海線外의 漁業保護管轄權問題」`까지 노출된다.

따라서 이 회차에서는 9/4·9/6 원문이나 총의 제174호의 본문을 보았다고 기록하지 않는다. 색인 검증과 원문 검증을 엄격히 분리한다.

## Claim-state consequences
1. `제98회 국무회의 도중 어업관할수역→어업보호수역으로 명칭이 변경되었다`는 명제는 계속 OPEN이다. Pass 99의 9/8 외정 제958호가 `어업보호수역` 안건의 원안통과를 증명하지만, 9/4·9/6 초안 또는 회의록 없이 회의 중 변경을 확정할 수 없다.
2. `총의 제174호가 제98회 처리결과를 어떤 문구로 통지했는가` 역시 INDEX_VERIFIED / TEXT_BLOCKED 상태다.
3. 지철근·김동조·김훈의 개인별 drafted_by/proposed_by attribution은 승격하지 않는다. 현재 확보된 것은 문서계보와 기관 수준의 연결이다.
4. 1951-05-04 보고서는 최소한 동시대 필사 보고서라는 점이 직접 노출되지만 작성자 실명은 아직 확보되지 않았다.

## New retrieval strategy
동일 URL 반복은 중단한다. 다음 회차는 (a) 문서 제목+번호+날짜로 한국사DB/국가기록원/외교사료관/학술 인용문에서 대체 전사본을 찾고, (b) NAHF XML/이미지 또는 다른 소장처의 동일 record를 역추적하며, (c) 제98회 국무회의 자체의 별도 회의록 계열을 찾아 독립 provenance로 교차검증한다.

## Concrete next leads
1. 국가기록원에서 `외정 제958호` + 1951-09-04 검색, 철/건 식별번호 회수.
2. 국가기록원에서 `총의 제174호` + 1951-09-08 검색, 국무총리비서실/총무처 계열 여부 확인.
3. 국사편찬위원회 한국사DB에서 `어업보호구역선포` 구표기 포함 전문검색.
4. 외교사료관 공개목록에서 한일회담 외교문서 `평화선 및 재한 일본 재산권` 원철 청구기호 확인.
5. NAHF `_0550` XML/이미지 대체 엔드포인트 또는 E-book 내 페이지 번호 역추적.
6. `_0560`과 `_0570`의 문서종류·형태·발수신자 메타데이터를 검색 인덱스로 분리 회수.
7. `_0580`의 발신기관·수신기관을 제목/문서번호 인용 논문에서 역추적.
8. 제98회 국무회의 1951-09-07 회의록을 국무회의기록/관보/국가기록원 별도 계열에서 검색.
9. 9/4 초안과 9/8 상신문 좌표·명칭 차이를 확인할 수 있는 후대 논문 각주 원문 추적.
10. 지철근 『평화선』 111~129쪽의 9월 회의 서술과 인용 문서번호 추출.
11. 김동조 『회상 30년 한일회담』의 평화선·독도 대목 원문 페이지 회수.
12. 1951-05-04 `_0421` 원이미지/전체 전사 대체 노출 경로 탐색.
13. 한일대 제1949호의 발신자·수신자 인용을 학술 DB에서 검색.
14. 외정 제402호의 결재선/첨부 보고서 관계를 국가기록원에서 확인.
15. 상수 제368호가 상공부 수산국 계열인지 문서기관 메타데이터로 확정.
16. 8/25 합석회의 참석자 명단을 논문/회고록에서 후보화한 뒤 원문과 대조.
17. 1951-09-07 외정 제963호의 발수신자·첨부자료 확인.
18. 1951-09~1952-01 경무대 문서에서 9/8 상신안의 결재/보류/수정 지시 탐색.
19. 1952-01-15 제4회 국무회의 원회의록과 1951-09-07 제98회 회의의 안건 연속성 비교.
20. 1952-01-18 국무원고시 제14호 좌표를 9/8 외정 제958호 좌표와 대조.
21. FRUS/미 국무부 문서에서 1951-09 한국 어업보호구역안 인지 시점을 탐색.
22. 일본 외무성 공개자료에서 1951-09 한국안 사전인지 여부 탐색.
23. 변영태의 1951-09 정확 재직·서명 여부를 정부 인사기록과 대조.
24. 김훈의 1951-06/09 상공부장관 재직기간을 공식 관보/인사기록으로 확정.
25. 지철근의 1951 수산행정 직위·소속을 직원록/관보에서 확정.
26. 김동조의 1951 외무부 정무국 직위·재직기간을 직원록에서 확정.
27. 5~9월 문서계보에서 각 문서의 첨부물 제목을 수집해 동일 초안 재사용 여부 확인.
28. `어업보호관할권`, `어업보호구역`, `어업보호수역`, `인접해양 주권` 용어변화를 날짜별 claim graph로 분리.
29. 문서 접근이 회복되면 `_0550`~`_0580`을 먼저 원문 회수하고 checksum/원문 위치를 document registry에 반영.
30. 원문이 계속 차단되면 BLOCKED 사유를 HISTORY_DEBT에 승격하고 대체 소장처 식별자를 붙인다.

## Execution ledger
- Independent research/retrieval lines advanced: 12.
- Meaningful official source records directly attempted/opened: 10 unique records (1 partial-text success, 9 individual-record 502 failures; parent index separately inspected and not counted as an original document).
- Official/primary documents with usable original text newly obtained: 1 partial opening (`1951-05-04` report). No inaccessible record is counted as text-opened.
- Existing open leads traced: 9.
- Adversarial/guardrail checks: 4.
- New concrete leads: 30.
- Non-president nodes newly promoted: 0; attribution evidence was insufficient.
- Event/sub-event newly promoted: 0; this was a source-access and uncertainty-narrowing pass.

Minimum targets for 20 research lines, 10 politician nodes, 40 opened documents, 20 primary texts, 10 adversarial searches and 8 event changes were not reached. The main limiting factor was reproducible 502 failure on the exact high-priority NAHF individual records. The run did not inflate counts by treating failed opens or the parent index as recovered originals.

**역사부채 주간 전수조사 미실시.**