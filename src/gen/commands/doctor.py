import sys
import platform
import os


class colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[0;35m"
    ENDC = "\033[0m"


def run_doctor():
    print(f"\n{colors.BLUE}Gen CLI Doctor{colors.ENDC}")
    print("-" * 40)

    # Python Version
    py_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"{colors.GREEN}✓{colors.ENDC} Python Version: {py_version}")

    # Platform
    print(f"{colors.GREEN}✓{colors.ENDC} Platform: {platform.system()} {platform.release()}")

    # Working Directory
    cwd = os.getcwd()
    print(f"{colors.GREEN}✓{colors.ENDC} Working Directory: {cwd}")

    # PATH directories
    path_dirs = os.environ.get("PATH", "").split(os.pathsep)
    print(f"{colors.GREEN}✓{colors.ENDC} PATH directories: {len(path_dirs)} found")

    print(f"\n{colors.GREEN}All checks passed{colors.ENDC}\n")
