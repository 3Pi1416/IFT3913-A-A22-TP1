import csv
import sys
from pathlib import Path
from typing import List

import jls
import lcsec
import nvloc
from JavaMetric import JavaMetric


def egon_command(args):
    if len(args) < 2 or len(args) > 3:
        print("Error: egon takes two or threes arguments.")
        return

    path_folder = Path(args[0])
    if not path_folder.is_dir():
        print(f"{path_folder} is not a folder.")
        return

    try:
        threshold = int(args[1])
    except ValueError:
        print(f"{args[1]} is not an integer.")
        return

    if threshold > 99 or threshold < 1:
        print("Threshold: [" + f"{threshold}] is not between 1 and 99.")
        return

    file_name = ""
    if len(args) == 3:
        file_name = args[2]

    java_metric_god_classes = calculate_egon(path_folder, threshold)

    output_path = Path("output")
    output_file = Path(output_path, f"egon_output_{file_name}{threshold}.csv")
    output_path.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(
            [java_metric.to_row(with_lcsec=True, with_nvloc=True) for java_metric in java_metric_god_classes])

    for java_metric in java_metric_god_classes:
        java_metric.print(with_lcsec=True, with_nvloc=True)


def calculate_egon(path_folder: Path, threshold: int):
    java_metric_list: List[JavaMetric] = jls.java_list(path_folder)
    java_metric_list = lcsec.calculate_lcsec_values(path_folder, java_metric_list)
    for java_metric in java_metric_list:
        java_metric.nvloc = nvloc.nvloc(path_folder.joinpath(java_metric.path))

    java_metric_god_classes: List[JavaMetric] = find_god_classes(java_metric_list, threshold)
    return java_metric_god_classes


def find_god_classes(java_metric_list: List[JavaMetric], threshold: int) -> List[JavaMetric]:
    lcsec_indexes = find_top_scores([[java_metric_list[i].lcsec, i] for i in range(len(java_metric_list))], threshold)
    nvloc_indexes = find_top_scores([[java_metric_list[i].nvloc, i] for i in range(len(java_metric_list))], threshold)

    indexes_to_print = list(set(lcsec_indexes).intersection(nvloc_indexes))
    god_class_list: List[JavaMetric] = []
    for index in indexes_to_print:
        god_class_list.append(java_metric_list[index])
    return god_class_list


def find_top_scores(scores: list, threshold: int) -> List[int]:
    indexes: List[int] = []
    scores.sort(reverse=True)
    num_above_threshold = calculate_num_within_percentile(len(scores), threshold)
    for i in range(num_above_threshold):
        indexes.append(scores[i][1])
    return indexes


def calculate_num_within_percentile(num_values: int, threshold: int) -> int:
    return round(((threshold / 100) * num_values))


if __name__ == "__main__":
    egon_command(sys.argv[1:])
