# Gen-CLI

**Gen-CLI** is a Python-based command-line tool for generating boilerplate code and
framework templates for multiple programming languages.

It supports:
- Single-file boilerplate generation based on file extension
- Project scaffolding using language and framework templates
- Directory tree visualization
- Environment diagnostics

---

## Installation

```bash
pip install gen-cli
````

*or run from source*

```bash
git clone https://github.com/yourname/gen-cli.git
cd gen-cli
python -m gen
```

---

## Usage

```bash
gen <command> [arguments]
```

---

## Commands

### `help`

Show the help message.

```bash
gen help
gen --help
gen -h
```

---

### `list`

List all available language templates.

```bash
gen list
```

---

### `doctor`

Check environment and configuration.

```bash
gen doctor
```

---

### `tree`

Display a tree view of the directory structure.

```bash
gen tree
gen tree -r           # recursive
gen tree -3           # depth = 3
gen tree path/to/dir
```

---

### `new`

Generate a new project using a language and framework template.

```bash
gen new <project_name> --lang <language> --template <framework>
```

#### Example

```bash
gen new myapp --lang python --template fastapi
```

> ⚠️ Both `--lang` and `--template` flags are required.

---

### Single File Generation

Generate a boilerplate file based on its extension.

```bash
gen main.py
gen app.go
gen index.js
```

The tool determines the template automatically using the file extension.

---

## Supported Languages & Templates

| Language   | Templates              |
| ---------- | ---------------------- |
| Python     | flask, fastapi, django |
| Go         | cli, web               |
| Rust       | actix, rocket          |
| C          | standard               |
| C++        | standard               |
| Java       | spring, standard       |
| JavaScript | node, react, vue       |
| HTML       | standard               |

---

## Directory Tree Example

```text
project/
├── main.py
├── app/
│   ├── __init__.py
│   └── routes.py
└── README.md
```

---

## Error Handling

* Invalid commands show the help message
* Invalid file extensions list supported templates
* Tree command falls back to current directory on error

---

## Project Structure

```text
gen/
├── commands/
│   ├── helper.py
│   ├── list_.py
│   └── template.py
├── config.py
└── main.py
```

---

## Limitations

* Argument parsing is manual (`sys.argv`)
* Flags must follow exact order for `new`
* No interactive mode
* No plugin system

---

## Roadmap

* [ ] Migrate to argparse / typer
* [ ] Improve error messages
* [ ] Add interactive project generator
* [ ] Add template registry
* [ ] Add shell auto-completion

---

## License

MIT License
