# Rhee Pass 86 — KIB liquidation primary-archive crosscheck

Date: 2026-09-23
Scope: 한국식산은행 해산·청산의 1954 실제 절차를 국가기록원 해설집과 제정 법령 연혁으로 재검증. Floot untouched.

## Why this pass
Pass 85 isolated a chronology hazard: later liquidation rules must not be projected backward into 1954. This pass follows the highest-priority lead by locating an official National Archives reconstruction that gives actual meeting dates and the asset-transfer sequence.

## Directly inspected sources
1. 국가기록원, 『중요 공개기록물 해설집 V - 국세청·성업공사 편』, Chapter III, 국가기록원 PDF, especially pp.267–270. The archive states that KIB became a liquidation corporation when KDB was established in April 1954; the government, as largest shareholder, convened an extraordinary shareholders meeting; the liquidation work began with the 1954-04-08 meeting and a 1954-05-31 shareholders meeting approved the balance sheet/property inventory as of 1954-04-01. It further describes sale/transfer of major land, buildings and movables to KDB and accounting transfer of other assets/liabilities.
2. Same official archive identifies source record DA0423463, `대일재산관계 자료철 (한국식산은행 청산사무국)`, and says the underlying liquidation records later passed through 성업공사/서울대 and into 국가기록원.
3. Same archive records government shareholding at roughly 78% and private holdings around 22%, explaining why a shareholder-resolution path mattered rather than treating the old bank as a wholly state-owned shell.
4. Same archive states liquidation ultimately ended in October 1981 and identifies the Kyungchun Railway compensation litigation and Japan-claim compensation as causes of the long tail.
5. 국가법령정보센터 official 1954 promulgation list: 한국산업은행법 제302호 (1953-12-30), 한국산업은행법시행령 제858호, 한국식산은행의청산에관한건 제859호, 한국산업은행설립에관한건 제860호 (all three decrees 1954-01-18), 한국산업은행등기처리규칙 대법원규칙 제20호 (1954-02-24).
6. 국가법령정보센터 original-law page confirms 대통령령 제859호 was enacted/effective 1954-01-18. The original article text remains a next-step target because the accessible page exposed metadata more reliably than all article bodies.
7. 국가기록원 산업은행 thematic page independently places drafting in 1951, National Assembly passage in Nov. 1953, promulgation in Dec. 1953, and KDB launch in Apr. 1954 after organization and government capital payment.
8. 한국민족문화대백과사전 KDB entry independently repeats the 1951 drafting / 1953 passage / 1954 launch sequence.

## Findings and corrections
### F1 — actual 1954 corporate action is now date-anchored
Official archival reconstruction gives **1954-04-08** for the extraordinary shareholders meeting that resolved dissolution and organization of the liquidation committee. This is stronger than the prior abstract statutory inference and should be the anchor event date.

### F2 — second governance checkpoint
A further shareholders meeting on **1954-05-31** approved the balance sheet and property inventory **as of 1954-04-01**. This creates three distinct dates that must not be collapsed: accounting reference date (04-01), dissolution/liquidation resolution (04-08), approval of opening liquidation accounts (05-31).

### F3 — succession was not a single blanket transfer
The archive distinguishes (a) sale/transfer of major land/buildings/movables to KDB from (b) accounting transfer of other assets and liabilities. Event modeling should therefore split physical/property disposition from ledger succession.

### F4 — shareholder structure explains procedure
The government held about 78% rather than 100%. Private/legal-person/individual holdings remained. The shareholder meeting and later compensation disputes were therefore substantive governance steps, not ceremonial paperwork.

### F5 — liquidation continued far beyond the Rhee presidency
The liquidation ended only in Oct. 1981. Later roles and rules belong to later phases. Any actor holding a liquidation office in the 1960s/1970s must not automatically be assigned the 1954 founding-liquidation role.

## Adversarial checks
1. Tested `KDB governor automatically became 1954 KIB liquidator`: **not established**; later statutory language remains unsafe for backward attribution.
2. Tested `KIB simply vanished when KDB opened`: **contradicted** by official archive; it became a liquidation corporation and persisted until 1981.
3. Tested `government owned all KIB shares`: **contradicted**; official archive shows substantial private holdings.
4. Tested `1954-04-01 was the liquidation resolution date`: **contradicted/narrowed**; it is the accounting reference date, while the archive places the extraordinary meeting on 04-08.
5. Tested `one transfer moved all KIB property to KDB`: **contradicted/narrowed**; archive distinguishes sale/transfer of major tangible assets and accounting transfer of other assets/liabilities.
6. Tested `the 04-08 meeting alone completed opening liquidation accounting`: **contradicted** by 05-31 approval checkpoint.
7. Tested `later Kyungchun Railway litigation can identify the 1954 representative liquidator`: **unsafe**; the archive itself describes a later KDB-governor representative plaintiff with redacted name.
8. Tested `liquidation was an exclusively finance-ministry desk process`: **too simple**; corporate shareholder/committee machinery and later multiple supervising agencies appear in the archive.
9. Tested `the legal chain can be reconstructed from one decree`: **contradicted**; Law 302, Decrees 858/859/860, Supreme Court Rule 20, corporate resolutions and later amendments all matter.
10. Tested `secondary biographies are sufficient to assign Yu Wan-chang's exact 1954 chair start date`: **not established**; keep role evidence provisional until committee minutes/appointment records are opened.

## Event/sub-event structure to carry forward
- EVT-KIB-1954-ACCOUNTING-CUTOFF — 1954-04-01 opening balance/property reference date.
- EVT-KIB-1954-EGM-DISSOLUTION — 1954-04-08 extraordinary shareholders meeting; dissolution + liquidation committee organization.
- EVT-KIB-1954-LIQUIDATOR-SELECTION — selection/appointment mechanics; identities still open pending minutes.
- EVT-KIB-1954-ASSET-SALE-KDB — major land/building/movable property sale/transfer to KDB.
- EVT-KIB-1954-LEDGER-TRANSFER-KDB — other assets/liabilities transferred by accounting entries.
- EVT-KIB-1954-0531-APPROVAL — 1954-05-31 shareholders meeting approval of 04-01 balance sheet/property inventory.
- EVT-KIB-LIQUIDATION-LONGTAIL — 1954–1981 unresolved claims/litigation and final closure.
- EVT-KIB-KYUNGCHUN-LITIGATION — 1963 filing through 1979 final judgment, explicitly later-phase governance.

## Actor nodes affected
- 구용서: KDB founding governor remains relevant to successor-bank side; do **not** infer 1954 KIB liquidator solely from later law.
- 유완창: secondary biographical sources identify him as KIB liquidation-committee chair, but exact appointment/start/end and 1954 meeting participation remain OPEN pending primary minutes.
- 임송본: no merge with redacted 1954 `Hong`; surname conflict remains decisive.
- `Choi` representative liquidator: identity remains OPEN; 04-08 and 05-31 corporate records are now the best direct targets.
- Government shareholder representative: identity OPEN; likely recoverable from 04-08 minutes/proxy/attendance records.

## Cross-check bundles
1. **Institutional creation**: 국가법령정보센터 promulgation chronology + 국가기록원 산업은행 page + AKS KDB history.
2. **Liquidation mechanics**: 국가기록원 official explanatory volume + its cited DA0423463 archival fonds + Decree 859 metadata.
3. **Chronology guardrail**: 04-01 accounting cutoff + 04-08 EGM + 05-31 approval, preventing silent date collapse.

## Concrete lead queue
1. 국가기록원 DA0423463에서 1954-04-08 임시주주총회 의사록 원문을 찾아 참석자·정부 주주대표·의장·청산인 선임안을 추출.
2. DA0423463 또는 연계철에서 1954-05-31 주주총회 의사록을 찾아 대차대조표 승인자와 감사/청산인 서명을 확인.
3. 국가법령정보센터/관보에서 대통령령 제859호 1954 제정 당시 제3조·제4조 원문을 확보.
4. 대통령령 제859호의 1959 개정문과 개정이유를 확보하여 청산인 규칙 변화를 diff.
5. 1960-11-29 전부개정문을 확보해 `KDB governor = liquidator` 조항의 최초 등장 시점을 확정.
6. 대통령령 제860호 원문에서 9인 설립위원회 임명·위원장 위촉 절차를 재확인.
7. 제860호 시행에 따른 재무부장관의 설립위원장 위촉 문서를 국가기록원에서 탐색.
8. KDB 10년사(1964)에서 9인 설립위원 실명을 전수 추출.
9. KDB 10년사에서 1954-04-01 발족 당시 임원/이사 명단을 추출.
10. 한국식산은행 1954-04-08 회의의 정부 보유 938,725주 의결권 행사자를 확인.
11. 민간 법인 22개 주주의 1954 회의 참석/위임 현황을 확인.
12. 개인주주 대표 또는 반대/기권 여부를 회의록에서 확인.
13. 1954-04-01 재산목록 원본의 토지·건물·동산 목록을 추출.
14. KDB로 매각된 유형자산의 평가가격·평가기관·승인자를 확인.
15. 계정상 양도된 기타 자산·부채의 총액과 책임자를 확인.
16. KIB 청산위원회 최초 위원 명단과 대표청산인 `Choi` 실명을 확인.
17. 유완창의 청산위원장 취임일·퇴임일을 관보/인사기록/위원회 의사록으로 확인.
18. 유완창이 1954-04-08 회의에 직접 참석했는지 확인.
19. 구용서가 04-08 또는 05-31 회의에 KDB 총재 자격으로 참석/보고했는지 확인.
20. 1954 당시 한국식산은행 은행장/대표이사의 정확한 인물과 임기 종료일을 확인.
21. redacted `Hong`의 직함이 은행장·청산인·임원 중 무엇인지 원문으로 분리.
22. redacted `Choi`가 1954 대표청산인인지 후대 대표청산인인지 시기를 확정.
23. 국가기록원 `동산 부동산관계 No 1(한국식산은행 청산위원회)` 관리번호를 확인하고 1954 자산매각 결재선을 추출.
24. `조선·식산은행 청산대책(1)` 원문에서 감독기관과 청산위원회 역할분담을 추출.
25. `제24차 연합청산위원회 의사록(2-1)`에서 KIB 관련 안건과 후대 감독 변화를 추출.
26. 재정경제부 『국가귀속 청산법인 청산자료집』(2000) 504–506쪽을 직접 확보해 1954 절차와 분배액을 대조.
27. 1961–1965 중간분배 결의 문서에서 정부/민간 분배 승인자를 확인.
28. 경춘철도 보상소송 1963 소장 원문에서 대표청산인 박씨 실명·직함·선임근거를 확인.
29. 1979 대법원 확정판결 사건번호와 당사자 표기를 확보.
30. 1981-10 청산종결 주주총회/정부 승인 문서를 확보해 최종 청산인을 확인.
31. 성업공사→서울대→국가기록원 이관목록에서 KIB 청산 관련 전체 기록철 목록을 생성.
32. 관재청이 1955년까지 담당한 감독문서에서 1954 최초 감독 담당 과/관료를 확인.
33. 재무부 관재국 1955–1963 인계문서에서 청산위원회 인적 연속성을 확인.
34. 국세청 징수국 1965–1977 이관문서에서 청산위원장/사무국장 명단을 확인.
35. 연합청산위원회 조직 근거와 KIB 안건 의결권자를 확인.
36. KIB 민간주주 보상대책위원회 결성문서에서 주요 주주·대표 인물을 정치인/경제관료 후보와 분리.
37. 1954 KDB 정부출자금 납입 결재문서에서 재무부장관·국고 담당자 역할을 확인.
38. 한국산업은행등기처리규칙 제20호 원문에서 설립등기 신청 주체와 첨부문서를 추출.
39. KDB 설립등기 원본/등기부에서 최초 총재·이사와 설립일을 확인.
40. 국회 1953 한국산업은행법 심의 회의록에서 정부 제안자·재경위 보고자·반대/수정 의원을 정치인 노드로 확장.

## Status
- Directly inspected meaningful source pages/documents this pass: 8 source objects/views, of which 6 are official/institutional primary-or-archival lineage.
- Independent research lines materially advanced: 12.
- Governance domains: finance, corporate/public-asset governance, executive administration, judicial/registration, legislative/legal history.
- Named non-president actors newly verified in this pass: 0; existing nodes narrowed without guessing identities.
- Event/sub-events materially structured: 8.
- Adversarial searches/checks: 10.
- Cross-check bundles: 3.
- Existing open leads narrowed: 7.
- New concrete leads: 40.

Minimum targets not reached: this bounded run did not reach 40 opened documents, 20 independent lines, six domains, or ten named non-president actors. Counts are deliberately not padded. The highest-value result is the official archive's 04-01 / 04-08 / 05-31 chronology, which materially corrects the risk of collapsing accounting, dissolution and approval dates.

**역사부채 주간 전수조사 미실시.** Wednesday; last full review remains 2026-09-20.
