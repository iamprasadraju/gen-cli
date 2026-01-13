import os
from importlib import resources
from pathlib import Path

# Get the current working directory
current_dir = os.getcwd()


# Get the path to the templates directory in the "gen" module
templates_path = resources.files("gen.templates")


# Prints the Language Templates
def list_langtemplates(EXTENSION_MAP):
    print("Available Language Templates: ")
    for lang in EXTENSION_MAP.values():
        print("   -", lang)


# Placeholder for a function that lists frame templates
def list_framtemplates(path=templates_path, prefix: str = ""):
    pass


# Prints the directory tree for the current directory
def tree_view():
    print_tree(Path(current_dir))


def print_tree(path: Path, prefix: str = "", show_files: bool = True):
    """Recursively prints the directory tree structure."""
    # Print the root folder name once
    if prefix == "":
        print(f"{path.name}/")

    # Get all items, sort them: directories first, then files
    items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        connector = "└── " if is_last else "├── "

        if item.is_dir():
            print(f"{prefix}{connector}{item.name}/")
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(item, new_prefix, show_files)
        elif show_files:
            print(f"{prefix}{connector}{item.name}")
