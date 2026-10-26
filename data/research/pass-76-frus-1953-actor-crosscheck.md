# Pass 76 — FRUS cross-check of the 1953 Korean actor network

Date: 2026-09-22
Scope: independent U.S. diplomatic provenance cross-check of Korean actors exposed in pass 75. Floot untouched.

## Why this pass

Pass 75 was dominated by NIKH aggregation. This pass deliberately moved to the U.S. Department of State FRUS corpus to test whether actor/action edges survive in an independent archival family. It does not treat U.S. diplomatic observation as proof of Korean private motives.

## Directly inspected FRUS documents/pages

1. FRUS 1952–54 Korea XV/1, doc. 578, editorial note: Choi Duk Shin, ROK delegate at Panmunjom, had boycotted plenaries since 15 May and was recalled 7 June; CINCUNC telegram C 62874 is identified as the underlying record.
2. XV/2 doc. 589, June armistice sequence reference page.
3. XV/2 doc. 611, 18 June memorandum: Paek Tu Chin and Yang You Chan met Dulles/Robertson/Nash/Young/Sullivan concerning Rhee's unilateral POW release.
4. XV/2 doc. 620, Clark/Taylor chain concerning prevention of further unilateral POW action.
5. XV/2 doc. 643, 28 June Clark→JCS joint message: Robertson/Clark report Rhee's response to U.S. answers on armistice-related questions.
6. XV/2 doc. 647, U.S. planning asks about ROK Army capability/probability of preventing Rhee from sabotaging armistice.
7. XV/2 doc. 679, 9 July Robertson→State: Prime Minister Paik suggested Robertson see Rhee alone and inferred Pyun should not be present.
8. XV/2 doc. 691, 11 July memorandum: Rhee met Robertson, Briggs, Paik Tu-chin, Pyon Yongtae, Young.
9. XV/2 doc. 703, July diplomatic reporting records a Paik/Pyun interaction and explicitly characterizes Pyun as having the upper hand in that meeting; retain as U.S. observer assessment only.
10. XV/2 doc. 727, 29 July memorandum: Yang You Chan and Robertson discuss Pyun; Yang is reported as saying he had tried to moderate Pyun's approach at the prior UN General Assembly. This is a contemporaneous diplomatic report, not direct proof of Pyun's intentions.
11. XV/2 doc. 734, 5 August first Dulles–Rhee meeting: Korean participants include Rhee, Prime Minister Paik, Foreign Minister Pyun, Defense Minister Sohn and Minister Kim. This creates explicit participant edges rather than presidential-only attribution.
12. XV/2 doc. 735, 5 August Dulles private conversation with Rhee on Korean unification.
13. XV/2 chapter II contents, documents 735–740, used to bound the Dulles visit sequence and prevent collapsing multiple meetings into one event.
14. XV/2 index: Cho Chung Whan and Choi Duk Shin have multiple page references, providing concrete follow-up locations for non-president actor work.
15. XV/2 doc. 914 (1954 follow-on): Yang You Chan with Pyo Wook Han and Dulles, useful for continuity of Yang's diplomatic role but not counted as a 1953 event.

## Cross-provenance findings

### Choi Duk Shin
Pass 75's Korean-side chronology edge is independently strengthened: FRUS doc. 578 identifies Choi as the ROK armistice delegate and gives an operational timeline, including boycott and recall. This is stronger than a bare appointment record because it distinguishes appointment/status from actual participation behavior. New lead: recover CINCUNC telegram C 62874 and the Korean recall order before attributing the recall decision to Rhee or a ministry.

### Paek Tu Chin
FRUS docs. 611, 679, 691 and 734 independently establish Paek as an active diplomatic participant, not merely a title in a Korean chronology. In doc. 679 he is the source of a tactical suggestion about meeting composition. This supports a `proposed_by`/`advised` relation for that meeting arrangement, but not a general claim that Paek controlled armistice policy.

### Yang You Chan
FRUS docs. 611 and 727 independently establish Yang as an active ambassadorial intermediary. Doc. 727 supports an `observed_statement` edge in which Yang is reported to describe his own attempts to moderate Pyun. Because the memorandum is U.S.-authored, the statement must remain `reported_by_us_diplomatic_record`, not silently upgraded to a Korean-origin document.

### Pyun Yung Tai
Docs. 691, 703, 727 and 734 show repeated participation and disagreement/mediation dynamics. The strongest safe claim is repeated participation plus U.S. observers' descriptions of Pyun's stance. Claims about motive or decisive control remain open.

### Choi/Paek/Yang attribution rule
The independent FRUS family confirms that event membership is heterogeneous: delegate status, participant status, suggestion, reported self-description, observer characterization and formal decision are different edge types. This validates the pass-75 warning against treating every indexed person as an operational actor.

## Adversarial checks

1. Choi appointment does not prove continuous attendance: doc. 578 supplies boycott/recall evidence.
2. Choi recall does not prove presidential direct order: underlying Korean recall instrument still missing.
3. Paek's presence does not prove authorship of Rhee policy: docs. 691/734 are participant lists.
4. Paek's suggestion in doc. 679 is limited to meeting composition and must not be generalized.
5. Yang's reported remarks about Pyun are mediated by a U.S. memorandum and need Korean-side corroboration.
6. Robertson's criticism of Pyun in doc. 727 is an American official's assessment, not a neutral fact about Pyun's motives.
7. Doc. 703's 'upper hand' characterization is observer language, not a formal decision record.
8. Dulles–Rhee private doc. 735 excludes the other Korean ministers and therefore cannot be used to attribute its private exchange to them.
9. The U.S. concern in doc. 647 about ROK Army behavior is planning/assessment, not proof that an ROK coup or refusal was planned.
10. The 1954 Yang record proves role continuity only and must not be back-projected into every 1953 decision.

## Leads narrowed

- Choi Duk Shin actual armistice participation: narrowed from appointment-only to appointment + boycott + recall timeline.
- Paek Tu Chin armistice-policy role: narrowed to documented meeting participant and one specific meeting-composition suggestion.
- Yang You Chan intermediary role: narrowed to documented participation plus reported mediation statement.
- Pyun Yung Tai influence: narrowed to repeated participation and contemporaneous U.S. descriptions; decisive-control claim remains unproven.
- 5 August Dulles visit: split into general meeting (doc. 734) and private Rhee conversation (doc. 735), preventing participant leakage.
- Korean POW-release diplomatic response: Paek and Yang are directly documented in Washington on 18 June (doc. 611).
- Choi recall provenance: underlying CINCUNC C 62874 identified.
- Cho Chung Whan follow-up: FRUS index yields a concrete page cluster for targeted extraction.

## Next concrete lead queue

1. Recover CINCUNC telegram C 62874, 1953-06-07, and identify who communicated Choi's recall.
2. Recover Korean Foreign Ministry/ROK delegation recall instrument for Choi, same date.
3. Recover records explaining Choi's boycott beginning 1953-05-15.
4. Compare Choi's own memoir/account with CINCUNC reporting on the boycott.
5. Extract FRUS pages 949–950, 1007, 1012, 1122, 1148, 1831 for every Choi edge.
6. Extract FRUS index page cluster 1521–1522 for Cho Chung Whan.
7. Extract Cho Chung Whan references 1528–1529, 1559, 1651, 1689, 1812, 1867.
8. Determine whether FRUS spelling Cho Chung Whan maps exactly to registry Cho Chong-hwan/曺正煥.
9. Recover Korean personnel record for Cho's vice-minister term and normalize Romanization.
10. Recover Korean appointment instrument for the 25 October Panmunjom preliminary delegation.
11. Recover Korean report submitted by Cho after first preliminary session.
12. Recover full FRUS doc. 703 context and identify exact Korean participants before coding influence edges.
13. Recover any Korean record of the same meeting in doc. 703.
14. Search Yang You Chan papers/cables for his own account of attempts to moderate Pyun.
15. Search Pyun Yung Tai papers/speeches for the UN General Assembly episode Yang referenced.
16. Compare Robertson's doc. 727 assessment with Briggs reporting on Pyun.
17. Compare doc. 727 with Rhee correspondence about Pyun during the Robertson mission.
18. Recover doc. 679 Korean-side diary/cabinet trace for Paek's meeting-composition suggestion.
19. Identify whether Paek acted as prime minister, personal adviser, or economic-policy representative in each 1953 event separately.
20. Recover Paek's 8 July CEB letter from the Korean/NIKH side and connect it to his FRUS diplomatic role without conflating functions.
21. Recover Hanlon 29 May CEB letter referenced in the Korean record.
22. Recover Pyun acting-PM 10 June CEB reply and test whether office/title is correctly normalized.
23. Recover full participant identity for 'Minister Kim' in FRUS doc. 734.
24. Normalize Defense Minister Sohn in doc. 734 to stable Korean actor ID with official personnel source.
25. Split 5 August Dulles visit into general, private-unification, and subsequent meeting sub-events.
26. Recover docs. 736–740 and code participant/author/decision edges separately.
27. Compare the 5 August Korean participant list against Korean Foreign Ministry minutes.
28. Trace doc. 611's Korean-side reporting of the 18 June Washington meeting.
29. Recover President Eisenhower's message to Rhee referenced in doc. 611.
30. Separate Paek/Yang knowledge of the POW release from evidence of advance knowledge; search for pre-18 June cables.
31. Recover doc. 620 full text and identify Korean recipients/actors in Clark's request chain.
32. Recover Korean military orders implementing or resisting Clark's post-release requests.
33. Compare doc. 647 planning assumptions with later observed ROK Army behavior.
34. Audit existing 1953 events for participant leakage between adjacent Robertson/Dulles meetings.
35. Add explicit relation vocabulary for `participant`, `suggested_meeting_arrangement`, `reported_self_description`, `observer_assessment`, `delegate_status`, `boycott`, `recalled_by_unknown_authority`.
36. Search official Korean personnel sources for Yang You Chan's exact ambassador term dates.
37. Search official Korean personnel sources for Pyun Yung Tai's foreign-minister and acting-PM dates.
38. Search official Korean personnel sources for Paek Tu Chin's prime-minister term dates.
39. Search Choi Duk Shin official biography for later ministerial/political offices before registry promotion.
40. Cross-check these actor edges against National Assembly records where domestic policy consequences were debated.

## Execution ledger

- meaningful FRUS documents/pages directly inspected: 15
- official/primary diplomatic publication family: 15
- independent research lines materially advanced: 10
- general domains touched: armistice/security, foreign affairs, executive coordination, military command, diplomatic representation, post-armistice planning (6)
- adversarial checks: 10
- existing leads narrowed: 8
- cross-provenance groups materially strengthened: 4 actor clusters (Choi, Paek, Yang, Pyun) across NIKH-derived prior work and FRUS
- new concrete leads: 40
- new politician nodes: 0; this pass deliberately deepened already surfaced non-president actors rather than inflate names
- new event candidates: 6 meeting/recall/participation sub-events identified for graph synchronization
- requested 40-document threshold: not reached; actual count retained without inflation
- requested 20 independent-line threshold: not reached; actual count 10
- Floot: untouched

역사부채 주간 전수조사 미실시. 화요일이며 일요일 첫 실행 조건이 아니다.
