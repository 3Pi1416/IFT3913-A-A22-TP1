from pathlib import Path
import jls
import nvloc
import lcsec
import math


def egon_command(args):
    if len(args) != 2:
        print("Error: egon takes two arguments.")
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

    full_csv = get_full_csv(path_folder)

    indexes = find_god_classes(full_csv, threshold)

    for index in indexes:
        print(",".join(full_csv[index]))


def get_full_csv(path_folder: Path):
    jls_output = []
    jls.java_list(jls_output, path_folder)
    full_csv = lcsec.lcsec_csv_like(path_folder, jls_output)

    for row in full_csv:
        absolute_path = Path.joinpath(path_folder, Path(row[0]))
        row.append(" " + str(nvloc.nvloc(absolute_path)))

    return full_csv


def find_god_classes(full_csv: list, threshold: int):
    indexes = []
    csec_scores = []
    nvloc_scores = []

    for i in range(len(full_csv)):
        csec_scores.append([str(full_csv[i][3]), i])
        nvloc_scores.append([str(full_csv[i][4]), i])

    csec_indices = find_top_scores(csec_scores, threshold)
    nvloc_indices = find_top_scores(nvloc_scores, threshold)

    indices_to_print = list(set(csec_indices).intersection(nvloc_indices))

    for index in indices_to_print:
        print(",".join(full_csv[index]))

    return indexes


def find_top_scores(scores: list, threshold: int):
    indexes = []

    scores.sort(reverse=True)
    num_above_threshold = calculate_num_within_percentile(len(scores), threshold)

    for i in range(num_above_threshold):
        indexes.append(scores[i][1])

    return indexes


def calculate_num_within_percentile(num_values: int, threshold: int):
    return math.ceil(((threshold / 100) * num_values))

