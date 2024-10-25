# This is the main Python file for the File Organizer Script project.
import os
import shutil

def organize_files(folder):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Music': ['.mp3', '.wav'],
        'Videos': ['.mp4', '.mkv'],
        'Compressed': ['.zip', '.rar'],
    }

    for filename in os.listdir(folder):
        file_ext = os.path.splitext(filename)[1].lower()
        for folder_name, extensions in file_types.items():
            if file_ext in extensions:
                dest_folder = os.path.join(folder, folder_name)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(os.path.join(folder, filename), dest_folder)

folder = input("Enter folder path to organize: ")
organize_files(folder)
