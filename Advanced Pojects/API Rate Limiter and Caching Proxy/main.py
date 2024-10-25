# This project manages API request limits and implements a caching proxy.
# Implement the code here

import time
import requests
from cachetools import TTLCache

cache = TTLCache(maxsize=100, ttl=300)  # Cache with a TTL of 5 minutes
last_request_time = 0
REQUEST_LIMIT = 60  # 60 requests per minute

def rate_limited_request(url):
    global last_request_time
    
    if url in cache:
        print('Using cached response.')
        return cache[url]
    
    current_time = time.time()
    if current_time - last_request_time < (60 / REQUEST_LIMIT):
        time.sleep((60 / REQUEST_LIMIT) - (current_time - last_request_time))
    
    response = requests.get(url)
    cache[url] = response.text
    last_request_time = current_time
    return response.text

# Example usage
response = rate_limited_request('https://api.example.com/data')
print(response)
