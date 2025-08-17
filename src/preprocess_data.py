import pandas as pd

# Function to preprocess reviews
def preprocess_data(bank_name):
    # Load the raw review data
    df = pd.read_csv(f'data/raw_reviews_{bank_name}.csv')

    # Remove duplicates based on the 'review' column (keeping the first occurrence)
    df.drop_duplicates(subset=['review'], keep='first', inplace=True)

    # Handle missing data: Fill missing reviews with "No Review" and ratings with 0
    df['review'].fillna('No Review', inplace=True)
    df['rating'].fillna(0, inplace=True)
    df['date'].fillna('2023-01-01', inplace=True)  # Default to a placeholder date if missing

    # Normalize dates: Convert to YYYY-MM-DD format
    df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')

    # Save the cleaned data to CSV
    df.to_csv(f'data/cleaned_reviews_{bank_name}.csv', index=False)
    print(f'Preprocessing completed for {bank_name}. Cleaned data saved to data/cleaned_reviews_{bank_name}.csv')

# Preprocess data for each bank
preprocess_data('CBE')
preprocess_data('BOA')
preprocess_data('Dashen')
