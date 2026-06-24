import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

print("Database Created")

# -------------------------
# Load Dimension Table
# -------------------------

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

dim_fund = fund_master[
    [
        "amfi_code",
        "fund_house",
        "scheme_name",
        "category",
        "sub_category",
        "plan",
        "benchmark",
        "expense_ratio_pct",
        "risk_category"
    ]
]

dim_fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("dim_fund loaded")

# -------------------------
# FACT NAV
# -------------------------

nav = pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("fact_nav loaded")

# -------------------------
# FACT TRANSACTIONS
# -------------------------

transactions = pd.read_csv(
    "data/processed/08_investor_transactions_clean.csv"
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("fact_transactions loaded")

# -------------------------
# FACT PERFORMANCE
# -------------------------

performance = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("fact_performance loaded")

# -------------------------
# FACT AUM
# -------------------------

aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("fact_aum loaded")

print("\nDatabase Loading Complete")