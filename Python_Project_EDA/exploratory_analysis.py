import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('customer_orders.csv')

# Quick overview
print(df.info())
print(df.describe())

# Missing values check
print("Missing values:\n", df.isnull().sum())

# Correlation heatmap
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Top 5 customers by total spending
top_customers = df.groupby('customer_id')['order_amount'].sum().sort_values(ascending=False).head(5)
print("Top 5 Customers:\n", top_customers)
