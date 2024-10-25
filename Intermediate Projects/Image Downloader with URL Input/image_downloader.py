# This is the main Python file for the Image Downloader with URL Input project.
import requests

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Image saved as {filename}")
    else:
        print("Failed to download image.")

url = input("Enter image URL: ")
filename = input("Enter filename to save as: ")
download_image(url, filename)
