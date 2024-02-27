import os
import shutil

# Get Current Directory
print('Current Dir:', os.getcwd())

# list all sub-directories
print(os.listdir())

# change directory
os.chdir(os.getcwd() + '\\Tutorial\\Files')
print('Current Dir:', os.getcwd())

# Making a New Directory
os.mkdir('test')
print(os.listdir())

# Renaming a Directory or a File
# rename a directory
os.rename('test', 'test1')
print(os.listdir())

# Removing Directory or File in
# delete test1 directory
os.rmdir("test1")

"""
delete "mydir" directory and all of its contents
"""
# make "mydir" directory
os.mkdir('mydir')

# Change current dir to "mydir"
os.chdir(os.getcwd() + '\\mydir')

# Create test.txt file inside "mydir"
open("test.txt", "x")

# Get the current working directory
current_directory = os.getcwd()

# Get the parent directory
parent_directory = os.path.dirname(current_directory)

# Change to the parent directory
os.chdir(parent_directory)

# Delete 
shutil.rmtree("mydir")