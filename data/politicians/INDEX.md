# 정치인 registry 확장 인덱스

- 기본 registry: `data/politicians.json` (기존 API 호환 유지)
- 2026-10-08 토지행정·제헌국회 독립 인물 12명: `data/politicians/run81-land-actors.json`
- 원문 기반 후보 상세: `data/research/candidates/run81-land-policy-actor-network.json`
- 안재홍 독립 실록: `data/annals/ahn-jae-hong.md`, 증거: `data/evidence/ahn-jae-hong.json`
- 신규 event/action: `data/events/run81-land-legal-actions.json`

조회 시 base와 overlay를 stable ID로 결합한다. 기존 ID를 삭제하거나 자동으로 덮어쓰지 않는다. `pol-lee-beom-seok-1900`과 `pol-lee-beom-seok`은 동일인 중복 의심이며 canonical은 후자로 제안하되 참조 전수조사 전 병합하지 않는다.


## 2026-10-08 · 제헌국회 식량법 의사절차 후보 10명 (run93)

`data/politicians/run93-grain-debate-candidates.json`: 공식 제헌국회 속기록 전사본의 실명·한자·의사행위에 근거한 독립 candidate ID 10명. 생몰·당적·지역구·동명이인 검증 전에는 정식 `data/politicians.json` 승격을 보류한다. 83:8은 철회안이 아니라 토론종결동의다.

## 2026-10-08 · 박상영 식량법 개정안 후보 (run95)
`data/politicians/run95-grain-actors.json`의 `pol-park-sang-yeong`은 1949-10-31·11-05 식량법 수정안 대표발의자 후보. 국사편찬위원회 헌정사 해제에 근거하며 국회 원속기록·생몰·한자·당선자원부 미대조. 후보 evidence/annals 별도 보존, 정식 승격 보류.

## 2026-10-08 · 교육법·계엄법 독립 후보 (run95 domain expansion)
`data/politicians/run95-domains-candidates.json`: 정광호(鄭光好)·김장열(金長烈)은 1949-10-25 제헌국회 제5회 제23차 계엄법 제2독회 원속기록의 서로 다른 수정안 발의자로 확인. 박희병(교육법 절충안)·안호상(문교부 초안)은 한국학중앙연구원 해제 단계의 후보로 등록. 네 명 모두 생몰·지역구·원면 보강 전 정식 registry 승격 보류.

## 2026-10-08 · 제헌국회 지방자치·귀속재산·사법·보안 입법 (run95)
원속기록으로 나용균·김수선·이주형·서성달·조헌영·김익로 6명을 독립 후보(`data/politicians/run95-legislative-candidates.json`)로 식별. 한자 표기는 해당 속기록 표기, 생몰·선거구·정당은 미검증. 1949-11-17 조헌영의 위원장 대리 낭독을 수정안 직접 발의로 오인하지 않는다.

## 2026-10-08 · 조병옥 유엔대표 (run95 FRUS)
`data/politicians/run95-frus-actors.json`의 `pol-cho-pyeong-ok`: 1949-05-16 이승만 공보실 정정문에 언급된 유엔대표. 방위협정 제안은 이승만의 전언으로 기록하며 조병옥 본인 발언 원문 확인 전 확정하지 않는다.

- 2026-10-08 임병직 독립 실록 승격: `data/annals/lim-byong-jik.md`, `data/evidence/lim-byong-jik.json`, 연계 `data/events/run96-uncok-nsc-limb.json` (UN 서한 원본은 미확보).


## Run97 · 1949년 인사·1950년 선거위원 후보
- `data/politicians/run97-1949-governance-candidates.json`: 후보 18명, 생몰·공직 원부 미검증.
- `data/annals/noh-jin-seol.md`: 노진설 독립 annals (초기).
- 최용덕·임병직·신성모·이범석은 기존 정식 ID에 새 증거만 연결, 중복 후보 없음.


## 2026-10-09 · run110d/e candidates
- `data/politicians/run110-1950-administrative-actors.json`: 4 existing actors, 6 new provisional candidates.
- `data/politicians/run110e-1950-political-actors.json`: 17 provisional candidates. No verified promotion yet.

## 2026-10-09 run111 중앙은행 정치인 실록 보강

- data/politicians/run111-bank-actors-a.json: 김도연·최순주 기존 ID와 관련 공직·사건·문서.
- data/politicians/run111-bank-actors-b.json: 구용서 기존 ID 보강.
- data/annals/kim-do-yeon-run111.md: 김도연 독립 실록.
- 원공한·원임명장 미확보로 신규 VERIFIED 승격 없음.

## Run113 (2026-10-09)

See `data/politicians/run113-prewar-network.json` for 12 sourced profiles. No canonical promotion before identity verification.

## Run113 extension · 1950-03-11 제헌국회 원속기록

`data/politicians/run113-assembly-19500311-actors.json`의 윤치영(尹致暎)·주기용(朱基瑢)·이주형(李周衡)·유성갑(柳聖甲)·서정희(徐廷禧)는 국회 원속기록의 의사행위로 식별. 윤치영은 `data/annals/yun-chi-yeong-run113.md` 독립 실록을 시험 개설하고 ANNALS_ACTIVE 후보로 관리한다. 생몰·선거구·당적 원부 확인 전 canonical 승격하지 않는다.

## Run118 (2026-10-09): 1950 미국 원조·내무행정 인물 연결

- `data/politicians/run118-us-aid-actors-a.json`: 장면·백성욱·김교석·김태선·김성수.
- `data/politicians/run118-us-aid-actors-b.json`: 신익희·이종린·조병옥.
- `data/politicians/run118-us-aid-actors-c.json`: 이범석·신성모.
- `data/annals/chang-myon-run118.md`: 장면 독립 실록.
- `data/annals/baek-seong-uk-run118.md`: 백성욱 독립 실록.
- 공식 한국 관보 신원 확인 전 신규 canonical 승격은 보류. 기존 canonical ID가 있는 조병옥·이범석·신성모를 재사용.

### Run118 Korean source correction

- `data/politicians/run118-identity-corrections.json`: FRUS Kim Kyo Suk의 김교석 후보 표기를 김효석(金孝錫) 동일인 가능성으로 정정. 기존 표기 및 검증 이력 보존.
- `data/annals/kim-tae-seon-run118.md`: 김태선(金泰善) 독립 실록. 한국학중앙연구원·서울경찰청·FRUS를 교차검증.
- 신규 정식 registry 승격은 임명 관보 확인 전 보류.

## Run120 (2026-10-09): 1950년 6월 제도·정당·노동 정치인

- `data/politicians/run120-june1950-actor-overlays.json`: 동시대 자료에 역할·한자·행위가 등장한 14명 기존 ID 재사용/후보 연결. 한글·한자·로마자 동명이인 주의.
- `data/annals/kim-seong-su-run120.md` 및 `data/evidence/politicians/kim-seong-su-run120.json`: 김성수 정당 지도부의 1950-06-07 발언과 공식 선거수치 분리.
- `data/annals/lee-yun-yeong-run120.md` 및 `data/evidence/politicians/lee-yun-yeong-run120.json`: 이윤영 사회부장관의 광산임금 체불 인정과 노동조합 독립 자료 대조.
- `data/organizations/run120-june1950-institutional-actors.json`: 1950년 반복 기관 stable ID overlay.
- 생몰·관보 원면 미확보로 VERIFIED 승격 없음.

## Run124a (2026-10-09): 1951년 원내·원외 자유당 분리 창당

- `data/politicians/run124-1951-party-actor-index.json` 및 `run124-1951-party-actors-c/d/e/g.json`, `run124-yang-u-jeong.json`, `run124-kim-yong-u.json`, `run124-im-yeong-sin.json`: 1950년 후대 당선자 목록과 1951년 당대 창당 보도에 연결한 비대통령 인물 12명(IDENTIFIED). 생몰·당적 원부 미확보로 VERIFIED 승격 없음.
- `data/annals/1951-liberty-two-foundings-run124.md`: 1950년 당적 소급 오류와 원내·원외 조직 혼동을 방지하는 실록.

## Run124c/d 후속 인물·행위 (2026-10-09)

- `data/politicians/run124c-party-military-actors-a.json`: 이활·이종찬, `run124c-police-secretariat-actors-b.json`: 김종삼·고재봉. 1951년 동시대 원문에 등장한 교섭·군사·경찰·비서 역할을 독립 IDENTIFIED 후보로 보존.
- `data/politicians/run124-kim-yong-u.json`: 1951-12-21 귀속재산처리법 심의보류 동의 90:0 기록을 추가. 정부안 통과로 오인 금지.
- 1951-12-21 정부안에 반대한 6명은 `d124d-0170` 원문에 기록. 의원등록원부·동명이인 대조 후 독립 후보 승격 검토.

## 2026-10-09 run127 인물망

`data/politicians/run127-civil-cabinet-network.json`: 선전대책위원회 차관급 12명과 이교선·정순조·김두한 3명 후보 IDENTIFIED, 기존 전진한·윤치영·김용택 3명 심화. 관보·생몰 미검증으로 canonical 승격 보류.

## Run129 (2026-10-09): 1952년 6~7월 국회·내각 의사절차

- `data/politicians/run129-1952-parliamentary-actors.json`: 20명 독립 candidate ID, 당시 원속기록 한자·직책·행위·문서·미해결 신원질문. 전원 IDENTIFIED, 생몰·당선원부 미확인으로 VERIFIED 승격 없음.
- `data/evidence/politicians/jo-ju-yeong-run129.json`, `lee-jong-hyeong-run129.json`: 정부측 개헌답변과 국회 출석요청·발췌표결을 분리한 독립 증거. 이종형은 기존 run128 후보 ID 재사용.
- `data/annals/1952-june-july-parliament-run129.md`: 7개 원속기록과 별도 국가기록원 전시 교차확인. 6월14일 보류표결·7월4일 2독회/3독회 분리.

### Run129 추가 교차검증 및 이름 충돌

- `data/documents/run129-new-primary-and-crossfamily.json`: 1952-07-07 관보 제688호, 1952-08-07 문화보호법 법률 제248호, 1952-06-12 FRUS, 동시대 신문 2건.
- `data/politicians/run129-minister-identity-conflict.json`: 법무장관 徐相權(국회 6/21) vs 徐相懽(관보 7/7) 원표기 충돌. canonical ID 확정 금지.
- `data/research/runs/run129-correction-addendum.md`: 6월11일 심의지연 뒤 7월21일 문화보호법 통과 및 8월7일 제정 확인, 원문 근거 보존.

## Run133 (2026-10-10): 1952-06-19 국회 조사단 보도 명단

`data/politicians/run133-1952-inquiry-roster-actors.json`: 동아일보 1952-06-21 기사에 기록된 이시목·유덕천·백남식·한국원·오성환·김판석·유승준·서상국·이진수·김익로의 한자, 로마자, 당일 파별, 조사위원 명단 등장행위를 개별 candidate ID로 분리했다. **10명 모두 IDENTIFIED / 공식 의원원부 미확인**, canonical 승격하지 않음. 관련 event: `evt-r133-19520619-inquiry-roster`. 본문 원문은 `d131-0619-0020`, 원문 대조 및 역사부채는 run133 ledger 참조.


## 2026-10-26 Run156: 1957 국방·재정·정당·사법 인물
- 정식 registry 신규 5명: `pol-kim-jeong-ryeol-1917`, `pol-yu-jae-heung-1921`, `pol-cho-jeong-hwan-1892`, `pol-lee-han-bin-1957`, 기존 run154 candidate `pol-r154-kim-tong-hyon`. VERIFIED 3명(원문·인물해제 대조), IDENTIFIED 2명(생몰·원임명장 미확보).
- 기존 심화 5명: 김용우, 백선엽, 양유찬, 김현철, 장면. 중복 stable ID 생성하지 않음.
- 독립 annals: `data/annals/kim-jeong-ryeol-run156.md`, `data/annals/yu-jae-heung-run156.md`.
- 원문 레지스트리: `data/documents/run156-frus1957-documents.json`; 사건/주장: `data/events/run156-1957-force-fiscal-judiciary.json`, `data/claims/run156-1957-defense-fiscal-adversarial.json`.

- Run156 후속: 이기붕·조병옥 선거법 협상(후대 AKS 연구), 이기붕의 1957-11-04 제6군단 시찰 동행(KTV 소장설명). 원회의록·영상 미열람.


## Run157 1958 정치인 독립 노드
`data/politicians.json`에 김진만·김종철 IDENTIFIED 등록, 기존 김정렬·유재흥·백선엽·장면·이기붕·조봉암·조병옥·윤성순 8명 사건 연결. `data/politicians/run157-candidate-kim-tal-ho.json` 김달호는 한자·생몰·지역구 미확인 candidate로 보류. 선거 원당선자명부 미확보.


## Run158 · 1958 선거법·지방자치법 원문
- 김원태(1909) `pol-kim-won-tae-1909` ANNALS_ACTIVE: AKS 현대인 약전 + 관보 제2206호 내무위원장 절차 설명. 신라시대 동명이인 AKS E0010050과 병합 금지. `data/annals/kim-won-tae-run158.md`.
- 박용일·이근직·정재설·손창환·문봉제 5명은 `data/politicians/run158-1958-cabinet-legislative-candidates.json`에서 생몰·한자 미확인 candidate로 보존. 1958-01-25 공포문 기명은 법안 개인 기초행위의 증거가 아니다.
- 원문·사건·주장: `data/documents/run158-1958-election-local-law.json`, `data/events/run158-1958-election-local-law.json`, `data/claims/run158-1958-law-election-adversarial.json`.


## Run158c · 1960 헌정 전환 비대통령 실록
- 허정 `pol-r139-heo-jeong` ANNALS_ACTIVE: 1960-04 외무장관·대통령권한대행, 06-15 개헌 후 총리, 06월 한일외교 발언. `data/annals/huh-chung-run158c.md`.
- 윤보선 `pol-yun-posun` IDENTIFIED: 기존 `president-yun-posun` backbone ID에 1960-08-11 합동회의 208:51 선출·8/17 김도연 부결·8/19 장면 인준 연결. 국내 원회의록 검증 전 MATURE 금지.
- 백낙준·김도연·이수영·이재현·General Song 후보는 `data/politicians/run158c-1960-transition-candidates.json`에 한자·생몰·원인사기록 미확인으로 보존.


## Run158d · 1960-06-15 국회 기명투표 원명부
- 국사편찬위 헌정사DB 국회 제4대 제35회 제37차 `cons_004_0020_0010_0080` 원문에서 **218명 행위**(찬성208·반대3·불참7) 추출: `data/votes/1960-06-15-constitutional-amendment.json`. 208명 전체를 성급히 정치인 registry로 승격하지 않고 원문 한자·행위·identity status를 보존.
- 이옥동·조일재·이영희 발언과 표결 일관성 증거, 반대3명 실명, 김원태·윤보선·곽상훈 직접 행위 연결. `data/annals/1960-constitutional-rollcall-run158d.md`.


## Run162 · 1953~1961 한미행정협정과 정치인 독립 노드
- 기존 노드 심화: 백두진, 변영태, 손원일, 임병직, 조정환, 장면. 기존 stable ID 유지.
- 신규 candidate: 김동조 `pol-kim-dong-jo`, 현석호 `pol-hyon-seok-ho`, 김용식 `pol-kim-yong-shik`, 유동한 `cand-r162-you-dong-han`; 최규하 `pol-choi-kyu-hah`는 후대 대통령 backbone과 병합 검토. 동명이인 방지·생몰·임명원부 검증 전 본 registry 승격 보류.
- 각 후보는 `data/politicians/run162-sofa-actors.json`에 시기별 역할, 원문, 사건, lead, 검증상태 기록. 1957 'Minister Han'은 성명 미확정이므로 인물 노드 미생성.
- 자료 `data/documents/run162-sofa-primary.json`; 사건 `data/events/run162-sofa-actions.json`; 주장 `data/claims/run162-sofa-adversarial.json`; 실록 `data/annals/rhee-sofa-diplomacy-run162.md`.

## Run165: 1950년 10월 7~10일 유엔 결의와 행정복구

- 정식 registry `data/politicians.json`에 **이준식**(`pol-r165-lee-jun-sik`)을 IDENTIFIED 후보로 신규 추가하고 이승만·신익희·신성모·조병옥·정일권·손원일의 1950년 10월 근거와 사건 연결을 보강했다.
- 인물 상세: `data/politicians/run165-1950-october-actors.json`; 사건 원장 `data/events.json`에 17개 신규 ID 추가, 상세 overlay `data/events/run165-october-governance.json`.
- 문서 25개 `data/documents/run165-october-governance.json`; 주장 16개 `data/claims/run165-october-adversarial.json`; 실록 `data/annals/rhee-syngman-run165.md`; 연구선 35개 `data/research/lead-queues/run165-next.json`.
- 외국 정치인 로무로는 대한민국 정치인 registry에 편입하지 않고 국제기구 사건의 외부 참여자로만 구별한다.


## Run166 (2026-10-26) · 1950-10-12~15 전시 행정·경찰·국회
`data/politicians/run166-october-actors.json`: 기존 stable ID 7명(신익희·신성모·조병옥·이준식·손원일·윤영선·김훈)의 시점별 발언·행동을 `evt-r166-*` 및 `doc166-*`에 연결. 한자·생몰·임명 원부를 이번 회차에 독립 재확인하지 않았으므로 VERIFIED 승격 없음. 기사에서 성씨만 표기된 윤·김 장관의 동일인 식별은 OPEN.


### Run166 확장 · 1950-10-11~14
`data/politicians/run166-october-actors.json`에 임병직·장택상·곽상훈·조정환·백낙준·정일권 기존 ID 6명 보강, 김석관(`pol-r166-kim-seok-gwan`), 지연해(`pol-r166-ji-yeon-hae`), 정재완(`pol-r166-jeong-jae-wan`) 신규 IDENTIFIED 후보 3명 추가. 신원 생몰·임명/당선원부 미확보로 VERIFIED 승격 없음. 김석관·조정환은 독립 annals/evidence 실험 파일 개설.


### Run166 1950-10-16~18 추가 후보
주석균(`pol-r166-joo-seok-gyun`, 朱碩均)은 1950-10-17 농림부차관 기자회견에서 추곡 520만석·경기 15만석·인천 외곡 6000톤을 설명한 행위로 IDENTIFIED 후보 등록. 생몰·임명원부 미확인. 기존 신익희·윤영선·김석관·백낙준·김훈 등 시기별 발언·행위 보강.


### Run166 평양 UN군정 12인·김용중
평양시정위원회 12명(`pol-r166-pyongyang-*`)은 1950-10-20~22 밀번 소장의 **군정 임명** 보도에 따라 IDENTIFIED 후보화. 임정득·우제순·오진환·김영일·이용서·선우요·이헌주·안병섭·전여찬·윤도성·이학천·김기엽. 임명일 기사 충돌, 생몰·재임원부 미확보. 김용중(`pol-r166-kim-yong-jung`)은 1950-10-20 분류 오스틴 유엔대사 서한의 전국총선 주장 당사자로 IDENTIFIED 후보화, 정통성 비판을 역사적 사실로 확정하지 않음.

## 2026-10-26 · Run167 북한 민정지침 승인·국무총리 인준 후속

`data/politicians/run167-1950-cabinet-actors.json`: 기존 stable ID 9개 재사용. 백낙준·신성모·장택상·김성수·신익희 등 1950년 11월 국무총리 지명·국회 동의 사건 연결. 맥락상 등장만 하는 인물은 직접행위로 계수하지 않음. `data/events/run167-north-civil-cabinet-events.json` 및 `data/documents/run167-octnov-frus-primary.json` 교차 참조. 신규 신원 VERIFIED 승격 없음.

## 2026-10-26 Run168 · 제2대 국회 선거구 기반 정치인 10명 독립 노드

`data/politicians/run168-1950-election-network.json`에서 신익희·조봉암·안재홍·지청천·조소앙·박순천·정일형·곽상훈·여운홍·황성수의 1950-05-30 선거구/소속/행위 유형/문서/lead 연결. canonical 신규 4명 IDENTIFIED, 기존 6명 심화. NIH 후대 공식 편년자료와 AKS 후대 해설을 개별 선관위 원공고·의회 표결 원문으로 오인하지 않음. `data/annals/ahn-jae-hong.md` 기존 독립 실록 유지, 신규 안재홍 canonical ID에 연결. 지청천 AKS 사망연도 본문 1957 vs 이미지 캡션 1959 충돌 추적.


## 2026-10-26 Run169 · 제헌국회 농지개혁·사법·전시외교 인물 12명
- `data/politicians/run169-parliament-cabinet-actors.json`: 기존 canonical 7명(이문원·서상일·황호현·김봉조·최운교·임병직·권승렬)의 날짜별 행위 보강, 새 candidate 5명(정준·김동원·이정래·김수선·김병로). 이름/한자/원속기록 행위·근거문서·event·lead 기록. 생몰/당적 미확인, 정식 승격 0명.
- 독립 annals: `data/annals/seo-sang-il-run169.md`, `data/annals/lim-byong-jik-run169.md`, `data/annals/jeong-jun-run169.md`. 기존 ID 중복 생성 금지.
- `data/events/run169-cabinet-parliament-diplomacy.json`: 절차 동의·정책안·명령·집행·반론 분리. base `data/events.json`은 canonical ID만 `politicians`에 넣고 신규 후보는 `candidatePoliticianIds`로 overlay 참조.


## Run170 (2026-10-26) · 1951~1952 개헌안 결정과 국회 행위자
- `data/politicians/run170-constitutional-actors.json`: 기존 8명과 신규 식별 조진만·후보 이순용 등 10명 프로필. 기존 인물은 원문 기반 날짜별 행위·공식 해제 명단을 추가했으나 연구성숙도 자동 승격 없음.
- `pol-cho-jin-man`: 기본 registry에 **IDENTIFIED** 등록, 독립 실록 `data/annals/cho-jin-man.md`, 증거 `data/evidence/cho-jin-man.json`. 인천광역시 약력 표제의 사망연도 1972와 AKS 1979-02-12가 충돌해 `died=null` 유지. 직접 사망증빙 확보 전 VERIFIED 금지.
- `cand-r170-lee-sun-yong`: 1951-11-30 개헌제의 국무위원 발기자 명단에 실명만 확인. 한자·생몰·당시 부처 확인 전 canonical 승격 금지.
- 관련 사건 `evt-r170-01`~`evt-r170-14`, 문서 `data/documents/run170-constitutional-process.json`, 미해결 `data/research/lead-queues/run170-next.json`.

## Run171 (2026-10-26) · 1952 헌정위기·선거 독립 정치인 실록
- `data/politicians/run171-1952-constitutional-election-actors.json`: 기존 14명과 1952 선거 신규 후보 5명(후보 ID, 한자·생몰 원본 미확인). 후보 수집과 심층 연구를 구분.
- `pol-r139-jang-taek-sang`: 1952-05-14 정부 개헌안 제출의 공식 전사와 06-03 총리 전언을 구분하여 `ANNALS_ACTIVE` 시범 승격. `data/annals/jang-taek-sang.md`, `data/evidence/jang-taek-sang.json`.
- `pol-lee-beom-seok`: 1952 내무장관 임명 편집주석, 06-03 의원 구금 제안 전언, 08-05 부통령 후보 공식 선거사로 `IDENTIFIED` 승격. `data/annals/lee-beom-seok.md`, `data/evidence/lee-beom-seok.json`. 중복 의심 `pol-lee-beom-seok-1900`은 참조 감사 전 병합 금지.
- 사건 18개 신규 + 기존 `evt-r141-local-2035`(1952-05-10 지방선거), `evt-r162-20`(1952-08-05 대통령선거) 2개 보강. `data/events/run171-1952-decision-actions.json`.
- 원문·출처 충돌: `data/documents/run171-1952-constitutional-election-and-frus.json`, `data/claims/run171-1952-adversarial-source-criticism.json`, `data/research/corrections/run171-1952-chronology-provenance.md`.


## 2026-10-27 · Run180 FRUS·국회 1949 인물 11명

- 기본 등록부: 김구 `pol-r180-kim-gu` IDENTIFIED_CANDIDATE, 차경모 `pol-r180-cha-gyeong-mo` DISCOVERED. 차경모 관련 1949-10-28 발언은 대통령의 주장이지 유죄 확정이 아님.
- 조병옥 `pol-cho-byeong-ok` DISCOVERED→IDENTIFIED: 1949-07-11 조병옥·장면의 미국 국무장관 회동 및 07-13 무초 후속서한. 기존 별도 후보 `pol-cho-pyeong-ok`과 참조 전수감사 전 자동병합 금지.
- 이범석·임병직·손원일·장면·이호·신익희·정준 및 대통령 이승만의 사건 연결 보강. `data/politicians/run180-1949-actor-audit.json`.
- 독립 실록: `data/annals/cho-byeong-ok-run180.md`, `sohn-won-yil-run180.md`, `kim-gu-run180.md`, `lee-beom-seok-run180.md` 및 대응 evidence. 중복 의심 ID는 보존.


## 2026-10-27 · Run180b 한국 1949 동시대 기사 정치인망

- `data/politicians/run180b-1949-korean-actor-network.json`: 비대통령 신규/기존 31명, 대통령 1명. 신규 기본 registry 14명(기존 run95 overlay `pol-kim-jang-yeol-1949` 정식 IDENTIFIED 포함).
- 사회당 교섭자 김장열(`pol-r180b-kim-jang-yeol-socialist`)과 계엄법 수정안 국회의원 김장열(`pol-kim-jang-yeol-1949`)은 동일인 미확인, 자동병합 금지.
- 반민특위: 김효석·이인·신익희·이범석·권승렬. 재정금융위: 김도연·장희창·홍성하·백두진. 한독당·사회당: 최명식·조경한·나재하·신창균·백홍균·양우조. 계엄법: 윤치영·신현모·정광호·김장열·나용균·박찬현.
- 독립 annals/evidence: 김효석·김훈·안호상·한통숙·최명식·김장열. 36개 동시대 전사에서 기사상 주장과 실제 행정 집행을 분리.


## Run181 (2026-10-27) · 1949년 11~12월 평시 국정·비대통령 정치인

`data/politicians/run181-1949-domestic-actor-network.json`에 13명 역할/행위 근거 연결. 기존 ID 재사용, 김태선 `pol-kim-tae-seon` Run118 overlay ID 유지·기본 registry 연결. 신규 백기호·이철원·도석균·박준섭은 생몰·임명원부 미확보 IDENTIFIED_CANDIDATE. `data/annals/*-run181.md` 및 `data/evidence/*-run181.json` 독립 실록·증거. 신규 사건은 `data/events/run181-1949-domestic-actions.json`, 문서·주장·후속단서는 동명 run181 파일. 신원 미검증 승격 금지.

### Run181 추가: 제헌국회 원속기록·무역·통계

`data/politicians/run181-1949-domestic-actor-network.json`에 강선명·김상돈·노일환·서정희·지대형·김익진 신규 candidate를 추가. 신태익·김훈·김약수·김준연·임영신·장희창 등 기존 ID 재사용. 공식 원속기록 12/01 제55차 1350~1352쪽에 근거한 신태익·서정희·김훈 행위를 별도 기록. 신규 인물 생몰/임명원부 미검증으로 VERIFIED 승격 보류.

## Run182 (2026-10-27) · 1948~1949 출입국·국적·법률 의사단계

- `data/politicians/run182-immigration-legal-actors.json`: 조정환(曺正煥) 외무처장대리 원관보 전사 서명에 기반한 IDENTIFIED 후보 1명, 기존 박상영·권승렬·이종현·서상일·조영규 재사용 5명. 생몰·임명원부 미확보로 신규 VERIFIED 승격 없음.
- `data/documents/run182-immigration-legal-documents.json`, `data/events/run182-immigration-legal-actions.json`, `data/claims/run182-immigration-legal-claims.json`: 원관보 전사·신문·후대 해제의 증거 등급을 분리. 기존 `d95-constitutional` 재사용.
- `data/annals/1948-1963-immigration-legal-transition-run182.md`: 출입국법 제65호 국회·내각·공포·집행 단계 분리.


## Run193 · 1950-01~08 정당 재편·예산·한국은행 정부안

- `data/politicians/run193-1950-caucus-actor-network.json`: 기존 canonical 17명은 1950-06-26 서울신문 교섭단체 교섭 또는 1950-07-04 국편 연표의 비상위원 명단에 문서·사건 연결만 추가. 연구상태 자동 승격 0명. 신규 `cand-r193-kim-beom-bu`는 金凡夫 신원 미확인 DISCOVERED 후보.
- 독립 인물 보충 실록: `data/annals/lee-beom-seok-run193-fiscal.md`, `data/annals/ahn-jae-hong-run193-caucus.md`.
- 증거·사건·주장: `data/documents/run193-1950-caucus-budget-bank.json`, `data/events/run193-1950-parliament-fiscal-actions.json`, `data/claims/run193-1950-party-budget-claims.json`.
- 6/26 신문상 교섭단체 가입·연합은 공식 당적과 별개. 8/1 예산표 금액은 원표 확보 전 신문 전사 수치임.


## Run196 · 1950-08-17~09-01 외교·내각이전 인물 관계
`data/politicians/run196-1950-actor-crosslinks.json`에서 기존 인물 10명(비대통령 9명)을 재연결했다. FRUS d441의 직책명만으로 신성모·조병옥·임병직 개인의 원결재를 확정하지 않는다. 신규 승격 없음.


### Run196 신원충돌 유보
`cand-r196-park-jong-man-assembly` (1950-08-17 국회사무총장으로 무초 보고)와 `cand-r195b-19` (1950-08-09 대한통신 사장 보도)는 동일한 '박종만' 이름이나 개인 동일성 미확인. `IDCOL-R196-01`로 자동병합 금지. `cand-r195e-02` 김준태도 국회 원속기록 대기.


### Run196B · 1950-08-22~09-07 국편 국내행정·전시선전대책위원회
`data/politicians/run196b-1950-domestic-actors.json`: 기존 24명(비대통령 23)의 동시대 실명발언·위원명단 연결, 새 후보 이윤영 헌병대장 소령은 사회부장관 동명이인 여부 미확인. 김도연/이범석 중복 canonical ID는 자동 통합하지 않았다. 개인 참석·표결·법원유죄 추정 금지.


### Run196C · 9월 헌법위원·UN대표단·여성의용군
`data/politicians/run196c-1950-september-actors.json` 기존 인물 27명, 신규 후보 손창섭·박승하 DISCOVERED. 임병직·장면·장택상·김동성·임영신·황성수 UN대표단은 후보→국회/정부 갈등→공식임명으로 분리.


## 2026-10-27 · run197 전시 국정·국회·복지·치안 정치인 overlay

`data/politicians/run197-1950-september-actor-network.json`: 기존 stable ID 정치인 25명(대통령 1명 포함)의 1950-09-01~11 시기별 행위·문서·사건 연결과 별도 후보 4명(헌병 이윤영 소령, 서상덕 의원, 손창섭 징병책임관, 선전위원 박종만). 이윤영 사회부장관과 헌병소령의 한자 동명, 박종만 3역할 충돌을 병합하지 않는다. 생몰·당적·임명원부 미검증이면 자동 VERIFIED/MATURE 승격하지 않는다. 원문 목록 `data/documents/run197-1950-september-contemporary.json`, 사건 `data/events/run197-1950-september-governance.json`, 부채 `data/research/HISTORY_DEBT.md`, 후속 `data/research/lead-queues/run197-next.json`.


## 2026-10-27 · run197b 정당·재정·입법·군정 인물 overlay

`data/politicians/run197b-1950-party-cabinet-military.json`: 기존 정치인 27명과 후보 4명(최창식 공병감·양정수 법무감·이종찬 3사단장·신상철 7사단장). 민주국민당 9/25 전국대회 신익희·지청천·김성수·백남훈·함상훈·김준연·최두선·나용균·서상일의 발언·낭독·의장 역할과 당론 구분. 원면·생몰·인사원부 미검증 후보 자동 승격 보류. 법률·통화·군정 cross-link: `data/events/run197b-1950-sep14-30-actions.json`.


## Run198 (2026-10-27) · 1950-10-22~31 일상국정·행정·UN군정

- 원문 전사 89건 + 법제처 대통령령391 + CIA 1950-10-30 원문 발췌, 사건 29개, 주장 20개를 교차 연결. 상세 `data/documents/run198-oct22-31-contemporary.json`, `data/events/run198-oct22-31-state-actions.json`, `data/claims/run198-october-adversarial.json`.
- 기존 비대통령 17명 실질 보강: 최순주·이기붕·이익흥·양성봉·김태선·조병옥·백낙준·윤영선·이범석·신성모·장면·손원일·임정득·오진환·신익희·이윤영·김석관. **기관맥락만인 김석관과 신원 불확실 이윤영은 개인 직접명령으로 귀속 금지.**
- 신규 DISCOVERED 4명: 김창룡(합동수사), 이정일(8사단 군령), 장두관(경남 계엄민사), 김윤근(1950 대한청년단장). 생몰·임명원부·한자 일부 미확인, VERIFIED 승격 0.
- **신원교정**: 기존 `pol-kim-yun-geun`은 1961 해병지휘관 기록. 1950 청년단장 金潤根과 동일인임이 입증되지 않아 `cand-r198-kim-yun-geun-youth1950` 별도 후보. `data/politicians/run198-october-actor-network.json`의 correctionHistory를 참조. 기존 이범석 중복 ID도 병합하지 않음.
- 독립 비대통령 실록 `data/annals/nonpresidential-october-run198.md`; 대통령 실록 `data/annals/rhee-syngman-run198.md`. 연구상태 점수·정치적 평가 없음.


### Run198b · 1950-11-01~07 (2026-10-27)
- 국편 신규 문서 87건, canonical 사건 36건 추가, 기존 비대통령 18명 보강, 신규 DISCOVERED 후보 8명. `data/politicians/run198b-nov-actor-network.json`.
- **번역 교정**: `dh_019_1950_11_04_0060`은 George Paek를 백두진으로 번역했으나 FRUS d746 교육장관 각주와 경향신문 1950-11-03 白樂濬은 **백낙준**. claim-r198b-01에 양쪽 원문·교정 이력 보존.
- **절차 구분**: 11/2 계엄해제 국회 요구, 11/7 새 경비계엄(11/10 시행), 11/3 총리인준 부결, 11/7 내각사임 건의 조건부 보류. 사건·주장·법적효력을 구분한다.

## 2026-10-27 · Run202 한국인 행위자 증분 연결

[run202 한국 정치인 기존 stable ID overlay](run202-dec07-12-korean-actors.json): 장면(`pol-chang-myon`)의 1950-12-11 정부 훈령 전언, 조병옥(`pol-cho-byeong-ok`)의 12-07 내무부 피난 관련 담화는 본문 직접 확인. 허정(`pol-r139-heo-jeong`)의 사회부 전시기구 개편은 날짜 색인만 확인되어 실질 심화 수에 미포함. 이기붕(`pol-yi-ki-pung`)과 무초 전문의 무명 서울시장 연결은 **잠정 신원추론**이며 새 승격 아님. `data/politicians.json` 원본 772KB는 이번 회차에서 변경하지 않았고 overlay 소비자 병합이 필요하다.

### Run202 추가 국편 본문 검증 (12월 7~14일)

기존 stable/candidate ID를 보존하며 총 19명의 한국 공직·정당·입법·행정 행위자에 대해 직책·행위·원문·다음 원문 표적을 추가했다. 허정·신익희·정일권·이호(동명이인 미확인)·양성봉·김주학(신규 후보)·장흥(신규 후보)·이범석·김창룡·장두관·곽상훈·강경옥·임병직·이성주·오제도·박문기(신규 후보)·신성모·장면·조병옥. [상세 overlay](run202-dec07-12-korean-actors.json). 생몰·임명원본 검증 전 canonical 승격 없음.

Run202 12/15~17 후속 행위자: 이시영(`pol-r189-lee-si-yeong`), 이진수(`pol-r141-lee-jin-su`), 이재형(`pol-r184-lee-jae-hyeong`), 장영근(`cand-r202-jang-yeong-geun`), 김천수(`cand-r202-kim-cheon-su`). 총 24명 비대통령 실질 행위자, 정식 후보 승격 없음.


## Run205 · 1951년 3~6월 외교·군사지휘 전환 (2026-10-27)

`data/politicians/run205-april-embassy-actors.json`에서 임병직(`pol-lim-byong-jik`) 기존 독립 실록을 FRUS d181·d243으로 심화하고, 김세선(`cand-r205-kim-se-sun`, Sae Sun Kim)과 한표욱(`cand-r205-han-pyo-wook`, Pyo Wook Han)을 1951-03-22·04-18·06-25 외교 접촉별 독립 후보로 구조화했다. 김세선은 run201의 대사 후임 예정 언급과 같은 영문 인명으로 보이나, 공식 주미대사 신임장 수여로 오인하지 않는다. 두 후보의 생몰·한자·임명 원부는 미확인으로 정식 승격 보류. 관련 annals `data/annals/run205-rhee-command-diplomacy.md`, event `data/events/run205-april-command-actions.json`, claim `data/claims/run205-april-command-adversarial.json`.


## Run205b · 1951년 4~5월 국회·내각·행정 정치인 20명

data/politicians/run205b-assembly-cabinet-actors.json: 김준연·조병옥·신성모·김종회·서민호·엄상섭·이재형·최국현·박철웅·황성수·김태선·손원일·박만원 등 기존 stable ID 심화, 김의준·박경구·김종순·장홍염·김정식·이상철 등 후보 식별. 1951 국민방위군사령관 金潤根은 1961 해병지휘관 pol-kim-yun-geun과 신원 병합하지 않는다. 생몰·인사원부·원속기록 검증 전 신규 정식 승격 없음.


## Run205e · 1951-05-22 농정·재정·사법 인물

data/politicians/run205e-may22-governance-actors.json: 장면(pol-chang-myon), 백두진(pol-paik-too-chin), 임문환(pol-r175-im-mun-hwan), 이재형 등 기존 인물의 구체적 부서·담화·표결 심화. 백남식·태완선·홍창섭·우문·정인승·김효섭을 개별 candidate로 식별. 우문(禹文)처럼 짧은 이름은 동명이인 합병 금지. 각 인물은 원문 ID·행위 유형·생몰 미검증·다음 조사원부를 보유.


## Run208 (2026-10-28) · 1951년 6월 외교·환율·재건행정
`data/politicians/run208-1951-june-korean-actors.json`: 이승만 `pol-rhee-syngman`, 장면 `pol-chang-myon`, 백두진 `pol-paik-too-chin` 기존 ID 재사용, 김세선 `cand-r205-kim-se-sun`, 한표욱 `cand-r205-han-pyo-wook` 기존 후보 심화. 한국 비대통령 **4명**만 신규 문서 근거로 심화; 영국·미국·인도 외교관은 한국 정치인으로 허위 계산하지 않음. FRUS d332/d339 환율 교섭 및 d356 정전교섭 참여요청을 event ID로 연결. 생몰·임명 원본 미확보, 후보 VERIFIED 승격 0. `data/annals/run208-1951-june-cabinet-diplomacy.md`.

Run208 기관명부 후속: 김훈 `pol-r164-kim-hun` 1950-05-09~1952-03-27 상공부장관 공식 재임명부와 FRUS d332 익명 상공부장관 환율 반대 보고 연결(본인 서명 없음). 조병옥 `pol-cho-byeong-ok` 1951-05-06 내무장관 퇴임, 이순용 `cand-r208-lee-soon-yong-interior1951` 1951-05-07 취임, 청주사건 문책 개인결재 미확인. `evt-r208-19`~`20`, `claim-r208-21`~`22`.

Run208 신원검증: `cand-r207-kim-su-hak` 金秀學(1950 고창갑 당선, AKS 1896~1967), `cand-r207-lee-jong-uk-caucus` 李鍾郁(1950 평창 국민회 승려 67세, AKS 1884~1969), `cand-r198b-so-seon-gyu` 蘇宣奎(1950 익산갑 민주국민당 당선) 기존 후보 ID 심화. canonical 金洙鶴·李宗郁와 원의원명부 대조 전 자동병합 금지. `data/annals/run208-1950-election-identity.md` 및 `data/evidence/run208-1950-election-identity.json`.


## Run209 (2026-10-28) · 1951-06-26 인사·전시행정 독립 인물
- `data/politicians/run209-june26-actors.json`: 김태선·이익흥·허정 기존 ID, 윤우경(尹宇景)·홍범희(洪範憙) 후보 ID, 백두진·김훈의 공동성명 당시 재임맥락을 분리. 신규 후보 2명은 관보·생몰 미확보로 VERIFIED 승격하지 않음.
- `data/evidence/politicians/run209-june26-actor-evidence.json`, `data/annals/run209-1951-june26-government-relief.md`: 보도된 인사/구호/정책과 실제 집행 분리. 기존 HD-R199B-04 김태순/김태선 충돌은 원신문 대조 전 NARROWED 유지.

### Run209 후속 독립 인물 실록
- [윤우경](../annals/politicians/cand-r209-yun-woo-gyeong.md): 서울경찰청 1951-06-24 재임시작 vs 민주신보 6/26 발령, 신원 1900~1995 AKS 확인, 정확한 취임일 CONFLICTED.
- [홍범희](../annals/politicians/cand-r209-hong-beom-hui.md): 제헌의원·1951 6~11 내무차관, 1917~1972 AKS 인물전기 확인, 원임명관보 미확보.
- 6/27~7/1 장면·이철원·이종찬·곽태진·양우정·김종회·양유찬·신성모·신현돈·조재천·부산특별시법안 발의자 등을 독립 ID로 연결. 원문 미확보 후보의 정식 승격은 보류.

## Run210 · 1951-07-02~07 비대통령 행위자

`data/politicians/run210-july02-07-actor-network.json`: 기존 stable 인물 재사용 및 안만복·양유정·손성겸 candidate ID 신설. 국회 질의, 군 지휘, 농정·재정, 지방 구호, 외교 행위를 사건·문서로 연결. `cand-r209-lee-jong-chan`은 Run209 기존 candidate ID 재사용, 한자 李鍾贊은 육본훈령191에서 직접 확인했으나 동명이인·생몰·원임명장 확인 전 canonical 병합 금지.

## Run211 (2026-10-28): 이승만 시대 1951년 7월 독립 비대통령 네트워크

[초기 인물 27기록](run211-july10-20-actor-network.json), [중기 22기록](run211-july16-20-actor-addendum.json), [후기 32기록](run211-july21-31-actor-addendum.json). 합계 81 evidence-linked actor records, 중복 제거한 비대통령 64명, 신규 provisional candidate 21명. 정식 registry 승격 **0명**: 신문 단독 등장과 생몰 미검증을 MATURE로 만들지 않음. 각각 ID, 이명·한자(확인 가능한 경우), 시기별 직책, 사건·문서, 확인수준, open lead를 보유.

인물 동일성 방어선: 1951 방위군 김윤근 / 1950 청년단장 김윤근 / 1961 해병 김윤근은 별도 노드로 유지; 1951 국방차관 김일환과 1956 상공장관 김일환도 검증 전 병합 금지. 엄상섭의 嚴祥燮/嚴詳燮 한자 표기는 CONFLICTED. 탄핵재판소 5+5 심판관, 1951 의료법 의원, 경찰 인사, 은행·재정위원, 정당인, 총리·장관·외교관을 이승만 대통령의 단순 부속 인물이 아닌 독립 actor로 취급한다.


## Run212 · 1951-08 헌법위원회·정부조직개편 인물 22명

[독립 actor 22건](run212-august-constitutional-reform-actor-network.json), 신규 candidate ID 8건, 기존 stable ID 재사용 14건(이승만 1건 포함). 국회측 헌법위원 소선규·정헌주·남송학·김봉조·이도영과 대법관측 김병로·김찬영·백한성·김두일·김우식을 별개 노드로 연결했다. 8/9 정부조직법 개정 제안자 오위영·서민호·방만수·양우정·김정실도 제안자별 독립 노드로 연결했다. 신문 전사로 확인된 직책을 원임명장 확인과 혼동하지 않고 생몰 미확인 후보는 승격하지 않는다. [비대통령 실록](../annals/politicians-1951-constitutional-committee-reform-run212.md), [22 사건](../events/run212-august01-10-actions.json).


Run212 8/11~15 후속으로 [계엄 공고 국무위원·이종찬·김종원·김석관·백낙준·이활·김대운 등](run212-august-constitutional-reform-actor-network.json)을 연결해 **37 actor records(비대통령 36)**, 신규 candidate 11개로 확장. 이름/생몰/동명이인 원전거 미확인 시 정식 승격 보류.

### Run213 (2026-10-28)
[11명 정치인·후보 증거 연결](run213-augsep-actor-network.json) · [행위별 근거](../evidence/politicians/run213-augsep-evidence.json) · [국정·외교·사법 사건](../events/run213-augsep-actions.json). 직접 발언/행위 7명과 기관 맥락만 4명을 분리하며 무근거 승격하지 않는다.

### Run213 후반 1951-08-25~31
[신규 후보 8명·기존 인물 심화](run213-aug25-31-actor-network.json) · [신당 준비회합 네트워크](../events/run213-aug25-31-actions.json) · [미대사관·대통령·언론 3계열 비교](../research/runs/2026-10-28-run213-final-report.md). 1951-08-17 준비회합 참석을 정식 창당·정당가입으로 오인하지 않는다.

## Run214 (2026-10-28)

`data/politicians/run214-september-actors.json`: 양유찬·백두진·장면·이종현·이윤영 5명과 김종순·주요한·한근조·신현돈 신규 후보 4명의 개별 문서·사건·행위유형·open lead. 성명 미확정 내무장관은 office-only, 이승만은 대통령 맥락. 비대통령 개인근거 9명, 정식 승격 0. `data/evidence/politicians/run214-september-evidence.json` 연동.

## Run216 (2026-10-28): 1951년 11월 정부개헌 관보·전시 국정

[관보 제562호 13 국무위원과 6명 추가 정치인, 총 19명](run216-nov1951-actors.json) · [21개 사건](../events/run216-nov1951-actions.json) · [정부개헌·외환·정전·농정 실록](../annals/run216-1951-nov-constitutional-economy.md). **이순용**(李淳鎔) 신규 candidate, **오한영·임문환** IDENTIFIED로 승격. 부서는 개별 개헌조문 발의·찬성을 증명하지 않는다. 변영태 외무부장관 한자는 관보 전사에서 일부 깨짐, 원면 확인 필요. 생몰 미확인 유지.

## 2026-10-28 · Run217 1951-12-23 자유당 원내·원외 발당

`data/politicians/run217-dec1951-party-actors.json`: 부산일보 1951-12-25에 기록된 개인별 역할 13명. 기존 stable/candidate ID 12명 재사용, 김주학만 신규 `cand-r217-kim-ju-hak`. 임시 ID 10개가 기존 registry와 중복됨을 발견해 교정했으며 대응표는 `canonicalIdReconciliation`에 보존. 원내·원외 별도 발당과 지도부 선출을 대통령 직접행동과 구분.


## Run220 (2026-10-28) · 1951-12-26 국회 농지·토지수득세·장관 답변

- `data/politicians/run220-dec1951-land-tax-actors.json`: 기존 ID 7명(정헌주·최헌길·강경옥·유홍·김종순·백두진·임문환) 재사용 및 곽의영(郭義榮) `cand-r220-kwak-ui-yeong` 신규 후보. 각자 동시대 기사에서의 감사보고·법안제안·동의·장관답변을 분리했다. 신원·생몰·원속기록 미확보로 VERIFIED 승격 0명.
- `data/documents/run220-dec1951-primary-and-press.json`, `data/events/run220-dec1951-actor-actions.json`, `data/claims/run220-dec1951-adversarial.json`, `data/annals/rhee-dec26-31-run220.md` 참조. 1951-12-26 김종순 개정안은 법률 성립으로 간주하지 않는다.


## Run220 2차 (2026-10-28) · 1952-01-01~03 비대통령 국정

`data/politicians/run220-jan1952-actor-addendum.json`: 기존 장면·허정·신익희·김병로 4개 ID에 직접 확인한 신년행사·유엔가입 신청서한 보도·사회부 피난민/군경원호 계획·국회의장 신년사를 연결. 정순조는 당대 신문에서 개헌 추진자로 등장하나 생몰·원의안 미확보로 신규 stable 승격 보류. 관련 문서/사건/주장/실록은 run220-jan1952 addendum 참조.

- Run220 12명 비대통령 독립 증거 객체: `data/evidence/politicians/run220-actor-evidence.json`. 역사부채 10건은 `data/research/HISTORY_DEBT.md`에 상태·다음 원문표적과 함께 동기화.

## Run221: 1952년 1월 독립 정치인·관료 evidence
- data/politicians/run221-jan1952-actors.json: 기존 9명 심화, 신규 후보 4명 이헌구·백홍석·이호석·이정희. 공식 생몰·임명원부 미검증, 정식 승격 0명.
- data/evidence/politicians/run221-evidence.json / data/events/run221-jan1952-actions.json / data/documents/run221-jan1952-sources.json / data/claims/run221-adversarial.json에 ID로 교차 연결. 별도 annals: data/annals/rhee-jan1952-run221.md.
