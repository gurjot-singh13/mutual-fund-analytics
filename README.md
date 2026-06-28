# Mutual Fund Analytics Platform

## Overview

This project is part of the Bluestock Fintech Data Analytics Internship Program.

The objective is to build an end-to-end Mutual Fund Analytics Platform using publicly available Indian mutual fund datasets and live NAV data.

The project covers:

- Data Ingestion & ETL
- Data Validation
- SQL Database Design
- Exploratory Data Analysis (EDA)
- Risk & Performance Analytics
- Benchmark Comparison
- Investor Demographics Analysis
- Power BI Dashboard Development

---

## Project Structure

```text
mutual-fund-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
├── sql/
├── dashboard/
├── reports/
├── scripts/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Datasets

The project uses 10 datasets:

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

## Day 1 Deliverables

Completed:

- Project setup
- Virtual environment configuration
- Dataset ingestion
- Data profiling
- Data quality checks
- AMFI code validation
- Live NAV API integration

### Data Quality Summary

- Total datasets loaded: 10
- No duplicate records found
- All AMFI codes validated successfully
- Only missing values detected:
  - `yoy_growth_pct` in Monthly SIP Inflows dataset
  - Missing values are expected due to lack of previous-year comparison data

---

## Tech Stack

- Python
- Pandas
- NumPy
- Requests
- SQLAlchemy
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook

---

## Author

Gurjot Khanuja

B.Tech CSE (AI & ML)
Bennett University