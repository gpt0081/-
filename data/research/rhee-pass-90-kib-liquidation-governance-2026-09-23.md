# Rhee Pass 90 — KIB liquidation governance and amendment trail

Date: 2026-09-23
Scope: Pass 89의 최우선 unresolved였던 대통령령 제859호의 법적 권한모델을, 현행 연혁표시와 국가기록원 청산 기록군으로 재구성. Floot untouched.

## Directly inspected sources
1. 국가법령정보센터 1954 공포목록: 대통령령 제859호 `한국식산은행의청산에관한건` 제정일/시행일 1954-01-18 확인.
2. 국가법령정보센터 제859호 1963-05-17 시행본(각령 제1302호): 제1~6조 및 부칙 연혁 확인.
3. 국가법령정보센터 1959-04-01 시행본 검색결과: 대통령령 제1473호 일부개정 존재 확인.
4. 국가기록원 `국무회의 안건 목록집 I`, 1959: `한국식산은행의 청산에 관한 건 중 개정의 건(안)`, 제26회, 1959-02-24, 법제실, 2쪽, BA0084223.
5. 국가기록원 `국무회의 안건 목록집 I`, 1960: 같은 제목의 개정안, 제66회, 1960-11-24, 재무부, 9쪽, BA0084254.
6. 국가기록원 중요 공개기록물 해설집 V, `청산분배관계문서철`, DA0423876: 생산기관 한국식산은행청산위원회, 1958~1967 청산분배 기록군.
7. 국가기록원 중요 공개기록물 해설집 V, `청산관리 업무현황`, 1972-04-30: 식산은행 포함 청산법인의 임직원 명단·청산인/청산위원회 구성인원·재산·소송 현황 존재 확인.
8. 국가기록원 중요 공개기록물 해설집 V, `대일재산관계자료철`, DA0423463 및 `대일청구권자료표`, DA0424710: 한국식산은행청산사무국 생산, 1966/1971 재산조사 계보.
9. 국가기록원 중요 공개기록물 해설집 V, 대일민간청구권 신고 관련 기록: 1971~1972 식산은행 청산위원회의 재무부 신고와 정부지분 78.2% 제외 방식 확인.
10. 한국은행 공식 역대총재 구용서 페이지: 1954~1958 한국산업은행 제1~2대 총재 경력 확인.
11. 한국은행 디지털아카이브 `금통위 관계` IT14968: 산업은행 업무계획 자문, 산업금융채권 매입 등 1958 정책금융 기록군 확인.
12. 국가기록원 1959 국무회의 목록: `한국산업은행의 단기4292년도 업무계획에 관한 건`, 재무부, 제19회 1959-02-10, 28쪽, BA0084223.
13. 국가기록원 1959 국무회의 목록: `한국산업은행의 단기4291년도 결산보고에 관한 건`, 재무부, 1959-04-24, 54쪽, BA0084225.
14. 국가기록원 산업은행 기록 해설: 1951 법안 기초→1953 법률 제302호→1954-04 발족의 공식 기관 연혁 재확인.
15. 산업정책사(KIET) 공식 간행물: 1954 산은이 식산은행 대출자금 약 5억원을 승계했다는 KDB 사사 인용 확인.

## Material findings

### F1 — 1963 본문은 1954 원문이 아니라 1960 전문개정 이후의 권한모델이다
현재 직접 읽히는 제3조는 `[전문개정 1960·11·29]`라고 명시한다. 따라서 `한국산업은행총재는 한국식산은행의 청산인이 된다` 및 `KDB 총재가 청산위원장`이라는 문구를 1954 제정 당시부터 존재했다고 소급할 수 없다. Pass 89의 continuity 가정은 더 강하게 제한되어야 한다.

### F2 — 현행 연혁본문 내부에는 서로 다른 청산인 선임 메커니즘이 공존한다
1960 전문개정 제3조는 KDB 총재를 법정 청산인으로 두지만 제4조는 식산은행 두취가 해산 후 10일 이내 임시주주총회를 소집하여 `청산인을 추천 또는 선임`하도록 규정한다. 이 조합은 단순히 `청산인=총재 한 명`으로 모델링할 수 없음을 뜻한다. 제4조의 1954/1959/1960 변동 여부와 실제 주주총회 결의를 확인해야 한다.

### F3 — 청산위원회는 후대의 비공식 명칭이 아니라 장기간 존속한 기록 생산기관이다
DA0423876은 생산기관을 `한국식산은행청산위원회`로 명시하고 1958~1967 청산분배 문서를 수록한다. 1958-10-25에는 청산위 위원장 `오○○`이 재무부장관에게 중간분배용 주식현황을 보고했다. 따라서 청산위원회는 최소 1958년에는 실재 행정행위자였다.

### F4 — 1959 개정은 별도 원문 표적이 확정됐다
1959-02-24 제26회 국무회의에 법제실 발의 2쪽 개정안이 BA0084223에 존재하고, 1959-04-01 대통령령 제1473호로 공포됐다. 이 2쪽은 1954 원문과 1960 전문개정 사이의 첫 diff를 복원하는 가장 짧고 가치 높은 원문이다.

### F5 — 1960 전문개정의 바로 앞 정부안도 정확히 식별됐다
1960-11-24 제66회 국무회의에서 재무부 발의 9쪽 개정안이 BA0084254에 존재한다. 5일 뒤 국무원령 제109호 전문개정과 연결된다. 제3조의 `KDB 총재=청산인`, 8인 청산위원회 구조가 왜 도입됐는지 제안이유·구조변경 설명을 확인할 수 있다.

### F6 — 청산은 1954 자산승계로 끝난 사건이 아니라 수십 년짜리 잔여재산·민간주주 권리 문제였다
1972 자료에서 식산은행은 발행주식 1,200,000주 중 정부보유 938,725주, 약 78%로 정리되며, 자산·부채·소송이 남아 있었다. 1971~72 대일청구권 신고에서도 정부지분 78.2%를 제외한 민간지분만 신고했다. `KIB→KDB 단순 흡수` 모델은 부정확하다.

### F7 — 식산은행 청산위원회는 독립적인 재산·외교청구 행위도 수행했다
청산위원회는 일본 소재 유가증권·화폐·지점 청산잉여금 등을 재무부에 신고했고, 1966/1971 재산조사 자료를 갱신했다. 따라서 event graph에서 `KDB founding`, `KIB liquidation`, `KIB Japanese-asset claims`를 별도 장기 event family로 분리해야 한다.

### F8 — 1958 청산분배 개시와 1959 산은 업무계획은 이승만기 평시 경제행정 연구선으로 연결된다
1958-10-25 청산중간분배 준비, 1959-02-10 KDB 연간 업무계획의 국무회의 심의, 1959-04-24 전년도 결산보고는 논쟁적 사건이 아닌 공공금융·재정·산업행정의 반복적 국정과정이다. 대통령 중심 attribution 없이 재무부·산은·금통위·청산위의 기관별 권한을 추적해야 한다.

## Adversarial checks
1. `1963 제3조는 1954 원문을 그대로 보여준다` → contradicted: 제3조 전문개정 1960-11-29.
2. `1954부터 KDB 총재가 청산인이었다고 현재 연혁본문만으로 확정 가능` → unsupported.
3. `청산위원회는 1960 전문개정 때 처음 생겼다` → challenged: DA0423876이 1958 청산위 행위를 기록.
4. `청산인은 오직 KDB 총재 한 명이었다` → challenged: 제4조의 주주총회 청산인 추천/선임 절차가 병존.
5. `KIB는 1954-04-01 KDB에 완전히 흡수되어 법적 잔여가 없었다` → contradicted by 장기 청산·민간주주·소송·재산 기록.
6. `청산위는 내부 회계조직일 뿐 대외 행위가 없었다` → contradicted by 재무부 보고와 대일청구권 신고.
7. `정부가 KIB 지분 100%를 보유했다` → contradicted: 약 78.2%, 민간지분 존속.
8. `1959 개정의 원문 위치가 불명확하다` → contradicted: BA0084223, 제26회, 1959-02-24, 2쪽.
9. `1960 전문개정의 정부안 위치가 불명확하다` → contradicted: BA0084254, 제66회, 1960-11-24, 9쪽.
10. `산은·식산은행 연구는 설립일 단일 사건만 보면 된다` → contradicted: 1958~59 업무계획·결산·청산분배와 1960+ 청산 거버넌스가 연속됨.

## Event/sub-event graph implications
- `EVT-KIB-1954-DISSOLUTION-TRIGGER`: KDB 설립일에 KIB 해산.
- `EVT-KIB-1954-SHAREHOLDER-LIQUIDATOR-SELECTION`: 해산 후 10일 내 임시주총과 청산인 추천/선임 절차. 실제 인물·결의 OPEN.
- `EVT-KIB-1958-INTERIM-DISTRIBUTION-PREPARATION`: 1958-10-25 청산위 위원장 오○○의 재무부 보고.
- `EVT-KIB-1959-LIQUIDATION-DECREE-AMENDMENT`: 1959-02-24 국무회의안→1959-04-01 제1473호.
- `EVT-KDB-1959-ANNUAL-BUSINESS-PLAN`: 재무부 제안, 제19회 국무회의, 1959-02-10.
- `EVT-KDB-1959-1958-SETTLEMENT-REPORT`: 재무부, 1959-04-24, BA0084225.
- `EVT-KIB-1960-LIQUIDATION-GOVERNANCE-REWRITE`: 1960-11-24 재무부안→11-29 전문개정.
- `EVT-KIB-1971-JAPAN-CLAIMS-SURVEY`: 청산위/청산사무국의 대일재산 조사·신고.
- `EVT-KIB-1972-LIQUIDATION-STATUS`: 재산·소송·임직원·정부지분 상태 스냅샷.

## Actor/node implications
- `pol-gu-yong-seo`: 1954~1958 KDB 총재는 VERIFIED. 그러나 1954 KIB 청산인 지위는 다시 OPEN.
- `cand-kib-liquidation-chair-o-1958`: 오○○, 1958-10-25 KIB 청산위원장. 성명 원문 복원 필요.
- `slot-kib-president-pre-dissolution-1954`: KIB 두취. 제4조상 임시주총 소집 책임자. 실명 원문 필요.
- `slot-kib-shareholder-liquidators-1954`: 임시주총이 추천/선임한 청산인 집합. 실명·수·대표권 OPEN.
- `slot-kib-liquidation-committee-1958`: 위원장/위원/대표청산인/청산인/감사 역할을 분리 저장.
- `org-ministry-finance`: 청산비용 승인, 국무회의안 발의, 청산분배 보고 수신, 대일청구권 신고 수신 등 장기 감독기관.

## Open/history-debt updates
- `KIB liquidation leadership chronology`: CONFLICTED_AUTHORITY_MODEL → NARROWED_MULTI_STAGE. 1958 청산위 실재, 1959 개정, 1960 전문개정, 제4조 주주총회 선임 메커니즘이 확인됨. 1954 원문과 최초 임시주총은 OPEN.
- `KDB governor statutory liquidator from 1954`: NARROWED_NOT_YET_PROVEN → REOPENED_STRONG_CAUTION. 현재 확인 문구가 1960 전문개정 조문이므로 1954 소급 근거가 약화됨.
- `KIB liquidation committee origin`: OPEN → NARROWED. 최소 1958 실재가 공식 기록군으로 확인. 설치일/근거는 OPEN.
- `1959 decree amendment`: OPEN → NARROWED. 국무회의 원문철·쪽수·심의일·공포번호까지 특정.
- `1960 governance rewrite`: OPEN → NARROWED. 국무회의 원문철·쪽수·심의일 및 전문개정일 특정.

## Next lead queue
1. 국가기록원 BA0084223의 1959-02-24 2쪽 개정안 원문에서 변경 조문과 제안이유 추출.
2. BA0084254의 1960-11-24 9쪽 개정안 원문에서 전문개정 이유·신구조문 추출.
3. 관보 1954-01-18 대통령령 제859호 원공포 6개 조문 전체 확보.
4. 관보/법령 연혁에서 1959 제1473호 신구조문 diff 확보.
5. 1960 국무원령 제109호 신구조문 diff 확보.
6. 1954-04-01~04-10 KIB 임시주주총회 소집공고 확보.
7. 같은 임시주총 회의록에서 추천/선임 청산인 실명·표결 확보.
8. 1954 KIB 두취 실명과 임기, 주총 소집 서명 교차검증.
9. 1954 최초 청산인 등기부 또는 등기공고 확보.
10. 1954 대표청산인 최○○의 성명·선임근거·대표권 범위 확인.
11. DA0423876에서 1958 청산위원장 오○○ 성명 원문 복원.
12. DA0423876 제9차 가결산과 1958-10-25 보고 원문 확보.
13. 1958 당시 청산위원/청산인/감사 명단 확보.
14. 1959 제1473호 개정 당시 청산위원회 인사구성 변동 확인.
15. 1960 전문개정 직전 청산위원회 구조와 직후 구조 비교.
16. 1960 제3조 위원 7인의 당시 실명(재무부 이재·사세·관재국장, 법무국장, 법제처 제2국장, 제일은행장, 장관 위촉자) 복원.
17. 1960 KDB 총재 실명과 청산위원장 취임 연결 확인.
18. 1962 각령 제655호가 제3조에서 바꾼 정확한 직위/인원 diff 확인.
19. 1963 각령 제1302호의 감사·상법 참작 변경 이유 확인.
20. 1966 대통령령 제2534호 후속 변경 조문·청산 지속 이유 확인.
21. 1972 `청산관리 업무현황` 원문 표에서 식산은행 대표청산인·위원장·청산인·감사 실명 추출.
22. 1972 식산은행 계류소송 사건번호·당사자·쟁점 확보.
23. DA0423463 1966 대일재산관계자료철의 작성·결재자 실명 추출.
24. DA0424710 1971 대일청구권자료표의 작성·결재·신고자 실명 추출.
25. 1971-12-16 대일민간청구권 신고서의 법인대표 서명자 확인.
26. 1972-03-14 일본지점 청산잉여금 신고서 서명자 확인.
27. 정부보유 938,725주와 1958 보고의 934,275주 차이를 주식변동대장으로 설명.
28. 1958 제1차 중간분배금 규모와 정부 귀속액·민간 배분액 확인.
29. 1962 제4차 중간분배가 경제개발자금에 실제 귀속됐는지 재무부 예산/세입 문서 교차검증.
30. 이병철 관련 식산은행 민사소송의 사건번호·재산·판결 결과 확인.
31. BA0084223의 1959 KDB 업무계획 28쪽 원문에서 산업별 융자계획·재원·정책 우선순위 추출.
32. BA0084225의 1958 KDB 결산보고 54쪽에서 실제 집행과 업무계획 차이 분석.
33. 한국은행 IT14968에서 KDB 업무계획에 대한 금통위 자문 답신 원문 분할 확보.
34. IT14968에서 제4회 산업금융채권 매입 결의의 금액·조건·표결일 확인.
35. KDB 10년사/30년사에서 1954~59 총재·이사·재무부 감독선과 업무계획 절차 교차검증.
36. 1959 국무회의 제19회 회의록에서 KDB 업무계획 토론자·수정·대통령 발언 유무 확인.
37. 1959 국무회의 제26회 회의록에서 식산은행 청산령 개정 토론·대통령 재가선 확인.
38. 1954 설립위원회 종합경과보고서와 KIB 청산 최초 주총 기록의 상호 인계문서 확인.
39. KIB→KDB 승계자산 약 5억원의 자산종류·평가기준·법적 승계일 확인.
40. KIB 잔여재산과 KDB 승계재산의 경계표/목록을 확보해 `승계`와 `청산` 자산을 분리.

## Execution ledger
- Meaningful documents/pages directly opened/inspected: 15.
- Official/primary or official institutional: 14.
- Independent research lines materially advanced: 13.
- Governance domains strengthened: 6 (public finance, industrial finance, administrative law, corporate liquidation, cabinet procedure, foreign-claims/property administration).
- Non-president named/slot nodes newly added or deepened: 6.
- Event/sub-events structured or materially strengthened: 9.
- Adversarial checks: 10.
- Cross-check bundles: 3 (statute history + cabinet index; statute + archival liquidation records; liquidation records + foreign-claims records).
- Existing open/history-debt lines narrowed/reopened: 5.
- Concrete next leads: 40.

Minimum shortfalls: this bounded run did not reach 40 directly opened documents, 20 independent research lines, or 10 named non-president politicians. Counts are not padded. The largest gain is methodological: the apparent 1954 `KDB governor = KIB liquidator` continuity is now explicitly unsafe because the visible 제3조 is a 1960 full amendment, while official archival records prove a liquidation committee existed by 1958.

역사부채 주간 전수조사 미실시. Wednesday; last full review remains 2026-09-20.
