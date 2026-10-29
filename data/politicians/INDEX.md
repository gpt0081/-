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

- 2026-10-28 pass236E: 부산일보 1953-03-05·03-08 자유당 입당심사 원기사, 신태악·양우정 신규 후보, 장택상 심화; 대통령기록관 시행령783호 박술음 朴術音 확인; 신익희 1952-07-04 임시의장 직무 정정. `data/annals/1953-march-party-admission-dispute.md`.

- 2026-10-28 pass236F: 국편 이승만서한철 1953-02~03 개별 서지 30건(원문이미지 미열람), 임병직·양유찬·변영태·백두진 원조·언론·군사·반대자 관련 발수신 네트워크: `data/documents/pass-236f-rhee-correspondence-catalog.json`, `data/events/pass-236f-correspondence-actions.json`, `data/annals/1953-rhee-correspondence-catalog-network.md`. 기존 부산일보·대통령기록관 문서 registry 중복 1건 제거.

- 2026-10-28 pass236G: 이승만서한철 1953-03-18~04-02 서지 30건, 교육·원조·한미재단·언론·대일외교 actor graph: `data/documents/pass-236g-march-april-correspondence-catalog.json`, `data/events/pass-236g-correspondence-actions.json`, `data/annals/1953-late-march-april-correspondence.md`. 원문이미지 미열람, 전문 수에 불산입.

- 2026-10-28 pass236H: 이승만서한철 1953-04-02~17 서지30건, UNKRA 대표권·Tasca 임명·신태영 국방장관 8240/8242부대·변영태 포로서한의 기관별 책임 분리: `data/documents/pass-236h-april-correspondence-catalog.json`, `data/events/pass-236h-april-actions.json`, `data/annals/1953-april-aid-military-correspondence.md`. 원문이미지 미열람.

## Pass237 1953-04~05 원문 추적 (2026-10-28)
- 한국 정치인 변영태·양유찬의 1953-04-16 포로교환 참관협의 및 4/24 안보면담 원문 기반 심화: `data/politicians/pass-237-actor-overlays.json`.
- 이승만 4/30 Clark 친서 8조건, 한국 국회 6인 참관결의(미군 보고), 미국 EVERREADY 계획(실행 미확인)을 `data/events/pass-237-armistice-actions.json`, `data/claims/pass-237-adversarial.json`, `data/documents/pass-237-frus-april-may.json`로 연결.
- `data/annals/1953-april-may-armistice-command.md`, `data/research/debt/pass-237-targeted-debt-review.json`, `data/research/coverage/pass-237-coverage-overlay.json` 및 34개 문서특정 후속 lead 참조. 원문전사 47건, 원본이미지 0건, 엄격 3계열 교차확증 0건.

- Pass237B 1953-04-29 국내 동시대 신문 6개 원문전사: 신중목 농림장관 비료배급 담화, 백두진 대변인 타스카 회담, 이승만 환도·농민회·휴전 기자회견을 `data/politicians/pass-237b-korean-actors.json`로 연결. 농민회 통합/농협법 제정·비료배급·구호양곡 실제 집행은 OPEN. `data/research/debt/pass-237b-domestic-debt.json`.

## Pass239 1953년 5월26일~6월7일 정치인·기관 그래프 (2026-10-28)
- Actor overlay A: `data/politicians/pass-239-actors.json`. 기존 10명 심화, 신규 candidate 6명(소선규·박충식·김완용·이상덕·이임도·유재흥). 신원·생몰·정식 임명은 별도 원본 확인 전 승격 금지.
- Actor overlay B: `data/politicians/pass-239b-actors.json`. 유완창(兪莞昌, 1906년생·사망 미상) AKS E0081271과 1953-06-06 관재청장 기자회견을 근거로 `pol-yu-wan-chang` 독립 실록·증거 활성화. 1953년 9월 사령 원본 등 OPEN.
- 독립 실록 `data/annals/yu-wan-chang.md`, `data/annals/pyun-yong-tae.md`, `data/annals/choi-duk-shin.md`에 1953년 5~6월 개별 행위와 주장·대통령 명령 귀속의 한계를 분리했다.
- 대통령기록관 1953-06-05 이승만 환율 원담화의 부정어 '아니요'와 동시대 신문 전사의 부정어 누락은 `CLM-P239B-fx-opposite`로 CONFLICTED 보존. 정치적 평가가 아닌 텍스트 대조다.
- 문서 `data/documents/pass-239-may-june-source-registry.json` 및 `data/documents/pass-239b-june2-6-sources.json`: 직접 열린 114개 페이지 중 동일 원작성 9개, 원본 아닌 기록해설 2개, 2차 인명항목 1개를 제외한 고유 102개. PDF 원본 이미지 0건.
- 사건 `data/events/pass-239-may-june-governance.json`, `data/events/pass-239b-june-policy-graph.json`, `data/events/pass-239c-actor-corrections.json`: 신규 55개, 국회·재정·농정·교육·노동·보건·복지·산업·치안·문화·수산·국유재산·외교안보.
- 주장 `data/claims/pass-239-adversarial.json`, `data/claims/pass-239b-adversarial.json`: 반증/산술/시기차이 31건. 출처 계열의 엄격한 3중 독립확증 0건은 과장하지 않는다.
- 후속 조사 `data/research/leads/pass-239-next-queue.json`: 초기 37개+추가 40개=77개. 처음 실행요약의 '35개'는 계산 착오이며 correction ledger와 HISTORY_DEBT에 이력 보존.
- 실행결과 `data/research/runs/pass-239-summary.md`와 `data/research/runs/pass-239-execution-ledger.json`. 기존 stable ID와 데이터 API 유지, Floot 미수정.

## Pass239D 1953-06-08~22 행위자·명령 그래프 (2026-10-28)
- `data/politicians/pass-239d-actors.json`: 10명 검토, 7명 구체행위 심화, 3명 직책 맥락만 확인(직접행위 단정 금지).
- 원용덕 `pol-won-yong-duk`은 기존 pass53/pass65 후보를 canonical로 승격. `data/annals/won-yong-duk.md`, `data/evidence/won-yong-duk.json` 별도 독립 실록.
- 사건·원문·주장: `data/events/pass-239d-june8-22-actions.json`, `data/documents/pass-239d-june8-22-source-registry.json`, `data/claims/pass-239d-adversarial.json`.

## Pass239E 1953-06-22~30 비대통령 인물 확장
- `data/politicians/pass-239e-actors.json`: 16명, 신규 IDENTIFIED 후보 7명. 국회 6/30 신형식 사건의 발언자·이견을 별도 노드로 보존.
- 박술음 `cand-p236-park-sul-eum`을 기존 ID 유지한 채 ANNALS_ACTIVE로 승격: `data/annals/park-sul-eum.md`, `data/evidence/park-sul-eum.json`.
- 신형식의 논쟁적 발언은 `CONFLICTED` 유지, 형사·정치적 유죄판정이나 순위화 금지.
- 정당·사회부·농림부·관재청·대한노총 등 기관 9개 stable ID: `data/organizations/pass-239e-1953-institutions.json`.

## 2026-10-29 pass239J · 1954–1955 조약·경제협정·군사원조 행위자
- 1954-07~1955-08 비대통령 12명 심화/후보: `data/politicians/pass-239j-1954-diplomacy-economy-actors.json` (기존 10명 + 신원 미확정 후보 최순주·김정렬 2명; 승격 전 한글/한자/임명원부 필요).
- 외무차관 조정환 1954-09-01 FRUS d934 확인. 변영태 1954-11-17 합의의사록 서명, 손원일 11/18 조약 공포, 백두진 7월 경제조정관, 양유찬 1955-08-12 500:1 수정 서명으로 각각 독립 행위 분리.
- 문서 `data/documents/pass-239j-1954-agreed-minute-ratification.json`, 사건 `data/events/pass-239j-1954-1955-actions.json`, 주장 `data/claims/pass-239j-treaty-aid-currency-adversarial.json`, 실록 `data/annals/1954-1955-treaty-minute-currency-actor-chain.md`. FRUS는 한 편찬계열, 한국 법제처는 별도 정부 원문계열.

- pass239J 증거원장 최종 동기화(2026-10-29): `data/evidence/pyun-yong-tae.json`, `data/evidence/cho-chung-whan.json` 신규 독립 원장; 기존 `data/evidence/rhee-syngman.json` chronology 3건·source 5건 추가. 변영태와 조정환은 증거원장+개인 annals 확보를 근거로 연구상태 ANNALS_ACTIVE 승격. 출생/사망·임명원부 미확인은 그대로 OPEN.


## 2026-10-29 pass239K · 1955년 국정·경제·안보·정당
- 정치인 14명 심화, 신원 미확정 신규 후보 5명: data/politicians/pass-239k-1955-actors.json. 이후락 Hu Rak Lee 신원은 군무관 사령 전 잠정.
- 손원일 ANNALS_ACTIVE 승격: data/annals/sohn-won-yil.md, data/evidence/sohn-won-yil.json. 한국 공식 조약 제34호와 미국 FRUS 1955 회담 기록을 분리.
- 이후락 후보 독립원장: data/annals/lee-hu-rak.md, data/evidence/lee-hu-rak.json.
- 문서 71 객체(70개 직접 열람, UN A/2711 1개 미열람): data/documents/pass-239k-1955-first-half.json; 사건 20: data/events/pass-239k-1955-first-half.json; 주장 16: data/claims/pass-239k-1955-adversarial.json; 기관 4: data/organizations/pass-239k-1955-reconstruction.json.


## 2026-10-29 pass239K · UNCURK A/2711 원문 교차검증
- UN 1954 원문 A/2711: data/annals/1954-uncurk-assembly-election-administration.md. 1954-08-09 민정이양 권고 5:1, 08-12 UNC 이승만 준비 통지, 실제 인계 미확정.
- 1954 총선 자유당 **당선 114**(선관위)와 1954년 8월 자유당 **원내 136**(UN)는 시점·모집단 차이. 무소속동지회 31명 지도자 곽상훈은 호헌동지회와 병합하지 않음.
- 1954 UN 내각명단 이중재·강성태 실명확인(1955 3월 연속재임 잠정), 최규옥·조용순·이선근·백한성·이광 신규 후보. data/politicians/pass-239k-1955-actors.json.
- 곽상훈 VERIFIED 독립 원장: data/evidence/kwak-sang-hun.json, data/annals/kwak-sang-hun.md. 손원일 ANNALS_ACTIVE 유지.
- 총 문서 객체 73개 모두 직접 열람, 원문/공식1차 65개, 비대통령 20명 보강, 사건 28개, 명제 21개, 새 lead 50개, 기존 14개 추적. FRUS 63개는 하나의 미국 편찬계열.

## Pass239L · 1955~1956 NNSC·선거·정당 독립 인물 확장 (2026-10-29)
- `data/politicians/pass-239l-1956-actors.json`: 17명 actor overlay, 신규 candidate 5명(인태식·김현철·이익흥·박기출·P.W. Han). 한자·생몰·임명일 미확인. P.W. Han과 한표욱 **자동병합 금지**.
- 조봉암·장면 `ANNALS_ACTIVE` 독립 실록: `data/annals/cho-bong-am.md`, `data/evidence/cho-bong-am.json`, `data/annals/chang-myon.md`, `data/evidence/chang-myon.json`. 신익희 기존 실록에 1956 선거·사망 후속 추가.
- 1956 선거 득표율 분모, FRUS 원작성 55건, UNGA 결의 910(X), 진보당 강령을 문서/사건/주장 그래프로 연결. FRUS 편집자 주석 d105·116·146·159는 원작성 문서 계수에서 제외.
- `data/research/leads/pass-239l-next-queue.json`: 구체 원문 표적 45개, 기존 lead 11개 추적. 주간 전수조사 미실시.

## Pass239L2 · UN A/2947 원문·1955 내각·1956 선거 보강 (2026-10-29)
- `data/documents/pass-239l2-1955-un-original-election-catalog.json`: UN A/2947 원문 PDF OCR 115,022자 직접 확인, 민주화운동기념사업회 선거 컬렉션·경향신문 사진목록 2개·서울기록원 주제해제. 사진 목록과 원사진 시각검증은 다름.
- `data/politicians/pass-239l2-1955-cabinet-election-actors.json`: 1955 정부 각료 및 1956 선거 인물 22명, 그중 신규 candidate 12명. UN 공식 부록에 근거한 각료는 IDENTIFIED, 후대 선거등록 후보는 DISCOVERED로 보수적으로 관리. 김현철은 UN 1955 재무장관 임명 근거로 VERIFIED(생몰·한자 미검증).
- `data/events/pass-239l2-1954-56-un-economic-cabinet-election.json`: 민정이양 실제 완료, 헌법개정, 정부조직법, 각료 인사, 예산·물가·산업·농정, 1956 후보등록·사퇴·취임 등 사건 28개.
- `data/claims/pass-239l2-un-adversarial.json`: UN vs FRUS 변영태 사임 07-30/08-01 충돌, 1954 개헌 날짜 충돌, 1955 농림장관 불신임 여당 참여, 환율조정 전 인플레이션 등 반증명제 12개.
- `data/research/leads/pass-239l2-next-queue.json`: 새 원문 표적 30개. A/2947 접근부채 RESOLVED, OCR 원PDF 이미지 대조 별도 OPEN. 주간 전수조사 미실시.


### pass242 (2026-10-29): 1957 감군·재정·평시 국정
- `data/politicians/pass-242-1957-actors.json`: 김정렬(1957 국방장관, 金貞烈, Kim Chung-yul), 유재흥, 백선엽, 조정환, 장면, 김현철, 양유찬, 윤길중, 조봉암, 송인상, 이한빈, 정재설, 손창환, 이기붕, 조병옥, 장택상 등 16명 연구 심화.
- 김정렬(1957)과 기존 잠정 1954 Kim Chong-yol 후보는 동일인 검증 원문 확보 전까지 silent merge하지 않는다. 인물 점수·선악판정 없음.


### pass243 (2026-10-29): 1958 감군·선거·신국가보안법·지방행정
- 원작성 미국 외교·군사·NSC 문서 50건: `data/documents/pass-243-1958-statecraft.json`. 이 50건은 미국 FRUS 단일 provenance 계열이며 facsimile 미확인.
- 한국 동시대 조선일보 1958-12-25 기사 전사, 국사편찬위원회 선거결과, 국가기록원 AA0002161 색인, 대법원 1959·2010 결정, AKS 후대 해제: 위 문서 registry에 별도 provenance 분리.
- 정치인 14명 overlay: `data/politicians/pass-243-1958-actor-evidence.json` (1차 원문 직접 이름 확인 9명, 2차 해제 확인 3명, 문서상 익명 각료 추정 2명은 미확정 후보로 격하). 기존 stable ID 유지.
- 사건/하위사건 18개: `data/events/pass-243-1958-statecraft.json` (기존 1958-12-24 상위 사건과 교차연결).
- 상충 명제·반증 17개: `data/claims/pass-243-1958-adversarial.json`. 1958 선거 FRUS d222 편집주석 137석·90.6%와 국편 126석·87.8% 충돌; 조봉암 1/13 체포는 2010 대법원 결정의 국가기록원 형사사건기록 인용으로 강하게 좁힘.
- 후속 원문 표적 48건: `data/research/leads/pass-243-1958-next.json`. 독립 3계열 원문 확증은 0, 미해결은 역사부채로 보존.

- pass243 추가 검증: FRUS d222 편집주석을 원문과 별개 2차 편집자료로 등록. 자유당 137(6/4 평가)과 126(5/2 당선)의 차이는 무소속 11명 입당 가설로 NARROWED, 원 국회 소속변동원장 확보 전 미확정. 원문표적 50개.

- `data/politicians/pass-244-1959-1960-actors.json` (2026-10-29; 16 actor evidence overlays)
- `data/politicians/id-aliases-pass244.json` (legacy ID resolver; not additional people)

- `data/politicians/pass-244g-1960-drafting-actors.json` (pass244g; 2026-10-29)

## pass246 1956~1960 인물·관보·선거법 (2026-10-29)
- 중앙 정치인 registry: 기존 10명 한자·부처·시기별 직책 IDENTIFIED, 신규 전택보(全澤珤) IDENTIFIED, 6/15 개헌 반대표 보도 이옥동·김공평·김창동 DISCOVERED. 생몰·임면원장 미확인.
- cand-p245-lee-ong-jun: 동일 관보1965 법률469 이옹준/470 이응준 및 1956 李應俊 충돌, 기존 ID 유지·자동병합 금지.
- cand-p245-oh-jeong-su: 5/11·6/23 吳楨洙 대 7/1 吳植洙 충돌.
- 허정/곽상훈 개헌 후 권한대행 즉시승계는 원관보 반증으로 CONFLICTED.
- 자료: data/politicians/pass-246-1956-1960-actor-deepening.json ; data/events/pass-246-1956-1960-constitutional-institutional-actions.json ; data/claims/pass-246-1956-1960-adversarial.json.

## pass247 (2026-10-29)
- `data/politicians/pass-247-1960-party-network.json`: 신규 후보 6명·기존 4명 심화.

## pass247b (2026-10-29)
- `data/politicians/pass-247b-succession-and-administration.json`: 백낙준 신규·곽상훈 권한대행 이력 NARROWED.

## pass247c (2026-10-29)
- `data/politicians/pass-247c-june1960-original-actors.json`: 신규5명·기존 원전 심화.

## pass247d (2026-10-29)
- `data/politicians/pass-247d-assembly-actors.json`: 민장식·변진갑·최규남·고담룡 신규4명, 기존 심화.

- 2026-10-29 pass247e 중앙 registry 호환 통합: `data/politicians/pass-247e-1960-legislative-actors.json` 후보5명/기존14명 보강. 최규남 두 노드는 신원 미확인으로 병합하지 않음.

- 2026-10-29 pass248: `data/politicians/pass-248-1960-election-actors.json` (1960 지방선거·김상돈·출처충돌 검증).

- 2026-10-29 pass249: `data/politicians/pass-249-civil-rights-actors.json` (신규 후보 16명; 1961 공민권 제한·의회 이의, 동명이인 병합 보류).

- pass249 1961-02-02 심사위원 후보는 직접 열린 DOC-P249-KD-0202 전사로 연결; 실제 위촉원부는 OPEN.


## Pass250 (2026-10-29)
- 신규 VERIFIED 독립 정치인 `pol-ji-cheong-cheon`: 독립기념관 인명사전과 미 OIR No.5824로 확인. 생일 음력/양력·실제 출마는 OPEN.
- `data/politicians/pass-250-1952-actors.json`: 기존 정치인 10명 동시대 문서 연결 후보. 단순 언급과 직접 행위는 구분. 이범석 중복 ID는 자동병합하지 않음.

- 2026-10-29 pass252: `data/politicians/pass-252-1952-aug20-27-actors.json` 기존 정치인 17명 심화, 칠곡 면장 박봉희 후보 1명 신규. 김시현은 pass229의 `cand-kim-si-hyeon-1952`를 중앙 registry에 승격하고 중복 candidate를 정정·폐기(정정 이력 보존). `data/annals/shin-ik-hui.md`, `data/evidence/shin-ik-hui.json` 독립 실록에 8/22~24 증거 추가.

- 2026-10-29 pass252B/C: `data/politicians/pass-252b-1952-aug26-30-actors.json` 기존 14명 심화·신규 함인섭/이진수 2명; `data/politicians/pass-252c-1952-aug31-actors.json` 기존 백선엽·배은희·백두진·신중목 4명 심화·신규 김종원/손권배 2명. 기존 백선엽 `pol-paik-sun-yup` 재사용해 중복 ID 미생성.

- 2026-10-29 pass255: 1952-09-26 자유당 전국대회 대통령 연설·동아일보 대조, 이활 신규 DISCOVERED 및 윤재욱·이갑성 기존 ID 심화. `data/politicians/pass-255-actor-overlay.json`, `data/evidence/pass-255-actor-evidence.json`, `data/annals/1952-sep26-maritime-party-prices.md`. 이범석 중복 stable ID는 병합하지 않음. 해상방위구역·손원일 일본인 상륙 체포 지시 전언을 한국정부 원명령으로 확정하지 않음.

- 2026-10-29 pass255B/C: 신규 DISCOVERED 5명(정문후·원상복·연일수·이신우·김봉재) `data/politicians/pass-255b-actor-overlay.json`; 기존 비대통령 인물 31명에 걸친 총 49개 새 actor-evidence 링크 `data/evidence/pass-255-actor-evidence.json`, `data/evidence/pass-255b-actor-evidence.json`, `data/evidence/pass-255c-actor-evidence.json`. 원임명·생몰·당적 미확인 후보는 VERIFIED 승격 금지.

- 2026-10-29 Pass255H: `data/politicians/pass-255h-actor-overlay.json` (원문 출처·불확실성 보존).
- 2026-10-29 Pass255H 사후 ID 교정: 신규 후보 2명(모윤숙·최주일), 기존 candidate 5명 심화. 지연해 한자 池連海/池蓮海는 충돌로 보존. `data/politicians/pass-255h-actor-overlay.json`.

- 2026-10-29 pass256: 1952-11 이갑성 총리지명·이윤영 부결 보도, FRUS d323 정변설 미측 반대평가 재검토: `data/politicians/pass-256-actor-evidence-overlay.json` (기존 한국 정치인 ID 10명, 신규 0명). 이갑성 독립 실록 `data/annals/lee-gap-seong-1952.md` 및 증거 `data/evidence/lee-gap-seong-1952.json`. 미확인 정변설을 사실로 승격 금지.

- 2026-10-29 pass256B/C: 1952-11-17 이갑성 총리인준 연기 요청 및 이승만 면담·외자구매처 일임 유시 보도. `data/politicians/pass-256-actor-evidence-overlay.json`에서 기존 ID 유지, `data/evidence/lee-gap-seong-1952.json` 추가 근거. 농림부 익명 국장·성명 미확인 김 국방부차관·개척단 민간인을 정치인으로 자동 등록하지 않음. 원문 `data/documents/pass-256b-1952-nov17-domestic.json`.


## Pass257 (2026-10-29): 1953-02 자유당 서울시당·경찰책임·전시 행정
- `data/politicians/pass-257-1953-party-policing-evidence.json`: 김일수(金一秀) 자유당 서울시당 조직부장 신규 IDENTIFIED 후보, 진헌식 내무장관의 1953-02-05 경찰/검찰 수사책임 발언, 이승만의 1953-02 서울환도·2/6 인터뷰 원문 연결. 신규 후보 1, 기존 2 보강. 이름·한자·동명이인 원명부 확인 전 VERIFIED/ANNALS_ACTIVE 자동승격 금지.
- `data/annals/1952nov-1953feb-crossprovenance-governance.md`, `data/documents/pass-257-1952nov-1953feb-crossprovenance.json`, `data/events/pass-257-pow-economy-governance.json`, `data/claims/pass-257-adversarial-crossprovenance.json`에 증거·사건·반증을 분리. 1952-11-24 중국 거부 각서는 인도/미국 2계열, UN 610 채택은 인도/미국/UN 3계열. UN PDF 접근 403은 BLOCKED lead로 유지.

- **Pass257C 국내 원문 확장**: 1953-02-06 민주신보에 직접 실명 확인된 조정훈·조순·서이환·이동환 의원 4명을 `IDENTIFIED` 후보로, 1953-02-06 조선일보의 진승국·박용만·김창민 3명을 정치사회단체 결성준비 `DISCOVERED`로 분리. 기존 이갑성·배은희·신중목·진헌식 심화, 김석관은 1952-11 원기사에 성씨 金만 있어 기존 ID에 `OPEN` identity bridge만 남김. 1953 조순과 1954 조순은 동일인 원명부 확인 전 병합하지 않음. 김일수 독립 evidence: `data/evidence/kim-il-su-1953.json`.

- **Pass257J 김유택 독립 실록 활성화**: `cand-p235i-kim-yu-taek` 후보 ID 유지(기존 참조 호환), 한국은행 공식 총재약력으로 1951-1956 총재·1961 장관·1963 국회의원 경력 검증. `data/annals/kim-yu-taek.md`, `data/evidence/kim-yu-taek-1953-currency.json` 추가. `data/politicians/pass-257j-actor-evidence.json`에 백두진·이승만과 직책별 책임 분리.

- **Pass257K 국회·노동 행위자 심화**: 신익희 국회의장 1953-04-22 근로기준법안·05-15 전시근로동원법안 이송, 박술음 사회부장관 및 백두진 총리서리 04-14 노동조합법 시행령 제782호 서명. `data/politicians/pass-257k-labor-institution-actors.json`에 기록. 원송부/서명 이미지 미확보.

- **Pass257M 경제정책 발언자 심화**: 김유택 1953-03-04 추가통화조치 부인, 이승만 8700만달러 상환예정, 백두진 8500만달러 청산완료 발언. `data/politicians/pass-257m-finance-public-claims.json`; 당사자 발언은 회계사실로 단정하지 않음.

- **Pass257N 국회 의원 17명 실질 심화**: `data/politicians/pass-257n-1953-finance-legislators.json` 중앙 registry 동기화. 신규 후보 권중돈·엄병학·이종현(1949 장관과 identity 분리) 3명. 무기명표결 개인찬반 귀속 금지, 분파 표기 원문 보존. 권중돈 사망 1983/1985 CONFLICTED.

- 2026-10-29 Pass257O: `data/politicians/pass-257o-1953-1954-identity-audit.json` (기존 5인 선거구·당적·보궐선거 신원 오독 방지).
- 2026-10-29 Pass257O2: `data/politicians/pass-257o2-1954-election-diplomatic-actor-overlay.json` (미국 원문 1954년 관찰 10인; 기존 ID 재사용, 신원승격 없음).

- 2026-10-29 Pass257O4: `data/politicians/pass-257o4-parliamentary-cabinet-actors.json` (최순주 candidate, 백두진·변영태·곽상훈 원문 인사·의정행위).

- 2026-10-29 Pass257P: `data/politicians/pass-257p-unkra-housing-local-actors.json` (기존 이승만·백두진·김태선 3개 ID 재사용, 사진 캡션·행사·법령연혁의 증거수준 분리; 중앙 `data/politicians.json` 연결 동기화; 신규 정치인/승격 0).

- 2026-10-29 Pass257Q: `data/politicians/pass-257q-1954-cabinet-actors.json` 21개 장관·국무위원 시간귀속 기록, 신규 candidate 5명, 기존 16명. 중앙 registry additive 반영.
- 2026-10-29 Pass257R 1954 선거구별 16인(기존13·신규후보3) 독립 인물 연구. `data/politicians/pass-257r-1954-election-governance-actors.json`.

- 2026-10-29 Pass257S: `data/politicians/pass-257s-1954-visit-nnsc-actors.json` 기존 10인 역할 심화·최순주 신규 candidate 1명; 생몰·한자 원문 미확인.
- 2026-10-29 Pass257T 이승만·원용덕·변영태 원문발언과 정책·행위 구분 보강.

## Pass257W 1954 총선·제네바·개헌 actor (2026-10-29)
- `data/politicians/pass-257w-1954-election-geneva-actors.json`: 변영태의 1954-05-22 제네바 원작성 미대표단 보고, 임철호·이선근 개헌추진위 후대 해설, 신규 이범녕 `cand-p257w-lee-beom-nyeong` DISCOVERED. 신규 후보는 `data/politicians.json`에도 additive 등록; 한자·생몰·임명원본 미확인.
- 관련 문서 `data/documents/pass-257w-1954-election-un-geneva-registry.json`, `data/documents/pass-257w2-1954-cabinet-industry-sources.json`; 사건 `data/events/pass-257w-1954-election-geneva-actions.json`, `data/events/pass-257w2-1954-cabinet-constitutional-actions.json`; 주장 `data/claims/pass-257w-1954-election-adversarial.json`, `data/claims/pass-257w2-1954-cabinet-provenance-conflicts.json`; 실록 `data/annals/1954-election-geneva-constitutional-source-audit.md`.

### Pass257W-UN 동시대 정부 명부 원문으로 22명 심화
- `data/politicians/pass-257w3-uncurk-1954-cabinet-assembly-roster.json`: UNCURK 1954 A/2711 Annex II 장관·국회의장·부의장 22명, 날짜별 임면·선출. 기존 20명 + 신규 로마자 잠정후보 Yoon Kun-Joong, Choi Kyoo-Ok 2명; 둘은 기본 `data/politicians.json`에도 IDENTIFIED로 추가. 한국어/한자 미확인 상태에서 임의 병합 금지.
- 유엔 본문·부록의 자유당 115/114 1석 불일치, 문교부장관 김법린 퇴임일 2/5 vs 4/20, 총리 백두진/변영태 발표일·지명일 구별. `data/annals/1954-election-geneva-constitutional-source-audit.md` §7.
- 독립 event 13개 추가 `data/events/pass-257w3-uncurk-1954-election-aid-cabinet-actions.json`, 원문 `data/documents/pass-257w3-uncurk-1954-original.json`.

- Pass257W4 신원 승격: UN Annex II `Yoon Kun-Joong` = 한국학중앙연구원 `윤건중(1897~1987)`, 1954-05 농림부장관. `cand-p257w-un-yoon-kun-joong` ID 보존, 기본 registry 연구상태 VERIFIED; 한자·원임면 관보는 OPEN. `Choi Kyoo-Ok`은 로마자 잠정 유지.

- 2026-10-30 Pass258A: `data/politicians/pass-258a-1954-actor-actions.json` (1954 FOA 원조 원문 및 1954 한미·총선 반증, 기존 FRUS canonical ID 재사용; Floot 변경 없음).

- `data/politicians/pass-258b-1954-rhee-aid-proposal.json` (이승만 1954-06-09 원조통제 개편 제안; 기존 stable ID 재사용, 승격 없음)
