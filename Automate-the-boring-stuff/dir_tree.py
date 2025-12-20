import os

for folder_name, sub_folders, file_names in os.walk(os.getcwd()):
    print(f"The current folder [{folder_name}]")

    for sub_folder in sub_folders:
        print(f"Sub folder of folder [{folder_name}]: {sub_folder}")

    for file_name in file_names:
        print(f"File inside [{folder_name}]: {file_name}")
