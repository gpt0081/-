# 정치인 registry 확장 인덱스

- 기본 registry: `data/politicians.json` (기존 API 호환 유지)
- 2026-10-08 토지행정·제헌국회 독립 인물 12명: `data/politicians/run81-land-actors.json`
- 원문 기반 후보 상세: `data/research/candidates/run81-land-policy-actor-network.json`
- 안재홍 독립 실록: `data/annals/ahn-jae-hong.md`, 증거: `data/evidence/ahn-jae-hong.json`
- 신규 event/action: `data/events/run81-land-legal-actions.json`

조회 시 base와 overlay를 stable ID로 결합한다. 기존 ID를 삭제하거나 자동으로 덮어쓰지 않는다. `pol-lee-beom-seok-1900`과 `pol-lee-beom-seok`은 동일인 중복 의심이며 canonical은 후자로 제안하되 참조 전수조사 전 병합하지 않는다.

- 2026-10-08 제헌국회 1949-04-27 심의 참여자 6명: `data/politicians/run82-1949-assembly-actors-a.json`, `data/politicians/run82-1949-assembly-actors-b.json`.
- 1949-03-18 노일환 후보: `data/politicians/run82-1949-assembly-actors-c.json`.
- 조헌영 초기 실록: `data/annals/cho-heon-yeong.md` 및 `data/evidence/cho-heon-yeong.json`.

- 2026-10-08 법원조직법·귀속재산처리법 원문 기반 제헌국회·법무부 정치인 후보 14명: `data/politicians/run84-1949-institutional-actors.json`.
- 서우석 독립 실록/증거: `data/annals/seo-woo-seok.md`, `data/evidence/seo-woo-seok.json`.
- 새 document/action/claim: `data/documents/run84-courts-vested-property.json`, `data/events/run84-judiciary-property-actions.json`, `data/claims/run84-judiciary-property-claims.json`.
