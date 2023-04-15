
# Importing module for working with JSON files
import json

def get_file_content(json_file):
    # Define variable that will contain this JSON file content
    json_content = 0

    # Here we'll open our file for reading
    with open(json_file, "r") as json_handler:
        # And store all contents to pre-defined variable
        json_content = json.load(json_handler)

    # Now we should return JSON file content
    return json_content
