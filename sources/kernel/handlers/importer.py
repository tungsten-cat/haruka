
import importlib

def import_module(module_name, package_name = None):
    try:
        module = importlib.import_module(module_name, package_name)
    except ImportError:
        print(f"Error: unable to import module {module_name}!")