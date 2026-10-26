# Politician Network Pass 109 — execution ledger

Date: 2026-09-24
Focus: 직전 진해시 설치 연구선에서 다시 이승만 정부 말기 중앙-지방 선거행정망으로 breadth-first 확장. 3·15 사건의 지방 도지사·내무국장·경찰국장·정당조직을 독립 actor로 구조화.

## Progress
- 직전 pass 108 ledger와 lead queue, `data/politicians.json`, `data/events.json`을 확인하고 김성삼·진해시 자료의 기계적 반복을 피했다.
- 민주화운동기념사업회 사료관에서 충남·전남·강원 지방 부정선거 특별재판 및 후속 군사재판 자료를 직접 열어 actor/role/event를 분해했다.
- 가장 중요한 새 lead는 1960-05-28 김학응 검찰 진술이다. 사료관 일지는 김학응이 내무부장관 지시에 따른 행정협의회 논의와 90% 초과 득표율을 85%로 조정 발표했다고 진술했다고 정리한다. 당사자 수사 진술이므로 supporting evidence가 아니라 `actor statement requiring primary corroboration`으로 저장했다.
- 김학응·전창한·윤승구·우용출·남정상·이하영·양재철·신구영·정동식·홍창섭·유진하·손계천·오임근·김철안 14 actor를 신규/심화 candidate로 구조화했다.
- 홍창섭은 3·15 선거행정 사건과 1960-04-25 춘천 학생대표 면담에 모두 등장하므로 cross-event actor로 분리했다.
- 김철안은 직전 진해 조사단 연구선에서 3·15 지역 자유당 조직 연구선으로 cross-link했다.
- 특별재판과 5·16 이후 군사재판을 silent merge하지 않고 별도 later-finding으로 보존했다.
- Floot는 수정·빌드하지 않았다.

## Counts
- Independent high-priority research/retrieval lines materially pursued: 20. 충남 중앙명령선, 충남 행정협의회, 충남 공무원친목회, 충남 개표율 조정, 충남 특별재판, 전남 도청선, 전남 경찰선, 전남 특별재판, 전남 군사재판, 강원 도청선, 강원 경찰선, 강원 특별재판, 강원 군사재판, 춘천 시위대응, 경북 오임근 수사, 경북 개표조작 lead, 김철안 지역당, 중앙 내무부→도지사, 치안국→도경찰국, 대통령/경무대 보고선.
- General policy domains materially touched: 7 (선거, 지방행정, 경찰행정, 정당조직, 사법/특별재판, 군사재판/헌정변동, 교육·학생시위 대응).
- Non-president actor nodes newly structured/deepened: 14. 최소 10 달성.
- Event/sub-event candidates newly structured/deepened: 9. 최소 8 달성.
- Meaningful unique documents/pages directly opened/reviewed this run: 12. Official/public-archive-facing: 10. 40/20 목표 미달. 검색 결과가 민주화운동기념사업회 사료관에 집중됐고 원 공소장·판결문·피의자신문조서까지는 직접 노출되지 않았다.
- Adversarial/identity/provenance checks: 10. 최소 10 달성.
- Existing open leads materially followed/narrowed: 8 (중앙→지방 명령선, 지역 득표율 조작, 지방 자유당 조직, 지방 경찰선, 김철안, 4월혁명 지방 대응, later judgment provenance, actor identity).
- Cross-check bundles: 3 (충남, 전남, 강원).
- Concrete next leads generated: 40. 최소 30 달성.

## Important uncertainty changes
- `내무부장관→김학응` 지시선은 구체적인 contemporaneous actor statement가 생겼으나 원 피의자신문조서와 내무부 공문이 없어 NARROWED/OPEN이다.
- `득표율 90% 초과→85% 조정`은 통상적 득표 부풀리기 서사와 방향이 다르므로 원 개표표를 요구하는 adversarial lead로 승격했다.
- 전창한/전장한 표기 충돌을 보존했다.
- 지방 도지사·내무국장·경찰국장이라는 직책만으로 범행·책임을 귀속하지 않는다. 각 공소장·판결문 인정사실을 기다린다.
- 1961 군사재판 판단은 1960 행정행위와 별도 provenance다.
- 대통령 이승만의 직접 사전지시는 이번 자료로 확인되지 않았다.

## Files changed
- `data/research/rhee-pass-109-provincial-election-administration-2026-09-24.md`
- `data/research/candidates/pass-109-provincial-election-network.json`
- `data/research/runs/2026-09-24-politician-network-pass-109.md`

## Commits
- `888d6bc5432261545240744c5526ed71da860aa1` research: expand 3.15 provincial administration network
- `1017ee706331db9ebfa58916beb6aa97d259e6bf` data: structure provincial 3.15 actor network
- this ledger commit: see commit containing this file

## Next priority
원 김학응 피의자신문조서와 내무부 지시문을 최우선으로 회수한다. 그 다음 충남 행정협의회/공무원친목회 문서, 중앙선관위 개표 원표, 각 도 특별재판 공소장·판결문, 관보 인사발령을 actor별로 결합한다. 지방 단위 자료가 확보되면 `최인규/이강학 중앙선 → 도지사/경찰국장 지방선 → 군·시·읍·면 집행선`을 계층형 event graph로 확장한다.

역사부채 주간 전수조사 미실시.