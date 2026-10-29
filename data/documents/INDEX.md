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
