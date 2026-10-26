# Run 30 — 2026-10-05

## Scope
Continuation of the Rhee Syngman backbone, concentrating on the 1952 Pusan constitutional crisis and 1953 anti-communist POW release. Floot was not modified or built.

## Material findings
1. **1952 martial-law command attribution narrowed materially.** In the May 27 Van Fleet conversation, Rhee said the Cabinet had decided on martial law, that he approved it, that he suggested Pusan be included, and that the martial-law commander would take orders directly from him. This is stronger than merely attributing the crisis to Rhee because it happened during his presidency.
2. **Do not transfer Yi Pom-sok's proposal to Rhee.** A contemporaneous diplomatic report of a cabinet meeting attributes the proposal to arrest all Assemblymen and put them in a stockade to Home Minister Yi Pom-sok. The Prime Minister rebuked it. Rhee's recorded instruction in that meeting was instead to Yi not to prevent demonstrators from entering Pusan. The claims are separated in the claim graph.
3. **June 2 dissolution ultimatum is explicit in the diplomatic record.** FRUS doc.159's note, based on telegram 1244, says Rhee asked his Prime Minister to tell the Assembly to pass direct presidential election within 24 hours or face dissolution.
4. **July constitutional passage involved coercive attendance measures.** FRUS doc.206, drawing on UN A/2187, records police rounding up legislators and keeping scores in the Assembly Hall before the July 4 vote. This rebuts a simple 'ordinary free vote' description while leaving the Korean stenographic record as a required domestic cross-check.
5. **POW release is a high-confidence direct-attribution case.** Rhee's June 18 letter and same-day statement expressly say he ordered the release on his own responsibility and instructed provincial governors and police to care for the released prisoners. UNC/US records independently treated it as his unilateral action.
6. **Operational detail remains separate.** Top-level authorship does not establish that Rhee personally wrote camp-by-camp escape instructions or guard orders. Those Korean implementation records remain open leads.

## Politician / actor nodes deepened
- 이승만 (Syngman Rhee): martial-law approval/direct-command relationship, dissolution ultimatum, demonstrator-flow instruction, POW-release self-attribution.
- 이범석 (Yi Pom-sok): Home Minister; explicit cabinet proposal to detain all Assembly members; separate from Rhee's recorded instructions.
- 홍범희 (Hong Pom-hui): Vice Home Minister appointed immediately before martial law; operational documentation still needed.
- 윤경 (Yun Kyong): national police chief appointed immediately before martial law; arrest-order chain still needed.
- 소민호 (So Min-ho): first named Assembly arrest after martial-law proclamation; warrant issuer remains open.
- 장택상/당시 총리 node: intended messenger of June 2 ultimatum and actor opposing Yi's mass-detention suggestion in the cabinet report; exact Korean cabinet record remains a lead.
- 백두진 (Paek Tu-chin): Prime Minister in Washington conversation on June 18 POW release; treated as an independent diplomatic actor rather than presidential proxy by default.
- 변영태 (Pyun Yung-tai): Foreign Minister in same-day armistice/POW diplomacy, already linked through Korean archival letter material.
- Mark W. Clark: UNC commander, external institutional actor observing/responding to release and 1952 crisis.
- James A. Van Fleet: direct interlocutor whose conversation record provides unusually specific martial-law command attribution.

## Event/sub-event graph work
Eight structured sub-events were added in `data/events/run30-rhee-command-events.json`: martial-law command, opposition arrests, dissolution ultimatum, cabinet mass-arrest proposal, extract-amendment passage, POW-release order, post-release command crisis, and armistice/security bargaining.

## Adversarial claim audit
Ten claims were explicitly modeled. The main adversarial result is asymmetry: evidence for Rhee's direct authorship is strong for the POW release and meaningful for martial-law command, but still insufficient for every individual 1952 arrest order. The explicit 'arrest all Assemblymen' proposal is attributed to Yi Pom-sok in the contemporaneous report, not silently reassigned to Rhee.

## Direct source ledger
Meaningful source documents/pages directly checked this run: **11**, all official diplomatic/documentary-edition or contemporaneous-document pages. This run intentionally reused the strongest unresolved leads from Run 29 rather than inflating counts by reopening already-logged pages.

Independent research lines materially advanced: **10**.
General governance domains materially advanced: **6** (constitutional order, cabinet/administration, policing/security, legislature, foreign affairs/armistice, local/provincial administration).
Non-president actors materially deepened or attributionally separated: **9**.
Event/sub-event nodes structured: **8**.
Adversarial claims: **10**.
Cross-provenance bundles materially strengthened: **2** (1952 crisis via FRUS + UN-document lead; 1953 POW release via Rhee letter + UNC/State records). A third fully independent Korean operational provenance was not obtained this run.
Existing open/debt lines materially followed: **3** (HD-RHEE-006, POW-release implementation chain, 1952 constitutional coercion/domestic-record chain).

## History debt status
- **HD-RHEE-006 Pusan arrests: NARROWED.** Presidential martial-law command is now stronger, but individual arrest warrants/orders remain missing. Do not mark RESOLVED.
- **1952 mass-arrest attribution: NARROWED.** Yi Pom-sok is the documented proposer of arresting all Assemblymen in the June cabinet report. Whether separate arrest orders came from Rhee, Yi, police leadership or martial-law command must be resolved document-by-document.
- **1953 POW release: decision attribution VERIFIED; implementation chain OPEN.** Rhee's authorship is direct; camp-level execution remains a distinct research object.

## Next lead queue
1. National Assembly stenographic record, 1952-05-25, on So Min-ho arrest and quorum.
2. National Assembly stenographic record, 1952-05-26~06-04, on martial-law termination motions.
3. Korean martial-law proclamation of 1952-05-24, exact text and countersignatures.
4. Defense Ministry decree appointing Won Yong-dok martial-law commander.
5. Order/document establishing that Won Yong-dok took orders directly from Rhee.
6. So Min-ho arrest warrant/order, issuer, statutory basis and executing unit.
7. Warrants/orders for the other opposition legislators arrested May 25-26.
8. Korean case file for the alleged Communist conspiracy used to justify arrests.
9. Telegram 1160 from Pusan, 1952-05-26, 795B.00/5-2652, full text.
10. Telegram 1244 from Pusan, 1952-06-02, 795.00/6-252, full text.
11. Korean cabinet minutes for the meeting reported in FRUS doc.163.
12. Identify the Prime Minister in that meeting and obtain his own memoir/official record cautiously as a party account.
13. Interior Ministry order book under Yi Pom-sok for 1952-05-24~07-05.
14. Hong Pom-hui vice-minister appointment and command documents.
15. Yun Kyong national-police-chief appointment and first operational directives.
16. Police orders concerning transport/escort of legislators to Assembly Hall July 2-4.
17. National Assembly July 4 stenographic record, attendance and vote procedure.
18. Special committee report that produced the compromise/extract amendment text.
19. UN document A/2187 pp.5-11, full original, for independent institutional chronology.
20. ROK Gazette publication of the 1952 constitutional amendment and implementing acts.
21. Rhee public statements calling for Assembly dissolution in June 1952, Korean originals.
22. Evidence identifying organizers/funders of the pro-dissolution demonstrations.
23. Police or Interior Ministry instructions on allowing demonstrators into Pusan.
24. Rhee-Clark correspondence immediately before June 18, 1953 to test prior-notice chronology.
25. ROKA guard orders for Pusan POW camp on June 17-18, 1953.
26. ROKA guard orders for Masan, Nonsan and Sang Mu Dai camps.
27. Provincial governor circular implementing care/reception of released POWs.
28. National Police operational circular for released POWs.
29. Korean Embassy Washington cable referenced as enclosure to Rhee's June 18 Clark letter.
30. Matthews files lot 53 D 413 telegrams on breakout mechanics and immediate UNC measures.
31. Clark message to Rhee dated June 18/20 as printed in State Department Bulletin June 29, 1953.
32. Pyun Yung-tai June 18 letter to Clark, compare Korean archival version with State Bulletin text.
33. Paek Tu-chin's Korean report of June 18 meeting with Dulles, if preserved in Foreign Ministry files.
34. Robertson mission memoranda distinguishing Rhee promises from US interpretations.
35. Korean cabinet discussion of armistice and POW release before/after June 18.
36. National Assembly debate on POW release and armistice policy.

## Floor accounting
The requested 40-document and 20-line floors were **not reached in this run**. Counts are not padded. The value of this run is attributional precision and graph normalization around two high-centrality episodes.

**역사부채 주간 전수조사 미실시** — Monday run; Sunday-only full review does not apply.
