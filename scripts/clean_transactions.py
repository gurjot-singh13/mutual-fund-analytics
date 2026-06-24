import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Convert date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Remove duplicates
before = len(df)
df = df.drop_duplicates()
after = len(df)

print(f"Duplicates Removed: {before-after}")

mapping = {
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
    .map(mapping)
)

print("\nTransaction Types:")
print(df["transaction_type"].unique())

# Validate amount > 0
invalid_amounts = (df["amount_inr"] <= 0).sum()

print("\nInvalid Amount Records:", invalid_amounts)

# Check KYC values
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

# Save cleaned file
df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("\nSaved Successfully")