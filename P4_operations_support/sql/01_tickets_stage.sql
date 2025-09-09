DROP TABLE IF EXISTS p4_tickets_stage;
CREATE TABLE p4_tickets_stage AS
SELECT
  CAST(ticket_id AS INTEGER) AS ticket_id,
  datetime(opened_at) AS opened_at,
  datetime(first_response_at) AS first_response_at,
  datetime(closed_at) AS closed_at,
  lower(trim(priority)) AS priority,
  lower(trim(queue))    AS queue,
  CAST(agent_id AS INTEGER) AS agent_id,
  CAST(sla_target_hours AS INTEGER) AS sla_target_hours,
  lower(trim(customer_type)) AS customer_type,
  CAST(csat_score AS REAL) AS csat_score,
  CAST(resolved AS INTEGER) AS resolved,
  (julianday(first_response_at) - julianday(opened_at)) * 24.0 AS first_response_hours,
  (julianday(closed_at)        - julianday(opened_at)) * 24.0 AS resolution_hours,
  CASE 
    WHEN ((julianday(closed_at) - julianday(opened_at)) * 24.0) <= sla_target_hours
    THEN 1 ELSE 0 END AS within_sla
FROM p4_tickets_raw;

CREATE INDEX IF NOT EXISTS idx_p4_tickets_stage_opened   ON p4_tickets_stage(opened_at);
CREATE INDEX IF NOT EXISTS idx_p4_tickets_stage_priority ON p4_tickets_stage(priority);
CREATE INDEX IF NOT EXISTS idx_p4_tickets_stage_queue    ON p4_tickets_stage(queue);
