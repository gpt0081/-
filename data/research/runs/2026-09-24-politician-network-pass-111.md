# Politician Network Pass 111 — execution ledger

Date: 2026-09-24
Focus: pass 110의 지방 판결 corpus를 절차단계별로 분해하고 형량·신원 충돌을 탐지하며 충북/충남/경남/전남/전북/경북 actor graph를 확장.

## Progress
- pass 110 ledger와 연구/candidate 파일을 읽고 동일 검색 반복 대신 지방별 특별재판→혁명재판 절차 차이, 형량 충돌, 충북 누락 경찰지휘선, 마산 발포지휘선 분리에 집중했다.
- 이하영 `4년 vs 5년`, 이정용 `7년 vs 17년`, 충북 보안과장 `이헌구 vs 이헌영`을 명시적 CONFLICTED 대상으로 만들었다.
- 강원은 특별재판 구형과 후대 혁명재판 판결 형량이 달라 절차단계 모델링 필요성이 확인됐다.
- 문학동·이화식·정동식·우용출·남정상·황종율·손석래를 신규 actor candidate로 구조화했고 정인택·신도성을 심화했다.
- 신도성은 1954 신당 강령기초위원 경력을 1960 경남지사 사건과 연결해 `한 사건의 피고`가 아니라 장기 정치인 노드로 확장했다.
- 선거부정 행정망과 마산 발포 명령망을 분리했다. 손석래의 발포명령 시인은 선거기획 command edge로 사용하지 않는다.
- Floot는 수정·빌드하지 않았다.

## Counts
- Independent high-priority research/retrieval lines materially pursued: 21.
- General domains materially touched: 7 (선거, 지방행정, 경찰행정, 사법/재판, 정당조직, 금융/선거자금, 4월혁명 후 인사행정).
- Non-president actor nodes newly structured/deepened: 10.
- Event/sub-event candidates newly structured/deepened: 15.
- Meaningful unique documents/pages directly opened/reviewed: 26. 이 중 공식/공공 아카이브·동시대 기록 계열 23. 총 40 목표는 미달했고 공식·1차/공공 계열 20 목표는 달성했다. 대형 판결문은 웹 인터페이스가 메타/첫 페이지 중심으로 노출되어 전체 본문을 읽었다고 계산하지 않았다.
- Adversarial/identity/provenance checks: 10.
- Existing open leads materially followed/narrowed: 11 (이하영 형량, 이정용 형량, 강원 절차, 충북 판결, 충남 판결, 김학응 절차, 경남 선거/발포 분리, 경북 득표율 조작, 중앙 금융선, 최병환 지방행정선, 지방 actor identity).
- Cross-check bundles: 5 (강원 구형↔판결; 전남 4년↔5년; 경북 이정용 7년↔17년; 충북 인물명 충돌; 경남 검찰↔국회조사↔후대판결).
- Concrete next leads generated: 40.

## Most important correction signals
1. `이하영 4년/5년`: 절차단계 차이 가능성이 높지만 원 확정문 전에는 해결하지 않는다.
2. `이정용 7년/17년`: 같은 12월8일을 가리키는 공공 데이터 계열 내부 충돌이다. 원 판결 주문이 최우선이다.
3. `이헌구/이헌영`: 사진 사료 캡션끼리 이름이 충돌한다. 자동 병합 금지.
4. 강원 피고군은 공소사실·피고인 부인·구형·후대 판결을 모두 별도 claim으로 유지한다.
5. 손석래의 마산 발포명령 진술은 3·15 선거행정 command와 별도 사건으로 유지한다.

## Files changed
- `data/research/rhee-pass-111-provincial-procedure-conflicts-2026-09-24.md`
- `data/research/candidates/pass-111-provincial-procedure-actors.json`
- `data/research/runs/2026-09-24-politician-network-pass-111.md`

## Commits
- `4de8be927bce5f4047cb8bb2db2e4e7bae1235ce` research: separate provincial 3.15 trial stages and sentence conflicts
- `5a6bfb9e28710a5318c8e5ad4aba98c47d016c60` data: structure provincial trial and cleanup actor expansion
- this ledger commit: see commit containing this file

## Next priority
가장 높은 정보가치는 `00849921 이정용 판결 주문 원문`과 `1961-12-21 혁명재판소 확정 발표 원문`의 직접 대조다. 이어 충북/충남 판결 등록번호를 회수하고, 충북신보 1960-07-13 및 관보로 문학동 지휘선과 이헌구/이헌영 신원을 확정한다. 병렬로 5개 지방 판결의 피고별 범죄사실 페이지를 추출해 proposed/decided/executed/observed/later_finding edge를 분리한다.

역사부채 주간 전수조사 미실시.