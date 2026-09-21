# Run report — Politician Network Pass 55

Date: 2026-09-21
Focus: 반공포로 석방의 camp-level 지휘관·사전인지·조직 provenance 검증

## Result
Pass 54에서 강해진 `이승만 -> 원용덕/군사경찰` 지휘선을 이번에는 반대 방향으로 검증했다. 이승만의 당사자 서한(FRUS 607), Clark의 군 전문(FRUS 612), 공공 2차 종합(AKS)을 분리해 보니 대통령 직접 결정과 원용덕 별도 헌병선은 강하지만, 6월6일 경무대 계획지시의 원 명령서와 8개 수용소별 한국군 지휘관·수신명령은 여전히 비어 있다. 백선엽·신태영의 사전인지도 원문으로 확인되지 않아 책임을 확장하지 않았다. 동시에 1952년 FRUS 자료를 비교해 일반 경찰, 군사경찰/헌병, 육군, 궁정경비를 별도 organization/action chain으로 유지해야 함을 보강했다.

## Counts
- 독립 연구선: 20 (6/6 계획지시, 6/18 대통령서한, 원용덕 직속성, camp 8개, camp 지휘관, Herren/KCOMZ, 백선엽 사전인지, 신태영 사전인지, 내무부, 도지사, 일반경찰, 궁정경비, casualty, 부평, UNC 사전경고, 워싱턴 외교대응, Robertson 협상, 상호방위조약 인과, 7월공세 인과, 석방자 사후관리)
- 이번 회차 웹에서 직접 열어 확인한 유의미 자료: 20+ 페이지/문서. 이 중 FRUS 공식 원문이 다수이나 Pass 54와 중복 검토가 있어 신규 고유 40건이라고 기록하지 않는다.
- 공식·1차·동시대 원문: 15+ 확인. FRUS XV/1·XV/2 중심.
- 일반 국정영역: 7 (국방, 군사행정, 외교, 내무/경찰, 지방행정, 헌정·정전정책, 전후 사회관리)
- 비대통령/관련 actor 신규·심화: 10 (원용덕, 백선엽, 백두진, 변영태, 양유찬, 신태영, 손원일, 진헌식, Thomas Herren, 성명 미확정 궁정경비대장 Kim). 외국 군인과 미확정 인물은 한국 정치인 registry가 아니라 candidate/external graph에만 둠.
- event/sub-event 신규/보강: 8 (military-police order, camp takeover, force confrontation risk, Washington diplomatic crisis, armistice-opposition policy, Robertson negotiations, provincial protection order, 1952 palace-security comparison event)
- adversarial checks: 10
- cross-provenance 묶음: 3 (Rhee letter vs Clark military report; FRUS contemporaneous vs AKS synthesis; 1952 UNC police/military separation vs 1953 command-chain interpretation)
- 추적 open lead/debt: 8
- concrete next leads: 40

## Interpretation changes
1. `6/6 이승만→원용덕 계획수립 지시`는 중요한 lead지만 현재 확보한 직접 근거가 AKS 공공 2차자료이므로 1차 명령 사실과 동일 등급으로 두지 않는다.
2. `백선엽 사전인지`와 `신태영 작전지휘`는 현 단계에서 확인되지 않았다. 직책만으로 석방 집행책임을 확대하지 않는다.
3. Herren는 한국 정치인 노드는 아니지만 POW camp administration과 6/19 UNC takeover를 잇는 핵심 external actor다. 장기적으로 event/document graph가 한국 정치인 registry 외 external-person ID를 수용해야 한다.
4. 1952년 자료에서 UNC는 ROK police와 military establishments를 별도 통제 대상으로 기록한다. 1953 사건에서도 일반경찰·헌병·육군을 합치지 않는 현재 모델이 타당하다.
5. 8개 camp의 전체 명칭·지휘관·탈출/잔류/사상자 표가 확보되기 전에는 `모든 camp에서 같은 명령·같은 방식`이라고 일반화하지 않는다.

## Files
- `data/research/rhee-pass-55-pow-camp-command-provenance-2026-09-21.md`
- `data/research/candidates/pass-55-pow-camp-command-actors.json`
- `data/research/runs/2026-09-21-politician-network-pass-55.md`

## Commits
- `2f5eed0aca1605e44e1052e6b23267f9d5b96f0d` research dossier
- `6cfec147e287b772618f4d8dce776cae5ab249c5` actor candidates
- this run-report commit

## Limitations
이번 회차는 자료 접근성과 실행시간 내에서 40개의 **신규 고유 원문** 하한을 달성하지 못했다. 반복 FRUS 구간을 숫자로 부풀리지 않았다. 국가기록원/국방부 군사편찬 자료의 원 명령철과 KCOMZ camp reports가 다음 병목이다. 정식 `politicians.json`·`events.json` 승격은 한국측 원문 없이 책임 귀속을 과도하게 확장할 위험이 있어 보류했다.

## History debt
역사부채 주간 전수조사 미실시. 일요일 첫 실행이 아니다.

## Floot
수정·빌드하지 않음.
