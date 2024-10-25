# This is the main Python file for the Recipe Finder with Web Scraping project.
import requests
from bs4 import BeautifulSoup

def find_recipes(ingredient):
    url = f"https://www.allrecipes.com/search/results/?wt={ingredient}&sort=re"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    recipes = soup.find_all('h3', class_='fixed-recipe-card__h3')

    for index, recipe in enumerate(recipes[:5], start=1):
        title = recipe.get_text(strip=True)
        print(f"{index}. {title}")

ingredient = input("Enter main ingredient: ")
find_recipes(ingredient)
