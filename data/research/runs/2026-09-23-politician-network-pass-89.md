# Politician Network Pass 89 — execution ledger

Date: 2026-09-23
Focus: 한국산업은행 설립위원회 법정 구조와 한국식산은행 청산권한 모델 재검증.

## Material progress
- Meaningful documents/pages directly opened and inspected: **5**.
- Official/primary or official institutional sources: **5 of 5**.
- Independent research lines materially advanced: **10**.
- Governance domains strengthened: **5**: public-bank founding, administrative organization, public finance/capitalization, records governance, liquidation administration.
- Non-president actor/actor-slot nodes added or materially deepened: **6**: 박희현, 구용서, 1954 설립위원장 slot, 9인 설립위원 slot, 대표청산인 최○○, 유완창.
- Event/sub-events newly structured or materially strengthened: **8**.
- Adversarial checks: **10**.
- Cross-check bundles: **2**: Act 302 + Decree 860; 1954 archival liquidation evidence + 1963 official decree text.
- Existing open/history-debt lines narrowed: **4**.
- Concrete next leads generated: **40**.

## Key findings
1. 대통령령 제860호는 산은 설립위원회를 **9인** 합의체로 만들고, 재무부장관이 별도 위원장 1인을 위촉하도록 했다.
2. 정관 작성은 일반 과반이 아니라 **설립위원 3분의2 이상** 의결을 요구했다. 정관 회의록은 개인별 제도설계 관여를 복원할 핵심 문서다.
3. 설립위원회는 KIB 안에 사무소를 두고 KIB에서 설립비용을 차입했으며, 비용은 이후 KDB가 부담했다. 제도적 단절보다 준비단계의 조직·재정 연속성이 명시적이다.
4. 설립위원회는 KDB 설립 즉시 자동 소멸하지 않고 설립일부터 30일 안에 해산하며, 관계문서를 KDB에 인계하고 재무부장관에게 `설립 종합경과보고서`를 제출해야 했다. 따라서 실명 9인과 실제 의사결정 기록의 보존 경로가 크게 좁혀졌다.
5. 국가법령정보센터의 1963 일부개정 제859호는 `한국산업은행총재는 한국식산은행의 청산인이 된다`고 명시한다. 이는 기존의 `청산위원회는 KDB와 별도 행위자` 모델을 폐기하기보다 법정 청산인·청산위원회·대표청산인의 권한관계를 재구성해야 한다는 반증 신호다. 단, 1954 제정 원문을 확보하기 전 1963 조문을 소급 적용하지 않았다.

## Files changed
- `data/research/rhee-pass-89-kdb-founding-decree-and-liquidator-authority-2026-09-23.md`
- `data/research/candidates/pass-89-kdb-founding-liquidator-authority.json`
- `data/research/runs/2026-09-23-politician-network-pass-89.md`

## Commits
- `b983ef6bb22bbc0464896a87fc62cffd51ebdeca` — research note, primary-decree reconstruction, adversarial checks, 40-lead queue.
- `fa2c0ec0dc6a6dc7cb35692bd8941dd42e901542` — structured organization/actor-slot/event/document/claim graph.
- This commit records the execution ledger.

## Minimum-target shortfalls
This bounded run did **not** reach the requested 40 directly opened documents, 20 independent research lines, 10 non-president named politicians, 6 governance domains, 3 cross-check bundles, or 8 existing debt/lead traces. Actual defensible counts are reported above and were not padded. It did reach 8 event/sub-events, 10 adversarial checks and 40 concrete next leads. The most valuable unresolved target remains the **1954 original text of Presidential Decree 859** and the **founding commission final report**.

## Next priority
First recover the 1954 promulgated Decree 859 and diff it against the 1963 amended text. In parallel recover the KDB founding commission's mandatory final report, appointment list of nine commissioners, chair designation, charter minutes, and 1954-04-01 handover. These can convert anonymous actor slots into independent politician/bureaucrat nodes and resolve the legal relationship among KDB governor, KIB liquidation committee, representative liquidator Choi○○, and later chair Yu Wan-chang.

**역사부채 주간 전수조사 미실시.** Wednesday; last full review remains 2026-09-20.
