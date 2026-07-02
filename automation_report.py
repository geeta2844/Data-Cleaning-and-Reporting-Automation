import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mobile_sales_data.csv")

original_rows = len(df)

missing_before = df.isnull().sum().sum()

# Fill missing values

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna("Unknown")
    else:
        df[col] = df[col].fillna(df[col].median())

duplicates_removed = df.duplicated().sum()

df = df.drop_duplicates()

df.to_csv("cleaned_sales_data.csv", index=False)

report = f"""
DATA QUALITY REPORT

Original Records: {original_rows}

Final Records: {len(df)}

Missing Values Found: {missing_before}

Duplicates Removed: {duplicates_removed}

Columns:
{list(df.columns)}
"""

with open("data_quality_report.txt", "w") as file:
    file.write(report)

print(report)

import os

os.makedirs("screenshots", exist_ok=True)

df["Revenue"] = df["Price"] * df["Quantity Sold"]

brand_sales = df.groupby("Brand")["Revenue"].sum()

plt.figure(figsize=(8,5))

brand_sales.plot(kind="bar")

plt.title("Revenue by Brand")

plt.tight_layout()

plt.savefig("screenshots/revenue_by_brand.png")

plt.close()

region_sales = df.groupby("Region")["Revenue"].sum()

plt.figure(figsize=(8,5))

region_sales.plot(kind="bar")

plt.title("Revenue by Region")

plt.tight_layout()

plt.savefig("screenshots/revenue_by_region.png")

plt.close()

missing_data = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum().values
})

plt.figure(figsize=(8,5))

plt.bar(
    missing_data["Column"],
    missing_data["Missing Values"]
)

plt.xticks(rotation=90)

plt.title("Missing Values Summary")

plt.tight_layout()

plt.savefig("screenshots/missing_values.png")

plt.close()

print("\nAutomation Completed Successfully!")
print("Cleaned dataset saved.")
print("Report generated.")
print("Charts generated.")
