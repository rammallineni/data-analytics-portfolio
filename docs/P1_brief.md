# P1 — Retail Sales Analytics

## Problem Statement

Sales leadership needs clear visibility into which categories, regions, and customer segments drive revenue and gross profit so they can tune discounts, promotions, and inventory.

## Stakeholder

Head of Sales & Merchandising

## Data

Source: `P1_retail_sales/data/raw/sample_sales.csv`  
Key columns: `order_id, order_date, ship_date, customer_id, customer_segment, region, product_id, category, sub_category, product_name, quantity, unit_price, discount, revenue, gross_margin_pct`.

## KPIs (with exact formulas)

- **Total Revenue** = `SUM(revenue)`
- **Gross Profit (GP)** = `SUM(revenue * gross_margin_pct)`
- **Gross Margin % (GM%)** = `SUM(revenue * gross_margin_pct) / NULLIF(SUM(revenue),0)`
- **Average Order Value (AOV)** = `SUM(revenue) / COUNT(DISTINCT order_id)`
- **Units per Order** = `SUM(quantity) / COUNT(DISTINCT order_id)`
- **YoY Growth (Revenue)** = `(Rev_this_year - Rev_last_year) / NULLIF(Rev_last_year,0)`

## Key Business Questions

1. What categories/sub-categories lead in **revenue** and **gross profit**?
2. How does performance shift by **month** and **weekday** (seasonality)?
3. Which **regions** and **segments** over/underperform (rev, GM%)?
4. What is the impact of **discount bands** on AOV and GM%?
5. Who are the **top products** by profit and is there a long tail?

## Methods / SQL Outline

- Derive calendar fields (month, weekday); group-bys and ranking.
- Compare **discount bands** (e.g., 0, 0–10%, 10–20%, 20%+).  
  **Example: Top 20 products by gross profit**

```sql
SELECT product_id, product_name,
       SUM(revenue * gross_margin_pct) AS gross_profit
FROM p1_sales_raw
GROUP BY 1,2
ORDER BY gross_profit DESC
LIMIT 20;
```
