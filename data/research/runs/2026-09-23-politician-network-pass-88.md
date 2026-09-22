# Politician Network Pass 88 — execution ledger

Date: 2026-09-23
Focus: 1953 한국산업은행법 원문 권한구조와 1954 한국식산은행→산은 선별승계·잔여청산의 행위자 분리.

## Material progress
- Meaningful source documents/pages directly opened and inspected: **15**.
- Official/primary or official institutional/archive lineage: **10 of 15**.
- Independent research lines materially advanced: **18**.
- Governance domains strengthened: **8**: finance, legislation, cabinet/public capitalization, public-bank governance, central-bank supervision, public-asset succession, liquidation administration, industrial reconstruction finance.
- Named/redacted non-president actor nodes newly added or materially deepened: **10**: 박희현, 구용서, 김유택, 백두진, 홍○○(1954 식산은행 두취), 최○○(1954 대표청산인), 홍승희, 유완창, 김영찬, 김영휘.
- Event/sub-events newly structured or materially strengthened: **10**.
- Adversarial checks: **10**.
- Cross-check bundles: **3**.
- Existing open/history-debt leads narrowed or made more precise: **8**.
- Concrete next leads generated: **40**.

## Key findings
1. 법률 제302호 부칙 제57조는 식산은행의 전 자산 자동승계가 아니라 산은 목적·업무에 맞는 자산만 `재무부장관 + 식산은행 두취 + 산은 총재` 3자 합의의 재산목록·가격에 따라 승계하도록 했다. `KIB→KDB`는 단일 successor edge가 아니라 선별승계 사건으로 모델링해야 한다.
2. 부칙 제59조는 잔여 식산은행 청산을 별도 대통령령 트랙으로 남겼다. 국가기록원 1954-04-23·07-07 기록에서도 청산위원회가 산은을 상대로 입금·임대계약 조치를 요구한다. 따라서 `한국식산은행 청산위원회`를 KDB와 별도 organization node로 구조화했다.
3. 국가기록원 해설집의 1954-04-01 계약에는 산은총재 `구○○`, 식산은행 두취 `홍○○`, 별도 대표청산인 `최○○`가 함께 등장한다. 구○○는 구용서로 강하게 좁혀지지만 비식별 원문이므로 확정하지 않았다. 홍○○·최○○도 추정 금지 상태로 candidate node를 만들었다.
4. 박희현은 1953-12-30 법 제정 당시 재무부장관으로서 부칙 제55조상 설립위원 임명·정관인가 권한을 가진 직위자였다. 다만 실제 임명·인가 문서를 확보하기 전에는 특정 실행행위를 박희현 개인에게 귀속하지 않는다.
5. KDB 법적 설립·발족일은 공식 공시 연혁과 국가기록원/동시대 회고 계열을 합치면 1954-04-01로 강하게 고정된다. 한국은행 후대 기관사 글의 `1954년 1월 출범`은 준비단계 가능성을 열어둔 채 날짜 근거로는 낮췄다.
6. 후대 인물자료에서 유완창이 `한국식산은행 청산위원회 위원장`을 지냈다는 경력이 나타나지만 공식 1954-04-01 기록은 `최○○ 대표청산인`을 적는다. 충돌로 즉시 단정하지 않고 서로 다른 직책 또는 순차 재임 가능성을 검증할 lead로 전환했다.

## Files changed
- `data/research/rhee-pass-88-kdb-1953-statute-and-1954-succession-governance-2026-09-23.md`
- `data/research/candidates/pass-88-kdb-statute-kib-succession-actors-events.json`
- `data/research/runs/2026-09-23-politician-network-pass-88.md`

## Commits
- `9cc1f0d7e08df588c4fffe0a9b5dff138a39442e` — research note, statutory reconstruction, adversarial checks, 40-lead queue.
- `29db6516b74c21e5190eaae3bb5ca593dfb6666c` — structured politician/organization/event/document/claim graph.
- This commit records the execution ledger.

## Minimum-target shortfalls
The bounded run did **not** defensibly reach 40 directly opened documents or 20 independent research lines. It reached 15 documents and 18 independent lines. The run did reach 8 governance domains, 10 actor nodes materially deepened/added, 10 event/sub-events, 10 adversarial checks, 3 cross-check bundles, 8 narrowed/open-debt lines, and 40 concrete next leads. Counts were not padded.

## Next priority
Recover the unredacted 1954-04-01 transaction and the implementing decree under Act 302 supplementary article 59. Those two sources can identify the last KIB president, representative liquidator, appointment authority and liquidation committee structure. In parallel, recover the MOF founding-commission appointment order and original KDB charter to turn currently anonymous founding commissioners into independent politician/bureaucrat nodes.

**역사부채 주간 전수조사 미실시.** Wednesday; last full review remains 2026-09-20.
