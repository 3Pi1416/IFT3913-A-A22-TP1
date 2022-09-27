import sys
from pathlib import Path


def nvloc_command(args):
    """
    read arguments and call the real nvloc methods
    Args:
        args: arguments from command line

    """
    if len(args) != 1:
        print("Error: nvloc takes one argument.")
        return
    file = Path(args[0])

    if not file.is_file():
        print(f"Error: {file.as_posix()} is not a file.")
        return

    print(nvloc(file))


def nvloc(file: Path) -> int:
    """

    Args:
        file: path to file to count its line number.

    Returns: number of none empty line

    """
    number_of_line_filled = 0
    with open(file) as open_file:
        for line in open_file:
            if line.strip().replace("\n", ""):
                number_of_line_filled += 1

    return number_of_line_filled


if __name__ == "__main__":
    nvloc_command(sys.argv[1:])
