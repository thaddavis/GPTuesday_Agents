# Useful commands for analyzing agent performance

- SELECT AVG(timing)::numeric(10,2) FROM agent_timing_stats;
- SELECT MAX(timing)::numeric(10,2) FROM agent_timing_stats;
- SELECT MIN(timing)::numeric(10,2) FROM agent_timing_stats;