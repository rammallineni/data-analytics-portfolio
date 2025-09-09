DROP TABLE IF EXISTS p2_ads_stage;
CREATE TABLE p2_ads_stage AS
SELECT
  date(date) AS date,
  lower(trim(channel))  AS channel,
  lower(trim(campaign)) AS campaign,
  CAST(impressions AS INTEGER) AS impressions,
  CAST(clicks AS INTEGER)      AS clicks,
  CAST(conversions AS INTEGER) AS conversions,
  CAST(cost AS REAL)           AS cost,
  CAST(revenue AS REAL)        AS revenue,
  CAST(clicks AS FLOAT)      / NULLIF(impressions,0) AS ctr,
  CAST(conversions AS FLOAT) / NULLIF(clicks,0)      AS cvr,
  CAST(cost AS FLOAT)        / NULLIF(clicks,0)      AS cpc,
  CAST(cost AS FLOAT)        / NULLIF(conversions,0) AS cac,
  CAST(revenue AS FLOAT)     / NULLIF(cost,0)        AS roas,
  strftime('%Y-%m', date(date)) AS ym
FROM p2_ads_raw;

CREATE INDEX IF NOT EXISTS idx_p2_ads_stage_date     ON p2_ads_stage(date);
CREATE INDEX IF NOT EXISTS idx_p2_ads_stage_channel  ON p2_ads_stage(channel);
CREATE INDEX IF NOT EXISTS idx_p2_ads_stage_campaign ON p2_ads_stage(campaign);
