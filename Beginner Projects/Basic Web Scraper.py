# Basic Web Scraper

import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    """Scrape and print all the titles (h2 tags) from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all h2 tags
        titles = soup.find_all('h2')

        if not titles:
            print("No h2 tags found on the page.")
            return

        print(f"Found {len(titles)} h2 tags:")
        for idx, title in enumerate(titles, 1):
            print(f"{idx}. {title.get_text(strip=True)}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to run the web scraper."""
    print("Simple Web Scraper")
    url = input("Enter the URL to scrape: ").strip()

    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    scrape_titles(url)

if __name__ == "__main__":
    main()
