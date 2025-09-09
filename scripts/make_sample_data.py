# scripts/make_sample_data.py
import numpy as np, pandas as pd
from pathlib import Path
rng = np.random.default_rng(42)
root = Path(__file__).resolve().parents[1]

# Ensure folders exist
folders = [
    root/"P1_retail_sales/data/raw",
    root/"P2_marketing_funnel/data/raw",
    root/"P3_subscription_churn/data/raw",
    root/"P4_operations_support/data/raw",
]
for f in folders: f.mkdir(parents=True, exist_ok=True)

# ---------- P1: Retail Sales ----------
n = 1200
dates = pd.date_range("2023-01-01", "2024-12-31", freq="D")
segments = ["Consumer","Corporate","Home Office"]
regions = ["West","East","Central","South"]
cats = [("Furniture","Chairs"),("Furniture","Tables"),
        ("Office Supplies","Paper"),("Office Supplies","Binders"),
        ("Technology","Phones"),("Technology","Accessories")]
q = rng.integers(1, 8, size=n)
price = rng.normal(60, 25, size=n).clip(5, 300)
discount = rng.choice([0, 0.1, 0.2, 0.3], size=n, p=[0.65,0.2,0.1,0.05])
gm = rng.uniform(0.2, 0.6, size=n)
cat_idx = rng.integers(0, len(cats), size=n)
order_dates = rng.choice(dates, size=n)
ship_offsets = rng.integers(1, 8, size=n)

p1 = pd.DataFrame({
    "order_id": np.arange(10001, 10001+n),
    "order_date": order_dates,
    "ship_date": order_dates + pd.to_timedelta(ship_offsets, unit="D"),
    "customer_id": rng.integers(5000, 6000, size=n),
    "customer_segment": rng.choice(segments, size=n),
    "region": rng.choice(regions, size=n),
    "product_id": rng.integers(2000, 3000, size=n),
    "category": [cats[i][0] for i in cat_idx],
    "sub_category": [cats[i][1] for i in cat_idx],
    "product_name": [f"SKU-{i}" for i in rng.integers(100,999,size=n)],
    "quantity": q,
    "unit_price": price.round(2),
    "discount": discount.round(2),
})
p1["revenue"] = (p1["quantity"] * p1["unit_price"] * (1 - p1["discount"])).round(2)
p1["gross_margin_pct"] = gm.round(3)
p1["cost"] = (p1["revenue"] * (1 - p1["gross_margin_pct"])).round(2)
p1.to_csv(root/"P1_retail_sales/data/raw/sample_sales.csv", index=False)

# ---------- P2: Marketing Funnel ----------
m = 900
channels = ["Paid Search","Organic Search","Email","Social","Display","Affiliate"]
campaigns = [f"Camp-{i}" for i in range(1, 21)]
days = pd.date_range("2024-01-01", "2024-12-31", freq="D")
imp = rng.integers(1000, 100_000, size=m)
clk = (imp * rng.uniform(0.005, 0.08, size=m)).astype(int)
conv = (clk * rng.uniform(0.01, 0.2, size=m)).astype(int)
cost = (clk * rng.uniform(0.2, 3.0, size=m)).round(2)
rev = (conv * rng.uniform(10, 120, size=m)).round(2)

p2 = pd.DataFrame({
    "date": rng.choice(days, size=m),
    "channel": rng.choice(channels, size=m),
    "campaign": rng.choice(campaigns, size=m),
    "impressions": imp,
    "clicks": clk,
    "conversions": conv,
    "cost": cost,
    "revenue": rev
})
p2.to_csv(root/"P2_marketing_funnel/data/raw/sample_ads.csv", index=False)

# ---------- P3: Subscription Churn ----------
k = 1000

# Make signup a Series so we can use .dt.days safely
signup = pd.Series(
    rng.choice(pd.date_range("2022-01-01", "2024-06-30"), size=k),
    name="signup_date"
)

plans = ["Basic", "Pro", "Premium"]
monthly_fee = {"Basic": 10, "Pro": 25, "Premium": 50}
plan_choice = rng.choice(plans, size=k, p=[0.5, 0.35, 0.15])

# Simple engagement features
sessions_30d = rng.poisson(lam=rng.uniform(1, 30, size=k)).clip(0)
tickets_90d  = rng.poisson(lam=rng.uniform(0, 3,  size=k)).clip(0)

# Tenure (months) as of 2024-12-31, minimum of 1 month
tenure_m = ((pd.Timestamp("2024-12-31") - signup).dt.days // 30).clip(lower=1)

# Risk heuristic to simulate churn probability
risk = (
    (sessions_30d < 3).astype(int)
    + (tickets_90d > 2).astype(int)
    + (np.array([monthly_fee[p] for p in plan_choice]) > 30).astype(int)
)

churned = (rng.random(k) < (0.08 + 0.08 * risk)).astype(int)
last_active = signup + pd.to_timedelta(rng.integers(30, 900, size=k), unit="D")

p3 = pd.DataFrame({
    "customer_id": np.arange(70001, 70001 + k),
    "signup_date": signup.astype("datetime64[ns]"),
    "country": rng.choice(["US","UK","DE","IN","CA","AU"], size=k),
    "plan": plan_choice,
    "monthly_fee": [monthly_fee[p] for p in plan_choice],
    "sessions_last_30d": sessions_30d.astype(int),
    "support_tickets_90d": tickets_90d.astype(int),
    "tenure_months": tenure_m.astype(int),
    "last_active_date": last_active,
    "churned": churned.astype(int),
})

p3.to_csv(root / "P3_subscription_churn/data/raw/sample_churn.csv", index=False)

# ---------- P4: Operations / Support ----------
t = 1100
opened = pd.to_datetime(rng.choice(pd.date_range("2024-03-01","2024-12-31"), size=t))
sla = rng.choice([8, 24, 48, 72], size=t, p=[0.3,0.4,0.2,0.1])
priority = rng.choice(["Low","Medium","High","Urgent"], size=t, p=[0.35,0.4,0.2,0.05])
queues = ["Billing","Tech","Orders","Returns","General"]
resp_hrs = (rng.gamma(shape=2.0, scale=2.5, size=t)).round(1)
resolve_hrs = (rng.gamma(shape=3.0, scale=6.0, size=t)).round(1)
closed = opened + pd.to_timedelta(resolve_hrs, unit="h")

p4 = pd.DataFrame({
    "ticket_id": np.arange(500001, 500001+t),
    "opened_at": opened,
    "first_response_at": opened + pd.to_timedelta(resp_hrs, unit="h"),
    "closed_at": closed,
    "priority": priority,
    "queue": rng.choice(queues, size=t),
    "agent_id": rng.integers(100, 160, size=t),
    "sla_target_hours": sla,
    "customer_type": rng.choice(["New","Returning","VIP"], size=t, p=[0.5,0.4,0.1]),
    "csat_score": rng.choice([1,2,3,4,5,np.nan], size=t, p=[0.05,0.1,0.2,0.35,0.25,0.05]),
    "resolved": (resolve_hrs <= sla).astype(int)
})
p4.to_csv(root/"P4_operations_support/data/raw/sample_tickets.csv", index=False)

print("Done. Created 4 CSVs under each project's data/raw/")
