import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

for table in tables:

    count = pd.read_sql(
        f"SELECT COUNT(*) as rows FROM {table}",
        engine
    )

    print(table)
    print(count)
    print("-" * 40)