# scripts/make_data_dictionary.py
import pandas as pd, numpy as np
from pathlib import Path
from sqlalchemy import create_engine, text

DB_URL = "sqlite:///da4.db"
engine = create_engine(DB_URL)

# table -> output md path
TABLES = {
    "p1_sales_stage":   Path("P1_retail_sales/reports/data_dictionary.md"),
    "p2_ads_stage":     Path("P2_marketing_funnel/reports/data_dictionary.md"),
    "p3_churn_stage":   Path("P3_subscription_churn/reports/data_dictionary.md"),
    "p4_tickets_stage": Path("P4_operations_support/reports/data_dictionary.md"),
}

def fmt_example(s: pd.Series, k=3):
    vals = s.dropna().unique()[:k]
    return ", ".join(map(lambda x: str(x)[:32], vals)) if len(vals) else ""

def minmax(s: pd.Series):
    try:
        return s.min(), s.max()
    except Exception:
        return None, None

def allowed_values_or_range(s: pd.Series):
    if pd.api.types.is_numeric_dtype(s):
        lo, hi = minmax(s)
        return f"{lo} – {hi}"
    if pd.api.types.is_datetime64_any_dtype(s):
        lo, hi = minmax(s)
        return f"{lo.date() if pd.notna(lo) else lo} – {hi.date() if pd.notna(hi) else hi}"
    # categorical-ish
    nunique = s.nunique(dropna=True)
    if nunique <= 20:
        vals = s.dropna().value_counts().index.tolist()
        return ", ".join(map(lambda x: str(x)[:24], vals))
    # too many: show top 10
    vals = s.dropna().value_counts().head(10).index.tolist()
    return "Top10: " + ", ".join(map(lambda x: str(x)[:24], vals))

def dict_for_table(tbl: str) -> str:
    with engine.begin() as conn:
        df = pd.read_sql(text(f"SELECT * FROM {tbl}"), conn)
    rows = []
    for col in df.columns:
        s = df[col]
        dtype = str(s.dtype)
        null_pct = round(float(s.isna().mean()*100), 2)
        allowed = allowed_values_or_range(s)
        example = fmt_example(s)
        notes = ""
        rows.append((col, dtype, f"{null_pct}%", allowed, example, notes))

    md = []
    md.append(f"# Data Dictionary — {tbl}\n")
    md.append("| Column | Type | Null % | Allowed Values / Range | Example | Notes |")
    md.append("|---|---|---:|---|---|---|")
    for r in rows:
        md.append("| " + " | ".join(map(lambda x: str(x).replace("\n"," "), r)) + " |")
    return "\n".join(md) + "\n"

def main():
    for tbl, outpath in TABLES.items():
        outpath.parent.mkdir(parents=True, exist_ok=True)
        md = dict_for_table(tbl)
        outpath.write_text(md, encoding="utf-8")
        print(f"Wrote {outpath}")

if __name__ == "__main__":
    main()
