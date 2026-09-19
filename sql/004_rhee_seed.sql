INSERT INTO records (id, politician_id, occurred_at, kind, topic, quote_or_action, context, claim_type) VALUES
('rhee-1948-oath', 'president-rhee-syngman', '1948-07-24', 'speech', '헌정질서', '국헌을 준수하고 국민의 복리를 증진하며 국가를 보호하여 대통령의 직책을 성실히 수행하겠다고 취임 선서했다.', '초대 대통령 취임식에서 한 공식 취임선서 기록이다.', 'normative'),
('rhee-1952-first-amendment', 'president-rhee-syngman', '1952-07-07', 'action', '헌정질서', '1952년 제1차 개헌이 공포되어 대통령 선출 방식이 간선제에서 직선제로 바뀌었다.', '한국사데이터베이스 헌정사 연표는 1952년 7월 4일 의결, 7월 7일 공포와 함께 대통령 직선제 도입을 기록한다.', 'institutional_change'),
('rhee-1954-second-amendment', 'president-rhee-syngman', '1954-11-29', 'action', '헌정질서', '1954년 제2차 개헌이 공포되면서 당시 대통령에게 중임 제한을 적용하지 않는 부칙이 포함되었다.', '국사편찬위원회 사료는 이 개헌의 부칙과 개헌안 처리 과정을 함께 제시한다.', 'institutional_change'),
('rhee-1960-resignation', 'president-rhee-syngman', '1960-04-26', 'action', '헌정질서', '4·19혁명 이후 1960년 4월 26일 하야성명을 발표했다.', '국가기록원 3·15 부정선거·4·19혁명 기록관의 하야 기록에 따른다.', 'office_exit')
ON CONFLICT (id) DO NOTHING;

INSERT INTO sources (id, record_id, title, url, publisher, source_grade, published_at) VALUES
('src-rhee-1948-oath', 'rhee-1948-oath', '이승만 취임선서', 'https://www.pa.go.kr/research/contents/speech/index.jsp?artid=1311382&catid=c_pa02064&spMode=view', '행정안전부 대통령기록관', 'primary', '1948-07-24'),
('src-rhee-1952-first-amendment', 'rhee-1952-first-amendment', '대한민국사연표 - 제1차 개헌', 'https://db.history.go.kr/id/tcct_1960_06_15_0020', '국사편찬위원회 한국사데이터베이스', 'primary', '1952-07-07'),
('src-rhee-1954-second-amendment', 'rhee-1954-second-amendment', '사사오입 개헌', 'https://contents.history.go.kr/front/hm/view.do?levelId=hm_149_0080', '국사편찬위원회 사료로 본 한국사', 'primary', '1954-11-29'),
('src-rhee-1960-resignation', 'rhee-1960-resignation', '이승만대통령의 하야', 'https://theme.archives.go.kr/next/history/samilos/sub3_12.do', '국가기록원', 'primary', '1960-04-26')
ON CONFLICT (id) DO NOTHING;
