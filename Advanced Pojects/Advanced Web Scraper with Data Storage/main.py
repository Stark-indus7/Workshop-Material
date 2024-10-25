# This project scrapes data from the web and stores it in a database.
# Implement the code here

import requests
from bs4 import BeautifulSoup
import sqlite3

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = [a['href'] for a in soup.find_all('a', href=True)]
    return data

def store_data(data):
    conn = sqlite3.connect('web_scraper.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS scraped_data (id INTEGER PRIMARY KEY, link TEXT)''')
    for link in data:
        cursor.execute('''INSERT INTO scraped_data (link) VALUES (?)''', (link,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    data = scrape_data(url)
    store_data(data)
    print("Data stored successfully.")
