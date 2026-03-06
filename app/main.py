import os
import subprocess
import sys

BUILT_INS = {
    "exit": lambda args: exit_func(),
    "type": lambda args: type_func(args),
    "echo": lambda args: echo_func(args),
    "pwd": lambda args: pwd_func(),
    "cd": lambda args: cd_func(args),
}

def main():
    repl()


def repl():
    while True:
        sys.stdout.write("$ ")
        
        # Wait for user input
        user_input = input()
        parts = user_input.split(" ")
        command, *args = parts
        
        if command in BUILT_INS:
            BUILT_INS[command](args)
        else:
            could_exec = try_exec(command, args)
            
            if not could_exec:
                print(f"{command}: command not found")


def exit_func():
    sys.exit(0)
    

def echo_func(args):
    print(" ".join(args))
    
    
def pwd_func():
    print(os.getcwd())
    

def type_func(args):    
    if args[0] in BUILT_INS:
        print(f"{args[0]} is a shell builtin")
        return

    exec_path = get_location_from_os_path(args[0])
    if exec_path is not None:
        print(f"{args[0]} is {exec_path}")
    else:
        print(f"{args[0]}: not found")
        

def cd_func(args):
    try:
        os.chdir(args[0])
    except:
        print(f"cd: {args[0]}: No such file or directory")


def try_exec(command, args):
    full_path = get_location_from_os_path(command)
    
    if full_path is not None:
        subprocess.run([command, *args])
        return True
    
    return False


def get_location_from_os_path(exec):
    system_path = os.environ['PATH']
    
    for dir in system_path.split(os.pathsep):
        exec_path = os.path.join(dir, exec)
        if (os.access(exec_path, os.X_OK)):
            return exec_path
        
    return None

if __name__ == "__main__":
    main()
