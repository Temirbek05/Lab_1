# Write a Python program to list only directories, files and all directories, files in a specified path.

import os

def list_directories_files(path):
    directories = []
    files = []
    all_directories_files = []

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            directories.append(item)
            all_directories_files.append(item)
        elif os.path.isfile(item_path):
            files.append(item)
            all_directories_files.append(item)

    print("Directories:", directories)
    print("Files:", files)
    print("All Directories and Files:", all_directories_files)

path = input("Enter your path: ")
list_directories_files(path)
