from importlib import resources
from pathlib import Path

from gen.paths import langs, frameworks


class colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[0;35m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ENDC = "\033[0m"


def print_list(title, items):
    print(f"\n{title}")
    print("-" * len(title))
    for item in items:
        print(f"  • {item}")
    print()


def tree_view(path=".", depth=2, show_hidden=False, prefix="", is_last=True):
    root = Path(path)
    if not root.exists():
        print(f"Path not found: {path}")
        return

    root_name = root.name if root.name else root.resolve().name
    print(f"{colors.BOLD}{colors.BLUE}{root_name}{colors.ENDC}")

    _tree_recursive(root, depth, show_hidden, prefix="", is_last=True)


def _tree_recursive(root, depth, show_hidden, prefix, is_last):
    if depth is not None and depth <= 0:
        return

    entries = sorted(root.iterdir())
    if not show_hidden:
        entries = [e for e in entries if not e.name.startswith(".")]

    for i, entry in enumerate(entries):
        is_last_entry = i == len(entries) - 1
        connector = f"{colors.DIM}{'└── ' if is_last_entry else '├── '}{colors.ENDC}"

        if entry.name.startswith("."):
            print(f"{prefix}{connector}{colors.DIM}{entry.name}{colors.ENDC}")
        elif entry.is_dir():
            print(f"{prefix}{connector}{colors.BOLD}{colors.BLUE}{entry.name}{colors.ENDC}")
        else:
            print(f"{prefix}{connector}{colors.GREEN}{entry.name}{colors.ENDC}")

        if entry.is_dir():
            extension = f"{colors.DIM}{'    ' if is_last_entry else '│   '}{colors.ENDC}"
            new_depth = depth - 1 if depth is not None else None
            if new_depth is None or new_depth > 0:
                _tree_recursive(entry, new_depth, show_hidden, prefix + extension, is_last_entry)


def print_tree_structure(template_dir, project_name):
    root = Path(template_dir)
    if not root.exists():
        print(f"Template not found: {template_dir}")
        return

    print(f"{colors.BOLD}{colors.BLUE}{project_name}{colors.ENDC}")
    _print_tree_recursive(root, prefix="", is_last=True)


def _print_tree_recursive(root, prefix, is_last):
    entries = sorted(root.iterdir())
    for i, entry in enumerate(entries):
        is_last_entry = i == len(entries) - 1
        connector = f"{colors.DIM}{'└── ' if is_last_entry else '├── '}{colors.ENDC}"

        if entry.is_dir():
            print(f"{prefix}{connector}{colors.BOLD}{colors.BLUE}{entry.name}{colors.ENDC}")
        else:
            print(f"{prefix}{connector}{colors.GREEN}{entry.name}{colors.ENDC}")

        if entry.is_dir():
            extension = f"{colors.DIM}{'    ' if is_last_entry else '│   '}{colors.ENDC}"
            _print_tree_recursive(entry, prefix + extension, is_last_entry)


if __name__ == "__main__":
    print_list("Available Languages", langs)
    print_list("Available Frameworks", frameworks)
