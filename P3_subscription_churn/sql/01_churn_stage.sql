DROP TABLE IF EXISTS p3_churn_stage;
CREATE TABLE p3_churn_stage AS
SELECT
  CAST(customer_id AS INTEGER) AS customer_id,
  date(signup_date) AS signup_date,
  strftime('%Y-%m', date(signup_date)) AS cohort_month,
  upper(country) AS country,
  lower(trim(plan)) AS plan,
  CAST(monthly_fee AS REAL) AS monthly_fee,
  CAST(sessions_last_30d AS INTEGER) AS sessions_last_30d,
  CAST(support_tickets_90d AS INTEGER) AS support_tickets_90d,
  CAST(tenure_months AS INTEGER) AS tenure_months,
  date(last_active_date) AS last_active_date,
  CAST(churned AS INTEGER) AS churned,
  CASE WHEN sessions_last_30d < 3 OR support_tickets_90d > 2 THEN 1 ELSE 0 END AS at_risk,
  CASE 
    WHEN tenure_months < 3  THEN '0-2m'
    WHEN tenure_months < 6  THEN '3-5m'
    WHEN tenure_months < 12 THEN '6-11m'
    ELSE '12m+'
  END AS tenure_bucket
FROM p3_churn_raw;

CREATE INDEX IF NOT EXISTS idx_p3_churn_stage_cohort  ON p3_churn_stage(cohort_month);
CREATE INDEX IF NOT EXISTS idx_p3_churn_stage_plan    ON p3_churn_stage(plan);
CREATE INDEX IF NOT EXISTS idx_p3_churn_stage_churned ON p3_churn_stage(churned);
