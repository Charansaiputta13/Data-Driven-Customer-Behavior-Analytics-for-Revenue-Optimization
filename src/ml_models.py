import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

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
