# This project aggregates news from different sources and analyzes them.
# Implement the code here

import requests
from textblob import TextBlob

def fetch_news(api_url):
    response = requests.get(api_url)
    return response.json().get('articles', [])

def analyze_sentiment(article_text):
    analysis = TextBlob(article_text)
    return 'Positive' if analysis.sentiment.polarity > 0 else 'Negative'

# Example usage
news_api_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=your_api_key'
news_articles = fetch_news(news_api_url)

for article in news_articles:
    sentiment = analyze_sentiment(article['title'])
    print(f"Title: {article['title']}\nSentiment: {sentiment}\n")
