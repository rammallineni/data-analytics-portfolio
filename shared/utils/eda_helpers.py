import pandas as pd

def quick_profile(df: pd.DataFrame, top_n=10):
    print("Shape:", df.shape)
    print("\nDtypes:\n", df.dtypes)
    print("\nMissing % (top):\n", df.isna().mean().sort_values(ascending=False).head(top_n))
    num = df.select_dtypes("number")
    if not num.empty:
        print("\nNumeric describe:\n", num.describe().T)
    return df

def top_values(df: pd.DataFrame, col: str, n=10):
    return df[col].value_counts(dropna=False).head(n).to_frame("count")
