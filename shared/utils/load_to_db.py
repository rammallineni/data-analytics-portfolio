import sys, pathlib, pandas as pd
from sqlalchemy import create_engine, text

def main():
    if len(sys.argv) < 4:
        print("Usage: python load_to_db.py <DB_URL> <CSV_PATH> <TABLE_NAME>")
        print("Example: python load_to_db.py sqlite:///da4.db P1_retail_sales/data/raw/sales.csv p1_sales_raw")
        sys.exit(1)

    db_url, csv_path, table = sys.argv[1], pathlib.Path(sys.argv[2]), sys.argv[3]
    if not csv_path.exists():
        raise FileNotFoundError(csv_path)

    # Load CSV
    df = pd.read_csv(csv_path)
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Write to DB
    engine = create_engine(db_url)
    with engine.begin() as conn:
        df.to_sql(table, conn, if_exists="replace", index=False)
        try:
            conn.execute(text("ANALYZE"))  # no-op on SQLite, fine elsewhere
        except Exception:
            pass
    print(f"Loaded {len(df):,} rows into {table}")

if __name__ == "__main__":
    main()
