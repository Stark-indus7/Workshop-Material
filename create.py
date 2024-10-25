import os

# Base directory for projects
base_folder = "D:\\Workshop\\Workshop-Material\\Advanced Pojects"

# List of projects with a brief description for README.md
projects = {
    "Advanced Web Scraper with Data Storage": "This project scrapes data from the web and stores it in a database.",
    "Automated File Backup System": "This project creates automated backups of specified files.",
    "Personal Finance Manager": "This project helps manage personal finances by tracking income and expenses.",
    "API Aggregator": "This project aggregates data from multiple APIs into a single output.",
    "Real-Time Data Processing Pipeline": "This project implements a real-time data processing pipeline using queues.",
    "Chat Application Using Sockets": "This project builds a simple chat server and client using Python sockets.",
    "System Monitoring Tool": "This project monitors CPU, memory, and network usage.",
    "Automated Report Generator": "This project generates reports in PDF format from provided data.",
    "Intelligent Chatbot with API Integration": "This project creates a chatbot that interacts with an API for responses.",
    "Task Scheduler and Automation Tool": "This project schedules and executes tasks at specified times.",
    "Web Scraper for Job Listings": "This project scrapes job listings from websites and stores them in a file.",
    "Scraping and Sentiment Analysis Tool": "This project scrapes data and performs sentiment analysis on the content.",
    "Intelligent File Organizer": "This project organizes files based on their type or date.",
    "API Rate Limiter and Caching Proxy": "This project manages API request limits and implements a caching proxy.",
    "Advanced Log Analyzer": "This project analyzes logs and provides detailed reports on errors and usage.",
    "Multi-threaded Downloader with Progress Tracking": "This project downloads files using multiple threads and tracks progress.",
    "Automated Social Media Posting Tool": "This project automates social media posts based on a schedule.",
    "IoT Data Collector and Analyzer": "This project collects and analyzes IoT device data in real time.",
    "Inventory Management System": "This project manages inventory data and tracks stock levels.",
    "Machine Learning Model Trainer and API": "This project trains machine learning models and serves them via an API.",
    "News Aggregator and Analyzer": "This project aggregates news from different sources and analyzes them.",
    "Language Translator with Caching": "This project translates text between languages and caches results for faster access.",
    "Movie Recommendation System": "This project recommends movies based on user preferences and past ratings.",
    "Stock Price Alert System": "This project tracks stock prices and sends alerts when certain thresholds are met."
}

# Create the base directory if it doesn't exist
if not os.path.exists(base_folder):
    os.makedirs(base_folder)

# Function to create project folder structure
def create_project_folder(project_name, description):
    project_path = os.path.join(base_folder, project_name)
    
    # Create project folder
    os.makedirs(project_path, exist_ok=True)

    # Create main.py file with a project description comment
    main_file_path = os.path.join(project_path, "main.py")
    with open(main_file_path, "w") as main_file:
        main_file.write(f"# {description}\n")
        main_file.write("# Implement the code here\n")
    
    # Create README.md file
    readme_file_path = os.path.join(project_path, "README.md")
    with open(readme_file_path, "w") as readme_file:
        readme_file.write(f"# {project_name}\n\n")
        readme_file.write(f"## Project Description\n{description}\n\n")
        readme_file.write("### How to Run\n")
        readme_file.write("1. Install necessary dependencies.\n")
        readme_file.write("2. Run the `main.py` file.\n")
        readme_file.write("```bash\npython main.py\n```\n")
    
    # Create LICENSE.txt file
    license_file_path = os.path.join(project_path, "LICENSE.txt")
    with open(license_file_path, "w") as license_file:
        license_file.write("MIT License\n\n")
        license_file.write("Permission is hereby granted, free of charge, to any person obtaining a copy\n")
        license_file.write("of this software and associated documentation files (the \"Software\"), to deal\n")
        license_file.write("in the Software without restriction, including without limitation the rights\n")
        license_file.write("to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n")
        license_file.write("copies of the Software, and to permit persons to whom the Software is\n")
        license_file.write("furnished to do so, subject to the following conditions:\n\n")
        license_file.write("THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n")
        license_file.write("IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n")
        license_file.write("FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n")
        license_file.write("AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n")
        license_file.write("LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n")
        license_file.write("OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n")
        license_file.write("SOFTWARE.\n")

# Create folders and files for each project
for project, description in projects.items():
    create_project_folder(project, description)

print("Project folders with main.py, README.md, and LICENSE.txt created successfully!")
