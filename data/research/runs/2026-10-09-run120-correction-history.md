# Run120 데이터 정합성·귀속 정정 이력 (2026-10-09)

초기 run120 커밋 d9d2f2335c2b925f1d0fd9e04fc54fa8da2bdf04를 조용히 덮어쓰지 않고 다음 수정을 기록한다.

1. 1950-06-02 금통위원 대통령 결재는 신문 **보도된 결재**이지 임명 원부의 직접 확인이 아니므로 `decided_by`에서 `reportedDecidedBy`로 분리.
2. 광산연맹 요구에 대한 상공부의 **실제 반대 의결**은 미확인. `opposed_by`에서 삭제. 노조의 규정 철회 요구는 사건 설명에 보존.
3. 이윤영 사회부장관은 제3자 관찰자가 아니라 회견 당사자. `observed_by` 대신 `executed_by`.
4. 대법원 소송 제기자들의 신원 확인 전 임의 조직 `org-election-plaintiffs-1950` 사용 중단, 보도상 한자 명단 별도 보존.
5. 1950-06-02 서울신문의 李定卓과 한국은행 2016년 사진 설명의 이정재 대조 근거는 **한국은행 역사 연표**가 아니라 **해당 사진 설명이 실린 해설 기사**로 바로잡음. IT27656 원사진은 목록만 확인.
6. 위원회·노총·사회부·관재국·북측 단체·UNCOK의 반복 등장 기관을 `org120-*` stable ID로 등록. 단, 동시대 법적 기관의 실제 동일성은 계속 검증.

관련: `data/documents/run120-june1950-direct-audit.json`, `data/claims/run120-june1950-adversarial.json`, `data/events/run120-june1950-institutional-actions.json`.
