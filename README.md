# 눈가리고아웅판별기 · 대한민국 정치인 실록

> **눈 가리고 아웅. 기록은 눈을 감지 않는다.**

대한민국 정치인의 과거 발언, 공약, 표결, 정책 행동, 행정·입법·사법 관련 기록, 해명과 사건 관계를 시간순으로 연결해 사용자가 직접 원문과 앞뒤 맥락을 검토할 수 있게 하는 **정치 기록 추적·디지털 실록 프로젝트**입니다.

## 최상위 목적

이 프로젝트의 최종 대상은 역대 대통령만이 아니라 **대한민국 정치사의 주요 정치인·기관·정당·사회세력과 그 관계망 전체**입니다. 대통령은 시간순 탐색을 위한 하나의 backbone일 뿐 연구의 중심축이나 데이터 모델의 상위 계층이 아닙니다.

대한민국 정치사는 대통령만으로 설명되지 않습니다. 국회·정당·관료제·사법부·헌법재판·검찰·군·경찰·정보기관·지방정치·기업·노동·농민·시민사회·언론·사회운동·외교안보와 지역·계층·세대·젠더 등의 정치적 균열을 독립된 구조층으로 함께 추적합니다.

전체 좌표계는 `docs/KOREA_POLITICAL_FOREST.md`의 **시대 × 구조층** 지도를 기준으로 합니다. 연구의 기본 순서는 `시대/체제 → 제도 → 기관 → 정치·사회 세력 → 균열/정책영역 → 사건 → 행위자 → 문서 → 주장/반증`입니다.

기존 `data/presidents.json`은 시간순 대통령 overlay, `data/politicians.json`은 정치인 registry, `data/events.json`은 사건 cross-link registry 역할을 합니다. 기존 대통령 중심 ID와 파일은 깨뜨리지 않고 `legacyIds`와 연결 필드로 점진적으로 일반화합니다.




## Run202 · 1950년 12월 6~14일 한국전쟁 외교·전시행정 교차검증

2026-10-27: [조사 보고](data/research/runs/2026-10-27-run202-report.md) · [고유 자료 146페이지](data/documents/run202-dec07-12-frus-korean-uk.json) · [65개 사건 overlay](data/events/run202-dec07-12-policy-actions.json) · [42개 반증 명제](data/claims/run202-dec07-12-adversarial.json) · [한국 정치인 ID 연결](data/politicians/run202-dec07-12-korean-actors.json) · [다음 93개 원문 표적](data/research/lead-queues/run202-next.json). 미국 FRUS 중심 자료편향·영국 의회/한국 동시대 신문 교차의 한계와 미검증 직접명령을 명시. Floot 변경 없음.

## Run199b · 11월 15~21일 법관·부역통계·농지개혁·전시재정 추가 대량채굴

2026-10-27: [추가 보고](data/research/runs/2026-10-27-run199b-report.md) · [69개 추가 직접열람](data/documents/run199b-nov15-21-sources.json) · [50개 사건](data/events/run199b-nov15-21-actions.json) · [기존 14명/후보 6명](data/politicians/run199b-nov-actor-network.json) · [19개 주장·반증](data/claims/run199b-nov15-21-adversarial.json) · [51개 원문 표적](data/research/lead-queues/run199b-next.json). **내무부 검거 통계 55,509/55,909 및 송치·석방 합계 오류**, 부산서 범죄 발생379/377·검거141/265, 김태순/김태선 치안국장 신원충돌을 CONFLICTED/NARROWED로 보존. 1951 지가증권 국가기록원 후속 원문, FRUS d847·d864, 1950 도시계획과 실제 시공 구분. Floot 미변경.

## Run199 · 1950년 11월 8~14일 국회·법률·평시국정과 인물망 확장

2026-10-27: [실행보고](data/research/runs/2026-10-27-run199-report.md) · [실행계정](data/research/runs/2026-10-27-run199-ledger.json) · [직접 열람 86개 문서](data/documents/run199-nov8-14-sources.json) · [36개 사건](data/events/run199-nov8-14-actions.json) · [비대통령 22명 연결](data/politicians/run199-nov-actor-network.json) · [16개 주장·반증](data/claims/run199-nov8-14-adversarial.json) · [55개 다음 원문 표적](data/research/lead-queues/run199-next.json). **법률 제156호 '사형'은 私刑**(법외 제재)이며 사형제 폐지법이 아님. 국회 11/13 재의결과 12/1 법률156·157 공포를 분리, 법률157 원본 소실·1963 재작성 보존. 11/14 대통령령393 확인, 부산 공장 합계22개·소금30t 차이를 CONFLICTED 기록. 64개 동시대 신문 전사, 공식 원문·법령 9, 영인면 0. Floot 미변경.

## Run197 · 1950년 9월 전시 국정·국회·피난민 행정 대량채굴

2026-10-27: [실행보고서](data/research/runs/2026-10-27-run197-report.md) · [검증 장부](data/research/runs/2026-10-27-run197-ledger.json) · [국편 개별본문 75개 문서 registry](data/documents/run197-1950-september-contemporary.json) · [33개 사건](data/events/run197-1950-september-governance.json) · [25명 기존 인물 및 4 후보](data/politicians/run197-1950-september-actor-network.json) · [17개 주장·반증](data/claims/run197-1950-september-adversarial-claims.json) · [45개 다음 원문 표적](data/research/lead-queues/run197-next.json). 21개 공식/1차 기원 전사, 원면 0. 국회 법안통과와 공포, 내각결정과 집행, 미·소 상반주장, 동명이인 충돌을 분리. Floot 미변경.


## Run197b · 9월 14~30일 신규 98개 원문 및 법률·금융 원문 대조

2026-10-27: [추가 보고서](data/research/runs/2026-10-27-run197b-report.md) · [국편 신규시기 98개](data/documents/run197b-1950-sep14-30-contemporary.json) · [37개 사건](data/events/run197b-1950-sep14-30-actions.json) · [18개 주장](data/claims/run197b-1950-legal-money-relief-claims.json) · [27명 기존 정치인/4 후보](data/politicians/run197b-1950-party-cabinet-military.json) · [42개 후속 원문](data/research/lead-queues/run197b-next.json). run197의 9/1~13 75개는 run196b/c 선등록 자료이므로 저장소 신규 0개로 정정. 9/25 법률146, 은행권교환, 구호예산 충돌, FRUS 9/26 초안과 9/29 승인 분리. Floot 미변경.


**run197c 원면 교정**: 국가기록원 관보394호 법률146 1면을 브라우저 자동화 에이전트가 렌더링·판독한 결과 제5조 **10일**, 제6조 **원**. 법제처 온라인 백만환·국편 전사 10월과 차이를 필드별 보존. [대조기록](data/claims/run197c-law146-original-collation.json). 3개 호스트는 동일 기초법령이므로 독립 원문 3건으로 세지 않음.

## 최신 연구 실행 (Run194)

2026-10-27: [Run194 보고서](data/research/runs/2026-10-27-run194-report.md) · [검증 가능한 실행계정](data/research/runs/2026-10-27-run194-ledger.json) · [문서 registry](data/documents/run194-1950-budget-defence-bok.json) · [주장·반증](data/claims/run194-1950-budget-defence-bok-claims.json) · [사건](data/events/run194-1950-budget-defence-bok-actions.json) · [정치인](data/politicians/run194-1950-cabinet-bok-local-actors.json) · [후속 18개 원문 표적](data/research/lead-queues/run194-next.json). 1950년 8월 공보처 예산 출처 차이, 긴급명령7 국회 승인 부결, 금융통화위원 정원 7인 교차검증을 기록. 출처 불일치와 인명·날짜 불확실성은 해소된 것처럼 처리하지 않음. Floot 미변경.

## Run194b 추가 원문 대량채굴

2026-10-27: [확장 보고서](data/research/runs/2026-10-27-run194b-report.md) · [57개 직접 열람 실행장부](data/research/runs/2026-10-27-run194b-ledger.json) · [42개 추가 문서](data/documents/run194b-1950-jul31-aug05-contemporary.json) · [22개 사건](data/events/run194b-1950-emergency-law-and-social-actions.json) · [20개 주장/충돌](data/claims/run194b-1950-legal-contradictions.json) · [12개 반증검토](data/research/runs/2026-10-27-run194b-adversarial.json) · [34개 후속 원문 표적](data/research/lead-queues/run194b-next.json). 핵심: 국회 불승인 긴급명령7(7/22)과 8/4 긴급명령9를 구분하고, 전시 국정·사회정치조직을 비대통령 인물 노드로 연결. Floot 미변경.

## Run194c 조문 비교

[긴급명령7·9 조문별 변경표](data/claims/run194c-decree7-vs9-crosswalk.json) · [법제처 연혁과 7호 비공식 전사](data/documents/run194c-1950-decree-legal-index.json). 1950년 7호의 경찰서장 임명권이 8월 9호에서 도지사·대한청년단 추천 구조로 바뀌고, 자위대 체포 후 경찰 인도 시한이 48시간에서 24시간으로 단축됨. 원관보 대조·법적 평가는 미완.

## Run194d 국편 7호 원문 보강

[국편 1950-07-22 긴급명령7 19조 전문](data/documents/run194c-1950-decree-legal-index.json) 확인으로 **총 59건 실질 열람**, 신규 document **56건**, 공식 발신 기록·연설 전사 **21건**, 사건 **34건**, 주장 **40건**, 구체 lead **54건**. 법령 원관보 원면은 아직 미확보. [실행 감사](data/research/runs/2026-10-27-run194-final-audit.md).

## 핵심 원칙

**AI가 정치인을 심판하지 않습니다.** 시스템은 관련 기록을 공격적으로 찾되 공개·확정은 보수적으로 처리합니다. 원문·날짜·당시 맥락·후속 설명·반증·불확실성을 함께 보여주고 최종 판단은 사용자에게 남깁니다.

- 1차 자료와 동시대 기록 우선
- 주장과 사실, 정치적·법적·행정적 책임, 직접 명령을 분리
- 발언 일부만 잘라 쓰지 않고 원문 문맥 보존
- 상반 자료와 반증을 별도로 탐색
- 비교 후보는 제시하되 자동적인 위선·선악·추천·순위 판정 금지
- 정치 성향·정당과 무관하게 동일한 데이터 규칙 적용
- 오류 정정, 반론, CONFLICTED/BLOCKED/REOPENED 이력 보존
- 모르는 것은 지우지 않고 역사부채로 관리
- 대통령 재임기라는 이유만으로 사건·정책의 직접 책임을 자동 귀속하지 않음

## 조사 모델

먼저 대한민국 정치사의 전체 숲을 빠르게 지도화합니다. coverage의 기본 단위는 인물 한 명이 아니라 `시대 × 구조층` 셀이며 `UNMAPPED → SEEDED → STRUCTURED → VERIFIED / DEBT_TRACKED` 상태로 관리합니다.

전국 breadth v1은 F0~F10 11개 시대 × 17개 구조층, 총 **187/187 고유 셀의 SEEDED를 전수 uniqueness audit으로 확인**했습니다. 감사 결과는 `data/research/forest-v1-uniqueness-audit.json`에 보존합니다. 이는 전체 숲의 위치를 빠짐없이 찍었다는 뜻이지, 187개 셀의 역사 명제가 검증 완료되었다는 뜻은 아닙니다.

현재 단계는 **forest depth pass**입니다. SEEDED 셀 가운데 연결중심성·역사적 영향범위·불확실성·자료 접근성을 기준으로 우선순위를 정해 `STRUCTURED → VERIFIED`로 심화합니다. 동시에 정치인·기관·정당·사건·문서·주장/반증 그래프를 시대를 가로질러 연결합니다.

조사 사슬은 가능한 범위에서 `검색어 확장 → 2차 자료에서 원문 단서 추출 → 공식/1차 아카이브 역추적 → 날짜·인물·기관·사건명 변형 검색 → 상반 자료 탐색 → 원문 교차검증 → 새 인물/사건/문서 단서 생성`을 반복합니다.

한 인물·대통령·시대의 모든 open lead가 사라질 때까지 기다리지 않습니다. 주요 구조가 형성되면 미해결 블랙박스는 `HISTORY_DEBT`와 open leads에 보존하고 전국 forest의 다음 고우선순위 연결부로 이동합니다.

역사부채 전체 전수 재조사는 매시간 반복하지 않고 **매주 일요일 첫 조사 회차에 1회** 수행합니다. 단, 평상시 조사에서 역사부채를 해결하거나 흔드는 새 증거가 발견되면 즉시 갱신합니다.

## 전체 숲의 주요 구조층

헌정질서, 국회·입법, 정당·정파, 선거·대표성, 행정부·관료제, 사법·헌법재판·검찰, 군·경찰·정보기관, 지방정치·지방행정, 정치경제, 노동·농민·직능·기업, 복지·사회정책, 시민사회·사회운동, 언론·공론장, 지역·계층·세대·젠더 균열, 외교·안보·분단, 정치자금·부패·정경관계, 과거사·전환기 정의를 시대별로 횡단합니다.

## 데이터 구조

- `docs/KOREA_POLITICAL_FOREST.md`: 대한민국 정치사 전체 숲 지도와 전국 coverage 좌표계
- `data/politicians.json`: 전체 정치인 stable ID, 이명, 직책, 조사상태와 연결
- `data/events.json`: 사건 stable ID와 정치인·기관·정당·정책 cross-link
- `data/presidents.json`: 대통령 임기순 시간축 overlay
- `data/evidence/`: 인물별 증거 원장
- `data/annals/`: 인물별 디지털 실록
- `data/research/`: coverage, open leads, HISTORY_DEBT, forest breadth/depth audit
- `docs/`: 방법론, 아키텍처, 조사 루프

## 운영 원칙

> **수집은 공격적으로, 공개는 보수적으로.**
>
> **GitHub에서 충분히 축적하고, Floot는 묶어서 빌드한다.**

수동 GPT 조사 루프의 결과는 먼저 GitHub의 `data/`, `docs/`, `sql/`에 축적합니다. 조사 1회마다 Floot를 다시 빌드하지 않습니다. Floot는 충분한 조사 묶음과 의미 있는 스키마/UI 변화가 쌓이고 사용자가 별도로 요청했을 때만 반영합니다.

## 현재 상태

**대한민국 정치사 숲 지도 v1 breadth audit 완료: 187/187 시대×구조층 셀이 최소 SEEDED 상태다.** 이제 빈칸 채우기 자체는 종료하고, 전체 숲에서 연결중심성이 높은 제도·조직·사건·인물군을 원문 단위로 심화한다.

이승만·제1공화국과 제2공화국·5·16 전환부에 이미 축적된 자료는 유지한다. 대통령 backbone도 시간순 탐색 보조선으로 남는다. 하지만 국회, 정당, 군·경찰·정보기관, 사법, 관료, 지방정치, 정치경제, 노동, 시민사회, 언론, 외교안보 등에서 연결중심성이 높은 사건·인물·기관은 대통령 순서와 관계없이 독립 연구선으로 들어간다.

다음 품질 목표는 collection-level seed를 item-level 문서로 교체하고, 주요 셀을 `STRUCTURED`로 승격하면서 `proposed_by / decided_by / executed_by / opposed_by / legal_authority / observed_by / later_finding` 관계를 명시하는 것이다. 이름이 seed anchor에 등장했다는 이유만으로 정치인을 VERIFIED로 승격하지 않는다.

세부 설계는 `docs/KOREA_POLITICAL_FOREST.md`, `docs/ARCHITECTURE.md`, `docs/HOURLY_ANNALS_LOOP.md`, `docs/RESEARCH_LOOP.md`, `docs/METHODOLOGY.md`, `docs/FLOOT_BUILD_POLICY.md`를 참고하세요.

## 로컬 실행

```bash
npm install
npm run dev
```

## 빌드

```bash
npm run build
```

Floot는 조사 저장소가 아니라 충분히 축적된 데이터를 보여주는 배포·인터랙션 계층으로 사용합니다.


## Run163 evidence increment (2026-10-26)

1950-09-14 군 미결수 검찰이관·고문금지 하달의 **당대 발표**와 1950-09-25 부산형무소 희생 **후대 조사**를 분리했고, 1960-01-01 공무원연금법 제533호·특별회계법 제534호 공포와 1/5 국무위원 연명 선언을 연결했다. 김해 한림면장 최대성 등 비대통령 인물 후보는 독립 노드로 보존한다. 원명령·원관보·집행기록은 OPEN. See `data/research/runs/2026-10-26-run163-report.md`. Floot unchanged.

### 164회 (2026-10-26): 1950년 9월 전시 국정·비대통령 정치인 확장

[실록](data/annals/rhee-syngman-run164.md) · [문서 60건 신규](data/documents/run164-1950-september-governance.json) · [14명 후보](data/politicians/run164-1950-september-candidates.json) · [15개 사건](data/events/run164-1950-september-actions.json) · [12개 반증검토](data/claims/run164-1950-september-adversarial.json) · [다음 52개 원문 표적](data/research/lead-queues/run164-next.json). **대통령은 시간순 backbone이며 대한민국 역대 주요 정치인 전체가 최종 코퍼스**다. 1950년 9/8 국무회의 피난민법 개정 결정과 9/25 법률 제146호 공포를 분리한다. Floot 미변경.

164회 추가 심층검증: [법제·지방복구·전재민 배급 문서 25건](data/documents/run164b-1950-september-recovery-and-law.json), [국회의원 4명](data/politicians/run164b-parliamentary-actors.json), [사건 9건](data/events/run164b-1950-recovery-law.json), [법률156·157 반증검토](data/claims/run164b-1950-law-and-rationing.json), [원문표적 20건](data/research/lead-queues/run164b-next.json). 9/18 국회 가결과 9/25 공포 분리, 사형금지법은 법정절차 없는 처형 금지임을 확인.

164회 3차 보강: [9/21~25 정당·군사사법·통화 자료 37건](data/documents/run164c-1950-september-party-justice-economy.json), [정치인 6명·비정치인 군법회의 actor](data/politicians/run164c-party-government-candidates.json), [사건 14건](data/events/run164c-1950-september-policies-and-party.json), [충돌·수정 이력](data/claims/run164c-primary-corrections-and-conflicts.json), [다음 24개 원문표적](data/research/lead-queues/run164c-next.json). 국사편찬위 1962년 무죄 vs 서울기록원 1964년 무죄, 법률146 전사 '10일/10월' 충돌을 삭제하지 않고 보존.

164회 4차: [9/26·29·30 원문 26건](data/documents/run164d-1950-september-recovery-decisions.json), [서민호](data/politicians/run164d-assembly-candidate.json), [사건 12건](data/events/run164d-1950-recovery-decisions.json), [반증 10건](data/claims/run164d-1950-budget-conscription-diplomacy.json), [다음 원문표적 21건](data/research/lead-queues/run164d-next.json). 사회부·재무부 구호예산 이견·징병불응 제재·북진 승인단계 구분.

164회 5차 보강: [1950-10-01/04/05 문서 25건](data/documents/run164e-1950-october-reconstruction.json), [양성봉 도지사](data/politicians/run164e-governor-candidate.json), [사건 11건](data/events/run164e-1950-october-administration.json), [주장 10건](data/claims/run164e-1950-education-relief.json), [원문표적 20건](data/research/lead-queues/run164e-next.json). 교육·귀향·식량·귀속재산 행정 복원.

## Run208 · 1951년 6월 외교·전시재정·UNKRA 사료 교차감사 (2026-10-28)
[실행보고](data/research/runs/2026-10-28-run208-report.md) · [FRUS 원문 41개 + 국편 3개](data/documents/run208-1951-june-frus-d318-d358.json) · [17개 사건](data/events/run208-1951-june-diplomacy-fiscal-actions.json) · [18개 주장·반증](data/claims/run208-1951-june-adversarial.json) · [한국인 정치·외교관 5명 연결](data/politicians/run208-1951-june-korean-actors.json) · [다음 36개 원문 표적](data/research/lead-queues/run208-next.json). 영문 FRUS 수입가격 최저 6,000원 vs 국편 번역 최고 6,000원 **의미 반전**과 공식환율 22,500/2,500원 충돌을 미해결로 보존. 원면 0건·3계열 교차검증 0건. Floot 미변경.

Run208 후속: [AKS·ODA Korea 환율 대조 및 외교사료관 원표 표적](data/research/runs/2026-10-28-run208-report.md) 추가. 1951년 5월 대충자금 6000원 책정, 6월 미국대사 승인 보고, 11월 일반시세 적용은 **동일한 단일 결정으로 병합 금지**. 환율 22500/2500 충돌과 국편 영한 번역 하한/상한 역전은 유지.

Run208 최종 검증: **51개 열람 페이지·50개 근원문서/저작, 23개 사건, 25개 주장·반증, 비대통령 10명 조사(실질 심화 8), 후속 표적 42개, 커밋 6개**. `HD-R206D-03` OPEN→NARROWED, `HD-R207-04` CONFLICTED 유지. 상세는 [최종 실행 계정](data/research/runs/2026-10-28-run208-ledger.json).


## Run209 · 1951년 6월 26일 인사·구호·전시경제 감사 (2026-10-28)
[실행보고](data/research/runs/2026-10-28-run209-report.md) · [직접 확인 실질문서 13건](data/documents/run209-june26-crossprovenance.json) · [사건 15개](data/events/run209-june26-state-actions.json) · [주장 14개](data/claims/run209-june26-adversarial.json) · [비대통령 7명 연결](data/politicians/run209-june26-actors.json) · [후속 41개 원문 표적](data/research/lead-queues/run209-next.json). 6/26 서울시장·치안국장·서울시 경찰국장·내무차관 연쇄 인사, ECA PR 5~10% 보증금, 7/1 대일수출 신용장 규제 예정, 허정 구호 연인원 단위 구분. 미국 G-2·영국 Hansard·북한 관보도 출처 성격을 분리해 수록. 40개 본문 목표 미달, 원면 0, 3계열 동일 명제 검증 0. Floot 미변경.

### Run209 추가 심화(6/27~7/1)
고유 실질자료 페이지 **70건**, 공식·동시대 1차 기록 및 원문 전사 **20건**(원면 직접 0), 국정·외교·사법·농정·구호·재정 등 17개 영역, 독립 연구선 34개. [추가 문서 registry](data/documents/run209-june26-crossprovenance.json) · [사건 51개](data/events/run209-june26-state-actions.json) · [반증 34개](data/claims/run209-june26-adversarial.json) · [후속 81개](data/research/lead-queues/run209-next.json). **윤우경 경찰국장 6/24 vs 6/26**, **국회 정전반대 결의 6/28 vs 6/29**, **부산 절도비율 96% vs 계산상 89.13%**, **전선도난 압수 500 vs 200톤** 충돌 보존. 6/27 이승만 반대담화와 6/30 정부 5개 정전조건을 별도 사건으로 기록. 엄격한 독립 3계열 동일명제 검증은 0건.

Run209 출처계열 교차검증 3개 명제는 [별도 장부](data/research/runs/2026-10-28-run209-crosschecks.json)에서 근거 계열·독립성 한계·충돌일을 명시한다. 3개 모두 엄격한 3계열 1차 원문 완결로 계산하지 않는다.

Run209 FRUS 영문 추가 감사: 유엔군 정전교섭권 법률의견(d395), 7/2 릿지웨이의 즉시 전투중지 해석 반대(d399), 한표욱 참석(d393)을 구조화. 최종 [실행장부](data/research/runs/2026-10-28-run209-ledger.json) 73건/공식23건/사건55/주장39/후속91건.
