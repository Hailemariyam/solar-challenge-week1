# dashboard/app/utils.py

import pandas as pd

def load_data():
    countries = ["benin", "sierraleone", "togo"]
    data = {}
    for country in countries:
        df = pd.read_csv(f"dashboard/data/{country}_clean.csv")
        df["Country"] = country.capitalize()

        # Add synthetic Region column so top_regions() works
        df["Region"] = f"{country.capitalize()} Main Station"

        data[country] = df
    return data

def get_summary_table(df):
    return df[["GHI", "DNI", "DHI"]].describe().T[["mean", "std", "min", "max"]]

def top_regions(df, metric="GHI", n=5):
    if "Region" in df.columns:
        return df.groupby("Region")[metric].mean().sort_values(ascending=False).head(n).reset_index()
    else:
        return pd.DataFrame({"Region": [], metric: []})
