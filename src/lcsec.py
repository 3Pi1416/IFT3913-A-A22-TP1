import csv
import sys
from pathlib import Path
from typing import List

from JavaMetric import JavaMetric, read_java_metric_from_csv


def lcsec_command(args):
    if len(args) != 2:
        print("Error: lcsec takes two arguments.")
        return

    path_folder = Path(args[0])
    if not path_folder.is_dir():
        print(f"{path_folder} is not a folder")
        return

    csv_file = Path(args[1])
    if not csv_file.is_file():
        print(f"Error: {csv_file.as_posix()} is not a file.")
        return

    java_metric_list = read_java_metric_from_csv(csv_file)
    java_metric_list = calculate_lcsec_values(path_folder, java_metric_list)

    output_path = Path("output")
    output_file = Path(output_path, "lcsec_output.csv")
    output_path.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows([java_metric.to_row(with_lcsec=True) for java_metric in java_metric_list])

    for java_metric in java_metric_list:
        java_metric.print(with_lcsec=True)


def calculate_lcsec_values(path_folder: Path, java_metric_list: List[JavaMetric]) -> List[JavaMetric]:
    tuple_metric_list = []
    for java_metric in java_metric_list:
        tuple_metric_list.append((java_metric, set()))

    for i in range(len(tuple_metric_list)):
        for j in range(i + 1, len(tuple_metric_list)):
            if mentions(path_folder, tuple_metric_list[i][0].path, tuple_metric_list[j][0].java_class) \
                    or mentions(path_folder, tuple_metric_list[j][0].path, tuple_metric_list[i][0].java_class):
                tuple_metric_list[i][1].add(tuple_metric_list[j][0].java_class)
                tuple_metric_list[j][1].add(tuple_metric_list[i][0].java_class)

    for tuple_metric in tuple_metric_list:
        tuple_metric[0].lcsec = len(tuple_metric[1])

    return java_metric_list


def mentions(path_folder: Path, file_path: Path, class_name: str):
    absolute_path = Path.joinpath(path_folder, file_path)

    with open(absolute_path) as file:
        for line in file:
            if line[0] != '/' or line[1] != '/':
                if class_name in line:
                    return True

    return False


if __name__ == "__main__":
    lcsec_command(sys.argv[1:])
