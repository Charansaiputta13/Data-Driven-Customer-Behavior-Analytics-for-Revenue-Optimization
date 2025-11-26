import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_loader import get_data
from src.analytics import calculate_kpis, get_revenue_by_category, get_revenue_by_gender, get_subscription_impact
from src.ml_models import perform_clustering, get_cluster_summary

# Page Config
st.set_page_config(page_title="Customer Analytics Dashboard", layout="wide")

# Load Data
try:
    df = get_data()
except FileNotFoundError as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Deep Dive", "ML Insights"])

st.sidebar.info("Data-Driven Customer Behavior Analytics")

if page == "Overview":
    st.title("📊 Executive Overview")
    
    # KPIs
    kpis = calculate_kpis(df)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"${kpis['Total Revenue']:,.2f}")
    col2.metric("Avg Purchase Value", f"${kpis['Avg Purchase Value']:.2f}")
    col3.metric("Total Customers", f"{kpis['Total Customers']:,}")
    col4.metric("Avg Rating", f"{kpis['Avg Rating']:.2f}")
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Revenue by Category")
        rev_by_cat = get_revenue_by_category(df).reset_index()
        fig_cat = px.bar(rev_by_cat, x='category', y='purchase_amount_(usd)', color='category')
        st.plotly_chart(fig_cat, use_container_width=True)
        
    with col2:
        st.subheader("Revenue by Gender")
        rev_by_gen = get_revenue_by_gender(df).reset_index()
        fig_gen = px.pie(rev_by_gen, values='purchase_amount_(usd)', names='gender', hole=0.4)
        st.plotly_chart(fig_gen, use_container_width=True)

elif page == "Deep Dive":
    st.title("🔍 Deep Dive Analytics")
    
    # Filters
    st.subheader("Filter Data")
    selected_gender = st.multiselect("Select Gender", df['gender'].unique(), default=df['gender'].unique())
    selected_category = st.multiselect("Select Category", df['category'].unique(), default=df['category'].unique())
    
    filtered_df = df[(df['gender'].isin(selected_gender)) & (df['category'].isin(selected_category))]
    
    st.write(f"Showing {len(filtered_df)} records")
    
    # Subscription Impact
    st.subheader("Subscription Impact on Spending")
    sub_impact = get_subscription_impact(filtered_df).reset_index()
    fig_sub = px.bar(sub_impact, x='subscription_status', y='purchase_amount_(usd)', 
                     title="Average Spend: Subscribers vs Non-Subscribers")
    st.plotly_chart(fig_sub, use_container_width=True)
    
    # Age Distribution
    st.subheader("Age Distribution of Customers")
    fig_age = px.histogram(filtered_df, x='age', nbins=20, title="Customer Age Distribution")
    st.plotly_chart(fig_age, use_container_width=True)

elif page == "ML Insights":
    st.title("🤖 Machine Learning Insights")
    st.markdown("Using **K-Means Clustering** to segment customers based on spending behavior, frequency, and ratings.")
    
    n_clusters = st.slider("Select Number of Clusters", 2, 6, 3)
    
    if st.button("Run Clustering"):
        with st.spinner("Running K-Means..."):
            clustered_df, model = perform_clustering(df, n_clusters)
            
            st.success("Clustering Complete!")
            
            # Cluster Summary
            st.subheader("Cluster Profiles")
            summary = get_cluster_summary(clustered_df)
            st.dataframe(summary.style.highlight_max(axis=0))
            
            # Visualization
            st.subheader("Cluster Visualization")
            fig_cluster = px.scatter_3d(clustered_df, x='purchase_amount_(usd)', y='previous_purchases', z='review_rating',
                                        color='cluster', title="Customer Segments (3D View)")
            st.plotly_chart(fig_cluster, use_container_width=True)
            
            st.markdown("""
            **Interpretation:**
            - **High Value**: Look for clusters with high Purchase Amount and high Previous Purchases.
            - **At Risk**: Look for clusters with low Recent Activity or low Ratings.
            """)
