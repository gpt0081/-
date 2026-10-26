# Politician Network Pass 110 — execution ledger

Date: 2026-09-24
Focus: pass 109의 지방 선거행정망을 중앙 자유당/내무부 명령선과 국가기록원 지방 판결 corpus에 접속.

## Progress
- 직전 pass 109 ledger와 연구문서를 읽고 김학응 단일 검색 반복 대신 중앙 명령선, 득표율 하향조정, 지방 판결 원문 corpus, 충북·경남 확장, FRUS contemporaneous observation으로 전환했다.
- 가장 중요한 진전은 `90% 초과→85%` 김학응 진술이 고립된 이상치가 아니라는 점이다. 1960-05-24 검찰 발표는 자유당 측이 95% 이상 보고를 80% 내외로 조정하라고 최인규에게 지시했고 최인규가 각 도경국장에 공문을 보냈다고 설명한다. 압수됐다는 한희석 지시문 원문이 다음 최우선 표적이다.
- 중앙 집행망을 경찰선(이강학)과 지방행정·교육선(최병환)으로 분리했다.
- 한희석의 `경무대 미보고/이승만 책임 없음` 진술을 기존 설명을 반박할 수 있는 actor statement로 보존했다. 자기방어 진술이므로 결론으로 채택하지 않았다.
- 강원·전남·전북·경북·경남 국가기록원 생산 판결문 객체를 직접 확인했다. 지방 actor별 인정사실을 페이지 단위로 채굴할 수 있는 409쪽 규모 corpus다.
- 전남의 1961-09-14 요약(이하영 5년)과 1961-11-10 국가기록원 판결(이하영 4년)의 충돌을 발견해 절차관계 open lead로 만들었다.
- 최병환·이성우·김정렬·김일환·곽의영·최순교·이정용·신도성·이수응·최남규·정인택·김상기·이기영·이헌구·박흥용 등 15 actor를 신규/심화 구조화했다.
- Floot는 수정·빌드하지 않았다.

## Counts
- Independent high-priority research/retrieval lines materially pursued: 22.
- General domains materially touched: 7 (선거, 중앙행정, 지방행정, 경찰행정, 교육공무원 동원, 정당조직, 사법/혁명재판; FRUS를 통한 외교 관찰도 보강).
- Non-president actor nodes newly structured/deepened: 15.
- Event/sub-event candidates newly structured/deepened: 12.
- Meaningful unique documents/pages directly opened/reviewed: 29. 이 중 공식/공공 아카이브 또는 동시대 외교문서 계열 22. 목표 40/20 중 총문서 수는 미달, 공식·1차계열 목표는 달성. 판결문 5건은 메타데이터/첫 페이지를 직접 확인했으며 전체 409쪽 본문은 이번 실행에서 모두 읽었다고 계산하지 않았다.
- Adversarial/identity/provenance checks: 12.
- Existing open leads materially followed/narrowed: 10 (김학응 85%, 중앙→지방 명령, 경찰선, 지방행정선, 경무대 보고, 지방 판결, 경북, 경남, 충북, 이승만 인지시점).
- Cross-check bundles: 4 (득표율 하향조정; 중앙 명령선; 지방 판결; 이승만 인지/외국관찰).
- Concrete next leads generated: 40.

## Cross-check bundles
1. 득표율 하향조정: 김학응 수사 진술 ↔ 1960-05-24 검찰 발표/압수 지시문 존재 주장. 방향 일치, 수치 차이는 OPEN.
2. 중앙 명령선: 최인규-이강학 대질/검찰 발표 ↔ 최병환 진술 ↔ 한희석 상반 책임진술. 경찰·지방행정·정당 의사결정을 분리.
3. 지방 판결: 특별재판 사진/공판 메타 ↔ 국가기록원 생산 혁명재판 판결문. 동일 사건의 절차단계를 silent merge하지 않음.
4. 대통령 인지: FRUS 3월 선거 전 외국 관찰 ↔ 4월26일 이승만의 4월25일 전면인지 주장 ↔ 김 국방장관의 group voting 사전인지 진술. 직접 사전명령은 여전히 확인되지 않음.

## Files changed
- `data/research/rhee-pass-110-central-provincial-election-chain-2026-09-24.md`
- `data/research/candidates/pass-110-central-provincial-actors.json`
- `data/research/runs/2026-09-24-politician-network-pass-110.md`

## Commits
- `d3266c253de8b2c968b45f17aa9bf851cd9d5c8a` research: recover central-provincial 3.15 command and judgment chain
- `5ef184421af5c04c08cbe586530b03ad9af6258b` data: structure central-provincial election actor expansion
- this ledger commit: see commit containing this file

## Next priority
409쪽 지방 판결 corpus의 본문을 피고별로 직접 추출하는 것이 최우선이다. 동시에 1960-05-24 압수 `득표율 삭감 지시문`, 최인규→도경국장 공문, 김학응 피의자신문조서를 회수하면 중앙→도 단위 command edge를 주장/검찰발표 수준에서 문서 수준으로 올릴 수 있다. 그 다음 6인위원회 원 회의록/공소장과 자유당 당무회의 원문을 대조한다.

역사부채 주간 전수조사 미실시.
