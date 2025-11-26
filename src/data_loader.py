import pandas as pd
import os

def load_data(filepath):
    """
    Loads the customer shopping behavior dataset.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} was not found.")
    
    df = pd.read_csv(filepath)
    return df

def clean_data(df):
    """
    Performs basic data cleaning and preprocessing.
    """
    # Standardize column names to snake_case
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    
    # Handle missing values (if any) - based on previous analysis, Review Rating had missing values
    if 'review_rating' in df.columns:
        df['review_rating'] = df['review_rating'].fillna(df['review_rating'].mean())

    return df

def get_data():
    """
    Wrapper function to load and clean data from the default location.
    """
    # Assuming the script is run from the root directory
    filepath = os.path.join('data', 'customer_shopping_behavior.csv')
    df = load_data(filepath)
    df = clean_data(df)
    return df
