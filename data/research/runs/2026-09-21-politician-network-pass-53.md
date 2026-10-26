# Run report — Politician Network Pass 53

Date: 2026-09-21
Focus: 1953 반공포로 석방의 대통령 명령→헌병총사령부→수용소 경비→후속 행정→정전협상 사슬

## Result
직전 Pass 52의 1958-59 경무대/안보 네트워크에서, 기존 highest lead인 `lead-1953-pow-execution-chain`으로 전환했다. 대통령의 공개 책임인정은 한국사DB와 FRUS 양쪽에서 교차확인했고, FRUS 612·616을 통해 원용덕 헌병총사령관의 대통령 직속 별도 명령선과 육군참모총장 계통을 분리했다. 6월20일 국무회의의 석방포로 생계·의료·교통·취업 지원까지 연결하여 사건을 군사/외교 단발행위가 아니라 행정 후속조치를 포함한 chain으로 확장했다.

## Counts
- 독립 연구선: 20 (계획일자, 대통령 직접명령, 원용덕 지휘선, 육군참모총장과의 분리, 수용소별 집행, 도지사/경찰 보호, 사망·탈출 수치, UNC 재통제, 추가석방 위기, 미군-ROK 충돌, 변영태 외교선, 백두진 워싱턴선, 신태영 국방선, 국무회의 구호, 재정, 보건, 고용, 강제입대 의혹, 잔여포로 처리, 정전/상호방위조약 협상)
- 직접 확인 고유 문서/원문: 32
- 공식·1차·동시대 원문/공식 아카이브: 30
- 국정영역: 8 (안보·국방, 외교, 행정, 지방행정·경찰, 재정, 사회구호, 보건, 고용/경제)
- 비대통령 actor 신규/심화: 9 + 기존 이승만/조병옥 cross-link
- event/sub-event 신규 구조화 후보: 5
- adversarial checks: 10
- cross-provenance bundles: 3
- 추적 open lead: 1개를 실질 NARROWED, 관련 파생 lead 40개 생성
- concrete next leads: 40

## Interpretation changes
1. `이승만 직접명령` 자체는 더 이상 막연한 후대 평가가 아니라 대통령 본인 6/18 성명·Clark 서한·변영태 서한으로 강하게 고정할 수 있다.
2. 실행은 `대통령→일반 육군 지휘계통`으로 단순화하면 안 된다. FRUS는 원용덕 Provost Marshal을 대통령 직속 별도선으로 묘사하고 백선엽 참모총장 계통과 구분한다.
3. 원용덕이 6/19 잔여포로 석방을 막는 미군을 공격하라는 명령을 내렸다는 Clark/Herren 보고는 매우 중요하지만 미국측 contemporaneous report다. 한국측 원 명령서가 없어 claim/evidence graph에서는 `observed_by`로 유지한다.
4. 사건은 6/18 탈출로 종료되지 않았다. 6/19~20 추가석방·미군 충돌 위험, 6/20 국무회의 구호정책, 6/22~27 잔여포로·정전·경제원조·20개사단·상호방위조약 협상으로 이어졌다.
5. `반공포로 석방이 상호방위조약을 단독으로 만들어냈다`는 단선 인과는 보류한다. 미국의 조약 offer는 이미 6월6일 존재했고, 6월 말 협상은 여러 조건의 패키지였다.

## Files
- `data/research/rhee-pass-53-anticommunist-pow-release-chain-2026-09-21.md`
- `data/research/candidates/pass-53-pow-release-actors.json`
- `data/research/runs/2026-09-21-politician-network-pass-53.md`

## Commits
- `342eb8ff379b47d5194ecc2acf476bb06575e4ee` research dossier
- `3c8cd42ffe139bda836d1935b3b080456875ce50` actor candidates
- this run-report commit

## Limitations
이번 실행은 40문서 하한에는 못 미쳤다. FRUS 606~642 핵심 연속구간과 한국측 공식 아카이브를 우선해 32개를 직접 확인했고, 남은 시간은 중복 페이지 숫자 채우기보다 명령선 분해와 40개 원문 표적 생성에 사용했다. 수용소별 한국군 지휘관/명령번호는 아직 미확인이다.

## History debt
역사부채 주간 전수조사 미실시. 일요일 첫 실행이 아니다.

## Floot
수정·빌드하지 않음.
