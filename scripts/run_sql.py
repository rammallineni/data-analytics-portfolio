# Run all staging SQL files
import sys, pathlib
from sqlalchemy import create_engine, text

def run_sql(engine, sql_path):
    sql = sql_path.read_text(encoding="utf-8")
    with engine.begin() as conn:
        for stmt in sql.split(";"):
            if stmt.strip():
                conn.execute(text(stmt))
    print(f"OK: {sql_path}")

if __name__ == "__main__":
    db_url = sys.argv[1] if len(sys.argv) > 1 else "sqlite:///da4.db"
    root = pathlib.Path(__file__).resolve().parents[1]
    files = [
        root / "P1_retail_sales/sql/01_sales_stage.sql",
        root / "P2_marketing_funnel/sql/01_ads_stage.sql",
        root / "P3_subscription_churn/sql/01_churn_stage.sql",
        root / "P4_operations_support/sql/01_tickets_stage.sql",
    ]
    engine = create_engine(db_url)
    for f in files:
        run_sql(engine, f)
    print("All staging tables built.")
# Usage: python scripts/run_sql.py "sqlite:///da4.db"