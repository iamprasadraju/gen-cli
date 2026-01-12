import sys

from gen.commands import helper, list_, template
from gen.config import EXTENSION_MAP


def main():
    if len(sys.argv) < 2:
        helper.help()
        return

    cmd = sys.argv[1]

    if cmd == "lang":
        try:
            if sys.argv[2] == "--list":
                list_.list_langtemplates()
        except:
            print("Usage: gen lang --list")

    elif cmd in ["framework", "lib"]:
        try:
            if sys.argv[2] == "--list":
                list_.list_framtemplates()
        except:
            print("Usage: gen framework/lib --list")
    elif cmd in ["-h", "--help", "help"]:
        helper.help()
    elif "." in cmd:
        try:
            parts = sys.argv[1].split(".")
            if len(parts) != 2:
                raise ValueError("Filename must contain exactly one extension.")
        except IndexError:
            print("Usage: gen <filename.extension> (To create a file)")
            sys.exit(1)
        except ValueError as e:
            print(e)
            sys.exit(1)

        filename, extension = parts[0], "." + parts[1]

        flag = sys.argv[2] if len(sys.argv) > 2 else None

        if flag:
            template.gen_langtemplate(filename, extension, flag=flag)
        else:
            template.gen_langtemplate(filename, extension)

    # check wheather lang has templates
    elif cmd == "new":
        try:
            if (
                "--" in sys.argv[3]
                and sys.argv[3][2:] in EXTENSION_MAP.values()
                and "--" in sys.argv[4]
            ):
                dir_name, lang, framework = (
                    sys.argv[2],
                    sys.argv[3][2:],
                    sys.argv[4][2:],
                )
                template.gen_framtemplate(dir_name, lang, framework)
        except IndexError:
            print("Usage: gen new <dir name> --<lang> --<framework>")

    else:
        print("Usage: gen <filename.extension> (To create a file)")
