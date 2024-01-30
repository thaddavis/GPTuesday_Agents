# TLDR - Setting up render.com db

- 1) Set up the `agent_timing_stats` table to track the performance of the agent

## STEPS for configuring render.com db regarding step 2 describe above

- 1) Configure .env with PostgreSQL env vars for connecting to render.com db instance
- 2) If schema update is needed then drop tables in the render.com db so connect to the render.com db
    - source .env
    - `PGPASSWORD=$PG_PASSWORD psql -h $PG_HOST -U $PG_USER $PG_DB` Worked! 🎉
- 3) SETUP UP TABLES FOR `agent_timing_stats`
    - `PGPASSWORD=$PG_PASSWORD psql -h $PG_HOST -U $PG_USER $PG_DB < ./reference_sql/agent_stats_schema.sql` Worked! 🎉

## STEPS for updating `agent_timing_stats` table column names

```.sql
ALTER TABLE agent_timing_stats RENAME COLUMN tool to agent_version;
```