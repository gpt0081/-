# Politician Network Research Pass 12 — 2026-09-20

## Scope
Continued the Rhee Syng-man backbone while treating the 1949 Farmland Reform Act as a politician/event network. The weekly full HISTORY_DEBT review was NOT repeated because `data/research/history-debt-review-state.json` records `last_full_review=2026-09-20` and `next_full_review=2026-09-27`.

## High-priority lead A — legal character of the 1949-05-16 government action
Primary/official constitutional-history material narrows HD-EVT-001 further. The National Institute of Korean History constitutional-history DB states that the bill was transmitted to the government on 1949-05-02 after the Second National Assembly session expired. Prime Minister Lee Beom-seok sent a `환부이유서` and a 1949-05-16 notice saying the government had intended to return the bill under Constitution Article 40 but could not do so while the Assembly was closed and therefore regarded the bill as naturally extinguished. The same source explicitly notes that the 1948 Constitution did not specify automatic extinction when the Assembly was closed.

The Third National Assembly debated the issue on 1949-06-14 and 06-15 (3rd Assembly, 16th sitting pp. 9–23 and 17th sitting) and resolved that the government's extinction notice was unlawful and that the bill had become law under Constitution Article 40(4). The government then promulgated it as Act No. 31 on 1949-06-21.

Research implication: do not normalize the domestic sequence into a generic `presidential veto -> override`. Preserve separate edges for (1) intended Article-40 return/reconsideration, (2) inability to return during recess, (3) government extinction theory, (4) Assembly finding of unlawfulness, (5) Assembly declaration of legal finality, and (6) government promulgation. FRUS's `veto / override / June 22 promulgation` remains a conflicting foreign diplomatic summary until the underlying embassy reporting is identified.

Primary/official source: https://db.history.go.kr/item/cons/level.do?levelId=cons_001_0020_0020_0030_0040_0060&viewType=tab

## High-priority lead B — exact transcript target
The constitutional-history DB gives the exact primary transcript target: Third National Assembly, 16th sitting (1949-06-14), pp. 9–23, plus the 17th sitting (1949-06-15). Web indexing still does not expose the full speaker-by-speaker text. This is now a bounded retrieval problem rather than an open-ended search.

Next extraction schema once the images/text are accessible:
`politician -> statement -> constitutional provision -> proposed procedural consequence -> support/opposition -> vote/result`.

## Adversarial search
A secondary pro-Rhee account cites the 1949-04-30 Second National Assembly closing-session stenographic record and quotes Rhee welcoming completion of farmland-reform deliberation while also expressing concern that landowners not be treated excessively harshly. This is useful only as a pointer to the stenographic record, not as a standalone basis for attributing policy authorship. It weakens any simplistic inference that the later government action proves opposition to farmland reform itself. The next step is direct verification of the cited closing-session pages.

Secondary pointer: https://www.newdaily.co.kr/site/data/html/2013/04/15/2013041500023.amp.html

## New politician candidate — Oh Seok-ju (吳錫柱)
Searches for the politician mentioned in the prior pass produced independent identity evidence. Contemporary `자유신문` election reporting indexes `吳錫柱` among the 1948 National Assembly election winners, and NIKH scholarship identifies Oh Seok-ju as a 5·10 election figure affiliated at election time with the Korean National Association for the Rapid Realisation of Independence (독립촉성국민회). This resolves the basic identity/hanja problem enough to create a candidate node in a subsequent registry update, but the claimed role in criticizing the farmland-reform extinction notice should still be tied to a direct Assembly or contemporary press record before assigning a strong event-action edge.

Sources:
- https://db.history.go.kr/contemp/level.do?levelId=npfp_1948_05_14_v0001_0030
- https://db.history.go.kr/id/kn_084_0060_0030_0010

## Non-controversial governance / implementation coverage
The farmland-reform corpus should distinguish enactment from implementation. Existing research has already identified the 1950 Farmland Committee regulation and Central Farmland Committee. This pass adds a methodological guardrail: committee membership is an institutional-role edge, not evidence of a member's personal position. Future extraction should connect implementation actors to administrative decisions only where minutes, appointment records, or signed decisions support the edge.

## History debt
- Weekly full review: not repeated; already completed for 2026-09-20.
- HD-EVT-001: remains CONFLICTED, but narrowed. The unresolved core is now specifically the mismatch between domestic constitutional procedure and FRUS terminology/date, plus the need for the 06-14/15 speaker-level transcript and FRUS underlying embassy source.
- No other debt status changed in this pass.

## Failed/blocked paths
- General web search did not expose the full 1949-06-14/15 stenographic text despite the exact sitting/page citation.
- No reliable indexed result yet identified the individual speakers in pp. 9–23.
- Therefore no speaker-specific constitutional stance is asserted from snippets.

## Next priorities
1. Retrieve/inspect Third National Assembly 16th sitting pp. 9–23 and 17th sitting; extract speaker-level constitutional arguments.
2. Directly verify Rhee's 1949-04-30 closing-session remarks in the stenographic record.
3. Locate the FRUS document's underlying Seoul embassy telegram/memorandum and determine why it says June 22 promulgation.
4. Find a primary record for Oh Seok-ju's alleged criticism of the extinction notice before adding that action as confirmed.
