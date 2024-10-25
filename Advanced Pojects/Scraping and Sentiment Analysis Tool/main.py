# This project scrapes data and performs sentiment analysis on the content.
# Implement the code here

from bs4 import BeautifulSoup
import requests
from textblob import TextBlob

def scrape_reviews(url):
    reviews = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for review in soup.find_all('div', class_='review'):
        text = review.find('p').text.strip()
        reviews.append(text)
    
    return reviews

def analyze_sentiment(reviews):
    for review in reviews:
        analysis = TextBlob(review)
        sentiment = 'Positive' if analysis.sentiment.polarity > 0 else 'Negative'
        print(f"Review: {review}\nSentiment: {sentiment}\n")

# Example usage
url = 'https://www.example.com/reviews'  # Replace with actual URL
reviews = scrape_reviews(url)
analyze_sentiment(reviews)
