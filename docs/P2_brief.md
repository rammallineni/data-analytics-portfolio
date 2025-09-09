docs/P2_brief.md

````md
# P2 — Marketing Funnel & A/B Performance

## Problem Statement

Marketing needs to optimize channel mix and campaign spend by measuring funnel efficiency and return on ad spend.

## Stakeholder

Performance Marketing Lead

## Data

Source: `P2_marketing_funnel/data/raw/sample_ads.csv`  
Key columns: `date, channel, campaign, impressions, clicks, conversions, cost, revenue`.

## KPIs (with exact formulas)

- **CTR** = `SUM(clicks) / NULLIF(SUM(impressions),0)`
- **CVR** = `SUM(conversions) / NULLIF(SUM(clicks),0)`
- **CPC** = `SUM(cost) / NULLIF(SUM(clicks),0)`
- **CAC / CPA** = `SUM(cost) / NULLIF(SUM(conversions),0)`
- **ROAS** = `SUM(revenue) / NULLIF(SUM(cost),0)`
- **Net Revenue** = `SUM(revenue) - SUM(cost)`

## Key Business Questions

1. Which **channels** deliver best **ROAS** and **CAC** overall and by month?
2. Which **campaigns** should we **scale** or **pause**?
3. How do **CTR** and **CVR** vary across channels and seasonally?
4. What’s the **Pareto** contribution (e.g., top 20% campaigns driving 80% revenue)?

## Methods / SQL Outline

- Aggregate by channel, campaign, and `strftime('%Y-%m', date)`.
- Optional A/B partition (suffixes like `-A`/`-B` on campaign names).  
  **Example: Channel leaderboard**

```sql
SELECT channel,
       SUM(impressions) AS imp,
       SUM(clicks) AS clk,
       SUM(conversions) AS cnv,
       SUM(cost) AS cost,
       SUM(revenue) AS rev,
       SUM(clicks)*1.0/NULLIF(SUM(impressions),0) AS ctr,
       SUM(conversions)*1.0/NULLIF(SUM(clicks),0) AS cvr,
       SUM(cost)*1.0/NULLIF(SUM(conversions),0) AS cac,
       SUM(revenue)*1.0/NULLIF(SUM(cost),0) AS roas
FROM p2_ads_raw
GROUP BY channel
ORDER BY roas DESC;
```
````
