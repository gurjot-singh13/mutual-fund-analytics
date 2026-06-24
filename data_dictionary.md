# Data Dictionary

## 01_fund_master.csv

| Column            | Data Type | Description                   |
| ----------------- | --------- | ----------------------------- |
| amfi_code         | Integer   | Unique AMFI scheme identifier |
| fund_house        | String    | Mutual fund company           |
| scheme_name       | String    | Scheme name                   |
| category          | String    | Fund category                 |
| sub_category      | String    | Fund sub-category             |
| plan              | String    | Direct/Regular plan           |
| benchmark         | String    | Benchmark index               |
| expense_ratio_pct | Float     | Expense ratio percentage      |
| risk_category     | String    | Risk classification           |

---

## 02_nav_history.csv

| Column    | Data Type | Description            |
| --------- | --------- | ---------------------- |
| amfi_code | Integer   | AMFI scheme identifier |
| date      | Date      | NAV date               |
| nav       | Float     | Net Asset Value        |

---

## 03_aum_by_fund_house.csv

| Column      | Data Type | Description                         |
| ----------- | --------- | ----------------------------------- |
| date        | Date      | Reporting date                      |
| fund_house  | String    | Mutual fund company                 |
| aum_crore   | Integer   | Assets under Management (Crore INR) |
| num_schemes | Integer   | Number of schemes managed           |

---

## 07_scheme_performance.csv

| Column           | Data Type | Description                   |
| ---------------- | --------- | ----------------------------- |
| return_1yr_pct   | Float     | 1-year return                 |
| return_3yr_pct   | Float     | 3-year return                 |
| return_5yr_pct   | Float     | 5-year return                 |
| alpha            | Float     | Excess return over benchmark  |
| beta             | Float     | Market sensitivity            |
| sharpe_ratio     | Float     | Risk-adjusted return          |
| sortino_ratio    | Float     | Downside-risk adjusted return |
| max_drawdown_pct | Float     | Maximum decline from peak     |

---

## 08_investor_transactions.csv

| Column           | Data Type | Description            |
| ---------------- | --------- | ---------------------- |
| investor_id      | String    | Unique investor ID     |
| transaction_date | Date      | Transaction date       |
| transaction_type | String    | SIP/Lumpsum/Redemption |
| amount_inr       | Integer   | Transaction amount     |
| state            | String    | Investor state         |
| city             | String    | Investor city          |
| age_group        | String    | Investor age segment   |
| gender           | String    | Investor gender        |

---

Source:
AMFI India, mfapi.in, Bluestock Mutual Fund Analytics Dataset
