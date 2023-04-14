
# Importing module for working with OS API
import os

def get_files_list(directory_path):
    # Define variable that will contain list of all files
    # Stored under the specified directory
    files_list = [ ]

    # Get list of all items under this directory 
    elements_list = os.listdir(directory_path)

    # Handling each element to check
    for element in elements_list:
        # If current handling element is a file
        if os.isfile(element):
            # Add this element to pre-defined list of files
            files_list.append(os.path.join(elements_list, element))

    # Finally we can return list of all files in this direcrory
    return files_list