# Run report — Politician Network Pass 61

Date: 2026-09-22
Focus: post-armistice mutual-defense treaty drafting/initialing/signing, aid governance, force expansion, and the boundary between treaty commitments and armistice compliance.

## Result
Pass 60의 정전 서명 직전 단계에서 다음 시기로 이동했다. 이번 회차의 핵심 교정은 `한미상호방위조약 체결`을 단일 사건으로 쓰지 않는 것이다. 1953-07-09 ROK 초안, 8/5 working party, 8/7 문안 교섭, 8/8 initialing, 10/1 signing, 별도의 UNC/정전준수 assurance를 분리했다. 7/9 ROK 초안에는 압록·두만까지의 관할 인정과 즉각 행동 문구가 있었고, 8월 교섭에서 이승만의 자동 군사행동 요구는 미국측이 받아들이지 않았다. 변영태는 실무협상·문안 수정·initialing·signing의 연속 행위자로 확인된다.

평시 국정축도 확장했다. 8/6 회의에서 이승만은 원조기관 중복을 비판하고 Combined Economic Board를 최고 조정기구로 삼으려 했으며, 별도 백두진-미국 육군장관 회의에서는 CEB MOU, 180:1 환율, 현지비용 부담, Tasca 계획, 육해공군 확장 요구가 구체적으로 제기됐다. 따라서 post-armistice 시기는 외교/안보만이 아니라 경제행정·재건·재정/환율·산업·군정책이 얽힌 별도 국정 묶음으로 구조화해야 한다.

## Politician / actor graph
실질 심화: 백두진, 변영태, 손원일. 신규/재식별 candidate: 백선엽, 박옥규, 최용덕, 임병직, 정체 미상의 `Minister Kim`, Philip Han. 군 지휘관은 자동으로 정치인 registry에 넣지 않고 군사행위자 노드와 정치인 승격 기준을 분리했다. `Minister Kim`과 Philip Han은 신원 미확정 상태를 보존했다.

## Evidence and adversarial work
- 직접 열어 확인한 유의미 고유 문서: 13개 FRUS 문서(682, 734, 735, 737, 738, 739, 740, 741, 762, 763, 772, 774, 792). 이번 회차는 40문서 하한 미달이며 숫자 부풀림 없음.
- 공식/1차·동시대 공공 문서계열: 13개 모두 미 국무부 FRUS 수록 정부 기록. 한국측 원문으로 재분류하지 않음.
- 독립 연구선: 20+ (조약 조문, working party, initialing/signing 구분, 자동개입, UNC assurance, CEB, Tasca, 환율, local-cost, UNKRA, ECA, 비료공장, 일본조달, 육군 20개 사단, 해군, 공군, Pyun 개인발언 경계, SE-48 attribution, Hull 경고, Senate ratification 등).
- adversarial checks: 12.
- cross-provenance 묶음: 1개의 강한 미국 정부 계열 내부 교차검증만 확보. 한국 정부/국회 독립 provenance를 추가하지 못했으므로 3묶음 하한 미달.
- event/sub-event 후보: 12.
- 기존 open lead 추적: `lead-1953-defense-treaty-diff`를 실질적으로 좁혔으나 한국어 원문/8월 발행문/10월 서명문 조문 diff가 남아 NARROWED 유지. 관련 post-armistice lead 8+를 구체화.
- concrete next leads: 40.

## Interpretation changes
1. 8/8은 서명이 아니라 initialing이며 10/1 signing과 분리해야 한다.
2. 조약과 이승만의 정전/UNC 준수 약속은 서로 다른 법적·정치적 객체다.
3. 7/9 ROK 초안의 요구범위는 최종 협상과 동일하지 않다.
4. 백두진은 단순 배석자가 아니라 경제원조·환율·군 확장과 조약해석에 직접 개입했다.
5. 변영태의 10/2 비무장화 탐색 발언은 본인이 개인적 의견이라고 한 만큼 정부 확정정책으로 승격할 수 없다.
6. SE-48은 이승만의 통제력에 관한 미국 정보판단이지 개별 명령의 직접증거가 아니다.
7. post-armistice 재건은 원조액뿐 아니라 누가 계획·조정·집행을 통제할 것인가라는 행정권 문제였다.

## Files / commits
- `data/research/rhee-pass-61-postarmistice-treaty-aid-chain-2026-09-22.md` — commit `434436309536a31aa6d1a664381f167736bbd303`
- `data/research/candidates/pass-61-postarmistice-treaty-aid-actors.json` — commit `e4f1918dc472f585254d642ec29ed56b1a982e21`
- this run report — current commit

## Limits
이번 실행은 접근 가능한 시간/도구 여력에서 13개 문서를 직접 열어 검증했으며 40개 문서 하한에는 못 미쳤다. 또한 FRUS라는 하나의 provenance 계열에 편중됐다. 다음 회차 최우선은 한국 외무부/국무회의/국회/관보 원문을 붙여 treaty diff를 완성하는 것이다. 비대통령 10명 하한은 `실질 심화 3 + 신규/재식별 6 = 9`로 미달이며, `Minister Kim` 같은 불확실 인물을 억지로 승격하지 않았다.

## History debt
역사부채 주간 전수조사 미실시. 화요일 회차이며 일요일 첫 실행 조건이 아니다.

## Floot
수정·빌드하지 않음.
