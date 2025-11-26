import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from mlxtend.frequent_patterns import apriori, association_rules

def perform_clustering(df, n_clusters=3):
    """
    Performs K-Means clustering on customer data.
    Uses 'purchase_amount_(usd)', 'previous_purchases', and 'review_rating' as features.
    """
    # Select features for clustering
    features = ['purchase_amount_(usd)', 'previous_purchases', 'review_rating']
    
    # Drop rows with missing values in these columns just in case
    X = df[features].dropna()
    
    # Standardize the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Apply K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(X_scaled)
    
    # Add cluster labels back to the original dataframe (subset)
    X['cluster'] = clusters
    
    return X, kmeans

def get_cluster_summary(df_clustered):
    """
    Returns the mean values of features for each cluster.
    """
    return df_clustered.groupby('cluster').mean()

def perform_market_basket_analysis(df, min_support=0.01):
    """
    Performs Market Basket Analysis using Apriori algorithm.
    Since the dataset is one row per transaction, we need to simulate baskets.
    We'll group by 'customer_id' and 'item_purchased'.
    """
    # Create a basket: Customer ID as rows, Items as columns, 1 if bought, 0 if not
    basket = (df.groupby(['customer_id', 'item_purchased'])['item_purchased']
              .count().unstack().reset_index().fillna(0)
              .set_index('customer_id'))

    # Convert counts to 1s and 0s
    def encode_units(x):
        return 1 if x >= 1 else 0

    basket_sets = basket.applymap(encode_units)

    # Apriori
    frequent_itemsets = apriori(basket_sets, min_support=min_support, use_colnames=True)
    
    if frequent_itemsets.empty:
        return pd.DataFrame()

    # Association Rules
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
    
    return rules

def predict_clv(df):
    """
    Simple heuristic for Customer Lifetime Value (CLV).
    CLV = Average Purchase Value * Purchase Frequency * Customer Lifespan (Assumed 1 year for now)
    """
    # Calculate metrics per customer
    customer_metrics = df.groupby('customer_id').agg({
        'purchase_amount_(usd)': ['mean', 'count']
    })
    customer_metrics.columns = ['avg_purchase_value', 'purchase_frequency']
    
    # Simple CLV formula (assuming 12 months lifespan for this snapshot)
    customer_metrics['predicted_clv'] = customer_metrics['avg_purchase_value'] * customer_metrics['purchase_frequency']
    
    return customer_metrics.sort_values(by='predicted_clv', ascending=False)
