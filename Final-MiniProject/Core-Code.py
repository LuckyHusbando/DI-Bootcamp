# Final Mini-Project - 12/11/2025

import numpy as np # linear algebra
import pandas as pd
import sqlite3

df_olist_customers = pd.read_csv('/kaggle/input/brazilian-ecommerce/olist_customers_dataset.csv')
df_olist_sellers = pd.read_csv('/kaggle/input/brazilian-ecommerce/olist_sellers_dataset.csv')
df_olist_order_reviews= pd.read_csv('/kaggle/input/brazilian-ecommerce/olist_order_reviews_dataset.csv')
df_olist_order_items= pd.read_csv('/kaggle/input/brazilian-ecommerce/olist_order_items_dataset.csv')
df_olist_products= pd.read_csv('/kaggle/input/brazilian-ecommerce/olist_products_dataset.csv')
df_olist_geolocation= pd.read_csv('/kaggle/input/brazilian-ecommerce/olist_geolocation_dataset.csv')
df_product_category_name_translation= pd.read_csv('/kaggle/input/brazilian-ecommerce/product_category_name_translation.csv')
df_olist_orders = pd.read_csv('/kaggle/input/brazilian-ecommerce/olist_orders_dataset.csv')
df_olist_order_payments= pd.read_csv('/kaggle/input/brazilian-ecommerce/olist_order_payments_dataset.csv')

df_olist_customers.head()

from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

# export the dataframe as a table 'playstore' to the sqlite engine
df_olist_customers.to_sql("olist_customers", con =engine)
df_olist_sellers.to_sql("olist_sellers", con =engine)
df_olist_order_reviews.to_sql("olist_order_reviews", con =engine)
df_olist_order_items.to_sql("olist_order_items", con =engine)
df_olist_products.to_sql("olist_products_dataset", con =engine)
df_olist_geolocation.to_sql("olist_geolocation", con =engine)
df_product_category_name_translation.to_sql("product_category_name_translation", con =engine)
df_olist_orders.to_sql("olist_orders", con =engine)
df_olist_order_payments.to_sql("olist_order_payments", con =engine)
df_olist_order_payments.head()

# Load the datasets
try:
    customers_df = pd.read_csv('olist_customers_dataset.csv')
    geolocation_df = pd.read_csv('olist_geolocation_dataset.csv')
    order_items_df = pd.read_csv('olist_order_items_dataset.csv')
    order_payments_df = pd.read_csv('olist_order_payments_dataset.csv')
    order_reviews_df = pd.read_csv('olist_order_reviews_dataset.csv')
    orders_df = pd.read_csv('olist_orders_dataset.csv')
    products_df = pd.read_csv('olist_products_dataset.csv')
    sellers_df = pd.read_csv('olist_sellers_dataset.csv')
    product_category_translation_df = pd.read_csv('product_category_name_translation.csv')
except FileNotFoundError as e:
    print(f"Error loading file: {e}")
    # Exit or handle the error appropriately
    
# Create SQLite engine
engine = create_engine('sqlite:///olist_data.db')

# Export DataFrames to SQL tables
dataframes = {
    'customers': customers_df,
    'geolocation': geolocation_df,
    'order_items': order_items_df,
    'order_payments': order_payments_df,
    'order_reviews': order_reviews_df,
    'orders': orders_df,
    'products': products_df,
    'sellers': sellers_df,
    'product_category_translation': product_category_translation_df
}

for table_name, df in dataframes.items():
    df.to_sql(table_name, engine, if_exists='replace', index=False)

print("✅ SQLite database 'olist_data.db' created and all DataFrames exported as tables.")



