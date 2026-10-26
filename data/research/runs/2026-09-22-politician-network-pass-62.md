# Run report — Politician Network Pass 62

Date: 2026-09-22
Focus: Korean-origin/public archival corroboration of the mutual-defense treaty legal chain after the FRUS-heavy Pass 61.

## Result
Pass 61의 가장 큰 약점이었던 `미국 정부 provenance 편중`을 일부 해소했다. 대통령기록관 특별전시와 복원 페이지를 직접 확인하여 1953-08-08 가조인, 1953-10-01 정식서명, 1954-01-13 대통령 재가, 1954-01-15 국회 동의, 1954-01-19 미국 상원 동의, 1954-01-22/29 외무부 비준서 교환 준비, 1954-02-01 주미대사 처리 지시, 1954-11-17 합의의사록/비준서 교환, 1954-11-18 발효를 서로 다른 단계로 분리했다.

핵심 attribution 교정도 강화됐다. 조약의 한국측 정식 서명자는 이승만이 아니라 외무장관 변영태이며, 이승만의 역할은 요구·협상·가조인식 참석·공개담화·대통령 재가 등으로 분해해야 한다. 1954-11-17 단계에는 주미대사 양유찬이 독립 행위자로 등장하므로 새 candidate node를 만들었다.

## Evidence / adversarial work
- 직접 연 유의미한 한국 공식 아카이브 페이지: 2. 페이지 안에 다수의 개별 기록물 메타데이터가 있지만 직접 원문을 연 것으로 부풀려 세지 않았다.
- 원문 다운로드는 ZIP/TIFF endpoint라 현재 텍스트 fetcher에서 직접 판독하지 못했다. 따라서 `원문 확보`로 기록하지 않고 access limitation으로 보존했다.
- adversarial checks: 10.
- 독립 연구선: 20+.
- cross-provenance: FRUS에서 얻은 `8/8 initialing ≠ 10/1 signature`, 자동개입 요구의 실패, treaty와 후속 command/Agreed Minute의 분리를 한국 대통령기록관/국가기록원 메타데이터로 독립 확인했다. 다만 국회 속기록·관보 원문은 아직 미확보다.
- event/sub-event: 9개 법적 단계 후보를 구조화했다.
- existing open lead: `lead-1953-defense-treaty-diff` 1개를 추가로 좁혔으나 조문 원문 diff가 없어 NARROWED 유지.
- new concrete leads: 30.

## Politician graph
- 변영태: 미국측 기록에 더해 한국 아카이브 provenance로 가조인·정식서명 행위를 강화.
- 양유찬: 신규 IDENTIFIED candidate. 1954-11-17 합의의사록/비준서 교환의 대한민국 대표로 확인.
- 이승만: `정식 서명자`로 잘못 귀속할 가능성을 차단하고 1954-01-13 재가 행위를 별도 노드화.

이번 회차는 비대통령 10명 하한을 충족하지 못했다. 억지로 인물을 늘리지 않고 treaty legal-chain의 한국 provenance 보강에 집중했다.

## Files / commits
- `data/research/rhee-pass-62-korean-treaty-ratification-chain-2026-09-22.md` — `6cc778ffe2d7534fc38491a88b40b5b6b76ec650`
- `data/research/candidates/pass-62-korean-treaty-ratification-actors.json` — `937b57e59ecbbc52ca35e4b326615e42f68e1ca0`
- this run report — current commit

## Limits
40개 직접 문서 하한과 비대통령 10명 하한, 8개 기존 debt/lead 추적 하한은 이번 실행에서 미달이다. 가장 큰 병목은 대통령기록관 개별 원문이 ZIP/TIFF로 제공되어 현재 텍스트 도구에서 직접 열리지 않은 점과, 국회 1954-01-15 속기록을 이번 실행에서 직접 확보하지 못한 점이다. 다음 회차는 국회 제18회 제15차 본회의와 관보 조약 제34호를 최우선으로 한다.

## History debt
역사부채 주간 전수조사 미실시. 화요일이며 일요일 첫 실행 조건이 아니다.

## Floot
수정·빌드하지 않음.
