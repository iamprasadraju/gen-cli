import argparse
import os
import sys
from importlib.metadata import version

from gen.commands import helper, list_, template, doctor
from gen.config import EXTENSION_MAP

current_dir = os.getcwd()


def get_version():
    return version("gen-cli")


def handle_filename(filename, dryrun=False, overwrite=False):
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


def parse_filename_mode():
    parser = argparse.ArgumentParser(prog="gen")
    parser.add_argument("filename")
    parser.add_argument("--dryrun", action="store_true", default=False)
    parser.add_argument("--overwrite", action="store_true", default=False)
    args = parser.parse_args()
    handle_filename(args.filename, dryrun=args.dryrun, overwrite=args.overwrite)


def parse_command_mode():
    parser = argparse.ArgumentParser(
        prog="gen",
        add_help=False,  # Manual help
    )
    parser.add_argument("-h", "--help", action="store_true")
    parser.add_argument("-v", "--version", action="store_true")

    subparsers = parser.add_subparsers(dest="command")

    # gen lang --list
    lang_parser = subparsers.add_parser("lang")
    lang_parser.add_argument("--list", action="store_true")

    list_parser = subparsers.add_parser("list")

    # gen tree -n / -r
    tree_parser = subparsers.add_parser("tree")
    tree_parser.add_argument("path", nargs="?", default=current_dir)
    tree_parser.add_argument("-r", action="store_true", help="recursive")
    tree_parser.add_argument("-d", type=int, default=1, help="depth (e.g. -d 2)")

    # gen templates --list
    template_parser = subparsers.add_parser("template")
    template_parser.add_argument("--list", action="store_true")

    # framework template generation
    new_parser = subparsers.add_parser("new")
    new_parser.add_argument("dir_name")
    new_parser.add_argument("--lang", required=True)
    new_parser.add_argument("--template", required=True)
    new_parser.add_argument("--dryrun", action="store_true")

    # gen doctor - diagnose environment
    doctor_parser = subparsers.add_parser("doctor")

    args = parser.parse_args()

    if args.help:
        helper.help()
        return

    if args.version:
        print(f"gen-cli version {get_version()}")
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
        path = os.path.join(current_dir, args.path)
        depth = None if args.r else args.d
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


def main():
    if len(sys.argv) > 1 and "." in sys.argv[1]:
        parse_filename_mode()
    else:
        parse_command_mode()


if __name__ == "__main__":
    main()
