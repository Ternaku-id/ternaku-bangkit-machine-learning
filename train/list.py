import os

def list_folders(directory):
    folders = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            folders.append(item)
    return folders

directory_path = 'D:\Bangkit 2023\CAPSTONE'

folder_names = list_folders(directory_path)

for folder_name in folder_names:
    print(folder_name)
