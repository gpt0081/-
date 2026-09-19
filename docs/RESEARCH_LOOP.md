# GPT Research Loop

핵심 운영 문장:

> **수집은 공격적으로, 공개는 보수적으로.**

## 목적

GPT 루프는 많은 공개 자료를 빠르게 훑어 사람이 놓치기 쉬운 과거 발언·공약·표결·행동 기록을 수집 후보로 만든다.

루프는 정치인을 판정하지 않는다. "내로남불", "위선", "좋은 후보", "나쁜 후보" 같은 결론을 생성하거나 점수화하지 않는다.

## 중립성 규칙

모든 추적 대상에 같은 검색 규칙을 적용한다.

- 정당·이념에 관계없이 같은 출처 우선순위 사용
- 모순 가능성이 있는 기록만 찾지 않고 일관성을 뒷받침하는 기록도 함께 수집
- 상대 진영의 주장만으로 사실 확정 금지
- 공식 원문과 1차 자료 우선
- 1차 자료가 없을 때만 신뢰할 수 있는 2차 보도를 보조적으로 사용
- 날짜·인용·URL·문맥을 추정해서 채우지 않음

## Floot loop

현재 설계:

- 3시간마다 실행
- Asia/Seoul 기준
- 한 번에 최대 2명의 enabled 실존 target 처리
- 가장 오래 검색되지 않은 target 우선
- gpt-5.6-luna + hosted web_search
- 한 target당 최대 10개 고가치 후보
- SHA-256 fingerprint로 중복 방지
- 결과는 research_candidates(status=pending)에만 적재
- demo 정치인은 검색 대상에서 제외

## 상태 흐름

research target
→ research run
→ pending research candidate
→ human review
→ record/source 등록
→ comparison candidate
→ human review
→ published comparison

중간 검토 단계를 건너뛰고 검색 결과를 공개 페이지에 직접 올리지 않는다.

## 다음 단계

- 관리자 전용 검토 큐
- candidate 승인/반려
- 승인 시 records + sources로 승격
- principle 자동 후보 추출
- 기존 기록과 의미 검색
- comparison candidate 생성
- 수정 이력과 반론 제출 기능
