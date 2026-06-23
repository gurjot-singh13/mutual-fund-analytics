import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")

csv_files = sorted(RAW_PATH.glob("*.csv"))

print("\n" + "=" * 80)
print(f"FOUND {len(csv_files)} DATASETS")
print("=" * 80)

dataset_summary = []

for file in csv_files:

    print("\n" + "=" * 80)
    print(f"DATASET: {file.name}")
    print("=" * 80)

    try:
        df = pd.read_csv(file)

        dataset_summary.append(
            {
                "dataset": file.name,
                "rows": df.shape[0],
                "columns": df.shape[1],
                "missing_values": int(df.isnull().sum().sum()),
                "duplicates": int(df.duplicated().sum())
            }
        )

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error loading {file.name}")
        print(e)

print("\n" + "=" * 80)
print("DATASET SUMMARY")
print("=" * 80)

summary_df = pd.DataFrame(dataset_summary)
print(summary_df)