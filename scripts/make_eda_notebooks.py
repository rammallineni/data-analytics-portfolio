# scripts/make_eda_notebooks.py
from pathlib import Path
import nbformat as nbf

ROOT = Path(__file__).resolve().parents[1]

def nb(cells):
    nb = nbf.v4.new_notebook()
    nb.cells = [nbf.v4.new_markdown_cell(c) if isinstance(c, str) and c.startswith("#")
                else nbf.v4.new_code_cell(c) for c in cells]
    return nb

def write_nb(path, cells):
    path.parent.mkdir(parents=True, exist_ok=True)
    nbf.write(nb(cells), path, version=4)
    print(f"Wrote {path}")

# ---------- P1: Retail ----------
p1_cells = [
"# P1 — Retail Sales Analytics : 01_eda",
"""import pandas as pd, numpy as np
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt

DB = 'sqlite:///../../da4.db'
TABLE = 'p1_sales_stage'

engine = create_engine(DB)
with engine.begin() as conn:
    df = pd.read_sql(text(f'SELECT * FROM {TABLE}'), conn)

print('Shape:', df.shape)
display(df.head())
display(df.describe(numeric_only=True).T)
print('\\nNull % (top):')
print((df.isna().mean()*100).sort_values(ascending=False).head(15))
""",
"""# --- Basic checks
df['order_date'] = pd.to_datetime(df['order_date'])
print('Date range:', df['order_date'].min(), '→', df['order_date'].max())
print('Duplicated order_id rows:', df.duplicated(['order_id','product_id']).sum())
""",
"""# --- Monthly revenue
mrev = (df.assign(ym=df['order_date'].dt.to_period('M').astype(str))
          .groupby('ym', as_index=False)['revenue'].sum().sort_values('ym'))
plt.figure(); plt.plot(mrev['ym'], mrev['revenue'])
plt.xticks(rotation=90); plt.title('Monthly Revenue'); plt.tight_layout(); plt.show()""",
"""# --- Top sub-categories by gross profit
top_sub = (df.groupby(['category','sub_category'], as_index=False)['gross_profit']
             .sum().sort_values('gross_profit', ascending=False).head(10))
plt.figure(); plt.bar(top_sub['sub_category'], top_sub['gross_profit'])
plt.xticks(rotation=45, ha='right'); plt.title('Top Sub-categories by Gross Profit')
plt.tight_layout(); plt.show()
top_sub""",
"""# --- Region x Segment revenue pivot
pv = df.pivot_table(values='revenue', index='region', columns='customer_segment', aggfunc='sum', fill_value=0)
pv
"""
]

# ---------- P2: Marketing ----------
p2_cells = [
"# P2 — Marketing Funnel & A/B : 01_eda",
"""import pandas as pd, numpy as np
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt

DB = 'sqlite:///../../da4.db'
TABLE = 'p2_ads_stage'

engine = create_engine(DB)
with engine.begin() as conn:
    df = pd.read_sql(text(f'SELECT * FROM {TABLE}'), conn)

print('Shape:', df.shape)
display(df.head())
display(df.describe(numeric_only=True).T)
print('\\nNull % (top):')
print((df.isna().mean()*100).sort_values(ascending=False).head(15))
""",
"""# --- Channel performance table
agg = (df.groupby('channel', as_index=False)
         .agg(imp=('impressions','sum'), clk=('clicks','sum'), cnv=('conversions','sum'),
              cost=('cost','sum'), rev=('revenue','sum')))
agg['ctr']  = agg['clk'] / agg['imp'].replace(0, pd.NA)
agg['cvr']  = agg['cnv'] / agg['clk'].replace(0, pd.NA)
agg['cac']  = agg['cost'] / agg['cnv'].replace(0, pd.NA)
agg['roas'] = agg['rev']  / agg['cost'].replace(0, pd.NA)
agg.sort_values('roas', ascending=False, inplace=True)
agg
""",
"""# --- ROAS by channel (bar)
plt.figure(); plt.bar(agg['channel'], agg['roas'])
plt.xticks(rotation=45, ha='right'); plt.title('ROAS by Channel')
plt.tight_layout(); plt.show()
""",
"""# --- Monthly ROAS trend
df['ym'] = pd.to_datetime(df['date']).dt.to_period('M').astype(str)
m = (df.groupby('ym', as_index=False)
       .agg(cost=('cost','sum'), rev=('revenue','sum'))
       .sort_values('ym'))
m['roas'] = m['rev'] / m['cost'].replace(0, pd.NA)
plt.figure(); plt.plot(m['ym'], m['roas'])
plt.xticks(rotation=90); plt.title('Monthly ROAS'); plt.tight_layout(); plt.show()
m
"""
]

# ---------- P3: Churn ----------
p3_cells = [
"# P3 — Subscription Churn & Retention : 01_eda",
"""import pandas as pd, numpy as np
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt

DB = 'sqlite:///../../da4.db'
TABLE = 'p3_churn_stage'

engine = create_engine(DB)
with engine.begin() as conn:
    df = pd.read_sql(text(f'SELECT * FROM {TABLE}'), conn)

print('Shape:', df.shape)
display(df.head())
display(df.describe(numeric_only=True).T)
print('\\nNull % (top):')
print((df.isna().mean()*100).sort_values(ascending=False).head(15))
""",
"""# --- Churn rate overall & by plan/tenure
overall = df['churned'].mean()
print('Overall churn %:', round(overall*100,2))
by_plan = df.groupby('plan', as_index=False)['churned'].mean()
by_ten  = df.groupby('tenure_bucket', as_index=False)['churned'].mean().sort_values('tenure_bucket')
plt.figure(); plt.bar(by_plan['plan'], by_plan['churned']*100)
plt.title('Churn % by Plan'); plt.tight_layout(); plt.show()
plt.figure(); plt.bar(by_ten['tenure_bucket'], by_ten['churned']*100)
plt.title('Churn % by Tenure Bucket'); plt.tight_layout(); plt.show()
by_plan, by_ten
""",
"""# --- Simple cohort retention proxy (share not churned by cohort)
coh = (df.groupby('cohort_month', as_index=False)
         .agg(active=('churned', lambda s: (1 - s).sum()),
              size=('churned','size')))
coh['retention_pct'] = coh['active'] / coh['size'] * 100
coh.sort_values('cohort_month', inplace=True)
plt.figure(); plt.plot(coh['cohort_month'], coh['retention_pct'])
plt.xticks(rotation=90); plt.title('Retention % by Signup Cohort'); plt.tight_layout(); plt.show()
coh
""",
"""# --- At-risk breakdown
risk = df.groupby(['plan','country'], as_index=False)['at_risk'].mean().sort_values('at_risk', ascending=False).head(10)
risk
"""
]

# ---------- P4: Operations ----------
p4_cells = [
"# P4 — Operations / Support Analytics : 01_eda",
"""import pandas as pd, numpy as np
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt

DB = 'sqlite:///../../da4.db'
TABLE = 'p4_tickets_stage'

engine = create_engine(DB)
with engine.begin() as conn:
    df = pd.read_sql(text(f'SELECT * FROM {TABLE}'), conn)

print('Shape:', df.shape)
display(df.head())
display(df.describe(numeric_only=True).T)
print('\\nNull % (top):')
print((df.isna().mean()*100).sort_values(ascending=False).head(15))
""",
"""# --- Distributions: first response & resolution hours
plt.figure(); df['first_response_hours'].dropna().plot(kind='hist', bins=30)
plt.title('First Response Hours'); plt.tight_layout(); plt.show()
plt.figure(); df['resolution_hours'].dropna().plot(kind='hist', bins=30)
plt.title('Resolution Hours'); plt.tight_layout(); plt.show()
""",
"""# --- SLA by queue/priority
sla = (df.groupby(['queue','priority'], as_index=False)['within_sla'].mean()
         .rename(columns={'within_sla':'sla_met_pct'}))
sla['sla_met_pct'] *= 100
sla.sort_values(['queue','priority'], inplace=True)
sla
""",
"""# --- Agent/queue table (top 10 slowest by resolution)
slow = (df.groupby(['agent_id','queue'], as_index=False)['resolution_hours']
          .mean().sort_values('resolution_hours', ascending=False).head(10))
slow
"""
]

write_nb(ROOT/"P1_retail_sales/notebooks/01_eda.ipynb", p1_cells)
write_nb(ROOT/"P2_marketing_funnel/notebooks/01_eda.ipynb", p2_cells)
write_nb(ROOT/"P3_subscription_churn/notebooks/01_eda.ipynb", p3_cells)
write_nb(ROOT/"P4_operations_support/notebooks/01_eda.ipynb", p4_cells)
