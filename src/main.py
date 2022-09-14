import sys
import os


def main():
    for line in sys.stdin:
        if line.upper() == "EXIT\n":
            quit()
        else:
            print(line)


if __name__ == "__main__":
    main()

