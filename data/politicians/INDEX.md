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
