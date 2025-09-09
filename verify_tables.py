from sqlalchemy import create_engine, text
import pandas as pd

e = create_engine("sqlite:///da4.db")
tables = {
    "p1_sales_raw": ["order_id","order_date","revenue","gross_margin_pct"],
    "p2_ads_raw":   ["date","channel","impressions","clicks","conversions"],
    "p3_churn_raw": ["customer_id","signup_date","tenure_months","churned"],
    "p4_tickets_raw":["ticket_id","opened_at","priority","resolved"]
}

with e.begin() as conn:
    for t, cols in tables.items():
        n = conn.execute(text(f"SELECT COUNT(*) FROM {t}")).scalar_one()
        print(f"{t}: {n:,} rows")
        preview = pd.read_sql(text(f"SELECT {', '.join(cols)} FROM {t} LIMIT 5"), conn)
        print(preview.to_string(index=False))
        print("-"*60)
