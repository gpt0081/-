# Politician Network Pass 11 — 2026-09-20

## Scope

Continue the Rhee Syngman backbone while treating the 1949 farmland-reform controversy as an event-centred constitutional and administrative network. Do not rerun the weekly full HISTORY_DEBT audit: `data/research/history-debt-review-state.json` already records `last_full_review=2026-09-20` and `next_full_review=2026-09-27`.

## Lead A — HD-EVT-001: legal character of the government's 1949-05-16 action

The National Institute of Korean History constitutional-history DB narrows the sequence further. The bill was sent to government on 1949-05-02 after the second National Assembly session had ended. Prime Minister Lee Beom-seok sent the Speaker a 1949-05-16 return-reason document arguing, among other things, that the compensation burden lacked financing and could cause inflation. The accompanying notice said the government had intended to return the bill under Constitution art. 40 but could not do so while the Assembly was out of session, and therefore regarded the bill as naturally extinguished.

The same source explicitly notes that the 1948 Constitution prescribed presidential reconsideration within 15 days but contained no rule saying a bill automatically lapsed when the Assembly was out of session. The third Assembly debated the matter on 1949-06-14 and 06-15 and resolved that the government's extinction notice was unlawful and that the bill had already become law under art. 40(4). Government then promulgated Act No. 31 on 1949-06-21.

Primary-record targets are now sharply bounded: Third Assembly 16th sitting (1949-06-14), pp. 9–23; Third Assembly 17th sitting (1949-06-15); the 1949-05-16 return-reason/notice original; and the promulgation/approval record for Act No. 31. Until those originals are compared with the U.S. diplomatic wording, HD-EVT-001 remains CONFLICTED rather than being flattened into a generic 'veto/override' narrative.

Source: https://db.history.go.kr/item/cons/level.do?levelId=cons_001_0020_0020_0030_0040_0060&viewType=tab

## Lead B — adversarial check: Rhee's position was not a simple anti-reform line

A source quoting the Constituent Assembly stenographic record identifies a 1949-04-30 closing-session speech in which Rhee welcomed completion of the farmland-reform bill while also expressing concern that landowners not be treated too harshly. This does not resolve the later 05-16 constitutional conflict, but it is important counterevidence against a one-dimensional inference that the later government action proves opposition to farmland reform as such. The system should distinguish support for reform, disagreement over compensation/finance, and the disputed constitutional procedure.

The quoted primary location is `制憲國會速記錄(4)`, Second Assembly closing ceremony (1949-04-30), p. 832. This is a primary-document lead, not yet a substitute for direct inspection of the stenographic page.

Lead source: https://biz.newdaily.co.kr/site/data/html/2013/04/15/2013041510018.html

## Lead C — new politician candidate: Oh Seok-ju (오석주)

The Academy of Korean Studies entry on the parliamentary group Sinjeonghoe identifies Oh Seok-ju as a political actor who publicly attacked the farmland-reform extinction notice, arguing that it would alienate public sentiment, criticizing abuse of presidential veto power, and demanding cabinet resignation. The same entry later identifies Sinjeonghoe as a 23-member parliamentary group in the 1949 reorganization and records its opposition to a later Industrial Committee attempt to raise compensation terms.

Candidate graph entry:

- candidate ID: `pol-oh-seok-ju-constituent`
- name: 오석주
- role/context: Constituent Assembly member; Sinjeonghoe political actor/representative
- event edge: `evt-1949-farmland-reform`
- relation: `criticized_government_extinction_notice`
- follow-up value: high for reconstructing the Assembly-side constitutional argument and the factional coalition around farmland reform
- caution: name collision with contemporary people is substantial; aliases, hanja, constituency and biographical dates must be verified from the National Assembly/constitutional member registry before promotion to the canonical `data/politicians.json` registry.

Source: https://encykorea.aks.ac.kr/Article/E0073445

## Lead D — ordinary administration / implementation gap

Farmland reform did not end with enactment. The Academy of Korean Studies entry on the Farmland Committee records that the Act required central and local farmland committees to review matters such as valuation before decisions by local authorities. Presidential Decree No. 275 established the committee rules on 1950-02-10, and the Central Farmland Committee first met on 1950-03-24. Named members included chair Yun Yeong-seon and members Ju Seok-gyun, Hong Heon-pyo, Lee Cheon-sang, Yun Wan-chang, Kim Ung-gak, Kim Seong-chan, Lee Sun-tak, Choi Sun-ju, Choi Gyu-hang, Seo Sang-il, Lee Hoon-gu, Kang Jeong-tak, Cho Baek-hyeon and Ji Yong-eun.

This creates an implementation network distinct from the enactment network. It should eventually become a sub-event or implementation phase linked to `evt-1949-farmland-reform`, because several politicians/officials recur across legislative design and administrative execution. Do not infer individual policy positions merely from committee membership.

Source: https://encykorea.aks.ac.kr/Article/E0080665

## New graph implications

1. Split the event into at least `drafting`, `Assembly legislation`, `government extinction notice`, `Assembly constitutional response`, `promulgation`, `1950 amendment`, and `implementation committees` phases.
2. Store constitutional characterization as source-specific claims: government position, Assembly resolution, later constitutional-history interpretation, and U.S. diplomatic shorthand.
3. Add Oh Seok-ju only after identity disambiguation; current evidence is sufficient for candidate-graph status but not for a fully populated stable registry node.
4. Central Farmland Committee membership supplies a new bridge from legislative politicians (Seo Sang-il, Lee Hoon-gu) to administrative implementation.

## Failed / incomplete routes

Searches for the exact 1949-06-14/15 speaker-by-speaker stenographic text did not expose the full pages through general web indexing. The NIKH constitutional-history DB supplies exact sitting/page references, so the next pass should target the National Assembly/NIKH original scans or text by those identifiers rather than repeat generic keyword searches.

## HISTORY_DEBT

Weekly full review not repeated. `HD-EVT-001` remains `CONFLICTED`, but the unresolved question is narrower: whether the 05-16 action was constitutionally effective as a reconsideration request, and how the 06-14/15 Assembly resolution legally treated it. No existing debt is marked RESOLVED from this pass.

## Next priority

Retrieve the Third Assembly 16th/17th sitting originals and extract every named speaker, motion, constitutional argument, vote/decision, and institutional role. Then compare those claims against the 05-16 return-reason document and the U.S. diplomatic description. This is the shortest route to converting HD-EVT-001 from a broad source conflict into a speaker- and document-level constitutional graph.
