import os
import shutil
from importlib import resources
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

template_root = resources.files("gen.templates")

env = Environment(
    loader=FileSystemLoader(str(template_root)),
    trim_blocks=True,
    lstrip_blocks=True,
)


# jinja template rendering
def render_framework(template_dir, target_root, context):
    for root, dirs, files in os.walk(template_dir):
        root_path = Path(root)

        rel_path = root_path.relative_to(template_dir)
        rel_path = Path(
            str(rel_path).replace("__project_name__", context["project_name"])
        )

        # Create directories
        for d in dirs:
            new_dir = d.replace("__project_name__", context["project_name"])
            (target_root / rel_path / new_dir).mkdir(parents=True, exist_ok=True)

        # Render files
        for file in files:
            template_file = root_path / file
            output_file = target_root / rel_path / file.replace(".j2", "")

            output_file.parent.mkdir(parents=True, exist_ok=True)
            if file.endswith(".j2"):
                template_path = template_file.relative_to(template_root)

                template = env.get_template(str(template_path))
                content = template.render(**context)

                output_file.parent.mkdir(parents=True, exist_ok=True)
                output_file.write_text(content)
            else:
                shutil.copy(template_file, output_file)
