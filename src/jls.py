
from genericpath import isdir
from posixpath import islink


import os


def jls(path_folder: str):
    for file in os.listdir:
        if os.path.islink(file):
            # pass if is a shortcut
            continue
        elif os.path.isdir(file):
            jls(file)
        else:
            print_CSV_Line(path_folder)


def print_CSV_Line(path_file: str, default_path_folder: str):
    print("%s , %s", path_file, default_path_folder)
