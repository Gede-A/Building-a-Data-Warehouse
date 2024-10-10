# preprocess.py
import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    
    # Basic text cleaning
    df['Message'] = df['Message'].str.replace(r'[^\x00-\x7F]+', '', regex=True)
    
    # Drop rows with empty messages
    df.dropna(subset=['Message'], inplace=True)
    
    return df

# Example usage:
# df_clean = clean_data('data/raw/channel1.csv')
# df_clean.to_csv('data/processed/channel1_clean.csv', index=False)
