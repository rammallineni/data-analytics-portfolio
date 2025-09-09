# data-analytics-portfolio

## Quickstart

```bash
# 1) Create & activate venv
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate

# 2) Install deps
pip install -r env/requirements.txt

# 3) Generate sample data
python scripts/make_sample_data.py

# 4) Load raw CSVs into SQLite
python shared/utils/load_to_db.py sqlite:///da4.db P1_retail_sales/data/raw/sample_sales.csv p1_sales_raw
python shared/utils/load_to_db.py sqlite:///da4.db P2_marketing_funnel/data/raw/sample_ads.csv p2_ads_raw
python shared/utils/load_to_db.py sqlite:///da4.db P3_subscription_churn/data/raw/sample_churn.csv p3_churn_raw
python shared/utils/load_to_db.py sqlite:///da4.db P4_operations_support/data/raw/sample_tickets.csv p4_tickets_raw

# 5) Build staging tables
python scripts/run_sql.py sqlite:///da4.db

# 6) Open any EDA notebook
jupyter lab P1_retail_sales/notebooks/01_eda.ipynb
```
