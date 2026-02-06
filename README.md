# Gen-CLI

**Gen-CLI** is a Python-based command-line tool for generating boilerplate code and framework templates for multiple programming languages.

## Features

- Single-file boilerplate generation based on file extension
- Project scaffolding using language and framework templates
- Directory tree visualization
- Environment diagnostics with `gen doctor`
- Version information with `--version` / `-v`
- Dry-run mode for previewing outputs

---

## Installation

### Using pip

```bash
pip install gen-cli
```

### Using uv (Faster)

```bash
uv pip install gen-cli
```

### Using pipx (Isolated)

```bash
pipx install gen-cli
```

### From Source

```bash
git clone https://github.com/iamprasadraju/gen-cli.git
cd gen-cli
pip install -e .
```

### Verify Installation

```bash
gen --version
```

---

## Quick Start

```bash
# Generate a Python file
gen main.py

# Generate a FastAPI project
gen new myapp --lang python --template fastapi

# Check your environment
gen doctor

# List available templates
gen list

# Show version
gen --version
```

---

## Commands

### `gen --version` / `gen -v`

Show the installed version of gen-cli.

```bash
gen --version
gen -v
```

Output: `gen-cli version 0.1.7`

---

### `gen --help` / `gen -h` / `gen help`

Show the help message.

```bash
gen --help
gen -h
gen help
```

---

### `gen doctor`

Check your environment and configuration for potential issues.

```bash
gen doctor
```

Output:
```
========================================
Gen CLI Doctor
========================================
Python Version: 3.14.2
Platform: macOS-15.7.3-arm64
Working Directory: /Users/user/project
PATH directories: 17
========================================
All checks passed!
```

---

### `gen list`

List all available language templates and framework templates.

```bash
gen list
```

---

### `gen tree`

Display a tree view of your directory structure.

```bash
gen tree                    # current directory
gen tree -r                 # recursive (all levels)
gen tree -d 3               # depth of 3 levels
gen tree path/to/dir        # specific directory
```

---

### `gen new`

Generate a new project from a language and framework template.

```bash
gen new <project_name> --lang <language> --template <template>
```

**Options:**

| Flag | Description | Required |
|------|-------------|----------|
| `--lang` | Programming language | Yes |
| `--template` | Framework or template name | Yes |
| `--dryrun` | Preview without creating files | No |

**Examples:**

```bash
# Python projects
gen new myapp --lang python --template fastapi
gen new api --lang python --template flask
gen new web --lang python --template django

# Go projects
gen new mytool --lang go --template cli
gen new service --lang go --template web

# Rust projects
gen new server --lang rust --template actix
gen new mylib --lang rust --template rocket

# JavaScript projects
gen new app --lang javascript --template react
gen new api --lang javascript --template node
```

---

### Single File Generation

Generate a boilerplate file directly by specifying its extension.

```bash
gen main.py          # Python file
gen app.go           # Go file
gen index.js         # JavaScript file
gen main.rs          # Rust file
gen main.c           # C file
gen main.cpp         # C++ file
gen main.java        # Java file
gen index.html       # HTML file
```

**Options:**

| Flag | Description |
|------|-------------|
| `--dryrun` | Preview the file content without creating it |
| `--overwrite` | Overwrite existing file |

**Examples:**

```bash
gen main.py --dryrun          # Preview Python file
gen app.py --overwrite        # Overwrite existing file
```

---

## Supported Languages & Templates

| Language | Templates |
|----------|-----------|
| Python | flask, fastapi, django, lib, project |
| Go | cli, web |
| Rust | actix, rocket |
| C | standard |
| C++ | standard |
| Java | spring, standard |
| JavaScript | node, react, vue |
| HTML | standard |

---

## File Extensions

| Extension | Language |
|-----------|----------|
| `.py` | Python |
| `.go` | Go |
| `.rs` | Rust |
| `.c` | C |
| `.cpp` | C++ |
| `.java` | Java |
| `.js` | JavaScript |
| `.html` | HTML |

---

## Error Handling

Gen-CLI provides clear error messages for common issues:

- **Invalid commands** → Displays help message
- **Unsupported file extensions** → Lists available templates
- **Invalid template combinations** → Shows valid options
- **Tree errors** → Falls back to current directory
- **Existing files/directories** → Shows appropriate message

---

## Development

### Running Tests

```bash
# Run all tests
python3 -m pytest tests/test_cli.py -v

# Run specific test
python3 -m pytest tests/test_cli.py::TestDoctor -v
```

### Test Coverage

| Test Class | Description |
|------------|-------------|
| `TestCLI` | Core CLI module tests |
| `TestVersion` | Version command tests |
| `TestFilenameMode` | Single file generation tests |
| `TestDoctor` | Environment diagnostics tests |
| `TestListCommand` | Template listing tests |
| `TestTreeCommand` | Tree visualization tests |
| `TestTemplateCommand` | Template generation tests |
| `TestConfig` | Configuration tests |
| `TestCore` | Core module tests |
| `TestHelper` | Help command tests |
| `TestMain` | Main entry point tests |

### Running from Source

```bash
python3 -m gen.cli <command>
```

---

## Project Structure

```
gen-cli/
├── src/
│   └── gen/
│       ├── __init__.py
│       ├── cli.py              # Main CLI entry point
│       ├── config.py           # Configuration & extension maps
│       ├── commands/
│       │   ├── __init__.py
│       │   ├── doctor.py       # Environment diagnostics
│       │   ├── helper.py       # Help messages
│       │   ├── list_.py        # Template listing
│       │   └── template.py     # Template generation
│       ├── core/
│       │   ├── __init__.py
│       │   └── render.py       # Jinja2 template rendering
│       └── templates/          # Built-in templates
├── tests/
│   └── test_cli.py             # Comprehensive unit tests
├── pyproject.toml
└── README.md
```

---

## License

MIT License

---

## Author

Prasad Raju G

---

## Repository

https://github.com/iamprasadraju/gen-cli
