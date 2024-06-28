# modules/data_processing.py

import pandas as pd

# Define the path to the subcategories CSV file
SUBCATEGORIES_FILE = "data/subcategories.csv"

def load_subcategories():
    """
    Load subcategories from a CSV file.
    """
    try:
        subcategories_df = pd.read_csv(SUBCATEGORIES_FILE)
    except FileNotFoundError:
        subcategories_df = pd.DataFrame(columns=['category', 'subcategory'])
    return subcategories_df

def save_subcategories(subcategories_df):
    """
    Save subcategories to a CSV file.
    """
    subcategories_df.to_csv(SUBCATEGORIES_FILE, index=False)

def get_subcategories(category):
    """
    Get subcategories based on the selected category.
    """
    subcategories_df = load_subcategories()
    return subcategories_df[subcategories_df['category'] == category]['subcategory'].tolist()

def add_subcategory(category, subcategory):
    """
    Add a new subcategory.
    """
    subcategories_df = load_subcategories()
    if subcategory not in subcategories_df[subcategories_df['category'] == category]['subcategory'].values:
        new_row = pd.DataFrame([[category, subcategory]], columns=['category', 'subcategory'])
        subcategories_df = pd.concat([subcategories_df, new_row], ignore_index=True)
        save_subcategories(subcategories_df)
        return True
    return False

def delete_subcategory(category, subcategory):
    """
    Delete an existing subcategory.
    """
    subcategories_df = load_subcategories()
    subcategories_df = subcategories_df.drop(subcategories_df[(subcategories_df['category'] == category) & (subcategories_df['subcategory'] == subcategory)].index).reset_index(drop=True)
    save_subcategories(subcategories_df)

def generate_summaries(data):
    """
    Generate monthly and weekly summaries.
    """
    data['date'] = pd.to_datetime(data['date'], format='%d-%m-%Y')
    data['amount'] = pd.to_numeric(data['amount'])
    
    # Group by month and sum the 'amount' column
    monthly_summary = data.groupby(data['date'].dt.to_period('M'))['amount'].sum()
    
    # Group by week and sum the 'amount' column
    weekly_summary = data.groupby(data['date'].dt.to_period('W'))['amount'].sum()
    
    return monthly_summary, weekly_summary