from google_play_scraper import reviews
import csv

# Function to scrape reviews for a specific app (bank)
def scrape_reviews(bank_name, app_package_name, num_reviews=400):
    reviews_data = []
    
    # Initial request to fetch reviews
    result, next_cursor = reviews(app_package_name, count=100, lang='en', country='US')
    reviews_data.extend(result)
    
    # Fetch additional reviews if needed
    while len(reviews_data) < num_reviews:
        result, next_cursor = reviews(app_package_name, count=100, lang='en', country='US', continuation_token=next_cursor)
        reviews_data.extend(result)
        if not next_cursor:
            break
    
    # Open CSV to write data
    with open(f'data/raw_reviews_{bank_name}.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['review', 'rating', 'date', 'bank', 'source'])

        # Write each review to the CSV
        for review in reviews_data:
            review_text = review['content']  # Extract the review content
            rating = review['score']         # Extract the review rating
            date = review['at']              # Extract the review date
            source = 'Google Play'           # Static as we are scraping from Google Play
            writer.writerow([review_text, rating, date, bank_name, source])

    print(f'Scraping completed for {bank_name}. Data saved to data/raw_reviews_{bank_name}.csv')

# Scrape reviews for each bank using the correct app IDs
scrape_reviews('CBE', 'com.combanketh.mobilebanking', 400)  # Commercial Bank of Ethiopia
scrape_reviews('BOA', 'com.boa.boaMobileBanking', 400)     # Bank of Abyssinia
scrape_reviews('Dashen', 'com.dashen.dashensuperapp', 400)  # Dashen Bank
