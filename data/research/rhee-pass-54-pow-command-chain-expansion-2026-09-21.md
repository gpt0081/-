# Rhee Pass 54 — 반공포로 석방 지휘선·수용소·정전 대응 확장

Date: 2026-09-21
Scope: Pass 53의 `lead-1953-pow-execution-chain` 후속. Floot 수정·빌드 없음.

## 핵심 진전
Pass 53의 가장 중요한 미해결점은 `이승만 -> 원용덕 -> 수용소 경비병` 사이의 실제 지휘선이었다. 이번 회차는 FRUS 연속문서와 한국학중앙연구원 항목을 다시 대조하여 다음을 더 단단히 고정한다.

1. 이승만은 6월18일 Clark에게 자신이 **Korean military police**에 즉시 석방을 명령했다고 직접 서술했다(FRUS XV/2 doc.607). 따라서 집행기관을 단순히 `ROK Army`라고 뭉뚱그리지 않고 헌병/군사경찰 계통으로 모델링해야 한다.
2. Clark의 6월19일 전문(doc.612)은 원용덕 Provost Marshal이 대통령에게 직접 종속되어 육군참모총장 백선엽과 별도의 명령을 내렸다고 관찰한다. 잔여 포로를 지키는 미군을 공격하라는 원용덕 명령도 이 문서에 보고되지만 한국측 원 명령서는 아직 없다.
3. Briggs의 같은 날 면담(doc.616)에서 변영태는 해당 병력이 `Provost Marshal General` 아래 있으며 그 지휘관은 대통령 외 누구의 명령도 받지 않는다고 한국정부 입장을 설명했다. 이는 미국측 군사정보와 한국정부 당사자 설명이라는 서로 다른 contemporaneous provenance가 같은 구조를 가리킨다.
4. 6월19일 미국군이 잔여 약 9,400명을 8개 mainland camp에서 직접 경비하게 되면서, 사건은 `석방`에서 `UNC 재통제와 한미 무력충돌 위험`으로 전환되었다(doc.613-614).
5. 이승만 공개성명은 각 도지사와 경찰에게 석방자를 돌보도록 지시했다고 명시한다. 즉 사건 graph에는 대통령-헌병 실행선과 별개로 `대통령 -> 지방행정/경찰 -> 석방자 보호` 후속선이 필요하다.
6. 6월26일 Robertson 회담(doc.639)은 이승만, 백두진, 변영태, 신태영, 손원일을 하나의 공식 협상 노드로 묶고, 잔여 포로·정치회담·경제원조/20개 사단·상호방위조약을 패키지로 확인한다.
7. Dulles의 6월22일 지침(doc.626)은 상호방위조약·약 3억달러 경제원조·정치회담을 이미 Robertson 임무의 세 축으로 제시했다. 따라서 `6/18 석방 하나가 조약을 만들어냈다`는 단일인과 서술은 계속 금지한다.

## 이번 회차 직접 확인 문서
Pass 53과 중복 여부를 분리하기 위해 이번 목록은 이번 회차에 실제 다시 열어 검토한 문서이며, 실행 통계의 신규 고유문서 수에는 Pass 53에서 이미 열었던 문서를 제외한다.

### FRUS / 미 국무부 공식 원문
- docs.606-615: 석방 발생, 이승만 서한/성명, NSC 반응, 백두진-덜레스 회담, Clark의 현장통제 전문.
- docs.616-625: Briggs-Rhee/Pyun 면담, 잔여포로 재통제, 추가 충돌 위험, Clark-Rhee 접촉과 후속 대응.
- docs.626-636: Robertson 임무 지침, 상호방위조약/경제원조/정치회담, 잔여포로 처리와 NSC 정책 검토.
- docs.637-646: NSC 157, Robertson 협상, Rhee의 4개 조건, 미국의 회신과 정전 복구 협상.

### 한국/국제 공식·공공 원문 및 보조
- 한국민족문화대백과 `반공포로 석방`: 6월6일 원용덕에게 계획 수립 지시, 8개 수용소, 35,698명 중 27,388명 탈출이라는 공공 2차 종합. 1차 명령문 표적 생성에만 사용.
- UN Security Council S/3043 (1953-06-26): UNC communiques 1651, 1653, 1654, 1655의 유엔 제출본. 후속 현장상황을 독립 국제기구 provenance로 대조하는 표적.
- FRUS doc.611의 한국사DB mirror(`frus_009_0010_0300`)도 확인하여 문서번호 695A.0024/6-1853과 참가자 백두진·양유찬을 교차확인.

## event/sub-event 구조화
### evt-1953-0618-pow-military-police-order
- decided_by: `pol-rhee-syngman`
- executed_through: `pol-won-yong-duk` / Korean military police chain
- evidence: FRUS 607, 612, 616
- status: STRONG, 단 수용소별 서면명령은 OPEN

### evt-1953-0618-provincial-protection-order
- decided_by: `pol-rhee-syngman`
- executed_by: provincial governors + police officers (개별 인물 미확인)
- evidence: FRUS 607 press release
- open: 1953-06-18 내무부/도경 지시문과 수신 도지사 명단

### evt-1953-0619-unc-camp-takeover
- decided/executed_by: UNC/Clark-Herren chain
- opposed_or_threatened_by: Won Yong Duk command as reported by Herren
- observed_by: Clark, Murphy
- result: 약 9,400 잔여포로를 8개 mainland camps에서 미군이 직접 경비

### evt-1953-0619-us-rok-force-confrontation-risk
- trigger: 잔여포로 추가석방 시도
- observed_by: Clark/Murphy
- evidence: FRUS 612-614
- status: VERIFIED as contemporaneous U.S. assessment; 실제 교전 발생 여부 별도 lead

### evt-1953-0622-robertson-mission-design
- proposed_by: Dulles/Eisenhower administration
- package: mutual defense treaty + economic assistance + political conference strategy
- evidence: FRUS 626-628

### evt-1953-0625-nsc157-korea-objectives
- observed/decided_by: U.S. NSC Planning Board
- significance: 정전 후 분단 지속/중립통일 대안과 ROK의 통일 요구를 별도 정책축으로 분석
- evidence: FRUS 637

### evt-1953-0626-robertson-rhee-expanded-meeting
- ROK participants: Rhee, Paek Tu Chin, Pyun Yung Tai, Shin Tai-Yong, Sohn Won Il
- U.S. participants: Robertson, Briggs
- package: 잔여 8,600 포로, 정치회담 90일, 경제원조+20개 사단, 상호방위조약
- evidence: FRUS 639

### evt-1953-0626-us-response-four-points
- decided_by: Eisenhower/Dulles side
- result: 포로 이전·군사/경제 지원·조약 방향 수용, 정치회담 90일 자동종료 조건은 수정
- evidence: FRUS 640

## 비대통령 actor 심화
- `pol-won-yong-duk`: VERIFIED_CANDIDATE 유지. 지휘선은 크게 좁혀졌으나 한국측 원 명령서가 없어 registry 정식승격 전 마지막 핵심 debt가 남음.
- `pol-pyun-yung-tai`: 6/19 Briggs 면담에서 헌병총사령관의 대통령 직속성을 직접 설명한 당사자로 evidence 강화.
- `pol-paik-sun-yup`: 육군참모총장과 원용덕 별도선의 대비가 doc.612에서 명확. 군 지휘구조 검증 actor로 심화.
- `pol-paek-tu-chin`: 6/18 워싱턴 Dulles 회담과 6/26 서울 확대회담 양쪽에 연결되어 외교-내각 bridge actor로 심화.
- `pol-yang-you-chan`: 6/18 워싱턴 회담 참가자. 주미대사관 전문 추적 필요.
- `pol-shin-tai-yong`: 6/26 확대회담 참가 및 국방정책 actor. 6/18 사전인지 여부는 OPEN.
- `pol-sohn-won-yil`: 6/26 확대회담 참가. 당시 해군참모총장 직책은 FRUS로 확인, 국방장관 취임일은 별도 공식 인사기록 표적.
- `pol-chin-hon-shik`: 이승만의 도지사·경찰 보호지시를 실제 내무행정으로 전달했는지 아직 직접증거 없음. OPEN 유지.
- `pol-choi-duk-shin`: 한국측 정전회담 대표로 새 후보. 6월8일 포로송환협정 전후 한국대표단 철수/보이콧의 정확한 명령선과 문서 확보 필요.
- `pol-hwang-ho-hyon`: 1953년 9월 진헌식 후임 내무장관 서리로 확인되는 후속 내무행정 actor. 반공포로 직접 관여 증거는 없어 별도 시계열 노드 후보로만 보존.

## adversarial checks
1. 대통령 직접명령 부정 가능성: Rhee 자신의 Clark 서한이 military police에 명령했다고 명시하여 크게 약화.
2. 일반 육군 지휘계통 집행설: Paik 참모총장과 Won의 별도선이 doc.612에서 구분되어 반박됨.
3. 원용덕 독단설: Pyun의 contemporaneous 설명과 Rhee 서한이 대통령 지시선을 지지하여 약화.
4. 미국 묵인설: NSC·Clark·Murphy 문서는 통제 회복과 충돌 우려를 기록. 단 사전정보 실패 원인은 별도 조사.
5. 6/18 단발사건설: 6/19 추가탈출·재통제, 6/22 이후 협상으로 반박.
6. 모든 비송환 포로 석방설: 8개 수용소에 약 9,400 잔류 기록으로 반박.
7. 한국정부 전체 동일역할설: 대통령/헌병/외무/총리/국방/지방경찰 역할이 분리됨.
8. 상호방위조약 단일인과설: 6/6 offer와 6/22 Robertson 지침이 선행하므로 보류.
9. 20개 사단 요구가 석방 당일 즉흥적으로 생겼다는 설명: 6/26 협상 패키지로는 확인되지만 기원은 이전 군증강 협상 추적 필요.
10. 지방경찰이 석방 자체를 집행했다는 설명: 현재 확보된 1차자료는 군사경찰 집행과 지방경찰의 사후 보호지시를 구분하므로 혼동 금지.

## open lead 추적 상태
- `lead-1953-pow-execution-chain`: NARROWED. 대통령→헌병총사령관/군사경찰까지는 강하게 좁혀짐. 수용소별 한국군 지휘관/명령번호는 OPEN.
- `lead-1953-pow-provincial-protection`: OPEN. 도지사·경찰 수신 원문 필요.
- `lead-1953-pow-defense-ministry-awareness`: OPEN. 신태영/국방부 사전인지·법적 지휘관계 미확인.
- `lead-1953-pow-army-chief-response`: NARROWED. Clark/Herren가 Paik에게 통보한 사실은 확인, 한국측 회신 미확인.
- `lead-1953-pow-mutual-defense-causality`: NARROWED. 조약 offer 선행 사실 때문에 단일인과 배제.
- `lead-1953-pow-camp-count`: NARROWED. FRUS는 8 mainland camps의 잔여포로를 명시, 6/18 실제 탈출 camp별 숫자는 추가 표 필요.
- `lead-1953-pow-casualties`: OPEN. FRUS의 30 killed/107 injured 초기보고와 후속 확정치를 교차해야 함.
- `lead-1953-pow-forced-enlistment`: OPEN. 공산측 주장·후대 연구는 있으나 한국군 인사/병적 원문 검증 필요.

## 다음 회차 concrete lead queue
1. NARA/Matthews files lot 53 D 413의 CX 63138 원문으로 camp별 최초 보고를 확보한다.
2. 같은 lot의 CX 63170 부속/원문에서 Herren의 Won 명령 정보 출처를 추적한다.
3. 한국 국방부/군사편찬연구소에서 1953-06-06 원용덕 계획수립 지시의 인용 원전을 역추적한다.
4. 헌병총사령부 1953년 6월 작전일지·명령철 소장 여부를 국가기록원에서 확인한다.
5. 부산 수용소의 한국군 경비부대와 지휘관 명단을 미8군 POW command 기록에서 찾는다.
6. 마산 수용소 경비부대/지휘관과 6/18 명령 수신시각을 찾는다.
7. 논산 수용소 경비부대/지휘관과 탈출 숫자를 찾는다.
8. 상무대/광주 수용소 경비부대/지휘관과 탈출 숫자를 찾는다.
9. 대구/가야리/거제리 명칭이 1953 공식 camp number와 어떻게 대응하는지 표준화한다.
10. FRUS가 말한 8 mainland camps의 camp number·위치를 모두 매핑한다.
11. 원용덕 회고/재판기록에서 반공포로 석방 명령 경위를 찾는다.
12. 백선엽 회고록의 1953-06-18~19 대목을 원문으로 열어 Clark 보고와 대조한다.
13. 신태영 국방장관의 6월 국방부 문서/성명에서 석방 사전인지 흔적을 찾는다.
14. 진헌식 내무장관 명의 6/18~20 경찰·도지사 지시문을 관보/국가기록원에서 찾는다.
15. 서울·경기·충남·전남·경남 도지사/경찰국장 인물명을 1953 인사기록에서 확정한다.
16. 석방포로 보호·숙식·교통 지원의 지방별 집행보고를 찾는다.
17. 6/20 국무회의 구호 결의의 국무회의록 원문과 참석자 명단을 확보한다.
18. 구호비 1인당 액수·광목·양곡 지급의 예산 근거와 재무부 집행문서를 찾는다.
19. 무료진료를 담당한 보건부/병원 지침과 책임 장관을 찾는다.
20. 직업알선을 담당한 사회부/노동행정 지침과 책임자를 찾는다.
21. 양유찬 주미대사의 6/18~20 서울 보고 전문을 외교사료에서 찾는다.
22. 백두진 귀국 후 이승만에게 정전 수용을 건의했는지 국무회의/회고 원문으로 검증한다.
23. 변영태 6/18 Clark 서한 Department of State Bulletin p.906 원문을 document registry에 독립 등록한다.
24. Clark 6/18 Rhee 서한 Bulletin p.907과 FRUS editorial note의 날짜 차이를 정리한다.
25. 최덕신 한국 정전회담 대표의 6/8 전후 철수/보이콧 명령 원문을 찾는다.
26. 6/18 국회 반응과 정전반대 결의/발언자를 국회 속기록에서 추출한다.
27. 6/18~20 각 정당 지도부의 공개성명과 실제 조직행동을 정당자료/신문에서 분리한다.
28. UN S/3043의 communiques 1651/1653/1654/1655를 각각 event graph에 매핑한다.
29. 공산측 Kim Il Sung/Peng Teh-huai의 Clark 서한을 UN/중국 공식 원문 계열로 확보해 adversarial evidence로 등록한다.
30. 포로 30명 사망·107명 부상 초기보고의 후속 확정 casualty table을 UNC 문서에서 찾는다.
31. 27,388/27,111/약25,000 등 상이한 석방 숫자의 집계시각·범위를 문서별로 분해한다.
32. 잔여 9,000/9,400/8,600 수치 차이도 날짜별 snapshot으로 정규화한다.
33. 강제입대 의혹을 병적기록·국방부 편찬사·포로 구술로 삼각검증한다.
34. 석방자 중 민간 정착·경찰 보호·군입대 비율을 확인할 통계 원문을 찾는다.
35. 6/19 실제 미군-ROK 발포/교전 사례가 있었는지 Eighth Army situation report로 검증한다.
36. 원용덕의 `attack US forces` 명령이 구두/서면 어느 형태였는지 Herren source chain을 역추적한다.
37. 6/6 상호방위조약 offer의 정확한 문구와 6/18 이전 한국측 반응을 별도 claim으로 등록한다.
38. 20개 사단 증강 요구의 최초 제안일을 1952~53 한미 군사협상에서 찾는다.
39. Tasca 경제원조 보고서와 반공포로 석방 이전 작성분을 비교해 경제원조 인과를 분리한다.
40. Robertson mission 이후 7월 정전 수용까지 ROK cabinet actor들의 입장 변화 시계열을 만든다.
