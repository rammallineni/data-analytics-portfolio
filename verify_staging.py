from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine("sqlite:///da4.db")
tables = {
    "p1_sales_stage":  ["order_id","order_date","gross_profit"],
    "p2_ads_stage":    ["date","channel","roas"],
    "p3_churn_stage":  ["customer_id","cohort_month","tenure_bucket","churned"],
    "p4_tickets_stage":["ticket_id","priority","queue","within_sla"]
}

with engine.begin() as conn:
    for t, cols in tables.items():
        n = conn.execute(text(f"SELECT COUNT(*) FROM {t}")).scalar_one()
        print(f"{t}: {n} rows")
        df = pd.read_sql(text(f"SELECT {', '.join(cols)} FROM {t} LIMIT 5"), conn)
        print(df.to_string(index=False))
        print("-"*60)
