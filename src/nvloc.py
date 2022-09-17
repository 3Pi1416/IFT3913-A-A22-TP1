from pathlib import Path


def nvloc_command(args):
    if len(args) != 1:
        print("Error: nvloc takes one argument.")
        return
    file = Path(args[0])

    if not file.is_file:
        print(f"Error: {file.as_posix()} is not a file.")
        return
    nvloc(file)


def nvloc(file: Path):
    number_of_line_filled = 0
    with open(file) as open_file:
        for line in open_file:
            if line.strip().replace("\n", ""):
                number_of_line_filled += 1
                
    print(f"NVLOC : {number_of_line_filled}")
