# Pass 78 — Korean History DB mirror attribution cross-check (2026-09-22)

## Scope
Follow-up to pass 77. This pass tests U.S. FRUS-derived actor attribution against the National Institute of Korean History / Korean History Database's Korean-language FRUS presentation, with special attention to 김법린, 손원일, 백두진, and the August 8 treaty-initialing action. Floot was not touched.

## Directly checked documents
1. U.S. Department of State, FRUS XV/2 d734, 1953-08-05 first Rhee–Dulles meeting.
2. National Institute of Korean History, Korean History DB, `frus_009r_0020_0090`, Korean presentation of d734.
3. U.S. Department of State, FRUS XV/2 d738, 1953-08-06 Paik/Stevens aid-defense meeting.
4. National Institute of Korean History, Korean History DB, `frus_009r_0020_0130`, Korean presentation of d738.
5. U.S. Department of State, FRUS XV/2 d741, 1953-08-08 final meeting.
6. National Institute of Korean History, Korean History DB, `frus_009r_0020_0160`, Korean presentation of d741.
7. U.S. Department of State, FRUS XV/2 d792, 1953-11-04 Eisenhower letter recalling the August 8 agreement.
8. U.S. Department of State, FRUS XV/2 d797, annex reproducing excerpts from the August 8 political-conference understanding.

## Findings and attribution corrections

### 1. 김법린 remains probable, but Korean History DB adds a transparent editorial reason
The Korean History DB presentation of the 1953-08-06 meeting renders `Minister Kim` as `장관 김법린` and explicitly marks this as an editor/translator inference: the original says Minister Kim and 김법린 was the only cabinet minister with surname Kim at the time. This is useful corroborative editorial reasoning, but it is **not an independent Korean-origin participant list**. Therefore `cand-kim-bop-rim-dulles-1953` stays NARROWED/probable rather than VERIFIED.

### 2. 손원일 identity is now independently normalized across two official publication hosts
The U.S. FRUS d738 names `Defense Minister Son Won II`; Korean History DB's corresponding record normalizes this to `국방부장관 손원일`. The first-meeting Korean presentation likewise gives `국방부장관 손원일(Sohn)`. This removes practical transliteration ambiguity in the meeting corpus. It still does not substitute for a Korean personnel/appointment record for exact term boundaries and registry biographical fields.

### 3. August 8 has a distinct treaty-initialing action edge
FRUS d741 states that after the joint statement was signed, **Secretary Dulles and Foreign Minister Pyun** moved to the prepared dining room and each initialed and exchanged an original of the draft Mutual Defense Treaty, in the presence of the ROK Cabinet, the U.S. party, correspondents and photographers. This requires a separate sub-event from generic final-meeting attendance: `evt-1953-0808-mutual-defense-treaty-initialing`, with `executedBy = [John Foster Dulles, pol-pyun-yung-tai]`. Rhee was present but should not be encoded as the person who initialed the treaty draft.

### 4. August 8 political-conference understanding persisted as an operative reference
FRUS d792 (Eisenhower to Rhee, 1953-11-04) explicitly recalls Rhee's August 8 agreement with Dulles regarding keeping ROK forces under the United Nations Command pending expected treaty entry into force. FRUS d797 later reproduces excerpts from the August 8 understanding concerning concurrent withdrawal from the political conference after 90 days if both governments judged it fruitless/exploitative. This shows that the August 8 outcome was not merely ceremonial treaty initialing; it also formed a continuing political-security reference point. Exact Korean-side instrument/provenance remains an open lead.

## Adversarial checks
1. Could the Korean History DB rendering alone verify 김법린? No; its own note identifies the mapping as an inference from cabinet composition.
2. Could `Son Won II` be a different person from 손원일? The parallel official publication records normalize the same defense-minister participant to 손원일; transliteration ambiguity is effectively collapsed.
3. Did Rhee initial the draft Mutual Defense Treaty on August 8? No; d741 assigns initialing to Dulles and Pyun.
4. Was the August 8 final meeting only ceremonial? No; later U.S. documents cite an August 8 political/security understanding as operative.
5. Does the Korean History DB constitute an independent originating source for these facts? No; it is a separate official archive/presentation of the FRUS source family, so provenance independence must not be overstated.
6. Does d738 prove 손원일 authored the three service expansion programs? No; it says the Defense Minister summarized programs proposed by the three services.
7. Does d738 prove 백선엽 personally authored the 20-division request? No; attendance plus service-level proposal is insufficient for individual authorship.
8. Does d741 allow cabinet-wide attribution of treaty initialing? No; witnesses and executors are distinct relations.
9. Does later U.S. recollection prove the Korean internal approval chain for the August 8 understanding? No; Korean-origin cabinet/presidential records remain needed.
10. Does a mirror-host cross-check count as independent originating provenance? No; it is useful for normalization/editorial transparency, not source-family independence.

## Structured consequences
- Promote practical meeting-corpus identity confidence for 손원일, but retain the Korean official personnel-record lead before full biographical registry normalization.
- Keep 김법린 at NARROWED/probable-editorial.
- Add treaty-initialing sub-event with 변영태 as Korean executor/signatory-side actor.
- Add an `August 8 understanding persistence` research edge from d792/d797, without claiming a Korean internal approval chain.

## Next priority leads
1. 국가기록원/관보: 손원일 국방부장관 1953-06-30 임명 발령 원문.
2. 관보/교육부: 1953-08-05~08 김법린 재임 확인 및 정확한 장관 직함.
3. 외교사료관: 1953-08-08 한미상호방위조약 가조인 한국측 보고서·초안·결재선.
4. 대통령기록/이승만 문서: 1953-08-08 정치회담 90일 조항 및 UNC 지휘 관련 한국측 기록.
5. 국회회의록: 1953년 상호방위조약 가조인 직후 변영태의 정부 보고.
6. 국가기록원: 1953-07-31 CEB Memorandum of Understanding 한국어 원본과 결재자.
7. 국무총리실/경제조정 기록: 백두진의 180:1 환율안 내부 검토문서.
8. 국방부 군사편찬연구소: 20개 사단안 작성·검토·결재 주체 분해.
9. 해군 사료: 박옥규 명의 1953년 증강안 원문.
10. 공군 사료: 최용덕 명의 1953년 증강안 원문.
11. 외교사료관: 변영태·김법린 조약 working-party 한국측 참석자 명단.
12. 한국사DB 이승만서한철: 1953-08-08 전후 Dulles/변영태/손원일 관련 서한.
13. FRUS source file 895.00/8-353: 1953-07-31 ROK MOU 전문.
14. NARA RG59 lot 64 D 199: d741 원 비망록의 참가자·수정 흔적.
15. Department of State Bulletin 1953-08-17 pp.203-204: 발행된 공동성명/조약초안과 d740/d741 협상문구 대조.
16. 외교부 역대 인사: 조정환 공식 재임기간과 1953년 직위.
17. UN records: 임병직의 정치회담 대표활동과 서울 지시선.
18. 국회회의록: CEB·180:1 환율·미군/UN군 현지비용 부담에 관한 백두진 답변.
19. 한국은행/재무부 사료: 군사환율 180:1 정책의 국내 제안자와 협상권한.
20. 대통령기록: 3군 증강안에 대한 이승만 승인/지시 문서 존재 여부.
21. 국방부 장관실: 손원일이 3군안을 취합·조정했는지 단순 전달했는지 확인.
22. 육군본부: 백선엽과 20개 사단안의 작성/승인 관계.
23. 해군본부: 손원일-박옥규 사이 증강안 보고선.
24. 공군본부: 손원일-최용덕 사이 증강안 보고선.
25. 외교사료관: 8월 8일 가조인 직후 미국측과 교환한 한국 외무부 전문.
26. 국회 비준자료: 1953년 조약 비준 논의에서 가조인 주체와 정부 설명 대조.
27. d792의 `August eighth agreement`가 지칭하는 한국측 문서 묶음 식별.
28. d797 annex의 August 8 understanding 원문과 공동성명 간 문언 차이 대조.
29. 1953-08 이후 NSC 문서에서 변영태/백두진/손원일의 독립 행위자 언급 추적.
30. 한국측 회고록은 원문 단서로만 사용해 위 1차 기록의 문서번호·날짜를 역추적.

## History debt
No weekly full review was due on this Tuesday run. 김법린 identity and Korean internal approval chains remain explicitly unresolved. **역사부채 주간 전수조사 미실시.**
