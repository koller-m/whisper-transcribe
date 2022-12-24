import os

# Rename files in output dir starting from 1

# Set the dir where the files are located
directory = "/path/to/directory"

# Get a list of all .txt files in the directory
files = [f for f in os.listdir(directory) if f.endswith(".txt")]

# Sort the list of files
files.sort()

# Iterate through the list of files
for i, file in enumerate(files):
    # Get the file path
    file_path = os.path.join(directory, file)
    # Split the file name and extension
    file_name, file_ext = os.path.splitext(file)
    # Create the new file name
    new_file_name = str(i+1)
    # Create the new file path
    new_file_path = os.path.join(directory, new_file_name + file_ext)
    # Rename the file
    os.rename(file_path, new_file_path)