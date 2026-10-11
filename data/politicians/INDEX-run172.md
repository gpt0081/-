# Run172 정치인 registry 통합 인덱스

- 정식 중앙 `data/politicians.json`에 연구 노드 2명 연결: `pol-r170-shin-jung-mok`(농림부장관, 독립 실록·증거 파일 보강), `pol-r172-kim-tae-seon`(내무부장관, 1952-08-26 대통령령 제812호 서명 및 기존 run118 독립 실록).
- 그 외 16명은 `data/politicians/run172-actors-a.json`~`run172-actors-d.json`의 후보·보강 노드로 보존. 한자·생몰·정당·지역구 미검증인 경우 승격 보류.
- 곽상훈은 run170의 `pol-r170-gwak-sang-hun`을 재사용한다. run172 임시 중복 ID는 후속 교정하여 합병했다.
- 지연해의 한자 `池蓮海`·`池連海` 표기 차이는 동일인 검증 전까지 보존.
- 노동단체 임원은 공직·정당 정치활동 검증 전에는 단체행위자로만 취급하고 정치인 등록을 자동 확정하지 않는다.
- 기존 독립 실록 `data/annals/kim-tae-seon-run118.md` 및 `data/annals/pol-r170-shin-jung-mok.md`를 재사용한다. 1952년 보강: `data/annals/shin-jung-mok-run172.md`.
- 김태선 생몰연도는 한국민족문화대백과사전 원문과 run118 기록을 대조했다. 후보 초안의 미확인 표기는 `data/politicians/run172-kim-tae-seon-biography-addendum.json`으로 정정 경위를 보존.

승격은 역사적 선악 판정이 아니라 자료 연결과 독립 실록의 연구 성숙도를 나타낸다.
