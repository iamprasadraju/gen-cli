import os
import sys

from gen.commands import helper, list_, template
from gen.config import EXTENSION_MAP

current_dir = os.getcwd()


def main():
    if len(sys.argv) < 2:
        helper.concise_help()
        return

    cmd = sys.argv[1]

    if cmd == "lang":
        try:
            if sys.argv[2] == "--list":
                list_.list_langtemplates()
        except:
            helper.concise_help()
    elif cmd in ["--list", "list"]:
        list_.list_langtemplates()
        list_.list_framtemplates()
    # This has to be fix (Exception Handling)
    elif cmd in ["--tree", "tree"]:
        path = current_dir
        depth = 1
        try:
            args = sys.argv[2:]  # args after tree

            if not args:
                pass

            elif len(args) == 1:
                if args[0] == "-r":
                    depth = None
                elif args[0].startswith("-"):
                    depth = int(args[0][1:])
                else:
                    path = os.path.join(current_dir, args[0])
            elif len(args) >= 2:
                path = os.path.join(current_dir, args[0])

                if args[1] == "-r":
                    depth = None
                elif args[1].startswith("-"):
                    depth = int(args[1][1:])

            list_.tree_view(path=path, depth=depth)
        except (ValueError, IndexError, OSError) as e:
            print(f"tree error: {e}")
            list_.tree_view(path=current_dir, depth=1)

    elif cmd == "template":
        try:
            if sys.argv[2] == "--list":
                list_.list_framtemplates()
        except Exception as e:
            print(e)
            helper.concise_help()

    elif cmd in ["-h", "--help", "help"]:
        helper.help()
    elif "." in cmd and len(sys.argv) >= 2:
        try:
            parts = sys.argv[1].split(".")
            if len(parts) != 2:
                raise ValueError("Filename must contain exactly one extension.")
        except IndexError:
            helper.concise_help()
            sys.exit(1)
        except ValueError as e:
            print(e)
            sys.exit(1)
        filename, extension = parts[0], "." + parts[1]
        if extension in EXTENSION_MAP.keys():
            flag = sys.argv[2] if len(sys.argv) > 2 else None
            if flag:
                template.gen_langtemplate(filename, extension, flag=flag)
            else:
                template.gen_langtemplate(filename, extension)
        else:
            print("Template does not exist.")
            list_.list_langtemplates()
    # check wheather lang has templates
    elif cmd == "new":  # gen new <project/dir> --lang<lang> --template<framework/lib>
        try:
            if (
                (len(sys.argv) >= 7)
                and (sys.argv[3] == "--lang")
                and (sys.argv[5] == "--template")
            ):
                dir_name, lang, framework_template = (
                    sys.argv[2],
                    sys.argv[4],
                    sys.argv[6],
                )

                template.gen_framtemplate(dir_name, lang, framework_template)
            else:
                helper.concise_help()
        except IndexError:
            helper.concise_help()
        except Exception as e:
            print(e)

    else:
        helper.concise_help()
