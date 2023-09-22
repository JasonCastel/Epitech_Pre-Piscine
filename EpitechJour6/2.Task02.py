import os

def list_files_and_directories(path):
    for root, directories, files in os.walk(path):
        for directory in directories:
            print(os.path.join(root, directory))
        for file in files:
            print(os.path.join(root, file))

# Get the current directory
current_directory = os.getcwd()

# List all files and directories recursively starting from the current directory
list_files_and_directories(current_directory)
