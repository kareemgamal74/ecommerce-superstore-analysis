
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# إعدادات العرض
pd.set_option("display.max_columns", None)
sns.set_style("whitegrid")

# =========================
# تحميل وتنظيف البيانات
def load_and_clean_data(filepath):
    df = pd.read_csv(filepath, encoding='latin1')
    df["Row ID"] = pd.to_numeric(df["Row ID"])
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)
    df['Postal Code'] = df['Postal Code'].fillna("not found").astype(str)
    return df

# =========================
# التحليلات والرسوم
def plot_sales_vs_profit(df):
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    plt.figure(figsize=(6, 4))
    sns.barplot(x=["Sales", "Profit"], y=[total_sales, total_profit], palette="Blues_d")
    plt.title("Total Sales vs Total Profit")
    for i, v in enumerate([total_sales, total_profit]):
        plt.text(i, v, f"{v:,.2f}", ha="center", va="bottom")
    plt.show()

def plot_sales_by_category(df):
    category_sales = df.groupby("Category")["Sales"].sum().sort_values()
    plt.figure(figsize=(7, 4))
    sns.barplot(x=category_sales.values, y=category_sales.index, palette="viridis")
    plt.title("Sales by Category")
    for i, v in enumerate(category_sales.values):
        plt.text(v, i, f"{v:,.2f}")
    plt.show()

def plot_sales_by_subcategory(df):
    sub_sales = df.groupby("Sub-Category")["Sales"].sum().sort_values()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sub_sales.values, y=sub_sales.index, palette="coolwarm")
    plt.title("Sales by Sub-Category")
    for i, v in enumerate(sub_sales.values):
        plt.text(v, i, f"{v:,.2f}")
    plt.show()

def plot_top_customers(df):
    top_customers = df.groupby("Customer Name")["Sales"].sum().nlargest(10)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=top_customers.index, y=top_customers.values, palette="magma")
    plt.title("Top 10 Customers by Sales")
    plt.xticks(rotation=45)
    for i, v in enumerate(top_customers.values):
        plt.text(i, v, f"{v:,.2f}", ha="center", va="bottom", color="red")
    plt.tight_layout()
    plt.show()

def plot_sales_over_years(df):
    df["Order Year"] = df["Order Date"].dt.year
    yearly_sales = df.groupby("Order Year")["Sales"].sum()
    plt.figure(figsize=(8, 5))
    sns.lineplot(x=yearly_sales.index, y=yearly_sales.values, marker="o", color="green")
    plt.title("Sales Over Years")
    plt.ylabel("Sales (USD)")
    plt.grid(True)
    plt.show()

def plot_top_cities(df):
    top_cities = df.groupby("City")["Sales"].sum().nlargest(10)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=top_cities.index, y=top_cities.values, palette="cubehelix")
    plt.title("Top 10 Cities by Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# =========================
#  ملخص التحليل
def print_summary(df):
    print("========== SUMMARY ==========")
    print(f"Total Sales: {df['Sales'].sum():,.2f} USD")
    print(f"Total Profit: {df['Profit'].sum():,.2f} USD")
    print(f"Number of Unique Customers: {df['Customer Name'].nunique()}")
    print(f"Number of Cities: {df['City'].nunique()}")
    print("=============================")

# =========================
# التنفيذ

if __name__ == "__main__":
    file_path = r"C:\Users\AdminOS\Desktop\python\ecommerce-superstore-analysis\data\Global_Superstore2.csv"
    df = load_and_clean_data(file_path)

    print_summary(df)
    plot_sales_vs_profit(df)
    plot_sales_by_category(df)
    plot_sales_by_subcategory(df)
    plot_top_customers(df)
    plot_sales_over_years(df)
    plot_top_cities(df)
