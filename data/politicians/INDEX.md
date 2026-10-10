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

## Run148 (2026-10-11): 1953 참의원선거법 인물망

`data/politicians/run148-1953-senate-actors.json`: 신규 후보 8명, 기존 ID 6명 심화. 1953-11-30 원속기록 기반 의사행위 확인, 생몰·당적·선거구 미검증. 1953 본회의 법안과 1958 법률 제469호 구별.
