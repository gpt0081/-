CREATE TYPE research_run_status AS ENUM ('running','completed','no_findings','error','out_of_credits','rate_limited');
CREATE TYPE research_candidate_status AS ENUM ('pending','reviewed','imported','rejected');

CREATE TABLE research_targets (
  politician_id text PRIMARY KEY REFERENCES politicians(id) ON DELETE CASCADE,
  enabled boolean NOT NULL DEFAULT true,
  priority integer NOT NULL DEFAULT 100,
  last_scanned_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE research_runs (
  id bigserial PRIMARY KEY,
  politician_id text NOT NULL REFERENCES politicians(id) ON DELETE CASCADE,
  started_at timestamptz NOT NULL DEFAULT now(),
  finished_at timestamptz,
  status research_run_status NOT NULL DEFAULT 'running',
  model text NOT NULL,
  search_brief text NOT NULL,
  findings_count integer NOT NULL DEFAULT 0,
  error_message text,
  floot_credits numeric,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE research_candidates (
  id bigserial PRIMARY KEY,
  run_id bigint NOT NULL REFERENCES research_runs(id) ON DELETE CASCADE,
  politician_id text NOT NULL REFERENCES politicians(id) ON DELETE CASCADE,
  occurred_at date,
  kind text NOT NULL,
  topic text NOT NULL,
  quote_or_action text NOT NULL,
  context text NOT NULL,
  source_title text NOT NULL,
  source_url text NOT NULL,
  source_publisher text,
  source_grade source_grade NOT NULL,
  relation_hint text,
  fingerprint text NOT NULL UNIQUE,
  status research_candidate_status NOT NULL DEFAULT 'pending',
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX research_targets_scan_idx ON research_targets (enabled, last_scanned_at, priority DESC);
CREATE INDEX research_runs_politician_started_idx ON research_runs (politician_id, started_at DESC);
CREATE INDEX research_candidates_review_idx ON research_candidates (status, politician_id, occurred_at DESC);
