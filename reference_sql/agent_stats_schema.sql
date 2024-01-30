CREATE TABLE IF NOT EXISTS agent_timing_stats (
   id serial PRIMARY KEY,
   call_id VARCHAR(100) UNIQUE NOT NULL,
   agent_version VARCHAR(100) NOT NULL,
   timing FLOAT,
   created_at TIMESTAMP,
   agent_log JSON NULL
);