import csv
import sys
from pathlib import Path
from typing import List

from JavaMetric import JavaMetric


def jls_command(args: List):
    """
    Read arguments and call the jls methods
    Args:
        args: arguments from command line

    """
    if len(args) < 1 or len(args) > 2:
        print("Error: jls takes one or two arguments.")
        return

    path_folder = Path(args[0])
    if not path_folder.is_dir():
        print(f"{path_folder} is not a folder")
        return

    if len(args) == 2:
        root = Path(args[1])
        java_metric_list = java_list(path_folder, root)
    else:
        java_metric_list = java_list(path_folder)

    output_path = Path("output")
    output_file = Path(output_path, "jls_output.csv")
    output_path.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w") as file:
        writer = csv.writer(file)
        writer.writerows([java_metric.to_row() for java_metric in java_metric_list])

    for java_metric in java_metric_list:
        java_metric.print()


def java_list(path_folder: Path, root: Path = None, java_metric_list: List[JavaMetric] = []) -> List[JavaMetric]:
    """This function reads all the files in a folder.
       Shortcuts (links in linux) will crash it.

    Args:
        path_folder (Path): folder containing files to read
        root (Path, optional): Root of the folder for the naming the packages. Defaults to path_folder.
        java_metric_list: for recursive function or to call java_list on multiple path with same output
    """

    if root is None:
        root = path_folder

    for file in path_folder.iterdir():
        if file.is_dir():
            java_metric_list = java_list(file, root, java_metric_list)
        elif file.suffix.upper() != "JAVA":
            java_metric_list.append(extract_java_jls(file, root))

    return java_metric_list


def extract_java_jls(path_file: Path, default_path_folder: Path = None) -> JavaMetric:
    """
    Register basic information from path
    Args:
        path_file: path to file to extract information from
        default_path_folder: if the path is relative to another one.

    Returns:java_metric: path, package and name

    """
    local_path_with_file_ext = path_file
    if default_path_folder is not None:
        local_path_with_file_ext = path_file.relative_to(default_path_folder)
    list_local_path_file = local_path_with_file_ext.with_suffix("").as_posix().split("/")
    package = ".".join(list_local_path_file[0:-1])
    java_metric = JavaMetric(path=local_path_with_file_ext, package=f"{package}",
                             java_class=f"{list_local_path_file[-1]}")
    return java_metric


if __name__ == "__main__":
    jls_command(sys.argv[1:])
