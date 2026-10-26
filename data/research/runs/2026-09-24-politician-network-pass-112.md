# Politician Network Pass 112 — execution ledger

Date: 2026-09-24
Focus: pass 111의 지방 3·15 재판 형량·신원 충돌을 절차단계별로 좁히고 충북/경북/경남 actor graph를 보강.

## Progress
- 직전 pass 111 ledger, 연구파일, candidate graph를 읽고 반복검색 대신 `이정용 7/17년`, `이하영 4/5년`, `이헌구/이헌영`, 마산 장소별 발포지휘선, 충북 문학동 지휘선을 우선 추적했다.
- 이정용 7년은 9/22 구형, 9/28 언도, 12/08 국가기록원 판결 객체에서 반복 확인되어 conflict를 NARROWED로 내렸다. 17년 원출처 미회수 때문에 RESOLVED로 만들지 않았다.
- 이하영은 9/14 5년 언도와 11/10 4년 판결이 서로 다른 날짜의 사료로 확인되어 단순 오기보다 절차 변경 가능성이 강해졌다.
- 충북 보안과장 이헌구/이헌영 충돌은 동일 KDemo 계열에서도 유지되어 CONFLICTED를 보존했다.
- 문학동의 1959-04-01 충북경찰국장 부임 및 1960 선거지휘 단서를 contemporaneous source를 인용한 지역사 본문까지 좁혔고, 원 충북신보/관보를 다음 표적으로 명시했다.
- 황종율 후보는 공신력 있는 인물자료에서 canonical `황종률(黃鍾律, 1909~1972)`과 다수 고위공직·국회의원 경력이 확인되어 VERIFIED 장기 정치인 노드로 승격했다.
- 손석래 발포명령은 시청 앞과 남성동 최초발포의 지휘관계가 다르다는 국회조사 증언을 반영해 multi-site sub-event로 분해했다. 서득룡 지청장 직접명령 가설에는 3/17 검찰 부정 발표를 adversarial evidence로 추가했다.
- Floot는 수정·빌드하지 않았다.

## Counts
- Independent high-priority research/retrieval lines materially pursued: 20.
- General domains materially touched: 7 (선거, 지방행정, 경찰행정, 사법/재판, 정당/선거자금, 인사행정, 사회/시위 대응).
- Non-president actor nodes newly structured/deepened: 10 (황종률, 문학동, 정인택, 이헌구/영, 이정용, 이하영, 손석래, 서득룡, 신도성, 이화식).
- Event/sub-event candidates newly structured/deepened: 10.
- Meaningful unique documents/pages directly opened/reviewed: 16. 이 중 공식/공공 아카이브·동시대 기록 계열 13. 총 40 및 공식·1차 20 목표 모두 미달. 검색 인터페이스가 대형 판결문 전체 페이지를 직접 노출하지 않아 메타 페이지를 전체 문서 열람으로 과대계산하지 않았다.
- Adversarial/identity/provenance checks: 10.
- Existing open leads/history-debt materially followed/narrowed: 10.
- Cross-check bundles: 5 (이정용 구형↔언도↔판결; 이하영 언도↔후속판결; 이헌구↔이헌영; 손석래 증언↔검찰 발표; 경남 폭로↔검찰 기소).
- Concrete next leads generated: 40.

## Most important correction signals
1. 이정용 7년은 현재 3개 절차 시점에서 반복된다. 17년은 원출처 회수 전까지 conflict 잔존.
2. 이하영 5년→4년은 날짜가 다른 재판자료라 procedural change 가능성이 높다.
3. 이헌구/이헌영은 여전히 자동 병합 금지.
4. 손석래는 시청 앞 발포명령을 시인했지만 남성동 최초 발포는 서장 명령 없이 이루어졌다고 진술했다. `마산 발포` 단일 edge 금지.
5. 황종률은 1960 충북 후속행정만의 인물이 아니라 경제관료·장관·국회의원으로 이어지는 독립 정치인 실록 후보다.

## Files changed
- `data/research/rhee-pass-112-provincial-judgment-corrections-2026-09-24.md`
- `data/research/candidates/pass-112-provincial-corrections-actors.json`
- `data/research/runs/2026-09-24-politician-network-pass-112.md`

## Commits
- `1fda180caf6044e12cb2c53b4ffc591cb3a67fc5` research: resolve provincial 3.15 judgment-stage corrections
- `042b063a78b0da69c6bef506bb7bc23e5a7eaa60` data: structure provincial judgment corrections and actor identities
- this ledger commit: see commit containing this file

## Next priority
최우선은 `00849921`과 `00849856`의 주문·절차경과 실제 페이지 회수다. 이정용 17년 표기의 각주/원출처를 찾아 7년 conflict를 해결하고, 이하영 9/14→11/10 형 변경 이유를 확인한다. 병렬로 충북신보 1960-07-13·1959-04-01 경찰 인사·충북 특별재판 공소장을 회수해 문학동 지휘선과 이헌구/이헌영 신원을 확정한다. 이후 황종률을 별도 annals/evidence를 가진 독립 정치인 실록으로 시험 승격한다.

역사부채 주간 전수조사 미실시.
