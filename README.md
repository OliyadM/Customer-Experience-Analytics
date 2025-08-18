# Customer Experience Analytics for Mobile Banking Apps

## Project Overview

This project analyzes user reviews for three Ethiopian mobile banking apps: **Commercial Bank of Ethiopia (CBE)**, **Bank of Abyssinia (BOA)**, and **Dashen Bank**. It aims to provide insights into customer satisfaction by analyzing sentiments and extracting themes from the reviews, followed by providing actionable recommendations to enhance user experience.

The analysis focuses on:
- **Sentiment Analysis**: Using VADER to classify reviews as positive, negative, or neutral.
- **Thematic Analysis**: Grouping reviews into themes (e.g., app performance, UI issues).
- **Insights and Recommendations**: Visualizing results and suggesting improvements.

---

## Project Structure

CUSTOMER-EXPERIENCE-ANALYTICS/
├── .gitignore # Gitignore file
├── README.md # Project documentation
├── requirements.txt # List of required Python packages
├── data/ # Folder containing scraped and cleaned reviews
│ └── (CSV files for reviews) # Processed data files
├── database/ # SQL scripts for Oracle DB setup
│ ├── create_tables.sql # SQL script for creating tables
│ └── insert_data.py # Script to insert data into Oracle DB
├── notebooks/ # Jupyter Notebooks for analysis and insights
│ ├── insights_and_recommendations.ipynb # Insights, recommendations, and visualizations
│ └── sentiment_and_thematic_analysis.ipynb # Sentiment and thematic analysis
└── src/ # Source code for data scraping and preprocessing
├── preprocess_data.py # Data preprocessing script
└── scrape_review.py # Web scraping script for Google Play Stor

---

## Key Features

- **Data Collection**: Scraped reviews from Google Play Store for three banks (CBE, BOA, Dashen).
- **Sentiment Analysis**: VADER Sentiment Analyzer to classify reviews into positive, neutral, and negative categories.
- **Thematic Analysis**: TF-IDF vectorization and KMeans clustering to extract themes from the reviews.
- **Oracle Database**: Store cleaned data into an Oracle database for further querying.
- **Visualization**: Use of Matplotlib and Seaborn to visualize sentiment trends, theme distributions, and keyword clouds.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/OliyadM/B5W2-Customer-Experience-Analytics.git
2. Navigate to the project directory:

    cd Customer-Experience-Analytics

3. install the required Python libraries

    pip install -r requirements.txt

## Usage
1. Data Scraping:

To scrape the Google Play reviews for the three banks:

python src/scrape_review.py

2. Data Preprocessing:

To preprocess and clean the scraped data:

python src/preprocess_data.py

Sentiment and Thematic Analysis:

3. Run the Jupyter notebook for sentiment and thematic analysis:

jupyter notebook notebooks/sentiment_and_thematic_analysis.ipynb

4. Insights and Recommendations:

Run the Jupyter notebook for generating insights and recommendations:

jupyter notebook notebooks/insights_and_recommendations.ipynb