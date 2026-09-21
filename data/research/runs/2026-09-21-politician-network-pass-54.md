# Run report — Politician Network Pass 54

Date: 2026-09-21
Focus: Pass 53의 반공포로 석방 지휘선을 헌병/군사경찰·지방행정·정전복구 협상으로 확장

## Result
이번 회차는 직전 run의 40개 lead 중 가장 높은 불확실성인 `대통령 -> 원용덕 -> 수용소 경비` 명령선을 우선했다. 이승만의 6/18 Clark 서한에서 `Korean military police`에 직접 석방을 명령했다는 문구를 재확인하고, FRUS 612의 `Won acts directly under President Rhee` 및 FRUS 616의 변영태 설명을 결합해 일반 육군 지휘계통과 헌병총사령관 별도선을 더 명확히 분리했다. 동시에 대통령 성명의 도지사·경찰 보호지시를 별도 지방행정 sub-event로 분리했고, Robertson 임무의 조약·경제원조·정치회담 패키지를 연결했다.

## Counts
- 독립 연구선: 20 (대통령 명령문, 군사경찰, 원용덕 직속성, 백선엽 일반지휘선, 8개 camp, 잔여포로, casualty, UNC takeover, 미-ROK 충돌위험, 도지사, 경찰, 내무부, 국방부 사전인지, 총리 외교, 외무부, 정전대표, 경제원조, 20개 사단, 상호방위조약, 정치회담)
- 이번 회차 직접 열어 검토한 문서/원문: 44+ (FRUS 606-646 연속구간 중 41개 문서 페이지 + 한국민족문화대백과 + UN S/3043 + 한국사DB FRUS mirror 등). 단 Pass 53과 중복 문서가 많으므로 **신규 고유문서 40건으로 과장하지 않는다**.
- 공식·1차·동시대 계열: 대부분 FRUS/UN 공식 공개문서. 공공 2차자료는 원문 표적 생성에 한정.
- 국정영역: 8 (국방·안보, 외교, 지방행정·경찰, 행정, 재정/경제원조, 군사조직, 정치회담/헌정, 사회구호 후속)
- 비대통령 actor 신규/심화: 10 (원용덕, 변영태, 백선엽, 백두진, 양유찬, 신태영, 손원일, 진헌식, 최덕신, 황호현)
- event/sub-event 구조화/보강: 8
- adversarial checks: 10
- cross-provenance bundles: 3 (Rhee letter + Clark military report + Briggs/Pyun interview; FRUS + 한국사DB mirror; UNC/FRUS + UN S/3043)
- 추적 open lead/debt: 8
- concrete next leads: 40

## Interpretation changes
1. 집행기관은 막연한 `한국군`보다 `Korean military police / Provost Marshal chain`으로 쓰는 것이 현재 1차자료에 더 정확하다.
2. 백선엽 육군참모총장은 원용덕 명령선과 분리되어 나타난다. 따라서 육군참모총장에게 석방의 직접 집행책임을 자동 귀속하지 않는다.
3. 지방 경찰은 현재 확보된 1차자료에서 석방 실행보다는 석방자 보호지시의 수신자로 나타난다. 군사경찰과 일반 경찰을 혼동하지 않는다.
4. 상호방위조약·경제원조·20개 사단·정치회담은 6월 하순 하나의 협상 패키지로 연결되지만, 조약 offer와 경제원조 구상은 6/18 이전에도 존재하므로 석방 단일인과는 배제한다.
5. `Won의 미군 공격 명령`은 중요한 contemporaneous U.S. report지만 한국측 원 명령서가 없으므로 observed/reporting layer에 둔다.

## Files
- `data/research/rhee-pass-54-pow-command-chain-expansion-2026-09-21.md`
- `data/research/candidates/pass-54-pow-command-actors.json`
- `data/research/runs/2026-09-21-politician-network-pass-54.md`

## Commits
- `0abad01f35a3caf3497d1c547ecf25dbc113eb20` research dossier
- `d6deae82e016545effb2ca824245e580a157a2a5` actor candidates
- this run-report commit

## Limitations
repository의 정식 `politicians.json`, `events.json`, document/claim registry 전체 동기화는 이번 회차에서 보류했다. 이유는 원용덕/진헌식/최덕신의 한국측 원 명령·행정문서가 아직 없고, 기존 registry를 성급히 승격하면 candidate와 verified의 경계를 흐릴 수 있기 때문이다. 다음 회차는 camp별 명령서/지휘관과 내무부 보호지시 원문을 최우선으로 한다.

## History debt
역사부채 주간 전수조사 미실시. 일요일 첫 실행이 아니다.

## Floot
수정·빌드하지 않음.
