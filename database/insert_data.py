import oracledb
import pandas as pd

# Oracle Database Connection details
dsn = oracledb.makedsn('localhost', 1521, service_name='XE')
connection = oracledb.connect(user="your_user", password="your_password", dsn=dsn)

# Load the cleaned reviews data
df_reviews = pd.read_csv('../data/processed_reviews_all_banks.csv')

# Insert bank data into the 'Banks' table
banks = df_reviews['bank'].unique()
cursor = connection.cursor()
for i, bank in enumerate(banks, start=1):
    cursor.execute("INSERT INTO Banks (bank_id, bank_name) VALUES (:1, :2)", (i, bank))
connection.commit()

# Insert review data into the 'Reviews' table
for _, row in df_reviews.iterrows():
    cursor.execute("""
        INSERT INTO Reviews (review_id, review_text, rating, date, bank_id, vader_sentiment, vader_sentiment_label, theme)
        VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6, :7, :8)
    """, (row['review_id'], row['review'], row['rating'], row['date'], banks.tolist().index(row['bank']) + 1, 
          row['vader_sentiment'], row['vader_sentiment_label'], row['theme']))

# Commit the transaction
connection.commit()

# Close the connection
cursor.close()
connection.close()

print("Data inserted successfully!")
