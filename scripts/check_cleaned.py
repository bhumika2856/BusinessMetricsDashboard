import pandas as pd

# Load cleaned CSV
df = pd.read_csv("../data/Cleaned_Retail_Data.csv")

print("Shape:", df.shape)
print(df.head())

# Keep the large dataset in CSV (no issue with size)
# Create a smaller Excel sample for viewing
sample = df.sample(50000, random_state=42)  # 50k rows only

# Save smaller version for Excel
sample.to_excel("../data/Cleaned_Retail_Sample.xlsx", index=False, engine="openpyxl")

print("Saved a 50k row sample as Cleaned_Retail_Sample.xlsx for Excel viewing")
