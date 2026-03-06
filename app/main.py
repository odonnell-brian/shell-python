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
    if args[0] in BUILT_INS:
        print(f"{args[0]} is a shell builtin")
    else:
        print(f"{args[0]}: not found")


if __name__ == "__main__":
    main()
