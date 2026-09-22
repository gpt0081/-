# Pass 77 — Dulles Seoul cabinet network and actor attribution (2026-09-22)

## Scope
This pass follows pass 76 by resolving actor identities and separating cabinet, military, diplomatic, economic-aid, and treaty-working-party roles in the 5–8 August 1953 Dulles–Rhee consultations. Floot was not touched.

## Directly opened official documents
All are U.S. Department of State, Office of the Historian, *FRUS 1952–1954, Korea, Vol. XV, Part 2*.

1. d734, 1953-08-05, first Rhee–Dulles meeting: https://history.state.gov/historicaldocuments/frus1952-54v15p2/d734
2. d735, 1953-08-05, private Rhee–Dulles conversation: https://history.state.gov/historicaldocuments/frus1952-54v15p2/d735
3. d736, 1953-08-06, Dulles telegram on possible initialing of security treaty: https://history.state.gov/historicaldocuments/frus1952-54v15p2/d736
4. d737, 1953-08-06, second meeting, economic assistance: https://history.state.gov/historicaldocuments/frus1952-54v15p2/d737
5. d738, 1953-08-06, Paik/Stevens economic-aid and armed-forces meeting: https://history.state.gov/historicaldocuments/frus1952-54v15p2/d738
6. d739, 1953-08-07, third meeting: https://history.state.gov/historicaldocuments/frus1952-54v15p2/d739
7. d740, 1953-08-07, fourth meeting: https://history.state.gov/historicaldocuments/frus1952-54v15p2/d740
8. d741, 1953-08-08, final meeting: https://history.state.gov/historicaldocuments/frus1952-54v15p2/d741
9. d742, immediate post-consultation record: https://history.state.gov/historicaldocuments/frus1952-54v15p2/d742
10. d743, immediate post-consultation record: https://history.state.gov/historicaldocuments/frus1952-54v15p2/d743

Cross-provenance mirror checked for the final meeting: National Institute of Korean History / Korean History Database FRUS record, https://db.history.go.kr/common/compareViewer.do?levelId=frus_009_0020_0160&type=contemp .

## Corrections and narrowed identities

### Defense Minister “Sohn”
Pass 76 left `cand-sohn-defense-minister-1953` unresolved. d737 spells the participant as “Sohn Won Il”; d738 spells “Son Won II” and identifies him as Defense Minister. FRUS China/Japan vol. XIV, part 2, d671 adds that Admiral Sohn received the defense-minister appointment on 1953-06-30. This is sufficient to map the candidate to **손원일 / Sohn Won Il**. The candidate should be retired in favor of stable `pol-sohn-won-il` once the Korean official personnel record supplies Hanja, lifespan, and exact term boundaries.

### “Minister Kim”
Pass 76 correctly left this unresolved. d734 itself contains an editorial footnote: **“Presumably Kim Bop Rim, Minister of Education, Republic of Korea.”** Therefore the identity is narrowed, not fully resolved. Encode as `cand-kim-bop-rim-dulles-1953` with confidence `probable-editorial`, not as a verified stable edge. Importantly, d734 also says Rhee selected Foreign Minister Pyun and Minister Kim as the ROK members of the mutual-defense-treaty working party. If Kim Bop Rim is confirmed, the education minister had a treaty-drafting role that should not be inferred merely from his portfolio.

### Cho Chung Whan
FRUS index usage and later biographical material strongly indicate **조정환 / Cho Chung-whan**. However this pass did not recover a Korean official personnel page, so pass 76’s `identity-crosscheck-required` remains appropriate. Do not silently promote from a secondary biographical page.

## Actor network extracted from d734–d741

- **백두진 / Paik Tu Chin**: prime minister; participant across the consultations; in d737 personally requests a separate meeting with Army Secretary Stevens; in d738 presses economic-aid MOU, military conversion rate, local-cost burden, Tasca program, UN-force utilities/services, and force-expansion questions. This is a direct policy-actor edge, not merely attendance.
- **변영태 / Pyun Yung Tai**: foreign minister; selected by Rhee for the bilateral treaty working party in d734; in d740 proposes an addition to the joint statement concerning ROK sovereignty and the right to drive Chinese Communist forces from Korean soil. The proposal is rejected by Dulles on consistency grounds and the Korean side accepts the objection.
- **손원일 / Sohn Won Il**: defense minister; in d738 summarizes proposed programs of the three ROK armed services. This supports `executive_program_presenter`, not proof that he originated each service request.
- **백선엽 / Paek Sun Yup**: ROK Army chief of staff, participant in d738. Presence supports a military-policy consultation edge; individual authorship of the 20-division request remains to be proven.
- **박옥규 / Park Ok Kyu**: ROK Navy chief of staff, participant in d738. Program authorship should remain service-level pending Korean naval records.
- **최용덕 / Choi Yong Duk**: ROK Air Force chief of staff, participant in d738. Same attribution caution.
- **임병직 / Ben C. Limb**: ROK observer to the UN, participant in d739–d741. This makes him a recurring post-armistice diplomatic node, not a one-off name.
- **김법린 / Kim Bop Rim**: probable identity of “Minister Kim” in d734 editorial apparatus; probable participant across d734/d737/d739/d741 and probable treaty-working-party member. Status remains NARROWED pending Korean-side corroboration.
- **조정환 / Cho Chung-whan**: keep identity crosscheck lead open; FRUS index recurrence makes him a high-value foreign-affairs node for the 1953–55 bridge.
- **양유찬 / Yang You Chan** and **최덕신 / Choi Duk Shin**: retained from pass 76 as cross-event diplomatic/military nodes; Korean-origin records remain necessary before converting U.S.-reported assessments into motive/influence claims.

## Event/sub-event decomposition

1. `evt-1953-0805-dulles-rhee-general-meeting`: general consultation, distinct from private d735 conversation.
2. `evt-1953-0805-mutual-defense-treaty-working-party-formation`: Rhee selects Pyun + “Minister Kim”; Dulles selects Dean + Young.
3. `evt-1953-0805-rhee-dulles-private-unification`: d735, bilateral private conversation; no cabinet participants should be backfilled into it.
4. `evt-1953-0806-economic-assistance-general-meeting`: d737, aid architecture and Combined Economic Board discussion.
5. `evt-1953-0806-paik-stevens-aid-defense-meeting`: d738, separate meeting requested by Paik; economic-aid and force-program agenda.
6. `evt-1953-0806-rok-service-expansion-presentation`: Sohn summarizes Army/Navy/Air Force proposals; service chiefs present.
7. `evt-1953-0807-third-rhee-dulles-meeting`: d739, post-armistice political/security consultation.
8. `evt-1953-0807-fourth-rhee-dulles-meeting`: d740, joint-statement and treaty-draft bargaining; Pyun amendment proposal is separately attributable.
9. `evt-1953-0808-final-rhee-dulles-meeting`: d741, final consultation with Limb and Minister Kim present.

## Adversarial checks performed

1. Tested whether “Sohn” could remain ambiguous: d737/d738 and FRUS d671 collapse the ambiguity to Sohn Won Il.
2. Tested whether “Minister Kim” could be safely normalized: no. FRUS itself says “presumably Kim Bop Rim”; retain uncertainty.
3. Tested whether all Aug. 5 statements can be attributed to the full cabinet: no. d735 is explicitly private Rhee–Dulles.
4. Tested whether Sohn’s d738 presentation proves personal authorship of all force programs: no; source says he summarized programs proposed by the three services.
5. Tested whether Paik was merely ceremonial: no; d737/d738 show concrete requests and policy bargaining.
6. Tested whether Pyun’s sovereignty language became the agreed text: no; d740 records Dulles’s objection and Korean acceptance of the objection.
7. Tested whether the treaty working party was identical to the general meeting: no; d734 names a four-person working party nested within the broader consultation.
8. Tested whether Ben Limb’s presence is one-off: no; he recurs across d739–d741.
9. Tested whether the Combined Economic Board proposal was solely an American design: d737 records Rhee advocating it as the supreme planning body, while d738 footnote points to a July 31 ROK memorandum seeking U.S. concurrence.
10. Tested whether a president-centered graph is adequate for d738: no; the source exposes prime-minister, defense-minister, and three service-chief action layers independent of presidential attendance.

## Cross-check bundles

- **Minister Kim identity**: FRUS d734 text + editorial footnote + recurrence in d737/d739/d741. Result: NARROWED to Kim Bop Rim, not VERIFIED.
- **Sohn identity/role**: FRUS d737 + d738 + FRUS XIV/2 d671 appointment footnote. Result: identity verified at source-family level; Korean official personnel record still wanted for registry normalization.
- **August 8 meeting provenance**: U.S. Office of Historian d741 + Korean History DB mirror. Result: independent archive-host provenance confirms the same FRUS record, but not an independent originating document.

## Concrete next leads

1. 국가기록원/관보: 손원일 국방부장관 1953-06-30 임명 발령 원문과 퇴임일 확인.
2. 국사편찬위원회 인물/관보 자료: 손원일 한자·생몰·국방장관 재임기간 정규화.
3. 국가기록원: 1953-08-05~08 한미상호방위조약 교섭 한국측 회의록/보고서 탐색.
4. 외교사료관: 변영태-김법린 조약 working party 문서 또는 초안 결재선 확인.
5. 관보/교육부 연혁: 1953-08 김법린 교육부장관 재임 여부를 날짜 단위로 확정.
6. 외교사료관: “Minister Kim”이 김법린임을 직접 적시하는 한국측 참석자 명단 탐색.
7. 국가기록원: 1953-07-31 Combined Economic Board MOU 한국어 원본/결재선 확보.
8. 외교사료관: telegram 121 from Seoul, 1953-08-03의 한국측 선행문서 식별.
9. 국방부 군사편찬연구소: 1953년 20개 사단 증강안 작성 주체와 결재선 확인.
10. 해군 기록: 박옥규가 제시한 해군 증강안 원문 및 손원일 전달관계 확인.
11. 공군 기록: 최용덕 명의 공군 증강안 원문 및 1953-08-06 회의 준비문서 확인.
12. 육군 기록: 백선엽과 20개 사단안의 제안/검토/승인 역할 분리.
13. 국회회의록: 1953년 상호방위조약 관련 정부 보고에서 변영태 발언 추적.
14. 국회회의록: 경제원조·환율 180:1·CEB 관련 백두진 보고/답변 추적.
15. 대통령기록/이승만 문서: 1953-08-05 조약 working party 지명 관련 메모 탐색.
16. 이승만 영문서한 DB: Dulles 방한 직전/직후 김법린·변영태 관련 서신 검색.
17. FRUS source file 795.00/8-553: Dulte 7 agenda 원문 회수 가능성 확인.
18. FRUS source file 895.00/8-353: 1953-07-31 ROK MOU 전문 원문 회수.
19. Department of State Bulletin 1953-08-17 pp.203-204: joint statement and draft treaty text 대조.
20. 미국 NARA RG59: lot 64 D 199의 원 memorandum에서 참가자 표기와 필기 수정 확인.
21. 한국사DB FRUS d734 mirror: footnote 번역/색인에서 Kim Bop Rim 표기 여부 확인.
22. 한국사DB FRUS d738 mirror: Paik/Sohn/Paek/Park/Choi 이름 정규화 대조.
23. 외교부 역대 주요인사: 조정환 1952-55 외무차관 재임기간 공식 확인.
24. 외교사료관: 조정환의 1953년 대미/정치회담 관련 전문 검색.
25. UN 기록: 임병직의 1953-08 이후 정치회담 관련 대표 활동 연결.
26. 외교사료관: 임병직-양유찬-변영태 사이 보고선과 지시선 구분.
27. 국가기록원: 백두진 국무총리실 경제원조 협의 문서 1953-08-06 전후 탐색.
28. 재무부/한국은행 사료: 군사환율 180:1 협상에서 백두진 외 재무 관료 역할 추적.
29. 국방부 장관실 기록: 손원일이 3군안을 단순 전달했는지 조정했는지 검증.
30. d742/d743의 후속 합의 이행사항을 d734–d741의 제안·결정·집행 단계와 연결.

## History debt
No full weekly history-debt review was due in this Tuesday run. Individual unresolved identities were narrowed without forcing RESOLVED. **역사부채 주간 전수조사 미실시.**
