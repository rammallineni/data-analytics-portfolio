# Wireframe — P3 Subscription Churn & Retention

## Layout

1. **KPI strip (top)**
   - Monthly Churn % | ARPU | At-Risk %
2. **Row 1**
   - (Left) Line: Retention % by Signup Cohort (cohort-month on x-axis)
   - (Right) Bar/Heat: Churn % by Plan × Tenure Bucket
3. **Row 2**
   - (Left) Bar: At-Risk % by Plan (top 5 countries stacked)
   - (Right) Table: Customer segments (Plan, Country, Tenure, At-Risk, Churned)

## Filters

Cohort month | Plan | Country | Tenure bucket

## Must-answer questions

- Which cohorts retain best?
- Which plans/tenure buckets churn more?
- Where is at-risk concentration for outreach?

## Notes

- Define at_risk = sessions_last_30d < 3 OR tickets_90d > 2.
