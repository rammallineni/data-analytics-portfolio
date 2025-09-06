from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine("sqlite:///da4.db")
with engine.begin() as conn:
    conn.execute(text("CREATE TABLE IF NOT EXISTS healthcheck (id INTEGER PRIMARY KEY, note TEXT)"))
    conn.execute(text("INSERT INTO healthcheck (note) VALUES ('ok')"))
    rows = conn.execute(text("SELECT COUNT(*) FROM healthcheck")).scalar_one()
    tables = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table'")).fetchall()

print("Smoke OK — rows in healthcheck:", rows)
print("Tables:", [t[0] for t in tables])
