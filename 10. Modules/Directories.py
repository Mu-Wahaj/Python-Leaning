# buitin durectories are special directories that are automatically created by Python when you create a new project or module. They are used to organize your code and make it easier to manage. Some common built-in directories include: you can search on the web for "python built-in directories" to find a list of these directories and their purposes. Here are some examples of built-in directories in Python:
from pathlib import Path
# The current working directory
current_directory = Path("../Package/ecommerce")
print(f"Current working directory: {current_directory}")
print(Path.exists(current_directory))  # Output: True (if the directory exists)
print(Path.is_dir(current_directory))  # Output: True (if it's a directory)
print(Path.is_file(current_directory))  # Output: False (since it's a directory, not a file)
print(Path.cwd())  # Output: The current working directory of the script
print(Path.home())  # Output: The home directory of the current user

path= Path("../../Mosh")
print(path)  # Output: ../../Mosh
print(path.exists())  # Output: True (if the path exists)
print(path.resolve())  # Output: The absolute path to the Mosh directory
for item in path.glob("*.py"):
    print(item)  # Output: List of Python files in the specified path
    
    
#there aorher sevral built-in directories in Python that are used for specific purposes, such as the site-packages directory for third-party packages, the __pycache__ directory for compiled bytecode files, and the __init__.py file for defining packages. These directories help to keep your code organized and make it easier to manage dependencies and modules in your Python projects.