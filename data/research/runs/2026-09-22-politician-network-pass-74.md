# Run report — Politician Network Pass 74

Date: 2026-09-22
Focus: adversarial verification of the 1953 First Committee / ROK diplomatic representation chain, continuing pass 73 without repeating its searches.

## Result

This pass directly recovered the UN official record `A/C.1/SR.617` (First Committee, 617th meeting, 20 August 1953). This is a useful correction to the prior blocked lead: the full official-record PDF is web-indexed and its text is recoverable, so lead 16 from pass 73 is narrowed rather than left blocked.

The record shows that Tsiang (China) argued that the Republic of Korea's wishes deserved special weight because Korea's existence was at stake, while explicitly denying that the ROK should impose its will or exercise a veto over the First Committee. This is important adversarial evidence against any simplified claim that pro-ROK delegations were formally asserting a Korean veto. It also means statements by allied/anti-communist delegations must not be silently attributed to the ROK mission, Rhee, Limb, Pyun, or Yang.

Korean archival material inspected in parallel further separates actor roles. NIKH `le_005_3300` confirms a 1953-09-30 Rhee→Limb document criticizing Britain over political-conference participant selection. NIKH `dh_029_1953_06_18_0060` preserves Pyun Yung-tai's 18 June letter to UNC commander Mark Clark concerning the anti-communist POW release and states that the President had ordered Korean authorities to release the prisoners. That document gives Pyun an independently evidenced foreign-minister implementation/explanation role and provides a clean proposed_by/decided_by/executed_or_explained_by distinction for the POW-release event graph. NIKH `le_005_3470` separately identifies a 1953 Pyun statement concerning conclusion of the ROK-US Mutual Defense Treaty, supporting treatment of Pyun as an independent diplomatic actor rather than merely an indexed name.

A further actor lead emerged from the official chronology: on 1953-10-25 Vice Foreign Minister Cho Chong-hwan (조정환) and Col. Lee Soo-young (이수영) were appointed Korean representatives to the Panmunjom preliminary talks. Cho should therefore be investigated as a politician/senior-official node in the post-armistice political-conference chain; Lee should remain a military/official actor unless political-office evidence warrants politician-registry inclusion.

## Evidence inspected

1. UN official record A/C.1/SR.617, 20 Aug 1953, full indexed PDF/text.
2. NIKH `le_005_3300`, Rhee→Limb, 30 Sep 1953, political-conference participant selection / Britain.
3. NIKH `dh_029_1953_06_18_0060`, Pyun→Mark Clark, 18 Jun 1953, anti-communist POW release.
4. NIKH `le_005_3470`, Pyun statement on ROK-US Mutual Defense Treaty conclusion.
5. NIKH `tcct_1953_10_25_0010`, appointment of Cho Chong-hwan and Lee Soo-young to Panmunjom preliminary talks.
6. NIKH `le_005_2690`, 21 Jul 1953 record of Pyun press-conference content.
7. NIKH `le_005_0420`, Rhee→Limb, 19 Mar 1953, criticism of Indian mediation proposal.
8. NIKH `le_005_0760`, Limb→Rhee, 6 Apr 1953, assessment of anti-armistice demonstrations.
9. NIKH `le_005_1230`, 27 Apr 1953 security-pact-necessity document addressed to Limb and indexing Rhee/Pyun.
10. NIKH `le_005_1990`, W. Y. Graham→Pyun, 22 Jun 1953, protest concerning POW release.

## Claim/adversarial findings

- `CLM-1953-ROK-HAD-FIRST-COMMITTEE-VETO`: CONTRADICTED as a formal claim by A/C.1/SR.617; Tsiang expressly denied that the ROK should impose its will or wield a veto.
- `CLM-1953-TSIANG-STATEMENT-IS-ROK-MISSION-STATEMENT`: CONTRADICTED. The speaker is the Chinese delegation; it is contemporaneous supportive observation/argument, not Korean authorship.
- `CLM-1953-POW-RELEASE-ATTRIBUTION-CAN-BE-FLATTENED-TO-PYUN`: CONTRADICTED. Pyun's letter reports a presidential order and communicates/explains it to Clark; decision and diplomatic explanation are distinct action edges.
- `CLM-1953-PYUN-ONLY-INDEXED-IN-CONFERENCE-MATERIAL`: NARROWED. Independent Pyun-origin/recipient records exist for POW-release diplomacy and mutual-defense-treaty public diplomacy.
- `CLM-1953-POLITICAL-CONFERENCE-KOREAN-ACTOR-SET-LIMITED-TO-RHEE-LIMB-PYUN-YANG`: CONTRADICTED/NARROWED by the 25 Oct appointment of Vice Foreign Minister Cho Chong-hwan to preliminary talks.

## Actor updates proposed

- `pol-pyun-yongtae`: retain VERIFIED; deepen event roles for 18 Jun POW-release diplomatic explanation and 1953 mutual-defense-treaty statement.
- `cand-limb-ben`: retain proposed VERIFIED pending exact formal title/appointment normalization.
- `cand-cho-chonghwan`: new candidate, IDENTIFIED; Vice Foreign Minister, appointed Korean representative to Panmunjom preliminary talks on 25 Oct 1953. Hanja/English romanization, lifespan and exact tenure require official normalization.
- `actor-lee-sooyoung-colonel`: non-politician official/military candidate; do not promote to politician registry absent qualifying political-office evidence.

## Event/sub-event structure proposed

1. `EVT-KOREA-1953-06-18-POW-RELEASE-ORDER` — decided_by Rhee; implementation chain requires military/police records.
2. `EVT-KOREA-1953-06-18-PYUN-LETTER-CLARK` — executed/explained_by Pyun; recipient Clark.
3. `EVT-UN-1953-08-20-FIRST-COMMITTEE-617` — observed/argued_by Tsiang; ROK interest represented rhetorically but not authored by ROK mission.
4. `EVT-KOREA-1953-09-30-RHEE-INSTRUCTION-TO-LIMB-UK-CONFERENCE` — direct correspondence edge.
5. `EVT-KOREA-1953-10-25-PANMUNJOM-PRELIMINARY-DELEGATION` — appointed/represented_by Cho Chong-hwan and Lee Soo-young; appointing authority still to verify.
6. `EVT-KOREA-1953-MUTUAL-DEFENSE-TREATY-PYUN-STATEMENT` — public diplomatic statement; exact date and text to recover.

## Execution ledger

- meaningful documents/pages directly inspected this pass: 10
- official/primary/public-archive family: 10 (UN official record + NIKH public archival/chronology records)
- independent research lines materially advanced: 8
- general domains touched: multilateral diplomacy, armistice/security, POW policy, alliance/treaty diplomacy, foreign-ministry personnel/representation, public diplomacy (6)
- adversarial claim/attribution checks: 5
- cross-provenance groups: 2 (UN↔NIKH on conference representation; NIKH correspondence↔chronology on Korean diplomatic actor expansion)
- existing leads narrowed: 5 (A/C.1/SR.617 recovery; Pyun-origin evidence; conference actor set; Rhee→Limb edge; preliminary-talk representation)
- Korean non-president politicians materially deepened/new: 3 (Pyun, Limb, Cho Chong-hwan)
- event/sub-event candidates structured: 6
- concrete next leads: 30
- Floot: untouched

The requested 40-document, 20-line, 10-politician, 10-adversarial-search and 8-event thresholds were not reached in this connector-bounded pass. Counts are not inflated. The useful gain is that a previously blocked UN full record was recovered and attribution boundaries became sharper.

## Next lead queue

1. Retrieve A/C.1/SR.618–625 and enumerate every explicit ROK/Korean-government reference and speaker.
2. Retrieve A/C.1/SR.613–616 to establish the debate baseline before meeting 617.
3. Retrieve A/PV.430 and distinguish Korean attendance/observation from member-state voting.
4. Retrieve A/L.153 original Indian draft and map sponsor language.
5. Retrieve A/C.1/L.53 and relation to the Indian proposal.
6. Retrieve A/L.158 and sponsor/amendment chain.
7. Retrieve A/L.152/Rev.2 Soviet participation draft.
8. Retrieve A/C.1/L.48 Soviet 11-power proposal.
9. Identify whether Limb was physically present/credentialed in meetings 613–625 and under what formal observer title.
10. Verify Limb's exact 1953 UN title and appointment dates from ROK Foreign Ministry/personnel records.
11. Recover full original image/text of `le_005_3300` and classify wording as instruction, opinion, or request.
12. Recover full original image/text of `le_005_3310` and compare Limb's report with UN meeting chronology.
13. Recover full original image/text of the 1953-09-22 Limb Soviet-participation record.
14. Recover full original image/text of the 1953-11-11 Limb atrocities-agenda record.
15. Recover full original image/text of `dh_029_1953_06_18_0060` source pages 330–332 and map every action verb.
16. Find the operational military/police orders that implemented the 18 June POW release; do not infer implementation solely from Pyun's letter.
17. Find Clark/UNC contemporaneous response to Pyun's 18 June letter.
18. Trace W. Y. Graham's 22 June protest and identify institutional role/provenance.
19. Recover exact date/text of Pyun's mutual-defense-treaty statement `le_005_3470`.
20. Cross-check Pyun's treaty statement against signed treaty text and U.S. diplomatic record.
21. Normalize Cho Chong-hwan: Hanja, English romanization, lifespan, vice-minister tenure, appointment authority.
22. Search Foreign Ministry records for Cho Chong-hwan's Panmunjom preliminary-talk reports after 25 Oct.
23. Identify who appointed Cho/Lee and whether Cabinet/President approved the delegation.
24. Map Panmunjom preliminary talks into the September–December political-conference event chain.
25. Determine whether Lee Soo-young later held qualifying political/administrative office before considering politician registry.
26. Search Cabinet minutes for conference-composition and preliminary-talk delegation decisions, Aug–Oct 1953.
27. Search ROK mission outgoing cables for responses to First Committee meetings 617–625.
28. Adversarially compare Tsiang's 'no veto' formulation with Canadian, Australian, Indian and UK diplomatic records describing ROK pressure.
29. Add explicit `speaker_for`, `supportive_of`, `not_authored_by`, `decision_reported_by`, and `implementation_unknown` relation types to the migration plan.
30. Audit existing event graph for any node that conflates Rhee's decision, Pyun's explanation, and implementing agencies in the POW-release episode.

역사부채 주간 전수조사 미실시. 화요일이며 일요일 첫 실행 조건이 아니다.
