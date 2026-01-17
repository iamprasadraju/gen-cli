HELP_TEXT = """
Gen-CLI — Generate boilerplate files and framework project templates
for multiple programming languages.

USAGE:
    gen <command> [options]

COMMANDS:
    new <project|file>    Generate a file or project from a template
    list                  List available languages and frameworks
    tree [depth|path]     Show directory tree
    doctor                Check environment and configuration
    help                  Show this help message

NEW COMMAND:
    gen new <project_name|file> --lang <language> --template <template> [options]

OPTIONS (for `new`):
    --lang <language>         Programming language
    --template <template>    Framework or template name
    --dry-run                Show output without writing files
    --overwrite              Overwrite existing files
    --project-name <name>    Name used inside templates
    --author <name>          Author name (optional)

SUPPORTED LANGUAGES & TEMPLATES:
    Python:     flask, fastapi, django
    Go:         cli, web
    Rust:       actix, rocket
    C:          standard
    C++:        standard
    Java:       spring, standard
    JavaScript: node, react, vue
    HTML:       standard

EXAMPLES:
    # Generate a single Python Flask file
    gen new main.py --lang python --template flask

    # Generate a FastAPI project (dry run)
    gen new myapp --lang python --template fastapi --dry-run

    # Generate a Go CLI project
    gen new mytool --lang go --template cli

    # List all supported languages and frameworks
    gen list

    # Show directory tree recursively
    gen tree -r

    # Check environment
    gen doctor

HELP:
    gen help
"""


COMMANDS_TEXT = """
AVAILABLE COMMANDS:

    gen new <project|file> --lang <language> --template <template>
        Generate a project or file from templates

    gen list
        List supported languages and templates

    gen tree [path] [-r|-<depth>]
        Display directory tree

    gen doctor
        Check environment and configuration

    gen help
        Show help information
"""


def help():
    print(HELP_TEXT)


def concise_help():
    print(COMMANDS_TEXT)
