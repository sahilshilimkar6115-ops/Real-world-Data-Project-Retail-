
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("retail_sales_data.csv")

# Basic information
print(df.head())
print(df.describe())

# Revenue by Product
product_revenue = df.groupby("Product")["Revenue"].sum()
print("\nRevenue by Product:")
print(product_revenue)

# Plot Revenue by Product
product_revenue.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

# Revenue by Region
region_revenue = df.groupby("Region")["Revenue"].sum()
print("\nRevenue by Region:")
print(region_revenue)

# Plot Revenue by Region
region_revenue.plot(kind="pie", autopct='%1.1f%%')
plt.title("Revenue Share by Region")
plt.ylabel("")
plt.show()
