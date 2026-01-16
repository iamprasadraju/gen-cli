EXTENSION_MAP = {
    ".py": "python",
    ".go": "go",
    ".c": "c",
    ".cpp": "cpp",
    ".js": "javascript",
    ".java": "java",
    ".rs": "rust",
    ".html": "html",
}

FRAMEWORK_CMD = {
    "python/django": ["pip install django", "django-admin startproject {project_name}"]
}


FRAMEWORK_JINJA = ["python/project", "python/lib"]
