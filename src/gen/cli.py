"""
CLI entry point for the gen-cli package.
"""

import argparse
import os
import sys
from importlib.metadata import version

from gen.commands import doctor, helper, list_, template
from gen.config import EXTENSION_MAP


def get_version() -> str:
    """
    Returns the version of the gen-cli package.
    """
    return version("gen-cli")


def handle_filename(
    filename: str, dryrun: bool = False, overwrite: bool = False
) -> None:
    """
    Handles the filename argument.

    :param filename: The filename to handle.
    :param dryrun: Whether to dryrun the command.
    :param overwrite: Whether to overwrite the file.
    """
    name, ext = os.path.splitext(filename)
    if not ext:
        raise argparse.ArgumentTypeError(
            "Filename must have an extension (e.g. main.py)"
        )

    if ext not in EXTENSION_MAP:
        print(f"Template for {ext} does not exist.")
        list_.list_langtemplates()
        return

    template.gen_langtemplate(name, ext, dryrun=dryrun, overwrite=overwrite)


def handle_filename(
    filename: str, dryrun: bool = False, overwrite: bool = False
) -> None:
    """
    Handles the filename argument.

    :param filename: The filename to handle.
    :param dryrun: Whether to dryrun the command.
    :param overwrite: Whether to overwrite the file.
    """
    name, ext = os.path.splitext(filename)
    if not ext:
        raise argparse.ArgumentTypeError(
            "Filename must have an extension (e.g. main.py)"
        )

    if ext not in EXTENSION_MAP:
        print(f"Template for {ext} does not exist.")
        list_.list_langtemplates()
        return

    template.gen_langtemplate(name, ext, dryrun=dryrun, overwrite=overwrite)


def parse_filename_mode() -> None:
    """
    Parses the filename mode.
    """
    parser = argparse.ArgumentParser(prog="gen")
    parser.add_argument("filename")
    parser.add_argument("--dryrun", action="store_true", default=False)
    parser.add_argument("--overwrite", action="store_true", default=False)
    args = parser.parse_args()
    handle_filename(args.filename, dryrun=args.dryrun, overwrite=args.overwrite)


def parse_command_mode() -> None:
    """
    Parses the command mode.
    """
    parser = argparse.ArgumentParser(
        prog="gen",
        add_help=True,
        description="Gen-CLI — Generate boilerplate files and project templates",
        epilog="Use 'gen <command> --help' for more info on a command.",
    )
    parser.add_argument("-v", "--version", action="store_true", help="Show version")

    subparsers = parser.add_subparsers(dest="command", metavar="<command>")

    lang_parser = subparsers.add_parser("lang", help="Language operations")
    lang_parser.add_argument(
        "--list", action="store_true", help="List language templates"
    )

    subparsers.add_parser("list", help="List all templates")

    tree_parser = subparsers.add_parser("tree", help="Show directory tree")
    tree_parser.add_argument("path", nargs="?", default=None, help="Directory path")
    tree_parser.add_argument("-r", action="store_true", help="Recursive (all levels)")
    tree_parser.add_argument(
        "-d", type=int, default=None, dest="depth", help="Depth level"
    )

    template_parser = subparsers.add_parser("template", help="Template operations")
    template_parser.add_argument(
        "--list", action="store_true", help="List framework templates"
    )

    new_parser = subparsers.add_parser("new", help="Generate a new project")
    new_parser.add_argument("dir_name", help="Project name")
    new_parser.add_argument("--lang", required=True, help="Programming language")
    new_parser.add_argument("--template", required=True, help="Framework or template")
    new_parser.add_argument(
        "--dryrun", action="store_true", help="Preview without creating files"
    )

    subparsers.add_parser("doctor", help="Check environment and configuration")

    args = parser.parse_args()

    if args.version:
        print(f"gen-cli version {get_version()}")
        return

    if not args.command:
        parser.print_help()
        return

    if args.command == "lang":
        if args.list:
            list_.list_langtemplates()
        else:
            helper.concise_help()

    elif args.command == "list":
        list_.list_langtemplates()
        list_.list_framtemplates()

    elif args.command == "tree":
        depth = 1
        path = os.getcwd()

        if args.r:
            depth = None
        elif args.depth:
            depth = args.depth
        elif args.path and args.path.startswith("-"):
            try:
                depth = int(args.path[1:])
            except ValueError:
                pass

        if args.path and not args.path.startswith("-"):
            if os.path.isdir(args.path):
                path = args.path
            else:
                path = args.path

        list_.tree_view(path=path, depth=depth)

    elif args.command == "template":
        if args.list:
            list_.list_framtemplates()
        else:
            helper.concise_help()

    elif args.command == "new":
        flag = "--dryrun" if args.dryrun else None
        template.gen_framtemplate(args.dir_name, args.lang, args.template, flag=flag)

    elif args.command == "doctor":
        doctor.run_doctor()

    else:
        helper.concise_help()


def main() -> None:
    """
    Main function.
    """
    if len(sys.argv) > 1 and "." in sys.argv[1]:
        parse_filename_mode()
    else:
        parse_command_mode()


if __name__ == "__main__":
    main()
