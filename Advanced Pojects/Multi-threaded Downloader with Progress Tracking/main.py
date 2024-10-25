# This project downloads files using multiple threads and tracks progress.
# Implement the code here

import requests
from threading import Thread
import os

def download_file(url, folder):
    response = requests.get(url, stream=True)
    file_name = os.path.join(folder, url.split('/')[-1])
    
    with open(file_name, 'wb') as file:
        total_length = int(response.headers.get('content-length'))
        dl = 0
        for data in response.iter_content(chunk_size=1024):
            dl += len(data)
            file.write(data)
            done = int(50 * dl / total_length)
            print(f"\r[{('=' * done).ljust(50)}] {dl}/{total_length} bytes", end='')
    print(f"\nDownloaded {file_name}")

def download_files(urls, folder):
    threads = []
    for url in urls:
        thread = Thread(target=download_file, args=(url, folder))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Example usage
download_files(['https://example.com/file1', 'https://example.com/file2'], '/path/to/folder')
