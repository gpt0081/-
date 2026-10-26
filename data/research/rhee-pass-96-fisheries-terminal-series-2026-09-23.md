# Rhee research pass 96 — 제2차 한일회담 어업위원회 terminal-series control

Date: 2026-09-23
Scope: Pass 95에서 M01~M10까지 고정한 제2차 한일회담 어업위원회 series control을 M11~M13 및 협정안 교환 문서군까지 확장한다. Floot는 건드리지 않는다.

## Directly inspected source set

1. 국사편찬위원회 한국사연구휘보 『한국외교문서 예비회담~제3차 한일회담』 상세 목차: 제2차 회담 어업위원회가 1953-05-06~07-23 범위이며 M10 p.977, M11 p.980, 일본 국내규제 설명서 p.984, M12 p.989, M13 p.993 순으로 수록됨을 직접 확인. https://db.history.go.kr/id/hb_194_01_001049
2. 대한민국 국회도서관 동일 자료총서 소장 목차: 위 terminal sequence와 페이지를 독립 bibliographic 계열로 교차확인. https://dl.nanet.go.kr/PrintText.do?cn=MONO12021000043830&pId=TOC
3. 동북아역사넷 제2차 한일회담 어업위원회 공식 catalogue `kj.d_0003_0040`: M04~M10의 meeting/report chronology 및 M09 일본측 협정요강을 재확인. 이번 접근에서는 원문 endpoint가 502를 반환하여 M11~M13 metadata를 추정하지 않음. https://contents.nahf.or.kr/item/level.do?levelId=kj.d_0003_0040
4. 동북아역사넷 후대 공식 편철 `kj.d_0011_0080`: 1953-06-29 일본측 어업협정 요강, 1953-07-17 대한민국 한일어업조약요강, 1953-07-23 일본측 제4항 설명의 존재와 날짜를 확인. https://contents.nahf.or.kr/id/NAHF.kj.d_0011_0080
5. 동북아역사넷 제1차 한일회담 어업위원회 catalogue `kj.d_0002_0050`: 1952년 15회 어업위원회와 1953-05-01 한일어업회담요지의 존재를 비교 series로 확인. https://contents.nahf.or.kr/item/level.do?levelId=kj.d_0002_0050
6. 한국학중앙연구원 한국민족문화대백과 `평화선`: 1952년 해양주권선의 정책 배경을 2차 설명으로 점검. https://encykorea.aks.ac.kr/Article/E0060099
7. U.S. Library of Congress, *The History and Law of the Republic of Korea*: 1952-01-18 proclamation을 State Council Notice No.14로 지칭하는 외국 법률자료를 adversarial provenance로 확인. https://tile.loc.gov/storage-services/service/ll/llglrdppub/2019668512/2019668512.pdf
8. CIA Reading Room, Central Intelligence Bulletin 1961-02-13: Rhee Line과 한일 어업분쟁에 대한 후대 미국 정보기관 관찰을 별도 provenance로 확인. https://www.cia.gov/readingroom/docs/CENTRAL%20INTELLIGENCE%20BULL%5B15815741%5D.pdf

## Material findings

### 1. M11~M13 bibliographic existence and order are now independently fixed
NIKH and National Assembly Library both reproduce the 2021 NAHF documentary edition with the same terminal order: M11 report → Japanese domestic regulation explanatory document → M12 report → M13 report. This proves existence/order at bibliography level, but does **not** establish meeting dates, report dates, document numbers, participants, speakers, or proposal authorship. Those fields remain OPEN until the underlying diplomatic documents are opened.

### 2. 1953-07-17 Korean proposal is a distinct document object
The later official compilation preserves `한일어업조약요강(대한민국안)` dated 1953-07-17 separately from the 1953-06-29 Japanese outline and 1953-07-23 Japanese explanation. Therefore the Korean proposal should be modeled as a reusable document object linked to the terminal negotiation sequence, not collapsed into an inferred M12/M13 statement. Drafter, proposer, approver and presenter remain OPEN.

### 3. 1953-07-23 Japanese explanation is specifically tied to the Japanese outline's article 4
The official compilation labels it `일측 요강 제4항에 관한 일측의 설명`. This narrows the next comparison task: align the 06-29 Japanese outline article 4, the 07-17 Korean outline, and the 07-23 explanation clause-by-clause before assigning negotiating actions to individual actors.

### 4. Series boundary guardrail
The documentary edition defines the second-talk fisheries committee corpus as 1953-05-06~07-23. This is a useful series boundary, but it must not be converted into an assertion that M13 necessarily occurred on 07-23 without opening the M13 record. The 07-23 date is independently attached to the Japanese explanation document, not yet to M13 in this pass.

## Adversarial checks

1. Two bibliographic catalogues repeating one documentary edition are independent access/provenance paths but not two independent eyewitness records.
2. M11/M12/M13 page order does not prove their meeting dates.
3. The 07-17 Korean outline date does not prove M12 occurred on 07-17.
4. The 07-23 Japanese explanation date does not prove M13 occurred on 07-23.
5. A later 1960s file preserving a 1953 attachment is not silently treated as the original 1953 file provenance.
6. The Korean proposal is not attributed to 지철근, 홍진기, 장윤걸, 조정환, 변영태 or 이승만 without a signature/routing/meeting record.
7. Foreign later summaries of the Peace Line are contextual/adversarial evidence, not proof of domestic drafting authorship.
8. State Council Notice No.14 citation in a foreign legal study is a concrete archival lead, not yet a substitute for opening the Korean notice itself.
9. The committee series is separated from presidential decision authority; attendance and technical expertise do not establish final approval.
10. NAHF 502 access failure is recorded as an access block rather than filled with guessed metadata.

## Cross-check bundles

1. Terminal-series bibliography: NIKH ↔ National Assembly Library ↔ NAHF catalogue family.
2. Proposal sequence: NAHF second-talk series ↔ NAHF later official compilation preserving 06-29 / 07-17 / 07-23 documents.
3. Peace Line provenance lead: Korean encyclopedia context ↔ U.S. Library of Congress legal history ↔ CIA retrospective observation, used only to generate/pressure-test primary-source targets.

## Open/history-debt lines narrowed

- M11~M13 existence/order: NARROWED to exact documentary-edition pages 980/989/993.
- Japanese domestic-regulation explanation: NARROWED to p.984 between M11 and M12 in documentary edition.
- 1953-07-17 Korean outline: NARROWED to a distinct official document object; authorship remains OPEN.
- 1953-07-23 Japanese explanation: NARROWED to article-4 explanation of Japanese outline; presenter/meeting linkage remains OPEN.
- M11~M13 exact dates/document numbers: BLOCKED_THIS_PASS by NAHF 502 and absent indexed detail; no inferred values entered.
- Peace Line domestic legal instrument: NARROWED by LoC citation to `State Council Notice No. 14, 1952-01-18`; Korean original still required.
- Peace Line drafting authorship: remains OPEN; secondary claim that 지철근 '주도' is not promoted without primary corroboration.
- M03 report-date anomaly from Pass 95 remains CONFLICTED; this pass found no original cover/dispatch image.

## Next lead queue

1. NAHF `kj.d_0003_0040` continuation: open M11 report and capture meeting date, report date, document number, roster.
2. Same file: open p-equivalent M12 report and capture exact metadata.
3. Same file: open M13 report and capture exact metadata.
4. M11: distinguish Korean/Japanese delegates, observers, recorders and speakers.
5. M12: identify who physically presented the Korean 1953-07-17 outline.
6. M13: test whether 1953-07-23 Japanese article-4 explanation was delivered in-session.
7. Open original 1953-06-29 Japanese outline and transcribe article 4 only.
8. Open original 1953-07-17 Korean outline and capture header, routing, signatures/stamps.
9. Open original 1953-07-23 Japanese explanation and capture author/presenter metadata.
10. Build clause-level diff of 06-29 Japanese and 07-17 Korean outlines.
11. Link clause-level positions to speakers only where transcript supports attribution.
12. Recover M03 original cover to resolve 05-15/05-20 conflict.
13. Open M05 transcript and extract roster/actions.
14. Open M07 transcript and extract roster/actions.
15. Open M10 transcript and extract roster/actions.
16. Search diplomatic personnel records for 장윤걸 appointment/term.
17. Search Gazette/personnel records for 홍진기 법무국장 appointment/term.
18. Search Commerce and Industry personnel records for 지철근 수산국장 appointment/term.
19. Recover `State Council Notice No.14` Korean original dated 1952-01-18.
20. Compare Notice No.14 wording with Presidential Proclamation text.
21. Recover cabinet agenda/minutes immediately preceding 1952-01-18 proclamation.
22. Identify who submitted the maritime-sovereignty agenda to cabinet.
23. Identify legal review chain for proclamation wording.
24. Test 지철근 drafting-role claim against cabinet/commerce-ministry records.
25. Search Japanese MOFA contemporaneous records for Korean domestic attribution.
26. Search FRUS Jan-Feb 1952 for U.S. embassy attribution of drafting/approval chain.
27. Open 1952 M01 transcript and normalize actor/action schema.
28. Continue 1952 M02-M05 rosters.
29. Continue 1952 M06-M10 rosters.
30. Continue 1952 M11-M15 rosters.
31. Trace 1952-04-21 Korean fisheries proposal drafting chain.
32. Compare 1952 proposal clauses with 1953-07-17 Korean outline.
33. Identify 조정환's exact supervisory role as vice foreign minister in 1953 routing records.
34. Identify 변영태's ministerial approval/signature appearances in terminal fisheries documents.
35. Separate 주일대표부 reporting chain from Seoul ministry approval chain.
36. Add stable organization IDs for 외무부/주일대표부/상공부 수산국/법무부 법무국 if registry migration permits.
37. Promote candidate actors only after identity and office-term cross-check.
38. Search 1953 cabinet minutes for fisheries-negotiation directives.
39. Search presidential papers for direct instructions on the 07-17 Korean outline.
40. Reconcile all terminal-series dates against 2021 documentary edition page images when archive access recovers.

**역사부채 주간 전수조사 미실시.**