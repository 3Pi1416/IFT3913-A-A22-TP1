from pathlib import Path


def egon_command(args):
    if len(args) != 1:
        print("Error: egon takes one argument.")
        return

    path_folder = Path(args[0])
    if not path_folder.is_dir():
        print(f"{path_folder} is not a folder.")
        return

