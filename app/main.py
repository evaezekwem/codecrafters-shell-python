import sys
import random


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    builtin_cmds = ["echo", "exit","type"]

    try:
        # Wait for user input
        while True:
            command: str = input()

            # if command.strip().split()[0] in builtins_cmds:
            
            if command.strip() == "exit 0":
                exit(0)
            elif command.strip().startswith("echo "):
                print(command.strip()[5:])
                sys.stdout.write("$ ")
            elif command.strip().startswith("type "): #and command.strip().split()[1].strip in builtins_cmds:
                print(f"{command.strip()[5:].partition(" ")[0]} is a shell builtin") if command.strip()[5:].partition(" ")[0] in builtin_cmds else print(f"{command.strip()[5:].partition(" ")[0]}: not found")
                sys.stdout.write("$ ")
            else:
                print(f"{command}: command not found")
                sys.stdout.write("$ ")
            
    except KeyboardInterrupt as e:
        print("\nExiting...")
        sys.exit(0)
    finally:
        sys.stdout.flush()
        exit(0)

if __name__ == "__main__":
    main()
