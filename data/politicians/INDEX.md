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
