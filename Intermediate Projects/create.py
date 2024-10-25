import os
import shutil

# Define the base folder and the project details
base_folder = "D:\\Workshop\\Workshop-Material\\Intermediate Projects"
projects = {
    "Weather Dashboard": "weather_dashboard.py",
    "To-Do List Application with SQLite": "todo_list.py",
    "Personal Expense Tracker": "expense_tracker.py",
    "File Organizer Script": "file_organizer.py",
    "Contact Book with Search Functionality": "contact_book.py",
    "Quiz Application with Timer": "quiz_app.py",
    "Image Downloader with URL Input": "image_downloader.py",
    "URL Shortener": "url_shortener.py",
    "Password Generator and Manager": "password_manager.py",
    "Automated Email Sender": "email_sender.py",
    "Data Visualization Dashboard": "data_dashboard.py",
    "Pomodoro Timer with Notifications": "pomodoro_timer.py",
    "Recipe Finder with Web Scraping": "recipe_finder.py",
    "Image Resizer and Converter": "image_resizer.py",
    "Text-Based Adventure Game": "adventure_game.py",
    "Personal Diary Application with Encryption": "diary_application.py"
}

# Example contents for main.py, README.md, and certificate.txt
readme_content = """
# {project_name}
This is a Python project that implements {description}.
"""

certificate_content = """
Congratulations on completing the {project_name} project!
This certificate recognizes your achievement in building this Python application.
"""

# Create the base folder
if not os.path.exists(base_folder):
    os.mkdir(base_folder)
    print(f"Created base folder: {base_folder}")

# Iterate through the project dictionary and create folders, main.py, README.md, and certificate.txt
for project_name, file_name in projects.items():
    # Create project folder
    project_folder = os.path.join(base_folder, project_name)
    if not os.path.exists(project_folder):
        os.mkdir(project_folder)
        print(f"Created project folder: {project_folder}")
    
    # Create main.py file
    main_file_path = os.path.join(project_folder, file_name)
    with open(main_file_path, "w") as main_file:
        main_file.write(f"# This is the main Python file for the {project_name} project.\n")
        print(f"Created {file_name} in {project_folder}")
    
    # Create README.md file
    readme_file_path = os.path.join(project_folder, "README.md")
    with open(readme_file_path, "w") as readme_file:
        readme_file.write(readme_content.format(project_name=project_name, description="a sample description"))
        print(f"Created README.md in {project_folder}")
    
    # Create certificate.txt file
    certificate_file_path = os.path.join(project_folder, "certificate.txt")
    with open(certificate_file_path, "w") as cert_file:
        cert_file.write(certificate_content.format(project_name=project_name))
        print(f"Created certificate.txt in {project_folder}")

print("\nAll project folders and files have been created successfully!")