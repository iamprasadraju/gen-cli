import sys
from importlib import metadata
from pathlib import Path

from .paths import langs, frameworks
from .commands.list_ import print_list, tree_view, print_tree_structure
from .commands.doctor import run_doctor
from .commands.helper import help as show_help, concise_help
from .core.render import render_framework


def get_version():
    return metadata.version("gen-cli")


def _parse_flags(args, valid_flags):
    flags = {}
    positional = []
    unknown = []

    for arg in args:
        if arg.startswith("--"):
            name = arg[2:]
            if name in valid_flags:
                flags[name] = True
            else:
                unknown.append(arg)
        elif arg.startswith("-") and len(arg) > 1:
            short = arg[1:]
            matched = False
            for v in valid_flags:
                if v.startswith(short):
                    flags[v] = True
                    matched = True
                    break
            if not matched:
                unknown.append(arg)
        else:
            positional.append(arg)

    return flags, positional, unknown


def parse_command_mode():
    if len(sys.argv) > 1 and sys.argv[1] == "tree":
        _handle_tree()
        return

    if len(sys.argv) == 2 and sys.argv[1] in ("--version", "-v"):
        print(f"gen-cli version {get_version()}")
        return

    if len(sys.argv) == 2 and sys.argv[1] in ("--help", "-h"):
        show_help()
        return

    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]
    parser_flags, positional, unknown = _parse_flags(
        sys.argv[2:], {"dryrun", "overwrite"}
    )

    if unknown:
        print(f"Unknown flag: {unknown[0]}")
        concise_help()
        return

    dryrun = parser_flags.get("dryrun", False)
    overwrite = parser_flags.get("overwrite", False)

    if command == "list":
        print_list("Available Languages", [ext[1:] for ext in langs.values()])
        print_list("Available Frameworks", list(frameworks.values()))
    elif command == "doctor":
        run_doctor()
    elif f".{command}" in langs.values():
        _generate_lang(command, dryrun=dryrun, overwrite=overwrite)
    elif command in frameworks.values():
        project_name = positional[0] if len(positional) > 0 else None
        _generate_framework(command, project_name=project_name, dryrun=dryrun, overwrite=overwrite)
    else:
        print(f"Unknown command: {command}")
        concise_help()


def _generate_lang(lang, dryrun=False, overwrite=False):
    template_file = None
    for path, ext in langs.items():
        if ext == f".{lang}":
            template_file = Path(path)
            break

    if template_file is None or not template_file.exists():
        print(f"Template for '{lang}' not found")
        return

    output_name = template_file.name
    dest = Path.cwd() / output_name

    if dryrun:
        content = template_file.read_text()
        print(f"--- Dry run: {output_name} ---")
        print(content)
        return

    if dest.exists() and not overwrite:
        print(f"{output_name} already exists")
        print(f"Use --overwrite to replace: gen {lang} --overwrite")
        return

    if dest.exists() and overwrite:
        dest.write_text(template_file.read_text())
        print(f"Overwritten {output_name}")
        return

    dest.write_text(template_file.read_text())
    print(f"Generated {output_name}")


def _generate_framework(framework, project_name=None, dryrun=False, overwrite=False):
    template_dir = None
    for path, name in frameworks.items():
        if name == framework:
            template_dir = Path(path)
            break

    if template_dir is None or not template_dir.exists():
        print(f"Template for '{framework}' not found")
        return

    if project_name is None and not dryrun:
        project_name = input("Enter project name: ").strip() or framework

    if project_name is None:
        project_name = framework

    target = Path.cwd() / project_name

    if dryrun:
        print(f"--- Dry run: {framework} project '{project_name}' ---")
        print_tree_structure(template_dir, project_name)
        return

    if target.exists() and not overwrite:
        print(f"Directory '{project_name}' already exists")
        print(f"Use --overwrite to replace: gen {framework} {project_name} --overwrite")
        return

    if target.exists() and overwrite:
        import shutil
        shutil.rmtree(target)

    context = {"project_name": project_name}
    render_framework(str(template_dir), target, context)
    print(f"Generated {framework} project in {project_name}/")


def _handle_tree():
    remaining = sys.argv[2:]
    depth = 2
    path = "."
    show_hidden = False

    for arg in remaining:
        if arg.startswith("-") and arg[1:].isdigit():
            depth = int(arg[1:])
        elif arg in ("-a", "--all"):
            show_hidden = True
        elif arg.isdigit():
            print(f"Invalid depth format: '{arg}'")
            print("Use '-' prefix for depth, e.g., 'gen tree -3' or 'gen tree -3 src'")
            return
        elif not arg.startswith("-"):
            path = arg

    tree_view(path=path, depth=depth, show_hidden=show_hidden)


def main():
    parse_command_mode()


if __name__ == "__main__":
    main()
