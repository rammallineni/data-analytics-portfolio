docs/P3_brief.md

````md
# P3 — Subscription Churn & Retention

## Problem Statement

Customer Success needs to understand drivers of churn and identify at-risk segments to prioritize retention actions.

## Stakeholder

Head of Customer Success / Growth

## Data

Source: `P3_subscription_churn/data/raw/sample_churn.csv`  
Key columns: `customer_id, signup_date, country, plan, monthly_fee, sessions_last_30d, support_tickets_90d, tenure_months, last_active_date, churned`.

## KPIs (with exact formulas)

- **Monthly Churn %** = `churned_customers_in_month / customers_active_at_start_of_month`
- **Retention (n-month)** = `active_after_n_months / cohort_size`
- **ARPU** = `SUM(monthly_fee for active users) / COUNT(active users)`
- **At-Risk %** = `COUNT(at_risk=1) / COUNT(*)` where `at_risk = (sessions_last_30d < 3 OR support_tickets_90d > 2)`

## Key Business Questions

1. Which **features** (sessions, tickets, plan, tenure) are most associated with **churn**?
2. Which **signup cohorts** (month/plan/country) retain best?
3. What is **expected LTV** by plan?
4. Which **at-risk** segments should receive proactive outreach?

## Methods / SQL + ML Outline

- Cohort table by `strftime('%Y-%m', signup_date)`; survival/retention curves.
- Baseline **logistic regression** (or rules) to rank churn drivers.  
  **Example: at-risk flag**

```sql
SELECT *,
       CASE WHEN sessions_last_30d < 3 OR support_tickets_90d > 2
            THEN 1 ELSE 0 END AS at_risk
FROM p3_churn_raw;
```
````
