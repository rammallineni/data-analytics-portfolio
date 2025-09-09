DROP TABLE IF EXISTS p1_sales_stage;
CREATE TABLE p1_sales_stage AS
SELECT
  CAST(order_id AS INTEGER) AS order_id,
  date(order_date) AS order_date,
  date(ship_date) AS ship_date,
  CAST(customer_id AS INTEGER) AS customer_id,
  lower(trim(customer_segment)) AS customer_segment,
  lower(trim(region)) AS region,
  CAST(product_id AS INTEGER) AS product_id,
  lower(trim(category)) AS category,
  lower(trim(sub_category)) AS sub_category,
  product_name,
  CAST(quantity AS INTEGER) AS quantity,
  CAST(unit_price AS REAL) AS unit_price,
  CAST(discount AS REAL) AS discount,
  CAST(revenue AS REAL) AS revenue,
  CAST(gross_margin_pct AS REAL) AS gross_margin_pct,
  round(revenue * gross_margin_pct, 2) AS gross_profit,
  CASE
    WHEN discount = 0 THEN '0%'
    WHEN discount < 0.10 THEN '0-10%'
    WHEN discount < 0.20 THEN '10-20%'
    ELSE '20%+'
  END AS discount_band
FROM p1_sales_raw;

CREATE INDEX IF NOT EXISTS idx_p1_sales_stage_order_date ON p1_sales_stage(order_date);
CREATE INDEX IF NOT EXISTS idx_p1_sales_stage_category   ON p1_sales_stage(category);
CREATE INDEX IF NOT EXISTS idx_p1_sales_stage_region     ON p1_sales_stage(region);
