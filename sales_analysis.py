import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": [
        "Laptop", "Mobile", "Headphones", "Laptop",
        "Mobile", "Keyboard", "Mouse", "Headphones",
        "Laptop", "Mobile"
    ],
    "Month": [
        "Jan", "Jan", "Jan", "Feb", "Feb",
        "Feb", "Mar", "Mar", "Mar", "Mar"
    ],
    "Quantity": [5, 10, 15, 3, 8, 12, 20, 10, 4, 6],
    "Price": [
        50000, 20000, 2000, 50000, 20000,
        1500, 500, 2000, 50000, 20000
    ]
}

df = pd.DataFrame(data)

# Calculate sales
df["Total Sales"] = df["Quantity"] * df["Price"]

# Display total revenue
print("TOTAL REVENUE: Rs.", df["Total Sales"].sum())

# Product-wise sales
product_sales = df.groupby("Product")["Total Sales"].sum()
print("\nPRODUCT-WISE SALES")
print(product_sales)

# Monthly sales
monthly_sales = df.groupby("Month")["Total Sales"].sum()
print("\nMONTHLY SALES")
print(monthly_sales)

# Save report
df.to_csv("sales_report.csv", index=False)

# Create chart
product_sales.plot(kind="bar", title="Product Sales Analysis")
plt.ylabel("Sales (Rs.)")
plt.tight_layout()
plt.savefig("product_sales.png")
plt.show()

print("\nProject completed successfully!")