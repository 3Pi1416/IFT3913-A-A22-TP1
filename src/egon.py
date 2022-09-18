from pathlib import Path
import jls
import nvloc
import lcsec


def egon_command(args):
    if len(args) != 1:
        print("Error: egon takes one argument.")
        return

    path_folder = Path(args[0])
    if not path_folder.is_dir():
        print(f"{path_folder} is not a folder.")
        return

    full_csv = get_full_csv(path_folder)

    indexes = find_god_classes(full_csv, 5)

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

    csec_indices = find_top_csec_scores(csec_scores)
    nvloc_indices = find_top_nvloc_scores(nvloc_scores)

    indices_to_print = list(set(csec_indices).intersection(nvloc_indices))

    for index in indices_to_print:
        print(",".join(full_csv[index]))

    return indexes

def find_top_csec_scores(csec_scores: list, threshold: int):
    return []

def find_top_nvloc_scores(nvloc_scores: list, threshold: int):
    return []


# egon_command(["/Users/maggierobert/Desktop/IFT3913/IFT3913-A-A22-TP1/tests/ressources/lcsec/folder2"])
