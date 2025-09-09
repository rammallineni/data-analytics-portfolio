# Data Dictionary — p3_churn_stage

| Column | Type | Null % | Allowed Values / Range | Example | Notes |
|---|---|---:|---|---|---|
| customer_id | int64 | 0.0% | 70001 – 71000 | 70001, 70002, 70003 |  |
| signup_date | object | 0.0% | Top10: 2023-08-12, 2022-08-08, 2023-11-30, 2024-03-13, 2022-10-31, 2023-07-14, 2022-05-12, 2022-02-11, 2023-07-20, 2022-11-09 | 2023-09-26, 2023-01-05, 2022-08-16 |  |
| cohort_month | object | 0.0% | Top10: 2023-08, 2024-03, 2023-07, 2023-12, 2023-01, 2024-02, 2022-10, 2024-06, 2024-04, 2022-08 | 2023-09, 2023-01, 2022-08 |  |
| country | object | 0.0% | UK, CA, DE, AU, IN, US | CA, US, UK |  |
| plan | object | 0.0% | basic, pro, premium | basic, pro, premium |  |
| monthly_fee | float64 | 0.0% | 10.0 – 50.0 | 10.0, 25.0, 50.0 |  |
| sessions_last_30d | int64 | 0.0% | 0 – 44 | 6, 14, 12 |  |
| support_tickets_90d | int64 | 0.0% | 0 – 9 | 0, 2, 6 |  |
| tenure_months | int64 | 0.0% | 6 – 36 | 15, 24, 28 |  |
| last_active_date | object | 0.0% | Top10: 2023-12-24, 2024-04-06, 2024-03-01, 2025-06-09, 2024-05-20, 2024-08-02, 2024-06-25, 2025-02-14, 2022-11-08, 2024-03-04 | 2023-12-15, 2025-01-13, 2022-10-19 |  |
| churned | int64 | 0.0% | 0 – 1 | 0, 1 |  |
| at_risk | int64 | 0.0% | 0 – 1 | 0, 1 |  |
| tenure_bucket | object | 0.0% | 12m+, 6-11m | 12m+, 6-11m |  |
