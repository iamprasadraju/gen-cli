from pathlib import Path

from gen.paths import langs, frameworks


def gen_langtemplate(filename, extension, dryrun=False):
    template_file = None
    for path, ext in langs.items():
        if ext == extension:
            template_file = Path(path)
            break

    if template_file is None or not template_file.exists():
        print(f"Template not found for {extension}")
        return

    content = template_file.read_text()

    if dryrun:
        print(f"--- Dry run: {filename}{extension} ---")
        print(content)
        return

    output_path = Path.cwd() / f"{filename}{extension}"
    if output_path.exists():
        print(f"{output_path.name} already exists")
        return

    output_path.write_text(content)
    print(f"Generated {output_path.name}")


def gen_framtemplate(framework, project_name, dryrun=False):
    template_dir = None
    for path, name in frameworks.items():
        if name == framework:
            template_dir = Path(path)
            break

    if template_dir is None or not template_dir.exists():
        print(f"Template not found for {framework}")
        return

    if dryrun:
        print(f"--- Dry run: {framework} project '{project_name}' ---")
        for f in template_dir.rglob("*"):
            if f.is_file():
                print(f"  {f.relative_to(template_dir)}")
        return

    target = Path.cwd() / project_name
    if target.exists():
        print(f"Directory '{project_name}' already exists")
        return

    from gen.core.render import render_framework

    context = {"project_name": project_name}
    render_framework(str(template_dir), target, context)
    print(f"Generated {framework} project in {project_name}/")
