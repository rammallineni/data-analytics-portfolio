# Wireframe — P4 Operations / Support Analytics

## Layout

1. **KPI strip (top)**
   - SLA Met % | Avg First Response (hrs) | Avg Resolution (hrs) | CSAT
2. **Row 1**
   - (Left) Heatmap: SLA Met % by Queue × Priority
   - (Right) Histogram: Resolution Hours (bucketed)
3. **Row 2**
   - (Left) Bar: First Response Hours by Priority
   - (Right) Table: Agent/Queue Performance (First Resp, Resolution, SLA %, CSAT)

## Filters

Date range | Queue | Priority | Agent | Customer type

## Must-answer questions

- Where are SLA breaches concentrated?
- Are Urgent/High handled appropriately?
- Which teams/agents need support?

## Notes

- Exclude NULL CSAT from averages; show count alongside average.
