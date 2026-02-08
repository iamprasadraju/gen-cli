"""
Doctor command for gen-cli.
"""

import os
import platform
import sys
from importlib.metadata import import_module, version
from importlib.resources import files


class Colors:
    """
    Colors for the terminal.
    """

    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    ENDC = "\033[0m"


def check_feature(name: str, func: callable) -> tuple[bool, str | None]:
    """
    Checks if a feature is working.

    :param name: The name of the feature.
    :param func: The function to check.
    :return: A tuple of (success, error).
    """
    try:
        func()
        return True, None
    except Exception as e:
        return False, str(e)


def run_doctor() -> None:
    """
    Runs the doctor command.
    """
    print("=" * 50)
    print(f"{Colors.BLUE}Gen CLI Doctor{Colors.ENDC}")
    print("=" * 50)

    checks = [
        ("Python Version", lambda: sys.version.split()[0]),
        ("Platform", lambda: platform.platform()),
        ("Working Directory", lambda: os.getcwd()),
        ("PATH directories", lambda: len(os.environ.get("PATH", "").split(":"))),
    ]

    print(f"\n{Colors.BLUE}Environment Checks:{Colors.ENDC}")
    print("-" * 50)
    for name, func in checks:
        try:
            result = func()
            print(f"{Colors.GREEN}OK{Colors.ENDC} {name}: {result}")
        except Exception as e:
            print(f"{Colors.RED}FAIL{Colors.ENDC} {name}: Error - {e}")

    print(f"\n{Colors.BLUE}Feature Checks:{Colors.ENDC}")
    print("-" * 50)

    feature_checks = [
        ("gen --version", lambda: version("gen-cli")),
        ("gen --help", lambda: import_module("gen.cli")),
        ("gen list", lambda: import_module("gen.commands.list_")),
        ("gen tree", lambda: import_module("gen.commands.list_")),
        ("gen new", lambda: import_module("gen.commands.template")),
        ("gen doctor", lambda: import_module("gen.commands.doctor")),
        ("Templates", lambda: files("gen.templates")),
    ]

    working = 0
    not_working = 0

    for name, func in feature_checks:
        success, error = check_feature(name, func)
        if success:
            print(f"{Colors.GREEN}OK{Colors.ENDC} {name}")
            working += 1
        else:
            print(f"{Colors.RED}FAIL{Colors.ENDC} {name}: {error}")
            not_working += 1

    print(f"\n{Colors.BLUE}Summary:{Colors.ENDC}")
    print("-" * 50)
    print(f"{Colors.GREEN}Working:{Colors.ENDC} {working}")
    print(f"{Colors.RED}Not Working:{Colors.ENDC} {not_working}")

    print("\n" + "=" * 50)
    if not_working == 0:
        print(f"{Colors.GREEN}All checks passed!{Colors.ENDC}")
    else:
        print(f"{Colors.YELLOW}Some features need attention.{Colors.ENDC}")
    print("=" * 50)
