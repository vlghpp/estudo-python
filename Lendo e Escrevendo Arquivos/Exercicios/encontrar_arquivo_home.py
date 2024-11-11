from pathlib import Path

path_home: Path = Path.home()


def search_archive(path, name_archive):
    for file in path_home.glob('**/*'):
        if file.is_file():
            if file.name == name_archive:
                print(f"{file}")




search_archive(Path.cwd(), "arquivo3.txt")