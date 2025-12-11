# Final Mini-Project - 12/11/2025

import numpy as np # Note: numpy is imported but not explicitly used in this snippet
import pandas as pd
# import sqlite3 # Not strictly necessary if using pandas/sqlalchemy to interact

from sqlalchemy import create_engine

# --- Configuration for Kaggle File Paths ---
# Base directory for the Brazilian Ecommerce dataset
KAGGLE_PATH = '/kaggle/input/brazilian-ecommerce/'

# --- 1. Load the Datasets ---
print("Attempting to load Olist datasets...")
try:
    df_olist_customers = pd.read_csv(KAGGLE_PATH + 'olist_customers_dataset.csv')
    df_olist_sellers = pd.read_csv(KAGGLE_PATH + 'olist_sellers_dataset.csv')
    df_olist_order_reviews = pd.read_csv(KAGGLE_PATH + 'olist_order_reviews_dataset.csv')
    df_olist_order_items = pd.read_csv(KAGGLE_PATH + 'olist_order_items_dataset.csv')
    df_olist_products = pd.read_csv(KAGGLE_PATH + 'olist_products_dataset.csv')
    df_olist_geolocation = pd.read_csv(KAGGLE_PATH + 'olist_geolocation_dataset.csv')
    df_product_category_name_translation = pd.read_csv(KAGGLE_PATH + 'product_category_name_translation.csv')
    df_olist_orders = pd.read_csv(KAGGLE_PATH + 'olist_orders_dataset.csv')
    df_olist_order_payments = pd.read_csv(KAGGLE_PATH + 'olist_order_payments_dataset.csv')
    print("✅ All datasets loaded successfully.")

except FileNotFoundError as e:
    print(f"Error loading file. Check your file path: {e}")
    # You might want to exit here if files are essential
    raise # Re-raise the exception to stop execution

# Display the head of one DataFrame (as in the original code)
print("\nHead of olist_customers_dataset:")
print(df_olist_customers.head())

# --- 2. Create SQLite Engine and Export DataFrames ---

# Use a file-based database (olist_data.db) instead of in-memory (sqlite://)
engine = create_engine('sqlite:///olist_data.db', echo=False)

# Define the DataFrames and their desired table names
dataframes_to_export = {
    "customers": df_olist_customers,
    "sellers": df_olist_sellers,
    "order_reviews": df_olist_order_reviews,
    "order_items": df_olist_order_items,
    "products": df_olist_products,
    "geolocation": df_olist_geolocation,
    "category_translation": df_product_category_name_translation,
    "orders": df_olist_orders,
    "order_payments": df_olist_order_payments
}

print("\nExporting DataFrames to SQLite tables...")
for table_name, df in dataframes_to_export.items():
    # 'if_exists=replace' will overwrite the table if it already exists
    # 'index=False' prevents pandas from writing the DataFrame index as a column
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"   - Exported {table_name}")

print("\n✅ SQLite database 'olist_data.db' created and all DataFrames exported as tables.")