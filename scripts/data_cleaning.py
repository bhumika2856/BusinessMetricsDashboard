import pandas as pd

# Load datasets
sales = pd.read_csv("../data/sales.csv", low_memory=False)
products = pd.read_csv("../data/product_hierarchy.csv")
stores = pd.read_csv("../data/store_cities.csv")

print("✅ Files loaded successfully")

# Convert order_date column if present
if "order_date" in sales.columns:
    sales['order_date'] = pd.to_datetime(sales['order_date'], errors='coerce')

# Merge sales with products
if "product_id" in sales.columns and "product_id" in products.columns:
    sales_products = sales.merge(products, on="product_id", how="left")
else:
    print("⚠️ product_id column missing in one of the files")
    sales_products = sales

# Merge with stores
if "store_id" in sales_products.columns and "store_id" in stores.columns:
    final_data = sales_products.merge(stores, on="store_id", how="left")
else:
    print("⚠️ store_id column missing in one of the files")
    final_data = sales_products

# Add calculated fields if columns exist
if "profit" in final_data.columns and "sales" in final_data.columns:
    final_data["ProfitMargin"] = final_data["profit"] / final_data["sales"]

# Save cleaned dataset
final_data.to_csv("../data/Cleaned_Retail_Data.csv", index=False)

print("✅ Final merged dataset saved as Cleaned_Retail_Data.csv")
