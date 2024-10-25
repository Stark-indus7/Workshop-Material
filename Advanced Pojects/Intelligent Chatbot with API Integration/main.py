# This project creates a chatbot that interacts with an API for responses.
# Implement the code here

import requests

def fetch_answer(query):
    api_url = f"https://api.example.com/chatbot?query={query}"
    response = requests.get(api_url)
    return response.json().get("answer")

if __name__ == "__main__":
    while True:
        query = input("You: ")
        if query.lower() in ['exit', 'quit']:
            break
        answer = fetch_answer(query)
        print(f"Bot: {answer}")
