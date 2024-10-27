import os

# Get the current working directory
current_directory = os.getcwd()
print(current_directory)

# Create an empty list called files_info to store your dictionaries
files_info = []

def list_files_in_directory(directory='.'):
    # Create an empty list to store dictionaries
    files_info = []
    
    # Loop through files in the directory
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        # Check if it's a file and add its info to the list
        if os.path.isfile(file_path):
            file_info = {
                'name': file,
                'size': os.path.getsize(file_path),
                'path': file_path
            }
            files_info.append(file_info)
    
    return files_info

# Create the list of files in the directory
file_list = list_files_in_directory()

# Print each file's details in a vertical list format
for file in file_list:
    print("Name:", file['name'])
    print("Size:", file['size'])
    print("Path:", file['path'])
