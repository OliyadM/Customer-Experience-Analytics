-- Create Bank Table
CREATE TABLE Banks (
    bank_id INT PRIMARY KEY,
    bank_name VARCHAR2(255) NOT NULL
);

-- Create Reviews Table
CREATE TABLE Reviews (
    review_id INT PRIMARY KEY,
    review_text CLOB NOT NULL,
    rating INT,
    date DATE,
    bank_id INT,
    vader_sentiment FLOAT,
    vader_sentiment_label VARCHAR2(10),
    theme VARCHAR2(50),
    FOREIGN KEY (bank_id) REFERENCES Banks(bank_id)
);
