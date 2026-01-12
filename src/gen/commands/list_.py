import os
from importlib import resources
from pathlib import Path

templates_path = resources.files("gen.templates")


# Prints the Language Templetes
def list_langtemplates():
    print_tree(templates_path, "", show_files=False)


def list_framtemplates():
    pass


def print_tree(path: Path, prefix: str = "", show_files: bool = True):
    """Recursively prints the directory tree structure."""
    if prefix == "":
        print(f"{path.name}/")  # Print the root folder name once

    # Get all items, sort them (optional), directories first
    items = sorted(list(path.iterdir()), key=lambda x: (not x.is_dir(), x.name.lower()))

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        connector = "└── " if is_last else "├── "

        if item.is_dir():
            print(f"{prefix}{connector}{item.name}/")
            # Recurse into subdirectory
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(item, new_prefix, show_files)
        elif show_files:
            print(f"{prefix}{connector}{item.name}")


# print_tree(templates_path)
