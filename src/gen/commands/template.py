import os
import shutil
import sys
from importlib import resources
from pathlib import Path

from gen.commands import list_
from gen.config import EXTENSION_MAP, FRAMEWORK_CMD, FRAMEWORK_JINJA
from gen.core.render import render_framework

working_dir = Path.cwd()


def gen_langtemplate(file, extension, dryrun=False, overwrite=False):
    lang = EXTENSION_MAP.get(extension)
    filename = file + extension
    create_path = os.path.join(working_dir, filename)
    template_name = f"main{extension}"
    template_path = resources.files("gen.templates").joinpath(lang, template_name)

    with open(template_path, "r") as template:
        # Reads the template (main.*)
        content = template.read()

    if dryrun:
        print(f"--- Dry run for {filename} ---")
        print(content)
        return

    if os.path.exists(create_path):  # check weather file exists
        if overwrite:
            with open(create_path, "w") as f:
                f.write(content)
            print(f"{filename} overwritten!")
        else:
            print(f"{filename} already exists. Use --overwrite to replace it.")
    else:
        with open(create_path, "w") as f:
            f.write(content)
        print(f"{filename} created!")


def gen_framtemplate(dir_name, lang, framework, flag=None):
    framework_path = resources.files("gen.templates").joinpath(lang, framework)

    if flag == "--dryrun":
        list_.print_tree(framework_path)
        sys.exit(1)

    target_root = working_dir / dir_name

    if target_root.exists():
        print(f"The directory '{dir_name}' already exists.")
        sys.exit(1)

    target_root.mkdir(parents=True)

    key = f"{lang}/{framework}"
    if key in FRAMEWORK_CMD:
        cmds = [c.format(project_name=dir_name) for c in FRAMEWORK_CMD[value]]
        for cmd in cmds:
            os.system(cmd)
        return

    if not framework_path.exists():
        list_.list_framtemplates()
        raise FileNotFoundError(f"{framework} template does not exist.")

    elif key in FRAMEWORK_JINJA:
        context = {"project_name": dir_name}
        render_framework(framework_path, target_root, context)
        print(f"'{dir_name}' Created using template '{key}'")
    else:
        shutil.copytree(framework_path, target_root, dirs_exist_ok=True)
        print(f"{dir_name} is created using {framework} template ")
