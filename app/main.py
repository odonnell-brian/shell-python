import os
import sys

BUILT_INS = {"exit", "type", "echo"}

def main():
    repl()


def repl():
    while True:
        sys.stdout.write("$ ")
        
        # Wait for user input
        user_input = input()
        parts = user_input.split(" ")
        command, *args = parts
        
        if command == "exit":
            return
        elif command == "echo":
            print(" ".join(args))
        elif command == "type":
            type_func(args)
        else:
            print(f"{command}: command not found")


def type_func(args):
    system_path = os.environ['PATH']
    
    if args[0] in BUILT_INS:
        print(f"{args[0]} is a shell builtin")
        return

    for dir in system_path.split(os.pathsep):
        exec_path = os.path.join(dir, args[0])
        if (os.access(exec_path, os.X_OK)):
            print(f"{args[0]} is {exec_path}")
            return

    print(f"{args[0]}: not found")


if __name__ == "__main__":
    main()
