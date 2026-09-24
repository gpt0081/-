# Politician Network Pass 117 — execution ledger

Date: 2026-09-24
Focus: 황종률의 1952~1953 외자행정에서 `겸임 직책`을 법적 권한 두 계열로 분해하고, 다음 원문 회수 표적을 action-level로 재설계.

## Progress
- pass 116의 30개 lead queue와 황종률 evidence/annals/candidate를 이어받았다.
- 조달청 공식 역대청장 기록을 재확인해 황종률의 두 기관장 동시 재임(1952-12-26~1953-05-28)을 유지했다.
- `외자구매처임시설치법` 법률 제72호 원문을 직접 확인했다. 외자구매처는 대통령 직속이며 정부자금 및 외국 원조자금으로 구매하는 외자의 수입·구매를 관장하고, 처장은 소속공무원을 지휘감독하며 외자구매 사항에 한해 국무회의 열석·발언권이 있었다.
- `임시외자관리청설치법` 법률 제79호 원문을 직접 확인했다. 임시외자관리청은 국무총리 직속이며 수입 원조물자의 관리·배당·경리와 부대사무를 관장하고, 청장은 임시외자운영위원회 부위원장이며 소관사무 국무회의 열석·발언권과 지방사무소 지휘선을 가졌다.
- 따라서 기존 `외자구매처장 겸 외자관리청장` 단일 role을 `구매/수입 authority family`와 `도입 후 관리/배당/경리 authority family`로 분리했다.
- 두 기관의 상급기관도 대통령 직속과 국무총리 직속으로 달랐으므로, 황종률 개인을 단일 명령선으로 처리하지 않도록 annals/evidence/candidate를 동기화했다.
- 법률상 국무회의 열석 가능성과 실제 출석·발언을 분리했다. 실제 출석은 1953-01~05 국무회의 원 회의록 회수 전 OPEN이다.
- 법률상 기관장 지휘감독권과 개별 구매계약·배당·협상·결재를 분리했다. 개별 행위 귀속은 계속 OPEN이다.
- 1955년 외자청 통합의 후대 기관사 자료도 확인해 두 기능이 후일 통합됐음을 맥락으로만 기록했으며, 이를 1953년 당시 조직 일원화의 증거로 역투사하지 않았다.
- Floot는 수정·빌드하지 않았다.

## Counts
- Independent research/retrieval lines materially pursued: 14. 최소 20 미달.
- General domains touched: 6 (외자조달, 원조물자 관리, 행정조직, 국무회의 권한, 지방집행, 기관승계).
- Non-president actor nodes materially deepened: 3 (황종률, 현근, 이순용). 최소 10 미달.
- Event/sub-event materially structured/deepened: 6 (두 기관 겸임, 구매/수입 authority, 관리/배당/경리 authority, 운영위원회 부위원장, 제한적 국무회의 열석권, 중앙→지방 관리청 지휘선). 최소 8 미달.
- Meaningful unique documents/pages directly opened/reviewed: 13. Official/public-institution, statutory primary-text, or scholarly-reference: 6. 최소 40/20 미달.
- Adversarial/provenance checks: 8. 최소 10 미달.
- Existing open leads materially followed/narrowed: 7. 최소 8 미달.
- Cross-check bundles: 3 (재임기간; 두 기관 법정 권한 분리; 1953 권한과 1955 통합의 시간적 경계).
- Concrete next leads generated/refined: 30.

## State change
`황종률이 1952~1953 외자행정을 맡았다`는 넓은 서술을 더 이상 하나의 role edge로 쓰지 않는다. 법률 제72호와 제79호를 근거로 외자구매처의 구매·수입 권한과 임시외자관리청의 관리·배당·경리 권한을 분리했다. 두 기관 모두 황종률이 동시에 수장이었지만 법적 상급기관과 의사결정 장치가 달랐다. 실제 개인 행위는 문서별로 확인한다.

## Files changed
- `data/evidence/hwang-jong-ryul.json`
- `data/annals/hwang-jong-ryul.md`
- `data/research/candidates/hwang-jong-ryul-1909.json`
- `data/research/runs/2026-09-24-politician-network-pass-117.md`

## Commits
- `a8600d5fbc5cd7b14d1dca2aff0087d10bd1019d` evidence: separate legal powers of Hwang Jong-ryul dual offices
- `42ed3cba0dfddbfebac64f573d3ae96a7e31792e` annals: split Hwang Jong-ryul procurement and aid-management authority
- `1420b9dbda3fc5c374866350b6b28d84d3517a92` candidate: refine Hwang Jong-ryul dual-office authority graph
- this ledger commit: see commit containing this file

## Next priority lead queue
1. 대한민국 관보 1952-12-26 황종률 외자구매처장 임명 발령번호.
2. 대한민국 관보 1952-12-26 황종률 임시외자관리청장 임명 발령번호.
3. 대한민국 관보 1953-05-28 황종률 면직 및 이순용 외자구매처장 후임 발령.
4. 대한민국 관보 1953-05-28 이순용 임시외자관리청장 후임 발령.
5. 대통령령 제237호 외자구매처직제 원문과 국·과별 사무분장.
6. 1952~1953 시행 임시외자관리청 직제 대통령령 원문과 국·과별 사무분장.
7. 임시외자운영위원회 1952-12-26~1953-01 회의록·심의안건.
8. 임시외자운영위원회 1953-02 회의록·심의안건.
9. 임시외자운영위원회 1953-03 회의록·심의안건.
10. 임시외자운영위원회 1953-04 회의록·심의안건.
11. 임시외자운영위원회 1953-05-01~28 회의록·심의안건.
12. 1953-01 국무회의록의 외자구매·원조물자 안건 및 황종률 출석 여부.
13. 1953-02 국무회의록의 외자구매·원조물자 안건 및 황종률 출석 여부.
14. 1953-03 국무회의록의 외자구매·원조물자 안건 및 황종률 출석 여부.
15. 1953-04 국무회의록의 외자구매·원조물자 안건 및 황종률 출석 여부.
16. 1953-05-01~28 국무회의록의 외자구매·원조물자 안건 및 황종률 출석 여부.
17. 국가기록원 외자구매처 생산기록에서 황종률 발신·결재 문서 색인.
18. 국가기록원 임시외자관리청 생산기록에서 황종률 발신·결재 문서 색인.
19. 외자구매처의 정부·외국기관·수입업 단체 구매위임 문서 중 황종률 재임기 사례.
20. 임시외자관리청 지방사무소에 내려간 황종률 명의 지시문.
21. 현근→황종률 1952-12-26 외자구매처 인수인계 문서.
22. 현근→황종률 1952-12-26 임시외자관리청 인수인계 문서.
23. 황종률→이순용 1953-05-28 외자구매처 인수인계 문서.
24. 황종률→이순용 1953-05-28 임시외자관리청 인수인계 문서.
25. FRUS 1952~1953 Korean procurement에서 Hwang Jong-ryul/Hwang Chong-yul 변형 검색.
26. NARA MSA/FOA 한국 원조 조달문서의 한국측 counterpart 명단.
27. UNKRA 조달·물자관리 기록에서 외자구매처/임시외자관리청 접촉 기록.
28. 1941 『조광』 「만주국경제정책의 기본동향」 원문 및 저자 표기.
29. 1962 『한국경제』 「미국원조 사용의 정직한 자세」 원문과 1952~1953 기록 대조.
30. 관보 1960-05/10 충북지사 황종률 임면과 정인택→황종률→조대연 transition 원문.

역사부채 주간 전수조사 미실시.
