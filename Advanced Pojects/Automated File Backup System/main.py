# This project creates automated backups of specified files.
# Implement the code here

import shutil
import os
from datetime import datetime

def backup_file(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = shutil.copy2(source, os.path.join(destination, f"{os.path.basename(source)}_{timestamp}"))
    return backup_file

if __name__ == "__main__":
    source = input("Enter the file path to backup: ")
    destination = input("Enter the destination folder: ")
    backup_path = backup_file(source, destination)
    print(f"Backup created at {backup_path}")
