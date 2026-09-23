# Politician Network Pass 91 — execution ledger

Date: 2026-09-23
Focus: 한국식산은행 해산 직전 두취 identity, 청산위원장 succession, 한일회담으로 이어지는 식산은행 비대통령 actor network.

## Material progress
- Meaningful documents/pages directly opened or substantively inspected: **15**.
- Official/primary or official-institutional sources: **13 of 15**.
- Independent research lines materially advanced: **14**.
- Governance domains strengthened: **7**: public finance, industrial finance, cabinet/administrative personnel, foreign claims, economic diplomacy, corporate liquidation, postwar reconstruction.
- Non-president actor nodes newly identified or materially deepened: **11**: 임송본, 백두진, 유완창, 양유찬, 김용식, 임철호, 유진오, 홍진기, 류태하, 김동조, 최규하.
- Event/sub-events newly structured or materially strengthened: **8**.
- Adversarial checks: **10**.
- Cross-check bundles: **3**.
- Existing/open history-debt lines narrowed or newly specified: **5**.
- Concrete next leads generated: **40**.

## Key findings
1. 1951-02-15 국사편찬위원회 자료는 백두진을 식산은행 두취로 명시하지만, 1951-10-20 한일회담 외교문서는 임송본을 식산은행 두취로 명시한다. 따라서 백두진을 1954 해산 직전 두취로 보는 연속성 가정은 기각했다.
2. 임송본은 1951-10-20 식산은행 두취이자 한일회담 한국측 대표였다. 1952 청구권 교섭 자료집에도 임송본 인사말이 별도 원문으로 존재한다.
3. 국가기록원 대한석탄공사 기관연혁은 임송본이 1954-03-31 석탄공사 사장에 취임했다고 명시한다. 식산은행 해산은 다음날인 1954-04-01이므로 해산 직전 두취가 임송본이었을 가능성이 크게 높아졌지만, 사임/후임·주총 원문 없이는 확정하지 않았다.
4. 유완창을 1958-10-25의 청산위원장 `오○○`과 합치는 가설은 성씨부터 맞지 않는다. 유완창의 후대 청산위원장 재임은 별도 chronology로 분리했다.
5. 1958 제1차 청산중간분배는 국가기록원 DA0423876뿐 아니라 공보실 `정부 시정업적 1957-1958` 재무부 이재행정 p.114에도 수록되어 두 공식 provenance 계열로 교차검증됐다.
6. 식산은행 actor graph가 한일회담·대일재산청구권으로 직접 뻗는다. 임송본과 함께 양유찬·김용식·임철호·유진오·홍진기·류태하·김동조·최규하를 shared-document actor network로 구조화했다.
7. 한국은행 기관사는 전 식산은행 두취 백두진이 재무장관 시절 초기 산은법안에 소극적이었다고 서술한다. 따라서 `전 식산은행장→산은 설립 추진자`라는 목적론적 attribution을 보류하고 국회·국무회의 원문을 다음 표적으로 고정했다.

## Files changed
- `data/research/rhee-pass-91-kib-actor-identification-2026-09-23.md`
- `data/research/candidates/pass-91-kib-actor-identification.json`
- `data/research/runs/2026-09-23-politician-network-pass-91.md`

## Commits
- `8a4a171a5dc39092d94d9e3c4dd772e039dadb6c` — research note, evidence chain, adversarial checks, 40-lead queue.
- `8246bb8c3af41c207736cb9ca4028bc392bce3e3` — structured actor/event/document/claim/history-debt graph.
- This commit records the execution ledger.

## Minimum-target shortfalls
This bounded run did **not** reach 40 directly opened documents or 20 independent research lines. Actual counts are reported and not padded. The main retrieval bottleneck was National Archives PDF/original-image timeout. It did reach 7 governance domains, 11 non-president actors, 8 event/sub-events, 10 adversarial checks, 3 cross-check bundles and 40 concrete next leads.

## Next priority
The highest-value target is now very narrow: obtain the 1954-03~04 personnel/board records and the 1954-04-01~10 extraordinary shareholders meeting minutes. These can resolve whether 임송본 was the statutory `두취` who had to summon the meeting and identify the original liquidators. In parallel, recover DA0423876's 1958-10-25 original to unmask `오○○`, then establish 유완창's separate chair tenure. After those identities are fixed, promote the relevant actors into the canonical politician registry with explicit evidence links rather than relying on candidate-only nodes.

**역사부채 주간 전수조사 미실시.** Wednesday; last full review remains 2026-09-20.
