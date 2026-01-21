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


# For those has framework commands for project creation
FRAMEWORK_CMD = {
    "python/django": ["pip install django", "django-admin startproject {project_name}"]
}

# For those uses jinja template
FRAMEWORK_JINJA = ["python/project", "python/lib"]
