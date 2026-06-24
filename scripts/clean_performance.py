import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Return columns
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct"
]

# Check numeric conversion
for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\nMissing values after numeric validation:")
print(df[return_cols].isnull().sum())

# Expense ratio validation
expense_issues = df[
    (df["expense_ratio_pct"] < 0.1)
    | (df["expense_ratio_pct"] > 2.5)
]

print("\nFunds with invalid expense ratio:")
print(len(expense_issues))

# Negative AUM check
invalid_aum = (df["aum_crore"] <= 0).sum()

print("\nInvalid AUM Records:", invalid_aum)

# Save cleaned data
df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("\nSaved Successfully")