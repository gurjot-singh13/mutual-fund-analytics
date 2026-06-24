import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Parse date
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(
    by=["amfi_code", "date"]
)

# Remove duplicates
before = len(df)

df = df.drop_duplicates()

after = len(df)

print(f"Duplicates Removed: {before-after}")

# Forward fill NAV by fund
df["nav"] = (
    df.groupby("amfi_code")["nav"]
    .ffill()
)

# Validate NAV > 0
invalid_nav = (df["nav"] <= 0).sum()

print("Invalid NAV Records:", invalid_nav)

df.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("Saved Successfully")