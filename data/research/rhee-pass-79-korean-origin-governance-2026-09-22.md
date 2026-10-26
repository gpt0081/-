# Pass 79 — Korean-origin governance and actor provenance (2026-09-22)

## Scope
Follow-up to pass 78. The priority was to move beyond the FRUS mirror family into Korean-origin records and ordinary governance. Floot was not touched.

## Directly checked material
1. 국사편찬위원회 한국사DB, `dh_029_1953_07_08_0020`, 백두진 한미합동경제위원회 한국대표의 1953-07-08 경제문제 서한.
2. 국사편찬위원회 한국사DB, `le_005_3470`, 1953년 변영태의 한미상호방위조약 체결 관련 성명서 catalog/original-image record.
3. 국사편찬위원회 한국사DB, 이승만서한철 1953년 전체 목록, including Korean-origin actor/document leads.
4. 국가법령정보센터 1953 공포법령 목록, including 대통령령 제801호 한국유네스코위원회설치령, 법률 제293호 형법, 법률 제302호 한국산업은행법, 대통령령 제844호 해양경찰대편성령.
5. 한국민족문화대백과사전, 한미경제조정협정.
6. 한국민족문화대백과사전, 백-우드협약.
7. 한국민족문화대백과사전, 손원일.
8. 한국민족문화대백과사전, 변영태.
9. 한국민족문화대백과사전, 김법린.
10. 한국민족문화대백과사전, 백두진.
11. 한국민족문화대백과사전, 농지조사위원회.
12. 한국사DB FRUS `frus_009r_0020_0140`, 1953-08-07 제3차 이승만-덜레스 회담, used only as a source-family comparison, not independent provenance.

## Findings

### A. 백두진 is independently documented as an active Korean-side economic policy actor
The 1953-07-08 Korean History DB record reproduces a letter under 백두진's name and capacity as the Republic of Korea representative on the Combined Economic Board. He refers to the May 13 Rhee–Tasca–Paik meeting, presses a fixed 180 환/$ military exchange rate, a new aid program, and controls on hwan issuance, and warns that the Korean government is considering stopping hwan payments to UNC after August 15 absent written assurance. This is substantially stronger actor attribution than merely recording his attendance in U.S. minutes.

Attribution rule: encode 백두진 as **proposer/negotiator** for the positions in his July 8 letter, not as unilateral decider of the final bilateral exchange-rate settlement.

### B. 변영태 has a Korean-origin treaty statement object
`le_005_3470` is catalogued in the 이승만관계서한자료집 as a 1953 statement by 변영태 concerning conclusion of the Mutual Defense Treaty, with original images available. This supplies a Korean-origin document node separate from FRUS. The searchable metadata does not expose the statement body, so claims about its exact wording remain OPEN until the images/transcription are recovered.

### C. 김법린's cabinet identity gains an independent institutional anchor, but not yet a Korean participant list
The Korean encyclopedia records 김법린's 1952 appointment as 문교부장관. Separately, the 1953-07-06 대통령령 제801호 created the Korean UNESCO Commission under the Minister of Education. This strengthens the cabinet-composition premise behind the FRUS editorial identification. It still does **not** independently prove that the unnamed `Minister Kim` attended each Dulles meeting; that attribution remains NARROWED until a Korean-origin participant list is found.

### D. Ordinary governance expands beyond armistice diplomacy
The 1953 official-law list exposes several contemporaneous governance nodes that should be followed independently of the Dulles/treaty corpus: 형법 제정, 한국산업은행법, 한국유네스코위원회설치령, 해양경찰대편성령. These open legal/justice, industrial-finance, education/culture, and maritime-administration research lines.

### E. 백두진 economic network predates and outlasts the August diplomatic meetings
The Korean encyclopedia identifies 백두진 as Korean signatory to the 1952-05-24 Meyer Agreement and Korean CEB representative; it also identifies the 1953-12-14 Paik-Wood Agreement as centered on 백두진 and Tyler Wood. This supports treating his 1953 role as a continuous economic-governance node rather than a cabinet-attendance footnote.

## Adversarial checks
1. Does 백두진's July 8 letter prove the 180:1 rate became permanently agreed? No; the letter itself is advocacy amid dispute.
2. Does it prove 백두진 alone originated the 180:1 proposal? No; he references a May 13 Rhee–Tasca–Paik understanding and prior correspondence.
3. Does the letter prove an actual August 15 cutoff occurred? No; it records consideration/threat conditional on assurances.
4. Does `le_005_3470` prove the precise content of 변영태's treaty statement? No; searchable metadata establishes authorship/topic, not body text.
5. Does 김법린's confirmed ministerial status prove he is `Minister Kim` in FRUS? It strengthens but does not independently close the participant-identity question.
6. Does 대통령령 제801호 prove 김법린 personally drafted the UNESCO commission decree? No.
7. Does the 1953 law list prove presidential personal authorship of each law/decree? No; legal promulgation and policy authorship are separate relations.
8. Does the Meyer Agreement make 백두진 the sole architect of aid policy? No; bilateral and institutional actors must remain separate.
9. Does the Paik-Wood Agreement retroactively prove July positions were accepted? No; December settlement requires its own text-level comparison.
10. Can Korean History DB's FRUS translation be counted as independent provenance against U.S. FRUS? No; source-family independence remains disallowed.

## Actor consequences
- `pol-paik-too-chin` / 백두진: deepen as CEB Korean representative and Korean-side economic negotiator; add July 8 letter as reusable document lead.
- `pol-pyun-yung-tai` / 변영태: add Korean-origin treaty-statement document lead.
- `pol-kim-bop-rim` candidate: strengthen verified cabinet-role evidence while keeping Dulles-meeting identity NARROWED.
- 손원일: biographical Korean reference confirms the independent career node, but exact official appointment instrument remains a lead.

## Event/sub-event candidates
1. `evt-1953-0708-ceb-paik-letter` — 백두진 economic-policy letter to Bennett; proposed_by/negotiated_by 백두진; decision outcome open.
2. `evt-1953-0706-unesco-commission-decree` — 대통령령 제801호; legal authority and ministerial institutional relation separated from authorship.
3. `evt-1953-0918-criminal-code-enactment` — 형법 제293호, justice/legal governance lead.
4. `evt-1953-1230-kdb-act` — 한국산업은행법 제302호, industrial-finance governance lead.
5. `evt-1953-1214-maritime-police-organization` — 해양경찰대편성령 제844호, maritime/local-security administration lead.
6. `evt-1952-0524-meyer-agreement` — 백두진–Clarence Meyer bilateral economic coordination agreement, predecessor relation.
7. `evt-1953-1214-paik-wood-agreement` — 백두진–Tyler Wood economic reconstruction/stabilization agreement, successor relation.
8. `evt-1953-pyun-mutual-defense-statement` — exact date/body open; document existence/authorship/topic established.

## Concrete next lead queue
1. 한국사DB `le_005_3470` 원문이미지: 변영태 성명서 전문과 작성일 확인.
2. 국가기록원/관보: 손원일 1953-06-30 국방부장관 임명 발령 원문.
3. 국가기록원/관보: 김법린 문교부장관 임명·면직 발령과 1953-08 재임 경계.
4. 국회회의록 1953-07~10: 변영태의 상호방위조약 가조인/서명 정부보고.
5. 외교사료관: 1953-08-08 가조인 한국측 보고서와 결재선.
6. 한국사DB 이승만서한철: `한미상호방위조약 초안` 원문이미지 및 작성자 식별.
7. 한국사DB 이승만서한철: `한미상호방위조약 내용에 대한 이승만 코멘트` 원문이미지.
8. 한국사DB: 백두진 1953-05-11 UNKRA 정책 관련 서한 전문.
9. 한국사DB: 변영태 서리의 1953-06-10 Hanlon 답신 원문.
10. 한국사DB: 백두진 1953-05-19 Hanlon 서한 원문.
11. 한국사DB/국가기록원: 1953-05-13 이승만–Tasca–백두진 회동 한국측 기록.
12. 국가기록원/재무부: 180환/$ 군대환율 내부 검토·결재문서.
13. 한국은행 사료: 1953년 통화개혁의 기획·집행자별 문서.
14. 국회회의록: 1953년 환율·환 발행·UNC 현지비용 관련 백두진 답변.
15. 1953-07-31 CEB MOU 한국어 원본, 서명자와 결재자 확인.
16. 백-우드협약 1953-12-14 원문: July 8 positions와 조항별 대조.
17. 마이어협정 1952-05-24 원문: 백두진의 법적 협상 권한과 CEB 설치 조항 확인.
18. 국가법령정보센터: 대통령령 제801호 조문 전체와 개정/폐지 이력 보존.
19. 유네스코한국위원회 공식 연혁: 김법린 위원장 취임일과 준비위원회 구성.
20. 국회 1952-11-10 본회의: UNESCO 헌장 준수서약 표결과 발언자.
21. 형법 제293호 제정 과정: 정부안/국회 심의·법사위 주요 정치인 분해.
22. 한국산업은행법 제302호 제정 과정: 재무부·국회·산업정책 행위자 분해.
23. 해양경찰대편성령 제844호: 제안·집행 부처와 책임자 확인.
24. 농지조사위원회/임시토지수득세: 백두진 재무장관 시기 국회 발언과 집행 책임 분해.
25. 손원일 해군/국방부 사료: 1953년 3군 증강안 취합·전달·승인 관계.
26. 박옥규 해군 증강안 원문과 손원일 보고선.
27. 최용덕 공군 증강안 원문과 손원일 보고선.
28. 백선엽 육군 20개 사단안 원문과 작성/승인 관계.
29. 김법린 관련 외교사료관 조약 working-party 한국측 명단.
30. 1953-08-07/08 한국측 회의록: 김법린 참석 여부를 FRUS와 독립 검증.
31. 변영태 생애 공식 인사기록: 외무장관/총리 정확한 재임 경계.
32. 백두진 공식 인사기록: 재무장관·총리·CEB 대표 겸직 경계.
33. 손원일 공식 인사기록: 해군참모총장→국방장관 전환일과 군 신분 관계.
34. 1953년 형법 공포 관보 원문: 공포·시행 주체와 날짜 확정.
35. 1953년 산업은행법 공포 관보 원문: 법률안 제출 경로와 시행 준비 확인.
36. 1953년 해양경찰대편성령 관보 원문: 행정조직·지휘 관계 확인.

## History debt
Tuesday run. Weekly full review not due. No unresolved item was forced to RESOLVED. **역사부채 주간 전수조사 미실시.**
