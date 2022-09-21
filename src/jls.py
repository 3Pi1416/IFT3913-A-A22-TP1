from pathlib import Path
from typing import List
import csv

from src.javaMetric import javaMetric


def jls_command(args: List):
    if len(args) == 0 or len(args) > 2:
        print("Error: jls takes one or two arguments.")
        return

    path_folder = Path(args[0])
    if not path_folder.is_dir():
        print(f"{path_folder} is not a folder")
        return

    if len(args) == 2:
        root = Path(args[1])
        java_list(root)
    else:
        java_list()

    output_file = Path("output", "jls_output.csv")
    with open(output_file, "w") as f:
        write = csv.writer(f)
        for row in output:
            print(",".join(row))
            write.writerow(row)


def java_list(path_folder: Path, root: Path = None, java_metric_list: List[javaMetric] = List[javaMetric]) -> \
        List[javaMetric]:
    """This function reads all files in folder.
       Shortcuts (links in linux) will crash it.

    Args:
        java_metric_list: for recursive or to call java_list on multiple path with same output
        path_folder (Path): folder where to start
        root (Path, optional): Root of the folder for naming all the package. Defaults to path_folder.
    """

    if root is None:
        root = path_folder

    for file in path_folder.iterdir():
        if file.is_dir():
            java_metric_list = java_list(file, root, java_metric_list)
        else:
            java_metric_list.append(add_csv_line(file, root))

    return java_metric_list


def add_csv_line(path_file: Path, default_path_folder: Path = None) -> javaMetric:
    local_path_with_file_ext = path_file
    if default_path_folder is not None:
        local_path_with_file_ext = path_file.relative_to(default_path_folder)
    list_local_path_file = local_path_with_file_ext.with_suffix("").as_posix().split("/")
    package = ".".join(list_local_path_file[0:-1])
    java_metric = javaMetric(path=f"./{local_path_with_file_ext.as_posix()}", package=f"{package}",
                             java_class=f"{list_local_path_file[-1]}")
    return java_metric
