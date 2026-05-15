import pathlib

langs_path = pathlib.Path(__file__).parent / "templates/lang"
langs = {}
for file in langs_path.iterdir():
    langs[file.as_posix()] = file.suffix

frameworks_path = pathlib.Path(__file__).parent / "templates/frameworks"
frameworks = {}
for folders in frameworks_path.iterdir():
    frameworks[folders.as_posix()] = folders.name

if __name__ == "__main__":
    print(langs)
    print(frameworks)