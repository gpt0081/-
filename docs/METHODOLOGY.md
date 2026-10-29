# 편집·검증 방법론 (정치인 실록 데이터 계층)

## 목적과 독립성
대한민국 역대 주요 정치인·정당·기관의 검증 가능한 디지털 실록을 만든다. 대통령은 시간순 탐색의 backbone일 뿐 상위 데이터 계층이 아니다. 기존 판별기 UI는 조사 데이터와 별도로 두며 AI가 인물별 위선·선악·추천·순위·정치성향 점수를 산출하지 않는다.

## 문서 → 주장 → 사건 → 인물
문서 registry에는 stable document ID, 문서번호, 원작성일, 발신·수신, 작성기관, 원문위치, 원면 확보 여부, 접근일, provenance family, 번역/편집/재인용 여부를 보존한다. FRUS 편집각주, 국편 전사, 당사자 원작성 문서는 증거의 독립성 측면에서 동일하지 않다. 같은 원작성 문서를 여러 사이트가 재인용해도 독립 증거 2건으로 세지 않는다.

주장 registry에는 `supporting_evidence`, `contradicting_or_limiting_evidence`, `contextual_evidence`, `insufficient_evidence`와 검토이력을 둔다. 사건은 `proposed_by / decided_by / executed_by / opposed_by / legal_authority / observed_by / later_finding`을 구분한다. 미국 외교관의 '이승만이 동의했다'는 보고는 한국 정부의 원서명·실제 군사집행과 동일하지 않다. 당사자의 경찰 미행 주장도 경찰 명령 증거가 아니다.

정치인은 안정 ID와 이명·한자·영문·생몰 확인수준·시기별 공직·당적·선출/임명·사건 연결·evidence coverage·open leads·history debt를 가진다. DISCOVERED → IDENTIFIED → VERIFIED → ANNALS_ACTIVE → MATURE는 자료성숙도일 뿐 인물의 가치·중요도 순위가 아니다. 기존 중복 ID는 전체 참조 검증 없이 자동병합하지 않는다.

## 사료 품질 및 수치 감사
당대 신문 보도·사설은 당시 보도·여론의 증거이지 그 속 모든 행정 결정의 실제 집행증거가 아니다. 통계는 분모, 기준시점, 조사대상, 통화/계량단위, 명목·실질 여부를 명시한다. 기사 산술이 불일치하면 원전 표기와 계산값을 병치하고 CONFLICTED로 남긴다. 원면/OCR 오류 가능성을 검증하기 전에는 원문을 무단 교정하지 않는다. 예: `data/research/audits/pass-255-public-tariff-arithmetic.json`.

## 검증 및 정정
공식 1차자료, 국회·법원·정부, 동시대 신문, 해외 외교문서의 독립 provenance를 우선한다. 반대 당사자 기록과 실제 결정·집행·후대 판단을 별도로 탐색한다. 새로운 자료가 기존 설명을 반박하면 silent overwrite 대신 review/correction history를 남긴다. OPEN/NARROWED/BLOCKED/CONFLICTED/REOPENED를 임의로 RESOLVED하지 않는다. 일요일 Asia/Seoul 첫 실행에만 역사부채 전수재검토를 수행한다.

## 운영
자료 조사·검증·커밋은 GitHub 데이터 계층에서 수행하며 Floot는 명시적 별도 요청 없이 수정·빌드하지 않는다. `docs/HOURLY_ANNALS_LOOP.md`와 `docs/KOREA_POLITICAL_FOREST.md`의 전역 지침을 따른다.
