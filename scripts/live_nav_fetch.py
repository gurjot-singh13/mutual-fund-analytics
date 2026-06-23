import requests
import pandas as pd
from pathlib import Path

SAVE_DIR = Path("data/raw/live_nav")
SAVE_DIR.mkdir(parents=True, exist_ok=True)

funds = {
    "hdfc_top100":125497,
    "sbi_bluechip":119551,
    "icici_bluechip":120503,
    "nippon_largecap":118632,
    "axis_bluechip":119092,
    "kotak_bluechip":120841
}

for fund_name, code in funds.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(
            SAVE_DIR / f"{fund_name}.csv",
            index=False
        )

        print(f"Saved: {fund_name}")
    else:
        print(f"Failed: {fund_name}")