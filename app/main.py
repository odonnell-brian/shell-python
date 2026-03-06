import sys


def main():
    repl()


def repl():
    while True:
        sys.stdout.write("$ ")
        
        # Wait for user input
        command = input()
        
        if command == "exit":
            return
        elif command.startswith("echo "):
            print(command[5:])
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
