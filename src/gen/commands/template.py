import os
import shutil
import sys
from importlib import resources

from gen.config import EXTENSION_MAP

working_dir = os.getcwd()


def gen_langtemplate(file, extension, flag=None):
    if file and extension:
        lang = EXTENSION_MAP.get(extension)
        filename = file + extension

        create_path = os.path.join(working_dir, filename)  # Gives absolute path

        current_dir = os.path.dirname(__file__)  # Gets the parent dir of lib
        template_name = f"main{extension}"

        try:
            template_path = resources.files("gen.templates").joinpath(
                lang, template_name
            )
            if not template_path.exists():
                raise FileNotFoundError("template does not exist.")
        except FileNotFoundError as e:
            print(e)
            sys.exit(1)

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
    else:
        pass


def gen_framtemplate(dir_name, lang, framework):
    try:
        framework_path = resources.files("gen.templates").joinpath(lang, framework)
        if not framework_path.exists():
            raise FileNotFoundError(f"{framework} template does not exist.")
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    create_path = os.path.join(working_dir, dir_name)
    if os.path.exists(create_path):
        print(f"The directory '{dir_name}' already exists.")
        sys.exit(1)
    else:
        os.makedirs(create_path)
        shutil.copytree(framework_path, create_path, dirs_exist_ok=True)
        print(f"{dir_name} is created using {framework} template ")
