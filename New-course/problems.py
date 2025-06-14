# Problem 1

import os

# Set the directory you want to list
directory = '/'  # Current directory. Change to your desired path

try:
    # List all files and directories
    contents = os.listdir(directory)
    print(f"Contents of '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory}' does not exist.")
except PermissionError:
    print(f"You do not have permission to access '{directory}'.")
