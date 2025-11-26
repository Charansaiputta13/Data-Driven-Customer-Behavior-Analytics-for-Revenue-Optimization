import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_loader import get_data
from src.analytics import calculate_kpis, get_revenue_by_category, get_revenue_by_gender, get_subscription_impact
from src.ml_models import perform_clustering, get_cluster_summary, perform_market_basket_analysis, predict_clv

# Page Config
st.set_page_config(page_title="Customer Analytics Dashboard", layout="wide", page_icon="🛒")

# Custom CSS for UI/UX
st.markdown("""
<style>
    .metric-card {
        background-color: #262730;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        text-align: center;
    }
    .metric-value {
        font-size: 2em;
        font-weight: bold;
        color: #F63366;
    }
    .metric-label {
        font-size: 1em;
        color: #FAFAFA;
    }
</style>
""", unsafe_allow_html=True)

# Load Data
try:
    df = get_data()
except FileNotFoundError as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100) # Placeholder Logo
page = st.sidebar.radio("Go to", ["Overview", "Deep Dive", "ML Insights", "Market Basket", "Predictive Analytics"])

st.sidebar.info("Data-Driven Customer Behavior Analytics")

if page == "Overview":
    st.title("📊 Executive Overview")
    
    # Custom KPI Cards
    kpis = calculate_kpis(df)
    col1, col2, col3, col4 = st.columns(4)
    
    def metric_card(label, value):
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

    with col1: metric_card("Total Revenue", f"${kpis['Total Revenue']:,.2f}")
    with col2: metric_card("Avg Purchase Value", f"${kpis['Avg Purchase Value']:.2f}")
    with col3: metric_card("Total Customers", f"{kpis['Total Customers']:,}")
    with col4: metric_card("Avg Rating", f"{kpis['Avg Rating']:.2f}")
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Revenue by Category")
        rev_by_cat = get_revenue_by_category(df).reset_index()
        fig_cat = px.bar(rev_by_cat, x='category', y='purchase_amount_(usd)', color='category', template="plotly_dark")
        st.plotly_chart(fig_cat, use_container_width=True)
        
    with col2:
        st.subheader("Revenue by Gender")
        rev_by_gen = get_revenue_by_gender(df).reset_index()
        fig_gen = px.pie(rev_by_gen, values='purchase_amount_(usd)', names='gender', hole=0.4, template="plotly_dark")
        st.plotly_chart(fig_gen, use_container_width=True)

elif page == "Deep Dive":
    st.title("🔍 Deep Dive Analytics")
    
    # Filters in Expander
    with st.expander("Filter Data", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            selected_gender = st.multiselect("Select Gender", df['gender'].unique(), default=df['gender'].unique())
        with col2:
            selected_category = st.multiselect("Select Category", df['category'].unique(), default=df['category'].unique())
    
    filtered_df = df[(df['gender'].isin(selected_gender)) & (df['category'].isin(selected_category))]
    
    st.write(f"Showing {len(filtered_df)} records")
    
    # Download Button
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Filtered Data", data=csv, file_name="filtered_data.csv", mime="text/csv")
    
    # Subscription Impact
    st.subheader("Subscription Impact on Spending")
    sub_impact = get_subscription_impact(filtered_df).reset_index()
    fig_sub = px.bar(sub_impact, x='subscription_status', y='purchase_amount_(usd)', 
                     title="Average Spend: Subscribers vs Non-Subscribers", template="plotly_dark")
    st.plotly_chart(fig_sub, use_container_width=True)
    
    # Age Distribution
    st.subheader("Age Distribution of Customers")
    fig_age = px.histogram(filtered_df, x='age', nbins=20, title="Customer Age Distribution", template="plotly_dark")
    st.plotly_chart(fig_age, use_container_width=True)

elif page == "ML Insights":
    st.title("🤖 Customer Segmentation (K-Means)")
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
                                        color='cluster', title="Customer Segments (3D View)", template="plotly_dark")
            st.plotly_chart(fig_cluster, use_container_width=True)

elif page == "Market Basket":
    st.title("🛒 Market Basket Analysis")
    st.markdown("Discovering relationships between products using **Association Rules (Apriori)**.")
    
    min_support = st.slider("Minimum Support (Frequency)", 0.001, 0.1, 0.01, step=0.001)
    
    if st.button("Find Associations"):
        with st.spinner("Mining rules..."):
            rules = perform_market_basket_analysis(df, min_support=min_support)
            
            if not rules.empty:
                st.success(f"Found {len(rules)} association rules!")
                st.dataframe(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].sort_values(by='lift', ascending=False))
                
                st.subheader("Top Rules by Lift")
                st.bar_chart(rules.sort_values(by='lift', ascending=False).head(10).set_index('antecedents')['lift'])
            else:
                st.warning("No rules found with current support level. Try lowering the minimum support.")

elif page == "Predictive Analytics":
    st.title("🔮 Predictive Analytics (CLV)")
    st.markdown("Predicting **Customer Lifetime Value (CLV)** based on purchase history.")
    
    if st.button("Predict CLV"):
        with st.spinner("Calculating CLV..."):
            clv_df = predict_clv(df)
            
            st.subheader("Top 10 High-Value Customers")
            st.dataframe(clv_df.head(10))
            
            st.subheader("CLV Distribution")
            fig_clv = px.histogram(clv_df, x='predicted_clv', title="Predicted CLV Distribution", template="plotly_dark")
            st.plotly_chart(fig_clv, use_container_width=True)
