import pandas as pd

def calculate_kpis(df):
    """
    Calculates high-level KPIs.
    """
    total_revenue = df['purchase_amount_(usd)'].sum()
    avg_purchase_value = df['purchase_amount_(usd)'].mean()
    total_customers = df['customer_id'].nunique()
    avg_rating = df['review_rating'].mean()
    
    return {
        "Total Revenue": total_revenue,
        "Avg Purchase Value": avg_purchase_value,
        "Total Customers": total_customers,
        "Avg Rating": avg_rating
    }

def get_revenue_by_category(df):
    """
    Aggregates revenue by category.
    """
    return df.groupby('category')['purchase_amount_(usd)'].sum().sort_values(ascending=False)

def get_revenue_by_gender(df):
    """
    Aggregates revenue by gender.
    """
    return df.groupby('gender')['purchase_amount_(usd)'].sum().sort_values(ascending=False)

def get_subscription_impact(df):
    """
    Compares spending between subscribers and non-subscribers.
    """
    return df.groupby('subscription_status')['purchase_amount_(usd)'].mean()
