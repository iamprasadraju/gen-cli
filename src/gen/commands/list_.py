import os
from importlib import resources
from pathlib import Path

from gen.config import EXTENSION_MAP

# Get the current working directory
current_dir = os.getcwd()


# Get the path to the templates directory in the "gen" module
templates_path = resources.files("gen.templates")


# Prints the Language Templates
def list_langtemplates():
    print("\nList of available Language Templates: ")
    print("--------------------------------------")
    for lang in EXTENSION_MAP.values():
        print("   -", lang)
    print("")


# Placeholder for a function that lists frame templates
def list_framtemplates(path=templates_path, prefix: str = ""):
    hide_folder = ["__pycache__"]
    print("\nList of available Frameworks Templates:")
    print("--------------------------------------")
    print_tree(
        path=templates_path, show_files=False, max_depth=2, hide_folders=hide_folder
    )
    print("")


# Prints the directory tree for the current directory
def tree_view(max_depth):
    print_tree(Path(current_dir), max_depth=max_depth)


def print_tree(
    path: Path,
    prefix: str = "",
    show_files: bool = True,
    max_depth: int | None = None,
    current_depth: int = 0,
    hide_folders=[],
):
    """Recursively prints the directory tree structure with optional depth limit."""

    # Print the root folder name once
    if prefix == "":
        print(f"{path.name}/")

    # Stop if we've reached the maximum depth
    if max_depth is not None and current_depth >= max_depth:
        return

    # Get all items, sort them: directories first, then files
    items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        connector = "└── " if is_last else "├── "

        if item.is_dir() and item.name not in hide_folders:
            print(f"{prefix}{connector}{item.name}/")
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(
                item,
                new_prefix,
                show_files,
                max_depth,
                current_depth + 1,
            )
        elif show_files:
            print(f"{prefix}{connector}{item.name}")
