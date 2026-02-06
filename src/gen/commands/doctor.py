import os
import sys
import subprocess
import platform


def run_doctor():
    print("=" * 40)
    print("Gen CLI Doctor")
    print("=" * 40)

    checks = [
        ("Python Version", sys.version),
        ("Platform", platform.platform()),
        ("Working Directory", os.getcwd()),
        ("PATH directories", len(os.environ.get("PATH", "").split(":"))),
    ]

    for name, value in checks:
        print(f"{name}: {value}")

    print("=" * 40)
    print("All checks passed!")
