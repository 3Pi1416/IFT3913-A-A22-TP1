from pathlib import Path
import csv
import sys

from dataclass_csv import DataclassWriter
from typing import List

from src.JavaMetric import JavaMetricLcsec, JavaMetric, read_java_metric_from_csv


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
    java_metric_lcsec_list = get_csec_values(path_folder, java_metric_list)

    output_path = Path("output")
    output_file = Path(output_path, "lcsec_output.csv")
    output_path.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w") as file:
        writer = DataclassWriter(file, java_metric_lcsec_list, JavaMetricLcsec)
        writer.write(True)

    for java_metric in java_metric_lcsec_list:
        java_metric.print()


def lcsec_with_list(path_folder: Path, csv_like_list: []):
    output = []
    paths = []
    file_names = []

    for row in csv_like_list:
        output.append(row)
        paths.append(Path(row[0]))
        file_names.append(row[2].replace(" ", ""))

    return get_csec_values(path_folder, paths, file_names, output)


def get_csec_values(path_folder: Path, java_metric_list: List[JavaMetric]) -> List[JavaMetricLcsec]:
    java_metric_lcsec_list: [JavaMetricLcsec] = []

    for java_metric in java_metric_list:
        new_java_metric = JavaMetricLcsec(java_metric)
        java_metric_lcsec_list.append(new_java_metric)

    for i in range(len(java_metric_lcsec_list)):
        for j in range(i + 1, len(java_metric_lcsec_list)):
            if mentions(path_folder, java_metric_lcsec_list[i].path, java_metric_lcsec_list[j].java_class) \
                    or mentions(path_folder, java_metric_lcsec_list[j].path, java_metric_lcsec_list[i].java_class):
                java_metric_lcsec_list[i].lcsec += 1
                java_metric_lcsec_list[j].lcsec += 1

    return java_metric_lcsec_list


def mentions(path_folder: Path, file_path: Path, class_name: str):
    absolute_path = Path.joinpath(path_folder, file_path)

    with open(absolute_path) as file:
        for line in file:
            if line[0] != '/' or line[1] != '/':
                if class_name in line:
                    return True

    return False


if __name__ == "__main__":
    lcsec_command(sys.argv)
