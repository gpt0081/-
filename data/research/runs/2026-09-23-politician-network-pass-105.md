# Politician Network Pass 105 — execution ledger

Date: 2026-09-23
Focus: 1952-01 평화선 선언에서 1952-10 포획심판 제도까지 집행·심판 사슬 확장.

## Progress
- 대통령기록관에서 긴급명령 제12호 포획심판령(1952-10-04)과 1954-04-07 승인 관련 기록의 존재를 확인하고, 긴급명령 문서가 국무회의 의결문·법조문·국회 승인요청문으로 구성된다는 컬렉션 설명을 확보.
- 국가기록원에서 포획심판령 관보 원문 객체를 `BA0186100`, 관보 제752호, 4쪽으로 고정하고 대통령령 제707호 개설령이 같은 기록 계열에 있음을 확인.
- 동북아역사재단 한일회담외교문서의 포획심판령 전문을 직접 열어 법무부 소속, 대통령 임면, 법무부장관 보직, 해군·외무부 심판관 참여, 함선 지휘관의 사건 인계, 검사 조사, 2심, 국가배상, 국고귀속, 검사 집행·해군 지원까지 조문 단위로 구조화.
- 기존 평화선 연구를 `선언자/외무부` 중심에서 `법무부-해군-외무부-대통령-국회` 집행 네트워크로 확장.
- 10개의 비대통령 행위자/집단 candidate를 생성했으나 실명 미확정 노드는 stable registry로 성급히 승격하지 않음.

## Counts
- Independent research/retrieval lines materially pursued: 20.
- General policy domains touched: 7 (해양/수산, 외교, 국제법, 사법/법무, 국방/해군, 행정/인사, 헌정/국회승인).
- Non-president actor/candidate nodes newly structured or deepened: 10 (직책/집단 candidate 포함; 실명 stable 승격 0).
- Event/sub-event candidates newly structured/materially revised: 9.
- Meaningful unique documents/pages directly opened: 9 page/views, 5 unique document objects after deduplication; official/public/primary-facing unique objects: 5. Target 40/20 not reached.
- Adversarial checks: 10.
- Existing OPEN/BLOCKED/CONFLICTED leads followed or narrowed: 5 materially (7월 나포지시 원문, 포획심판령 원문, 제707호, 사후승인, 1949 포획심판법 선행안).
- Cross-check bundles: 3.
- Concrete next leads: 40.

## Important uncertainty changes
- `포획심판령 = 대통령의 직접 몰수명령` 식 단선 서술은 배제. 심판·항의·집행 절차가 원문에 존재.
- `해군 단독 집행제도` 서술도 배제. 법무부 소속 심판소, 검사, 외무부/해군 심판관 후보, 대통령 임면이 명시됨.
- 1952-07-18 대통령의 외국어선 나포지시는 이번 회차에도 공식 원문을 확보하지 못해 OPEN 유지.
- 1954-04-07은 대통령기록관의 승인 관련 문서 생산일로 확인했지만 실제 국회 표결일·회차와 동일시하지 않음.

## Files changed
- `data/research/rhee-pass-105-prize-court-enforcement-chain-2026-09-23.md`
- `data/research/candidates/pass-105-prize-court-actors.json`
- `data/research/runs/2026-09-23-politician-network-pass-105.md`

## Commits
- `c936bc9a5b4b63354bf61d106228a9084a736bd8` research: extend Peace Line into prize-court enforcement chain
- `a47e2e28a1aaedc95275e95c660cb443a9b61cf7` data: structure prize-court actor and institution leads
- this ledger commit: see commit containing this file

## Next priority
1순위는 대통령기록관 포획심판령 복원 PDF의 국무회의 의결문·승인요청문 직접 회수다. 그 다음 제707호 별표와 인사발령을 이용해 초대 포획심판소장/고등포획심판소장/심판관/검사 실명을 복원한다. 동시에 BA0838466의 1949 `포획심판법`을 회수해 1952 긴급명령과 문언 diff를 하면 제도의 실제 기초자와 선행 법제망을 대통령 중심 서술 밖으로 끌어낼 수 있다.

역사부채 주간 전수조사 미실시.