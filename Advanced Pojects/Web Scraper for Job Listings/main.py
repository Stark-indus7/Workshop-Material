# This project scrapes job listings from websites and stores them in a file.
# Implement the code here

import requests
from bs4 import BeautifulSoup
import csv

def scrape_jobs(url):
    jobs = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for job_card in soup.find_all('div', class_='job-card'):
        title = job_card.find('h2', class_='title').text.strip()
        company = job_card.find('div', class_='company').text.strip()
        location = job_card.find('div', class_='location').text.strip()
        jobs.append([title, company, location])
    
    return jobs

def save_to_csv(jobs, filename='job_listings.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Company', 'Location'])
        writer.writerows(jobs)
    print(f'Saved {len(jobs)} job listings to {filename}')

# Example usage
url = 'https://www.example.com/jobs'  # Replace with actual job board URL
job_listings = scrape_jobs(url)
save_to_csv(job_listings)
