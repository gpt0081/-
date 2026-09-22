# Run report — Politician Network Pass 71

Date: 2026-09-22
Focus: pass 70의 UN 원문 lead queue를 따라 A/2450·711(VII)·1953 UN Yearbook·resumed-session Index로 provenance를 넓힘.

## Result

이번 회차의 핵심은 FRUS 내부에서만 돌던 정치회담 서술을 UN 자체 문서 계열로 교차검증한 것이다. A/2450의 검색색인 원문은 A/L.151/Rev.1이 ROK와 희망하는 Unified Command 병력기여국의 참가를 권고하면서도 각 참가국이 독립적으로 행동하고 자신이 동의한 결정·협정에만 구속된다고 설계했음을 확인한다. 따라서 `UN side`를 하나의 단일 의사결정 행위자로 취급하면 안 된다.

India 문제는 더 좁혀졌다. UN Yearbook은 First Committee가 A/L.153을 27–21–11로 채택했다고 기록하고, UN Index는 8월 28일 plenary에서 India 요청으로 해당 안을 표결하지 않았다고 명시한다. 이는 FRUS d752와 독립적으로 일치한다. 동시에 Yearbook은 미국이 공개적으로 `India 자체`가 아니라 비교전국 참가에 반대한다는 논리를 제시했고, India 참가 반대가 미국 외 여러 대표단에도 존재했음을 기록한다. 따라서 `이승만 반대 → 미국 복종 → India 배제` 단선 모델은 유지할 수 없다.

또 하나의 중요한 데이터 모델 함정을 발견했다. A/2450 단계의 resolution C는 India 참가안이고 D는 PRC/DPRK 통보안이지만, India안은 plenary에서 표결되지 않았다. 최종 UN Digital Library에는 A/RES/711(VII)[A]/[B]/[C]가 존재한다. 그러므로 `committee C = final 711C`라고 ID 문자만 보고 연결하면 잘못된 사건 귀속이 생긴다. draft → committee resolution → plenary disposition → final component의 version lineage가 필요하다.

## Execution ledger

- 직접 확인/검색색인으로 실질 확인한 문서·페이지: 9
- 공식·1차·공공기관 계열: 8
- 독립 연구선: 10
- adversarial checks: 10
- cross-provenance 묶음: 2 (UN 문서계열 ↔ FRUS, 그리고 UN report/index/yearbook 상호검증)
- 기존 lead 실질 진전: A/2450, 711 metadata, India committee/plenary disposition, Soviet conditional participation, A/C.1/L.48 indexing
- 새 concrete leads: 40
- event/sub-event 신규/보강 후보: 8
- 비대통령 한국 정치인 신규 승격: 0. 숫자를 맞추기 위한 이름 수집을 하지 않았고 임병직·변영태의 한국측 원문 lead를 유지함.
- Floot: 수정·빌드하지 않음

40문서/10 비대통령 한국정치인 하한은 이번 실행 창에서 달성하지 못했다. A/2450 PDF 직접 open은 UN 서버 403으로 막혀 검색색인 텍스트만 확인했으며 이를 PDF 직접 열람으로 허위 계산하지 않았다.

## Main adversarial findings

1. `India was voted down in First Committee` → CONTRADICTED.
2. `India was voted down in plenary` → CONTRADICTED.
3. `U.S. public India rationale was only Rhee pressure` → CONTRADICTED/NARROWED.
4. `Only U.S./ROK opposed India` → CONTRADICTED.
5. `USSR participation was unconditional` → CONTRADICTED.
6. `committee resolution C = final A/RES/711(VII)[C]` → CONTRADICTED; document-lineage trap.
7. `UN-side participants were one bound bloc` → CONTRADICTED.
8. `U.S. could unilaterally fix conference date/site` → CONTRADICTED/NARROWED by consultation/mutual-satisfaction language.
9. `FRUS India chronology is merely U.S. interpretation` → independently corroborated by UN records.
10. `A/C.1/L.48 exact membership is now fully primary-verified` → NOT YET; original remains a next target.

## Files / commits

- `data/research/rhee-pass-71-un-primary-record-crosscheck-2026-09-22.md` — `24d843d91b2c106eace6922ab9090e72cf616623`
- `data/research/candidates/pass-71-un-primary-record-actors.json` — `6dbfbd0f8ccdddcadd1b3b42a2d6098412125991`
- this report — current commit

## Highest-priority next queue

1. A/PV.430 exact Menon language.
2. First Committee 625th record.
3. A/L.153 original.
4. A/C.1/L.53 original.
5. A/L.152/Rev.2 original.
6. A/C.1/L.48 original.
7. A/C.1/L.48 revision.
8. A/C.1/L.52.
9. A/C.1/L.54–56.
10. A/L.158.
11. A/L.159.
12. A/2431/S/3079.
13. Resolution 705(VII).
14. A/L.151 vs Rev.1 diff.
15. consolidated 711 text.
16. committee A/B/C/D → final A/B/C lineage.
17. ROK speakers meetings 613–625.
18. 임병직 UN statements.
19. 변영태 instructions/statements.
20. ROK Observer Mission correspondence.
21. ROK cabinet minutes Aug.14–28.
22. ROK delegation official roster.
23. Lodge DOS Bulletin statement.
24. Canadian Paul Martin records.
25. Australian Spender records.
26. Indian MEA/Nehru records.
27. Soviet/Vyshinsky record.
28. PRC/Zhou record.
29. DPRK response.
30. organization registry IDs.
31. document-version relation schema.
32. public-vs-private rationale evidence typing.
33. committee/plenary vote-level field.
34. roll-call/non-recorded vote type.
35. UN final-component label lineage audit.
36. A/2450 Add.1.
37. meetings 613–624 argument evolution.
38. 15 contributor states' participation decisions.
39. Geneva 1954 participant comparison.
40. Berlin/Geneva forward linkage.

역사부채 주간 전수조사 미실시. 화요일이며 일요일 첫 실행 조건이 아니다.
