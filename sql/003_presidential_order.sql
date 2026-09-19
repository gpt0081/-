ALTER TABLE politicians
  ADD COLUMN IF NOT EXISTS presidency_order integer,
  ADD COLUMN IF NOT EXISTS term_label text,
  ADD COLUMN IF NOT EXISTS presidency_period text;

UPDATE politicians SET presidency_order=1, term_label='제1~3대', presidency_period='1948.07~1960.04' WHERE id='president-rhee-syngman';
UPDATE politicians SET presidency_order=2, term_label='제4대', presidency_period='1960.08~1962.03' WHERE id='president-yun-posun';
UPDATE politicians SET presidency_order=3, term_label='제5~9대', presidency_period='1963.12~1979.10' WHERE id='president-park-chunghee';
UPDATE politicians SET presidency_order=4, term_label='제10대', presidency_period='1979.12~1980.08' WHERE id='president-choi-kyuhah';
UPDATE politicians SET presidency_order=5, term_label='제11~12대', presidency_period='1980.09~1988.02' WHERE id='president-chun-doohwan';
UPDATE politicians SET presidency_order=6, term_label='제13대', presidency_period='1988.02~1993.02' WHERE id='president-roh-taewoo';
UPDATE politicians SET presidency_order=7, term_label='제14대', presidency_period='1993.02~1998.02' WHERE id='president-kim-youngsam';
UPDATE politicians SET presidency_order=8, term_label='제15대', presidency_period='1998.02~2003.02' WHERE id='president-kim-daejung';
UPDATE politicians SET presidency_order=9, term_label='제16대', presidency_period='2003.02~2008.02' WHERE id='president-roh-moohyun';
UPDATE politicians SET presidency_order=10, term_label='제17대', presidency_period='2008.02~2013.02' WHERE id='president-lee-myungbak';
UPDATE politicians SET presidency_order=11, term_label='제18대', presidency_period='2013.02~2017.03' WHERE id='president-park-geunhye';
UPDATE politicians SET presidency_order=12, term_label='제19대', presidency_period='2017.05~2022.05' WHERE id='president-moon-jaein';
UPDATE politicians SET presidency_order=13, term_label='제20대', presidency_period='2022.05~2025.04' WHERE id='president-yoon-sukyeol';
UPDATE politicians SET presidency_order=14, term_label='제21대', presidency_period='2025.06~현재' WHERE id='president-lee-jaemyung';

CREATE INDEX IF NOT EXISTS politicians_presidency_order_idx
  ON politicians (presidency_order)
  WHERE presidency_order IS NOT NULL;
