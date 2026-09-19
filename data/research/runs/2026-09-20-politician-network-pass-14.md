# Politician network research pass 14 — 2026-09-20

## Scope

Continue the Rhee Syng-man presidential backbone while growing the politician-centric network. This pass did not repeat the Sunday full HISTORY_DEBT audit because `history-debt-review-state.json` already records `last_full_review=2026-09-20`.

Primary targets: (1) test the candidate-graph claim that Kang Jin-guk was a substantive farmland-reform policy actor using contemporary material, (2) test the later electoral-trajectory lead without promoting it on weak evidence, (3) extend the implementation/administrative layer below minister and bureau-chief level.

## New evidence

### Kang Jin-guk: contemporary record substantially strengthens policy-actor status

The National Institute of Korean History `자료대한민국사` exposes multiple contemporary newspaper records under 姜辰國:

- 1949-01-15, `대구시보`: Kang, explicitly titled 농림부 농지국장, lectured on `농지개혁과 한국경제의 장래` and discussed the drafting philosophy (`農改起案理念`).
- 1949-01-25, `서울신문`: after a Jan 4–22 field trip through Gangwon, Chungcheong, Gyeongsang and Jeolla areas, Kang described meetings with local officials, land-administration personnel and farmers. This is direct contemporary evidence for field investigation feeding policy preparation.
- 1949-02-04, `수산경제신문`: the record explicitly calls Kang the `농림부案의 입안자` while reporting his response to large revisions of the farmland-reform bill. This materially upgrades the previous secondary-source-only claim that he was a drafting actor.
- 1949-04-17, `동아일보`: Kang published/explained `농지개혁과 지주대책`, identifying destruction of the tenancy system as the reform's fundamental purpose and explaining its social-economic rationale.
- 1949-08-08, `국도신문`: after promulgation, Kang publicly explained landlord return-to-farming and forced-sale disputes. This connects him not only to drafting but also to implementation guidance.

These are contemporary reports preserved by an official historical database. They do not prove that every clause was personally authored by Kang, so clause-level attribution remains open.

Sources:
- https://db.history.go.kr/contemp/level.do?levelId=dh_010_1949_01_15_0020
- https://db.history.go.kr/contemp/level.do?levelId=dh_010_1949_01_25_0050
- https://db.history.go.kr/contemp/level.do?levelId=dh_010_1949_02_04_0010
- https://db.history.go.kr/contemp/level.do?levelId=dh_011_1949_04_17_0010
- https://db.history.go.kr/contemp/level.do?levelId=dh_013_1949_08_08_0010

### Surviving 1949 Kang publication

Seoul National University Library's rare-book catalogue identifies `農地改革法解說 / 姜辰國 著`, published in Seoul in 1949, 64+10 pages, with `農地改革과 韓國經濟의 將來` appended. The catalogue says the copy is available in the Heritage Library. This is a high-value next-step original-text target because it can be compared against the enacted statute and Kang's contemporary statements.

Source: https://rarebook.snu.ac.kr/advance-search/detail/?cid=192313&lang=en&mmsid=99160046302591

## Adversarial / uncertainty check

The search for Kang's alleged 1950, 1954 and 1960 election runs did not produce an authoritative NEC/National Assembly candidate record in this pass. A derived election table does contain a Kang Jin-guk candidate in 1954 Yeongdeungpo-gap, and the long-form secondary biography reports three election attempts including 1960 Dongnae, but this is insufficient to promote him to the stable politician registry. The prior candidate graph's 1950 district description is therefore weakened to `district unresolved` until a candidate list or official election history is obtained.

This is deliberate negative progress: policy authorship is now much stronger, while the electoral-politician identity link remains unconfirmed.

## New candidate actors from the drafting team

A detailed secondary account names the three section chiefs under Kang Jin-guk as:

- 윤택중 — 지정과장
- 배기철 — 분배과장
- 안창수 — 사정과장

They are added only to the candidate graph, not the stable politician registry. Their exact personnel records, hanja spellings (except the tentative 윤택중 spelling), life dates, and later political activity require official personnel/gazette verification. Their value is structural: they open the layer between `농지국장` and actual land designation/distribution/assessment administration.

Secondary lead: https://www.ohmynews.com/NWS_Web/Mobile/at_pg.aspx?CNTN_CD=A0002777874&SRS_CD=0000013278

## General governance coverage added

Farmland reform is now traceable as an administrative chain, not only a constitutional controversy:

`minister / vice-minister → farmland bureau chief → designation / distribution / assessment sections → field investigation → bill explanation → post-promulgation implementation guidance`.

This is useful for future politician/person annals because it distinguishes policy sponsorship, drafting, statutory revision and implementation.

## HISTORY_DEBT

Weekly full review not repeated. No existing debt status changed. HD-EVT-001 remains conflicted; this pass did not find new primary material resolving the May–June 1949 constitutional procedure conflict.

## Files changed

- `data/research/candidate-politician-graph.json`
- `data/research/runs/2026-09-20-politician-network-pass-14.md`

## Next priority

1. Obtain official candidate lists/election history for 姜辰國 in 1950/1954/1960; do not infer identity from name alone.
2. Trace 윤택중·배기철·안창수 through official gazette/personnel records and the Ministry of Agriculture organization chart.
3. Obtain/read the 1949 `農地改革法解說` original and map its propositions against the Agriculture Ministry draft, Planning Board revisions, National Assembly amendments and enacted text.
4. Continue the unresolved 3rd National Assembly session 16/17 transcript hunt for HD-EVT-001 when an original transcript surface becomes available.
