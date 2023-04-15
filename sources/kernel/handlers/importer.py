
# Importing module for handling another modules import
import importlib

# Importing module for working with OS API
import os
# Importing module for working with ENV files
import dotenv

# Looking for ENV configuration file
dotenv_config = dotenv.find_dotenv()
# Loading variables from ENV configuration file
dotenv.load_dotenv(dotenv_config)

# Setting variable for configuring PROJECT_MODE (i.e. DEBUG or RELEASE)
PROJECT_CONFIG = os.environ.get("PROJECT_CONFIG")

def import_module(module_name, package_name = None):
    try:
        module = importlib.import_module(module_name, package_name)
    except ImportError:
        print(f"Error: unable to import module {module_name}!")
    else:
        if PROJECT_CONFIG == "DEBUG":
            print(f"Successfully imported module {module_name}!")