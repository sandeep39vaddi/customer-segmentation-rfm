import pandas as pd

df = pd.read_csv(
    'C:/Users/sande/Desktop/DATA_ANALYST_PORTFOLIO/P1_ECOMMERCE_ANALYSIS/DATA/superstore.csv',
    encoding='latin1'
)

print(df.head())
print(df.info())
print(df.describe())
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
print(df.dtypes)
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Month Name'] = df['Order Date'].dt.month_name()
print("Total Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())
print(df.groupby('Region')['Sales'].sum())
print(df.groupby('Region')['Profit'].sum())
print(df.groupby('Month Name')['Sales'].sum())
loss_products = df[df['Profit'] < 0]

print(loss_products.groupby('Product Name')['Profit'].sum().sort_values().head(10))
print(df.groupby('Category')['Profit'].sum())
print(df.groupby('Discount')['Profit'].mean())
month_order = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

monthly_sales = df.groupby('Month Name')['Sales'].sum().reindex(month_order)

print(monthly_sales)
import matplotlib.pyplot as plt

monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.show()
df.to_csv(
    'C:/Users/sande/Desktop/DATA_ANALYST_PORTFOLIO/P1_ECOMMERCE_ANALYSIS/DATA/cleaned_superstore.csv', 
    index=False
)
import matplotlib.pyplot as plt

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('C:/Users/sande/Desktop/DATA_ANALYST_PORTFOLIO/P1_ECOMMERCE_ANALYSIS/images/monthly_sales.png')
plt.show()

sales_region = df.groupby('Region')['Sales'].sum()

plt.figure()
sales_region.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()

plt.savefig('C:/Users/sande/Desktop/DATA_ANALYST_PORTFOLIO/P1_ECOMMERCE_ANALYSIS/images/sales_region.png')
plt.show()

profit_category = df.groupby('Category')['Profit'].sum()

plt.figure()
profit_category.plot(kind='bar')
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()

plt.savefig('C:/Users/sande/Desktop/DATA_ANALYST_PORTFOLIO/P1_ECOMMERCE_ANALYSIS/images/profit_category.png')
plt.show()

top_loss = loss_products.groupby('Product Name')['Profit'].sum().sort_values().head(10)

plt.figure()
top_loss.plot(kind='bar')
plt.title("Top 10 Loss-Making Products")
plt.xticks(rotation=75)
plt.tight_layout()

plt.savefig('C:/Users/sande/Desktop/DATA_ANALYST_PORTFOLIO/P1_ECOMMERCE_ANALYSIS/images/loss_products.png')
plt.show()

plt.figure()
plt.scatter(df['Discount'], df['Profit'])
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()

plt.savefig('C:/Users/sande/Desktop/DATA_ANALYST_PORTFOLIO/P1_ECOMMERCE_ANALYSIS/images/discount_profit.png')
plt.show()