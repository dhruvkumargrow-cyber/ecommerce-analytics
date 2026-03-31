import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

print("Loading datasets...")

# Load all datasets
orders = pd.read_csv('olist_orders_dataset.csv')
customers = pd.read_csv('olist_customers_dataset.csv')
order_items = pd.read_csv('olist_order_items_dataset.csv')
payments = pd.read_csv('olist_order_payments_dataset.csv')
reviews = pd.read_csv('olist_order_reviews_dataset.csv')
products = pd.read_csv('olist_products_dataset.csv')
sellers = pd.read_csv('olist_sellers_dataset.csv')
category_translation = pd.read_csv('product_category_name_translation.csv')

print(f"✅ Orders: {len(orders):,} rows")
print(f"✅ Customers: {len(customers):,} rows")
print(f"✅ Order Items: {len(order_items):,} rows")
print(f"✅ Payments: {len(payments):,} rows")
print(f"✅ Reviews: {len(reviews):,} rows")
print(f"✅ Products: {len(products):,} rows")
print(f"✅ Sellers: {len(sellers):,} rows")

# ── Clean orders ──────────────────────────────────────
print("\nCleaning data...")

# Convert date columns
date_cols = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]
for col in date_cols:
    orders[col] = pd.to_datetime(orders[col])

# Keep only delivered orders
orders = orders[orders['order_status'] == 'delivered'].copy()
print(f"✅ Delivered orders: {len(orders):,}")

# Extract time features
orders['order_year']    = orders['order_purchase_timestamp'].dt.year
orders['order_month']   = orders['order_purchase_timestamp'].dt.month
orders['order_day']     = orders['order_purchase_timestamp'].dt.day
orders['order_weekday'] = orders['order_purchase_timestamp'].dt.day_name()
orders['order_hour']    = orders['order_purchase_timestamp'].dt.hour
orders['year_month']    = orders['order_purchase_timestamp'].dt.to_period('M').astype(str)

# Delivery time in days
orders['delivery_days'] = (
    orders['order_delivered_customer_date'] -
    orders['order_purchase_timestamp']
).dt.days

# ── Merge datasets ────────────────────────────────────
print("\nMerging datasets...")

# Merge products with English category names
products = products.merge(
    category_translation,
    on='product_category_name',
    how='left'
)
products['category'] = products['product_category_name_english'].fillna('unknown')

# Main merged dataset
df = orders.merge(customers, on='customer_id', how='left')
df = df.merge(order_items, on='order_id', how='left')
df = df.merge(products[['product_id', 'category']], on='product_id', how='left')
df = df.merge(sellers[['seller_id', 'seller_state']], on='seller_id', how='left')

# Merge payments
payment_summary = payments.groupby('order_id').agg(
    total_payment=('payment_value', 'sum'),
    payment_type=('payment_type', 'first')
).reset_index()
df = df.merge(payment_summary, on='order_id', how='left')

# Merge reviews
review_summary = reviews.groupby('order_id').agg(
    review_score=('review_score', 'mean')
).reset_index()
df = df.merge(review_summary, on='order_id', how='left')

print(f"✅ Final merged dataset: {len(df):,} rows, {len(df.columns)} columns")

# ── Clean merged dataset ──────────────────────────────
df = df.dropna(subset=['total_payment', 'category'])
df = df[df['total_payment'] > 0]
df = df[df['delivery_days'] > 0]
df = df[df['delivery_days'] < 120]

print(f"✅ After cleaning: {len(df):,} rows")

# ── Create analysis tables ────────────────────────────
print("\nCreating analysis tables...")

# 1. Monthly revenue
monthly_revenue = df.groupby('year_month').agg(
    total_revenue=('total_payment', 'sum'),
    total_orders=('order_id', 'nunique'),
    avg_order_value=('total_payment', 'mean')
).reset_index()
monthly_revenue = monthly_revenue.sort_values('year_month')
monthly_revenue.to_csv('monthly_revenue.csv', index=False)
print("✅ monthly_revenue.csv")

# 2. Category performance
category_performance = df.groupby('category').agg(
    total_revenue=('total_payment', 'sum'),
    total_orders=('order_id', 'nunique'),
    avg_order_value=('total_payment', 'mean'),
    avg_review_score=('review_score', 'mean')
).reset_index()
category_performance = category_performance.sort_values(
    'total_revenue', ascending=False
).head(20)
category_performance.to_csv('category_performance.csv', index=False)
print("✅ category_performance.csv")

# 3. State performance
state_performance = df.groupby('customer_state').agg(
    total_revenue=('total_payment', 'sum'),
    total_orders=('order_id', 'nunique'),
    avg_order_value=('total_payment', 'mean'),
    avg_delivery_days=('delivery_days', 'mean')
).reset_index()
state_performance = state_performance.sort_values(
    'total_revenue', ascending=False
)
state_performance.to_csv('state_performance.csv', index=False)
print("✅ state_performance.csv")

# 4. Payment methods
payment_analysis = df.groupby('payment_type').agg(
    total_revenue=('total_payment', 'sum'),
    total_orders=('order_id', 'nunique'),
    avg_payment=('total_payment', 'mean')
).reset_index()
payment_analysis.to_csv('payment_analysis.csv', index=False)
print("✅ payment_analysis.csv")

# 5. Delivery performance
delivery_performance = df.groupby('customer_state').agg(
    avg_delivery_days=('delivery_days', 'mean'),
    total_orders=('order_id', 'nunique')
).reset_index()
delivery_performance = delivery_performance.sort_values(
    'avg_delivery_days'
)
delivery_performance.to_csv('delivery_performance.csv', index=False)
print("✅ delivery_performance.csv")

# 6. Weekday analysis
weekday_analysis = df.groupby('order_weekday').agg(
    total_orders=('order_id', 'nunique'),
    total_revenue=('total_payment', 'sum'),
    avg_order_value=('total_payment', 'mean')
).reset_index()
weekday_analysis.to_csv('weekday_analysis.csv', index=False)
print("✅ weekday_analysis.csv")

# 7. Hourly analysis
hourly_analysis = df.groupby('order_hour').agg(
    total_orders=('order_id', 'nunique'),
    total_revenue=('total_payment', 'sum')
).reset_index()
hourly_analysis.to_csv('hourly_analysis.csv', index=False)
print("✅ hourly_analysis.csv")

# 8. Review score distribution
review_distribution = df.groupby('review_score').agg(
    total_orders=('order_id', 'nunique'),
    total_revenue=('total_payment', 'sum')
).reset_index()
review_distribution.to_csv('review_distribution.csv', index=False)
print("✅ review_distribution.csv")

# 9. Master dataset for Power BI
master_df = df[[
    'order_id', 'customer_id', 'order_year', 'order_month',
    'year_month', 'order_weekday', 'order_hour',
    'customer_state', 'category', 'seller_state',
    'total_payment', 'payment_type', 'review_score',
    'delivery_days'
]].copy()
master_df.to_csv('master_dataset.csv', index=False)
print("✅ master_dataset.csv")

print(f"\n🎉 Data cleaning complete!")
print(f"📊 Total Revenue: R$ {df['total_payment'].sum():,.2f}")
print(f"📦 Total Orders: {df['order_id'].nunique():,}")
print(f"⭐ Avg Review Score: {df['review_score'].mean():.2f}")
print(f"🚚 Avg Delivery Days: {df['delivery_days'].mean():.1f}")
print(f"🏷️ Top Category: {category_performance.iloc[0]['category']}")