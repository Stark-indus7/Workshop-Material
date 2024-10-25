# This project translates text between languages and caches results for faster access.
# Implement the code here

from googletrans import Translator
from cachetools import TTLCache

translator = Translator()
cache = TTLCache(maxsize=100, ttl=86400)  # 1-day cache

def translate_text(text, target_lang):
    cache_key = (text, target_lang)
    
    if cache_key in cache:
        print("Using cached translation.")
        return cache[cache_key]
    
    translation = translator.translate(text, dest=target_lang).text
    cache[cache_key] = translation
    return translation

# Example usage
translated_text = translate_text("Hello, how are you?", "es")
print(translated_text)
