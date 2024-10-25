# This project organizes files based on their type or date.
# Implement the code here

import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_ext = filename.split('.')[-1]
            target_dir = os.path.join(directory, file_ext + "_files")
            
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            
            shutil.move(filepath, os.path.join(target_dir, filename))

# Example usage
organize_files('/path/to/directory')
