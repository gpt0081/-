# Document registry shard index

갱신 기준: 2026-10-29, pass244 추가. 경로 색인이며 전수 중복 URL/ID 정규화는 별도 과제.

`original_text_opened`와 `document_kind`를 반드시 구분하고, 색인 페이지·후대 편집주석을 원작성 원문으로 계산하지 않는다.

## Shards

- `data/documents/pass-229-1952-cabinet-economy-trial.json`
- `data/documents/pass-229b-1952-governance-oversight.json`
- `data/documents/pass-229c-1952-martial-constitution-welfare.json`
- `data/documents/pass-229d-1952-local-justice-economy.json`
- `data/documents/pass-231-1952-june-july-diplomacy-election.json`
- `data/documents/pass-232-1952-september-governance.json`
- `data/documents/pass-233-1952-oct-nov-frus-un.json`
- `data/documents/pass-233-addendum-1952-nikh-press-letters.json`
- `data/documents/pass-233-dec1-unkra-rok-confirmation.json`
- `data/documents/pass-233-followup-un-japan-primary.json`
- `data/documents/pass-234-1952-dec-state-finance.json`
- `data/documents/pass-234-addendum-1950-icrc-un-1952.json`
- `data/documents/pass-234-addendum-1952-dec-11-15.json`
- `data/documents/pass-234-addendum-d-1952-1955-economic.json`
- `data/documents/pass-235-1953-jan-mar-crossprovenance.json`
- `data/documents/pass-235-addendum-b-domestic-budget-culture.json`
- `data/documents/pass-235-addendum-c-february-currency-courts.json`
- `data/documents/pass-235-addendum-d-original-legal-provenance.json`
- `data/documents/pass-235-addendum-e-assembly-energy-fisheries.json`
- `data/documents/pass-235-addendum-f-1945-1953-economy-diplomacy.json`
- `data/documents/pass-235-addendum-g-agriculture-statistics-fisheries.json`
- `data/documents/pass-235-addendum-h-diplomacy-soldier-welfare.json`
- `data/documents/pass-235-addendum-i-march-finance-party.json`
- `data/documents/pass-236-frus-march-april-registry.json`
- `data/documents/pass-236-labor-law-registry.json`
- `data/documents/pass-236e-party-labor-sources.json`
- `data/documents/pass-236f-rhee-correspondence-catalog.json`
- `data/documents/pass-236g-march-april-correspondence-catalog.json`
- `data/documents/pass-236h-april-correspondence-catalog.json`
- `data/documents/pass-237-frus-april-may.json`
- `data/documents/pass-237b-korean-contemporary.json`
- `data/documents/pass-238-may-armistice.json`
- `data/documents/pass-239-may-june-source-registry.json`
- `data/documents/pass-239b-june2-6-sources.json`
- `data/documents/pass-239d-june8-22-source-registry.json`
- `data/documents/pass-239e-june22-30-korean-originals.json`
- `data/documents/pass-239f-labor-institution-registry.json`
- `data/documents/pass-239g-july-organization.json`
- `data/documents/pass-239h-july1953-diplomacy-cabinet.json`
- `data/documents/pass-239i-postarmistice-treaty.json`
- `data/documents/pass-239j-1954-agreed-minute-ratification.json`
- `data/documents/pass-239k-1955-first-half.json`
- `data/documents/pass-239k2-1955-second-half.json`
- `data/documents/pass-239l-1955-56-diplomacy-election.json`
- `data/documents/pass-239l2-1955-un-original-election-catalog.json`
- `data/documents/pass-239m-1954-constitutional-originals.json`
- `data/documents/pass-239m2-1954-proposal-and-reversal-signers.json`
- `data/documents/pass-239m2-expanded-primary-registry.json`
- `data/documents/pass-239m2-fiscal-foreign-addendum.json`
- `data/documents/pass-239m3-1954-economic-assembly-originals.json`
- `data/documents/pass-240-1955-originals.json`
- `data/documents/pass-241-1956-57-originals.json`
- `data/documents/pass-242-1957-jun-dec.json`
- `data/documents/pass-242b-1958-followthrough.json`
- `data/documents/pass-243-1958-statecraft.json`
- `data/documents/pass301-documents.json`
- `data/documents/pass302-documents.json`
- `data/documents/pass303-documents.json`
- `data/documents/pass305-korean-documents.json`
- `data/documents/pass306-breadth-documents.json`
- `data/documents/pass317-education-health-documents.json`
- `data/documents/pass318-rhee-documents.json`
- `data/documents/run10-rhee-debt-documents.json`
- `data/documents/run11-rhee-statecraft-documents.json`
- `data/documents/run11b-1960-crisis-documents.json`
- `data/documents/run12-1960-transition-frus.json`
- `data/documents/run13-1960-transition-korean-primary.json`
- `data/documents/run14-419-firing-accountability.json`
- `data/documents/run16-peacetime-institutions-documents.json`
- `data/documents/run18-rhee-security-constitutional-crosscheck.json`
- `data/documents/run20-land-reform-documents.json`
- `data/documents/run21-education-statebuilding-documents.json`
- `data/documents/run22-education-legislation-primary-documents.json`
- `data/documents/run23-education-institutions-documents.json`
- `data/documents/run24-education-governance-documents.json`
- `data/documents/run25-education-finance-legislative-documents.json`
- `data/documents/run26-education-finance-local-implementation.json`
- `data/documents/run27-education-finance-legal-clarification.json`
- `data/documents/run30-rhee-command-documents.json`
- `data/documents/run32-pusan-domestic-actors.json`
- `data/documents/run33-1952-constitutional-statecraft.json`
- `data/documents/run36-1952-pusan-adversarial-followup.json`
- `data/documents/run37-1952-pusan-command-compromise.json`
- `data/documents/run47-pow-command-frus.json`
- `data/documents/run48-pow-jcs-source-trail.json`
- `data/documents/run50-pow-armistice-frus.json`
- `data/documents/run51-robertson-armistice-bargain.json`
- `data/documents/run52-armistice-implementation-reconstruction.json`
- `data/documents/run52-robertson-negotiation-documents.json`
- `data/documents/run53-postarmistice-frus-734-779.json`
- `data/documents/run54-v2-treaty-korean-crosscheck.json`
- `data/documents/run55-treaty-ratification.json`
- `data/documents/run60-first-republic-institutional-network.json`
- `data/documents/run61-labor-progressive-japan.json`
- `data/documents/run62-state-capacity-network.json`
- `data/documents/run63-aid-reconstruction-economic-governance.json`
- `data/documents/run64-first-republic-institutional-opposition-network.json`
- `data/documents/run65-315-election-accountability.json`
- `data/documents/run66-economic-governance-network.json`
- `data/documents/run69-election-control-documents.json`
- `data/documents/run74-april1960-transition-documents.json`
- `data/documents/run75-second-republic-transition-documents.json`
- `data/documents/run77-315-command-chain.json`
- `data/documents/run79-landreform-parliamentary-correction.json`
- `data/documents/run80-farmland-parliamentary-primary.json`
- `data/documents/run81-land-legal-primary.json`
- `data/documents/run88-civil-audit.json`
- `data/documents/run88-constitutional-treaty-labor.json`
- `data/documents/run88-economic-education.json`
- `data/documents/run88-education-court-originals.json`
- `data/documents/run88-farmland-government-org.json`
- `data/documents/run88-health-local.json`
- `data/documents/run88-investigative-organization.json`
- `data/documents/run88-judicial-security-primary.json`
- `data/documents/run88-martial-land-defense.json`
- `data/documents/run88-politics-personnel.json`
- `data/documents/run88-who-membership-and-1951.json`
- `data/documents/run88-who-official-records.json`
- `data/documents/weekly-history-debt-documents-2026-10-04.json`

- `data/documents/pass-244-1959-1960-originals.json` (pass244; 2026-10-29)
- `data/documents/pass-244b-1960-transition-originals.json` (pass244; 2026-10-29)

- `data/documents/pass-244c-official-crosschecks.json` (pass244f; NEC/NIKH/Eisenhower archival finding aid)

- `data/documents/pass-244d-constitutional-sources.json` (pass244g; 2026-10-29)

- `data/documents/pass-244e-senate-election-law-metadata.json` (pass244h; law469/502/551 metadata)

## pass246 (2026-10-29)
- data/documents/pass-246-1956-1960-law-and-identity.json : 관보 법률385·388·470·공고91·548·551·552·557·563, 민주화운동기념사업회 6/15 신문인용일지, 국편 3/15 선거표. 기존 DOC-P245-GAZ-05(469), DOC-P245-GAZ-09(헌법4호), DOC-P245-NA-08(국회37차)는 중복 생성하지 않고 재사용. 같은 관보 URL에 서로 다른 법률469·470이 포함될 수 있음.

## pass247 (2026-10-29)
- `data/documents/pass-247-1960-constitutional-party-sources.json`: 헌법제52조·부칙, 2명 김성숙, 당무 사료 16건(색인 1 제외).

## pass247b (2026-10-29)
- `data/documents/pass-247b-succession-and-administration.json`: 1960 미국대사관 원전·국가기록원 국무회의·1952 인구/경제·AKS 곽상훈/백낙준.

## pass247c (2026-10-29)
- `data/documents/pass-247c-june1960-original-diplomacy.json`: 1960 미대사관·USIS 원전8건.

## pass247d (2026-10-29)
- `data/documents/pass-247d-korean-assembly-originals.json`: 국회 원회의록 12건, 6/15 개헌208:3 국내원문.

- 2026-10-29 pass248: `data/documents/pass-248-1960-local-election-crosscheck.json` (1960 지방선거·김상돈·출처충돌 검증).

- 2026-10-29 pass249: `data/documents/pass-249-civic-rights-seoul.json` (법률원문 전사·공문서 색인·신문전사·서울시 사진목록; original_text_opened 구분).

- pass249 정정: 법률587 본문 JS 미확보 original_text_opened=false; LE-00-29053(14쪽)·BA0084191(13쪽) 원면 추적.

- pass249 UN Yearbook 1952 pp175~178 원문 전사 1건(4쪽 중복계수 금지), 국편 1952-10-21 신문 원문 전사 1건, 중앙선관위 1952 대선 통계 해설 2건. A/2187 원보고서 미열람.

- pass249 FRUS Korea XV/1 d135·d137~155 20개 독립 문서 직접 열람, d138 후대 편집주석 1개는 원문 1차 자료에서 제외. 19개 미국 외교·합참 원문.

- `data/documents/pass-250-1952-primary.json`: 1952년 3~6월 국편 헌정사 원문 전사 17건(원면 0), provenance별 구분.

- 2026-10-29 pass252: `data/documents/pass-252-1952-aug20-27-primary.json` 신규 문서 65건(신문전사 52, 번역발췌7, 관보1, FRUS3, 대통령기록관1, 국편해제1); 직접 열린 고유 문서 66건 중 기존 DOC-NIKH-P229-dh_026_1952_08_22_0070 재사용 1건. 원면 이미지 0건.

- 2026-10-29 pass252B: `data/documents/pass-252b-1952-aug26-30-originals.json` 직접열람 40건, 신규 등록 39건, 기존 DOC-P231-KOR-0826 재사용. FRUS XV/1 245~250 6건·관보 제812호 1건 포함.
- 2026-10-29 pass252C: `data/documents/pass-252c-1952-aug31-originals.json` 직접열람·신규 등록 9건. 육군본부 지령 제60호 전사·동시대 국무위원 명단·부산 지방세·경찰 고문 의혹 반론 포함.

- data/documents/pass-253-1952-september-frus-and-domestic.json (pass253, 2026-10-29)

- data/documents/pass-253d-september-korean-followup.json (pass253D, 2026-10-29)

- data/documents/pass-253e-september-sept9-11.json (pass253E, 2026-10-29)

- data/documents/pass-253f-september-sept12-15.json (pass253F, 2026-10-29)

- 2026-10-29 Pass255H: `data/documents/pass-255h-oct13-17-assembly-economy.json` (원문 출처·불확실성 보존).

- 2026-10-29 Pass257J: `data/documents/pass-257j-un-plenary-finance.json` 12건(UN 원속기/원수정안4, 한국 동시대 신문2, 후대 기관/법제처6). 법률277호 원면은 아직 미확보; 검색발췌는 원문 열람 수에 불포함.

- 2026-10-29 Pass257K: `data/documents/pass-257k-1953-constitutional-labor-archives.json` 3건 대통령기록관 개별 원문철 **해제** + 1건 법제처 법률276호 **색인**. 원문 원면 열람으로 계산하지 않음.

- 2026-10-29 Pass257L: `data/documents/pass-257l-un-committee-originals.json` UN A/2278 원보고서(심한 OCR 손상, 부분 판독) 및 A/2284 재정위원회 원보고서(주요 항목 판독) 2건. 원면 육안검증은 아직 미실시.

- 2026-10-29 Pass257M: `data/documents/pass-257m-1953-mar-apr-public-economy.json` 동시대 원신문 전사 4건(김유택·이승만 담화, 민주신보 비판, 서울시 비상미 배급 지연).

- 2026-10-29 Pass257N: `data/documents/pass-257n-1953-feb19-27-parliament-press.json` 1953-02-19/27 동시대 원신문 10건+AKS 후대 전기 2건. 법277호 제9·11조 표결 원기사 직접 열람.

- 2026-10-29 Pass257O: `data/documents/pass-257o-1953-law-1954-election-audit.json` (국편 선거 후대 편찬표, 법제처 1953/1962 동명 법령 색인, 국가기록원 해설, 제3자 파생집계; original body 0).

- 2026-10-29 Pass257O2: `data/documents/pass-257o2-1954-election-frus-originals.json` (FRUS 1954-05-24, 1954-07-14 동시대 원문 2건 및 국편 헌정사 후대 해제 1건).

- 2026-10-29 Pass257O3: `data/documents/pass-257o3-1953-law277-bok.json` (법277 24개 조문 제3자 역사법령 재현·한국은행 1953 후대 공식전시; 별표·원관보 미열람).

- 2026-10-29 Pass257O4: `data/documents/pass-257o4-uncurk-yearbook-originals.json` (기존 DOC-P239K-UN-A2711·DOC-P239K-NEC-1954-ELECTION ID 재사용, 신규 UN Yearbook 1954 1건).

- 2026-10-29 Pass257P: `data/documents/pass-257p-unkra-housing-finance-primary-audit.json` (UN A/2750·UNCURK A/2810·UN 제2위원회 SR340/SR341 원문 전체, UN A/RES/410(V) 5쪽·725(VIII) 1쪽·828(IX) 2쪽, 서울기록원 재건주택 공식해설·사진 5점 원이미지, 외무부 CA0002578 32쪽 원본의 **목록만** 확보; 법제처 법률302·311/대통령령860 연혁 메타데이터; 원문/목록/시각사료 분리).

  - Pass257P supplement: A/2487 1953 UN Board of Auditors 원문, A/2222 1952 초기보고, A/3651 1957 후속보고 직접 열람. 고유 등록 문서 22개 중 동시대 원문 텍스트 10건·동시대 사진 5점, 원문 미확보 목록 별도.

  - Pass257P supplement2: A/2801 1954 UN ACABQ 원문·A/RES/880(IX) 원결의·영국 하원 1953/1954/1955 Hansard 원문 5건 추가. 총 등록 27건(원문 텍스트 15, 사진 원이미지 5, 기타 공식 해설·목록).

- 2026-10-29 Pass257Q: `data/documents/pass-257q-1954-cabinet-gazette-originals.json` 제5회 국무회의록 1/22, 관보1049 1/23 신규 원전사 2건, 기존 7건 ID 재사용. 목록 11/29 충돌.

- Pass257Q FRUS addendum: original documents d862/d867/d873/d868/d869, Jan27–Feb25 1954 tungsten renewal and presidential letter; 5 new document IDs in `data/documents/pass-257q-1954-cabinet-gazette-originals.json`.

- Pass257Q health addendum: 법률307·308호 official metadata, KDCA 검역사, later judicial judgment, National Archives 1954 timeline (full original statutes not extracted).

- Pass257Q diplomatic addendum: four FRUS originals d692/d737/d871/v14p2-d606 for 1953 aid complaints, Feb1954 letter withdrawal and 1952 maritime tensions.

- Pass257Q UN original addendum: ECAFE Economic Survey1956 and UNKRA A/3195 primary original PDF texts, independent tungsten agreement expiry/exports.
- 2026-10-29 Pass257R 1954 FRUS 원문 36신규+2재사용, NEC/NIKH/NAK 공식 후대자료8. `data/documents/pass-257r-1954-policy-election-frus.json`.

- 2026-10-29 Pass257S: `data/documents/pass-257s-1954-july-august-originals.json` FRUS 1954-05-10·07-07~08-05 원문 16 신규·2 재사용, 편집주석2 원문과 분리.
- 2026-10-29 Pass257T 대통령기록관 1954/1955 이승만 발언 13건 및 1954 조약 원문 재검증, Pass257S FRUS d921~931 중복 9건 canonical Pass239J ID로 정정.
- 2026-10-29 Pass257U 1954 대통령 주거·신문·한글·정당 발언 원문 4건.

- 2026-10-29 Pass257W: 1954 선관위 2010 총선연구, FRUS 제네바 5/22, 국편 개헌 해설, 국가기록원 1954 국무회의 원문발췌, 산업용 화약 원기사 재인용: `data/documents/pass-257w-1954-election-un-geneva-registry.json`, `data/documents/pass-257w2-1954-cabinet-industry-sources.json`.
- Pass257W3 **1954 UNCURK A/2711 원문 OCR 직접 확보** (기존 403 접근이력 보존): `data/documents/pass-257w3-uncurk-1954-original.json`. 본문 §74 자유당115·무소속67 vs 부록 III 자유당114·무소속68. 원면 시각 검증은 미실시.
- Pass257W4 윤건중 AKS 독립 인명·생몰, 1954-04-06 담화의 04-08 경향신문 보도 후대 인용: `data/documents/pass-257w4-1954-minister-speech-secondary.json`.

- 2026-10-30 Pass258A: `data/documents/pass-258a-1954-foa-frus-source-audit.json` (1954 FOA 원조 원문 및 1954 한미·총선 반증, 기존 FRUS canonical ID 재사용; Floot 변경 없음).

- `data/documents/pass-258b-1953-54-aid-authority-primary.json` (1953 닷지 조직안·FRUS d728·EO10458·아이젠하워 의회교서·1954 6월 OEC 비망록 5절; 동일 원작성 계열 중복 주의)
- `data/documents/pass-258b-fy1955-rok-us-agreed-draft-signed.json` (1954 FY55 의회원조 문서 5종 + FRUS d980, 9월 초안 vs 11월 서명 분리)

- 2026-10-30 Pass258C: `data/documents/pass-258c-1954-55-implementation.json` (existing treaty and FRUS IDs reused).

- 2026-10-30 Pass258D: `data/documents/pass-258d-1955-56-exchange-nnsc.json` (1955 환율 270·700·500, NNSC 8월 사건, 비대통령 행위자·증거 불확실성).

- `data/documents/pass-258e-1956-domestic-governance.json` (Pass258E, 2026-10-30; 기존 canonical FRUS 재사용, 1956 국내 국정 연결)

- 2026-11-22 Pass329 김성수 부통령 사표 제출·수리 절차: `data/documents/run329-kim-seong-su-resignation.json` (국편 자료대한민국사 제25권의 서울신문 1952-05-31·경향신문 1952-06-30 전사 2건, AKS 해제 2건, 국편 사망연표 1건, 2010년 후대 재인용 1건. 원신문 원지면·사표 원본은 미확보; provenance 계열을 분리).
