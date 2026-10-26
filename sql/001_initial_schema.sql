CREATE TYPE record_kind AS ENUM ('speech','pledge','vote','bill','policy','appointment','statement','action','explanation');
CREATE TYPE source_grade AS ENUM ('primary','secondary','analysis');
CREATE TYPE comparison_status AS ENUM ('candidate','reviewed','published','rejected');

CREATE TABLE politicians (
  id text PRIMARY KEY,
  name text NOT NULL,
  party text,
  role text,
  is_demo boolean NOT NULL DEFAULT false,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE records (
  id text PRIMARY KEY,
  politician_id text NOT NULL REFERENCES politicians(id) ON DELETE CASCADE,
  occurred_at date NOT NULL,
  kind record_kind NOT NULL,
  topic text NOT NULL,
  quote_or_action text NOT NULL,
  context text NOT NULL,
  claim_type text NOT NULL DEFAULT 'statement',
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE sources (
  id text PRIMARY KEY,
  record_id text NOT NULL REFERENCES records(id) ON DELETE CASCADE,
  title text NOT NULL,
  url text,
  publisher text,
  source_grade source_grade NOT NULL,
  published_at date,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE principles (
  id text PRIMARY KEY,
  politician_id text NOT NULL REFERENCES politicians(id) ON DELETE CASCADE,
  normalized_rule text NOT NULL,
  first_record_id text REFERENCES records(id) ON DELETE SET NULL,
  topic text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE comparisons (
  id text PRIMARY KEY,
  politician_id text NOT NULL REFERENCES politicians(id) ON DELETE CASCADE,
  record_a_id text NOT NULL REFERENCES records(id) ON DELETE CASCADE,
  record_b_id text NOT NULL REFERENCES records(id) ON DELETE CASCADE,
  principle_id text REFERENCES principles(id) ON DELETE SET NULL,
  topic text NOT NULL,
  rationale text NOT NULL,
  changed_conditions text,
  explanation text,
  review_question text NOT NULL,
  status comparison_status NOT NULL DEFAULT 'candidate',
  created_at timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT distinct_comparison_records CHECK (record_a_id <> record_b_id)
);

CREATE INDEX records_politician_date_idx ON records (politician_id, occurred_at DESC);
CREATE INDEX records_topic_idx ON records (topic);
CREATE INDEX comparisons_politician_status_idx ON comparisons (politician_id, status);
CREATE INDEX sources_record_idx ON sources (record_id);
