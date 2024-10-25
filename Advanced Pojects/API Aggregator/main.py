# This project aggregates data from multiple APIs into a single output.
# Implement the code here

import requests

def fetch_api_data(api_urls):
    aggregated_data = {}
    for api_name, api_url in api_urls.items():
        response = requests.get(api_url)
        aggregated_data[api_name] = response.json()
    return aggregated_data

if __name__ == "__main__":
    api_urls = {
        "API 1": "https://api.example.com/data1",
        "API 2": "https://api.example.com/data2"
    }
    data = fetch_api_data(api_urls)
    print(data)
