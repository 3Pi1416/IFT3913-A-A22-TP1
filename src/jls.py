from pathlib import Path

from typing import List


def jls_command(args: List):
    if len(args) == 0 or len(args) > 2:
        print("Error: jls takes one or two arguments.")
        return

    path_folder = Path(args[0])
    if not path_folder.is_dir():
        print(f"{path_folder} is not a folder")
        return

    if len(args) == 2:
        root=Path(args[1])
        java_list(path_folder, root)
    else:
        java_list(path_folder)


def java_list(path_folder: Path, root: Path=None):
    """This function reads all files in folder.
       Shortcuts (links in linux) will crash it.

    Args:
        path_folder (Path): folder where to start
        root (Path, optional): Root of the folder for naming all the package. Defaults to path_folder.
    """
    if root is None:
        root=path_folder

    for file in path_folder.iterdir():
        if file.is_dir():
            java_list(file, root)
        else:
            print_csv_line(file, root)


def print_csv_line(path_file: Path, default_path_folder: Path=None) -> None:
    if default_path_folder is not None:
        local_path_with_file_ext=path_file.relative_to(default_path_folder)
    list_local_path_file=local_path_with_file_ext.with_suffix("").as_posix().split("/")
    package=".".join(list_local_path_file[0:-1])
    print(f"./{local_path_with_file_ext.as_posix()}, {package}, {list_local_path_file[-1]}")
