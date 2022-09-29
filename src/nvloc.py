import sys
from pathlib import Path


def nvloc_command(args):
    """
    Read arguments and call the nvloc methods
    Args:
        args: arguments from command line

    """
    if len(args) != 1:
        print("Error: nvloc takes one argument.")
        return
    file = Path(args[0])

    if not file.is_file() and file.suffix.upper() != "JAVA":
        print(f"Error: {file.as_posix()} is not a java file.")
        return

    print(nvloc(file))


def nvloc(file: Path) -> int:
    """

    Args:
        file: path to a file to count the number of lines

    Returns: number of non-empty lines

    """
    number_of_line_filled = 0
    with open(file) as open_file:
        for line in open_file:
            if line.strip().replace("\n", ""):
                number_of_line_filled += 1

    return number_of_line_filled


if __name__ == "__main__":
    nvloc_command(sys.argv[1:])
