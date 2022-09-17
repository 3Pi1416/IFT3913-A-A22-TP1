import sys
import jls
import nvloc


def quit_program(args):
    quit()

# define all the function to that can be execute
dict_function = {"EXIT": quit_program, "JLS": jls.jls_command, "NVLOC": nvloc.nvloc_command}


def main():
    for line in sys.stdin:
        command, args = read_line(line)
        function_to_execute = dict_function.get(command.upper())
        if function_to_execute is None:
            function_to_execute(args)
        else:
            print(f"{command} is not a valid command.")


def read_line(line: str):
    commands = line.strip().split(" ")
    return commands.pop(0), commands


if __name__ == "__main__":
    main()
