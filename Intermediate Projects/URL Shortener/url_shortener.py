# This is the main Python file for the URL Shortener project.
import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

url = input("Enter URL to shorten: ")
print("Shortened URL:", shorten_url(url))
