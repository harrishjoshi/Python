#! python3

# backup_to_zip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import os
import sys
import zipfile


def backup_to_zip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)  # make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exist
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zip_filename):
            break
        number = number + 1

    # Create the zip file.
    print("Creating %s..." % (zip_filename))
    backup_zip = zipfile.ZipFile(zip_filename, "w")

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print("Adding files in %s..." % (foldername))
        # Add the current folder to the ZIP file.
        backup_zip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            # Skip existing backup files
            if filename.startswith(
                os.path.basename(folder) + "_"
            ) and filename.endswith(".zip"):
                continue

            backup_zip.write(os.path.join(foldername, filename))

    backup_zip.close()
    print("Backup completed.")


if len(sys.argv) < 2:
    print("Usage: python backup_to_zip.py [folder] - backup folder to zip file")
    sys.exit()

folder = sys.argv[1]
if not os.path.isdir(folder):
    print(f"Folder name [{folder}] does not exist.")
    sys.exit()

backup_to_zip(folder)
