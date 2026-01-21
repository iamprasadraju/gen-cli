import os
import shutil
import sys
from importlib import resources
from pathlib import Path

from gen.commands import list_
from gen.config import EXTENSION_MAP, FRAMEWORK_CMD, FRAMEWORK_JINJA
from gen.core.render import render_framework

working_dir = Path.cwd()


def gen_langtemplate(file, extension, flag=None):
    lang = EXTENSION_MAP.get(extension)

    filename = file + extension

    create_path = os.path.join(working_dir, filename)  # Gives absolute path
    template_name = f"main{extension}"

    template_path = resources.files("gen.templates").joinpath(lang, template_name)

    # print(template_path)
    with open(template_path, "r") as template:
        # Reads the template (main.*)
        content = template.read()
    if flag is None:
        if os.path.isfile(create_path):  # check weather file exists
            print("File is already exists")
        else:
            with open(create_path, "w") as file:
                file.write(content)
                print(f"{filename} created!")
    else:
        if flag == "--dryrun":
            print(content)
        elif flag == "--overwrite":
            with open(create_path, "w") as file:
                file.write(content)
                print(f"{filename} overwrited!")


def gen_framtemplate(dir_name, lang, framework, flag):
    key = f"{lang}/{framework}"
    if key in FRAMEWORK_CMD:
        cmds = [c.format(project_name=dir_name) for c in FRAMEWORK_CMD[value]]
        for cmd in cmds:
            os.system(cmd)
        return
    framework_path = resources.files("gen.templates").joinpath(lang, framework)

    if not framework_path.exists():
        list_.list_framtemplates()
        raise FileNotFoundError(f"{framework} template does not exist.")

    target_root = working_dir / dir_name

    if target_root.exists():
        print(f"The directory '{dir_name}' already exists.")
        sys.exit(1)

    target_root.mkdir(parents=True)

    if flag == "--dryrun":
        list_.print_tree(framework_path)

    elif key in FRAMEWORK_JINJA:
        context = {"project_name": dir_name}
        render_framework(framework_path, target_root, context)
        print(f"'{dir_name}' Created using template '{key}'")
    else:
        shutil.copytree(framework_path, target_root, dirs_exist_ok=True)
        print(f"{dir_name} is created using {framework} template ")
