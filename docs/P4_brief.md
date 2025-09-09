docs/P4_brief.md

````md
# P4 — Operations / Support Analytics

## Problem Statement

Support Ops needs to improve SLA compliance and customer experience by reducing time to first response and time to resolution.

## Stakeholder

Support Operations Manager

## Data

Source: `P4_operations_support/data/raw/sample_tickets.csv`  
Key columns: `ticket_id, opened_at, first_response_at, closed_at, priority, queue, agent_id, sla_target_hours, customer_type, csat_score, resolved`.

## KPIs (with exact formulas)

- **SLA Met %** = `AVG(resolved)` (1 if resolved within SLA, else 0)
- **Avg First Response (hrs)** = `AVG((julianday(first_response_at)-julianday(opened_at))*24)`
- **Avg Resolution (hrs)** = `AVG((julianday(closed_at)-julianday(opened_at))*24)`
- **Backlog (proxy)** = `COUNT(*) WHERE resolved = 0`
- **CSAT Average** = `AVG(csat_score)` excluding NULLs

## Key Business Questions

1. Which **queues** and **priorities** breach SLA most?
2. Are **Urgent/High** tickets getting faster first response but slower overall resolution?
3. Which **agents/teams** need support or training?
4. How does **CSAT** vary with response/resolution times?

## Methods / SQL Outline

- Derive response and resolution hours using `julianday` deltas (SQLite).  
  **Example: SLA & timing by queue × priority**

```sql
SELECT queue, priority,
       AVG(resolved)*100 AS sla_met_pct,
       AVG((julianday(first_response_at)-julianday(opened_at))*24) AS first_resp_hrs,
       AVG((julianday(closed_at)-julianday(opened_at))*24) AS resolve_hrs
FROM p4_tickets_raw
GROUP BY queue, priority
ORDER BY sla_met_pct ASC;
```
````
