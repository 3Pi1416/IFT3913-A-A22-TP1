from pathlib import Path
import csv


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

    output = lcsec(path_folder, csv_file)
    for row in output:
        print(",".join(row))


def lcsec_csv_like(path_folder: Path, csv_like_list: list):
    output = []
    paths = []
    file_names = []

    for row in csv_like_list:
        output.append(row)
        paths.append(Path(row[0]))
        file_names.append(row[2].replace(" ", ""))

    csec_values = [0] * len(output)

    for i in range(len(paths)):
        for j in range(i + 1, len(paths)):
            if mentions(path_folder, paths[i], file_names[j]) or mentions(path_folder, paths[j], file_names[i]):
                csec_values[i] += 1
                csec_values[j] += 1
        output[i].append(" " + str(csec_values[i]))

    return output


def lcsec(path_folder: Path, csv_file: Path):
    output = []
    paths = []
    file_names = []

    with open(csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            output.append(row)
            paths.append(Path(row[0]))
            file_names.append(row[2].replace(" ", ""))

    csec_values = [0] * len(output)

    for i in range(len(paths)):
        for j in range(i+1, len(paths)):
            if mentions(path_folder, paths[i], file_names[j]) or mentions(path_folder, paths[j], file_names[i]):
                csec_values[i] += 1
                csec_values[j] += 1
        output[i].append(" " + str(csec_values[i]))

    return output


def mentions(path_folder: Path, file_path: Path, class_name: str):
    absolute_path = Path.joinpath(path_folder, file_path)

    with open(absolute_path) as file:
        for line in file:
            if line[0] != '/' or line[1] != '/':
                if class_name in line:
                    return True

    return False

