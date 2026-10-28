# 정치인 registry 확장 인덱스

- 기본 registry: `data/politicians.json` (기존 API 호환 유지)
- 2026-10-08 토지행정·제헌국회 독립 인물 12명: `data/politicians/run81-land-actors.json`
- 원문 기반 후보 상세: `data/research/candidates/run81-land-policy-actor-network.json`
- 안재홍 독립 실록: `data/annals/ahn-jae-hong.md`, 증거: `data/evidence/ahn-jae-hong.json`
- 신규 event/action: `data/events/run81-land-legal-actions.json`

조회 시 base와 overlay를 stable ID로 결합한다. 기존 ID를 삭제하거나 자동으로 덮어쓰지 않는다. `pol-lee-beom-seok-1900`과 `pol-lee-beom-seok`은 동일인 중복 의심이며 canonical은 후자로 제안하되 참조 전수조사 전 병합하지 않는다.

- 2026-10-28 1952년 장관교체·경제협정·저격미수 공판·산업노동 행위자 14명: `data/politicians/pass-229-1952-cabinet-economy-trial.json` (기존 stable ID 보존, 신규 candidate ID는 병합 전 신원 검증).
- 장석윤 독립 실록: `data/annals/jang-seok-yun.md`; 원문 및 주장·사건 그래프: `data/documents/pass-229-1952-cabinet-economy-trial.json`, `data/claims/pass-229-1952-cabinet-economy-trial.json`, `data/events/pass-229-1952-cabinet-economy-trial.json`.

- 2026-10-28 추가 1952년 중석불 국회 조사위원 12인·정순조 조사권 요청 및 5월7일 각료 10인: `data/politicians/pass-229b-1952-cabinet-oversight.json`. 국회 123인 서명과 1950 총선의 시기별 정당소속을 구분하며 鄭順朝/鄭純朝 불일치 보존.

- 2026-10-28 계엄 598·599호·헌법 제2호·최창순 원호·김태선/이윤영 인물노드: `data/annals/1952-martial-constitution-welfare.md`, `data/politicians/pass-229b-1952-cabinet-oversight.json`.

- 2026-10-28 서민호 독립 실록·재판/검찰/군법회의 actor 9인, 1952-05-10 도의원 당선자 8인: `data/annals/seo-min-ho.md`, `data/politicians/pass-229d-1952-local-justice-actors.json`. 대통령 재임 사건과 직접 지시를 분리.

- 2026-10-28 pass231 1952년 8월 대통령·부통령 후보, 중석불 국회감사·검찰 불기소·지방행정 등 비대통령 후보 14명과 기존 노드 13개 연결 보강: `data/politicians/pass-231-1952-election-accountability.json`. 5개 신원확인 단계 후보는 기본 `data/politicians.json`에도 additive 등록. 생몰·한자 미확인, 동일인 자동병합 금지.
- 이들 독립 행위·증거·문서 연결: `data/events/pass-231-1952-constitutional-election-pow.json`, `data/documents/pass-231-1952-june-july-diplomacy-election.json`, `data/claims/pass-231-1952-election-pow-accountability.json`, `data/annals/1952-july-august-election-economic-accountability.md`.


- 2026-10-28 pass232: 1952년 9월 16~19일 내각·도지사 인사·경찰·정당 통합·해양주권·재외국민 정치인 23명(신규 candidate 14, 기존 ID 9 심화)을 `data/politicians/pass-232-1952-september-actors.json`에 독립 노드로 연결. 한자 확인은 동시대 보도 범위, 생몰·임명 효력일·당적은 원본 대기. 1952 GATT 가입 '결정'과 1967 정식 가입은 별도 event/claim으로 보존.
- pass232 문서·사건·주장·실록: `data/documents/pass-232-1952-september-governance.json`, `data/events/pass-232-1952-september-governance.json`, `data/claims/pass-232-1952-september-governance.json`, `data/annals/1952-september-state-party-economy.md`. 1952년 9월 정당스케치의 풍자·전언을 검증된 사실로 승격하지 않음.

- pass232 후속: 전규홍 주불공사(1952-02 GATT 복명서 작성자로 2017 학술초록에서 언급)를 `DISCOVERED` 독립 candidate로 추가. 외무부 원본·한자·생몰·재임 원장 확보 전 검증 승격 금지. 산업부흥국채법 제254호·특별회계법 제255호(1952-09-28) 및 1954년 최초 발행의 시차는 event/claim에 연결.


## Pass233 1952년 10~11월 외교·재건·정보 네트워크 (2026-10-28)
- actor overlay: `data/politicians/pass-233-1952-rok-diplomacy-network.json` (13명, 신규 후보 5명; 기존 8명 교차연결).
- 1952-10-17 변영태·양유찬·임병직 UNCURK/UN 가입·조약 요청은 FRUS d288 원문으로 연결. 장면·조봉암·이종찬·정일권·신성모 관련 d323 첩보는 **동시대 강한 부정평가가 병기된 미확정 의혹**이며 인물 혐의 사실이 아님.
- 김용식·함상훈은 국편 목록만 확인, 본문 미열람 상태 `DISCOVERED`로 유지. 이름·한자·생몰은 원관보 확인 전 임의 VERIFIED 승격 금지.


## Pass233 addendum 1952-10~11 한국 원문 기반 독립 정치인 노드
- `data/politicians/pass-233-addendum-1952-domestic-actors.json`: 직접 기사·서한으로 확인한 12명, 신규 canonical 5명.
- 함상훈·조병옥·유진산의 민주국민당 야당연합 준비, 김용식의 대일 외교성명, 윤재욱 서울시의원 UN 집회, 이윤영·이갑성 별도 총리지명, 배은희 자유당 교섭단체, 백두진 국무총리서리 대독, 신중목 농정 계획, 양유찬·임병직 대통령 서한 수신을 각각 문서/사건으로 연결.
- 한자·영문 이명은 원문 출현 표기를 우선하며 생몰 원자료 확인 전 `MATURE` 승격 금지.


## Pass233 1952-12-01 UNKRA 재무부 인선
- `data/politicians/pass-233-dec1-unkra-liaisons.json`: 이병호(李丙虎, 전 상공·내무 차관)와 원용석(元容奭, 전 농림차관)을 1952-12-01 재무부 발표에 근거해 candidate `IDENTIFIED`로 추가. 정식 인사발령·생몰 미확인.


## 2026-10-28 pass234: 1952년 12월 국회 재정·농정 인물
- `data/politicians/pass-234-1952-dec-legislative-actors.json`: 오위영(재경위원장), 정재완·엄상섭(추경 질의), 윤담(가마니 가격 수정), 임흥순(한국인 전범자 석방 건의). 신문전사에 실명·한자·행위가 확인되어 IDENTIFIED, 생몰·원속기록은 OPEN.


## 2026-10-28 pass234B 행정·인사 후속
- `data/politicians/pass-234-addendum-1952-dec-actors.json`: 윤명운 서울특별시 경찰국장 IDENTIFIED 신규. 백두진·진헌식·윤치영·이기붕·임병직 5명 기존 노드 심화. 후보 물망/실제 지명 및 수사계획/유죄 확정 분리.

## Pass235: 1953-01~03 국회·군정·재정 행위자 (2026-10-28)
- `data/politicians/pass-235-1953-assembly-cabinet-actors.json`: 기존7명 심화 + 국회 위원장 **후보 보도** 8명 잠정 신규. 후보와 실제 당선은 구별. 원선거 기록 필요.
- 관련: `data/events/pass-235-1953-governance-currency-pow.json`, `data/claims/pass-235-1953-adversarial.json`, `data/annals/1953-jan-mar-governance-currency-pow.md`.

### Pass235B 국내 예산·문화외교 보강
- `data/politicians/pass-235-addendum-b-culture-speaker-minister.json`: 신익희 1953 신년사, 이범석 중복 ID review, 이철원 공보처장 문화사절단. 신문상 사절단 3명은 정치인 자동승격하지 않음.

### Pass235C 1953-02-17 통화개혁·진헌식·정일권·이형근
- `data/politicians/pass-235-addendum-c-jin-chung-lee.json`: 진헌식 VERIFIED 근거 보강, 정일권 2군단장, 이형근 제1군단장 신규 후보. 이범석 직함 충돌은 history debt.

### Pass235E 1953-01-29 국회 위원장 선거 보도 검증
- `data/politicians/pass-235-addendum-e-committee-chairs.json`: 당선·낙선·후보 양보·민간어업 협의·불신임안 발의 관련 12명 잠정 노드. 1/20 후보명단과 2/1 선거보도 cross-link, 원개표표 검증 전 최종 승격 금지.

### Pass235I 1953-03 금융·정당·내각 행위자
- `data/politicians/pass-235-addendum-i-bok-party.json`: 김유택 한국은행총재와 원내 자유당 이동 계획·장택상 당내 논쟁 관련 9명 잠정 후보. 10명 주장 vs 실명9명 보존, 실제 입당 확인 전 승격 금지.

- 2026-10-28 pass236A: 노동 3법 국회 의결·이송·공포·시행령과 신익희·백두진·박술음 독립 인물 노드: `data/politicians/pass-236-labor-actors.json`, `data/events/pass-236-labor-laws.json`, `data/documents/pass-236-labor-law-registry.json`, `data/claims/pass-236-labor-adversarial.json`.

- 2026-10-28 pass236B: FRUS 1953년 3~4월 43개 고유 문서(원작성 41·편집주석2), 포로·환도·통화정산·정전·한미외교 인물·사건·주장·문서 그래프: `data/politicians/pass-236-frus-diplomacy-actors.json`, `data/events/pass-236-frus-march-april.json`, `data/claims/pass-236-frus-adversarial.json`, `data/documents/pass-236-frus-march-april-registry.json`, `data/research/runs/pass-236-execution-ledger.json`.

- 2026-10-28 pass236C: 기존 evidence에 있던 한강교·국민방위군·거창사건 3개 event ID를 누락된 root event registry에 재연결: `data/events/pass-236-legacy-command-backfill.json`, `data/annals/1950-1951-command-event-backfill.md`. 새 사료 수로 계산하지 않음.

- 2026-10-28 pass236D: 신익희 첫 독립 국회의장 실록 시험 승격 `ANNALS_ACTIVE`: `data/annals/shin-ik-hui.md`, `data/evidence/shin-ik-hui.json`. 기존 candidate ID 보존, 생몰·당적·표결 미확인. 구 evidenceCoverage 단문자 migration 오류 2건 교정.
