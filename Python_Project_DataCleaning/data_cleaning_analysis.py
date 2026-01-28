import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('sales_data.csv')

# Data cleaning
df['order_date'] = pd.to_datetime(df['order_date'])
df.dropna(subset=['product_name', 'quantity', 'price'], inplace=True)

# Add total revenue column
df['total_revenue'] = df['quantity'] * df['price']

# Aggregate revenue by product
product_revenue = df.groupby('product_name')['total_revenue'].sum().sort_values(ascending=False)
print("Top Products by Revenue:\n", product_revenue)

# Visualize top 5 products
product_revenue.head(5).plot(kind='bar', figsize=(8,5), title='Top 5 Products by Revenue')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()
